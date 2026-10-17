"""Flipp unauthenticated search/flyer API client (independent merchants).

Endpoints (discovered 2026-10-13, no auth required):
  GET https://cdn-gateflipp.flippback.com/bf/flipp/items/search
      ?q=<merchant>&postal_code=<FSA>&locale=<fr|en>
      -> {flyers: [{id}], items: [...], merchants: [...], facets: {...}}
      Note: items[] is capped (~150); use the flyer endpoint for completeness.
  GET https://cdn-gateflipp.flippback.com/bf/flipp/flyers/{flyer_id}
      -> {items: [...], pages: [...]}  (complete item list for one flyer)

Recipe: search by merchant name to discover flyer IDs, then fetch each flyer.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

import requests

from ..prices import parse_price_text
from .base import FlyerEdition, FlyerItem
from .flipp import _to_date
from .names import split_bilingual_name

BASE_URL = "https://cdn-gateflipp.flippback.com/bf/flipp"
TIMEOUT = 30
USER_AGENT = "grocery-meta-search/0.1 (research project)"


class FlippSearchError(RuntimeError):
    """Raised when the Flipp search API misbehaves."""


@dataclass
class SearchConfig:
    store_slug: str
    merchant_name: str  # query string for the search endpoint
    postal_code: str  # FSA for localization, e.g. "H3Y2Y6"


def _bbox_of(item: dict[str, Any]) -> dict[str, Any] | None:
    bbox = {k: item[k] for k in ("left", "top", "right", "bottom") if item.get(k) is not None}
    return bbox or None


def item_from_search_item(item: dict[str, Any], locale: str) -> FlyerItem:
    name = (item.get("name") or "").strip() or None
    name_fr, name_en = split_bilingual_name(name)
    if name_en is None and name_fr is not None and not locale.startswith("fr"):
        # Single-language name from an English-locale fetch.
        name_fr, name_en = None, name_fr
    price_text = item.get("price")
    if price_text is not None:
        price_text = str(price_text).strip() or None
    price_value, price_unit = parse_price_text(price_text or "")
    conditions: dict[str, Any] = {}
    if item.get("discount"):
        conditions["discount"] = item["discount"]
    return FlyerItem(
        name_fr=name_fr,
        name_en=name_en,
        price_text=price_text,
        price_value=price_value,
        price_unit=price_unit,
        image_url=item.get("cutout_image_url"),
        bbox=_bbox_of(item),
        brand=item.get("brand"),
        conditions=conditions,
        valid_from=_to_date(item.get("valid_from")),
        valid_to=_to_date(item.get("valid_to")),
        languages=[locale],
        raw=item,
        confidence=1.0,
    )


class FlippSearchClient:
    """Thin client for the unauthenticated Flipp search/flyer API."""

    def __init__(self, session: requests.Session | None = None) -> None:
        self.session = session or requests.Session()
        self.session.headers.setdefault("User-Agent", USER_AGENT)

    def _get(self, path: str, params: dict[str, Any]) -> Any:
        url = f"{BASE_URL}{path}"
        try:
            resp = self.session.get(url, params=params, timeout=TIMEOUT)
        except requests.RequestException as exc:
            raise FlippSearchError(f"request failed: {url}: {exc}") from exc
        if resp.status_code != 200:
            raise FlippSearchError(f"unexpected status {resp.status_code} for {url}")
        try:
            return resp.json()
        except json.JSONDecodeError as exc:
            raise FlippSearchError(f"invalid JSON from {url}") from exc

    def search(self, cfg: SearchConfig, locale: str = "fr") -> dict[str, Any]:
        data = self._get(
            "/items/search",
            {"q": cfg.merchant_name, "postal_code": cfg.postal_code, "locale": locale},
        )
        if not isinstance(data, dict):
            raise FlippSearchError("unexpected search response shape")
        return data

    def merchant_flyer_ids(self, cfg: SearchConfig, locale: str = "fr") -> list[int]:
        data = self.search(cfg, locale)
        ids: list[int] = []
        for flyer in data.get("flyers", []):
            fid = flyer.get("id")
            if isinstance(fid, int) and fid not in ids:
                ids.append(fid)
        return ids

    def get_flyer(self, flyer_id: int) -> dict[str, Any]:
        data = self._get(f"/flyers/{flyer_id}", {})
        if not isinstance(data, dict):
            raise FlippSearchError("unexpected flyer response shape")
        return data

    def fetch_store_editions(self, cfg: SearchConfig, locale: str = "fr") -> list[FlyerEdition]:
        """Fetch all current flyers for a merchant, with complete item lists."""
        editions: list[FlyerEdition] = []
        for flyer_id in self.merchant_flyer_ids(cfg, locale):
            flyer = self.get_flyer(flyer_id)
            raw_items = flyer.get("items", [])
            items = [item_from_search_item(it, locale) for it in raw_items]
            valid_from = valid_to = None
            for item in items:
                valid_from = valid_from or item.valid_from
                valid_to = valid_to or item.valid_to
                if item.valid_from is None:
                    item.valid_from = valid_from
                if item.valid_to is None:
                    item.valid_to = valid_to
            editions.append(
                FlyerEdition(
                    valid_from=valid_from,
                    valid_to=valid_to,
                    flyer_type="weekly",
                    source_ref=str(flyer_id),
                    languages=[locale],
                    raw={"flyer_id": flyer_id, "pages": flyer.get("pages", [])},
                    items=items,
                )
            )
        return editions
