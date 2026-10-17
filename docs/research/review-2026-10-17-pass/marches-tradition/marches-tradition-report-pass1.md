# Les Marchés Tradition — full product report

Store slug: `marches-tradition`. Generated from `data/grocery.db`. A sampled subset of 18 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 76, valid 2026-10-15 → 2026-10-21, 77 items). The expired Oct 8–14 edition is correctly excluded.
- **Sample counts:** 10 classified + 8 unclassified shown, as drawn.
- **Issues found:** 5 wrong prices and 1 duplicate. Two items stored 66.00 — the apples (a 1.81 kg bag at 3.99; the "66" is the garbled "Rég. 6,99$") and the aluminum foil (3.99). The garbage bags stored 50.00 — the foil's "50 ft/pi" length read as a price; the bags print 8.99. The grapes stored 3.66 for a printed 3.99/lb (9→6 twice), and the Genova bottle 6.68 for 8.99. Item 10468 ("FUN SIZE PETITES JOIES", 95.00) is a duplicate capture of the Mars treats box — the "95" is its piece count printed on the box; the product is properly carried by item 10459 at 21.99, so 10468 is deleted. The household items in the sample (foil, garbage bags, Hefty plates) sit unclassified and are kept for review under the standing rule.
- **Fixes applied this pass:** 10427 → 3.99, 10440 → 3.99/lb, 10491 → 3.99, 10492 → 8.99, 10501 → 8.99; item 10468 deleted (duplicate).

## Flyer 76 — valid 2026-10-15 → 2026-10-21 (10 classified items, 8 unclassified)

Source ref: `circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026` · fetched 2026-10-13T18:15:46.681Z

### Item 10432

![item 10432](images/item-10432.jpg)

