"""circulaires.club client tests: sitemap discovery window,
dedupe/sort, page-image filling and error mapping — fake session."""

from __future__ import annotations

from datetime import date

import pytest
import requests

from grocery_meta_search.sources.circulaires_club import (
    CCEdition,
    CirculairesClubClient,
    CirculairesClubError,
    parse_edition_url,
)

TODAY = date(2026, 10, 18)
REF_CURRENT = "circulaire-marche-test-du-15-au-21-octobre-2026"
REF_NEXT = "circulaire-marche-test-du-22-au-28-octobre-2026"
SITEMAP = f"""<?xml version="1.0"?>
<urlset>
  <url><loc>https://circulaires.club/circulaire/{REF_CURRENT}/</loc></url>
  <url><loc>https://circulaires.club/circulaire/{REF_CURRENT}/</loc></url>
  <url><loc>https://circulaires.club/circulaire/{REF_NEXT}/</loc></url>
  <url><loc>https://circulaires.club/circulaire/circulaire-marche-test-du-1-au-7-octobre-2026/</loc></url>
  <url><loc>https://circulaires.club/circulaire/circulaire-marche-test-du-5-au-11-novembre-2026/</loc></url>
  <url><loc>https://circulaires.club/circulaire/circulaire-autre-du-15-au-21-octobre-2026/</loc></url>
  <url><loc>https://circulaires.club/categorie/alimentation/</loc></url>
</urlset>"""
PAGE_HTML = f"""
<img src="/images/{REF_CURRENT}/w/2.webp">
<img src="/images/{REF_CURRENT}/w/1.webp">
<img src="/images/{REF_CURRENT}/w/10.webp">
<img src="/images/circulaire-autre-du-15-au-21-octobre-2026/w/1.webp">
"""


class FakeResponse:
    def __init__(self, text: str = "", fail: bool = False) -> None:
        self.text = text
        self._fail = fail

    def raise_for_status(self) -> None:
        if self._fail:
            raise requests.HTTPError("HTTP 500")


class FakeSession:
    def __init__(self, routes: dict[str, FakeResponse]) -> None:
        self.routes = routes
        self.headers: dict[str, str] = {}
        self.calls: list[str] = []

    def get(self, url: str, timeout: int = 0) -> FakeResponse:
        self.calls.append(url)
        for fragment, resp in self.routes.items():
            if fragment in url:
                return resp
        raise AssertionError(f"unrouted {url}")


def _client(session: FakeSession) -> CirculairesClubClient:
    return CirculairesClubClient(session=session)  # type: ignore[arg-type]


def test_editions_for_window_dedupe_and_sort() -> None:
    session = FakeSession({"sitemap": FakeResponse(SITEMAP)})
    client = _client(session)
    editions = client.editions_for(["marche-test"], TODAY)
    # Expired, far-future, other-store and duplicate entries are out;
    # the next cycle (starts within the 7-day lookahead) is in.
    assert [e.edition_ref for e in editions] == [REF_CURRENT, REF_NEXT]
    assert editions[0].valid_from == date(2026, 10, 15)
    # The sitemap is fetched once and cached.
    client.editions_for(["marche-test"], TODAY)
    assert sum(1 for u in session.calls if "sitemap" in u) == 1


def test_fetch_current_editions_fills_images() -> None:
    session = FakeSession(
        {"sitemap": FakeResponse(SITEMAP), REF_CURRENT: FakeResponse(PAGE_HTML), REF_NEXT: FakeResponse("")}
    )
    client = _client(session)
    editions = client.fetch_current_editions(["marche-test"], today=TODAY)
    # The next edition's page carries no images yet -> dropped.
    assert [e.edition_ref for e in editions] == [REF_CURRENT]
    assert editions[0].page_images == [
        f"https://circulaires.club/images/{REF_CURRENT}/01.webp",
        f"https://circulaires.club/images/{REF_CURRENT}/02.webp",
        f"https://circulaires.club/images/{REF_CURRENT}/10.webp",
    ]


def test_get_text_http_error_maps_to_client_error() -> None:
    session = FakeSession({"sitemap": FakeResponse(fail=True)})
    client = _client(session)
    with pytest.raises(CirculairesClubError, match="failed"):
        client.list_edition_urls()


def test_edition_properties() -> None:
    weekly = CCEdition("s", "r", date(2026, 10, 15), date(2026, 10, 21))
    monthly = CCEdition("s", "r", date(2026, 10, 1), date(2026, 10, 31))
    assert weekly.flyer_type == "weekly" and monthly.flyer_type == "monthly"
    assert weekly.page_url == "https://circulaires.club/circulaire/r/"


def test_parse_invalid_date_and_month() -> None:
    assert parse_edition_url("https://circulaires.club/circulaire/circulaire-x-du-31-au-31-fevrier-2026/") is None
    assert parse_edition_url("https://circulaires.club/circulaire/circulaire-x-du-1-au-7-smarch-2026/") is None
