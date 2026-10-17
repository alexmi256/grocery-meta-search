# Maxi — full product report

Store slug: `maxi`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 141, valid 2026-10-15 → 2026-10-21, 254 items). The expired Oct 8–14 edition is correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown — classification success on this Flipp feed.
- **Issues found:** none. Every sampled cutout matches its name, and the prices are the payload's. One sampled item (Québon milk, 4 L) has no price — the documented Flipp payload gap (this store has ~42 such items DB-wide); the price is honestly absent rather than invented.
- **Fixes applied this pass:** none needed.

## Flyer 141 — valid 2026-10-15 → 2026-10-21 (10 classified items, 0 unclassified)

Source ref: `8181341` · fetched 2026-10-16T12:43:16.078Z

### Item 13982

![item 13982](images/item-13982.jpg)

- **Name (English):** KEFIR, 1 L
- **Name (French):** KÉFIR PC BIOLOGIQUE
- **Brand:** PC
- **Category (English):** Dairy & Eggs > Yogurt
- **Category (French):** Produits laitiers et œufs > Yogourt
- **How classified:** rule (`yogurt`)
- **Size:** 1 L
- **Price:** 5.50
- **Printed Price:** “5.50”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24270220/8ca196ba-c293-11f1-9c86-5211c5948fcb/x_large
- **Details:** SKU: 20944278_EA · confidence: 1.00 · item_key: `be535280eac38dc2`
- **Conditions:** `{"description": "certaines variétés\n\nselected varieties"}`
- **Raw:** `{"id": 1046421261, "name": "KÉFIR PC BIOLOGIQUE | KEFIR, 1 L", "sale_story": null, "sku": "20944278_EA", "description": "certaines variétés\n\nselected varieties", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24270220/8ca196ba-c293-11f1-9c86-5211c5948fcb/x_large", "custom_id_field_1": "20944278_EA", "custom_id_field_2": null, "custom_id_field_3": null, "custom_i`

**Item Review Analysis (Pass 1):** Correct. PC organic kefir (plain, 1 L) at 5.50 — cutout matches. Yogurt is the kefir shelf.

### Item 13987

![item 13987](images/item-13987.jpg)

- **Name (English):** CANDY, 1,5 KG
- **Name (French):** FRIANDISES MEGA MONDOUX
- **Brand:** MONDOUX
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 1,5 KG
- **Price:** 13.99
- **Printed Price:** “13.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24270220/997c9b6e-c293-11f1-9c86-5211c5948fcb/x_large
- **Details:** SKU: 21451401_EA · confidence: 1.00 · item_key: `d976afec53913cbd`
- **Raw:** `{"id": 1046421362, "name": "FRIANDISES MEGA MONDOUX | CANDY, 1,5 KG", "sale_story": null, "sku": "21451401_EA", "description": null, "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24270220/997c9b6e-c293-11f1-9c86-5211c5948fcb/x_large", "custom_id_field_1": "21451401_EA", "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4": null, "custom_id_fi`

**Item Review Analysis (Pass 1):** Correct. Mondoux Mega candy bag (1.5 kg, ~200 pieces) at 13.99 — cutout matches. Candy & Chocolate is right.

### Item 13989

![item 13989](images/item-13989.jpg)

- **Name (English):** WIENERS, 450 G
- **Name (French):** SAUCISSES FUMÉES LAFLEUR
- **Brand:** Lafleur
- **Category (English):** Meat > Hot Dogs
- **Category (French):** Viande > Saucisses hot-dog
- **How classified:** rule (`hot-dogs`)
- **Size:** 450 G
- **Price:** 3.50
- **Printed Price:** “3.50”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24270217/843cdd68-c293-11f1-a174-326aa727ed51/x_large
- **Details:** SKU: 20131096_EA · confidence: 1.00 · item_key: `34f844ee145c9cad`
- **Conditions:** `{"sale_story": "Préparé au Québec", "description": "certaines variétés\n\nselective varieties"}`
- **Raw:** `{"id": 1046419653, "name": "SAUCISSES FUMÉES LAFLEUR | WIENERS, 450 G", "sale_story": "Préparé au Québec", "sku": "20131096_EA", "description": "certaines variétés\n\nselective varieties", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24270217/843cdd68-c293-11f1-a174-326aa727ed51/x_large", "custom_id_field_1": "20131096_EA", "custom_id_field_2": null, "custom_id_`

**Item Review Analysis (Pass 1):** Correct. Lafleur smoked wieners (Original, 450 g, 12) at 3.50 — cutout matches. Hot Dogs is right.

### Item 14006

![item 14006](images/item-14006.jpg)

