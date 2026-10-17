"""Page-harvest stage: fill package_size / price_unit from flyer images.

Some printed fields exist ONLY in the flyer page image — the Flipp
payload carries no size text at all, and the OCR segmenter drops
size-only lines (2026-10-16 visual review, G1/G2). This stage OCRs each
affected item's flyer cell and extracts the missing fields:

- Flipp-shaped items (wishabi image_url): the item image IS the cell
  region render (or the product cutout, whose label often prints the
  size) — OCR it directly.
- OCR items: crop the flyer page at the item's normalized bbox (the
  review._crop geometry) and OCR the crop.

Per-store enablement lives in sources/harvest_config.json (store-level
config; evidence in docs/research/page-harvest.md). Only missing fields
are filled, and fills are conservative: a size is stored only when the
cell yields exactly one distinct value, or several values that the
fields policy resolves to a weight/volume while the rest are counts
("60-70 UNITÉS 907 g"); a unit only when exactly one distinct price
unit appears. Harvested values are recorded in the item's raw JSON
under "harvest" for audit.

Runs at ingest (fetch_store calls harvest_store for enabled stores)
and standalone for backfills:

    python -m grocery_meta_search.pipeline.harvest \
        --db data/grocery.db --slugs marches-tau,super-c [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path
from typing import Any

from PIL import Image

from ..classify.review import PAGE_HOSTS, _fetch_page, _sane_bbox
from ..ocr.engine import detect_lines, upscale_for_ocr
from ..ocr.segment import _unit_in_text
from ..prices import multibuy_count, split_unit
from .fields import extract_package_size, find_package_sizes

_CONFIG_PATH = Path(__file__).parent.parent / "sources" / "harvest_config.json"
_CACHE_DIR = Path("work/harvest-cache")
_WV_HINT = re.compile(r"\b(?:g|kg|mg|l|ml|lb|oz|gr)\b", re.IGNORECASE)

# Grocery flyers print no package above ~25 L (18.9 L water jugs are
# the top end); the fields-level litre cap is looser because hardware
# flyers print real bin capacities. Harvest candidates above this are
# OCR stitches (round-2 review: celery stored as "66L").
_HARVEST_LITRE_CAP = 25.0
_LITRE_PAIR_RE = re.compile(r"(\d+(?:[.,]\d+)?)\s*l\b", re.IGNORECASE)


def _harvest_size_ok(value: str) -> bool:
    for qty in _LITRE_PAIR_RE.findall(value):
        if float(qty.replace(",", ".")) > _HARVEST_LITRE_CAP:
            return False
    return True


def load_harvest_configs() -> dict[str, dict[str, Any]]:
    data = json.loads(_CONFIG_PATH.read_text(encoding="utf-8"))
    stores: dict[str, dict[str, Any]] = data.get("stores", {})
    return {slug: dict(cfg) for slug, cfg in stores.items()}


def _norm_size(value: str) -> str:
    return re.sub(r"\s+", "", value).lower()


_RANGE_RE = re.compile(r"^(\d+(?:[.,]\d+)?)\s*-\s*(\d+(?:[.,]\d+)?)")


def _descending_range(value: str) -> bool:
    """Ranges print low-high ("500 - 650 G"); a descending 'range' is an
    OCR garble stitched from two different format ranges (metro cheese:
    '250-220g' out of '340-460 g' + '220-325 g')."""
    m = _RANGE_RE.match(value)
    if not m:
        return False
    return float(m.group(1).replace(",", ".")) > float(m.group(2).replace(",", "."))


_PER_UNIT_RE = re.compile(
    r"\d+(?:[.,]\d+)?\s*/\s*(\d+(?:[.,]\d+)?)\s*(g|kg|mg|ml|cl|l|oz|lb|gr)\b",
    re.IGNORECASE,
)
# The French rate form "le 100 g" (under the headline price) is a
# denominator too, glued by OCR as often as not ("le100g").
_LE_UNIT_RE = re.compile(
    r"le\s*(\d+(?:[.,]\d+)?)\s*(g|kg|mg|ml|cl|l|oz|lb|gr)\b",
    re.IGNORECASE,
)


def _per_unit_denominators(line: str) -> set[str]:
    """Normalized size strings used as per-unit price denominators on
    this line ("0,79-1,06/100 ml" -> {"100ml"}). Flyers print unit-price
    references in small print beside the real offer; a denominator is
    never the package size, and for a pack item it is not the price
    unit either (round-2 review, giant-tiger: a 12-pack's unit stored
    as 100g, a jam's size blocked by the reference's ambiguity)."""
    denoms = {
        _norm_size(f"{m.group(1)}{m.group(2)}")
        for m in _PER_UNIT_RE.finditer(line)
    }
    denoms |= {
        _norm_size(f"{m.group(1)}{m.group(2)}")
        for m in _LE_UNIT_RE.finditer(line)
    }
    return denoms


# A price of its own on the line (an equivalent-rate line like
# "15,83/lb" carries one; the headline rate line "le100g" does not).
_PRICE_TOKEN_RE = re.compile(r"\d+[.,]\d{2}\b|\d+\s*(?:¢|cents\b)|\$\s*\d+")


def harvest_from_lines(
    lines: list[str], want_size: bool, want_unit: bool
) -> dict[str, str]:
    """Extraction policy over one cell's OCR lines (pure, testable)."""
    out: dict[str, str] = {}
    joined = " | ".join(lines)
    found: dict[str, str] = {}
    for line in lines:
        denoms = _per_unit_denominators(line)
        for value in find_package_sizes(line):
            if _PER_UNIT_RE.search(value):
                # The candidate itself stitches a unit price into a
                # fake size ("0,50/100 g" read as one package size).
                continue
            lead = re.match(r"\d+(?:[.,]\d+)?", value)
            if lead and float(lead.group(0).replace(",", ".")) == 0:
                # A zero quantity is an OCR misread of the real size
                # printed beside it (the same "600 g" read again as
                # "000g" on the bag) — never a package size, and as a
                # rival candidate it poisons the unambiguous pick.
                continue
            if _norm_size(value) in denoms:
                continue
            if not _descending_range(value) and _harvest_size_ok(value):
                found.setdefault(_norm_size(value), value)
    if want_size:
        if len(found) == 1:
            out["size"] = next(iter(found.values()))
        elif len(found) > 1:
            # A single range is the offer's stated size ("836-888 g,
            # 4 un."): count rivals are the pack count, and a lone
            # weight rival inside the range is one variety's stamp
            # (frozen pizza "325-410 g" beside a 395 g box print) —
            # both are consistent with the range, not contradictions.
            ranges = [v for v in found.values() if _RANGE_RE.match(v)]
            if len(ranges) == 1:
                rng = ranges[0]
                m = _RANGE_RE.match(rng)
                assert m is not None
                lo = float(m.group(1).replace(",", "."))
                hi = float(m.group(2).replace(",", "."))
                consistent = True
                for v in found.values():
                    if v == rng or not _WV_HINT.search(v):
                        continue
                    nums = re.findall(r"\d+(?:[.,]\d+)?", v)
                    if not nums or not lo <= float(
                        nums[0].replace(",", ".")
                    ) <= hi:
                        consistent = False
                if consistent:
                    out["size"] = rng
            if "size" not in out:
                # Several distinct sizes: trust the fields policy only
                # when it picks a weight/volume and every rival is
                # count-only (shrimp "60-70 UNITÉS" beside the pack's
                # "907 g").
                pick = extract_package_size(joined)
                denoms_all = set().union(
                    *(_per_unit_denominators(line) for line in lines)
                )
                if (
                    pick
                    and _WV_HINT.search(pick)
                    and not _PER_UNIT_RE.search(pick)
                    and _norm_size(pick) not in denoms_all
                ):
                    rivals = [
                        v for k, v in found.items() if k != _norm_size(pick)
                    ]
                    if rivals and all(
                        not _WV_HINT.search(v) for v in rivals
                    ):
                        out["size"] = pick
    if want_unit:
        # A per-unit denominator is a price *reference* when the cell
        # also carries a package size (the pack's price is the offer);
        # with no size anywhere it is the offer's own basis (weighed
        # goods priced "2,99/100 g") and stays a valid unit.
        pick_any = extract_package_size(joined)
        denoms_all = (
            set().union(*(_per_unit_denominators(line) for line in lines))
            if lines
            else set()
        )
        # A "size" pick that is itself a rate denominator ("le 100 g")
        # is not package evidence — the cell is a weighed-good offer.
        size_evidence = bool(found) or (
            pick_any is not None
            and not _PER_UNIT_RE.search(pick_any)
            and _norm_size(pick_any) not in denoms_all
        )
        units: set[str] = set()
        unmarked: set[str] = set()
        for line in lines:
            u = _unit_in_text(line)
            if u is None:
                continue
            if size_evidence and _norm_size(u) in _per_unit_denominators(line):
                continue
            units.add(u)
            if not _PRICE_TOKEN_RE.search(line):
                unmarked.add(u)
        # Dual-rate cells (Adonis brie: headline "3,49 le 100 g" plus
        # the small-print equivalent "15,83/lb"): the headline rate
        # rides a line with no price of its own, while equivalent
        # rates carry theirs. Prefer the unmarked unit when it is
        # unambiguous; otherwise fall back to a single distinct unit.
        if len(unmarked) == 1:
            out["unit"] = next(iter(unmarked))
        elif len(units) == 1:
            out["unit"] = next(iter(units))
    return out


