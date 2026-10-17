# Provigo — full product report

Store slug: `provigo`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 148, valid 2026-10-15 → 2026-10-21, 160 items). The expired Oct 8–14 edition is correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown — classification success on this Flipp feed.
- **Issues found:** none. Every sampled cutout matches its name (the St-Hubert item offers breaded chicken or mozzarella sticks; the render shows the sticks variant), and where a render prints a price it matches the payload (Krema 6.50, Hershey's 8$, Activia 8.50). The round prices elsewhere are this flyer's whole-dollar price points.
- **Fixes applied this pass:** none needed.

## Flyer 148 — valid 2026-10-15 → 2026-10-21 (10 classified items, 0 unclassified)

Source ref: `8183853` · fetched 2026-10-16T12:49:16.617Z

### Item 14574

![item 14574](images/item-14574.jpg)

- **Name (English):** CEDAR VALLEY PITA CHIPS, 180 G
- **Name (French):** CROUSTILLES DE PITA CEDAR VALLEY
- **Brand:** Cedar Valley
- **Category (English):** Snacks, Chips & Candy > Chips & Snacks
- **Category (French):** Grignotines, croustilles et friandises > Croustilles et grignotines
- **How classified:** rule (`specific-snacks`)
- **Size:** 180 G
- **Price:** 3.00
- **Printed Price:** “3.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24279172/8d57aace-c3f9-11f1-ab8f-aa5820cd2cd7/x_large
- **Details:** SKU: 21524190_EA · confidence: 1.00 · item_key: `40c13393339fb84c`
- **Conditions:** `{"disclaimer_text": "LIMITE DE 6 APRÈS LIMITÉ 45 CH.", "description": "CERTAINES VARIÉTÉS"}`
- **Raw:** `{"id": 1046915293, "name": "CROUSTILLES DE PITA CEDAR VALLEY | CEDAR VALLEY PITA CHIPS, 180 G", "sale_story": null, "sku": "21524190_EA", "description": "CERTAINES VARIÉTÉS", "disclaimer_text": "LIMITE DE 6 APRÈS LIMITÉ 45 CH.", "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24279172/8d57aace-c3f9-11f1-ab8f-aa5820cd2cd7/x_large", "custom_id_field_1": "21524190_EA", "custom_id_field_2": "2`

**Item Review Analysis (Pass 1):** Correct. Cedar Valley pita chips (garlic & herb, 180 g) at 3.00 — cutout matches. Chips & Snacks is right.

### Item 14578

![item 14578](images/item-14578.jpg)

- **Name (English):** MINI-PETITS GÂTEAUX DÉLICES DU MARCHÉ, 12 UN.
- **Name (French):** MINI-PETITS GÂTEAUX DÉLICES DU MARCHÉ, 12 UN.
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Snack Cakes
- **Category (French):** Grignotines, croustilles et friandises > Petits gâteaux à grignoter
- **How classified:** rule (`snack-cakes`)
- **Size:** 12 UN
- **Price:** 5.50
- **Printed Price:** “5.50”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24279164/9ce21cfe-c3f9-11f1-94ba-828ca7d3e80b/x_large
- **Details:** SKU: 21634742_EA · confidence: 1.00 · item_key: `50cf0364a037885a`
- **Conditions:** `{"description": "CERTAINES VARIÉTÉS"}`
- **Raw:** `{"id": 1046915150, "name": "MINI-PETITS GÂTEAUX DÉLICES DU MARCHÉ, 12 UN.", "sale_story": null, "sku": "21634742_EA", "description": "CERTAINES VARIÉTÉS", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24279164/9ce21cfe-c3f9-11f1-94ba-828ca7d3e80b/x_large", "custom_id_field_1": "21634742_EA", "custom_id_field_2": "21643619_EA", "custom_id_field_3": null, "custom_i`

**Item Review Analysis (Pass 1):** Correct. Délices du Marché mini cupcakes (chocolate, 12) at 5.50 — cutout matches. Snack Cakes is right.

### Item 14589

![item 14589](images/item-14589.jpg)

- **Name (English):** ST HUBERT BREADED CHICKEN OR MOZZARELLA CHEESE STICKS
- **Name (French):** POULET PANÉ 600 G OU BÂTONNETS DE FROMAGE MOZZARRELLA 510 G ST-HUBERT
- **Brand:** ST-HUBERT
- **Category (English):** Meat > Chicken & Turkey
- **Category (French):** Viande > Poulet et dinde
- **How classified:** rule (`chicken-turkey`)
- **Size:** 510 G
- **Price:** 9.00
- **Printed Price:** “9.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24279164/8ee69634-c3f9-11f1-94ba-828ca7d3e80b/x_large
- **Details:** SKU: 20719691_EA · confidence: 1.00 · item_key: `0f1f3f4193669066`
- **Conditions:** `{"description": "SURGELÉES"}`
- **Raw:** `{"id": 1046915138, "name": "POULET PANÉ 600 G OU BÂTONNETS DE FROMAGE MOZZARRELLA 510 G ST-HUBERT | ST HUBERT BREADED CHICKEN OR MOZZARELLA CHEESE STICKS", "sale_story": null, "sku": "20719691_EA", "description": "SURGELÉES", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24279164/8ee69634-c3f9-11f1-94ba-828ca7d3e80b/x_large", "custom_id_field_1": "20719691_EA", "`

**Item Review Analysis (Pass 1):** Correct. The item offers breaded chicken (600 g) or mozzarella cheese sticks; the render shows the St-Hubert sticks (510 g). At 9.00. Chicken & Turkey leads the combined name.

### Item 14654

![item 14654](images/item-14654.jpg)

- **Name (English):** CREAMY YOGURT, 2 KG
- **Name (French):** IÖGO YOGOURT CRÉMEUX
- **Brand:** Iögo
- **Category (English):** Dairy & Eggs > Yogurt
- **Category (French):** Produits laitiers et œufs > Yogourt
- **How classified:** rule (`yogurt`)
- **Size:** 2 KG
- **Price:** 10.00
- **Printed Price:** “10.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24279169/97ffd802-c3f9-11f1-b1f9-2a0b48ea34e6/x_large
- **Details:** SKU: 21761131_EA · confidence: 1.00 · item_key: `d3648d1b414024a8`
- **Conditions:** `{"description": "certaines variétés"}`
- **Raw:** `{"id": 1046915355, "name": "IÖGO YOGOURT CRÉMEUX | CREAMY YOGURT, 2 KG", "sale_story": null, "sku": "21761131_EA", "description": "certaines variétés", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24279169/97ffd802-c3f9-11f1-b1f9-2a0b48ea34e6/x_large", "custom_id_field_1": "21761131_EA", "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": `

**Item Review Analysis (Pass 1):** Correct. iögo creamy yogurt (vanilla, 2 kg pouch) at 10.00 — cutout matches. Yogurt is right.

### Item 14665

![item 14665](images/item-14665.jpg)

- **Name (English):** VAN HOUTTE GROUND COFFEE, 640-908 G
- **Name (French):** CAFÉ MOULU VAN HOUTTE
- **Brand:** Van Houtte
- **Category (English):** Drinks > Coffee
- **Category (French):** Boissons > Cafés
- **How classified:** rule (`coffee`)
- **Size:** 640-908 G
- **Price:** 24.00
- **Printed Price:** “24.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24279165/98e98894-c3f9-11f1-8855-ca01485b66ab/x_large
- **Details:** SKU: 21702600_EA · confidence: 1.00 · item_key: `575d6eebb864d8d5`
- **Conditions:** `{"sale_story": "Obtenez PC OPTIMUM 3 000 pts, 3$ remise en points", "description": "CERTAINES VARIÉTÉS"}`
- **Raw:** `{"id": 1046915184, "name": "CAFÉ MOULU VAN HOUTTE | VAN HOUTTE GROUND COFFEE, 640-908 G", "sale_story": "Obtenez PC OPTIMUM 3 000 pts, 3$ remise en points", "sku": "21702600_EA", "description": "CERTAINES VARIÉTÉS", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24279165/98e98894-c3f9-11f1-8855-ca01485b66ab/x_large", "custom_id_field_1": "21702600_EA", "custom_id_`

**Item Review Analysis (Pass 1):** Correct. Van Houtte ground coffee (French Roast, 908 g) at 24.00 — cutout matches. Coffee is right.

### Item 14667

![item 14667](images/item-14667.jpg)

- **Name (English):** NONAME NATURALLY IMPERFECT MIXED PEPPERS
- **Name (French):** POIVRONS NATURELLEMENT IMPARFAITS SANS NOM®
- **Brand:** sans nom®
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 3.00
- **Printed Price:** “3.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24279164/9c21cd64-c3f9-11f1-94ba-828ca7d3e80b/x_large
- **Details:** SKU: 20921434001_EA · confidence: 1.00 · item_key: `7178a52d5d5cdf6d`
- **Conditions:** `{"description": "PRODUIT DU CANADA\nSAC DE 2.5 LB"}`
- **Raw:** `{"id": 1046915141, "name": "POIVRONS NATURELLEMENT IMPARFAITS SANS NOM® | NONAME NATURALLY IMPERFECT MIXED PEPPERS", "sale_story": null, "sku": "20921434001_EA", "description": "PRODUIT DU CANADA\nSAC DE 2.5 LB", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24279164/9c21cd64-c3f9-11f1-94ba-828ca7d3e80b/x_large", "custom_id_field_1": "20921434001_EA", "custom_id_`

**Item Review Analysis (Pass 1):** Correct. No Name Naturally Imperfect sweet peppers (1.5 kg bag) at 3.00 — cutout matches. Fresh Vegetables is right.

### Item 14695

![item 14695](images/item-14695.jpg)

- **Name (English):** BEN & JERRY'S OR TALENTI GELATO OR SORBETTO OR MAGNUM BARS, 3/4 UN.
- **Name (French):** BEN & JERRY'S OR GELATO OR SORBETTO TALENTI 473 ML OR BARRES MAGNUM
- **Brand:** Talenti
- **Category (English):** Frozen Food > Ice Cream & Frozen Desserts
- **Category (French):** Produits surgelés > Crèmes glacées et desserts glacés
- **How classified:** rule (`ice-cream`)
- **Size:** 473 ML
- **Price:** 5.00
- **Printed Price:** “5.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24279165/95836382-c3f9-11f1-8855-ca01485b66ab/x_large
- **Details:** SKU: 21428403_EA · confidence: 1.00 · item_key: `20ae23e9a0c58a96`
- **Conditions:** `{"description": "CERTAINES VARIÉTÉS SURGELÉES"}`
- **Raw:** `{"id": 1046915158, "name": "BEN & JERRY'S OR GELATO OR SORBETTO TALENTI 473 ML OR BARRES MAGNUM | BEN & JERRY'S OR TALENTI GELATO OR SORBETTO OR MAGNUM BARS, 3/4 UN.", "sale_story": null, "sku": "21428403_EA", "description": "CERTAINES VARIÉTÉS SURGELÉES", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24279165/95836382-c3f9-11f1-8855-ca01485b66ab/x_large", "custo`

**Item Review Analysis (Pass 1):** Correct. Ben & Jerry's (Half Baked shown) or Talenti gelato/sorbetto (473 ml) at 5.00 — cutout matches. Ice Cream & Frozen Desserts is right.

### Item 14702

![item 14702](images/item-14702.jpg)

- **Name (English):** KREMA YOGURT
- **Name (French):** OLYMPIC YOGOURT KREMA, 650 G
- **Brand:** Olympic
- **Category (English):** Dairy & Eggs > Yogurt
- **Category (French):** Produits laitiers et œufs > Yogourt
- **How classified:** rule (`yogurt`)
- **Size:** 650 G
- **Price:** 6.50
- **Printed Price:** “6.50”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_items/437063879/1791590988/extra_large.jpg
- **Details:** SKU: 20588372001_EA · confidence: 1.00 · item_key: `5cb35c7fa8d97d14`
- **Conditions:** `{"description": "Certaines variétés"}`
- **Raw:** `{"id": 1046915358, "name": "OLYMPIC YOGOURT KREMA, 650 G | KREMA YOGURT", "sale_story": null, "sku": "20588372001_EA", "description": "Certaines variétés", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_items/437063879/1791590988/extra_large.jpg", "custom_id_field_1": "20588372001_EA", "custom_id_field_2": "21693264_EA", "custom_id_field_3": null, "custom_id_field_4": null, `

**Item Review Analysis (Pass 1):** Correct. Olympic Krema yogurt (650 g) at 6.50 — the price is printed in the render and matches. Yogurt is right.

### Item 14705

![item 14705](images/item-14705.jpg)

- **Name (English):** HERSHEY'S CHOCOLATS VARIÉS OU FRIANDISES SANS ARACHIDES 100 UN. OU AMOUREUX REESE'S 90 UN., 909 G-1,02 KG
- **Name (French):** HERSHEY'S CHOCOLATS VARIÉS OU FRIANDISES SANS ARACHIDES 100 UN. OU AMOUREUX REESE'S 90 UN., 909 G-1,02 KG
- **Brand:** Hershey's
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 1,02 KG
- **Price:** 8.00
- **Printed Price:** “8.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_items/437063914/1791590982/extra_large.jpg
- **Details:** SKU: 21599604_EA · confidence: 1.00 · item_key: `05279688f179ad8b`
- **Conditions:** `{"disclaimer_text": "TAXES APPLICABLES", "description": "certaines variétés"}`
- **Raw:** `{"id": 1046915373, "name": "HERSHEY'S CHOCOLATS VARIÉS OU FRIANDISES SANS ARACHIDES 100 UN. OU AMOUREUX REESE'S 90 UN., 909 G-1,02 KG", "sale_story": null, "sku": "21599604_EA", "description": "certaines variétés", "disclaimer_text": "TAXES APPLICABLES", "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_items/437063914/1791590982/extra_large.jpg", "custom_id_field_1": "21599604_EA", "custom_id_field_2"`

**Item Review Analysis (Pass 1):** Correct. Hershey's assorted chocolates (Reese's snack format shown, 25 count) at 8.00 — printed in the render. Candy & Chocolate is right.

### Item 14720

![item 14720](images/item-14720.jpg)

- **Name (English):** ACTIVIA, 12 x 100 g
- **Name (French):** ACTIVIA, 12 x 100 g
- **Brand:** Activia
- **Category (English):** Dairy & Eggs > Yogurt
- **Category (French):** Produits laitiers et œufs > Yogourt
- **How classified:** rule (`yogurt`)
- **Size:** 12 x 100 g
- **Price:** 8.50
- **Printed Price:** “8.50”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_items/437074235/1791590991/extra_large.jpg
- **Details:** SKU: 20303412001_EA · confidence: 1.00 · item_key: `5373dd9fc2a07fa6`
- **Conditions:** `{"description": "certaines variétés"}`
- **Raw:** `{"id": 1046915428, "name": "ACTIVIA, 12 x 100 g", "sale_story": null, "sku": "20303412001_EA", "description": "certaines variétés", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_items/437074235/1791590991/extra_large.jpg", "custom_id_field_1": "20303412001_EA", "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "custom_id_field_5": null, "custo`

**Item Review Analysis (Pass 1):** Correct. Activia yogurt (12 x 100 g) at 8.50 — printed in the render and matches. Yogurt is right.
