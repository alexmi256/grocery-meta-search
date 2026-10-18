"""Sampled multi-store review pack.

For every selected store with items in the DB, sample N random
classified and M random unclassified items (seeded, reproducible)
and render each store with the standard store_report format into
its own subfolder. An index README.md summarizes the pack, and each
store report records the sampling seed and quantities so the exact
selection can be reproduced. Optionally zip the pack folder.

Usage:
    python -m grocery_meta_search.classify.review_sample \
        --db data/grocery.db --out-dir docs/research/review-2026-10-18 \
        --slugs all --per-classified 10 --per-unclassified 10 \
        --seed 20261018 --zip ~/workspace/your_files/review-2026-10-18.zip

--slugs takes a comma-separated list of store slugs, or "all"
(the default) for every store with items. --per-class sets both
quantities at once; --per-classified / --per-unclassified override
individually.
"""

from __future__ import annotations

import argparse
import random
import sqlite3
import zipfile
from pathlib import Path

from grocery_meta_search.classify.store_report import generate


def sample_store_ids(conn: sqlite3.Connection, slug: str,
                     per_classified: int, per_unclassified: int,
                     seed: int, today: str) -> tuple[set[int], int, int]:
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
    picked = set(rng.sample(classified, min(per_classified, len(classified))))
    picked |= set(rng.sample(unclassified, min(per_unclassified, len(unclassified))))
    return picked, len(classified), len(unclassified)


def zip_pack(out_dir: Path, zip_path: Path) -> int:
    """Zip the pack folder (the folder itself is the archive root,
    matching the earlier review zips). Returns the file count."""
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(out_dir.rglob("*")):
            if path.is_file():
                zf.write(path, Path(out_dir.name) / path.relative_to(out_dir))
                count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--per-class", type=int, default=None,
                        help="set BOTH the classified and unclassified "
                             "quantities (default 10 each)")
    parser.add_argument("--per-classified", type=int, default=None,
                        help="classified items per store (overrides --per-class)")
    parser.add_argument("--per-unclassified", type=int, default=None,
                        help="unclassified items per store (overrides --per-class)")
    parser.add_argument("--seed", type=int, default=20261016)
    parser.add_argument("--today", default=None,
                        help="YYYY-MM-DD; only flyers valid on/after this "
                             "date are sampled (default: today)")
    parser.add_argument("--slugs", default=None,
                        help="comma-separated store slugs, or 'all' "
                             "(default: all stores with items). In "
                             "per-store mode (a list, not 'all') the pack "
                             "index is skipped, for per-store review passes")
    parser.add_argument("--zip", default=None,
                        help="also write the pack as a zip archive at "
                             "this path (the pack folder is the root)")
    args = parser.parse_args()
    from datetime import date

    base = args.per_class if args.per_class is not None else 10
    per_classified = args.per_classified if args.per_classified is not None else base
    per_unclassified = (
        args.per_unclassified if args.per_unclassified is not None else base
    )
    slugs_all = args.slugs is None or args.slugs.strip().lower() == "all"
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
    if not slugs_all:
        wanted = {s.strip() for s in args.slugs.split(",") if s.strip()}
        stores = [row for row in stores if row[0] in wanted]

    index: list[str] = [
        "# Classification review pack",
        "",
        f"Per store: up to {per_classified} random classified + "
        f"{per_unclassified} random unclassified items (seed {args.seed}), "
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
        picked, n_class, n_unc = sample_store_ids(
            conn, slug, per_classified, per_unclassified, args.seed, today
        )
        if not picked:
            skipped.append(f"{name} (`{slug}`)")
            index.append(
                f"| {name} (`{slug}`) | — | — | *no current flyer — skipped* |"
            )
            print(f"{slug}: no current flyer, skipped")
            continue
        sc = min(per_classified, n_class)
        su = min(per_unclassified, n_unc)
        sample_info = (
            f"Sample: {sc} classified + {su} unclassified items sampled "
            f"(of {n_class} classified / {n_unc} unclassified in current "
            f"flyers), random selection seed {args.seed}. Reproduce with "
            f"`review_sample --seed {args.seed}` and the same quantities."
        )
        stats = generate(args.db, slug, out_dir / slug, only_ids=picked,
                         sample_info=sample_info)
        for k in totals:
            totals[k] += stats[k]
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
    if not slugs_all:
        conn.close()
        print("per-store run (--slugs list): index skipped")
    else:
        (out_dir / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
        conn.close()
        print(f"index written: {out_dir / 'README.md'}")
    if args.zip:
        n_files = zip_pack(out_dir, Path(args.zip))
        print(f"zip written: {args.zip} ({n_files} files)")


if __name__ == "__main__":
    main()
