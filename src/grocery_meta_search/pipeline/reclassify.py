"""Reclassification pass: re-run the current classifier over the
stored pool.

Classifications are frozen at ingest, so rule improvements (the
2026-10-16 round-1 and round-2 review fixes) never reached items on
still-current flyers — Tau's Silk yogurt stayed a "non-dairy milk"
for a day after the rule was understood. This pass recomputes
classify_item for every stored item and updates flyer_items.category
+ item_classifications where the verdict changed, reporting flips.

It deliberately does NOT delete anything: an item that becomes
Unclassified is kept for review like any other (the exclusion-layer
cleanup is a separate, audited step), and a classified non-grocery
verdict stays stored, mirroring ingest behaviour on the live pool.

    python -m grocery_meta_search.pipeline.reclassify \
        --db data/grocery.db [--dry-run]
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

from ..classify.rules import classify_item
from ..classify.taxonomy import UNCLASSIFIED, category_label
from ..db import connect, init_schema


def reclassify(db_path: str, dry_run: bool = False) -> dict[str, object]:
    """Recompute classifications for all stored items.

    Returns {"total", "flips", "transitions": Counter[(old, new)]}.
    """
    conn = connect(db_path)
    init_schema(conn)
    now = datetime.now(UTC).isoformat(timespec="seconds")
    rows = conn.execute(
        """
        SELECT fi.id, fi.store_slug, fi.name_fr, fi.name_en, fi.brand,
               ic.department, ic.subcategory
        FROM flyer_items fi
        JOIN item_classifications ic ON ic.item_id = fi.id
        """
    ).fetchall()
    transitions: Counter[tuple[str, str]] = Counter()
    flips = 0
    for row in rows:
        dept, sub, method, rule_id = classify_item(row["name_fr"], row["name_en"], row["brand"], row["store_slug"])
        old = (row["department"], row["subcategory"])
        if (dept, sub) == old:
            continue
        flips += 1
        transitions[(f"{old[0]} > {old[1]}", f"{dept} > {sub}")] += 1
        if dry_run:
            continue
        label = UNCLASSIFIED if dept == UNCLASSIFIED else category_label(dept, sub)
        conn.execute("UPDATE flyer_items SET category = ? WHERE id = ?", (label, row["id"]))
        conn.execute(
            """
            UPDATE item_classifications
            SET department = ?, subcategory = ?, method = ?, rule_id = ?,
                classified_at = ?
            WHERE item_id = ?
            """,
            (dept, sub, method, rule_id, now, row["id"]),
        )
    if not dry_run:
        conn.commit()
    conn.close()
    return {"total": len(rows), "flips": flips, "transitions": transitions}


def main() -> None:
    parser = argparse.ArgumentParser(description="Re-run the classifier over stored items.")
    parser.add_argument("--db", required=True, type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    result = reclassify(str(args.db), args.dry_run)
    transitions = result["transitions"]
    assert isinstance(transitions, Counter)
    print(f"{result['total']} items, {result['flips']} flips" + ("  [dry run]" if args.dry_run else ""))
    for (old, new), n in transitions.most_common(40):
        print(f"  {n:5}  {old}  ->  {new}")


if __name__ == "__main__":
    main()
