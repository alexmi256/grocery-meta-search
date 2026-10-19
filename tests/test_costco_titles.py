"""Costco prix_line printed titles (2026-10-17).

The warehouse booklet prints a clean title under each photo
('Simplement chocolat chaud Carnation de Nestlé'), but prix_line
stitched names from the product LABEL's OCR text - garbled and
word-glued ('CHOCOLAT CHAUD SimplementchocolatchaudCarnationde',
'BiscuitsBiscoffdeLotus' unclassifiable). Every cell also prints a
red channel line ('Entrepôt et en ligne' / 'En entrepôt seulement')
directly above the title block, followed by detail lines (size,
'N° d'article', 'Valide du...'). _prix_line_title anchors on the
channel line, re-OCRs the block up to the first detail line with
Tesseract, and strips the detail markers. Fixture: real page 3 of
the Sep 28 - Oct 25, 2026 booklet with captured RapidOCR lines.
"""

import json
from pathlib import Path
from typing import Any

from ocr_fixtures import fixture_image, require_french_ocr
from PIL import Image

from grocery_meta_search.ocr.engine import OcrLine
from grocery_meta_search.ocr.segment import segment_page
from grocery_meta_search.pipeline.fetch import _cc_ocr_config

FIXTURES = Path(__file__).with_name("fixtures")


def test_costco_names_are_the_printed_titles() -> None:
    require_french_ocr()
    data: list[dict[str, Any]] = json.loads((FIXTURES / "costco_p3_lines.json").read_text(encoding="utf-8"))
    lines = [OcrLine(x=d["x"], y=d["y"], w=d["w"], h=d["h"], text=d["text"], conf=d["conf"]) for d in data]
    image = Image.open(fixture_image("costco_p3.jpg")).convert("RGB")
    cfg = _cc_ocr_config("costco")
    assert cfg.price_strategy == "prix_line"
    items = segment_page(image, lines, cfg, page_url="fixture://", page_number=3)
    names = {it.price_value: it.name_fr for it in items}
    assert names[12.99].startswith("Simplement chocolat chaud Carnation")
    assert names[8.99] == "Biscuits Biscoff de Lotus"
    assert names[13.99].startswith("Pizza quatre fromages sans gluten")
    assert names[10.99].startswith("Mousse au spéculoos")
    assert names[42.99].startswith("Café de torréfaction supérieure")
    # No label stitches or article-number tails survive.
    for name in names.values():
        assert "article" not in name.lower()
        assert "Biscoffde" not in name
