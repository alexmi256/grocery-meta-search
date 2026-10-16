# Akhavan — full product report

Store slug: `akhavan`. Generated from `data/grocery.db`. Every item stored for this store, with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).

## What changed in this edition of the report (2026-10-16)

- **Structured fields:** names are no longer one glued string. The PDF parser now splits each cell by typography — FR name (large bold black), brand (red), EN name (smaller bold), size (small regular) — and stores them in the separate `name_fr` / `name_en` / `brand` fields (size in the raw payload; there is no size column yet). Brand is absent for the no-brand butcher/produce items, as printed.
- **Report style:** item headers are just the item number; name/brand/category/size are separate properties; price is split into Price / Printed Price / Unit.
- **Classification fixes** (from the previous review): prunes and dried limes → Dried Fruits & Nuts (new dried-marker remap, mirroring the frozen one); tomato paste and pickled items → Pantry > Canned & Pickled; jams → Pantry > Honey, Syrups & Spreads; date vinegar → Pantry > Oils & Vinegar; lamb ribs → Meat > Lamb & Veal (lamb rule now precedes pork). The processed-form rules (canned/pickled, oils/vinegar, spreads) now sit before the generic fresh-produce rules.
- **All 8 previously unclassified items are now classified**, with rules added for the vocabulary: falafel and kashk → International Foods > Middle Eastern Foods; mahlab → Pantry > Spices & Seasonings; citronnelle/lemongrass → Fresh Vegetables; blé jaune / shelled wheat → Pantry > Dried Beans, Vegetables & Grains; cornichon écrasé → Canned & Pickled; thé kalami → Drinks > Tea & Hot Drinks; corégone/whitefish → Fish & Seafood > Fish. This edition has **0 unclassified items**, so the “Unclassified items — kept for review” section does not appear.

## Flyer 158 — valid 2026-10-14 → 2026-10-20 (36 classified items, 0 unclassified)

Source ref: `https://akhavanfood.com/wp-content/uploads/2026/10/41-26-Akhavan-8x175-1.pdf` · fetched 2026-10-16T14:33:30.517Z

### Item 15150

![item 15150](images/item-15150.jpg)

- **Name (English):** HUMMUS
- **Name (French):** HOUMOUS
- **Brand:** AKHAVAN
- **Category (English):** Deli > Antipasto, Dips & Spreads
- **Category (French):** Charcuterie > Antipasti, trempettes et tartinades
- **How classified:** rule (`dips-spreads-deli`)
- **Size:** 425 g
- **Price:** 3.99
- **Printed Price:** “3 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 245, right 165, bottom 348, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `9a411b92456e747a`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "99"], "cell_pt": [4.2, 220.8, 116.8, 312.8], "size": "425 g"}`

### Item 15151

![item 15151](images/item-15151.jpg)

- **Name (French):** FALAFEL
- **Brand:** AKHAVAN
- **Category (English):** International Foods > Middle Eastern Foods
- **Category (French):** Aliments internationaux > Aliments du Moyen-Orient
- **How classified:** rule (`middle-eastern`)
- **Size:** 200 g
- **Price:** 2.99
- **Printed Price:** “2 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 172, top 245, right 330, bottom 348, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `372bc6b62a5b7d72`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["2", "99"], "cell_pt": [121.8, 220.8, 234.2, 312.8], "size": "200 g"}`

### Item 15152

![item 15152](images/item-15152.jpg)

- **Name (English):** TAFTOON BREAD
- **Name (French):** PAIN TAFTOON
- **Brand:** AKHAVAN
- **Category (English):** Bakery > Bread
- **Category (French):** Boulangerie > Pain
- **How classified:** rule (`bread`)
- **Size:** 3 PCS
- **Price:** 1.99
- **Printed Price:** “1 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 337, top 245, right 496, bottom 348, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `abd94b410ff5cc64`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["1", "99"], "cell_pt": [239.2, 220.8, 351.8, 312.8], "size": "3 PCS"}`

### Item 15153

![item 15153](images/item-15153.jpg)

- **Name (English):** PITTED PRUNES
- **Name (French):** PRUNES DÉNOYAUTÉES
- **Brand:** AKHAVAN
- **Category (English):** Fruits & Vegetables > Dried Fruits & Nuts
- **Category (French):** Fruits et légumes > Fruits séchés et noix
- **How classified:** dried-remap (`fruits`)
- **Size:** 454 g
- **Price:** 4.49
- **Printed Price:** “4 49”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 503, top 245, right 662, bottom 348, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `fd99079218d7ef75`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["4", "49"], "cell_pt": [356.8, 220.8, 469.2, 312.8], "size": "454 g"}`

