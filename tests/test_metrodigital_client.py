"""Metro Digital client tests: config loading, flyer discovery,
page fetching, retry behaviour and error mapping — fake session,
no network."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import requests

from grocery_meta_search.sources.metrodigital import (
    MetroDigitalClient,
    MetroDigitalConfig,
    MetroDigitalError,
)

FIXTURE = Path(__file__).parent / "fixtures" / "metrodigital_pages.json"
CFG = MetroDigitalConfig(slug="adonis", config_url="https://banner.test/config/app.json", store_id=21937, locale="fr")
APP_CONFIG = {
    "api": "https://api.test/api",
    "apikey": "test-key",
    "banner_id": "test-banner",
    "api_version": "3.0",
}
LISTING = {
    "flyers": [
        {
            "title": "84250q",
            "flyerId": "pub-id",
            "storeName": "Sauvé",
            "pageCount": 2,
            "startDate": "2026-10-15T00:00:00Z",
            "endDate": "2026-10-21T23:59:00Z",
        },
        {"flyerId": "no-title-flyer"},  # skipped: no title
    ]
}


class FakeResponse:
    def __init__(self, payload: Any = None, status: int = 200) -> None:
        self._payload = payload
        self.status_code = status

    def json(self) -> Any:
        return self._payload

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}", response=self)  # type: ignore[arg-type]


class FakeSession:
    """Routes by URL fragment; a route value may be a list of
    outcomes consumed in order (for retry tests)."""

    def __init__(self, routes: dict[str, Any]) -> None:
        self.routes = routes
        self.calls: list[tuple[str, dict[str, str]]] = []

    def get(self, url: str, headers: dict[str, str] | None = None, timeout: int = 0) -> FakeResponse:
        self.calls.append((url, headers or {}))
        for fragment, outcome in self.routes.items():
            if fragment in url:
                if isinstance(outcome, list):
                    outcome = outcome.pop(0)
                if isinstance(outcome, Exception):
                    raise outcome
                return outcome
        raise AssertionError(f"unrouted URL: {url}")


@pytest.fixture(autouse=True)
def _no_sleep(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("time.sleep", lambda _s: None)


def _pages_payload() -> Any:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def _client(routes: dict[str, Any]) -> tuple[MetroDigitalClient, FakeSession]:
    session = FakeSession(routes)
    return MetroDigitalClient(session=session), session  # type: ignore[arg-type]


def _happy_routes() -> dict[str, Any]:
    return {
        "config/app.json": FakeResponse(APP_CONFIG),
        "/flyers/": FakeResponse(LISTING),
        "/pages/": FakeResponse(_pages_payload()),
    }


def test_fetch_store_editions_happy_path() -> None:
    client, session = _client(_happy_routes())
    editions = client.fetch_store_editions(CFG)
    assert len(editions) == 1  # the title-less flyer is skipped
    ed = editions[0]
    assert ed.source_ref == "84250q"
    assert ed.valid_from == "2026-10-15" and ed.valid_to == "2026-10-21"
    assert len(ed.items) == 3  # fixture: veal + plain + no-price (deduped)
    assert ed.raw["metrodigital"]["store_name"] == "Sauvé"
    # The listing call carried the credentials from the app config.
    flyers_call = next(h for u, h in session.calls if "/flyers/" in u)
    assert flyers_call["Ocp-Apim-Subscription-Key"] == "test-key"
    assert flyers_call["Banner"] == "test-banner"
    assert flyers_call["x-api-version"] == "3.0"


def test_fetch_store_editions_no_flyers() -> None:
    client, _ = _client({"config/app.json": FakeResponse(APP_CONFIG), "/flyers/": FakeResponse({"flyers": []})})
    assert client.fetch_store_editions(CFG) == []


def test_config_http_error_is_not_retried() -> None:
    client, session = _client({"config/app.json": FakeResponse(status=404)})
    with pytest.raises(MetroDigitalError, match="config fetch failed"):
        client.fetch_store_editions(CFG)
    assert len(session.calls) == 1  # 4xx: no retry


def test_incomplete_config_rejected() -> None:
    client, _ = _client({"config/app.json": FakeResponse({"api": "https://api.test/api"})})
    with pytest.raises(MetroDigitalError, match="incomplete app config"):
        client.fetch_store_editions(CFG)


def test_pages_retry_then_success() -> None:
    routes = _happy_routes()
    routes["/pages/"] = [
        requests.ConnectionError("stall"),
        requests.ConnectionError("stall again"),
        FakeResponse(_pages_payload()),
    ]
    client, session = _client(routes)
    editions = client.fetch_store_editions(CFG)
    assert len(editions) == 1 and len(editions[0].items) == 3
    assert sum(1 for u, _ in session.calls if "/pages/" in u) == 3


def test_pages_persistent_failure_raises() -> None:
    routes = _happy_routes()
    routes["/pages/"] = FakeResponse(status=503)
    client, session = _client(routes)
    with pytest.raises(MetroDigitalError, match="pages fetch failed"):
        client.fetch_store_editions(CFG)
    assert sum(1 for u, _ in session.calls if "/pages/" in u) == 3  # retried, then gave up


def test_listing_failure_raises() -> None:
    routes = _happy_routes()
    routes["/flyers/"] = requests.ConnectionError("no route")
    client, _ = _client(routes)
    with pytest.raises(MetroDigitalError, match="flyer list failed"):
        client.fetch_store_editions(CFG)
