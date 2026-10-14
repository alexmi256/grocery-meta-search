"""Official-platform flyer sources (Phase 3 group 4).

Stores whose flyer lives on their own site rather than an aggregator:

- ``image_page`` — a web page embedding flyer page images (Wix galleries,
  WordPress pages). Images are OCR'd by the shared pipeline.
- ``pdf_page`` — a page linking a dated PDF flyer (image-wrapped PDFs are
  rendered to page images, then OCR'd).
- ``woo_specials`` — a WooCommerce "promotions" page backed by the public
  Store API (``/wp-json/wc/store/v1/products?on_sale=true``): structured.
- ``flyerify`` — Flyerify-hosted flyers (brand page lists regional offers
  with dates in the title; page images follow a numbered URL pattern).

Per-store configuration lives in ``official_stores.json`` next to this
module. Discovery/extraction helpers are pure functions, unit-tested
against saved HTML fixtures.
"""

from __future__ import annotations

import hashlib
import html as html_lib
import json
import re
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path
from typing import Any
from urllib.parse import quote, unquote, urljoin

import requests

_CONFIG_PATH = Path(__file__).parent / "official_stores.json"
_UA = {"User-Agent": "Mozilla/5.0 (compatible; grocery-meta-search/0.1)"}
_TIMEOUT = 60

