# Marché Fu Tai — full product report

Store slug: `marche-fu-tai`. Generated from `data/grocery.db`. A sampled subset of 20 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 167, valid 2026-10-16 → 2026-10-22, 56 items across 5 pages). The expired Oct 9–15 edition is correctly excluded.
- **Sample counts:** 10 classified + 10 unclassified shown. Unclassified here are mostly glued FR/EN/Chinese name stitches; their prices are largely right.
- **Issues found:** (1) A junk item: the page footer's VISA payment logo had formed an item carrying the persimmons' 2.58/lb — purged, and payment marks (visa/mastercard/interac) are now flyer furniture in the exclusion layer (tests green). (2) Five wrong prices, all corrected from crops/pages: the jasmine rice carried the shiitake's 7.98 (its own: 15.88 for 15 lb), the three-spot crab carried the frozen yam's 2.88 (its own: 8.88), the udon noodles read 3.08 for a printed 3.88 (8→0), the sand goby stored 58.62 for a printed 5.98, and the raw shrimp bag (2 lb) stored 1.19 for a printed 11.98. Two sampled items from the first draw (udon, shrimp) were corrected in the data but fell out of the redrawn sample; the footer item is gone from it.
- **Fixes applied this pass:** exclusion furniture for payment marks (committed); 15730 purged; 15710 → 8.88, 15717 → 15.88, 15749 → 3.88, 15754 → 5.98, 15764 → 11.98.

## Flyer 167 — valid 2026-10-16 → 2026-10-22 (10 classified items, 10 unclassified)

Source ref: `circulaire-marche-fu-tai-du-16-au-22-octobre-2026` · fetched 2026-10-17T06:23:51.418Z

### Item 15717

![item 15717](images/item-15717.jpg)