- **Name (English):** BOISSONS DÉSALTÉRANTES GATORADE, 710 ML
- **Name (French):** BOISSONS DÉSALTÉRANTES GATORADE, 710 ML
- **Brand:** Gatorade
- **Category (English):** Drinks > Sports & Energy
- **Category (French):** Boissons > Boissons énergisantes et pour sportifs
- **How classified:** rule (`sports-energy`)
- **Size:** 710 ML
- **Price:** 1.50
- **Printed Price:** “1.50”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_items/436793607/1791415208/extra_large.jpg
- **Details:** SKU: 20305775001_EA · confidence: 1.00 · item_key: `412dc45f715779ef`
- **Conditions:** `{"disclaimer_text": "Consigne", "description": "Certaines Variétés"}`
- **Raw:** `{"id": 1046422914, "name": "BOISSONS DÉSALTÉRANTES GATORADE, 710 ML", "sale_story": null, "sku": "20305775001_EA", "description": "Certaines Variétés", "disclaimer_text": "Consigne", "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_items/436793607/1791415208/extra_large.jpg", "custom_id_field_1": "20305775001_EA", "custom_id_field_2": "21357035_EA", "custom_id_field_3": null, "custom_id_field_4": null`

**Item Review Analysis (Pass 1):** Correct. Gatorade thirst-quencher drinks (710 ml) at 1.50 +tx — the price is printed in this item's render and matches. Sports & Energy is right.

### Item 14087

![item 14087](images/item-14087.jpg)

- **Name (English):** AUBERGINE,OU OU ÉPINARD EN BOTTE, 2$ CH.
- **Name (French):** AUBERGINE,OU OU ÉPINARD EN BOTTE, 2$ CH.
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 2.00
- **Printed Price:** “2.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24270216/9201b13a-c293-11f1-890b-92421b08d44b/x_large
- **Details:** SKU: 20155709001_KG · confidence: 1.00 · item_key: `433961bca84682f2`
- **Conditions:** `{"description": "*2$/LB-2,20$/KG produit des É.-U, produit du Mexique ou des É.-U."}`
- **Raw:** `{"id": 1046419489, "name": "AUBERGINE,OU OU ÉPINARD EN BOTTE, 2$ CH.", "sale_story": null, "sku": "20155709001_KG", "description": "*2$/LB-2,20$/KG produit des É.-U, produit du Mexique ou des É.-U.", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24270216/9201b13a-c293-11f1-890b-92421b08d44b/x_large", "custom_id_field_1": "20155709001_KG", "custom_id_field_2": "20`

**Item Review Analysis (Pass 1):** Correct. Eggplant (or bunched spinach) at 2.00 each — the price is in the name itself ("2$ CH."); cutout matches the eggplant. Fresh Vegetables is right.

### Item 14114

![item 14114](images/item-14114.jpg)

- **Name (English):** AILES DE POULET SANS NOM®, 908 G
- **Name (French):** AILES DE POULET SANS NOM®, 908 G
- **Brand:** sans nom®
- **Category (English):** Meat > Chicken & Turkey
- **Category (French):** Viande > Poulet et dinde
- **How classified:** rule (`chicken-turkey`)
- **Size:** 908 G
- **Price:** 12.99
- **Printed Price:** “12.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24270217/84f0ba54-c293-11f1-a174-326aa727ed51/x_large
- **Details:** SKU: 21045668_EA · confidence: 1.00 · item_key: `1f28499673a692ac`
- **Conditions:** `{"description": "certaines variétés, surgelées"}`
- **Raw:** `{"id": 1046419731, "name": "AILES DE POULET SANS NOM®, 908 G", "sale_story": null, "sku": "21045668_EA", "description": "certaines variétés, surgelées", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24270217/84f0ba54-c293-11f1-a174-326aa727ed51/x_large", "custom_id_field_1": "21045668_EA", "custom_id_field_2": null, "custom_id_field_3": null, "custom_id_field_4":`

**Item Review Analysis (Pass 1):** Correct. No Name buffalo chicken wings (908 g) at 12.99 — cutout matches. Chicken & Turkey is right.

### Item 14156

![item 14156](images/item-14156.jpg)

- **Name (English):** CAFÉ MOULU CREMA E GUSTO, QUALITÀ ORO OU QUALITÀ ROSSA LAVAZZA, 250 G
- **Name (French):** CAFÉ MOULU CREMA E GUSTO, QUALITÀ ORO OU QUALITÀ ROSSA LAVAZZA, 250 G
- **Brand:** LavAzza
- **Category (English):** Drinks > Coffee
- **Category (French):** Boissons > Cafés
- **How classified:** rule (`coffee`)
- **Size:** 250 G
- **Price:** 6.00
- **Printed Price:** “6.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24270220/8b940690-c293-11f1-9c86-5211c5948fcb/x_large
- **Details:** SKU: 21553695_EA · confidence: 1.00 · item_key: `c224e76c5a1fc3e7`
- **Conditions:** `{"description": "Certaines variétés"}`
- **Raw:** `{"id": 1046421375, "name": "CAFÉ MOULU CREMA E GUSTO, QUALITÀ ORO OU QUALITÀ ROSSA LAVAZZA, 250 G", "sale_story": null, "sku": "21553695_EA", "description": "Certaines variétés", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24270220/8b940690-c293-11f1-9c86-5211c5948fcb/x_large", "custom_id_field_1": "21553695_EA", "custom_id_field_2": null, "custom_id_field_3": `

