# M&M Food Market — full product report

Store slug: `mm-food-market`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 146, valid 2026-10-15 → 2026-10-21, 54 items; the printed validity line on page 1 matches). The expired Oct 8–14 edition is correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown — inflated classification: several "classified" items are name fragments (a count band like "12-13 UNITÉS" classified as Fresh Vegetables), so the 0 unclassified is the fragment lottery, not clean capture.
- **Issues found:** this flyer's cells stack photo (with the price badge at its top-left) → count/size band → product name, and the segmenter repeatedly anchored the badge of the cell BELOW. Four of ten sampled prices were wrong: the breaded haddock stored the fries' badge below it (4.99 for a member price of 27.99), the garlic shrimp stored the breaded bites' 19.99 (theirs: 12.99), the Italian meatballs stored the main cell's 16.99 when the meatballs are the "aussi disponible" side-box variant at 22.99, and the quesadillas stored the NON-member price (12.99) where the store's convention — and every other item — is the red member price (11.99). All four corrected from the pages. Prices at this store are member (Récompenses) prices throughout; the non-member price prints beside them.
- **Fixes applied this pass:** 14321 → 22.99, 14341 → 12.99, 14349 → 11.99, 14374 → 27.99.

## Flyer 146 — valid 2026-10-15 → 2026-10-21 (10 classified items, 0 unclassified)

Source ref: `circulaire-les-aliments-mm-du-15-au-21-octobre-2026` · fetched 2026-10-16T12:46:26.858Z

### Item 14316

![item 14316](images/item-14316.jpg)

