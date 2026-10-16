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
        FlyerItem(name_fr="Détergent à lessive", price_text="5.00", price_value=5.0),
    ]
    # Classified non-grocery ("Détergent à lessive" -> Household) is
    # discarded at ingest; unclassified items are KEPT for review.
    stats: dict = {}
    assert insert_items(conn, 1, "maxi", items, stats) == 2
    assert stats["discarded"] == 1
    rows = conn.execute(
        "SELECT name_fr, price_value, category, item_key FROM flyer_items ORDER BY id"
    ).fetchall()
    assert len(rows) == 2
    assert rows[0][0] == "Pommes" and rows[0][1] == 2.5
    assert rows[0][2] == "Fruits & Vegetables > Fresh Fruits"
    assert rows[1][0] == "Recette du chef" and rows[1][2] == "Unclassified"
    prov = [
        tuple(r)
        for r in conn.execute(
            "SELECT department, subcategory, method FROM item_classifications ORDER BY item_id"
        ).fetchall()
    ]
    assert prov == [
        ("Fruits & Vegetables", "Fresh Fruits", "rule"),
        ("Unclassified", "Unclassified", "none"),
    ]
    obs = conn.execute("SELECT COUNT(*) FROM price_observations").fetchone()[0]
    assert obs == 1  # only the priced kept item gets an observation
    conn.close()


def test_insert_items_exclusion_layer() -> None:
    conn = _conn()
    items = [
        # Unclassified furniture: excluded at ingest, with the reason.
        FlyerItem(name_fr="Banner - Rollback", price_text=None, price_value=None),
        FlyerItem(name_fr="Plus taxes", price_text=None, price_value=None),
        # Unclassified but plausibly grocery: kept for review.
        FlyerItem(name_fr="Recette du chef", price_text=None, price_value=None),
    ]
    stats: dict = {}
    assert insert_items(conn, 1, "maxi", items, stats) == 1
    assert stats["excluded"] == 2
    assert stats["excluded_reasons"] == {
        "furniture:banner": 1,
        "boilerplate": 1,
    }
    rows = conn.execute("SELECT name_fr FROM flyer_items").fetchall()
    assert [r[0] for r in rows] == ["Recette du chef"]
    conn.close()