- **Name (English):** None
- **Name (French):** a —RIZAAU JASMINE RICE JAS MIN
- **Brand:** None
- **Category (English):** Pantry > Rice
- **Category (French):** Produits du garde-manger > Riz
- **How classified:** rule (`rice`)
- **Size:** None
- **Price:** 15.88
- **Printed Price:** “15.88”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 440, top 426, right 647, bottom 520, page 1
- **Full page:** [pages/flyer167-page1-ff5737d9fa.jpg (flyer page 1)](pages/flyer167-page1-ff5737d9fa.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `84af4be7a0f6e112`
- **Raw:** `{"block_text": "a —RIZAAU\nJASMINE RICE JAS MIN", "ocr_lines": ["RIZAU", "THAI", "JASMINERICEJ", "JASMIN"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Thai jasmine rice (15 lb) prints 15.88; the DB had 7.98 — the dried shiitake's price from the cell at the left. Rice is right.

### Item 15721

![item 15721](images/item-15721.jpg)

- **Name (English):** None
- **Name (French):** PANIER DE PE CONCOMBRES/
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 1.49
- **Printed Price:** “2/2.98”
- **Unit quantity:** 2.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 683, top 419, right 987, bottom 489, page 2
- **Full page:** [pages/flyer167-page2-61c3667977.jpg (flyer page 2)](pages/flyer167-page2-61c3667977.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `7ff9997150643784`
- **Conditions:** `{"multibuy": {"count": 2, "total": 2.98}}`
- **Raw:** `{"block_text": "PANIER DE PE\nCONCOMBRES/\nBe \\5M\n\nDU CANADA", "ocr_lines": ["PANIER DEPE", "CONCOMBRES", "DUCANADA"]}`

**Item Review Analysis (Pass 1):** Correct. Mini cucumbers (Canada) print "2/2.98"; the stored 1.49 is the faithful split. Fresh Vegetables is right.

### Item 15722

![item 15722](images/item-15722.jpg)

- **Name (English):** None
- **Name (French):** POTATOES JAUNE : YELLOW
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 1.98
- **Printed Price:** “1.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 115, top 792, right 327, bottom 883, page 2
- **Full page:** [pages/flyer167-page2-61c3667977.jpg (flyer page 2)](pages/flyer167-page2-61c3667977.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `6ab6aa1d352abea6`
- **Raw:** `{"block_text": "À >» uit _< a ee\nPOTATOES\nJAUNE : YELLOW\ndefeu GANADA NO r", "ocr_lines": ["POTATOES", "JAUNE·YELLOW", "CANADA NO"]}`

**Item Review Analysis (Pass 1):** Correct. Yellow potatoes (10 lb bag) at 1.98/bag — verified. Fresh Vegetables is right.

### Item 15725

![item 15725](images/item-15725.jpg)

- **Name (English):** None
- **Name (French):** CRESSON
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 1.49
- **Printed Price:** “2/2.98”
- **Unit quantity:** 2.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 353, top 420, right 656, bottom 488, page 2
- **Full page:** [pages/flyer167-page2-61c3667977.jpg (flyer page 2)](pages/flyer167-page2-61c3667977.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `da3d0524e7126960`
- **Conditions:** `{"multibuy": {"count": 2, "total": 2.98}}`
- **Raw:** `{"block_text": "CRESSON\nER\nIU MEXIQUE", "ocr_lines": ["CRESSON", "IUMEXIQUE"]}`

**Item Review Analysis (Pass 1):** Correct. Watercress (Mexico) prints "2/2.98" → stored 1.49. Fresh Vegetables is right.

### Item 15727

![item 15727](images/item-15727.jpg)

- **Name (English):** None
- **Name (French):** TOMATE ROMA
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 1.58
- **Printed Price:** “1.58”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 513, top 616, right 787, bottom 684, page 2
- **Full page:** [pages/flyer167-page2-61c3667977.jpg (flyer page 2)](pages/flyer167-page2-61c3667977.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `48f08565a40e795a`
- **Raw:** `{"block_text": "TOMATE ROMA\nS3Sii\nnu quent", "ocr_lines": ["TOMATEROMA", "DUQUEREC"]}`

**Item Review Analysis (Pass 1):** Correct. Roma tomatoes (Quebec) at 1.58/lb — verified. Fresh Vegetables is right.

### Item 15733

![item 15733](images/item-15733.jpg)

- **Name (English):** None
- **Name (French):** JAMBON DÉSOSSÉ DE PORC
- **Brand:** None
- **Category (English):** Meat > Pork & Ham
- **Category (French):** Viande > Porc et jambon
- **How classified:** rule (`pork-ham`)
- **Size:** None
- **Price:** 2.98
- **Printed Price:** “2.98”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 697, top 213, right 984, bottom 313, page 3
- **Full page:** [pages/flyer167-page3-3cfea4065d.jpg (flyer page 3)](pages/flyer167-page3-3cfea4065d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.90 · item_key: `75b83affd9b76430`
- **Raw:** `{"block_text": "JAMBON DÉSOSSÉ\nDE PORC", "ocr_lines": ["JAMBONDESOSSE", "DEPORC"]}`

**Item Review Analysis (Pass 1):** Correct. Boneless pork ham at 2.98/lb — verified. Pork & Ham is right.

### Item 15734

![item 15734](images/item-15734.jpg)

- **Name (English):** None
- **Name (French):** JARRET DE BOEUF SANS 0S
- **Brand:** None
- **Category (English):** Meat > Beef
- **Category (French):** Viande > Bœuf
- **How classified:** rule (`beef`)
- **Size:** None
- **Price:** 6.88
- **Printed Price:** “6.88”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 40, top 414, right 321, bottom 505, page 3
- **Full page:** [pages/flyer167-page3-3cfea4065d.jpg (flyer page 3)](pages/flyer167-page3-3cfea4065d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.95 · item_key: `1e894593faa37394`
- **Raw:** `{"block_text": "JARRET DE BOEUF\nSANS 0S", "ocr_lines": ["JARRETDEBOEUF", "SANSOS"]}`

**Item Review Analysis (Pass 1):** Correct. Boneless beef shank at 6.88/lb (15.14/kg) — verified. Beef is right.

### Item 15737

![item 15737](images/item-15737.jpg)

- **Name (English):** None
- **Name (French):** FAUX FILET DE BŒUF
- **Brand:** None
- **Category (English):** Meat > Beef
- **Category (French):** Viande > Bœuf
- **How classified:** rule (`beef`)
- **Size:** None
- **Price:** 12.88
- **Printed Price:** “12.88”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 699, top 413, right 981, bottom 504, page 3
- **Full page:** [pages/flyer167-page3-3cfea4065d.jpg (flyer page 3)](pages/flyer167-page3-3cfea4065d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.88 · item_key: `c752c799541e51a1`
- **Raw:** `{"block_text": "FAUX FILET\nDE BŒUF", "ocr_lines": ["FAUXFILET", "DEBCEUF"]}`

**Item Review Analysis (Pass 1):** Correct. Beef rib steak (faux filet) at 12.88/lb (28.34/kg) — verified. Beef is right.

### Item 15739

![item 15739](images/item-15739.jpg)

- **Name (English):** None
- **Name (French):** MERLAN ENTIER GROS y
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** None
- **Price:** 4.98
- **Printed Price:** “4.98”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 369, top 913, right 645, bottom 999, page 3
- **Full page:** [pages/flyer167-page3-3cfea4065d.jpg (flyer page 3)](pages/flyer167-page3-3cfea4065d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.89 · item_key: `7d6f745ae93ce95c`
- **Raw:** `{"block_text": "MERLAN ENTIER GROS y", "ocr_lines": ["MERLAN ENTIERGROS"]}`

**Item Review Analysis (Pass 1):** Correct. Whole whiting at 4.98/lb — verified. Fish is right.

### Item 15757

![item 15757](images/item-15757.jpg)

- **Name (English):** None
- **Name (French):** FRE 8 AT COOKED HEAD-ON SHRIMP CUS AVEC TÈTE CREVETTE
- **Brand:** None
- **Category (English):** Fish & Seafood > Shrimp
- **Category (French):** Poissons et fruits de mer > Crevette
- **How classified:** rule (`shrimp`)
- **Size:** None
- **Price:** 2.49
- **Printed Price:** “2/4.98”
- **Unit quantity:** 2.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 94, top 720, right 364, bottom 814, page 5
- **Full page:** [pages/flyer167-page5-a467ff4f28.jpg (flyer page 5)](pages/flyer167-page5-a467ff4f28.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/05.webp
- **Details:** confidence: 0.81 · item_key: `af446d121d3a3e3c`
- **Conditions:** `{"multibuy": {"count": 2, "total": 4.98}}`
- **Raw:** `{"block_text": "FRE 8 AT\nCOOKED HEAD-ON SHRIMP\nCUS AVEC TÈTE CREVETTE\n\nopenceus venr amet)", "ocr_lines": ["COOKED HEAD-ONSHRIMP", "CUIT AVECTETECREVETTE"]}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 167 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Correct as stored, with a note. The name stitches two shrimp offers; the price (2.49) is the faithful split of the visible "2/4.98" badge, which belongs to the wild dried small shrimp at the left of the crop. Shrimp is right either way.

### Item 15710

![item 15710](images/item-15710.jpg)

- **Name (English):** None
- **Name (French):** (CRABEZANTROISTACHES PENTIER 'CONGELE)
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 1KG
- **Price:** 8.88
- **Printed Price:** “8.88”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 283, top 763, right 450, bottom 872, page 1
- **Full page:** [pages/flyer167-page1-ff5737d9fa.jpg (flyer page 1)](pages/flyer167-page1-ff5737d9fa.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/01.webp
- **Details:** confidence: 0.68 · item_key: `5653a1709d27c449`
- **Raw:** `{"block_text": "(CRABEZANTROISTACHES\nPENTIER 'CONGELE)\n\nmere MOTS, SE= RTE\nTHREE St Or CRAB = SEVEN BASKETS\npu _ ee 140%", "ocr_lines": ["CRABEA TROIS TACHES", "ENTIER CONGELE", "FROZEN", "THREE SPOTCRAB", "SEVENBASKETS"], "harvest": {"size": "1KG", "via": "crop"}}`

— from flyer 167 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 1. Seven Baskets frozen three-spot crab (1 kg) prints 8.88; the DB had 2.88 — the frozen yam's badge above. The glued name keeps it unclassified.

### Item 15713

![item 15713](images/item-15713.jpg)

- **Name (English):** None
- **Name (French):** OERCONGELE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 8.88
- **Printed Price:** “8.88”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 353, top 896, right 562, bottom 962, page 1
- **Full page:** [pages/flyer167-page1-ff5737d9fa.jpg (flyer page 1)](pages/flyer167-page1-ff5737d9fa.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/01.webp
- **Details:** confidence: 0.70 · item_key: `56b0a1268b4ca06c`
- **Raw:** `{"block_text": "DER COnGete\nFe PL AKG", "ocr_lines": ["OERCONGELE"]}`

— from flyer 167 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Price correct, name garble. Golden pompano (frozen, 1 kg) at 8.88 each — verified; "OERCONGELE" is OCR noise.

### Item 15714

![item 15714](images/item-15714.jpg)

- **Name (English):** None
- **Name (French):** CAUAMARS) CONGELES) [SEVEN BASKETS} ZA NCE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 450G
- **Price:** 4.98
- **Printed Price:** “4.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 167, top 834, right 263, bottom 963, page 1
- **Full page:** [pages/flyer167-page1-ff5737d9fa.jpg (flyer page 1)](pages/flyer167-page1-ff5737d9fa.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/01.webp
- **Details:** confidence: 0.82 · item_key: `1cf044f8d623c675`
- **Raw:** `{"block_text": "CAUAMARS)\nCONGELES)\n[SEVEN BASKETS}\nZA NCE", "ocr_lines": ["CALAMARS", "CONGELES", "SEVEN BASKETS"], "harvest": {"size": "450G", "via": "crop"}}`

— from flyer 167 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Correct. Seven Baskets frozen squid (450 g) at 4.98 each — verified; name stitch keeps it unclassified.

### Item 15719

![item 15719](images/item-15719.jpg)

- **Name (English):** None
- **Name (French):** DARNESDE CARPEDHERBE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 2.98
- **Printed Price:** “2.98”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 691, top 724, right 801, bottom 827, page 1
- **Full page:** [pages/flyer167-page1-ff5737d9fa.jpg (flyer page 1)](pages/flyer167-page1-ff5737d9fa.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/01.webp
- **Details:** confidence: 0.61 · item_key: `6425b8ec1940c25a`
- **Raw:** `{"block_text": "DARNESIDE\nCARRE|D|HERBE", "ocr_lines": ["DARNESDE", "CARPEDHERBE"]}`

— from flyer 167 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Correct. Grass carp steaks at 2.98/lb — verified on the crop; the glued name keeps it unclassified.

### Item 15720

![item 15720](images/item-15720.jpg)

- **Name (English):** None
- **Name (French):** DIAMONDBRAND
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 454G
- **Price:** 1.58
- **Printed Price:** “1.58”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 140, top 463, right 209, bottom 521, page 1
- **Full page:** [pages/flyer167-page1-ff5737d9fa.jpg (flyer page 1)](pages/flyer167-page1-ff5737d9fa.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `a52180c54cb43b71`
- **Raw:** `{"block_text": "ms PALO)\nDIANOND|BRAND}\n“gain", "ocr_lines": ["DIAMONDBRAND"], "harvest": {"size": "454G", "via": "crop"}}`

— from flyer 167 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Correct. Diamond Brand instant fried noodles (454 g) at 1.58 each — verified; the brand-only name keeps it unclassified.

### Item 15732

![item 15732](images/item-15732.jpg)

- **Name (English):** None
- **Name (French):** ACHAT LOCAL
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 1.98
- **Printed Price:** “1.98”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 849, top 546, right 989, bottom 684, page 2
- **Full page:** [pages/flyer167-page2-61c3667977.jpg (flyer page 2)](pages/flyer167-page2-61c3667977.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `623fd103e3bd377d`
- **Raw:** `{"block_text": "2\n| ACHAT LOCAL |", "ocr_lines": ["ACHATLOCAL"]}`

— from flyer 167 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Price correct, name is a logo. The item is tomatoes at 1.98/lb; its name is the "ACHAT LOCAL" buy-local badge that sits over the cell. Kept for review.

### Item 15738

![item 15738](images/item-15738.jpg)

- **Name (English):** None
- **Name (French):** PAPILLON DE MER
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 2.98
- **Printed Price:** “2.98”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 698, top 717, right 980, bottom 811, page 3
- **Full page:** [pages/flyer167-page3-3cfea4065d.jpg (flyer page 3)](pages/flyer167-page3-3cfea4065d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.82 · item_key: `948b271783df49a6`
- **Raw:** `{"block_text": "PAPILLON DE MER", "ocr_lines": ["PAPILLON DEMER"]}`

— from flyer 167 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Correct. Papillon de mer (pomfret) at 2.98/lb — verified; unclassified on vocabulary.

### Item 15741

![item 15741](images/item-15741.jpg)

- **Name (English):** None
- **Name (French):** ESTOMAC DE COCHON
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 2.48
- **Printed Price:** “2.48”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 369, top 213, right 655, bottom 312, page 3
- **Full page:** [pages/flyer167-page3-3cfea4065d.jpg (flyer page 3)](pages/flyer167-page3-3cfea4065d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.97 · item_key: `61b96733c5cf3213`
- **Raw:** `{"block_text": "ESTOMAC\nDE COCHON", "ocr_lines": ["ESTOMAC", "DE COCHON"]}`

— from flyer 167 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Correct. Pork stomach at 2.48/lb (5.46/kg) — verified; unclassified on the glued name.

### Item 15743

![item 15743](images/item-15743.jpg)

- **Name (English):** None
- **Name (French):** COURBINE JAUNE LOCALE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 1.98
- **Printed Price:** “1.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 41, top 722, right 312, bottom 794, page 3
- **Full page:** [pages/flyer167-page3-3cfea4065d.jpg (flyer page 3)](pages/flyer167-page3-3cfea4065d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `3228d7d927bc82b7`
- **Raw:** `{"block_text": "COURBINE\nJAUNE LOCALE", "ocr_lines": ["COURBINE", "JAUNELOCALE"]}`

— from flyer 167 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Correct. Local yellow croaker at 1.98/lb — verified; unclassified on vocabulary.

### Item 15754

![item 15754](images/item-15754.jpg)

- **Name (English):** None
- **Name (French):** ;-GOBY DE a SABLE TCONGELE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 5.98
- **Printed Price:** “5.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 613, top 373, right 996, bottom 493, page 5
- **Full page:** [pages/flyer167-page5-a467ff4f28.jpg (flyer page 5)](pages/flyer167-page5-a467ff4f28.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-fu-tai-du-16-au-22-octobre-2026/05.webp
- **Details:** confidence: 0.59 · item_key: `a8a66a3cbe80761b`
- **Raw:** `{"block_text": ";-GOBY DE\na SABLE\nTCONGELE", "ocr_lines": ["GOBYDE", "SABLE", "CONGELE"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Frozen sand goby prints 5.98 each; the DB had 58.62, a merged-digit garble. The name stitch keeps it unclassified.
