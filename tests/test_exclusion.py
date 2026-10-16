"""Exclusion-layer tests: each layer fires; grocery names are protected."""

from grocery_meta_search.classify.exclusion import exclusion_reason


def test_merch_phrase_fires() -> None:
    assert exclusion_reason("Pneu d'hiver Pirelli", None, None) == "merch:pneu"
    assert exclusion_reason(None, "Paper Towels 6 rolls", None) == (
        "merch:paper towels"
    )


def test_furniture_fires() -> None:
    assert exclusion_reason("Banner - Rollback", None, None) == "furniture:banner"
    assert exclusion_reason("HALAL", None, None) == "furniture:exact"
    assert exclusion_reason("Plus taxes", None, None) == "boilerplate"


def test_supplement_form_fires_but_coffee_capsules_protected() -> None:
    assert (
        exclusion_reason("Vitamine D3 90 capsules", None, None) == "supplement-form"
    )
    # Coffee capsules are a grocery product: never excluded by dosage form.
    assert exclusion_reason("Capsules de café espresso", None, None) is None
    assert exclusion_reason("Nespresso capsules variées", None, None) is None


def test_merged_garble_fires() -> None:
    assert (
        exclusion_reason("Essuietoutnettoyantmultiusage", None, None)
        == "garble:merch-merged"
    )


def test_empty_name() -> None:
    assert exclusion_reason(None, None, None) == "empty"
    assert exclusion_reason("", "  ", None) == "empty"


def test_grocery_names_never_excluded() -> None:
    # Rule vocabulary in the name vetoes exclusion (unclassified tails).
    assert exclusion_reason("Kashk fermenté", None, None) is None
    assert exclusion_reason("Piments shishito frais", None, None) is None
    assert exclusion_reason("Mahlab moulu", None, None) is None
    assert exclusion_reason("Chou vert frisé", None, None) is None
