# Akhavan — full product report

Store slug: `akhavan`. Generated from `data/grocery.db`. Every item stored for this store, with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).

## How this edition was parsed (2026-10-16)

Akhavan no longer comes from circulaires.club page images + OCR (the source of the merged items in the previous report: 19 items, most of them several products glued together). It now comes from the store's **official PDF** (akhavanfood.com/weekly-flyer), whose text is selectable: a dedicated parser reads the PDF text layer, anchors on the big display prices, recovers the printed cell grid from the red border lines, and assembles each cell's name from the text inside it. No OCR is involved.

Result for the current edition (Oct 14–20): **36 products — the flyer's full grid — each a single product with its exact printed name and price.** All 36 crops were visually checked against the flyer: 36/36 show exactly their own product. 8 items the classifier could not categorize are listed at the end under “Unclassified items — kept for review” (falafel, mahlab, citronnelle, blé jaune, kashk, cornichon écrasé, thé kalami, corégone) — those are classifier vocabulary gaps, not parsing errors.

The previous OCR-parsed edition (Oct 7–13, 19 merged items) is still in the database for reference but is not shown in this report (--latest-only).

## Flyer 158 — valid 2026-10-14 → 2026-10-20 (28 classified items, 8 unclassified)

Source ref: `https://akhavanfood.com/wp-content/uploads/2026/10/41-26-Akhavan-8x175-1.pdf` · fetched 2026-10-16T13:43:05.104Z

### Item 15150 — HOUMOUS AKHAVAN | HUMMUS | 425 g

![item 15150](images/item-15150.jpg)

- **Category:** Deli > Antipasto, Dips & Spreads (FR: Charcuterie > Antipasti, trempettes et tartinades)
- **How classified:** rule (`dips-spreads-deli`)
- **Price:** 3.99 $ · as printed: “3 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 245, right 165, bottom 348, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `bbd9df5e3b3c6bbe`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "99"], "cell_pt": [4.2, 220.8, 116.8, 312.8]}`

### Item 15152 — PAIN TAFTOON AKHAVAN | TAFTOON BREAD | 3 PCS

![item 15152](images/item-15152.jpg)

- **Category:** Bakery > Bread (FR: Boulangerie > Pain)
- **How classified:** rule (`bread`)
- **Price:** 1.99 $ · as printed: “1 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 337, top 245, right 496, bottom 348, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `c54565f4c21b37b4`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["1", "99"], "cell_pt": [239.2, 220.8, 351.8, 312.8]}`

### Item 15153 — PRUNES DÉNOYAUTÉES | AKHAVAN | PITTED PRUNES | 454 g

![item 15153](images/item-15153.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 4.49 $ · as printed: “4 49” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 503, top 245, right 662, bottom 348, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `b993bbe6e4b6a19e`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["4", "49"], "cell_pt": [356.8, 220.8, 469.2, 312.8]}`

### Item 15156 — HARICOTS ROMAINS | AKHAVAN | ROMANO BEANS | 10 lb.

![item 15156](images/item-15156.jpg)

- **Category:** Pantry > Dried Beans, Vegetables & Grains (FR: Produits du garde-manger > Haricots secs, légumes et grains)
- **How classified:** rule (`beans-grains`)
- **Price:** 11.99 $ · as printed: “11 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 351, right 165, bottom 454, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `da5c6b06046d3630`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["11", "99"], "cell_pt": [4.2, 316.2, 116.8, 408.2]}`

### Item 15157 — LIMETTES SÉCHÉES | BLANCHES AKHAVAN | DRIED WHITE LIME | 2 lbs.

![item 15157](images/item-15157.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 7.99 $ · as printed: “7 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 172, top 351, right 330, bottom 454, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `6bead7671d0406f2`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["7", "99"], "cell_pt": [121.8, 316.2, 234.2, 408.2]}`

### Item 15159 — HARICOTS MÉLANGÉS | (Ashy) AKHAVAN | MIXED BEANS (Ashy) | 750 g

![item 15159](images/item-15159.jpg)

- **Category:** Pantry > Dried Beans, Vegetables & Grains (FR: Produits du garde-manger > Haricots secs, légumes et grains)
- **How classified:** rule (`beans-grains`)
- **Price:** 2.49 $ · as printed: “2 49” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 503, top 351, right 662, bottom 454, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `97ce282926f768fb`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["2", "49"], "cell_pt": [356.8, 316.2, 469.2, 408.2]}`

