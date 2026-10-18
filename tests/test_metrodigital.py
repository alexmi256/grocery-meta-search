"""Metro Digital source: payload flattening and product mapping."""

from __future__ import annotations

import json
from pathlib import Path

from grocery_meta_search.sources.metrodigital import (
    item_from_product,
    load_metrodigital_configs,
    products_from_pages,
)

FIXTURE = Path(__file__).parent / "fixtures" / "metrodigital_pages.json"


def _pages() -> list:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def test_products_flatten_dedupe_and_skip_inblocks() -> None:
    found = products_from_pages(_pages())
    # veal + plain on page 1, no-price on page 2; the page-2 repeat
    # of plain (same SKU) is deduped, the Inblock block is skipped.
    assert [page for page, _ in found] == [1, 1, 2]
    assert [p["sku"] for _, p in found] == ["38445001", "38944001", "45162101"]


def test_item_mapping_full_product() -> None:
    _, veal = products_from_pages(_pages())[0]
    item = item_from_product(veal, 1, "2026-10-15", "2026-10-21")
    assert item.name_fr == "côtelettes de veau de grain nature ou marinées Halal"
    assert item.name_en == "grain-fed veal chops regular or marinated Halal"
    assert item.price_value == 14.99
    assert item.price_unit == "lb"
    assert item.price_text == "14.99 /lb"
    assert item.sku == "38445001"
    assert item.conditions["alternate_price"] == "33.04/kg"
    assert item.conditions["regular_price"] == "17,99/lb - 39,66/kg"
    assert item.conditions["native_category_en"] == "Meat and Deli"
    assert item.conditions["halal"] is True
    assert item.valid_from == "2026-10-15"
    assert item.valid_to == "2026-10-21"
    assert item.languages == ["fr", "en"]
    # First click region, percent coords scaled to the 1000 grid.
    assert item.bbox == {"x": 13, "y": 165, "w": 972, "h": 414, "page": 1}


def test_item_mapping_missing_price() -> None:
    found = products_from_pages(_pages())
    item = item_from_product(found[2][1], 2, "2026-10-15", "2026-10-21")
    assert item.price_value is None
    assert item.price_text is None


def test_unit_normalization() -> None:
    base = {"productFr": "x", "salePrice": "1.99"}
    cases = {
        "/lb": "lb",
        "/kg": "kg",
        "le 100 g": "100g",
        "ch.": "each",
        "+TX": None,
        None: None,
    }
    for raw, expected in cases.items():
        item = item_from_product({**base, "promoUnitFr": raw}, 1, None, None)
        assert item.price_unit == expected, raw
    pack = item_from_product({**base, "promoUnitFr": "6 un."}, 1, None, None)
    assert pack.price_unit is None
    assert pack.package_size == "6 un."
    assert pack.conditions["pack_count"] == 6


def test_multibuy_single_from_alternate() -> None:
    item = item_from_product(
        {"productFr": "pâtes Barilla", "salePrice": "5.0", "priceQuantity": "3", "alternatePrice": "ou 1,67 l’unité"},
        1,
        None,
        None,
    )
    assert item.price_value == 1.67
    assert item.conditions["multibuy"] == {"count": 3, "total": 5.0}


def test_multibuy_single_from_promo_unit_text() -> None:
    item = item_from_product(
        {
            "productFr": "grosse mangue rouge",
            "salePrice": "5.0",
            "priceQuantity": "2",
            "promoUnitFr": "ou 2,50 l'unité",
        },
        1,
        None,
        None,
    )
    assert item.price_value == 2.50
    assert item.price_unit is None
    assert item.conditions["multibuy"] == {"count": 2, "total": 5.0}


def test_multibuy_no_single_falls_back_to_total_over_count() -> None:
    item = item_from_product({"productFr": "bières du monde", "salePrice": "28.0", "priceQuantity": "2"}, 1, None, None)
    assert item.price_value == 14.0
    assert item.conditions["multibuy"] == {"count": 2, "total": 28.0}


def test_multibuy_case_price_phrase() -> None:
    item = item_from_product(
        {
            "productFr": "bière Corona",
            "salePrice": "77.48",
            "priceQuantity": "2",
            "alternatePrice": "ou à partir de 43,29 +TX la caisse",
        },
        1,
        None,
        None,
    )
    assert item.price_value == 43.29
    assert item.conditions["multibuy"] == {"count": 2, "total": 77.48}


def test_store_configs_load() -> None:
    configs = load_metrodigital_configs()
    assert {slug: c.store_id for slug, c in configs.items()} == {
        "adonis": 21937,
        "metro": 380,
        "metro-plus": 381,
        "super-c": 443,
    }
    assert all(c.config_url.endswith("/config/app.json") for c in configs.values())