### Item 15154

![item 15154](images/item-15154.jpg)

- **Name (English):** MAHLAB POWDER
- **Name (French):** MAHLAB EN POUDRE
- **Brand:** AKHAVAN
- **Category (English):** Pantry > Spices & Seasonings
- **Category (French):** Produits du garde-manger > Épices et assaisonnements
- **How classified:** rule (`spices`)
- **Size:** 100 g
- **Price:** 3.49
- **Printed Price:** “3 49”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 669, top 245, right 828, bottom 348, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `0ed239349d9ea3e2`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "49"], "cell_pt": [474.2, 220.8, 586.8, 312.8], "size": "100 g"}`

### Item 15155

![item 15155](images/item-15155.jpg)

- **Name (English):** LEMONGRASS
- **Name (French):** CITRONNELLE
- **Brand:** AKHAVAN
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** 30 g
- **Price:** 0.99
- **Printed Price:** “99¢”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 245, right 993, bottom 348, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `3ef76d386db51e2d`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["99", "¢"], "cell_pt": [591.8, 220.8, 704.2, 312.8], "size": "30 g"}`

### Item 15156

![item 15156](images/item-15156.jpg)

- **Name (English):** ROMANO BEANS
- **Name (French):** HARICOTS ROMAINS
- **Brand:** AKHAVAN
- **Category (English):** Pantry > Dried Beans, Vegetables & Grains
- **Category (French):** Produits du garde-manger > Haricots secs, légumes et grains
- **How classified:** rule (`beans-grains`)
- **Size:** 10 lb.
- **Price:** 11.99
- **Printed Price:** “11 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 351, right 165, bottom 454, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `aacc188be4d03e2b`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["11", "99"], "cell_pt": [4.2, 316.2, 116.8, 408.2], "size": "10 lb."}`

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
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 172, top 351, right 330, bottom 454, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `0a195599e6a2512c`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["7", "99"], "cell_pt": [121.8, 316.2, 234.2, 408.2], "size": "2 lbs."}`

### Item 15158

![item 15158](images/item-15158.jpg)

- **Name (English):** YELLOW SHELLED WHEAT
- **Name (French):** BLÉ JAUNE (Durum)
- **Brand:** AKHAVAN
- **Category (English):** Pantry > Dried Beans, Vegetables & Grains
- **Category (French):** Produits du garde-manger > Haricots secs, légumes et grains
- **How classified:** rule (`beans-grains`)
- **Size:** 700 g
- **Price:** 1.99
- **Printed Price:** “1 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 337, top 351, right 496, bottom 454, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `3e5b4bd3244aaf50`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["1", "99"], "cell_pt": [239.2, 316.2, 351.8, 408.2], "size": "700 g"}`

### Item 15159

![item 15159](images/item-15159.jpg)

- **Name (English):** MIXED BEANS (Ashy)
- **Name (French):** HARICOTS MÉLANGÉS (Ashy)
- **Brand:** AKHAVAN
- **Category (English):** Pantry > Dried Beans, Vegetables & Grains
- **Category (French):** Produits du garde-manger > Haricots secs, légumes et grains
- **How classified:** rule (`beans-grains`)
- **Size:** 750 g
- **Price:** 2.49
- **Printed Price:** “2 49”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 503, top 351, right 662, bottom 454, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `4805c03a23315b06`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["2", "49"], "cell_pt": [356.8, 316.2, 469.2, 408.2], "size": "750 g"}`

### Item 15160

![item 15160](images/item-15160.jpg)

