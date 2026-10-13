"""circulaires.club discovery client.

The site is a static Astro build. All flyer editions are listed in
``sitemap-0.xml`` with dated URLs of the form::

    /circulaire/circulaire-{slug}-du-{d}[-{month}]-au-{d}-{month}-{year}/

Each edition page embeds page images at
``/images/{edition}/w/{NN}.webp`` (900px) — the same path without the
``/w/`` segment serves the full-resolution page (1600px), which is what
the OCR pipeline consumes.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from datetime import date, timedelta

import requests

BASE_URL = "https://circulaires.club"
SITEMAP_URL = f"{BASE_URL}/sitemap-0.xml"
USER_AGENT = "Mozilla/5.0 (compatible; grocery-meta-search/0.1)"
TIMEOUT = 30

_FR_MONTHS = {
    "janvier": 1,
    "fevrier": 2,
    "mars": 3,
    "avril": 4,
    "mai": 5,
    "juin": 6,
    "juillet": 7,
    "aout": 8,
    "septembre": 9,
    "octobre": 10,
    "novembre": 11,
    "decembre": 12,
}

_EDITION_RE = re.compile(
    r"/circulaire/(circulaire-(?P<slug>[a-z0-9-]+?)-du-(?P<d1>\d{1,2})"
    r"(?:-(?P<m1>[a-z]+))?-au-(?P<d2>\d{1,2})-(?P<m2>[a-z]+)-(?P<y>\d{4}))/?$"
)
_PAGE_IMG_RE = re.compile(r"/images/([a-z0-9-]+)/w/(\d+)\.webp")


class CirculairesClubError(RuntimeError):
    """Raised when circulaires.club cannot be read."""


def _strip_accents(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))


def parse_edition_url(url: str) -> tuple[str, date, date] | None:
    """Parse a circulaire edition URL into (cc_slug, valid_from, valid_to)."""
    m = _EDITION_RE.search(url)
    if not m:
        return None
    month2 = _FR_MONTHS.get(_strip_accents(m.group("m2")))
    if month2 is None:
        return None
    month1 = month2
    if m.group("m1"):
        month1 = _FR_MONTHS.get(_strip_accents(m.group("m1")), month2)
    year = int(m.group("y"))
    year1 = year if (month1, int(m.group("d1"))) <= (month2, int(m.group("d2"))) else year - 1
    try:
        start = date(year1, month1, int(m.group("d1")))
        end = date(year, month2, int(m.group("d2")))
    except ValueError:
        return None
    return m.group("slug"), start, end


@dataclass
class CCEdition:
    """One circulaires.club flyer edition."""

    cc_slug: str
    edition_ref: str  # e.g. circulaire-marche-bonichoix-du-8-au-14-octobre-2026
    valid_from: date
    valid_to: date
    page_images: list[str] = field(default_factory=list)  # full-res URLs, in order

    @property
    def flyer_type(self) -> str:
        span = (self.valid_to - self.valid_from).days
        return "monthly" if span > 14 else "weekly"

    @property
    def page_url(self) -> str:
        return f"{BASE_URL}/circulaire/{self.edition_ref}/"


class CirculairesClubClient:
    def __init__(self, session: requests.Session | None = None) -> None:
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        self._sitemap_cache: list[str] | None = None

    def _get_text(self, url: str) -> str:
        try:
            resp = self.session.get(url, timeout=TIMEOUT)
            resp.raise_for_status()
        except requests.RequestException as exc:
            raise CirculairesClubError(f"GET {url} failed: {exc}") from exc
        return resp.text

    def list_edition_urls(self) -> list[str]:
        """All edition page URLs from the sitemap (cached per client)."""
        if self._sitemap_cache is None:
            xml = self._get_text(SITEMAP_URL)
            self._sitemap_cache = re.findall(
                r"<loc>(https://circulaires\.club/circulaire/[^<]+)</loc>", xml
            )
        return self._sitemap_cache

    def editions_for(
        self, cc_slugs: list[str], today: date, lookahead_days: int = 7
    ) -> list[CCEdition]:
        """Editions for the given cc slugs that are current or start soon.

        An edition qualifies when it has not ended before ``today`` and it
        starts no later than ``today + lookahead_days`` (next week's flyer
        is often published a few days early).
        """
        wanted = set(cc_slugs)
        found: list[CCEdition] = []
        seen: set[str] = set()
        for url in self.list_edition_urls():
            parsed = parse_edition_url(url)
            if parsed is None:
                continue
            slug, start, end = parsed
            if slug not in wanted or end < today or start > today + timedelta(days=lookahead_days):
                continue
            ref = url.rstrip("/").rsplit("/", 1)[-1]
            if ref in seen:
                continue
            seen.add(ref)
            found.append(CCEdition(cc_slug=slug, edition_ref=ref, valid_from=start, valid_to=end))
        found.sort(key=lambda e: (e.valid_from, e.cc_slug))
        return found

    def fill_page_images(self, edition: CCEdition) -> CCEdition:
        """Fetch the edition page and record full-resolution page image URLs."""
        html = self._get_text(edition.page_url)
        pages: dict[int, str] = {}
        for ref, num in _PAGE_IMG_RE.findall(html):
            if ref == edition.edition_ref:
                pages[int(num)] = f"{BASE_URL}/images/{ref}/{int(num):02d}.webp"
        edition.page_images = [pages[n] for n in sorted(pages)]
        return edition

    def fetch_current_editions(
        self, cc_slugs: list[str], today: date | None = None
    ) -> list[CCEdition]:
        today = today or date.today()
        editions = [self.fill_page_images(e) for e in self.editions_for(cc_slugs, today)]
        return [e for e in editions if e.page_images]
