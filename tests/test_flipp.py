"""Golden-sample tests for the Flipp FlyerKit client.

Fixtures are trimmed real API responses captured 2026-10-12
(Maxi publication 8172743). No network access in tests.
"""

import json
from pathlib import Path

from grocery_meta_search.sources.flipp import (
    _to_date,
    edition_from_publication,
    item_from_product,
    merge_locales,
)

FIXTURES = Path(__file__).with_name("fixtures")


def _load(name: str):  # type: ignore[no-untyped-def]
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def test_to_date_iso_with_offset() -> None:
    assert _to_date("2026-10-08T00:00:00-04:00") == "2026-10-08"


def test_to_date_none() -> None:
    assert _to_date(None) is None


def test_edition_from_publication() -> None:
    pub = _load("flipp_publication.json")
    edition = edition_from_publication(pub)
    assert edition.valid_from == "2026-10-08"
    assert edition.valid_to == "2026-10-14"
    assert edition.flyer_type  # source's own type label round-trips


def test_item_from_product_fr() -> None:
    product = _load("flipp_products_fr.json")[0]
    item = item_from_product(product, "fr")
    assert item.name_fr == "CROUSTILLES PRINGLES | POTATO CHIPS"
    assert item.name_en is None
    assert item.price_text == "2.50"
    assert item.price_value == 2.5
    assert item.sku == "21003832_EA"
    assert item.image_url and item.image_url.startswith("http")
    assert item.bbox is not None and "page" in item.bbox
    assert item.valid_from == "2026-10-08"
    assert item.valid_to == "2026-10-14"
    assert item.languages == ["fr"]
    assert item.confidence == 1.0


def test_item_from_product_empty_price() -> None:
    products = _load("flipp_products_fr.json")
    empties = [p for p in products if not p.get("price_text")]
    assert empties, "fixture should include a price-less product"
    item = item_from_product(empties[0], "fr")
    assert item.price_text is None
    assert item.price_value is None
    assert item.name_fr  # still a real item (recipe/brand ad)


def test_merge_locales_by_sku() -> None:
    fr = [item_from_product(p, "fr") for p in _load("flipp_products_fr.json")]
    en = [item_from_product(p, "en") for p in _load("flipp_products_en.json")]
    merged = merge_locales(fr, en)
    assert len(merged) == len(fr)  # every FR item matched its EN twin
    for item in merged:
        assert item.name_fr
        assert item.name_en
        assert set(item.languages) == {"fr", "en"}


def test_merge_locales_en_only_kept() -> None:
    fr = [item_from_product(p, "fr") for p in _load("flipp_products_fr.json")[:2]]
    en = [item_from_product(p, "en") for p in _load("flipp_products_en.json")]
    merged = merge_locales(fr, en)
    assert len(merged) == len(en)  # unmatched EN items kept with name_en
    en_only = [m for m in merged if m.name_fr is None]
    assert en_only
    assert all(m.name_en for m in en_only)
