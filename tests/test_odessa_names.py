"""Odessa Poissonnier tailored pass (2026-10-17).

The wholesale catalogue prints, per product: FR name / EN italic /
brand / size stacked above a price line that pairs the headline
('10,99 $/lb') with a smaller unit rate ('24,23 $/kg*'). Stock
segmentation produced brand-only names (the mixed-case EN line is
not a caps candidate, so growth from the brand seed never reached
the FR name), origin-banner names, and rate-priced items (the rate
anchored its own item and stole the name block). The tailored
config: name_position 'above', block_y_gap_frac 0.05 (bridges the
non-candidate rungs), and pair_rate_anchors (same-line pairs merge
into the leftmost/headline anchor, the rate rides as an alt price).
A parser guard rejects multibuy counts > 100 (glued price lines
like '15998/400' parsed as 15,998-for-$4 phantoms at 0.00025).
Fixtures: pages 2, 3, 7, 12 of the Oct 8-21, 2026 catalogue,
upscaled to production width 1600 with captured RapidOCR lines.
Ground truth read visually + the campaign's hand corrections.
Residuals: goberge/rouleaux headlines fuse into garbled tokens on
some OCR rolls; the feuillete headline reads '1g99' (9->g).
"""

import json
from pathlib import Path
from typing import Any

from ocr_fixtures import fixture_image, require_french_ocr
from PIL import Image

from grocery_meta_search.ocr.engine import OcrLine, upscale_for_ocr
from grocery_meta_search.ocr.segment import segment_page
from grocery_meta_search.pipeline.fetch import _cc_ocr_config

FIXTURES = Path(__file__).with_name("fixtures")


def _odessa_items(page: int) -> list[Any]:
    require_french_ocr()
    data: list[dict[str, Any]] = json.loads((FIXTURES / f"odessa_p{page}_lines.json").read_text(encoding="utf-8"))
    lines = [OcrLine(x=d["x"], y=d["y"], w=d["w"], h=d["h"], text=d["text"], conf=d["conf"]) for d in data]
    image = upscale_for_ocr(
        Image.open(fixture_image(f"odessa_p{page}.jpg")).convert("RGB"),
        min_width=1600,
    )
    cfg = _cc_ocr_config("odessa-poissonnier")
    assert cfg.pair_rate_anchors and cfg.name_position == "above"
    return segment_page(image, lines, cfg, page_url="fixture://", page_number=page)


def test_odessa_headline_wins_over_rate() -> None:
    items = _odessa_items(2)
    tilapia = [it for it in items if it.price_value == 10.99]
    assert len(tilapia) == 1
    assert tilapia[0].name_fr.startswith("FILET DE TILAPIA")
    # No rate-priced or phantom micro-price items survive.
    assert all(it.price_value > 0.5 for it in items)


def test_odessa_oyster_ladder_folds_to_single_price() -> None:
    items = _odessa_items(3)
    assert len(items) == 1
    assert items[0].price_value == 1.69
    assert items[0].name_fr.startswith("HUÎTRE LA GRANDE")


def test_odessa_feature_card_name() -> None:
    items = _odessa_items(7)
    assert len(items) == 1
    assert items[0].price_value == 26.99
    assert items[0].name_fr.startswith("CREVETTE TIGRÉE")


def test_odessa_brand_only_names_fixed() -> None:
    items = _odessa_items(12)
    names = {it.price_value: it.name_fr for it in items}
    assert names[4.99].startswith("RAIFORT")
    assert names[5.49].startswith("SAUCE PONZU")
    assert names[11.99].startswith("GRATIN DAUPHINOIS")
    assert "CAVIAR DE LOMPE" in names[10.99]
