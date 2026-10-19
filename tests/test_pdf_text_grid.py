"""PDF grid + end-to-end tests for sources/pdf_text.py.

The existing test_pdf_text.py works on synthetic spans; these build
a REAL PDF with PyMuPDF (red grid lines, big price type, small name
type) and run the full extraction path the Akhavan/Costco flyers
take: extract_pdf -> find_prices -> detect_grid_cells ->
parse_pdf_flyer.
"""

from __future__ import annotations

from datetime import date

import pymupdf

from grocery_meta_search.sources.pdf_text import (
    Price,
    Span,
    derive_cells,
    detect_grid_cells,
    extract_pdf,
    match_cells,
    parse_pdf_flyer,
)

RED = (1, 0, 0)
BLACK = (0, 0, 0)


def _flyer_pdf() -> bytes:
    doc = pymupdf.open()
    page = doc.new_page(width=612, height=792)
    # Red grid: 2 columns x 2 rows over y 100..700.
    for y in (100, 400, 700):
        page.draw_line((0, y), (612, y), color=RED, width=3)
    for x in (50, 330, 610):
        page.draw_line((x, 100), (x, 700), color=RED, width=3)
    # Top-left cell: name above a 3,99 price.
    page.insert_text((70, 150), "JUS D'ORANGE", fontsize=11, color=BLACK)
    page.insert_text((70, 220), "3", fontsize=40, color=BLACK)
    page.insert_text((95, 220), "99", fontsize=23, color=BLACK)
    # Top-right cell: name above a 49¢ price.
    page.insert_text((350, 150), "BONBONS", fontsize=11, color=BLACK)
    page.insert_text((350, 220), "49", fontsize=40, color=BLACK)
    page.insert_text((398, 204), "¢", fontsize=23, color=BLACK)
    return doc.tobytes()


def _plain_pdf() -> bytes:
    doc = pymupdf.open()
    page = doc.new_page(width=612, height=792)
    page.insert_text((70, 150), "NO GRID HERE", fontsize=11, color=BLACK)
    return doc.tobytes()


def test_extract_pdf_spans_and_dimensions() -> None:
    spans, width, height, _text = extract_pdf(_flyer_pdf())
    assert (width, height) == (612, 792)
    texts = {s.text for s in spans}
    assert "JUS D'ORANGE" in texts and "3" in texts and "99" in texts


def test_detect_grid_cells_found_and_absent() -> None:
    cells = detect_grid_cells(_flyer_pdf())
    assert cells is not None and len(cells) == 4
    # Row-major: first cell is the top-left quadrant of the grid.
    x0, y0, x1, y1 = cells[0]
    assert x0 < 100 < x1 and y0 < 200 < y1
    assert detect_grid_cells(_plain_pdf()) is None


def _price(value: float, cx: float, cy: float) -> Price:
    span = Span("x", 40, cx - 5, cy - 5, cx + 5, cy + 5)
    return Price(value, "x", [span])


def test_match_cells_containment_and_nearest() -> None:
    cells = [(0.0, 0.0, 100.0, 100.0), (100.0, 0.0, 200.0, 100.0)]
    inside = _price(1.0, 150, 50)
    outside = _price(2.0, 30, 400)  # below both: nearest centre wins
    paired = match_cells([inside, outside], cells)
    by_value = {p.value: c for p, c in paired}
    assert by_value[1.0] == cells[1]
    assert by_value[2.0] == cells[0]


def test_derive_cells_partitions_page() -> None:
    prices = [_price(1.0, 100, 100), _price(2.0, 500, 100), _price(3.0, 100, 500), _price(4.0, 500, 500)]
    paired = derive_cells(prices, 612, 792)
    assert [p.value for p, _ in paired] == [1.0, 2.0, 3.0, 4.0]  # row-major
    cells = {p.value: c for p, c in paired}
    # The vertical split sits between the two price columns.
    assert cells[1.0][2] == cells[2.0][0]
    assert 100 < cells[1.0][2] < 500
    # Edge cells reach the page edges.
    assert cells[1.0][0] == 0 and cells[4.0][2] == 612


def test_parse_pdf_flyer_end_to_end() -> None:
    items = parse_pdf_flyer(
        _flyer_pdf(),
        valid_from=date(2026, 10, 15),
        valid_to=date(2026, 10, 21),
        image_url="https://example.test/flyer.pdf",
    )
    assert len(items) == 2
    by_value = {it.price_value: it for it in items}
    assert set(by_value) == {3.99, 0.49}
    jus = by_value[3.99]
    assert jus.name_fr and "JUS" in jus.name_fr
    assert jus.valid_from == "2026-10-15" and jus.valid_to == "2026-10-21"
    assert jus.raw["parser"] == "pdf_text"
    assert jus.bbox is not None
    assert 0 <= jus.bbox["left"] < jus.bbox["right"] <= 1000
    assert jus.bbox["page"] == 1
