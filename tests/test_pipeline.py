"""Fetch-pipeline unit tests (item keys, inserts). No network."""

import sqlite3

from grocery_meta_search.db import connect, init_schema
from grocery_meta_search.pipeline.fetch import insert_items, item_key, normalize_name
from grocery_meta_search.sources.base import FlyerItem


def _conn() -> sqlite3.Connection:
    conn = connect(":memory:")
    init_schema(conn)
    conn.execute("INSERT INTO stores (slug, name) VALUES ('maxi', 'Maxi')")
    conn.execute(
        "INSERT INTO flyers (id, store_slug, flyer_type, valid_from, valid_to) "
        "VALUES (1, 'maxi', 'weekly', '2026-10-08', '2026-10-14')"
    )
    return conn


def test_normalize_name() -> None:
    assert normalize_name("  CROUSTILLES  Pringles ") == "croustilles pringles"


def test_item_key_stable_and_fr_preferred() -> None:
    a = FlyerItem(name_fr="Pommes", name_en="Apples", price_unit="lb")
    b = FlyerItem(name_fr="  POMMES ", name_en="Apples", price_unit="lb")
    c = FlyerItem(name_fr="Pommes", name_en="Apples", price_unit="kg")
    assert item_key("maxi", a) == item_key("maxi", b)
    assert item_key("maxi", a) != item_key("maxi", c)
    assert item_key("maxi", a) != item_key("iga", a)


def test_insert_items_and_observations() -> None:
    conn = _conn()
    items = [
        FlyerItem(name_fr="Pommes", price_text="2.50", price_value=2.5, sku="1"),
        FlyerItem(name_fr="Recette du chef", price_text=None, price_value=None),
    ]
    assert insert_items(conn, 1, "maxi", items) == 2
    rows = conn.execute(
        "SELECT name_fr, price_value, category, item_key FROM flyer_items ORDER BY id"
    ).fetchall()
    assert rows[0][0] == "Pommes" and rows[0][1] == 2.5
    assert rows[0][2] == "Unclassified"  # Phase 4 will classify
    assert rows[0][3] and rows[1][3] and rows[0][3] != rows[1][3]
    obs = conn.execute("SELECT COUNT(*) FROM price_observations").fetchone()[0]
    assert obs == 1  # only the priced item gets an observation
    conn.close()
