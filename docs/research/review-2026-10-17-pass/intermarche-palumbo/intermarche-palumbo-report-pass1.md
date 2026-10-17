# L'intermarché Palumbo — full product report

Store slug: `intermarche-palumbo`. Generated from `data/grocery.db`. A sampled subset of 5 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17) — edition repaired during this review

- **Flyers in this review:** 1 current edition (Oct 15–21; the printed validity on the page, "DU 15 AU 21 OCTOBRE 2026", matches). The expired Oct 8–14 edition is correctly excluded.
- **Sample counts:** 1 classified + 4 unclassified — everything the edition holds. The page prints 6 products; the edition now holds 5 of them (see below).
- **Issues found — a silently degraded fetch, repaired:** as first generated, this packet held ONE item (the chicken). The page prints 6 priced products, and a fresh segmentation run forms all 6 — the stored edition was a partial capture from the Oct 16 parallel-refresh degradation, missed by the earlier audit because the store's baseline is tiny (7 items; the thin-edition guard needs a shortfall of 10+ by design). The edition was deleted and re-fetched solo (the sanctioned repair): now 5 of 6 products, every price correct against the page (2.99, 9.99, 8.99, 6.99/lb, 10.99). The missing sixth, Cuddy turkey at 13.99/lb, forms only intermittently — this run's OCR did not assemble it.
- **Issues found — names from labels, not display type:** four items are unclassified because the segmenter names them from the product LABEL text ("SAUCE BABILICO" off the Rudolfi jar, "Pre _ DARMESAN—)" off the Grande bags) instead of the flyer's big green display names ("SAUCE POUR PÂTES RUDOLFI", "ROMANO OU PARMESAN RÂPÉ GRANDE"). Raising the name-line height cap did not change the picks — the display lines lose the block assembly for another reason. Recorded as this store's tailored-detection item (same class as the Frutta Si flag); prices are unaffected.
- **Fixes applied this pass:** edition deleted and re-fetched solo (flyer 175 replaces the degraded flyer 124); backup `grocery.db.bak-20261017d` predates the repair.

## Flyer 175 — valid 2026-10-15 → 2026-10-21 (1 classified items, 4 unclassified)

Source ref: `circulaire-intermarche-palumbo-du-15-au-21-octobre-2026` · fetched 2026-10-17T17:01:32.468Z

### Item 16431

![item 16431](images/item-16431.jpg)

- **Name (English):** None
- **Name (French):** POITRINE DE POULET DESOSSEE BONELESS CHICKEN
- **Brand:** None
- **Category (English):** Meat > Chicken & Turkey
- **Category (French):** Viande > Poulet et dinde
- **How classified:** rule (`chicken-turkey`)
- **Size:** None
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 689, top 428, right 981, bottom 686, page 1
- **Full page:** [pages/flyer175-page1-4e20a10cf6.jpg (flyer page 1)](pages/flyer175-page1-4e20a10cf6.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-intermarche-palumbo-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `5b0895509d8e4ad7`
- **Raw:** `{"block_text": "POITRINE DE POULET\nDESOSSEE\nBONELESS CHICKEN", "ocr_lines": ["POITRINEDEPOULET", "DESOSSEE", "BONELESSCHICKEN", "BREAST"]}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 175 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Boneless chicken breast at 6.99/lb (15.41/kg) — verified on the page. Chicken & Turkey is right; this was the degraded edition's sole survivor.

### Item 16428

![item 16428](images/item-16428.jpg)

- **Name (English):** None
- **Name (French):** SAUCE BABILICO
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
- **bbox:** left 33, top 884, right 180, bottom 988, page 1
- **Full page:** [pages/flyer175-page1-4e20a10cf6.jpg (flyer page 1)](pages/flyer175-page1-4e20a10cf6.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-intermarche-palumbo-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `d4977eb809124c25`
- **Raw:** `{"block_text": "SAUCE\nBABILICO\n~ ds", "ocr_lines": ["SAUCE", "BASILICO"]}`

— from flyer 175 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Price correct (2.99, Rudolfi pasta sauce 680 ml, reg. 6.49); name wrong — taken from the jar label ("SAUCE BABILICO") instead of the display name "SAUCE POUR PÂTES RUDOLFI", so it sits unclassified. Recorded in the header analysis.

### Item 16429

![item 16429](images/item-16429.jpg)

- **Name (English):** None
- **Name (French):** Pre _ DARMESAN—)
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 9.99
- **Printed Price:** “9.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 350, top 882, right 563, bottom 995, page 1
- **Full page:** [pages/flyer175-page1-4e20a10cf6.jpg (flyer page 1)](pages/flyer175-page1-4e20a10cf6.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-intermarche-palumbo-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `ebccd49ca76f67ac`
- **Raw:** `{"block_text": "Pme,\nPre _ DARMESAN—)\n[Saw Motu AQ0, MOBTUREAS |", "ocr_lines": ["ROMANO=PARMESAN="]}`

— from flyer 175 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Price correct (9.99, Grande grated romano/parmesan 500 g, reg. 12.99); name is label garble ("Pre _ DARMESAN—)") instead of "ROMANO OU PARMESAN RÂPÉ GRANDE" — unclassified on the garble.

### Item 16430

![item 16430](images/item-16430.jpg)

- **Name (English):** None
- **Name (French):** BORBONE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 8.99
- **Printed Price:** “8.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 50, top 539, right 263, bottom 703, page 1
- **Full page:** [pages/flyer175-page1-4e20a10cf6.jpg (flyer page 1)](pages/flyer175-page1-4e20a10cf6.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-intermarche-palumbo-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `ef9c3b9ffb329ba3`
- **Conditions:** `{"alt_prices": ["12.99"]}`
- **Raw:** `{"block_text": "RS\nBORBONE |", "ocr_lines": ["BORBONE"]}`

— from flyer 175 (valid 2026-10-15 → 2026-10-21)

**Item Review Analysis (Pass 1):** Price correct (8.99, Borbone coffee capsules, 30 count assorted, reg. 12.99); the name is just the brand — the display name "CAPSULES DE CAFÉ ASSORTIS" was not assembled, so it sits unclassified (with the full name it is Drinks > Coffee).

### Item 16432

![item 16432](images/item-16432.jpg)

- **Name (English):** None
- **Name (French):** TENTACULES DE CALAMARS FERMA 908G
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 908G
- **Price:** 10.99
- **Printed Price:** “10.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 703, top 731, right 938, bottom 996, page 1
- **Full page:** [pages/flyer175-page1-4e20a10cf6.jpg (flyer page 1)](pages/flyer175-page1-4e20a10cf6.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-intermarche-palumbo-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `64da338ccea7e236`
- **Raw:** `{"block_text": "TENTACULES DE\nCALAMARS\nFERMA 908G", "ocr_lines": ["TENTACULESDE", "CALAMARS", "FERMA"]}`

**Item Review Analysis (Pass 1):** Price correct (10.99, Ferma squid tentacles 908 g, reg. 15.99) and the name is complete — but "tentacules de calamars" has no classifier vocabulary, so it stays unclassified for review. A genuine vocabulary gap, recorded rather than patched for one item.
