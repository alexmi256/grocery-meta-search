# Metro Plus — full product report

Store slug: `metro-plus`. Generated from `data/grocery.db`. A sampled subset of 20 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 4 concurrent publications mirroring Metro's (flyer 52: the 326-item main circular, Oct 15–21; flyer 53: 13 items, Oct 8–21; flyer 144: 11 items; flyer 145: 39 items — all valid). The expired Oct 8–14 pair is correctly excluded.
- **Sample counts:** 10 classified + 10 unclassified shown across the publications.
- **Issues found:** Metro Plus's sample is heavier on loyalty tiles than Metro's: six of the twenty sampled items are Moi points tiles or brand banners with no price at all — the pâté chinois tile twice (flyers 52 and 144, identical image), an Eggo waffles points tile (sitting in Frozen Bakery), a three-meat pâté points tile, a fruit-cups points tile, and the Irrésistible slogan banner. All six deleted as promo boilerplate. One price error: the Evive smoothie bites stored the 2/12$ total; the render prints "ou 8,99 l'unité" — corrected to 8.99 with the multibuy recorded. The wine item's missing price is honest (a 15%-off offer across a price range, no fixed price). Everything else verified, several against renders identical to Metro's.
- **Fixes applied this pass:** 8982 → 8.99 (multibuy recorded); items 9190, 14271, 14309, 14312, 9194, 9075 deleted.

## Flyer 53 — valid 2026-10-08 → 2026-10-21 (1 classified items, 1 unclassified)

Source ref: `8171685` · fetched 2026-10-13T04:28:44.752Z

### Item 9190

![item 9190](images/item-9190.jpg)

- **Name (English):** None
- **Name (French):** GAUFRES SURGELÉES EGGO
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Bakery & Breakfast
- **Category (French):** Produits surgelés > Boulangerie et déjeuner surgelés
- **How classified:** frozen-remap (`bagels-croissants`)
- **Size:** 1,68kg
- **Price:** None
- **Printed Price:** None
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-08 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436193337/1790831662/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `cbb33c544644c86c`
- **Raw:** `{"id": 1044925045, "flyer_id": 8171685, "name": "GAUFRES SURGELÉES EGGO", "display_type": 1, "brand": "", "left": 4798.7, "bottom": -1288.51, "right": 5786.88, "top": -719.41, "cutout_image_url": "http://f.wishabi.net/page_items/436193337/1790831662/extra_large.jpg", "valid_from": "2026-10-08T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "", "print_id": null, "short_na`

## Flyer 52 — valid 2026-10-15 → 2026-10-21 (5 classified items, 9 unclassified)

Source ref: `8181580` · fetched 2026-10-13T04:28:44.128Z

**Item Review Analysis (Pass 1):** DELETED — not a priced offer. A Moi points tile ("250 points à l'achat de gaufres surgelées Eggo, format écono 1,68 kg") captured as an item in Frozen Bakery; it carries no price. The Eggo product itself is a separate flyer item. Promo boilerplate.

### Item 8834

![item 8834](images/item-8834.jpg)

- **Name (English):** VH CHINESE SAUCE
- **Name (French):** SAUCETTE CHINOISE VH
- **Brand:** None
- **Category (English):** Pantry > Condiments
- **Category (French):** Produits du garde-manger > Condiments et garnitures
- **How classified:** rule (`condiments`)
- **Size:** None
- **Price:** 2.22
- **Printed Price:** “2.22”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436825648/1791488162/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `f489511055cac4ac`
- **Raw:** `{"id": 1046480912, "flyer_id": 8181580, "name": "SAUCETTE CHINOISE VH | VH CHINESE SAUCE", "display_type": 1, "brand": "", "left": 751.56, "bottom": -2039.64, "right": 1142.18, "top": -1672.61, "cutout_image_url": "http://f.wishabi.net/page_items/436825648/1791488162/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "2.22", "prin`

**Item Review Analysis (Pass 1):** Correct. VH Chinese sauces (plum / soya, 341-380 ml) at 2.22 (reg. 4.79-5.79$) — verified; the "j'accumule 1$" badge is a points promo, not the price. Condiments is right.

### Item 8862

![item 8862](images/item-8862.jpg)

