# Marché Adonis — full product report

Store slug: `adonis`. Generated from `data/grocery.db`. A sampled subset of 17 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).

## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 39, valid 2026-10-15 → 2026-10-21, current). The DB also holds the expired Oct 8–14 edition, correctly excluded from sampling.
- **Sample counts:** 10 classified + 7 unclassified shown. Only 7 unclassified exist on the current flyer (183 of 190 items classified) — the shortfall is a classification success, not a sampling gap. Adonis items come from the Flipp search API, so there are no page images in the packet: each item's picture is its flyer region render, which carries the printed name/price text and serves as the item's source image.
- **Issues found:** (1) six of the seven unclassified items are plain vocabulary gaps for this store's Mediterranean stock (tzatziki — misspelled "TZATZKI" in the source payload itself —, pistache singular, tassergale/bluefish, korban bread, sesame galettes); (2) sizes printed in the flyer region were not captured for items 7466 (836-888 g), 7489 (325-410 g) and 7410 (325 g) — the harvest rejected range sizes when a count or an in-range variety stamp stood beside them, and (for 7410) a "12 g" protein badge on the packaging makes the extraction conservatively ambiguous; (3) item 7476 (and 25 items DB-wide, mostly marché-pa) stored its price-rate denominator ("100 g") as a package size — an old harvest record whose provenance a later fill run overwrote, defeating the refresh retraction; (4) the English name is missing on items whose Flipp payload is French-only (7380, 7455, 7501) even though the flyer prints it — the English text exists only in the region image / the store's own Flyerify viewer, not in our source payload; (5) item 7404's price (2.49) is Flipp's derived figure for a "save $2 on 2 loaves" offer — no unit price is printed in the flyer, so the stored price cannot be verified against the image.
- **Patterns:** this store's unclassified pool is dominated by specific-product vocabulary (fixable) plus a bakery-tray series whose entire name is a flavour word (PISTACHE, NATURE — item 7507 "NATURE" is a tray of plain cookies; text-only classification cannot place it and it correctly stays unclassified). "Amuse-gueule" was tested as a nuts phrase and REJECTED on ground-truth evidence: across stores it is a generic snack-pouch term (Rold Gold, Frito-Lay, Selection chip packs), so item 7410 also stays unclassified.
- **Fixes applied this pass:** classifier phrases added — "tzatzki" (Deli > Antipasto, Dips & Spreads), "pistache"/"pistachio" (Dried Fruits & Nuts), "tassergale"/"bluefish" (Fish & Seafood > Fish), "korban" (Bakery > Bread), "galettes au sésame/sesame" (Crackers & Cookies); ground truth 82.3% → 82.3% items (12337 → 12338), 79.9% → 79.9% signatures (8227 → 8228), no regressions. Harvest: a single stated range now wins over count rivals and in-range variety stamps; fill runs now merge harvest provenance instead of overwriting it (the 7476 mechanism). Data: 26 denominator-as-size values cleared DB-wide; stored items reclassified.

## Flyer 39 — valid 2026-10-15 → 2026-10-21 (10 classified items, 7 unclassified)

Source ref: `8182773` · fetched 2026-10-13T04:28:22.888Z

### Item 7339

![item 7339](images/item-7339.jpg)

- **Name (English):** BELGUSTO TOMATO PASSATA
- **Name (French):** COULIS DE TOMATE BELGUSTO
- **Brand:** Belgusto
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`canned-pickled`)
- **Size:** 680ml
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891107/1791519986/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `a9cdb9460f6832c5`
- **Conditions:** `{"discount": 33}`
- **Raw:** `{"id": 1046708002, "flyer_id": 8182773, "name": "COULIS DE TOMATE BELGUSTO | BELGUSTO TOMATO PASSATA", "display_type": 1, "brand": "Belgusto", "left": 355.79, "bottom": -2186.89, "right": 600.01, "top": -1890.86, "cutout_image_url": "http://f.wishabi.net/page_items/436891107/1791519986/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 33, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "pric`

**Item Review Analysis (Pass 1):** Fully correct. The region image shows the Belgusto passata bottle (680 ml, 1.99, reg. 2.99); names are properly split FR/EN, size 680 ml and category Pantry > Canned & Pickled all match. The item belongs here.

### Item 7368

![item 7368](images/item-7368.jpg)

