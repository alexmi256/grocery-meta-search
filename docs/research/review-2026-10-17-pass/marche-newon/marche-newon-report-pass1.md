# Marché Newon — full product report

Store slug: `marche-newon`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 2 concurrent publications (flyer 137: 45 items; flyer 138: 21 items — both valid 2026-10-16 → 2026-10-22). The expired Oct 9–15 pair is correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown across the two flyers — classification success; the shortfall is the split across two publications, not a failure.
- **Issues found:** 6 wrong prices of 10. This flyer sets prices as a big dollar digit with superscript cents, and the segmenter repeatedly dropped the dollar digit or read the cents as the price: egg-tart pastry 98.00 (prints 10.88), samosas 88.00 (prints 1.88), yellow onions 98.00 (prints 0.98/bag), Classico sauce stored the Dettol antiseptic's 10.98 from the cell above (the sauce prints 3.98), Peking duck 7.00 (prints 11.88). The rock sugar's 59.00 is a real case price with its cents dropped (prints 59.98/boîte for 50 x 454 g; unit now pack). The right-edge crop clipping noted in round 2 is visible again on several crops — the badges sit at the pages' right edge and the zooms above the crops were needed to read them.
- **Fixes applied this pass:** 13786 → 10.88, 13796 → 1.88, 13799 → 59.98 (pack), 13806 → 3.98, 13811 → 11.88, 13814 → 0.98.

## Flyer 137 — valid 2026-10-16 → 2026-10-22 (7 classified items, 0 unclassified)

Source ref: `circulaire-marche-newon-jean-talon-du-16-au-22-octobre-2026` · fetched 2026-10-16T12:37:03.382Z

### Item 13771

![item 13771](images/item-13771.jpg)

