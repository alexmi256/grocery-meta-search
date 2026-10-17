# Marché Adonis — full product report

Store slug: `adonis`. Generated from `data/grocery.db`. A sampled subset of 12 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 2 (2026-10-17, verification after Pass 1 fixes)

- Packet regenerated after the Pass 1 fixes. **The fixes held:** the current flyer's unclassified pool dropped from 7 to 2 — items 7410 and 7507, the two Pass 1 deliberately left (generic snack term; flavour-only name). The five vocabulary fixes classify correctly in the stored data (7334 → Dried Fruits & Nuts, 7352 → Deli dips, 7455 → Fish, 7498 → Bakery > Bread, 7506 → Crackers & Cookies), items 7466/7489 now carry their printed range sizes (836-888g, 325-410g), and item 7476's rate-denominator size is cleared.
- This pass sampled a fresh 10 classified + the 2 unclassified. All 10 classified items verify against their region images on name, price and category, with three recurring source-shaped caveats, none new: (a) multibuy totals from the Flipp payload read as unit prices (7377: 6.00 for "2/6$ ou 3,49 l'unité"; 7378: 5.00 for "2/5$"; 7473: 9.00 for "6/9$") — the payload carries only the collapsed figure, a documented unrecoverable; (b) French-only payloads lack the English name the flyer prints (7338); (c) the bakery-tray flavour series (7496 "CHOCOLAT") classifies by its flavour word — Candy & Chocolate for what the photo shows is a bakery cookie tray, the same text-only limit documented for 7334/7507 in Pass 1.
- No regressions found. Pass 1's full analysis is preserved in `adonis-report-pass1.md`. Store review complete.

## Flyer 39 — valid 2026-10-15 → 2026-10-21 (10 classified items, 2 unclassified)

Source ref: `8182773` · fetched 2026-10-13T04:28:22.888Z

### Item 7338

![item 7338](images/item-7338.jpg)

- **Name (English):** None
- **Name (French):** tablette de chocolat Ritter Sport
- **Brand:** Ritter Sport
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 100g
- **Price:** 3.49
- **Printed Price:** “3.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891106/1791519985/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `3d27e78c680189c9`
- **Conditions:** `{"discount": 42}`
- **Raw:** `{"id": 1046708001, "flyer_id": 8182773, "name": "tablette de chocolat Ritter Sport", "display_type": 1, "brand": "Ritter Sport", "left": 601.35, "bottom": -2494.76, "right": 848.1, "top": -2187.58, "cutout_image_url": "http://f.wishabi.net/page_items/436891106/1791519985/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 42, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "3.49", "pr`

**Item Review Analysis (Pass 2):** Verified: Ritter Sport chocolate bar, 100 g (stored ✓), 3.49. English name absent (French-only payload; printed in the image) — known source limit.

### Item 7366

![item 7366](images/item-7366.jpg)

- **Name (English):** GREEN AND BLACK SEEDLESS GRAPES
- **Name (French):** RAISINS VERTS ET NOIRS SANS PÉPINS
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891194/1791520001/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `869237da4fccdbe1`
- **Raw:** `{"id": 1046708064, "flyer_id": 8182773, "name": "RAISINS VERTS ET NOIRS SANS PÉPINS | GREEN AND BLACK SEEDLESS GRAPES", "display_type": 1, "brand": null, "left": 3166.0, "bottom": -1538.72, "right": 3448.25, "top": -1281.72, "cutout_image_url": "http://f.wishabi.net/page_items/436891194/1791520001/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url`

**Item Review Analysis (Pass 2):** Verified: green and black seedless grapes, 3.99/lb headline with 8,80/kg equivalent; stored unit pound ✓, names split ✓.

### Item 7377

![item 7377](images/item-7377.jpg)

- **Name (English):** None
- **Name (French):** boisson gazeuse Coca-Cola ou croustilles Pringles
- **Brand:** None
- **Category (English):** Drinks > Soft Drinks
- **Category (French):** Boissons > Boissons gazeuses
- **How classified:** rule (`soft-drinks`)
- **Size:** 148-156g
- **Price:** 6.00
- **Printed Price:** “6.0”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891290/1791519995/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `44830db9e20b635a`
- **Conditions:** `{"discount": 25}`
- **Raw:** `{"id": 1046708489, "flyer_id": 8182773, "name": "boisson gazeuse Coca-Cola ou croustilles Pringles", "display_type": 1, "brand": null, "left": 7484.88, "bottom": -2050.41, "right": 7765.61, "top": -1794.64, "cutout_image_url": "http://f.wishabi.net/page_items/436891290/1791519995/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 25, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "6`

