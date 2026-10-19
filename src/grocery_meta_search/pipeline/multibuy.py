"""Image-based multibuy recovery for Flipp-sourced items.

The Flipp/wishabi payload collapses a multibuy offer into a single
price: for a printed "2 POUR 5$" badge the payload price is the
bundle total (5.0), and neither the count nor the per-unit price
("2,99/CH") appears anywhere in the payload (verified on Kim Phat
raw payloads, 2026-10-17). The printed offer survives only in the
item's own cell render (the wishabi image IS the flyer cell: photo,
price badge, name block). This stage OCRs that image and, under
strict gates, rewrites the item: price_value becomes the printed
per-unit price and conditions gains {"multibuy": {count, total}}.

Gates (all must hold; the payload price is the collapsed total):
- a badge "N POUR <digits>" (or "N FOR") reads in the cell text;
- either a per-unit "X,XX/CH" print (not the "REG." reference) with
  unit < payload < count * unit (bundle arithmetic), giving
  price = unit, or
- no unit print, but the badge total parses unambiguously and
  equals the payload, giving price = total / count.
Anything else is left untouched. Per-store enablement lives in
sources/multibuy_config.json (Kim Phat first: 15 of 137 items on
flyer 125 carried badges, 13 with printed units, all validated
against the campaign's hand corrections, zero false positives).

The write-back keeps the price-bearing columns in step: flyer_items.
price_value (the printed unit price), the derived unit pair
(unit_quantity = count, unit_measurement = 'multiple' — the same split
ingest applies to a multibuy condition), and the matching
price_observations row, which is written once at ingest and would
otherwise keep the collapsed bundle total (2026-10-19 review). The
printed price_text is deliberately left as printed on both rows, so it
still reads the collapse ("1.99") beside the corrected value (1.29).

A store pass reconciles every row that already carries a multibuy
condition — items recovered before this rule existed, and the
campaign's hand-corrected offers — recomputing the unit pair and the
price observation from the recorded count, without re-OCR. The CLI's
--reconcile mode runs that repair on its own (no image recovery), so
stores outside multibuy_config.json — which can carry hand-corrected
multibuy rows but must not run image recovery — can be healed too.
"""

from __future__ import annotations

import json
import re
import sqlite3
import urllib.request
from pathlib import Path
from typing import Any

from PIL import Image

from ..ocr.engine import detect_lines
from ..prices import multibuy_count, split_unit

_CONFIG_PATH = Path(__file__).resolve().parent.parent / "sources" / "multibuy_config.json"
_CACHE_DIR = Path("work/multibuy-cache")

_BADGE_RE = re.compile(r"(\d{1,2})\s*(?:POUR|FOR)\s*(\d{1,3}(?:[., ]\d{2,3})?)\s*\$?")
# Slash form ('2/4$'), the Metro/Loblaws house style; the trailing
# $ is required so size fractions ('1/2') never match.
_BADGE_SLASH_RE = re.compile(r"(\d{1,2})\s*/\s*(\d{1,3}(?:[.,]\d{2})?)\s*\$")
_UNIT_RE = re.compile(r"(\d{1,2})[.,](\d{2})\s*(?:/\s*(?:CH|EA)\b|L'UNITÉ|L'UNITE|\bEACH\b)")
# Spaced-decimal unit ('2 99 l'unité', '3 67 l'un.'), Metro style.
_UNIT_SPACED_RE = re.compile(r"(\d{1,2})\s(\d{2})\s*(?:L'UNITÉ|L'UNITE|L'UN\.?)")


