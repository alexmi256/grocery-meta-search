"""Group 4 (official platforms): discovery/extraction unit tests."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from grocery_meta_search.sources.official import (
    extract_image_urls,
    extract_wix_image_urls,
    fetch_week,
    flyerify_current_offer,
    flyerify_offer_id,
    flyerify_page_count,
    load_official_configs,
    month_bounds,
    parse_offer_range,
    url_month,
    woo_product_to_item,
)

FIXTURES = Path(__file__).parent / "fixtures"
TODAY = date(2026, 10, 13)  # Tuesday


def test_fetch_week() -> None:
    assert fetch_week(TODAY) == (date(2026, 10, 8), date(2026, 10, 14))
    assert fetch_week(date(2026, 10, 8)) == (date(2026, 10, 8), date(2026, 10, 14))
    assert fetch_week(date(2026, 10, 14)) == (date(2026, 10, 8), date(2026, 10, 14))


def test_month_bounds() -> None:
    assert month_bounds(2026, 10) == (date(2026, 10, 1), date(2026, 10, 31))
    assert month_bounds(2026, 12) == (date(2026, 12, 1), date(2026, 12, 31))
    assert month_bounds(2026, 2) == (date(2026, 2, 1), date(2026, 2, 28))


def test_url_month() -> None:
    assert url_month("https://x.ca/wp-content/uploads/2026/10/flyer.jpg") == (
        date(2026, 10, 1),
        date(2026, 10, 31),
    )
    merci = "https://alimentsmerci.com/wp-content/uploads/2026/09/Circulaire-SEPTEMBRE26VV.pdf"
    assert url_month(merci) == (date(2026, 9, 1), date(2026, 9, 30))
    assert url_month("https://x.ca/circulaire-fevrier-2026.pdf") == (
        date(2026, 2, 1),
        date(2026, 2, 28),
    )
    assert url_month("https://x.ca/plain.jpg") is None


WIX_HTML = """
<img src="https://static.wixstatic.com/media/aaaa_111~mv2.jpg/v1/fill/w_529,h_684,al_c/x.jpg">
<img src="https://static.wixstatic.com/media/aaaa_111~mv2.jpg/v1/fill/w_1058,h_1368,al_c/x.jpg">
<img src="https://static.wixstatic.com/media/bbbb_222%7Emv2.png/v1/fill/w_32,h_32,al_c/x.png">
<img src="https://static.wixstatic.com/media/cccc_333~mv2.jpg/v1/fill/w_750,h_4612,al_c/x.jpg">
"""


def test_extract_wix_image_urls() -> None:
    urls = extract_wix_image_urls(WIX_HTML, min_w=600, min_h=900)
    assert urls == [
        "https://static.wixstatic.com/media/aaaa_111~mv2.jpg",
        "https://static.wixstatic.com/media/cccc_333~mv2.jpg",
    ]


GENERIC_HTML = """
<img src="https://i0.wp.com/shop.ca/wp-content/uploads/2026/10/poster-a.png?resize=800%2C1000">
<img src="https://shop.ca/wp-content/uploads/2026/10/poster-a-300x375.png">
<img src="https://shop.ca/wp-content/uploads/2026/09/poster-old.png">
<img src="https://shop.ca/wp-content/uploads/2026/10/Logo-5.png">
"""


def test_extract_image_urls_latest_month() -> None:
    urls = extract_image_urls(
        GENERIC_HTML,
        include="/wp-content/uploads/",
        exclude="logo",
        latest_upload_month=True,
    )
    assert urls == ["https://shop.ca/wp-content/uploads/2026/10/poster-a.png"]


def test_flyerify_brand_page() -> None:
    brand = (FIXTURES / "official_flyerify_brand.html").read_text(encoding="utf-8")
    offer = flyerify_current_offer(brand, "QC", TODAY)
    assert offer is not None
    url, slug, start, end = offer
    assert slug == "wholesale-club-qc-flyer-october-8-to-14"
    assert url.endswith("/" + slug)
    assert (start, end) == (date(2026, 10, 8), date(2026, 10, 14))


def test_flyerify_offer_page() -> None:
    offer_html = (FIXTURES / "official_flyerify_offer.html").read_text(encoding="utf-8")
    assert flyerify_page_count(offer_html) == 19
    assert flyerify_offer_id(offer_html, "wholesale-club-qc-flyer-october-8-to-14") == "827102"


def test_parse_offer_range_year_wrap() -> None:
    rng = parse_offer_range("Flyer December 30 to January 5", date(2026, 12, 29))
    assert rng == (date(2026, 12, 30), date(2027, 1, 5))


def test_woo_product_to_item() -> None:
    prod = json.loads(
        '{"id": 9038, "name": "Biscuits DUCALES", "sku": "4367",'
        ' "permalink": "https://www.marcheandes.com/produit/galletas-ducales-bolsa/",'
        ' "prices": {"price": "289", "regular_price": "329",'
        ' "currency_minor_unit": 2},'
        ' "images": [{"src": "https://www.marcheandes.com/img.jpg"}]}'
    )
    item = woo_product_to_item(prod)
    assert item.name_fr == "Biscuits DUCALES"
    assert item.price_value == 2.89
    assert item.conditions["regular_price"] == 3.29
    assert item.sku == "4367"
    assert item.image_url == "https://www.marcheandes.com/img.jpg"


def test_parse_fr_validity() -> None:
    from grocery_meta_search.sources.official import parse_fr_validity

    assert parse_fr_validity("CIRCULAIRE VALIDE DU 08 AU 21 OCTOBRE 2026", TODAY) == (
        date(2026, 10, 8),
        date(2026, 10, 21),
    )
    assert parse_fr_validity("du 30 septembre au 5 octobre 2026", TODAY) == (
        date(2026, 9, 30),
        date(2026, 10, 5),
    )
    assert parse_fr_validity("valide du 8 au 14 octobre", TODAY) == (
        date(2026, 10, 8),
        date(2026, 10, 14),
    )
    # RapidOCR drops spaces in caps text: the whole header is one token run.
    assert parse_fr_validity("CIRCULAIREVALIDEDU08AU21OCTOBRE 2026", TODAY) == (
        date(2026, 10, 8),
        date(2026, 10, 21),
    )
    assert parse_fr_validity("aucune date ici", TODAY) is None


def test_official_configs_load() -> None:
    configs = load_official_configs()
    assert set(configs) == {
        "3-saisons-fruits-legumes",
        "aliments-merci",
        "baia-dei-formaggi",
        "h-marche",
        "marche-andes",
        "marche-bkr",
        "marche-c-t",
        "marche-korea",
        "marche-sultan",
        "mayrand",
        "milano-fruiterie",
        "pa-nature",
        "wholesale-club",
    }
    assert configs["wholesale-club"].kind == "flyerify"
    assert configs["marche-andes"].kind == "woo_specials"
    assert configs["marche-sultan"].kind == "circulaires"
    assert configs["pa-nature"].kind == "flyerbox"


def _fixture(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


def test_parse_flyers_do_fixture() -> None:
    from grocery_meta_search.sources.official import parse_flyers_do

    parsed = parse_flyers_do(_fixture("official_flyers_do.html"))
    assert parsed is not None
    valid_from, valid_to, first_src = parsed
    assert (valid_from, valid_to) == (date(2026, 10, 8), date(2026, 10, 14))
    assert first_src == "marche-sultan/11/s1.jpg"
    assert parse_flyers_do("<html>no flyer here</html>") is None


def test_flyerbox_meta_fixture() -> None:
    from grocery_meta_search.sources.official import (
        flyerbox_fragment_image,
        flyerbox_meta,
    )

    html_text = _fixture("official_flyerbox.html")
    meta = flyerbox_meta(html_text)
    assert meta is not None
    brochure_id, max_pages, valid_from, valid_to = meta
    assert brochure_id == 144988
    assert max_pages == 4
    assert (valid_from, valid_to) == (date(2026, 10, 12), date(2026, 10, 25))
    img = flyerbox_fragment_image(html_text)
    assert img is not None and "/144988/0.jpg" in img
    assert flyerbox_meta("<html></html>") is None
