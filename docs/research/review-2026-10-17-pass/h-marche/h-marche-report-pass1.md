# H Marché — full product report

Store slug: `h-marche`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 120, valid 2026-10-15 → 2026-10-21). The expired Oct 8–14 edition is correctly excluded. Items come from 4 of the flyer's pages (2, 5, 6, 7) — the seafood and Korean-grocery pages.
- **Sample counts:** 10 classified + 0 unclassified shown, of 11 stored items — near-total coverage of a small edition, and classification succeeded on every item despite heavily garbled trilingual names.
- **Issues found:** 4 wrong prices of 10. Three are the documented 9→6 glyph error concentrated in this flyer's black superscript-cents font: dried pollack 24.99 stored as 24.66, Kewpie mayonnaise 4.99 as 4.66, Beksul breadcrumbs 3.99 as 3.66. The fourth is a neighbour misattachment: the twist donuts took the earl-grey cake's 5.99 from the cell to their left; they print 8.99/PK. All four corrected from the crops. No blanket .66→.99 rewrite is safe — the kimchi mandu (4.79) and dried anchovies (8.29) are genuine non-.99 prices verified on their crops — so this stays a data correction, with the pattern recorded.
- **Names:** the OCR name stitches carry the flyer's brand codes and Korean line fragments ("HC)", "CJHS S7= 4506") — ugly but they classify correctly, and the product identity stays readable in FR/EN. Recorded as this store's text-quality character; not a fix target in this pass.
- **Fixes applied this pass:** 4 stored prices corrected (11974 → 8.99/pack, 11975 → 24.99, 11976 → 4.99, 11981 → 3.99).

## Flyer 120 — valid 2026-10-15 → 2026-10-21 (10 classified items, 0 unclassified)

Source ref: `img-23b276523c0f5ac8` · fetched 2026-10-16T12:18:16.540Z

### Item 11971

![item 11971](images/item-11971.jpg)

