# IGA Express / Mini — full product report

Store slug: `iga-express`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 122, valid 2026-10-15 → 2026-10-21). **Audit note:** this edition holds exactly 356 items — the same count as IGA's current flyer, and the two banners' older editions match too (371 and 46 items). IGA Express is publishing the IGA circular: same Flipp-sourced content under both storefronts. That is the chain's own distribution (Express locations run the IGA flyer), recorded here so the duplication is a known fact, not a pipeline error.
- **Sample counts:** 10 classified + 0 unclassified shown — classification success on the shared structured feed.
- **Issues found:** none. Every sampled item's product shot matches its name and category; prices are Flipp payload values. One source quirk: the payload itself misspells the Liberté yogurt as "YOGOURT GERC" (for GREC) — reproduced faithfully, not our error.
- **Fixes applied this pass:** none needed.

## Flyer 122 — valid 2026-10-15 → 2026-10-21 (10 classified items, 0 unclassified)

Source ref: `8180961` · fetched 2026-10-16T12:18:22.018Z

### Item 12359

![item 12359](images/item-12359.jpg)

- **Name (English):** CÔTES DE DOS DE PORC FRAIS BÂTON ROUGE
- **Name (French):** CÔTES DE DOS DE PORC FRAIS BÂTON ROUGE
- **Brand:** BÂTON ROUGE
- **Category (English):** Meat > Pork & Ham
- **Category (French):** Viande > Porc et jambon
- **How classified:** rule (`pork-ham`)
- **Size:** 585g
- **Price:** 12.99
- **Printed Price:** “12.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268540/547374b2-c274-11f1-bb28-56ea36667e5c/x_large
- **Details:** SKU: 00000_000000077657896601 · confidence: 1.00 · item_key: `ddd3df9e809ccc3b`
- **Conditions:** `{"description": "585 g"}`
- **Raw:** `{"id": 1046441593, "name": "CÔTES DE DOS DE PORC FRAIS BÂTON ROUGE", "sale_story": null, "sku": "00000_000000077657896601", "description": "585 g", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268540/547374b2-c274-11f1-bb28-56ea36667e5c/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "custom`

**Item Review Analysis (Pass 1):** Correct. Bâton Rouge BBQ pork back ribs (585 g, fully cooked) at 12.99 from the payload — shot matches. Pork & Ham is right.

### Item 12362

![item 12362](images/item-12362.jpg)

- **Name (English):** AILES DE POULET SURGELÉES PINTY'S
- **Name (French):** AILES DE POULET SURGELÉES PINTY'S
- **Brand:** PINTY'S
- **Category (English):** Frozen Food > Frozen Meat and Seafood
- **Category (French):** Produits surgelés > Viande et fruits de mer surgelés
- **How classified:** frozen-remap (`chicken-turkey`)
- **Size:** 700g
- **Price:** 17.99
- **Printed Price:** “17.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268540/5b262bec-c274-11f1-bb28-56ea36667e5c/x_large
- **Details:** SKU: 00000_000000006909463582 · confidence: 1.00 · item_key: `2c260a28bbaddd57`
- **Conditions:** `{"sale_story": "DEUXIÈME À 50% DE RABAIS", "description": "700 ou 720 g"}`
- **Raw:** `{"id": 1046441575, "name": "AILES DE POULET SURGELÉES PINTY'S", "sale_story": "DEUXIÈME À 50% DE RABAIS", "sku": "00000_000000006909463582", "description": "700 ou 720 g", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268540/5b262bec-c274-11f1-bb28-56ea36667e5c/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "custom_id`

**Item Review Analysis (Pass 1):** Correct. Pinty's frozen chicken wings (700 g, Tennessee BBQ) at 17.99 — shot matches. Frozen Meat and Seafood is right.

### Item 12366

![item 12366](images/item-12366.jpg)

- **Name (English):** YOGOURT GERC LIBERTÉ
- **Name (French):** YOGOURT GERC LIBERTÉ
- **Brand:** Liberté
- **Category (English):** Dairy & Eggs > Yogurt
- **Category (French):** Produits laitiers et œufs > Yogourt
- **How classified:** rule (`yogurt`)
- **Size:** None
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268543/581ee7d6-c274-11f1-b3b8-26c84f172ddc/x_large
- **Details:** SKU: 00000_000000006568400510 · confidence: 1.00 · item_key: `405130395cf136e6`
- **Conditions:** `{"description": "650 g ou 750 g"}`
- **Raw:** `{"id": 1046442618, "name": "YOGOURT GERC LIBERTÉ", "sale_story": null, "sku": "00000_000000006568400510", "description": "650 g ou 750 g", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268543/581ee7d6-c274-11f1-b3b8-26c84f172ddc/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "custom_id_field`

