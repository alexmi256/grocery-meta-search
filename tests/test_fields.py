"""Package-size extraction cases from the 2026-10-16 visual review."""

from grocery_meta_search.pipeline.fields import extract_package_size


def test_basic_sizes() -> None:
    assert extract_package_size("FRAISES 340G") == "340G"
    assert extract_package_size("JUS D'ORANGE 1.89L") == "1.89L"
    assert extract_package_size("RIZ BASMATI 2 lb") == "2 lb"
    assert extract_package_size("ŒUFS 12 UNITÉS") == "12 UNITÉS"
    assert extract_package_size("POMMES") is None


def test_quebec_gr_abbreviation() -> None:
    # euro-marche / h-marche print "650 GR", "350G" style sizes.
    assert extract_package_size("YOGOURT ACTIVIA 650 GR OU DANINO GO") == "650 GR"
    assert extract_package_size("SAUMON 350G") == "350G"


def test_ranges() -> None:
    assert extract_package_size("FROMAGE 100-154 g") == "100-154 g"
    assert extract_package_size("POULET 125 à 200 g") == "125 à 200 g"
    assert extract_package_size("BŒUF 208-350 g") == "208-350 g"


def test_counts_without_weight() -> None:
    # familiprix / uniprix pack counts carry no weight unit.
    assert extract_package_size("BARRES 40 mini barres 90 gélules molles") is not None
    assert extract_package_size("MÉLATONINE 90 GÉLULES") == "90 GÉLULES"
    assert extract_package_size("DOLE 24 UN.") == "24 UN"  # trailing dot stripped
    assert extract_package_size("VITAMINES 80 capsules") == "80 capsules"
    assert extract_package_size("SIROP 100 ml 24 comprimés") == "100 ml"


def test_weight_beats_count() -> None:
    # M&M-style: the count describes the pieces, the weight is the size.
    assert extract_package_size("CREVETTES 60-70 UNITÉS 907 g") == "907 g"
    assert extract_package_size("MINI-BARRES NESTLÉ, 100 UN., 977 G") == "977 G"


def test_bundle_first_product_wins() -> None:
    # Pharmaprix/Provigo bundles: the item is the first-named product.
    assert extract_package_size("JUS (800 g) ou LAIT (907 g)") == "800 g"
    assert extract_package_size("ACTIVIA 650 g | MINUTE MAID 1,54 L") == "650 g"
    # Single product, decoy early match: trailing size still wins.
    assert extract_package_size("LAIT 2% M.G. 4 L") == "4 L"
