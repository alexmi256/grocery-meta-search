"""Flipp search client tests (sources/flipp_search.py): the
unauthenticated search/flyer API over a fake session, using the
real captured fixtures (Maxi flyer 8179372)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import requests

from grocery_meta_search.sources.flipp_search import (
    FlippSearchClient,
    FlippSearchError,
    SearchConfig,
)

FIXTURES = Path(__file__).parent / "fixtures"
CFG = SearchConfig(store_slug="maxi", merchant_name="maxi", postal_code="H0H0H0")


def _load(name: str) -> Any:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class FakeResponse:
    def __init__(self, payload: Any = None, status: int = 200) -> None:
        self._payload = payload
        self.status_code = status

    def json(self) -> Any:
        return self._payload


class FakeSession:
    def __init__(self, handler: Any) -> None:
        self.handler = handler
        self.headers: dict[str, str] = {}
        self.calls: list[str] = []

    def get(self, url: str, params: dict[str, Any] | None = None, timeout: int = 0) -> FakeResponse:
        self.calls.append(url)
        return self.handler(url, params or {})


def _handler(url: str, params: dict[str, Any]) -> FakeResponse:
    if "/items/search" in url:
        assert params["q"] == "maxi" and params["postal_code"] == "H0H0H0"
        return FakeResponse(_load("flipp_search.json"))
    if "/flyers/" in url:
        return FakeResponse(_load("flipp_search_flyer.json"))
    raise AssertionError(url)


def test_fetch_store_editions_from_fixtures() -> None:
    session = FakeSession(_handler)
    client = FlippSearchClient(session=session)  # type: ignore[arg-type]
    editions = client.fetch_store_editions(CFG)
    assert len(editions) == 1
    ed = editions[0]
    assert ed.source_ref == "8179372"
    assert len(ed.items) == len(_load("flipp_search_flyer.json")["items"])
    assert ed.valid_from is not None and ed.valid_to is not None
    assert all(it.valid_from == ed.valid_from for it in ed.items)


def test_merchant_flyer_ids_dedupes_and_filters() -> None:
    def handler(url: str, params: dict[str, Any]) -> FakeResponse:
        return FakeResponse({"flyers": [{"id": 5}, {"id": 5}, {"id": "7"}, {"name": "x"}, {"id": 9}]})

    client = FlippSearchClient(session=FakeSession(handler))  # type: ignore[arg-type]
    assert client.merchant_flyer_ids(CFG) == [5, 9]


def test_response_shape_and_status_errors() -> None:
    def list_payload(url: str, params: dict[str, Any]) -> FakeResponse:
        return FakeResponse([1, 2, 3])

    client = FlippSearchClient(session=FakeSession(list_payload))  # type: ignore[arg-type]
    with pytest.raises(FlippSearchError, match="unexpected search response shape"):
        client.search(CFG)
    with pytest.raises(FlippSearchError, match="unexpected flyer response shape"):
        client.get_flyer(1)

    def status500(url: str, params: dict[str, Any]) -> FakeResponse:
        return FakeResponse(status=500)

    client = FlippSearchClient(session=FakeSession(status500))  # type: ignore[arg-type]
    with pytest.raises(FlippSearchError, match="unexpected status 500"):
        client.search(CFG)

    class DownSession:
        headers: dict[str, str] = {}

        def get(self, url: str, params: Any = None, timeout: int = 0) -> FakeResponse:
            raise requests.ConnectionError("down")

    client = FlippSearchClient(session=DownSession())  # type: ignore[arg-type]
    with pytest.raises(FlippSearchError, match="request failed"):
        client.search(CFG)