**Item Review Analysis (Pass 1):** Correct. Liberté Greek yogurt 0% (750 g) at 6.99 — shot matches; the name's "GERC" is the payload's own misspelling of GREC. Yogurt is right.

### Item 12412

![item 12412](images/item-12412.jpg)

- **Name (English):** MÉLANGE À SAUCE OU MÉLANGE À SAUCE POUR PÂTES KNORR
- **Name (French):** MÉLANGE À SAUCE OU MÉLANGE À SAUCE POUR PÂTES KNORR
- **Brand:** Knorr
- **Category (English):** Pantry > Condiments
- **Category (French):** Produits du garde-manger > Condiments et garnitures
- **How classified:** rule (`condiments`)
- **Size:** None
- **Price:** 4.98
- **Printed Price:** “4.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_items/436821468/1791427541/extra_large.jpg
- **Details:** SKU: 00000_000000005522008071 · confidence: 1.00 · item_key: `657e3841a5258854`
- **Conditions:** `{"description": "22 à 48 g\nSélection variée\nRég. 2,29$ à 2,49$"}`
- **Raw:** `{"id": 1046443227, "name": "MÉLANGE À SAUCE OU MÉLANGE À SAUCE POUR PÂTES KNORR", "sale_story": null, "sku": "00000_000000005522008071", "description": "22 à 48 g\nSélection variée\nRég. 2,29$ à 2,49$", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_items/436821468/1791427541/extra_large.jpg", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "`

**Item Review Analysis (Pass 1):** Correct. Knorr sauce mix (hollandaise pictured) at 4.98 — a group offer over sauce/pasta-sauce mixes. Condiments is right.

### Item 12450

![item 12450](images/item-12450.jpg)

- **Name (English):** CHAMPIGNONS PLEUROTES MÉLANGÉS, GRIS OU ROYAL
- **Name (French):** CHAMPIGNONS PLEUROTES MÉLANGÉS, GRIS OU ROYAL
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** 200g
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268533/54113964-c274-11f1-bbb6-d235ee54bd5b/x_large
- **Details:** SKU: 00000_000000082710100046 · confidence: 1.00 · item_key: `ca70f9c2558fc513`
- **Conditions:** `{"sale_story": "60 scene+ pts", "description": "Produits du Québec\n200 g"}`
- **Raw:** `{"id": 1046444256, "name": "CHAMPIGNONS PLEUROTES MÉLANGÉS, GRIS OU ROYAL", "sale_story": "60 scene+ pts", "sku": "00000_000000082710100046", "description": "Produits du Québec\n200 g", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268533/54113964-c274-11f1-bbb6-d235ee54bd5b/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": nu`

**Item Review Analysis (Pass 1):** Correct. Leciel mixed oyster mushrooms (200 g) at 5.99 — shot matches. Fresh Vegetables is right.

### Item 12525

![item 12525](images/item-12525.jpg)

- **Name (English):** KOMBUCHA BIOLOGIQUE FOUS DE L'ÎLE
- **Name (French):** KOMBUCHA BIOLOGIQUE FOUS DE L'ÎLE
- **Brand:** FOUS DE L' ÎLE
- **Category (English):** Drinks > Non-alcoholic drinks
- **Category (French):** Boissons > Boissons non alcoolisées
- **How classified:** rule (`non-alcoholic`)
- **Size:** 355ML
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268536/55c062e4-c274-11f1-96dc-be11d9e5f703/x_large
- **Details:** SKU: 00000_000000062811067562 · confidence: 1.00 · item_key: `3c88069b43a842a8`
- **Conditions:** `{"disclaimer_text": "Canette consignée", "description": "355 mL\nRég. 3,79$ à 3,99$"}`
- **Raw:** `{"id": 1046445039, "name": "KOMBUCHA BIOLOGIQUE FOUS DE L'ÎLE", "sale_story": null, "sku": "00000_000000062811067562", "description": "355 mL\nRég. 3,79$ à 3,99$", "disclaimer_text": "Canette consignée", "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268536/55c062e4-c274-11f1-96dc-be11d9e5f703/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "cu`

**Item Review Analysis (Pass 1):** Correct. Fous de l'Île organic kombucha (355 ml, lychee passion) at 2.99 — shot matches. Non-alcoholic drinks is right.

### Item 12581

![item 12581](images/item-12581.jpg)

