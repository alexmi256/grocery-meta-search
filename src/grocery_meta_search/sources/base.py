"""Shared flyer-source data model."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class FlyerItem:
    """One product parsed from a flyer edition."""

    name_fr: str | None = None
    name_en: str | None = None
    price_text: str | None = None
    price_value: float | None = None
    price_unit: str | None = None
    image_url: str | None = None
    bbox: dict[str, Any] | None = None
    sku: str | None = None
    brand: str | None = None
    section: str | None = None
    conditions: dict[str, Any] = field(default_factory=dict)
    loyalty_gated: bool = False
    valid_from: str | None = None
    valid_to: str | None = None
    languages: list[str] = field(default_factory=list)
    raw: dict[str, Any] = field(default_factory=dict)
    confidence: float = 1.0


@dataclass
class FlyerEdition:
    """One flyer edition (a dated publication) with its items."""

    valid_from: str | None
    valid_to: str | None
    flyer_type: str = "weekly"
    languages: list[str] = field(default_factory=list)
    raw: dict[str, Any] = field(default_factory=dict)
    items: list[FlyerItem] = field(default_factory=list)
