# Bulk Barn — full product report

Store slug: `bulk-barn`. Generated from `data/grocery.db`. A sampled subset of 3 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 109, valid 2026-10-15 → 2026-10-21). The printed validity on the page ("Du 15 octobre au 21 octobre 2026") matches. The DB also holds the expired Oct 8–14 edition, correctly excluded.
- **Sample counts:** 3 classified + 0 unclassified shown, of 3 + 0 on the flyer — everything captured is shown. The shortfall against the page's 5 products is a CAPTURE gap, not a sampling or classification effect (see below).
- **Page coverage:** the flyer is a single page with 5 products. Three are captured with correct prices, units and categories. Two are missing, both re-investigated this morning and again today against this exact page image: (1) **dry roasted almonds (2.06/100 g)** — the price badge anchors, but the product name sits at the page's top-left while the badge sits at the far right behind the "Des économies à la pelle!" promo tag; no name-assembly setting tested connects them without breaking the other cells; (2) **Dare jelly beans (79¢/100 g)** — the small cents badge anchors in only about 1 of 3 OCR runs; it did not anchor in today's segmentation run either (4 of 5 badges found). Both are recorded as this store's documented limits.
- **Issues found in the captured items:** stored names concatenate the French and English name lines into the French field with accents stripped (the CC page-OCR pattern — the classifier handles them fine, and item search still matches either language's words, but name_en is never populated for this source). Crops catch a sliver of the neighbouring cell at one edge (the wide name band) — cosmetic. One name carries an OCR-glued descriptor ("Rotiesetsalees").
- **Patterns:** none new — Bulk Barn's poster layout (badges detached from names, percent-off banners) is the pipeline's hardest single-page shape, and its three straightforward cells extract perfectly.
- **Fixes applied this pass:** none. The two missing products were already chased with per-store settings this morning; the remaining options (position-tolerant name assembly for this one page) risk the working cells and are not warranted for two bulk items. Recorded as the store's known limit.

## Flyer 109 — valid 2026-10-15 → 2026-10-21 (3 classified items, 0 unclassified)

Source ref: `circulaire-bulk-barn-du-15-au-21-octobre-2026` · fetched 2026-10-16T12:04:55.684Z

### Item 11668

![item 11668](images/item-11668.jpg)

- **Name (English):** None
- **Name (French):** Tranches de mangues sechees Non sucrees Dried Mango Slices
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Dried Fruits & Nuts
- **Category (French):** Fruits et légumes > Fruits séchés et noix
- **How classified:** dried-remap (`fruits`)
- **Size:** None
- **Price:** 3.88
- **Printed Price:** “3.88”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 16, top 500, right 482, bottom 612, page 1
- **Full page:** [pages/flyer109-page1-d71b5bdf0d.jpg (flyer page 1)](pages/flyer109-page1-d71b5bdf0d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bulk-barn-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `6d0fa69bd0234a6e`
- **Raw:** `{"block_text": "Tranches de mangues séchées\nNon sucrées\nDried Mango Slices fi &", "ocr_lines": ["Tranches de mangues sechees", "Non sucrees", "Dried Mango Slices", "Unsweetened"], "harvest": {"unit": "100g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Dried mango slices, unsweetened, 3.88 per 100 g (was 5.18) — price, unit (100 g via the segment fallback + the store's unit-only harvest) and Dried Fruits & Nuts category all verified on the page. Size None is valid: bulk product sold by weight. Stored name concatenates the FR and EN lines (CC source pattern).

### Item 11669

![item 11669](images/item-11669.jpg)

- **Name (English):** None
- **Name (French):** Friandises Reese's Pieces Originales Reese's Pieces
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** None
- **Price:** 2.26
- **Printed Price:** “2.26”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 506, top 715, right 964, bottom 825, page 1
- **Full page:** [pages/flyer109-page1-d71b5bdf0d.jpg (flyer page 1)](pages/flyer109-page1-d71b5bdf0d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bulk-barn-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `4294e788dd9058e7`
- **Raw:** `{"block_text": "Friandises Reese’s Pieces\nOriginales\n|Reese’s Pieces ~", "ocr_lines": ["Friandises Reese's Pieces", "Originales", "Reese's Pieces"], "harvest": {"unit": "100g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Reese's Pieces, 2.26 per 100 g (was 3.02) — all values verified on the page. Candy & Chocolate is right. Size None is valid (bulk).

### Item 11670

![item 11670](images/item-11670.jpg)

- **Name (English):** None
- **Name (French):** Noix melangees avec arachides Rotiesetsalees Mixed Nuts with Peanuts
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Dried Fruits & Nuts
- **Category (French):** Fruits et légumes > Fruits séchés et noix
- **How classified:** rule (`dried-fruits-nuts`)
- **Size:** None
- **Price:** 2.47
- **Printed Price:** “2.47”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 507, top 501, right 964, bottom 615, page 1
- **Full page:** [pages/flyer109-page1-d71b5bdf0d.jpg (flyer page 1)](pages/flyer109-page1-d71b5bdf0d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-bulk-barn-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `e30a34e636a80d67`
- **Conditions:** `{"alt_prices": ["2.06"]}`
- **Raw:** `{"block_text": "Noix mélangées avec arachides\nRôties et salées\nMixed Nuts with Peanuts faa", "ocr_lines": ["Noix melangees avec arachides", "Rotiesetsalees", "Mixed Nuts with Peanuts"], "harvest": {"unit": "100g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Mixed nuts with peanuts, roasted and salted, 2.47 per 100 g (was 3.30) — price, unit and Dried Fruits & Nuts verified. The stored name's descriptor is OCR-glued ("Rotiesetsalees"); cosmetic. Size None is valid (bulk).