- **Name (English):** IRANIAN CURRY POWDER
- **Name (French):** POUDRE DE CARI IRANIEN
- **Brand:** AKHAVAN
- **Category (English):** Pantry > Spices & Seasonings
- **Category (French):** Produits du garde-manger > Épices et assaisonnements
- **How classified:** rule (`spices`)
- **Size:** 110 g
- **Price:** 2.99
- **Printed Price:** “2 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 669, top 351, right 828, bottom 454, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `67dd553416f3f547`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["2", "99"], "cell_pt": [474.2, 316.2, 586.8, 408.2], "size": "110 g"}`

### Item 15161

![item 15161](images/item-15161.jpg)

- **Name (English):** PRUNES HAJ HASSANI
- **Name (French):** PRUNE HAJ HASSANI
- **Brand:** AKHAVAN
- **Category (English):** Fruits & Vegetables > Dried Fruits & Nuts
- **Category (French):** Fruits et légumes > Fruits séchés et noix
- **How classified:** rule (`dried-fruits-nuts`)
- **Size:** 500 g
- **Price:** 4.99
- **Printed Price:** “4 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 351, right 993, bottom 454, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `409182617f103e05`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["4", "99"], "cell_pt": [591.8, 316.2, 704.2, 408.2], "size": "500 g"}`

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
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 458, right 165, bottom 560, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `6f7aef3056ce367a`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["16", "99"], "cell_pt": [4.2, 412.2, 116.8, 504.2], "size": "4350 g"}`

### Item 15163

![item 15163](images/item-15163.jpg)

- **Name (English):** YOGURT SODA (Doogh)
- **Name (French):** BOISSON AU YOGOURT (Doogh)
- **Brand:** LIONA
- **Category (English):** Drinks > Soft Drinks
- **Category (French):** Boissons > Boissons gazeuses
- **How classified:** rule (`soft-drinks`)
- **Size:** 1.5 L
- **Price:** 3.79
- **Printed Price:** “3 79”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 172, top 458, right 330, bottom 560, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `00d91426cd13c7a7`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "79"], "cell_pt": [121.8, 412.2, 234.2, 504.2], "size": "1.5 L"}`

### Item 15164

![item 15164](images/item-15164.jpg)

- **Name (English):** TINY CAKE WITH HAZELNUT
- **Name (French):** PETIT GÂTEAU À NOISETTE
- **Brand:** SHIRIN ASAL
- **Category (English):** Bakery > Cakes
- **Category (French):** Boulangerie > Gâteaux
- **How classified:** rule (`cakes`)
- **Size:** 24x60 g
- **Price:** 20.00
- **Printed Price:** “20 00”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 337, top 458, right 496, bottom 560, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `ff9754cb86e8b809`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["20", "00"], "cell_pt": [239.2, 412.2, 351.8, 504.2], "size": "24x60 g"}`

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
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 503, top 458, right 662, bottom 560, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `b030c0783889aa07`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["20", "00"], "cell_pt": [356.8, 412.2, 469.2, 504.2], "size": "24x60 g"}`

### Item 15166

![item 15166](images/item-15166.jpg)

- **Name (English):** VANILLA COTTON CANDY
- **Name (French):** BARBE À PAPA VANILLE
- **Brand:** UGURLU
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 240 g
- **Price:** 3.99
- **Printed Price:** “3 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 669, top 458, right 828, bottom 560, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `86769682f64a79d4`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "99"], "cell_pt": [474.2, 412.2, 586.8, 504.2], "size": "240 g"}`

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
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 458, right 993, bottom 560, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `7dacc855089db1c3`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["2", "99"], "cell_pt": [591.8, 412.2, 704.2, 504.2], "size": "14 SACHETS - 14 TEA BAGS"}`

### Item 15168

![item 15168](images/item-15168.jpg)

- **Name (French):** TAHINA
- **Brand:** CORTAS
- **Category (English):** International Foods > Middle Eastern Foods
- **Category (French):** Aliments internationaux > Aliments du Moyen-Orient
- **How classified:** rule (`middle-eastern`)
- **Size:** 454 g
- **Price:** 3.99
- **Printed Price:** “3 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 565, right 165, bottom 667, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `5381b1222a71c258`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "99"], "cell_pt": [4.2, 508.2, 116.8, 600.2], "size": "454 g"}`

### Item 15169

![item 15169](images/item-15169.jpg)

- **Name (French):** KASHK
- **Brand:** SOMAYEH
- **Category (English):** International Foods > Middle Eastern Foods
- **Category (French):** Aliments internationaux > Aliments du Moyen-Orient
- **How classified:** rule (`middle-eastern`)
- **Size:** 450 g
- **Price:** 4.99
- **Printed Price:** “4 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 172, top 565, right 330, bottom 667, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `1e909b37f6e3b6a0`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["4", "99"], "cell_pt": [121.8, 508.2, 234.2, 600.2], "size": "450 g"}`

### Item 15170

![item 15170](images/item-15170.jpg)

