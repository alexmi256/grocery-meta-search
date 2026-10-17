# Milano Fruiterie — full product report

Store slug: `milano-fruiterie`. Generated from `data/grocery.db`. A sampled subset of 14 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 97, valid 2026-10-08 → 2026-10-21, 15 items — a single-page, two-week circular; the whole edition is sampled at 10 + 4). Note the page itself scopes some offers "08 au 14 octobre" — week-scoped cells inside a fortnight circular; the edition window stands as published.
- **Sample counts:** 10 classified + 4 unclassified shown — that is the whole edition (15 items; one non-sampled item besides).
- **Issues found:** one wrong price, of the dual-rate family. This deli flyer prices by weight with dual rates ("X /100gr — Y kg"), and the Rocha pears — sold by the bag ("Sac 2.5 lbs", 4.99/sac) — were stored at 19.90 per 100 g: the per-kg rate line of the cheese cell to their left, paired with a 100 g unit. Corrected to 4.99 per bag. Every other sampled price verified with its unit (serrano 6.99/100 g, mortadella 2.59/100 g, pecorino 3.59/100 g, prime rib steak 65.99/kg, blade roast 24.99/kg) — the units in the DB are right throughout.
- **Fixes applied this pass:** 11115 → 4.99 per bag (unit pack).

## Flyer 97 — valid 2026-10-08 → 2026-10-21 (10 classified items, 4 unclassified)

Source ref: `img-a7ec779ec0a23df8` · fetched 2026-10-14T03:56:03.125Z

### Item 11113

![item 11113](images/item-11113.jpg)