- **Name (English):** TOMATES PELÉES OU POLPA MUTTI
- **Name (French):** TOMATES PELÉES OU POLPA MUTTI
- **Brand:** Mutti
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`canned-pickled`)
- **Size:** 796ml
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268543/5e1cb5e6-c274-11f1-b3b8-26c84f172ddc/x_large
- **Details:** SKU: 00000_000000085469300017 · confidence: 1.00 · item_key: `14471b8901b8d5d2`
- **Conditions:** `{"description": "796 mL\nRég. 6,99$ à 8,49$"}`
- **Raw:** `{"id": 1046442844, "name": "TOMATES PELÉES OU POLPA MUTTI", "sale_story": null, "sku": "00000_000000085469300017", "description": "796 mL\nRég. 6,99$ à 8,49$", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268543/5e1cb5e6-c274-11f1-b3b8-26c84f172ddc/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": n`

**Item Review Analysis (Pass 1):** Correct. Mutti finely chopped tomatoes (Polpa, 796 ml) at 5.99 — shot matches. Canned & Pickled is right.

### Item 12600

![item 12600](images/item-12600.jpg)

- **Name (English):** PIZZA SURGELÉE DR.OETKER
- **Name (French):** PIZZA SURGELÉE DR.OETKER
- **Brand:** Dr. Oetker
- **Category (English):** Frozen Food > Frozen Pizza
- **Category (French):** Produits surgelés > Pizzas surgelées
- **How classified:** frozen-remap (`pizza-prepared`)
- **Size:** 410g
- **Price:** 3.47
- **Printed Price:** “3.47”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268530/5f19ea04-c274-11f1-be97-3e102d04e6b0/x_large
- **Details:** SKU: 00000_000000003338345781 · confidence: 1.00 · item_key: `3fc230934ff00ed9`
- **Conditions:** `{"description": "269 à/to 410 g"}`
- **Raw:** `{"id": 1046440439, "name": "PIZZA SURGELÉE DR.OETKER", "sale_story": null, "sku": "00000_000000003338345781", "description": "269 à/to 410 g", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268530/5f19ea04-c274-11f1-be97-3e102d04e6b0/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "custom_id_f`

**Item Review Analysis (Pass 1):** Correct. Dr. Oetker Casa di Mama frozen pizza (410 g) at 3.47 — shot matches. Frozen Pizza is right.

### Item 12629

![item 12629](images/item-12629.jpg)

- **Name (English):** PÂTES ALIMENTAIRES BIOLOGIQUES CHICKAPEA
- **Name (French):** PÂTES ALIMENTAIRES BIOLOGIQUES CHICKAPEA
- **Brand:** Chickapea
- **Category (English):** Pantry > Pasta & Pasta Sauce
- **Category (French):** Produits du garde-manger > Pâtes et sauces
- **How classified:** rule (`specific-pasta`)
- **Size:** None
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268535/5da0fb7c-c274-11f1-96ba-aad9f7bf7024/x_large
- **Details:** SKU: 00000_000000062845186870 · confidence: 1.00 · item_key: `e0979916ba395c7e`
- **Conditions:** `{"description": "227 g\nRég. 6,49$ à 6,79$"}`
- **Raw:** `{"id": 1046444847, "name": "PÂTES ALIMENTAIRES BIOLOGIQUES CHICKAPEA", "sale_story": null, "sku": "00000_000000062845186870", "description": "227 g\nRég. 6,49$ à 6,79$", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268535/5da0fb7c-c274-11f1-96ba-aad9f7bf7024/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_f`

**Item Review Analysis (Pass 1):** Correct. Chickapea organic chickpea pasta (227 g) at 4.99 — shot matches. Pasta & Pasta Sauce is right.

### Item 12675

![item 12675](images/item-12675.jpg)

- **Name (English):** BOUILLON CAMPBELL'S
- **Name (French):** BOUILLON CAMPBELL'S
- **Brand:** Campbell's
- **Category (English):** Prepared Meals > Salads & Soups
- **Category (French):** Repas préparés > Salades et soupes
- **How classified:** rule (`specific-broth`)
- **Size:** 900ml
- **Price:** 1.47
- **Printed Price:** “1.47”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268530/61175c9c-c274-11f1-be97-3e102d04e6b0/x_large
- **Details:** SKU: 00000_000000006321112114 · confidence: 1.00 · item_key: `a579b20a9d9326cd`
- **Conditions:** `{"disclaimer_text": "*Excepté biologique\n\nSans carte Scène+ 1,77", "description": "900 ml\nReg. 2,69$ à 3,19$"}`
- **Raw:** `{"id": 1046440419, "name": "BOUILLON CAMPBELL'S", "sale_story": null, "sku": "00000_000000006321112114", "description": "900 ml\nReg. 2,69$ à 3,19$", "disclaimer_text": "*Excepté biologique\n\nSans carte Scène+ 1,77", "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268530/61175c9c-c274-11f1-be97-3e102d04e6b0/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field`

**Item Review Analysis (Pass 1):** Correct. Campbell's chicken broth (900 ml) at 1.47 — shot matches. Salads & Soups is the taxonomy's broth shelf.
