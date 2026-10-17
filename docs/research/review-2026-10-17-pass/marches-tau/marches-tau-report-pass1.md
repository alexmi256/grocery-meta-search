# Les Marchés Tau — full product report

Store slug: `marches-tau`. Generated from `data/grocery.db`. A sampled subset of 20 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 92, valid 2026-10-05 → 2026-11-15 — a six-week catalogue, still current; 35 items, of which the sample draws 10 + 10). No other edition exists to exclude.
- **Sample counts:** 10 classified + 10 unclassified shown, as drawn — the unclassified half is this catalogue's character: glued bilingual names ("BOISSOND'AMANDE", "FARINEBIOLOGIQUETOUTUSAGE") defeat the token classifier, and the catalogue carries supplements and household items alongside food.
- **Issues found:** 4 wrong prices and 1 duplicate. The Oatly barista oat drink stored 1.99 for a printed 4.99; the vegetable acras stored a round 10.00 for 9.99; the hand-soap item carried the Ester-C vitamin's 22.99 (its own price is 6.99, proven by the flour item's crop, where the soap's badge sits); the Abénakis flour carried that same 6.99 (its own badge is 4.49) — a two-item price rotation on page 1. Item 11030 ("MILK CHOCOLATE +PROTEIN") is a second capture of the Little Cacao chocolate bar from its packaging text, priced with the coffee beans' 14.99; the bar is properly carried by item 11033, so 11030 is deleted. Multibuy splits elsewhere are faithful (Bloom 2/5$ → 2.50, tuna 2/7$ → 3.50, pasta 3/8$ → 2.67, tomatoes 2/5$ → 2.50).
- **Fixes applied this pass:** 11021 → 6.99, 11023 → 4.49, 11035 → 4.99, 11043 → 9.99; item 11030 deleted (duplicate).

## Flyer 92 — valid 2026-10-05 → 2026-11-15 (10 classified items, 10 unclassified)

Source ref: `circulaire-marches-tau-du-5-octobre-au-15-novembre-2026` · fetched 2026-10-13T23:10:10.683Z

### Item 11025

![item 11025](images/item-11025.jpg)

