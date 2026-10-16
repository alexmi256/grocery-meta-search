"""Regression tests for bbox cropping.

OCR bboxes are normalized to 1000x1000 (ocr/segment.py); the crop
helper must denormalize them against the real page size. The
2026-10-15 review docs treated them as pixels and every crop was
displaced.
"""

import json
from pathlib import Path

from PIL import Image

from grocery_meta_search.classify.review import _crop, _sane_bbox


def test_sane_bbox_accepts_normalized() -> None:
    raw = json.dumps({"left": 250, "top": 500, "right": 500, "bottom": 750, "page": 1})
    b = _sane_bbox(raw)
    assert b is not None and b["left"] == 250 and b["page"] == 1


def test_sane_bbox_rejects_pixel_space() -> None:
    raw = json.dumps({"left": 1200, "top": 300, "right": 1800, "bottom": 900})
    assert _sane_bbox(raw) is None


def test_crop_denormalizes(tmp_path: Path) -> None:
    # 2000x1000 page; white box at pixels (500,500)-(1000,750),
    # i.e. normalized (250,500)-(500,750).
    page = Image.new("RGB", (2000, 1000), "black")
    for x in range(500, 1000):
        for y in range(500, 750):
            page.putpixel((x, y), (255, 255, 255))
    page_path = tmp_path / "page.jpg"
    page.save(page_path)
    out = tmp_path / "crop.jpg"
    bbox = {"left": 250.0, "top": 500.0, "right": 500.0, "bottom": 750.0}
    assert _crop(page_path, bbox, out)
    with Image.open(out) as crop:
        cx, cy = crop.size[0] // 2, crop.size[1] // 2
        assert crop.getpixel((cx, cy)) == (255, 255, 255)
