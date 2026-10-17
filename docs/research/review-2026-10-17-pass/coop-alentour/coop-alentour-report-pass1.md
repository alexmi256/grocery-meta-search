# Coop Alentour — full product report

Store slug: `coop-alentour`. Generated from `data/grocery.db`. A sampled subset of 15 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 166, valid 2026-10-14 → 2026-10-20). One page image, but the page bundles TWO printed circulars: "Fruits et légumes" (Oct 14–20, 6 products) and "Épicerie et suppléments" (Oct 7 – Nov 3, 16 products). The flyer record carries the first window; everything sampled is in force today either way, but grocery/supplement items from the second circular actually run to Nov 3 while the record expires them Oct 20 — a source-page granularity limit, recorded here.
- **Sample counts:** 10 classified + 5 unclassified shown, of 11 + 5 on the flyer — nearly the whole edition. The page holds 22 products: 16 captured, 5 discarded at ingest by design (laundry/dish detergent, vitamin C, an herbal tincture and two omega-3 supplements all classify non-grocery), and 1 true capture miss (the multigrain bread, whose three-line name sits under a shared price badge).
- **Issues found:** (1) four of the five unclassified items are supplements the vocabulary couldn't name (Flux-O-Bile, millepertuis/St John's Wort, a "Multi une par jour" multivitamin, plus a respiratory formula) — all carry ground-truth verdicts of Health & Beauty > Vitamins & Supplements, i.e. they should classify OUT of the grocery pool, not sit in review; (2) the kombucha (item 15694, not sampled) is captured at the right price and category but its name carries a stray "ESA " prefix glued from neighbouring print; (3) the generic snack box ("COLLATION SAVEURS ASSORTIES" — Henri bars, 5 x 40 g) was unclassified although the ground truth shelves it in Chips & Snacks.
- **Patterns:** natural-food co-ops stock supplements whose names are pure brand/product words with no category vocabulary; a small set of product-name phrases in the vitamins rule routes them correctly. Prices throughout use the flyer's large member price (the small "régulier membre" badge is the regular price) — the right choice, verified per item.
- **Fixes applied this pass:** vitamins vocabulary added (millepertuis, flux o bile, multi une par jour) and the exact phrase "collation saveurs assorties" added to Chips & Snacks. Ground truth 12372 → 12376 items, 8260 → 8264 signatures. Data: reclassify flipped 8 items; the 6 newly non-grocery supplements were purged. Remaining unclassified at this store: the respiratory formula (no vocabulary exists for it) — kept for review.

## Flyer 166 — valid 2026-10-14 → 2026-10-20 (10 classified items, 5 unclassified)

Source ref: `circulaire-coop-alentour-du-14-au-20-octobre-2026` · fetched 2026-10-17T05:50:21.590Z

### Item 15699

![item 15699](images/item-15699.jpg)

- **Name (English):** None
- **Name (French):** CITROUILLES VERTE-BEIGE (WAN FU) BIO
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 0.85
- **Printed Price:** “0.85”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 64, top 279, right 346, bottom 307, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.92 · item_key: `74f025bbce9d82d0`
- **Raw:** `{"block_text": "0,85 S$ /Ib\nCITROUILLES VERTE-BEIGE (WAN FU) BIO", "ocr_lines": ["QUEBE", "CITROUILLESVERTE-BEIGE(WANFU)BIO"]}`

**Item Review Analysis (Pass 1):** Correct. Wan Fu green-beige pumpkins, bulk, at the member price 0.85 $/lb (regular 1.35) — stored price 0.85 with unit pound is right; Fresh Vegetables fits. Crop is exactly the price banner + name.

### Item 15701

![item 15701](images/item-15701.jpg)

