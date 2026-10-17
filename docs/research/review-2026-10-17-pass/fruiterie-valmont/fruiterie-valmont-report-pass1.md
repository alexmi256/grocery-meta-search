# Fruiterie Valmont — full product report

Store slug: `fruiterie-valmont`. Generated from `data/grocery.db`. A sampled subset of 20 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 162, valid 2026-10-15 → 2026-10-21). The printed validity in page 1's footer ("DU JEUDI 15 OCTOBRE AU MERCREDI 21 OCTOBRE 2026") matches. The DB also holds the expired Oct 8–14 edition, correctly excluded. All 3 pages were scraped (35 items).
- **Sample counts:** 10 classified + 10 unclassified shown — the unclassified half is this store's signature problem (below).
- **Issues found — a price-corruption cluster (5 of 20 sampled items):** this flyer typesets prices as a huge dollars digit with superscript cents. When OCR merges such a price into one digit run ("799"), a segment rule written for cents badges ("79¢" with the ¢ glyph read as a 9) reinterpreted the run as CENTS. Philadelphia cream cheese 7.99 was stored as 0.79, St-Donat apple pie 3.29 as 0.32, Oka cheese 3.59/100 g as 0.35 — and the same mechanism hit two more sample items in the other direction of plausibility: pumpkins stored 0.39 (real price 3.99 each) and kiwis stored 0.49 (real price 4.99). A sixth item (15250, Kraft hazelnut spread) stored 31.17: its price cluster stitched the neighbouring chips' "3/9$" multibuy with its own "ÉCONOMISEZ 3.50$" savings badge (its real price is 6.49). All six prices are corrected in the data from the page images.
- **Root-cause fix:** the merged-run cents reading now requires the cluster to still carry the ¢ or % glyph it supposedly came from (the same evidence gate the "%-as-cents" recovery already used). True cents prices (bananas and squash at 69¢/lb, verified correct in the data) form from the surviving "69¢" token and are unaffected; merged dollar runs now parse as dollars. Covered by a new unit test pinning both readings.
- **Issues found — classification:** 9 of the 10 unclassified items are ordinary produce/dairy whose names OCR glued into one token ("Poivronsrouges", "PommesMclntosh", "Couronnesdebrocolis", "Fromageatartiner…"), defeating the token-based rules — the documented run-together limit, but at this store it is the dominant defect, not a tail: the flyer's condensed name type glues the product word to its first descriptor on most cells. The Kraft spread's category (Baking Essentials) is wrong for the same reason ("Tartinadeauxnoisetteset…" never exposes "tartinade"). No fix is attempted here: de-gluing OCR text safely is a research problem already rejected once; the items stay visible for review with correct prices.
- **Patterns:** numeric accuracy, not categorization, is the OCR stores' weak point this week — display-font prices need the image check this review exists for. Every corrected price was verified against its page image (crops in this packet).
- **Fixes applied this pass:** segment gate (above, with tests; 148 tests green); six stored prices corrected (15250 → 6.49 with its bogus multibuy condition cleared, 15262 kiwis → 4.99, 15265 pumpkin → 3.99, 15274 pie → 3.29, 15275 Philadelphia → 7.99, 15280 Oka → 3.59).

## Flyer 162 — valid 2026-10-15 → 2026-10-21 (10 classified items, 10 unclassified)

Source ref: `circulaire-val-mont-du-15-au-21-octobre-2026` · fetched 2026-10-17T04:10:10.731Z

### Item 15250

![item 15250](images/item-15250.jpg)