- **Name (English):** None
- **Name (French):** JAMBON SERRANO 24 MOIS PRODUIT ESPAGNOL
- **Brand:** None
- **Category (English):** Meat > Pork & Ham
- **Category (French):** Viande > Porc et jambon
- **How classified:** rule (`pork-ham`)
- **Size:** None
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 64, top 228, right 246, bottom 369, page 1
- **Full page:** [pages/flyer97-page1-5aa76795d9.jpg (flyer page 1)](pages/flyer97-page1-5aa76795d9.jpg)
- **Image source URL:** https://milanofruiterie.ca/wp-content/uploads/2026/10/20260068-NewFlyer_Milano-Fruiterie-final.ai-15.jpg
- **Details:** confidence: 0.85 · item_key: `a97b47d5732481be`
- **Conditions:** `{"alt_prices": ["69.90"]}`
- **Raw:** `{"block_text": "JAMBON SERRANO\n24 MOIS\nPRODUIT ESPAGNOL", "ocr_lines": ["JAMBONSERRANO", "24MOIS", "PRODUITESPAGNOL"], "harvest": {"unit": "100g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Serrano ham (24 months, Spain) at 6.99/100 g (69.90/kg, reg. 8.29/100 g) — verified, unit right. Pork & Ham is right.

### Item 11115

![item 11115](images/item-11115.jpg)

- **Name (English):** None
- **Name (French):** POIRE ROCHA PORTUGAL
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 19.90
- **Printed Price:** “19.90”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 679, top 428, right 837, bottom 539, page 1
- **Full page:** [pages/flyer97-page1-5aa76795d9.jpg (flyer page 1)](pages/flyer97-page1-5aa76795d9.jpg)
- **Image source URL:** https://milanofruiterie.ca/wp-content/uploads/2026/10/20260068-NewFlyer_Milano-Fruiterie-final.ai-15.jpg
- **Details:** confidence: 0.99 · item_key: `d7c1315dc1a91282`
- **Conditions:** `{"alt_prices": ["1.99"]}`
- **Raw:** `{"block_text": "POIRE ROCHA\nPORTUGAL\n—_— .", "ocr_lines": ["POIREROCHA", "PORTUGAL"], "harvest": {"unit": "100g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the page. Rocha pears (Portugal) are sold by the bag — "Sac 2.5 lbs" at 4.99 per bag (reg. 5.99). The DB had 19.90 per 100 g: the per-kg rate of the cheese cell to the left ("1,99/100gr — 19,90 kg"), mis-paired. Now 4.99, unit pack. Fresh Fruits is right.

### Item 11116

![item 11116](images/item-11116.jpg)

- **Name (English):** None
- **Name (French):** PRINCIPE MORTADELLA PISTACHE
- **Brand:** None
- **Category (English):** Deli > Deli Meat
- **Category (French):** Charcuterie > Charcuterie
- **How classified:** rule (`deli-meat`)
- **Size:** None
- **Price:** 2.59
- **Printed Price:** “2.59”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 288, top 225, right 459, bottom 360, page 1
- **Full page:** [pages/flyer97-page1-5aa76795d9.jpg (flyer page 1)](pages/flyer97-page1-5aa76795d9.jpg)
- **Image source URL:** https://milanofruiterie.ca/wp-content/uploads/2026/10/20260068-NewFlyer_Milano-Fruiterie-final.ai-15.jpg
- **Details:** confidence: 0.90 · item_key: `8a768c7c5916119f`
- **Conditions:** `{"alt_prices": ["25.90"]}`
- **Raw:** `{"block_text": "PRINCIPE MORTADELLA\nPISTACHE", "ocr_lines": ["PRINCIPEMORTADELLA", "PISTACHE"], "harvest": {"unit": "100g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Principe mortadella with pistachio at 2.59/100 g (25.90/kg, reg. 2.89/100 g) — verified. Deli Meat is right.

### Item 11117

![item 11117](images/item-11117.jpg)

- **Name (English):** None
- **Name (French):** DAL MOLISE BOULES MOZZA RELLA
- **Brand:** None
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** 100gr
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 740, top 577, right 934, bottom 718, page 1
- **Full page:** [pages/flyer97-page1-5aa76795d9.jpg (flyer page 1)](pages/flyer97-page1-5aa76795d9.jpg)
- **Image source URL:** https://milanofruiterie.ca/wp-content/uploads/2026/10/20260068-NewFlyer_Milano-Fruiterie-final.ai-15.jpg
- **Details:** confidence: 0.88 · item_key: `30ca2609dd2c4502`
- **Raw:** `{"block_text": "DAL MOLISE\nBOULES MOZZA RELLA", "ocr_lines": ["DALMOLISE", "BOULESMOZZARELLA"], "harvest": {"size": "100gr", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Dal Molise mozzarella balls (100 g) at 2.99 each (reg. 3.59) — verified. Cheese is right.

### Item 11118

![item 11118](images/item-11118.jpg)

- **Name (English):** None
- **Name (French):** TOMATES ENTIÈRE PELÉES LA SAN MARZANO
- **Brand:** None
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`specific-canned`)
- **Size:** 796ml
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 63, top 575, right 258, bottom 719, page 1
- **Full page:** [pages/flyer97-page1-5aa76795d9.jpg (flyer page 1)](pages/flyer97-page1-5aa76795d9.jpg)
- **Image source URL:** https://milanofruiterie.ca/wp-content/uploads/2026/10/20260068-NewFlyer_Milano-Fruiterie-final.ai-15.jpg
- **Details:** confidence: 0.87 · item_key: `425fb021b75f028b`
- **Raw:** `{"block_text": "TOMATES ENTIÈRE PELÉES\nLA SAN MARZANO", "ocr_lines": ["TOMATESENTIEREPELEES", "LASANMARZANO"], "harvest": {"size": "796ml", "unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. La San Marzano whole peeled tomatoes (796 ml) at 2.99 (reg. 4.29) — verified. Canned & Pickled is right.

### Item 11120

![item 11120](images/item-11120.jpg)

- **Name (English):** None
- **Name (French):** PECORINO ROMANO PRODUIT ITALIEN
- **Brand:** None
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** None
- **Price:** 3.59
- **Printed Price:** “3.59”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 288, top 398, right 488, bottom 540, page 1
- **Full page:** [pages/flyer97-page1-5aa76795d9.jpg (flyer page 1)](pages/flyer97-page1-5aa76795d9.jpg)
- **Image source URL:** https://milanofruiterie.ca/wp-content/uploads/2026/10/20260068-NewFlyer_Milano-Fruiterie-final.ai-15.jpg
- **Details:** confidence: 0.87 · item_key: `0c5ac2890c55dfdd`
- **Conditions:** `{"alt_prices": ["35.90"]}`
- **Raw:** `{"block_text": "PECORINO ROMANO\nPRODUIT ITALIEN", "ocr_lines": ["PECORINOROMANO", "PRODUITITALIEN"], "harvest": {"unit": "100g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Pecorino Romano (Italy) at 3.59/100 g (35.90/kg, reg. 4.49/100 g) — verified. Cheese is right.

### Item 11121

![item 11121](images/item-11121.jpg)

- **Name (English):** None
- **Name (French):** RÔTI DE PALETTE
- **Brand:** None
- **Category (English):** Meat > Beef
- **Category (French):** Viande > Bœuf
- **How classified:** rule (`beef`)
- **Size:** None
- **Price:** 24.99
- **Printed Price:** “24.99”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 743, top 751, right 936, bottom 891, page 1
- **Full page:** [pages/flyer97-page1-5aa76795d9.jpg (flyer page 1)](pages/flyer97-page1-5aa76795d9.jpg)
- **Image source URL:** https://milanofruiterie.ca/wp-content/uploads/2026/10/20260068-NewFlyer_Milano-Fruiterie-final.ai-15.jpg
- **Details:** confidence: 0.90 · item_key: `5e77f8e9c49e4864`
- **Raw:** `{"block_text": "RÔTI DE PALETTE\nBOEUF ~ coms,", "ocr_lines": ["ROTIDEPALETTE", "BOEUF"], "harvest": {"unit": "kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Beef blade roast at 24.99/kg (reg. 28.99/kg) — verified, unit right. Beef is right.

### Item 11122

![item 11122](images/item-11122.jpg)

- **Name (English):** None
- **Name (French):** BROCHETTE DE LEGUMES MARINÉS
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** guard-remap (`kebabs-marinated`)
- **Size:** None
- **Price:** 1.69
- **Printed Price:** “1.69”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 288, top 751, right 482, bottom 901, page 1
- **Full page:** [pages/flyer97-page1-5aa76795d9.jpg (flyer page 1)](pages/flyer97-page1-5aa76795d9.jpg)
- **Image source URL:** https://milanofruiterie.ca/wp-content/uploads/2026/10/20260068-NewFlyer_Milano-Fruiterie-final.ai-15.jpg
- **Details:** confidence: 0.94 · item_key: `c216104557c62b13`
- **Conditions:** `{"alt_prices": ["16.90"]}`
- **Raw:** `{"block_text": "BROCHETTE DE LEGUMES\nMARINÉS", "ocr_lines": ["BROCHETTEDELEGUMES", "MARINES"], "harvest": {"unit": "100g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Marinated vegetable brochettes at 1.69/100 g (16.90/kg, reg. 1.99/100 g) — verified. Fresh Vegetables is the classifier's shelf for the jarred brochettes.

### Item 11123

![item 11123](images/item-11123.jpg)

- **Name (English):** None
- **Name (French):** RIB STEAK PRIME BOEUF
- **Brand:** None
- **Category (English):** Meat > Beef
- **Category (French):** Viande > Bœuf
- **How classified:** rule (`beef`)
- **Size:** None
- **Price:** 65.99
- **Printed Price:** “65.99”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 512, top 750, right 703, bottom 895, page 1
- **Full page:** [pages/flyer97-page1-5aa76795d9.jpg (flyer page 1)](pages/flyer97-page1-5aa76795d9.jpg)
- **Image source URL:** https://milanofruiterie.ca/wp-content/uploads/2026/10/20260068-NewFlyer_Milano-Fruiterie-final.ai-15.jpg
- **Details:** confidence: 0.97 · item_key: `6b437708f216aac4`
- **Raw:** `{"block_text": "RIB STEAK PRIME\nBOEUF", "ocr_lines": ["RIBSTEAKPRIME", "BOEUF"], "harvest": {"unit": "kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Prime rib steak at 65.99/kg (reg. 69.99/kg) — verified, unit right. Beef is right.

### Item 11124

![item 11124](images/item-11124.jpg)

- **Name (English):** None
- **Name (French):** POIREAUX
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 1.49
- **Printed Price:** “1.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 739, top 293, right 934, bottom 414, page 1
- **Full page:** [pages/flyer97-page1-5aa76795d9.jpg (flyer page 1)](pages/flyer97-page1-5aa76795d9.jpg)
- **Image source URL:** https://milanofruiterie.ca/wp-content/uploads/2026/10/20260068-NewFlyer_Milano-Fruiterie-final.ai-15.jpg
- **Details:** confidence: 0.89 · item_key: `e935d638b4fe36b6`
- **Raw:** `{"block_text": "st\nPOIREAUX", "ocr_lines": ["POIREAUX"], "harvest": {"unit": "each", "via": "crop"}}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 97 (valid 2026-10-08 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct. Leeks at 1.49 each (reg. 2.49) — verified. Fresh Vegetables is right.

### Item 11110

![item 11110](images/item-11110.jpg)

- **Name (English):** None
- **Name (French):** HUILEO'OLIVE EXTRAVIERGE EXTRAVIRGIN OLIVEOIL
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 39.99
- **Printed Price:** “39.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 364, top 646, right 487, bottom 717, page 1
- **Full page:** [pages/flyer97-page1-5aa76795d9.jpg (flyer page 1)](pages/flyer97-page1-5aa76795d9.jpg)
- **Image source URL:** https://milanofruiterie.ca/wp-content/uploads/2026/10/20260068-NewFlyer_Milano-Fruiterie-final.ai-15.jpg
- **Details:** confidence: 0.93 · item_key: `fa5c0788dbe47c9d`
- **Raw:** `{"block_text": null, "ocr_lines": ["HUILEO'OLIVE", "EXTRAVIERGE", "EXTRAVIRGIN", "OLIVEOIL"], "harvest": {"unit": "each", "via": "crop"}}`

— from flyer 97 (valid 2026-10-08 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct price. Delicia extra virgin olive oil (3 L tin) at 39.99 (reg. 49.99) — verified on the crop. Unclassified under its glued name ("HUILEO'OLIVE EXTRAVIERGE").

### Item 11111

![item 11111](images/item-11111.jpg)

- **Name (English):** None
- **Name (French):** MURCAS
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 19.99
- **Printed Price:** “19.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 590, top 660, right 710, bottom 716, page 1
- **Full page:** [pages/flyer97-page1-5aa76795d9.jpg (flyer page 1)](pages/flyer97-page1-5aa76795d9.jpg)
- **Image source URL:** https://milanofruiterie.ca/wp-content/uploads/2026/10/20260068-NewFlyer_Milano-Fruiterie-final.ai-15.jpg
- **Details:** confidence: 0.93 · item_key: `559a8790ed8df2da`
- **Raw:** `{"block_text": "MURÇAS", "ocr_lines": ["MURCAS"], "harvest": {"unit": "each", "via": "crop"}}`

— from flyer 97 (valid 2026-10-08 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct price. Murcas olive oil (500 ml, Rég. 31.49) at 19.99 — verified. Unclassified under the brand-only name.

### Item 11112

![item 11112](images/item-11112.jpg)

- **Name (English):** None
- **Name (French):** FOURCHEESERISOTTO TRUFFLERISOTTO
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 175gr
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 92, top 807, right 236, bottom 897, page 1
- **Full page:** [pages/flyer97-page1-5aa76795d9.jpg (flyer page 1)](pages/flyer97-page1-5aa76795d9.jpg)
- **Image source URL:** https://milanofruiterie.ca/wp-content/uploads/2026/10/20260068-NewFlyer_Milano-Fruiterie-final.ai-15.jpg
- **Details:** confidence: 0.95 · item_key: `cecbb106c7f79f1b`
- **Raw:** `{"block_text": null, "ocr_lines": ["FOURCHEESERISOTTO", "TRUFFLERISOTTO"], "harvest": {"size": "175gr", "unit": "each", "via": "crop"}}`

— from flyer 97 (valid 2026-10-08 → 2026-10-21)

**Item Review Analysis (Pass 1):** Correct price. Vincotto risotto (truffle or four-cheese, 175 g) at 4.99 (reg. 6.69) — verified. Unclassified under its glued name.

### Item 11119

![item 11119](images/item-11119.jpg)

- **Name (English):** None
- **Name (French):** IL ROSSINO DI MASSIMILIANO PRODUIT ITALIEN
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 66, top 401, right 264, bottom 532, page 1
- **Full page:** [pages/flyer97-page1-5aa76795d9.jpg (flyer page 1)](pages/flyer97-page1-5aa76795d9.jpg)
- **Image source URL:** https://milanofruiterie.ca/wp-content/uploads/2026/10/20260068-NewFlyer_Milano-Fruiterie-final.ai-15.jpg
- **Details:** confidence: 0.82 · item_key: `eab8cfcc2b6c4594`
- **Conditions:** `{"alt_prices": ["49.90"]}`
- **Raw:** `{"block_text": "IL ROSSINO DI MASSIMILIANO\nPRODUIT ITALIEN", "ocr_lines": ["ILROSSINODIMASSIMILIANO", "PRODUITITALIEN"], "harvest": {"unit": "100g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct price. Il Rossino di Massimiliano cheese at 4.99/100 g (49.90/kg, reg. 5.29/100 g) — verified, unit right. Unclassified under its name form.
