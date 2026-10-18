"""Metro Digital flyer platform source (metrodigital-apim.azure-api.net).

Metro-group banners (Adonis, Metro QC, Super C, …) render their
flyers through a shared SPA whose public config
(<banner circulaire host>/config/app.json) publishes the API base,
banner id and subscription key — the same public frontend
credentials every visitor's browser uses. They are read from that
config at fetch time, never stored here, so key rotation on the
platform side does not break the source.

Flow per store: GET {api}/flyers/{store_id}/{locale}?date=<today>
lists the store's active publications (title, dates, page count);
GET {api}/pages/{title}/{store_id}/{locale}/ returns every page
with its blocks; blocks hold the products (actionType "Product")
with structured bilingual names, sale/regular/alternate prices,
promo units, SKUs, native categories and page click regions.

The /en/ and /fr/ page payloads are identical (all fields are
bilingual in one response), so one call per publication suffices.

Per-store settings (SPA config URL, platform store id, locale)
live in metrodigital_stores.json next to this module. Approach
cross-checked against the open-source grocery_flyer project
(github.com/Jonathan-Pearce/grocery_flyer), which scrapes the
same platform for these banners.
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import requests

from grocery_meta_search.pipeline.fields import extract_package_size
from grocery_meta_search.sources.base import FlyerEdition, FlyerItem

_CONFIG_PATH = Path(__file__).with_name("metrodigital_stores.json")
_UA = {"User-Agent": "Mozilla/5.0 (compatible; grocery-meta-search/0.1)"}


class MetroDigitalError(Exception):
    """The Metro Digital API could not be read."""


@dataclass(frozen=True)
class MetroDigitalConfig:
    slug: str
    config_url: str  # the banner SPA's public /config/app.json
    store_id: int  # platform store id (one Montreal-area location)
    locale: str = "fr"


@dataclass(frozen=True)
class _AppConfig:
    api_base: str
    api_key: str
    banner_id: str
    api_version: str


def load_metrodigital_configs(
    path: Path | None = None,
) -> dict[str, MetroDigitalConfig]:
    path = path or _CONFIG_PATH
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {
        slug: MetroDigitalConfig(
            slug=slug,
            config_url=str(entry["config_url"]),
            store_id=int(entry["store_id"]),
            locale=str(entry.get("locale", "fr")),
        )
        for slug, entry in data.items()
        if not slug.startswith("_")
    }


def _date_part(value: Any) -> str | None:
    if isinstance(value, str) and len(value) >= 10:
        return value[:10]
    return None


def _price_float(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        m = re.search(r"\d+(?:[.,]\d+)?", value.replace(" ", ""))
        if m:
            return float(m.group(0).replace(",", "."))
    return None


def _promo_unit_raw(product: dict[str, Any]) -> str | None:
    raw = product.get("promoUnitEn") or product.get("promoUnitFr")
    return raw if isinstance(raw, str) and raw.strip() else None


def _unit_of(product: dict[str, Any]) -> str | None:
    """Normalize the printed promo unit to the price_unit vocabulary
    ('lb', 'kg', '100g', 'each'). Pack counts ('6 un.') and tax
    markers ('+TX') are not rate units and return None here."""
    raw = _promo_unit_raw(product)
    if raw is None:
        return None
    unit = raw.strip().lower().lstrip("/").rstrip(".")
    unit = re.sub(r"^(le|la|l['’])\s+", "", unit)
    unit = unit.replace(" ", "")
    if unit in ("lb", "kg", "100g", "g"):
        return unit
    if unit in ("ch", "chaque", "each", "un", "unité", "unite"):
        return "each"
    return None


def _pack_count(product: dict[str, Any]) -> int | None:
    raw = _promo_unit_raw(product)
    if raw is None:
        return None
    m = re.fullmatch(r"(\d{1,3})\s*un\.?", raw.strip().lower())
    return int(m.group(1)) if m else None


_SINGLE_RE = re.compile(
    r"(\d+(?:[.,]\d+)?)\s*(?:\+\s*tx)?\s*(?:l['’]unité|l['’]un\.|la caisse)",
    re.IGNORECASE,
)


def _multibuy_of(
    product: dict[str, Any],
) -> tuple[int, float, float | None] | None:
    """Detect a bundle offer: (count, bundle_total, single_price).

    priceQuantity >= 2 marks the offer and salePrice is the BUNDLE
    total ("2 pour 6$"); the single-item price, when printed, rides
    in alternatePrice or in the promo unit text as an "ou 3,49
    l'unité" / "ou 17,09 +tx la caisse" phrase. Mirrors the Flipp
    multibuy-recovery semantics: the stored price is the printed
    single price when present, else total / count.
    """
    raw_count = product.get("priceQuantity")
    try:
        count = int(str(raw_count).strip())
    except (TypeError, ValueError):
        return None
    if count < 2 or count > 100:
        return None
    total = _price_float(product.get("salePrice"))
    if total is None:
        return None
    single: float | None = None
    for text in (product.get("alternatePrice"), _promo_unit_raw(product)):
        if isinstance(text, str):
            m = _SINGLE_RE.search(text)
            if m:
                single = float(m.group(1).replace(",", "."))
                break
    if single is not None and not (total / count < single <= total):
        single = None
    return count, total, single


def _coord(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, dict):  # {"source": "54.0", "parsedValue": 54}
        parsed = value.get("parsedValue")
        if isinstance(parsed, (int, float)):
            return float(parsed)
    return None


def _bbox_of(product: dict[str, Any], page_number: int) -> dict[str, Any] | None:
    regions = product.get("clickRegions")
    if not isinstance(regions, list) or not regions:
        return None
    region = regions[0]
    if not isinstance(region, dict):
        return None
    vals = {k: _coord(region.get(k)) for k in ("left", "top", "width", "height")}
    if any(v is None for v in vals.values()):
        return None
    # Click regions are percentages of the page; item bboxes are
    # stored normalized to 1000x1000.
    return {
        "x": int(vals["left"] * 10),  # type: ignore[operator]
        "y": int(vals["top"] * 10),  # type: ignore[operator]
        "w": int(vals["width"] * 10),  # type: ignore[operator]
        "h": int(vals["height"] * 10),  # type: ignore[operator]
        "page": page_number,
    }


def products_from_pages(pages: list[Any]) -> list[tuple[int, dict[str, Any]]]:
    """Flatten a pages payload to (page_number, product) pairs.

    Blocks nest their products (a block can hold several products);
    non-product blocks (videos, banners — actionType "Inblock") are
    skipped, and products are deduped by SKU within the flyer.
    """
    found: list[tuple[int, dict[str, Any]]] = []
    seen_skus: set[str] = set()

    def walk(node: Any, page_number: int) -> None:
        if isinstance(node, dict):
            if node.get("actionType") == "Product":
                sku = node.get("sku")
                if isinstance(sku, str) and sku:
                    if sku in seen_skus:
                        return
                    seen_skus.add(sku)
                found.append((page_number, node))
                return
            for value in node.values():
                walk(value, page_number)
        elif isinstance(node, list):
            for value in node:
                walk(value, page_number)

    for page in pages:
        if not isinstance(page, dict):
            continue
        index = page.get("index")
        page_number = int(index) + 1 if isinstance(index, int) else 1
        walk(page.get("blocks"), page_number)
    return found


def item_from_product(
    product: dict[str, Any],
    page_number: int,
    valid_from: str | None,
    valid_to: str | None,
) -> FlyerItem:
    name_fr = (product.get("productFr") or "").strip() or None
    name_en = (product.get("productEn") or "").strip() or None
    if name_en is None:
        # The English product name rides in bodyEn; bodyFr usually
        # carries the size/variant line instead of a name.
        name_en = (product.get("bodyEn") or "").strip() or None
    sale = _price_float(product.get("salePrice"))
    unit = _unit_of(product)
    price_text = None
    if isinstance(product.get("salePrice"), str) and product["salePrice"].strip():
        price_text = product["salePrice"].strip()
        promo = product.get("promoUnitFr") or product.get("promoUnitEn")
        if isinstance(promo, str) and promo.strip():
            price_text = f"{price_text} {promo.strip()}"
    conditions: dict[str, Any] = {}
    multibuy = _multibuy_of(product)
    if multibuy is not None:
        count, total, single = multibuy
        sale = single if single is not None else round(total / count, 2)
        unit = None
        conditions["multibuy"] = {"count": count, "total": total}
        alt = product.get("alternatePrice")
        if price_text is not None and isinstance(alt, str) and alt.strip() and _SINGLE_RE.search(alt):
            price_text = f"{price_text} {alt.strip()}"
    if product.get("alternatePrice"):
        conditions["alternate_price"] = product["alternatePrice"]
    if product.get("regularPrice"):
        conditions["regular_price"] = product["regularPrice"]
    savings = product.get("savingsFr") or product.get("savingsEn")
    if savings:
        conditions["savings"] = savings
    if product.get("mainCategoryEn"):
        conditions["native_category_en"] = product["mainCategoryEn"]
    if product.get("mainCategoryFr"):
        conditions["native_category_fr"] = product["mainCategoryFr"]
    if product.get("subCategoryEn"):
        conditions["native_subcategory_en"] = product["subCategoryEn"]
    if product.get("halal"):
        conditions["halal"] = True
    if product.get("madeInQuebec"):
        conditions["made_in_quebec"] = True
    if product.get("priceQuantity"):
        conditions["price_quantity"] = product["priceQuantity"]
    brand = None
    brands = product.get("productBrands")
    if isinstance(brands, list) and brands and isinstance(brands[0], str):
        brand = brands[0]
    size = extract_package_size(
        product.get("bodyFr") if isinstance(product.get("bodyFr"), str) else None,
        product.get("bodyEn") if isinstance(product.get("bodyEn"), str) else None,
    )
    pack = _pack_count(product)
    if size is None and pack is not None:
        size = f"{pack} un."
    if pack is not None:
        conditions["pack_count"] = pack
    languages = ["fr"] + (["en"] if name_en else [])
    return FlyerItem(
        name_fr=name_fr,
        name_en=name_en,
        price_text=price_text,
        price_value=sale,
        price_unit=unit,
        image_url=(product.get("productImage") or "").strip() or None,
        bbox=_bbox_of(product, page_number),
        sku=(product.get("sku") or "").strip() or None,
        brand=brand,
        package_size=size,
        conditions=conditions,
        valid_from=_date_part(product.get("validFrom")) or valid_from,
        valid_to=_date_part(product.get("validTo")) or valid_to,
        languages=languages,
        raw=product,
        confidence=1.0,
    )


class MetroDigitalClient:
    def __init__(self, session: requests.Session | None = None) -> None:
        self.session = session or requests.Session()

    def _get_json(self, url: str, headers: dict[str, str]) -> Any:
        # The pages payloads are megabyte-sized and the APIM (or the
        # network path to it) occasionally stalls mid-transfer; these
        # are idempotent reads, so retry with backoff before failing.
        last_exc: requests.RequestException | None = None
        for delay in (0, 5, 20):
            if delay:
                time.sleep(delay)
            try:
                resp = self.session.get(url, headers=headers, timeout=120)
                resp.raise_for_status()
                return resp.json()
            except requests.RequestException as exc:
                last_exc = exc
                if isinstance(exc, requests.HTTPError) and exc.response is not None and exc.response.status_code < 500:
                    raise
        assert last_exc is not None
        raise last_exc

    def _app_config(self, cfg: MetroDigitalConfig) -> _AppConfig:
        try:
            data = self._get_json(cfg.config_url, _UA)
        except requests.RequestException as exc:
            raise MetroDigitalError(f"config fetch failed: {exc}") from exc
        api_base = str(data.get("api") or "").rstrip("/")
        api_key = str(data.get("apikey") or "")
        banner_id = str(data.get("banner_id") or "")
        if not api_base or not api_key or not banner_id:
            raise MetroDigitalError(f"incomplete app config at {cfg.config_url}")
        return _AppConfig(
            api_base=api_base,
            api_key=api_key,
            banner_id=banner_id,
            api_version=str(data.get("api_version") or "3.0"),
        )

    def fetch_store_editions(self, cfg: MetroDigitalConfig, today: date | None = None) -> list[FlyerEdition]:
        app = self._app_config(cfg)
        headers = {
            **_UA,
            "Ocp-Apim-Subscription-Key": app.api_key,
            "Banner": app.banner_id,
            "x-api-version": app.api_version,
            "Accept": "application/json",
        }
        day = (today or date.today()).isoformat()
        try:
            listing = self._get_json(
                f"{app.api_base}/flyers/{cfg.store_id}/{cfg.locale}?date={day}",
                headers,
            )
        except requests.RequestException as exc:
            raise MetroDigitalError(f"flyer list failed: {exc}") from exc
        editions: list[FlyerEdition] = []
        for flyer in listing.get("flyers", []):
            title = flyer.get("title")
            if not isinstance(title, str) or not title:
                continue
            valid_from = _date_part(flyer.get("startDate"))
            valid_to = _date_part(flyer.get("endDate"))
            try:
                pages = self._get_json(
                    f"{app.api_base}/pages/{title}/{cfg.store_id}/{cfg.locale}/",
                    headers,
                )
            except requests.RequestException as exc:
                raise MetroDigitalError(f"pages fetch failed for {title}: {exc}") from exc
            if not isinstance(pages, list):
                raise MetroDigitalError(f"pages payload for {title} is not a list")
            items = [
                item_from_product(product, page_number, valid_from, valid_to)
                for page_number, product in products_from_pages(pages)
            ]
            editions.append(
                FlyerEdition(
                    valid_from=valid_from,
                    valid_to=valid_to,
                    source_ref=title,
                    languages=["fr", "en"],
                    raw={
                        "metrodigital": {
                            "flyer_id": flyer.get("flyerId"),
                            "store_id": cfg.store_id,
                            "store_name": flyer.get("storeName"),
                            "page_count": flyer.get("pageCount"),
                        }
                    },
                    items=items,
                )
            )
        return editions