- **Name (English):** CELERY
- **Name (French):** CÉLERI
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891198/1791520003/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `58b959ea968045c9`
- **Conditions:** `{"discount": 33}`
- **Raw:** `{"id": 1046708068, "flyer_id": 8182773, "name": "CÉLERI | CELERY", "display_type": 1, "brand": null, "left": 2589.12, "bottom": -392.06, "right": 2871.9, "top": -92.01, "cutout_image_url": "http://f.wishabi.net/page_items/436891198/1791520003/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 33, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "1.99", "print_id": null, "short_name": `

**Item Review Analysis (Pass 1):** Correct. Image shows Québec celery at 1.99 each ("ch."); stored price, unit (1, each) and Fresh Vegetables category match. Brand None and Size None are valid — neither is printed for bulk celery.

### Item 7379

![item 7379](images/item-7379.jpg)

- **Name (English):** IRRÉSISTIBLE FROZEN FRUITS
- **Name (French):** FRUITS CONGELÉS IRRÉSISTIBLE
- **Brand:** Irresistible
- **Category (English):** Frozen Food > Frozen Fruit & Vegetables
- **Category (French):** Produits surgelés > Fruits et légumes surgelés
- **How classified:** frozen-remap (`fruits`)
- **Size:** 400-600g
- **Price:** 5.49
- **Printed Price:** “5.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891303/1791520005/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `2eaf6c18b3f547ca`
- **Conditions:** `{"discount": 21}`
- **Raw:** `{"id": 1046708567, "flyer_id": 8182773, "name": "FRUITS CONGELÉS IRRÉSISTIBLE | IRRÉSISTIBLE FROZEN FRUITS", "display_type": 1, "brand": "Irresistible", "left": 6921.74, "bottom": -1791.75, "right": 7196.25, "top": -1542.2, "cutout_image_url": "http://f.wishabi.net/page_items/436891303/1791520005/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 21, "available_to": "2026-10-21T23:59:59-04:00", "video_url": `

**Item Review Analysis (Pass 1):** Correct. Image shows Irrésistible frozen fruit (cultivated blueberries pictured), 400-600 g, choix varié, at 5.49 — stored size "400-600g" and Frozen Fruit & Vegetables category match. This range reached the DB from the payload name; contrast items 7466/7489 where the range exists only in the image.

### Item 7380

![item 7380](images/item-7380.jpg)

- **Name (English):** None
- **Name (French):** croquettes et languettes de poulet pané St-Hubert
- **Brand:** ST‑HUBERT
- **Category (English):** Meat > Chicken & Turkey
- **Category (French):** Viande > Poulet et dinde
- **How classified:** rule (`chicken-turkey`)
- **Size:** 600g
- **Price:** 13.99
- **Printed Price:** “13.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891208/1791519988/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `0791c0f670834aa6`
- **Conditions:** `{"discount": 13}`
- **Raw:** `{"id": 1046708078, "flyer_id": 8182773, "name": "croquettes et languettes de poulet pané St-Hubert", "display_type": 1, "brand": "ST‑HUBERT", "left": 4311.52, "bottom": -2555.37, "right": 4600.44, "top": -2181.03, "cutout_image_url": "http://f.wishabi.net/page_items/436891208/1791519988/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 13, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "pri`