- **Name (English):** APRICOT JAM
- **Name (French):** CONFITURE D’ABRICOT
- **Brand:** CORTAS
- **Category (English):** Pantry > Honey, Syrups & Spreads
- **Category (French):** Produits du garde-manger > Miel, sirops et tartinades
- **How classified:** rule (`honey-spreads`)
- **Size:** 625 ml
- **Price:** 4.99
- **Printed Price:** “4 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 337, top 565, right 496, bottom 667, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `5bc6fe966bbe90ae`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["4", "99"], "cell_pt": [239.2, 508.2, 351.8, 600.2], "size": "625 ml"}`

### Item 15171

![item 15171](images/item-15171.jpg)

- **Name (English):** PICKLED PEELED GARLIC
- **Name (French):** CORNICHON À L’AIL PELÉ
- **Brand:** 1&1
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`canned-pickled`)
- **Size:** 700 g
- **Price:** 3.49
- **Printed Price:** “3 49”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 503, top 565, right 662, bottom 667, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `5bcdfd1a593d60b4`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "49"], "cell_pt": [356.8, 508.2, 469.2, 600.2], "size": "700 g"}`

### Item 15172

![item 15172](images/item-15172.jpg)

- **Name (English):** CARROT JAM
- **Name (French):** CONFITURE DE CARROT
- **Brand:** 1&1
- **Category (English):** Pantry > Honey, Syrups & Spreads
- **Category (French):** Produits du garde-manger > Miel, sirops et tartinades
- **How classified:** rule (`honey-spreads`)
- **Size:** 350 g
- **Price:** 1.99
- **Printed Price:** “1 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 669, top 565, right 828, bottom 667, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `1c2d7fe187889edd`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["1", "99"], "cell_pt": [474.2, 508.2, 586.8, 600.2], "size": "350 g"}`

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
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 565, right 993, bottom 667, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `044444feb258f184`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["1", "99"], "cell_pt": [591.8, 508.2, 704.2, 600.2], "size": "330 ml"}`

### Item 15174

![item 15174](images/item-15174.jpg)

- **Name (English):** WALNUTS
- **Name (French):** GRENOBLE NOIX
- **Brand:** AKHAVAN
- **Category (English):** Fruits & Vegetables > Dried Fruits & Nuts
- **Category (French):** Fruits et légumes > Fruits séchés et noix
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 4.49
- **Printed Price:** “4 49”
- **Unit:** lb
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 671, right 165, bottom 774, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `15e9bc1cb3907308`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["4", "49"], "cell_pt": [4.2, 604.2, 116.8, 696.2]}`

### Item 15175

![item 15175](images/item-15175.jpg)

- **Name (English):** EXTRA LONG SELLA BASMATI RICE
- **Name (French):** RIZ BASMATI SELLA À GRAINS EXTRA LONGS
- **Brand:** MEHRAN
- **Category (English):** Pantry > Rice
- **Category (French):** Produits du garde-manger > Riz
- **How classified:** rule (`rice`)
- **Size:** 2 lb
- **Price:** 2.49
- **Printed Price:** “2 49”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 172, top 671, right 330, bottom 774, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `e9b394730abb8dcf`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["2", "49"], "cell_pt": [121.8, 604.2, 234.2, 696.2], "size": "2 lb"}`

### Item 15176

![item 15176](images/item-15176.jpg)

- **Name (English):** EXTRA LONG BASMATI RICE
- **Name (French):** RIZ BASMATI À GRAINS EXTRA LONGS
- **Brand:** MEHRAN
- **Category (English):** Pantry > Rice
- **Category (French):** Produits du garde-manger > Riz
- **How classified:** rule (`rice`)
- **Size:** 2 lb
- **Price:** 2.49
- **Printed Price:** “2 49”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 337, top 671, right 496, bottom 774, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `87231a286222e908`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["2", "49"], "cell_pt": [239.2, 604.2, 351.8, 696.2], "size": "2 lb"}`

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
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 503, top 671, right 662, bottom 774, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `714a82d047c67e3d`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["1", "99"], "cell_pt": [356.8, 604.2, 469.2, 696.2], "size": "650 g"}`

### Item 15178

![item 15178](images/item-15178.jpg)