- **Name (English):** SMALL POTATOES
- **Name (French):** PETITES POMMES DE TERRE BLANCHES, ROUGES OU A CHAIR JAUNE
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
- **Image source URL:** http://f.wishabi.net/page_items/436825725/1791442099/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `d931a5a8cf690d51`
- **Conditions:** `{"discount": 33}`
- **Raw:** `{"id": 1046481427, "flyer_id": 8181580, "name": "PETITES POMMES DE TERRE BLANCHES, ROUGES OU A CHAIR JAUNE | SMALL POTATOES", "display_type": 1, "brand": "", "left": 8076.98, "bottom": -2541.46, "right": 8354.02, "top": -2182.12, "cutout_image_url": "http://f.wishabi.net/page_items/436825725/1791442099/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 33, "available_to": "2026-10-21T23:59:59-04:00", "video_`

**Item Review Analysis (Pass 1):** Correct. Small potatoes (white/red/yellow, Quebec, 3 lb bag) at 1.99 (reg. 2.99) — verified. Fresh Vegetables is right.

### Item 9027

![item 9027](images/item-9027.jpg)

- **Name (English):** RED OR WHITE WINE
- **Name (French):** VIN ROUGE OU BLANC
- **Brand:** None
- **Category (English):** Beer & Wine > Wine
- **Category (French):** Bières et vins > Vins
- **How classified:** rule (`wine`)
- **Size:** 750ml
- **Price:** None
- **Printed Price:** None
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436825869/1791442100/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `5ede375ac0f02f22`
- **Conditions:** `{"discount": 15}`
- **Raw:** `{"id": 1046482345, "flyer_id": 8181580, "name": "VIN ROUGE OU BLANC | RED OR WHITE WINE", "display_type": 1, "brand": "", "left": 22462.3, "bottom": -2257.11, "right": 23023.4, "top": -1931.11, "cutout_image_url": "http://f.wishabi.net/page_items/436825869/1791442100/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 15, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "", "print_id":`

**Item Review Analysis (Pass 1):** Price honestly absent. Red or white wine (750 ml) at "15% de rabais" over a 15.49-20.39$ range — a percentage offer with no single price; shown as None rather than invented. Wine is right.

### Item 9072

![item 9072](images/item-9072.jpg)

- **Name (English):** None
- **Name (French):** LAIT ÉVAPORÉ SELECTION
- **Brand:** None
- **Category (English):** Dairy & Eggs > Milk & Cream
- **Category (French):** Produits laitiers et œufs > Lait et crème
- **How classified:** rule (`milk-cream`)
- **Size:** 354ml
- **Price:** 2.29
- **Printed Price:** “2.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436897475/1791506175/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `f958ca9ce5706ffb`
- **Raw:** `{"id": 1046655333, "flyer_id": 8181580, "name": "LAIT ÉVAPORÉ SELECTION", "display_type": 1, "brand": "", "left": 5771.64, "bottom": -1266.48, "right": 6122.71, "top": -931.57, "cutout_image_url": "http://f.wishabi.net/page_items/436897475/1791506175/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "2.29", "print_id": null, "sho`

**Item Review Analysis (Pass 1):** Correct. Selection evaporated milk (354 ml) at 2.29 — verified. Milk & Cream is right.

### Item 9088

![item 9088](images/item-9088.jpg)

- **Name (English):** None
- **Name (French):** JAMBON FUMÉ FORET NOIR
- **Brand:** None
- **Category (English):** Meat > Pork & Ham
- **Category (French):** Viande > Porc et jambon
- **How classified:** rule (`pork-ham`)
- **Size:** 175g
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436897470/1791506172/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `2c1a21664b0759e4`
- **Raw:** `{"id": 1046655291, "flyer_id": 8181580, "name": "JAMBON FUMÉ FORET NOIR", "display_type": 1, "brand": "", "left": 6518.71, "bottom": -921.08, "right": 6896.78, "top": -561.2, "cutout_image_url": "http://f.wishabi.net/page_items/436897470/1791506172/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "5.99", "print_id": null, "short`

## Flyer 144 — valid 2026-10-15 → 2026-10-21 (1 classified items, 0 unclassified)

Source ref: `8181590` · fetched 2026-10-16T12:44:48.261Z

**Item Review Analysis (Pass 1):** Correct. Selection sliced smoked ham or turkey breast (Black Forest, 175 g) at 5.99 — verified. Pork & Ham is right.

### Item 14271

![item 14271](images/item-14271.jpg)

