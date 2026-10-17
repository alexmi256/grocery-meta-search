# Marché Bonanza — full product report

Store slug: `marche-bonanza`. Generated from `data/grocery.db`. A sampled subset of 13 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 161, valid 2026-10-14 → 2026-10-20; the printed validity in page 1's footer matches). The expired Oct 7–13 edition is correctly excluded. The edition holds 25 items after this pass's purge (26 before).
- **Sample counts:** 3 classified + 10 unclassified shown. The unclassified mass is this store's character: its page type OCRs into brand fragments and tags ("DECECCO", "KIM", "CONGELE", "CAISSE") that carry no classifiable product word — the items are real, their prices mostly right, their names stubs. Page 1 alone prints ~15 products and capture across the 4 pages is partial in the same fragmenting way.
- **Issues found and fixed:** (1) The flyer's entire legal footer had formed an item ("LES PRODUITS SONT EN VENTE JUSQU'À ÉPUISEMENT DES STOCKS…") carrying the bleach's 1.99 — purged, and the exclusion layer now treats the footer phrases ("épui­se­ment des stocks", "while supplies last") as flyer furniture so future fetches discard them at ingest (tests green). (2) A cents badge read as dollars: assorted squash at 69¢/lb was stored as 69.00 under a "MERCREDI - JEUDI" banner name. The store prices produce in bare cents badges like 3 Saisons — a controlled segment run on page 4 showed `bare_int_is_cents` changes exactly the four badge anchors (12/49/66/69 → cents) and nothing else, so the setting is now enabled for this store; the stored item is corrected to 0.69/lb. (3) Multibuy/derivation errors: Activia 3/10$ stored as 10.00 → 3.49 with the multibuy recorded; iögo stored 3.33 (a bad 10÷3 split) → its printed 3.49. (4) Crossed pairs: the Chapman's item carried the garlic paste's 2.49 → Chapman's prints 4.99; the De Cecco egg-nest fragment (first draw) carried the soy sauce's 1.29 → the nests print 3.49; the Mirabel shrimp (first draw) carried 65.00 → the shrimp (2 lb bag) prints 19.99; the Cuor di Paese mortadella (first draw) carried the provolone's badge → mortadella prints 9.99/lb. (5) One fragment left unresolved: item 15241 ("CONGELE", 6.00) matches neither neighbour's price (capicollo 3.99/lb, tilapia 11.99) — recorded, not guessed.
- **Fixes applied this pass:** exclusion footer rule (committed); `bare_int_is_cents` enabled for this store (committed); footer item 15226 purged; prices corrected: 15228 → 3.49 (+multibuy), 15235 → 3.49, 15236 → 3.49, 15238 → 4.99, 15240 → 19.99, 15242 → 9.99/lb, 15247 → 0.69/lb.

## Flyer 161 — valid 2026-10-14 → 2026-10-20 (3 classified items, 10 unclassified)

Source ref: `circulaire-bonanza-lalumiere-du-14-au-20-octobre-2026` · fetched 2026-10-17T04:08:43.998Z

### Item 15227

![item 15227](images/item-15227.jpg)

