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


def test_audit_regressions() -> None:
    # Pâtes (pasta) must not land in Deli Meat via the pâté token.
    assert cat("PÂTES ALIMENTAIRES 900G") == ("Pantry", "Pasta & Pasta Sauce")
    # Plain noodles are pasta; instant forms stay Easy Meals.
    assert cat("NOUILLES AUX ŒUFS") == ("Pantry", "Pasta & Pasta Sauce")
    assert cat("NOUILLES INSTANTANÉES SAVEUR POULET") == (
        "Pantry",
        "Easy Meals & Sides",
    )
    # Snack bars are not sea bass.
    assert cat("BARRE PROTÉINÉE AUX ARACHIDES") == ("Pantry", "Cereal & Breakfast")
    assert cat("PROTEIN BAR CHOCOLATE") == ("Pantry", "Cereal & Breakfast")
    # Rice noodles belong with pasta, not East Asian.
    assert cat("VERMICELLES DE RIZ 400G") == ("Pantry", "Pasta & Pasta Sauce")
    # Rôti (roast) is not roti (flatbread).
    assert cat("RÔTI DE PALETTE DÉSOSSÉ") == ("Meat", "Beef")
    # Coffee creamer is not coffee.
    assert cat("REHAUSSEUR DE CAFÉ INTERNATIONAL DELIGHT") == (
        "Dairy & Eggs",
        "Milk & Cream",
    )
    # Kraft Dinner is an easy meal, not pasta sauce or cheese.
    assert cat("MACARONI ET FROMAGE KRAFT DINNER") == (
        "Pantry",
        "Easy Meals & Sides",
    )


def test_audit_classify_item() -> None:
    # Supplements split from OTC pharmacy.
    assert classify_item("MÉLATONINE 10MG 90 COMPRIMÉS", None, None, "maxi")[:2] == (
        "Health & Beauty",
        "Vitamins & Supplements",
    )
    assert classify_item("PROBIOTIQUES 30 MILLIARDS", None, None, "maxi")[:2] == (
        "Health & Beauty",
        "Vitamins & Supplements",
    )
    assert classify_item("BENYLIN SIROP CONTRE LA TOUX", None, None, "maxi")[:2] == (
        "Health & Beauty",
        "Pharmacy",
    )
    # Banner/junk lines never classify, even under a store prior.
    dept, sub, method, _ = classify_item(": SPECIAL", None, None, "monde-au-naturel")
    assert (dept, method) == ("Unclassified", "junk")
    dept, sub, method, _ = classify_item("BANNER ROLLBACK", None, None, "walmart")
    assert (dept, method) == ("Unclassified", "junk")
    # Thawed (décongelé) fish is fresh, not frozen.
    assert classify_item("POMPANO DÉCONGELÉ", None, None, "maxi")[:2] == (
        "Fish & Seafood",
        "Fish",
    )
    # Frozen prepared pizza remaps to Frozen Pizza.
    assert classify_item("PIZZA SURGELÉE TOUTE GARNIE", None, None, "maxi")[:2] == (
        "Frozen Food",
        "Frozen Pizza",
    )
    # Frozen fries remap to Frozen Fruit & Vegetables.
    assert classify_item("FRITES SURGELÉES 2KG", None, None, "maxi")[:2] == (
        "Frozen Food",
        "Frozen Fruit & Vegetables",
    )
    # Cat litter is Pet Supplies, not Pet Food.
    assert classify_item("LITIÈRE AGGLOMÉRANTE 14KG", None, None, "maxi")[:2] == (
        "Pet",
        "Pet Supplies",
    )