FR_MONTHS = {
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
EN_MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


class OfficialError(Exception):
    """Raised when an official source cannot be fetched or parsed."""


@dataclass
class OfficialConfig:
    slug: str
    kind: str  # image_page | pdf_page | woo_specials | flyerify
    source_name: str  # flyer_sources.name, e.g. "official:wix"
    page_url: str
    flyer_type: str = "weekly"
    languages: list[str] = field(default_factory=lambda: ["fr"])
    validity: str = "fetch_week"  # fetch_week | fetch_month | url_month | offer
    extractor: str = "generic"  # wix | generic (image_page only)
    image: dict[str, Any] = field(default_factory=dict)
    ocr: dict[str, Any] = field(default_factory=dict)


@dataclass
class OfficialEdition:
    """A discovered edition: validity + page images (OCR kinds) or items."""

    valid_from: date
    valid_to: date
    flyer_type: str
    source_ref: str
    languages: list[str]
    page_images: list[str] = field(default_factory=list)
    pdf_url: str | None = None
    items: list[Any] = field(default_factory=list)  # FlyerItem, structured kinds


def load_official_configs() -> dict[str, OfficialConfig]:
    data = json.loads(_CONFIG_PATH.read_text(encoding="utf-8"))
    configs: dict[str, OfficialConfig] = {}
    for slug, raw in data.items():
        if slug.startswith("_"):
            continue
        configs[slug] = OfficialConfig(slug=slug, **raw)
    return configs


# ── validity helpers ──────────────────────────────────────────────────


def fetch_week(today: date) -> tuple[date, date]:
    """The Quebec flyer week (Thursday-Wednesday) containing ``today``."""
    delta = (today.weekday() - 3) % 7  # Thursday = weekday 3
    start = today - timedelta(days=delta)
    return start, start + timedelta(days=6)


def month_bounds(year: int, month: int) -> tuple[date, date]:
    first = date(year, month, 1)
    nxt = date(year + 1, 1, 1) if month == 12 else date(year, month + 1, 1)
    return first, nxt - timedelta(days=1)


def _strip_accents(text: str) -> str:
    import unicodedata

    return "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))


def url_month(url: str) -> tuple[date, date] | None:
    """Validity month from a URL: /uploads/2026/10/ or a FR month name."""
    m = re.search(r"/(20\d{2})/(0[1-9]|1[0-2])(?:/|$)", url)
    if m:
        return month_bounds(int(m.group(1)), int(m.group(2)))
    low = _strip_accents(url.lower())
    for name, num in FR_MONTHS.items():
        m = re.search(rf"{name}[-_ ]?(20)?(\d{{2}})", low)
        if m:
            return month_bounds(2000 + int(m.group(2)), num)
    return None


# ── image extraction ──────────────────────────────────────────────────


def extract_wix_image_urls(page_html: str, min_w: int = 600, min_h: int = 900) -> list[str]:
    """Original URLs of large Wix images, in page order.

    Wix serves one media file at many sizes; the HTML carries sized
    variants (``/v1/fill/w_…,h_…/``). We keep, per media id, the largest
    declared variant and filter on it; the bare media URL serves the
    original upload.
    """
    from urllib.parse import unquote

    dims: dict[str, tuple[int, int]] = {}
    order: list[str] = []
    pattern = (
        r"static\.wixstatic\.com/media/([0-9a-zA-Z_%.~-]+?)/v1/[^\"'\s]*?"
        r"[wW]_(%?\d+)[^\"'\s]*?[hH]_(%?\d+)"
    )
    for m in re.finditer(pattern, page_html):
        media_id = unquote(m.group(1))
        wh = (int(m.group(2).replace("%", "")), int(m.group(3).replace("%", "")))
        if media_id not in dims:
            order.append(media_id)
            dims[media_id] = wh
        else:
            dims[media_id] = max(dims[media_id], wh)
    urls = []
    for media_id in order:
        w, h = dims[media_id]
        if w >= min_w and h >= min_h:
            urls.append(f"https://static.wixstatic.com/media/{media_id}")
    return urls


_IMG_URL_RE = re.compile(r"https?://[^\s\"'<>]+?\.(?:jpe?g|png|webp)(?:\?[^\s\"'<>]*)?")
_WP_SIZED_RE = re.compile(r"-\d{2,4}x\d{2,4}\.(?:jpe?g|png|webp)$", re.IGNORECASE)


def extract_image_urls(
    page_html: str,
    include: str | None = None,
    exclude: str | None = None,
    latest_upload_month: bool = False,
) -> list[str]:
    """Image URLs from a page, unwrapped (Jetpack i0.wp.com) and filtered."""
    urls: list[str] = []
    seen: set[str] = set()
    for m in _IMG_URL_RE.finditer(page_html):
        url = html_lib.unescape(m.group(0))
        url = re.sub(r"^https?://i\d\.wp\.com/", "https://", url)
        url = url.split("?")[0]
        if _WP_SIZED_RE.search(url):  # WordPress thumbnail variant
            continue
        if include and not re.search(include, url, re.IGNORECASE):
            continue
        if exclude and re.search(exclude, url, re.IGNORECASE):
            continue
        if url not in seen:
            seen.add(url)
            urls.append(url)
    if latest_upload_month:
        dated: list[tuple[str, str, str]] = []
        for u in urls:
            dm = re.search(r"/uploads/(20\d{2})/(\d{2})/", u)
            if dm:
                dated.append((dm.group(1), dm.group(2), u))
        if dated:
            newest = max((y, mo) for y, mo, _ in dated)
            urls = [u for y, mo, u in dated if (y, mo) == newest]
    return urls


def images_source_ref(page_url: str, image_urls: list[str]) -> str:
    digest = hashlib.sha1("\n".join([page_url, *image_urls]).encode()).hexdigest()
    return f"img-{digest[:16]}"


# ── Flyerify ──────────────────────────────────────────────────────────

_OFFER_LINK_RE = re.compile(
    r'href="(https://[a-z0-9-]+\.flyerify\.com/([a-z0-9-]+))"\s+title="([^"]+)"'
)
_RANGE_RE = re.compile(
    r"([A-Za-z]+)\s+(\d{1,2})\s+to\s+(?:([A-Za-z]+)\s+)?(\d{1,2})", re.IGNORECASE
)


def parse_offer_range(title: str, today: date) -> tuple[date, date] | None:
    """'Wholesale Club (QC) Flyer October 8 to 14' → (Oct 8, Oct 14)."""
    m = _RANGE_RE.search(title)
    if not m:
        return None
    mon1 = EN_MONTHS.get(m.group(1).lower())
    mon2 = EN_MONTHS.get(m.group(3).lower()) if m.group(3) else mon1
    if mon1 is None or mon2 is None:
        return None
    d1, d2 = int(m.group(2)), int(m.group(4))
    wrap = 1 if mon2 < mon1 else 0
    year = today.year
    start, end = date(year, mon1, d1), date(year + wrap, mon2, d2)
    if end < today - timedelta(days=21):
        start, end = date(year + 1, mon1, d1), date(year + 1 + wrap, mon2, d2)
    elif start > today + timedelta(days=21):
        start, end = date(year - 1, mon1, d1), date(year - 1 + wrap, mon2, d2)
    return start, end


def flyerify_current_offer(
    brand_html: str, region: str, today: date
) -> tuple[str, str, date, date] | None:
    """(offer_url, offer_slug, valid_from, valid_to) for the current offer."""
    best: tuple[str, str, date, date] | None = None
    for m in _OFFER_LINK_RE.finditer(brand_html):
        url, slug, title = m.group(1), m.group(2), html_lib.unescape(m.group(3))
        if f"({region})" not in title:
            continue
        rng = parse_offer_range(title, today)
        if rng is None:
            continue
        start, end = rng
        if end < today:  # past edition
            continue
        if best is None or start > best[2]:
            best = (url, slug, start, end)
    return best


def flyerify_page_count(offer_html: str) -> int:
    pages = [int(n) for n in re.findall(r'aria-label="Goto page (\d+)"', offer_html)]
    return max(pages) if pages else 1


def flyerify_offer_id(offer_html: str, offer_slug: str) -> str | None:
    m = re.search(rf"images/offers/(\d+)/{re.escape(offer_slug)}-", offer_html)
    return m.group(1) if m else None


def flyerify_image_url(offer_id: str, offer_slug: str, page: int) -> str:
    return f"https://flyerify.com/images/offers/{offer_id}/{offer_slug}-{page}-max.jpg"


# ── WooCommerce Store API (specials) ──────────────────────────────────


def woo_product_to_item(prod: dict[str, Any]) -> Any:
    """Map one Store API product to a FlyerItem (structured)."""
    from .base import FlyerItem

    prices = prod.get("prices") or {}
    minor = int(prices.get("currency_minor_unit", 2))

    def money(raw: Any) -> float | None:
        try:
            value: float = round(int(raw) / (10**minor), 2)
        except (TypeError, ValueError):
            return None
        return value

    price = money(prices.get("price"))
    regular = money(prices.get("regular_price"))
    name = re.sub(r"<[^>]+>", "", str(prod.get("name") or "")).strip()
    images = prod.get("images") or []
    conditions: dict[str, Any] = {}
    if regular is not None and price is not None and regular > price:
        conditions["regular_price"] = regular
    return FlyerItem(
        name_fr=name or None,
        price_text=f"{price:.2f}" if price is not None else None,
        price_value=price,
        image_url=images[0]["src"] if images else None,
        sku=str(prod["sku"]) if prod.get("sku") else None,
        conditions=conditions,
        languages=["fr"],
        raw={"woo_id": prod.get("id"), "permalink": prod.get("permalink")},
    )


# ── client ────────────────────────────────────────────────────────────


class OfficialClient:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update(_UA)

    def _get(self, url: str, timeout: int = _TIMEOUT, retries: int = 0) -> requests.Response:
        last_exc: requests.RequestException | None = None
        for _ in range(retries + 1):
            try:
                resp = self.session.get(url, timeout=timeout)
                resp.raise_for_status()
                return resp
            except requests.RequestException as exc:
                last_exc = exc
        raise OfficialError(f"GET {url}: {last_exc}")

    def fetch_editions(
        self, cfg: OfficialConfig, today: date | None = None
    ) -> list[OfficialEdition]:
        today = today or date.today()
        if cfg.kind == "image_page":
            return [self._image_page(cfg, today)]
        if cfg.kind == "pdf_page":
            return [self._pdf_page(cfg, today)]
        if cfg.kind == "flyerify":
            return [self._flyerify(cfg, today)]
        if cfg.kind == "circulaires":
            return [self._circulaires(cfg, today)]
        if cfg.kind == "flyerbox":
            return [self._flyerbox(cfg, today)]
        if cfg.kind == "woo_specials":
            return [self._woo_specials(cfg, today)]
        raise OfficialError(f"unknown kind {cfg.kind!r}")

    def _validity(self, cfg: OfficialConfig, today: date) -> tuple[date, date]:
        if cfg.validity == "fetch_month":
            return month_bounds(today.year, today.month)
        return fetch_week(today)

    def _image_page(self, cfg: OfficialConfig, today: date) -> OfficialEdition:
        page_html = self._get(cfg.page_url).text
        if cfg.extractor == "wix":
            urls = extract_wix_image_urls(
                page_html,
                min_w=int(cfg.image.get("min_w", 600)),
                min_h=int(cfg.image.get("min_h", 900)),
            )
        else:
            urls = extract_image_urls(
                page_html,
                include=cfg.image.get("include"),
                exclude=cfg.image.get("exclude"),
                latest_upload_month=bool(cfg.image.get("latest_upload_month")),
            )
        if not urls:
            raise OfficialError(f"no flyer images found at {cfg.page_url}")
        valid_from, valid_to = self._validity(cfg, today)
        if cfg.validity == "url_month":
            for u in urls:
                bounds = url_month(u)
                if bounds is not None:
                    valid_from, valid_to = bounds
                    break
        return OfficialEdition(
            valid_from=valid_from,
            valid_to=valid_to,
            flyer_type=cfg.flyer_type,
            source_ref=images_source_ref(cfg.page_url, urls),
            languages=cfg.languages,
            page_images=urls,
        )

    def _pdf_page(self, cfg: OfficialConfig, today: date) -> OfficialEdition:
        page_html = self._get(cfg.page_url).text
        pdfs = sorted(
            {
                html_lib.unescape(m.group(1))
                for m in re.finditer(r'href="([^"]+\.pdf)"', page_html, re.IGNORECASE)
            }
        )
        if not pdfs:
            raise OfficialError(f"no PDF links at {cfg.page_url}")
        pdf_url = pdfs[-1]  # dated filenames sort chronologically
        # Mayrand names its PDF with the printed range ("Circulaire du 14
        # au 20 octobre 2026 ... .pdf") — that beats the URL-month guess.
        parsed = parse_fr_validity(unquote(pdf_url), today)
        bounds = parsed or url_month(pdf_url) or self._validity(cfg, today)
        return OfficialEdition(
            valid_from=bounds[0],
            valid_to=bounds[1],
            flyer_type=cfg.flyer_type,
            source_ref=pdf_url,
            languages=cfg.languages,
            pdf_url=pdf_url,
        )

    def _flyerify(self, cfg: OfficialConfig, today: date) -> OfficialEdition:
        brand_html = self._get(cfg.page_url).text
        region = str(cfg.image.get("region", "QC"))
        offer = flyerify_current_offer(brand_html, region, today)
        if offer is None:
            raise OfficialError(f"no current {region} offer at {cfg.page_url}")
        offer_url, slug, valid_from, valid_to = offer
        offer_html = self._get(offer_url).text
        offer_id = flyerify_offer_id(offer_html, slug)
        if offer_id is None:
            raise OfficialError(f"offer id not found at {offer_url}")
        count = flyerify_page_count(offer_html)
        urls = [flyerify_image_url(offer_id, slug, n) for n in range(1, count + 1)]
        return OfficialEdition(
            valid_from=valid_from,
            valid_to=valid_to,
            flyer_type=cfg.flyer_type,
            source_ref=slug,
            languages=cfg.languages,
            page_images=urls,
        )

    def _circulaires(self, cfg: OfficialConfig, today: date) -> OfficialEdition:
        """circulaires.com legacy viewer (flyers.do, plain HTTP only — the
        HTTPS endpoint drops connections). The landing page prints the
        validity range and the first page image; the remaining pages sit
        in the same directory with sloppy hand-uploaded names, so probe
        the plausible patterns and dedupe by content hash."""
        page_html = self._get(cfg.page_url).text
        parsed = parse_flyers_do(page_html)
        if parsed is None:
            raise OfficialError(f"flyers.do page not recognized at {cfg.page_url}")
        valid_from, valid_to, first_src = parsed
        base = urljoin(cfg.page_url, first_src)
        directory = base.rsplit("/", 1)[0]
        urls: list[str] = []
        seen_hashes: set[str] = set()
        for n in range(1, 13):
            for name in (f"s{n}.jpg", f"b{n}.jpg", f"s{n:02d}.jpg", f"b{n:02d}.jpg"):
                url = f"{directory}/{name}"
                if url == base:
                    candidate = base
                else:
                    try:
                        resp = self._get(url)
                    except OfficialError:
                        continue
                    candidate = url
                    digest = hashlib.sha1(resp.content).hexdigest()
                    if digest in seen_hashes:
                        continue
                    seen_hashes.add(digest)
                if candidate not in urls:
                    urls.append(candidate)
        if not urls:
            raise OfficialError(f"no viewer pages found for {cfg.page_url}")
        return OfficialEdition(
            valid_from=valid_from,
            valid_to=valid_to,
            flyer_type=cfg.flyer_type,
            source_ref=f"circ-{directory.rsplit('/', 1)[-1]}-{valid_from.isoformat()}",
            languages=cfg.languages,
            page_images=urls,
        )

    def _flyerbox(self, cfg: OfficialConfig, today: date) -> OfficialEdition:
        """flyerbox.ca (Leaflets platform): the store listing links the
        current flyer; the flyer page carries maxPages + printed validity;
        each page's signed CDN image URL is served by an AJAX fragment
        endpoint (page=k returns image k-1; page 0 is in the flyer HTML)."""
        listing_html = self._get(cfg.page_url).text
        pattern = str(cfg.image.get("flyer_link_pattern", "flyer"))
        hrefs = re.findall(r'href="([^"]+)"', listing_html)
        flyer_path = next((h for h in hrefs if pattern in h), None)
        if flyer_path is None:
            raise OfficialError(f"no flyer link matching {pattern!r} at {cfg.page_url}")
        flyer_url = urljoin(cfg.page_url, flyer_path)
        flyer_html = self._get(flyer_url).text
        meta = flyerbox_meta(flyer_html)
        if meta is None:
            raise OfficialError(f"flyer page metadata not found at {flyer_url}")
        brochure_id, max_pages, valid_from, valid_to = meta
        urls: list[str] = []
        first = flyerbox_fragment_image(flyer_html)
        if first:
            urls.append(first)
        origin = re.match(r"https?://[^/]+", flyer_url)
        base = origin.group(0) if origin else "https://www.flyerbox.ca"
        for k in range(2, max_pages + 1):
            frag_url = (
                f"{base}/brochure/brochure-page/?brochureId={brochure_id}"
                f"&page={k}&current_url={quote(flyer_url, safe='')}"
                f"&hasElevatedAccess=0"
            )
            frag = self.session.get(
                frag_url,
                timeout=60,
                headers={"X-Requested-With": "XMLHttpRequest"},
            )
            frag.raise_for_status()
            img = flyerbox_fragment_image(frag.text)
            if img and img not in urls:
                urls.append(img)
        if not urls:
            raise OfficialError(f"no flyerbox page images at {flyer_url}")
        return OfficialEdition(
            valid_from=valid_from,
            valid_to=valid_to,
            flyer_type=cfg.flyer_type,
            source_ref=f"flyerbox-{brochure_id}",
            languages=cfg.languages,
            page_images=urls,
        )

    def _woo_specials(self, cfg: OfficialConfig, today: date) -> OfficialEdition:
        base = cfg.page_url.rstrip("/")
        items: list[Any] = []
        page = 1
        while True:
            # marchekorea.com sits behind Cloudflare bot management whose
            # __cf_bm cookie makes follow-up requests hang; go cookieless.
            self.session.cookies.clear()
            resp = self._get(
                f"{base}/wp-json/wc/store/v1/products?on_sale=true&per_page=25&page={page}",
                timeout=120,
                retries=1,
            )
            products = resp.json()
            if not isinstance(products, list) or not products:
                break
            items.extend(woo_product_to_item(p) for p in products)
            if len(products) < 25:
                break
            page += 1
        valid_from, valid_to = self._validity(cfg, today)
        for item in items:
            item.valid_from = valid_from.isoformat()
            item.valid_to = valid_to.isoformat()
        return OfficialEdition(
            valid_from=valid_from,
            valid_to=valid_to,
            flyer_type=cfg.flyer_type,
            source_ref=f"specials-{valid_from.isoformat()}",
            languages=cfg.languages,
            items=items,
        )


_FLYERS_DO_DATE = re.compile(r"Du\s+(\d{1,2})-(\d{1,2})-(\d{4})\s+au\s+(\d{1,2})-(\d{1,2})-(\d{4})")
_FLYERS_DO_IMG = re.compile(r'src="((?:marche|magasin)-[\w-]+/\d+/[\w.]+\.jpg)"')


def parse_flyers_do(page_html: str) -> tuple[date, date, str] | None:
    """Parse a circulaires.com flyers.do viewer page: the printed range
    ("Du 8-10-2026 au 14-10-2026") and the first page image path."""
    m = _FLYERS_DO_DATE.search(page_html)
    img = _FLYERS_DO_IMG.search(page_html)
    if not m or not img:
        return None
    valid_from = date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
    valid_to = date(int(m.group(6)), int(m.group(5)), int(m.group(4)))
    return valid_from, valid_to, img.group(1)


_FLYERBOX_ID = re.compile(r"pageBrochureId\s*=\s*(\d+)")
_FLYERBOX_PAGES = re.compile(r"maxPages\s*=\s*(\d+)")
_FLYERBOX_VALID = re.compile(r"valid (\w{3,9}) (\d{1,2}), (\d{4}) - (\w{3,9}) (\d{1,2}), (\d{4})")
_FLYERBOX_IMG = re.compile(
    r"https://na\.leafletscdn\.com/thumbor/[^\"']+?/ca/data/\d+/\d+/\d+\.jpg(?:\?t=\d+)?"
)
_EN_MONTHS = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}


