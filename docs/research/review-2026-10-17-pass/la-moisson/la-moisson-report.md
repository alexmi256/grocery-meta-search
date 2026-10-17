# La Moisson Supermarché Santé — full product report

Store slug: `la-moisson`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 127, valid 2026-10-16 → 2026-11-01 — a two-week circular, current). The prior edition (Oct 1–15) is correctly excluded. Items come from 5 of the flyer's pages.
- **Sample counts:** 10 classified + 0 unclassified shown, of 23 stored items — classification success.
- **Issues found:** none. Every sampled price was verified against its crop — this store prices in x.95/x.05 endings (4,05 $, 8,05 $) and the OCR reads its green price badges cleanly. Several offers are "À partir de" group prices (seed butters, flours, the Gusta seitan line) and the stored price is the printed starting price, as the flyer states it. Name OCR is garbled on two items (the cashew dip's stitch, the seitan's symbol noise) but both still classified correctly and stay identifiable.
- **Fixes applied this pass:** none needed.


## Review Analysis — Pass 2 (2026-10-17, verification after Pass 1)

- No fixes were needed in Pass 1; the packet is unchanged and the verdicts stand (Pass 1 preserved in `la-moisson-report-pass1.md`). Store review complete — clean.

## Flyer 127 — valid 2026-10-16 → 2026-11-01 (10 classified items, 0 unclassified)

Source ref: `circulaire-la-moisson-supermarche-sante-du-16-octobre-au-1-novembre-2026` · fetched 2026-10-16T12:22:40.987Z

### Item 13279

![item 13279](images/item-13279.jpg)

