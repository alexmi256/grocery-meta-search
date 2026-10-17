# L'Intermarché — full product report

Store slug: `l-intermarche`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 126, valid 2026-10-15 → 2026-10-21, 68 items across 5+ pages). The expired Oct 8–14 edition is correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown — classification success on this OCR feed (the flyer is the PC-branded L'Intermarché circular; names stitch FR product lines in caps).
- **Issues found:** 2 wrong prices of 10. The Oasis juice item (13233) carries its right-hand neighbour's price: its name block stitched the juice and the Philadelphia cream cheese into one item and took the cheese's 6.99; the juice's own price is 4.99 (the item is classified and led as the juice, so 4.99 is the right correction). The soft-drink group (13223) stored 1.00 against a printed 1.49. Both corrected from the crops. The multibuy derivations elsewhere are faithful (macaroni 3/4$ → 1.33; candy bags 4/5$ → 1.25 — both verified on their crops).
- **Fixes applied this pass:** 13233 → 4.99, 13223 → 1.49.

## Flyer 126 — valid 2026-10-15 → 2026-10-21 (10 classified items, 0 unclassified)

Source ref: `circulaire-lintermarche-du-15-au-21-octobre-2026` · fetched 2026-10-16T12:21:25.657Z

### Item 13214

![item 13214](images/item-13214.jpg)

- **Name (English):** None
- **Name (French):** CROUSTILLES SANS NOM° CERTAINES VARIETES
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Chips & Snacks
- **Category (French):** Grignotines, croustilles et friandises > Croustilles et grignotines
- **How classified:** rule (`specific-snacks`)
- **Size:** 200 G
- **Price:** 1.79
- **Printed Price:** “1.79”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 644, top 751, right 978, bottom 790, page 1
- **Full page:** [pages/flyer126-page1-c46b1b869c.jpg (flyer page 1)](pages/flyer126-page1-c46b1b869c.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-lintermarche-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.95 · item_key: `dfb266daafcaaceb`
- **Raw:** `{"block_text": "CROUSTILLES SANS NOM°\nCERTAINES VARIETES\n\n200 G\n\nPOTATO CHIPS\n21302821_EA/21302946 EA", "ocr_lines": ["CROUSTILLESSANSNOM", "CERTAINESVARIETES", "POTATO CHIPS", "21302821_EA/21302946_EA"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. No Name chips (200 g, selected varieties) at 1.79 — verified on the crop. Chips & Snacks is right.

### Item 13219

![item 13219](images/item-13219.jpg)

- **Name (English):** None
- **Name (French):** MORES OU FRAMBOISES, PRODUIT DES É.-U. OU DU MEXIQUE OU BLEUETS, PRODUIT DU PÉROU
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** 6OZ
- **Price:** 3.29
- **Printed Price:** “3.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 516, top 366, right 971, bottom 405, page 2
- **Full page:** [pages/flyer126-page2-0b927b9315.jpg (flyer page 2)](pages/flyer126-page2-0b927b9315.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-lintermarche-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `e7314dca0eaa3a45`
- **Raw:** `{"block_text": "MORES OU FRAMBOISES, PRODUIT DES É.-U.\nOU DU MEXIQUE OU BLEUETS, PRODUIT\n\nDU PÉROU\n\n60Z\n\nBLACKBERRIES, RASPBERRIES OR BLUEBERRIES", "ocr_lines": ["MURESOUFRAMBOISES,PRODUITDESE.-U.", "OUDUMEXIQUEOUBLEUETS,PRODUIT", "DUPEROU", "BLACKBERRIES,RASPBERRIESORBLUEBERRIES"], "harvest": {"size": "6OZ", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Blackberries/raspberries (USA/Mexico) or blueberries (Peru), 6 oz, at 3.29 — verified. Fresh Fruits is right.

### Item 13223

![item 13223](images/item-13223.jpg)

- **Name (English):** None
- **Name (French):** BOISSON GAZEUSE PC” 2 L (CONSIGNE) OÙ JUS OASIS, DEL MONTE OÙ ARIZONA
- **Brand:** None
- **Category (English):** Drinks > Soft Drinks
- **Category (French):** Boissons > Boissons gazeuses
- **How classified:** rule (`soft-drinks`)
- **Size:** 2 L
- **Price:** 1.00
- **Printed Price:** “1”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 10, top 746, right 141, bottom 830, page 2
- **Full page:** [pages/flyer126-page2-0b927b9315.jpg (flyer page 2)](pages/flyer126-page2-0b927b9315.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-lintermarche-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `079633064de8c093`
- **Raw:** `{"block_text": "BOISSON GAZEUSE\nPC” 2 L (CONSIGNE)\nOÙ JUS OASIS,\n\nDEL MONTE\n\nOÙ ARIZONA\n\n960 ML/1 L\nCERTAINES VARIÉTÉS |\nSOFT DRINKS OR JUICE", "ocr_lines": ["BOISSONGAZEUSE", "PCMD2L(CONSIGNE)", "OUJUS OASIS,", "DELMONTE", "OUARIZONA", "960ML/1L", "CERTAINESVARIETES", "SOFTDRINKSORJUICE"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. PC soft drinks 2 L or Oasis/Del Monte/Arizona juice (960 ml/1 L) print 1.49; the DB had 1.00. Soft Drinks is right for the lead product.

### Item 13233

![item 13233](images/item-13233.jpg)

- **Name (English):** None
- **Name (French):** JUS D'ORANGE, MÉLANGES PRODUIT DE FROMAGE À PAUSE SANTÉ, MÉLANGE DE JUS LA CRÈME PHILADELPHIA 340 G OU SMOOTHIE OASIS (CONSIGNE) OU CHEEZ WHIZ KRAFT 450 G CERTAINES VARIÉTÉS, 1,5/1,6 L CERTAINES VARIÉTÉS ORANGE JUICE, JUICE BLENDS OR SMOOTHIES CREAM CHEESE PRODUCT OR CHEEZ WHIZ
- **Brand:** None
- **Category (English):** Drinks > Juice
- **Category (French):** Boissons > Jus
- **How classified:** rule (`juice`)
- **Size:** 1,6 L
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 1, top 925, right 486, bottom 1000, page 3
- **Full page:** [pages/flyer126-page3-f1da95f436.jpg (flyer page 3)](pages/flyer126-page3-f1da95f436.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-lintermarche-du-15-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `e95f073af2934ccc`
- **Raw:** `{"block_text": "JUS D'ORANGE, MÉLANGES PRODUIT DE FROMAGE À\nPAUSE SANTÉ, MÉLANGE DE JUS LA CRÈME PHILADELPHIA 340 G\nOU SMOOTHIE OASIS (CONSIGNE) OU CHEEZ WHIZ KRAFT 450 G\nCERTAINES VARIÉTÉS, 1,5/1,6 L CERTAINES VARIÉTÉS\nORANGE JUICE, JUICE BLENDS OR SMOOTHIES CREAM CHEESE PRODUCT OR CHEEZ WHIZ\n21376778_EA/21529910 EA 20659606001_EA/20866929002_EA\n\nITM AXP 02", "ocr_lines": ["JUSD'ORANGE,MELANGES", "PRODUITDEFROMAGEA", "PAUSESANTE,MELANGEDEJUS", "LACREMEPHILADELPHIA340G", "OUSMOOTHIEOASIS(`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. This item stitches two cells: Oasis orange juice/juice blends (1.5/1.6 L) at 4.99 and Philadelphia cream cheese/Cheez Whiz at 6.99. The item is named and classified as the juice, so its price is corrected to the juice's 4.99; the stitched name tail is the segmenter's two-cell merge, recorded here.

### Item 13242

![item 13242](images/item-13242.jpg)

- **Name (English):** None
- **Name (French):** FROMAGE BRIE OU CAMEMBERT PRÉSIDENT 185 - 230 G, FROMAGE LE ROITELET, ILE-ASH-ISLAND, LE SOEUR ANGÈLE, ROUBINE DE NOYAN, MARIA CHAPDELAINE, LE PÉRIBONKA,
- **Brand:** None
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** 185 - 230 G
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 759, top 914, right 991, bottom 990, page 4
- **Full page:** [pages/flyer126-page4-848fe58364.jpg (flyer page 4)](pages/flyer126-page4-848fe58364.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-lintermarche-du-15-au-21-octobre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `8c871151d43dedcf`
- **Raw:** `{"block_text": "FROMAGE BRIE OU CAMEMBERT\nPRÉSIDENT 185 - 230 G, FROMAGE\n\nLE ROITELET, ILE-ASH-ISLAND,\n\nLE SOEUR ANGÈLE, ROUBINE DE NOYAN,\nMARIA CHAPDELAINE, LE PÉRIBONKA,\nLE NOBLE OU ST-MORGON 150 - 250 G\nCERTAINES VARIÉTÉS\n\nCHEESE", "ocr_lines": ["FROMAGEBRIEOUCAMEMBERT", "PRESIDENT185-230G,FROMAGE", "LEROITELET,ILE-ASH-ISLAND", "LESOEURANGELE,ROUBINEDENOYAN,", "MARIACHAPDELAINE,LEPERIBONKA,", "LENOBLEOUST-MORGON150-250G", "CERTAINESVARIETES", "CHEESE"]}`

**Item Review Analysis (Pass 1):** Correct. Brie/camembert group (Président 185-230 g and seven Quebec cheeses 150-250 g) at 6.99 — verified. Cheese is right.

### Item 13247

![item 13247](images/item-13247.jpg)

- **Name (English):** None
- **Name (French):** HAUTS DE CUISSE DE POULET FORMAT CLUB CHICKEN THIGHS
- **Brand:** None
- **Category (English):** Meat > Chicken & Turkey
- **Category (French):** Viande > Poulet et dinde
- **How classified:** rule (`chicken-turkey`)
- **Size:** None
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 190, top 262, right 488, bottom 296, page 4
- **Full page:** [pages/flyer126-page4-848fe58364.jpg (flyer page 4)](pages/flyer126-page4-848fe58364.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-lintermarche-du-15-au-21-octobre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `c43d1ef187dfa4ad`
- **Conditions:** `{"alt_prices": ["1.49", "4"]}`
- **Raw:** `{"block_text": "HAUTS DE CUISSE\nDE POULET\nFORMAT CLUB\nCHICKEN THIGHS", "ocr_lines": ["HAUTSDECUISSE", "DEPOULET", "FORMATCLUB", "CHICKENTHIGHS"], "harvest": {"unit": "kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Chicken thighs, club format, at 3.99/lb (9.90/kg) — verified. Chicken & Turkey is right.

### Item 13250

![item 13250](images/item-13250.jpg)

- **Name (English):** None
- **Name (French):** POULET FARCI SANS NOM® CERTAINES VARIÉTÉS, SURGELÉ
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Meat and Seafood
- **Category (French):** Produits surgelés > Viande et fruits de mer surgelés
- **How classified:** frozen-remap (`chicken-turkey`)
- **Size:** 284G
- **Price:** 4.49
- **Printed Price:** “4.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 11, top 729, right 212, bottom 783, page 4
- **Full page:** [pages/flyer126-page4-848fe58364.jpg (flyer page 4)](pages/flyer126-page4-848fe58364.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-lintermarche-du-15-au-21-octobre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `cfa4eacf4ab29eba`
- **Raw:** `{"block_text": "POULET FARCI SANS NOM®\nCERTAINES VARIÉTÉS, SURGELÉ\n284G\n\nSTUFFED CHICKEN", "ocr_lines": ["POULETFARCI SANSNOM", "CERTAINESVARIETES,SURGELE", "STUFFED CHICKEN"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. No Name stuffed chicken (284 g, frozen) at 4.49 — verified. Frozen Meat and Seafood is right (the name carries "surgelé").

### Item 13266

![item 13266](images/item-13266.jpg)

- **Name (English):** None
- **Name (French):** SACHET DE BONBONS CARNABY SWEET CERTAINES VARIÉTÉS
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 125 G
- **Price:** 1.25
- **Printed Price:** “4/5.00”
- **Unit quantity:** 4.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 8, top 799, right 302, bottom 833, page 6
- **Full page:** [pages/flyer126-page6-19e9bffcc3.jpg (flyer page 6)](pages/flyer126-page6-19e9bffcc3.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-lintermarche-du-15-au-21-octobre-2026/06.webp
- **Details:** confidence: 0.97 · item_key: `49073e7dc7264b6b`
- **Conditions:** `{"multibuy": {"count": 4, "total": 5.0}}`
- **Raw:** `{"block_text": "SACHET DE BONBONS\nCARNABY SWEET\nCERTAINES VARIÉTÉS\n125 G\n\nCANDY BAG", "ocr_lines": ["SACHETDEBONBONS", "CARNABYSWEET", "CERTAINESVARIETES", "CANDYBAG"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Carnaby Sweet candy bags (125 g) at 4/5$ → stored 1.25 each — the derivation matches the printed "1,25 CH." Candy & Chocolate is right.

### Item 13269

![item 13269](images/item-13269.jpg)

- **Name (English):** None
- **Name (French):** DÎNER DE MACARONI AU FROMAGE PC“ CERTAINES VARIÉTÉS
- **Brand:** None
- **Category (English):** Pantry > Easy Meals & Sides
- **Category (French):** Produits du garde-manger > Mets faciles et accompagnements
- **How classified:** rule (`specific-mac-cheese`)
- **Size:** 200/225 G
- **Price:** 1.33
- **Printed Price:** “3/4.00”
- **Unit quantity:** 3.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 347, top 956, right 664, bottom 987, page 6
- **Full page:** [pages/flyer126-page6-19e9bffcc3.jpg (flyer page 6)](pages/flyer126-page6-19e9bffcc3.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-lintermarche-du-15-au-21-octobre-2026/06.webp
- **Details:** confidence: 0.95 · item_key: `0f820b77cc194a8b`
- **Conditions:** `{"multibuy": {"count": 3, "total": 4.0}}`
- **Raw:** `{"block_text": "DÎNER DE MACARONI AU\nFROMAGE PC“\nCERTAINES VARIÉTÉS\n200/225 G\n\nMACARONI AND CHEESE DINNER", "ocr_lines": ["DINERDEMACARONIAU", "FROMAGEPCMD", "CERTAINESVARIETES", "MACARONIAND CHEESEDINNER"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. PC macaroni & cheese dinner (200/225 g) at 3/4$ → stored 1.33 — matches the printed "1,33 CH." Easy Meals & Sides is right.

### Item 13275

![item 13275](images/item-13275.jpg)

- **Name (English):** None
- **Name (French):** POISSON SANS NOM® CERTAINES VARIETES, SURGELE
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Meat and Seafood
- **Category (French):** Produits surgelés > Viande et fruits de mer surgelés
- **How classified:** frozen-remap (`fish`)
- **Size:** 454G
- **Price:** 5.49
- **Printed Price:** “5.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 19, top 179, right 392, bottom 218, page 6
- **Full page:** [pages/flyer126-page6-19e9bffcc3.jpg (flyer page 6)](pages/flyer126-page6-19e9bffcc3.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-lintermarche-du-15-au-21-octobre-2026/06.webp
- **Details:** confidence: 0.89 · item_key: `0a983915afc19b7d`
- **Raw:** `{"block_text": "POISSON SANS NOM®\nCERTAINES VARIETES, SURGELE\n454G\n\nFISH", "ocr_lines": ["POISSONSANSNOM", "CERTAINESVARIETES,SURGELE", "FISH"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. No Name frozen fish (454 g) at 5.49 — verified. Frozen Meat and Seafood is right.