def flyerbox_meta(page_html: str) -> tuple[int, int, date, date] | None:
    """Extract (brochure id, page count, valid_from, valid_to) from a
    flyerbox flyer page ("valid Oct 12, 2026 - Oct 25, 2026")."""
    bid = _FLYERBOX_ID.search(page_html)
    pages = _FLYERBOX_PAGES.search(page_html)
    valid = _FLYERBOX_VALID.search(page_html)
    if not bid or not pages or not valid:
        return None
    mon1 = _EN_MONTHS.get(valid.group(1)[:3].lower())
    mon2 = _EN_MONTHS.get(valid.group(4)[:3].lower())
    if not mon1 or not mon2:
        return None
    return (
        int(bid.group(1)),
        int(pages.group(1)),
        date(int(valid.group(3)), mon1, int(valid.group(2))),
        date(int(valid.group(6)), mon2, int(valid.group(5))),
    )


def flyerbox_fragment_image(fragment_html: str) -> str | None:
    """The signed leafletscdn page-image URL inside a flyerbox page or
    brochure-page fragment."""
    m = _FLYERBOX_IMG.search(fragment_html)
    return m.group(0) if m else None


def render_pdf_pages(pdf_bytes: bytes, dpi: int = 200) -> list[Any]:
    """Render an image-wrapped PDF to PIL images (one per page)."""
    import io

    import pymupdf
    from PIL import Image

    doc: Any = pymupdf.open(  # type: ignore[no-untyped-call]
        stream=pdf_bytes, filetype="pdf"
    )
    images = []
    for page in doc:
        pix = page.get_pixmap(dpi=dpi)
        images.append(Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB"))
    return images


# ── French validity ranges printed on flyers ─────────────────────────

_FR_RANGE_SAME_MONTH = re.compile(
    r"(\d{1,2})\s*(?:er)?\s*au\s*(\d{1,2})\s*([a-z]+)\s*(\d{4})", re.IGNORECASE
)
_FR_RANGE_TWO_MONTHS = re.compile(
    r"(\d{1,2})\s*(?:er)?\s*([a-z]+)\s*au\s*(\d{1,2})\s*([a-z]+)\s*(\d{4})",
    re.IGNORECASE,
)
_FR_RANGE_NO_YEAR = re.compile(
    r"(\d{1,2})\s*(?:er)?\s+au\s+(\d{1,2})\s+([a-z]+)(?!\s+\d)", re.IGNORECASE
)


def parse_fr_validity(text: str, today: date) -> tuple[date, date] | None:
    """Parse a French date range printed on a flyer ("VALIDE DU 08 AU 21
    OCTOBRE 2026", "du 30 septembre au 5 octobre 2026"). OCR often drops
    the spaces in caps text, so ranges are also tried fully squashed."""
    flat = _strip_accents(text).lower()
    squashed = flat.replace(" ", "")
    m = _FR_RANGE_TWO_MONTHS.search(flat) or _FR_RANGE_TWO_MONTHS.search(squashed)
    if m:
        mon1 = FR_MONTHS.get(m.group(2))
        mon2 = FR_MONTHS.get(m.group(4))
        if mon1 and mon2:
            year = int(m.group(5))
            return date(year, mon1, int(m.group(1))), date(year, mon2, int(m.group(3)))
    m = _FR_RANGE_SAME_MONTH.search(flat) or _FR_RANGE_SAME_MONTH.search(squashed)
    if m:
        mon = FR_MONTHS.get(m.group(3))
        if mon:
            year = int(m.group(4))
            return date(year, mon, int(m.group(1))), date(year, mon, int(m.group(2)))
    m = _FR_RANGE_NO_YEAR.search(flat)
    if m:
        mon = FR_MONTHS.get(m.group(3))
        if mon:
            start = date(today.year, mon, int(m.group(1)))
            end = date(today.year, mon, int(m.group(2)))
            if end < today - timedelta(days=30):
                start = date(today.year + 1, mon, int(m.group(1)))
                end = date(today.year + 1, mon, int(m.group(2)))
            return start, end
    return None
