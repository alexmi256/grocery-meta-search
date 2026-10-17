# Marché Korea — full product report

Store slug: `marche-korea`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 135, valid 2026-10-15 → 2026-10-21, 111 items). The expired Oct 8–14 edition is correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown — classification success.
- **Source character:** this store's flyer is its WooCommerce specials feed (the Marché Andes pattern): names and prices are structured shop data (FR + Korean), and the item images are the products' own shots. Every sampled shot matches its name. Prices are the feed's sale prices — including two 0.99 specials (a wasabi tube and a walnut-vanilla spread tube) that are this shop's deep-discount style, not read errors; there is no printed badge to check them against beyond the feed itself.
- **Issues found:** none. One shelf note: the sliced rice cakes (tteok) classify to Bakery > Cakes on "gâteaux de riz" — the taxonomy has no rice-cake home and the placement is the text result, left as-is.
- **Fixes applied this pass:** none needed.

## Flyer 135 — valid 2026-10-15 → 2026-10-21 (10 classified items, 0 unclassified)

Source ref: `specials-2026-10-15` · fetched 2026-10-16T12:35:05.078Z

### Item 13574

![item 13574](images/item-13574.png)

- **Name (English):** None
- **Name (French):** Samlip Gâteau castella au miel 삼립 벌꿀 카스테라
- **Brand:** None
- **Category (English):** Bakery > Cakes
- **Category (French):** Boulangerie > Gâteaux
- **How classified:** rule (`cakes`)
- **Size:** None
- **Price:** 14.99
- **Printed Price:** “14.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/09/%EC%B9%B4%EC%8A%A4%ED%85%8C%EB%9D%BC.png?fit=500%2C500&ssl=1
- **Details:** SKU: 8801068923346 · confidence: 1.00 · item_key: `6ebd88eeed94f7aa`
- **Conditions:** `{"regular_price": 19.99}`
- **Raw:** `{"woo_id": 118797, "permalink": "https://marchekorea.com/shop/samlip-gateau-castella-au-miel-%ec%82%bc%eb%a6%bd-%eb%b2%8c%ea%bf%80-%ec%b9%b4%ec%8a%a4%ed%85%8c%eb%9d%bc/"}`

**Item Review Analysis (Pass 1):** Correct. Samlip honey castella cake at 14.99 — shot matches the product. Bakery > Cakes is right.

### Item 13575

![item 13575](images/item-13575.png)

- **Name (English):** None
- **Name (French):** Cham Biscuit au Gingembre 참 생강맛 전병 250g
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** 250g
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/09/%EC%B0%B8-%EC%83%9D%EA%B0%95%EB%A7%9B.png?fit=500%2C500&ssl=1
- **Details:** SKU: 8809571510626 · confidence: 1.00 · item_key: `acfcc857d2cf431d`
- **Conditions:** `{"regular_price": 4.49}`
- **Raw:** `{"woo_id": 118788, "permalink": "https://marchekorea.com/shop/cham-biscuit-au-gingembre-%ec%b0%b8-%ec%83%9d%ea%b0%95%eb%a7%9b-%ec%a0%84%eb%b3%91-250g/"}`

**Item Review Analysis (Pass 1):** Correct. Cham ginger biscuits (250 g) at 2.99 — shot matches. Crackers & Cookies is right.

### Item 13586

![item 13586](images/item-13586.png)

- **Name (English):** None
- **Name (French):** DONGWON Gâteaux de riz tranchés 양반 떡국떡 320G
- **Brand:** None
- **Category (English):** Bakery > Cakes
- **Category (French):** Boulangerie > Gâteaux
- **How classified:** rule (`cakes`)
- **Size:** 320G
- **Price:** 1.50
- **Printed Price:** “1.50”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/08/%EC%96%91%EB%B0%98-%EB%96%A1%EA%B5%AD%EB%96%A1.png?fit=500%2C500&ssl=1
- **Details:** SKU: 8801047627838 · confidence: 1.00 · item_key: `55632d62e62bd0ff`
- **Conditions:** `{"regular_price": 3.79}`
- **Raw:** `{"woo_id": 118511, "permalink": "https://marchekorea.com/shop/dongwon-gateaux-de-riz-tranches-%ec%96%91%eb%b0%98-%eb%96%a1%ea%b5%ad%eb%96%a1-320g/"}`

**Item Review Analysis (Pass 1):** Correct price and product. Dongwon sliced rice cakes (tteok, 320 g) at 1.50 — shot matches. Shelf note in the header (Cakes via "gâteaux de riz").

