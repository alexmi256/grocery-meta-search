"""Flipp FlyerKit API client — structured JSON flyer products over plain HTTPS.

Endpoint reference (verified live 2026-10-12):
  GET /flyerkit/publications/{brand_slug}?locale=..&languages[]=..&access_token=..&store_code=..
  GET /flyerkit/publication/{id}/products?display_type=all&locale=..&access_token=..

Per-brand access tokens are public static strings (published in the
open-source grocery_flyer scraper); they can be rotated by Flipp at any time.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from typing import Any

import requests

from ..prices import parse_price_text
from .base import FlyerEdition, FlyerItem

BASE_URL = "https://dam.flippenterprise.net/flyerkit"
TIMEOUT = 30
USER_AGENT = "grocery-meta-search/0.1 (research project)"


def _as_dict_list(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    return []


class FlyerKitError(RuntimeError):
    """Raised when the FlyerKit API misbehaves."""


@dataclass
class BrandConfig:
    store_slug: str
    brand_slug: str
    access_token: str
    store_code: str


def _to_date(value: Any) -> str | None:
    """ISO timestamp (with tz offset) -> 'YYYY-MM-DD'. Passes through date strings."""
    if not value or not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value).date().isoformat()
    except ValueError:
        return value[:10] if len(value) >= 10 else None


def _bbox_of(product: dict[str, Any]) -> dict[str, Any] | None:
    bbox = {
        k: product[k]
        for k in ("left", "top", "right", "bottom", "page")
        if product.get(k) is not None
    }
    return bbox or None


def _conditions_of(product: dict[str, Any]) -> dict[str, Any]:
    conditions: dict[str, Any] = {}
    for key in ("disclaimer_text", "sale_story", "description"):
        value = product.get(key)
        if value:
            conditions[key] = value
    if product.get("in_store_only"):
        conditions["in_store_only"] = True
    return conditions


_MEMBER_RE = re.compile(r"\bmembres?\b|\bmembers?\b", re.IGNORECASE)
_PROGRAM_RES = [
    (re.compile(r"pc\s*optimum", re.IGNORECASE), "PC Optimum"),
    (re.compile(r"sc[eè]ne\s*\+", re.IGNORECASE), "Scène+"),
    (
        re.compile(
            r"prix[^.]{0,30}\bmoi\b|\bcarte\s+moi\b|\bprogramme\s+moi\b",
            re.IGNORECASE,
        ),
        "Moi",
    ),
]

# Banner slug -> loyalty program backing its "membre" prices.
BANNER_PROGRAMS = {
    "maxi": "PC Optimum",
    "provigo": "PC Optimum",
    "loblaws": "PC Optimum",
    "igaquebec": "Scène+",
}

# Fields carrying price conditions. The product NAME is excluded: a name like
# "... - IGA Scene+" marks a points offer, not necessarily a gated price.
_PRICE_TEXT_FIELDS = (
    "sale_story",
    "pre_price_text",
    "post_price_text",
    "disclaimer_text",
    "description",
)


def _price_text_blob(product: dict[str, Any]) -> str:
    return " ".join(str(product.get(k) or "") for k in _PRICE_TEXT_FIELDS)


def loyalty_program_of(product: dict[str, Any], default: str | None = None) -> str | None:
    """Name the loyalty program gating this item's price, if identifiable."""
    text = _price_text_blob(product) + " " + str(product.get("name") or "")
    for pattern, program in _PROGRAM_RES:
        if pattern.search(text):
            return program
    return default


def _is_loyalty_gated(product: dict[str, Any]) -> bool:
    return bool(_MEMBER_RE.search(_price_text_blob(product)))


def edition_from_publication(pub: dict[str, Any]) -> FlyerEdition:
    return FlyerEdition(
        valid_from=_to_date(pub.get("valid_from")),
        valid_to=_to_date(pub.get("valid_to")),
        flyer_type=str(pub.get("flyer_type") or "weekly"),
        raw=pub,
    )


def item_from_product(
    product: dict[str, Any], locale: str, default_program: str | None = None
) -> FlyerItem:
    name = (product.get("name") or "").strip() or None
    price_text = product.get("price_text") or None
    price_value, price_unit = parse_price_text(price_text or "")
    valid_from = _to_date(product.get("valid_from"))
    valid_to = _to_date(product.get("valid_to"))
    gated = _is_loyalty_gated(product)
    conditions = _conditions_of(product)
    if gated:
        program = loyalty_program_of(product, default_program)
        if program:
            conditions["loyalty_program"] = program
    return FlyerItem(
        name_fr=name if locale.startswith("fr") else None,
        name_en=name if locale.startswith("en") else None,
        price_text=price_text,
        price_value=price_value,
        price_unit=price_unit,
        image_url=product.get("image_url"),
        bbox=_bbox_of(product),
        sku=product.get("sku"),
        brand=product.get("brand"),
        conditions=conditions,
        loyalty_gated=gated,
        valid_from=valid_from,
        valid_to=valid_to,
        languages=[locale],
        raw=product,
        confidence=1.0,
    )