def test_round2_traps() -> None:
    """2026-10-16 round-2 visual review: context tokens that outranked
    the product token, and the vocabulary the sample proved missing."""
    c = classify_item
    # Halloween pumpkin decorations and oyster tools are merchandise.
    assert c(
        "Citrouille lanterne avec œil d'araignée animée",
        None,
        None,
        "canadian-tire",
    )[0] == "Household"
    assert c("PLANCHE À HUÎTRES", None, None, "odessa-poissonnier")[0] == "Household"
    # Chocolate pumpkins are candy.
    assert c(
        "FREDDO, Citrouilles, Chocolat au lait avec centre de caramel, 390 g",
        None,
        "FREDDO",
        "familiprix",
    )[1] == "Candy & Chocolate"
    # Contact-lens solution is pharmacy, not dried beans.
    assert c(
        "Bausch + Lomb Biotrue solution pour lentilles cornéennes 300ml",
        None,
        None,
        "familiprix",
    )[1] == "Pharmacy"
    # Laundry water is cleaning, not drinking water.
    assert c(
        "SOJA & CO. Eaux de linge choisies",
        None,
        None,
        "jean-coutu",
    )[1] == "Cleaning & Laundry"
    # A steeped-tea K-Cup is tea despite the coffee-pod format tokens.
    assert c(
        "Dosettes K-Cup® de thé infusé Tim Hortons, 30 un Keurig",
        None,
        "Keurig",
        "canadian-tire",
    )[1] == "Tea & Hot Drinks"
    # Juicing carrots (flyer typo included) are produce.
    assert c(
        "CARROTTES A JUS ECONOMIQUES BIO",
        None,
        None,
        "coop-alentour",
    )[1] == "Fresh Vegetables"
    assert c(
        "CAROTTES A JUS ECONOMIQUES BIO".replace("CAROTTES", "CARROTES"),
        None,
        None,
        "coop-alentour",
    )[1] == "Fresh Vegetables"
    # "Sandwich steak" is a beef cut; oyster sauce is a condiment.
    assert c(
        "BIFTECK ATTENDRI OU SANDWICH TENDERIZED OR SANDWICH STEAK",
        None,
        None,
        "marche-bonichoix",
    )[1] == "Beef"
    assert c("Sauce aromatisee aux huitres panda", None, None, "marche-c-t")[1] == "Condiments"
    # Beef ribs (glued "deboeuf") are beef; coffee beans are coffee.
    assert c("Cotes levees deboeuf Decongelé", None, None, "marche-c-t")[1] == "Beef"
    assert c("CAFE EN GRAINS OU MOULU", None, None, "marche-esposito")[1] == "Coffee"
    # Frozen corn dogs leave the vegetable department.
    assert c("COMPLIMENTS FROZEN CORN DOGS", None, None, "marches-tradition")[0] == "Frozen Food"
    # Canned tomato forms are canned, incl. passata (no pizza-brand steal).
    assert c("Tomates entieres peles 6x796ml", None, None, "frutta-si")[1] == "Canned & Pickled"
    assert c("BURCU PATE DE TOMATE 800G", None, None, "marche-bkr")[1] == "Canned & Pickled"
    assert c("RENDE DOMATES PASSATA RUSTICA", None, None, "marche-sultan")[1] == "Canned & Pickled"
    # Soy-marinated crab is seafood.
    assert c("KOBON Soy Sauce Marinated Crab", None, None, "marche-korea")[1] == "Shellfish"
    # A yogurt named yogurt is yogurt, plant-based or not.
    assert c(
        "SILK YOGOURTABASEDEPLANTES PLANT BASED YOGURT",
        None,
        None,
        "marches-tau",
    )[1] == "Yogurt"
    # Halloween candy bars are candy, not home goods.
    assert c(
        "MINTBARS D'HALLOWEEN SAVEURS MIXTES | UNREAL | X26",
        None,
        None,
        "shop-sante",
    )[1] == "Candy & Chocolate"
    # Takeout coffee boxes are paper goods.
    assert c(
        "BOÎTES CAFÉ EXPRESS EN KRAFT PE 8-32 OZ., 50 UN.",
        None,
        None,
        "wholesale-club",
    )[1] == "Paper & Storage"
    # Vocabulary the round-2 sample proved missing.
    assert c("PÂTE PHYLLO LILAS", None, "LILAS", "adonis")[1] == "Baking Essentials"
    assert c(
        "PÂTE FILO SURGELÉE ELZYMI",
        None,
        "ELZYMI",
        "adonis",
    )[1] == "Frozen Bakery & Breakfast"
    assert c(
        "VOL-AU-VENT ST-HUBERT PASTRY SHELLS",
        None,
        None,
        "marche-bonichoix",
    )[1] == "Frozen Appetizers & Snacks"
    assert c(
        "RAVIOLI OU TORTELLINI VILLA RAVIOLI",
        None,
        None,
        "marche-bonichoix",
    )[1] == "Fresh Pasta & Sauce"
    assert c(
        "PÂTÉ ST-HUBERT | ST-HUBERT POT PIE",
        None,
        "ST-HUBERT",
        "marche-richelieu",
    )[1] == "Quiches & Pies"
    assert c("PÂTÉ, TERRINE OU MOUSSE, 125/150 G", None, None, "maxi")[1] == "Deli Meat"
    assert c("HACHE EXTRA MAIGRE", None, None, "marche-bkr")[1] == "Beef"
    assert c("DE BCEUF HACHE MI-MAIGRE", None, None, "marche-bonichoix")[1] == "Beef"
    assert c("GREEN WORLD MOLOKHIA 400G", None, None, "marche-bkr")[1] == "Fresh Vegetables"
    assert c("MAKDOUCE", None, None, "marche-bkr")[1] == "Canned & Pickled"
    assert c("CUISSES DE GRENOUILLE | Frog Legs", None, None, "marche-pa")[0] == "Fish & Seafood"
    assert c("POIVRE VERT | Green Peppercorns", None, None, "marche-pa")[1] == "Spices & Seasonings"
    assert c("SWEETCORN", None, None, "marche-sultan")[1] == "Fresh Vegetables"
    assert c("DEMLIK 40POSET", None, None, "marche-sultan")[1] == "Tea & Hot Drinks"
    assert c("Pâte de soja assaisonnée 500g", None, None, "marche-korea")[1] == "East Asian Foods"
    assert c(
        "BLOOM BOISSON ENERGETIQUE NATURELLE",
        None,
        None,
        "marches-tau",
    )[1] == "Sports & Energy"
    assert c(
        "LIFE SMART NATURALIA ALMOND BEVERAGE",
        None,
        None,
        "metro",
    )[1] == "Non-Dairy Milk Alternatives"
    assert c(
        "CHAUSSONS CHEF DUMAS | CHEF DUMAS TURNOVERS",
        None,
        None,
        "metro",
    )[1] == "Cookies, Muffins & Desserts"
    assert c(
        "DÎNER SELECTION | SELECTION FROZEN MEAL",
        None,
        None,
        "metro",
    )[1] == "Frozen Meals, Entrees & Sides"
    assert c(
        "BARRES GO PURE OU CHOCOMAX LECLERC",
        None,
        "Leclerc",
        "maxi",
    )[1] == "Cereal & Breakfast"
    assert c("TreStelle PARMIGIANO REGGIANO", None, None, "mayrand")[1] == "Cheese"
    assert c("BOISSON FRUITÉ | FRUITÉ DRINK", None, None, "super-c")[1] == "Juice"
    assert c("SAUCE FRANK'S REDHOT", None, None, "super-c")[1] == "Condiments"
    assert c(
        "BOISSON PÉTILLANTE FEVER-TREE | SPARKLING DRINK",
        None,
        None,
        "metro-plus",
    )[1] == "Soft Drinks"
    assert c(
        "CHAPELURE SELECTION | SELECTION BREADCRUMB",
        None,
        None,
        "metro",
    )[1] == "Baking Essentials"
    assert c("biscuit Lu pim's ou Pepito", None, None, "adonis")[1] == "Crackers & Cookies"
    assert c(
        "Cham Biscuit au Gingembre 250g",
        None,
        None,
        "marche-korea",
    )[1] == "Crackers & Cookies"
    assert c("FRESHTODAY Real Carrot Bread", None, None, "marche-korea")[1] == "Bread"
    assert c(
        "Orville Redenbacher 492 g",
        "Maïs à éclaté BoomChickaPop de Angie's 136 g",
        "ORVILLE REDENBACHER",
        "walmart",
    )[1] == "Chips & Snacks"
    # The sugar-reduction campaign banner is junk, not baking.
    dept, sub, method, _ = c("Réduire le sucre: défi accepté!", None, None, "avril")
    assert (dept, method) == ("Unclassified", "junk")


