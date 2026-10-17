"""Thin-edition guard tests (pipeline/guard.py). No network.

The guard groups a store's flyers into cycles by valid_from and flags
a still-valid cycle whose stored item total collapsed below half the
median of the up-to-3 previous cycles (with a 10-item absolute floor).
"""
import json
import sqlite3

from grocery_meta_search.db import connect, init_schema
from grocery_meta_search.pipeline.guard import (
    cycle_totals,
    evaluate_store,
    record_warnings,
)

TODAY = "2026-10-17"


def _conn() -> sqlite3.Connection:
    conn = connect(":memory:")
    init_schema(conn)
    conn.execute("INSERT INTO stores (slug, name) VALUES ('s', 'Store')")
    return conn


def _cycle(
    conn: sqlite3.Connection,
    valid_from: str,
    valid_to: str,
    items: int,
    source_ref: str | None = None,
) -> None:
    cur = conn.execute(
        "INSERT INTO flyers (store_slug, valid_from, valid_to, source_ref, raw) "
        "VALUES ('s', ?, ?, ?, '{}')",
        (valid_from, valid_to, source_ref),
    )
    flyer_id = cur.lastrowid
    for i in range(items):
        conn.execute(
            "INSERT INTO flyer_items (flyer_id, store_slug, item_key) VALUES (?, 's', ?)",
            (flyer_id, f"{valid_from}-{i}"),
        )
    conn.commit()


def test_cycle_totals_aggregates_publications() -> None:
    conn = _conn()
    _cycle(conn, "2026-10-08", "2026-10-14", 10, source_ref="pub-a")
    _cycle(conn, "2026-10-08", "2026-10-14", 5, source_ref="pub-b")  # 2nd publication
    _cycle(conn, "2026-10-15", "2026-10-21", 7)
    assert cycle_totals(conn, "s") == [
        ("2026-10-08", "2026-10-14", 15),
        ("2026-10-15", "2026-10-21", 7),
    ]


def test_collapse_flags() -> None:
    conn = _conn()
    _cycle(conn, "2026-09-24", "2026-09-30", 30)
    _cycle(conn, "2026-10-01", "2026-10-07", 28)
    _cycle(conn, "2026-10-08", "2026-10-14", 32)
    _cycle(conn, "2026-10-15", "2026-10-21", 3)  # the Bonanza shape: 27+ -> 2
    warnings = evaluate_store(conn, "s", today=TODAY)
    assert len(warnings) == 1
    w = warnings[0]
    assert w.current == 3 and w.baseline == 30.0 and w.cycle_from == "2026-10-15"


def test_normal_variance_does_not_flag() -> None:
    conn = _conn()
    _cycle(conn, "2026-10-01", "2026-10-07", 30)
    _cycle(conn, "2026-10-08", "2026-10-14", 28)
    _cycle(conn, "2026-10-15", "2026-10-21", 24)  # 83% of baseline: fine
    assert evaluate_store(conn, "s", today=TODAY) == []


def test_no_history_does_not_flag() -> None:
    conn = _conn()
    _cycle(conn, "2026-10-15", "2026-10-21", 1)
    assert evaluate_store(conn, "s", today=TODAY) == []


def test_tiny_store_floor() -> None:
    conn = _conn()
    _cycle(conn, "2026-10-08", "2026-10-14", 4)
    _cycle(conn, "2026-10-15", "2026-10-21", 1)  # drop of 3 < MIN_DROP
    assert evaluate_store(conn, "s", today=TODAY) == []


def test_expired_thin_cycle_not_flagged() -> None:
    conn = _conn()
    _cycle(conn, "2026-10-01", "2026-10-07", 40)
    _cycle(conn, "2026-10-08", "2026-10-14", 2)  # thin but no longer valid
    assert evaluate_store(conn, "s", today=TODAY) == []


def test_zero_item_cycle_flags() -> None:
    conn = _conn()
    _cycle(conn, "2026-10-08", "2026-10-14", 50)
    _cycle(conn, "2026-10-15", "2026-10-21", 0)
    warnings = evaluate_store(conn, "s", today=TODAY)
    assert len(warnings) == 1 and warnings[0].current == 0


def test_record_warnings_stamps_flyer_raw() -> None:
    conn = _conn()
    _cycle(conn, "2026-10-08", "2026-10-14", 40)
    _cycle(conn, "2026-10-15", "2026-10-21", 2)
    warnings = evaluate_store(conn, "s", today=TODAY)
    record_warnings(conn, warnings, today=TODAY)
    raw = conn.execute(
        "SELECT raw FROM flyers WHERE valid_from = '2026-10-15'"
    ).fetchone()["raw"]
    stamp = json.loads(raw)["thin_edition_guard"]
    assert stamp["current"] == 2 and stamp["baseline"] == 40.0
    assert stamp["flagged_on"] == TODAY
