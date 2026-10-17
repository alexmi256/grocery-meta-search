# IGA Extra — full product report

Store slug: `iga-extra`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 123, valid 2026-10-15 → 2026-10-21, 367 items). **Audit note:** IGA's edition holds 356 items and IGA Express's is identical to IGA's; Extra's 367 is the same circular plus a handful of Extra-only items — the three IGA banners share one Flipp-sourced circular with small per-banner deltas. Recorded as the chain's distribution, not a pipeline error.
- **Sample counts:** 10 classified + 0 unclassified shown — classification success on the structured feed.
- **Issues found:** none requiring a fix. Every sampled item's shot matches its offer; prices are payload values (the organic strawberries' 3.97 is verified on its region render: 454 g, reg. 8.99). Two source characters worth recording: group offers carry stitched multi-variant names (13063's cheese name strings Chaussée aux Moines / Petit Saint-Paulin while the pictured variant is Président Saint Morgon — the payload's own composition), and the fresh drinking coconut sits in Dried Fruits & Nuts, the classifier's standing treatment of "noix de coco" (borderline for a fresh coconut, left as-is).
- **Fixes applied this pass:** none needed.


## Review Analysis — Pass 2 (2026-10-17, verification after Pass 1)

- No fixes were needed in Pass 1; the packet is unchanged and the verdicts stand (Pass 1 preserved in `iga-extra-report-pass1.md`). Store review complete — clean.

## Flyer 123 — valid 2026-10-15 → 2026-10-21 (10 classified items, 0 unclassified)

Source ref: `8180975` · fetched 2026-10-16T12:18:25.383Z

### Item 12705

![item 12705](images/item-12705.jpg)

- **Name (English):** CÉRÉALES POST
- **Name (French):** CONFITURE, TARTINADE, GELÉE OU MARMELADE DORA
- **Brand:** DORA
- **Category (English):** Pantry > Honey, Syrups & Spreads
- **Category (French):** Produits du garde-manger > Miel, sirops et tartinades
- **How classified:** rule (`honey-spreads`)
- **Size:** 500mL
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268543/5c3b8996-c274-11f1-b3b8-26c84f172ddc/x_large
- **Details:** SKU: 00000_000000006481932717 · confidence: 1.00 · item_key: `8e9dbc94fb709a22`
- **Conditions:** `{"description": "(500 mL)\nRég. 4,79$ à 6,79$"}`
- **Raw:** `{"id": 1046445292, "name": "CONFITURE, TARTINADE, GELÉE OU MARMELADE DORA", "sale_story": null, "sku": "00000_000000006481932717", "description": "(500 mL)\nRég. 4,79$ à 6,79$", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268543/5c3b8996-c274-11f1-b3b8-26c84f172ddc/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "cus`

**Item Review Analysis (Pass 1):** Correct. A group jam/spread offer (Dora pictured, 500 ml) at 3.99 from the payload. Honey, Syrups & Spreads is right.

### Item 12724

![item 12724](images/item-12724.jpg)

- **Name (English):** BROCHETTES DE SURLONGE DE PORC À LA GRECQUE OLYMEL
- **Name (French):** BROCHETTES DE SURLONGE DE PORC À LA GRECQUE OLYMEL
- **Brand:** Olymel
- **Category (English):** Meat > Kebabs & Marinated Meat
- **Category (French):** Viande > Brochettes et viande marinée
- **How classified:** rule (`kebabs-marinated`)
- **Size:** 23g
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268533/6b19322e-c274-11f1-bbb6-d235ee54bd5b/x_large
- **Details:** SKU: 00000_000000028120800000 · loyalty-gated price · confidence: 1.00 · item_key: `794749b7e4739652`
- **Conditions:** `{"disclaimer_text": "Avec carte Scène+ 7,99$", "description": "280 g", "loyalty_program": "Scène+"}`
- **Raw:** `{"id": 1046446963, "name": "BROCHETTES DE SURLONGE DE PORC À LA GRECQUE OLYMEL", "sale_story": null, "sku": "00000_000000028120800000", "description": "280 g", "disclaimer_text": "Avec carte Scène+ 7,99$", "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268533/6b19322e-c274-11f1-bbb6-d235ee54bd5b/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "`

**Item Review Analysis (Pass 1):** Correct. Olymel Greek-style pork sirloin skewers at 6.99 — shot matches. Kebabs & Marinated Meat is right.

### Item 12771

![item 12771](images/item-12771.jpg)

