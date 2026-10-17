# Akhavan — full product report

Store slug: `akhavan`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 158, valid 2026-10-14 → 2026-10-20). The printed validity on the page ("Spéciaux en vigueur du mercredi 14 octobre au mardi 20 octobre 2026") matches. The DB also holds the expired Oct 7–13 edition, correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown, of 36 + 0 on the current flyer. Zero unclassified is a classification success: Akhavan is parsed from its official PDF's text layer (structured brand + FR/EN names), and every item classifies. The full edition was verified beyond the sample: all 36 products on the page are in the DB with correct prices.
- **Page coverage:** the flyer is a single-page PDF (6 × 6 grid = 36 products); the page was scraped completely — 36 of 36 products captured.
- **Issues found:** none affecting correctness. Two source quirks worth recording: (1) item 15167's French and English names describe different flavours ("THÉ HERBAL À LA BORAGE" vs "MIX HERBAL TEA (Mint Mix)") — that is the flyer's own printed text, faithfully captured, not a pairing error; (2) item 15180's size is "30 cm", the fish's length as printed — the size slot carries the source's spec verbatim. Item 15185's size ("10 lbs") and the potatoes' ("Sac 10 lbs. /4.54 kg bag") are likewise verbatim source strings.
- **Patterns:** the structured text-layer parse is this pipeline's most reliable source class — crops are exact cells, per-lb pricing is captured correctly (walnuts 4.49/lb, lamb ribs 8.99/lb, kafta kebab 6.99/lb, beets 0.49/lb), and no field needed correction.
- **Fixes applied this pass:** none required.

## Flyer 158 — valid 2026-10-14 → 2026-10-20 (10 classified items, 0 unclassified)

Source ref: `https://akhavanfood.com/wp-content/uploads/2026/10/41-26-Akhavan-8x175-1.pdf` · fetched 2026-10-16T14:33:30.517Z

### Item 15157

![item 15157](images/item-15157.jpg)

- **Name (English):** DRIED WHITE LIME
- **Name (French):** LIMETTES SÉCHÉES BLANCHES
- **Brand:** AKHAVAN
- **Category (English):** Fruits & Vegetables > Dried Fruits & Nuts
- **Category (French):** Fruits et légumes > Fruits séchés et noix
- **How classified:** dried-remap (`fruits`)
- **Size:** 2 lbs.
- **Price:** 7.99
- **Printed Price:** “7 99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 172, top 351, right 330, bottom 454, page 1
- **Full page:** [pages/flyer158-page1-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page1-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `0a195599e6a2512c`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["7", "99"], "cell_pt": [121.8, 316.2, 234.2, 408.2], "size": "2 lbs."}`

**Item Review Analysis (Pass 1):** Correct. Crop/page show dried white limes ("LIMETTES SÉCHÉES BLANCHES / DRIED WHITE LIME"), 2 lbs, at 7.99 — stored values match. Dried Fruits & Nuts is right.

### Item 15160

![item 15160](images/item-15160.jpg)

- **Name (English):** IRANIAN CURRY POWDER
- **Name (French):** POUDRE DE CARI IRANIEN
- **Brand:** AKHAVAN
- **Category (English):** International Foods > South Asian Foods
- **Category (French):** Aliments internationaux > Aliments de l'Asie du Sud
- **How classified:** rule (`south-asian`)
- **Size:** 110 g
- **Price:** 2.99
- **Printed Price:** “2 99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 669, top 351, right 828, bottom 454, page 1
- **Full page:** [pages/flyer158-page1-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page1-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `67dd553416f3f547`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["2", "99"], "cell_pt": [474.2, 316.2, 586.8, 408.2], "size": "110 g"}`

**Item Review Analysis (Pass 1):** Correct. Iranian curry powder, 110 g, 2.99 — matches the page. South Asian Foods fits a curry powder in this taxonomy.

### Item 15162

![item 15162](images/item-15162.jpg)

- **Name (English):** TOMATO PASTE
- **Name (French):** CONCENTRÉ DE TOMATE
- **Brand:** ÖNCÜ
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`canned-pickled`)
- **Size:** 4350 g
- **Price:** 16.99
- **Printed Price:** “16 99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 458, right 165, bottom 560, page 1
- **Full page:** [pages/flyer158-page1-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page1-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `6f7aef3056ce367a`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["16", "99"], "cell_pt": [4.2, 412.2, 116.8, 504.2], "size": "4350 g"}`

**Item Review Analysis (Pass 1):** Correct. Öncü tomato paste in the large food-service format — the printed size really is 4350 g — at 16.99. Canned & Pickled is right; the crop is exactly the product's cell.

### Item 15165

![item 15165](images/item-15165.jpg)

- **Name (English):** TI-TAP CAKE
- **Name (French):** GÂTEAU TI-TAP
- **Brand:** SALEMIN
- **Category (English):** Bakery > Cakes
- **Category (French):** Boulangerie > Gâteaux
- **How classified:** rule (`cakes`)
- **Size:** 24x60 g
- **Price:** 20.00
- **Printed Price:** “20 00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 503, top 458, right 662, bottom 560, page 1
- **Full page:** [pages/flyer158-page1-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page1-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `b030c0783889aa07`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["20", "00"], "cell_pt": [356.8, 412.2, 469.2, 504.2], "size": "24x60 g"}`

**Item Review Analysis (Pass 1):** Correct. Salemin Ti-Tap cake, 24x60 g case, 20.00 — matches the page (the neighbouring hazelnut tiny-cake at the same price is a separate item in the DB). Bakery > Cakes is right.

