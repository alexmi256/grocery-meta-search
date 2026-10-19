"""Monde au Naturel 'name_cells' segmentation (2026-10-17).

The Monde catalogue prints no dollar prices: each product sits in a
green-framed cell with its name in white caps on a green band and a
'SPÉCIAL n %' leaf badge. Fixture: real page 2 of the Oct 2026
catalogue (image + captured RapidOCR lines). Ground truth read
visually: 11 products, badges 15% on the top row, 20% elsewhere.
Band names come from real Tesseract crop OCR (deterministic).
"""

import json
from pathlib import Path
from typing import Any

from ocr_fixtures import fixture_image, require_cv2, require_french_ocr
from PIL import Image

from grocery_meta_search.ocr.engine import OcrLine
from grocery_meta_search.ocr.segment import OcrStoreConfig, segment_page

FIXTURES = Path(__file__).with_name("fixtures")


def _monde_items() -> list[Any]:
    require_cv2()
    require_french_ocr()
    data: dict[str, Any] = json.loads((FIXTURES / "cc_monde_p2_lines.json").read_text(encoding="utf-8"))
    lines = [OcrLine(x=d["x"], y=d["y"], w=d["w"], h=d["h"], text=d["text"], conf=d["conf"]) for d in data["lines"]]
    image = Image.open(fixture_image("monde_p2.webp")).convert("RGB")
    cfg = OcrStoreConfig(price_strategy="name_cells", bare_int_anchor=False)
    return segment_page(image, lines, cfg, page_url="fixture://", page_number=2)


def test_monde_page2_lists_products_price_less() -> None:
    items = _monde_items()
    assert len(items) == 11
    assert all(it.price_value is None and it.price_text is None for it in items)
    names = [it.name_fr or "" for it in items]
    assert any("CROUSTADE AUX POMMES" in n for n in names)
    assert sum("TAHINI" in n for n in names) == 4
    discounts = [it.conditions.get("discount_percent") for it in items]
    assert discounts[:3] == [15, 15, 15]
    assert all(d == 20 for d in discounts[3:])
