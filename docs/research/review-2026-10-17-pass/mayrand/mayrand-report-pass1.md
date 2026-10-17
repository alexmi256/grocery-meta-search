# Mayrand Food Group — full product report

Store slug: `mayrand`. Generated from `data/grocery.db`. A sampled subset of 20 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 105, valid 2026-10-14 → 2026-10-20, 30 items — the whole edition is sampled at 10 + 10 of 30).
- **Sample counts:** 10 classified + 10 unclassified shown, as drawn.
- **Issues found:** this store's table layout is the story. Each product row prints a name cell, a descriptor cell ("Fresh / SKU / price-per-kg") and a big price cell, and the segmenter repeatedly captured the descriptor cell as its own item. Three sampled items are pure fragments of rows whose products are properly in the DB — "Fresh 16.51/kg" is the Beef Bourguignon Cubes' descriptor (SKU 50111 matches item 11515), "Fresh 8.80/kg" is the Capicollo's (SKU 52048, item 11514), and "TOP" is a TOP DEAL badge over a struck-through regular price — all three deleted. A fourth fragment ("Fresh", SKU 52236, 6.59/kg) has no named parent item in the DB, so it stays as the only trace of that product. One real price error: the Natrel milk/cream cups item stored 2.10, which matches neither printed price; the item anchors the cream cups, corrected to 6.99 (the milk cups print 4.99). The classified items' prices all verified, including the roast at 6.49/lb against its 14.31$/kg descriptor.
- **Fixes applied this pass:** 11526 → 6.99; items 11501, 11509, 11510 deleted (fragments of items 11515/11514 and a deal badge).

## Flyer 105 — valid 2026-10-14 → 2026-10-20 (10 classified items, 10 unclassified)

Source ref: `https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf` · fetched 2026-10-14T17:40:16.956Z

### Item 11505

![item 11505](images/item-11505.jpg)