def test_round2_barres_collateral() -> None:
    """The bare 'barres' phrase must not steal veal, dairy bars,
    ice-cream bars or barcode instructions."""
    c = classify_item
    assert c("VEAU HACHÉ MAIGRE", None, None, "iga")[1] == "Lamb & Veal"
    assert c("BARRES DE YOGOURT PC MENU BLEU, 6x80 mL", None, None, "maxi")[1] == "Yogurt"
    assert c("BARRES DE FROMAGE SAPUTO, 1 KG", None, None, "maxi")[1] == "Cheese"
    assert c(
        "Chapman's barres de crème glacée",
        None,
        None,
        "walmart",
    )[1] == "Ice Cream & Frozen Desserts"
    assert c(
        "BARRES DE CHOCOLAT NESTLÉ, 24 UN.",
        None,
        None,
        "wholesale-club",
    )[1] == "Candy & Chocolate"
    dept, sub, method, _ = c(
        "Étape 1: Enregistrer ce code-barres pour le scanner",
        None,
        None,
        "pharmaprix",
    )
    assert (dept, method) == ("Unclassified", "junk")


def test_pumpkin_candy_and_decorations_are_not_produce() -> None:
    """Chocolate/marshmallow pumpkins are Halloween candy and pumpkin
    lanterns/inflatables/carving kits are merchandise; only a bare
    pumpkin is produce (jean-coutu review, 2026-10-17; GT token-trap
    verdicts). Guards are scoped to Fresh Vegetables so pumpkin-spice
    coffee and pumpkin pie keep their existing shelves."""
    c = classify_item
    for name, brand, store in (
        ("FREDDO, Citrouilles, Chocolat au lait avec centre de caramel, 390 g",
         "FREDDO", "familiprix"),
        ("FREDDO Citrouilles en chocolat au caramel", "FREDDO", "jean-coutu"),
        ("CITROUILLES CHOCOLATÉES SELECTION", None, "metro"),
        ("BRANDS UNLIMITED, Citrouilles en guimauve, 50 unités", "BRANDS UNLIMITED", "familiprix"),
        ("CARNABY SWEET Suçon en chocolat belge en forme de fantôme ou citrouille",
         None, "pharmaprix"),
        ("CONFISERIES REGAL Citrouilles en chocolat", None, "uniprix"),
        ("FREDDO Citrouilles", "FREDDO", "familiprix"),
    ):
        dept, sub, _, _ = c(name, None, brand, store)
        assert (dept, sub) == ("Snacks, Chips & Candy", "Candy & Chocolate"), name
    # The short forms hit Fresh Vegetables first and need the guard.
    for name, brand, store in (
        ("FREDDO Citrouilles en chocolat au caramel", "FREDDO", "jean-coutu"),
        ("CITROUILLES CHOCOLATÉES SELECTION", None, "metro"),
        ("FREDDO Citrouilles", "FREDDO", "familiprix"),
    ):
        _, _, method, _ = c(name, None, brand, store)
        assert method == "guard-remap", name
    for name, store in (
        ("Citrouille lanterne gonflable", "canadian-tire"),
        ("Citrouilles lanternes empilées gonflables, 8 pi", "canadian-tire"),
        ("PUMPKIN MASTERS Ensemble de découpe de citrouille", "pharmaprix"),
    ):
        dept, sub, _, _ = c(name, None, None, store)
        assert (dept, sub) == ("Household", "Home Goods"), name
    # Not swept up: real pumpkins, pumpkin pie, pumpkin-spice coffee.
    assert c("Grosse citrouille", None, None, "walmart")[:2] == (
        "Fruits & Vegetables", "Fresh Vegetables")
    assert c("Capsules K-Cup de café Starbucks caramel ou citrouille épicée",
             None, "Starbucks", "walmart")[:2] == ("Drinks", "Coffee")
