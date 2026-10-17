# Fruits & Légumes 3 Saisons — full product report

Store slug: `3-saisons-fruits-legumes`. Generated from `data/grocery.db`. A sampled subset of 4 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).

## Review Analysis — Pass 2 (2026-10-17, verification after Pass 1 fixes)

- Packet regenerated after the Pass 1 crop-padding fix. **The fix held:** item 16424's crop now shows only the OKA wedges and its own 2,99$ price (the cauliflower's 2/6$ tail is gone); item 16427's crop is likewise clean.
- Counts, flyer and validity unchanged: 1 flyer (174), 2026-10-15 → 2026-10-21, 4 classified + 0 unclassified of the page's 5 products.
- Stored data re-verified against the page: all 4 items' names, prices, units and categories are correct (bananes 0.69/lb, chou-fleur 2/6$, emmental 1.99/100 g, OKA 2.99/100 g).
- **Remaining known issues (documented, not fixable without regressions):** the hero pommes product (87¢/lb) is not captured — its name sits left of the price in script font and every name-assembly variant that reaches it misassigns the other four names; item 16426 still carries the apples' prices in its `alt_prices` metadata (own price correct); item 16424's name includes packaging text ("Special OKA OKA" for "OKA").
- Pass 1's full analysis is preserved in `3-saisons-fruits-legumes-report-pass1.md`. Store review complete.

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
