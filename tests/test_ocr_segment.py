"""Golden-sample tests for OCR flyer segmentation (Phase 3b).

Fixtures are RapidOCR line dumps captured 2026-10-13 from real
circulaires.club pages, with ground truth read visually by the author:

- bonichoix p1: classic IGA-style flyer, caps names, big orange prices.
  Known OCR limitation in the fixture: the beer price "40 99" is read by
  RapidOCR as "40 66" (9/6 glyph confusion) — the pipeline faithfully
  returns 40.66; the true price is 40.99.
- tt p1: dense trilingual grid, mixed-case names, cents-only prices,
  dual prices. Hardest layout; only price-level assertions.
- costco p1: savings book. The big number is the discount; real prices
  come from "Prix X,XX $" lines. The laptop's Prix amount was garbled
  by OCR ("$66666") and must be derived: 1149.99 - 150.00 = 999.99.

Tesseract re-OCR is disabled in these tests (deterministic fallback to
detected line text).
"""

import json
from pathlib import Path
from typing import Any

import pytest
from PIL import Image

from grocery_meta_search.ocr import segment as segment_mod
from grocery_meta_search.ocr.engine import OcrLine
from grocery_meta_search.ocr.segment import (
    OcrStoreConfig,
    _parse_fragment_value,
    _price_core,
    _split_dual_prices,
    find_price_anchors,
    segment_page,
)

FIXTURES = Path(__file__).with_name("fixtures")


