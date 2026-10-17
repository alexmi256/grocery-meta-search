"""Quebec price-text parsing tests."""

from grocery_meta_search.prices import parse_price_text


def test_plain_decimal() -> None:
    assert parse_price_text("2.50") == (2.5, None)


def test_comma_decimal_with_dollar() -> None:
    assert parse_price_text("9,99 $") == (9.99, None)


def test_multibuy_slash() -> None:
    assert parse_price_text("2/5$") == (2.5, "each")


def test_multibuy_pour() -> None:
    assert parse_price_text("2 pour 4$") == (2.0, "each")


def test_multibuy_each_price_rounded_to_cents() -> None:
    # Round-2 review: 4-dp multibuy splits left float tails in the
    # stored pool (1.3333...). Each-prices are money: 2 dp.
    assert parse_price_text("3/4$") == (1.33, "each")
    assert parse_price_text("2/1,99") == (0.99, "each")


def test_per_lb() -> None:
    assert parse_price_text("3,49/lb") == (3.49, "lb")


def test_per_kg() -> None:
    assert parse_price_text("7.99/kg") == (7.99, "kg")


def test_each_alias() -> None:
    assert parse_price_text("1.00/ch") == (1.0, "each")


def test_empty() -> None:
    assert parse_price_text("") == (None, None)
    assert parse_price_text("   ") == (None, None)


def test_no_number() -> None:
    assert parse_price_text("voir en magasin") == (None, None)


def test_split_unit() -> None:
    from grocery_meta_search.prices import split_unit

    assert split_unit(None) == (1.0, "each")
    assert split_unit("each") == (1.0, "each")
    assert split_unit("lb") == (1.0, "pound")
    assert split_unit("kg") == (1.0, "kilogram")
    assert split_unit("100g") == (100.0, "gram")
    assert split_unit("box") == (1.0, "pack")
    assert split_unit("bogus") == (1.0, "each")
    # Multibuy wins over the unit: the price covers that many items.
    assert split_unit("each", 3) == (3.0, "multiple")
    assert split_unit("lb", 2) == (2.0, "multiple")
    assert split_unit("lb", 15998) == (1.0, "pound")  # OCR-garbled count
    assert split_unit("lb", 1) == (1.0, "pound")


def test_multibuy_count() -> None:
    from grocery_meta_search.prices import multibuy_count

    assert multibuy_count({"multibuy": {"count": 2, "total": 5.0}}) == 2
    assert multibuy_count('{"multibuy": {"count": 3, "total": 5.97}}') == 3
    assert multibuy_count({}) is None
    assert multibuy_count(None) is None
    assert multibuy_count("not json") is None
