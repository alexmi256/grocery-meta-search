"""Thin-edition guard: flag flyer cycles whose item count collapsed.

Motivated by the 2026-10-17 partial-capture incident (see
docs/research/thin-edition-guard.md): during a loaded parallel refresh,
network timeouts silently truncated many stores' fetches. The editions
were stored with fetch_status 'ok', and because stored editions are
skipped on later runs, the thin captures were permanent. Fetch success
status cannot detect this failure mode — only the item count can.

How it works: a store's flyers are grouped into cycles by valid_from
(all publications starting the same day count as one cycle). For every
cycle still valid today, the guard compares its stored item total
against a baseline — the median total of the up-to-3 most recent
earlier cycles. A cycle is flagged when BOTH:

- its total is below RATIO (0.5) x baseline, and
- the absolute shortfall is at least MIN_DROP (10) items

(the absolute floor keeps tiny stores — 1-to-5-item cycles — from
tripping on ordinary variance).

The guard is advisory: it never fails a fetch and never deletes
anything. It surfaces a WARNING line in the fetch report and stamps
each flyer of the thin cycle's raw JSON with a "thin_edition_guard"
record so the flag is queryable later. Run standalone to audit a
database without fetching:

    python -m grocery_meta_search.pipeline.guard --db data/grocery.db
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import statistics
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

RATIO = 0.5
BASELINE_CYCLES = 3
MIN_DROP = 10


@dataclass
class ThinEditionWarning:
    store_slug: str
    cycle_from: str
    cycle_to: str
    current: int
    baseline: float
    prior_cycles: list[tuple[str, int]] = field(default_factory=list)


def cycle_totals(conn: sqlite3.Connection, store_slug: str) -> list[tuple[str, str, int]]:
    """(valid_from, max valid_to, stored item total) per cycle, oldest first."""
    rows = conn.execute(
        """
        SELECT f.valid_from AS vf, MAX(f.valid_to) AS vt, COUNT(i.id) AS n
        FROM flyers f LEFT JOIN flyer_items i ON i.flyer_id = f.id
        WHERE f.store_slug = ? AND f.valid_from IS NOT NULL AND f.valid_to IS NOT NULL
        GROUP BY f.valid_from
        ORDER BY f.valid_from
        """,
        (store_slug,),
    ).fetchall()
    return [(str(r["vf"]), str(r["vt"]), int(r["n"])) for r in rows]


def evaluate_store(conn: sqlite3.Connection, store_slug: str, today: str | None = None) -> list[ThinEditionWarning]:
    """Flag the store's still-valid cycles whose totals collapsed."""
    today = today or date.today().isoformat()
    cycles = cycle_totals(conn, store_slug)
    warnings: list[ThinEditionWarning] = []
    for idx, (cycle_from, cycle_to, current) in enumerate(cycles):
        if cycle_to < today:
            continue
        priors = cycles[max(0, idx - BASELINE_CYCLES) : idx]
        if not priors:
            continue
        baseline = float(statistics.median(c for _, _, c in priors))
        if current < RATIO * baseline and baseline - current >= MIN_DROP:
            warnings.append(
                ThinEditionWarning(
                    store_slug=store_slug,
                    cycle_from=cycle_from,
                    cycle_to=cycle_to,
                    current=current,
                    baseline=baseline,
                    prior_cycles=[(vf, n) for vf, _, n in priors],
                )
            )
    return warnings


def warning_text(w: ThinEditionWarning) -> str:
    priors = ", ".join(f"{vf}: {n}" for vf, n in w.prior_cycles)
    return (
        f"THIN EDITION {w.store_slug} cycle {w.cycle_from}..{w.cycle_to}: "
        f"{w.current} items vs baseline {w.baseline:g} "
        f"(prior cycles {priors}) — verify with a solo re-fetch"
    )


def record_warnings(conn: sqlite3.Connection, warnings: list[ThinEditionWarning], today: str | None = None) -> None:
    """Stamp each flyer of a thin cycle's raw JSON with the guard record."""
    today = today or date.today().isoformat()
    for w in warnings:
        rows = conn.execute(
            "SELECT id, raw FROM flyers WHERE store_slug = ? AND valid_from = ?",
            (w.store_slug, w.cycle_from),
        ).fetchall()
        for row in rows:
            try:
                raw: dict[str, Any] = json.loads(row["raw"]) if row["raw"] else {}
            except (TypeError, json.JSONDecodeError):
                raw = {}
            if not isinstance(raw, dict):
                raw = {"_source_raw": raw}
            raw["thin_edition_guard"] = {
                "flagged_on": today,
                "current": w.current,
                "baseline": w.baseline,
                "prior_cycles": [[vf, n] for vf, n in w.prior_cycles],
            }
            conn.execute(
                "UPDATE flyers SET raw = ? WHERE id = ?",
                (json.dumps(raw, ensure_ascii=False), int(row["id"])),
            )
    conn.commit()


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit stored flyer cycles for thin (partially captured) editions.")
    parser.add_argument("--db", required=True, type=Path)
    parser.add_argument("--slugs", default=None, help="comma-separated; default: all stores")
    parser.add_argument("--today", default=None, help="ISO date override (default: today)")
    parser.add_argument("--stamp", action="store_true", help="also record flags in flyer raw JSON")
    args = parser.parse_args()

    from ..db import connect, init_schema

    conn = connect(args.db)
    init_schema(conn)
    if args.slugs:
        slugs = [s.strip() for s in args.slugs.split(",") if s.strip()]
    else:
        slugs = [
            str(r["store_slug"]) for r in conn.execute("SELECT DISTINCT store_slug FROM flyers ORDER BY store_slug")
        ]
    flagged = 0
    for slug in slugs:
        warnings = evaluate_store(conn, slug, today=args.today)
        for w in warnings:
            print(warning_text(w))
            flagged += 1
        if args.stamp and warnings:
            record_warnings(conn, warnings, today=args.today)
    if not flagged:
        print("no thin editions")
    conn.close()


if __name__ == "__main__":
    main()
