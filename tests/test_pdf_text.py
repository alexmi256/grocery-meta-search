"""Unit tests for the PDF text-layer parser (sources/pdf_text.py),
on synthetic span data — the algorithm pieces that the Akhavan
flyer exercises: duplicated spans, dollar+cents pairing, cents
prices with a separate ¢ span, and name assembly."""

from grocery_meta_search.sources.pdf_text import (
    Span,
    assemble_name,
    dedupe_spans,
    find_prices,
    price_unit,
)


def _span(text: str, size: float, x0: float, y0: float) -> Span:
    return Span(text, size, x0, y0, x0 + 8 * len(text), y0 + size)


def test_dedupe_spans() -> None:
    s = _span("HOUMOUS", 11, 10, 10)
    assert dedupe_spans([s, s, _span("FALAFEL", 11, 10, 30)]) == [
        s,
        _span("FALAFEL", 11, 10, 30),
    ]


def test_find_prices_dollar_cents() -> None:
    spans = [
        _span("3", 40, 100, 100),
        _span("99", 23, 124, 103),
        _span("99", 23, 124, 103),  # shadow duplicate
    ]
    prices = find_prices(dedupe_spans(spans), 17.0)
    assert len(prices) == 1
    assert prices[0].value == 3.99
    assert prices[0].text == "3 99"


def test_find_prices_cents_with_separate_cent_sign() -> None:
    spans = [_span("49", 40, 100, 100), _span("¢", 23, 128, 103)]
    prices = find_prices(spans, 17.0)
    assert len(prices) == 1
    assert prices[0].value == 0.49
    assert prices[0].text == "49¢"


def test_find_prices_two_digit_dollars() -> None:
    spans = [_span("16", 40, 100, 100), _span("99", 23, 140, 103)]
    prices = find_prices(spans, 17.0)
    assert len(prices) == 1 and prices[0].value == 16.99


def test_assemble_name_drops_price_units() -> None:
    spans = [
        _span("HOUMOUS", 11, 10, 10),
        _span("AKHAVAN", 11, 70, 10),
        _span("HUMMUS", 9, 10, 26),
        _span("425 g", 9, 10, 40),
        _span("ch.", 9, 100, 90),
        _span("ea.", 9, 112, 90),
    ]
    name = assemble_name(spans, (0, 0, 200, 120), 17.0)
    assert name == "HOUMOUS AKHAVAN | HUMMUS | 425 g"


def test_price_unit_lb_near_price() -> None:
    price = find_prices([_span("4", 40, 100, 100), _span("49", 23, 120, 103)], 17.0)[0]
    spans = [_span("lb.", 9, 110, 128)]
    assert price_unit(spans, price) == "lb"
    assert price_unit([], price) == "each"


def test_split_cell_text() -> None:
    from grocery_meta_search.sources.pdf_text import Price, split_cell_text

    black, red = 0x231F20, 0xD2232A
    price = Price(4.49, "4 49", [_span("4", 40, 160, 90), _span("49", 23, 184, 93)])
    spans = [
        Span("PRUNES DÉNOYAUTÉES", 11.5, 10, 10, 110, 22, color=black),
        Span("AKHAVAN", 11.5, 10, 24, 60, 36, color=red),
        Span("PITTED PRUNES", 9.0, 10, 38, 90, 48, color=black),
        Span("454 g", 7.0, 10, 50, 40, 58, color=black),
        Span("ch.", 8.0, 150, 108, 162, 116, color=black),  # below price: ignored
    ]
    ct = split_cell_text(spans, (0, 0, 200, 140), price, 17.0)
    assert ct.name_fr == "PRUNES DÉNOYAUTÉES"
    assert ct.name_en == "PITTED PRUNES"
    assert ct.brand == "AKHAVAN"
    assert ct.size == "454 g"