def _merge_key(item: FlyerItem) -> str:
    if item.sku:
        return f"sku:{item.sku}"
    page = item.bbox.get("page") if item.bbox else None
    name = (item.name_fr or item.name_en or "").strip().lower()
    return f"pos:{page}:{name}"


def merge_locales(fr_items: list[FlyerItem], en_items: list[FlyerItem]) -> list[FlyerItem]:
    """Merge FR and EN product lists into single bilingual items.

    Matches by SKU when present, else by (page, name). EN-only items are kept
    with name_en set; FR-only items keep name_fr.
    """
    en_by_key = {_merge_key(it): it for it in en_items}
    merged: list[FlyerItem] = []
    used: set[str] = set()
    for fr in fr_items:
        key = _merge_key(fr)
        en = en_by_key.get(key)
        if en is not None:
            used.add(key)
            fr.name_en = en.name_en or en.name_fr
            fr.languages = sorted(set(fr.languages) | set(en.languages))
            if fr.valid_from is None:
                fr.valid_from = en.valid_from
            if fr.valid_to is None:
                fr.valid_to = en.valid_to
        merged.append(fr)
    for key, en in en_by_key.items():
        if key not in used:
            en.name_en = en.name_en or en.name_fr
            merged.append(en)
    return merged


class FlyerKitClient:
    """Thin client for the Flipp FlyerKit JSON API."""

    def __init__(self, session: requests.Session | None = None) -> None:
        self.session = session or requests.Session()
        self.session.headers.setdefault("User-Agent", USER_AGENT)

    def _get(self, path: str, params: dict[str, Any]) -> Any:
        url = f"{BASE_URL}{path}"
        try:
            resp = self.session.get(url, params=params, timeout=TIMEOUT)
        except requests.RequestException as exc:
            raise FlyerKitError(f"request failed: {url}: {exc}") from exc
        if resp.status_code != 200:
            raise FlyerKitError(f"unexpected status {resp.status_code} for {url}")
        try:
            return resp.json()
        except json.JSONDecodeError as exc:
            raise FlyerKitError(f"invalid JSON from {url}") from exc

    def get_publications(self, cfg: BrandConfig, locale: str = "fr") -> list[dict[str, Any]]:
        params: dict[str, Any] = {
            "locale": locale,
            "languages[]": locale,
            "access_token": cfg.access_token,
            "store_code": cfg.store_code,
        }
        data = self._get(f"/publications/{cfg.brand_slug}", params)
        if isinstance(data, dict):
            for key in ("flyers", "publications", "data", "results"):
                found = _as_dict_list(data.get(key))
                if found:
                    return found
            return []
        return _as_dict_list(data)

    def get_products(
        self, publication_id: int | str, cfg: BrandConfig, locale: str = "fr"
    ) -> list[dict[str, Any]]:
        params: dict[str, Any] = {
            "display_type": "all",
            "locale": locale,
            "access_token": cfg.access_token,
        }
        data = self._get(f"/publication/{publication_id}/products", params)
        if isinstance(data, dict):
            for key in ("products", "data", "results"):
                found = _as_dict_list(data.get(key))
                if found:
                    return found
            return []
        return _as_dict_list(data)

    def fetch_store_editions(
        self, cfg: BrandConfig, locales: tuple[str, ...] = ("fr", "en")
    ) -> list[FlyerEdition]:
        """Fetch active publications and their products, merged across locales."""
        publications = self.get_publications(cfg, locales[0])
        editions: list[FlyerEdition] = []
        for pub in publications:
            pub_id = pub.get("id")
            if pub_id is None:
                continue
            edition = edition_from_publication(pub)
            edition.languages = list(locales)
            per_locale = [
                [
                    item_from_product(p, loc, BANNER_PROGRAMS.get(cfg.brand_slug))
                    for p in self.get_products(pub_id, cfg, loc)
                ]
                for loc in locales
            ]
            items = per_locale[0]
            for other in per_locale[1:]:
                items = merge_locales(items, other)
            # Fall back to edition validity when the item carries none.
            for item in items:
                if item.valid_from is None:
                    item.valid_from = edition.valid_from
                if item.valid_to is None:
                    item.valid_to = edition.valid_to
            edition.items = items
            editions.append(edition)
        return editions
