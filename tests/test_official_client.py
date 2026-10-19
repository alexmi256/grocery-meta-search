"""Official-site client tests: the retrying _get, fetch_editions
kind dispatch, and the generic image_page fetcher — fake session,
no network."""

from __future__ import annotations

from datetime import date
from types import SimpleNamespace
from typing import Any

import pytest
import requests

from grocery_meta_search.sources.official import (
    OfficialClient,
    OfficialConfig,
    OfficialEdition,
    OfficialError,
)

TODAY = date(2026, 10, 18)


class FakeResponse:
    def __init__(self, text: str = "", fail: bool = False) -> None:
        self.text = text
        self._fail = fail

    def raise_for_status(self) -> None:
        if self._fail:
            raise requests.HTTPError("HTTP 500")


class FakeSession:
    def __init__(self, outcomes: list[Any]) -> None:
        self.outcomes = outcomes
        self.headers: dict[str, str] = {}
        self.calls = 0

    def get(self, url: str, timeout: int = 0, headers: Any = None) -> FakeResponse:
        self.calls += 1
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


def _client(outcomes: list[Any]) -> tuple[OfficialClient, FakeSession]:
    client = OfficialClient()
    session = FakeSession(outcomes)
    client.session = session  # type: ignore[assignment]
    return client, session


def test_get_retries_then_succeeds() -> None:
    client, session = _client([requests.ConnectionError("x"), FakeResponse(fail=True), FakeResponse("ok")])
    resp = client._get("https://x.test/", retries=2)
    assert resp.text == "ok"
    assert session.calls == 3


def test_get_gives_up_after_retries() -> None:
    client, session = _client([requests.ConnectionError("x")] * 3)
    with pytest.raises(OfficialError, match="GET https://x.test/"):
        client._get("https://x.test/", retries=1)
    assert session.calls == 2  # initial attempt + one retry


def test_fetch_editions_dispatches_every_kind(monkeypatch: pytest.MonkeyPatch) -> None:
    client, _ = _client([])
    sentinel = OfficialEdition(TODAY, TODAY, "weekly", "ref", ["fr"])
    kinds = {
        "image_page": "_image_page",
        "pdf_page": "_pdf_page",
        "flyerify": "_flyerify",
        "circulaires": "_circulaires",
        "flyerbox": "_flyerbox",
        "woo_specials": "_woo_specials",
        "pdf_text": "_pdf_text",
    }
    for kind, method in kinds.items():
        monkeypatch.setattr(client, method, lambda cfg, today, _s=sentinel: _s)
        cfg = OfficialConfig(slug="t", kind=kind, source_name="official:t", page_url="https://x")
        assert client.fetch_editions(cfg, today=TODAY) == [sentinel], kind
    bad = OfficialConfig(slug="t", kind="hologram", source_name="official:t", page_url="https://x")
    with pytest.raises(OfficialError, match="unknown kind"):
        client.fetch_editions(bad, today=TODAY)


def test_image_page_generic_extraction() -> None:
    html = """
    <img src="https://cdn.test/flyer/page1.jpg">
    <img src="https://cdn.test/flyer/page2.jpg">
    <img src="https://cdn.test/logo.png">
    """
    client, _ = _client([])
    client._get = lambda url, **kw: SimpleNamespace(text=html)  # type: ignore[method-assign]
    cfg = OfficialConfig(
        slug="t",
        kind="image_page",
        source_name="official:t",
        page_url="https://x.test/flyer",
        image={"include": "flyer/"},
    )
    edition = client.fetch_editions(cfg, today=TODAY)[0]
    assert edition.page_images == [
        "https://cdn.test/flyer/page1.jpg",
        "https://cdn.test/flyer/page2.jpg",
    ]
    assert edition.valid_from <= TODAY <= edition.valid_to


def test_image_page_without_images_raises() -> None:
    client, _ = _client([])
    client._get = lambda url, **kw: SimpleNamespace(text="<html>no flyer</html>")  # type: ignore[method-assign]
    cfg = OfficialConfig(slug="t", kind="image_page", source_name="official:t", page_url="https://x")
    with pytest.raises(OfficialError, match="no flyer images"):
        client.fetch_editions(cfg, today=TODAY)


def test_validity_fetch_month() -> None:
    client, _ = _client([])
    cfg = OfficialConfig(
        slug="t", kind="image_page", source_name="official:t", page_url="https://x", validity="fetch_month"
    )
    assert client._validity(cfg, TODAY) == (date(2026, 10, 1), date(2026, 10, 31))