### Item 15167

![item 15167](images/item-15167.jpg)

- **Name (English):** MIX HERBAL TEA (Mint Mix)
- **Name (French):** THÉ HERBAL À LA BORAGE
- **Brand:** MEHRE GIAH
- **Category (English):** Drinks > Tea & Hot Drinks
- **Category (French):** Boissons > Thés et boissons chaudes
- **How classified:** rule (`tea-hot-drinks`)
- **Size:** 14 SACHETS - 14 TEA BAGS
- **Price:** 2.99
- **Printed Price:** “2 99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 458, right 993, bottom 560, page 1
- **Full page:** [pages/flyer158-page1-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page1-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `7dacc855089db1c3`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["2", "99"], "cell_pt": [591.8, 412.2, 704.2, 504.2], "size": "14 SACHETS - 14 TEA BAGS"}`

**Item Review Analysis (Pass 1):** Faithful to a quirky source. The cell prints "THÉ HERBAL À LA BORAGE" in French and "MIX HERBAL TEA (Mint Mix)" in English for one product (14 tea bags, 2.99, both stored correctly). The flavour mismatch is the flyer's own text, not a parse error. Tea & Hot Drinks is right.

### Item 15168

![item 15168](images/item-15168.jpg)

- **Name (English):** TAHINA
- **Name (French):** TAHINA
- **Brand:** CORTAS
- **Category (English):** International Foods > Middle Eastern Foods
- **Category (French):** Aliments internationaux > Aliments du Moyen-Orient
- **How classified:** rule (`middle-eastern`)
- **Size:** 454 g
- **Price:** 3.99
- **Printed Price:** “3 99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 565, right 165, bottom 667, page 1
- **Full page:** [pages/flyer158-page1-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page1-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `5381b1222a71c258`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "99"], "cell_pt": [4.2, 508.2, 116.8, 600.2], "size": "454 g"}`

**Item Review Analysis (Pass 1):** Correct. Cortas tahina, 454 g, 3.99 — matches the page. Middle Eastern Foods is the taxonomy's home for tahina.

### Item 15173

![item 15173](images/item-15173.jpg)

- **Name (English):** DATE VINEGAR
- **Name (French):** VINAIGRE DE DATTES
- **Brand:** 1&1
- **Category (English):** Pantry > Oils & Vinegar
- **Category (French):** Produits du garde-manger > Huile et vinaigre
- **How classified:** rule (`oils-vinegar`)
- **Size:** 330 ml
- **Price:** 1.99
- **Printed Price:** “1 99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 565, right 993, bottom 667, page 1
- **Full page:** [pages/flyer158-page1-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page1-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `044444feb258f184`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["1", "99"], "cell_pt": [591.8, 508.2, 704.2, 600.2], "size": "330 ml"}`

**Item Review Analysis (Pass 1):** Correct. 1&1 date vinegar, 330 ml, 1.99 — matches the page. Oils & Vinegar is right.

### Item 15177

![item 15177](images/item-15177.jpg)

- **Name (English):** MAZAFATI DATE ORGANIC
- **Name (French):** DATES MAZAFATI
- **Brand:** EMTIAZ
- **Category (English):** Fruits & Vegetables > Dried Fruits & Nuts
- **Category (French):** Fruits et légumes > Fruits séchés et noix
- **How classified:** rule (`dried-fruits-nuts`)
- **Size:** 650 g
- **Price:** 1.99
- **Printed Price:** “1 99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 503, top 671, right 662, bottom 774, page 1
- **Full page:** [pages/flyer158-page1-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page1-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `714a82d047c67e3d`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["1", "99"], "cell_pt": [356.8, 604.2, 469.2, 696.2], "size": "650 g"}`

**Item Review Analysis (Pass 1):** Correct. Emtiaz Mazafati dates, 650 g, at 1.99 — the price looks low for the size but is exactly what the page prints (a loss-leader). Dried Fruits & Nuts is right.

### Item 15180

![item 15180](images/item-15180.jpg)

- **Name (English):** CANADIAN LAKE WHITEFISH
- **Name (French):** CORÉGONE DE LAC CANADIEN
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** 30 cm
- **Price:** 8.99
- **Printed Price:** “8 99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 778, right 165, bottom 880, page 1
- **Full page:** [pages/flyer158-page1-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page1-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `b3399505368fbce4`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["8", "99"], "cell_pt": [4.2, 700.2, 116.8, 792.2], "size": "30 cm"}`

**Item Review Analysis (Pass 1):** Correct. Canadian lake whitefish at 8.99 each; the stored size "30 cm" is the fish length printed in the cell — the source's spec carried verbatim, not a package weight. Fish & Seafood > Fish is right. Brand None is valid (none printed).

### Item 15185

![item 15185](images/item-15185.jpg)

- **Name (English):** ONIONS
- **Name (French):** OGNIONS
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** 10 lbs
- **Price:** 3.99
- **Printed Price:** “3 99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 778, right 993, bottom 880, page 1
- **Full page:** [pages/flyer158-page1-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page1-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `3231e27d409c1feb`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "99"], "cell_pt": [591.8, 700.2, 704.2, 792.2], "size": "10 lbs"}`

**Item Review Analysis (Pass 1):** Correct. Onions, 10 lbs bag, 3.99 — matches the page; size stored verbatim as printed. Fresh Vegetables is right.