def _plan(row: sqlite3.Row) -> tuple[str, str, dict[str, float] | None] | None:
    """Decide how to obtain the item's cell image.

    Returns ("image", url, None) for Flipp-shaped items,
    ("crop", page_url, bbox) for OCR items, or None.
    """
    url = row["image_url"] or ""
    if "wishabi.net" in url:
        return ("image", url, None)
    bbox = _sane_bbox(row["bbox"])
    if bbox is None:
        return None
    host = re.sub(r"^https?://", "", url).split("/")[0]
    if host in PAGE_HOSTS or ".pdf" in url:
        return ("crop", url.split("#")[0], bbox)
    return None


# Crop padding as fractions of the bbox size (x, up, down). Tighter at
# the top than classify/review.py's judging crop: the 2026-10-16 sample
# validation showed +35% up reaches into the cell ABOVE and imports its
# size line (Tau: a neighbour's "156 - 198 G" filled two items). Sizes
# print inside the cell, usually under the price, so allow more below.
_DEFAULT_PAD = (0.12, 0.08, 0.20)


def _crop_image(
    page: Image.Image,
    bbox: dict[str, float],
    pad: tuple[float, float, float] = _DEFAULT_PAD,
) -> Image.Image:
    w, h = page.size
    left = bbox["left"] / 1000 * w
    right = bbox["right"] / 1000 * w
    top = bbox["top"] / 1000 * h
    bottom = bbox["bottom"] / 1000 * h
    bw, bh = right - left, bottom - top
    x0 = max(0, int(left - bw * pad[0]))
    x1 = min(w, int(right + bw * pad[0]))
    y0 = max(0, int(top - bh * pad[1]))
    y1 = min(h, int(bottom + bh * pad[2]))
    return page.crop((x0, y0, x1, y1))


