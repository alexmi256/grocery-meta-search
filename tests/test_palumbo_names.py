"""Intermarche Palumbo name assembly (2026-10-17).

Palumbo's flyer stacks display name / photo / price vertically. The
display names print in the chain's dark green; packaging label text
sits on the photo, nearer the price, and won plain nearest-line
seeding ('SAUCE BABILICO' off the Rudolfi jar, label garble for the
Grande bags). Two store-scoped gates fix the assembly:
name_green_gate restricts name candidates to green-ink lines
(display 0.64-0.94 vs labels 0.00-0.05 on this page), and
name_lines_verify drops re-OCR block lines that share no content
with the detected lines (the WOW badge intrudes into block crops).
Fixture: real page 1 of the Oct 15-21, 2026 edition. Ground truth
read visually: 6 products. Known residual: 'ROMANO OU' is occluded
by the WOW badge in detection, so the cheese item assembles as
'PARMESAN RAPE GRANDE'.
"""

import json
from pathlib import Path
from typing import Any

from ocr_fixtures import fixture_image, require_cv2, require_french_ocr
from PIL import Image

from grocery_meta_search.ocr.engine import OcrLine
from grocery_meta_search.ocr.segment import segment_page
from grocery_meta_search.pipeline.fetch import _cc_ocr_config

FIXTURES = Path(__file__).with_name("fixtures")


def _palumbo_items() -> list[Any]:
    require_cv2()
    require_french_ocr()
    data: list[dict[str, Any]] = json.loads((FIXTURES / "palumbo_p1_lines.json").read_text(encoding="utf-8"))
    lines = [OcrLine(x=d["x"], y=d["y"], w=d["w"], h=d["h"], text=d["text"], conf=d["conf"]) for d in data]
    image = Image.open(fixture_image("palumbo_p1.jpg")).convert("RGB")
    cfg = _cc_ocr_config("intermarche-palumbo")
    assert cfg.name_green_gate and cfg.name_lines_verify
    return segment_page(image, lines, cfg, page_url="fixture://", page_number=1)


def test_palumbo_names_come_from_display_type() -> None:
    items = _palumbo_items()
    assert len(items) == 6
    by_price = {it.price_value: it for it in items}
    assert by_price[8.99].name_fr.startswith("BORBONE")
    assert "CAPSULES DE CAFE" in by_price[8.99].name_fr
    assert by_price[13.99].name_fr.startswith("DINDE")
    assert "TURKEY" in by_price[13.99].name_fr
    assert by_price[13.99].price_unit == "lb"
    assert by_price[6.99].name_fr.startswith("POITRINE DE POULET")
    assert by_price[2.99].name_fr.startswith("SAUCE POUR PATES")
    assert "BABILICO" not in by_price[2.99].name_fr
    assert by_price[9.99].name_fr.startswith("PARMESAN RAPE")
    assert "GRANDE" in by_price[9.99].name_fr
    assert "TENTACULES" in by_price[10.99].name_fr
    assert "CALAMARS" in by_price[10.99].name_fr
