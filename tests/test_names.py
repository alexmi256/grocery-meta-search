"""Bilingual name splitting (sources/names.py)."""

from grocery_meta_search.sources.names import split_bilingual_name


def test_fr_en_combined() -> None:
    assert split_bilingual_name("COULIS DE TOMATE BELGUSTO | BELGUSTO TOMATO PASSATA") == (
        "COULIS DE TOMATE BELGUSTO",
        "BELGUSTO TOMATO PASSATA",
    )


def test_en_fr_order_detected() -> None:
    fr, en = split_bilingual_name("LANTIC GRANULATED SUGAR, 2 KG | SUCRE GRANULÉ LANTIC")
    assert fr == "SUCRE GRANULÉ LANTIC"
    assert en == "LANTIC GRANULATED SUGAR, 2 KG"


def test_single_name_untouched() -> None:
    assert split_bilingual_name("croquettes de poulet St-Hubert") == (
        "croquettes de poulet St-Hubert",
        None,
    )
    assert split_bilingual_name(None) == (None, None)
    assert split_bilingual_name("") == (None, None)


def test_lowercase_pair() -> None:
    assert split_bilingual_name("tartinade Nutella | Nutella spread") == (
        "tartinade Nutella",
        "Nutella spread",
    )