@pytest.fixture(autouse=True)
def _no_tesseract(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(segment_mod, "ocr_crop_text", lambda *a, **k: None)


def _load(name: str) -> tuple[list[OcrLine], int, int]:
    data: dict[str, Any] = json.loads(
        (FIXTURES / f"cc_{name}_p1_lines.json").read_text(encoding="utf-8")
    )
    lines = [
        OcrLine(x=d["x"], y=d["y"], w=d["w"], h=d["h"], text=d["text"], conf=d["conf"])
        for d in data["lines"]
    ]
    return lines, int(data["page_w"]), int(data["page_h"])


def _load_fixture(filename: str) -> tuple[list[OcrLine], int, int]:
    data: dict[str, Any] = json.loads(
        (FIXTURES / filename).read_text(encoding="utf-8")
    )
    lines = [
        OcrLine(x=d["x"], y=d["y"], w=d["w"], h=d["h"], text=d["text"], conf=d["conf"])
        for d in data["lines"]
    ]
    return lines, int(data["page_w"]), int(data["page_h"])


def _segment(name: str, cfg: OcrStoreConfig) -> list[Any]:
    lines, w, h = _load(name)
    image = Image.new("RGB", (w, h))
    return segment_page(image, lines, cfg, page_url="fixture://", page_number=1)


def test_parse_fragment_values() -> None:
    assert _parse_fragment_value(["1599"]) == (15.99, "15.99", None)
    assert _parse_fragment_value(["744"]) == (7.44, "7.44", None)
    assert _parse_fragment_value(["6", "49"]) == (6.49, "6.49", None)
    assert _parse_fragment_value(["7.97"]) == (7.97, "7.97", None)
    value, text, multibuy = _parse_fragment_value(["2/500"])  # type: ignore[misc]
    assert value == 2.50 and multibuy == (2, 5.00)
    assert _parse_fragment_value(["abc"]) is None


def test_bonichoix_price_anchors() -> None:
    lines, w, h = _load("bonichoix")
    anchors = find_price_anchors(lines, w, h, OcrStoreConfig())
    values = sorted(a.value for a in anchors)
    assert values == [2.50, 2.50, 3.33, 4.97, 5.97, 5.99, 6.49, 6.99, 7.44, 15.99, 40.66]


def test_bonichoix_items() -> None:
    items = _segment("bonichoix", OcrStoreConfig())
    assert len(items) == 10
    by_price = {it.price_value: it.name_fr or "" for it in items}
    assert "BAVETTE" in by_price[15.99]
    assert "SAUCISSES" in by_price[6.49]
    assert "FRAMBOISES" in by_price[2.50]
    assert "COKE" in by_price[6.99]
    assert "MAYONNAISE" in by_price[5.97]
    framboises = next(it for it in items if it.price_value == 2.50)
    assert framboises.conditions.get("multibuy") == {"count": 2, "total": 5.00}
    for it in items:
        assert it.bbox and it.bbox["page"] == 1
        assert it.image_url == "fixture://"


def test_tt_items() -> None:
    cfg = OcrStoreConfig(name_case="any", price_min_h_frac=0.016, bare_int_is_cents=True)
    items = _segment("tt", cfg)
    prices = {it.price_value for it in items}
    # Prices read off the page visually; the pipeline should find these.
    assert 0.68 in prices  # melon hami, cents-only price
    assert 14.98 in prices  # filet saumon
    assert 8.88 in prices  # anguille grillee
    assert 21.97 in prices  # riz golden royal ox
    assert len(items) >= 12


def test_costco_prix_line_items() -> None:
    items = _segment("costco", OcrStoreConfig(price_strategy="prix_line"))
    by_price = {it.price_value: it.name_fr or "" for it in items}
    assert len(items) == 10
    assert "Televiseur" in by_price[1511.74]
    assert "Ordinateur" in by_price[999.99]  # derived: 1149.99 - 150.00
    assert "Plancher" in by_price[24.99]


def test_price_core_strips_units() -> None:
    assert _price_core("0,99 $/lb") == "0,99"
    assert _price_core("2,95$/KG") == "2,95"
    assert _price_core("3,99 ch.") == "3,99"
    assert _price_core("499s/ch") == "499"
    assert _price_core("14,99 s/ch.") == "14,99"
    assert _price_core("4,40S") == "4,40"
    assert _price_core("3,30S/lb") == "3,30"
    assert _price_core("1,40 $/1b") == "1,40"
    assert _price_core("85¢") == "85"
    assert _price_core("$4.99") == "4.99"
    assert _price_core("2,99 $") == "2,99"
    # size-only lines must NOT be stripped into fake prices
    assert _price_core("4,43 l") == "4,43 l"
    assert _price_core("227 g") == "227 g"
    assert _price_core("MANGUES") == "MANGUES"


def test_split_dual_prices() -> None:
    assert _split_dual_prices(["24992999"]) == [(24.99, "24.99"), (29.99, "29.99")]
    assert _split_dual_prices(["1499", "1699"]) == [(14.99, "14.99"), (16.99, "16.99")]
    assert _split_dual_prices(["1599"]) is None  # single normal price
    assert _split_dual_prices(["6", "49"]) is None  # dollars + cents fragments
    assert _split_dual_prices(["114999"]) is None  # 6-digit: ambiguous, leave alone


def test_parse_fragment_value_dollar_multibuy() -> None:
    value, text, multibuy = _parse_fragment_value(["2/$5"])  # type: ignore[misc]
    assert value == 2.50 and multibuy == (2, 5.00)


def test_stoplist_coerced_to_tuple() -> None:
    cfg = OcrStoreConfig(stoplist=["a", "b"])  # type: ignore[arg-type]
    assert cfg.stoplist == ("a", "b")


def test_dedupe_candidates() -> None:
    from grocery_meta_search.ocr.segment import _dedupe_candidates

    a = OcrLine(x=10, y=10, w=100, h=20, text="Pommesdeterre augratin supremes", conf=0.9)
    b = OcrLine(x=12, y=11, w=98, h=19, text="Pommes deterre augratinsupremes", conf=0.8)
    c = OcrLine(x=10, y=200, w=100, h=20, text="Pommesdeterre augratin supremes", conf=0.9)
    deduped = _dedupe_candidates([a, b, c])
    assert len(deduped) == 2  # b dropped as a duplicate of a; c kept (far away)
    assert deduped[0].conf == 0.9


def test_lamoisson_unit_prices() -> None:
    """La Moisson prints prices as '2,95 $ / KG' badges: the unit suffix used
    to make the whole line non-digitish, so no anchors were found at all."""
    lines, w, h = _load_fixture("cc_lamoisson_p2_lines.json")
    anchors = find_price_anchors(lines, w, h, OcrStoreConfig())
    assert sorted(a.value for a in anchors) == [1.95, 1.95, 2.95, 3.45, 4.95]
    image = Image.new("RGB", (w, h))
    items = segment_page(
        image, lines, OcrStoreConfig(), page_url="fixture://", page_number=1
    )
    by_price = {it.price_value: it.name_fr or "" for it in items}
    assert len(items) == 5
    assert "BANANE" in by_price[2.95]
    assert "KIWI" in by_price[4.95]
    names_195 = {it.name_fr or "" for it in items if it.price_value == 1.95}
    assert any("CORIANDRE" in n for n in names_195)
    assert any("PERSIL" in n for n in names_195)
