# Canadian Tire — full product report

Store slug: `canadian-tire`. Generated from `data/grocery.db`. A sampled subset of 20 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 163, valid 2026-10-15 → 2026-10-21, current). The DB also holds the expired Oct 8–14 edition, correctly excluded.
- **Sample counts:** 10 classified + 10 unclassified shown, of 292 current-flyer items (28 classified, 264 unclassified before this pass's fixes). The balance is this store's reality: Canadian Tire's flyer is overwhelmingly general merchandise, which the grocery classifier leaves Unclassified and which stays in the pool for review under Alex's rule. The durable answer for such stores is the store-native category mapping recorded as a future TODO — not built here.
- **Issues found:** the classified sample contains the merchandise traps Alex flagged in this morning's pack — 7 of the 10 "classified grocery" items were not food at all (string lights as fresh fruit, a water softener as bottled water, milk frothers as milk, a log splitter as cake, a cookie sheet as cookies, a wine-pouring Halloween cauldron as wine). Every one of these shapes carries an adjudicated ground-truth verdict of Household > Home Goods. Two unclassified items (15468 "Women in Sport", 15496 "Canada Garage Ad") are price-less promo tiles rather than products, and one (15518) carries only a name fragment ("Format de 3,78 L.").
- **Patterns:** at general-merchandise stores the classifier's false-grocery rate is driven by single food words inside hardware names (orange, eau, lait, bûches, biscuits, vin). Phrase guards keyed to the hardware words (fendeuse, adoucisseur, mousseur, brumisateur) are precise fixes because those words have no grocery meaning; the residual mass is honestly Unclassified.
- **Fixes applied this pass:** guard remaps to Household > Home Goods for fendeuse / adoucisseur / mousseur(s) à lait / plaque à biscuits / brumisateur / boule de cristal, and for produce-classified items naming lights (lumières/NOMA). Ground truth 12346 → 12357 items, 8234 → 8245 signatures (80.1%). Data: reclassify flipped exactly 11 items — all Canadian Tire, all to Household > Home Goods — and the purge deleted those 11 (backup `data/grocery.db.bak-20261017c`). The two promo tiles and the name-fragment item stay: no sanctioned rule discards them, and Unclassified items are kept for review.

## Flyer 163 — valid 2026-10-15 → 2026-10-21 (10 classified items, 10 unclassified)

Source ref: `8180834` · fetched 2026-10-17T05:38:43.264Z

### Item 15286

![item 15286](images/item-15286.jpg)

- **Name (English):** None
- **Name (French):** Taxable Croustilles ou bâtonnets au fromage Old Dutch, 24/paq.
- **Brand:** Old Dutch
- **Category (English):** Snacks, Chips & Candy > Chips & Snacks
- **Category (French):** Grignotines, croustilles et friandises > Croustilles et grignotines
- **How classified:** rule (`specific-snacks`)
- **Size:** None
- **Price:** 8.99
- **Printed Price:** “8.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436750088/1791518176/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `a7105105af3a59e7`
- **Raw:** `{"id": 1046694297, "flyer_id": 8180834, "name": "Taxable Croustilles ou bâtonnets au fromage Old Dutch, 24/paq.", "display_type": 1, "brand": "Old Dutch", "left": 2941.46, "bottom": -1281.41, "right": 3166.03, "top": -1058.57, "cutout_image_url": "http://f.wishabi.net/page_items/436750088/1791518176/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_u`

**Item Review Analysis (Pass 1):** Correct, genuine grocery. Image confirms Old Dutch potato chips / cheese sticks 24-pack at 8.99 — Chips & Snacks is right. Size None: the payload name carries the count (24/paq.) but no weight, and the harvest found no unambiguous size in the region.

### Item 15310

![item 15310](images/item-15310.jpg)

- **Name (English):** None
- **Name (French):** Jeu de 30 lumières étoilées orange à DEL NOMA, 10 pi. NOMA
- **Brand:** NOMA
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 19.99
- **Printed Price:** “19.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436898269/1791518194/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `c91f1f71429dabef`
- **Raw:** `{"id": 1046694744, "flyer_id": 8180834, "name": "Jeu de 30 lumières étoilées orange à DEL NOMA, 10 pi. NOMA", "display_type": 1, "brand": "NOMA", "left": 2946.5, "bottom": -2353.89, "right": 3163.5, "top": -2191.89, "cutout_image_url": "http://f.wishabi.net/page_items/436898269/1791518194/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, `

**Item Review Analysis (Pass 1):** REMOVED this pass. NOMA orange star string lights (photo confirms: orange LED string lights) — the colour word "orange" classified a lighting product as Fresh Fruits. Guard remap (produce + lumières/NOMA → Household > Home Goods, the GT verdict), then purged as non-grocery.

### Item 15384

![item 15384](images/item-15384.jpg)

- **Name (English):** None
- **Name (French):** Whirlpool Adoucisseur d'eau à 30 000 granules
- **Brand:** Whirlpool
- **Category (English):** Drinks > Water
- **Category (French):** Boissons > Eau
- **How classified:** rule (`water`)
- **Size:** None
- **Price:** 649.99
- **Printed Price:** “649.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436754521/1791518193/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `f69e9be98e00dff2`
- **Conditions:** `{"discount": 13}`
- **Raw:** `{"id": 1046702573, "flyer_id": 8180834, "name": "Whirlpool Adoucisseur d'eau à 30 000 granules", "display_type": 1, "brand": "Whirlpool", "left": 10223.91, "bottom": -2382.25, "right": 10449.43, "top": -2197.44, "cutout_image_url": "http://f.wishabi.net/page_items/436754521/1791518193/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 13, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price`

**Item Review Analysis (Pass 1):** REMOVED this pass. Whirlpool 30,000-grain water softener, 649.99 — "Adoucisseur d'eau" classified a plumbing appliance as Drinks > Water. Guard (adoucisseur) + purge.

### Item 15410

![item 15410](images/item-15410.jpg)

- **Name (English):** None
- **Name (French):** Mousseur à lait électrique à piles Primula
- **Brand:** Primula
- **Category (English):** Dairy & Eggs > Milk & Cream
- **Category (French):** Produits laitiers et œufs > Lait et crème
- **How classified:** rule (`milk-cream`)
- **Size:** None
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436901891/1791518213/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `9d3f1a15287e5f7e`
- **Conditions:** `{"discount": 50}`
- **Raw:** `{"id": 1046700923, "flyer_id": 8180834, "name": "Mousseur à lait électrique à piles Primula", "display_type": 1, "brand": "Primula", "left": 7608.5, "bottom": -1922.79, "right": 7728.5, "top": -1629.79, "cutout_image_url": "http://f.wishabi.net/page_items/436901891/1791518213/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 50, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "4.99"`

**Item Review Analysis (Pass 1):** REMOVED this pass. Primula battery milk frother, 4.99 — "Mousseur à lait" classified a kitchen appliance as Milk & Cream. Guard (mousseur à lait) + purge.

### Item 15439

![item 15439](images/item-15439.jpg)

- **Name (English):** None
- **Name (French):** Faucheuse marécageuse animée dans une boule de cristal 1 pi 7 po ou brumisateur-chaudron à DEL versant du vin 8 po
- **Brand:** None
- **Category (English):** Beer & Wine > Wine
- **Category (French):** Bières et vins > Vins
- **How classified:** rule (`wine`)
- **Size:** 7 po
- **Price:** 39.99
- **Printed Price:** “39.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436750092/1791518179/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `c12a62a8dcba1109`
- **Raw:** `{"id": 1046694367, "flyer_id": 8180834, "name": "Faucheuse marécageuse animée dans une boule de cristal 1 pi 7 po ou brumisateur-chaudron à DEL versant du vin 8 po", "display_type": 1, "brand": null, "left": 3167.7, "bottom": -1278.63, "right": 3361.29, "top": -1203.12, "cutout_image_url": "http://f.wishabi.net/page_items/436750092/1791518179/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "availabl`

**Item Review Analysis (Pass 1):** REMOVED this pass. Animated swamp-reaper Halloween decoration in a crystal ball, 39.99 — "versant du vin" (the companion wine-pouring cauldron) classified decor as Wine. Guard (boule de cristal / brumisateur) + purge.

### Item 15440

![item 15440](images/item-15440.jpg)

- **Name (English):** None
- **Name (French):** Fendeuse de bûches électrique à coupe double, 5 tonnes, 15 A yardworks
- **Brand:** Yardworks
- **Category (English):** Bakery > Cakes
- **Category (French):** Boulangerie > Gâteaux
- **How classified:** rule (`cakes`)
- **Size:** None
- **Price:** 299.99
- **Printed Price:** “299.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436750303/1791518188/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `393e6bc47e2939d3`
- **Conditions:** `{"discount": 36}`
- **Raw:** `{"id": 1046695377, "flyer_id": 8180834, "name": "Fendeuse de bûches électrique à coupe double, 5 tonnes, 15 A yardworks", "display_type": 1, "brand": "Yardworks", "left": 4146.96, "bottom": -2192.9, "right": 4372.02, "top": -2139.3, "cutout_image_url": "http://f.wishabi.net/page_items/436750303/1791518188/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 36, "available_to": "2026-10-21T23:59:59-04:00", "vid`

**Item Review Analysis (Pass 1):** REMOVED this pass. Yardworks 5-ton electric log splitter, 299.99 — "Fendeuse de bûches" classified a wood splitter as Bakery > Cakes (bûche). Guard (fendeuse) + purge.

### Item 15453

![item 15453](images/item-15453.jpg)

- **Name (English):** None
- **Name (French):** Dosettes K-Cup® de thé infusé Tim Hortons, 30 un Keurig
- **Brand:** Keurig
- **Category (English):** Drinks > Tea & Hot Drinks
- **Category (French):** Boissons > Thés et boissons chaudes
- **How classified:** guard-remap (`coffee`)
- **Size:** None
- **Price:** 26.99
- **Printed Price:** “26.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436854859/1791518218/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `b9591ea97bf8c7e2`
- **Raw:** `{"id": 1046702246, "flyer_id": 8180834, "name": "Dosettes K-Cup® de thé infusé Tim Hortons, 30 un Keurig", "display_type": 1, "brand": "Keurig", "left": 8900.0, "bottom": -2324.06, "right": 9004.0, "top": -2202.06, "cutout_image_url": "http://f.wishabi.net/page_items/436854859/1791518218/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "`

**Item Review Analysis (Pass 1):** Correct, genuine grocery. Tim Hortons steeped-tea K-Cup pods, 30 count — Tea & Hot Drinks is right; price 26.99 is payload-sourced (the region render is a bare cutout with no price block to verify against).

### Item 15509

![item 15509](images/item-15509.jpg)

- **Name (English):** None
- **Name (French):** Certains mousseurs à lait, théière ou infuseur de thé Bodum
- **Brand:** bodum
- **Category (English):** Dairy & Eggs > Milk & Cream
- **Category (French):** Produits laitiers et œufs > Lait et crème
- **How classified:** rule (`milk-cream`)
- **Size:** None
- **Price:** 19.99
- **Printed Price:** “19.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436898129/1791518214/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `7e6856d0a53c423e`
- **Conditions:** `{"discount": 20}`
- **Raw:** `{"id": 1046700877, "flyer_id": 8180834, "name": "Certains mousseurs à lait, théière ou infuseur de thé Bodum", "display_type": 1, "brand": "bodum", "left": 8274.46, "bottom": -2198.35, "right": 8497.67, "top": -2142.54, "cutout_image_url": "http://f.wishabi.net/page_items/436898129/1791518214/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 20, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null`

**Item Review Analysis (Pass 1):** REMOVED this pass. Bodum milk frothers / teapot / tea infuser assortment, 19.99 — small appliances classified as Milk & Cream via "mousseurs à lait". Guard + purge.

### Item 15560

![item 15560](images/item-15560.jpg)

- **Name (English):** None
- **Name (French):** Café de torréfaction classique Folgers
- **Brand:** Folgers
- **Category (English):** Drinks > Coffee
- **Category (French):** Boissons > Cafés
- **How classified:** rule (`coffee`)
- **Size:** 816g
- **Price:** 16.99
- **Printed Price:** “16.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436753673/1791518194/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `d451a30855d022c6`
- **Conditions:** `{"discount": 11}`
- **Raw:** `{"id": 1046701285, "flyer_id": 8180834, "name": "Café de torréfaction classique Folgers", "display_type": 1, "brand": "Folgers", "left": 8564.18, "bottom": -2367.83, "right": 8789.51, "top": -2199.38, "cutout_image_url": "http://f.wishabi.net/page_items/436753673/1791518194/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 11, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "16.99",`

**Item Review Analysis (Pass 1):** Fully correct. Image confirms Folgers Classic Roast coffee, 816 g, 16.99 (reg. 18.99, save 10%) — name, size, price and Coffee category all match.

### Item 15572

![item 15572](images/item-15572.jpg)

- **Name (English):** None
- **Name (French):** Plaque à biscuits, 17 po. Master Chef
- **Brand:** Master Chef
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** 17 po
- **Price:** 8.99
- **Printed Price:** “8.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436756520/1791518213/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `da3fd7c076d3f37a`
- **Conditions:** `{"discount": 47}`
- **Raw:** `{"id": 1046706506, "flyer_id": 8180834, "name": "Plaque à biscuits, 17 po. Master Chef", "display_type": 1, "brand": "Master Chef", "left": 26137.15, "bottom": -1317.44, "right": 26558.09, "top": -818.75, "cutout_image_url": "http://f.wishabi.net/page_items/436756520/1791518213/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 47, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "8.9`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 163 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** REMOVED this pass. Master Chef 17-inch cookie sheet, 8.99 — "Plaque à biscuits" classified bakeware as Crackers & Cookies. Its stored size "17 po" is the sheet's dimension. Guard (plaque à biscuits) + purge.

### Item 15306

![item 15306](images/item-15306.jpg)

- **Name (English):** None
- **Name (French):** Rallonge d'attelage Big Bed Jr.
- **Brand:** Big Bed Jr.
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 99.99
- **Printed Price:** “99.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436756066/1791518209/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `2feef5d3b1287472`
- **Conditions:** `{"discount": 31}`
- **Raw:** `{"id": 1046705814, "flyer_id": 8180834, "name": "Rallonge d'attelage Big Bed Jr.", "display_type": 1, "brand": "Big Bed Jr.", "left": 17478.59, "bottom": -827.31, "right": 17919.15, "top": -502.77, "cutout_image_url": "http://f.wishabi.net/page_items/436756066/1791518209/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 31, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "99.99", "p`

— from flyer 163 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correctly Unclassified, kept for review: Big Bed Jr. trailer-hitch extension, 99.99 — general merchandise, no grocery reading.

### Item 15318

![item 15318](images/item-15318.jpg)

- **Name (English):** None
- **Name (French):** Serpent de jardin illuminé, vert
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 119.99
- **Printed Price:** “119.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436750097/1791518182/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `7e7509ea5faf8f02`
- **Raw:** `{"id": 1046694464, "flyer_id": 8180834, "name": "Serpent de jardin illuminé, vert", "display_type": 1, "brand": null, "left": 3172.94, "bottom": -1655.94, "right": 3452.25, "top": -1453.86, "cutout_image_url": "http://f.wishabi.net/page_items/436750097/1791518182/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "119.99", "print_`

— from flyer 163 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correctly Unclassified, kept: lighted garden snake decoration, 119.99 — merchandise (a "serpent" that is not food; rightly not forced anywhere).

### Item 15334

![item 15334](images/item-15334.jpg)

- **Name (English):** None
- **Name (French):** Dévidoir de tuyau pneumatique avec tuyau hybride, 50 pi.
- **Brand:** MAXIMUM
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 104.99
- **Printed Price:** “104.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436755126/1791518200/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `7aca68dfc3f5df45`
- **Conditions:** `{"discount": 43}`
- **Raw:** `{"id": 1046703894, "flyer_id": 8180834, "name": "Dévidoir de tuyau pneumatique avec tuyau hybride, 50 pi.", "display_type": 1, "brand": "MAXIMUM", "left": 10969.5, "bottom": -1280.35, "right": 11197.46, "top": -1058.95, "cutout_image_url": "http://f.wishabi.net/page_items/436755126/1791518200/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 43, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null`

— from flyer 163 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correctly Unclassified, kept: pneumatic hose reel with 50 ft hybrid hose, 104.99 — hardware.

### Item 15428

![item 15428](images/item-15428.jpg)

- **Name (English):** None
- **Name (French):** Ensemble-cadeau d'entretien automobile, 7 pces ARMOR ALL
- **Brand:** Armor All
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 39.99
- **Printed Price:** “39.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436756204/1791518216/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `0d99056c5546bd9f`
- **Conditions:** `{"discount": 33}`
- **Raw:** `{"id": 1046706110, "flyer_id": 8180834, "name": "Ensemble-cadeau d'entretien automobile, 7 pces ARMOR ALL", "display_type": 1, "brand": "Armor All", "left": 19048.43, "bottom": -2215.04, "right": 19493.57, "top": -1862.83, "cutout_image_url": "http://f.wishabi.net/page_items/436756204/1791518216/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 33, "available_to": "2026-10-21T23:59:59-04:00", "video_url": n`

— from flyer 163 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correctly Unclassified, kept: Armor All 7-piece car-care gift set, 39.99 — automotive.

### Item 15435

![item 15435](images/item-15435.jpg)

- **Name (English):** None
- **Name (French):** Foyer mural Napoleon, 36 po, Relègue 750 W et 1500 W.
- **Brand:** NAPOLEON
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 36 po
- **Price:** 249.99
- **Printed Price:** “249.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436756856/1791518228/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `b774f3c87cab8696`
- **Conditions:** `{"discount": 38}`
- **Raw:** `{"id": 1046706735, "flyer_id": 8180834, "name": "Foyer mural Napoleon, 36 po, Relègue 750 W et 1500 W.", "display_type": 1, "brand": "NAPOLEON", "left": 27327.14, "bottom": -969.59, "right": 28164.67, "top": -652.72, "cutout_image_url": "http://f.wishabi.net/page_items/436756856/1791518228/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 38, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "`

— from flyer 163 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correctly Unclassified, kept: Napoleon 36-inch wall fireplace, 249.99 — appliance.

### Item 15460

![item 15460](images/item-15460.jpg)

- **Name (English):** None
- **Name (French):** Piles au lithium CR2450 NOMA
- **Brand:** NOMA
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 5.07
- **Printed Price:** “5.07”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436756729/1791518226/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `66cf4ebb99f04727`
- **Raw:** `{"id": 1046706687, "flyer_id": 8180834, "name": "Piles au lithium CR2450 NOMA", "display_type": 1, "brand": "NOMA", "left": 28212.17, "bottom": -2255.6, "right": 28657.32, "top": -1862.31, "cutout_image_url": "http://f.wishabi.net/page_items/436756729/1791518226/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "5.07", "print_id"`

— from flyer 163 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correctly Unclassified, kept: NOMA CR2450 lithium batteries, 5.07 — electronics consumable.

### Item 15468

![item 15468](images/item-15468.jpg)

- **Name (English):** None
- **Name (French):** Women in Sport
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
- **Image source URL:** http://f.wishabi.net/page_items/436758849/1791479797/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `b42a1867c9819ca0`
- **Raw:** `{"id": 1047116791, "flyer_id": 8180834, "name": "Women in Sport", "display_type": 5, "brand": null, "left": 29726.89, "bottom": -2548.59, "right": 30257.68, "top": -16.69, "cutout_image_url": "http://f.wishabi.net/page_items/436758849/1791479797/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "", "print_id": null, "short_name":`

— from flyer 163 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Promo tile, not a product: "Women in Sport" with no price — a campaign banner the flyer payload lists as an item. Kept under the current rules (no sanctioned discard for banner tiles beyond the approved exclusion phrases); flagged here as the kind of row a future store-native mapping or banner rule would drop.

### Item 15496

![item 15496](images/item-15496.jpg)

- **Name (English):** None
- **Name (French):** Canada Garage Ad
- **Brand:** Castrol
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** None
- **Printed Price:** None
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437110160/1791774736/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `a10fac7bf90be9fc`
- **Raw:** `{"id": 1047122329, "flyer_id": 8180834, "name": "Canada Garage Ad", "display_type": 5, "brand": "Castrol", "left": 18041.44, "bottom": -2488.82, "right": 18508.1, "top": -36.57, "cutout_image_url": "http://f.wishabi.net/page_items/437110160/1791774736/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "", "print_id": null, "short_`

— from flyer 163 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Promo tile, not a product: "Canada Garage Ad", no price — an advertising tile in the payload. Same disposition as 15468.

### Item 15518

![item 15518](images/item-15518.jpg)

- **Name (English):** None
- **Name (French):** Format de 3,78 L.
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 3,78 L
- **Price:** 39.99
- **Printed Price:** “39.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436886523/1791518220/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `b4961b4e480f3582`
- **Raw:** `{"id": 1046705224, "flyer_id": 8180834, "name": "Format de 3,78 L.", "display_type": 1, "brand": null, "left": 11942.72, "bottom": -1972.13, "right": 12066.73, "top": -1938.03, "cutout_image_url": "http://f.wishabi.net/page_items/436886523/1791518220/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "39.99", "print_id": null, "sh`

— from flyer 163 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Weak data, kept: the name is only a fragment ("Format de 3,78 L." — the product's name line never made it into the payload name) at 39.99. Unclassified, correctly; the fragment gives nothing safe to classify on.

### Item 15555

![item 15555](images/item-15555.jpg)

- **Name (English):** None
- **Name (French):** Remise à toit pointu étanche, 10 x 10 x 8 pi H Weather Fast
- **Brand:** Weather Fast
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 229.99
- **Printed Price:** “229.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436755720/1791518206/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `a2e0aaff779d6457`
- **Conditions:** `{"discount": 38}`
- **Raw:** `{"id": 1046705380, "flyer_id": 8180834, "name": "Remise à toit pointu étanche, 10 x 10 x 8 pi H Weather Fast", "display_type": 1, "brand": "Weather Fast", "left": 12462.25, "bottom": -2198.53, "right": 12691.52, "top": -1972.07, "cutout_image_url": "http://f.wishabi.net/page_items/436755720/1791518206/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 38, "available_to": "2026-10-21T23:59:59-04:00", "video_u`

**Item Review Analysis (Pass 1):** Correctly Unclassified, kept: Weather Fast 10x10x8 ft peaked-roof shed, 229.99 — outdoor merchandise.
