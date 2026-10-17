# Odessa Poissonnier — full product report

Store slug: `odessa-poissonnier`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 88, valid 2026-10-08 → 2026-10-21 — a two-week wholesale catalogue; 15 items, 10 sampled).
- **Sample counts:** 10 classified + 0 unclassified shown — that classification success is misleading: two sampled items are a ponzu sauce and a potato dish classified as Fish (the flyer is a fish catalogue and the names carry no product tokens of their own).
- **Issues found:** this catalogue prints every product with a headline price plus a smaller unit rate beside it ("10,99 $/lb — 24,23 $/kg*", "15,99 $/400 g — 4,00 $/100 g"), and the pipeline took the RATE for most sampled items instead of the headline: tilapia stored at its $/kg rate, halibut likewise (72.73 for a 32.99/lb headline), pollock likewise, tiger shrimp and the salmon puff pastry stored at their $/100 g rates instead of the bag prices (26.99/908 g, 19.99/750 g), the cod fritters' 90 g pack price labelled as a 100 g rate, the oysters stored at the 100-count derived rate (1.55) instead of the printed single price (1.69), and the lobster-shrimp spring rolls stored at 0.00 outright. Eight of ten sampled items needed correction — the dual-rate trap in its purest form. All corrected to the headline prices below.
- **Fixes applied this pass:** 10968 → 10.99/lb, 10969 → 8.99/lb, 10971 → 1.69 each, 10977 → 32.99/lb, 10983 → 26.99 (bag), 10988 → 15.99, 10989 unit → each (90 g pack), 10990 → 19.99.

## Flyer 88 — valid 2026-10-08 → 2026-10-21 (10 classified items, 0 unclassified)

Source ref: `circulaire-odessa-poissonnier-du-8-au-21-octobre-2026` · fetched 2026-10-13T23:06:29.022Z

### Item 10968

![item 10968](images/item-10968.jpg)