### Item 15160 — POUDRE DE CARI | IRANIEN AKHAVAN | IRANIAN CURRY POWDER | 110 g

![item 15160](images/item-15160.jpg)

- **Category:** Pantry > Spices & Seasonings (FR: Produits du garde-manger > Épices et assaisonnements)
- **How classified:** rule (`spices`)
- **Price:** 2.99 $ · as printed: “2 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 669, top 351, right 828, bottom 454, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `d5fa1319a65cbb6b`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["2", "99"], "cell_pt": [474.2, 316.2, 586.8, 408.2]}`

### Item 15161 — PRUNE HAJ HASSANI | AKHAVAN | PRUNES HAJ HASSANI | 500 g

![item 15161](images/item-15161.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 4.99 $ · as printed: “4 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 351, right 993, bottom 454, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `884eb1bab83b04d8`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["4", "99"], "cell_pt": [591.8, 316.2, 704.2, 408.2]}`

### Item 15162 — CONCENTRÉ DE | TOMATE | ÖNCÜ | TOMATO PASTE | 4350 g

![item 15162](images/item-15162.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 16.99 $ · as printed: “16 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 458, right 165, bottom 560, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `9c82613bb3ff40c6`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["16", "99"], "cell_pt": [4.2, 412.2, 116.8, 504.2]}`

### Item 15163 — BOISSON AU YOGOURT | (Doogh) | LIONA | YOGURT SODA (Doogh) | 1.5 L

![item 15163](images/item-15163.jpg)

- **Category:** Drinks > Soft Drinks (FR: Boissons > Boissons gazeuses)
- **How classified:** rule (`soft-drinks`)
- **Price:** 3.79 $ · as printed: “3 79” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 172, top 458, right 330, bottom 560, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `af56e58dee7e5815`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "79"], "cell_pt": [121.8, 412.2, 234.2, 504.2]}`

### Item 15164 — PETIT GÂTEAU À | NOISETTE | SHIRIN ASAL | TINY CAKE WITH HAZELNUT | 24x60 g

![item 15164](images/item-15164.jpg)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 20.00 $ · as printed: “20 00” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 337, top 458, right 496, bottom 560, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `5a8efa815224f36f`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["20", "00"], "cell_pt": [239.2, 412.2, 351.8, 504.2]}`

### Item 15165 — GÂTEAU TI-TAP | SALEMIN | TI-TAP CAKE | 24x60 g

![item 15165](images/item-15165.jpg)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 20.00 $ · as printed: “20 00” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 503, top 458, right 662, bottom 560, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `a0e6bdebdbf17f1f`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["20", "00"], "cell_pt": [356.8, 412.2, 469.2, 504.2]}`

### Item 15166 — BARBE À PAPA VANILLE | UGURLU | VANILLA COTTON CANDY | 240 g

![item 15166](images/item-15166.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 3.99 $ · as printed: “3 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 669, top 458, right 828, bottom 560, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `46a13c309be975db`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "99"], "cell_pt": [474.2, 412.2, 586.8, 504.2]}`

### Item 15167 — THÉ HERBAL À LA | BORAGE MEHRE GIAH | MIX HERBAL TEA (Mint Mix) | 14 SACHETS - 14 TEA BAGS

![item 15167](images/item-15167.jpg)

- **Category:** Drinks > Tea & Hot Drinks (FR: Boissons > Thés et boissons chaudes)
- **How classified:** rule (`tea-hot-drinks`)
- **Price:** 2.99 $ · as printed: “2 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 458, right 993, bottom 560, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `1225b2286821a6fe`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["2", "99"], "cell_pt": [591.8, 412.2, 704.2, 504.2]}`

### Item 15168 — TAHINA CORTAS | TAHINA | 454 g

![item 15168](images/item-15168.jpg)