def _page_image(url: str, page_no: int, cache_dir: Path) -> Image.Image | None:
    path = _fetch_page(url, cache_dir)
    if path is None:
        return None
    try:
        if ".pdf" in url:
            import pymupdf

            doc: Any = pymupdf.open(path)  # type: ignore[no-untyped-call]
            page = doc.load_page(max(0, min(page_no - 1, doc.page_count - 1)))
            pix = page.get_pixmap(dpi=200)
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            doc.close()
            return img
        with Image.open(path) as im:
            return im.convert("RGB")
    except Exception:
        return None


def _ocr_lines(img: Image.Image) -> list[str]:
    try:
        return [ln.text for ln in detect_lines(upscale_for_ocr(img))]
    except Exception:
        return []


def _refresh_row(
    conn: sqlite3.Connection,
    row: sqlite3.Row,
    got: dict[str, str],
    kind: str,
    stats: dict[str, int],
    dry_run: bool,
) -> None:
    """Reconcile one already-harvested item with a fresh extraction.

    Only fields carrying harvest provenance are retracted or updated;
    a field the extraction newly finds on an empty column still fills.
    """
    raw = json.loads(row["raw"]) if row["raw"] else {}
    prev = raw.get("harvest") or {}
    prev_fields = {f for f in ("size", "unit") if f in prev}
    if not prev_fields and not got:
        return
    sets: list[str] = []
    params: list[object] = []
    for field, col in (("size", "package_size"), ("unit", "price_unit")):
        cur = row["package_size"] if field == "size" else row["price_unit"]
        unit_touched = False
        if field in prev_fields:
            if field in got:
                if cur != got[field]:
                    stats[f"changed_{field}"] += 1
                    sets.append(f"{col} = ?")
                    params.append(got[field])
                    unit_touched = field == "unit"
            else:
                stats[f"cleared_{field}"] += 1
                sets.append(f"{col} = NULL")
                unit_touched = field == "unit"
        elif field in got and cur is None:
            stats[f"filled_{field}"] += 1
            sets.append(f"{col} = ?")
            params.append(got[field])
            unit_touched = field == "unit"
        if unit_touched:
            # Keep the split unit pair in sync with price_unit.
            quantity, measurement = split_unit(
                got.get("unit"), multibuy_count(row["conditions"])
            )
            sets.append("unit_quantity = ?")
            params.append(quantity)
            sets.append("unit_measurement = ?")
            params.append(measurement)
    if dry_run:
        return
    new_raw = dict(raw)
    if got:
        new_raw["harvest"] = {**got, "via": kind}
    else:
        new_raw.pop("harvest", None)
    sets.insert(0, "raw = ?")
    params.insert(0, json.dumps(new_raw, ensure_ascii=False))
    params.append(row["id"])
    conn.execute(f"UPDATE flyer_items SET {', '.join(sets)} WHERE id = ?", params)


