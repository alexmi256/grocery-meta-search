"""Single-store product report with locally downloaded images.

Renders every item of one store (all editions in the DB) with its
full stored details and a local picture: the bbox crop from the
flyer page for OCR items, the product image for API items. Full
page images are saved alongside so crops can be judged in context.

Usage:
    python -m grocery_meta_search.classify.store_report --db data/grocery.db \
        --slug akhavan --out-dir docs/research/akhavan-report
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import urllib.request
from pathlib import Path

from PIL import Image

from grocery_meta_search.classify.review import _crop, _sane_bbox
from grocery_meta_search.classify.taxonomy import category_label_fr

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) grocery-report"}


def _download(url: str, dest: Path) -> bool:
    if dest.exists():
        return True
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=30) as resp:
            dest.write_bytes(resp.read())
        return True
    except Exception:
        return False


def _is_pdf(path: Path) -> bool:
    try:
        with path.open("rb") as fh:
            return fh.read(4) == b"%PDF"
    except Exception:
        return False


def _render_pdf_page(pdf_path: Path, page_no: int, dest: Path) -> bool:
    """Render one page (1-based) of a PDF flyer to JPG at 200 DPI."""
    if dest.exists():
        return True
    try:
        from typing import Any

        import pymupdf

        doc: Any = pymupdf.open(pdf_path)  # type: ignore[no-untyped-call]
        with doc:
            page = doc.load_page(max(0, min(page_no - 1, doc.page_count - 1)))
            pix = page.get_pixmap(dpi=200)
            pix.save(dest)
        return True
    except Exception:
        return False


def _raw_size(row: sqlite3.Row) -> str | None:
    """The item's package size: the flyer_items.package_size
    column, falling back to the legacy raw-payload value for items
    stored before the column existed."""
    if row["package_size"]:
        return str(row["package_size"])
    raw = row["raw"]
    if not raw:
        return None
    try:
        data = json.loads(raw)
    except Exception:
        return None
    if isinstance(data, dict) and data.get("size"):
        return str(data["size"])
    return None


def _to_jpg(src: Path, dest: Path) -> bool:
    if dest.exists():
        return True
    try:
        with Image.open(src) as im:
            im.convert("RGB").save(dest, "JPEG", quality=88)
        return True
    except Exception:
        return False


def generate(db_path: str, slug: str, out_dir: Path, latest_only: bool = False,
             only_ids: set[int] | None = None) -> dict[str, int]:
    from urllib.parse import urlparse

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    store = conn.execute("SELECT * FROM stores WHERE slug=?", (slug,)).fetchone()
    if store is None:
        raise SystemExit(f"unknown store {slug}")
    images_dir = out_dir / "images"
    pages_dir = out_dir / "pages"
    raw_dir = out_dir / "_downloads"
    for d in (images_dir, pages_dir, raw_dir):
        d.mkdir(parents=True, exist_ok=True)

    flyers = conn.execute(
        "SELECT * FROM flyers WHERE store_slug=? ORDER BY valid_from", (slug,)
    ).fetchall()
    if latest_only and flyers:
        flyers = [max(flyers, key=lambda f: (f["valid_to"], f["id"]))]
    intro = (
        "Every item stored for this store, with all stored details and "
        "a locally downloaded picture (bbox crop from the flyer page; "
        "full pages under `pages/`)."
    )
    if only_ids is not None:
        intro = (
            f"A sampled subset of {len(only_ids)} items stored for this "
            "store (random sample, see the review index), with all "
            "stored details and a locally downloaded picture (bbox crop "
            "from the flyer page; full pages under `pages/`)."
        )
    lines: list[str] = [
        f"# {store['name']} — full product report",
        "",
        f"Store slug: `{slug}`. Generated from `data/grocery.db`. " + intro,
        "",
    ]
    stats = {"items": 0, "crops": 0, "direct": 0, "missing": 0, "pages": 0}

    def emit(row: sqlite3.Row, flyer: sqlite3.Row) -> None:
        stats["items"] += 1
        lines.append(f"### Item {row['id']}")
        lines.append("")
        bbox = _sane_bbox(row["bbox"])
        pictured = False
        page_ref = ""
        # A sane (0-1000 normalized) bbox means image_url is a flyer
        # PAGE and the picture is a crop of it — regardless of host
        # (OCR pages, PDF preview pages). Items without one carry a
        # direct product image instead.
        if row["image_url"] and bbox is not None:
            import hashlib

            url_key = hashlib.sha256(row["image_url"].encode()).hexdigest()[:10]
            raw = raw_dir / f"page-src-{url_key}"
            page_no = int(bbox["page"]) if bbox.get("page") else 1
            page_jpg = pages_dir / f"flyer{flyer['id']}-page{page_no}-{url_key}.jpg"
            # PDF flyers (pdf_page sources) keep the PDF as image_url:
            # render the item's page; image pages convert directly.
            ok = _download(row["image_url"], raw) and (
                _render_pdf_page(raw, page_no, page_jpg)
                if _is_pdf(raw)
                else _to_jpg(raw, page_jpg)
            )
            if ok:
                page_ref = f"pages/{page_jpg.name} (flyer page {page_no})"
                if bbox is not None:
                    crop = images_dir / f"item-{row['id']}.jpg"
                    if _crop(page_jpg, bbox, crop):
                        lines.append(f"![item {row['id']}](images/item-{row['id']}.jpg)")
                        stats["crops"] += 1
                        pictured = True
        if not pictured and row["image_url"]:
            ext = Path(urlparse(row["image_url"]).path).suffix or ".jpg"
            raw = raw_dir / f"product-{row['id']}{ext}"
            dest = images_dir / f"item-{row['id']}{ext}"
            if _download(row["image_url"], raw):
                try:
                    dest.write_bytes(raw.read_bytes())
                    lines.append(f"![item {row['id']}](images/{dest.name})")
                    stats["direct"] += 1
                    pictured = True
                except Exception:
                    pass
        if not pictured:
            lines.append("*(no picture could be downloaded)*")
            stats["missing"] += 1
        lines.append("")
        dept = row["department"] or "Unclassified"
        sub = row["subcategory"] or "Unclassified"
        if row["name_en"] and row["name_en"] != row["name_fr"]:
            lines.append(f"- **Name (English):** {row['name_en']}")
        if row["name_fr"]:
            lines.append(f"- **Name (French):** {row['name_fr']}")
        if row["brand"]:
            lines.append(f"- **Brand:** {row['brand']}")
        if dept == "Unclassified":
            lines.append("- **Category (English):** Unclassified")
            lines.append("- **Category (French):** Non classé")
        else:
            lines.append(f"- **Category (English):** {dept} > {sub}")
            lines.append(f"- **Category (French):** {category_label_fr(dept, sub)}")
        method = row["method"] or "none"
        rule = f" (`{row['rule_id']}`)" if row["rule_id"] else ""
        lines.append(f"- **How classified:** {method}{rule}")
        size = _raw_size(row)
        if size:
            lines.append(f"- **Size:** {size}")
        price = f"{row['price_value']:.2f}" if row["price_value"] is not None else "—"
        lines.append(f"- **Price:** {price}")
        lines.append(f"- **Printed Price:** “{row['price_text']}”")
        lines.append(f"- **Unit:** {row['price_unit'] or '—'}")
        lines.append(f"- **Item validity:** {row['valid_from'] or '?'} → {row['valid_to'] or '?'}")
        if bbox is not None:
            lines.append(
                f"- **bbox:** left {bbox['left']:.0f}, top {bbox['top']:.0f}, "
                f"right {bbox['right']:.0f}, bottom {bbox['bottom']:.0f}"
                + (f", page {int(bbox['page'])}" if bbox.get("page") else "")
            )
        if page_ref:
            lines.append(f"- **Full page:** [{page_ref}]({page_ref.split(' ')[0]})")
        if row["image_url"]:
            lines.append(f"- **Image source URL:** {row['image_url']}")
        details = []
        if row["sku"]:
            details.append(f"SKU: {row['sku']}")
        if row["loyalty_gated"]:
            details.append("loyalty-gated price")
        if row["confidence"] is not None:
            details.append(f"confidence: {row['confidence']:.2f}")
        details.append(f"item_key: `{row['item_key']}`")
        lines.append(f"- **Details:** {' · '.join(details)}")
        if row["conditions"] and row["conditions"] != "{}":
            lines.append(f"- **Conditions:** `{row['conditions']}`")
        if row["raw"]:
            raw_txt = " ".join(str(row["raw"]).split())[:500]
            lines.append(f"- **Raw:** `{raw_txt}`")
        lines.append("")

    pending_unc: list[tuple[sqlite3.Row, sqlite3.Row]] = []
    for flyer in flyers:
        items = conn.execute(
            """
            SELECT i.*, x.department, x.subcategory, x.method, x.rule_id
            FROM flyer_items i
            LEFT JOIN item_classifications x ON x.item_id = i.id
            WHERE i.flyer_id = ? ORDER BY i.id
            """,
            (flyer["id"],),
        ).fetchall()
        if only_ids is not None:
            items = [r for r in items if r["id"] in only_ids]
            if not items:
                continue
        main_items = [r for r in items if (r["department"] or "Unclassified") != "Unclassified"]
        unc_items = [r for r in items if (r["department"] or "Unclassified") == "Unclassified"]
        pending_unc.extend((flyer, r) for r in unc_items)
        lines.append(
            f"## Flyer {flyer['id']} — valid {flyer['valid_from']} → "
            f"{flyer['valid_to']} ({len(main_items)} classified items, "
            f"{len(unc_items)} unclassified)"
        )
        lines.append("")
        lines.append(f"Source ref: `{flyer['source_ref']}` · fetched {flyer['created_at']}")
        lines.append("")
        for row in main_items:
            emit(row, flyer)
    if pending_unc:
        lines.append("## Unclassified items — kept for review")
        lines.append("")
        lines.append(
            "The classifier could not assign these items a category. "
            "They are kept in the database (not discarded) so a human "
            "can review them and improve the rules."
        )
        lines.append("")
        for flyer, row in pending_unc:
            lines.append(
                f"— from flyer {flyer['id']} (valid {flyer['valid_from']} → {flyer['valid_to']})"
            )
            lines.append("")
            emit(row, flyer)
    stats["pages"] = len(list(pages_dir.glob("*.jpg")))
    (out_dir / f"{slug}-report.md").write_text("\n".join(lines), encoding="utf-8")
    conn.close()
    return stats


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--latest-only", action="store_true")
    args = parser.parse_args()
    stats = generate(args.db, args.slug, Path(args.out_dir), args.latest_only)
    print(f"{args.slug}: {stats}")


if __name__ == "__main__":
    main()