- **Name (English):** BIÈRE HEINEKEN
- **Name (French):** BIÈRE HEINEKEN
- **Brand:** Heineken
- **Category (English):** Beer & Wine > Beer
- **Category (French):** Bières et vins > Bières
- **How classified:** rule (`beer`)
- **Size:** None
- **Price:** 23.99
- **Printed Price:** “23.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268545/742cdfbe-c274-11f1-9ee5-9acc78cb8fd5/x_large
- **Details:** SKU: 00000_000000007289000117 · confidence: 1.00 · item_key: `fddd178d38f692aa`
- **Conditions:** `{"disclaimer_text": "Canettes ou bouteilles consignées", "description": "12 x 330 mL\nRég. 27,99$ à 29,49$"}`
- **Raw:** `{"id": 1046446480, "name": "BIÈRE HEINEKEN", "sale_story": null, "sku": "00000_000000007289000117", "description": "12 x 330 mL\nRég. 27,99$ à 29,49$", "disclaimer_text": "Canettes ou bouteilles consignées", "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268545/742cdfbe-c274-11f1-9ee5-9acc78cb8fd5/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null,`

**Item Review Analysis (Pass 1):** Correct as sourced. Heineken beer at the payload's 23.99 (case format per the source). Beer is right.

### Item 12816

![item 12816](images/item-12816.jpg)

- **Name (English):** CROUSTILLES MISS VICKIE'S
- **Name (French):** CROUSTILLES MISS VICKIE'S
- **Brand:** Miss Vickies
- **Category (English):** Snacks, Chips & Candy > Chips & Snacks
- **Category (French):** Grignotines, croustilles et friandises > Croustilles et grignotines
- **How classified:** rule (`specific-snacks`)
- **Size:** 200g
- **Price:** 8.00
- **Printed Price:** “8.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268545/76660fee-c274-11f1-9ee5-9acc78cb8fd5/x_large
- **Details:** SKU: 00000_000000006041004667 · confidence: 1.00 · item_key: `151a9ae073c8e37d`
- **Conditions:** `{"description": "190 ou 200 g"}`
- **Raw:** `{"id": 1046446204, "name": "CROUSTILLES MISS VICKIE'S", "sale_story": null, "sku": "00000_000000006041004667", "description": "190 ou 200 g", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268545/76660fee-c274-11f1-9ee5-9acc78cb8fd5/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "custom_id_fi`

**Item Review Analysis (Pass 1):** Correct as sourced. Miss Vickie's chips (190-200 g per the stored description) at 8.00 — the payload carries no multibuy structure, so the price stands as the source states it. Chips & Snacks is right.

### Item 12843

![item 12843](images/item-12843.jpg)

- **Name (English):** ÉPAULE DE PORC FUMÉ MONTRÉAL 457
- **Name (French):** ÉPAULE DE PORC FUMÉ MONTRÉAL 457
- **Brand:** MONTRÉAL 457
- **Category (English):** Meat > Pork & Ham
- **Category (French):** Viande > Porc et jambon
- **How classified:** rule (`pork-ham`)
- **Size:** None
- **Price:** 4.49
- **Printed Price:** “4.49”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268533/5d4fcfd6-c274-11f1-bbb6-d235ee54bd5b/x_large
- **Details:** SKU: 00000_000000022424600000 · confidence: 1.00 · item_key: `4016644da6cf551d`
- **Conditions:** `{"sale_story": "300 Scène+ PTS"}`
- **Raw:** `{"id": 1046446991, "name": "ÉPAULE DE PORC FUMÉ MONTRÉAL 457", "sale_story": "300 Scène+ PTS", "sku": "00000_000000022424600000", "description": null, "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268533/5d4fcfd6-c274-11f1-bbb6-d235ee54bd5b/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "cus`

**Item Review Analysis (Pass 1):** Correct. Montréal 457 smoked picnic shoulder ("457" is the brand mark, visible on the label) at 4.49 — Pork & Ham is right.

### Item 12936

![item 12936](images/item-12936.jpg)

- **Name (English):** NOIX DE COCO
- **Name (French):** NOIX DE COCO
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Dried Fruits & Nuts
- **Category (French):** Fruits et légumes > Fruits séchés et noix
- **How classified:** rule (`dried-fruits-nuts`)
- **Size:** None
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268532/63df342c-c274-11f1-ba1d-8ab3d1675c95/x_large
- **Details:** SKU: 00000_000000009863825467 · confidence: 1.00 · item_key: `91e1b3b52eedbc8c`
- **Conditions:** `{"description": "Produit du Vietnam"}`
- **Raw:** `{"id": 1046446752, "name": "NOIX DE COCO", "sale_story": null, "sku": "00000_000000009863825467", "description": "Produit du Vietnam", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268532/63df342c-c274-11f1-ba1d-8ab3d1675c95/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "custom_id_field_5":`

**Item Review Analysis (Pass 1):** Borderline, left. A fresh young drinking coconut (Vietnam, with straw) classified Dried Fruits & Nuts on "noix de coco" — the classifier's standing coconut treatment; a fresh-produce reading is also defensible. Price 3.99 from the payload.

### Item 12937

![item 12937](images/item-12937.jpg)