def harvest_store(
    conn: sqlite3.Connection,
    slug: str,
    *,
    today: date | None = None,
    dry_run: bool = False,
    limit: int | None = None,
    cache_dir: Path = _CACHE_DIR,
    refresh_harvested: bool = False,
) -> dict[str, int]:
    """Fill missing size/unit for one store's current-flyer items.

    With refresh_harvested, items already carrying harvest provenance
    are re-extracted instead: a field the new extraction no longer
    produces is cleared, one it changes is updated (round-2: the
    per-unit-denominator fix must be able to retract a bad fill).
    Fields without harvest provenance are never touched.
    """
    cfg = load_harvest_configs().get(slug)
    stats = {
        "items": 0, "filled_size": 0, "filled_unit": 0,
        "ambiguous": 0, "no_plan": 0, "no_image": 0,
        "cleared_size": 0, "cleared_unit": 0,
        "changed_size": 0, "changed_unit": 0,
    }
    if cfg is None:
        return stats
    fields = cfg.get("fields", ["size", "unit"])
    want_size, want_unit = "size" in fields, "unit" in fields
    today = today or date.today()
    if refresh_harvested:
        conds = ["fi.raw LIKE '%\"harvest\"%'"]
    else:
        conds = []
        if want_size:
            conds.append("fi.package_size IS NULL")
        if want_unit:
            conds.append("fi.price_unit IS NULL")
    if not conds:
        return stats
    rows = conn.execute(
        f"""
        SELECT fi.id, fi.image_url, fi.bbox, fi.raw,
               fi.package_size, fi.price_unit, fi.conditions
        FROM flyer_items fi JOIN flyers f ON f.id = fi.flyer_id
        WHERE fi.store_slug = ? AND f.valid_to >= ?
          AND ({" OR ".join(conds)})
        ORDER BY fi.id
        """,
        (slug, today.isoformat()),
    ).fetchall()
    if limit:
        rows = rows[:limit]
    pad_cfg = cfg.get("pad")
    pad = tuple(pad_cfg) if pad_cfg else _DEFAULT_PAD
    page_cache: dict[str, Image.Image | None] = {}
    cache_lock = threading.Lock()

    def cached_image(url: str) -> Image.Image | None:
        with cache_lock:
            if url in page_cache:
                return page_cache[url]
        path = _fetch_page(url, cache_dir)
        img: Image.Image | None = None
        if path is not None:
            try:
                with Image.open(path) as im:
                    img = im.convert("RGB")
            except Exception:
                img = None
        with cache_lock:
            # A same-URL race may have populated the cache meanwhile.
            if url in page_cache:
                return page_cache[url]
            page_cache[url] = img
        return img

    def cached_page(url: str, page_no: int) -> Image.Image | None:
        # Single-flight under the lock: page images are shared by many
        # items, and concurrent _fetch_page writes to the same cache
        # path corrupt each other (2026-10-16: la-moisson + h-marche
        # lost every item to this race). One retry guards a transient
        # network failure from poisoning the whole page.
        key = f"{url}#{page_no}"
        with cache_lock:
            if key in page_cache:
                return page_cache[key]
            img = _page_image(url, page_no, cache_dir)
            if img is None:
                img = _page_image(url, page_no, cache_dir)
            page_cache[key] = img
            return img

    def work(row: sqlite3.Row) -> tuple[str, dict[str, str], str]:
        plan = _plan(row)
        if plan is None:
            return ("no_plan", {}, "")
        kind, url, bbox = plan
        if kind == "image":
            img = cached_image(url)
        else:
            assert bbox is not None
            page_img = cached_page(url, int(bbox.get("page", 1)))
            img = _crop_image(page_img, bbox, pad) if page_img is not None else None
        if img is None:
            return ("no_image", {}, kind)
        got = harvest_from_lines(
            _ocr_lines(img),
            want_size and (refresh_harvested or row["package_size"] is None),
            want_unit and (refresh_harvested or row["price_unit"] is None),
        )
        return ("ok" if got else "ambiguous", got, kind)

    # Downloads + OCR run in parallel (onnxruntime releases the GIL);
    # DB writes stay on this thread.
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(work, rows))
    for row, (status, got, kind) in zip(rows, results, strict=True):
        stats["items"] += 1
        if status == "no_plan":
            stats["no_plan"] += 1
            continue
        if status == "no_image":
            stats["no_image"] += 1
            continue
        if refresh_harvested:
            _refresh_row(conn, row, got, kind, stats, dry_run)
            continue
        if not got:
            stats["ambiguous"] += 1
            continue
        if "size" in got:
            stats["filled_size"] += 1
        if "unit" in got:
            stats["filled_unit"] += 1
        if dry_run:
            continue
        raw = json.loads(row["raw"]) if row["raw"] else {}
        # Merge provenance: a fill run must not erase the record of
        # fields an earlier harvest set (a later --refresh-harvested
        # run retracts by that record; overwriting it strands values
        # like a rate denominator stored as a size — adonis 7476).
        prior = raw.get("harvest") or {}
        merged = {k: v for k, v in prior.items() if k != "via"}
        merged.update(got)
        raw["harvest"] = {**merged, "via": kind}
        sets: list[str] = ["raw = ?"]
        params: list[object] = [json.dumps(raw, ensure_ascii=False)]
        if "size" in got:
            sets.append("package_size = ?")
            params.append(got["size"])
        if "unit" in got:
            sets.append("price_unit = ?")
            params.append(got["unit"])
            quantity, measurement = split_unit(
                got["unit"], multibuy_count(row["conditions"])
            )
            sets.append("unit_quantity = ?")
            params.append(quantity)
            sets.append("unit_measurement = ?")
            params.append(measurement)
        params.append(row["id"])
        conn.execute(
            f"UPDATE flyer_items SET {', '.join(sets)} WHERE id = ?", params
        )
    if not dry_run:
        conn.commit()
    return stats


