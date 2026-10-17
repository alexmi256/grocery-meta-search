# Marché Sultan — full product report

Store slug: `marche-sultan`. Generated from `data/grocery.db`. A sampled subset of 15 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 160, valid 2026-10-15 → 2026-10-21, 27 items). The expired Oct 8–14 edition is correctly excluded.
- **Sample counts:** 5 classified + 10 unclassified shown (15 of the edition's 27 items) — the shortfall is the small edition, and the unclassified tilt is this store's character: a Turkish/Middle-Eastern assortment whose product names OCR into Turkish strings the classifier's FR/EN vocabulary doesn't cover.
- **Issues found:** one dominant defect — 7 of 15 sampled prices were the crossed-out REGULAR price, not the sale price. This flyer's layout prints the regular price small with a red X at the top-right of the cell and the sale price big below it; when the big price fell outside the item's text block, the segmenter anchored the crossed price (Demlik tea 4.99 for 3.99, mozzarella 6.29 for 4.99, ajvar 2.79 for 1.79, chick peas 2.29 for 1.79, spaghetti 2.49 for 1.49). Two more were value garbles: the Rize tea at 6.69 for a printed 6.99 (9→6) and the vine leaves at 79.99 for 7.99 (decimal shift). All seven plus the two garbles corrected from the pages. Two sampled items are household chemicals (Vatan softener, Vatan tulle polish) carried unclassified under garbled names — kept for review under the standing rule.
- **Fixes applied this pass:** 15199 → 3.99, 15200 → 6.99, 15203 → 7.99, 15206 → 1.79, 15212 → 1.49, 15217 → 1.79, 15221 → 4.99.

## Flyer 160 — valid 2026-10-15 → 2026-10-21 (5 classified items, 10 unclassified)

Source ref: `circ-22-2026-10-15` · fetched 2026-10-16T20:42:46.351Z

### Item 15199

![item 15199](images/item-15199.jpg)

- **Name (English):** None
- **Name (French):** DEMLIK 40POSET
- **Brand:** None
- **Category (English):** Drinks > Tea & Hot Drinks
- **Category (French):** Boissons > Thés et boissons chaudes
- **How classified:** rule (`tea-hot-drinks`)
- **Size:** None
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 835, top 549, right 969, bottom 588, page 2
- **Full page:** [pages/flyer160-page2-ec02b60dde.jpg (flyer page 2)](pages/flyer160-page2-ec02b60dde.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s1.jpg
- **Details:** confidence: 0.88 · item_key: `82b2ba23657e7817`
- **Conditions:** `{"alt_prices": ["3.99", "4.99"]}`
- **Raw:** `{"block_text": "A tt\n\n, de te\na AUK\nfi 0", "ocr_lines": ["DEMLIK", "40POSET"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 2. Demlik tea bags (40 sachets) sell at 3.99; the DB had 4.99 — the crossed-out regular price above it. Tea & Hot Drinks is right.

### Item 15201

![item 15201](images/item-15201.jpg)

- **Name (English):** None
- **Name (French):** SWEETCORN
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** 6L
- **Price:** 1.79
- **Printed Price:** “1.79”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 455, top 849, right 648, bottom 957, page 2
- **Full page:** [pages/flyer160-page2-ec02b60dde.jpg (flyer page 2)](pages/flyer160-page2-ec02b60dde.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s1.jpg
- **Details:** confidence: 0.99 · item_key: `bf2f14e7bed74efe`
- **Conditions:** `{"alt_prices": ["1.99"]}`
- **Raw:** `{"block_text": "LE LL. D 4 LES\nSWEET CORN", "ocr_lines": ["SWEETCORN"], "harvest": {"size": "6L", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Sweet corn at 1.79 (reg. 1.99, crossed, visible in the crop) — the segmenter took the big sale price here. Fresh Vegetables is right.

### Item 15205

![item 15205](images/item-15205.jpg)

- **Name (English):** None
- **Name (French):** Tomato Paste
- **Brand:** None
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`canned-pickled`)
- **Size:** None
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 763, top 277, right 984, bottom 402, page 3
- **Full page:** [pages/flyer160-page3-e8ddcc3721.jpg (flyer page 3)](pages/flyer160-page3-e8ddcc3721.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s2.jpg
- **Details:** confidence: 0.99 · item_key: `6cbac7bdbc8b80ac`
- **Raw:** `{"block_text": "Spin Lex\nTomato Paste", "ocr_lines": ["Tomato Paste"]}`

**Item Review Analysis (Pass 1):** Correct. Tomato paste at 2.99 (reg. 3.99) — verified. Canned & Pickled is right.

### Item 15210

![item 15210](images/item-15210.jpg)

- **Name (English):** None
- **Name (French):** RENDE DOMATES PASSATA RUSTICA
- **Brand:** None
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`specific-canned`)
- **Size:** None
- **Price:** 1.79
- **Printed Price:** “1.79”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 729, top 843, right 983, bottom 958, page 4
- **Full page:** [pages/flyer160-page4-c20fd0122b.jpg (flyer page 4)](pages/flyer160-page4-c20fd0122b.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s3.jpg
- **Details:** confidence: 0.99 · item_key: `87cf62d7b123b5ef`
- **Conditions:** `{"alt_prices": ["2.49"]}`
- **Raw:** `{"block_text": "LR. nn.\nRENDE\nDOMATES\nPASSATA RUSTICA", "ocr_lines": ["RENDE", "DOMATES", "PASSATA RUSTICA"]}`

**Item Review Analysis (Pass 1):** Correct. Burcu grated-tomato passata (685 g) at 1.79 (reg. 2.49) — verified. Canned & Pickled is right.

### Item 15221

![item 15221](images/item-15221.jpg)

- **Name (English):** None
- **Name (French):** Mozzarella Ball Balle
- **Brand:** None
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** 260g
- **Price:** 6.29
- **Printed Price:** “6.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 32, top 497, right 314, bottom 583, page 6
- **Full page:** [pages/flyer160-page6-8074c1dd9b.jpg (flyer page 6)](pages/flyer160-page6-8074c1dd9b.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s5.jpg
- **Details:** confidence: 0.93 · item_key: `1b727addbf8fbbc6`
- **Conditions:** `{"alt_prices": ["4.66", "15.99", "20.99"]}`
- **Raw:** `{"block_text": "Mozzarella Ball Balle\nProcessed Cheese Prodoct ! : 5", "ocr_lines": ["Mozzarella Ball Balle"], "harvest": {"size": "260g", "via": "crop"}}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 160 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 6. Silani mozzarella ball (260 g) sells at 4.99; the DB had 6.29 — the crossed-out regular price. Cheese is right.

### Item 15200

![item 15200](images/item-15200.jpg)

- **Name (English):** None
- **Name (French):** Rize turistcayi
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 6.69
- **Printed Price:** “6.69”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 471, top 237, right 638, bottom 306, page 2
- **Full page:** [pages/flyer160-page2-ec02b60dde.jpg (flyer page 2)](pages/flyer160-page2-ec02b60dde.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s1.jpg
- **Details:** confidence: 0.99 · item_key: `306ddbab20195cde`
- **Conditions:** `{"alt_prices": ["5.99"]}`
- **Raw:** `{"block_text": "[ Rize\nturist çayl", "ocr_lines": ["Rize", "turistcayi"]}`

— from flyer 160 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Çaykur Rize tourist tea prints 6.99; the DB had 6.69 (the 9→6 glyph error). Unclassified under its Turkish name.

### Item 15202

![item 15202](images/item-15202.jpg)

- **Name (English):** None
- **Name (French):** Goksen
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 8.99
- **Printed Price:** “8.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 160, top 241, right 320, bottom 396, page 2
- **Full page:** [pages/flyer160-page2-ec02b60dde.jpg (flyer page 2)](pages/flyer160-page2-ec02b60dde.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s1.jpg
- **Details:** confidence: 0.99 · item_key: `0802425a906edc93`
- **Raw:** `{"block_text": null, "ocr_lines": ["Goksen"]}`

— from flyer 160 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Göksen strawberry jam at 8.99 (reg. 12.99) — verified on the crop. Unclassified under the brand-only name.

### Item 15203

![item 15203](images/item-15203.jpg)

- **Name (English):** None
- **Name (French):** AMURABAGTYAI HASLANMISTIR
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 79.99
- **Printed Price:** “79.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 86, top 870, right 321, bottom 962, page 3
- **Full page:** [pages/flyer160-page3-e8ddcc3721.jpg (flyer page 3)](pages/flyer160-page3-e8ddcc3721.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s2.jpg
- **Details:** confidence: 0.89 · item_key: `24a9b3eda62b490b`
- **Conditions:** `{"alt_prices": ["6.66"]}`
- **Raw:** `{"block_text": "SE til |\npy NURA BAG TA!\ni HASLANMISTIR.", "ocr_lines": ["AMURABAGTYAI", "HASLANMISTIR."]}`

— from flyer 160 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Muttalip stuffed vine leaves print 7.99 (reg. 9.99); the DB had 79.99 — a decimal shift. Unclassified under its garbled Turkish name.

### Item 15206

![item 15206](images/item-15206.jpg)

- **Name (English):** None
- **Name (French):** PHOENICIA
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 2.29
- **Printed Price:** “2.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 771, top 528, right 979, bottom 589, page 3
- **Full page:** [pages/flyer160-page3-e8ddcc3721.jpg (flyer page 3)](pages/flyer160-page3-e8ddcc3721.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s2.jpg
- **Details:** confidence: 0.99 · item_key: `27d4fca7cb0cdfc0`
- **Conditions:** `{"alt_prices": ["1.79"]}`
- **Raw:** `{"block_text": "7\nDPHOENICIA\nSa", "ocr_lines": ["PHOENICIA"]}`

— from flyer 160 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 3. Cedar Phoenicia chick peas (540 ml) sell at 1.79; the DB had 2.29 — the crossed-out regular price. Unclassified under the brand-only name.

### Item 15212

![item 15212](images/item-15212.jpg)

- **Name (English):** None
- **Name (French):** Ne500ge isiinrSurcsi
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 500g
- **Price:** 2.49
- **Printed Price:** “2.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 161, top 436, right 323, bottom 537, page 4
- **Full page:** [pages/flyer160-page4-c20fd0122b.jpg (flyer page 4)](pages/flyer160-page4-c20fd0122b.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s3.jpg
- **Details:** confidence: 0.94 · item_key: `510ef5368220460d`
- **Conditions:** `{"alt_prices": ["1.49"]}`
- **Raw:** `{"block_text": "NIEME\n\nNa 5M g\n| + |\nslip Bikes", "ocr_lines": ["Ne500ge", "isiinrSurcsi"], "harvest": {"size": "500g", "via": "crop"}}`

— from flyer 160 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 4. Ankara spaghetti (500 g) sells at 1.49; the DB had 2.49 — the crossed-out regular price. Unclassified under its garbled name.

### Item 15214

![item 15214](images/item-15214.jpg)

- **Name (English):** None
- **Name (French):** Vatan Komsu Catlatan
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 4.49
- **Printed Price:** “4.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 800, top 546, right 973, bottom 682, page 5
- **Full page:** [pages/flyer160-page5-2e8f6a3907.jpg (flyer page 5)](pages/flyer160-page5-2e8f6a3907.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s4.jpg
- **Details:** confidence: 0.79 · item_key: `f76a5ea82e0d80fc`
- **Raw:** `{"block_text": "| Kon Sores %\nRomsu |\nCatlatam", "ocr_lines": ["Vatan", "Komsu", "Catlatan"]}`

— from flyer 160 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Price correct, product noted. Vatan fabric softener at 4.49 +tx (reg. 5.99 +tx) — verified. A household chemical carried unclassified under a garbled name; kept for review under the standing rule.

### Item 15215

![item 15215](images/item-15215.jpg)

- **Name (English):** None
- **Name (French):** TUPEPOLISH GOLD
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 750, top 865, right 994, bottom 974, page 5
- **Full page:** [pages/flyer160-page5-2e8f6a3907.jpg (flyer page 5)](pages/flyer160-page5-2e8f6a3907.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s4.jpg
- **Details:** confidence: 0.99 · item_key: `c863bcda062a8aaf`
- **Raw:** `{"block_text": "RCA LISE\nid =\nt e", "ocr_lines": ["TUPEPOLISH", "GOLD"]}`

— from flyer 160 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Price correct, product noted. Vatan tulle polish (1 L) at 2.99 +tx (reg. 3.99 +tx) — verified. Household chemical, unclassified; kept for review.

### Item 15217

![item 15217](images/item-15217.jpg)

- **Name (English):** None
- **Name (French):** AJVARSWEET
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 2.79
- **Printed Price:** “2.79”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 775, top 263, right 984, bottom 303, page 5
- **Full page:** [pages/flyer160-page5-2e8f6a3907.jpg (flyer page 5)](pages/flyer160-page5-2e8f6a3907.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s4.jpg
- **Details:** confidence: 0.99 · item_key: `ebc73aec635bdc12`
- **Raw:** `{"block_text": "_AJVAR SWEET", "ocr_lines": ["AJVARSWEET"]}`

— from flyer 160 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 5. Burcu ajvar (sweet pepper spread, 310 g) sells at 1.79; the DB had 2.79 — the crossed-out regular price. Unclassified.

### Item 15218

![item 15218](images/item-15218.jpg)

- **Name (English):** None
- **Name (French):** Vatan Cadlten Sena "Dunur
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 11.99
- **Printed Price:** “11.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 511, top 311, right 683, bottom 592, page 5
- **Full page:** [pages/flyer160-page5-2e8f6a3907.jpg (flyer page 5)](pages/flyer160-page5-2e8f6a3907.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s4.jpg
- **Details:** confidence: 0.99 · item_key: `28b9ebb0b7f736bf`
- **Raw:** `{"block_text": "Gia) =\nCadlitan Sert\nDünür\ndl", "ocr_lines": ["Vatan", "Cadlten Sena", "\"Dunur", "Catlatan"]}`

— from flyer 160 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. The 11.99 (reg. 13.99) belongs to the peppers pictured above; the stored name bleeds in the Vatan softener text from the row below. Unclassified.

### Item 15220

![item 15220](images/item-15220.jpg)

- **Name (English):** None
- **Name (French):** SMOOTH. SAVOURY& NUTTY
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 779, top 258, right 988, bottom 409, page 6
- **Full page:** [pages/flyer160-page6-8074c1dd9b.jpg (flyer page 6)](pages/flyer160-page6-8074c1dd9b.jpg)
- **Image source URL:** http://circulaires.com/b/marche-sultan/22/s5.jpg
- **Details:** confidence: 0.99 · item_key: `6017fbf16bb70f1f`
- **Conditions:** `{"alt_prices": ["7.99", "29.99"]}`
- **Raw:** `{"block_text": "<mooll.\nSAVOURT &\n\nNUTTY\nONCTUEUX\nAV etIX 4", "ocr_lines": ["SMOOTH.", "SAVOURY&", "NUTTY", "ONCTUEUX"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. The smooth/savoury/nutty cheese (Beemster-style) at 6.99 (reg. 7.99) — verified. Unclassified under its description-only name.
