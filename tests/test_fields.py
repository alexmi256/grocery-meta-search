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


def test_sku_digits_rejected() -> None:
    # Round-2 review: PC-banner OCR names glue the retailer SKU to
    # the unit ("20058163 KG"); a 6+ digit token is never a quantity.
    assert extract_package_size("FILET DE PORC 20058163 KG") is None
    assert extract_package_size("SAUMON 20821339KG") is None
    # A real size in the same name still wins over the SKU candidate.
    assert extract_package_size("FROMAGE 20821339KG 340 g") == "340 g"


def test_protein_callouts_rejected() -> None:
    # Round-2 review: per-portion protein claims are not package
    # sizes (IGA skewers "23g", La Moisson seitan "14g", Perfect Bar).
    assert extract_package_size("BROCHETTES 23G DE PROTÉINES") is None
    assert extract_package_size("SEITAN 14G DE PROTÉINES PAR PORTION") is None
    assert extract_package_size("BARRE 10G PROTEIN") is None
    assert extract_package_size("POUDRE PROTEIN 23G") is None
    # Product-type mentions, not callouts: the size survives.
    assert extract_package_size("BARRE PROTÉINÉE 55 G") == "55 G"
    assert extract_package_size("PROTEIN BAR 55 G") == "55 G"
    # A real size elsewhere in the name still wins.
    assert extract_package_size("YOGOURT 750 G 23G DE PROTÉINES") == "750 G"


def test_implausible_quantities_rejected() -> None:
    # Round-2 review: "1,54 L" stitches stored as "154 L"/"458l".
    assert extract_package_size("JUS 154 L") is None
    assert extract_package_size("BOISSON 458l") is None
    assert extract_package_size("EAU DE SOURCE 18.9 L") == "18.9 L"
    assert extract_package_size("RIZ 20 KG") == "20 KG"
    assert extract_package_size("FARINE 10 KG") == "10 KG"
    # Hardware flyers print real bin capacities; they survive here
    # (the grocery-only harvest stage caps litres more strictly).
    assert extract_package_size("BAC DE RANGEMENT 63 L") == "63 L"
    # Count beside a protein product line is a pack count, not a
    # per-portion protein callout.
    assert extract_package_size("GAUFRES PROTÉINES 8 UN.") == "8 UN"