- **Name (English):** None
- **Name (French):** PÂTÉ CHINOIS METROGO!
- **Brand:** None
- **Category (English):** Prepared Meals > Quiches & Pies
- **Category (French):** Repas préparés > Quiches et pâtés
- **How classified:** rule (`quiches-pies`)
- **Size:** None
- **Price:** None
- **Printed Price:** None
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436825638/1791442719/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `4e40b16a7a2e06f9`
- **Raw:** `{"id": 1046480700, "flyer_id": 8181590, "name": "PÂTÉ CHINOIS METROGO!", "display_type": 1, "brand": "", "left": 5827.21, "bottom": -1850.68, "right": 6845.62, "top": -1286.62, "cutout_image_url": "http://f.wishabi.net/page_items/436825638/1791442719/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "", "print_id": null, "short_n`

## Flyer 145 — valid 2026-10-15 → 2026-10-21 (3 classified items, 0 unclassified)

Source ref: `8181588` · fetched 2026-10-16T12:44:48.281Z

**Item Review Analysis (Pass 1):** DELETED — the Moi pâté chinois points tile (identical image to item 9194 in flyer 52, and to the tiles deleted at Metro). No price, no product offer.

### Item 14306

![item 14306](images/item-14306.jpg)

- **Name (English):** 100% BUTTER CROISSANTS
- **Name (French):** CROISSANTS 100 % BEURRE
- **Brand:** None
- **Category (English):** Bakery > Bagels, Croissants & English Muffins
- **Category (French):** Boulangerie > Bagels, croissants et muffins anglais
- **How classified:** rule (`specific-audit-fixes`)
- **Size:** 10/57g
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436825613/1791489070/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `f55d6f880a193f79`
- **Raw:** `{"id": 1046483072, "flyer_id": 8181588, "name": "CROISSANTS 100 % BEURRE | 100% BUTTER CROISSANTS", "display_type": 1, "brand": null, "left": 10626.5, "bottom": -1496.9, "right": 11475.4, "top": -1134.53, "cutout_image_url": "http://f.wishabi.net/page_items/436825613/1791489070/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "5`

**Item Review Analysis (Pass 1):** Correct. 100% butter croissants (10 x 57 g) at 5.99 — verified. Bagels, Croissants & English Muffins is right.

### Item 14309

![item 14309](images/item-14309.jpg)

- **Name (English):** None
- **Name (French):** PÂTÉ AUX TROIS VIANDES IRRÉSISTIBLE
- **Brand:** None
- **Category (English):** Deli > Deli Meat
- **Category (French):** Charcuterie > Charcuterie
- **How classified:** rule (`deli-meat`)
- **Size:** 12kg
- **Price:** None
- **Printed Price:** None
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-28
- **Image source URL:** http://f.wishabi.net/page_items/436825625/1791489085/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `10988c3a8d068db0`
- **Raw:** `{"id": 1046483085, "flyer_id": 8181588, "name": "PÂTÉ AUX TROIS VIANDES IRRÉSISTIBLE", "display_type": 1, "brand": "", "left": 14164.8, "bottom": -2044.65, "right": 14804.89, "top": -1694.52, "cutout_image_url": "http://f.wishabi.net/page_items/436825625/1791489085/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-28T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "", "print_id":`

**Item Review Analysis (Pass 1):** DELETED — a Moi points tile ("375 points à l'achat d'un pâté aux trois viandes Irrésistible, format écono 1,2 kg"); no price. Promo boilerplate.

### Item 14312

![item 14312](images/item-14312.jpg)

- **Name (English):** None
- **Name (French):** FRUITS SELECTION OU MIEUX-Ê
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** None
- **Printed Price:** None
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-28
- **Image source URL:** http://f.wishabi.net/page_items/436825621/1791489081/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `d35ee0368a213de9`
- **Raw:** `{"id": 1046483081, "flyer_id": 8181588, "name": "FRUITS SELECTION OU MIEUX-Ê", "display_type": 1, "brand": "", "left": 13116.77, "bottom": -2417.38, "right": 13747.89, "top": -2050.29, "cutout_image_url": "http://f.wishabi.net/page_items/436825621/1791489081/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-28T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "", "print_id": null, `

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 53 (valid 2026-10-08 → 2026-10-21)

**Item Review Analysis (Pass 1):** DELETED — a Moi points tile ("125 points à l'achat de 3 collations aux fruits Selection ou Mieux-être"); no price. Promo boilerplate.

### Item 9194

![item 9194](images/item-9194.jpg)

