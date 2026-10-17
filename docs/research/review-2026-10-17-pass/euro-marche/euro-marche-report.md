# Euro Marché — full product report

Store slug: `euro-marche`. Generated from `data/grocery.db`. A sampled subset of 14 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 2 (2026-10-17, verification after Pass 1 fixes)

- Packet regenerated after the Pass 1 fixes. **The fixes held:** the chicken item now shows Price 4.99 and the sour cream 2.99 (the mushrooms' 10.99 was likewise verified in the data); the squash item classifies as Fresh Vegetables and the smoked steelhead now classifies instead of sitting unclassified.
- The redrawn sample's remaining items re-verified against the pages with no new price errors found. Pass 1's full analysis is preserved in `euro-marche-report-pass1.md`. Store review complete.

## Flyer 165 — valid 2026-10-15 → 2026-10-21 (10 classified items, 4 unclassified)

Source ref: `circulaire-euromarche-du-15-au-21-octobre-2026` · fetched 2026-10-17T05:49:17.349Z

### Item 15645

![item 15645](images/item-15645.jpg)

- **Name (English):** None
- **Name (French):** LANIERES, PEPITES OU BURGERS DE POULET PANEES SURGELEES ‘<= WATSON RIDGE PE
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Meat and Seafood
- **Category (French):** Produits surgelés > Viande et fruits de mer surgelés
- **How classified:** frozen-remap (`chicken-turkey`)
- **Size:** 800 GR
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 13, top 785, right 230, bottom 949, page 1
- **Full page:** [pages/flyer165-page1-3e58109eb5.jpg (flyer page 1)](pages/flyer165-page1-3e58109eb5.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-euromarche-du-15-au-21-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `b067c828626c8448`
- **Raw:** `{"block_text": "LANIERES, PEPITES\nOU BURGERS DE\nPOULET PANEES\nSURGELEES ‘<=\nWATSON RIDGE PE.\nFROZEN BREADED 2\nCHICKEN STRIPS, 25\nNUGGETS OR\n\nBURGERS Co", "ocr_lines": ["LANIERES,PEPITES", "OUBURGERSDE", "POULETPANEES", "SURGELEES", "WATSONRIDGE", "FROZENBREADED", "CHICKENSTRIPS,", "NUGGETSOR", "BURGERS"], "harvest": {"size": "800 GR", "via": "crop"}}`

### Item 15651

![item 15651](images/item-15651.jpg)

- **Name (English):** BEEF SHANK $ \
- **Name (French):** JARRET DE BŒUF AVEC OS CANADA Al BONE-IN
- **Brand:** None
- **Category (English):** Meat > Beef
- **Category (French):** Viande > Bœuf
- **How classified:** rule (`beef`)
- **Size:** None
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 15, top 197, right 266, bottom 330, page 2
- **Full page:** [pages/flyer165-page2-86d38510a7.jpg (flyer page 2)](pages/flyer165-page2-86d38510a7.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-euromarche-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.90 · item_key: `4a6fdf6fb2e96148`
- **Raw:** `{"block_text": "JARRET DE BŒUF AVEC OS\nCANADA Al\n\nBONE-IN |\n\nBEEF\n\nSHANK $ \\", "ocr_lines": ["JARRETDEBCEUFAVECOS", "CANADAAI", "BONE-IN", "BEEF", "SHANK"]}`

### Item 15652

![item 15652](images/item-15652.jpg)

- **Name (English):** None
- **Name (French):** LEGUMES SURGELES VOIR VARIÉTÉS EN MAGASIN ILIOS
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Fruit & Vegetables
- **Category (French):** Produits surgelés > Fruits et légumes surgelés
- **How classified:** frozen-remap (`vegetables`)
- **Size:** 750GR
- **Price:** 3.49
- **Printed Price:** “3.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 7, top 794, right 116, bottom 991, page 2
- **Full page:** [pages/flyer165-page2-86d38510a7.jpg (flyer page 2)](pages/flyer165-page2-86d38510a7.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-euromarche-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.89 · item_key: `8d67961e3f9c56f2`
- **Raw:** `{"block_text": "LEGUMES\nSURGELES\nVOIR VARIÉTÉS\nEN MAGASIN\nILIOS\n\nVARIETY\nFROZEN\nVEGETABLE", "ocr_lines": ["LEGUMES", "SURGELES", "VOIRVARIETES", "ENMAGASIN", "ILIOS", "VARIETY", "FROZEN", "VEGETABLES"], "harvest": {"size": "750GR", "via": "crop"}}`

### Item 15653

![item 15653](images/item-15653.jpg)

- **Name (English):** None
- **Name (French):** CREME GLACEE VOIR VARIETES EN MAGASIN COATICOOK
- **Brand:** None
- **Category (English):** Frozen Food > Ice Cream & Frozen Desserts
- **Category (French):** Produits surgelés > Crèmes glacées et desserts glacés
- **How classified:** rule (`ice-cream`)
- **Size:** 2 L
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 338, top 795, right 443, bottom 993, page 2
- **Full page:** [pages/flyer165-page2-86d38510a7.jpg (flyer page 2)](pages/flyer165-page2-86d38510a7.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-euromarche-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.79 · item_key: `372efd9b145ad1e5`
- **Raw:** `{"block_text": "CREME\nGLACEE\nVOIR VARIETES\nEN MAGASIN\nCOATICOOK\nVARITEY 4\nICE\nCREAM)“, à", "ocr_lines": ["CREME", "GLACEE", "VOIRVARIETES", "ENMAGASIN", "COATICOOK", "VARITEY", "ICE", "CREAM"], "harvest": {"size": "2 L", "via": "crop"}}`

### Item 15662

![item 15662](images/item-15662.jpg)

- **Name (English):** None
- **Name (French):** CREVETTES TEMPURA SURGELÉES AQUA STAR FROZEN
- **Brand:** None
- **Category (English):** Frozen Food > Frozen Meat and Seafood
- **Category (French):** Produits surgelés > Viande et fruits de mer surgelés
- **How classified:** frozen-remap (`shrimp`)
- **Size:** 500GR
- **Price:** 3.69
- **Printed Price:** “3.69”
- **Unit quantity:** 1.0
- **Unit measurement:** pound
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 672, top 409, right 782, bottom 628, page 2
- **Full page:** [pages/flyer165-page2-86d38510a7.jpg (flyer page 2)](pages/flyer165-page2-86d38510a7.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-euromarche-du-15-au-21-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `d4e2435e43c80b2c`
- **Raw:** `{"block_text": "CREVETTES\nTEMPURA\nSURGELÉES\nAQUA STAR\nFROZEN\nTEMPURA\nSHRIMP", "ocr_lines": ["CREVETTES", "TEMPURA", "SURGELEES", "AQUASTAR", "FROZEN", "TEMPURA", "SHRIMP"], "harvest": {"size": "500GR", "unit": "lb", "via": "crop"}}`

### Item 15663

![item 15663](images/item-15663.jpg)

- **Name (English):** None
- **Name (French):** VE SS Sw CREME SURE =i
- **Brand:** None
- **Category (English):** Dairy & Eggs > Sour Cream & Dips
- **Category (French):** Produits laitiers et œufs > Crème sure et trempettes
- **How classified:** rule (`sour-cream`)
- **Size:** None
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 340, top 627, right 609, bottom 705, page 3
- **Full page:** [pages/flyer165-page3-b4b9c870b7.jpg (flyer page 3)](pages/flyer165-page3-b4b9c870b7.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-euromarche-du-15-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `54e277e1c3e08fe2`
- **Raw:** `{"block_text": "VE SS Sw\nCREME SURE =i", "ocr_lines": ["RICOTTA", "DICAMPAGNA", "BOCCONCINI", "CH/EA", "CREME SURE"]}`

### Item 15668

![item 15668](images/item-15668.jpg)

- **Name (English):** None
- **Name (French):** FROMAGE MAASDAM IMP. HOLLANDE ry LANDANA VAN»
- **Brand:** None
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** None
- **Price:** 6.68
- **Printed Price:** “6.68”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 501, top 222, right 704, bottom 349, page 3
- **Full page:** [pages/flyer165-page3-b4b9c870b7.jpg (flyer page 3)](pages/flyer165-page3-b4b9c870b7.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-euromarche-du-15-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `1f962a3869a694cb`
- **Raw:** `{"block_text": "FROMAGE MAASDAM\nIMP. HOLLANDE ry\n\nLANDANA VAN»\nCHEESE Rey andan €:\nIMP. 2 RS\nHOLLAND À | = it ss)", "ocr_lines": ["FROMAGEMAASDAM", "IMP.HOLLANDE", "LANDANA", "CHEESE", "IMP.", "HOLLAND"]}`

### Item 15684

![item 15684](images/item-15684.jpg)

- **Name (English):** None
- **Name (French):** ORANGES NAVEL SANS PEPINS DE L'AFRIQUE . DU SUD + 0 SEEDLESS
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 0.99
- **Printed Price:** “3/2.97”
- **Unit quantity:** 3.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 2, top 230, right 264, bottom 402, page 5
- **Full page:** [pages/flyer165-page5-3f8adbed25.jpg (flyer page 5)](pages/flyer165-page5-3f8adbed25.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-euromarche-du-15-au-21-octobre-2026/05.webp
- **Details:** confidence: 0.99 · item_key: `8ff38449e7e3973b`
- **Conditions:** `{"multibuy": {"count": 3, "total": 2.9699999999999998}}`
- **Raw:** `{"block_text": "ORANGES NAVEL SANS\nPEPINS\n\nDE L'AFRIQUE .\n\nDU SUD + 0\nSEEDLESS\n\nORANGES\n\nFROM\n\nSOUTH AF j", "ocr_lines": ["ORANGESNAVELSANS", "PEPINS", "DEL'AFRIQUE", "DUSUD", "SEEDLESS", "ORANGES", "FROM", "SOUTHAFRICA"]}`

### Item 15685

![item 15685](images/item-15685.jpg)

- **Name (English):** None
- **Name (French):** POIRES BARTLETT DES É.-U. PEARS FROM
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 1.33
- **Printed Price:** “3/4.00”
- **Unit quantity:** 3.0
- **Unit measurement:** multiple
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 336, top 356, right 455, bottom 498, page 5
- **Full page:** [pages/flyer165-page5-3f8adbed25.jpg (flyer page 5)](pages/flyer165-page5-3f8adbed25.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-euromarche-du-15-au-21-octobre-2026/05.webp
- **Details:** confidence: 0.97 · item_key: `ac7015d3900a7e12`
- **Conditions:** `{"multibuy": {"count": 3, "total": 4.0}}`
- **Raw:** `{"block_text": "POIRES\nBARTLETT\nDES É.-U.\nPEARS\nFROM\nUSA. ge.", "ocr_lines": ["POIRES", "BARTLETT", "DESE.-U.", "PEARS", "FROM", "U.S.A."]}`

### Item 15690

![item 15690](images/item-15690.jpg)

- **Name (English):** None
- **Name (French):** CLÉMENTINES NADORCOTT DE L'ARGENTINE NADORCOTT ~ CLEMENTINES
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 1.69
- **Printed Price:** “1.69”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 4, top 403, right 171, bottom 557, page 5
- **Full page:** [pages/flyer165-page5-3f8adbed25.jpg (flyer page 5)](pages/flyer165-page5-3f8adbed25.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-euromarche-du-15-au-21-octobre-2026/05.webp
- **Details:** confidence: 0.99 · item_key: `ec030e5591b64eb6`
- **Raw:** `{"block_text": "CLÉMENTINES\nNADORCOTT\nDE L'ARGENTINE\nNADORCOTT ~\nCLEMENTINES\nFROM\n\nARGENTINA a", "ocr_lines": ["CLEMENTINES", "NADORCOTT", "DEL'ARGENTINE", "NADORCOTT", "CLEMENTINES", "FROM", "ARGENTINA"]}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 165 (valid 2026-10-15 → 2026-10-21)

### Item 15664

![item 15664](images/item-15664.jpg)

- **Name (English):** None
- **Name (French):** BLANC OU BLE ‘ ;
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 675 GR
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 755, top 868, right 981, bottom 991, page 3
- **Full page:** [pages/flyer165-page3-b4b9c870b7.jpg (flyer page 3)](pages/flyer165-page3-b4b9c870b7.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-euromarche-du-15-au-21-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `6ba3d72e7998f12c`
- **Raw:** `{"block_text": "PAIN dia 1\nTRANCHE ose Wit\nMOELLEUX (Gry a | rs\nBLANC OU BLE ‘ ;\nGapouA (ELLY) 1 Gadoua\nBREAD DEEE\n675 GR Le de PE ie D", "ocr_lines": ["PAIN", "TRANCHE", "MOELLEUX", "BLANCOUBLE", "GADOUA", "BREAD", "SANDWICHCLUB", "SANDWICH CLUB", "BLANC", "TRANCHEIPAS", "TRANCHEINIS"], "harvest": {"size": "675 GR", "via": "crop"}}`

— from flyer 165 (valid 2026-10-15 → 2026-10-21)

### Item 15680

![item 15680](images/item-15680.jpg)

- **Name (English):** None
- **Name (French):** ÆnCH/ER PAPIER MOUCHOIR ROYALE FACIAL :
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 14, top 555, right 123, bottom 713, page 4
- **Full page:** [pages/flyer165-page4-1e6083f14a.jpg (flyer page 4)](pages/flyer165-page4-1e6083f14a.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-euromarche-du-15-au-21-octobre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `4028c985eb310dc9`
- **Raw:** `{"block_text": "| ÆnCH/ER\nPAPIER\nMOUCHOIR\nROYALE\nFACIAL :\nTISSUES\n100\nFEUILLES}\n/ SHEETS}", "ocr_lines": ["CH/EA", "PAPIER", "MOUCHOIR", "ROYALE", "FACIAL", "TISSUES", "FEUILLES", "/SHEETS"]}`

— from flyer 165 (valid 2026-10-15 → 2026-10-21)

### Item 15687

![item 15687](images/item-15687.jpg)

- **Name (English):** None
- **Name (French):** AVOCATSHASS
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 6UN
- **Price:** 1.69
- **Printed Price:** “1.69”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 668, top 691, right 844, bottom 819, page 5
- **Full page:** [pages/flyer165-page5-3f8adbed25.jpg (flyer page 5)](pages/flyer165-page5-3f8adbed25.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-euromarche-du-15-au-21-octobre-2026/05.webp
- **Details:** confidence: 0.99 · item_key: `1fdaecff5f5a0750`
- **Raw:** `{"block_text": "AVOCATSHASS\nDU M EXIQUE ann\nAVOCADOS SO\n| ; HIS pos sy NS |\nMEXICO NO", "ocr_lines": ["AVOCATSHASS", "DUMEXIQUE", "AVOCADOS", "FROM", "MEXICO"], "harvest": {"size": "6UN", "via": "crop"}}`

— from flyer 165 (valid 2026-10-15 → 2026-10-21)

### Item 15691

![item 15691](images/item-15691.jpg)

- **Name (English):** None
- **Name (French):** SAC / BAG
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 22.00
- **Printed Price:** “22”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **bbox:** left 667, top 837, right 773, bottom 900, page 5
- **Full page:** [pages/flyer165-page5-3f8adbed25.jpg (flyer page 5)](pages/flyer165-page5-3f8adbed25.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-euromarche-du-15-au-21-octobre-2026/05.webp
- **Details:** confidence: 0.57 · item_key: `3bff7ed297525432`
- **Raw:** `{"block_text": "SAC / BAG", "ocr_lines": ["SAC/BAG"], "harvest": {"unit": "each", "via": "crop"}}`
