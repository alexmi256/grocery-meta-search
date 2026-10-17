# Marché Richelieu — full product report

Store slug: `marche-richelieu`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 139, valid 2026-10-15 → 2026-10-21, 95 items). The expired Oct 8–14 edition is correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown — classification success on this Flipp feed.
- **Issues found:** none. All ten prices verified against their renders. One shelf note: the Dole pineapple is canned (398 ml tins in the render) but the payload name carries no canned marker, so it sits in Fresh Fruits — a text-only limit, recorded on the item.
- **Fixes applied this pass:** none needed.


## Review Analysis — Pass 2 (2026-10-17, verification after Pass 1)

- No fixes were needed in Pass 1; the packet is unchanged and the verdicts stand (Pass 1 preserved in `marche-richelieu-report-pass1.md`). Store review complete — clean.

## Flyer 139 — valid 2026-10-15 → 2026-10-21 (10 classified items, 0 unclassified)

Source ref: `8179275` · fetched 2026-10-16T12:37:06.810Z

### Item 13832

![item 13832](images/item-13832.jpg)

- **Name (English):** BERGERON CLASSIC CHEESE
- **Name (French):** FROMAGE BERGERON CLASSIQUE
- **Brand:** Bergeron
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** 170-200g
- **Price:** 8.49
- **Printed Price:** “8.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436667589/1791359125/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `a6584545bc0d8001`
- **Raw:** `{"id": 1046286993, "flyer_id": 8179275, "name": "FROMAGE BERGERON CLASSIQUE | BERGERON CLASSIC CHEESE", "display_type": 1, "brand": "Bergeron", "left": 2318.34, "bottom": -2271.72, "right": 2586.92, "top": -2049.38, "cutout_image_url": "http://f.wishabi.net/page_items/436667589/1791359125/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, `

**Item Review Analysis (Pass 1):** Correct. Bergeron Classique cheese (lactose-free, 170-200 g) "à partir de 8.49" — verified on the render. Cheese is right.

### Item 13859

![item 13859](images/item-13859.jpg)

- **Name (English):** WHITE, RED, YELLOW OR RUSSET POTATOES
- **Name (French):** POMMES DE TERRE BLANCHES, ROUGES, JAUNES OU RUSSET
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** 20g
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436667604/1791359121/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `2a17468c33fe9eb1`
- **Conditions:** `{"discount": 60}`
- **Raw:** `{"id": 1046286964, "flyer_id": 8179275, "name": "POMMES DE TERRE BLANCHES, ROUGES, JAUNES OU RUSSET | WHITE, RED, YELLOW OR RUSSET POTATOES", "display_type": 1, "brand": null, "left": 18.6, "bottom": -730.9, "right": 542.66, "top": -219.1, "cutout_image_url": "http://f.wishabi.net/page_items/436667604/1791359121/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 60, "available_to": "2026-10-21T23:59:59-04:00`

**Item Review Analysis (Pass 1):** Correct. Potatoes (white/red/yellow/Russet, Quebec, 5 lb bag) at 1.99 (reg. 4.99) — verified. Fresh Vegetables is right.

### Item 13868

![item 13868](images/item-13868.jpg)

- **Name (English):** LIFE SMART APPLE SNACK
- **Name (French):** COLLATION AUX POMMES MIEUX-ÊTRE
- **Brand:** Life Smart
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** 6/113g
- **Price:** 2.49
- **Printed Price:** “2.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436667667/1791359129/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `0376677b38ddfcff`
- **Conditions:** `{"discount": 29}`
- **Raw:** `{"id": 1046287160, "flyer_id": 8179275, "name": "COLLATION AUX POMMES MIEUX-ÊTRE | LIFE SMART APPLE SNACK", "display_type": 1, "brand": "Life Smart", "left": 6043.76, "bottom": -1934.05, "right": 6332.69, "top": -1629.48, "cutout_image_url": "http://f.wishabi.net/page_items/436667667/1791359129/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 29, "available_to": "2026-10-21T23:59:59-04:00", "video_url": nu`

