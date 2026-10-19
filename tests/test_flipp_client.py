"""FlyerKit client tests: publication/product fetching over a fake
session, payload-shape tolerance, locale merge through the client,
flyer-type filtering, and error mapping.

Payloads are the real captured fixtures from test_flipp.py (Maxi
publication 8172743) — only the transport is fake.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import requests

from grocery_meta_search.sources.flipp import (
    BrandConfig,
    FlyerKitClient,
    FlyerKitError,
)

FIXTURES = Path(__file__).parent / "fixtures"
CFG = BrandConfig(store_slug="maxi", brand_slug="maxi", access_token="tok", store_code="123")


def _load(name: str) -> Any:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class FakeResponse:
    def __init__(self, payload: Any = None, status: int = 200, json_error: bool = False) -> None:
        self._payload = payload
        self.status_code = status
        self._json_error = json_error

    def json(self) -> Any:
        if self._json_error:
            raise json.JSONDecodeError("bad", "doc", 0)
        return self._payload


class FakeSession:
    def __init__(self, handler: Any) -> None:
        self.handler = handler
        self.headers: dict[str, str] = {}
        self.calls: list[tuple[str, dict[str, Any]]] = []

    def get(self, url: str, params: dict[str, Any] | None = None, timeout: int = 0) -> FakeResponse:
        self.calls.append((url, params or {}))
        return self.handler(url, params or {})


def _api_handler(url: str, params: dict[str, Any]) -> FakeResponse:
    if "/publications/" in url:
        return FakeResponse([_load("flipp_publication.json")])
    if "/products" in url:
        locale = params.get("locale", "fr")
        return FakeResponse(_load(f"flipp_products_{locale}.json"))
    raise AssertionError(url)


def test_fetch_store_editions_merges_locales() -> None:
    client = FlyerKitClient(session=FakeSession(_api_handler))  # type: ignore[arg-type]
    editions = client.fetch_store_editions(CFG)
    assert len(editions) == 1
    ed = editions[0]
    assert ed.valid_from == "2026-10-08" and ed.valid_to == "2026-10-14"
    assert ed.languages == ["fr", "en"]
    assert len(ed.items) == len(_load("flipp_products_fr.json"))
    first = ed.items[0]
    assert first.name_fr and first.name_en  # FR item gained its EN name
    assert first.valid_from == "2026-10-08"  # validity present on items


def test_publication_payload_shapes() -> None:
    pub = _load("flipp_publication.json")

    def wrapped(key: str) -> Any:
        def handler(url: str, params: dict[str, Any]) -> FakeResponse:
            if "/publications/" in url:
                return FakeResponse({key: [pub]})
            return FakeResponse({"products": []})

        return handler

    for key in ("flyers", "publications", "data", "results"):
        client = FlyerKitClient(session=FakeSession(wrapped(key)))  # type: ignore[arg-type]
        assert len(client.get_publications(CFG)) == 1, key
    client = FlyerKitClient(session=FakeSession(wrapped("nope")))  # type: ignore[arg-type]
    assert client.get_publications(CFG) == []


def test_flyer_type_filter_and_id_less_publications() -> None:
    pub = dict(_load("flipp_publication.json"))
    pub["flyer_type"] = "weekly"
    other = dict(pub, id=999, flyer_type="monthly")
    no_id = dict(pub)
    del no_id["id"]

    def handler(url: str, params: dict[str, Any]) -> FakeResponse:
        if "/publications/" in url:
            return FakeResponse([pub, other, no_id])
        return FakeResponse([])

    client = FlyerKitClient(session=FakeSession(handler))  # type: ignore[arg-type]
    filtered = BrandConfig(
        store_slug="maxi", brand_slug="maxi", access_token="t", store_code="1", flyer_type_filter="weekly"
    )
    editions = client.fetch_store_editions(filtered, locales=("fr",))
    assert [e.source_ref for e in editions] == [str(pub["id"])]
    all_editions = client.fetch_store_editions(CFG, locales=("fr",))
    assert len(all_editions) == 2  # the id-less publication is skipped


def test_http_errors_map_to_flyerkit_error() -> None:
    def status500(url: str, params: dict[str, Any]) -> FakeResponse:
        return FakeResponse(status=500)

    client = FlyerKitClient(session=FakeSession(status500))  # type: ignore[arg-type]
    with pytest.raises(FlyerKitError, match="unexpected status 500"):
        client.get_publications(CFG)

    def bad_json(url: str, params: dict[str, Any]) -> FakeResponse:
        return FakeResponse(json_error=True)

    client = FlyerKitClient(session=FakeSession(bad_json))  # type: ignore[arg-type]
    with pytest.raises(FlyerKitError, match="invalid JSON"):
        client.get_publications(CFG)

    class DownSession:
        headers: dict[str, str] = {}

        def get(self, url: str, params: Any = None, timeout: int = 0) -> FakeResponse:
            raise requests.ConnectionError("no route")

    client = FlyerKitClient(session=DownSession())  # type: ignore[arg-type]
    with pytest.raises(FlyerKitError, match="request failed"):
        client.get_publications(CFG)