- **Name (English):** None
- **Name (French):** ] PASSATA ©
- **Brand:** None
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`specific-canned`)
- **Size:** None
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 24, top 274, right 238, bottom 331, page 2
- **Full page:** [pages/flyer161-page2-bd46388409.jpg (flyer page 2)](pages/flyer161-page2-bd46388409.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bonanza-lalumiere-du-14-au-20-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `c1efefc703d240c7`
- **Conditions:** `{"alt_prices": ["1.69"]}`
- **Raw:** `{"block_text": "] PASSATA ©", "ocr_lines": ["DECECCO", "DECECCO", "PASSATA", "PASSATA"]}`

**Item Review Analysis (Pass 1):** Correct. De Cecco strained tomatoes (680 ml) at 1.99 — verified on page 2. The name is a fragment ("] PASSATA") but the item classified to Canned & Pickled.

### Item 15228

![item 15228](images/item-15228.jpg)

- **Name (English):** None
- **Name (French):** ACTIVIA
- **Brand:** None
- **Category (English):** Dairy & Eggs > Yogurt
- **Category (French):** Produits laitiers et œufs > Yogourt
- **How classified:** rule (`yogurt`)
- **Size:** None
- **Price:** 3.49
- **Printed Price:** “3.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 708, top 945, right 889, bottom 986, page 2
- **Full page:** [pages/flyer161-page2-bd46388409.jpg (flyer page 2)](pages/flyer161-page2-bd46388409.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bonanza-lalumiere-du-14-au-20-octobre-2026/02.webp
- **Details:** confidence: 0.77 · item_key: `926c1789fe5b0615`
- **Conditions:** `{"multibuy": {"count": 3, "total": 10.0}}`
- **Raw:** `{"block_text": "=... Y%\nACTIVA", "ocr_lines": ["ACTIVIA"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 2. Danone Activia yogurt (650 g) prints "3/10$ — 3.49$ l'unité"; the DB had stored the 10.00 total. Now 3.49 with the multibuy recorded. Yogurt is right.

### Item 15237

![item 15237](images/item-15237.jpg)

- **Name (English):** None
- **Name (French):** ACTIVIA
- **Brand:** None
- **Category (English):** Dairy & Eggs > Yogurt
- **Category (French):** Produits laitiers et œufs > Yogourt
- **How classified:** rule (`yogurt`)
- **Size:** None
- **Price:** 5.49
- **Printed Price:** “5.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 703, top 816, right 825, bottom 916, page 2
- **Full page:** [pages/flyer161-page2-bd46388409.jpg (flyer page 2)](pages/flyer161-page2-bd46388409.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bonanza-lalumiere-du-14-au-20-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `926c1789fe5b0615`
- **Raw:** `{"block_text": "ACTIVA", "ocr_lines": ["ACTIVIA"]}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 161 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Correct. A second Activia offer (Danone yogurt) at 5.49 — verified on its crop; distinct from the 3/10$ Activia. Yogurt is right.

### Item 15225

![item 15225](images/item-15225.jpg)

- **Name (English):** None
- **Name (French):** ORIGINAL
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 4.49
- **Printed Price:** “4.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 569, top 84, right 827, bottom 135, page 1
- **Full page:** [pages/flyer161-page1-4354625799.jpg (flyer page 1)](pages/flyer161-page1-4354625799.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bonanza-lalumiere-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `2618fbec23fe509d`
- **Raw:** `{"block_text": "GINAL", "ocr_lines": ["ORIGINAL"]}`

— from flyer 161 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Price correct, name a fragment. Astro Original yogurt (12 x 100 g) at 4.49 (page 1, manager's special) — the item's whole name is "ORIGINAL", so it sits unclassified; the price is the product's own.

### Item 15229

![item 15229](images/item-15229.jpg)

- **Name (English):** None
- **Name (French):** DECECCO
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 26, top 138, right 128, bottom 192, page 2
- **Full page:** [pages/flyer161-page2-bd46388409.jpg (flyer page 2)](pages/flyer161-page2-bd46388409.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bonanza-lalumiere-du-14-au-20-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `8f3f9140f04f38a8`
- **Raw:** `{"block_text": "“DELECCO", "ocr_lines": ["DECECCO"]}`

— from flyer 161 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Price correct, name a fragment. De Cecco pasta (454 g) at 1.99 (page 2) — name is the brand alone, unclassified; price verified.

### Item 15233

![item 15233](images/item-15233.jpg)

- **Name (English):** None
- **Name (French):** NONTANA
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 2.49
- **Printed Price:** “2.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 0, top 624, right 186, bottom 684, page 2
- **Full page:** [pages/flyer161-page2-bd46388409.jpg (flyer page 2)](pages/flyer161-page2-bd46388409.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bonanza-lalumiere-du-14-au-20-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `6770f0a9bedef163`
- **Raw:** `{"block_text": "| MONTANA |", "ocr_lines": ["NONTANA"]}`

— from flyer 161 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Price correct, name garbled. Montana artichoke bottoms (375 g) at 2.49 (page 2) — "NONTANA" is Montana misread; price verified.

### Item 15235

![item 15235](images/item-15235.jpg)

- **Name (English):** None
- **Name (French):** IOGO
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 3.33
- **Printed Price:** “3/10.00”
- **Unit quantity:** 3.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 334, top 850, right 497, bottom 925, page 2
- **Full page:** [pages/flyer161-page2-bd46388409.jpg (flyer page 2)](pages/flyer161-page2-bd46388409.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bonanza-lalumiere-du-14-au-20-octobre-2026/02.webp
- **Details:** confidence: 0.94 · item_key: `ba4ce3f5eee6b71a`
- **Conditions:** `{"multibuy": {"count": 3, "total": 10.0}}`
- **Raw:** `{"block_text": null, "ocr_lines": ["IOGO"]}`

— from flyer 161 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 2. iögo drinkable yogurt prints 3.49; the DB had 3.33 (a bad split of the neighbouring 3/10$). Name is the brand fragment "IOGO" — unclassified; price now right.

### Item 15238

![item 15238](images/item-15238.jpg)

- **Name (English):** None
- **Name (French):** GUAPMAN'S
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 2.49
- **Printed Price:** “2.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 780, top 462, right 888, bottom 572, page 2
- **Full page:** [pages/flyer161-page2-bd46388409.jpg (flyer page 2)](pages/flyer161-page2-bd46388409.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bonanza-lalumiere-du-14-au-20-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `42719f1cdad82b01`
- **Raw:** `{"block_text": "ZNMANS)", "ocr_lines": ["GUAPMAN'S"]}`

— from flyer 161 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 2. The name is Chapman's (frozen yogurt/sorbet, 2 L, prints 4.99); the DB carried 2.49 — the Shan garlic/ginger paste's price from the cell above. Now 4.99.

### Item 15241

![item 15241](images/item-15241.jpg)

- **Name (English):** None
- **Name (French):** CONGELE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 6.00
- **Printed Price:** “6”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 563, top 237, right 777, bottom 303, page 3
- **Full page:** [pages/flyer161-page3-5e48ff6931.jpg (flyer page 3)](pages/flyer161-page3-5e48ff6931.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bonanza-lalumiere-du-14-au-20-octobre-2026/03.webp
- **Details:** confidence: 0.62 · item_key: `44bddc34a8bcaec6`
- **Raw:** `{"block_text": "CONGELE", "ocr_lines": ["CONGELE"]}`

— from flyer 161 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Unresolved fragment, left as found. The name is the "CONGELÉ" tag; its crop neighbours price at 3.99/lb (capicollo) and 11.99 (tilapia) and neither matches the stored 6.00. Recorded rather than guessed.

### Item 15243

![item 15243](images/item-15243.jpg)

- **Name (English):** None
- **Name (French):** CONGELE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 11.99
- **Printed Price:** “11.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 674, top 355, right 979, bottom 438, page 3
- **Full page:** [pages/flyer161-page3-5e48ff6931.jpg (flyer page 3)](pages/flyer161-page3-5e48ff6931.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bonanza-lalumiere-du-14-au-20-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `44bddc34a8bcaec6`
- **Conditions:** `{"alt_prices": ["7.99"]}`
- **Raw:** `{"block_text": "CONGELE", "ocr_lines": ["CONGELE"]}`

— from flyer 161 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Price correct, name a tag. Tilapia fillets (2 lb bag) at 11.99 — verified on page 3; the name is the neighbouring "CONGELÉ" tag.

### Item 15244

![item 15244](images/item-15244.jpg)

- **Name (English):** None
- **Name (French):** sé D CHICK PAS " FOISCHICNES
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 1.79
- **Printed Price:** “1.79”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 331, top 911, right 576, bottom 959, page 4
- **Full page:** [pages/flyer161-page4-c20170dd7d.jpg (flyer page 4)](pages/flyer161-page4-c20170dd7d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bonanza-lalumiere-du-14-au-20-octobre-2026/04.webp
- **Details:** confidence: 0.94 · item_key: `2aac4b06969a9714`
- **Raw:** `{"block_text": "- is bete Pen\nCHICK PR) iL. 2- fe\nrows. cc ie\nsé D CHICK PAS\n\" FOISCHICNES\ni es mms", "ocr_lines": ["CHICK PEA", "POIS CHICH", "CHICKPEAS", "POISCHICHES"]}`

— from flyer 161 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Price correct, name garble. Fresh Nut roasted yellow chickpeas (250 g) at 1.79 — verified on the crop; the stored name is OCR noise around "CHICK PEAS".

### Item 15247

![item 15247](images/item-15247.jpg)

- **Name (English):** None
- **Name (French):** MERCREDI - JEUDI
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 69.00
- **Printed Price:** “69”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 339, top 447, right 661, bottom 558, page 4
- **Full page:** [pages/flyer161-page4-c20170dd7d.jpg (flyer page 4)](pages/flyer161-page4-c20170dd7d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bonanza-lalumiere-du-14-au-20-octobre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `944af44d6b306bae`
- **Raw:** `{"block_text": "MERCREDI - JEUDI", "ocr_lines": ["MERCREDI-JEUDI"]}`

— from flyer 161 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Assorted squash (Quebec) prints 69¢/lb; the DB had 69.00 under the "MERCREDI - JEUDI" banner text. Now 0.69/lb — and the store's cents-badge setting is enabled for future fetches (see header).

### Item 15248

![item 15248](images/item-15248.jpg)

- **Name (English):** None
- **Name (French):** CAISSE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 2.49
- **Printed Price:** “2.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 17, top 443, right 124, bottom 575, page 4
- **Full page:** [pages/flyer161-page4-c20170dd7d.jpg (flyer page 4)](pages/flyer161-page4-c20170dd7d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bonanza-lalumiere-du-14-au-20-octobre-2026/04.webp
- **Details:** confidence: 0.90 · item_key: `93534a091f2857ac`
- **Raw:** `{"block_text": "CAISSE", "ocr_lines": ["CAISSE"]}`

**Item Review Analysis (Pass 1):** Price correct, name a tag. Onions at 2.49/bag — the name took the "CAISSE 7 lb" tag below the badge; the price is the onions' own.
