"""Apply the classifier to every flyer item in the database.

Writes flyer_items.category ("Department > Subcategory", EN labels —
'Unclassified' when nothing matched) and an item_classifications
provenance table (method + rule id per item) so every assignment is
auditable. Idempotent: re-running replaces both.

Usage:
    python -m grocery_meta_search.classify.run --db data/grocery.db
"""

from __future__ import annotations

import argparse
import sqlite3
from collections import Counter
from datetime import UTC, datetime

from grocery_meta_search.classify.rules import classify_item
from grocery_meta_search.classify.taxonomy import UNCLASSIFIED, category_label


def apply_classification(db_path: str) -> Counter[str]:
    conn = sqlite3.connect(db_path)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS item_classifications (
            item_id INTEGER PRIMARY KEY,
            department TEXT NOT NULL,
            subcategory TEXT NOT NULL,
            method TEXT NOT NULL,
            rule_id TEXT NOT NULL,
            classified_at TEXT NOT NULL
        )
        """
    )
    rows = conn.execute(
        "SELECT id, name_fr, name_en, brand, store_slug FROM flyer_items"
    ).fetchall()
    now = datetime.now(UTC).isoformat(timespec="seconds")
    stats: Counter[str] = Counter()
    out_rows = []
    label_rows = []
    for item_id, name_fr, name_en, brand, store_slug in rows:
        dept, sub, method, rule_id = classify_item(name_fr, name_en, brand, store_slug)
        label = UNCLASSIFIED if dept == UNCLASSIFIED else category_label(dept, sub)
        out_rows.append((item_id, dept, sub, method, rule_id, now))
        label_rows.append((label, item_id))
        stats[dept] += 1
    conn.execute("DELETE FROM item_classifications")
    conn.executemany("INSERT INTO item_classifications VALUES (?,?,?,?,?,?)", out_rows)
    conn.executemany("UPDATE flyer_items SET category=? WHERE id=?", label_rows)
    conn.commit()
    conn.close()
    return stats


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", required=True)
    args = parser.parse_args()
    stats = apply_classification(args.db)
    total = sum(stats.values())
    classified = total - stats.get(UNCLASSIFIED, 0)
    print(f"total {total}  classified {classified} ({classified / total:.1%})")
    for dept, n in stats.most_common():
        print(f"  {n:>6}  {dept}")


if __name__ == "__main__":
    main()