- **Category:** International Foods > Middle Eastern Foods (FR: Aliments internationaux > Aliments du Moyen-Orient)
- **How classified:** rule (`middle-eastern`)
- **Price:** 3.99 $ · as printed: “3 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 565, right 165, bottom 667, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `4666ad52d966c3b6`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "99"], "cell_pt": [4.2, 508.2, 116.8, 600.2]}`

### Item 15170 — CONFITURE D’ABRICOT | CORTAS | APRICOT JAM | 625 ml

![item 15170](images/item-15170.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 4.99 $ · as printed: “4 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 337, top 565, right 496, bottom 667, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `1f843dbcac5f5545`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["4", "99"], "cell_pt": [239.2, 508.2, 351.8, 600.2]}`

### Item 15171 — CORNICHON À | L’AIL PELÉ 1&1 | PICKLED PEELED GARLIC | 700 g

![item 15171](images/item-15171.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 3.49 $ · as printed: “3 49” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 503, top 565, right 662, bottom 667, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `62efa66bd50432ae`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "49"], "cell_pt": [356.8, 508.2, 469.2, 600.2]}`

### Item 15172 — CONFITURE DE CARROT | 1&1 | CARROT JAM | 350 g

![item 15172](images/item-15172.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.99 $ · as printed: “1 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 669, top 565, right 828, bottom 667, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `cbdcce353279f439`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["1", "99"], "cell_pt": [474.2, 508.2, 586.8, 600.2]}`

### Item 15173 — VINAIGRE DE DATTES | 1&1 | DATE VINEGAR | 330 ml

![item 15173](images/item-15173.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 1.99 $ · as printed: “1 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 565, right 993, bottom 667, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `028c1a7b0bd4d9d0`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["1", "99"], "cell_pt": [591.8, 508.2, 704.2, 600.2]}`

### Item 15174 — GRENOBLE NOIX | AKHAVAN | WALNUTS | $9.88 kg | lb.

![item 15174](images/item-15174.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 4.49 $ · as printed: “4 49” · unit: lb
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 671, right 165, bottom 774, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `88b2f51438d03af1`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["4", "49"], "cell_pt": [4.2, 604.2, 116.8, 696.2]}`

### Item 15175 — RIZ BASMATI SELLA À | GRAINS EXTRA LONGS | MEHRAN | EXTRA LONG SELLA | BASMATI RICE | 2 lb

![item 15175](images/item-15175.jpg)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 2.49 $ · as printed: “2 49” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 172, top 671, right 330, bottom 774, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `25edeba9f3aff4c5`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["2", "49"], "cell_pt": [121.8, 604.2, 234.2, 696.2]}`

### Item 15176 — RIZ BASMATI À GRAINS | EXTRA LONGS MEHRAN | EXTRA LONG BASMATI RICE | 2 lb

![item 15176](images/item-15176.jpg)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 2.49 $ · as printed: “2 49” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 337, top 671, right 496, bottom 774, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `9236a23f49e6356e`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["2", "49"], "cell_pt": [239.2, 604.2, 351.8, 696.2]}`

### Item 15177 — DATES MAZAFATI | EMTIAZ | MAZAFATI DATE ORGANIC | 650 g

![item 15177](images/item-15177.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 1.99 $ · as printed: “1 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 503, top 671, right 662, bottom 774, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `bd334213c73534eb`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["1", "99"], "cell_pt": [356.8, 604.2, 469.2, 696.2]}`

### Item 15181 — CÔTES LEVÉES | D’AGNEAU | LAMB RIBS | $19.78 kg | lb. | HALAL

![item 15181](images/item-15181.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 8.99 $ · as printed: “8 99” · unit: lb
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 172, top 778, right 330, bottom 880, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `244567d72cf2f143`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["8", "99"], "cell_pt": [121.8, 700.2, 234.2, 792.2]}`

### Item 15182 — KOODIDEH KEBAB | KAFTA KEBAB | $15.38 kg | lb. | HALAL

![item 15182](images/item-15182.jpg)

- **Category:** Meat > Kebabs & Marinated Meat (FR: Viande > Brochettes et viande marinée)
- **How classified:** rule (`kebabs-marinated`)
- **Price:** 6.99 $ · as printed: “6 99” · unit: lb
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 337, top 778, right 496, bottom 880, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `28a37ea617e0b3db`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["6", "99"], "cell_pt": [239.2, 700.2, 351.8, 792.2]}`

### Item 15183 — BETTERAVES | BEETS | lb.

![item 15183](images/item-15183.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 0.49 $ · as printed: “49¢” · unit: lb
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 503, top 778, right 662, bottom 880, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `bcc5f0d150e5393c`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["49", "¢"], "cell_pt": [356.8, 700.2, 469.2, 792.2]}`

