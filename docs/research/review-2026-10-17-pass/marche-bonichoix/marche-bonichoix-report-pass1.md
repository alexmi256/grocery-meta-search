# Marché Bonichoix — full product report

Store slug: `marche-bonichoix`. Generated from `data/grocery.db`. A sampled subset of 17 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 57, valid 2026-10-15 → 2026-10-21, 74 items across 7 pages). The expired Oct 8–14 edition is correctly excluded.
- **Sample counts:** 10 classified + 7 unclassified shown — the unclassified seven are mostly name fragments (label text and partial lines) whose prices are largely right.
- **Issues found:** 6 wrong prices of 17, all corrected from the crops/page. Two are count-or-total substitutions: the Hershey's Halloween bag's piece count (50) became its price (real: 12.49), and the Bubly/Montellier water item took its 2/17.00 multibuy total (real single: 9.99, multibuy recorded). Three are neighbour badges: the Humpty Dumpty snacks took the water's 7.29 (theirs: 3.99), the Clark maple beans took the bakery's 4.49 (theirs: 1.99), the compostable plates took a 6.00 (they print 4.99). One is a digit drop: Janes frozen fish fillets print 15.99, stored 5.99. Also verified as genuine, against first impressions: this flyer's price-point endings (2.22 biscuits, 2.77 blueberries, 2.33 bars, 1.25 soup) are printed exactly so.
- **Fixes applied this pass:** 9703 → 9.99 (+multibuy), 9704 → 3.99, 9713 → 15.99, 9746 → 12.49, 9757 → 4.99, 9765 → 1.99.

## Flyer 57 — valid 2026-10-15 → 2026-10-21 (10 classified items, 7 unclassified)

Source ref: `circulaire-marche-bonichoix-du-15-au-21-octobre-2026` · fetched 2026-10-13T14:59:32.540Z

### Item 9692

![item 9692](images/item-9692.jpg)

