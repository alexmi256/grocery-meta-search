# Shop Santé — full product report

Store slug: `shop-sante`. Generated from `data/grocery.db`. A sampled subset of 17 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 80, valid 2026-10-01 → 2026-10-31 — a month-long catalogue; 23 items, 17 sampled).
- **Sample counts:** 7 classified + 10 unclassified shown — the unclassified tilt is this store's assortment: supplements (pre-workouts, collagen, EAA, liver support) whose name forms don't trip the dosage-form exclusion and carry no grocery vocabulary.
- **Issues found:** one price error — the Rule One Source 7 protein stored 39.00 against a printed 39.99 (dropped cents). Everything else verified against its badge, including the dual-price Krono bar (3.49 single / 39.99 the box of 12 — the single is stored, correctly) and the two distinct Unreal Halloween mini-bar offers (29.99 the 26-count, 23.99 the 300 g). One item's price could not be visually confirmed (10584, a brand-collage page) with no contradicting value found.
- **Fixes applied this pass:** 10613 → 39.99.

## Flyer 80 — valid 2026-10-01 → 2026-10-31 (7 classified items, 10 unclassified)

Source ref: `circulaire-shop-sante-du-1-au-31-octobre-2026` · fetched 2026-10-13T18:19:55.217Z

### Item 10583

![item 10583](images/item-10583.jpg)