- **Name (English):** None
- **Name (French):** CARROTTES A JUS ECONOMIQUES BIO
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** 11,35kg
- **Price:** 17.99
- **Printed Price:** “17.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 364, top 382, right 639, bottom 409, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.92 · item_key: `f03dc95ef44e77da`
- **Raw:** `{"block_text": "_ 17,998 |\nCARROTTES A JUS ECONOMIQUES BIO", "ocr_lines": ["QUEBE", "CARROTTESAJUSECONOMIQUESBIO"], "harvest": {"size": "11,35kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Bulk juicing carrots, 11.35 kg case at 17.99 (member; regular 19.99) — price, size (stored "11,35kg") and Fresh Vegetables all match the page.

### Item 15702

![item 15702](images/item-15702.jpg)

- **Name (English):** None
- **Name (French):** CAISSE DE TOMATE RONDE OU ITALIENNE DÉCLASSÉES BIO
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** 9,07 kg
- **Price:** 18.99
- **Printed Price:** “18.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 682, top 384, right 960, bottom 417, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.96 · item_key: `d573c967425b5479`
- **Raw:** `{"block_text": "CAISSE DE TOMATE RONDE OU ITALIENNE\nDÉCLASSÉES BIO", "ocr_lines": ["CAISSEDETOMATERONDEOUITALIENNE", "DECLASSEESBIO"], "harvest": {"size": "9,07 kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Case of downgraded round/Italian tomatoes, 9.07 kg at 18.99 (regular 26.99) — all values match.

### Item 15703

![item 15703](images/item-15703.jpg)

- **Name (English):** None
- **Name (French):** LEVURE NUTRITIONNELLE EN FLOCONS
- **Brand:** None
- **Category (English):** Pantry > Baking Essentials
- **Category (French):** Produits du garde-manger > Essentiels de cuisson
- **How classified:** rule (`baking`)
- **Size:** 284g
- **Price:** 19.99
- **Printed Price:** “19.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 767, top 703, right 959, bottom 737, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.86 · item_key: `4c342c3fa727df30`
- **Raw:** `{"block_text": "LEVURE NUTRITIONNELLE EN\nFLOCONS", "ocr_lines": ["LEVURENUTRITIONNELLEEN", "FLOCONS"], "harvest": {"size": "284g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. NOW nutritional yeast flakes, 284 g at 19.99 — Baking Essentials is where this taxonomy shelves nutritional yeast; name/price/size verified on the page.

### Item 15704

![item 15704](images/item-15704.jpg)

- **Name (English):** None
- **Name (French):** PERSIL ITALIEN OU FRISE BIO
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Herbs
- **Category (French):** Fruits et légumes > Fines herbes
- **How classified:** rule (`herbs-fresh`)
- **Size:** None
- **Price:** 2.15
- **Printed Price:** “2.15”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 724, top 281, right 919, bottom 307, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.88 · item_key: `d0cbdcab7dfbd51e`
- **Raw:** `{"block_text": "—————————x—”—\nPERSIL ITALIEN OU FRISE BIO", "ocr_lines": ["PERSIL ITALIEN OU FRISEBIO"]}`

**Item Review Analysis (Pass 1):** Correct. Italian or curly parsley, organic, 2.15 each (regular 2.79) — Herbs is right; size None is valid for a herb bunch.

### Item 15705

![item 15705](images/item-15705.jpg)

- **Name (English):** None
- **Name (French):** PIZZA SORTES VARIÉES
- **Brand:** None
- **Category (English):** Prepared Meals > Pizza
- **Category (French):** Repas préparés > Pizzas
- **How classified:** rule (`pizza-prepared`)
- **Size:** 400 -500 g
- **Price:** 11.99
- **Printed Price:** “11.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 114, top 704, right 273, bottom 730, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.91 · item_key: `0b860439207453d4`
- **Raw:** `{"block_text": "PIZZA SORTES VARIÉES", "ocr_lines": ["PIZZASORTESVARIEES"], "harvest": {"size": "400 -500 g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Porta assorted pizzas, 400-500 g at 11.99 (regular 13.99) — Prepared Meals > Pizza, size range stored as printed.

### Item 15706

![item 15706](images/item-15706.jpg)

- **Name (English):** None
- **Name (French):** AVOCAT BIO
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 0.99
- **Printed Price:** “0.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 464, top 280, right 562, bottom 307, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.91 · item_key: `2d67d6d5e6012632`
- **Raw:** `{"block_text": "AVOCAT BIO", "ocr_lines": ["AVOCATBIO"]}`

**Item Review Analysis (Pass 1):** Correct. Organic avocado at 0.99 each (regular 1.29) — Fresh Fruits is right.

### Item 15707

![item 15707](images/item-15707.jpg)

- **Name (English):** None
- **Name (French):** LAIT DE COCO BIO
- **Brand:** None
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`specific-coconut-milk`)
- **Size:** 400ml
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 133, top 596, right 254, bottom 622, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.89 · item_key: `d0981757b2e65d1d`
- **Raw:** `{"block_text": "LAIT DE COCO BIO", "ocr_lines": ["LAITDECOCOBIO"], "harvest": {"size": "400ml", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Mère Nature organic coconut milk, 400 ml at 2.99 (regular 3.29) — Canned & Pickled is the taxonomy's shelf for canned coconut milk.

### Item 15708

![item 15708](images/item-15708.jpg)

- **Name (English):** None
- **Name (French):** BEURRE DE TAHINI BIO
- **Brand:** None
- **Category (English):** Dairy & Eggs > Butter & Spreads
- **Category (French):** Produits laitiers et œufs > Beurre et tartinades
- **How classified:** rule (`butter`)
- **Size:** 735g
- **Price:** 12.99
- **Printed Price:** “12.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 345, top 705, right 496, bottom 730, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.91 · item_key: `c3f802be760c5521`
- **Raw:** `{"block_text": "BEURRE DE TAHINI BIO", "ocr_lines": ["BEURREDETAHINIBIO"], "harvest": {"size": "735g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Nuts to You organic tahini butter, 735 g at 12.99 (regular 14.99) — all values match. Category note: Dairy & Eggs > Butter & Spreads here ("beurre de tahini"), while Adonis's tahina sits in International > Middle Eastern — both defensible readings of the same product under this taxonomy.

### Item 15709

![item 15709](images/item-15709.jpg)

- **Name (English):** None
- **Name (French):** KALE EN SAC BIO
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Packaged Salads & Dressing
- **Category (French):** Fruits et légumes > Salades préemballées et vinaigrettes
- **How classified:** rule (`packaged-salads`)
- **Size:** 200 g
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 152, top 382, right 266, bottom 409, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.98 · item_key: `67b4ddb825e967b2`
- **Raw:** `{"block_text": "KALE EN SAC BIO", "ocr_lines": ["KALE ENSACBIO"], "harvest": {"size": "200 g", "via": "crop"}}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 166 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Correct. Bagged organic kale, 200 g at 2.99 (regular 3.49) — Packaged Salads & Dressing is the bagged-greens shelf; values match.

### Item 15695

![item 15695](images/item-15695.jpg)

- **Name (English):** None
- **Name (French):** COLLATION SAVEURS ASSORTIES
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 5 x 40 g
- **Price:** 5.49
- **Printed Price:** “5.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 532, top 596, right 708, bottom 630, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.89 · item_key: `49ee55a700ff72a1`
- **Raw:** `{"block_text": "COLLATION SAVEURS\nASSORTIES", "ocr_lines": ["QUEBE", "COLLATIONSAVEURS", "ASSORTIES"], "harvest": {"size": "5 x 40 g", "via": "crop"}}`

— from flyer 166 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Fixed this pass. Henri assorted snack bars (5 x 40 g) at 5.49 — the picture confirms a boxed snack product; the name is only the generic words "COLLATION SAVEURS ASSORTIES", which no rule matched. The exact phrase now maps to Chips & Snacks, per the ground-truth verdict.

### Item 15696

![item 15696](images/item-15696.jpg)

- **Name (English):** None
- **Name (French):** FLUX-O-BILE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 10 unites
- **Price:** 24.59
- **Printed Price:** “24.59”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 79, top 942, right 225, bottom 966, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.90 · item_key: `08c7cac1f209bb19`
- **Raw:** `{"block_text": "ma 24,59 :\nFLUX-O-BILE", "ocr_lines": ["QUEBE", "FLUX-O-BILE"], "harvest": {"size": "10 unites", "via": "crop"}}`

— from flyer 166 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Fixed this pass. Flux-O-Bile (Nutripur digestive supplement, 10 units) at 24.59 — a supplement, not a grocery item; the product-name phrase was added to the vitamins rule, it reclassified to Health & Beauty > Vitamins & Supplements and was purged as non-grocery.

### Item 15697

![item 15697](images/item-15697.jpg)

- **Name (English):** None
- **Name (French):** MULTI UNE PAR JOUR AVEC FER SUPRÊME
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 180unites
- **Price:** 40.89
- **Printed Price:** “40.89”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 505, top 943, right 718, bottom 973, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.93 · item_key: `09074d57495d0f55`
- **Raw:** `{"block_text": "MULTI UNE PAR JOUR AVEC FER\nSUPRÊME", "ocr_lines": ["MULTIUNEPARJOURAVECFER", "SUPREME"], "harvest": {"size": "180unites", "via": "crop"}}`

— from flyer 166 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Fixed this pass. Health First "Multi une par jour avec fer" multivitamin (180 units) at 40.89 — same disposition as 15696: vitamins phrase added, reclassified, purged.

### Item 15698

![item 15698](images/item-15698.jpg)

- **Name (English):** None
- **Name (French):** MILLEPERTUIS 400 MG
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 400 MG
- **Price:** 16.49
- **Printed Price:** “16.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 78, top 843, right 244, bottom 867, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.85 · item_key: `88efc9404a037bf8`
- **Raw:** `{"block_text": "MILLEPERTUIS 400 MG", "ocr_lines": ["QUEBEC", "MILLEPERTUIS400MG"]}`

— from flyer 166 (valid 2026-10-14 → 2026-10-20)

**Item Review Analysis (Pass 1):** Fixed this pass. Gamma Force millepertuis (St John's Wort, 400 mg, 60 units) at 16.49 — "millepertuis" added to the vitamins vocabulary; reclassified and purged.

### Item 15700

![item 15700](images/item-15700.jpg)

- **Name (English):** None
- **Name (French):** POUMONS, BRONCHES ET SINUS SAINS
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 90 unites
- **Price:** 23.89
- **Printed Price:** “23.89”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 744, top 842, right 914, bottom 874, page 1
- **Full page:** [pages/flyer166-page1-92ef40a8d4.jpg (flyer page 1)](pages/flyer166-page1-92ef40a8d4.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-coop-alentour-du-14-au-20-octobre-2026/01.webp
- **Details:** confidence: 0.91 · item_key: `da4721ea0c750db4`
- **Raw:** `{"block_text": "POUMONS, BRONCHES ET\nSINUS SAINS", "ocr_lines": ["POUMONS,BRONCHESET", "SINUS SAINS"], "harvest": {"size": "90 unites", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Kept, correctly unclassified. Natural Factors "Poumons, bronches et sinus sains" respiratory supplement (90 units) at 23.89 — a supplement by the photo and dosage form, but the name is a health claim with no product vocabulary; no honest phrase routes it. It stays in the review pool.
