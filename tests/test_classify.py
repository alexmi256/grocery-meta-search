from grocery_meta_search.classify.rules import classify_item, classify_name


def cat(name: str) -> tuple[str, str] | None:
    hit = classify_name(name)
    return (hit[0], hit[1]) if hit else None


def test_french_names() -> None:
    assert cat("FRAISES FRAÎCHES 340G") == ("Fruits & Vegetables", "Fresh Fruits")
    assert cat("POMMES DE TERRE 10LB") == (
        "Fruits & Vegetables",
        "Fresh Vegetables",
    )
    assert cat("SAUMON FUMÉ 150G") == ("Fish & Seafood", "Smoked Fish")
    assert cat("CAMEMBERT 300G") == ("Dairy & Eggs", "Cheese")
    assert cat("FARINE DE BLÉ ENRICHIE") == ("Pantry", "Baking Essentials")
    assert cat("SAUCISSES ITALIENNES DOUCES") == ("Meat", "Sausages")
    assert cat("THON EN CONSERVE 170G") == ("Pantry", "Canned & Pickled")


def test_english_and_plurals() -> None:
    assert cat("FRESH TOMATOES ON THE VINE") == (
        "Fruits & Vegetables",
        "Fresh Vegetables",
    )
    assert cat("STRAWBERRIES 454G") == ("Fruits & Vegetables", "Fresh Fruits")
    assert cat("CHICKEN BREAST BONELESS") == ("Meat", "Chicken & Turkey")
    assert cat("ORANGE JUICE 1.89L") == ("Drinks", "Juice")


def test_specific_forms_beat_generic() -> None:
    assert cat("BOUILLON DE POULET 900ML") == ("Prepared Meals", "Salads & Soups")
    assert cat("BEURRE D'ARACHIDE CRÉMEUX") == (
        "Pantry",
        "Honey, Syrups & Spreads",
    )
    assert cat("LAIT DE COCO 400ML") == ("Pantry", "Canned & Pickled")
    assert cat("JUS D'ORANGE 1.89L") == ("Drinks", "Juice")
    assert cat("CRÈME GLACÉE VANILLE") == (
        "Frozen Food",
        "Ice Cream & Frozen Desserts",
    )
    assert cat("PIZZA DELISSIO PEPPERONI") == ("Frozen Food", "Frozen Pizza")


def test_non_food() -> None:
    assert cat("DÉTERGENT À LESSIVE TIDE") == (
        "Household",
        "Cleaning & Laundry",
    )
    assert cat("NOURRITURE POUR CHAT 3KG") == ("Pet", "Pet Food")
    assert cat("PAPIER HYGIÉNIQUE 12 ROULEAUX") == (
        "Household",
        "Paper & Storage",
    )


def test_word_boundaries() -> None:
    # "vin" must not fire inside "vinaigre" (an oils/vinegar product).
    assert cat("VINAIGRE DE VIN ROUGE") == ("Pantry", "Oils & Vinegar")
    # "persil" must not fire inside "persillade".
    assert cat("SAUCE PERSILLADE") is None
    # Loyalty-card names must not classify as food (camembert lesson).
    assert cat("MOI PROGRAMME DE FIDÉLITÉ") is None


def test_frozen_remap() -> None:
    dept, sub, method, _ = classify_item("CREVETTES PANÉES SURGELÉES", None, None, "maxi")
    assert (dept, sub) == ("Frozen Food", "Frozen Meat and Seafood")
    assert method == "frozen-remap"
    dept, sub, method, _ = classify_item("PIZZA FRAÎCHE", None, None, "maxi")
    assert (dept, sub) == ("Prepared Meals", "Pizza")
    assert method == "rule"


def test_unclassified() -> None:
    assert classify_name("XYLOPHONE EN PLASTIQUE") is None
    dept, sub, method, _ = classify_item("???", None, None, "maxi")
    assert (dept, sub, method) == ("Unclassified", "Unclassified", "none")


def test_store_prior() -> None:
    dept, sub, method, _ = classify_item("PRODUIT MYSTÈRE 123", None, None, "odessa-poissonnier")
    assert (dept, sub, method) == ("Fish & Seafood", "Fish", "store-prior")


def test_processed_forms_beat_fresh_produce() -> None:
    # 2026-10-16 (user review of the Akhavan report): processed
    # forms must not classify as fresh produce, and lamb beats the
    # generic ribs association with pork.
    assert cat("CONCENTRÉ DE TOMATE") == ("Pantry", "Canned & Pickled")
    assert cat("TOMATO PASTE") == ("Pantry", "Canned & Pickled")
    assert cat("CONFITURE D'ABRICOT") == ("Pantry", "Honey, Syrups & Spreads")
    assert cat("CARROT JAM") == ("Pantry", "Honey, Syrups & Spreads")
    assert cat("CORNICHON À L'AIL PELÉ") == ("Pantry", "Canned & Pickled")
    assert cat("CRUSHED PICKLE") == ("Pantry", "Canned & Pickled")
    assert cat("VINAIGRE DE DATTES") == ("Pantry", "Oils & Vinegar")
    assert cat("CÔTES LEVÉES D'AGNEAU") == ("Meat", "Lamb & Veal")
    assert cat("LAMB RIBS") == ("Meat", "Lamb & Veal")


def test_dried_remap_and_dried_tokens() -> None:
    assert classify_item("PRUNES DÉNOYAUTÉES", "PITTED PRUNES", None, "x")[:2] == (
        "Fruits & Vegetables",
        "Dried Fruits & Nuts",
    )
    assert classify_item("LIMETTES SÉCHÉES", "DRIED WHITE LIME", None, "x")[:2] == (
        "Fruits & Vegetables",
        "Dried Fruits & Nuts",
    )
    assert classify_item("PRUNE HAJ HASSANI", None, None, "x")[:2] == (
        "Fruits & Vegetables",
        "Dried Fruits & Nuts",
    )
    # Fresh produce without a dried marker stays fresh.
    assert classify_item("POMMES FRAÎCHES", None, None, "x")[:2] == (
        "Fruits & Vegetables",
        "Fresh Fruits",
    )


def test_specialty_vocabulary() -> None:
    assert cat("FALAFEL") == ("International Foods", "Middle Eastern Foods")
    assert cat("KASHK") == ("International Foods", "Middle Eastern Foods")
    assert cat("MAHLAB EN POUDRE") == ("Pantry", "Spices & Seasonings")
    assert cat("CITRONNELLE") == ("Fruits & Vegetables", "Fresh Vegetables")
    assert cat("LEMONGRASS") == ("Fruits & Vegetables", "Fresh Vegetables")
    assert cat("BLÉ JAUNE (Durum)") == ("Pantry", "Dried Beans, Vegetables & Grains")
    assert cat("YELLOW SHELLED WHEAT") == (
        "Pantry",
        "Dried Beans, Vegetables & Grains",
    )
    assert cat("THÉ KALAMI") == ("Drinks", "Tea & Hot Drinks")
    assert cat("KALAMI TEA") == ("Drinks", "Tea & Hot Drinks")
    assert cat("CORÉGONE DE LAC") == ("Fish & Seafood", "Fish")
    assert cat("CANADIAN LAKE WHITEFISH") == ("Fish & Seafood", "Fish")
