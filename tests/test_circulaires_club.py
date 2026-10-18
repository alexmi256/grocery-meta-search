"""Golden-sample tests for the circulaires.club discovery client.

No network access: URL parsing and edition selection only.
"""

from datetime import date

from grocery_meta_search.sources.circulaires_club import parse_edition_url


def test_parse_same_month() -> None:
    parsed = parse_edition_url(
        "https://circulaires.club/circulaire/circulaire-marche-bonichoix-du-8-au-14-octobre-2026/"
    )
    assert parsed is not None
    slug, start, end = parsed
    assert slug == "marche-bonichoix"
    assert start == date(2026, 10, 8)
    assert end == date(2026, 10, 14)


def test_parse_cross_month() -> None:
    parsed = parse_edition_url(
        "https://circulaires.club/circulaire/circulaire-costco-du-28-septembre-au-25-octobre-2026/"
    )
    assert parsed is not None
    slug, start, end = parsed
    assert slug == "costco"
    assert start == date(2026, 9, 28)
    assert end == date(2026, 10, 25)


def test_parse_cross_year() -> None:
    parsed = parse_edition_url("https://circulaires.club/circulaire/circulaire-x-du-29-decembre-au-4-janvier-2027/")
    assert parsed is not None
    _, start, end = parsed
    assert start == date(2026, 12, 29)
    assert end == date(2027, 1, 4)


def test_parse_rejects_non_edition() -> None:
    assert parse_edition_url("https://circulaires.club/categorie/alimentation/") is None
    assert parse_edition_url("https://circulaires.club/") is None
