# Wholesale Club — full product report

Store slug: `wholesale-club`. Generated from `data/grocery.db`. A sampled subset of 20 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 172, valid 2026-10-15 → 2026-10-21, 77 items). The expired Oct 8–14 flyer (93 items) is correctly excluded.
- **Sample counts:** 10 classified + 10 unclassified shown.
- **Issues found:** this flyerify OCR flyer prints big blue prices at each cell's edge, "était" was-price badges, and PC Optimum points promos — and the capture confuses all three. Six fixes: the assorted Hershey's/Reese's 100-count bags stored the piece count as a 1.00 price (theirs: 14.99); the Sunspun sausages stored 20.00, assembled from the "OBTENEZ 2 000 pts" points badge on a price-less brand page — price cleared to none; a nameless item stored 1.47, the derived unit of a "15/22$ ou 1,99 ch." multibuy — restored to the printed 1.99 single price with the multibuy recorded; the Flamingo wings were captured twice (59.99 correctly, and again with the Frank's RedHot neighbour's 15.99) — the duplicate is deleted; and two records are pure badge phantoms (a was-price badge plus a "Fabriqué/Préparé au Canada" leaf, no product) — deleted. The genuine bulk prices verify (Hafner 2.4 kg cake 49.99, Maripesca cod loins 56.99, Kurkure 30-case 41.99).
- **Fixes applied this pass:** 16282 → 14.99; 16298 price → none (points phantom); 16352 → 1.99 + multibuy {15, 22.0}; items 16273, 16278, 16317 deleted.

## Flyer 172 — valid 2026-10-15 → 2026-10-21 (10 classified items, 10 unclassified)

Source ref: `wholesale-club-qc-flyer-october-15-to-21` · fetched 2026-10-17T06:46:21.864Z

### Item 16271

![item 16271](images/item-16271.jpg)

