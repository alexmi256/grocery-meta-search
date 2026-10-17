"""Sampled multi-store review pack.

For every store with items in the DB, sample N random classified and
N random unclassified items (seeded, reproducible) and render each
store with the standard store_report format into its own subfolder.
An index README.md summarizes the pack. Zip the output folder for
offline review.

Usage:
    python -m grocery_meta_search.classify.review_sample \
        --db data/grocery.db --out-dir docs/research/review-2026-10-16 \
        --per-class 10 --seed 20261016
"""

from __future__ import annotations

import argparse
import random
import sqlite3
from pathlib import Path

from grocery_meta_search.classify.store_report import generate


def sample_store_ids(conn: sqlite3.Connection, slug: str,
                     per_class: int, seed: int, today: str) -> tuple[set[int], int, int]:
    """Sample item ids from the store's CURRENT flyers only
    (flyer valid_to >= today). Expired editions never enter a
    review pack."""
    rows = conn.execute(
        """
        SELECT i.id, x.department
        FROM flyer_items i
        JOIN flyers f ON f.id = i.flyer_id
        LEFT JOIN item_classifications x ON x.item_id = i.id
        WHERE i.store_slug = ? AND f.valid_to >= ?
        """,
        (slug, today),
    ).fetchall()
    classified = sorted(r[0] for r in rows if (r[1] or "Unclassified") != "Unclassified")
    unclassified = sorted(r[0] for r in rows if (r[1] or "Unclassified") == "Unclassified")
    rng = random.Random(f"{seed}:{slug}")
    picked = set(rng.sample(classified, min(per_class, len(classified))))
    picked |= set(rng.sample(unclassified, min(per_class, len(unclassified))))
    return picked, len(classified), len(unclassified)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--per-class", type=int, default=10)
    parser.add_argument("--seed", type=int, default=20261016)
    parser.add_argument("--today", default=None,
                        help="YYYY-MM-DD; only flyers valid on/after this "
                             "date are sampled (default: today)")
    parser.add_argument("--slugs", default=None,
                        help="comma-separated store slugs; render only "
                             "these stores and skip the pack index (for "
                             "per-store review passes)")
    args = parser.parse_args()
    from datetime import date

    today = args.today or date.today().isoformat()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(args.db)
    stores = conn.execute(
        """
        SELECT s.slug, s.name FROM stores s
        WHERE EXISTS (SELECT 1 FROM flyer_items i WHERE i.store_slug = s.slug)
        ORDER BY s.slug
        """
    ).fetchall()
    if args.slugs:
        wanted = {s.strip() for s in args.slugs.split(",") if s.strip()}
        stores = [row for row in stores if row[0] in wanted]

    index: list[str] = [
        "# Classification review pack",
        "",
        f"Per store: up to {args.per_class} random classified + "
        f"{args.per_class} random unclassified items (seed {args.seed}), "
        "rendered in the standard store report format with local images. "
        f"Only current flyers (valid through {today} or later) are sampled; "
        "expired editions are excluded.",
        "",
        "| Store | In DB (class. / unclass.) | Sampled (class. / unclass.) | Report |",
        "|---|---|---|---|",
    ]
    totals = {"items": 0, "crops": 0, "direct": 0, "missing": 0}
    sampled_c = sampled_u = 0
    skipped: list[str] = []
    for slug, name in stores:
        picked, n_class, n_unc = sample_store_ids(conn, slug, args.per_class,
                                                  args.seed, today)
        if not picked:
            skipped.append(f"{name} (`{slug}`)")
            index.append(
                f"| {name} (`{slug}`) | — | — | *no current flyer — skipped* |"
            )
            print(f"{slug}: no current flyer, skipped")
            continue
        stats = generate(args.db, slug, out_dir / slug, only_ids=picked)
        for k in totals:
            totals[k] += stats[k]
        sc = min(args.per_class, n_class)
        su = min(args.per_class, n_unc)
        sampled_c += sc
        sampled_u += su
        index.append(
            f"| {name} (`{slug}`) | {n_class} / {n_unc} | {sc} / {su} | "
            f"[{slug}-report.md]({slug}/{slug}-report.md) |"
        )
        print(f"{slug}: sampled {sc}+{su} of {n_class}+{n_unc} -> {stats}")
    index += [
        "",
        f"**Totals:** {len(stores) - len(skipped)} stores sampled, "
        f"{sampled_c} classified + {sampled_u} unclassified items; pictures: "
        f"{totals['crops']} crops, {totals['direct']} direct images, "
        f"{totals['missing']} missing.",
    ]
    if skipped:
        index += [
            "",
            "Stores with items in the DB but **no current flyer** "
            f"(skipped): {', '.join(skipped)}.",
        ]
    if args.slugs:
        conn.close()
        print("per-store run (--slugs): index skipped")
        return
    (out_dir / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    conn.close()
    print(f"index written: {out_dir / 'README.md'}")


if __name__ == "__main__":
    main()