- **Name (English):** None
- **Name (French):** Beef Inside Round Roast Fresh
- **Brand:** None
- **Category (English):** Meat > Beef
- **Category (French):** Viande > Bœuf
- **How classified:** rule (`beef`)
- **Size:** None
- **Price:** 6.49
- **Printed Price:** “6.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 33, top 342, right 114, bottom 561, page 1
- **Full page:** [pages/flyer105-page1-804eb6d28a.jpg (flyer page 1)](pages/flyer105-page1-804eb6d28a.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=1
- **Details:** confidence: 0.98 · item_key: `6e27d7c7f430f033`
- **Raw:** `{"block_text": "Beef Inside\nRound|Roast\nFresh -_", "ocr_lines": ["Beef Inside", "Round Roast", "Fresh"]}`

**Item Review Analysis (Pass 1):** Correct. Beef inside round roast at 6.49/lb — the crop shows the full row (Fresh / SKU 50107 / 14.31$/kg / reg. 21.99/kg), and the headline rate is the stored one. Beef is right.

### Item 11508

![item 11508](images/item-11508.jpg)

- **Name (English):** None
- **Name (French):** CREVETTES BLAND DUPACIFIQU ACIFICWHITE
- **Brand:** None
- **Category (English):** Fish & Seafood > Shrimp
- **Category (French):** Poissons et fruits de mer > Crevette
- **How classified:** rule (`shrimp`)
- **Size:** None
- **Price:** 13.99
- **Printed Price:** “13.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 696, top 785, right 877, bottom 902, page 2
- **Full page:** [pages/flyer105-page2-27e031b174.jpg (flyer page 2)](pages/flyer105-page2-27e031b174.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=2
- **Details:** confidence: 0.96 · item_key: `58907b41978159b7`
- **Raw:** `{"block_text": "LA >” né a >\nREVETTES BLANg\nDU PACIFiay\nACIFIC Al", "ocr_lines": ["CREVETTES BLAND", "DUPACIFIQU", "ACIFICWHITE"]}`

**Item Review Analysis (Pass 1):** Correct. Pacific white shrimp (907 g) at 13.99 (reg. 16.49) — verified. Shrimp is right.

### Item 11514

![item 11514](images/item-11514.jpg)

- **Name (English):** None
- **Name (French):** Capicollo Pork
- **Brand:** None
- **Category (English):** Meat > Pork & Ham
- **Category (French):** Viande > Porc et jambon
- **How classified:** rule (`pork-ham`)
- **Size:** None
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 32, top 295, right 119, bottom 561, page 2
- **Full page:** [pages/flyer105-page2-27e031b174.jpg (flyer page 2)](pages/flyer105-page2-27e031b174.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=2
- **Details:** confidence: 0.99 · item_key: `0ae2ec4d5c4c96e9`
- **Raw:** `{"block_text": "Capicollo Pork", "ocr_lines": ["Capicollo Pork"]}`

**Item Review Analysis (Pass 1):** Correct. Capicollo pork at 3.99/lb (8.80$/kg, reg. 10.99/kg) — verified; its descriptor cell became the separate fragment item 11510, deleted in this pass. Pork & Ham is right.

### Item 11515

![item 11515](images/item-11515.jpg)

- **Name (English):** None
- **Name (French):** Beef Bourguignon Cubes
- **Brand:** None
- **Category (English):** Meat > Beef
- **Category (French):** Viande > Bœuf
- **How classified:** rule (`beef`)
- **Size:** None
- **Price:** 7.49
- **Printed Price:** “7.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 28, top 620, right 139, bottom 883, page 2
- **Full page:** [pages/flyer105-page2-27e031b174.jpg (flyer page 2)](pages/flyer105-page2-27e031b174.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=2
- **Details:** confidence: 0.61 · item_key: `47f4f019f602c15c`
- **Raw:** `{"block_text": "Beef Bourguignon\nCubes | 5", "ocr_lines": ["Beef Bourguignon", "Cubes"]}`

**Item Review Analysis (Pass 1):** Correct. Beef bourguignon cubes at 7.49/lb (16.51$/kg, reg. 23.59$/kg) — verified from page 2; its descriptor cell became fragment item 11509, deleted in this pass. Beef is right.

### Item 11516

![item 11516](images/item-11516.jpg)

- **Name (English):** None
- **Name (French):** GASPESIEN SALAMI
- **Brand:** None
- **Category (English):** Deli > Deli Meat
- **Category (French):** Charcuterie > Charcuterie
- **How classified:** rule (`deli-meat`)
- **Size:** None
- **Price:** 3.49
- **Printed Price:** “3.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 318, top 443, right 445, bottom 577, page 3
- **Full page:** [pages/flyer105-page3-190b06c68f.jpg (flyer page 3)](pages/flyer105-page3-190b06c68f.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=3
- **Details:** confidence: 0.98 · item_key: `45602a2dc9da8e04`
- **Raw:** `{"block_text": "SALAMI", "ocr_lines": ["GASPESIEN", "SALAMI"]}`

**Item Review Analysis (Pass 1):** Correct. Gaspésien salami (175-250 g) from 3.49 (reg. up to 4.99) — verified. Deli Meat is right.

### Item 11517

![item 11517](images/item-11517.jpg)

- **Name (English):** None
- **Name (French):** TreStelle PARMIGIANO REGGIANO
- **Brand:** None
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** 500g
- **Price:** 19.99
- **Printed Price:** “19.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 70, top 402, right 225, bottom 505, page 3
- **Full page:** [pages/flyer105-page3-190b06c68f.jpg (flyer page 3)](pages/flyer105-page3-190b06c68f.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=3
- **Details:** confidence: 0.99 · item_key: `978d86c7ae3f0ad7`
- **Raw:** `{"block_text": "~\nREGUS\n. ; “HV\nbn ANO\"", "ocr_lines": ["TreStelle", "PARMIGIANO", "REGGIANO"], "harvest": {"size": "500g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Tre Stelle Parmigiano Reggiano (500 g) at 19.99 (reg. 23.99) — verified. Cheese is right.

### Item 11521

![item 11521](images/item-11521.jpg)

- **Name (English):** None
- **Name (French):** TARTEAUX BLEUETS SAUVAGES
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** 650g
- **Price:** 5.59
- **Printed Price:** “5.59”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 56, top 449, right 217, bottom 578, page 4
- **Full page:** [pages/flyer105-page4-e079076f03.jpg (flyer page 4)](pages/flyer105-page4-e079076f03.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=4
- **Details:** confidence: 0.98 · item_key: `cd06a47390257065`
- **Raw:** `{"block_text": "SU) TARTE AUX\n| BLEUETS\nSAUVAGES\n\nU SAGUENAY—LAC-SAINT-JEAN\noe\nPRETE A CUIRE\nREADY TO BAKE", "ocr_lines": ["TARTEAUX", "BLEUETS", "SAUVAGES", "DUSACUENAY-LAC-SAINT-JEAN", "WILDBLUEBERRYPIE", "PRETEACUIRE"], "harvest": {"size": "650g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Price correct, shelf note. Wild blueberry pie (ready to bake, 650 g) at 5.59 (reg. 7.59) — verified. It sits in Fresh Fruits on the blueberry wording; it's a bakery pie — a text-classification result, left as-is.

### Item 11524

![item 11524](images/item-11524.jpg)

- **Name (English):** None
- **Name (French):** Quebec Oranges or colored
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** 4.54 Kg
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 756, top 734, right 848, bottom 908, page 4
- **Full page:** [pages/flyer105-page4-e079076f03.jpg (flyer page 4)](pages/flyer105-page4-e079076f03.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=4
- **Details:** confidence: 0.99 · item_key: `60c6190d47266401`
- **Raw:** `{"block_text": "Quebec ARR\nà Le ÿ\nOrangestogeolored", "ocr_lines": ["Quebec", " Oranges or colored "], "harvest": {"size": "4.54 Kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Price correct, name truncated. The product is Quebec carrots (orange or coloured, 4.54 kg) at 4.99 (reg. up to 11.99) — the photo shows carrots; the OCR name dropped "carottes", leaving "Oranges or colored", which is also why it sits in Fresh Fruits. A text-only consequence, recorded.

### Item 11526

![item 11526](images/item-11526.jpg)

- **Name (English):** None
- **Name (French):** Natrel RYCREA
- **Brand:** None
- **Category (English):** Dairy & Eggs > Milk & Cream
- **Category (French):** Produits laitiers et œufs > Lait et crème
- **How classified:** rule (`milk-cream`)
- **Size:** None
- **Price:** 2.10
- **Printed Price:** “2.10”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 366, top 732, right 512, bottom 801, page 5
- **Full page:** [pages/flyer105-page5-e8692148f8.jpg (flyer page 5)](pages/flyer105-page5-e8692148f8.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=5
- **Details:** confidence: 0.94 · item_key: `59bffa478411dcf7`
- **Raw:** `{"block_text": "‘Natrel", "ocr_lines": ["Natrel", "RYCREA"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 5. The cell offers Natrel individual cups — 2% milk (100 x 15 ml) at 4.99 and 10% cream (100 x 15 ml) at 6.99. The stored item anchors the cream side (its garbled name reads "RYCREA" from "DAIRY CREAMERS") and stored 2.10, which matches neither price; corrected to 6.99. Milk & Cream is right.

### Item 11528

![item 11528](images/item-11528.jpg)

- **Name (English):** None
- **Name (French):** San Marzano CATEGORIE DE CHOIX Tomates
- **Brand:** None
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`specific-canned`)
- **Size:** 2.84 L
- **Price:** 8.49
- **Printed Price:** “8.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 839, top 486, right 946, bottom 648, page 5
- **Full page:** [pages/flyer105-page5-e8692148f8.jpg (flyer page 5)](pages/flyer105-page5-e8692148f8.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=5
- **Details:** confidence: 0.99 · item_key: `2a7eeff77dcc52cc`
- **Raw:** `{"block_text": "San Marzanoÿ Lit !\n2.84 L GATEGORIEDE CHOIX\n21840", "ocr_lines": ["San Marzano", "CATEGORIE DE CHOIX", "Tomates"]}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 105 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Correct. La San Marzano whole peeled tomatoes (2.84 L) at 8.49 (reg. 9.99) — verified. Canned & Pickled is right.

### Item 11501

![item 11501](images/item-11501.jpg)

- **Name (English):** None
- **Name (French):** TOP
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 4.08
- **Printed Price:** “4.08”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 352, top 506, right 456, bottom 562, page 1
- **Full page:** [pages/flyer105-page1-804eb6d28a.jpg (flyer page 1)](pages/flyer105-page1-804eb6d28a.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=1
- **Details:** confidence: 0.93 · item_key: `538dee3b3d3aeb11`
- **Raw:** `{"block_text": "TOP", "ocr_lines": ["TOP"]}`

— from flyer 105 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** DELETED — not a product. The "item" is a TOP DEAL badge over a struck-through regular price (4.08$/lb); no product identity survives in it. Boilerplate of the footer-phantom family.

### Item 11502

![item 11502](images/item-11502.jpg)

- **Name (English):** None
- **Name (French):** Fresh
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 6.59
- **Printed Price:** “6.59”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 266, top 404, right 305, bottom 454, page 1
- **Full page:** [pages/flyer105-page1-804eb6d28a.jpg (flyer page 1)](pages/flyer105-page1-804eb6d28a.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=1
- **Details:** confidence: 0.98 · item_key: `e2f6a3f5315e7244`
- **Raw:** `{"block_text": "Fresh", "ocr_lines": ["Fresh"], "harvest": {"unit": "kg", "via": "crop"}}`

— from flyer 105 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Kept, flagged. A descriptor-cell fragment ("Fresh" / SKU 52236 / 6.59$/kg) whose named parent row is not in the DB — it is the only trace of that product, so it stays for review (contrast 11509/11510, whose parents are present and which were deleted as duplicates).

### Item 11504

![item 11504](images/item-11504.jpg)

- **Name (English):** None
- **Name (French):** FRAIS
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 11.49
- **Printed Price:** “11.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 51, top 798, right 117, bottom 904, page 1
- **Full page:** [pages/flyer105-page1-804eb6d28a.jpg (flyer page 1)](pages/flyer105-page1-804eb6d28a.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=1
- **Details:** confidence: 0.81 · item_key: `fc977b5d110c64ee`
- **Raw:** `{"block_text": "Pio.\nFg", "ocr_lines": ["FRAIS"]}`

— from flyer 105 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Kept. "FRAIS" is a descriptor word, but this fragment carries a real product's sale price (11.49, reg. 21.99, visible in its crop) whose name cell didn't survive as an item. Unclassified.

### Item 11509

![item 11509](images/item-11509.jpg)

- **Name (English):** None
- **Name (French):** Fresh
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 16.51
- **Printed Price:** “16.51”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 28, top 723, right 68, bottom 774, page 2
- **Full page:** [pages/flyer105-page2-27e031b174.jpg (flyer page 2)](pages/flyer105-page2-27e031b174.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=2
- **Details:** confidence: 0.99 · item_key: `e2f6a3f5315e7244`
- **Raw:** `{"block_text": "Fresh,", "ocr_lines": ["Fresh"], "harvest": {"unit": "kg", "via": "crop"}}`

— from flyer 105 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** DELETED — duplicate fragment. "Fresh / 50111 / 16.51$/kg" is the descriptor cell of the Beef Bourguignon Cubes (item 11515, SKU 50111, whose headline price is 7.49/lb).

### Item 11510

![item 11510](images/item-11510.jpg)

- **Name (English):** None
- **Name (French):** Fresh
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 8.80
- **Printed Price:** “8.80”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 28, top 394, right 69, bottom 444, page 2
- **Full page:** [pages/flyer105-page2-27e031b174.jpg (flyer page 2)](pages/flyer105-page2-27e031b174.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=2
- **Details:** confidence: 0.92 · item_key: `e2f6a3f5315e7244`
- **Raw:** `{"block_text": "Fresh", "ocr_lines": ["Fresh"], "harvest": {"unit": "kg", "via": "crop"}}`

— from flyer 105 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** DELETED — duplicate fragment. "Fresh / 52048 / 8.80$/kg" is the descriptor cell of the Capicollo Pork (item 11514, SKU 52048, headline 3.99/lb).

### Item 11511

![item 11511](images/item-11511.jpg)

- **Name (English):** None
- **Name (French):** ELLESDECALMY SQUIDRINGS
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 6.49
- **Printed Price:** “6.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 707, top 471, right 872, bottom 564, page 2
- **Full page:** [pages/flyer105-page2-27e031b174.jpg (flyer page 2)](pages/flyer105-page2-27e031b174.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=2
- **Details:** confidence: 0.99 · item_key: `59b63008edb40635`
- **Raw:** `{"block_text": "ELLES pg CAL\nFi RINGS 4\nae", "ocr_lines": ["ELLESDECALMY", "SQUIDRINGS"]}`

— from flyer 105 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Price correct, name garbled. Wild-caught squid rings (454 g) at 6.49 (reg. 7.69) — verified on the crop ("RONDELLES DE CALMAR / SQUID RINGS" read as "ELLESDECALMY SQUIDRINGS"). Unclassified on the garble.

### Item 11520

![item 11520](images/item-11520.jpg)

- **Name (English):** None
- **Name (French):** Bianco di Napoli Fire-roasted crushed or diced
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 796 ml
- **Price:** 6.49
- **Printed Price:** “6.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 269, top 726, right 476, bottom 910, page 4
- **Full page:** [pages/flyer105-page4-e079076f03.jpg (flyer page 4)](pages/flyer105-page4-e079076f03.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=4
- **Details:** confidence: 0.99 · item_key: `a673408111e697c7`
- **Raw:** `{"block_text": "9\" OR DA\nBiancoldi po. 2 £: | Je D\nFire Coreg ele La 4]\npone DNA A\n\nice Grade + Qualité a à\nmms fanéea Griléesè | * =\nReg. price SS ES Dj NPA PY ni\nates Con wit if Bio ogiques\n*68Nic Crushéa i\ndim _. = era cam Om 4088 (", "ocr_lines": [" Bianco di Napoli", "Fire-roasted crushed or diced", "796 ml DiNAPqL", "hoppedT", "tates ConcasEesBioogiques", "Organic CrushedTom.toes"], "harvest": {"size": "796 ml", "via": "crop"}}`

— from flyer 105 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Price correct. Bianco di Napoli fire-roasted crushed tomatoes (796 ml) at 6.49 (reg. 7.99) — verified. Unclassified: the surviving name text is brand + English description without a "tomato" token (the word is on the can, not in the name block).

### Item 11533

![item 11533](images/item-11533.jpg)

- **Name (English):** None
- **Name (French):** GRILL-X
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 8.49
- **Printed Price:** “8.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 671, top 486, right 780, bottom 607, page 6
- **Full page:** [pages/flyer105-page6-1b95704e93.jpg (flyer page 6)](pages/flyer105-page6-1b95704e93.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=6
- **Details:** confidence: 0.98 · item_key: `5ce45e1f046251a9`
- **Raw:** `{"block_text": "GRILL-X |", "ocr_lines": ["GRILL-X"]}`

— from flyer 105 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Price correct, product noted. GRILL-X griddle and fryer cleaner at 8.49 (reg. 10.49) — verified. A commercial cleaning product, unclassified; kept for review under the standing rule.

### Item 11535

![item 11535](images/item-11535.jpg)

- **Name (English):** None
- **Name (French):** MAYRAND"
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 25.49
- **Printed Price:** “25.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 832, top 458, right 916, bottom 603, page 6
- **Full page:** [pages/flyer105-page6-1b95704e93.jpg (flyer page 6)](pages/flyer105-page6-1b95704e93.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=6
- **Details:** confidence: 0.99 · item_key: `9c7178d7a215f512`
- **Raw:** `{"block_text": "ET", "ocr_lines": ["MAYRAND\""]}`

— from flyer 105 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Price correct, product noted. Mayrand Chef hand soap with triclosan at 25.49 (reg. 29.99) — verified; the stored name is just the brand fragment. Household, unclassified; kept for review.

### Item 11536

![item 11536](images/item-11536.jpg)

- **Name (English):** None
- **Name (French):** Platinum
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 26.75
- **Printed Price:** “26.75”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 805, top 145, right 905, bottom 310, page 6
- **Full page:** [pages/flyer105-page6-1b95704e93.jpg (flyer page 6)](pages/flyer105-page6-1b95704e93.jpg)
- **Image source URL:** https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=6
- **Details:** confidence: 0.97 · item_key: `c345d6ce7310f303`
- **Raw:** `{"block_text": "Platinum", "ocr_lines": ["Platinum"]}`

**Item Review Analysis (Pass 1):** Price correct, product noted. Platinum paper towels (12 rolls) at 26.75 (reg. 29.99) — verified. Household, unclassified; kept for review.
