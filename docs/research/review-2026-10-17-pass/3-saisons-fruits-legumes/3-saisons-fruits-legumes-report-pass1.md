# Fruits & Légumes 3 Saisons — full product report

Store slug: `3-saisons-fruits-legumes`. Generated from `data/grocery.db`. A sampled subset of 4 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).

## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 174). Validity 2026-10-15 → 2026-10-21 matches the dates printed on the page ("SPÉCIAUX EN VIGUEUR DU 15 AU 21 OCTOBRE 2026"). Current and valid.
- **Sample counts:** 4 classified + 0 unclassified shown, of 4 + 0 in the DB. Below the 10 + 10 target for a valid reason: the flyer is a single page with only 5 products. Zero unclassified because every captured item classified cleanly — a classification success, not a sampling gap.
- **Page coverage:** the flyer has 1 page; it was scraped. 4 of the page's 5 products are captured. The missing one is the hero product (Pommes McIntosh/Cortland/Empire, 87¢/lb) — see patterns.
- **Issues found:** (1) the hero apples product is not captured at all; (2) item 16426 (chou-fleur) carries `alt_prices` of 8.79 and 1.92, which are the apples' prices, not the cauliflower's — metadata noise, its own price (2/6$) is correct; (3) the review crops of items 16424 and 16427 include a thin strip of the neighbouring cell's price splash at the top (cosmetic; stored data unaffected); (4) item 16424's name "Special OKA OKA" includes packaging text from the cheese wedges.
- **Patterns:** the page's hero layout (full-width banner product, name on a wooden sign to the LEFT of the price splash, script font) defeats the name-above-price assembly — tested `name_position: any` again this pass: it misassigns names across the whole page (bananas named "PRODUIT IMPORTE", cauliflower named onto the apples' price), so `above` stands and the miss is a documented layout limit. Dual-format prices ($/lb headline with $/kg equivalent) are handled correctly on the items that were captured.
- **Fixes applied this pass:** per-store crop padding override for this store in the review renderer (0.12 up-pad instead of 0.35) so crops stop importing the upstairs price splash. No ingest changes — the stored data for the 4 captured items is correct.

## Flyer 174 — valid 2026-10-15 → 2026-10-21 (4 classified items, 0 unclassified)

Source ref: `img-b715037618e68da8` · fetched 2026-10-17T15:40:03.633Z

### Item 16424

![item 16424](images/item-16424.jpg)

- **Name (English):** None
- **Name (French):** Special OKA OKA
- **Brand:** None
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** None
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 648, top 595, right 993, bottom 814, page 1
- **Full page:** [pages/flyer174-page1-fa2836c24e.jpg (flyer page 1)](pages/flyer174-page1-fa2836c24e.jpg)
- **Image source URL:** https://static.wixstatic.com/media/c266a2_a5de86dff5fb438cab37776097a1d151~mv2.jpeg
- **Details:** confidence: 0.93 · item_key: `f8b1f5f4d53b0f4b`
- **Raw:** `{"block_text": "> . x\n *\n& e ‘Sp\n. :\n: . . . :\n* « atid ih P -x\n- 2 Te eT .\nev CCl\n>) CR e\nFe\n+ es\ncase bere =\nà CENT © Nhe\n126 Coutts a\nAe FAA tour an > D>\nOnt Ore Det CS ne,\nCl ag «remis PC CE\nOC Ae Vers, Met\nao\" » Wa,\"", "ocr_lines": ["Special", "OKA", "OKA", "OKA"]}`

