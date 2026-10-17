# Marché C&T — full product report

Store slug: `marche-c-t`. Generated from `data/grocery.db`. A sampled subset of 20 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 164, valid 2026-10-15 → 2026-10-21, 57 items across 4 pages; this is the St-Laurent store circular). The expired Oct 8–14 edition is correctly excluded.
- **Sample counts:** 10 classified + 10 unclassified shown. Names throughout are glued FR/EN stitches with "Reg:" fragments baked in — this store's OCR character.
- **The store's signature defect — the dual-rate trap:** page 1 prints every meat/produce price twice (a small $/kg line above the big $/lb badge), and the segmenter repeatedly stored the kg rate as the price. Six sampled items corrected to their lb headline: beef back ribs 4.39 → 3.99/lb, beef short ribs 14.53 → 6.59/lb, chicken drumsticks 4.39 → 1.99/lb, Chinese celery 1.50 → 1.59/lb, whole salmon 3.99 → 5.59/lb (its bbox and the "Reg:7.99" in its name both anchor the salmon, not the carangue below), mutton leg 12.11 → 5.49/lb.
- **Case prices are real here:** pages 2–3 sell produce and frozen goods by the case ("case/boîte") — nappa cabbage 25.99, Korean cabbage 15.99, spinach 30.99 and carrots (corrected 4.99 → 14.99) are per-case prices as printed; their units are now recorded as pack. The spinach deserves a line of its own: page 1 sells spinach at 1.59/lb, and this 30.99 item is a different, case-priced spinach on page 2 — verified on its crop before touching it.
- **Other corrections:** Rich Land cucumber jar 0.11 → 4.59 (a garbage value), Chin-Su fish sauce 5.99 → 1.99, Kopiko coffee 6.68 → 8.99. Left as found, with reasons on the items: the three-product grocery stitch (15614, priced 8.99 against three cells at 7.99/3.99/1.99 — no honest single correction), the pork-intestine fragment (15632, its badge is cut off in the crop), and the "EFRIGERATED" case item (15627, name is a packaging fragment; its 24.99 case price is as printed).
- **Fixes applied this pass:** 10 prices corrected; case units set on 4 items.

## Flyer 164 — valid 2026-10-15 → 2026-10-21 (10 classified items, 10 unclassified)

Source ref: `img-75e7de04218f5d52` · fetched 2026-10-17T05:46:28.721Z

### Item 15587

![item 15587](images/item-15587.jpg)

