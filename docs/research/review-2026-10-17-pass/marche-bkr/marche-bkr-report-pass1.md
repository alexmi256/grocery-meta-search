# Marché BKR — full product report

Store slug: `marche-bkr`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 159, valid 2026-10-15 → 2026-10-21). The expired Oct 8–14 edition is correctly excluded. The edition holds 10 items across 5 viewer pages (the pages are mostly single-product spreads) — the sample is the whole edition.
- **Sample counts:** 10 classified + 0 unclassified — full coverage, classification success.
- **Issues found:** 1 wrong price. The Al Afia grape leaves (15190) print 5.99$; the DB stored 6.69. Corrected from the crop. Everything else verified, including the two identical 1.29 prices (molokhia and green tea — a coincidence the crops confirm) and the per-kg meat/cheese/makdous rates.
- **Fixes applied this pass:** 15190 → 5.99.

## Flyer 159 — valid 2026-10-15 → 2026-10-21 (10 classified items, 0 unclassified)

Source ref: `circ-22-2026-10-15` · fetched 2026-10-16T20:41:10.191Z

### Item 15186

![item 15186](images/item-15186.jpg)

- **Name (English):** None
- **Name (French):** HALIBNA POUDRE DE LAIT 900G
- **Brand:** None
- **Category (English):** Dairy & Eggs > Milk & Cream
- **Category (French):** Produits laitiers et œufs > Lait et crème
- **How classified:** rule (`milk-cream`)
- **Size:** 900G
- **Price:** 19.99
- **Printed Price:** “19.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 746, top 684, right 970, bottom 926, page 1
- **Full page:** [pages/flyer159-page1-1996c7a797.jpg (flyer page 1)](pages/flyer159-page1-1996c7a797.jpg)
- **Image source URL:** http://circulaires.com/b/marche-bkr/22/b1.jpg
- **Details:** confidence: 0.99 · item_key: `3eb362f4b88b8e89`
- **Raw:** `{"block_text": "HALIBNA POUDRE\nDE LAIT 900G", "ocr_lines": ["HALIBNA POUDRE", "DE LAIT900G"]}`

**Item Review Analysis (Pass 1):** Correct. Halibna milk powder (900 g) at 19.99$ — verified on the crop. Milk & Cream is the taxonomy's shelf for milk powder.

### Item 15187

![item 15187](images/item-15187.jpg)

- **Name (English):** None
- **Name (French):** BURCU PATE DE TOMATE 800G
- **Brand:** None
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`specific-canned`)
- **Size:** 800G
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 118, top 688, right 306, bottom 928, page 1
- **Full page:** [pages/flyer159-page1-1996c7a797.jpg (flyer page 1)](pages/flyer159-page1-1996c7a797.jpg)
- **Image source URL:** http://circulaires.com/b/marche-bkr/22/b1.jpg
- **Details:** confidence: 0.99 · item_key: `3c1fc5702fc22b18`
- **Raw:** `{"block_text": "BURCU PATE\nDE TOMATE 800G", "ocr_lines": ["BURCU PATE", "DE TOMATE 800G"]}`

**Item Review Analysis (Pass 1):** Correct. Burcu tomato paste (800 g) at 2.99$ — verified. Canned & Pickled is right.

### Item 15188

![item 15188](images/item-15188.jpg)

- **Name (English):** None
- **Name (French):** GREEN WORLD MOLOKHIA 400G
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** 400G
- **Price:** 1.29
- **Printed Price:** “1.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 468, top 688, right 644, bottom 925, page 1
- **Full page:** [pages/flyer159-page1-1996c7a797.jpg (flyer page 1)](pages/flyer159-page1-1996c7a797.jpg)
- **Image source URL:** http://circulaires.com/b/marche-bkr/22/b1.jpg
- **Details:** confidence: 0.99 · item_key: `406424af6737b7aa`
- **Raw:** `{"block_text": "GREEN WORLD\nMOLOKHIA 400G", "ocr_lines": ["GREENWORLD", "MOLOKHIA400G"]}`

**Item Review Analysis (Pass 1):** Correct. Green World molokhia (400 g) at 1.29$ — verified. Fresh Vegetables is right.

### Item 15189

![item 15189](images/item-15189.jpg)

- **Name (English):** None
- **Name (French):** ETOILES DE NUIT THÉ VERT 160G
- **Brand:** None
- **Category (English):** Drinks > Tea & Hot Drinks
- **Category (French):** Boissons > Thés et boissons chaudes
- **How classified:** rule (`tea-hot-drinks`)
- **Size:** 160G
- **Price:** 1.29
- **Printed Price:** “1.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 734, top 689, right 918, bottom 927, page 2
- **Full page:** [pages/flyer159-page2-c762147e24.jpg (flyer page 2)](pages/flyer159-page2-c762147e24.jpg)
- **Image source URL:** http://circulaires.com/b/marche-bkr/22/b2.jpg
- **Details:** confidence: 0.99 · item_key: `e1118f20f2df6405`
- **Raw:** `{"block_text": "ETOILES DE NUIT\nTHÉ VERT 160G", "ocr_lines": ["ETOILESDENUIT", "THEVERT 160G"]}`

**Item Review Analysis (Pass 1):** Correct. Étoiles de Nuit green tea (160 g) at 1.29$ — verified; the matching molokhia price is a genuine coincidence. Tea & Hot Drinks is right.

### Item 15190

![item 15190](images/item-15190.jpg)