**Item Review Analysis (Pass 1):** Correct product, price and unit: the crop shows the OKA wedges at 2,99$ le 100 g, matching the stored 2.99 with unit (100, gram). Category Dairy & Eggs > Cheese is right. Two cosmetic issues: the name "Special OKA OKA" is assembled from the packaging labels printed on the wedges (the flyer's own product name is just "OKA"), and the crop's top edge catches the tail of the cauliflower's "2/6$" splash from the cell above — the stored price is unaffected. Brand None is valid (OKA is the product name; no separate brand is printed). Size None is valid: the cheese is sold per 100 g, no package size exists. The item belongs here.

### Item 16425

![item 16425](images/item-16425.jpg)

- **Name (English):** None
- **Name (French):** BANANES
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
- **bbox:** left 40, top 384, right 438, bottom 566, page 1
- **Full page:** [pages/flyer174-page1-fa2836c24e.jpg (flyer page 1)](pages/flyer174-page1-fa2836c24e.jpg)
- **Image source URL:** https://static.wixstatic.com/media/c266a2_a5de86dff5fb438cab37776097a1d151~mv2.jpeg
- **Details:** confidence: 0.81 · item_key: `55a68d013a09fec9`
- **Conditions:** `{"alt_prices": ["1.52"]}`
- **Raw:** `{"block_text": "BANANES", "ocr_lines": ["BANANES"]}`

**Item Review Analysis (Pass 1):** Fully correct. The crop shows bananas at 69¢/lb with the 1,52 $/kg equivalent printed beneath; the stored headline price 0.69 with unit (1, pound) is the right one, and the kg equivalent is correctly kept as an alt price rather than the headline. Name and category (Fresh Fruits) are right. Brand None and Size None are valid — bulk produce, neither is printed. The crop includes a strip of the page's validity banner at the top, which is harmless. The item belongs here.

### Item 16426

![item 16426](images/item-16426.jpg)

- **Name (English):** None
- **Name (French):** CHOU-FLEUR
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 3.00
- **Printed Price:** “2/6.00”
- **Unit quantity:** 2.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 524, top 385, right 989, bottom 578, page 1
- **Full page:** [pages/flyer174-page1-fa2836c24e.jpg (flyer page 1)](pages/flyer174-page1-fa2836c24e.jpg)
- **Image source URL:** https://static.wixstatic.com/media/c266a2_a5de86dff5fb438cab37776097a1d151~mv2.jpeg
- **Details:** confidence: 0.91 · item_key: `82d847d66d26933b`
- **Conditions:** `{"multibuy": {"count": 2, "total": 6.0}, "alt_prices": ["8.79", "1.92"]}`
- **Raw:** `{"block_text": "CHOU-FLEUR", "ocr_lines": ["CHOU-FLEUR"]}`

**Item Review Analysis (Pass 1):** Correct product, price and category: the crop shows the cauliflower at 2/6$, stored as 3.00 per item with unit (2, multiple) and printed price "2/6.00" — right. One data defect: the stored conditions list `alt_prices` of 8.79 and 1.92, which are the hero apples' prices from the top of the page (87¢ misread as 8.79, plus its 1,92 $/kg equivalent), folded into this item during segmentation. They do not affect the item's own price but are wrong metadata; left in place (no safe automatic cleanup distinguishes them from legitimate dual-rate alt prices like the bananas' 1.52) and recorded here. Brand None and Size None are valid — sold per unit, neither is printed. The item belongs here.

### Item 16427

![item 16427](images/item-16427.jpg)

- **Name (English):** None
- **Name (French):** EMMENTAL
- **Brand:** None
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** None
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 42, top 595, right 459, bottom 808, page 1
- **Full page:** [pages/flyer174-page1-fa2836c24e.jpg (flyer page 1)](pages/flyer174-page1-fa2836c24e.jpg)
- **Image source URL:** https://static.wixstatic.com/media/c266a2_a5de86dff5fb438cab37776097a1d151~mv2.jpeg
- **Details:** confidence: 0.82 · item_key: `4902dd590fe46afa`
- **Raw:** `{"block_text": "EMMENTAL", "ocr_lines": ["EMMENTAL"]}`

**Item Review Analysis (Pass 1):** Correct product, price, unit and category: the crop shows the emmental at 1,99$ le 100 g, matching the stored 1.99 with unit (100, gram). Name is clean. The crop's top edge catches a sliver of the bananas' price splash above (cosmetic; addressed by this store's crop-padding override). Brand None and Size None are valid — deli cheese sold per 100 g, neither a brand nor a package size is printed. The item belongs here.