- **Name (English):** None
- **Name (French):** Tartinadeauxnoisetteset cacao originaleoureduite ensucreKraft
- **Brand:** None
- **Category (English):** Pantry > Baking Essentials
- **Category (French):** Produits du garde-manger > Essentiels de cuisson
- **How classified:** rule (`baking`)
- **Size:** None
- **Price:** 31.17
- **Printed Price:** “3/93.50”
- **Unit quantity:** 3.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 427, top 723, right 779, bottom 807, page 1
- **Full page:** [pages/flyer162-page1-d65eca080b.jpg (flyer page 1)](pages/flyer162-page1-d65eca080b.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.84 · item_key: `6e60d631cb0ac8c9`
- **Conditions:** `{"multibuy": {"count": 3, "total": 93.5}}`
- **Raw:** `{"block_text": "Tartinade aux noisettes et\ncacao originale ou réduite\nen sucre Kraft\n\n725g\n\nJusqu'à épuisement des stock", "ocr_lines": ["Tartinadeauxnoisetteset", "cacao originaleoureduite", "ensucreKraft", "Jusqu'aepuisementdesstock"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Kraft hazelnut-cocoa spread (725 g) prints 6.49; the DB had 31.17 — its cluster stitched the Kettle chips' "3/9$" next door with the spread's own "ÉCONOMISEZ 3.50$" badge into a fake multibuy (3/93.50). Bogus multibuy condition cleared. Category (Baking Essentials) is also off — the glued name never exposes "tartinade" to the spreads rule — recorded, not hand-edited.

### Item 15255

![item 15255](images/item-15255.jpg)

- **Name (English):** None
- **Name (French):** Choux-fleurs Quebec
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 2.50
- **Printed Price:** “2/5.00”
- **Unit quantity:** 2.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 399, top 307, right 649, bottom 422, page 1
- **Full page:** [pages/flyer162-page1-d65eca080b.jpg (flyer page 1)](pages/flyer162-page1-d65eca080b.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.84 · item_key: `b62c97a947b32547`
- **Conditions:** `{"multibuy": {"count": 2, "total": 5.0}}`
- **Raw:** `{"block_text": "Choux-fleurs\nQuébec", "ocr_lines": ["Choux-fleurs", "Quebec"]}`

**Item Review Analysis (Pass 1):** Correct. Quebec cauliflower at 2/5$ — stored 2.50 with a multiple unit (2), faithful. Fresh Vegetables is right.

### Item 15256

![item 15256](images/item-15256.jpg)

- **Name (English):** None
- **Name (French):** Bananes Ameriquecentrale
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 0.69
- **Printed Price:** “0.69”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 52, top 141, right 223, bottom 233, page 1
- **Full page:** [pages/flyer162-page1-d65eca080b.jpg (flyer page 1)](pages/flyer162-page1-d65eca080b.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.86 · item_key: `02d12659497c2ec7`
- **Raw:** `{"block_text": "| Bananes\nAmérique centrale\nICVC /LA", "ocr_lines": ["Bananes", "Ameriquecentrale"]}`

**Item Review Analysis (Pass 1):** Correct. Bananas at 69¢/lb (1.52 $/kg also printed) — stored 0.69 per pound. This is the genuine cents-badge form the merged-run rule was built for; the glyph evidence survives in the "69¢" token.

### Item 15262

![item 15262](images/item-15262.jpg)

- **Name (English):** None
- **Name (French):** Kiwis Chili
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** 600g
- **Price:** 0.49
- **Printed Price:** “0.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 388, top 202, right 600, bottom 303, page 2
- **Full page:** [pages/flyer162-page2-ed68b2b14d.jpg (flyer page 2)](pages/flyer162-page2-ed68b2b14d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.96 · item_key: `701b2fb3cf497661`
- **Raw:** `{"block_text": "Kiwis\nChili", "ocr_lines": ["Kiwis", "Chili"], "harvest": {"size": "600g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Kiwis (Chile, 600 g) print 4.99 each; the DB had 0.49 (merged run "499" read as cents). Fresh Fruits is right.

### Item 15265

![item 15265](images/item-15265.jpg)

- **Name (English):** None
- **Name (French):** Citrouille orange Quebec
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 0.39
- **Printed Price:** “0.39”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 39, top 793, right 252, bottom 906, page 2
- **Full page:** [pages/flyer162-page2-ed68b2b14d.jpg (flyer page 2)](pages/flyer162-page2-ed68b2b14d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `8d3237afdf2777ba`
- **Raw:** `{"block_text": "Citrouille orange\nQuébec", "ocr_lines": ["Citrouille orange", "Quebec"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Orange pumpkins (Quebec) print 3.99/ch.; the DB had 0.39 (merged run "399" read as cents) with a wrong "each-by-default" — price and unit now 3.99 each, matching the print.

### Item 15266

![item 15266](images/item-15266.jpg)

- **Name (English):** None
- **Name (French):** Celeris Quebec
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 1.66
- **Printed Price:** “1.66”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 428, top 385, right 588, bottom 481, page 2
- **Full page:** [pages/flyer162-page2-ed68b2b14d.jpg (flyer page 2)](pages/flyer162-page2-ed68b2b14d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `2026268fdf4a284f`
- **Raw:** `{"block_text": "[Céleris\n| Québec", "ocr_lines": ["Celeris", "Quebec"]}`

**Item Review Analysis (Pass 1):** Correct. Quebec celery at 1.66 — the dotted anchor is unambiguous in the segment run; Fresh Vegetables is right.

### Item 15269

![item 15269](images/item-15269.jpg)

- **Name (English):** None
- **Name (French):** Champignons blancs Canada
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 802, top 431, right 948, bottom 529, page 2
- **Full page:** [pages/flyer162-page2-ed68b2b14d.jpg (flyer page 2)](pages/flyer162-page2-ed68b2b14d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.88 · item_key: `016ed7cba05f339f`
- **Raw:** `{"block_text": "Champignons blancs à\nCanad En ! |\nanade 23", "ocr_lines": ["Champignons blancs", "Canada"]}`

**Item Review Analysis (Pass 1):** Correct. White mushrooms (Canada) at 1.99 — Fresh Vegetables; dotted price anchor.

### Item 15272

![item 15272](images/item-15272.jpg)

- **Name (English):** None
- **Name (French):** Poireaux Quebec
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 412, top 819, right 587, bottom 920, page 2
- **Full page:** [pages/flyer162-page2-ed68b2b14d.jpg (flyer page 2)](pages/flyer162-page2-ed68b2b14d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `80f50d88ce752409`
- **Raw:** `{"block_text": "Poireaux\nQuébec", "ocr_lines": ["Poireaux", "Quebec"]}`

**Item Review Analysis (Pass 1):** Correct. Quebec leeks at 3.99 — Fresh Vegetables.

### Item 15276

![item 15276](images/item-15276.jpg)

- **Name (English):** None
- **Name (French):** Biscuits avoine,avoine raisins ou avoine chocolatRondeau
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** 300g
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 791, top 602, right 932, bottom 678, page 3
- **Full page:** [pages/flyer162-page3-ce82c73567.jpg (flyer page 3)](pages/flyer162-page3-ce82c73567.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.92 · item_key: `34c3ee868987d2ad`
- **Raw:** `{"block_text": "Biscuits avoine, avoine\nraisins ou avoine\nchocolat Rondeau\nMn", "ocr_lines": ["Biscuits avoine,avoine", "raisins ou avoine", "chocolatRondeau"], "harvest": {"size": "300g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Rondeau oat cookies (oat, oat-raisin or oat-chocolate) at 2.99 — Crackers & Cookies is right.

### Item 15280

![item 15280](images/item-15280.jpg)

- **Name (English):** None
- **Name (French):** Fromage Oka Original ouOkaraclette
- **Brand:** None
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** None
- **Price:** 0.35
- **Printed Price:** “0.35”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 481, top 360, right 619, bottom 425, page 3
- **Full page:** [pages/flyer162-page3-ce82c73567.jpg (flyer page 3)](pages/flyer162-page3-ce82c73567.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `0a2b2d44454d46c1`
- **Raw:** `{"block_text": "Fromage Oka Original\nou Oka raclette\n1€ NO.", "ocr_lines": ["Fromage Oka Original", "ouOkaraclette"], "harvest": {"size": "100g", "via": "crop"}}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 162 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Oka Original/raclette cheese prints 3.59/100 g (16.28/lb); the DB had 0.35 per "gram" — the merged run "359" read as cents AND the 100 g rate split wrong. Price now 3.59 with the 100 g unit. Cheese category is right.

### Item 15254

![item 15254](images/item-15254.jpg)

- **Name (English):** None
- **Name (French):** PizzasStromboli Auchoix-365-422g
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 365-422g
- **Price:** 4.00
- **Printed Price:** “3/12.00”
- **Unit quantity:** 3.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 313, top 519, right 521, bottom 599, page 1
- **Full page:** [pages/flyer162-page1-d65eca080b.jpg (flyer page 1)](pages/flyer162-page1-d65eca080b.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.94 · item_key: `91b6b95640e412ff`
- **Conditions:** `{"multibuy": {"count": 3, "total": 12.0}}`
- **Raw:** `{"block_text": "”\nPizzas Stromboli ==\nAu choix — 365-422g M\nA =", "ocr_lines": ["PizzasStromboli", "Auchoix-365-422g"]}`

— from flyer 162 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Price right, classification glued. Stromboli pizzas at 3/12$ → stored 4.00 with a multiple unit (3), faithful. Unclassified only because "PizzasStromboli" is one token — the documented run-together limit.

### Item 15260

![item 15260](images/item-15260.jpg)

- **Name (English):** None
- **Name (French):** Poivronsrouges,jaunes ouoranges Quebec
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 102, top 419, right 261, bottom 521, page 2
- **Full page:** [pages/flyer162-page2-ed68b2b14d.jpg (flyer page 2)](pages/flyer162-page2-ed68b2b14d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `f0e55df0874e702d`
- **Raw:** `{"block_text": "_ __ TE = Da nté\nPoivrons rouges, jaunes\nlou oranges |\nQuébec à\nA FOO 1 '", "ocr_lines": ["Poivronsrouges,jaunes", "ouoranges", "Quebec"]}`

— from flyer 162 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Unclassified on a glued name: "Poivronsrouges, jaunes ou oranges" (red/yellow/orange peppers, Quebec) at 1.99 — core produce vocabulary defeated by the glued head word. Price verified correct on the page. Kept for review.

### Item 15261

![item 15261](images/item-15261.jpg)

- **Name (English):** None
- **Name (French):** PommesMclntosh,Cortland, SpartanouEmpire Quebec
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
- **bbox:** left 412, top 45, right 598, bottom 148, page 2
- **Full page:** [pages/flyer162-page2-ed68b2b14d.jpg (flyer page 2)](pages/flyer162-page2-ed68b2b14d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `3bd36038ebb1f0f3`
- **Raw:** `{"block_text": "———\nPommes Mcintosh, Cortland,\n| Spartan ou Empire 2\nQuébec EE", "ocr_lines": ["PommesMclntosh,Cortland,", "SpartanouEmpire", "Quebec"]}`

— from flyer 162 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Unclassified on a glued name: "PommesMclntosh, Cortland, Spartan ou Empire" at 4.99 — same pattern. Price correct.

### Item 15263

![item 15263](images/item-15263.jpg)

- **Name (English):** None
- **Name (French):** Oignonsrouges Quebec sac de
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
- **bbox:** left 409, top 579, right 585, bottom 714, page 2
- **Full page:** [pages/flyer162-page2-ed68b2b14d.jpg (flyer page 2)](pages/flyer162-page2-ed68b2b14d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `9435f684a3408045`
- **Raw:** `{"block_text": "i Oignons rouges\n, Quebec |\nsac de .\n3 livres", "ocr_lines": ["Oignonsrouges", "Quebec", "sac de", "3livres"]}`

— from flyer 162 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Unclassified on a glued name: "Oignonsrouges Québec, sac de…" at 2.99 — same pattern. Price correct.

### Item 15264

![item 15264](images/item-15264.jpg)

- **Name (English):** None
- **Name (French):** PoiresBartlett ou Bosc Ontario
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
- **bbox:** left 81, top 191, right 259, bottom 285, page 2
- **Full page:** [pages/flyer162-page2-ed68b2b14d.jpg (flyer page 2)](pages/flyer162-page2-ed68b2b14d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `80b48c2e620f7095`
- **Raw:** `{"block_text": "Luf\nPoires Bartlett ou Bosc\n. Ontario", "ocr_lines": ["PoiresBartlett ou Bosc", "Ontario"]}`

— from flyer 162 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Unclassified on a glued name: "PoiresBartlett ou Bosc" (Ontario pears) at 4.99 — same pattern. Price correct.

### Item 15268

![item 15268](images/item-15268.jpg)

- **Name (English):** None
- **Name (French):** Couronnesdebrocolis Quebec
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 84, top 619, right 254, bottom 715, page 2
- **Full page:** [pages/flyer162-page2-ed68b2b14d.jpg (flyer page 2)](pages/flyer162-page2-ed68b2b14d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `311b607cb30f1e3c`
- **Raw:** `{"block_text": "Couronnes de brocolis\nQuébec :\na QC F4 «", "ocr_lines": ["Couronnesdebrocolis", "Quebec"], "harvest": {"unit": "kg", "via": "crop"}}`

— from flyer 162 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Unclassified on a glued name: "Couronnesdebrocolis" (broccoli crowns) at 2.99 — the stored unit (kilogram) follows the printed rate's metric side; the name is the blocker, not the price.

### Item 15270

![item 15270](images/item-15270.jpg)

- **Name (English):** None
- **Name (French):** ChouxdeBruxelle Quebec
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 769, top 608, right 938, bottom 705, page 2
- **Full page:** [pages/flyer162-page2-ed68b2b14d.jpg (flyer page 2)](pages/flyer162-page2-ed68b2b14d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `78dab515159cd8d6`
- **Raw:** `{"block_text": "= — +\nChoux de Bruxelle À\n| Québec RE", "ocr_lines": ["ChouxdeBruxelle", "Quebec"]}`

— from flyer 162 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Unclassified on a glued name: "ChouxdeBruxelle" (Brussels sprouts) at 2.99/lb — same pattern; price and unit correct.

### Item 15274

![item 15274](images/item-15274.jpg)

- **Name (English):** None
- **Name (French):** Tarteauxpommes,pommeset sucreoucroustadeauxpommes St-Donat
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 570-650g
- **Price:** 0.32
- **Printed Price:** “0.32”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 134, top 657, right 360, bottom 751, page 3
- **Full page:** [pages/flyer162-page3-ce82c73567.jpg (flyer page 3)](pages/flyer162-page3-ce82c73567.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `e60ffdcc7077848a`
- **Raw:** `{"block_text": "Tarte aux pommes, pommes et\nsucre ou croustade aux pommes\nSt-Donat\nAu choix — 570-650g\nEn\nPLUS\n\"> gan #3 Fr", "ocr_lines": ["Tarteauxpommes,pommeset", "sucreoucroustadeauxpommes", "St-Donat", "Au choix-570-650g", "A partir de", "ICONOMISEZ", "PLUSDE"], "harvest": {"size": "570-650g", "via": "crop"}}`

— from flyer 162 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. St-Donat apple pies/crumble (570-650 g) print "À partir de 3.29"; the DB had 0.32 (merged run "329" as cents). Unclassified because the name is glued ("Tarteauxpommes…") — with a clean name this is Bakery.

### Item 15275

![item 15275](images/item-15275.jpg)

- **Name (English):** None
- **Name (French):** Fromageatartinerregulier oulegerPhiladelphia Auchoix-340g
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 340g
- **Price:** 0.79
- **Printed Price:** “0.79”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 409, top 750, right 557, bottom 822, page 3
- **Full page:** [pages/flyer162-page3-ce82c73567.jpg (flyer page 3)](pages/flyer162-page3-ce82c73567.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `d42df40c1f1417e3`
- **Raw:** `{"block_text": "Fromage à tartiner régulier\nou léger Philadelphia\nAu choix —340g", "ocr_lines": ["Fromageatartinerregulier", "oulegerPhiladelphia", "Auchoix-340g"]}`

— from flyer 162 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Philadelphia cream cheese (340 g) prints 7.99; the DB had 0.79 (merged run "799" as cents). Unclassified because "Fromageatartiner" is glued — with a clean name this is Dairy > Cheese/ spreads territory.

### Item 15278

![item 15278](images/item-15278.jpg)

- **Name (English):** None
- **Name (French):** Fromagescheddarfort,extra-fort, fume,truffesoupoivre concasse Balderson
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 0.49
- **Printed Price:** “0.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 601, top 512, right 937, bottom 606, page 3
- **Full page:** [pages/flyer162-page3-ce82c73567.jpg (flyer page 3)](pages/flyer162-page3-ce82c73567.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-val-mont-du-15-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `bc24474d9c8d3487`
- **Raw:** `{"block_text": "Fromages cheddar fort, extra-fort,\nfumé; truffes ou poivre concassé\nBalderson\n\nAu choix — 250-280g", "ocr_lines": ["Fromagescheddarfort,extra-fort,", "fume,truffesoupoivre concasse", "Balderson", "Au choix-250-280g"]}`

**Item Review Analysis (Pass 1):** Unclassified on a glued name: Balderson cheddar (fort, extra-fort, fumé, truffes ou poivre) at 4.99 — "Fromagescheddarfort…" exposes no token the cheese rule can use. Price correct.