- **Name (English):** None
- **Name (French):** CHINOIS METROGO!
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** None
- **Printed Price:** None
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-08 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436193341/1790831666/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `0657468b9a40a3f8`
- **Raw:** `{"id": 1044925049, "flyer_id": 8171685, "name": "CHINOIS METROGO!", "display_type": 1, "brand": null, "left": 5827.25, "bottom": -1850.57, "right": 6845.55, "top": -1286.57, "cutout_image_url": "http://f.wishabi.net/page_items/436193341/1790831666/extra_large.jpg", "valid_from": "2026-10-08T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "", "print_id": null, "short_name`

— from flyer 52 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** DELETED — the same Moi pâté chinois points tile as 14271 (identical image).

### Item 8894

![item 8894](images/item-8894.jpg)

- **Name (English):** COOL & SIMPLE FROZEN SIDE DISH
- **Name (French):** ACCOMPAGNEMENT SURGELÉ COOL & SIMPLE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 500g
- **Price:** 7.99
- **Printed Price:** “7.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436825894/1791442096/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `242681cbaeaeadc0`
- **Conditions:** `{"discount": 26}`
- **Raw:** `{"id": 1046482462, "flyer_id": 8181580, "name": "ACCOMPAGNEMENT SURGELÉ COOL & SIMPLE | COOL & SIMPLE FROZEN SIDE DISH", "display_type": 1, "brand": "", "left": 23614.7, "bottom": -969.32, "right": 23899.3, "top": -644.72, "cutout_image_url": "http://f.wishabi.net/page_items/436825894/1791442096/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 26, "available_to": "2026-10-21T23:59:59-04:00", "video_url": n`

— from flyer 52 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Cool & Simple frozen side dish (all-dressed skillet, 500 g) at 7.99 (reg. 10.79) — verified. Unclassified under its generic name.

### Item 8982

![item 8982](images/item-8982.jpg)

- **Name (English):** EVIVE BITES
- **Name (French):** BOUCHÉS EVIVE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 144g
- **Price:** 12.00
- **Printed Price:** “12.0”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436825904/1791442102/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `50e49da14d6e5c94`
- **Raw:** `{"id": 1046482512, "flyer_id": 8181580, "name": "BOUCHÉS EVIVE | EVIVE BITES", "display_type": 1, "brand": "", "left": 23051.7, "bottom": -638.86, "right": 23325.4, "top": -347.72, "cutout_image_url": "http://f.wishabi.net/page_items/436825904/1791442102/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "12.0", "print_id": null, `

— from flyer 52 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the render. Evive smoothie bites (144 g) print "2/12$ ou 8,99 l'unité"; the DB stored the 12.00 total. Now 8.99 with the multibuy recorded. Unclassified.

### Item 8986

![item 8986](images/item-8986.jpg)

- **Name (English):** None
- **Name (French):** CAISSE DE 12 CANETTES
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 27.99
- **Printed Price:** “27.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436825967/1791442100/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `3f978a7a80d2ed91`
- **Raw:** `{"id": 1046482795, "flyer_id": 8181580, "name": "CAISSE DE 12 CANETTES", "display_type": 1, "brand": "", "left": 27081.0, "bottom": -1202.43, "right": 27631.2, "top": -841.78, "cutout_image_url": "http://f.wishabi.net/page_items/436825967/1791442100/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "27.99", "print_id": null, "sho`

— from flyer 52 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct price. Unibroue beer, case of 12 cans, at 27.99$ + taxes and deposit — identical render to Metro's item 5996. Unclassified on its case-only name; kept.

### Item 8987

![item 8987](images/item-8987.jpg)

- **Name (English):** None
- **Name (French):** SCOTTIES®' SUPREME EMBALLAGE MULTIPLE DE 6 OU SPONGETOWELS® ULTRA 3=6 ROULEAUX
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436825954/1791442098/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `2b98e5fa6bd3ddfa`
- **Raw:** `{"id": 1046482720, "flyer_id": 8181580, "name": "SCOTTIES®' SUPREME EMBALLAGE MULTIPLE DE 6 OU SPONGETOWELS® ULTRA 3=6 ROULEAUX", "display_type": 1, "brand": "", "left": 25360.0, "bottom": -866.65, "right": 25916.8, "top": -590.58, "cutout_image_url": "http://f.wishabi.net/page_items/436825954/1791442098/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "vi`

— from flyer 52 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Scotties Supreme tissues (6-pack) or SpongeTowels Ultra at 6.99$ +tx — identical render to Metro's item 5997. Household, unclassified; kept for review.

### Item 9006

![item 9006](images/item-9006.jpg)

