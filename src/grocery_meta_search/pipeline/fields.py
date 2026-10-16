"""Package-size extraction from item names.

Many sources print the package size inside the product name
("FRAISES 340G", "JUS D'ORANGE 1.89L", "ŒUFS 12 UNITÉS") instead of
a structured field. extract_package_size finds that printed size so
it can live in flyer_items.package_size. Names are never modified —
the size text is copied, not cut (item keys and classification
inputs stay stable).

Per-store expectations (which stores can carry a size at all, and
how brand/size are distinguished per source) are documented in
docs/research/item-field-extraction.md.
"""

from __future__ import annotations

import re

# A quantity: "1.89", "340", "1/2", optionally with a multiplier
# prefix "6 x" / "24x". A unit: weight, volume, length or count.
_QTY = r"\d+(?:[.,]\d+)?(?:\s*/\s*\d+)?"
_UNIT = (
    r"(?:kg|mg|ml|cl|oz|lb|lbs|g|l|grammes?|grams?|kilogrammes?|"
    r"litres?|unites?|units?|pieces?|pcs|sachets?|cm|mm|douzaine)"
)
_MULT = r"(?:\d+\s*[x×]\s*)?"
_SIZE_RE = re.compile(
    rf"(?P<full>{_MULT}{_QTY}\s*{_UNIT}\b(?:\s*/\s*{_QTY}\s*{_UNIT}\b)?)",
    re.IGNORECASE,
)
# A bare count trailing a food noun ("ŒUFS 12", "BAGELS 6") is a
# package count, but bare numbers are too ambiguous to trust alone;
# only the unit-bearing forms above are extracted.


def reprocess(db_path: str, dry_run: bool = False) -> dict[str, dict[str, int]]:
    """Fill flyer_items.package_size for existing items: first
    from a structured raw payload (pdf_text items), then by
    extracting the printed size from the item's names. Also fills
    flyer_items.price_unit from the raw Flipp post_price_text
    ("/lb 4,39$/kg") for items whose unit was never parsed.
    Idempotent; returns per-store counters."""
    import json

    from ..db import connect, init_schema
    from ..prices import parse_price_text

    conn = connect(db_path)
    init_schema(conn)
    stats: dict[str, dict[str, int]] = {}
    rows = conn.execute(
        "SELECT id, store_slug, name_fr, name_en, raw, package_size, price_unit"
        " FROM flyer_items"
    ).fetchall()
    for row in rows:
        st = stats.setdefault(
            row["store_slug"],
            {"total": 0, "set": 0, "from_raw": 0, "from_name": 0, "unit_set": 0},
        )
        st["total"] += 1
        if row["price_unit"]:
            st["unit_set"] += 1
        elif row["raw"]:
            try:
                data = json.loads(row["raw"])
            except Exception:
                data = None
            if isinstance(data, dict) and data.get("post_price_text"):
                _, unit = parse_price_text(str(data["post_price_text"]))
                if unit:
                    st["unit_set"] += 1
                    if not dry_run:
                        conn.execute(
                            "UPDATE flyer_items SET price_unit=? WHERE id=?",
                            (unit, row["id"]),
                        )
        if row["package_size"]:
            st["set"] += 1
            continue
        size: str | None = None
        origin = ""
        if row["raw"]:
            try:
                data = json.loads(row["raw"])
            except Exception:
                data = None
            if isinstance(data, dict) and data.get("size"):
                size, origin = str(data["size"]), "from_raw"
        if size is None:
            size = extract_package_size(row["name_fr"], row["name_en"])
            origin = "from_name" if size else ""
        if size:
            st[origin] += 1
            st["set"] += 1
            if not dry_run:
                conn.execute(
                    "UPDATE flyer_items SET package_size=? WHERE id=?",
                    (size, row["id"]),
                )
    if not dry_run:
        conn.commit()
    conn.close()
    return stats


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--db", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    stats = reprocess(args.db, args.dry_run)
    total = {"total": 0, "set": 0, "from_raw": 0, "from_name": 0}
    for slug in sorted(stats):
        st = stats[slug]
        for k in total:
            total[k] += st[k]
        print(
            f"{slug:28} {st['set']:5}/{st['total']:<5} "
            f"(raw {st['from_raw']}, name {st['from_name']})"
        )
    print(
        f"{'TOTAL':28} {total['set']:5}/{total['total']:<5} "
        f"(raw {total['from_raw']}, name {total['from_name']})"
        + ("  [dry run]" if args.dry_run else "")
    )



def extract_package_size(*names: str | None) -> str | None:
    """Return the printed package size found in a name, or None.

    When several candidates appear, the LAST one wins — sizes print
    at the end of flyer names ("RIZ BASMATI 2 lb", not the "2" of
    "2% M.F." mid-name; a trailing unit match is the package).
    """
    for name in names:
        if not name:
            continue
        matches = list(_SIZE_RE.finditer(name))
        if matches:
            text = matches[-1].group("full")
            return re.sub(r"\s+", " ", text).strip(" ,.-")
    return None

if __name__ == "__main__":
    main()
