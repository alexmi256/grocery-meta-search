"""Regression tests: store_report must render PDF flyer pages.

Mayrand / Aliments Merci items keep the flyer PDF as image_url with
a normalized bbox. Before the fix, _to_jpg failed on the PDF and the
report embedded the whole multi-MB PDF as the item 'picture'.
"""

from __future__ import annotations

from pathlib import Path

import pymupdf
from PIL import Image

from grocery_meta_search.classify.store_report import _is_pdf, _render_pdf_page


def _make_pdf(path: Path) -> None:
    with pymupdf.open() as doc:
        for color in ((1, 0, 0), (0, 0, 1)):
            page = doc.new_page(width=200, height=200)
            page.draw_rect(pymupdf.Rect(0, 0, 200, 200), fill=color)
        doc.save(path)


def test_is_pdf(tmp_path: Path) -> None:
    pdf = tmp_path / "flyer.pdf"
    _make_pdf(pdf)
    assert _is_pdf(pdf)
    jpg = tmp_path / "x.jpg"
    Image.new("RGB", (10, 10)).save(jpg)
    assert not _is_pdf(jpg)
    assert not _is_pdf(tmp_path / "missing")


def test_render_pdf_page(tmp_path: Path) -> None:
    pdf = tmp_path / "flyer.pdf"
    _make_pdf(pdf)
    out = tmp_path / "page2.jpg"
    assert _render_pdf_page(pdf, 2, out)
    with Image.open(out) as im:
        assert im.format == "JPEG"
        r, g, b = im.convert("RGB").getpixel((5, 5))
        assert b > 150 and r < 100  # second page is blue
    # out-of-range pages clamp instead of failing
    out99 = tmp_path / "page99.jpg"
    assert _render_pdf_page(pdf, 99, out99)
