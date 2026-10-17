"""Quebec flyer price-text parsing.

Handles formats seen on Montreal flyers: "2.50", "9,99 $", "2/5$",
"3,49/lb", "2 pour 4$". Returns (unit_price, unit).
"""

from __future__ import annotations

import re

_MULTI_RE = re.compile(r"^\s*(\d+)\s*/\s*\$?\s*([\d\s,\.]+)\s*\$?\s*$")
_POUR_RE = re.compile(r"^\s*(\d+)\s+pour\s+\$?\s*([\d\s,\.]+)\s*\$?\s*$", re.IGNORECASE)
_UNIT_RE = re.compile(r"/\s*(lb|kg|g|ch|ea|each|un|unité|unite)\b", re.IGNORECASE)
_NUM_RE = re.compile(r"[\d][\d\s,\.]*")

_UNIT_ALIASES = {
    "ch": "each",
    "ea": "each",
    "each": "each",
    "un": "each",
    "unité": "each",
    "unite": "each",
    "lb": "lb",
    "kg": "kg",
    "g": "g",
}


# Unit split (2026-10-17, Alex): a price always carries a quantity and
# a measurement, so prices can be normalized per weight/volume and
# compared across stores. Defaults: quantity 1, measurement 'each'.
# Multibuy offers ("3/15$") use measurement 'multiple' with the count
# as quantity; per-100g pricing is (100, 'gram').
MEASUREMENTS = (
    "each",
    "gram",
    "ounce",
    "kilogram",
    "pound",
    "liter",
    "milliliter",
    "pack",
    "multiple",
)

_UNIT_PAIRS: dict[str, tuple[float, str]] = {
    "each": (1.0, "each"),
    "lb": (1.0, "pound"),
    "kg": (1.0, "kilogram"),
    "g": (1.0, "gram"),
    "100g": (100.0, "gram"),
    "box": (1.0, "pack"),
    "l": (1.0, "liter"),
    "ml": (1.0, "milliliter"),
    "oz": (1.0, "ounce"),
}


def multibuy_count(conditions: object) -> int | None:
    """The multibuy count from a conditions dict or its JSON text."""
    import json

    data: object = conditions
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except ValueError:
            return None
    if isinstance(data, dict):
        multi = data.get("multibuy")
        if isinstance(multi, dict):
            count = multi.get("count")
            if isinstance(count, int) and count > 0:
                return count
    return None


def split_unit(unit: str | None, multibuy: int | None = None) -> tuple[float, str]:
    """Split a legacy price_unit into (unit_quantity, unit_measurement).

    A multibuy count above 1 wins over the unit: the price covers
    that many items. Unknown or missing units fall back to the
    default (1, 'each').
    """
    if multibuy is not None and multibuy > 1:
        return float(multibuy), "multiple"
    if unit:
        pair = _UNIT_PAIRS.get(unit.strip().lower())
        if pair is not None:
            return pair
    return 1.0, "each"


def _to_float(num: str) -> float | None:
    num = num.replace(" ", "").replace("\u00a0", "")
    if "," in num and "." not in num:
        num = num.replace(",", ".")  # "9,99" -> "9.99"
    elif "," in num:
        num = num.replace(",", "")  # "1,234.56" -> "1234.56"
    try:
        return float(num)
    except ValueError:
        return None


def parse_price_text(text: str) -> tuple[float | None, str | None]:
    """Parse a flyer price string into (unit_price, unit).

    unit is one of 'each', 'lb', 'kg', 'g', or None when not determinable.
    Multi-buys ("2/5$") resolve to the effective unit price.
    """
    if not text or not text.strip():
        return None, None
    s = text.strip()
    unit: str | None = None
    m = _UNIT_RE.search(s)
    if m:
        unit = _UNIT_ALIASES.get(m.group(1).lower())
        s = _UNIT_RE.sub("", s)
    s = s.replace("$", "").strip()

    m = _MULTI_RE.match(s) or _POUR_RE.match(s)
    if m:
        qty = int(m.group(1))
        total = _to_float(m.group(2))
        if total is None or qty == 0:
            return None, unit
        return round(total / qty, 2), unit or "each"

    m = _NUM_RE.search(s)
    if not m:
        return None, unit
    return _to_float(m.group(0)), unit