- **Name (English):** 4732
- **Name (French):** BOISSON ÉNERGISANTE GHOST
- **Brand:** None
- **Category (English):** Drinks > Sports & Energy
- **Category (French):** Boissons > Boissons énergisantes et pour sportifs
- **How classified:** rule (`sports-energy`)
- **Size:** 473ML
- **Price:** 4.49
- **Printed Price:** “4.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 139, top 816, right 304, bottom 904, page 2
- **Full page:** [pages/flyer80-page2-542ba22b32.jpg (flyer page 2)](pages/flyer80-page2-542ba22b32.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `67cbe80156416606`
- **Raw:** `{"block_text": "BOISSON ÉNERGISANTE\nGHOST | 4732", "ocr_lines": ["BOISSON ENERGISANTE", "GHOSTI473ML"], "harvest": {"size": "473ML", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Ghost energy drink (473 ml) at 4.49 — verified on the badge. Sports & Energy is right.

### Item 10584

![item 10584](images/item-10584.jpg)

- **Name (English):** None
- **Name (French):** HUILE DE CAMELINE EN VAPORISATEUR PRET. TSF
- **Brand:** None
- **Category (English):** Pantry > Oils & Vinegar
- **Category (French):** Produits du garde-manger > Huile et vinaigre
- **How classified:** rule (`oils-vinegar`)
- **Size:** None
- **Price:** 9.94
- **Printed Price:** “9.94”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 729, top 386, right 822, bottom 431, page 3
- **Full page:** [pages/flyer80-page3-2c2cf9b1f9.jpg (flyer page 3)](pages/flyer80-page3-2c2cf9b1f9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/03.webp
- **Details:** confidence: 0.59 · item_key: `1e0fe9d4222974a5`
- **Raw:** `{"block_text": "HUILE DE CAMELINE\nEN VAPORISATEUR\nPRET. TSF.", "ocr_lines": ["HUILEDECAMELINE", "ENVAPORISATEUR"]}`

**Item Review Analysis (Pass 1):** Not visually confirmed, no contradiction found. FitCook camelina oil spray (butter taste) — the item is the bottle's own label text on a FitCook range-collage page; no price badge sits in its cell. The stored 9.94 stands (plausible for the product); recorded as unverified. Oils & Vinegar is right.

### Item 10589

![item 10589](images/item-10589.jpg)

- **Name (English):** 456-466 X 12
- **Name (French):** BARRE DE CÉRÉALES DE RIZ KRONO NUTRITION
- **Brand:** None
- **Category (English):** Pantry > Cereal & Breakfast
- **Category (French):** Produits du garde-manger > Céréales et petits-déjeuners
- **How classified:** rule (`specific-protein-bars`)
- **Size:** 45G
- **Price:** 3.49
- **Printed Price:** “3.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 141, top 534, right 367, bottom 616, page 8
- **Full page:** [pages/flyer80-page8-c2efd8d0f0.jpg (flyer page 8)](pages/flyer80-page8-c2efd8d0f0.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/08.webp
- **Details:** confidence: 0.99 · item_key: `ede3f8c2e226a837`
- **Raw:** `{"block_text": "BARRE DE CÉRÉALES DE RIZ\nKRONO NUTRITION | 456-466 X 12", "ocr_lines": ["BARRE DECEREALESDERIZ", "KRONONUTRITION|45G-45GX12"], "harvest": {"size": "45G", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Krono Nutrition rice cereal bar (45 g) at 3.49 — the badge also offers 39.99 for the box of 12; the single-bar price is stored. Cereal & Breakfast is the classifier's shelf for it.

### Item 10595

![item 10595](images/item-10595.jpg)

- **Name (English):** BAREBELLS
- **Name (French):** BARRE PROTÉINÉE
- **Brand:** None
- **Category (English):** Pantry > Cereal & Breakfast
- **Category (French):** Produits du garde-manger > Céréales et petits-déjeuners
- **How classified:** rule (`specific-protein-bars`)
- **Size:** 55 G
- **Price:** 4.19
- **Printed Price:** “4.19”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 138, top 548, right 362, bottom 629, page 12
- **Full page:** [pages/flyer80-page12-a714a8df7b.jpg (flyer page 12)](pages/flyer80-page12-a714a8df7b.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/12.webp
- **Details:** confidence: 0.99 · item_key: `ac8638eb6987c1bd`
- **Raw:** `{"block_text": "BARRE PROTÉINÉE | BAREBELLS\n55 G | REG.: 4,49", "ocr_lines": ["BARREPROTEINEEIBAREBELLS", "55GIREG.:4.49"]}`

**Item Review Analysis (Pass 1):** Correct. Barebells protein bar (55 g) at 4.19 (reg. 4.49) — verified. (Shelved under Cereal & Breakfast with the other bars.)

### Item 10605

![item 10605](images/item-10605.jpg)

- **Name (English):** UNREAL | X26
- **Name (French):** MINTBARS D'HALLOWEEN SAVEURS MIXTES
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** guard-remap (`household-goods`)
- **Size:** None
- **Price:** 29.99
- **Printed Price:** “29.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 624, top 34, right 868, bottom 113, page 15
- **Full page:** [pages/flyer80-page15-effbeb6e2f.jpg (flyer page 15)](pages/flyer80-page15-effbeb6e2f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/15.webp
- **Details:** confidence: 0.87 · item_key: `5403d8c1992ef36f`
- **Raw:** `{"block_text": "MINTBARS D'HALLOWEEN\nSAVEURS MIXTES | UNREAL | X26", "ocr_lines": ["MINIBARSD'HALLOWEEN", "SAVEURSMIXTESIUNREAL|X26"]}`

**Item Review Analysis (Pass 1):** Correct. Halloween mini bars, assorted (Unreal, 26-count) at 29.99 — verified; a different offer from item 10606 (300 g at 23.99). The stored name garbles "MINI" as "MINT". Candy & Chocolate is right.

### Item 10606

![item 10606](images/item-10606.jpg)

- **Name (English):** 300 6
- **Name (French):** MINI BARS D'HALLOWEEN UNREAL
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** guard-remap (`specific-protein-bars`)
- **Size:** 300G
- **Price:** 23.99
- **Printed Price:** “23.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 206, top 36, right 396, bottom 116, page 15
- **Full page:** [pages/flyer80-page15-effbeb6e2f.jpg (flyer page 15)](pages/flyer80-page15-effbeb6e2f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/15.webp
- **Details:** confidence: 0.92 · item_key: `47bea16cf517d58c`
- **Raw:** `{"block_text": "MINI BARS D'HALLOWEEN\nUNREAL | 300 6", "ocr_lines": ["MINIBARSD'HALLOWEEN", "UNREALI300G"], "harvest": {"size": "300G", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Unreal Halloween mini bars (300 g) at 23.99 — verified. Candy & Chocolate is right.

### Item 10607

![item 10607](images/item-10607.jpg)

- **Name (English):** j £NEAGY DRINK BOISSON ENERGISANTE 2
- **Name (French):** ME
- **Brand:** None
- **Category (English):** Drinks > Sports & Energy
- **Category (French):** Boissons > Boissons énergisantes et pour sportifs
- **How classified:** rule (`sports-energy`)
- **Size:** 473 ML
- **Price:** 3.49
- **Printed Price:** “3.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 79, top 548, right 302, bottom 640, page 16
- **Full page:** [pages/flyer80-page16-dd396d47ca.jpg (flyer page 16)](pages/flyer80-page16-dd396d47ca.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/16.webp
- **Details:** confidence: 0.99 · item_key: `a765ac9b4f7699e1`
- **Raw:** `{"block_text": "ME | j £NEAGY DRINK\nBOISSON ENERGISANTE 2\n\nrept\nRYSE | 473 ML om\nREG.: 3,99", "ocr_lines": ["ENERGYDRINK", "BOISSON ENERGISANTE", "RYSE1473ML", "REG.:3,99"]}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 80 (valid 2026-10-01 → 2026-10-31)

**Item Review Analysis (Pass 1):** Correct price. Ryse energy drink (473 ml) at 3.49 (reg. 3.99) — verified; the stored name is the fragment "ME". Sports & Energy is right.

### Item 10586

![item 10586](images/item-10586.jpg)

- **Name (English):** None
- **Name (French):** THAVAGE PRE-WORKOUT CBUM
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 520 G
- **Price:** 49.99
- **Printed Price:** “49.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 132, top 555, right 316, bottom 652, page 6
- **Full page:** [pages/flyer80-page6-e1b4e88dce.jpg (flyer page 6)](pages/flyer80-page6-e1b4e88dce.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/06.webp
- **Details:** confidence: 0.97 · item_key: `f32f8efd864c4846`
- **Raw:** `{"block_text": "THAVAGE PRE-WORKOUT\nCBUM\n520 G | REG.: 59,99", "ocr_lines": ["THAVAGEPRE-WORKOUT", "CBUM", "520G|REG:59.99"]}`

— from flyer 80 (valid 2026-10-01 → 2026-10-31)

**Item Review Analysis (Pass 1):** Correct price. Thavage pre-workout by CBUM (520 g) at 49.99 (reg. 59.99) — verified. A supplement, unclassified.

### Item 10587

![item 10587](images/item-10587.jpg)

- **Name (English):** None
- **Name (French):** 40 PORTIONS
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 34.99
- **Printed Price:** “34.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 653, top 408, right 885, bottom 488, page 6
- **Full page:** [pages/flyer80-page6-e1b4e88dce.jpg (flyer page 6)](pages/flyer80-page6-e1b4e88dce.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/06.webp
- **Details:** confidence: 0.89 · item_key: `55fcec2761151b2e`
- **Raw:** `{"block_text": "ee: PHARMA\n40 PORTIONS |", "ocr_lines": ["PUNCHOUT2.OINOVAPHARMA", "40PORTIONS"]}`

— from flyer 80 (valid 2026-10-01 → 2026-10-31)

**Item Review Analysis (Pass 1):** Correct price. Nova Pharma Punch Out 2.0 pre-workout (40 servings) at 34.99 (reg. 44.99) — verified; the stored name is its serving line. Unclassified.

### Item 10588

![item 10588](images/item-10588.jpg)

- **Name (English):** None
- **Name (French):** SYNERMAG PLUS,
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 90 CAPSULES
- **Price:** 34.99
- **Printed Price:** “34.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 137, top 836, right 295, bottom 917, page 7
- **Full page:** [pages/flyer80-page7-2c4e1316f2.jpg (flyer page 7)](pages/flyer80-page7-2c4e1316f2.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/07.webp
- **Details:** confidence: 0.99 · item_key: `93037a1197eb7c28`
- **Raw:** `{"block_text": "SYNERMAG PLUS,\nATP LAB | sokAPSèRS", "ocr_lines": ["SYNERMAG PLUS", "ATPLABI90CAPSULES"], "harvest": {"size": "90 CAPSULES", "via": "crop"}}`

— from flyer 80 (valid 2026-10-01 → 2026-10-31)

**Item Review Analysis (Pass 1):** Correct price. ATP Lab Synermag Plus (90 capsules) at 34.99 — verified. A supplement, unclassified (this name form doesn't trip the dosage-form exclusion).

### Item 10592

![item 10592](images/item-10592.jpg)

- **Name (English):** None
- **Name (French):** LIVERIREVIVE 120 CAPSULESIREG:79.99
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 120 CAPSULES
- **Price:** 69.99
- **Printed Price:** “69.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 362, top 912, right 582, bottom 950, page 10
- **Full page:** [pages/flyer80-page10-43e260130d.jpg (flyer page 10)](pages/flyer80-page10-43e260130d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/10.webp
- **Details:** confidence: 0.95 · item_key: `841b9a5de16baa8c`
- **Raw:** `{"block_text": "LIVER [REVIVE\n120 CAPSULES | REG.: 79,99", "ocr_lines": ["LIVERIREVIVE", "120 CAPSULESIREG:79.99"]}`

— from flyer 80 (valid 2026-10-01 → 2026-10-31)

**Item Review Analysis (Pass 1):** Correct price. Liver Revive (120 capsules) at 69.99 (reg. 79.99) — verified. A supplement, unclassified.

### Item 10594

![item 10594](images/item-10594.jpg)

- **Name (English):** None
- **Name (French):** JWID'COLLAGENLXPN
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 500ML
- **Price:** 23.99
- **Printed Price:** “23.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 66, top 912, right 304, bottom 951, page 10
- **Full page:** [pages/flyer80-page10-43e260130d.jpg (flyer page 10)](pages/flyer80-page10-43e260130d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/10.webp
- **Details:** confidence: 0.99 · item_key: `06313d5c994a585e`
- **Raw:** `{"block_text": "JWID'COLLAGENLXPN\nOOM Be;", "ocr_lines": ["LIQUID COLLAGENIXPN", "500MLRE20.99"], "harvest": {"size": "500ML", "via": "crop"}}`

— from flyer 80 (valid 2026-10-01 → 2026-10-31)

**Item Review Analysis (Pass 1):** Correct price. XPN liquid collagen (500 ml) at 23.99 (reg. 29.99) — verified. A supplement, unclassified.

### Item 10596

![item 10596](images/item-10596.jpg)

- **Name (English):** 1006
- **Name (French):** BOUCHÉES PROTÉINÉES PROBITES
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 100 G
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 139, top 376, right 306, bottom 460, page 12
- **Full page:** [pages/flyer80-page12-a714a8df7b.jpg (flyer page 12)](pages/flyer80-page12-a714a8df7b.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/12.webp
- **Details:** confidence: 0.97 · item_key: `fbcd6775460a5c0a`
- **Raw:** `{"block_text": "BOUCHÉES PROTÉINÉES\nPROBITES | 1006 |", "ocr_lines": ["BOUCHEES PROTEINEES", "PROBITESI100G"], "harvest": {"size": "100 G", "via": "crop"}}`

— from flyer 80 (valid 2026-10-01 → 2026-10-31)

**Item Review Analysis (Pass 1):** Correct price. Probites protein bites (100 g) at 4.99 — verified. Unclassified under its name form.

### Item 10603

![item 10603](images/item-10603.jpg)

- **Name (English):** None
- **Name (French):** ÆAA-HD HD MUSCLE"
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 39.99
- **Printed Price:** “39.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 48, top 414, right 203, bottom 474, page 14
- **Full page:** [pages/flyer80-page14-ced07889f5.jpg (flyer page 14)](pages/flyer80-page14-ced07889f5.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/14.webp
- **Details:** confidence: 0.94 · item_key: `10364269330d490c`
- **Raw:** `{"block_text": "ÆAA-HD HD MUSCLE\"", "ocr_lines": ["EAA HDIHD MUSCLE"]}`

— from flyer 80 (valid 2026-10-01 → 2026-10-31)

**Item Review Analysis (Pass 1):** Correct price. HD Muscle EAA HD at 39.99 — verified. A supplement, unclassified.

### Item 10609

![item 10609](images/item-10609.jpg)

- **Name (English):** None
- **Name (French):** BOISSON PROTEINEE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 355ML
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 136, top 376, right 299, bottom 458, page 16
- **Full page:** [pages/flyer80-page16-dd396d47ca.jpg (flyer page 16)](pages/flyer80-page16-dd396d47ca.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/16.webp
- **Details:** confidence: 0.92 · item_key: `540dafd24463957a`
- **Raw:** `{"block_text": "BOISSON PROTEINEE |\nRYSE | 355ML| caf", "ocr_lines": ["BOISSON PROTEINEE", "RYSE|355ML|REG5.99"]}`

— from flyer 80 (valid 2026-10-01 → 2026-10-31)

**Item Review Analysis (Pass 1):** Correct price. Ryse protein drink (355 ml) at 4.99 (reg. 5.99) — verified. Unclassified under its generic name.

### Item 10612

![item 10612](images/item-10612.jpg)

- **Name (English):** None
- **Name (French):** LIQUIDE Py CR APPLIEDINUTRITION’ 480 M
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 29.99
- **Printed Price:** “29.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 460, top 887, right 732, bottom 968, page 17
- **Full page:** [pages/flyer80-page17-1a1329a31e.jpg (flyer page 17)](pages/flyer80-page17-1a1329a31e.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/17.webp
- **Details:** confidence: 0.99 · item_key: `04aab7c7973a1602`
- **Raw:** `{"block_text": "LIQUIDE Py CR\nAPPLIEDINUTRITION’ 480 M", "ocr_lines": ["LIQUIDEL-CARNITINE3000", "APPLIEDNUTRITIONT480MLIE99"]}`

— from flyer 80 (valid 2026-10-01 → 2026-10-31)

**Item Review Analysis (Pass 1):** Correct price. Applied Nutrition liquid L-carnitine 3000 (480 ml) at 29.99 (reg. 39.99) — verified. A supplement, unclassified.

### Item 10613

![item 10613](images/item-10613.jpg)

- **Name (English):** None
- **Name (French):** SOURCE 7 PROTÉINE RULE ONE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 18LBS
- **Price:** 39.00
- **Printed Price:** “39”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 132, top 542, right 283, bottom 634, page 18
- **Full page:** [pages/flyer80-page18-1b2dd5bed6.jpg (flyer page 18)](pages/flyer80-page18-1b2dd5bed6.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-shop-sante-du-1-au-31-octobre-2026/18.webp
- **Details:** confidence: 0.76 · item_key: `2760535a21e199f4`
- **Raw:** `{"block_text": "SOURCE 7 PROTÉINE\nRULE ONE\n18LBS | REG.: 47,99", "ocr_lines": ["SOURCE7 PROTEINE", "RULE ONE", "1.8LBS|REG.47.99"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Rule One Source 7 protein (1.8 lbs) prints 39.99 (reg. 47.99); the DB had 39.00 — dropped cents. Unclassified.
