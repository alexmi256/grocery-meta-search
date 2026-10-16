# Akhavan — full product report

Store slug: `akhavan`. Generated from `data/grocery.db`. Every item stored for this store, with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).

## Image audit (2026-10-16)

The wrong/weird crops in the earlier review documents were a bug in the reporting code, not in the stored data: OCR bounding boxes are stored normalized to a 1000×1000 scale (`ocr/segment.py`), and the crop code treated them as raw pixels, displacing every crop toward the top-left. Fixed in `classify/review.py` (`_crop` now denormalizes; regression tests in `tests/test_review_crop.py`).

All 19 crops below were visually checked against the flyer page: **19/19 show the correct product.** Notes:

- Flyer layout merges several products per cell, so some crops include a neighbour (items 9768, 9769, 9782, 9784); the named product is in frame in every case.
- Items 9774 and 9782: the item's own price falls just outside the crop (bbox sits slightly high); the product itself is in frame.
- Separate OCR data defects (not image problems): several prices are wrong — 99¢ items stored as price `99` (9774, 9775, 9776, 9777, 9781), item 9772 stored 1.49 vs printed 4.49/lb, and items 9778/9779/9786 carry a neighbouring product's price. Names are likewise merged/noisy on multi-product cells (9768, 9769).

Akhavan's only stored edition is Oct 7–13: circulaires.club listed no newer Akhavan edition at the Oct 16 refresh.

## Flyer 58 — valid 2026-10-07 → 2026-10-13 (19 items)

Source ref: `circulaire-akhavan-du-7-au-13-octobre-2026` · fetched 2026-10-13T15:01:25.805Z

### Item 9768 — KASHK (CORNICHONS AL’AIL!| CORNICHON MÉLANGÉ SOMAYEHMN HYDERABADI MEHRAN (= MEHRAN KASHK ‘GARLIC HYDERABADI PICKLE MIXED HYDERABADI PICKLE