**Item Review Analysis (Pass 2):** Verified as a combo offer (Coca-Cola 2 L or Pringles 148-156 g, "2/6$ ou 3,49 l'unité"). Stored price 6.00 is the payload's collapsed multibuy total and size "148-156g" is only the Pringles side — documented Flipp-payload limits; Soft Drinks classification follows the first-named alternative.

### Item 7378

![item 7378](images/item-7378.jpg)

- **Name (English):** CEDAR LENTILS
- **Name (French):** LENTILLES CEDAR
- **Brand:** None
- **Category (English):** Pantry > Dried Beans, Vegetables & Grains
- **Category (French):** Produits du garde-manger > Haricots secs, légumes et grains
- **How classified:** rule (`beans-grains`)
- **Size:** 907g
- **Price:** 5.00
- **Printed Price:** “5.0”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891298/1791520001/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `1d2f5772381769db`
- **Raw:** `{"id": 1046708538, "flyer_id": 8182773, "name": "LENTILLES CEDAR | CEDAR LENTILS", "display_type": 1, "brand": null, "left": 7485.74, "bottom": -509.87, "right": 7768.15, "top": -126.95, "cutout_image_url": "http://f.wishabi.net/page_items/436891298/1791520001/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "5.0", "print_id": n`

**Item Review Analysis (Pass 2):** Verified: Cedar lentils 907 g (stored ✓); price 5.00 is the "2/5$" multibuy total from the payload (single is 2,99) — same documented limit as 7377.

### Item 7402

![item 7402](images/item-7402.jpg)

- **Name (English):** IRRÉSISTIBLE COOKED SHRIMPS 51-60
- **Name (French):** CREVETTE CUITES 51-60 IRRÉSISTIBLE
- **Brand:** Irresistible
- **Category (English):** Fish & Seafood > Shrimp
- **Category (French):** Poissons et fruits de mer > Crevette
- **How classified:** rule (`shrimp`)
- **Size:** 340g
- **Price:** 5.77
- **Printed Price:** “5.77”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891118/1791519993/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `1943c401ca2ca29b`
- **Conditions:** `{"discount": 42}`
- **Raw:** `{"id": 1046708013, "flyer_id": 8182773, "name": "CREVETTE CUITES 51-60 IRRÉSISTIBLE | IRRÉSISTIBLE COOKED SHRIMPS 51-60", "display_type": 1, "brand": "Irresistible", "left": 760.21, "bottom": -1269.93, "right": 1140.74, "top": -990.36, "cutout_image_url": "http://f.wishabi.net/page_items/436891118/1791519993/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 42, "available_to": "2026-10-21T23:59:59-04:00", "`

**Item Review Analysis (Pass 2):** Verified: Irrésistible cooked shrimp 51-60, 340 g (stored ✓), 5.77. Shrimp category correct.

### Item 7463

![item 7463](images/item-7463.jpg)

- **Name (English):** CLOVER LEAF IMITATION CRAB FLAVOURED SEAFOOD
- **Name (French):** IMITATION SAVEUR DE CRABE EN FLOCONS CLOVER LEAF
- **Brand:** Clover Leaf
- **Category (English):** Fish & Seafood > Shellfish
- **Category (French):** Poissons et fruits de mer > Crustacés
- **How classified:** rule (`shellfish`)
- **Size:** 227g
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891231/1791519989/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `256bd8b4e75f5e9b`
- **Conditions:** `{"discount": 27}`
- **Raw:** `{"id": 1046708121, "flyer_id": 8182773, "name": "IMITATION SAVEUR DE CRABE EN FLOCONS CLOVER LEAF | CLOVER LEAF IMITATION CRAB FLAVOURED SEAFOOD", "display_type": 1, "brand": "Clover Leaf", "left": 5464.22, "bottom": -900.02, "right": 5749.05, "top": -519.59, "cutout_image_url": "http://f.wishabi.net/page_items/436891231/1791519989/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 27, "available_to": "2026-`

**Item Review Analysis (Pass 2):** Verified: Clover Leaf imitation crab flakes, 227 g (stored ✓), 3.99. Shellfish is the taxonomy's only home for imitation crab.

### Item 7473

![item 7473](images/item-7473.jpg)