- **Name (English):** None
- **Name (French):** FILET DE TILAPIA 7/9 7/9 TILAPIA FILLET
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** None
- **Price:** 24.23
- **Printed Price:** “24.23”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 29, top 419, right 348, bottom 520, page 2
- **Full page:** [pages/flyer88-page2-764420a29b.jpg (flyer page 2)](pages/flyer88-page2-764420a29b.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-odessa-poissonnier-du-8-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.91 · item_key: `9d131358be5435ab`
- **Conditions:** `{"alt_prices": ["10.99"]}`
- **Raw:** `{"block_text": "FILET DE TILAPIA 7/9\n7/9 TILAPIA FILLET", "ocr_lines": ["FILET DE TILAPIA 7/9", "7/9TILAPIAFILLET"], "harvest": {"unit": "kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Tilapia fillets 7/9 headline at 10.99 $/lb (reg. 14.99/lb); the DB stored the 24.23 $/kg rate beside it. Now 10.99/lb. Fish is right.

### Item 10969

![item 10969](images/item-10969.jpg)

- **Name (English):** None
- **Name (French):** FILET DE GOBERGE 6 OZ+
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** 6 OZ
- **Price:** 19.82
- **Printed Price:** “19.82”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 29, top 839, right 406, bottom 939, page 2
- **Full page:** [pages/flyer88-page2-764420a29b.jpg (flyer page 2)](pages/flyer88-page2-764420a29b.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-odessa-poissonnier-du-8-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.87 · item_key: `f696eacbe34efc92`
- **Conditions:** `{"alt_prices": ["0.99"]}`
- **Raw:** `{"block_text": "FILET DE GOBERGE 6 OZ+\n6 OZ+ POLLOCK FILLET", "ocr_lines": ["FILET DE GOBERGE 6 OZ+", "6OZ+POLLOCKFILLET"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Pollock fillets 6 oz+ headline at 8.99 $/lb (reg. 10.99/lb); the DB stored the 19.82 $/kg rate. Now 8.99/lb. Fish is right.

### Item 10971

![item 10971](images/item-10971.jpg)

- **Name (English):** None
- **Name (French):** HUÎTRE LA GRANDE ENTRÉE
- **Brand:** None
- **Category (English):** Fish & Seafood > Shellfish
- **Category (French):** Poissons et fruits de mer > Crustacés
- **How classified:** rule (`shellfish`)
- **Size:** None
- **Price:** 1.55
- **Printed Price:** “1.55”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 77, top 676, right 320, bottom 892, page 3
- **Full page:** [pages/flyer88-page3-033af84823.jpg (flyer page 3)](pages/flyer88-page3-033af84823.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-odessa-poissonnier-du-8-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.98 · item_key: `99dd9edf9f338c57`
- **Raw:** `{"block_text": "HUÎTRE LA GRANDE\nENTRÉE", "ocr_lines": ["HUITRE LA GRANDE", "ENTREE"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. La Grande Entrée oysters (Magdalen Islands) print a ladder: 1.69 $ each, 29.99 $/18, 154.99 $/100. The DB stored 1.55 — the derived per-unit rate of the 100-box. Now the printed single price, 1.69 each; the pack prices are as printed here. Shellfish is right.

### Item 10977

![item 10977](images/item-10977.jpg)

- **Name (English):** None
- **Name (French):** FILET DE FLÉTAN
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** None
- **Price:** 72.73
- **Printed Price:** “72.73”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 85, top 761, right 307, bottom 876, page 5
- **Full page:** [pages/flyer88-page5-921d0d126e.jpg (flyer page 5)](pages/flyer88-page5-921d0d126e.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-odessa-poissonnier-du-8-au-21-octobre-2026/05.webp
- **Details:** confidence: 0.83 · item_key: `8bb8fa6fdd03fc42`
- **Raw:** `{"block_text": "FILET DE FLÉTAN", "ocr_lines": ["FILET DE FLETAN"], "harvest": {"unit": "kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Quebec halibut fillets headline at 32.99 $/lb; the DB stored the 72.73 $/kg rate. Now 32.99/lb. Fish is right.

### Item 10983

![item 10983](images/item-10983.jpg)

- **Name (English):** None
- **Name (French):** CREVETTE TIGRÉE
- **Brand:** None
- **Category (English):** Fish & Seafood > Shrimp
- **Category (French):** Poissons et fruits de mer > Crevette
- **How classified:** rule (`shrimp`)
- **Size:** None
- **Price:** 2.97
- **Printed Price:** “2.97”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 79, top 704, right 320, bottom 862, page 7
- **Full page:** [pages/flyer88-page7-ec91f058eb.jpg (flyer page 7)](pages/flyer88-page7-ec91f058eb.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-odessa-poissonnier-du-8-au-21-octobre-2026/07.webp
- **Details:** confidence: 0.91 · item_key: `ebe55be304e39b3c`
- **Raw:** `{"block_text": "CREVETTE TIGRÉE", "ocr_lines": ["CREVETTE TIGREE"], "harvest": {"size": "100g", "unit": "100g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Tiger shrimp 21/25 (Sea-Ray, India) headline at 26.99 $/908 g bag; the DB stored the 2.97 $/100 g rate. Now 26.99 per bag. Shrimp is right.

### Item 10988

![item 10988](images/item-10988.jpg)

- **Name (English):** None
- **Name (French):** ROULEAUX IMPERIAUX HOMARD ET CREVETTE
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Appetizers & Snacks
- **Category (French):** Produits surgelés > Entrées et collations surgelés
- **How classified:** rule (`frozen-appetizers`)
- **Size:** None
- **Price:** 0.00
- **Printed Price:** “15998/4.00”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 131, top 764, right 395, bottom 863, page 10
- **Full page:** [pages/flyer88-page10-d139a6ba4d.jpg (flyer page 10)](pages/flyer88-page10-d139a6ba4d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-odessa-poissonnier-du-8-au-21-octobre-2026/10.webp
- **Details:** confidence: 0.74 · item_key: `41a12575e93ac635`
- **Conditions:** `{"multibuy": {"count": 15998, "total": 4.0}, "alt_prices": ["1.00"]}`
- **Raw:** `{"block_text": "ROULEAUX IMPERIAUX\nHOMARD ET CREVETTE", "ocr_lines": ["ROULEAUX IMPERIAUX", "HOMARDETCREVETTE"], "harvest": {"unit": "100g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Lobster and shrimp spring rolls (4 x 100 g) headline at 15.99 $/400 g (reg. 17.99); the DB stored 0.00. Now 15.99. Frozen Appetizers & Snacks is right.

### Item 10989

![item 10989](images/item-10989.jpg)

- **Name (English):** None
- **Name (French):** ACRAS DE MORUES
- **Brand:** None
- **Category (English):** Prepared Meals > Entrees & Appetizers
- **Category (French):** Repas préparés > Plats principaux et apéritifs
- **How classified:** rule (`entrees`)
- **Size:** 8/100g
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 151, top 328, right 369, bottom 401, page 10
- **Full page:** [pages/flyer88-page10-d139a6ba4d.jpg (flyer page 10)](pages/flyer88-page10-d139a6ba4d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-odessa-poissonnier-du-8-au-21-octobre-2026/10.webp
- **Details:** confidence: 0.79 · item_key: `1c8da932de4f621d`
- **Conditions:** `{"alt_prices": ["3.32"]}`
- **Raw:** `{"block_text": "ACRAS DE MORUES", "ocr_lines": ["ACRASDEMORUES"], "harvest": {"size": "8/100g", "unit": "100g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** UNIT CORRECTED. Cod fritters (acras de morue) print 2.99 $/90 g pack (rate 3.32 $/100 g beside it); the value was right but labelled as a 100 g rate. Now 2.99 each (90 g pack). Entrees & Appetizers is right.

### Item 10990

![item 10990](images/item-10990.jpg)

- **Name (English):** None
- **Name (French):** FEUILLETÉ SAUMON & ÉPINARD
- **Brand:** None
- **Category (English):** Fish & Seafood > Salmon
- **Category (French):** Poissons et fruits de mer > Saumon
- **How classified:** rule (`salmon`)
- **Size:** None
- **Price:** 2.67
- **Printed Price:** “2.67”
- **Unit quantity:** 100.0
- **Unit measurement:** gram
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 575, top 326, right 937, bottom 396, page 10
- **Full page:** [pages/flyer88-page10-d139a6ba4d.jpg (flyer page 10)](pages/flyer88-page10-d139a6ba4d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-odessa-poissonnier-du-8-au-21-octobre-2026/10.webp
- **Details:** confidence: 0.96 · item_key: `c72de9746b971013`
- **Raw:** `{"block_text": "FEUILLETÉ SAUMON & ÉPINARD", "ocr_lines": ["FEUILLETESAUMON&EPINARD"], "harvest": {"unit": "100g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Salmon and spinach puff pastry headlines at 19.99 $/750 g (reg. 22.99); the DB stored the 2.67 $/100 g rate. Now 19.99. Salmon is the classifier's shelf.

### Item 10993

![item 10993](images/item-10993.jpg)

- **Name (English):** None
- **Name (French):** KIKKOMAN
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** store-prior
- **Size:** None
- **Price:** 5.49
- **Printed Price:** “5.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 656, top 806, right 857, bottom 874, page 12
- **Full page:** [pages/flyer88-page12-5b7a79a3d3.jpg (flyer page 12)](pages/flyer88-page12-5b7a79a3d3.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-odessa-poissonnier-du-8-au-21-octobre-2026/12.webp
- **Details:** confidence: 0.90 · item_key: `3d68f646858be45f`
- **Raw:** `{"block_text": "KIKKOMAN", "ocr_lines": ["KIKKOMAN"]}`

**Item Review Analysis (Pass 1):** Price correct, shelf note. Kikkoman ponzu sauce (296 ml) at 5.49 — verified. It sits in Fish & Seafood because the name is the bare brand "KIKKOMAN" in a fish catalogue; the product is a sauce. Text-only result, recorded.

### Item 10994

![item 10994](images/item-10994.jpg)

- **Name (English):** None
- **Name (French):** COOL & SIMPLE
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** store-prior
- **Size:** None
- **Price:** 11.99
- **Printed Price:** “11.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-08 → 2026-10-21
- **bbox:** left 644, top 371, right 821, bottom 439, page 12
- **Full page:** [pages/flyer88-page12-5b7a79a3d3.jpg (flyer page 12)](pages/flyer88-page12-5b7a79a3d3.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-odessa-poissonnier-du-8-au-21-octobre-2026/12.webp
- **Details:** confidence: 0.92 · item_key: `efc2d105718995fa`
- **Conditions:** `{"alt_prices": ["2.50"]}`
- **Raw:** `{"block_text": "COOL & SIMPLE", "ocr_lines": ["COOL&SIMPLE"]}`

**Item Review Analysis (Pass 1):** Price correct, shelf note. Cool & Simple Dauphinoise potatoes (480 g) at 11.99 — verified. Shelved in Fish & Seafood on the bare brand name, same effect as 10993; the product is a potato side dish.
