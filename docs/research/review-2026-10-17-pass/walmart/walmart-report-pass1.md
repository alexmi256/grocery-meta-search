# Walmart — full product report

Store slug: `walmart`. Generated from `data/grocery.db`. A sampled subset of 20 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 2 concurrent (flyer 170: the 225-item weekly, Oct 15–21; flyer 171: a 97-item promo book, Oct 15 – Nov 11). The expired Oct 8–14 flyer (286 items) is correctly excluded.
- **Sample counts:** 10 classified + 10 unclassified shown (split across both flyers).
- **Issues found:** Walmart is a Flipp-payload store — the renders are product cutouts, so vision verifies identity and the payload carries the price (the two renders that do print prices, the Cadbury Celebrations tin at 11.98 and the Dairy Milk bars at 2.62, match the payload exactly). One junk record: item 16166, whose name is an image filename ("FR_1242x210_Flash Deals 40-3") over a flash-deals banner — deleted. One classifier trap: the Lemon Aide floor cleaner ("NETTOYANT POUR PLANCHERS") sits in Fresh Fruits on "Lemon" — left as the text-only classifier's result and flagged here. The unclassified sample is Walmart's general merchandise (kids' boots, a dog ball launcher, diapers, plastic cups) plus household cleaners — kept for review.
- **Fixes applied this pass:** item 16166 deleted (banner junk).

## Flyer 170 — valid 2026-10-15 → 2026-10-21 (5 classified items, 6 unclassified)

Source ref: `8185037` · fetched 2026-10-17T06:31:59.530Z

### Item 16029

![item 16029](images/item-16029.jpg)

- **Name (English):** Nettoyant tout naturel Lemon Aide
- **Name (French):** Nettoyant tout naturel Lemon Aide
- **Brand:** Lemonaide
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 7.97
- **Printed Price:** “7.97”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24275768/3f0f07fe-c368-11f1-bb71-c2b36a6db0c1/x_large
- **Details:** SKU: 6000206441218 · confidence: 1.00 · item_key: `0002c1ee53961e97`
- **Conditions:** `{"description": "Chac. Variétés sélectionnées.\n#50225718."}`
- **Raw:** `{"id": 1047227541, "name": "Nettoyant tout naturel Lemon Aide", "sale_story": null, "sku": "6000206441218", "description": "Chac. Variétés sélectionnées.\n#50225718.", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24275768/3f0f07fe-c368-11f1-bb71-c2b36a6db0c1/x_large", "custom_id_field_1": "6000206441218", "custom_id_field_2": null, "custom_id_field_3": null, "cu`

**Item Review Analysis (Pass 1):** Classifier trap, left as-is. Lemon Aide floor cleaner ("NETTOYANT POUR PLANCHERS — à l'huile essentielle de citron") — identity verified on the cutout; the classifier shelved it in Fresh Fruits on "Lemon". Flagged in the header.

### Item 16031

![item 16031](images/item-16031.jpg)

- **Name (English):** Cheddar Balderson
- **Name (French):** Balderson cheddar ou Mon marché fraîcheur double cream brie
- **Brand:** Balderson
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** None
- **Price:** 6.67
- **Printed Price:** “6.67”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24270707/ddde30a2-c2a1-11f1-b4bb-6e73685caa31/x_large
- **Details:** SKU: 6000205483611 · confidence: 1.00 · item_key: `402a9f76ae881302`
- **Conditions:** `{"sale_story": "Chute de prix", "description": "Chac. Variétés et formats sélectionnés.\nN° 31397272."}`
- **Raw:** `{"id": 1047085233, "name": "Balderson cheddar ou Mon marché fraîcheur double cream brie", "sale_story": "Chute de prix", "sku": "6000205483611", "description": "Chac. Variétés et formats sélectionnés.\nN° 31397272.", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24270707/ddde30a2-c2a1-11f1-b4bb-6e73685caa31/x_large", "custom_id_field_1": "6000205483611", "custom_`

**Item Review Analysis (Pass 1):** Correct. Balderson cheddar or Your Fresh Market double-cream brie (200 g) at 6.67 — the cutout shows the brie. Cheese is right.

### Item 16120

![item 16120](images/item-16120.jpg)

- **Name (English):** Garniture fouettée Great Value 1 L ou croûtes à tarte profondes Tenderflake 340 - 397 g
- **Name (French):** Garniture fouettée Great Value 1 L ou croûtes à tarte profondes Tenderflake 340 - 397 g
- **Brand:** Great Value
- **Category (English):** Bakery > Cakes
- **Category (French):** Boulangerie > Gâteaux
- **How classified:** rule (`cakes`)
- **Size:** 1 L
- **Price:** 2.97
- **Printed Price:** “2.97”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24270724/e52f8c2a-c2a1-11f1-864c-ba095fce49c5/x_large
- **Details:** SKU: 6000191270221 · confidence: 1.00 · item_key: `92776fa334594ea1`
- **Conditions:** `{"sale_story": "Chute de prix", "description": "Chac. Surgelées.\nVariétés sélectionnées.\nN° 9130968."}`
- **Raw:** `{"id": 1047086149, "name": "Garniture fouettée Great Value 1 L ou croûtes à tarte profondes Tenderflake 340 - 397 g", "sale_story": "Chute de prix", "sku": "6000191270221", "description": "Chac. Surgelées.\nVariétés sélectionnées.\nN° 9130968.", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24270724/e52f8c2a-c2a1-11f1-864c-ba095fce49c5/x_large", "custom_id_field_`

**Item Review Analysis (Pass 1):** Correct. Great Value whipped topping (1 L) or Tenderflake pie shells (2 x 350 g) at 2.97 — the cutout shows the Tenderflake shells. (Shelved under Cakes for the shells.)

### Item 16140

![item 16140](images/item-16140.jpg)

- **Name (English):** Biscuits Marie Gold de Britania
- **Name (French):** Biscuits Marie Gold de Britania
- **Brand:** Britannia
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** None
- **Price:** 0.97
- **Printed Price:** “0.97”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24282669/ddb114e8-c51a-11f1-8cf8-46d0f523916a/x_large
- **Details:** SKU: 6000199196140 · confidence: 1.00 · item_key: `7d342cd453227bee`
- **Conditions:** `{"sale_story": "Chute de prix", "description": "Chac. 150 g.\nEach. N° 30513032."}`
- **Raw:** `{"id": 1047228622, "name": "Biscuits Marie Gold de Britania", "sale_story": "Chute de prix", "sku": "6000199196140", "description": "Chac. 150 g.\nEach. N° 30513032.", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24282669/ddb114e8-c51a-11f1-8cf8-46d0f523916a/x_large", "custom_id_field_1": "6000199196140", "custom_id_field_2": null, "custom_id_field_3": null, "cu`

**Item Review Analysis (Pass 1):** Correct. Britannia Marie Gold biscuits at 0.97 — identity verified. Crackers & Cookies is right.

### Item 16171

![item 16171](images/item-16171.jpg)

- **Name (English):** Craquelins RITZ de Christie
- **Name (French):** Craquelins RITZ de Christie
- **Brand:** Ritz
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** 180 g
- **Price:** 2.48
- **Printed Price:** “2.48”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24270724/efddc592-c2a1-11f1-864c-ba095fce49c5/x_large
- **Details:** SKU: 2I6TH6ZDIXWL · confidence: 1.00 · item_key: `41171b9db470c4be`
- **Conditions:** `{"sale_story": "Chute de prix", "description": "Chac. Variétés sélectionnées.\n162 - 180 g.\n# 50297426."}`
- **Raw:** `{"id": 1047086124, "name": "Craquelins RITZ de Christie", "sale_story": "Chute de prix", "sku": "2I6TH6ZDIXWL", "description": "Chac. Variétés sélectionnées.\n162 - 180 g.\n# 50297426.", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24270724/efddc592-c2a1-11f1-864c-ba095fce49c5/x_large", "custom_id_field_1": "2I6TH6ZDIXWL", "custom_id_field_2": null, "custom_id_f`

## Flyer 171 — valid 2026-10-15 → 2026-11-11 (5 classified items, 4 unclassified)

Source ref: `8186434` · fetched 2026-10-17T06:31:59.913Z

**Item Review Analysis (Pass 1):** Correct. Christie Ritz crackers (180 g) at 2.48 — identity verified. Crackers & Cookies is right.

### Item 16179

![item 16179](images/item-16179.jpg)

- **Name (English):** Barre de chocolat à partager Dairy Milk de Cadbury
- **Name (French):** Boîte métallique de chocolats Celebrations de Cadbury
- **Brand:** Cadbury
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 353 g
- **Price:** 11.98
- **Printed Price:** “11.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-11-11
- **Image source URL:** https://f.wishabi.net/page_items/437465849/1792113179/extra_large.jpg
- **Details:** SKU: 5DU93P15LG7M · confidence: 1.00 · item_key: `af935196280513ea`
- **Conditions:** `{"sale_story": "Chute de prix", "description": "353 g"}`
- **Raw:** `{"id": 1047908440, "name": "Boîte métallique de chocolats Celebrations de Cadbury", "sale_story": "Chute de prix", "sku": "5DU93P15LG7M", "description": "353 g", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-11-11T23:59:59-05:00", "image_url": "https://f.wishabi.net/page_items/437465849/1792113179/extra_large.jpg", "custom_id_field_1": "5DU93P15LG7M", "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "cust`

**Item Review Analysis (Pass 1):** Correct. Cadbury Celebrations chocolate tin (353 g) at 11.98 (down from 13.98) — the price prints on this render and matches the payload. Candy & Chocolate is right.

### Item 16212

![item 16212](images/item-16212.jpg)

- **Name (English):** Barre de chocolat Dairy Milk de Cadbury 90 - 105 g
- **Name (French):** Barre de chocolat Dairy Milk de Cadbury 90 - 105 g
- **Brand:** Cadbury
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 90 - 105 g
- **Price:** 2.62
- **Printed Price:** “2.62”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-11-11
- **Image source URL:** https://f.wishabi.net/page_items/437465847/1792113178/extra_large.jpg
- **Details:** SKU: 28HWNCSUCTSU · confidence: 1.00 · item_key: `5540ac10ba4ba4b7`
- **Raw:** `{"id": 1047908436, "name": "Barre de chocolat Dairy Milk de Cadbury 90 - 105 g", "sale_story": null, "sku": "28HWNCSUCTSU", "description": null, "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-11-11T23:59:59-05:00", "image_url": "https://f.wishabi.net/page_items/437465847/1792113178/extra_large.jpg", "custom_id_field_1": "28HWNCSUCTSU", "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "custom_id_field_5": n`

**Item Review Analysis (Pass 1):** Correct. Cadbury Dairy Milk bars (90-105 g) at 2.62 — printed on the render, matches the payload. Candy & Chocolate is right.

### Item 16222

![item 16222](images/item-16222.jpg)

- **Name (English):** Boîte de 24 chocolats Ferrero Collection Experience ou Ferrero Roche
- **Name (French):** Boîte de 24 chocolats Ferrero Collection Experience ou Ferrero Roche
- **Brand:** Ferrero
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** None
- **Price:** 12.97
- **Printed Price:** “12.97”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-11-11
- **Image source URL:** https://f.wishabi.net/page_items/437465855/1792113182/extra_large.jpg
- **Details:** SKU: 6000188432756 · confidence: 1.00 · item_key: `bafacbd01aadb0b9`
- **Conditions:** `{"sale_story": "Chute de prix", "description": "30800165"}`
- **Raw:** `{"id": 1047908452, "name": "Boîte de 24 chocolats Ferrero Collection Experience ou Ferrero Roche", "sale_story": "Chute de prix", "sku": "6000188432756", "description": "30800165", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-11-11T23:59:59-05:00", "image_url": "https://f.wishabi.net/page_items/437465855/1792113182/extra_large.jpg", "custom_id_field_1": "6000188432756", "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_f`

**Item Review Analysis (Pass 1):** Correct. Ferrero Collection / Rocher 24-chocolate box at 12.97 — the cutout shows the Rocher 24. Candy & Chocolate is right.

### Item 16252

![item 16252](images/item-16252.jpg)

- **Name (English):** Ferrero Rocher® or Ferrero Collection chocolates 16s
- **Name (French):** Ferrero Rocher® or Ferrero Collection chocolates 16s
- **Brand:** Ferrero
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** None
- **Price:** 10.47
- **Printed Price:** “10.47”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-11-11
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24303264/8e28960c-c8d6-11f1-8e45-5e7ab7a55f55/x_large
- **Details:** SKU: 10293352 · confidence: 1.00 · item_key: `0ca3c5f8bd189b49`
- **Raw:** `{"id": 1047908444, "name": "Ferrero Rocher® or Ferrero Collection chocolates 16s", "sale_story": null, "sku": "10293352", "description": null, "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-11-11T23:59:59-05:00", "image_url": "https://f.wishabi.net/page_pdf_images/24303264/8e28960c-c8d6-11f1-8e45-5e7ab7a55f55/x_large", "custom_id_field_1": "10293352", "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "custo`

**Item Review Analysis (Pass 1):** Correct. Ferrero Rocher or Ferrero Collection chocolates at 10.47 — group cutout verified. Candy & Chocolate is right.

### Item 16260

![item 16260](images/item-16260.jpg)

- **Name (English):** Biscuits Peak Freans de CHRISTIE
- **Name (French):** Biscuits Peak Freans de CHRISTIE
- **Brand:** Christie
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** 300g
- **Price:** 4.28
- **Printed Price:** “4.28”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-11-11
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24297608/bdda2c52-c855-11f1-8152-ca4a88f45bd4/x_large
- **Details:** SKU: 10238647 · confidence: 1.00 · item_key: `da077c38e219ca70`
- **Conditions:** `{"description": "N°30748659"}`
- **Raw:** `{"id": 1047935111, "name": "Biscuits Peak Freans de CHRISTIE", "sale_story": null, "sku": "10238647", "description": "N°30748659", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-11-11T23:59:59-05:00", "image_url": "https://f.wishabi.net/page_pdf_images/24297608/bdda2c52-c855-11f1-8152-ca4a88f45bd4/x_large", "custom_id_field_1": "10238647", "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "custom_id_field_5`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 170 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Christie Peak Freans biscuits (digestive / fruit crème, 300 g) at 4.28 — identity verified. Crackers & Cookies is right.

### Item 15961

![item 15961](images/item-15961.jpg)

- **Name (English):** Bottillons mode pour enfants ou tout-petits
- **Name (French):** Bottillons mode pour enfants ou tout-petits
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 29.00
- **Printed Price:** “29.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24301578/17e7bbae-c8ad-11f1-b75f-82ec5d3fe613/x_large
- **Details:** SKU: 0SK43WXNWXJE · confidence: 1.00 · item_key: `5780a4ade9de47f9`
- **Conditions:** `{"description": "La paire.\nN° 51014603"}`
- **Raw:** `{"id": 1047878240, "name": "Bottillons mode pour enfants ou tout-petits", "sale_story": null, "sku": "0SK43WXNWXJE", "description": "La paire.\nN° 51014603", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24301578/17e7bbae-c8ad-11f1-b75f-82ec5d3fe613/x_large", "custom_id_field_1": "0SK43WXNWXJE", "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_fie`

— from flyer 170 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct as merchandise. Kids'/toddlers' fashion boots at 29.00 — identity verified. Unclassified, kept for review.

### Item 16087

![item 16087](images/item-16087.jpg)

- **Name (English):** Quatre-quarts tranché Mon marche fraîcheurMc
- **Name (French):** Quatre-quarts tranché Mon marche fraîcheurMc
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 5.24
- **Printed Price:** “5.24”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24270712/dc127210-c2a1-11f1-9c45-debafaa9e176/x_large
- **Details:** SKU: 7A8RPBZ5XUWW · confidence: 1.00 · item_key: `4442fe59e057b718`
- **Conditions:** `{"description": "Chac. Varietes et formats\nsélectionnés.\nN° 51124256"}`
- **Raw:** `{"id": 1047085674, "name": "Quatre-quarts tranché Mon marche fraîcheurMc", "sale_story": null, "sku": "7A8RPBZ5XUWW", "description": "Chac. Varietes et formats\nsélectionnés.\nN° 51124256", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24270712/dc127210-c2a1-11f1-9c45-debafaa9e176/x_large", "custom_id_field_1": "7A8RPBZ5XUWW", "custom_id_field_2": null, "custom_i`

— from flyer 170 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct as captured. Your Fresh Market sliced butter-pecan pound cake (400 g, 8 slices) at 5.24 — identity verified; unclassified under its glued bilingual name.

### Item 16089

![item 16089](images/item-16089.jpg)

- **Name (English):** Lance-balle Chuckit!
- **Name (French):** Lance-balle Chuckit!
- **Brand:** Chuckit!
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 29.97
- **Printed Price:** “29.97”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24270757/fbc787c6-c2a1-11f1-b320-eeb6002e303f/x_large
- **Details:** SKU: 1OEFX1DL6TI3 · confidence: 1.00 · item_key: `475d78dde12b775e`
- **Conditions:** `{"description": "Chac. N° 51115906."}`
- **Raw:** `{"id": 1047088807, "name": "Lance-balle Chuckit!", "sale_story": null, "sku": "1OEFX1DL6TI3", "description": "Chac. N° 51115906.", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24270757/fbc787c6-c2a1-11f1-b320-eeb6002e303f/x_large", "custom_id_field_1": "1OEFX1DL6TI3", "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "custom_id_fie`

— from flyer 170 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct as merchandise. Chuckit! ball launcher (pet toy) at 29.97 — identity verified. Unclassified, kept for review.

### Item 16129

![item 16129](images/item-16129.jpg)

- **Name (English):** Nettoyant Attitude
- **Name (French):** Nettoyant Attitude
- **Brand:** Attitude
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 5.96
- **Printed Price:** “5.96”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24275768/3421ea96-c368-11f1-bb71-c2b36a6db0c1/x_large
- **Details:** SKU: 6000202319394 · confidence: 1.00 · item_key: `6573fd1cb369bfeb`
- **Conditions:** `{"description": "Each. Selected varieties.\nN° 30159727."}`
- **Raw:** `{"id": 1047227522, "name": "Nettoyant Attitude", "sale_story": null, "sku": "6000202319394", "description": "Each. Selected varieties.\nN° 30159727.", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24275768/3421ea96-c368-11f1-bb71-c2b36a6db0c1/x_large", "custom_id_field_1": "6000202319394", "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4":`

— from flyer 170 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct as merchandise. Attitude kitchen cleaner disinfectant (800 ml) at 5.96 — identity verified. Unclassified, kept for review.

### Item 16143

![item 16143](images/item-16143.jpg)

- **Name (English):** Rascals Night Pants
- **Name (French):** Rascals Night Pants
- **Brand:** Rascals
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 17-32 kg
- **Price:** 25.88
- **Printed Price:** “25.88”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24270732/f1a878e0-c2a1-11f1-8552-96afbad3421d/x_large
- **Details:** SKU: 6000208889651 · confidence: 1.00 · item_key: `690f0562462634b4`
- **Conditions:** `{"description": "NIGHTTIME UNDERWEAR\nSelected varieties and sizes.\nN° 50706485."}`
- **Raw:** `{"id": 1047087012, "name": "Rascals Night Pants", "sale_story": null, "sku": "6000208889651", "description": "NIGHTTIME UNDERWEAR\nSelected varieties and sizes.\nN° 50706485.", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24270732/f1a878e0-c2a1-11f1-8552-96afbad3421d/x_large", "custom_id_field_1": "6000208889651", "custom_id_field_2": null, "custom_id_field_3": `

— from flyer 170 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct as merchandise. Rascals Night Pants (S/M, 44 count) at 25.88 — identity verified. Unclassified, kept for review.

### Item 16166

![item 16166](images/item-16166.jpg)

- **Name (English):** FR_1242x210_Flash Deals 40-3
- **Name (French):** FR_1242x210_Flash Deals 40-3
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
- **Image source URL:** https://f.wishabi.net/page_items/437227794/1791934249/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `a90466047abcb7f6`
- **Raw:** `{"id": 1047406574, "name": "FR_1242x210_Flash Deals 40-3", "sale_story": null, "sku": null, "description": null, "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_items/437227794/1791934249/extra_large.jpg", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "custom_id_field_5": null, "custom_id_field_6": null, "valid_fro`

— from flyer 171 (valid 2026-10-15 → 2026-11-11)

**Item Review Analysis (Pass 1):** DELETED — a flash-deals promo banner ("Aubaines éclair — jusqu'à 40%") whose stored name is the banner's image filename. No product, no price.

### Item 16184

![item 16184](images/item-16184.jpg)

- **Name (English):** Boisson Rubicon
- **Name (French):** Boisson Rubicon
- **Brand:** Rubicon
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 1.98
- **Printed Price:** “1.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-11-11
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24282669/d4e8cc34-c51a-11f1-8cf8-46d0f523916a/x_large
- **Details:** SKU: 6000189293134 · confidence: 1.00 · item_key: `35a179bbd872c99e`
- **Conditions:** `{"sale_story": "Chute de prix", "description": "Chac. Variétés sélectionnées. 1l.\nN° 9205321."}`
- **Raw:** `{"id": 1047238823, "name": "Boisson Rubicon", "sale_story": "Chute de prix", "sku": "6000189293134", "description": "Chac. Variétés sélectionnées. 1l.\nN° 9205321.", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-11-11T23:59:59-05:00", "image_url": "https://f.wishabi.net/page_pdf_images/24282669/d4e8cc34-c51a-11f1-8cf8-46d0f523916a/x_large", "custom_id_field_1": "6000189293134", "custom_id_field_2": null, "custom_id_field_3": null, "cust`

— from flyer 171 (valid 2026-10-15 → 2026-11-11)

**Item Review Analysis (Pass 1):** Correct. Rubicon mango exotic juice drink (1 L) at 1.98 — identity verified. Unclassified under its short name.

### Item 16188

![item 16188](images/item-16188.jpg)

- **Name (English):** Couverts en bois Eco de Great Value
- **Name (French):** Couverts en bois Eco de Great Value
- **Brand:** Great Value
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 18.76
- **Printed Price:** “18.76”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-11-11
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24297595/b7908e22-c855-11f1-bf94-ce6741743b9e/x_large
- **Details:** SKU: 6000203500660 · confidence: 1.00 · item_key: `bfdacefbb40f9884`
- **Conditions:** `{"description": "#31712686"}`
- **Raw:** `{"id": 1047930834, "name": "Couverts en bois Eco de Great Value", "sale_story": null, "sku": "6000203500660", "description": "#31712686", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-11-11T23:59:59-05:00", "image_url": "https://f.wishabi.net/page_pdf_images/24297595/b7908e22-c855-11f1-bf94-ce6741743b9e/x_large", "custom_id_field_1": "6000203500660", "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "custo`

— from flyer 171 (valid 2026-10-15 → 2026-11-11)

**Item Review Analysis (Pass 1):** Correct as merchandise. Great Value Eco wooden cutlery at 18.76 — identity verified (a large-count pack at the payload price; cutouts carry no badge to cross-check). Unclassified, kept for review.

### Item 16191

![item 16191](images/item-16191.jpg)

- **Name (English):** Gobelets rouges ou transparents paq. de 60 ou gobelets de couleur Great Value Paq. de 40.
- **Name (French):** Gobelets rouges ou transparents paq. de 60 ou gobelets de couleur Great Value Paq. de 40.
- **Brand:** Great Value
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 5.97
- **Printed Price:** “5.97”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-11-11
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24297595/bcbfd07e-c855-11f1-bf94-ce6741743b9e/x_large
- **Details:** SKU: 7AUUZ01IB1TT · confidence: 1.00 · item_key: `2397cf3a8999c11e`
- **Raw:** `{"id": 1047930939, "name": "Gobelets rouges ou transparents paq. de 60 ou gobelets de couleur Great Value Paq. de 40.", "sale_story": null, "sku": "7AUUZ01IB1TT", "description": null, "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-11-11T23:59:59-05:00", "image_url": "https://f.wishabi.net/page_pdf_images/24297595/bcbfd07e-c855-11f1-bf94-ce6741743b9e/x_large", "custom_id_field_1": "7AUUZ01IB1TT", "custom_id_field_2": null, "custom_id_fiel`

— from flyer 171 (valid 2026-10-15 → 2026-11-11)

**Item Review Analysis (Pass 1):** Correct as merchandise. Great Value plastic cups (60 count) at 5.97 — identity verified. Unclassified, kept for review.

### Item 16262

![item 16262](images/item-16262.jpg)

- **Name (English):** Dessert Brar's
- **Name (French):** Dessert Brar's
- **Brand:** Brar's
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 9.27
- **Printed Price:** “9.27”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-11-11
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24282669/dfc7752e-c51a-11f1-8cf8-46d0f523916a/x_large
- **Details:** SKU: 6000196034795 · confidence: 1.00 · item_key: `7b1aedf5d5eca447`
- **Conditions:** `{"sale_story": "Chute de prix", "description": "Chac. Variétés et formats sélectionnés.\nN° 30392188."}`
- **Raw:** `{"id": 1047239135, "name": "Dessert Brar's", "sale_story": "Chute de prix", "sku": "6000196034795", "description": "Chac. Variétés et formats sélectionnés.\nN° 30392188.", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-11-11T23:59:59-05:00", "image_url": "https://f.wishabi.net/page_pdf_images/24282669/dfc7752e-c51a-11f1-8cf8-46d0f523916a/x_large", "custom_id_field_1": "6000196034795", "custom_id_field_2": null, "custom_id_field_3": null,`

**Item Review Analysis (Pass 1):** Correct. Brar's Kesar Rasmalai dessert (12 pieces, 850 g) at 9.27 — identity verified. Unclassified under its short name.
