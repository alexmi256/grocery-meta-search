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

_CONFIG_PATH = Path(__file__).resolve().parent.parent / "sources" / "multibuy_config.json"
_CACHE_DIR = Path("work/multibuy-cache")

_BADGE_RE = re.compile(
    r"(\d{1,2})\s*(?:POUR|FOR)\s*(\d{1,3}(?:[., ]\d{2,3})?)\s*\$?"
)
_UNIT_RE = re.compile(r"(\d{1,2})[.,](\d{2})\s*/\s*(?:CH|EA)\b")


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
    """First 'X,XX/CH' that is not the 'REG.' regular-price line."""
    for m in _UNIT_RE.finditer(text):
        if "REG" in text[max(0, m.start() - 8) : m.start()]:
            continue
        return float(f"{m.group(1)}.{m.group(2)}")
    return None


def extract_multibuy(
    text: str, payload_price: float | None
) -> tuple[float, int, float] | None:
    """(unit_price, count, total) from a cell render's OCR text.

    The payload price is the bundle total by construction, so it
    arbitrates the garbled badge digits: with a printed unit, the
    bundle inequalities identify the offer; without one, the badge
    total must parse to exactly the payload.
    """
    if payload_price is None:
        return None
    upper = text.upper()
    m = _BADGE_RE.search(upper)
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


def _payload_price(raw: str | None) -> float | None:
    if not raw:
        return None
    try:
        value = json.loads(raw).get("price")
        return float(value)
    except (TypeError, ValueError, AttributeError):
        return None


def _cell_text(image_path: Path) -> str:
    image = Image.open(image_path).convert("RGB")
    return " ".join(ln.text for ln in detect_lines(image))


def multibuy_store(
    conn: sqlite3.Connection,
    store_slug: str,
    *,
    cache_dir: Path = _CACHE_DIR,
) -> dict[str, int]:
    """Recover multibuy offers for one store's stored Flipp items.

    Only items whose stored price still equals the payload price and
    that carry no multibuy condition are candidates (idempotent; the
    campaign's hand corrections are never overwritten).
    """
    cache_dir.mkdir(parents=True, exist_ok=True)
    rows = conn.execute(
        "SELECT id, price_value, conditions, image_url, raw FROM flyer_items"
        " WHERE store_slug = ?",
        (store_slug,),
    ).fetchall()
    recovered = 0
    for row in rows:
        item_id, price_value, conditions_s, image_url, raw = row
        payload = _payload_price(raw)
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
        raw_d: dict[str, Any] = json.loads(raw) if raw else {}
        raw_d["multibuy_recovery"] = {
            "via": "image",
            "unit": unit,
            "count": count,
            "total": total,
        }
        conn.execute(
            "UPDATE flyer_items SET price_value = ?, conditions = ?, raw = ?"
            " WHERE id = ?",
            (unit, json.dumps(conditions, ensure_ascii=False),
             json.dumps(raw_d, ensure_ascii=False), item_id),
        )
        # Commit per item: a full store pass OCRs hundreds of cell
        # renders and must stay resumable if interrupted.
        conn.commit()
        recovered += 1
    return {"recovered": recovered}


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True)
    parser.add_argument("--slugs", required=True, help="comma-separated")
    args = parser.parse_args(argv)
    conn = sqlite3.connect(args.db)
    configs = load_multibuy_configs()
    for slug in [s.strip() for s in args.slugs.split(",") if s.strip()]:
        if slug not in configs:
            print(f"{slug}: not enabled in multibuy_config.json, skipped")
            continue
        stats = multibuy_store(conn, slug)
        print(f"{slug}: {stats['recovered']} multibuy offers recovered")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