def load_multibuy_configs() -> dict[str, dict[str, Any]]:
    try:
        data = json.loads(_CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    stores: dict[str, dict[str, Any]] = data.get("stores", {})
    return stores


def _parse_total(text: str) -> float | None:
    """Badge total as printed: '5' -> 5.0, '2.99' -> 2.99,
    '199' -> 1.99 (cents-style), '6 99' -> 6.99 (spaced cents)."""
    s = text.replace(" ", "")
    if re.fullmatch(r"\d{1,3}[.,]\d{2}", s):
        return float(s.replace(",", "."))
    if re.fullmatch(r"\d{3,4}", s):
        return int(s) / 100
    if re.fullmatch(r"\d{1,2}", s):
        return float(s)
    return None


def _printed_unit(text: str) -> float | None:
    """First per-unit print that is not the 'REG.' regular-price line."""
    for regex in (_UNIT_RE, _UNIT_SPACED_RE):
        for m in regex.finditer(text):
            if "REG" in text[max(0, m.start() - 8) : m.start()]:
                continue
            return float(f"{m.group(1)}.{m.group(2)}")
    return None


def extract_multibuy(text: str, payload_price: float | None) -> tuple[float, int, float] | None:
    """(unit_price, count, total) from a cell render's OCR text.

    The payload price is the bundle total by construction, so it
    arbitrates the garbled badge digits: with a printed unit, the
    bundle inequalities identify the offer; without one, the badge
    total must parse to exactly the payload.
    """
    if payload_price is None:
        return None
    upper = text.upper()
    m = _BADGE_RE.search(upper) or _BADGE_SLASH_RE.search(upper)
    if m is None:
        return None
    count = int(m.group(1))
    if count < 2:
        return None
    unit = _printed_unit(upper)
    if unit is not None and unit < payload_price < count * unit:
        return (unit, count, payload_price)
    if unit is None:
        total = _parse_total(m.group(2))
        if total is not None and abs(total - payload_price) < 0.011:
            return (round(total / count, 2), count, total)
    return None


def _payload_price(raw: dict[str, Any]) -> float | None:
    """The Flipp payload price carried inside the item's parsed raw JSON."""
    value = raw.get("price")
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _sync_observation(
    conn: sqlite3.Connection,
    item_key: str,
    store_slug: str,
    flyer_id: int,
    price_value: float,
) -> bool:
    """Mirror a unit price into the item's price observation.

    price_observations is written once at ingest (pipeline/fetch.py); a
    write-back that changes flyer_items.price_value must carry the
    history with it, or the two disagree for the offer's whole life
    (2026-10-19 review). price_text is left as printed — flyer_items
    keeps the printed text too.

    The table carries no item id, so a row is addressed by
    (item_key, store_slug, flyer_id). Two same-flyer items can share an
    item_key (it hashes store + name + price_unit only), and then the
    observation cannot be attributed to the recovered item: the update
    is skipped rather than risk rewriting a sibling's history. Returns
    True only when it writes.
    """
    rows = conn.execute(
        "SELECT id, price_value FROM price_observations WHERE item_key = ? AND store_slug = ? AND flyer_id = ?",
        (item_key, store_slug, flyer_id),
    ).fetchall()
    if len(rows) != 1:
        return False
    obs_id, current = rows[0]
    if current is not None and abs(float(current) - price_value) <= 0.001:
        return False
    conn.execute("UPDATE price_observations SET price_value = ? WHERE id = ?", (price_value, obs_id))
    return True


def _reconcile_recovered(
    conn: sqlite3.Connection,
    *,
    item_id: int,
    item_key: str,
    store_slug: str,
    flyer_id: int,
    price_value: float | None,
    unit_quantity: float,
    unit_measurement: str,
    count: int | None,
) -> bool:
    """Repair an item whose price already reads as a unit price but whose
    derived columns predate the write-back that keeps them in step.

    Covers rows recovered under the old code and the campaign's
    hand-corrected multibuy rows (both carry conditions.multibuy but may
    keep the pre-correction unit pair). The item's own price is never
    touched, so a hand correction stands. A count above 100 is OCR
    garble, not an offer: the unit pair is left alone. Idempotent:
    returns True only when it writes.
    """
    changed = False
    if isinstance(count, int) and 1 < count <= 100:
        quantity, measurement = split_unit(None, count)
        if (unit_quantity, unit_measurement) != (quantity, measurement):
            conn.execute(
                "UPDATE flyer_items SET unit_quantity = ?, unit_measurement = ? WHERE id = ?",
                (quantity, measurement, item_id),
            )
            changed = True
    if price_value is not None and _sync_observation(conn, item_key, store_slug, flyer_id, price_value):
        changed = True
    return changed


def _cell_text(image_path: Path) -> str:
    # OCR text is cached next to the image: a store pass examines
    # hundreds of items, most without offers, and repeat runs (fetch
    # cycles, resumed backfills) must not re-OCR them.
    text_path = image_path.with_suffix(".txt")
    if text_path.exists():
        return text_path.read_text(encoding="utf-8")
    image = Image.open(image_path).convert("RGB")
    text = " ".join(ln.text for ln in detect_lines(image))
    text_path.write_text(text, encoding="utf-8")
    return text


def multibuy_store(
    conn: sqlite3.Connection,
    store_slug: str,
    *,
    cache_dir: Path = _CACHE_DIR,
    recover: bool = True,
) -> dict[str, int]:
    """Recover multibuy offers for one store's stored Flipp items.

    Only items whose stored price still equals the payload price and
    that carry no multibuy condition are candidates (idempotent; the
    campaign's hand corrections are never overwritten). Rows that
    already carry a multibuy condition — recovered here before, or
    hand-corrected — are reconciled in place instead (unit pair + price
    observation), which heals rows written before the write-back synced
    them.

    With recover=False (the CLI's --reconcile mode) the candidate pass
    is skipped entirely: only those already-multibuy rows are repaired,
    so nothing is downloaded or OCR'd and stores not enabled for image
    recovery can still be healed.
    """
    if recover:
        cache_dir.mkdir(parents=True, exist_ok=True)
    rows = conn.execute(
        "SELECT id, item_key, flyer_id, price_value, unit_quantity, unit_measurement,"
        " conditions, image_url, raw FROM flyer_items WHERE store_slug = ?",
        (store_slug,),
    ).fetchall()
    recovered = 0
    reconciled = 0
    for row in rows:
        (
            item_id,
            item_key,
            flyer_id,
            price_value,
            unit_quantity,
            unit_measurement,
            conditions_s,
            image_url,
            raw,
        ) = row
        try:
            raw_d: dict[str, Any] = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            raw_d = {}
        if not isinstance(raw_d, dict):
            raw_d = {}
        prov = raw_d.get("multibuy_recovery")
        prov = prov if isinstance(prov, dict) else {}
        count = multibuy_count(conditions_s)
        if (not isinstance(count, int) or count < 2) and isinstance(prov.get("count"), int):
            count = int(prov["count"])
        # Rows already holding a multibuy condition are reconciled rather
        # than re-examined: their stored price is a unit price, so the
        # derived unit pair and the price observation must agree with it.
        # That is every row this stage recovered, plus the campaign's
        # hand-corrected offers (which carry the condition but no
        # provenance, and predate the pair/history sync).
        if (isinstance(count, int) and count > 1) or prov:
            if _reconcile_recovered(
                conn,
                item_id=int(item_id),
                item_key=str(item_key),
                store_slug=store_slug,
                flyer_id=int(flyer_id),
                price_value=float(price_value) if price_value is not None else None,
                unit_quantity=float(unit_quantity),
                unit_measurement=str(unit_measurement),
                count=count,
            ):
                conn.commit()
                reconciled += 1
            continue
        if not recover:
            continue
        payload = _payload_price(raw_d)
        if payload is None or price_value is None:
            continue
        if abs(float(price_value) - payload) > 0.001:
            continue
        conditions: dict[str, Any] = {}
        if conditions_s:
            try:
                conditions = json.loads(conditions_s)
            except json.JSONDecodeError:
                conditions = {}
        if "multibuy" in conditions:
            continue
        if not image_url or "wishabi.net" not in image_url:
            continue
        path = cache_dir / f"{item_id}.jpg"
        if not path.exists():
            try:
                urllib.request.urlretrieve(image_url, path)
            except Exception:
                continue
        try:
            found = extract_multibuy(_cell_text(path), payload)
        except Exception:
            continue
        if found is None:
            continue
        unit, count, total = found
        conditions["multibuy"] = {"count": count, "total": total}
        raw_d["multibuy_recovery"] = {
            "via": "image",
            "unit": unit,
            "count": count,
            "total": total,
        }
        quantity, measurement = split_unit(None, count)
        conn.execute(
            "UPDATE flyer_items SET price_value = ?, unit_quantity = ?, unit_measurement = ?,"
            " conditions = ?, raw = ? WHERE id = ?",
            (
                unit,
                quantity,
                measurement,
                json.dumps(conditions, ensure_ascii=False),
                json.dumps(raw_d, ensure_ascii=False),
                item_id,
            ),
        )
        _sync_observation(conn, str(item_key), store_slug, int(flyer_id), unit)
        # Commit per item: a full store pass OCRs hundreds of cell
        # renders and must stay resumable if interrupted.
        conn.commit()
        recovered += 1
    return {"recovered": recovered, "reconciled": reconciled}


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True)
    parser.add_argument("--slugs", required=True, help="comma-separated")
    parser.add_argument(
        "--reconcile",
        action="store_true",
        help="only repair rows that already carry a multibuy condition (unit pair + price history); "
        "no image recovery, so stores outside multibuy_config.json are accepted",
    )
    args = parser.parse_args(argv)
    conn = sqlite3.connect(args.db)
    configs = load_multibuy_configs()
    for slug in [s.strip() for s in args.slugs.split(",") if s.strip()]:
        if not args.reconcile and slug not in configs:
            print(f"{slug}: not enabled in multibuy_config.json, skipped")
            continue
        stats = multibuy_store(conn, slug, recover=not args.reconcile)
        if args.reconcile:
            print(f"{slug}: {stats['reconciled']} multibuy rows reconciled")
        else:
            extra = f", {stats['reconciled']} reconciled" if stats["reconciled"] else ""
            print(f"{slug}: {stats['recovered']} multibuy offers recovered{extra}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
