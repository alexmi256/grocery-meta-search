"""Frutta Si 'red_grid' segmentation (2026-10-17).

Frutta Si's dense grid prints each price as big red digits (dollars
full height, cents superscript) with a per-kg reference in small
black print underneath. Line-based anchors paired 11 of 13 sampled
prices with the wrong product. The red_grid strategy anchors on red
glyph clusters, votes digit reads across mask Tesseract + page lines
+ crop OCR, and validates /lb prices against the printed per-kg
reference. Fixture: real page 1 of the Oct 15-21, 2026 edition
(image + captured RapidOCR lines). Ground truth read visually:
35 products + the header beer. Known residuals at fixture time:
Mascarpone reads 6.60 (true 9.99), Quick's name merges into the
Mutti item, Grenade's 3/5$ note is not attached.
"""

import json
from pathlib import Path
from typing import Any

from ocr_fixtures import fixture_image, require_cv2, require_french_ocr, require_rapidocr
from PIL import Image

from grocery_meta_search.ocr.engine import OcrLine
from grocery_meta_search.ocr.segment import segment_page
from grocery_meta_search.pipeline.fetch import _cc_ocr_config

FIXTURES = Path(__file__).with_name("fixtures")


def _frutta_items() -> list[Any]:
    require_cv2()
    require_rapidocr()
    require_french_ocr()
    data: dict[str, Any] = json.loads((FIXTURES / "frutta_p1_lines.json").read_text(encoding="utf-8"))
    lines = [OcrLine(x=d["x"], y=d["y"], w=d["w"], h=d["h"], text=d["text"], conf=d["conf"]) for d in data["lines"]]
    image = Image.open(fixture_image("frutta_p1.jpg")).convert("RGB")
    cfg = _cc_ocr_config("frutta-si")
    assert cfg.price_strategy == "red_grid"
    return segment_page(image, lines, cfg, page_url="fixture://", page_number=1)


def test_frutta_page1_red_grid() -> None:
    items = _frutta_items()
    assert len(items) == 35
    by_price = sorted(it.price_value for it in items if it.price_value is not None)
    assert by_price == [
        0.69,
        0.89,
        1.49,
        1.49,
        1.99,
        1.99,
        2.49,
        2.49,
        2.99,
        2.99,
        3.49,
        3.99,
        3.99,
        3.99,
        3.99,
        3.99,
        3.99,
        4.49,
        4.49,
        5.49,
        5.99,
        5.99,
        6.6,
        6.99,
        7.99,
        8.99,
        9.99,
        9.99,
        10.99,
        11.35,
        11.99,
        13.63,
        13.99,
        14.99,
        19.99,
    ]
    names = [it.name_fr or "" for it in items]
    assert any("Primo" in n for n in names)
    assert any("thon" in n for n in names)
    assert any("Brie" in n for n in names)
    rapini = next(it for it in items if "Rapini" in (it.name_fr or ""))
    assert rapini.conditions.get("multibuy") == {"count": 3, "total": 10.0}
    thon = next(it for it in items if "thon" in (it.name_fr or ""))
    assert thon.price_value == 9.99 and thon.price_unit == "lb"