def main() -> None:
    parser = argparse.ArgumentParser(description="Page-harvest missing size/unit fields.")
    parser.add_argument("--db", required=True, type=Path)
    parser.add_argument("--slugs", required=True, help="comma-separated store slugs")
    parser.add_argument("--today", type=date.fromisoformat, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument(
        "--refresh-harvested",
        action="store_true",
        help="re-extract items already carrying harvest provenance, "
        "retracting or updating the fields it set",
    )
    args = parser.parse_args()
    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    for slug in [s.strip() for s in args.slugs.split(",") if s.strip()]:
        stats = harvest_store(
            conn,
            slug,
            today=args.today,
            dry_run=args.dry_run,
            limit=args.limit,
            refresh_harvested=args.refresh_harvested,
        )
        extra = ""
        if args.refresh_harvested:
            extra = (
                f", -{stats['cleared_size']} size, -{stats['cleared_unit']} unit, "
                f"~{stats['changed_size']} size, ~{stats['changed_unit']} unit"
            )
        print(
            f"{slug}: {stats['items']} candidates, "
            f"+{stats['filled_size']} size, +{stats['filled_unit']} unit{extra}, "
            f"{stats['ambiguous']} ambiguous/none, {stats['no_plan']} no-plan, "
            f"{stats['no_image']} no-image"
            + ("  [dry run]" if args.dry_run else "")
        )
    conn.close()


if __name__ == "__main__":
    main()