### Item 13589

![item 13589](images/item-13589.png)

- **Name (English):** None
- **Name (French):** WOOMTREE Pâte de wasabi (pour la viande) 움트리 육류 생와사비랑 120g
- **Brand:** None
- **Category (English):** International Foods > East Asian Foods
- **Category (French):** Aliments internationaux > Aliments de l'Asie de l'Est
- **How classified:** rule (`east-asian`)
- **Size:** 120g
- **Price:** 0.99
- **Printed Price:** “0.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/08/%EC%9B%80%ED%8A%B8%EB%A6%AC-%EC%9C%A1%EB%A5%98.png?fit=500%2C500&ssl=1
- **Details:** SKU: 8801558500286 · confidence: 1.00 · item_key: `c200dcec5aa2fa64`
- **Conditions:** `{"regular_price": 6.99}`
- **Raw:** `{"woo_id": 118479, "permalink": "https://marchekorea.com/shop/woomtree-pate-de-wasabi-pour-la-viande-%ec%9b%80%ed%8a%b8%eb%a6%ac-%ec%9c%a1%eb%a5%98-%ec%83%9d%ec%99%80%ec%82%ac%eb%b9%84%eb%9e%91-120g/"}`

**Item Review Analysis (Pass 1):** Correct. Woomtree fresh wasabi paste (for meat) at 0.99 — the shop's structured sale price; shot matches the tube. East Asian Foods is right.

### Item 13593

![item 13593](images/item-13593.png)

- **Name (English):** None
- **Name (French):** CJ HCD Vinaigrette épicé au Gochujang 해찬들 초고추장 300G
- **Brand:** None
- **Category (English):** Pantry > Condiments
- **Category (French):** Produits du garde-manger > Condiments et garnitures
- **How classified:** rule (`condiments`)
- **Size:** 300G
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/08/%ED%95%B4%EC%B0%AC%EB%93%A4-%EC%B4%88%EA%B3%A0%EC%B6%94-%EC%9E%A5300-g.png?fit=500%2C500&ssl=1
- **Details:** confidence: 1.00 · item_key: `012874956601df68`
- **Conditions:** `{"regular_price": 5.99}`
- **Raw:** `{"woo_id": 118004, "permalink": "https://marchekorea.com/shop/cj-hcd-vinaigrette-epice-au-gochujang-%ed%95%b4%ec%b0%ac%eb%93%a4-%ec%b4%88%ea%b3%a0%ec%b6%94%ec%9e%a5-300g/"}`

**Item Review Analysis (Pass 1):** Correct. CJ Haechandle spicy gochujang vinaigrette at 3.99 — shot matches. Condiments is right.

### Item 13604

![item 13604](images/item-13604.png)

- **Name (English):** None
- **Name (French):** HWAMI Poudre de gelée de gland 화미 도토리묵가루 400G
- **Brand:** None
- **Category (English):** Pantry > Honey, Syrups & Spreads
- **Category (French):** Produits du garde-manger > Miel, sirops et tartinades
- **How classified:** rule (`honey-spreads`)
- **Size:** 400G
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/07/148.png?fit=500%2C500&ssl=1
- **Details:** SKU: 8802867528121 · confidence: 1.00 · item_key: `ebaa80aa64d643f8`
- **Conditions:** `{"regular_price": 9.99}`
- **Raw:** `{"woo_id": 117571, "permalink": "https://marchekorea.com/shop/hwami-poudre-de-gelee-de-gland-%ed%99%94%eb%af%b8-%eb%8f%84%ed%86%a0%eb%a6%ac%eb%ac%b5%ea%b0%80%eb%a3%a8-400g/"}`