- **Name (English):** None
- **Name (French):** BIFTECK ATTENDRI OU SANDWICH TENDERIZED OR SANDWICH STEAK
- **Brand:** None
- **Category (English):** Meat > Beef
- **Category (French):** Viande > Bœuf
- **How classified:** rule (`beef`)
- **Size:** None
- **Price:** 12.99
- **Printed Price:** “12.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 710, top 264, right 981, bottom 306, page 2
- **Full page:** [pages/flyer76-page2-614e05e2ca.jpg (flyer page 2)](pages/flyer76-page2-614e05e2ca.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `baa1440c75564ee6`
- **Raw:** `{"block_text": "BIFTECK ATTENDRI\nOU SANDWICH\nTENDERIZED OR\nSANDWICH STEAK\nFormat familial", "ocr_lines": ["BIFTECKATTENDRI", "OUSANDWICH", "TENDERIZEDOR", "SANDWICHSTEAK"]}`

**Item Review Analysis (Pass 1):** Correct. Tenderized or sandwich steak (family size) at 12.99/lb — verified. Beef is right.

### Item 10440

![item 10440](images/item-10440.jpg)

- **Name (English):** None
- **Name (French):** RAISINS ROUGES SANS PEPINS
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 3.66
- **Printed Price:** “3.66”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 407, top 612, right 655, bottom 641, page 2
- **Full page:** [pages/flyer76-page2-614e05e2ca.jpg (flyer page 2)](pages/flyer76-page2-614e05e2ca.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.98 · item_key: `ec6938d2fb3bcad8`
- **Raw:** `{"block_text": ">... =\nRAISINS ROUGES\nSANS PEPINS\nProduit des Etats-Unis", "ocr_lines": ["RAISINSROUGES", "SANSPEPINS"], "harvest": {"unit": "lb", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Seedless red grapes (USA) print 3.99/lb; the DB had 3.66 (the 9→6 glyph error, twice). Unit now pound. Fresh Fruits is right.

### Item 10444

![item 10444](images/item-10444.jpg)

- **Name (English):** None
- **Name (French):** SALADE C'EST PRET! SALAD OR COLESLAW
- **Brand:** None
- **Category (English):** Prepared Meals > Salads & Soups
- **Category (French):** Repas préparés > Salades et soupes
- **How classified:** rule (`salads-soups`)
- **Size:** 454g
- **Price:** 3.49
- **Printed Price:** “3.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 357, top 899, right 485, bottom 947, page 3
- **Full page:** [pages/flyer76-page3-f25e252b3b.jpg (flyer page 3)](pages/flyer76-page3-f25e252b3b.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `fe52503085b4fe96`
- **Raw:** `{"block_text": "—_—\nSALADE\nC'EST PRET!\nSALAD OR COLESLAW\n454g", "ocr_lines": ["SALADE", "ESTPRET!", "SALADORCOLESLAW"]}`

**Item Review Analysis (Pass 1):** Correct. C'est Prêt! salad or coleslaw (454 g) at 3.49 +tx — verified. Salads & Soups is right.

### Item 10459

![item 10459](images/item-10459.jpg)

- **Name (English):** None
- **Name (French):** FRIANDISES MARS CANADA PETITES JOIES
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 1kg
- **Price:** 21.99
- **Printed Price:** “21.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 754, top 873, right 890, bottom 931, page 5
- **Full page:** [pages/flyer76-page5-926cb046b9.jpg (flyer page 5)](pages/flyer76-page5-926cb046b9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/05.webp
- **Details:** confidence: 0.99 · item_key: `abf490b3f15e76fd`
- **Raw:** `{"block_text": "FRIANDISES\nMARS CANADA\nPETITES JOIES\nAssortiment\nTREATS\n\nOS aiv/ar 106", "ocr_lines": ["FRIANDISES", "MARSCANADA", "PETITESJOIES", "TREATS"], "harvest": {"size": "1kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Mars Canada assorted treats (1 kg, 95 or 105 count) at 21.99 +tx (reg. 22.99-24.49$) — verified. Candy & Chocolate is right.

### Item 10486

![item 10486](images/item-10486.jpg)

- **Name (English):** None
- **Name (French):** PAIN TRANCHÉ COMPLIMENTS
- **Brand:** None
- **Category (English):** Bakery > Bread
- **Category (French):** Boulangerie > Pain
- **How classified:** rule (`bread`)
- **Size:** 500g
- **Price:** 5.49
- **Printed Price:** “5.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 892, top 408, right 990, bottom 468, page 7
- **Full page:** [pages/flyer76-page7-3c2812d5f7.jpg (flyer page 7)](pages/flyer76-page7-3c2812d5f7.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/07.webp
- **Details:** confidence: 0.99 · item_key: `a35ae8e1a1474fac`
- **Raw:** `{"block_text": "PAIN TRANCHÉ\nCOMPLIMENTS\nMultigrain,\n\nSeigle marbré\nSLICED BREAD\nea", "ocr_lines": ["PAIN TRANCHE", "SLICED BREAD"], "harvest": {"size": "500g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Compliments sliced bread (multigrain/marble rye, 500 g) at 5.49 (reg. 5.99$) — verified. Bread is right.

### Item 10493

![item 10493](images/item-10493.jpg)

- **Name (English):** None
- **Name (French):** QUART DE JAMBON TOUPIE DÉSOSSÉ GASPÉSIEN TOUPIE BONELESS QUARTER HAM
- **Brand:** None
- **Category (English):** Meat > Pork & Ham
- **Category (French):** Viande > Porc et jambon
- **How classified:** rule (`pork-ham`)
- **Size:** 750g
- **Price:** 11.99
- **Printed Price:** “11.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 336, top 219, right 530, bottom 286, page 8
- **Full page:** [pages/flyer76-page8-cc11298662.jpg (flyer page 8)](pages/flyer76-page8-cc11298662.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/08.webp
- **Details:** confidence: 0.99 · item_key: `318f93144e9a6ca3`
- **Raw:** `{"block_text": "L\nQUART DE JAMBON\nTOUPIE DÉSOSSÉ\nGASPÉSIEN\nTOUPIE BONELESS\nQUARTER HAM\n750a", "ocr_lines": ["QUARTDEJAMBON", "TOUPIEDESOSSE", "GASPESIEN", "TOUPIEBONELESS", "QUARTERHAM"], "harvest": {"size": "750g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Toupie boneless quarter ham, Gaspésien (750 g) at 11.99 (reg. 13.99-15.49$) — verified. Pork & Ham is right.

### Item 10494

![item 10494](images/item-10494.jpg)

- **Name (English):** None
- **Name (French):** SANDWICHS
- **Brand:** None
- **Category (English):** Prepared Meals > Sandwiches
- **Category (French):** Repas préparés > Sandwichs
- **How classified:** rule (`sandwiches`)
- **Size:** None
- **Price:** 3.50
- **Printed Price:** “2/7.00”
- **Unit quantity:** 2.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 194, top 471, right 416, bottom 514, page 8
- **Full page:** [pages/flyer76-page8-cc11298662.jpg (flyer page 8)](pages/flyer76-page8-cc11298662.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/08.webp
- **Details:** confidence: 0.94 · item_key: `5be8b3d1d5bc0b15`
- **Conditions:** `{"multibuy": {"count": 2, "total": 7.0}}`
- **Raw:** `{"block_text": "SANDWICHS\n\nOU PAINS Lagat\nC'EST PRET!\n\nSTUFFED SANDWICHES\nOR BREADS\n\nSélection variée", "ocr_lines": ["SANDWICHS", "OUPAINSFARCIS", "STUFFEDSANDWICHES", "ORBREADS"]}`

**Item Review Analysis (Pass 1):** Correct. C'est Prêt! stuffed sandwiches or breads print "2/7$"; the stored 3.50 is the split. Sandwiches is right.

### Item 10499

![item 10499](images/item-10499.jpg)

- **Name (English):** None
- **Name (French):** MINI BEIGNETS SAVEURS DU FOUR MINI DONUTS
- **Brand:** None
- **Category (English):** Bakery > Cookies, Muffins & Desserts
- **Category (French):** Boulangerie > Biscuits, muffins et desserts
- **How classified:** rule (`bakery-cookies-muffins`)
- **Size:** None
- **Price:** 9.49
- **Printed Price:** “9.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 492, top 467, right 683, bottom 503, page 8
- **Full page:** [pages/flyer76-page8-cc11298662.jpg (flyer page 8)](pages/flyer76-page8-cc11298662.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/08.webp
- **Details:** confidence: 0.99 · item_key: `2f23c4f7ebb431b5`
- **Raw:** `{"block_text": "MINI BEIGNETS\nSAVEURS DU FOUR\nMINI DONUTS\nEmballage de 12", "ocr_lines": ["MINIBEIGNETS", "MINIDONUTS"]}`

**Item Review Analysis (Pass 1):** Correct. Saveurs du Four mini donuts (pack of 12) at 9.49 (reg. 9.99$) — verified. Cookies, Muffins & Desserts is right.

### Item 10500

![item 10500](images/item-10500.jpg)

- **Name (English):** None
- **Name (French):** PEPPERONI CASERTA ROMA PEPPERONI CASERTA
- **Brand:** None
- **Category (English):** Deli > Deli Meat
- **Category (French):** Charcuterie > Charcuterie
- **How classified:** rule (`deli-meat`)
- **Size:** 200g
- **Price:** 3.49
- **Printed Price:** “3.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 43, top 209, right 267, bottom 244, page 8
- **Full page:** [pages/flyer76-page8-cc11298662.jpg (flyer page 8)](pages/flyer76-page8-cc11298662.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/08.webp
- **Details:** confidence: 0.99 · item_key: `5dd09ddf700a18b8`
- **Raw:** `{"block_text": "PEPPERONI CASERTA\nROMA\n\nPEPPERONI CASERTA\n2009", "ocr_lines": ["PEPPERONI CASERTA", "PEPPERONICASERTA"], "harvest": {"size": "200g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Caserta Roma pepperoni (200 g) at 3.49 (reg. 3.99-4.39$) — verified. Deli Meat is right.

### Item 10509

![item 10509](images/item-10509.jpg)

- **Name (English):** None
- **Name (French):** BOISSON GAZEUSE COMPLIMENTS SOFT DRINK
- **Brand:** None
- **Category (English):** Drinks > Soft Drinks
- **Category (French):** Boissons > Boissons gazeuses
- **How classified:** rule (`soft-drinks`)
- **Size:** 12×355mL
- **Price:** 8.79
- **Printed Price:** “8.79”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 88, top 473, right 196, bottom 648, page 9
- **Full page:** [pages/flyer76-page9-4766204cdc.jpg (flyer page 9)](pages/flyer76-page9-4766204cdc.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/09.webp
- **Details:** confidence: 0.99 · item_key: `179ec75fec36ee62`
- **Raw:** `{"block_text": "BOISSON GAZEUSE\nCOMPLIMENTS\n\nSOFT DRINK\n\n19 v 255 mi", "ocr_lines": ["BOISSONGAZEUSE", "COMPLIMENTS", "SOFTDRINK"], "harvest": {"size": "12×355mL", "via": "crop"}}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 76 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Compliments soft drinks (12 x 355 ml) at 8.79 +tx (reg. 9.29$) — verified. Soft Drinks is right.

### Item 10427

![item 10427](images/item-10427.jpg)

- **Name (English):** None
- **Name (French):** IPOMMES McINTOSH, SPARTAN, CORTLAND OU EMPIRE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 1,81kg
- **Price:** 66.00
- **Printed Price:** “66”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 827, top 347, right 993, bottom 452, page 1
- **Full page:** [pages/flyer76-page1-28b99f9daf.jpg (flyer page 1)](pages/flyer76-page1-28b99f9daf.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.54 · item_key: `4b51b5e81492e7a9`
- **Raw:** `{"block_text": "IPOMMES McINTOSH,\nSPARTAN, CORTLAND\nOU EMPIRE\n\n7 Produits du Québec\n\n34 Canada no 1\nCOMPLIMENTS\nMcINTOSH, SPARTAN,\nCORTLAND OR EMPIRE\nProducts of Quebec", "ocr_lines": ["POMMESMCINTOSH", "SPARTAN,CORTLAND", "OUEMPIRE", "COMPLIMENTS", "McINTOSH,SPARTAN,", "CORTLANDOREMPIRE"], "harvest": {"size": "1,81kg", "via": "crop"}}`

— from flyer 76 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Compliments apples (McIntosh/Spartan/Cortland/Empire, Quebec, 1.81 kg bag) print 3.99 (reg. 6.99$); the DB had 66.00 — the garbled regular price. Unclassified under its OCR-prefixed name ("IPOMMES").

### Item 10445

![item 10445](images/item-10445.jpg)

- **Name (English):** None
- **Name (French):** LYMEL OU/OR LAFLEUR
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 175g
- **Price:** 6.49
- **Printed Price:** “6.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 857, top 324, right 981, bottom 381, page 3
- **Full page:** [pages/flyer76-page3-f25e252b3b.jpg (flyer page 3)](pages/flyer76-page3-f25e252b3b.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `b0375185361af336`
- **Raw:** `{"block_text": "ru mp hd ass crus\nLYMEL OU/OR LAFLEUR\nAO phone Dinde", "ocr_lines": ["CHARCUTERIES", "EMINCEES", "OLYMELOUIORLAFLEUR"], "harvest": {"size": "175g", "via": "crop"}}`

— from flyer 76 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Olymel or Lafleur shaved deli meat (ham/turkey, 175 g) at 6.49 — verified. Unclassified under its garbled name.

### Item 10468

![item 10468](images/item-10468.jpg)

- **Name (English):** None
- **Name (French):** FUN SIZE PETITES JOIES
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 95.00
- **Printed Price:** “95”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 828, top 779, right 907, bottom 814, page 5
- **Full page:** [pages/flyer76-page5-926cb046b9.jpg (flyer page 5)](pages/flyer76-page5-926cb046b9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/05.webp
- **Details:** confidence: 0.99 · item_key: `b28f414f73a01bbd`
- **Raw:** `{"block_text": "FUN SIZE\nPETITES JOIES\nle. cg", "ocr_lines": ["FUN SIZE", "PETITESJOIES"]}`

— from flyer 76 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** DELETED — duplicate. The "item" is the Mars Fun Size treats box read from its own artwork ("FUN SIZE / PETITES JOIES / 95"); the 95 is the piece count, not a price. The product is properly carried by item 10459 at 21.99.

### Item 10480

![item 10480](images/item-10480.jpg)

- **Name (English):** None
- **Name (French):** ENERG
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 3.75
- **Printed Price:** “3.75”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 319, top 438, right 420, bottom 498, page 6
- **Full page:** [pages/flyer76-page6-e5a09e0d95.jpg (flyer page 6)](pages/flyer76-page6-e5a09e0d95.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/06.webp
- **Details:** confidence: 0.99 · item_key: `d16a61c4abff1152`
- **Raw:** `{"block_text": null, "ocr_lines": ["ENERG"], "harvest": {"unit": "each", "via": "crop"}}`

— from flyer 76 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. The energy drink (Red Bull) prints "7.50 +tx ou/or 3.75 ch." — the stored 3.75 is the per-can price. Unclassified under the truncated name "ENERG…".

### Item 10491

![item 10491](images/item-10491.jpg)

- **Name (English):** None
- **Name (French):** >' ALUMINIUM [NTS
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 66.00
- **Printed Price:** “66”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 368, top 797, right 592, bottom 819, page 7
- **Full page:** [pages/flyer76-page7-3c2812d5f7.jpg (flyer page 7)](pages/flyer76-page7-3c2812d5f7.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/07.webp
- **Details:** confidence: 0.99 · item_key: `8c68015cd0a0f37c`
- **Raw:** `{"block_text": ">' ALUMINIUM\n[NTS", "ocr_lines": ["ALUMINIUM"]}`

— from flyer 76 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Compliments aluminum foil prints 3.99; the DB had 66.00. A household item, unclassified; kept for review under the standing rule.

### Item 10492

![item 10492](images/item-10492.jpg)

- **Name (English):** None
- **Name (French):** GARBAGE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 50.00
- **Printed Price:** “50”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 439, top 670, right 572, bottom 791, page 7
- **Full page:** [pages/flyer76-page7-3c2812d5f7.jpg (flyer page 7)](pages/flyer76-page7-3c2812d5f7.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/07.webp
- **Details:** confidence: 0.99 · item_key: `98509febe04d2075`
- **Raw:** `{"block_text": "Not 8 Prat ee oma Lah\nGARBAGE\nBags » Sacs à\n\n| ORDURES", "ocr_lines": ["GARBAGE", "ORDURES"]}`

— from flyer 76 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 7. Compliments garbage bags (20-40 count) print 8.99 +tx (reg. 13.49-14.49$); the DB had 50.00 — the foil's "50 ft/pi" length from the cell below read as a price. Household item, unclassified; kept for review.

### Item 10498

![item 10498](images/item-10498.jpg)

- **Name (English):** None
- **Name (French):** ASSIETTES À DÎNER Heft COMPOSTABLES HEFTY ECOSAVE RECYCLABLE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 343, top 725, right 617, bottom 805, page 8
- **Full page:** [pages/flyer76-page8-cc11298662.jpg (flyer page 8)](pages/flyer76-page8-cc11298662.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/08.webp
- **Details:** confidence: 0.98 · item_key: `234f970466ce313c`
- **Raw:** `{"block_text": "a £\nASSIETTES À DÎNER Heft\nCOMPOSTABLES\nHEFTY\nECOSAVE\nRECYCLABLE\nDINNER PLATES\n0 0\nan 6.995 COMPOSTABLE # RECYCLABLE", "ocr_lines": ["ASSIETTESADINER", "COMPOSTABLES", "ECOSAVE", "ECOSAVE", "RECYCLABLE", "COMPOSTABLE'RECYCLABLE'"]}`

— from flyer 76 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Hefty EcoSave compostable dinner plates (20) at 4.99 +tx (reg. 6.99$) — verified. Household item, unclassified; kept for review.

### Item 10501

![item 10501](images/item-10501.jpg)

- **Name (English):** None
- **Name (French):** GENOVA
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
- **bbox:** left 793, top 387, right 955, bottom 425, page 8
- **Full page:** [pages/flyer76-page8-cc11298662.jpg (flyer page 8)](pages/flyer76-page8-cc11298662.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-marches-tradition-marches-coop-du-15-au-21-octobre-2026/08.webp
- **Details:** confidence: 0.99 · item_key: `ea6acf3ac9dd92c1`
- **Raw:** `{"block_text": "GENOVA |", "ocr_lines": ["GENOVA"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Genova (Italy, 175 g) prints 8.99 (reg. 10.99$); the DB had 6.68. Unclassified under the brand-only name.