- **Name (English):** CRUSHED PICKLE
- **Name (French):** CORNICHON ÉCRASÉ
- **Brand:** MEHRAN
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`canned-pickled`)
- **Size:** 320 g
- **Price:** 1.99
- **Printed Price:** “1 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 669, top 671, right 828, bottom 774, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `92197418968dbe4b`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["1", "99"], "cell_pt": [474.2, 604.2, 586.8, 696.2], "size": "320 g"}`

### Item 15179

![item 15179](images/item-15179.jpg)

- **Name (English):** KALAMI TEA
- **Name (French):** THÉ KALAMI
- **Brand:** GULABI
- **Category (English):** Drinks > Tea & Hot Drinks
- **Category (French):** Boissons > Thés et boissons chaudes
- **How classified:** rule (`tea-hot-drinks`)
- **Size:** 500 g
- **Price:** 9.99
- **Printed Price:** “9 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 671, right 993, bottom 774, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `f13652e5eedd9788`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["9", "99"], "cell_pt": [591.8, 604.2, 704.2, 696.2], "size": "500 g"}`

### Item 15180

![item 15180](images/item-15180.jpg)

- **Name (English):** CANADIAN LAKE WHITEFISH
- **Name (French):** CORÉGONE DE LAC CANADIEN
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** 30 cm
- **Price:** 8.99
- **Printed Price:** “8 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 6, top 778, right 165, bottom 880, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `b3399505368fbce4`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["8", "99"], "cell_pt": [4.2, 700.2, 116.8, 792.2], "size": "30 cm"}`

### Item 15181

![item 15181](images/item-15181.jpg)

- **Name (English):** LAMB RIBS
- **Name (French):** CÔTES LEVÉES D’AGNEAU
- **Category (English):** Meat > Lamb & Veal
- **Category (French):** Viande > Agneau et veau
- **How classified:** rule (`lamb-veal`)
- **Price:** 8.99
- **Printed Price:** “8 99”
- **Unit:** lb
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 172, top 778, right 330, bottom 880, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `fc286508f6b8af5e`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["8", "99"], "cell_pt": [121.8, 700.2, 234.2, 792.2]}`

### Item 15182

![item 15182](images/item-15182.jpg)

- **Name (English):** KAFTA KEBAB
- **Name (French):** KOODIDEH KEBAB
- **Category (English):** Meat > Kebabs & Marinated Meat
- **Category (French):** Viande > Brochettes et viande marinée
- **How classified:** rule (`kebabs-marinated`)
- **Price:** 6.99
- **Printed Price:** “6 99”
- **Unit:** lb
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 337, top 778, right 496, bottom 880, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `b16008dd47ef206f`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["6", "99"], "cell_pt": [239.2, 700.2, 351.8, 792.2]}`

### Item 15183

![item 15183](images/item-15183.jpg)

- **Name (English):** BEETS
- **Name (French):** BETTERAVES
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Price:** 0.49
- **Printed Price:** “49¢”
- **Unit:** lb
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 503, top 778, right 662, bottom 880, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `e297a2ac9c871749`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["49", "¢"], "cell_pt": [356.8, 700.2, 469.2, 792.2]}`

### Item 15184

![item 15184](images/item-15184.jpg)

- **Name (English):** POTATOES
- **Name (French):** PATATES
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** Sac 10 lbs. /4.54 kg bag
- **Price:** 3.99
- **Printed Price:** “3 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 669, top 778, right 828, bottom 880, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `a7fceea89fc7d7b5`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "99"], "cell_pt": [474.2, 700.2, 586.8, 792.2], "size": "Sac 10 lbs. /4.54 kg bag"}`

### Item 15185

![item 15185](images/item-15185.jpg)

- **Name (English):** ONIONS
- **Name (French):** OGNIONS
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** 10 lbs
- **Price:** 3.99
- **Printed Price:** “3 99”
- **Unit:** each
- **Item validity:** 2026-10-14 → 2026-10-20
- **bbox:** left 835, top 778, right 993, bottom 880, page 1
- **Full page:** [pages/flyer158-page-168a8aa3c8.jpg (flyer page 1)](pages/flyer158-page-168a8aa3c8.jpg)
- **Image source URL:** https://akhavanfood.com/wp-content/uploads/2026/10/weekly-flyer-preview-1-scaled.jpg
- **Details:** confidence: 1.00 · item_key: `3231e27d409c1feb`
- **Raw:** `{"parser": "pdf_text", "price_parts": ["3", "99"], "cell_pt": [591.8, 700.2, 704.2, 792.2], "size": "10 lbs"}`