- **Name (English):** None
- **Name (French):** y BISCUITS DARE PETITS PLAISIRS NORMANDIE, SUPREME,
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** 310g
- **Price:** 2.22
- **Printed Price:** “2.22”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 847, top 657, right 992, bottom 759, page 1
- **Full page:** [pages/flyer57-page1-2ba4109ffb.jpg (flyer page 1)](pages/flyer57-page1-2ba4109ffb.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `0d86dd552f138c8e`
- **Raw:** `{"block_text": "y BISCUITS\nDARE\n\nPETITS PLAISIRS\nNORMANDIE,\nSUPREME,\nMAXI-FRUITS,\nMETEO\nCOOKIES\n\n280 à/to 310 a", "ocr_lines": ["BISCUITS", "DARE", "PETITSPLAISIRS", "MAND", "SUPREME,", "MAXI-FRUITS.", "COOKIES"], "harvest": {"size": "310g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Dare Petits Plaisirs cookies (280-310 g) at 2.22 — the flyer's price-point style, verified on the crop (reg. 4.79-4.99). Crackers & Cookies is right.

### Item 9694

![item 9694](images/item-9694.jpg)

- **Name (English):** None
- **Name (French):** BLEUETS
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** 170g
- **Price:** 2.77
- **Printed Price:** “2.77”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 853, top 343, right 990, bottom 423, page 1
- **Full page:** [pages/flyer57-page1-2ba4109ffb.jpg (flyer page 1)](pages/flyer57-page1-2ba4109ffb.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `db178fac10f880c2`
- **Raw:** `{"block_text": "BLEUETS\n’roduit du Pérou\njorie no 1 Grade\n\nBLUEBERRIES\nProduct nf Por:", "ocr_lines": ["BLEUETS", "BLUEBERRIES"], "harvest": {"size": "170g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Blueberries (Peru, grade 1, 170 g) at 2.77 — verified. Fresh Fruits is right.

### Item 9699

![item 9699](images/item-9699.jpg)

- **Name (English):** None
- **Name (French):** BARRES BARS
- **Brand:** None
- **Category (English):** Pantry > Cereal & Breakfast
- **Category (French):** Produits du garde-manger > Céréales et petits-déjeuners
- **How classified:** rule (`specific-protein-bars`)
- **Size:** None
- **Price:** 2.33
- **Printed Price:** “2.33”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 394, top 296, right 653, bottom 329, page 2
- **Full page:** [pages/flyer57-page2-3a3c255d21.jpg (flyer page 2)](pages/flyer57-page2-3a3c255d21.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `646d4c44a9c7cd8e`
- **Raw:** `{"block_text": "BARRES\nQUAKER\nCHEWY, DIP\nLECLERC\nCHOCOMA)\nBARS\n\n1390 over 1", "ocr_lines": ["BARRES", "BARS"]}`

**Item Review Analysis (Pass 1):** Correct. Quaker Chewy/Dipps or Leclerc Chocomax bars (120-175 g) at 2.33 — verified. Cereal & Breakfast is right.

### Item 9700

![item 9700](images/item-9700.jpg)

- **Name (English):** None
- **Name (French):** SOUPE SOUP
- **Brand:** None
- **Category (English):** Prepared Meals > Salads & Soups
- **Category (French):** Repas préparés > Salades et soupes
- **How classified:** rule (`salads-soups`)
- **Size:** 284mL
- **Price:** 1.25
- **Printed Price:** “1.25”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 869, top 605, right 978, bottom 672, page 2
- **Full page:** [pages/flyer57-page2-3a3c255d21.jpg (flyer page 2)](pages/flyer57-page2-3a3c255d21.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `49c983a3c74ddba9`
- **Raw:** `{"block_text": "_ SOUPE\nAMPBELL'S\nSOUP\n\n924 mi", "ocr_lines": ["SOUPE", "SOUP"], "harvest": {"size": "284mL", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Campbell's soup (284 ml) at 1.25 — verified. Salads & Soups is right.

### Item 9708

![item 9708](images/item-9708.jpg)

- **Name (English):** RICARDO \ FRESH FLATTENED | CHICKEN
- **Name (French):** POULET CRAPAUDINE FRAIS \
- **Brand:** None
- **Category (English):** Meat > Chicken & Turkey
- **Category (French):** Viande > Poulet et dinde
- **How classified:** rule (`chicken-turkey`)
- **Size:** None
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 215, top 242, right 333, bottom 326, page 3
- **Full page:** [pages/flyer57-page3-2a18259968.jpg (flyer page 3)](pages/flyer57-page3-2a18259968.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `1c98f5dbc7a8bae6`
- **Raw:** `{"block_text": "_\nPOULET\nCRAPAUDINE FRAIS\n\\ | RICARDO\n\\ FRESH FLATTENED\n| CHICKEN\nL Sélection variée", "ocr_lines": ["POULET", "CRAPAUDINEFRAIS", "RICARDO", "CHICKEN"]}`

**Item Review Analysis (Pass 1):** Correct. Ricardo fresh flattened chicken at 6.99/lb (15.41/kg) — verified. Chicken & Turkey is right.

### Item 9713

![item 9713](images/item-9713.jpg)

- **Name (English):** None
- **Name (French):** FILETS DE POISSON PANES SURGELÉS ( JANES ULTIMES,LÉGÉREMENT SAUPOUDRÉE
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Meat and Seafood
- **Category (French):** Produits surgelés > Viande et fruits de mer surgelés
- **How classified:** frozen-remap (`fish`)
- **Size:** 590g
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 138, top 320, right 366, bottom 365, page 4
- **Full page:** [pages/flyer57-page4-b147e9975a.jpg (flyer page 4)](pages/flyer57-page4-b147e9975a.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `42bcc1fbcbd443d3`
- **Raw:** `{"block_text": "FILETS DE POISSON\nPANES SURGELÉS (\nJANES\nULTIMES,LÉGÉREMENT\nSAUPOUDRÉE\n\nFROZEN BREADED\n\nFISH FILLETS\n\n450 to 590 a", "ocr_lines": ["FILETSDEPOISSON", "PANESSURGELES", "ANES", "ULTIMES.LEGEREMENT", "SAUPOUDREE", "FROZENBREADED", "FISHFILLETS"], "harvest": {"size": "590g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Janes frozen breaded fish fillets (450-590 g) print 15.99; the DB had 5.99 (leading digit lost). Frozen Meat and Seafood is right.

### Item 9722

![item 9722](images/item-9722.jpg)

- **Name (English):** None
- **Name (French):** VOL-AU-VENT ST-HUBERT PASTRY SHELLS
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Appetizers & Snacks
- **Category (French):** Produits surgelés > Entrées et collations surgelés
- **How classified:** rule (`frozen-appetizers`)
- **Size:** 150g
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 339, top 72, right 453, bottom 134, page 4
- **Full page:** [pages/flyer57-page4-b147e9975a.jpg (flyer page 4)](pages/flyer57-page4-b147e9975a.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `04407e899e84c335`
- **Raw:** `{"block_text": "VOL-AU-VENT\nST-HUBERT\nPASTRY SHELLS\nEmballace de 6", "ocr_lines": ["VOL-AU-VENT", "ST-HUBERT", "PASTRYSHELLS"], "harvest": {"size": "150g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. St-Hubert vol-au-vent pastry shells (pack of 6, 150 g) at 6.99 — verified. Frozen Appetizers & Snacks is right.

### Item 9737

![item 9737](images/item-9737.jpg)

- **Name (English):** None
- **Name (French):** 1 «JUS DE FRUITS _ ou COCKTAN DE, — LÉGUME
- **Brand:** None
- **Category (English):** Drinks > Juice
- **Category (French):** Boissons > Jus
- **How classified:** rule (`juice`)
- **Size:** 8X200 mL
- **Price:** 4.29
- **Printed Price:** “4.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 714, top 287, right 799, bottom 404, page 5
- **Full page:** [pages/flyer57-page5-fe218909dc.jpg (flyer page 5)](pages/flyer57-page5-fe218909dc.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/05.webp
- **Details:** confidence: 0.99 · item_key: `74f4a06024028dfe`
- **Raw:** `{"block_text": "Wer procets | DE\nnn D'LA Gi | ~\nLe. ;\nwe: le.\n1 «JUS DE FRUITS _\nou COCKTAN DE,\n— LÉGUME\nA® oasis\nROUGEMONT _\nD NECTAR\n“gel DEL MONTE «\nAou THÉ GLACE |\n~ ARIZONA\n1 aoe\nOR VEGETABLE ©\nCOCKTAIL, NECTAR\n[OR ICED TEA\n8X200 mL.", "ocr_lines": ["D'ICI", "JUSDEFRUITS", "OUCOCKTAILDE", "LEGUMES", "OASIS", "ROUGEMONT", "NECTAR", "DELMONTE", "ARIZONA", "FRUITJUICE", "ORVEGETABLE", "COCKTAIL,NECTAR", "ORICEDTEA"]}`

**Item Review Analysis (Pass 1):** Correct. Oasis fruit juice / Rougemont nectar / Del Monte or Arizona (8 x 200 ml) at 4.29 — verified. Juice is right.

### Item 9753

![item 9753](images/item-9753.jpg)

- **Name (English):** None
- **Name (French):** FARINE COMPLIMENTS FLOUR
- **Brand:** None
- **Category (English):** Pantry > Baking Essentials
- **Category (French):** Produits du garde-manger > Essentiels de cuisson
- **How classified:** rule (`baking`)
- **Size:** 2,5kg
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 880, top 929, right 977, bottom 980, page 6
- **Full page:** [pages/flyer57-page6-4563dbf93d.jpg (flyer page 6)](pages/flyer57-page6-4563dbf93d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/06.webp
- **Details:** confidence: 0.99 · item_key: `8235fc696369f350`
- **Raw:** `{"block_text": "FARINE\nCOMPLIMENTS\nFLOUR", "ocr_lines": ["FARINE", "COMPL"], "harvest": {"size": "2,5kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Compliments flour (2.5 kg) at 3.99 (reg. 4.79) — verified. Baking Essentials is right.

### Item 9754

![item 9754](images/item-9754.jpg)

- **Name (English):** None
- **Name (French):** EAU DE SOURCE NATURELLE COMPLIMENTS NATURAL SPRING WATER
- **Brand:** None
- **Category (English):** Drinks > Water
- **Category (French):** Boissons > Eau
- **How classified:** rule (`water`)
- **Size:** 12x500mL
- **Price:** 3.29
- **Printed Price:** “3.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 719, top 626, right 978, bottom 664, page 6
- **Full page:** [pages/flyer57-page6-4563dbf93d.jpg (flyer page 6)](pages/flyer57-page6-4563dbf93d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/06.webp
- **Details:** confidence: 0.99 · item_key: `e0061bb15a1900ca`
- **Raw:** `{"block_text": "EAU DE SOURCE NATURELLE\nCOMPLIMENTS\n\nNATURAL SPRING WATER\n2x500mt", "ocr_lines": ["EAUDESOURCE NATURELLE", "NATURALSPRING WATER"], "harvest": {"size": "12x500mL", "via": "crop"}}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 57 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Compliments spring water (12 x 500 ml) at 3.29 — verified. Water is right.

### Item 9703

![item 9703](images/item-9703.jpg)

- **Name (English):** MONTELLIER | =
- **Name (French):** ~—
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 10 x 355 mL
- **Price:** 17.00
- **Printed Price:** “17.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 94, top 918, right 441, bottom 982, page 3
- **Full page:** [pages/flyer57-page3-2a18259968.jpg (flyer page 3)](pages/flyer57-page3-2a18259968.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `3d5665085bd249fe`
- **Raw:** `{"block_text": "\"779 LELTT 2 ill : | Sa\n~— | MONTELLIER | =\nMot produats\nBOISSON A BASE D'ICI\nD'EAU PÉTILLANTE\nBUBLY (12 x 355 mL)\nOU EAU DE SOURCE =\nNATURELLE GAZÉIFIÉE\nMONTELLIER (10 x 355 mL)\nCARBONATED NATURAL\nSPRING WATER\nOR SPARKLING WATER\nBEVERAGE\nCanettes consianées", "ocr_lines": ["MONTELLiER", "D'ICI", "BOISSONA BASE", "D'EAUPETILLANTE", "BUBLY(12×355mL)", "OUEAUDESOURCE", "NATURELLEGAZEIFIEE", "MONTELLIER（10x355mL)", "CARBONATEDNATURAL", "SPRINGWATER", "ORSPARKLINGWATER"`

— from flyer 57 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Bubly (12 x 355 ml) or Montellier (10 x 355 ml) sparkling water prints "2/17.00 ou 9.99"; the DB stored the 17.00 total under a garbled name ("~—"). Now 9.99 with the multibuy recorded. The name garble keeps it unclassified.

### Item 9704

![item 9704](images/item-9704.jpg)

- **Name (English):** None
- **Name (French):** : HUMPTY DUMPTY
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 300 g
- **Price:** 7.29
- **Printed Price:** “7.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 373, top 879, right 655, bottom 980, page 3
- **Full page:** [pages/flyer57-page3-2a18259968.jpg (flyer page 3)](pages/flyer57-page3-2a18259968.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `ec88af220c425ee6`
- **Raw:** `{"block_text": "ye ae MNIVUING tives\n: HUMPTY DUMPTY\n‘il LE (250 a/to 300 g)\nou mais A ECLATER\na J) ORVILLE REDENBACHER\n“3 x 82 g ou/or 116 a/to 220 g)\nSNACKS OR POPCORN\nRén © 40¢4 € 006", "ocr_lines": ["HUMPTYDUMPTY", "OUMAISAECLATER", "ORVILLEREDENBACHER", "SNACKSORPOPCORN"]}`

— from flyer 57 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 3. Humpty Dumpty snacks or Orville popcorn (reg. 5.49-5.99) sell at 3.99 — the badge under the products; the DB had 7.29, the Montellier water's badge from the left. Name is the brand fragment; price now right.

### Item 9716

![item 9716](images/item-9716.jpg)

- **Name (English):** None
- **Name (French):** AFFINE EN
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 8.49
- **Printed Price:** “8.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 801, top 694, right 981, bottom 746, page 4
- **Full page:** [pages/flyer57-page4-b147e9975a.jpg (flyer page 4)](pages/flyer57-page4-b147e9975a.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `de97263b7acaccec`
- **Raw:** `{"block_text": "sp =\n\nAFFINE EN\n\nSor Suna niente\n20° es", "ocr_lines": ["FROMAGEAPATEMOLLE", "AFFINE EN SURFACE", "SOFTSURFACERIPEEDCHEESE"]}`

— from flyer 57 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Price correct, name a label fragment. A soft surface-ripened cheese (180 g, "Fromage Le Sœur…") at 8.49 — verified on the crop; the stored name ("AFFINE EN") is the label's middle line, so it sits unclassified.

### Item 9726

![item 9726](images/item-9726.jpg)

- **Name (English):** None
- **Name (French):** FRIANDIS! Es 3 OCKETS (50 0g)
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 0g
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 37, top 818, right 250, bottom 859, page 5
- **Full page:** [pages/flyer57-page5-fe218909dc.jpg (flyer page 5)](pages/flyer57-page5-fe218909dc.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/05.webp
- **Details:** confidence: 0.99 · item_key: `6fc24fc9f7702f7f`
- **Raw:** `{"block_text": "FRIANDIS! Es\n3 OCKETS (50 0g)\n\nous UCONS\n\nOMPLIN ENTS (100 u nites\nTREA TS OR LOLLIPOPS:\nRéa 6996", "ocr_lines": ["FRIANDISES", "ROCKETS(500g）", "OUSUCONS", "TREATSORLOLLIPOPS"]}`

— from flyer 57 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Rockets candy rolls (500 g) or Compliments lollipops (100 units) at 5.99 (reg. 6.99) — verified; the name is a garbled fragment, price is the cell's own.

### Item 9746

![item 9746](images/item-9746.jpg)

- **Name (English):** None
- **Name (French):** SHERY!
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
- **bbox:** left 542, top 744, right 646, bottom 840, page 5
- **Full page:** [pages/flyer57-page5-fe218909dc.jpg (flyer page 5)](pages/flyer57-page5-fe218909dc.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/05.webp
- **Details:** confidence: 0.99 · item_key: `705cdcc9514a7780`
- **Raw:** `{"block_text": null, "ocr_lines": ["SHERY!"]}`

— from flyer 57 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 5. Hershey's snack-size treats, 50 count (reg. 13.99), sell at 12.49 — the DB had taken the bag's big "50" count as the price. The name fragment ("SHERY!") keeps it unclassified.

### Item 9757

![item 9757](images/item-9757.jpg)

- **Name (English):** None
- **Name (French):** ASSIETTES COMPOSTABLES HEFTY ECOSAVE (20) RECYCLABLE PLATES
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 6.00
- **Printed Price:** “6”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 218, top 771, right 358, bottom 839, page 7
- **Full page:** [pages/flyer57-page7-c0f4481468.jpg (flyer page 7)](pages/flyer57-page7-c0f4481468.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/07.webp
- **Details:** confidence: 0.54 · item_key: `ca580cd25963cef4`
- **Raw:** `{"block_text": "ASSIETTES\nCOMPOSTABLES\nHEFTY ECOSAVE (20)\n\nRECYCLABLE PLATES\nRéa 6 996", "ocr_lines": ["ASSIETTES", "COMPOSTABLES", "HEFTY ECOSAVE(20)", "RECYCLABLEPLATES"]}`

— from flyer 57 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Hefty EcoSave compostable plates (20) print 4.99 (reg. 6.99); the DB had 6.00. A household item kept unclassified for review, per the standing rule — noted, not discarded.

### Item 9765

![item 9765](images/item-9765.jpg)

- **Name (English):** None
- **Name (French):** CIARK L CLASSIQUE] SIROP D'ÉRABL!
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 710ml
- **Price:** 4.49
- **Printed Price:** “4.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 312, top 512, right 528, bottom 637, page 7
- **Full page:** [pages/flyer57-page7-c0f4481468.jpg (flyer page 7)](pages/flyer57-page7-c0f4481468.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-bonichoix-du-15-au-21-octobre-2026/07.webp
- **Details:** confidence: 0.99 · item_key: `d3fb7575ea7a3751`
- **Raw:** `{"block_text": "DE\nCIARK\n\nL CLASSIQUE]\nSIROP D'ÉRABL!", "ocr_lines": ["D'ICI", "CLARK", "CLASSIQUE", "SIROP D'ERABLE"], "harvest": {"size": "710ml", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 7. Clark maple-flavoured beans (398 ml) print 1.99 (reg. 2.79); the DB had 4.49 — the bakery box's price above. The name garble ("CIARK L CLASSIQUE] SIROP D'ÉRABL!") keeps it unclassified.