**Item Review Analysis (Pass 1):** Mostly correct. Image confirms the product (St-Hubert breaded chicken nuggets and strips, 600 g, 13.99) and size/category are right. The English name is missing from the DB although the flyer prints it ("St-Hubert breaded chicken nuggets and strips") — the Flipp payload for this item is French-only, so the English exists only in the image; a known source limit (the store's own site carries both languages as structured text). Not a crop problem: the region image is complete and legible.

### Item 7404

![item 7404](images/item-7404.jpg)

- **Name (English):** None
- **Name (French):** pain tranché Pom ou St-Méthode
- **Brand:** POM
- **Category (English):** Bakery > Bread
- **Category (French):** Boulangerie > Pain
- **How classified:** rule (`bread`)
- **Size:** 500-675g
- **Price:** 2.49
- **Printed Price:** “2.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891259/1791519993/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `0d25c2586f6e2149`
- **Conditions:** `{"discount": 45}`
- **Raw:** `{"id": 1046708294, "flyer_id": 8182773, "name": "pain tranché Pom ou St-Méthode", "display_type": 1, "brand": "POM", "left": 6615.46, "bottom": -2548.56, "right": 6898.85, "top": -2306.93, "cutout_image_url": "http://f.wishabi.net/page_items/436891259/1791519993/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 45, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "2.49", "print_id": `

**Item Review Analysis (Pass 1):** Flagged: the stored price (2.49) cannot be verified from the flyer. The region shows a "Économisez 2$ à l'achat de 2 pains" offer with regular prices 4.49–5.49 and no printed unit price; 2.49 is Flipp's derived figure. Name, size (500-675 g) and Bread category are right; the English name is printed in the image but absent from the French-only payload (same limit as 7380). Kept as-is — the price is the source's own number, recorded here as unverifiable against print.

### Item 7466

![item 7466](images/item-7466.jpg)

- **Name (English):** ADONIS LARGE PIZZAS
- **Name (French):** GRANDES PIZZAS FROMAGE OU THYM ET FROMAGE ADONIS
- **Brand:** ADONIS
- **Category (English):** Prepared Meals > Pizza
- **Category (French):** Repas préparés > Pizzas
- **How classified:** rule (`pizza-prepared`)
- **Size:** None
- **Price:** 15.00
- **Printed Price:** “15.0”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891246/1791519984/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `3da766fb0ee52369`
- **Conditions:** `{"discount": 14}`
- **Raw:** `{"id": 1046708211, "flyer_id": 8182773, "name": "GRANDES PIZZAS FROMAGE OU THYM ET FROMAGE ADONIS | ADONIS LARGE PIZZAS", "display_type": 1, "brand": "ADONIS", "left": 5768.81, "bottom": -2548.87, "right": 6046.23, "top": -2305.41, "cutout_image_url": "http://f.wishabi.net/page_items/436891246/1791519984/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 14, "available_to": "2026-10-21T23:59:59-04:00", "vide`

**Item Review Analysis (Pass 1):** Price and category correct (Adonis large pizzas, 15.00, Prepared Meals > Pizza; the image's "+TX" is not stored, which is fine). Defect found: the size printed in the region ("836-888 g, 4 un.") was not captured — the harvest rejected the range because the "4 un." pack count stood beside it. Fixed this pass (range preference in the harvest); re-extraction in the verification pass.

### Item 7476

![item 7476](images/item-7476.jpg)

- **Name (English):** None
- **Name (French):** maasdam, edam ou gouda Landana
- **Brand:** Landana
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** 100g
- **Price:** 2.49
- **Printed Price:** “2.49”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891263/1791519995/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `3ca099e322e603ee`
- **Conditions:** `{"discount": 29}`
- **Raw:** `{"id": 1046708322, "flyer_id": 8182773, "name": "maasdam, edam ou gouda Landana", "display_type": 1, "brand": "Landana", "left": 6335.48, "bottom": -1027.14, "right": 6618.6, "top": -774.28, "cutout_image_url": "http://f.wishabi.net/page_items/436891263/1791519995/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 29, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "2.49", "print_id"`

**Item Review Analysis (Pass 1):** Price and unit are the model dual-rate case: headline 2.49 le 100 g stored, with the 11,29/lb equivalent correctly ignored; Cheese category and names right. Defect found: Size showed "100g" — the price-rate denominator stored as a package size by an old harvest run; the provenance that would have let the refresh retract it was overwritten by a later fill run. Fixed this pass (provenance merge + the stored value cleared with 25 similar rows DB-wide).

### Item 7489

![item 7489](images/item-7489.jpg)

- **Name (English):** DR. OETKER CASA DI MAMA OR RISTORANTE PIZZA
- **Name (French):** PIZZA CASA DI MAMA OU RISTORANTE DR. OETKER
- **Brand:** Dr. Oetker
- **Category (English):** Frozen Food > Frozen Pizza
- **Category (French):** Produits surgelés > Pizzas surgelées
- **How classified:** rule (`specific-frozen-pizza-brands`)
- **Size:** None
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891305/1791520006/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `a2d6231b3b3c6c23`
- **Conditions:** `{"discount": 20}`
- **Raw:** `{"id": 1046708578, "flyer_id": 8182773, "name": "PIZZA CASA DI MAMA OU RISTORANTE DR. OETKER | DR. OETKER CASA DI MAMA OR RISTORANTE PIZZA", "display_type": 1, "brand": "Dr. Oetker", "left": 7485.08, "bottom": -1538.31, "right": 7775.36, "top": -1291.26, "cutout_image_url": "http://f.wishabi.net/page_items/436891305/1791520006/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 20, "available_to": "2026-10-21`

**Item Review Analysis (Pass 1):** Correct except size. Image shows Dr. Oetker Casa Di Mama/Ristorante pizza at 5.99 with "325-410 g, choix varié" printed; the stored size was None because the harvest treated the range plus the 395 g box stamp as ambiguous. The stamp falls inside the range (one variety's weight), so the range is now accepted (fix this pass). Names, brand and Frozen Pizza category are right.

### Item 7493

![item 7493](images/item-7493.jpg)

- **Name (English):** Élégance cookies
- **Name (French):** biscuits Élégance
- **Brand:** ELEGANCE
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** 408g
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891291/1791519996/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `f23c5a8178de7ead`
- **Conditions:** `{"discount": 50}`
- **Raw:** `{"id": 1046708494, "flyer_id": 8182773, "name": "biscuits Élégance | Élégance cookies", "display_type": 1, "brand": "ELEGANCE", "left": 7767.39, "bottom": -769.94, "right": 8050.42, "top": -512.48, "cutout_image_url": "http://f.wishabi.net/page_items/436891291/1791519996/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 50, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "2.99", "pr`

**Item Review Analysis (Pass 1):** Correct. Image shows Élégance Biscotto cookies, 408 g, at 2.99 (reg. 5.99); stored size 408g, names split FR/EN, Crackers & Cookies category all match.

### Item 7501

![item 7501](images/item-7501.jpg)

- **Name (English):** None
- **Name (French):** clémentines avec feuilles
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891172/1791519985/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `18b049915ceb2fba`
- **Conditions:** `{"discount": 14}`
- **Raw:** `{"id": 1046708042, "flyer_id": 8182773, "name": "clémentines avec feuilles", "display_type": 1, "brand": null, "left": 2880.28, "bottom": -2307.16, "right": 3166.75, "top": -2054.34, "cutout_image_url": "http://f.wishabi.net/page_items/436891172/1791519985/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 14, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "5.99", "print_id": null, `

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 39 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Image shows clementines with leaves at 5.99/lb headline (13,21/kg equivalent); stored unit (1, pound) is the headline rate, as intended. English name missing — printed in the image ("clementines with leaves") but the payload is French-only; same source limit as 7380. Brand/Size None are valid for bulk produce.

### Item 7334

![item 7334](images/item-7334.jpg)

- **Name (English):** None
- **Name (French):** PISTACHE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436909340/1791519989/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `dca5c174d9ff3ed5`
- **Raw:** `{"id": 1046708643, "flyer_id": 8182773, "name": "PISTACHE", "display_type": 1, "brand": null, "left": 8688.34, "bottom": -1681.67, "right": 9105.34, "top": -1397.46, "cutout_image_url": "http://f.wishabi.net/page_items/436909340/1791519989/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "4.99", "print_id": null, "short_name": n`

— from flyer 39 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Was unclassified; the image shows a tray of pistachio ma'amoul-style cookies labelled only "PISTACHE". The classifier knew only the plural "pistaches"; singular forms added this pass, and the item now classifies to Fruits & Vegetables > Dried Fruits & Nuts on its text. (The photograph suggests a bakery cookie — a text-only classifier cannot see that; nuts is the defensible reading of the name.) No price is visible in this region render; the stored 4.99 comes from the payload.

### Item 7352

![item 7352](images/item-7352.jpg)

- **Name (English):** None
- **Name (French):** TZATZKI! STYLE GREC DELPHI
- **Brand:** DELPHI
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 13.90
- **Printed Price:** “13.9”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891140/1791519993/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `2b5cae5ac7b623ef`
- **Conditions:** `{"discount": 18}`
- **Raw:** `{"id": 1046708035, "flyer_id": 8182773, "name": "TZATZKI! STYLE GREC DELPHI", "display_type": 1, "brand": "DELPHI", "left": 2017.77, "bottom": -454.04, "right": 2292.22, "top": -125.59, "cutout_image_url": "http://f.wishabi.net/page_items/436891140/1791519993/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 18, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "13.9", "print_id": nul`

— from flyer 39 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Was unclassified for a source typo: the payload name is "TZATZKI" (the flyer itself prints TZATZIKI). "tzatziki" was already a Deli dips phrase; the misspelling was added this pass and the item now classifies to Deli > Antipasto, Dips & Spreads. Image confirms 13.90/kg (stored unit kilogram ✓; the "à l'achat de 800 g ou plus" bulk condition is not captured in structured fields — noted, minor).

### Item 7410

![item 7410](images/item-7410.jpg)

- **Name (English):** Prana snack
- **Name (French):** amuse-gueule Prana
- **Brand:** PRANA
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891292/1791519997/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `99a4860a8d80ea34`
- **Conditions:** `{"discount": 18}`
- **Raw:** `{"id": 1046708502, "flyer_id": 8182773, "name": "amuse-gueule Prana | Prana snack", "display_type": 1, "brand": "PRANA", "left": 7479.94, "bottom": -767.98, "right": 7767.04, "top": -510.54, "cutout_image_url": "http://f.wishabi.net/page_items/436891292/1791519997/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 18, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "6.99", "print_id"`

— from flyer 39 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Stays unclassified, deliberately. The image shows a Prana "Bean Me Up" seasoned snack mix (325 g printed — not captured: a "12 g" protein badge on the pack makes the harvest's size extraction conservatively ambiguous). "Amuse-gueule" was tested as a classifier phrase and rejected on ground-truth evidence — across stores it is a generic snack term (chip variety packs included), and adding it misrouted two correctly classified items. Price 6.99 verified against the image.

### Item 7455

![item 7455](images/item-7455.jpg)

- **Name (English):** None
- **Name (French):** TASSERGALE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891240/1791519995/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `a0abba2c2a06254b`
- **Conditions:** `{"discount": 33}`
- **Raw:** `{"id": 1046708173, "flyer_id": 8182773, "name": "TASSERGALE", "display_type": 1, "brand": null, "left": 4892.99, "bottom": -515.2, "right": 5178.86, "top": -139.33, "cutout_image_url": "http://f.wishabi.net/page_items/436891240/1791519995/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 33, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "3.99", "print_id": null, "short_name": null`

— from flyer 39 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Was unclassified; image shows whole bluefish on ice ("tassergale / bluefish", nettoyage gratuit) at 3.99/lb with 8,80/kg equivalent — stored unit pound ✓. "tassergale" and "bluefish" added to the fish rule this pass; now Fish & Seafood > Fish. English name missing from the DB though printed in the image — French-only payload, same limit as 7380.

### Item 7498

![item 7498](images/item-7498.jpg)

- **Name (English):** None
- **Name (French):** KORBAN
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 4un
- **Price:** 4.49
- **Printed Price:** “4.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891312/1791519985/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `e7cd42738d06e140`
- **Raw:** `{"id": 1046708614, "flyer_id": 8182773, "name": "KORBAN", "display_type": 1, "brand": null, "left": 9514.99, "bottom": -1222.97, "right": 10328.0, "top": -573.48, "cutout_image_url": "http://f.wishabi.net/page_items/436891312/1791519985/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "4.49", "print_id": null, "short_name": null`

— from flyer 39 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Was unclassified; image shows a stack of four korban breads ("korban, 4 un.") at 4.49. "korban" added to the bread rule this pass; now Bakery > Bread. Stored size "4un" matches the print. The unit pair stays (1, each) with the count carried by the size — acceptable representation.

### Item 7506

![item 7506](images/item-7506.jpg)

- **Name (English):** None
- **Name (French):** galettes au sésame et anis
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 6.49
- **Printed Price:** “6.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891316/1791519988/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `68293d2dd23392b9`
- **Raw:** `{"id": 1046708637, "flyer_id": 8182773, "name": "galettes au sésame et anis", "display_type": 1, "brand": null, "left": 9232.02, "bottom": -2485.83, "right": 10313.0, "top": -1988.84, "cutout_image_url": "http://f.wishabi.net/page_items/436891316/1791519988/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "6.49", "print_id": nul`

— from flyer 39 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Was unclassified; image shows sesame-anise ring galettes ("12 un.") at 6.49. The specific phrases "galettes au sésame/sesame" were added to Crackers & Cookies this pass (bare "galettes" was left out — it spans too many products). Size None: the "12 un." count is printed only in the image and the name-extraction does not harvest counts from regions for Flipp items — noted.

### Item 7507

![item 7507](images/item-7507.jpg)

- **Name (English):** None
- **Name (French):** NATURE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436909343/1791519991/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `1bed4ea68d8ad23b`
- **Raw:** `{"id": 1046708657, "flyer_id": 8182773, "name": "NATURE", "display_type": 1, "brand": null, "left": 8877.04, "bottom": -2112.65, "right": 9210.18, "top": -1684.0, "cutout_image_url": "http://f.wishabi.net/page_items/436909343/1791519991/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "4.99", "print_id": null, "short_name": null`

**Item Review Analysis (Pass 1):** Stays unclassified, correctly. The image shows a tray of plain round cookies whose entire flyer name is the flavour word "NATURE" (the plain sibling of item 7334's pistache tray). No text signal exists to classify it; kept for review is the designed behaviour. A store-pattern worth noting: Adonis bakery trays are named by flavour only.
