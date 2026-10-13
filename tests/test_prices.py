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