- **Name (English):** ST-HUBERT PIE
- **Name (French):** PÂTÉ ST‑HUBERT
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 10.99
- **Printed Price:** “10.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436825813/1791488336/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `dd44ae25a5f10bb2`
- **Conditions:** `{"discount": 12}`
- **Raw:** `{"id": 1046482046, "flyer_id": 8181580, "name": "PÂTÉ ST‑HUBERT | ST-HUBERT PIE", "display_type": 1, "brand": "", "left": 16994.8, "bottom": -975.74, "right": 17268.1, "top": -645.79, "cutout_image_url": "http://f.wishabi.net/page_items/436825813/1791488336/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 12, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "10.99", "print_id": null`

— from flyer 52 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct price. St-Hubert pot pie (525-645 g) at 10.99 (reg. 12.49) — identical render to Metro's item 6016. Unclassified on the short payload name.

### Item 9075

![item 9075](images/item-9075.jpg)

- **Name (English):** None
- **Name (French):** IRRESISTIBLE IMPOSSIBLE D'Y RÉSISTER
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** None
- **Printed Price:** None
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436875823/1791488307/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `80c8b941dcf62745`
- **Raw:** `{"id": 1046603743, "flyer_id": 8181580, "name": "IRRESISTIBLE IMPOSSIBLE D'Y RÉSISTER", "display_type": 5, "brand": "", "left": 14414.0, "bottom": -1337.39, "right": 14959.7, "top": -1304.74, "cutout_image_url": "http://f.wishabi.net/page_items/436875823/1791488307/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "", "print_id":`

— from flyer 52 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** DELETED — the Irrésistible slogan banner ("Impossible d'y résister"), same as Metro's item 6085. No product, no price.

### Item 9093

![item 9093](images/item-9093.jpg)

- **Name (English):** LA STATION DE COMPTON
- **Name (French):** LA STATION DE COMPTON
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 150g
- **Price:** 11.99
- **Printed Price:** “11.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436825828/1791488346/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `273aa013620581b5`
- **Conditions:** `{"discount": 10}`
- **Raw:** `{"id": 1046482141, "flyer_id": 8181580, "name": "LA STATION DE COMPTON | LA STATION DE COMPTON", "display_type": 1, "brand": "", "left": 16965.8, "bottom": -1887.32, "right": 17270.1, "top": -1621.47, "cutout_image_url": "http://f.wishabi.net/page_items/436825828/1791488346/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 10, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "11.99",`

— from flyer 52 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct price. La Station de Compton cheese (150 g) at 11.99 (reg. 13.29) — identical render to Metro's item 6103. Unclassified under its brand-only name.

### Item 9098

![item 9098](images/item-9098.jpg)

- **Name (English):** CORDON BLEU STEW
- **Name (French):** RAGOUT CORDON BLEU
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 410g
- **Price:** 4.29
- **Printed Price:** “4.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436825884/1791442111/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `1cff6ef8773754b5`
- **Conditions:** `{"discount": 28}`
- **Raw:** `{"id": 1046482412, "flyer_id": 8181580, "name": "RAGOUT CORDON BLEU | CORDON BLEU STEW", "display_type": 1, "brand": "", "left": 21901.8, "bottom": -2255.38, "right": 22170.5, "top": -1928.68, "cutout_image_url": "http://f.wishabi.net/page_items/436825884/1791442111/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 28, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "4.29", "print_i`

— from flyer 52 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Cordon Bleu meatball stew (ragoût de boulettes, 410 g) at 4.29 (reg. 5.99) — verified. Unclassified under its name form.

### Item 9122

![item 9122](images/item-9122.jpg)

- **Name (English):** SELECTION DRINK
- **Name (French):** BOISSON SELECTION
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 2 L
- **Price:** 2.25
- **Printed Price:** “2.25”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436825885/1791442111/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `b1f15f00dab5a9c8`
- **Conditions:** `{"discount": 25}`
- **Raw:** `{"id": 1046482417, "flyer_id": 8181580, "name": "BOISSON SELECTION | SELECTION DRINK", "display_type": 1, "brand": "", "left": 22747.6, "bottom": -340.34, "right": 23022.8, "top": -31.23, "cutout_image_url": "http://f.wishabi.net/page_items/436825885/1791442111/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 25, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "2.25", "print_id": n`

**Item Review Analysis (Pass 1):** Correct. Selection drink (fruit punch / peach, 2 L) at 2.25 (reg. 2.99) — identical render to Metro's item 6132. Unclassified under its generic name.