- **Name (English):** None
- **Name (French):** BLOOM BOISSON ENERGETIQUE NATURELLE
- **Brand:** None
- **Category (English):** Drinks > Sports & Energy
- **Category (French):** Boissons > Boissons énergisantes et pour sportifs
- **How classified:** rule (`sports-energy`)
- **Size:** 355 ML
- **Price:** 2.50
- **Printed Price:** “2/5.00”
- **Unit quantity:** 2.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 446, top 799, right 591, bottom 929, page 1
- **Full page:** [pages/flyer92-page1-a53f9f6b55.jpg (flyer page 1)](pages/flyer92-page1-a53f9f6b55.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `a0a696ba9c4db64e`
- **Conditions:** `{"multibuy": {"count": 2, "total": 5.0}}`
- **Raw:** `{"block_text": "BLOOM\n\nBOISSON ÉNERGÉTIQUE\nNATURELLE\n\nNATURAL ENERGY DRINK", "ocr_lines": ["BLOOM", "BOISSON ENERGETIQUE", "NATURELLE", "NATURALENERGYDRINK"], "harvest": {"size": "355 ML", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Bloom natural energy drink (355 ml) prints "2/5$"; the stored 2.50 is the split. Sports & Energy is right.

### Item 11029

![item 11029](images/item-11029.jpg)

- **Name (English):** None
- **Name (French):** CALIFIAFARM BOISSOND'AMANDE ALMOND BEVERAGE
- **Brand:** None
- **Category (English):** Dairy & Eggs > Non-Dairy Milk Alternatives
- **Category (French):** Produits laitiers et œufs > Laits non laitiers
- **How classified:** rule (`non-dairy-milk`)
- **Size:** 1.4L
- **Price:** 5.49
- **Printed Price:** “5.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 852, top 581, right 962, bottom 721, page 2
- **Full page:** [pages/flyer92-page2-ba23d7ffb3.jpg (flyer page 2)](pages/flyer92-page2-ba23d7ffb3.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `132516c6ee24f071`
- **Raw:** `{"block_text": "CALIFIA FARM\nBOISSON D'AMANDE\nALMOND BEVERAGE\nCERTAINES VARIETES\nSELECTED VARIETIES", "ocr_lines": ["CALIFIAFARM", "BOISSOND'AMANDE", "ALMOND BEVERAGE", "CERTAINESVARIETES", "SELECTEDVARIETIES"], "harvest": {"size": "1.4L", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Califia Farms almond beverage (1.4 L) at 5.49 — verified. Non-Dairy Milk Alternatives is right.

### Item 11030

![item 11030](images/item-11030.jpg)

- **Name (English):** None
- **Name (French):** MILK CHOCOLATE +PROTEIN +PROTEINE
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`specific-chocolat-au-lait`)
- **Size:** None
- **Price:** 14.99
- **Printed Price:** “14.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 250, top 859, right 495, bottom 922, page 2
- **Full page:** [pages/flyer92-page2-ba23d7ffb3.jpg (flyer page 2)](pages/flyer92-page2-ba23d7ffb3.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `1f6dffc49657cb81`
- **Raw:** `{"block_text": "Me Seger Attet\nMILK CHOCOLATE\n+PROTEIN\n| +PROTEINE\n| CHOCOLAT » LAIT\neme verre", "ocr_lines": ["MILK CHOCOLATE", "+PROTEIN", "+PROTEINE", "CHOCOLAT-LAIT"]}`

**Item Review Analysis (Pass 1):** DELETED — duplicate. This "item" is the Little Cacao protein milk-chocolate bar read from its packaging text, priced with the Barista coffee beans' 14.99 from the cell to its left. The same bar is properly carried by item 11033 (full name, 6.99).

### Item 11031

![item 11031](images/item-11031.jpg)

- **Name (English):** None
- **Name (French):** KICKINGHORSE CAFE EN GRAINS BIOLOGIQUE
- **Brand:** None
- **Category (English):** Drinks > Coffee
- **Category (French):** Boissons > Cafés
- **How classified:** rule (`coffee`)
- **Size:** 454G
- **Price:** 23.99
- **Printed Price:** “23.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 829, top 760, right 982, bottom 919, page 2
- **Full page:** [pages/flyer92-page2-ba23d7ffb3.jpg (flyer page 2)](pages/flyer92-page2-ba23d7ffb3.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `00c378d7ebf19e4f`
- **Raw:** `{"block_text": "KICKING HORSE\n\nCAFE EN GRAINS\nBIOLOGIQUE\nORGANIC COFFEE\nBEANS MIX wa", "ocr_lines": ["KICKINGHORSE", "CAFE EN GRAINS", "BIOLOGIQUE", "ORGANICCOFFEE", "BEANSMIX"], "harvest": {"size": "454G", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Kicking Horse organic coffee beans (454 g) at 23.99 (save 6$) — verified. Coffee is right.

### Item 11033

![item 11033](images/item-11033.jpg)

- **Name (English):** None
- **Name (French):** THE LITTLECACAO CHOCOLATAU LAITSANS SUCRE AJOUTEPROTEINE
- **Brand:** None
- **Category (English):** Pantry > Baking Essentials
- **Category (French):** Produits du garde-manger > Essentiels de cuisson
- **How classified:** rule (`baking`)
- **Size:** 70 G
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 543, top 761, right 674, bottom 921, page 2
- **Full page:** [pages/flyer92-page2-ba23d7ffb3.jpg (flyer page 2)](pages/flyer92-page2-ba23d7ffb3.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/02.webp
- **Details:** confidence: 0.98 · item_key: `744dc32840cdb2ae`
- **Raw:** `{"block_text": "THE LITTLE CACAO\n\nCHOCOLAT AU LAIT SANS\nSUCRE AJOUTE PROTEINE\nNO ADDED SUGAR\nPROTEIN\n\nCHOCOLATE", "ocr_lines": ["THE LITTLECACAO", "CHOCOLATAU LAITSANS", "SUCRE AJOUTEPROTEINE", "NO ADDED SUGAR", "PROTEIN", "CHOCOLATE"], "harvest": {"size": "70 G", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. The Little Cacao no-added-sugar protein milk chocolate (70 g) at 6.99 — verified. (Shelved under Baking Essentials on the cacao wording; the bar itself is a snack — text result, left.)

### Item 11035

![item 11035](images/item-11035.jpg)

- **Name (English):** None
- **Name (French):** OAT-LY BOISSOND'AVOINE BARISTA
- **Brand:** None
- **Category (English):** Dairy & Eggs > Non-Dairy Milk Alternatives
- **Category (French):** Produits laitiers et œufs > Laits non laitiers
- **How classified:** rule (`non-dairy-milk`)
- **Size:** None
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 561, top 585, right 667, bottom 694, page 2
- **Full page:** [pages/flyer92-page2-ba23d7ffb3.jpg (flyer page 2)](pages/flyer92-page2-ba23d7ffb3.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/02.webp
- **Details:** confidence: 0.85 · item_key: `9636056ee517dcbd`
- **Raw:** `{"block_text": "OAT-LY\n\nBOISSON D’AVOINE\nBARISTA\n\nOAT DRINK BARISTA", "ocr_lines": ["OAT-LY", "BOISSOND'AVOINE", "BARISTA", "OATDRINK BARISTA"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Oatly barista oat drink prints 4.99; the DB had 1.99. Non-Dairy Milk Alternatives is right.

### Item 11039

![item 11039](images/item-11039.jpg)

- **Name (English):** None
- **Name (French):** TAU PATES BIOLOGIQUES ORGANICPASTA
- **Brand:** None
- **Category (English):** Pantry > Pasta & Pasta Sauce
- **Category (French):** Produits du garde-manger > Pâtes et sauces
- **How classified:** rule (`specific-pasta`)
- **Size:** 500G
- **Price:** 2.67
- **Printed Price:** “3/8.00”
- **Unit quantity:** 3.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 708, top 34, right 831, bottom 164, page 3
- **Full page:** [pages/flyer92-page3-862e94e966.jpg (flyer page 3)](pages/flyer92-page3-862e94e966.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/03.webp
- **Details:** confidence: 0.97 · item_key: `e07ad4d0f44523e8`
- **Conditions:** `{"multibuy": {"count": 3, "total": 8.0}}`
- **Raw:** `{"block_text": "TAU =\nPATES BIOLOGIQUES\nORGANICPASTA\nCERTAINES VARIÉTÉS\nSELECTED VARIETIES", "ocr_lines": ["TAU", "PATES BIOLOGIQUES", "ORGANICPASTA", "CERTAINESVARIETES", "SELECTEDVARIETIES"], "harvest": {"size": "500G", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Tau organic pasta (500 g) prints "3/8$"; the stored 2.67 is the split. Pasta & Pasta Sauce is right.

### Item 11049

![item 11049](images/item-11049.jpg)

- **Name (English):** None
- **Name (French):** CHIWIS CROUSTILLES DEFRUITS FRUITSCHIPS
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Chips & Snacks
- **Category (French):** Grignotines, croustilles et friandises > Croustilles et grignotines
- **How classified:** rule (`specific-snacks`)
- **Size:** 50G
- **Price:** 5.49
- **Printed Price:** “5.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 224, top 605, right 357, bottom 723, page 4
- **Full page:** [pages/flyer92-page4-0a4a96a2cc.jpg (flyer page 4)](pages/flyer92-page4-0a4a96a2cc.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `02880d5ae4890915`
- **Raw:** `{"block_text": "| CHIWIS\nCROUSTILLES DE FRUITS\nFRUITS CHIPS", "ocr_lines": ["CHIWIS", "CROUSTILLES DEFRUITS", "FRUITSCHIPS"], "harvest": {"size": "50G", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Chiwis fruit chips (50 g) at 5.49 — verified. Chips & Snacks is right.

### Item 11051

![item 11051](images/item-11051.jpg)

- **Name (English):** None
- **Name (French):** Seta matcha LATTE
- **Brand:** None
- **Category (English):** Drinks > Tea & Hot Drinks
- **Category (French):** Boissons > Thés et boissons chaudes
- **How classified:** rule (`tea-hot-drinks`)
- **Size:** 110G
- **Price:** 21.99
- **Printed Price:** “21.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 702, top 795, right 943, bottom 918, page 4
- **Full page:** [pages/flyer92-page4-0a4a96a2cc.jpg (flyer page 4)](pages/flyer92-page4-0a4a96a2cc.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `996d7db097a1c2c5`
- **Raw:** `{"block_text": "Seba\nLATTE", "ocr_lines": ["Seta", "matcha", "LATTE"], "harvest": {"size": "110G", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Seta Organic matcha latte (110 g) at 21.99 — verified. Tea & Hot Drinks is right.

### Item 11053

![item 11053](images/item-11053.jpg)

- **Name (English):** None
- **Name (French):** DELICIA BOISSON CHOCOLAT CHAUDA LA DATTE
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 300 G
- **Price:** 10.99
- **Printed Price:** “10.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 505, top 766, right 644, bottom 918, page 4
- **Full page:** [pages/flyer92-page4-0a4a96a2cc.jpg (flyer page 4)](pages/flyer92-page4-0a4a96a2cc.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `0c9e14d9d4a1b7b8`
- **Raw:** `{"block_text": "DELICIA\n\nBOISSON CHOCOLAT\nCHAUD A LA DATTE\nDATE HOT CHOCOLATE\nDRINK", "ocr_lines": ["DELICIA", "BOISSON CHOCOLAT", "CHAUDA LA DATTE", "DATE HOT CHOCOLATE", "DRINK"], "harvest": {"size": "300 G", "via": "crop"}}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 92 (valid 2026-10-05 → 2026-11-15)

**Item Review Analysis (Pass 1):** Correct. Delicia date hot chocolate drink (300 g) at 10.99 — verified. (Shelved under Candy & Chocolate on the chocolate wording.)

### Item 11020

![item 11020](images/item-11020.jpg)

- **Name (English):** None
- **Name (French):** O'MER THONSAUVAGEALBACORE WILDALBACORETUNA
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 3.50
- **Printed Price:** “2/7.00”
- **Unit quantity:** 2.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 372, top 643, right 635, bottom 709, page 1
- **Full page:** [pages/flyer92-page1-a53f9f6b55.jpg (flyer page 1)](pages/flyer92-page1-a53f9f6b55.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/01.webp
- **Details:** confidence: 0.98 · item_key: `e153ff726369469f`
- **Conditions:** `{"multibuy": {"count": 2, "total": 7.0}}`
- **Raw:** `{"block_text": "O'MER |\nTHON SAUVAGE ALBACORE\nWILD ALBACORE TUNA", "ocr_lines": ["O'MER", "THONSAUVAGEALBACORE", "WILDALBACORETUNA"]}`

— from flyer 92 (valid 2026-10-05 → 2026-11-15)

**Item Review Analysis (Pass 1):** Correct. O'Mer wild albacore tuna (111 g) prints "2/7$"; the stored 3.50 is the split. Unclassified under its glued bilingual name.

### Item 11021

![item 11021](images/item-11021.jpg)

- **Name (English):** None
- **Name (French):** 90COMP/TABS THE UNSCENTED SAVONAMAINOU
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 500MG
- **Price:** 22.99
- **Printed Price:** “22.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 327, top 217, right 469, bottom 428, page 1
- **Full page:** [pages/flyer92-page1-a53f9f6b55.jpg (flyer page 1)](pages/flyer92-page1-a53f9f6b55.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `7871594d21f839e0`
- **Raw:** `{"block_text": "soul pais “A\nTHE UNSCENTED\nSAVON À MAIN OU\nBARRE DÉTACHANTE\nHAND SOAP OR STAIN\nREMOVER BAR\nCERTAINES VARIETES\nSELECTED VARIETIES |", "ocr_lines": ["90COMP/TABS", "THE UNSCENTED", "SAVONAMAINOU", "BARREDETACHANTE", "HAND SOAPORSTAIN", "REMOVERBAR", "CERTAINESVARIETES", "SELECTEDVARIETIES", "THE", "UNSCENTED", "COMPANY`"], "harvest": {"size": "500MG", "via": "crop"}}`

— from flyer 92 (valid 2026-10-05 → 2026-11-15)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from item 11023's crop. The Unscented Company hand soap / stain-remover bar prints 6.99; the DB had 22.99 — the Sisu Ester-C 500 mg price from the product above. A household item, unclassified; kept for review under the standing rule.

### Item 11023

![item 11023](images/item-11023.jpg)

- **Name (English):** None
- **Name (French):** ABENAKIS FARINEBIOLOGIQUETOUTUSAGE ORGANICALLPURPOSEFLOUR
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 434, top 467, right 738, bottom 550, page 1
- **Full page:** [pages/flyer92-page1-a53f9f6b55.jpg (flyer page 1)](pages/flyer92-page1-a53f9f6b55.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `41167da6d4ea72fb`
- **Raw:** `{"block_text": "ABÉNAKIS En TK\nFARINE BIOLOGIQUE TOUT USAGE\nORGANIC ALL PURPOSE FLOUR", "ocr_lines": ["ABENAKIS", "FARINEBIOLOGIQUETOUTUSAGE", "ORGANICALLPURPOSEFLOUR"]}`

— from flyer 92 (valid 2026-10-05 → 2026-11-15)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Abénakis organic all-purpose flour (1 kg) prints 4.49; the DB had 6.99 — the hand soap's badge to its left. Unclassified under its glued name ("FARINEBIOLOGIQUETOUTUSAGE").

### Item 11027

![item 11027](images/item-11027.jpg)

- **Name (English):** None
- **Name (French):** VITAMINEC Ester-C600mg VITAMINC
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 600mg
- **Price:** 29.99
- **Printed Price:** “29.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 546, top 151, right 719, bottom 266, page 1
- **Full page:** [pages/flyer92-page1-a53f9f6b55.jpg (flyer page 1)](pages/flyer92-page1-a53f9f6b55.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `fbc635d68869b154`
- **Raw:** `{"block_text": "PE «ia\n‘Wi Te\nEster-C vl NEX\n<a 600M6 2%\nge VITAMING", "ocr_lines": ["VITAMINEC", "Ester-C600mg", "VITAMINC"]}`

— from flyer 92 (valid 2026-10-05 → 2026-11-15)

**Item Review Analysis (Pass 1):** Correct price. Sisu Ester-C 600 mg (120 vcaps) at 29.99 — verified. A supplement, unclassified (the dosage-form exclusion doesn't fire on this name form).

### Item 11032

![item 11032](images/item-11032.jpg)

- **Name (English):** None
- **Name (French):** PRANA CHIA AU FRIGO BIOLOGIQUE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 250G
- **Price:** 5.49
- **Printed Price:** “5.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 272, top 185, right 371, bottom 319, page 2
- **Full page:** [pages/flyer92-page2-ba23d7ffb3.jpg (flyer page 2)](pages/flyer92-page2-ba23d7ffb3.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `b346e436de9611be`
- **Raw:** `{"block_text": "PRANA\n\nCHIA AU FRIGO\nBIOLOGIQUE\nORGANIC\nOVERNIGHT CHIA", "ocr_lines": ["PRANA", "CHIA AU FRIGO", "BIOLOGIQUE", "ORGANIC", "OVERNIGHT CHIA"], "harvest": {"size": "250G", "via": "crop"}}`

— from flyer 92 (valid 2026-10-05 → 2026-11-15)

**Item Review Analysis (Pass 1):** Correct. Prana organic overnight chia (250 g) at 5.49 — verified. Unclassified under its name form.

### Item 11038

![item 11038](images/item-11038.jpg)

- **Name (English):** None
- **Name (French):** TAU TOMATESBIOLOGIQUES ORGANICTOMATOES
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 398ML
- **Price:** 2.50
- **Printed Price:** “2/5.00”
- **Unit quantity:** 2.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 163, top 442, right 290, bottom 575, page 3
- **Full page:** [pages/flyer92-page3-862e94e966.jpg (flyer page 3)](pages/flyer92-page3-862e94e966.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/03.webp
- **Details:** confidence: 0.98 · item_key: `abc839f7c7b90cc8`
- **Conditions:** `{"multibuy": {"count": 2, "total": 5.0}}`
- **Raw:** `{"block_text": "TAU\n\nTOMATES BIOLOGIQUES\nORGANIC TOMATOES\nCERTAINES VARIÉTÉS\nSELECTED VARIETIES", "ocr_lines": ["TAU", "TOMATESBIOLOGIQUES", "ORGANICTOMATOES", "CERTAINESVARIETES", "SELECTEDVARIETIES"], "harvest": {"size": "398ML", "via": "crop"}}`

— from flyer 92 (valid 2026-10-05 → 2026-11-15)

**Item Review Analysis (Pass 1):** Correct. Tau organic tomatoes (398 ml) print "2/5$"; the stored 2.50 is the split. Unclassified.

### Item 11043

![item 11043](images/item-11043.jpg)

- **Name (English):** None
- **Name (French):** ACRAMENT'BON ACRASDELEGUMES VEGETABLESACRAS
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 10.00
- **Printed Price:** “10.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 529, top 541, right 658, bottom 643, page 4
- **Full page:** [pages/flyer92-page4-0a4a96a2cc.jpg (flyer page 4)](pages/flyer92-page4-0a4a96a2cc.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `800295d089e7aa15`
- **Raw:** `{"block_text": "ACRAMENT’BON\nACRAS DE LEGUMES\nVEGETABLES ACRAS", "ocr_lines": ["ACRAMENT'BON", "ACRASDELEGUMES", "VEGETABLESACRAS"]}`

— from flyer 92 (valid 2026-10-05 → 2026-11-15)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 4. Acrament'Bon vegetable acras (300 g) print 9.99 (save 3$); the DB had a round 10.00. Unclassified under its glued name.

### Item 11045

![item 11045](images/item-11045.jpg)

- **Name (English):** None
- **Name (French):** mitsoh PEMMICAN STRIP
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 23G
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 136, top 356, right 322, bottom 517, page 4
- **Full page:** [pages/flyer92-page4-0a4a96a2cc.jpg (flyer page 4)](pages/flyer92-page4-0a4a96a2cc.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `58816824a5c8197f`
- **Raw:** `{"block_text": "PRE\n\nMITSOH\n\nPEMMICAN SANS GLUTEN\n: & SANS SOYA\n= À GLUTEN AND SOY FREE\n= =] PEMMICAN", "ocr_lines": ["mitsoh", "PEMMICAN", "STRIP", "MITSOH", "BLUEBERY", "PEMMICANSANSGLUTEN", "&SANSSOYA", "GLUTEN ANDSOYFREE", "PEMMICAN"], "harvest": {"size": "23G", "via": "crop"}}`

— from flyer 92 (valid 2026-10-05 → 2026-11-15)

**Item Review Analysis (Pass 1):** Correct. Mitsoh pemmican strip (gluten/soy-free, 23 g) at 4.99 — verified. Unclassified.

### Item 11047

![item 11047](images/item-11047.jpg)

- **Name (English):** None
- **Name (French):** OLIVEITUP OLIVESDENOYAUTEES FRAICHES
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 200 G
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 518, top 384, right 639, bottom 519, page 4
- **Full page:** [pages/flyer92-page4-0a4a96a2cc.jpg (flyer page 4)](pages/flyer92-page4-0a4a96a2cc.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/04.webp
- **Details:** confidence: 0.86 · item_key: `1f1d50bccac4a897`
- **Raw:** `{"block_text": "OLIVE IT UP\n\nOLIVES DENOYAUTEES\nFRAICHES\n\nPITTED GREEN FRESH\nOLIVES", "ocr_lines": ["OLIVEITUP", "OLIVESDENOYAUTEES", "FRAICHES", "PITTED GREEN FRESH", "OLIVES"], "harvest": {"size": "200 G", "via": "crop"}}`

— from flyer 92 (valid 2026-10-05 → 2026-11-15)

**Item Review Analysis (Pass 1):** Correct. Olive It Up fresh pitted green olives (200 g) at 4.99 — verified. Unclassified under its glued name.

### Item 11048

![item 11048](images/item-11048.jpg)

- **Name (English):** None
- **Name (French):** TENDANCE TRENDY
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 290G
- **Price:** 8.99
- **Printed Price:** “8.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-05 → 2026-11-15
- **bbox:** left 815, top 614, right 930, bottom 718, page 4
- **Full page:** [pages/flyer92-page4-0a4a96a2cc.jpg (flyer page 4)](pages/flyer92-page4-0a4a96a2cc.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marches-tau-du-5-octobre-au-15-novembre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `e29079ed569efdd2`
- **Raw:** `{"block_text": "TENDANCE\nLe TRENDY y", "ocr_lines": ["TENDANCE", "TRENDY"], "harvest": {"size": "290G", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Price correct, name is a badge. The product is a spicy/smoked honey (290 g) at 8.99; the stored name is just the "TENDANCE / TRENDY" callout printed above the price. Unclassified.