### Item 15184 — PATATES | POTATOES | Sac 10 lbs. /4.54 kg bag

![item 15184](images/item-15184.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 3.99 $ · as printed: “3 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 669, top 778, right 828, bottom 880, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `0b283f33ef201bc3`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "99"], "cell_pt": [474.2, 700.2, 586.8, 792.2]}`

### Item 15185 — OGNIONS | ONIONS | 10 lbs

![item 15185](images/item-15185.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 3.99 $ · as printed: “3 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 778, right 993, bottom 880, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `d9d5f4611e969d16`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "99"], "cell_pt": [591.8, 700.2, 704.2, 792.2]}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 158 (valid 2026-10-14 → 2026-10-20)

### Item 15151 — FALAFEL AKHAVAN | FALAFEL | 200 g

![item 15151](images/item-15151.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.99 $ · as printed: “2 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 172, top 245, right 330, bottom 348, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `49bf2b4eeefc458d`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["2", "99"], "cell_pt": [121.8, 220.8, 234.2, 312.8]}`

— from flyer 158 (valid 2026-10-14 → 2026-10-20)

### Item 15154 — MAHLAB EN POUDRE | AKHAVAN | MAHLAB POWDER | 100 g

![item 15154](images/item-15154.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.49 $ · as printed: “3 49” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 669, top 245, right 828, bottom 348, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `b51978a1215dab32`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "49"], "cell_pt": [474.2, 220.8, 586.8, 312.8]}`

— from flyer 158 (valid 2026-10-14 → 2026-10-20)

### Item 15155 — CITRONNELLE | AKHAVAN | LEMONGRASS | 30 g

![item 15155](images/item-15155.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 0.99 $ · as printed: “99¢” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 245, right 993, bottom 348, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `38eaa1e8e79f43ba`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["99", "¢"], "cell_pt": [591.8, 220.8, 704.2, 312.8]}`

— from flyer 158 (valid 2026-10-14 → 2026-10-20)

### Item 15158 — BLÉ JAUNE (Durum) | AKHAVAN | YELLOW SHELLED WHEAT | 700 g

![item 15158](images/item-15158.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.99 $ · as printed: “1 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 337, top 351, right 496, bottom 454, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `03c0ad5cb4d3daed`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["1", "99"], "cell_pt": [239.2, 316.2, 351.8, 408.2]}`

— from flyer 158 (valid 2026-10-14 → 2026-10-20)

### Item 15169 — KASHK | SOMAYEH | KASHK | 450 g

![item 15169](images/item-15169.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 4.99 $ · as printed: “4 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 172, top 565, right 330, bottom 667, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `cd9c93608c53bf5b`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["4", "99"], "cell_pt": [121.8, 508.2, 234.2, 600.2]}`

— from flyer 158 (valid 2026-10-14 → 2026-10-20)

### Item 15178 — CORNICHON ÉCRASÉ | MEHRAN | CRUSHED PICKLE | 320 g

![item 15178](images/item-15178.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.99 $ · as printed: “1 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 669, top 671, right 828, bottom 774, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `04d35c874a156b2e`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["1", "99"], "cell_pt": [474.2, 604.2, 586.8, 696.2]}`

— from flyer 158 (valid 2026-10-14 → 2026-10-20)

### Item 15179 — THÉ KALAMI | GULABI | KALAMI TEA | 500 g

![item 15179](images/item-15179.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 9.99 $ · as printed: “9 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 671, right 993, bottom 774, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `aacbe2a7a295f444`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["9", "99"], "cell_pt": [591.8, 604.2, 704.2, 696.2]}`

— from flyer 158 (valid 2026-10-14 → 2026-10-20)

### Item 15180 — CORÉGONE DE LAC | CANADIEN | CANADIAN LAKE WHITEFISH | 30 cm

![item 15180](images/item-15180.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 8.99 $ · as printed: “8 99” · unit: each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 778, right 165, bottom 880, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `68d6c9a94b446949`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["8", "99"], "cell_pt": [4.2, 700.2, 116.8, 792.2]}`