**Item Review Analysis (Pass 1):** Correct. Mieux-être apple snack cups (6 x 113 g) at 2.49 (reg. 3.49) — verified. Fresh Fruits covers the fruit cups.

### Item 13870

![item 13870](images/item-13870.jpg)

- **Name (English):** MCCAIN PIZZA POCKETS
- **Name (French):** PIZZA POCHETTES MCCAIN
- **Brand:** McCain
- **Category (English):** Frozen Food > Frozen Pizza
- **Category (French):** Produits surgelés > Pizzas surgelées
- **How classified:** rule (`specific-frozen-pizza-products`)
- **Size:** 540-600g
- **Price:** 7.99
- **Printed Price:** “7.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436667656/1791359121/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `a4bdb8be778a94d3`
- **Conditions:** `{"discount": 11}`
- **Raw:** `{"id": 1046287129, "flyer_id": 8179275, "name": "PIZZA POCHETTES MCCAIN | MCCAIN PIZZA POCKETS", "display_type": 1, "brand": "McCain", "left": 6047.59, "bottom": -1270.96, "right": 6334.99, "top": -974.92, "cutout_image_url": "http://f.wishabi.net/page_items/436667656/1791359121/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 11, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "7.`

**Item Review Analysis (Pass 1):** Correct. McCain pizza pockets (frozen, 540-600 g) at 7.99 (reg. 8.99) — verified. Frozen Pizza is right.

### Item 13880

![item 13880](images/item-13880.jpg)

- **Name (English):** P'TIT QUÉBEC CHEESE SNACKS
- **Name (French):** GOÛTERS AU FROMAGE P'TIT QUÉBEC
- **Brand:** P'Tit Quebec
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** 168g
- **Price:** 5.49
- **Printed Price:** “5.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436667664/1791359127/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `b50f43bdb5cd8a31`
- **Conditions:** `{"discount": 8}`
- **Raw:** `{"id": 1046287152, "flyer_id": 8179275, "name": "GOÛTERS AU FROMAGE P'TIT QUÉBEC | P'TIT QUÉBEC CHEESE SNACKS", "display_type": 1, "brand": "P'Tit Quebec", "left": 6333.96, "bottom": -1937.23, "right": 6615.1, "top": -1620.32, "cutout_image_url": "http://f.wishabi.net/page_items/436667664/1791359127/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 8, "available_to": "2026-10-21T23:59:59-04:00", "video_url"`

**Item Review Analysis (Pass 1):** Correct. P'tit Québec cheese snacks (Cracker Barrel, 168 g) at 5.49 (reg. 5.99) — verified. Cheese is right.

### Item 13885

![item 13885](images/item-13885.jpg)

- **Name (English):** GOGO SQUEEZ APPLE SNACK
- **Name (French):** COLLATION AUX POMMES GOGO SQUEEZ
- **Brand:** GoGo squeeZ
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 3.49
- **Printed Price:** “3.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436667649/1791359117/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `78ae79cb07e0655d`
- **Conditions:** `{"discount": 34}`
- **Raw:** `{"id": 1046287110, "flyer_id": 8179275, "name": "COLLATION AUX POMMES GOGO SQUEEZ | GOGO SQUEEZ APPLE SNACK", "display_type": 1, "brand": "GoGo squeeZ", "left": 6337.51, "bottom": -2257.36, "right": 6610.84, "top": -1939.29, "cutout_image_url": "http://f.wishabi.net/page_items/436667649/1791359117/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 34, "available_to": "2026-10-21T23:59:59-04:00", "video_url":`

**Item Review Analysis (Pass 1):** Correct. GoGo Squeez apple snack (4 x 90 g) at 3.49 (reg. 5.29) — verified. Fresh Fruits is right.

### Item 13902

![item 13902](images/item-13902.jpg)

