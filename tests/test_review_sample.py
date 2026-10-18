"""Split-quantity, seeded sampling for the review pack generator."""

from __future__ import annotations

import sqlite3

from grocery_meta_search.classify.review_sample import sample_store_ids

SCHEMA = """
CREATE TABLE flyers (id INTEGER PRIMARY KEY, valid_to TEXT);
CREATE TABLE flyer_items (id INTEGER PRIMARY KEY, flyer_id INTEGER,
                           store_slug TEXT);
CREATE TABLE item_classifications (item_id INTEGER, department TEXT);
"""


def _db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.executescript(SCHEMA)
    conn.execute("INSERT INTO flyers VALUES (1, '2026-10-31')")
    conn.execute("INSERT INTO flyers VALUES (2, '2026-10-01')")  # expired
    for item_id in range(1, 41):  # 30 classified + 10 unclassified, current
        conn.execute("INSERT INTO flyer_items VALUES (?, 1, 's')", (item_id,))
        dept = "Pantry" if item_id <= 30 else "Unclassified"
        conn.execute("INSERT INTO item_classifications VALUES (?, ?)",
                     (item_id, dept))
    for item_id in range(41, 46):  # expired-flyer items, never sampled
        conn.execute("INSERT INTO flyer_items VALUES (?, 2, 's')", (item_id,))
        conn.execute("INSERT INTO item_classifications VALUES (?, 'Pantry')",
                     (item_id,))
    return conn


def test_split_quantities_and_current_only() -> None:
    conn = _db()
    picked, n_class, n_unc = sample_store_ids(conn, "s", 5, 3, 42, "2026-10-18")
    assert (n_class, n_unc) == (30, 10)
    assert len(picked) == 8
    assert sum(1 for i in picked if i <= 30) == 5
    assert sum(1 for i in picked if 31 <= i <= 40) == 3
    assert all(i <= 40 for i in picked)  # nothing from the expired flyer


def test_seed_reproduces_and_changes_selection() -> None:
    conn = _db()
    a, _, _ = sample_store_ids(conn, "s", 10, 10, 20261018, "2026-10-18")
    b, _, _ = sample_store_ids(conn, "s", 10, 10, 20261018, "2026-10-18")
    c, _, _ = sample_store_ids(conn, "s", 10, 10, 777, "2026-10-18")
    assert a == b
    assert a != c


def test_quantities_capped_by_pool() -> None:
    conn = _db()
    picked, _, _ = sample_store_ids(conn, "s", 100, 100, 1, "2026-10-18")
    assert len(picked) == 40