- **Name (English):** None
- **Name (French):** BARRES DE CHOCOLAT INDIVIDUELLES NESTLÉ CERTAINES VARIÉTÉS, 24 UN,
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** guard-remap (`specific-protein-bars`)
- **Size:** 24UN
- **Price:** 23.99
- **Printed Price:** “23.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 138, top 630, right 878, bottom 672, page 2
- **Full page:** [pages/flyer172-page2-989d8dc41a.jpg (flyer page 2)](pages/flyer172-page2-989d8dc41a.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-2-max.jpg
- **Details:** confidence: 0.90 · item_key: `8376dc6f431b82a0`
- **Raw:** `{"block_text": "BARRES DE CHOCOLAT INDIVIDUELLES\nNESTLÉ\nCERTAINES VARIÉTÉS, 24 UN,", "ocr_lines": ["BARRESDECHOCOLAT INDIVIDUELLES", "CERTAINESVARIETES.24 UN."], "harvest": {"size": "24UN", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Nestlé single chocolate bars (24 count) at 23.99 — verified. Candy & Chocolate is right.

### Item 16279

![item 16279](images/item-16279.jpg)

- **Name (English):** None
- **Name (French):** 4 BARRES DE CHOCOLAT OU CONFISERIES GRAND FORMAT HERSHEY'S, OH HENRY! OU REESE'S CERTAINES VARIETES, 16-24 UN. CHOCOLATE OR CANDY
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** guard-remap (`specific-protein-bars`)
- **Size:** 16-24 UN
- **Price:** 14.99
- **Printed Price:** “14.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 264, top 709, right 659, bottom 766, page 5
- **Full page:** [pages/flyer172-page5-3cd5ada473.jpg (flyer page 5)](pages/flyer172-page5-3cd5ada473.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-5-max.jpg
- **Details:** confidence: 0.96 · item_key: `fd29a5f2831f7adf`
- **Raw:** `{"block_text": "4 BARRES DE CHOCOLAT OU\nCONFISERIES GRAND FORMAT\nHERSHEY'S, OH HENRY! OU REESE'S\nCERTAINES VARIETES, 16-24 UN.\nCHOCOLATE OR CANDY", "ocr_lines": ["BARRES DECHOCOLAT OU", "CONFISERIESGRANDFORMAT", "HERSHEY'S,OHHENRYIOUREESE'S", "CERTAINESVARIETES.16-24UN.", "CHOCOLATEOR CANDY"]}`

**Item Review Analysis (Pass 1):** Correct. Hershey's / Oh Henry! / Reese's king-size bars or candy (16-24 count) at 14.99 +tx — verified on its own badge (the same 14.99 prints under the neighbouring assorted-bags cell, item 16282). Candy & Chocolate is right.

### Item 16282

![item 16282](images/item-16282.jpg)

- **Name (English):** None
- **Name (French):** CHOCOLATS OU FRIANDISES ASSORTIS HERSHEY'S OU REESE'S CERTAINES VARIETES
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 1.02kg
- **Price:** 1.00
- **Printed Price:** “1.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 614, top 595, right 925, bottom 761, page 5
- **Full page:** [pages/flyer172-page5-3cd5ada473.jpg (flyer page 5)](pages/flyer172-page5-3cd5ada473.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-5-max.jpg
- **Details:** confidence: 0.99 · item_key: `b51b2606a89e21eb`
- **Conditions:** `{"alt_prices": ["1.00"]}`
- **Raw:** `{"block_text": "CHOCOLATS OU\nFRIANDISES ASSORTIS\nHERSHEY'S OU REESE'S\nCERTAINES VARIETES\n909/962 G\n\nASSORTED CHOCOLATES\n21668235 EA/21736093 EA", "ocr_lines": ["CHOCOLATS OU", "FRIANDISES ASSORTIS", "HERSHEY'SOU REESE'S", "CERTAINESVARIETES", "ASSORTED CHOCOLATES", "21668235_EA/21736093 EA"], "harvest": {"size": "1.02kg", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 5. Hershey's or Reese's assorted chocolates (100-count bags, 909/962 g) print 14.99 +tx; the DB had 1.00 — the piece count read as a price. Candy & Chocolate is right.

### Item 16288

![item 16288](images/item-16288.jpg)

- **Name (English):** None
- **Name (French):** BARRES a DE CHOCOLAT & NESTLE Le CERTAINES VARIÉTÉS, 95 - 105 G CHOCOLATE BARS
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** guard-remap (`specific-protein-bars`)
- **Size:** 95 - 105 G
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 663, top 660, right 937, bottom 726, page 7
- **Full page:** [pages/flyer172-page7-b95fb1847d.jpg (flyer page 7)](pages/flyer172-page7-b95fb1847d.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-7-max.jpg
- **Details:** confidence: 0.97 · item_key: `9ca8479c3492dece`
- **Conditions:** `{"alt_prices": ["13.88"]}`
- **Raw:** `{"block_text": "BARRES a\n\nDE CHOCOLAT &\n\nNESTLE Le\n\nCERTAINES VARIÉTÉS, 95 - 105 G\nCHOCOLATE BARS", "ocr_lines": ["BARRES", "DE CHOCOLAT", "NESTLE", "CERTAINESVARIETES,95-105G", "CHOCOLATE BARS"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Nestlé chocolate bars (95-105 g) at 2.99 — verified. Candy & Chocolate is right.

### Item 16298

![item 16298](images/item-16298.jpg)

- **Name (English):** None
- **Name (French):** SAUCISSES À DÉJEUNER SUNSPUN” CERTAINES VARIETES SURGELEES, 5 KG BREAKFAST SAUSAGES
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Meat and Seafood
- **Category (French):** Produits surgelés > Viande et fruits de mer surgelés
- **How classified:** frozen-remap (`sausages`)
- **Size:** 5 KG
- **Price:** 20.00
- **Printed Price:** “20.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 79, top 187, right 230, bottom 304, page 9
- **Full page:** [pages/flyer172-page9-156b6ac125.jpg (flyer page 9)](pages/flyer172-page9-156b6ac125.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-9-max.jpg
- **Details:** confidence: 0.99 · item_key: `ba605de8f33c2d29`
- **Raw:** `{"block_text": "SAUCISSES À DÉJEUNER\nSUNSPUN”\nCERTAINES VARIETES\nSURGELEES, 5 KG\nBREAKFAST SAUSAGES", "ocr_lines": ["SAUCISSESA DEJEUNER", "SUNSPUN\"", "CERTAINESVARIETES", "SURGELEES,5KG", "BREAKFASTSAUSAGES"]}`

**Item Review Analysis (Pass 1):** PRICE CLEARED — points phantom. Sunspun frozen breakfast sausages (5 kg) appear on a Sunspun brand page whose offer is "OBTENEZ 2 000 pts" (PC Optimum); no dollar price prints for them. The stored 20.00 was assembled from the 2 000 points. Price now none, honestly. Frozen Meat and Seafood is right.

### Item 16302

![item 16302](images/item-16302.jpg)

- **Name (English):** None
- **Name (French):** BAGELS SANS NOM” CERTAINES VARIÉTÉS
- **Brand:** None
- **Category (English):** Bakery > Bagels, Croissants & English Muffins
- **Category (French):** Boulangerie > Bagels, croissants et muffins anglais
- **How classified:** rule (`bagels-croissants`)
- **Size:** 6UN
- **Price:** 4.49
- **Printed Price:** “4.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 562, top 880, right 794, bottom 929, page 10
- **Full page:** [pages/flyer172-page10-e17f328438.jpg (flyer page 10)](pages/flyer172-page10-e17f328438.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-10-max.jpg
- **Details:** confidence: 0.94 · item_key: `00b8f2670b282b13`
- **Conditions:** `{"alt_prices": ["2.29"]}`
- **Raw:** `{"block_text": "BAGELS\n\nSANS NOM”\nCERTAINES VARIÉTÉS\n6 UN.\n\nBAGELS\n\n21217965 EA/21217970 EA", "ocr_lines": ["BAGELS", "SANSNOM", "CERTAINESVARIETES", "BAGELS", "21217965EA/21217970EA"], "harvest": {"size": "6UN", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. No Name bagels (6 count) at 4.49 — verified. Bagels is right.

### Item 16329

![item 16329](images/item-16329.jpg)

- **Name (English):** None
- **Name (French):** FÈVES GERMÉES
- **Brand:** None
- **Category (English):** Pantry > Dried Beans, Vegetables & Grains
- **Category (French):** Produits du garde-manger > Haricots secs, légumes et grains
- **How classified:** rule (`beans-grains`)
- **Size:** None
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 268, top 413, right 501, bottom 457, page 13
- **Full page:** [pages/flyer172-page13-77b7c43418.jpg (flyer page 13)](pages/flyer172-page13-77b7c43418.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-13-max.jpg
- **Details:** confidence: 0.91 · item_key: `dd56544e46beef84`
- **Raw:** `{"block_text": "FÈVES GERMÉES\nPRODUIT DU QUÉBEC\n370 G\n\nBEAN SPROUTS", "ocr_lines": ["FEVES GERMEES", "PRODUIT DU QUEBEC", "BEAN SPROUTS"]}`

**Item Review Analysis (Pass 1):** Correct price. Bean sprouts (Québec, 370 g) at 4.99 — verified. (Shelved under Dried Beans on "fèves"; the product is fresh sprouts — a text result.)

### Item 16335

![item 16335](images/item-16335.jpg)

- **Name (English):** None
- **Name (French):** GÂTEAU TOURBILLON VANILLE ET CARAMEL HAFNER SURGELÉ, 2,4 KG VANILLA CARAMEL SWIRL CAKE
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Bakery & Breakfast
- **Category (French):** Produits surgelés > Boulangerie et déjeuner surgelés
- **How classified:** frozen-remap (`cakes`)
- **Size:** 2,4 KG
- **Price:** 49.99
- **Printed Price:** “49.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 396, top 879, right 714, bottom 928, page 14
- **Full page:** [pages/flyer172-page14-3c36e46662.jpg (flyer page 14)](pages/flyer172-page14-3c36e46662.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-14-max.jpg
- **Details:** confidence: 0.98 · item_key: `22e0d87929206743`
- **Conditions:** `{"alt_prices": ["34.99"]}`
- **Raw:** `{"block_text": "GÂTEAU TOURBILLON\n\nVANILLE ET CARAMEL\n\nHAFNER\n\nSURGELÉ, 2,4 KG\n\nVANILLA CARAMEL SWIRL CAKE", "ocr_lines": ["GATEAU TOURBILLON", "VANILLEET CARAMEL", "HAFNER", "SURGELE,2.4KG", "VANILLA CARAMEL SWIRLCAKE"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Hafner frozen vanilla-caramel swirl cake (2.4 kg) at 49.99 — verified; a foodservice-size cake at a real bulk price. Frozen Bakery & Breakfast is right.

### Item 16343

![item 16343](images/item-16343.jpg)

- **Name (English):** None
- **Name (French):** FRIANDISES KINDER BUENO CERTAINES VARIÉTÉS
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`specific-chocolate-eggs`)
- **Size:** 20 UN
- **Price:** 13.99
- **Printed Price:** “13.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 397, top 465, right 644, bottom 513, page 15
- **Full page:** [pages/flyer172-page15-dc56f6e922.jpg (flyer page 15)](pages/flyer172-page15-dc56f6e922.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-15-max.jpg
- **Details:** confidence: 0.95 · item_key: `3e1f36730212a016`
- **Conditions:** `{"alt_prices": ["1.20", "23.99"]}`
- **Raw:** `{"block_text": "FRIANDISES\n\nKINDER BUENO\nCERTAINES VARIÉTÉS\n20 UN.\n\nBUENO", "ocr_lines": ["FRIANDISES", "KINDER BUENO", "CERTAINESVARIETES", "BUENO"], "harvest": {"size": "20 UN", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Kinder Bueno treats (20 count) at 13.99 — verified. Candy & Chocolate is right.

### Item 16346

![item 16346](images/item-16346.jpg)

- **Name (English):** None
- **Name (French):** POUDRE POUR THÉ GLACÉ MIO CERTAINES VARIÉTÉS, 540 G ICED TEA POWDER
- **Brand:** None
- **Category (English):** Drinks > Tea & Hot Drinks
- **Category (French):** Boissons > Thés et boissons chaudes
- **How classified:** rule (`tea-hot-drinks`)
- **Size:** 540 G
- **Price:** 13.99
- **Printed Price:** “13.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 376, top 293, right 684, bottom 336, page 16
- **Full page:** [pages/flyer172-page16-671c2b2bd7.jpg (flyer page 16)](pages/flyer172-page16-671c2b2bd7.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-16-max.jpg
- **Details:** confidence: 0.96 · item_key: `03e53f8feddb7f84`
- **Raw:** `{"block_text": "POUDRE POUR THÉ GLACÉ\nMIO\n\nCERTAINES VARIÉTÉS, 540 G\nICED TEA POWDER", "ocr_lines": ["POUDRE POUR THE GLACE", "MIO", "CERTAINESVARIETES,540G", "ICED TEAPOWDER"], "harvest": {"unit": "each", "via": "crop"}}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 172 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Mio iced-tea powder (540 g) at 13.99 +tx — verified. Tea & Hot Drinks is right.

### Item 16273

![item 16273](images/item-16273.jpg)

- **Name (English):** None
- **Name (French):** KEN WINGS
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 4KG
- **Price:** 15.99
- **Printed Price:** “15.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 278, top 355, right 662, bottom 414, page 4
- **Full page:** [pages/flyer172-page4-47ab4a8b63.jpg (flyer page 4)](pages/flyer172-page4-47ab4a8b63.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-4-max.jpg
- **Details:** confidence: 0.99 · item_key: `0d4b8c8b9d4c2def`
- **Raw:** `{"block_text": "PP Naa Le but\n\nCERT, > | T fe\n=e ml facies one DCS es ES.\nKEN WINGS", "ocr_lines": ["AILESDEPOULET", "FLAMINGO", "CERTAINESVARIETES", "SURGELEES,ENTIEREMENT CUITES", "CHICKEN WINGS"], "harvest": {"size": "4KG", "via": "crop"}}`

— from flyer 172 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** DELETED — duplicate capture of the Flamingo chicken wings (same SKU 20798904_C01 as item 16275) carrying the Frank's RedHot neighbour's 15.99. The wings are properly carried by 16275 at the printed 59.99.

### Item 16275

![item 16275](images/item-16275.jpg)

- **Name (English):** None
- **Name (French):** PREPARE A
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 4KG
- **Price:** 59.99
- **Printed Price:** “59.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 76, top 367, right 476, bottom 462, page 4
- **Full page:** [pages/flyer172-page4-47ab4a8b63.jpg (flyer page 4)](pages/flyer172-page4-47ab4a8b63.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-4-max.jpg
- **Details:** confidence: 0.96 · item_key: `49567ecb7e02085d`
- **Raw:** `{"block_text": "PREPARE A", "ocr_lines": ["PREPAREAU", "CANADA"], "harvest": {"size": "4KG", "via": "crop"}}`

— from flyer 172 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Flamingo frozen fully-cooked chicken wings (4 kg) at 59.99 — verified on page 4; the stored name is a fragment of the cell's "PRÉPARÉ AU CANADA" leaf. Unclassified.

### Item 16276

![item 16276](images/item-16276.jpg)

- **Name (English):** None
- **Name (French):** MEGA
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 24.96
- **Printed Price:** “24.96”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 550, top 483, right 672, bottom 495, page 4
- **Full page:** [pages/flyer172-page4-47ab4a8b63.jpg (flyer page 4)](pages/flyer172-page4-47ab4a8b63.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-4-max.jpg
- **Details:** confidence: 0.90 · item_key: `d13dd2b655b363c8`
- **Raw:** `{"block_text": null, "ocr_lines": ["MEGA"]}`

— from flyer 172 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Kept as-is. The record is the Charmin MEGA toilet-paper pack (24 = 96 rolls) visible at the bottom of page 4; only "MEGA" survived as its name. The stored 24.96 stands as its price (member pricing prints on this page; not independently verified). Merchandise, unclassified.

### Item 16278

![item 16278](images/item-16278.jpg)

- **Name (English):** None
- **Name (French):** AUCANADA
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
- **bbox:** left 76, top 138, right 480, bottom 161, page 4
- **Full page:** [pages/flyer172-page4-47ab4a8b63.jpg (flyer page 4)](pages/flyer172-page4-47ab4a8b63.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-4-max.jpg
- **Details:** confidence: 0.97 · item_key: `9c6b908143303ff4`
- **Raw:** `{"block_text": null, "ocr_lines": ["AUCANADA"]}`

— from flyer 172 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** DELETED — badge phantom. The record's crop is a red "était 79,99$" was-price badge beside a "FABRIQUÉ AU CANADA" leaf; no product name or product exists in it.

### Item 16309

![item 16309](images/item-16309.jpg)

- **Name (English):** None
- **Name (French):** SAUVAGE MARIPESCA LONGE DE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 2.27KG
- **Price:** 56.99
- **Printed Price:** “56.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 518, top 455, right 926, bottom 497, page 11
- **Full page:** [pages/flyer172-page11-3ce9554acb.jpg (flyer page 11)](pages/flyer172-page11-3ce9554acb.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-11-max.jpg
- **Details:** confidence: 0.92 · item_key: `70dc1fa13b6b965d`
- **Raw:** `{"block_text": "SAUVAGE\nMARIPESCA LONGE DE\nCERTAINES VARIÉTÉS Mutilati tel:\nSURGELÉES, 2,27 KG a ee", "ocr_lines": ["LONGE DE", "MORUESAUVAGE", "CERTAINESVARIETES", "SURGELEES.2,27KG"], "harvest": {"size": "2.27KG", "unit": "each", "via": "crop"}}`

— from flyer 172 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Maripesca wild cod loins (frozen, 2.27 kg) at 56.99 — verified. Unclassified under its garbled name.

### Item 16317

![item 16317](images/item-16317.jpg)

- **Name (English):** None
- **Name (French):** PREPAREAU CANADA CANADA
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 1.79
- **Printed Price:** “1.79”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 572, top 562, right 732, bottom 585, page 12
- **Full page:** [pages/flyer172-page12-78375276bc.jpg (flyer page 12)](pages/flyer172-page12-78375276bc.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-12-max.jpg
- **Details:** confidence: 0.98 · item_key: `2daee253e4b7d182`
- **Raw:** `{"block_text": null, "ocr_lines": ["PREPAREAU", "CANADA", "CANADA"]}`

— from flyer 172 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** DELETED — badge phantom. The record's crop is a "PRÉPARÉ AU CANADA" leaf beside an "était 1,79$" was-price badge; no product exists in it.

### Item 16322

![item 16322](images/item-16322.jpg)

- **Name (English):** None
- **Name (French):** COLLATION SE SAVOUREUSE KURKURE a CERTAINES VARIETES
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 30X115G
- **Price:** 41.99
- **Printed Price:** “41.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 664, top 714, right 906, bottom 772, page 13
- **Full page:** [pages/flyer172-page13-77b7c43418.jpg (flyer page 13)](pages/flyer172-page13-77b7c43418.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-13-max.jpg
- **Details:** confidence: 0.98 · item_key: `fda762576727cefd`
- **Raw:** `{"block_text": "COLLATION SE\nSAVOUREUSE\nKURKURE a\nCERTAINES VARIETES\n30 X 115G\nFLAVOURED SNACK", "ocr_lines": ["COLLATION", "SAVOUREUSE", "KURKURE", "CERTAINESVARIETES", "FLAVOURED SNACK"], "harvest": {"size": "30X115G", "via": "crop"}}`

— from flyer 172 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Kurkure flavoured snack (case of 30 x 115 g) at 41.99 +tx — verified; a case price. Unclassified.

### Item 16342

![item 16342](images/item-16342.jpg)

- **Name (English):** None
- **Name (French):** TIAFLARLEVEEENPROTENES JUMBO
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 40X40G
- **Price:** 3.49
- **Printed Price:** “3.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 224, top 291, right 612, bottom 384, page 15
- **Full page:** [pages/flyer172-page15-dc56f6e922.jpg (flyer page 15)](pages/flyer172-page15-dc56f6e922.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-15-max.jpg
- **Details:** confidence: 0.98 · item_key: `f0d56a2543e30884`
- **Raw:** `{"block_text": "FOR LA PES CES a\nRE hatin Din", "ocr_lines": ["TIAFLARLEVEEENPROTENES", "JUMBO"], "harvest": {"size": "40X40G", "unit": "each", "via": "crop"}}`

— from flyer 172 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Kept as-is. A JUMBO high-protein meat snack bag; the badge beside its cell prints 2.99 member / 3.49 non-member, and the stored 3.49 is the non-member price. Its stored name is packaging garble. Unclassified.

### Item 16345

![item 16345](images/item-16345.jpg)

- **Name (English):** None
- **Name (French):** BAR
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 17.99
- **Printed Price:** “17.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 602, top 856, right 926, bottom 929, page 15
- **Full page:** [pages/flyer172-page15-dc56f6e922.jpg (flyer page 15)](pages/flyer172-page15-dc56f6e922.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-15-max.jpg
- **Details:** confidence: 0.98 · item_key: `c96e211bd5ba0ac7`
- **Raw:** `{"block_text": "| BAR |", "ocr_lines": ["BAR"]}`

— from flyer 172 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct price. Clif Bar (12 x 68 g) at 17.99 — verified; the stored name is the fragment "BAR". Unclassified.

### Item 16352

![item 16352](images/item-16352.jpg)

- **Name (English):** None
- **Name (French):** RÉPARÉ AU CANADA
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 1.47
- **Printed Price:** “15/22.00”
- **Unit quantity:** 15.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 794, top 686, right 920, bottom 773, page 16
- **Full page:** [pages/flyer172-page16-671c2b2bd7.jpg (flyer page 16)](pages/flyer172-page16-671c2b2bd7.jpg)
- **Image source URL:** https://flyerify.com/images/offers/835163/wholesale-club-qc-flyer-october-15-to-21-16-max.jpg
- **Details:** confidence: 0.97 · item_key: `6d608aedb9723e72`
- **Conditions:** `{"multibuy": {"count": 15, "total": 22.0}, "alt_prices": ["12.99"]}`
- **Raw:** `{"block_text": "RÉPARÉ AU\nCANADA", "ocr_lines": ["PREPAREAU", "CANADA"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. The offer prints "15/22$ ou 1,99 ch."; the DB had stored 1.47 — the derived per-unit of the multibuy. Now the printed 1.99 single price, with the 15-for-22 multibuy recorded. The product's name did not survive (the record is named for the "Préparé au Canada" leaf). Unclassified.