- **Name (English):** SUJUK, FAJITA OR PEPPERONI ROLLS HALAL
- **Name (French):** ROULEAUX DE SUJUK, FAJITA OU PEPPERONI
- **Brand:** None
- **Category (English):** International Foods > Middle Eastern Foods
- **Category (French):** Aliments internationaux > Aliments du Moyen-Orient
- **How classified:** rule (`middle-eastern`)
- **Size:** 6un
- **Price:** 9.00
- **Printed Price:** “9.0”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891251/1791519987/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `d54ad0eb3c355fc3`
- **Raw:** `{"id": 1046708242, "flyer_id": 8182773, "name": "ROULEAUX DE SUJUK, FAJITA OU PEPPERONI | SUJUK, FAJITA OR PEPPERONI ROLLS HALAL", "display_type": 1, "brand": null, "left": 6044.74, "bottom": -2546.28, "right": 6331.76, "top": -2304.35, "cutout_image_url": "http://f.wishabi.net/page_items/436891251/1791519987/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00"`

**Item Review Analysis (Pass 2):** Verified: sujuk/fajita/pepperoni rolls, 6 un. (stored size ✓), "6/9$ ou 1,69 l'unité" — stored 9.00 is the pack total (payload limit, as 7377). Middle Eastern classification follows the lead product (sujuk).

### Item 7486

![item 7486](images/item-7486.jpg)

- **Name (English):** CEDAR FROZEN VEGETABLES
- **Name (French):** LÉGUMES SURGELÉS CEDAR
- **Brand:** Cedar
- **Category (English):** Frozen Food > Frozen Fruit & Vegetables
- **Category (French):** Produits surgelés > Fruits et légumes surgelés
- **How classified:** frozen-remap (`vegetables`)
- **Size:** 750g
- **Price:** 2.79
- **Printed Price:** “2.79”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891289/1791519995/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `5c9d0a4fc1fc3b7b`
- **Conditions:** `{"discount": 30}`
- **Raw:** `{"id": 1046708483, "flyer_id": 8182773, "name": "LÉGUMES SURGELÉS CEDAR | CEDAR FROZEN VEGETABLES", "display_type": 1, "brand": "Cedar", "left": 6922.23, "bottom": -1540.6, "right": 7195.53, "top": -1290.55, "cutout_image_url": "http://f.wishabi.net/page_items/436891289/1791519995/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 30, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "`

**Item Review Analysis (Pass 2):** Verified: Cedar frozen mixed vegetables, 750 g (stored ✓), 2.79.

### Item 7490

![item 7490](images/item-7490.jpg)

- **Name (English):** Oatly gluten free oat beverage
- **Name (French):** boisson d'avoine sans gluten Oatly
- **Brand:** None
- **Category (English):** Dairy & Eggs > Non-Dairy Milk Alternatives
- **Category (French):** Produits laitiers et œufs > Laits non laitiers
- **How classified:** rule (`non-dairy-milk`)
- **Size:** 946ml
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436891281/1791519988/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `eb48e28cb38be83e`
- **Conditions:** `{"discount": 17}`
- **Raw:** `{"id": 1046708438, "flyer_id": 8182773, "name": "boisson d'avoine sans gluten Oatly | Oatly gluten free oat beverage", "display_type": 1, "brand": null, "left": 7486.08, "bottom": -2549.16, "right": 7767.72, "top": -2306.73, "cutout_image_url": "http://f.wishabi.net/page_items/436891281/1791519988/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 17, "available_to": "2026-10-21T23:59:59-04:00", "video_url":`

**Item Review Analysis (Pass 2):** Verified: Oatly gluten-free oat beverage, 946 ml per the printed text (stored ✓ — the pictured cartons say 1 L, the offer text governs), 4.99. Non-Dairy Milk Alternatives correct.

### Item 7496

![item 7496](images/item-7496.jpg)

- **Name (English):** None
- **Name (French):** CHOCOLAT
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** None
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436909342/1791519990/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `a4726061f61df798`
- **Raw:** `{"id": 1046708653, "flyer_id": 8182773, "name": "CHOCOLAT", "display_type": 1, "brand": null, "left": 8476.34, "bottom": -2196.52, "right": 8870.05, "top": -1788.83, "cutout_image_url": "http://f.wishabi.net/page_items/436909342/1791519990/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "4.99", "print_id": null, "short_name": n`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 39 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 2):** Third sibling of the bakery-tray flavour series (with 7334 PISTACHE and 7507 NATURE): the photo shows chocolate ma'amoul-style cookies, but the entire name is "CHOCOLAT", so the text classifier places it in Candy & Chocolate. A text-only limit on flavour-only names, documented in Pass 1; no rule change (the word is correct for thousands of real chocolate items).

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

**Item Review Analysis (Pass 2):** Unchanged by design (Pass 1): generic snack term; "amuse-gueule" phrase rejected on ground-truth evidence.

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

**Item Review Analysis (Pass 2):** Unchanged by design (Pass 1): flavour-only name "NATURE"; no text signal; kept for review.