- **Name (English):** PREMIÈRE MOISSON SLICED BREAD
- **Name (French):** PAIN TRANCHÉ PREMIÈRE MOISSON
- **Brand:** PREMIÈRE MOISSON
- **Category (English):** Bakery > Bread
- **Category (French):** Boulangerie > Pain
- **How classified:** rule (`bread`)
- **Size:** 475g
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436667569/1791359121/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `581a9bd0094a9ef8`
- **Conditions:** `{"discount": 25}`
- **Raw:** `{"id": 1046286973, "flyer_id": 8179275, "name": "PAIN TRANCHÉ PREMIÈRE MOISSON | PREMIÈRE MOISSON SLICED BREAD", "display_type": 1, "brand": "PREMIÈRE MOISSON", "left": 1168.93, "bottom": -862.61, "right": 1736.62, "top": -444.47, "cutout_image_url": "http://f.wishabi.net/page_items/436667569/1791359121/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 25, "available_to": "2026-10-21T23:59:59-04:00", "video`

**Item Review Analysis (Pass 1):** Correct. Première Moisson sliced bread (475 g) at 2.99 (reg. 3.99) — verified. Bread is right.

### Item 13909

![item 13909](images/item-13909.jpg)

- **Name (English):** ST-HUBERT POT PIE
- **Name (French):** PÂTÉ ST-HUBERT
- **Brand:** ST-HUBERT
- **Category (English):** Prepared Meals > Quiches & Pies
- **Category (French):** Repas préparés > Quiches et pâtés
- **How classified:** rule (`specific-pot-pie`)
- **Size:** 525-645g
- **Price:** 10.99
- **Printed Price:** “10.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436667592/1791359127/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `8d5405b386e9a48f`
- **Conditions:** `{"discount": 12}`
- **Raw:** `{"id": 1046286996, "flyer_id": 8179275, "name": "PÂTÉ ST-HUBERT | ST-HUBERT POT PIE", "display_type": 1, "brand": "ST-HUBERT", "left": 3163.42, "bottom": -2271.92, "right": 3437.9, "top": -2054.4, "cutout_image_url": "http://f.wishabi.net/page_items/436667592/1791359127/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 12, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "10.99", "pr`

**Item Review Analysis (Pass 1):** Correct. St-Hubert pot pie / tourtière / quiche (525-645 g) at 10.99 (reg. 12.49) — verified. Quiches & Pies is right.

### Item 13911

![item 13911](images/item-13911.jpg)

- **Name (English):** DOLE PINEAPPLE
- **Name (French):** ANANAS DOLE
- **Brand:** Dole
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 2.49
- **Printed Price:** “2.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436667669/1791359130/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `5fe16fcf05d18895`
- **Conditions:** `{"discount": 29}`
- **Raw:** `{"id": 1046287165, "flyer_id": 8179275, "name": "ANANAS DOLE | DOLE PINEAPPLE", "display_type": 1, "brand": "Dole", "left": 6611.01, "bottom": -2257.18, "right": 6896.45, "top": -1937.04, "cutout_image_url": "http://f.wishabi.net/page_items/436667669/1791359130/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 29, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "2.49", "print_id": n`

**Item Review Analysis (Pass 1):** Price correct, shelf note. Dole pineapple (398 ml) at 2.49 (reg. 3.50) — verified; the render shows cans, but the payload name has no canned marker, so Fresh Fruits is the text-only result.

### Item 13922

![item 13922](images/item-13922.jpg)

- **Name (English):** DARE CRISPS CRACKERS
- **Name (French):** CRAQUELINS CRISPS DARE
- **Brand:** Dare
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** 100g
- **Price:** 3.49
- **Printed Price:** “3.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436768310/1791397116/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `3b82357c380c1783`
- **Conditions:** `{"discount": 22}`
- **Raw:** `{"id": 1046386425, "flyer_id": 8179275, "name": "CRAQUELINS CRISPS DARE | DARE CRISPS CRACKERS", "display_type": 1, "brand": "Dare", "left": 4623.89, "bottom": -1787.71, "right": 4899.55, "top": -1398.3, "cutout_image_url": "http://f.wishabi.net/page_items/436768310/1791397116/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 22, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "3.49`

**Item Review Analysis (Pass 1):** Correct. Dare Veggie Crisps crackers (100 g) at 3.49 (reg. 4.49) — verified. Crackers & Cookies is right.