- **Name (English):** TRANCHES DE FROMAGE COMPLIMENTS
- **Name (French):** TRANCHES DE FROMAGE COMPLIMENTS
- **Brand:** Compliments
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** 230 g
- **Price:** 5.49
- **Printed Price:** “5.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268544/6a312952-c274-11f1-8248-8a02ca7e33cb/x_large
- **Details:** SKU: 00000_000000005574254182 · confidence: 1.00 · item_key: `977a2e1fccf8262b`
- **Conditions:** `{"description": "210 ou 230 g\n\nRég. 6,79$ à 7,29$"}`
- **Raw:** `{"id": 1046445632, "name": "TRANCHES DE FROMAGE COMPLIMENTS", "sale_story": null, "sku": "00000_000000005574254182", "description": "210 ou 230 g\n\nRég. 6,79$ à 7,29$", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268544/6a312952-c274-11f1-8248-8a02ca7e33cb/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_f`

**Item Review Analysis (Pass 1):** Correct as sourced. Compliments cheese slices at 5.49 from the payload. Cheese is right.

### Item 12973

![item 12973](images/item-12973.jpg)

- **Name (English):** PAINS GARNIS C'EST PRÊT!
- **Name (French):** PAINS GARNIS C'EST PRÊT!
- **Brand:** C'EST PRÊT!
- **Category (English):** Bakery > Bread
- **Category (French):** Boulangerie > Pain
- **How classified:** rule (`bread`)
- **Size:** None
- **Price:** 4.49
- **Printed Price:** “4.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268541/52ca40fa-c274-11f1-a07c-0ef9fcbcc086/x_large
- **Details:** SKU: 00000_000000028368600000 · confidence: 1.00 · item_key: `c074a2afdcf07309`
- **Conditions:** `{"sale_story": "50 Scène+ PTS", "description": "Simili-crabe épicé,\nGoberge et crevettes\nEmballage de 2"}`
- **Raw:** `{"id": 1046443772, "name": "PAINS GARNIS C'EST PRÊT!", "sale_story": "50 Scène+ PTS", "sku": "00000_000000028368600000", "description": "Simili-crabe épicé,\nGoberge et crevettes\nEmballage de 2", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268541/52ca40fa-c274-11f1-a07c-0ef9fcbcc086/x_large", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_f`

**Item Review Analysis (Pass 1):** Correct. "C'est Prêt!" stuffed breads (shrimp/seafood pictured) at 4.49 — Bakery > Bread is the taxonomy's shelf for these. Shot matches.

### Item 13014

![item 13014](images/item-13014.jpg)

- **Name (English):** FRAISES BIOLOGIQUES
- **Name (French):** FRAISES BIOLOGIQUES
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** 454g
- **Price:** 3.97
- **Printed Price:** “3.97”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_items/437123403/1791818321/extra_large.jpg
- **Details:** SKU: A0071575620011 · confidence: 1.00 · item_key: `1be2212b3d9f82b1`
- **Conditions:** `{"description": "Produits des États-Unis\n454 g"}`
- **Raw:** `{"id": 1047186358, "name": "FRAISES BIOLOGIQUES", "sale_story": null, "sku": "A0071575620011", "description": "Produits des États-Unis\n454 g", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_items/437123403/1791818321/extra_large.jpg", "custom_id_field_1": null, "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "custom_id_field_5": null, "custo`

**Item Review Analysis (Pass 1):** Correct — verified on the region render: organic strawberries (USA, 454 g) at 3.97 (reg. 8.99). Fresh Fruits is right.

### Item 13063

![item 13063](images/item-13063.jpg)

- **Name (English):** FROMAGE CHAUSSÉE AUX MO LE PETIT SAINT-PAULIN OU SAINT-MORGON DISTRIBUTION PARAL
- **Name (French):** FROMAGE CHAUSSÉE AUX MO LE PETIT SAINT-PAULIN OU SAINT-MORGON DISTRIBUTION PARAL
- **Brand:** President
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** 200g
- **Price:** 8.99
- **Printed Price:** “8.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24268542/543dad82-c274-11f1-95a7-8a3f53363a22/x_large
- **Details:** SKU: 00000_000000303891000447 · confidence: 1.00 · item_key: `fac6664370fde4a9`
- **Conditions:** `{"description": "(200 ou 230 g)\nRég. 10,99$ à 11,99$"}`
- **Raw:** `{"id": 1046444088, "name": "FROMAGE CHAUSSÉE AUX MO LE PETIT SAINT-PAULIN OU SAINT-MORGON DISTRIBUTION PARAL", "sale_story": null, "sku": "00000_000000303891000447", "description": "(200 ou 230 g)\nRég. 10,99$ à 11,99$", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24268542/543dad82-c274-11f1-95a7-8a3f53363a22/x_large", "custom_id_field_1": null, "custom_id_fiel`

**Item Review Analysis (Pass 1):** Correct as a group offer. Président cheeses at 8.99; the stored name stitches several variants (Chaussée aux Moines, Petit Saint-Paulin) while the pictured one is Saint Morgon (200 g) — the payload's own composition. Cheese is right.
