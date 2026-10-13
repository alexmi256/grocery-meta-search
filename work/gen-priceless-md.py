"""Generate the price-less sample items review doc.

Usage: .venv/bin/python work/gen-priceless-md.py
Reads data/grocery.db, writes docs/research/phase3-sample-priceless-items.md
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "data" / "grocery.db"
OUT = ROOT / "docs" / "research" / "phase3-sample-priceless-items.md"


def _md_cell(value: str | None) -> str:
    return (value or "").replace("|", "\\|").replace("\n", " ").strip()


def main() -> None:
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    total = conn.execute(
        "SELECT COUNT(*) FROM flyer_items WHERE price_value IS NULL"
    ).fetchone()[0]

    lines = [
        "# Price-less items — group 1 sample",
        "",
        f"Sample fetch of 2026-10-12/13 (Maxi, IGA, Provigo via Flipp FlyerKit).",
        f"{total} of 1010 items have no parseable price. These are typically",
        "recipe/brand ads, stamp-collection promos, multi-product offers priced",
        "on a parent item, or alcohol with 'see in store' pricing.",
        "",
    ]
    stores = [
        r[0]
        for r in conn.execute(
            "SELECT DISTINCT store_slug FROM flyer_items WHERE price_value IS NULL ORDER BY 1"
        )
    ]
    for store in stores:
        rows = conn.execute(
            """
            SELECT name_fr, name_en, brand, price_text, sku, valid_from, valid_to,
                   image_url, conditions
            FROM flyer_items
            WHERE store_slug = ? AND price_value IS NULL
            ORDER BY name_fr
            """,
            (store,),
        ).fetchall()
        lines += [f"## {store} — {len(rows)} items", ""]
        for r in rows:
            d = dict(r)
            name = d["name_fr"] or d["name_en"] or "(unnamed)"
            lines.append(f"### {_md_cell(name)}")
            lines.append("")
            if d["image_url"]:
                lines.append(f"![{_md_cell(name)}]({d['image_url']})")
                lines.append("")
            details = []
            if d["name_en"] and d["name_en"] != d["name_fr"]:
                details.append(f"EN: {_md_cell(d['name_en'])}")
            if d["brand"]:
                details.append(f"brand: {_md_cell(d['brand'])}")
            if d["price_text"]:
                details.append(f"price_text: {_md_cell(d['price_text'])}")
            if d["sku"]:
                details.append(f"sku: `{_md_cell(d['sku'])}`")
            if d["valid_from"] or d["valid_to"]:
                details.append(f"valid: {d['valid_from']} → {d['valid_to']}")
            cond = json.loads(d["conditions"] or "{}")
            for key in ("sale_story", "disclaimer_text"):
                if cond.get(key):
                    snippet = _md_cell(cond[key])[:200]
                    details.append(f"{key}: {snippet}")
            for detail in details:
                lines.append(f"- {detail}")
            lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT} ({total} items)")


if __name__ == "__main__":
    main()