- **Name (English):** None
- **Name (French):** Reg:4.99 Cotes levees deboeuf Decongelé
- **Brand:** None
- **Category (English):** Meat > Beef
- **Category (French):** Viande > Bœuf
- **How classified:** guard-remap (`pork-ham`)
- **Size:** None
- **Price:** 14.53
- **Printed Price:** “14.53”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 711, top 195, right 961, bottom 265, page 1
- **Full page:** [pages/flyer164-page1-afaf565b17.jpg (flyer page 1)](pages/flyer164-page1-afaf565b17.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_2_5363436284931.jpg
- **Details:** confidence: 0.99 · item_key: `f31dae75205f2ccc`
- **Conditions:** `{"alt_prices": ["8.80"]}`
- **Raw:** `{"block_text": "a — | Rég:4.99\nCotes ‘levees.de) boeuf\nDécongelé' +=\nThawed;Beefishortiribs a", "ocr_lines": ["Reg:4.99", "Cotes levees deboeuf", "Decongelé", "ThawedBeefshortribs"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED — dual-rate trap. Beef short ribs print $14.53/kg small over a 6.59/lb badge; the DB stored the kg rate. Now 6.59/lb. Beef is right.

### Item 15589

![item 15589](images/item-15589.jpg)

- **Name (English):** None
- **Name (French):** Reg: 3.99 Pied de porc Decongele Thawed Pig's trotters
- **Brand:** None
- **Category (English):** Meat > Pork & Ham
- **Category (French):** Viande > Porc et jambon
- **How classified:** rule (`pork-ham`)
- **Size:** None
- **Price:** 1.59
- **Printed Price:** “1.59”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 450, top 197, right 688, bottom 286, page 1
- **Full page:** [pages/flyer164-page1-afaf565b17.jpg (flyer page 1)](pages/flyer164-page1-afaf565b17.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_2_5363436284931.jpg
- **Details:** confidence: 0.92 · item_key: `4a5217c0ae7c30bd`
- **Conditions:** `{"alt_prices": ["3.51"]}`
- **Raw:** `{"block_text": "|_Rég: 3.99\nPied deporc. Décongelé\nThawed Pig's trotters»", "ocr_lines": ["Reg: 3.99", "Pied de porc Decongele", "Thawed Pig's trotters"]}`

**Item Review Analysis (Pass 1):** Correct. Thawed pig's trotters at 1.59/lb ($3.51/kg) — the headline rate was stored correctly here. Pork & Ham is right.

### Item 15595

![item 15595](images/item-15595.jpg)

- **Name (English):** None
- **Name (French):** Celeri Chinoise Chinese
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 1.50
- **Printed Price:** “2/3.00”
- **Unit quantity:** 2.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 606, top 474, right 959, bottom 637, page 1
- **Full page:** [pages/flyer164-page1-afaf565b17.jpg (flyer page 1)](pages/flyer164-page1-afaf565b17.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_2_5363436284931.jpg
- **Details:** confidence: 0.92 · item_key: `c7e0bc9994453ca0`
- **Conditions:** `{"multibuy": {"count": 2, "total": 3.0}}`
- **Raw:** `{"block_text": "Céleri\n\nChinoise\n\nchinese\nsCelenyay", "ocr_lines": ["Celeri", "Chinoise", "Chinese", "Cmmese", "Celery"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED — dual-rate trap variant. Chinese celery prints 1.59/lb ($3.51/kg); the DB had 1.50. Now 1.59/lb. Fresh Vegetables is right.

### Item 15614

![item 15614](images/item-15614.jpg)

- **Name (English):** None
- **Name (French):** Feve de soja Vin de Cuissine Biscuit aux
- **Brand:** None
- **Category (English):** Beer & Wine > Wine
- **Category (French):** Bières et vins > Vins
- **How classified:** rule (`wine`)
- **Size:** None
- **Price:** 8.99
- **Printed Price:** “8.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 44, top 55, right 458, bottom 215, page 2
- **Full page:** [pages/flyer164-page2-c3cf323b35.jpg (flyer page 2)](pages/flyer164-page2-c3cf323b35.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_3_11041454222137.jpg
- **Details:** confidence: 0.86 · item_key: `8276fc79081681f2`
- **Raw:** `{"block_text": "Fève de soja “Vin de Cuissine Biscuit aux\nDunya Brand Soya | Tangsong Brand amandes\nBeans 10lb Shaoxing cookingwine Biscotti Almond\n\n| — chips 345g", "ocr_lines": ["Feve de soja", "Vin de Cuissine", "Biscuit aux", "Dunya Brand Soya", "Tangsong Brand", "amandes", "Beans 10lb", "Shaoxing cooking wine", "BiscottiAlmond", "chips 345g"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** LEFT AS FOUND. One item stitches three page-3 products (Dunya soya beans 7.99, Tangsong Shaoxing cooking wine 3.99, almond biscotti 1.99) into a single name and carries 8.99, which matches none of them. It classifies as Wine on the middle product. No honest single-price correction exists; recorded as a three-cell stitch.

### Item 15633

![item 15633](images/item-15633.jpg)

- **Name (English):** None
- **Name (French):** Chou coreen Korean Cabbage
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 15.99
- **Printed Price:** “15.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 331, top 717, right 494, bottom 842, page 4
- **Full page:** [pages/flyer164-page4-b7e53edaf4.jpg (flyer page 4)](pages/flyer164-page4-b7e53edaf4.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_4_4756009534970.jpg
- **Details:** confidence: 0.97 · item_key: `f818a020b067b8aa`
- **Raw:** `{"block_text": "Chou coréen\nKorean Cabbage", "ocr_lines": ["Chou coreen", "Korean Cabbage"]}`

**Item Review Analysis (Pass 1):** Correct as printed. Korean cabbage at 15.99 per case ("case/boîte") — verified on the crop; unit now recorded as pack. Fresh Vegetables is right.

### Item 15634

![item 15634](images/item-15634.jpg)

- **Name (English):** None
- **Name (French):** Estomac de porc congele FrozenButterfly
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Meat and Seafood
- **Category (French):** Produits surgelés > Viande et fruits de mer surgelés
- **How classified:** frozen-remap (`pork-ham`)
- **Size:** None
- **Price:** 2.29
- **Printed Price:** “2.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 576, top 383, right 798, bottom 502, page 4
- **Full page:** [pages/flyer164-page4-b7e53edaf4.jpg (flyer page 4)](pages/flyer164-page4-b7e53edaf4.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_4_4756009534970.jpg
- **Details:** confidence: 0.99 · item_key: `10b083677a4f1fcf`
- **Raw:** `{"block_text": "Estomac de\n\nporc congelé\nFrozen Butterfly\nstomach® . Ey", "ocr_lines": ["Estomac de", "porc congele", "FrozenButterfly", "stomach", "SINCE1997"]}`

**Item Review Analysis (Pass 1):** Correct. Frozen butterfly pork stomach at 2.29/lb (sold from 22 lb cases) — verified. Frozen Meat and Seafood is right.

### Item 15640

![item 15640](images/item-15640.jpg)

- **Name (English):** None
- **Name (French):** Chou chinois nappa Napa Cabbage
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 25.99
- **Printed Price:** “25.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 55, top 717, right 249, bottom 840, page 4
- **Full page:** [pages/flyer164-page4-b7e53edaf4.jpg (flyer page 4)](pages/flyer164-page4-b7e53edaf4.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_4_4756009534970.jpg
- **Details:** confidence: 0.99 · item_key: `5ee67815cbf092ab`
- **Raw:** `{"block_text": "Chou chinois nappa\nNapa Cabbage", "ocr_lines": ["Chou chinois nappa", "Napa Cabbage"]}`

**Item Review Analysis (Pass 1):** Correct as printed. Napa cabbage at 25.99 per case — verified; unit now pack. Fresh Vegetables is right.

### Item 15641

![item 15641](images/item-15641.jpg)

- **Name (English):** None
- **Name (French):** ea/ch Reg:12.99 Filet de pangasius
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** None
- **Price:** 2.50
- **Printed Price:** “2/5.00”
- **Unit quantity:** 2.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 770, top 159, right 968, bottom 334, page 4
- **Full page:** [pages/flyer164-page4-b7e53edaf4.jpg (flyer page 4)](pages/flyer164-page4-b7e53edaf4.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_4_4756009534970.jpg
- **Details:** confidence: 0.94 · item_key: `33defee201864e71`
- **Conditions:** `{"multibuy": {"count": 2, "total": 5.0}}`
- **Raw:** `{"block_text": "SD) =) Y ea/ch |\nES = fi Rég: 12.99\nFilet de pangasius\nBasa Fillet 400g", "ocr_lines": ["ea/ch", "Reg:12.99", "Filet de pangasius", "Basa Fillet 400g"]}`

**Item Review Analysis (Pass 1):** Correct derivation. Basa fillet (400 g) prints "2/5.00" (reg 2.99); the stored 2.50 is the per-unit split. (Its name absorbed the mussels' "Reg:12.99" line from the cell above.) Fish is right.

### Item 15642

![item 15642](images/item-15642.jpg)

- **Name (English):** None
- **Name (French):** Produitsdu Canada Epinards
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 30.99
- **Printed Price:** “30.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 308, top 820, right 485, bottom 970, page 4
- **Full page:** [pages/flyer164-page4-b7e53edaf4.jpg (flyer page 4)](pages/flyer164-page4-b7e53edaf4.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_4_4756009534970.jpg
- **Details:** confidence: 0.99 · item_key: `2ac90348c254b7bc`
- **Raw:** `{"block_text": "Épinards\nspins", "ocr_lines": ["Produitsdu", "Canada", "Epinards", "Spinach"]}`

**Item Review Analysis (Pass 1):** Correct as printed — checked carefully. This spinach is the page-2 case item at 30.99 per case, NOT the page-1 spinach at 1.59/lb. Unit now pack. Fresh Vegetables is right.

### Item 15643

![item 15643](images/item-15643.jpg)

- **Name (English):** None
- **Name (French):** Carotte Carrot
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 564, top 719, right 725, bottom 831, page 4
- **Full page:** [pages/flyer164-page4-b7e53edaf4.jpg (flyer page 4)](pages/flyer164-page4-b7e53edaf4.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_4_4756009534970.jpg
- **Details:** confidence: 0.99 · item_key: `9331bd6604fb6e92`
- **Raw:** `{"block_text": "Carotte\nCarrot", "ocr_lines": ["Carotte", "Carrot"]}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 164 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Carrots print 14.99 per case; the DB had 4.99. Unit now pack. Fresh Vegetables is right.

### Item 15586

![item 15586](images/item-15586.jpg)

- **Name (English):** None
- **Name (French):** CotesleveesdeBoeuf Decongele ThawedBeefBackRib
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 4.39
- **Printed Price:** “4.39”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 626, top 107, right 884, bottom 162, page 1
- **Full page:** [pages/flyer164-page1-afaf565b17.jpg (flyer page 1)](pages/flyer164-page1-afaf565b17.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_2_5363436284931.jpg
- **Details:** confidence: 0.99 · item_key: `5712e681ae695a70`
- **Raw:** `{"block_text": "Décor levées de Boeuf\nDécongeléh |\nThawed Beet Doce RDS", "ocr_lines": ["CotesleveesdeBoeuf", "Decongele", "ThawedBeefBackRib"]}`

— from flyer 164 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED — dual-rate neighbour. Beef back ribs print 3.99/lb ($8.80/kg); the DB stored 4.39, the pork eye-of-round's kg rate from the left. Now 3.99/lb. The glued name keeps it unclassified; its classified sibling (15587) is the short ribs.

### Item 15592

![item 15592](images/item-15592.jpg)

- **Name (English):** None
- **Name (French):** Reg: 8.99 Pilon depouletfrais Freshchicken drumstick
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 4.39
- **Printed Price:** “4.39”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 723, top 303, right 953, bottom 380, page 1
- **Full page:** [pages/flyer164-page1-afaf565b17.jpg (flyer page 1)](pages/flyer164-page1-afaf565b17.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_2_5363436284931.jpg
- **Details:** confidence: 0.98 · item_key: `7abd2ab00926c9d9`
- **Raw:** `{"block_text": "À Yee RS | Rég: 8.99\nPilon,de;poulet frais\nFresh chicken drumstick", "ocr_lines": ["Reg: 8.99", "Pilon depouletfrais", "Freshchicken drumstick"]}`

— from flyer 164 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED — dual-rate trap. Fresh chicken drumsticks print 1.99/lb ($4.39/kg); the DB stored the kg rate. Now 1.99/lb. The glued name keeps it unclassified.

### Item 15596

![item 15596](images/item-15596.jpg)

- **Name (English):** None
- **Name (French):** Jusqu'aepuisemen desstocks! Reg:7.99
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 31, top 281, right 227, bottom 386, page 1
- **Full page:** [pages/flyer164-page1-afaf565b17.jpg (flyer page 1)](pages/flyer164-page1-afaf565b17.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_2_5363436284931.jpg
- **Details:** confidence: 0.99 · item_key: `eee726eb250aa419`
- **Conditions:** `{"alt_prices": ["8.80"]}`
- **Raw:** `{"block_text": "Jusqu' à épuiseme iv D:\ndes stocks! Ib\noc Bl IE Rég:7.\nAE ee Reg:7-99-\nREA RUN Sr LT ST\nFCarangue” st),\nA = A Ne ae - Sy AG", "ocr_lines": ["Jusqu'aepuisemen", "desstocks!", "Reg:7.99", "Carangue", "JackFish"]}`

— from flyer 164 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop + bbox. The item's name is the "Jusqu'à épuisement des stocks!" tag plus "Reg:7.99" — both belong to the whole-salmon cell (5.59/lb, reg 7.99), which its bbox anchors; the stored 3.99 was the carangue's badge below. Now 5.59/lb.

### Item 15605

![item 15605](images/item-15605.jpg)

- **Name (English):** None
- **Name (French):** RICH LAND Whole Cucumher
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 0.11
- **Printed Price:** “4592/500.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 223, top 346, right 642, bottom 411, page 2
- **Full page:** [pages/flyer164-page2-c3cf323b35.jpg (flyer page 2)](pages/flyer164-page2-c3cf323b35.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_3_11041454222137.jpg
- **Details:** confidence: 0.94 · item_key: `3f9599c5c60d4dfa`
- **Conditions:** `{"multibuy": {"count": 4592, "total": 500.99}}`
- **Raw:** `{"block_text": null, "ocr_lines": ["RICH LAND", "Whole Cucumher"]}`

— from flyer 164 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Rich Land whole cucumber (pickles) prints 4.59 each; the DB had 0.11, a garbage value. The brand-only name keeps it unclassified.

### Item 15606

![item 15606](images/item-15606.jpg)

- **Name (English):** None
- **Name (French):** CHIN-S5F Thai Tu. an Thai Tu
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 52, top 522, right 167, bottom 573, page 2
- **Full page:** [pages/flyer164-page2-c3cf323b35.jpg (flyer page 2)](pages/flyer164-page2-c3cf323b35.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_3_11041454222137.jpg
- **Details:** confidence: 0.80 · item_key: `2fdba80a33c9d19d`
- **Raw:** `{"block_text": "} CuM-SU\" À | CMH-sU\"\n2 Vv g\n‘ t\nfe | le |\n|\nMB er MAL © “4", "ocr_lines": ["CHIN-S5F", "Thai Tu.", "an Thai Tu."], "harvest": {"unit": "each", "via": "crop"}}`

— from flyer 164 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Chin-Su fish sauce prints 1.99 each; the DB had 5.99. Name garble keeps it unclassified.

### Item 15609

![item 15609](images/item-15609.jpg)

- **Name (English):** None
- **Name (French):** BrownCoffee IMPROVEDTASTET
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 6.68
- **Printed Price:** “6.68”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 207, top 513, right 329, bottom 569, page 2
- **Full page:** [pages/flyer164-page2-c3cf323b35.jpg (flyer page 2)](pages/flyer164-page2-c3cf323b35.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_3_11041454222137.jpg
- **Details:** confidence: 0.95 · item_key: `574d5c06cc83f58f`
- **Raw:** `{"block_text": "Brown Co)\n\nGOW 2e\n\nture (COaS\n© IMPROVED TASTES à\n: STRONG, DI MAPAIT\n\n| FS", "ocr_lines": ["BrownCoffee", "IMPROVEDTASTET"], "harvest": {"unit": "each", "via": "crop"}}`

— from flyer 164 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Kopiko coffee (brown/black 3-in-1) prints 8.99 each; the DB had 6.68. Unclassified on the glued name.

### Item 15617

![item 15617](images/item-15617.jpg)

- **Name (English):** None
- **Name (French):** Real. Simple. Vrai. Simple. LEAF
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
- **bbox:** left 404, top 877, right 525, bottom 954, page 3
- **Full page:** [pages/flyer164-page3-5f7d5a3463.jpg (flyer page 3)](pages/flyer164-page3-5f7d5a3463.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_1_5481611045464.jpg
- **Details:** confidence: 0.99 · item_key: `8f29b716c603f42d`
- **Raw:** `{"block_text": "Real. Simple. À Vrai. Simple.\nLEAF\nLAZY MAPLE", "ocr_lines": ["Real. Simple.", "Vrai. Simple.", "LEAF", "NATURALBACONNATUREL", "LAZY MAPLE."], "harvest": {"unit": "each", "via": "crop"}}`

— from flyer 164 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Maple Leaf Natural bacon (Lazy Maple) at 2.99 each — verified; the stored name is the pack's slogan text ("Real. Simple. Vrai. Simple."), so it sits unclassified.

### Item 15625

![item 15625](images/item-15625.jpg)

- **Name (English):** None
- **Name (French):** ea/ch Reg:3.99 JambedeMouton
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 88g
- **Price:** 12.11
- **Printed Price:** “12.11”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 550, top 730, right 963, bottom 925, page 3
- **Full page:** [pages/flyer164-page3-5f7d5a3463.jpg (flyer page 3)](pages/flyer164-page3-5f7d5a3463.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_1_5481611045464.jpg
- **Details:** confidence: 0.99 · item_key: `f43990a1b0dfbfc9`
- **Conditions:** `{"alt_prices": ["1.99"]}`
- **Raw:** `{"block_text": "| 7 ear i ea/ch\nRég:3.58 | Rég:3.99 |\nJambon Forêt-Noir fumé/ Jambe de Mouton\npoitrine de dinde rôti au four Décongelé\n\nMaple Leaf Brand Smoked Black Thawed Mutton leg\n\nBlack forest Ham/Oven Roasted\n\nTey Breast 88g", "ocr_lines": ["ea/ch", "Reg:3.99", "JambedeMouton", "JambonForet-Noirfumel", "Decongele", "poitrine de dinderoti au four", "Thawed Mutton leg", "MapleLeafBrandSmokedBlack", "BlackforestHam/OvenRoasted", "TurkeyBreast88g"], "harvest": {"size": "88g", "via": "`

— from flyer 164 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED — dual-rate trap. Thawed mutton leg prints 5.49/lb ($12.11/kg); the DB stored the kg rate. Now 5.49/lb. The glued name keeps it unclassified.

### Item 15627

![item 15627](images/item-15627.jpg)

- **Name (English):** None
- **Name (French):** EFRIGERATED
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 24.99
- **Printed Price:** “24.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 836, top 650, right 931, bottom 685, page 4
- **Full page:** [pages/flyer164-page4-b7e53edaf4.jpg (flyer page 4)](pages/flyer164-page4-b7e53edaf4.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_4_4756009534970.jpg
- **Details:** confidence: 0.99 · item_key: `ab2e01f3603ce5fa`
- **Raw:** `{"block_text": "Be OF CANS £\nÉFRIGERATET)", "ocr_lines": ["EFRIGERATED"]}`

— from flyer 164 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Left as found. The name is a box fragment ("…REFRIGERATED") and the item is a 24.99 case of greens — the case price is as printed; the product itself is not identifiable from the fragment.

### Item 15632

![item 15632](images/item-15632.jpg)

- **Name (English):** None
- **Name (French):** Intestin dePorc Congele FrozenPorkIntestine
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 22lb
- **Price:** 2.79
- **Printed Price:** “2.79”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 340, top 382, right 564, bottom 493, page 4
- **Full page:** [pages/flyer164-page4-b7e53edaf4.jpg (flyer page 4)](pages/flyer164-page4-b7e53edaf4.jpg)
- **Image source URL:** https://d280crdu6dot2n.cloudfront.net/flyers/C_T_St-Laurent_fr_4_4756009534970.jpg
- **Details:** confidence: 0.89 · item_key: `d4e4827f7fa5f0ce`
- **Raw:** `{"block_text": "Intestin de Porc\nCongelé / ss\nFrozen santas", "ocr_lines": ["Intestin dePorc", "Congele", "FrozenPorkIntestine"], "harvest": {"size": "22lb", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Left as found. Frozen pork intestine (22 lb cases); its own badge is cut off at the crop's right edge and the visible 2.79/lb belongs to the chicken box at the left — the stored 2.79 cannot be confirmed or refuted from the crop.