- **Name (English):** None
- **Name (French):** PAMPANGA. TRANCHE DE PORC PORK TOGO À
- **Brand:** None
- **Category (English):** International Foods > Filipino Foods
- **Category (French):** Aliments internationaux > Aliments des Philippines
- **How classified:** rule (`filipino`)
- **Size:** 375G
- **Price:** 3.98
- **Printed Price:** “3.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 441, top 917, right 590, bottom 957, page 2
- **Full page:** [pages/flyer137-page2-1e60f4dd72.jpg (flyer page 2)](pages/flyer137-page2-1e60f4dd72.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-newon-jean-talon-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.95 · item_key: `b57cc40aa3dfe387`
- **Raw:** `{"block_text": "PAMPANGA.\nTRANCHE DE PORC\nPORK TOGO À", "ocr_lines": ["PAMPANGA.", "TRANCHEDEPORC", "PORKTOCINO"], "harvest": {"size": "375G", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Pampanga pork tocino (375 g) at 3.98 — verified on the crop. Filipino Foods is right.

### Item 13786

![item 13786](images/item-13786.jpg)

- **Name (English):** None
- **Name (French):** PATE FEUILLETEE POUR OEUF TART RZ iB EACH RL 2.2LB/51PCS
- **Brand:** None
- **Category (English):** Dairy & Eggs > Desserts & Doughs
- **Category (French):** Produits laitiers et œufs > Desserts et pâtes
- **How classified:** rule (`specific-doughs`)
- **Size:** 2.2LB/51PCS
- **Price:** 98.00
- **Printed Price:** “98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 53, top 166, right 238, bottom 316, page 3
- **Full page:** [pages/flyer137-page3-67e1c74251.jpg (flyer page 3)](pages/flyer137-page3-67e1c74251.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-newon-jean-talon-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `ec26902ce695b755`
- **Raw:** `{"block_text": "PATE FEUILLETEE POUR OEUF\nTART RZ iB EACH RL\n2.2LB/51PCS", "ocr_lines": ["PATEFEUILLETEEPOUROEUF", "2.2LB/51PCS"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 3. Egg tart puff pastry (2.2 lb / 51 pcs) prints 10.88; the DB had 98.00 (dollar digit dropped, cents read as dollars). Desserts & Doughs is right.

### Item 13787

![item 13787](images/item-13787.jpg)

- **Name (English):** None
- **Name (French):** COTES DE PORCEPICE /\ARGE/SPICY PORK™
- **Brand:** None
- **Category (English):** Meat > Pork & Ham
- **Category (French):** Viande > Porc et jambon
- **How classified:** rule (`pork-ham`)
- **Size:** None
- **Price:** 10.99
- **Printed Price:** “10.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 769, top 597, right 952, bottom 649, page 3
- **Full page:** [pages/flyer137-page3-67e1c74251.jpg (flyer page 3)](pages/flyer137-page3-67e1c74251.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-newon-jean-talon-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `07c83aa13c8ff996`
- **Raw:** `{"block_text": "COTES DE PORCEPICE\n/\\ARGE/SPICY PORK™", "ocr_lines": ["COTES DEPORCEPICE", "AARGE/SPICYPORK"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Spicy pork ribs at 10.99 — verified on the crop. Pork & Ham is right.

### Item 13796

![item 13796](images/item-13796.jpg)

- **Name (English):** None
- **Name (French):** PREMIUM SAMOSA DESHI STYLE
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Appetizers & Snacks
- **Category (French):** Produits surgelés > Entrées et collations surgelés
- **How classified:** rule (`frozen-appetizers`)
- **Size:** 400G
- **Price:** 88.00
- **Printed Price:** “88”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 755, top 151, right 950, bottom 188, page 3
- **Full page:** [pages/flyer137-page3-67e1c74251.jpg (flyer page 3)](pages/flyer137-page3-67e1c74251.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-newon-jean-talon-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `cebefef38f3bfe6c`
- **Raw:** `{"block_text": "PREMIUM SAMOSA DESHI STYLE.", "ocr_lines": ["PREMIUMSAMOSADESHISTYLE"], "harvest": {"size": "400G", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Premium Deshi-style vegetable samosas (400 g) print 1.88; the DB had 88.00. Frozen Appetizers & Snacks is right.

### Item 13799

![item 13799](images/item-13799.jpg)

- **Name (English):** SUN FUNGPrO®
- **Name (French):** ! SUCRE mes LOCK SUGAR D'ORGE EEE NORCEALUK | D A KE EN Q 10}
- **Brand:** None
- **Category (English):** Pantry > Baking Essentials
- **Category (French):** Produits du garde-manger > Essentiels de cuisson
- **How classified:** rule (`baking`)
- **Size:** 50x454G
- **Price:** 59.00
- **Printed Price:** “59”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 255, top 604, right 402, bottom 681, page 4
- **Full page:** [pages/flyer137-page4-df8fc771ae.jpg (flyer page 4)](pages/flyer137-page4-df8fc771ae.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-newon-jean-talon-du-16-au-22-octobre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `0d91829945086202`
- **Raw:** `{"block_text": "SUN FUNGPrO® |!\n\nSUCRE mes LOCK SUGAR\n\nD'ORGE EEE\n\nNORCEALUK | D A\nKE EN Q 10}", "ocr_lines": ["OCK SUGAR", "SUCRE", "D'ORGEN", "MORCEAUX"], "harvest": {"size": "50x454G", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED (cents) from the crop. Sun Fung rock sugar is a restaurant case (50 x 454 g) at 59.98 per box; the DB had 59.00 with the cents dropped. Unit now pack. Baking Essentials is the classifier's sugar shelf.

### Item 13806

![item 13806](images/item-13806.jpg)

- **Name (English):** None
- **Name (French):** CLASSICO. SAUCE POUR PATES CHOIX VARIES CLASSICO
- **Brand:** None
- **Category (English):** Pantry > Pasta & Pasta Sauce
- **Category (French):** Produits du garde-manger > Pâtes et sauces
- **How classified:** rule (`pasta-sauce`)
- **Size:** 410ML
- **Price:** 10.98
- **Printed Price:** “10.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 658, top 285, right 769, bottom 392, page 4
- **Full page:** [pages/flyer137-page4-df8fc771ae.jpg (flyer page 4)](pages/flyer137-page4-df8fc771ae.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-newon-jean-talon-du-16-au-22-octobre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `ec5b85e09313b106`
- **Raw:** `{"block_text": "CLASSICO. SAUCE\nPOUR PATES CHOIX\nVARIES CLASSICO", "ocr_lines": ["CLASSICO.SAUCE", "POURPATES CHOIX", "VARIESCIASSICO"], "harvest": {"size": "410ML", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 4. Classico pasta sauce (410-650 ml) prints 3.98; the DB had 10.98 — the Dettol antiseptic's price from the cell above. Pasta & Pasta Sauce is right.

### Item 13807

![item 13807](images/item-13807.jpg)

- **Name (English):** None
- **Name (French):** JIADEWEIDAO VERIAICELLE RIZ
- **Brand:** None
- **Category (English):** Pantry > Rice
- **Category (French):** Produits du garde-manger > Riz
- **How classified:** rule (`rice`)
- **Size:** 1KG
- **Price:** 2.98
- **Printed Price:** “2.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 191, top 102, right 265, bottom 179, page 4
- **Full page:** [pages/flyer137-page4-df8fc771ae.jpg (flyer page 4)](pages/flyer137-page4-df8fc771ae.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-newon-jean-talon-du-16-au-22-octobre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `dcb375982cc76da8`
- **Raw:** `{"block_text": "JIADEWEIDAO\nVERIAICELLE RIZ", "ocr_lines": ["JIADEWEIDAO", "VERMICELLERIZ"], "harvest": {"size": "1KG", "unit": "each", "via": "crop"}}`

## Flyer 138 — valid 2026-10-16 → 2026-10-22 (3 classified items, 0 unclassified)

Source ref: `circulaire-marche-newon-ste-catherine-du-16-au-22-octobre-2026` · fetched 2026-10-16T12:37:03.444Z

**Item Review Analysis (Pass 1):** Correct. Jia De Wei Dao rice vermicelli (1 kg) at 2.98 — verified. Rice is the vermicelli shelf.

### Item 13811

![item 13811](images/item-13811.jpg)

- **Name (English):** None
- **Name (French):** AC CANARD ROTI STYLE PEKINOISE
- **Brand:** None
- **Category (English):** Meat > Game Meat, Offals & Fowl
- **Category (French):** Viande > Viande exotique
- **How classified:** rule (`game-offal`)
- **Size:** None
- **Price:** 7.00
- **Printed Price:** “7”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 722, top 474, right 960, bottom 535, page 1
- **Full page:** [pages/flyer138-page1-674e04d23b.jpg (flyer page 1)](pages/flyer138-page1-674e04d23b.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-newon-ste-catherine-du-16-au-22-octobre-2026/01.webp
- **Details:** confidence: 0.92 · item_key: `2c5070f94d7a7931`
- **Conditions:** `{"alt_prices": ["12", "88"]}`
- **Raw:** `{"block_text": "AC CANARD ROTI STYLE PEKINOISE", "ocr_lines": ["ACCANARDROTISTYLEPEKINOISE"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 1. AC cooked Peking-style roasted duck (500 g) prints 11.88; the DB had 7.00. Game Meat, Offals & Fowl is the taxonomy's duck shelf.

### Item 13812

![item 13812](images/item-13812.jpg)

- **Name (English):** None
- **Name (French):** GRANDE PAPAYE
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 0.98
- **Printed Price:** “0.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 30, top 315, right 142, bottom 381, page 2
- **Full page:** [pages/flyer138-page2-5932da89d5.jpg (flyer page 2)](pages/flyer138-page2-5932da89d5.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-newon-ste-catherine-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `7ef74509b24f1d9c`
- **Raw:** `{"block_text": "GRANDE PAPAYE", "ocr_lines": ["GRANDEPAPAYE"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Large papaya at 0.98 each — verified. Fresh Fruits is right.

### Item 13814

![item 13814](images/item-13814.jpg)

- **Name (English):** None
- **Name (French):** OIGNONS JAUNES
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 98.00
- **Printed Price:** “98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 30, top 165, right 171, bottom 231, page 2
- **Full page:** [pages/flyer138-page2-5932da89d5.jpg (flyer page 2)](pages/flyer138-page2-5932da89d5.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-newon-ste-catherine-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `66db3d814279fac3`
- **Raw:** `{"block_text": "OIGNONS JAUNES", "ocr_lines": ["OIGNONSJAUNES"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 2. Yellow onions (2 lb bag) print 0.98 each; the DB had 98.00 (the lettuce's 1.98/lb badge above, misread). Fresh Vegetables is right.
