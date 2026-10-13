"""Database schema and edition-idempotency tests."""

import sqlite3

from grocery_meta_search.db import connect, init_schema
from grocery_meta_search.pipeline.fetch import upsert_edition
from grocery_meta_search.sources.base import FlyerEdition


def _conn() -> sqlite3.Connection:
    conn = connect(":memory:")
    init_schema(conn)
    conn.execute("INSERT INTO stores (slug, name) VALUES ('maxi', 'Maxi')")
    conn.execute("INSERT INTO flyer_sources (id, store_slug, name) VALUES (1, 'maxi', 'flipp')")
    return conn


def test_schema_tables_exist() -> None:
    conn = _conn()
    tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    assert {"stores", "flyer_sources", "flyers", "flyer_items", "price_observations"} <= tables
    conn.close()


def test_edition_upsert_is_idempotent() -> None:
    conn = _conn()
    edition = FlyerEdition(valid_from="2026-10-08", valid_to="2026-10-14")
    first_id, first_new = upsert_edition(conn, "maxi", 1, edition)
    second_id, second_new = upsert_edition(conn, "maxi", 1, edition)
    assert first_new is True
    assert second_new is False
    assert first_id == second_id
    assert conn.execute("SELECT COUNT(*) FROM flyers").fetchone()[0] == 1
    conn.close()


def test_edition_distinct_weeks_coexist() -> None:
    conn = _conn()
    e1 = FlyerEdition(valid_from="2026-10-08", valid_to="2026-10-14")
    e2 = FlyerEdition(valid_from="2026-10-15", valid_to="2026-10-21")
    upsert_edition(conn, "maxi", 1, e1)
    upsert_edition(conn, "maxi", 1, e2)
    assert conn.execute("SELECT COUNT(*) FROM flyers").fetchone()[0] == 2
    conn.close()