**Item Review Analysis (Pass 1):** Correct. Hwami acorn jelly powder (400 g) at 5.99 — shot matches. The classifier shelves jelly powders with Honey, Syrups & Spreads (same treatment as Esposito's).

### Item 13609

![item 13609](images/item-13609.png)

- **Name (English):** None
- **Name (French):** NISHIK Riz brun de première à grains Brown Rice 15LBS
- **Brand:** None
- **Category (English):** Pantry > Rice
- **Category (French):** Produits du garde-manger > Riz
- **How classified:** rule (`rice`)
- **Size:** 15LBS
- **Price:** 19.99
- **Printed Price:** “19.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/07/%EB%8B%88%EC%8B%9C%ED%82%A4-%EB%B8%8C%EB%9D%BC%EC%9A%B4.png?fit=500%2C500&ssl=1
- **Details:** SKU: 011152188041 · confidence: 1.00 · item_key: `2d7f32ec2540815e`
- **Conditions:** `{"regular_price": 30.99}`
- **Raw:** `{"woo_id": 117497, "permalink": "https://marchekorea.com/shop/nishik-riz-brun-de-premiere-qualite-riz-a-grains-grain-rice-15lbs/"}`

**Item Review Analysis (Pass 1):** Correct. Nishiki premium brown rice (15 lb bag in the shot) at 19.99 — the feed's price. Rice is right.

### Item 13632

![item 13632](images/item-13632.png)

- **Name (English):** None
- **Name (French):** GOMPYO Farine de blé tout usage 곰표 밀가루 1KG
- **Brand:** None
- **Category (English):** Pantry > Baking Essentials
- **Category (French):** Produits du garde-manger > Essentiels de cuisson
- **How classified:** rule (`baking`)
- **Size:** 1KG
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/05/%EA%B3%B0%ED%91%9C-%EB%B0%80%EA%B0%80%EB%A3%A8-1kg.png?fit=500%2C500&ssl=1
- **Details:** SKU: 8801176101193-801176101194 · confidence: 1.00 · item_key: `6852b01fdc67feba`
- **Conditions:** `{"regular_price": 4.99}`
- **Raw:** `{"woo_id": 117043, "permalink": "https://marchekorea.com/shop/gompyo-farine-de-ble-tout-usage-%ea%b3%b0%ed%91%9c-%eb%b0%80%ea%b0%80%eb%a3%a8-1kg/"}`

**Item Review Analysis (Pass 1):** Correct. Gompyo all-purpose wheat flour (1 kg) at 3.99 — shot matches. Baking Essentials is right.

### Item 13643

![item 13643](images/item-13643.png)

- **Name (English):** None
- **Name (French):** DAESANG Tartinade aux noix et vanille 복음자리 호두바닐라 스프레드 130g
- **Brand:** None
- **Category (English):** Pantry > Honey, Syrups & Spreads
- **Category (French):** Produits du garde-manger > Miel, sirops et tartinades
- **How classified:** rule (`honey-spreads`)
- **Size:** 130g
- **Price:** 0.99
- **Printed Price:** “0.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/04/%EB%B3%B5%EC%9D%8C%EC%9E%90%EB%A6%AC-%ED%98%B8%EB%91%90%EB%B0%94%EB%8B%90%EB%9D%BC.png?fit=500%2C500&ssl=1
- **Details:** SKU: 8805999603964 · confidence: 1.00 · item_key: `9b68ce0d5adedf57`
- **Conditions:** `{"regular_price": 4.49}`
- **Raw:** `{"woo_id": 116677, "permalink": "https://marchekorea.com/shop/daesang-tartinade-aux-noix-et-vanille-%eb%b3%b5%ec%9d%8c%ec%9e%90%eb%a6%ac-%ed%98%b8%eb%91%90%eb%b0%94%eb%8b%90%eb%9d%bc-%ec%8a%a4%ed%94%84%eb%a0%88%eb%93%9c-130g/"}`

**Item Review Analysis (Pass 1):** Correct. Daesang (Bokumjari) walnut vanilla butter spread at 0.99 — the feed's sale price; shot matches the tube. Honey, Syrups & Spreads is right.

### Item 13652

![item 13652](images/item-13652.png)

- **Name (English):** None
- **Name (French):** GOMPYO Panko 곰표 빵가루 200g
- **Brand:** None
- **Category (English):** International Foods > East Asian Foods
- **Category (French):** Aliments internationaux > Aliments de l'Asie de l'Est
- **How classified:** rule (`east-asian`)
- **Size:** 200g
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/04/%EA%B3%B0%ED%91%9C-%EB%B9%B5%EA%B0%80%EB%A3%A8.png?fit=500%2C500&ssl=1
- **Details:** SKU: 8801176679586 · confidence: 1.00 · item_key: `6fc25dd390e79869`
- **Conditions:** `{"regular_price": 3.99}`
- **Raw:** `{"woo_id": 116623, "permalink": "https://marchekorea.com/shop/gompyo-panko-%ea%b3%b0%ed%91%9c-%eb%b9%b5%ea%b0%80%eb%a3%a8-200g/"}`

**Item Review Analysis (Pass 1):** Correct. Gompyo panko bread crumbs (200 g) at 1.99 — shot matches. East Asian Foods is right.
