"""Golden-sample tests for the unauthenticated Flipp search client.

Fixtures are trimmed real API responses captured 2026-10-13
(Kim Phat flyer 8179372). No network access in tests.
"""

import json
from pathlib import Path
from typing import Any

import pytest

from grocery_meta_search.sources.flipp_search import (
    FlippSearchClient,
    SearchConfig,
    item_from_search_item,
)

FIXTURES = Path(__file__).with_name("fixtures")


def _load(name: str) -> Any:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def test_merchant_flyer_ids_from_search() -> None:
    data = _load("flipp_search.json")
    ids = [f["id"] for f in data["flyers"] if isinstance(f.get("id"), int)]
    assert ids, "fixture should contain flyer IDs"
    assert len(ids) == len(set(ids))  # deduplicated


def test_item_from_search_item() -> None:
    raw = _load("flipp_search_flyer.json")["items"][0]
    item = item_from_search_item(raw, "fr")
    assert item.name_fr
    assert item.name_en is None
    assert item.price_text is not None
    assert item.price_value is not None
    assert item.image_url and item.image_url.startswith("http")
    assert item.bbox is not None
    assert item.valid_from and item.valid_to
    assert item.languages == ["fr"]
    assert item.confidence == 1.0


def test_fetch_store_editions_merges(monkeypatch: pytest.MonkeyPatch) -> None:
    """fetch_store_editions works end-to-end against fixture data."""
    search_data = _load("flipp_search.json")
    flyer_data = _load("flipp_search_flyer.json")

    client = FlippSearchClient()

    def fake_search(cfg: SearchConfig, locale: str = "fr") -> dict[str, Any]:
        result: dict[str, Any] = search_data
        return result

    def fake_get_flyer(flyer_id: int) -> dict[str, Any]:
        result: dict[str, Any] = flyer_data
        return result

    monkeypatch.setattr(client, "search", fake_search)
    monkeypatch.setattr(client, "get_flyer", fake_get_flyer)

    cfg = SearchConfig(store_slug="kim-phat", merchant_name="kim phat", postal_code="H3Y2Y6")
    editions = client.fetch_store_editions(cfg)
    assert len(editions) == len(search_data["flyers"])
    for edition in editions:
        assert edition.source_ref is not None
        assert edition.valid_from and edition.valid_to
        assert len(edition.items) == len(flyer_data["items"])
