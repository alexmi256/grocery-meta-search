"""Generate the classification review document.

For every store, samples N random items (fixed seed, reproducible)
and renders each with its picture, full stored details and its
assigned category, for human review of classifier quality.

Pictures: Flipp/Woo items already carry product images (embedded by
URL). OCR items carry a flyer *page* image plus a pixel bbox — those
are cropped from the page (downloaded once, cached under work/) and
saved next to the document.

Usage:
    python -m grocery_meta_search.classify.review --db data/grocery.db \
        --out docs/research/classification-review.md \
        --assets docs/research/classification-review-assets
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import sqlite3
import urllib.request
from pathlib import Path

from PIL import Image

from grocery_meta_search.classify.taxonomy import UNCLASSIFIED, category_label_fr

PAGE_HOSTS = {
    "circulaires.club",
    "flyerify.com",
    "d280crdu6dot2n.cloudfront.net",
    "circulaires.com",
    "mayrand.ca",
    "alimentsmerci.com",
    "static.wixstatic.com",
    "milanofruiterie.ca",
    "na.leafletscdn.com",
}
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) grocery-review"}


def _fetch_page(url: str, cache_dir: Path) -> Path | None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha256(url.encode()).hexdigest()[:20]
    path = cache_dir / f"{key}.img"
    if path.exists():
        return path
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=30) as resp:
            path.write_bytes(resp.read())
        return path
    except Exception:
        return None


def _crop(page_path: Path, bbox: dict[str, float], out_path: Path) -> bool:
    try:
        with Image.open(page_path) as im:
            w, h = im.size
            bw = bbox["right"] - bbox["left"]
            bh = bbox["bottom"] - bbox["top"]
            x0 = max(0, int(bbox["left"] - bw * 0.12))
            x1 = min(w, int(bbox["right"] + bw * 0.12))
            y0 = max(0, int(bbox["top"] - bh * 0.35))
            y1 = min(h, int(bbox["bottom"] + bh * 0.15))
            if x1 - x0 < 10 or y1 - y0 < 10:
                return False
            crop = im.convert("RGB").crop((x0, y0, x1, y1))
            crop.save(out_path, "JPEG", quality=82)
        return True
    except Exception:
        return False


def _sane_bbox(raw: str | None) -> dict[str, float] | None:
    if not raw:
        return None
    try:
        data = json.loads(raw)
        b = {k: float(data[k]) for k in ("left", "top", "right", "bottom")}
        if data.get("page") is not None:
            b["page"] = float(data["page"])
    except Exception:
        return None
    if 0 <= b["left"] < b["right"] <= 6000 and 0 <= b["top"] < b["bottom"] <= 9000:
        return b
    return None


def _fmt_price(row: sqlite3.Row) -> str:
    parts = []
    if row["price_value"] is not None:
        parts.append(f"{row['price_value']:.2f} $")
    if row["price_text"]:
        parts.append(f"as printed: “{row['price_text']}”")
    if row["price_unit"]:
        parts.append(f"unit: {row['price_unit']}")
    return " · ".join(parts) if parts else "—"


def _fmt_conditions(raw: str | None) -> str:
    if not raw:
        return ""
    try:
        cond = json.loads(raw)
    except Exception:
        return ""
    bits = []
    if cond.get("regular_price") is not None:
        bits.append(f"regular price {cond['regular_price']}")
    if cond.get("alt_prices"):
        bits.append("other printed prices: " + ", ".join(cond["alt_prices"]))
    if cond.get("description"):
        desc = " ".join(str(cond["description"]).split())
        bits.append(f"“{desc[:180]}”")
    return " · ".join(bits)


def generate(
    db_path: str, out_path: Path, assets_dir: Path, seed: int, per_store: int
) -> dict[str, int]:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    assets_dir.mkdir(parents=True, exist_ok=True)
    page_cache = Path("work/review-pages")
    rng = random.Random(seed)

    stores = conn.execute(
        """
        SELECT s.slug, s.name, count(*) AS n,
               sum(CASE WHEN i.category != 'Unclassified' THEN 1 ELSE 0 END) AS k
        FROM flyer_items i JOIN stores s ON s.slug = i.store_slug
        GROUP BY s.slug ORDER BY s.name
        """
    ).fetchall()
    total = conn.execute("SELECT count(*) FROM flyer_items").fetchone()[0]
    classified = conn.execute(
        "SELECT count(*) FROM flyer_items WHERE category != 'Unclassified'"
    ).fetchone()[0]

    lines: list[str] = []
    lines.append("# Classification review — PC Express taxonomy")
    lines.append("")
    lines.append(
        f"Generated from `data/grocery.db` ({total} items, "
        f"{classified} classified = {classified / total:.1%}). "
        f"{per_store} random items per store (seed {seed}), each with "
        "its picture, stored details and assigned category."
    )
    lines.append("")
    lines.append(
        "Taxonomy: PC Express departments/subcategories as documented in "
        "[product-categories.md](product-categories.md), minus the "
        "attribute-based *Natural and Organic* department, plus Baby / "
        "Pet / Household / Health & Beauty buckets for non-food flyer "
        "items. Method `rule` = a named keyword rule fired; "
        "`frozen-remap` = fresh hit remapped by a frozen marker; "
        "`store-prior` = no rule matched, fell back to the store's trade."
    )
    lines.append("")
    lines.append("| Store | Items | Classified |")
    lines.append("|---|---:|---:|")
    for s in stores:
        lines.append(f"| {s['name']} | {s['n']} | {s['k'] / s['n']:.0%} |")
    lines.append("")

    stats = {"crops": 0, "direct": 0, "missing": 0}
    for s in stores:
        ids = [
            r[0]
            for r in conn.execute(
                "SELECT id FROM flyer_items WHERE store_slug=? ORDER BY id",
                (s["slug"],),
            )
        ]
        sample = rng.sample(ids, min(per_store, len(ids)))
        lines.append(f"## {s['name']} (`{s['slug']}`)")
        lines.append("")
        for n, item_id in enumerate(sample, 1):
            row = conn.execute(
                """
                SELECT i.*, x.department, x.subcategory, x.method, x.rule_id
                FROM flyer_items i
                LEFT JOIN item_classifications x ON x.item_id = i.id
                WHERE i.id = ?
                """,
                (item_id,),
            ).fetchone()
            title = row["name_fr"] or row["name_en"] or "(no name)"
            lines.append(f"### {n}. {title}")
            lines.append("")
            # Picture.
            host = ""
            if row["image_url"]:
                from urllib.parse import urlparse

                host = urlparse(row["image_url"]).netloc
            bbox = _sane_bbox(row["bbox"])
            pictured = False
            if row["image_url"] and host in PAGE_HOSTS and bbox is not None:
                page = _fetch_page(row["image_url"], page_cache)
                out_img = assets_dir / f"item-{item_id}.jpg"
                if page is not None and _crop(page, bbox, out_img):
                    rel = f"classification-review-assets/item-{item_id}.jpg"
                    lines.append(f"![item {item_id}]({rel})")
                    stats["crops"] += 1
                    pictured = True
            if not pictured and row["image_url"]:
                lines.append(f"![item {item_id}]({row['image_url']})")
                stats["direct"] += 1
                pictured = True
            if not pictured:
                lines.append("*(no picture available)*")
                stats["missing"] += 1
            lines.append("")
            dept = row["department"] or UNCLASSIFIED
            sub = row["subcategory"] or UNCLASSIFIED
            if dept == UNCLASSIFIED:
                cat_line = "**Unclassified**"
            else:
                cat_line = f"{dept} > {sub} (FR: {category_label_fr(dept, sub)})"
            lines.append(f"- **Category:** {cat_line}")
            method = row["method"] or "none"
            rule = f" (`{row['rule_id']}`)" if row["rule_id"] else ""
            lines.append(f"- **How classified:** {method}{rule}")
            if (row["name_en"] or "") != (row["name_fr"] or "") and row["name_en"]:
                lines.append(f"- **Name (EN):** {row['name_en']}")
            lines.append(f"- **Price:** {_fmt_price(row)}")
            validity = f"{row['valid_from'] or '?'} → {row['valid_to'] or '?'}"
            page_no = ""
            if bbox is not None and bbox.get("page"):
                page_no = f" · flyer page {int(bbox['page'])}"
            lines.append(f"- **Flyer validity:** {validity}{page_no}")
            extra = []
            if row["brand"]:
                extra.append(f"brand: {row['brand']}")
            if row["sku"]:
                extra.append(f"SKU: {row['sku']}")
            if row["loyalty_gated"]:
                extra.append("loyalty-gated price")
            if row["confidence"] is not None:
                extra.append(f"OCR/extraction confidence: {row['confidence']:.2f}")
            cond = _fmt_conditions(row["conditions"])
            if cond:
                extra.append(cond)
            if extra:
                lines.append(f"- **Details:** {' · '.join(extra)}")
            lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    conn.close()
    return stats


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--assets", required=True)
    parser.add_argument("--seed", type=int, default=20261015)
    parser.add_argument("--per-store", type=int, default=10)
    args = parser.parse_args()
    stats = generate(args.db, Path(args.out), Path(args.assets), args.seed, args.per_store)
    print(f"wrote {args.out}: {stats}")


if __name__ == "__main__":
    main()