- **Name (English):** None
- **Name (French):** AL AFIA FEUILLE DE VIGNE 45uG
- **Brand:** None
- **Category (English):** International Foods > Middle Eastern Foods
- **Category (French):** Aliments internationaux > Aliments du Moyen-Orient
- **How classified:** rule (`middle-eastern`)
- **Size:** 454G
- **Price:** 6.69
- **Printed Price:** “6.69”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 424, top 688, right 610, bottom 934, page 2
- **Full page:** [pages/flyer159-page2-c762147e24.jpg (flyer page 2)](pages/flyer159-page2-c762147e24.jpg)
- **Image source URL:** http://circulaires.com/b/marche-bkr/22/b2.jpg
- **Details:** confidence: 0.77 · item_key: `99167611b8e5f17b`
- **Raw:** `{"block_text": "AL AFIA FEUILLE\nDE VIGNE 45uG", "ocr_lines": ["AL AFIA FEUILLE", "DE VIGNE 454G"], "harvest": {"size": "454G", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Al Afia grape leaves (454 g) print 5.99$; the DB had 6.69. Middle Eastern Foods is right. (The stored name garbles the size as "45uG" — OCR text only; the crop reads 454G.)

### Item 15191

![item 15191](images/item-15191.jpg)

- **Name (English):** None
- **Name (French):** ALDOHA RIZ EGYPTIEN 10LBS
- **Brand:** None
- **Category (English):** Pantry > Rice
- **Category (French):** Produits du garde-manger > Riz
- **How classified:** rule (`rice`)
- **Size:** 10LBS
- **Price:** 10.99
- **Printed Price:** “10.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 686, top 684, right 908, bottom 927, page 3
- **Full page:** [pages/flyer159-page3-ff9b1169ee.jpg (flyer page 3)](pages/flyer159-page3-ff9b1169ee.jpg)
- **Image source URL:** http://circulaires.com/b/marche-bkr/22/b4.jpg
- **Details:** confidence: 0.99 · item_key: `582c8fd70f532874`
- **Raw:** `{"block_text": "ALDOHA\nRIZ EGYPTIEN 10LBS", "ocr_lines": ["ALDOHA", "RIZEGYPTIEN 10LBS"]}`

**Item Review Analysis (Pass 1):** Correct. Aldoha Egyptian rice (10 lbs) at 10.99$ — verified. Rice is right.

### Item 15192

![item 15192](images/item-15192.jpg)

- **Name (English):** None
- **Name (French):** FROMAGE BALADI
- **Brand:** None
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** None
- **Price:** 16.99
- **Printed Price:** “16.99”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 111, top 685, right 436, bottom 928, page 3
- **Full page:** [pages/flyer159-page3-ff9b1169ee.jpg (flyer page 3)](pages/flyer159-page3-ff9b1169ee.jpg)
- **Image source URL:** http://circulaires.com/b/marche-bkr/22/b4.jpg
- **Details:** confidence: 0.99 · item_key: `12c811e041cb0f4b`
- **Raw:** `{"block_text": "FROMAGE BALADI", "ocr_lines": ["FROMAGE BALADI"]}`

**Item Review Analysis (Pass 1):** Correct. Baladi cheese at 16.99$/kg — verified. Cheese is right.

### Item 15193

![item 15193](images/item-15193.jpg)

- **Name (English):** None
- **Name (French):** MAKDOUCE
- **Brand:** None
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`canned-pickled`)
- **Size:** None
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 638, top 686, right 916, bottom 936, page 4
- **Full page:** [pages/flyer159-page4-310a06f70c.jpg (flyer page 4)](pages/flyer159-page4-310a06f70c.jpg)
- **Image source URL:** http://circulaires.com/b/marche-bkr/22/b5.jpg
- **Details:** confidence: 0.99 · item_key: `a6fa90ae03df6f35`
- **Raw:** `{"block_text": "MAKDOUCE", "ocr_lines": ["MAKDOUCE"]}`

**Item Review Analysis (Pass 1):** Correct. Makdous (pickled stuffed eggplant) at 6.99$/kg — verified. Canned & Pickled is right.

### Item 15194

![item 15194](images/item-15194.jpg)

- **Name (English):** None
- **Name (French):** HACHE EXTRA MAIGRE
- **Brand:** None
- **Category (English):** Meat > Beef
- **Category (French):** Viande > Bœuf
- **How classified:** rule (`beef`)
- **Size:** None
- **Price:** 19.99
- **Printed Price:** “19.99”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 94, top 688, right 419, bottom 928, page 5
- **Full page:** [pages/flyer159-page5-323cfda93a.jpg (flyer page 5)](pages/flyer159-page5-323cfda93a.jpg)
- **Image source URL:** http://circulaires.com/b/marche-bkr/22/b6.jpg
- **Details:** confidence: 0.99 · item_key: `46c74e0d9b604340`
- **Raw:** `{"block_text": "HACHE EXTRA MAIGRE", "ocr_lines": ["HACHE EXTRA MAIGRE"]}`

**Item Review Analysis (Pass 1):** Correct. Extra-lean ground beef at 19.99$/kg — verified. Beef is right.

### Item 15195

![item 15195](images/item-15195.jpg)

- **Name (English):** None
- **Name (French):** FAUX FILET
- **Brand:** None
- **Category (English):** Meat > Beef
- **Category (French):** Viande > Bœuf
- **How classified:** rule (`beef`)
- **Size:** None
- **Price:** 34.99
- **Printed Price:** “34.99”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 626, top 684, right 953, bottom 926, page 5
- **Full page:** [pages/flyer159-page5-323cfda93a.jpg (flyer page 5)](pages/flyer159-page5-323cfda93a.jpg)
- **Image source URL:** http://circulaires.com/b/marche-bkr/22/b6.jpg
- **Details:** confidence: 0.99 · item_key: `38bd26dd84956140`
- **Raw:** `{"block_text": "FAUX FILET", "ocr_lines": ["FAUX FILET"]}`

**Item Review Analysis (Pass 1):** Correct. Faux filet (rib steak) at 34.99$/kg — verified. Beef is right.