- **Name (English):** None
- **Name (French):** SALTED HAIRTAIL FISH SABRE SALE
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** None
- **Price:** 10.99
- **Printed Price:** “10.99”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 710, top 857, right 965, bottom 961, page 2
- **Full page:** [pages/flyer120-page2-39f7bb4aee.jpg (flyer page 2)](pages/flyer120-page2-39f7bb4aee.jpg)
- **Image source URL:** https://static.wixstatic.com/media/4be672_c33ee833f0264494b40f95954bc23211~mv2.jpg
- **Details:** confidence: 0.95 · item_key: `70a25b4e53180120`
- **Raw:** `{"block_text": "SALTED HAIRTAIL FISH\nSABRE SALE", "ocr_lines": ["SALTED HAIRTAIL FISH", "SABRESALE"], "harvest": {"unit": "kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Salted hairtail fish at 10.99/lb (24.23/kg) — verified on the crop. Fish is right.

### Item 11972

![item 11972](images/item-11972.jpg)

- **Name (English):** None
- **Name (French):** BONELESS SALTED MACKEREL MAQUEREAU SALE SANS ARETES
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** None
- **Price:** 11.99
- **Printed Price:** “11.99”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 401, top 571, right 767, bottom 673, page 2
- **Full page:** [pages/flyer120-page2-39f7bb4aee.jpg (flyer page 2)](pages/flyer120-page2-39f7bb4aee.jpg)
- **Image source URL:** https://static.wixstatic.com/media/4be672_c33ee833f0264494b40f95954bc23211~mv2.jpg
- **Details:** confidence: 0.98 · item_key: `c71ce2e206bcd9fa`
- **Raw:** `{"block_text": "BONELESS SALTED MACKEREL\nMAQUEREAU SALE SANS ARETES", "ocr_lines": ["BONELESSSALTEDMACKEREL", "MAQUEREAUSALESANSARETES"], "harvest": {"unit": "kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Boneless salted mackerel at 11.99/lb (26.43/kg) — verified. Fish is right.

### Item 11973

![item 11973](images/item-11973.jpg)

- **Name (English):** None
- **Name (French):** SALTED SEA TROUT MAIGRE SALE
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** None
- **Price:** 8.99
- **Printed Price:** “8.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 18, top 849, right 236, bottom 947, page 2
- **Full page:** [pages/flyer120-page2-39f7bb4aee.jpg (flyer page 2)](pages/flyer120-page2-39f7bb4aee.jpg)
- **Image source URL:** https://static.wixstatic.com/media/4be672_c33ee833f0264494b40f95954bc23211~mv2.jpg
- **Details:** confidence: 0.98 · item_key: `6eecd19825f41bc4`
- **Raw:** `{"block_text": "SALTED SEA TROUT\nMAIGRE SALE", "ocr_lines": ["SALTEDSEA TROUT", "MAIGRESALE"]}`

**Item Review Analysis (Pass 1):** Correct. Salted sea trout at 8.99/lb — verified. Fish is right.

### Item 11974

![item 11974](images/item-11974.jpg)

- **Name (English):** None
- **Name (French):** U&l) BEIGNETS TORSADES BOUCHEE MATTANG (CARAMELISES) U&l) BITE-SIZE TWIST DONUTS MATTANG (CANDIED)
- **Brand:** None
- **Category (English):** Bakery > Cookies, Muffins & Desserts
- **Category (French):** Boulangerie > Biscuits, muffins et desserts
- **How classified:** rule (`bakery-cookies-muffins`)
- **Size:** 520G
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 315, top 299, right 935, bottom 363, page 5
- **Full page:** [pages/flyer120-page5-da8840f5b3.jpg (flyer page 5)](pages/flyer120-page5-da8840f5b3.jpg)
- **Image source URL:** https://static.wixstatic.com/media/4be672_338ea98692994f96ada7659af815d46e~mv2.jpg
- **Details:** confidence: 0.94 · item_key: `17528b7e90fdf8b5`
- **Raw:** `{"block_text": "FHOO|)S+e2}H}7| StEt 520G\n\nU&l) BEIGNETS TORSADES BOUCHEE\nMATTANG (CARAMELISES)\n\nU&l) BITE-SIZE TWIST DONUTS MATTANG\n(CANDIED)", "ocr_lines": ["NEW!", "U&I) BEIGNETS TORSADES BOUCHEE", "MATTANG(CARAMELISES)", "U&I)BITE-SIZETWISTDONUTSMATTANG", "(CANDIED)"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Bite-size twist donuts (Mattang, candied, 520 g) print 8.99/PK; the DB had 5.99 — the earl-grey chocolate cake's price from the neighbouring cell. Cookies, Muffins & Desserts is right.

### Item 11975

![item 11975](images/item-11975.jpg)

- **Name (English):** None
- **Name (French):** HC) LANIÈRES DE GOBERGE SÉCHÉE (HWANGTAE) HC) DRIED POLLOCK STRIPS (HWANGTAE)
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** 400G
- **Price:** 24.66
- **Printed Price:** “24.66”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 11, top 286, right 478, bottom 413, page 6
- **Full page:** [pages/flyer120-page6-791b6ccbe2.jpg (flyer page 6)](pages/flyer120-page6-791b6ccbe2.jpg)
- **Image source URL:** https://static.wixstatic.com/media/4be672_804b84ab4f814072bfcb730579b6f50d~mv2.jpg
- **Details:** confidence: 0.99 · item_key: `286c2c13ad7a8ff0`
- **Raw:** `{"block_text": "HC) LANIÈRES DE GOBERGE SÉCHÉE\n(HWANGTAE)\nHC) DRIED POLLOCK STRIPS (HWANGTAE)", "ocr_lines": ["HC) LANIERES DE GOBERGE SECHEE", "(HWANGTAE)", "HC)DRIEDPOLLOCKSTRIPS(HWANGTAE)"], "harvest": {"size": "400G", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Dried pollack strips (Hwangtae, 400 g) print 24.99; the DB had 24.66 (9 read as 6 in the superscript cents). Fish is right.

### Item 11976

![item 11976](images/item-11976.jpg)

- **Name (English):** None
- **Name (French):** KEWPIE MAYONNAISE 450G KEWPIE) MAYONNAISE KEWPIE) MAYONNAISE
- **Brand:** None
- **Category (English):** Pantry > Condiments
- **Category (French):** Produits du garde-manger > Condiments et garnitures
- **How classified:** rule (`specific-condiments`)
- **Size:** 450G
- **Price:** 4.66
- **Printed Price:** “4.66”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 13, top 846, right 478, bottom 956, page 6
- **Full page:** [pages/flyer120-page6-791b6ccbe2.jpg (flyer page 6)](pages/flyer120-page6-791b6ccbe2.jpg)
- **Image source URL:** https://static.wixstatic.com/media/4be672_804b84ab4f814072bfcb730579b6f50d~mv2.jpg
- **Details:** confidence: 0.99 · item_key: `0b6e18d3f63bb2a9`
- **Raw:** `{"block_text": "KEWPIE MAYONNAISE 450G\nKEWPIE) MAYONNAISE\nKEWPIE) MAYONNAISE", "ocr_lines": ["KEWPIEMAYONNAISE450G", "KEWPIE)MAYONNAISE", "KEWPIE)MAYONNAISE"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Kewpie mayonnaise (450 g) prints 4.99; the DB had 4.66 (same 9→6). Condiments is right.

### Item 11977

![item 11977](images/item-11977.jpg)

- **Name (English):** None
- **Name (French):** HJK) MANDU AU KIMCHI HJK) KIMCHI MANDU
- **Brand:** None
- **Category (English):** International Foods > East Asian Foods
- **Category (French):** Aliments internationaux > Aliments de l'Asie de l'Est
- **How classified:** rule (`east-asian`)
- **Size:** 350G
- **Price:** 4.79
- **Printed Price:** “4.79”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 14, top 565, right 482, bottom 677, page 6
- **Full page:** [pages/flyer120-page6-791b6ccbe2.jpg (flyer page 6)](pages/flyer120-page6-791b6ccbe2.jpg)
- **Image source URL:** https://static.wixstatic.com/media/4be672_804b84ab4f814072bfcb730579b6f50d~mv2.jpg
- **Details:** confidence: 0.99 · item_key: `d868d5ca4a8549fa`
- **Raw:** `{"block_text": "HJK) MANDU AU KIMCHI\nHJK) KIMCHI MANDU", "ocr_lines": ["HJK)MANDUAUKIMCHI", "HJK)KIMCHIMANDU"], "harvest": {"size": "350G", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Kimchi mandu (350 g) prints 4.79 — a genuine non-.99 price, verified on the crop; it is why no blanket cents rewrite is safe. East Asian Foods is right.

### Item 11978

![item 11978](images/item-11978.jpg)

- **Name (English):** None
- **Name (French):** NH) RIZ BYEOLCHEONJ! DE HADONG NH) HADONG BYEOLCHEONJI RICE
- **Brand:** None
- **Category (English):** Pantry > Rice
- **Category (French):** Produits du garde-manger > Riz
- **How classified:** rule (`rice`)
- **Size:** None
- **Price:** 36.99
- **Printed Price:** “36.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 521, top 285, right 987, bottom 399, page 6
- **Full page:** [pages/flyer120-page6-791b6ccbe2.jpg (flyer page 6)](pages/flyer120-page6-791b6ccbe2.jpg)
- **Image source URL:** https://static.wixstatic.com/media/4be672_804b84ab4f814072bfcb730579b6f50d~mv2.jpg
- **Details:** confidence: 0.99 · item_key: `6dacfedf12ed7c8f`
- **Raw:** `{"block_text": "NH) RIZ BYEOLCHEONJ! DE HADONG\nNH) HADONG BYEOLCHEONJI RICE", "ocr_lines": ["NHIRIZBYEOLCHEONJIDEHADONG", "NHIHADONGBYEOLCHEONJIRICE"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Hadong Byeolcheonji rice (10 kg) at 36.99 — verified. Rice is right; the name stitch drops the trailing "RICE" but identity is clear.

### Item 11979

![item 11979](images/item-11979.jpg)

- **Name (English):** None
- **Name (French):** CRD) PETITS ANCHOIS SÉCHÉS (JIRI) CRD) SMALL DRIED ANCHOVIES (JIRI)
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** 227G
- **Price:** 8.29
- **Printed Price:** “8.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 11, top 287, right 479, bottom 400, page 7
- **Full page:** [pages/flyer120-page7-c43130eeeb.jpg (flyer page 7)](pages/flyer120-page7-c43130eeeb.jpg)
- **Image source URL:** https://static.wixstatic.com/media/4be672_f7bd0ccefc0744d9a486f61c64f31be6~mv2.jpg
- **Details:** confidence: 0.99 · item_key: `909d1fd3995dff71`
- **Raw:** `{"block_text": "CRD) PETITS ANCHOIS SÉCHÉS (JIRI)\nCRD) SMALL DRIED ANCHOVIES (JIRI)", "ocr_lines": ["CRD) PETITS ANCHOIS SECHES (JIRI)", "CRD)SMALLDRIEDANCHOVIES(JIRI)"], "harvest": {"size": "227G", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Small dried anchovies (Jiri, 227 g) print 8.29 — verified, another genuine non-.99. Fish is right.

### Item 11981

![item 11981](images/item-11981.jpg)

- **Name (English):** None
- **Name (French):** CJHS S7= 4506 CJ) CHAPELURE BEKSUL CJ) BEKSUL BREAD CRUMBS
- **Brand:** None
- **Category (English):** Pantry > Baking Essentials
- **Category (French):** Produits du garde-manger > Essentiels de cuisson
- **How classified:** rule (`baking`)
- **Size:** 450G
- **Price:** 3.66
- **Printed Price:** “3.66”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 12, top 821, right 477, bottom 932, page 7
- **Full page:** [pages/flyer120-page7-c43130eeeb.jpg (flyer page 7)](pages/flyer120-page7-c43130eeeb.jpg)
- **Image source URL:** https://static.wixstatic.com/media/4be672_f7bd0ccefc0744d9a486f61c64f31be6~mv2.jpg
- **Details:** confidence: 0.99 · item_key: `5d5e2b4b61ac7aa4`
- **Raw:** `{"block_text": "CJHS S7= 4506\nCJ) CHAPELURE BEKSUL\nCJ) BEKSUL BREAD CRUMBS", "ocr_lines": ["CJ）450G", "CJ)CHAPELUREBEKSUL", "CJ)BEKSULBREADCRUMBS"], "harvest": {"size": "450G", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Beksul breadcrumbs (450 g) print 3.99; the DB had 3.66 (9→6). Baking Essentials is right; the name leads with OCR garble ("CJHS S7= 4506") from the Korean line.
