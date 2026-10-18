"""PA Nature 'chalkboard' segmentation (2026-10-17).

PA Nature's flyerbox pages print each price on a small chalkboard
(near-black board, light wood frame) with hatched chalk digits, and
the product name in black caps above the board. Fixture: real page 1
of the Oct 12-25, 2026 edition (image + captured RapidOCR lines).
Ground truth read visually from the page: 10 products, all 10 prices
recovered. Board digits come from live crop OCR + token voting, so
this test is slow (minutes) but exercises the production config.
"""

import json
from pathlib import Path
from typing import Any

from PIL import Image

from grocery_meta_search.ocr.engine import OcrLine
from grocery_meta_search.ocr.segment import segment_page
from grocery_meta_search.pipeline.fetch import _official_ocr_config
from grocery_meta_search.sources.official import load_official_configs

FIXTURES = Path(__file__).with_name("fixtures")


def _pa_items() -> list[Any]:
    data: dict[str, Any] = json.loads((FIXTURES / "pa_nature_p1_lines.json").read_text(encoding="utf-8"))
    lines = [OcrLine(x=d["x"], y=d["y"], w=d["w"], h=d["h"], text=d["text"], conf=d["conf"]) for d in data["lines"]]
    image = Image.open(FIXTURES / "pa_nature_p1.jpg").convert("RGB")
    cfg = _official_ocr_config(load_official_configs()["pa-nature"])
    assert cfg.price_strategy == "chalkboard"
    return segment_page(image, lines, cfg, page_url="fixture://", page_number=1)


def test_pa_nature_page1_chalkboards() -> None:
    items = _pa_items()
    assert len(items) == 10
    names = [it.name_fr or "" for it in items]
    assert any("BAVETTE" in n for n in names)
    assert any("SAUMON" in n for n in names)
    assert any("AMANDES" in n for n in names)
    priced = sorted(
        ((round(it.price_value, 2), it.price_unit) for it in items if it.price_value is not None),
        key=lambda p: (p[0], p[1] or ""),
    )
    # Multibuy anchors also carry their unit price (total / count).
    assert priced == [
        (1.5, None),
        (1.67, None),
        (1.67, None),
        (2.99, None),
        (2.99, "lb"),
        (2.99, "lb"),
        (6.99, None),
        (9.99, "lb"),
        (14.99, "lb"),
        (17.99, "lb"),
    ]
    multibuys = sorted(
        (it.conditions["multibuy"]["count"], it.conditions["multibuy"]["total"])
        for it in items
        if "multibuy" in it.conditions
    )
    assert multibuys == [(2, 3.0), (3, 5.0), (3, 5.0)]