- **Name (English):** None
- **Name (French):** BEURRES DE GRAINES & TAHINI
- **Brand:** None
- **Category (English):** Dairy & Eggs > Butter & Spreads
- **Category (French):** Produits laitiers et œufs > Beurre et tartinades
- **How classified:** rule (`butter`)
- **Size:** None
- **Price:** 4.05
- **Printed Price:** “4.05”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-11-01
- **bbox:** left 630, top 322, right 808, bottom 412, page 1
- **Full page:** [pages/flyer127-page1-c22d5f1f92.jpg (flyer page 1)](pages/flyer127-page1-c22d5f1f92.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-la-moisson-supermarche-sante-du-16-octobre-au-1-novembre-2026/01.webp
- **Details:** confidence: 0.89 · item_key: `509b41c1dad22411`
- **Raw:** `{"block_text": "BEURRES DE\nGRAINES & TAHINI", "ocr_lines": ["BEURRESDE", "GRAINES&TAHINI"]}`

**Item Review Analysis (Pass 1):** Correct. Nuts To You seed butters & tahini, "À partir de 4,05 $" — verified; the stored price is the printed starting price. Butter & Spreads is right (the standing tahini placement; cf. the coop note).

### Item 13282

![item 13282](images/item-13282.jpg)

- **Name (English):** None
- **Name (French):** MEXIQUE KIWI EN SAC 1LBS
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** 1LBS
- **Price:** 4.95
- **Printed Price:** “4.95”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-11-01
- **bbox:** left 163, top 380, right 439, bottom 471, page 2
- **Full page:** [pages/flyer127-page2-a4c28bd34f.jpg (flyer page 2)](pages/flyer127-page2-a4c28bd34f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-la-moisson-supermarche-sante-du-16-octobre-au-1-novembre-2026/02.webp
- **Details:** confidence: 0.91 · item_key: `02e7b1fce6ad9abd`
- **Raw:** `{"block_text": "MEXIQUE\nKIWI EN SAC 1LBS", "ocr_lines": ["MEXIQUE", "KIWIENSAC1LBS"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Kiwi bag 1 lb (Mexico) at 4.95/unit — verified. Fresh Fruits is right.

### Item 13284

![item 13284](images/item-13284.jpg)

- **Name (English):** None
- **Name (French):** QUÉBEC CORIANDRE BIO
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Herbs
- **Category (French):** Fruits et légumes > Fines herbes
- **How classified:** rule (`herbs-fresh`)
- **Size:** None
- **Price:** 1.95
- **Printed Price:** “1.95”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-11-01
- **bbox:** left 188, top 698, right 464, bottom 793, page 2
- **Full page:** [pages/flyer127-page2-a4c28bd34f.jpg (flyer page 2)](pages/flyer127-page2-a4c28bd34f.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-la-moisson-supermarche-sante-du-16-octobre-au-1-novembre-2026/02.webp
- **Details:** confidence: 0.92 · item_key: `b6aeb3c5be0a01f0`
- **Raw:** `{"block_text": "QUÉBEC\nCORIANDRE BIO", "ocr_lines": ["QUEBEC", "CORIANDREBIO"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Organic coriander (Quebec) at 1.95/unit — verified. Herbs is right.

### Item 13286

![item 13286](images/item-13286.jpg)

- **Name (English):** None
- **Name (French):** LANIERES VEGETALES, == SEITAN EFFILOCHE #—. &THONVEGE
- **Brand:** None
- **Category (English):** Meat > Plant-Based Meat Alternatives
- **Category (French):** Viande > Substituts de viande à base de plantes
- **How classified:** rule (`plant-based-meat`)
- **Size:** 14g
- **Price:** 4.95
- **Printed Price:** “4.95”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-11-01
- **bbox:** left 267, top 371, right 544, bottom 494, page 3
- **Full page:** [pages/flyer127-page3-90a496fdf2.jpg (flyer page 3)](pages/flyer127-page3-90a496fdf2.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-la-moisson-supermarche-sante-du-16-octobre-au-1-novembre-2026/03.webp
- **Details:** confidence: 0.95 · item_key: `cb9a4f2954d77ce0`
- **Raw:** `{"block_text": "DUR ‘°°. Pe\nLANIERES VEGETALES,\n== SEITAN EFFILOCHE\n#—. &THONVEGE", "ocr_lines": ["OFPROTEIN", "LANIERESVEGETALES,", "DEPROTEINES", "SEITAN EFFILOCHE", "&THON VEGE"], "harvest": {"size": "14g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Gusta plant-based strips / shredded seitan / vegan tuna, "À partir de 4,95 $" — verified. Plant-Based Meat Alternatives is right; the stored name carries symbol garble from the layout but identifies the product.

### Item 13288

![item 13288](images/item-13288.jpg)

- **Name (English):** None
- **Name (French):** SOUPES FRAÎCHES
- **Brand:** None
- **Category (English):** Prepared Meals > Salads & Soups
- **Category (French):** Repas préparés > Salades et soupes
- **How classified:** rule (`salads-soups`)
- **Size:** None
- **Price:** 4.95
- **Printed Price:** “4.95”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-11-01
- **bbox:** left 172, top 610, right 268, bottom 710, page 3
- **Full page:** [pages/flyer127-page3-90a496fdf2.jpg (flyer page 3)](pages/flyer127-page3-90a496fdf2.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-la-moisson-supermarche-sante-du-16-octobre-au-1-novembre-2026/03.webp
- **Details:** confidence: 0.93 · item_key: `122c6109fb8434dd`
- **Raw:** `{"block_text": "SOUPES\nFRAÎCHES", "ocr_lines": ["SOUPES", "FRAICHES"]}`

**Item Review Analysis (Pass 1):** Correct. DimmidiSì fresh soups at 4.95 — verified. Salads & Soups is right.

### Item 13290

![item 13290](images/item-13290.jpg)

- **Name (English):** None
- **Name (French):** : ASHEW DIP TREMPCTIE MRÉMEUSE AUX CAJOU >
- **Brand:** None
- **Category (English):** Deli > Antipasto, Dips & Spreads
- **Category (French):** Charcuterie > Antipasti, trempettes et tartinades
- **How classified:** rule (`dips-spreads-deli`)
- **Size:** None
- **Price:** 8.05
- **Printed Price:** “8.05”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-11-01
- **bbox:** left 624, top 302, right 942, bottom 347, page 3
- **Full page:** [pages/flyer127-page3-90a496fdf2.jpg (flyer page 3)](pages/flyer127-page3-90a496fdf2.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-la-moisson-supermarche-sante-du-16-octobre-au-1-novembre-2026/03.webp
- **Details:** confidence: 0.90 · item_key: `1a78966c6629a7b6`
- **Raw:** `{"block_text": "EE\n: ASHEW DIP\nTREMPCTIE MRÉMEUSE AUX CAJOU >\n\\ A Det Gralon pe Probe Rite", "ocr_lines": ["CREAMYCASHEW DIP", "TREMPETTECREMEUSEAUXCAJOUS"]}`

**Item Review Analysis (Pass 1):** Correct. Creamy cashew dip (roasted red pepper) "À partir de 8,05 $" — verified on the crop; the name stitch garbles "trempette crémeuse" but the dip classified correctly to Antipasto, Dips & Spreads.

### Item 13294

![item 13294](images/item-13294.jpg)

- **Name (English):** None
- **Name (French):** FARINES 1 KG & MELANGES A PATISSERIE
- **Brand:** None
- **Category (English):** Pantry > Baking Essentials
- **Category (French):** Produits du garde-manger > Essentiels de cuisson
- **How classified:** rule (`baking`)
- **Size:** 1 KG
- **Price:** 3.25
- **Printed Price:** “3.25”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-11-01
- **bbox:** left 656, top 636, right 928, bottom 688, page 5
- **Full page:** [pages/flyer127-page5-0a0732eaca.jpg (flyer page 5)](pages/flyer127-page5-0a0732eaca.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-la-moisson-supermarche-sante-du-16-octobre-au-1-novembre-2026/05.webp
- **Details:** confidence: 0.90 · item_key: `c626d3b1a088da0d`
- **Raw:** `{"block_text": "FARINES 1 KG &\nMELANGES A\nPATISSERIE", "ocr_lines": ["FARINES1KG&", "MELANGES A", "PATISSERIE"]}`

**Item Review Analysis (Pass 1):** Correct. Moulin Abénakis flours 1 kg & pastry mixes, "À partir de 3,25 $" — verified. Baking Essentials is right.

### Item 13295

![item 13295](images/item-13295.jpg)

- **Name (English):** None
- **Name (French):** RIZ & GALETTES DE RIZ BRUN
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** None
- **Price:** 5.15
- **Printed Price:** “5.15”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-11-01
- **bbox:** left 668, top 480, right 943, bottom 512, page 5
- **Full page:** [pages/flyer127-page5-0a0732eaca.jpg (flyer page 5)](pages/flyer127-page5-0a0732eaca.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-la-moisson-supermarche-sante-du-16-octobre-au-1-novembre-2026/05.webp
- **Details:** confidence: 0.89 · item_key: `7e526b497b4bfdfb`
- **Raw:** `{"block_text": "RIZ & GALETTES\nDE RIZ BRUN", "ocr_lines": ["RIZ&GALETTES", "DERIZBRUN"]}`

**Item Review Analysis (Pass 1):** Correct. Lundberg brown rice & rice cakes, "À partir de 5,15 $" — verified. Crackers & Cookies covers the rice cakes; the group also spans rice, recorded as the flyer's own grouping.

### Item 13297

![item 13297](images/item-13297.jpg)

- **Name (English):** None
- **Name (French):** FARINE FLOUR _ BIOLOGIQUE + ORGANIC TOUT USAGE NON BLANCHIE
- **Brand:** None
- **Category (English):** Pantry > Baking Essentials
- **Category (French):** Produits du garde-manger > Essentiels de cuisson
- **How classified:** rule (`baking`)
- **Size:** 1kg
- **Price:** 2.85
- **Printed Price:** “2.85”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-11-01
- **bbox:** left 443, top 866, right 733, bottom 941, page 5
- **Full page:** [pages/flyer127-page5-0a0732eaca.jpg (flyer page 5)](pages/flyer127-page5-0a0732eaca.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-la-moisson-supermarche-sante-du-16-octobre-au-1-novembre-2026/05.webp
- **Details:** confidence: 0.90 · item_key: `54649e52b53b020c`
- **Raw:** `{"block_text": "FARINE\nFLOUR _\nBIOLOGIQUE + ORGANIC\nTOUT USAGE\nNON BLANCHIE\nALL PURPOSE\nUNBLEACHED", "ocr_lines": ["FARINE", "FLOUR", "BIOLOGIQUE·ORGANIC", "TOUTUSAGE", "NON BLANCHIE", "ALLPURPOSE"], "harvest": {"size": "1kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Abénakis organic all-purpose flour (1 kg), "À partir de 2,85 $" — verified. Baking Essentials is right.

### Item 13300

![item 13300](images/item-13300.jpg)

- **Name (English):** None
- **Name (French):** CHOCOLAT SANS SUCRES AJOUTES
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** None
- **Price:** 2.65
- **Printed Price:** “2.65”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-11-01
- **bbox:** left 326, top 335, right 496, bottom 438, page 6
- **Full page:** [pages/flyer127-page6-940676ba58.jpg (flyer page 6)](pages/flyer127-page6-940676ba58.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-la-moisson-supermarche-sante-du-16-octobre-au-1-novembre-2026/06.webp
- **Details:** confidence: 0.93 · item_key: `8ac72315adbfb2c2`
- **Raw:** `{"block_text": "CHOCOLAT SANS\nSUCRES AJOUTES", "ocr_lines": ["CHOCOLATSANS", "SUCRES AJOUTES"]}`

**Item Review Analysis (Pass 1):** Correct. Mode chocolat no-added-sugar chocolate at 2.65 — verified. Candy & Chocolate is right.
