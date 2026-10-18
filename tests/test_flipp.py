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
    loyalty_program_of,
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
    # Wishabi names are combined 'FR | EN'; they split at ingestion.
    assert item.name_fr == "CROUSTILLES PRINGLES"
    assert item.name_en == "POTATO CHIPS"
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


def test_item_from_product_unit_in_post_price_text() -> None:
    # Flipp carries by-weight units in post_price_text ("/lb 4,39$/kg"),
    # not in the bare price_text; the unit must still be captured.
    product = dict(_load("flipp_products_fr.json")[0])
    product["price_text"] = "1.99"
    product["post_price_text"] = "/lb 4,39$/kg"
    item = item_from_product(product, "fr")
    assert item.price_value == 1.99
    assert item.price_unit == "lb"


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


def test_loyalty_camembert_not_gated() -> None:
    """'member' inside 'camembert' must not flag loyalty gating."""
    item = item_from_product({"name": "FROMAGE BRIE OU CAMEMBERT ILE DE FRANCE"}, "fr")
    assert not item.loyalty_gated


def test_loyalty_scene_plus() -> None:
    item = item_from_product({"name": "CRAQUELINS CHEEZ-IT", "pre_price_text": "Prix Membre Scène+"}, "fr")
    assert item.loyalty_gated
    assert loyalty_program_of({"pre_price_text": "Prix Membre Scène+"}) == "Scène+"


def test_loyalty_pc_optimum() -> None:
    product = {
        "name": "BOEUF HACHÉ",
        "pre_price_text": "Prix membre*",
        "disclaimer_text": "Prix pour les membres PC Optimum.",
    }
    item = item_from_product(product, "fr")
    assert item.loyalty_gated
    assert loyalty_program_of(product) == "PC Optimum"
    assert item.conditions["loyalty_program"] == "PC Optimum"


def test_loyalty_banner_default_program() -> None:
    item = item_from_product(
        {"name": "BOEUF HACHÉ", "pre_price_text": "Prix membre*"},
        "fr",
        default_program="PC Optimum",
    )
    assert item.loyalty_gated
    assert item.conditions["loyalty_program"] == "PC Optimum"


def test_loyalty_program_not_set_when_not_gated() -> None:
    item = item_from_product({"name": "POMMES"}, "fr", default_program="PC Optimum")
    assert not item.loyalty_gated
    assert "loyalty_program" not in item.conditions


def test_loyalty_name_only_scene_plus_not_gated() -> None:
    """'Scene+' in the name alone is a points offer, not a gated price."""
    item = item_from_product({"name": "SIROP - IGA Scene+", "price_text": "5.99"}, "fr")
    assert not item.loyalty_gated
