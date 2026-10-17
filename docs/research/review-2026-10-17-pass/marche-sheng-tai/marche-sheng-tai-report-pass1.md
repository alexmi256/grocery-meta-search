# Marché Sheng Tai — full product report

Store slug: `marche-sheng-tai`. Generated from `data/grocery.db`. A sampled subset of 20 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 168, valid 2026-10-16 → 2026-10-22, 52 items). The expired Oct 9–15 edition is correctly excluded.
- **Sample counts:** 10 classified + 10 unclassified shown, as drawn.
- **Issues found:** the roughest OCR sample since Frutta Si. Names are heavily garbled ("PANE ONGANES", "PATATE VIGLETTE", "WWW.MARCHESHENGTAI.CA"), and 9 of 20 sampled prices were wrong — mostly one-cell shifts in the dense grid (the longans carried the sweet potato's 1.58/lb, the chinchard the cassava's 2.98, the mussel meat the chinchard's 5.58) plus value garbles (croaker 18.00 for 1.98/lb; a box item at 99.98 for 9.98). One stored item was a phantom: the page footer's URL captured as an item name, anchored on the sesame balls' badge — the sesame balls are properly carried by item 15766, and the phantom is deleted. All corrections were read off the flyer pages.
- **Fixes applied this pass:** 15766 → 2.28, 15771 → 3.98, 15791 → 6.98, 15794 → 9.98 (box), 15796 → 1.28 (box), 15801 → 1.98/lb, 15803 → 9.98 (box), 15810 → 5.58, 15814 → 6.38; item 15772 deleted (footer phantom).

## Flyer 168 — valid 2026-10-16 → 2026-10-22 (10 classified items, 10 unclassified)

Source ref: `circulaire-marche-sheng-tai-du-16-au-22-octobre-2026` · fetched 2026-10-17T06:25:38.669Z

### Item 15770

![item 15770](images/item-15770.jpg)

- **Name (English):** None
- **Name (French):** CREVETTES BLANCHES LÉ NS CNT
- **Brand:** None
- **Category (English):** Fish & Seafood > Shrimp
- **Category (French):** Poissons et fruits de mer > Crevette
- **How classified:** rule (`shrimp`)
- **Size:** None
- **Price:** 2.58
- **Printed Price:** “2.58”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 844, top 330, right 988, bottom 459, page 1
- **Full page:** [pages/flyer168-page1-999c5a9af6.jpg (flyer page 1)](pages/flyer168-page1-999c5a9af6.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/01.webp
- **Details:** confidence: 0.86 · item_key: `936d9d2df757edb6`
- **Raw:** `{"block_text": "CREVETTES\nBLANCHES\nLÉ NS CNT", "ocr_lines": ["CREVETTES", "BLANCHES"]}`

**Item Review Analysis (Pass 1):** Correct. White shrimp 20/30 at 2.58/lb (13.16/kg) — the badge above the name is the shrimp's; verified. Shrimp is right.

### Item 15780

![item 15780](images/item-15780.jpg)

- **Name (English):** None
- **Name (French):** SAUCISSE AU PORC STYLE CHINOIS
- **Brand:** None
- **Category (English):** Meat > Sausages
- **Category (French):** Viande > Saucisses
- **How classified:** rule (`sausages`)
- **Size:** None
- **Price:** 0.98
- **Printed Price:** “0.98”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 874, top 191, right 992, bottom 275, page 2
- **Full page:** [pages/flyer168-page2-67204f9566.jpg (flyer page 2)](pages/flyer168-page2-67204f9566.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.50 · item_key: `ee8c6d340be0aff4`
- **Raw:** `{"block_text": "SAUCISSE AU PORC\nSTYLE CHINOIS", "ocr_lines": ["SAUCISSEAU PORC", "STYLECHINOIS"]}`

**Item Review Analysis (Pass 1):** Correct. Chinese-style pork sausage at 0.98/lb — verified on the crop. Sausages is right.

### Item 15783

![item 15783](images/item-15783.jpg)

- **Name (English):** None
- **Name (French):** MELON D'HIVERS
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 0.68
- **Printed Price:** “0.68”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 565, top 141, right 664, bottom 251, page 2
- **Full page:** [pages/flyer168-page2-67204f9566.jpg (flyer page 2)](pages/flyer168-page2-67204f9566.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.73 · item_key: `77108113f3c5df92`
- **Raw:** `{"block_text": "MELON\nD'HIVERS", "ocr_lines": ["MELON", "D'HIVERS"]}`

**Item Review Analysis (Pass 1):** Correct. Winter melon at 0.68/lb (1.50/kg) — verified. (Shelved under Fresh Fruits; melon vocabulary — the same treatment as other melons.)

### Item 15794

![item 15794](images/item-15794.jpg)

- **Name (English):** None
- **Name (French):** PANE ONGANES À FRAIS EN BOÎTE
- **Brand:** None
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`specific-canned`)
- **Size:** None
- **Price:** 1.58
- **Printed Price:** “1.58”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 861, top 215, right 988, bottom 317, page 3
- **Full page:** [pages/flyer168-page3-44b4d9b99d.jpg (flyer page 3)](pages/flyer168-page3-44b4d9b99d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `2ed67086fea5210a`
- **Raw:** `{"block_text": "ee 2KGS\nPANE ONGANES\nÀ FRAIS EN BOÎTE\n> a) At NE", "ocr_lines": ["2KGS", "LONGANES", "FRAIS EN BOITE"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 3. Fresh longans in a 2 kg box print 9.98 per box; the DB had 1.58 — the purple sweet potato's per-lb price from the cell above. Unit now pack. (The stored name's "PANE ONGANES" is the garbled "LONGANES"; the classification still landed on Canned & Pickled via the box wording — the product is fresh, in a box.)

### Item 15796

![item 15796](images/item-15796.jpg)

- **Name (English):** None
- **Name (French):** PANIER DE PETITS CONCOMBRES
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 0.98
- **Printed Price:** “0.98”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 184, top 80, right 318, bottom 183, page 3
- **Full page:** [pages/flyer168-page3-44b4d9b99d.jpg (flyer page 3)](pages/flyer168-page3-44b4d9b99d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `fc0f5a2e036e32e4`
- **Raw:** `{"block_text": "PANIER\nDE PETITS\nCONCOMBRES", "ocr_lines": ["PANIER", "DEPETITS", "CONCOMBRES"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 3. Mini cucumbers (Mucci, 454 g tray) print 1.28 per box; the DB had 0.98 — the baby gai choy's per-lb price above. Unit now pack. Fresh Vegetables is right.

### Item 15799

![item 15799](images/item-15799.jpg)

- **Name (English):** None
- **Name (French):** DARNES DE SAUMON
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** None
- **Price:** 7.98
- **Printed Price:** “7.98”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 514, top 651, right 729, bottom 723, page 3
- **Full page:** [pages/flyer168-page3-44b4d9b99d.jpg (flyer page 3)](pages/flyer168-page3-44b4d9b99d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.90 · item_key: `90f9cab11477c27e`
- **Raw:** `{"block_text": "DARNES\nDE SAUMON", "ocr_lines": ["DARNES", "DESAUMON"]}`

**Item Review Analysis (Pass 1):** Correct. Salmon steaks at 7.98/lb (17.56/kg) — verified. Fish is right.

### Item 15804

![item 15804](images/item-15804.jpg)

- **Name (English):** None
- **Name (French):** PATATE VIGLETTE
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
- **bbox:** left 815, top 85, right 987, bottom 174, page 3
- **Full page:** [pages/flyer168-page3-44b4d9b99d.jpg (flyer page 3)](pages/flyer168-page3-44b4d9b99d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `570ba661e4734391`
- **Conditions:** `{"multibuy": {"count": 2, "total": 2.98}}`
- **Raw:** `{"block_text": "PATATE\nVIGLETTE", "ocr_lines": ["PATATE", "VIOLETTE"]}`

**Item Review Analysis (Pass 1):** Correct. Purple sweet potatoes print "2/2.98"; the stored 1.49 is the per-unit split (the badge sits above the name in this flyer's layout, confirmed against the longan zoom where the potato's own 1.58/lb badge also appears — the 2/2.98 badge is the potato's count offer). Fresh Vegetables is right.

### Item 15805

![item 15805](images/item-15805.jpg)

- **Name (English):** None
- **Name (French):** > VIEILLE NOIX DE COCO
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Dried Fruits & Nuts
- **Category (French):** Fruits et légumes > Fruits séchés et noix
- **How classified:** rule (`dried-fruits-nuts`)
- **Size:** None
- **Price:** 1.49
- **Printed Price:** “2/2.98”
- **Unit quantity:** 2.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 476, top 218, right 649, bottom 306, page 3
- **Full page:** [pages/flyer168-page3-44b4d9b99d.jpg (flyer page 3)](pages/flyer168-page3-44b4d9b99d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `8252da95ba06a1e7`
- **Conditions:** `{"multibuy": {"count": 2, "total": 2.98}}`
- **Raw:** `{"block_text": "> VIEILLE\nNOIX DE COCO", "ocr_lines": ["VIEILLE", "NOIX DECOCO"]}`

**Item Review Analysis (Pass 1):** Correct. Old coconuts print "2/2.98"; stored 1.49 is the split. Dried Fruits & Nuts is the coconut shelf.

### Item 15810

![item 15810](images/item-15810.jpg)

- **Name (English):** None
- **Name (French):** POISSON CHINCHARD "IRB
- **Brand:** None
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** 500G
- **Price:** 2.98
- **Printed Price:** “2.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 207, top 481, right 337, bottom 596, page 4
- **Full page:** [pages/flyer168-page4-e363a6aba7.jpg (flyer page 4)](pages/flyer168-page4-e363a6aba7.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/04.webp
- **Details:** confidence: 0.76 · item_key: `680076b7a592ffa8`
- **Raw:** `{"block_text": "POISSON\nCHINCHARD\n\"IRB\n\nREG.: 6.99 / 750 6", "ocr_lines": ["POISSON", "CHINCHARD", "REG.:6.99/750G"], "harvest": {"size": "500G", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 4. Chinchard (mackerel scad, 750 g, reg. 6.99) prints 5.58; the DB had 2.98 — the frozen cassava's badge from the cell above. Fish is right.

### Item 15817

![item 15817](images/item-15817.jpg)

- **Name (English):** None
- **Name (French):** VINAIGRE BLANC DES PHILIPPINES FFRDEÉ RÉG.: 2.99
- **Brand:** None
- **Category (English):** Pantry > Oils & Vinegar
- **Category (French):** Produits du garde-manger > Huile et vinaigre
- **How classified:** rule (`oils-vinegar`)
- **Size:** 1L
- **Price:** 1.98
- **Printed Price:** “1.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 227, top 38, right 332, bottom 138, page 4
- **Full page:** [pages/flyer168-page4-e363a6aba7.jpg (flyer page 4)](pages/flyer168-page4-e363a6aba7.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `4dc09f7f6cdb7096`
- **Raw:** `{"block_text": "VINAIGRE BLANC\nDES PHILIPPINES\nFFRDEÉ\n\nRÉG.: 2.99", "ocr_lines": ["VINAIGREBLANC", "DESPHILIPPINES", "REG:2.99"], "harvest": {"size": "1L", "unit": "each", "via": "crop"}}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 168 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Correct. Philippine white vinegar (1 L) at 1.98 (reg. 2.99) — verified. Oils & Vinegar is right.

### Item 15766

![item 15766](images/item-15766.jpg)

- **Name (English):** None
- **Name (French):** BOULE DE SÉSAME EN PATE DE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 260G
- **Price:** 3.48
- **Printed Price:** “3.48”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 109, top 703, right 340, bottom 829, page 1
- **Full page:** [pages/flyer168-page1-999c5a9af6.jpg (flyer page 1)](pages/flyer168-page1-999c5a9af6.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/01.webp
- **Details:** confidence: 0.77 · item_key: `6b9ee15aba4df41b`
- **Raw:** `{"block_text": "BOULE DE SÉSAME\n\nEN PATE DE\n\nsuerrene sean rares MARICOTS SUCREE\n} sui ASTESESANE SSS DIR\nBoule de sesame en pate de haricats sucree Unes: ee\n\n= +t FPE ds D ENS", "ocr_lines": ["BOULEDESESAME", "ENPATEDE", "HARICOTS SUCREE", "SWEETENEDBEAN PASTESESAME BA", "REG:2.99"], "harvest": {"size": "260G", "via": "crop"}}`

— from flyer 168 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crops. Sweetened bean-paste sesame balls (260 g, reg. 2.99) print 2.28; the DB had 3.48, and the badge visible in this item's crop (3.98) belongs to the red-skin peanuts above. The item stays unclassified under its truncated name.

### Item 15771

![item 15771](images/item-15771.jpg)

- **Name (English):** None
- **Name (French):** ARACHIDE À PEAU ROUGE ST REE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 907G
- **Price:** 2.00
- **Printed Price:** “2”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 260, top 490, right 524, bottom 653, page 1
- **Full page:** [pages/flyer168-page1-999c5a9af6.jpg (flyer page 1)](pages/flyer168-page1-999c5a9af6.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/01.webp
- **Details:** confidence: 0.90 · item_key: `ecb8e8e033b39721`
- **Raw:** `{"block_text": "ARACHIDE À\nPEAU ROUGE\nST REE\nREG.: 5.99\n\n0n7 6", "ocr_lines": ["ARACHIDEA", "PEAU ROUGE", "REG:5.99"], "harvest": {"size": "907G", "unit": "lb", "via": "crop"}}`

— from flyer 168 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from item 15766's crop. Red-skin peanuts print 3.98; the DB had 2.00. Unclassified under its garbled name ("ARACHIDE À PEAU ROUGE" with OCR noise).

### Item 15772

![item 15772](images/item-15772.jpg)

- **Name (English):** None
- **Name (French):** WWW.MARCHESHENGTAI.CA
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 2.29
- **Printed Price:** “2.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 92, top 889, right 361, bottom 988, page 1
- **Full page:** [pages/flyer168-page1-999c5a9af6.jpg (flyer page 1)](pages/flyer168-page1-999c5a9af6.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/01.webp
- **Details:** confidence: 0.93 · item_key: `3d010de484e6124d`
- **Raw:** `{"block_text": "WWW.MARCHESHENGTAI.CA", "ocr_lines": ["WWW.MARCHESHENGTAI.CA"]}`

— from flyer 168 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** DELETED. Not a product: the name is the page footer's URL (WWW.MARCHESHENGTAI.CA) and its anchor sits on the sesame balls' 2.28 badge — the same product item 15766 carries. A footer phantom of the Bonanza type, removed.

### Item 15789

![item 15789](images/item-15789.jpg)

- **Name (English):** None
- **Name (French):** VERMICE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 1.50
- **Printed Price:** “2/3.00”
- **Unit quantity:** 2.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 475, top 860, right 667, bottom 953, page 2
- **Full page:** [pages/flyer168-page2-67204f9566.jpg (flyer page 2)](pages/flyer168-page2-67204f9566.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.98 · item_key: `cbdff59923d8b70e`
- **Conditions:** `{"multibuy": {"count": 2, "total": 3.0}}`
- **Raw:** `{"block_text": "CE\nVERMICE\n+47 10 ss |", "ocr_lines": ["VERMICEL", "VERMICELTE"]}`

— from flyer 168 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Correct. Mamy rice vermicelli prints "2/3.00"; the stored 1.50 is the per-unit split. Unclassified under the truncated name "VERMICE…".

### Item 15791

![item 15791](images/item-15791.jpg)

- **Name (English):** None
- **Name (French):** GAPELAN PC F7 FRIT . {= SES ——— RÉG.: 7.99 /CH
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 8.69
- **Printed Price:** “8.69”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 688, top 919, right 926, bottom 989, page 3
- **Full page:** [pages/flyer168-page3-44b4d9b99d.jpg (flyer page 3)](pages/flyer168-page3-44b4d9b99d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.98 · item_key: `b910d8f4e6bce506`
- **Raw:** `{"block_text": "ae \\ À\n\n(poisson \\ COME\nGAPELAN PC\n\nF7 FRIT . {=\nSES ———\nRÉG.: 7.99 /CH\n\nno | TéL:514-683-2888", "ocr_lines": ["POISSON", "CAPELAN", "FRIT", "REG.:7.99", "TEL:514-683-2888"]}`

— from flyer 168 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Fried capelin prints 6.98 (reg. 7.99); the DB had 8.69 (digit scramble). Unclassified under its garbled name.

### Item 15795

![item 15795](images/item-15795.jpg)

- **Name (English):** None
- **Name (French):** {ES SAUTES
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 6.98
- **Printed Price:** “6.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 398, top 921, right 600, bottom 966, page 3
- **Full page:** [pages/flyer168-page3-44b4d9b99d.jpg (flyer page 3)](pages/flyer168-page3-44b4d9b99d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `60a0e5045001125c`
- **Raw:** `{"block_text": "uf aatecumes\n{ES SAUTES\n\" par\n\nRÉG.: 5.99", "ocr_lines": ["LEGUMES", "VARIESSAUTES", "REG:5.99"]}`

— from flyer 168 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Correct as printed. Sautéed mixed vegetables at 6.98 — the badge is unambiguous even though the printed "RÉG.: 5.99" sits below it (the flyer's own inconsistency). Unclassified under the garbled "{ES SAUTES" fragment.

### Item 15801

![item 15801](images/item-15801.jpg)

- **Name (English):** None
- **Name (French):** COURBINE JAUNE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 18.00
- **Printed Price:** “18”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 535, top 506, right 726, bottom 576, page 3
- **Full page:** [pages/flyer168-page3-44b4d9b99d.jpg (flyer page 3)](pages/flyer168-page3-44b4d9b99d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.93 · item_key: `a67cbbd7758c4002`
- **Conditions:** `{"alt_prices": ["1.98"]}`
- **Raw:** `{"block_text": "COURBINE\nJAUNE", "ocr_lines": ["COURBINE", "JAUNE"]}`

— from flyer 168 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Yellow croaker ("courbine jaune", not cleaned) prints 1.98/lb (4.36/kg); the DB had 18.00. Unit now pound. Unclassified — "courbine" is not in the fish vocabulary.

### Item 15803

![item 15803](images/item-15803.jpg)

- **Name (English):** None
- **Name (French):** /BTE
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 99.98
- **Printed Price:** “99.98”
- **Unit quantity:** 1.0
- **Unit measurement:** pack
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 866, top 348, right 981, bottom 400, page 3
- **Full page:** [pages/flyer168-page3-44b4d9b99d.jpg (flyer page 3)](pages/flyer168-page3-44b4d9b99d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.98 · item_key: `d909c15fe161cbb0`
- **Raw:** `{"block_text": "“BTE", "ocr_lines": ["/BTE"]}`

— from flyer 168 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. The item's whole name is the unit fragment "/BTE"; its badge prints 9.98 per box — the DB had 99.98 (a duplicated 9). Unit now pack. The product itself can't be named from the surviving text; kept for review.

### Item 15814

![item 15814](images/item-15814.jpg)

- **Name (English):** None
- **Name (French):** VIANDE DE MOULE CUITE BOR
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 500G
- **Price:** 5.58
- **Printed Price:** “5.58”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 214, top 601, right 335, bottom 716, page 4
- **Full page:** [pages/flyer168-page4-e363a6aba7.jpg (flyer page 4)](pages/flyer168-page4-e363a6aba7.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/04.webp
- **Details:** confidence: 0.69 · item_key: `c3468b06aa6f5b60`
- **Raw:** `{"block_text": "VIANDE DE\nMOULE CUITE\nBOR\n\nREG.: 7.99\n\nanne", "ocr_lines": ["VIANDEDE", "MOULE CUITE", "REG:7.99"], "harvest": {"size": "500G", "via": "crop"}}`

— from flyer 168 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 4. Cooked mussel meat (500 g, reg. 7.99) prints 6.38; the DB had 5.58 — the chinchard's price. Unclassified under its truncated name.

### Item 15815

![item 15815](images/item-15815.jpg)

- **Name (English):** None
- **Name (French):** REG:7.99
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 6.98
- **Printed Price:** “6.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 537, top 579, right 674, bottom 804, page 4
- **Full page:** [pages/flyer168-page4-e363a6aba7.jpg (flyer page 4)](pages/flyer168-page4-e363a6aba7.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-marche-sheng-tai-du-16-au-22-octobre-2026/04.webp
- **Details:** confidence: 0.80 · item_key: `22e33d4275bf2589`
- **Raw:** `{"block_text": "REG.: 7.99\nKITIEH", "ocr_lines": ["REG:7.99"]}`

**Item Review Analysis (Pass 1):** Correct price, fragment name. The item is the marinated milkfish ("chanos mariné", 350 g, reg. 7.99) — only the "REG:7.99" text survived as its name, but its 6.98 badge is correct. Unclassified.