**Item Review Analysis (Pass 1):** Correct. Lavazza ground coffee (Crema e Gusto / Qualità Oro / Rossa, 250 g) at 6.00 — cutout matches. Coffee is right.

### Item 14171

![item 14171](images/item-14171.jpg)

- **Name (English):** DARNE DE THON JAUNE SAUVAGE, 92 G OU SAUMON STEELHEAD, FUMÉ 50 G
- **Name (French):** DARNE DE THON JAUNE SAUVAGE, 92 G OU SAUMON STEELHEAD, FUMÉ 50 G
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** 50 G
- **Price:** 2.00
- **Printed Price:** “2.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-30
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24270215/87fe97e8-c293-11f1-a260-f22ab89aad65/x_large
- **Details:** SKU: 21694839_EA · confidence: 1.00 · item_key: `68f78cccb154bf46`
- **Conditions:** `{"disclaimer_text": "Limite de 6 ou 3$ après limite", "description": "certaines variétés, surgelés"}`
- **Raw:** `{"id": 1046419245, "name": "DARNE DE THON JAUNE SAUVAGE, 92 G OU SAUMON STEELHEAD, FUMÉ 50 G", "sale_story": null, "sku": "21694839_EA", "description": "certaines variétés, surgelés", "disclaimer_text": "Limite de 6 ou 3$ après limite", "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24270215/87fe97e8-c293-11f1-a260-f22ab89aad65/x_large", "custom_id_field_1": "21694839_EA", "custom_id_fiel`

**Item Review Analysis (Pass 1):** Correct. The item offers a choice (wild yellowfin tuna steak 92 g or steelhead salmon); the cutout shows the smoked steelhead salmon variant. At 2.00. Fish is right.

### Item 14176

![item 14176](images/item-14176.jpg)

- **Name (English):** TORTILLAS, 400/540 G
- **Name (French):** TORTILLAS MEJICANO,
- **Brand:** MEJICANO
- **Category (English):** Bakery > Wraps, Flatbread & Pizza Crust
- **Category (French):** Boulangerie > Roulés, pains plats et croûtes à pizza
- **How classified:** rule (`wraps-flatbread`)
- **Size:** 400/540 G
- **Price:** 3.55
- **Printed Price:** “3.55”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24270218/9b38e142-c293-11f1-b679-2e599553d05e/x_large
- **Details:** SKU: 21484946_EA · confidence: 1.00 · item_key: `52ee9731c70edd69`
- **Conditions:** `{"description": "10 pouces, certaines variétés\n\n10 inch, selected varieties"}`
- **Raw:** `{"id": 1046420132, "name": "TORTILLAS MEJICANO, | TORTILLAS, 400/540 G", "sale_story": null, "sku": "21484946_EA", "description": "10 pouces, certaines variétés\n\n10 inch, selected varieties", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24270218/9b38e142-c293-11f1-b679-2e599553d05e/x_large", "custom_id_field_1": "21484946_EA", "custom_id_field_2": null, "custo`

**Item Review Analysis (Pass 1):** Correct. Mejicano tortillas (regular, 540 g) at 3.55 — cutout matches. Wraps, Flatbread & Pizza Crust is right.

### Item 14210

![item 14210](images/item-14210.jpg)

- **Name (English):** MILK, 4 L
- **Name (French):** LAIT QUÉBON, SEALTEST OU NUTRILAIT
- **Brand:** QUÉBON | NUTRILAIT
- **Category (English):** Dairy & Eggs > Milk & Cream
- **Category (French):** Produits laitiers et œufs > Lait et crème
- **How classified:** rule (`milk-cream`)
- **Size:** 4 L
- **Price:** None
- **Printed Price:** None
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://f.wishabi.net/page_pdf_images/24294991/19b8fdac-c7f5-11f1-9348-521b37dde379/x_large
- **Details:** SKU: 20021564_EA · confidence: 1.00 · item_key: `dad7338731806994`
- **Conditions:** `{"description": "Certaines variétés\n\nselected varieties"}`
- **Raw:** `{"id": 1047643072, "name": "LAIT QUÉBON, SEALTEST OU NUTRILAIT | MILK, 4 L", "sale_story": null, "sku": "20021564_EA", "description": "Certaines variétés\n\nselected varieties", "disclaimer_text": null, "valid_from_timestamp": "2026-10-15T00:00:00-04:00", "valid_to_timestamp": "2026-10-21T23:59:59-04:00", "image_url": "https://f.wishabi.net/page_pdf_images/24294991/19b8fdac-c7f5-11f1-9348-521b37dde379/x_large", "custom_id_field_1": "20021564_EA", "custom_id_field_2": "20894811_EA", "custom_id_fi`

**Item Review Analysis (Pass 1):** Price absent — documented source gap. Québon (or Sealtest/Nutrilait) milk, 4 L bag; the Flipp payload carried no price for this item (one of ~42 price-less items at this store). Shown honestly as None; not invented.