- **Name (English):** None
- **Name (French):** Soupes
- **Brand:** None
- **Category (English):** Prepared Meals > Salads & Soups
- **Category (French):** Repas préparés > Salades et soupes
- **How classified:** rule (`salads-soups`)
- **Size:** 400ml
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 30, top 803, right 200, bottom 921, page 1
- **Full page:** [pages/flyer146-page1-d77c55847a.jpg (flyer page 1)](pages/flyer146-page1-d77c55847a.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-aliments-mm-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.97 · item_key: `17686db27a23b503`
- **Conditions:** `{"alt_prices": ["6.99"]}`
- **Raw:** `{"block_text": "FAS £ a\nSoupes\n255)g 400ml", "ocr_lines": ["Soupes", "255g-400mL"]}`

**Item Review Analysis (Pass 1):** Correct. Soups (255 g - 400 ml, several varieties) at 5.99 each member price (6.99 non-member) — the badge sits inside the soups' own cell on page 1. Salads & Soups is right.

### Item 14317

![item 14317](images/item-14317.jpg)

- **Name (English):** None
- **Name (French):** Languettesdepouletau fromagenacho680g
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Meals, Entrees & Sides
- **Category (French):** Produits surgelés > Repas, plats principaux et accompagnements
- **How classified:** store-prior
- **Size:** 680g
- **Price:** 16.99
- **Printed Price:** “16.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 346, top 446, right 714, bottom 507, page 1
- **Full page:** [pages/flyer146-page1-d77c55847a.jpg (flyer page 1)](pages/flyer146-page1-d77c55847a.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-aliments-mm-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.94 · item_key: `f0e7005a5a367cc0`
- **Conditions:** `{"alt_prices": ["19.99"]}`
- **Raw:** `{"block_text": "Languettes de poulet au\nfromage nacho 680 g\nPy PARK ST TY Re ET", "ocr_lines": ["Languettesdepouletau", "fromagenacho680g"]}`

**Item Review Analysis (Pass 1):** Correct. Nacho-cheese chicken strips (680 g) at 16.99 member — proven by page 1's side box, which repeats the variant and both prices (16.99 / 19.99). Frozen Meals is right.

### Item 14321

![item 14321](images/item-14321.jpg)

- **Name (English):** None
- **Name (French):** Boulettes debceuf al'italienne 130-140UNITES
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Meals, Entrees & Sides
- **Category (French):** Produits surgelés > Repas, plats principaux et accompagnements
- **How classified:** store-prior
- **Size:** 130-140UNITES
- **Price:** 16.99
- **Printed Price:** “16.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 29, top 62, right 313, bottom 112, page 2
- **Full page:** [pages/flyer146-page2-b271596e74.jpg (flyer page 2)](pages/flyer146-page2-b271596e74.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-aliments-mm-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `b65aecfc3d81d736`
- **Conditions:** `{"alt_prices": ["17.99"]}`
- **Raw:** `{"block_text": "Boulettes de bœuf\nà l'italienne\n130-140 UNITÉS", "ocr_lines": ["Boulettes debceuf", "al'italienne", "130-140UNITES"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 2. The Italian-style beef meatballs (130-140 count, 1.36 kg) are the cell's "aussi disponible" variant, priced in the side box at 22.99 member; the DB had 16.99 — the main cell product's price. Frozen Meals is right.

### Item 14335

![item 14335](images/item-14335.jpg)

- **Name (English):** None
- **Name (French):** AQUECA
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Meals, Entrees & Sides
- **Category (French):** Produits surgelés > Repas, plats principaux et accompagnements
- **How classified:** store-prior
- **Size:** None
- **Price:** 17.99
- **Printed Price:** “17.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 42, top 62, right 214, bottom 163, page 4
- **Full page:** [pages/flyer146-page4-1320b16523.jpg (flyer page 4)](pages/flyer146-page4-1320b16523.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-aliments-mm-du-15-au-21-octobre-2026/04.webp
- **Details:** confidence: 0.96 · item_key: `7fa5ff5e542048e8`
- **Conditions:** `{"alt_prices": ["19.99"]}`
- **Raw:** `{"block_text": "re", "ocr_lines": ["AQUECA"]}`

**Item Review Analysis (Pass 1):** Correct. The item (name fragment "AQUECA") carries the badge inside its own cell: 17.99 member (19.99 non-member) — verified from page 4. Frozen Meals is right.

### Item 14341

![item 14341](images/item-14341.jpg)

- **Name (English):** 340g Crevettesal'ail
- **Name (French):** 12-13UNITES
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** 340g
- **Price:** 19.99
- **Printed Price:** “19.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 33, top 696, right 321, bottom 837, page 5
- **Full page:** [pages/flyer146-page5-64fcd96675.jpg (flyer page 5)](pages/flyer146-page5-64fcd96675.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-aliments-mm-du-15-au-21-octobre-2026/05.webp
- **Details:** confidence: 0.99 · item_key: `159f561df8a95af1`
- **Conditions:** `{"alt_prices": ["24.99"]}`
- **Raw:** `{"block_text": "Crevettes à l'ail", "ocr_lines": ["12-13UNITES|340g", "Crevettesal'ail"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 5. Garlic shrimp (12-13 count, 340 g) print 12.99 member (14.99 non-member); the DB had 19.99 — the badge of the breaded product below. The stored name is only the count band ("12-13 UNITÉS"), which is also why it sits in Fresh Vegetables; the product is shrimp.

### Item 14349

![item 14349](images/item-14349.jpg)

- **Name (English):** 500g Quesadillasaupouletetaufromage
- **Name (French):** 4QUESADILLAS
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Meals, Entrees & Sides
- **Category (French):** Produits surgelés > Repas, plats principaux et accompagnements
- **How classified:** store-prior
- **Size:** 500g
- **Price:** 12.99
- **Printed Price:** “12.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 548, top 433, right 940, bottom 574, page 6
- **Full page:** [pages/flyer146-page6-c61c6e0670.jpg (flyer page 6)](pages/flyer146-page6-c61c6e0670.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-aliments-mm-du-15-au-21-octobre-2026/06.webp
- **Details:** confidence: 0.99 · item_key: `3da128029779a994`
- **Conditions:** `{"alt_prices": ["14.99"]}`
- **Raw:** `{"block_text": "Quésadillas au poulet et au fromage", "ocr_lines": ["4QUESADILLAS|500g", "Quesadillasaupouletetaufromage"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 6. Chicken and cheese quesadillas (4, 500 g) print 11.99 member / 12.99 non-member; the DB stored the non-member price — the one sampled item that broke the store's member-price convention. Now 11.99. Frozen Meals is right.

### Item 14351

![item 14351](images/item-14351.jpg)

- **Name (English):** 454g Batonnetsdemozzarella
- **Name (French):** 15-21UNITES
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Meals, Entrees & Sides
- **Category (French):** Produits surgelés > Repas, plats principaux et accompagnements
- **How classified:** store-prior
- **Size:** 454g
- **Price:** 12.99
- **Printed Price:** “12.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 25, top 532, right 296, bottom 706, page 6
- **Full page:** [pages/flyer146-page6-c61c6e0670.jpg (flyer page 6)](pages/flyer146-page6-c61c6e0670.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-aliments-mm-du-15-au-21-octobre-2026/06.webp
- **Details:** confidence: 0.99 · item_key: `6985aea0ef79ff2c`
- **Conditions:** `{"alt_prices": ["14.99"]}`
- **Raw:** `{"block_text": "Bâtonnets de mozzarella", "ocr_lines": ["15-21UNITES|454g", "Batonnetsdemozzarella"]}`

**Item Review Analysis (Pass 1):** Correct. Mozzarella sticks (15-21 count, 454 g) at 12.99 member (14.99 non-member) — verified from page 6; the stored name is the count band. Frozen Meals is right.

### Item 14356

![item 14356](images/item-14356.jpg)

- **Name (English):** None
- **Name (French):** Pouletetpatesavec sauceroseecremeuse
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Meals, Entrees & Sides
- **Category (French):** Produits surgelés > Repas, plats principaux et accompagnements
- **How classified:** store-prior
- **Size:** None
- **Price:** 19.99
- **Printed Price:** “19.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 24, top 226, right 271, bottom 353, page 7
- **Full page:** [pages/flyer146-page7-175be8837e.jpg (flyer page 7)](pages/flyer146-page7-175be8837e.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-aliments-mm-du-15-au-21-octobre-2026/07.webp
- **Details:** confidence: 0.99 · item_key: `f089cd86bf278a46`
- **Conditions:** `{"alt_prices": ["21.99", "19.99", "21.99"]}`
- **Raw:** `{"block_text": "Poulet et pâtes avec\nsauce rosée crémeuse", "ocr_lines": ["Pouletetpatesavec", "sauceroseecremeuse"]}`

**Item Review Analysis (Pass 1):** Correct. Chicken and pasta with creamy rosé sauce (907 g) at 19.99 member (21.99 non-member) — verified from page 7. Frozen Meals is right.

### Item 14358

![item 14358](images/item-14358.jpg)

- **Name (English):** None
- **Name (French):** Sautédepoulet
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Meals, Entrees & Sides
- **Category (French):** Produits surgelés > Repas, plats principaux et accompagnements
- **How classified:** store-prior
- **Size:** None
- **Price:** 19.99
- **Printed Price:** “19.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 540, top 237, right 711, bottom 352, page 7
- **Full page:** [pages/flyer146-page7-175be8837e.jpg (flyer page 7)](pages/flyer146-page7-175be8837e.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-aliments-mm-du-15-au-21-octobre-2026/07.webp
- **Details:** confidence: 0.99 · item_key: `46899c3ab8b107ae`
- **Conditions:** `{"alt_prices": ["21.99"]}`
- **Raw:** `{"block_text": "Sauté de poulet", "ocr_lines": ["Sautédepoulet"]}`

**Item Review Analysis (Pass 1):** Correct. Chicken stir-fry (840 g) at 19.99 member (21.99 non-member) — verified from page 7. Frozen Meals is right.

### Item 14374

![item 14374](images/item-14374.jpg)

- **Name (English):** None
- **Name (French):** AIGLEFIN PANE 7-10UNITES907g
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** 907g
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 522, top 283, right 688, bottom 392, page 10
- **Full page:** [pages/flyer146-page10-ada1fd1c4d.jpg (flyer page 10)](pages/flyer146-page10-ada1fd1c4d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-les-aliments-mm-du-15-au-21-octobre-2026/10.webp
- **Details:** confidence: 0.97 · item_key: `f11d373ec22b41db`
- **Conditions:** `{"alt_prices": ["5.99"]}`
- **Raw:** `{"block_text": "AIGLEFIN PANÉ\n7-10 UNITÉS 907 g", "ocr_lines": ["AIGLEFIN PANE", "7-10UNITES907g"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 10. Breaded haddock (7-10 count, 907 g) prints 27.99 member (29.99 non-member); the DB had 4.99 — the badge of the fries in the cell below. Fish is right.