![item 9768](images/item-9768.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 4.99 $ · as printed: “4.99” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 258, top 565, right 662, bottom 661, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `661124116cbec3cc`
- **Raw:** `{"block_text": "| KASHK (CORNICHONS AL’AIL!| CORNICHON MÉLANGÉ\nSOMAYEHMN HYDERABADI MEHRAN (= MEHRAN\nKASHK ‘GARLIC HYDERABADI PICKLE MIXED HYDERABADI PICKLE\n\nAnn ET. | RANA eg ee AANn n", "ocr_lines": ["CORNICHONSAL'AIL", "CORNICHON MELANGE", "KASHK", "SOMAYEH", "HYDERABADI MEHRAN", "KASHK", "GARLICHYDERABADIPICKLE", "MIXED HYDERABADIPICKLE"]}`

### Item 9769 — = MÉLANGE D'ÉPICESMN CURRY.EN POUDRE DE = | HALEEM MADRAS SHIP —— MEHRAN URRY POWDER MADRAS fo ZODN HALEEM MIX 500g

![item 9769](images/item-9769.jpg)

- **Category:** Pantry > Spices & Seasonings (FR: Produits du garde-manger > Épices et assaisonnements)
- **How classified:** rule (`spices`)
- **Price:** 99.66 $ · as printed: “99.66” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 623, top 671, right 995, bottom 773, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `7a54eed18e892ebe`
- **Raw:** `{"block_text": "= MÉLANGE D'ÉPICESMN CURRY.EN POUDRE DE\n\n= | HALEEM MADRAS SHIP\n\n—— MEHRAN URRY POWDER MADRAS\n\nfo ZODN HALEEM MIX 500g\n, EN ao", "ocr_lines": ["CURRY EN POUDREDE", "MELANGED'EPICES", "MADRASSHIP", "HALEEM", "CURRY POWDER MADRAS", "MEHRAN", "HALEEMMIX"]}`

### Item 9770 — RHARICOTS ROMAINS NORGE:PERLÉE AKHAVAN Gal AKHAVAN La » PEARLED BARLEY M BEANSN |= * 1 750g

![item 9770](images/item-9770.jpg)

- **Category:** Pantry > Dried Beans, Vegetables & Grains (FR: Produits du garde-manger > Haricots secs, légumes et grains)
- **How classified:** rule (`beans-grains`)
- **Price:** 66.00 $ · as printed: “66” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 36, top 305, right 330, bottom 389, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `1631cae6265b2184`
- **Raw:** `{"block_text": "RHARICOTS ROMAINS NORGE:PERLÉE AKHAVAN\nGal AKHAVAN La » PEARLED BARLEY\nM BEANSN |= * 1 750g\nMERS 4 SD son 4 Re NE", "ocr_lines": ["HARICOTSROMAINS", "ORGEPERLEEAKHAVAN", "AKHAVAN", "PEARLEDBARLEY", "ROMANO BEANS"]}`

### Item 9771 — MELANGE || CONFITURE DE CARROT| MEHRAN 181| BADI PICKLE M }f x à CARROT JAM QAN = CP, 260 a

![item 9771](images/item-9771.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.99 $ · as printed: “1.99” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 592, top 566, right 827, bottom 658, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `b9e3ae12ef646441`
- **Raw:** `{"block_text": "MELANGE || CONFITURE DE CARROT|\nMEHRAN 181|\nBADI PICKLE M }f x à CARROT JAM\nQAN = CP, 260 a", "ocr_lines": ["CONFITUREDECARROT", "MEHRAN", "CARROTJAM"]}`

### Item 9772 — CORÉGONE DE LAC CANADIEN CANADIAN LAKE WHITEFISH

![item 9772](images/item-9772.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.49 $ · as printed: “1.49” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 14, top 731, right 165, bottom 815, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.89 · item_key: `c710ee7484feb58a`
- **Raw:** `{"block_text": "Le pe\nSa CH\nCORÉGONE DE LAC\nCANADIEN\n\nCANADIAN LAKE WHITEFISH", "ocr_lines": ["AKHAYAN", "COREGONEDELAC", "CANADIEN", "CANADIANLAKEWHITEFISH"]}`

### Item 9773 — MAHLAB EN POUDRE

![item 9773](images/item-9773.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.49 $ · as printed: “3.49” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 685, top 249, right 828, bottom 332, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `5fb274f539b33908`
- **Raw:** `{"block_text": "MAHLAB EN POUDRE\n\nvate | AKHAVAN\n| _ = MAHLAB POWDER\n4 Ai at ù 1009\n| an", "ocr_lines": ["MAHLABENPOUDRE", "AKHAVAN", "AKHAVAN", "MAHLABPOWDER", "MAHILAB"]}`

### Item 9774 — BLENTILLES ROUGES MENTIÈRES AKHAVAN ls WHOLE RED LENTILS

![item 9774](images/item-9774.jpg)

- **Category:** Pantry > Dried Beans, Vegetables & Grains (FR: Produits du garde-manger > Haricots secs, légumes et grains)
- **How classified:** rule (`beans-grains`)
- **Price:** 99.00 $ · as printed: “99” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 289, top 304, right 497, bottom 391, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `1e9b51f6230a3e8c`
- **Raw:** `{"block_text": "BLENTILLES ROUGES\nMENTIÈRES AKHAVAN\nls WHOLE RED LENTILS\nBOER Pep ae) 600 a", "ocr_lines": ["LENTILLES ROUGES", "ENTIERESAKHAVAN", "WHOLEREDLENTILS"]}`

### Item 9775 — VINAIGRE DE DATTES

![item 9775](images/item-9775.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 99.00 $ · as printed: “99” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 851, top 567, right 994, bottom 651, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `e3eff09b0f0c6c9b`
- **Raw:** `{"block_text": "DE a a\nVINAIGRE DE DATTES\ns 1&1|\n\nA DATE VINEGAR\n\n330 mi", "ocr_lines": ["VINAIGREDEDATTES", "DATEVINEGAR"]}`

### Item 9776 — DATES MARIE gMAZAFAT DATE ORGANIC

![item 9776](images/item-9776.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 99.00 $ · as printed: “99” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 521, top 626, right 824, bottom 710, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `2c131df8aba05738`
- **Raw:** `{"block_text": "DATES MARIE\ngMAZAFAT DATE ORGANIC\nB50 0", "ocr_lines": ["DATESMAZAFATI", "EMTIAZ", "MAZAFATI DATEORGANIC"]}`

### Item 9777 — AUS DE NAVET FORT a DOGANAY HOT TURNIP JUICE

![item 9777](images/item-9777.jpg)

- **Category:** Drinks > Juice (FR: Boissons > Jus)
- **How classified:** rule (`juice`)
- **Price:** 99.00 $ · as printed: “99” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 354, top 625, right 497, bottom 709, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `b3810c116f562cac`
- **Raw:** `{"block_text": "AUS DE NAVET FORT\na DOGANAY\nHOT TURNIP JUICE\n\n11", "ocr_lines": ["JUSDENAVETFORT", "DOGANAY", "HOTTURNIPJUICE"]}`

### Item 9778 — OGNIONS| ONIONS)

![item 9778](images/item-9778.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 5.99 $ · as printed: “5.99” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 920, top 719, right 999, bottom 805, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `fe1c929ab54d26d1`
- **Raw:** `{"block_text": "OGNIONS|\nONIONS)\n10 Ihe", "ocr_lines": ["OGNIONS", "ONIONS"]}`

### Item 9779 — CÔTES LEVÉES 4 D'AGNEAU | \\ SALAM RBs

![item 9779](images/item-9779.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 6.68 $ · as printed: “6.68” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 91, top 779, right 329, bottom 880, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `3d972adcccd7af05`
- **Raw:** `{"block_text": "CÔTES LEVÉES\n4 D'AGNEAU\n| \\\\ SALAM RBs", "ocr_lines": ["COTESLEVEES", "D'AGNEAU", "LAMBRIBS"]}`

### Item 9780 — ft SIROP DE MENTHE = KAMBIZ}

![item 9780](images/item-9780.jpg)

- **Category:** Fruits & Vegetables > Herbs (FR: Fruits et légumes > Fines herbes)
- **How classified:** rule (`herbs-fresh`)
- **Price:** 3.99 $ · as printed: “3.99” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 851, top 457, right 997, bottom 552, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `b385838562b12033`
- **Raw:** `{"block_text": "ft SIROP DE MENTHE\n= KAMBIZ}\n(SEKANJEBIN MINT svaur|", "ocr_lines": ["SIROP DEMENTHE", "KAMBIZ", "SEKANJEBIN MINTSYRUP"]}`

### Item 9781 — FENUGREC AKHAVAN FENUGREEK

![item 9781](images/item-9781.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 99.00 $ · as printed: “99” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 754, top 353, right 828, bottom 437, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `a79a10431ce6fd20`
- **Raw:** `{"block_text": "FENUGREC\nAKHAVAN\nFENUGREEK |\n400", "ocr_lines": ["FENUGREC", "AKHAVAN", "FENUGREEK"]}`

### Item 9782 — PRUNE HAJ a ‘ QUES HAJ HASSANI

![item 9782](images/item-9782.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.99 $ · as printed: “2.99” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 854, top 305, right 995, bottom 390, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `089dcd691a7124fc`
- **Raw:** `{"block_text": "PRUNE HAJ a\n‘ QUES HAJ HASSANI", "ocr_lines": ["PRUNE HAJ HASSANI", "AKHAVAN", "PRUNES HAJ HASSANI"]}`

### Item 9783 — RIT RES ANA RE | EAU DES CHICOREE | ? TUBA à CHICORY WATER

![item 9783](images/item-9783.jpg)

- **Category:** Drinks > Water (FR: Boissons > Eau)
- **How classified:** rule (`water`)
- **Price:** 66.00 $ · as printed: “66” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 699, top 413, right 993, bottom 499, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `0c6321276588d405`
- **Raw:** `{"block_text": "RIT RES ANA RE |\nEAU DES CHICOREE |\n? TUBA\nà CHICORY WATER |\n4\" | 300 mi", "ocr_lines": ["EAUDESCHICOREE", "TUBA", "CHICORYWATER"]}`

### Item 9784 — GRENOBLE NOIX:

![item 9784](images/item-9784.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 1.99 $ · as printed: “1.99” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 57, top 625, right 165, bottom 709, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `c0d2ed924d68e63d`
- **Raw:** `{"block_text": "GRENOBLE NOIX:\nte AKHAVAN\ntg WALNUTS", "ocr_lines": ["GRENOBLENOIX", "AKHAVAN", "WALNUTS"]}`

### Item 9785 — PATATES| | POTATOES,

![item 9785](images/item-9785.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 3.99 $ · as printed: “3.99” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 767, top 780, right 993, bottom 864, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `b2e4e43234400985`
- **Raw:** `{"block_text": "PATATES| |\nPOTATOES,", "ocr_lines": ["PATATES", "POTATOES"]}`

### Item 9786 — BETTERAVES | e0%, BEETS

![item 9786](images/item-9786.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 3.99 $ · as printed: “3.99” · unit: —
- **Item validity:** 2026-10-07 → 2026-10-13
- **bbox:** left 577, top 780, right 830, bottom 868, page 1
- **Full page:** [pages/flyer58-page-1960aca5a9.jpg (flyer page 1)](pages/flyer58-page-1960aca5a9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-akhavan-du-7-au-13-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `324575459c1c00ee`
- **Raw:** `{"block_text": "BETTERAVES |\ne0%, BEETS\nHo >", "ocr_lines": ["BETTERAVES", "BEETS"]}`
