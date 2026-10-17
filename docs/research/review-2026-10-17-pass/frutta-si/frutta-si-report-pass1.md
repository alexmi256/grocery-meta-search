# Marché Frutta Si — full product report

Store slug: `frutta-si`. Generated from `data/grocery.db`. A sampled subset of 11 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17) — ⚠ STORE FLAGGED: extraction unreliable, needs a tailored-segmentation decision

- **Flyers in this review:** 1 (flyer 118, valid 2026-10-15 → 2026-10-21). The printed validity on the page ("SPÉCIAUX EN VIGUEUR DU JEUDI 15 AU MERCREDI 21 OCTOBRE 2026") matches. Two older expired editions are correctly excluded.
- **Sample counts:** 10 classified + 1 unclassified shown, of 12 + 1 stored. The page prints ~40 products; only 13 were captured (~33%) — and the sample's verdict on those 13 is damning (below).
- **Issues found — wholesale price misattachment:** ELEVEN of the thirteen stored items carried ANOTHER product's price (the twelfth and thirteenth verified correct). The page is a dense grid of small cells, each with its price in a band under the product; the segmenter's name↔price pairing shuffled them systematically: apples got the header beer price (13.99 instead of 1.49/lb), ground beef got the mozzarella price (14.99 instead of 4.49/lb), Jarlsberg got a generic 3.99 instead of 11.35/lb, tomato paste got 18.00 instead of 89¢, shrimp got 66.61 instead of 19.99. All eleven prices (and their units) are corrected in the data from the page image, item by item in the notes below — the full stored edition now matches the page.
- **Patterns:** unlike Valmont (digit-level misreads), Frutta Si's failure is GEOMETRIC: names and prices are individually read correctly but paired wrongly across the tight grid, and two-thirds of the products never form items at all. Per Alex's standing direction (per-store tailored detection over universal solutions), the durable fix is a tailored segmentation for this page layout — a row/column-band pairing pass, the same class of intervention as the Akhavan PDF rebuild. That is a build, not a review fix: it is FLAGGED here for Alex's decision and NOT attempted in this pass. Until then, this store's flyer data should be treated as unreliable between manual corrections.
- **Fixes applied this pass:** the 11 stored prices/units corrected from the page (11936, 11937, 11938, 11939, 11940, 11941, 11942, 11943, 11944, 11945, 11946). Classifications of the captured items were otherwise sound (the tomato paste's unclassified state is its glued name, "Pate detomate").

## Flyer 118 — valid 2026-10-15 → 2026-10-21 (10 classified items, 1 unclassified)

Source ref: `circulaire-frutta-si-du-15-au-21-octobre-2026` · fetched 2026-10-16T12:11:15.948Z

### Item 11935

![item 11935](images/item-11935.jpg)

- **Name (English):** None
- **Name (French):** Orgoglio Tomates entieres peles
- **Brand:** None
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`specific-canned`)
- **Size:** 6x796ml
- **Price:** 10.99
- **Printed Price:** “10.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 593, top 834, right 718, bottom 915, page 1
- **Full page:** [pages/flyer118-page1-9d188a385f.jpg (flyer page 1)](pages/flyer118-page1-9d188a385f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-frutta-si-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `4a2770f54568a53b`
- **Raw:** `{"block_text": "Tomates\n3", "ocr_lines": ["Orgoglio", "Tomates", "entieres peles", "Wholepeeled", "Tomato", "6x796ml"], "harvest": {"size": "6x796ml", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct — one of only two stored items whose price was right. Orgoglio whole peeled tomatoes, 6 x 796 ml, at 10.99. Canned & Pickled is right.

### Item 11936

![item 11936](images/item-11936.jpg)

- **Name (English):** None
- **Name (French):** Pomme GoldenetRusset Apple
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 13.99
- **Printed Price:** “13.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 119, top 148, right 467, bottom 199, page 1
- **Full page:** [pages/flyer118-page1-9d188a385f.jpg (flyer page 1)](pages/flyer118-page1-9d188a385f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-frutta-si-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `e2bce5812d98c581`
- **Raw:** `{"block_text": "Pomme Golden et Russet\nApple", "ocr_lines": ["Pomme GoldenetRusset", "Apple"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Golden/Russet apples print 1.49/lb (3.28 $/kg); the DB had 13.99 — the Red Stripe beer price from the page header. Fresh Fruits is right.

### Item 11938

![item 11938](images/item-11938.jpg)

- **Name (English):** None
- **Name (French):** Soc de porc desosse Boneless pork butt
- **Brand:** None
- **Category (English):** Meat > Pork & Ham
- **Category (French):** Viande > Porc et jambon
- **How classified:** rule (`pork-ham`)
- **Size:** None
- **Price:** 5.49
- **Printed Price:** “5.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 39, top 580, right 331, bottom 647, page 1
- **Full page:** [pages/flyer118-page1-9d188a385f.jpg (flyer page 1)](pages/flyer118-page1-9d188a385f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-frutta-si-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.92 · item_key: `a624c33751d34440`
- **Conditions:** `{"alt_prices": ["9.99"]}`
- **Raw:** `{"block_text": "Soc de porc\n\ndésossé\n\nBoneless pork butt\nDE “ee", "ocr_lines": ["Soc de porc", "desosse", "Boneless pork butt"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Boneless pork butt prints 3.49/lb (7.69 $/kg); the DB had 5.49 (the lupini beans' price). Pork & Ham is right.

### Item 11939

![item 11939](images/item-11939.jpg)

- **Name (English):** None
- **Name (French):** Jalsberg Fromage Cheese
- **Brand:** None
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** None
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 588, top 579, right 760, bottom 646, page 1
- **Full page:** [pages/flyer118-page1-9d188a385f.jpg (flyer page 1)](pages/flyer118-page1-9d188a385f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-frutta-si-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `e971b6bff7b2e736`
- **Raw:** `{"block_text": "Jalsberg\nFromage\nCheese", "ocr_lines": ["Jalsberg", "Fromage", "Cheese"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Jarlsberg cheese prints 11.35/lb (24.99 $/kg); the DB had 3.99. Cheese is right.

### Item 11940

![item 11940](images/item-11940.jpg)

- **Name (English):** None
- **Name (French):** Bceufhache mi-maigre Medium ground beef
- **Brand:** None
- **Category (English):** Meat > Beef
- **Category (French):** Viande > Bœuf
- **How classified:** rule (`beef`)
- **Size:** 500g
- **Price:** 14.99
- **Printed Price:** “14.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 522, top 731, right 961, bottom 814, page 1
- **Full page:** [pages/flyer118-page1-9d188a385f.jpg (flyer page 1)](pages/flyer118-page1-9d188a385f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-frutta-si-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `39a0f96e20e5dbb8`
- **Conditions:** `{"alt_prices": ["9.99"]}`
- **Raw:** `{"block_text": "Bœuf haché\n\nmi-maigre® =\nMedium'ground beef\nFAMILIAL}", "ocr_lines": ["Bceufhache", "mi-maigre", "Medium ground beef", "FAMILIAL"], "harvest": {"size": "500g", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Medium ground beef (family pack) prints 4.49/lb (9.90 $/kg); the DB had 14.99 — the Saputo mozzarella's price. Beef is right.

### Item 11941

![item 11941](images/item-11941.jpg)

- **Name (English):** None
- **Name (French):** Maruja Biscuits cacao Cacao cokkdios
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** None
- **Price:** 6.96
- **Printed Price:** “6.96”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 255, top 358, right 461, bottom 425, page 1
- **Full page:** [pages/flyer118-page1-9d188a385f.jpg (flyer page 1)](pages/flyer118-page1-9d188a385f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-frutta-si-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.72 · item_key: `820fba0facc89e57`
- **Raw:** `{"block_text": "Maruja\nBiscuits cacao\nCacao cokkies", "ocr_lines": ["Maruja", "Biscuits cacao", "Cacao cokkdios"], "harvest": {"unit": "kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Maruja cacao cookies print 3.99 each; the DB had 6.96 with a bogus kg unit. Crackers & Cookies is right.

### Item 11942

![item 11942](images/item-11942.jpg)

- **Name (English):** None
- **Name (French):** Poitrine de poulet desossee Bonelesschickenbreast
- **Brand:** None
- **Category (English):** Meat > Chicken & Turkey
- **Category (French):** Viande > Poulet et dinde
- **How classified:** rule (`chicken-turkey`)
- **Size:** None
- **Price:** 3.49
- **Printed Price:** “3.49”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 158, top 688, right 426, bottom 763, page 1
- **Full page:** [pages/flyer118-page1-9d188a385f.jpg (flyer page 1)](pages/flyer118-page1-9d188a385f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-frutta-si-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `872a42aba28af37c`
- **Conditions:** `{"alt_prices": ["3.99"]}`
- **Raw:** `{"block_text": "Poitrine de poulet\n\ndésossée _\n#Boneless chickenbreast\n\nFAMILIALE E", "ocr_lines": ["Poitrine de poulet", "desossee", "Bonelesschickenbreast", "FAMILIAL"], "harvest": {"unit": "kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Boneless chicken breast (family pack) prints 6.99/lb (15.41 $/kg); the DB had 3.49 with a kg unit (the pork butt's price). Chicken & Turkey is right.

### Item 11943

![item 11943](images/item-11943.jpg)

- **Name (English):** None
- **Name (French):** Anchors Bay Tilapia entier Whole tilapia
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** None
- **Price:** 8.99
- **Printed Price:** “8.99”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 344, top 785, right 532, bottom 882, page 1
- **Full page:** [pages/flyer118-page1-9d188a385f.jpg (flyer page 1)](pages/flyer118-page1-9d188a385f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-frutta-si-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `969b616b37852ca3`
- **Raw:** `{"block_text": "tAnchors|Bays\nLTilapia'entier\nWhole tilapia\nbe TILAPIA", "ocr_lines": ["Anchors Bay", "Tilapia entier", "Whole tilapia", "TILAPIA"], "harvest": {"unit": "kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Whole tilapia prints 7.99 each; the DB had 8.99 with a kg unit (the chicken cutlets' per-lb price). Fish is right.

### Item 11944

![item 11944](images/item-11944.jpg)

- **Name (English):** None
- **Name (French):** Spalding Bacon
- **Brand:** None
- **Category (English):** Meat > Bacon
- **Category (French):** Viande > Bacon
- **How classified:** rule (`bacon`)
- **Size:** 500g
- **Price:** 2.49
- **Printed Price:** “2.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 828, top 467, right 934, bottom 526, page 1
- **Full page:** [pages/flyer118-page1-9d188a385f.jpg (flyer page 1)](pages/flyer118-page1-9d188a385f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-frutta-si-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `1cdfad824cf19fa6`
- **Raw:** `{"block_text": ".Spalding", "ocr_lines": ["Spalding", "Bacon"], "harvest": {"size": "500g", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Spalding bacon (500 g) prints 3.99 each; the DB had 2.49. Bacon is right.

### Item 11946

![item 11946](images/item-11946.jpg)

- **Name (English):** None
- **Name (French):** del biscotto IRipieni Biscuits noisettes
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** None
- **Price:** 0.68
- **Printed Price:** “0.68”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 529, top 409, right 779, bottom 494, page 1
- **Full page:** [pages/flyer118-page1-9d188a385f.jpg (flyer page 1)](pages/flyer118-page1-9d188a385f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-frutta-si-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.86 · item_key: `990ab81cda06f002`
- **Raw:** `{"block_text": "re cane\ndel biscotto\nI Ripieni™\nBiscuits noisettes\nHazelnut cookies", "ocr_lines": ["del biscotto", "IRipieni", "Biscuits noisettes", "Hazelnut cookies"], "harvest": {"unit": "each", "via": "crop"}}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 118 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. I Ripieni hazelnut cookies (200 g) print 2.49 each; the DB had 0.68. Crackers & Cookies is right; the name is a partial stitch ("del biscotto I Ripieni…" — the brand line's tail leads).

### Item 11937

![item 11937](images/item-11937.jpg)

- **Name (English):** None
- **Name (French):** Primo Pate detomate Tomatopaste
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 156ml
- **Price:** 18.00
- **Printed Price:** “3/53.99”
- **Unit quantity:** 3.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 586, top 353, right 862, bottom 434, page 1
- **Full page:** [pages/flyer118-page1-9d188a385f.jpg (flyer page 1)](pages/flyer118-page1-9d188a385f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-frutta-si-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.86 · item_key: `f45e3e0a8c234333`
- **Conditions:** `{"multibuy": {"count": 3, "total": 53.99}}`
- **Raw:** `{"block_text": "Primo\n\nPâteide tomate\nTomato pastes\nDER MC", "ocr_lines": ["Primo", "Pate detomate", "Tomatopaste", "156mlRIMO"], "harvest": {"size": "156ml", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Primo tomato paste (156 ml) prints 89¢ each; the DB had 18.00. Unclassified only because the name is glued ("Pate detomate Tomatopaste") — the documented run-together limit; with a clean name it is Canned & Pickled.
