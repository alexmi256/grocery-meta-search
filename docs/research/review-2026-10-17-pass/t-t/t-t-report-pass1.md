# T&T Supermarché — full product report

Store slug: `t-t`. Generated from `data/grocery.db`. A sampled subset of 20 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 169, valid 2026-10-16 → 2026-10-22, 130 items). The expired Oct 9–15 edition is correctly excluded.
- **Sample counts:** 10 classified + 10 unclassified shown.
- **Issues found:** 7 wrong prices and 1 points phantom. This flyer prints member prices as a green sub-badge under a red special price; the corrections below use the red special price (the one every customer pays), with member prices noted per item. The errors: sriracha stored at 0.04 (its price is 4.97), dried prunes stored with the neighbouring turtle chips' 4.50 (theirs: 6.97 special / 5.97 member), the Luckin espresso stored with a tea's 6.97 from the row above (its own: 16.99 / 15.99 member), the frozen carp stored with the tempura platter's 10.57 (its own: 7.98 / 6.98), the lamb shoulder with the sliced meat's 9.99 to its left (its own: 11.99/lb), a merged noodles-and-tea item carrying the tea's regular price (the noodles lead the name: 4.97 / 3.97 member), and a dumpling item named "Jch" priced 2.66 against a printed 9.97. Item 15908 merged two snacks from the points-redemption page and stored 7.00 — assembled from a "700 Pts" badge; that page section prices in points, not dollars, so the item is deleted.
- **Fixes applied this pass:** 15833 → 9.97, 15840 → 11.99/lb, 15851 → 16.99, 15854 → 4.97, 15902 → 6.97, 15914 → 7.98, 15947 → 4.97; item 15908 deleted.

## Flyer 169 — valid 2026-10-16 → 2026-10-22 (10 classified items, 10 unclassified)

Source ref: `circulaire-supermarche-tt-du-16-au-22-octobre-2026` · fetched 2026-10-17T06:29:17.896Z

### Item 15829

![item 15829](images/item-15829.jpg)

- **Name (English):** None
- **Name (French):** T&Tnoixde cajou//noix melange
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Dried Fruits & Nuts
- **Category (French):** Fruits et légumes > Fruits séchés et noix
- **How classified:** rule (`dried-fruits-nuts`)
- **Size:** 700g/800g
- **Price:** 13.97
- **Printed Price:** “13.97”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 790, top 892, right 922, bottom 940, page 1
- **Full page:** [pages/flyer169-page1-f01465bd04.jpg (flyer page 1)](pages/flyer169-page1-f01465bd04.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/01.webp
- **Details:** confidence: 0.99 · item_key: `bbd4eae45231da3e`
- **Raw:** `{"block_text": "we «\nT&Tinoix de\ncajou//ñoix\nmélange ® :\n+ 6 hCUg", "ocr_lines": ["T&Tnoixde", "cajou//noix", "melange"], "harvest": {"size": "700g/800g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. T&T cashews / mixed nuts (700-800 g) at 13.97 + taxes — verified. Dried Fruits & Nuts is right.

### Item 15835

![item 15835](images/item-15835.jpg)

- **Name (English):** None
- **Name (French):** Pomelode miel/Pomelo Rouge
- **Brand:** None
- **Category (English):** Pantry > Honey, Syrups & Spreads
- **Category (French):** Produits du garde-manger > Miel, sirops et tartinades
- **How classified:** rule (`honey-spreads`)
- **Size:** None
- **Price:** 2.49
- **Printed Price:** “2.49”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 214, top 116, right 360, bottom 161, page 2
- **Full page:** [pages/flyer169-page2-f0171445e8.jpg (flyer page 2)](pages/flyer169-page2-f0171445e8.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `dd86dbf8b5094811`
- **Raw:** `{"block_text": "= Pomelo comm\nmiel/ Pomelo\n)49 Rouge\nAmma AAT\nM ib54rg La Chine ou", "ocr_lines": ["Pomelode", "miel/Pomelo", "Rouge", "o5.49/kg", "La Chine"], "harvest": {"unit": "kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Price correct, shelf note. Honey pomelo (China) at 2.49/lb (5.49/kg) — verified. It sits in Honey, Syrups & Spreads because "pomelo de miel" names the honey-pomelo variety; the product is a fresh fruit. Text trap, recorded.

### Item 15851

![item 15851](images/item-15851.jpg)

- **Name (English):** None
- **Name (French):** Luckin Seleclionne espresso
- **Brand:** None
- **Category (English):** Drinks > Coffee
- **Category (French):** Boissons > Cafés
- **How classified:** rule (`coffee`)
- **Size:** 1kg
- **Price:** 6.97
- **Printed Price:** “6.97”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 295, top 830, right 438, bottom 922, page 2
- **Full page:** [pages/flyer169-page2-f0171445e8.jpg (flyer page 2)](pages/flyer169-page2-f0171445e8.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.77 · item_key: `090e747c93cce739`
- **Raw:** `{"block_text": "Sélectionné Luckin pas\n\nWE espresso #.\n\n} concentré de\n\n1 wm café lauices |\n| | (à La noix à.\n\nà oh de coCo/::\n\nai }. espresso) =\n\nwe Pee eet OTS", "ocr_lines": ["Luckin", "Seleclionne", "espresso", "concentrede", "cafeliquide", "(a lanoix（", "decoco/", "espresso)"], "harvest": {"size": "1kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 2. Luckin liquid espresso concentrate (coconut, 576 ml) prints 16.99 special (15.99 member); the DB had 6.97 — a yuja tea's price from the row above. Coffee is right.

### Item 15869

![item 15869](images/item-15869.jpg)

- **Name (English):** None
- **Name (French):** T&T-tartelette auxceufsala portugaise
- **Brand:** None
- **Category (English):** Bakery > Cakes
- **Category (French):** Boulangerie > Gâteaux
- **How classified:** rule (`cakes`)
- **Size:** None
- **Price:** 5.97
- **Printed Price:** “5.97”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 640, top 240, right 788, bottom 285, page 3
- **Full page:** [pages/flyer169-page3-47331c9aa9.jpg (flyer page 3)](pages/flyer169-page3-47331c9aa9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `dbe013805e35e78b`
- **Raw:** `{"block_text": "| TaTtartelettes\naux œufs à la\n7 portugaise |\nRAIN |\nIch 50gx6", "ocr_lines": ["T&T-tartelette", "auxceufsala", "portugaise", "lch"], "harvest": {"unit": "each", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. T&T Portuguese egg tarts (50 g x 6) at 5.97 — verified. Cakes is right.

### Item 15902

![item 15902](images/item-15902.jpg)

- **Name (English):** None
- **Name (French):** MAGMAG prunes sechees"
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Dried Fruits & Nuts
- **Category (French):** Fruits et légumes > Fruits séchés et noix
- **How classified:** dried-remap (`fruits`)
- **Size:** None
- **Price:** 4.50
- **Printed Price:** “4.50”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 649, top 544, right 896, bottom 601, page 4
- **Full page:** [pages/flyer169-page4-2a64ff6c6b.jpg (flyer page 4)](pages/flyer169-page4-2a64ff6c6b.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/04.webp
- **Details:** confidence: 0.96 · item_key: `7d7354bffa5500b7`
- **Conditions:** `{"alt_prices": ["3.50"]}`
- **Raw:** `{"block_text": "MAMA CIE\nprunes >\nséchées 48\nRAMAGMAG °°\nre se €", "ocr_lines": ["MAGMAG", "prunes", "sechees\"", "泰国MAGMAG"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. MAGMAG dried prunes (186 g) print 6.97 special (5.97 member); the DB had 4.50 — the Orion turtle chips' price to the right. Now 6.97. Dried Fruits & Nuts is right.

### Item 15908

![item 15908](images/item-15908.jpg)

- **Name (English):** None
- **Name (French):** Want want bonbons Threesquirrels collationkonjacepice
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 200g
- **Price:** 7.00
- **Printed Price:** “7.00”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 37, top 885, right 356, bottom 942, page 4
- **Full page:** [pages/flyer169-page4-2a64ff6c6b.jpg (flyer page 4)](pages/flyer169-page4-2a64ff6c6b.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/04.webp
- **Details:** confidence: 0.99 · item_key: `95aa6a5b207a346d`
- **Raw:** `{"block_text": "É\\ ; Lu un |\nThree squimmelss (yf Want wanionbens\ncollation}konjac épicé gélifiés Spies)\nRASE eee LUS REfENGA |\nRSR | 1) pec soon Tt}\n200g A =) 2009 EL", "ocr_lines": ["Want want bonbons", "Threesquirrels", "collationkonjacepice", "gelifiessavmixtes", "Pts"], "harvest": {"size": "200g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** DELETED — points phantom. The record merges two snacks (Three Squirrels konjac snack, Want Want NBA gummies) from the flyer's points-redemption page, where offers price in points (700 Pts / 1000 Pts); the stored 7.00 was assembled from the 700 Pts badge. No dollar price exists for this record.

### Item 15928

![item 15928](images/item-15928.jpg)

- **Name (English):** None
- **Name (French):** Gateaumousse litchi oolong osmanthus
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** 1100g
- **Price:** 44.99
- **Printed Price:** “44.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 366, top 286, right 566, bottom 339, page 6
- **Full page:** [pages/flyer169-page6-1d27e84a73.jpg (flyer page 6)](pages/flyer169-page6-1d27e84a73.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/06.webp
- **Details:** confidence: 0.97 · item_key: `fab422a418c3bb60`
- **Raw:** `{"block_text": "Gâteau mousse litchi\noolong osmanthus\nCE LE LT EP TE LE TP QU", "ocr_lines": ["Gateaumousse litchi", "oolong osmanthus"], "harvest": {"size": "1100g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Price correct, shelf note. Lychee oolong osmanthus mousse cake (1100 g) at 44.99 (4.09/100 g) — verified. It sits in Fresh Fruits on "litchi"; the product is a whole cake. Text result, recorded.

### Item 15940

![item 15940](images/item-15940.jpg)

- **Name (English):** None
- **Name (French):** coffee cafe glacelait vietnamien
- **Brand:** None
- **Category (English):** Drinks > Coffee
- **Category (French):** Boissons > Cafés
- **How classified:** rule (`coffee`)
- **Size:** None
- **Price:** 4.59
- **Printed Price:** “4.59”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 165, top 674, right 361, bottom 736, page 7
- **Full page:** [pages/flyer169-page7-ae7c8400ba.jpg (flyer page 7)](pages/flyer169-page7-ae7c8400ba.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/07.webp
- **Details:** confidence: 0.99 · item_key: `769c535317942fa5`
- **Raw:** `{"block_text": "2 com\ncoffee café}\nglacé lait\n\nÀ >,\nvietnamien!\n235mIx6", "ocr_lines": ["coffee cafe", "glacelait", "vietnamien", "235mlx6"]}`

**Item Review Analysis (Pass 1):** Correct. Highland Vietnamese iced milk coffee (235 ml x 6) at 4.59 — verified. Coffee is right.

### Item 15941

![item 15941](images/item-15941.jpg)

- **Name (English):** None
- **Name (French):** Alphonso/ ALjuice jus
- **Brand:** None
- **Category (English):** Drinks > Juice
- **Category (French):** Boissons > Jus
- **How classified:** rule (`juice`)
- **Size:** 1.75L
- **Price:** 4.29
- **Printed Price:** “4.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 513, top 838, right 730, bottom 886, page 7
- **Full page:** [pages/flyer169-page7-ae7c8400ba.jpg (flyer page 7)](pages/flyer169-page7-ae7c8400ba.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/07.webp
- **Details:** confidence: 0.98 · item_key: `faf753c1df4efe44`
- **Raw:** `{"block_text": "Alphonso/_\nAljuice jus", "ocr_lines": ["Alphonso/", "ALjuice jus"], "harvest": {"size": "1.75L", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Alphonso / AL juice (1.75 L) at 4.29 — verified. Juice is right.

### Item 15947

![item 15947](images/item-15947.jpg)

- **Name (English):** None
- **Name (French):** Huy Fong saucechili sriracha
- **Brand:** None
- **Category (English):** Pantry > Condiments
- **Category (French):** Produits du garde-manger > Condiments et garnitures
- **How classified:** rule (`condiments`)
- **Size:** 714ml
- **Price:** 0.04
- **Printed Price:** “0.04”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 746, top 362, right 916, bottom 408, page 7
- **Full page:** [pages/flyer169-page7-ae7c8400ba.jpg (flyer page 7)](pages/flyer169-page7-ae7c8400ba.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/07.webp
- **Details:** confidence: 0.95 · item_key: `c60f437b33e4af5b`
- **Conditions:** `{"alt_prices": ["1.97"]}`
- **Raw:** `{"block_text": "Huy Fong\nsauce chili\nsriracha", "ocr_lines": ["Huy Fong", "saucechili", "sriracha"], "harvest": {"size": "714ml", "via": "crop"}}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 169 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 7. Huy Fong sriracha chili sauce (714 ml) prints 4.97; the DB had 0.04. Condiments is right.

### Item 15833

![item 15833](images/item-15833.jpg)

- **Name (English):** None
- **Name (French):** Jch
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 2.66
- **Printed Price:** “2.66”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 853, top 376, right 914, bottom 412, page 1
- **Full page:** [pages/flyer169-page1-f01465bd04.jpg (flyer page 1)](pages/flyer169-page1-f01465bd04.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/01.webp
- **Details:** confidence: 0.72 · item_key: `e07e4e9d2b092f90`
- **Raw:** `{"block_text": "Eh", "ocr_lines": ["Jch"]}`

— from flyer 169 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 1. The item is a T&T Sélectionné dumpling bag (its name survived only as "Jch"); it prints 9.97. The DB had 2.66. Unclassified.

### Item 15840

![item 15840](images/item-15840.jpg)

- **Name (English):** None
- **Name (French):** SPRINGLAME LAND SHOULOER CPAULEDASO
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 26.43kg
- **Price:** 9.99
- **Printed Price:** “9.99”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 194, top 545, right 531, bottom 649, page 2
- **Full page:** [pages/flyer169-page2-f0171445e8.jpg (flyer page 2)](pages/flyer169-page2-f0171445e8.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `a0a1bf1fb39f9dc9`
- **Raw:** `{"block_text": "9 à 2 L 2 \\ \"a ‘a\nCE X mm Srainc LAME FT È 4) Z\nVE .… RER ree!\nYi, Epaulo cae ES CLR AE\nd'agneau ésa es queues. |\nud (congelee™ = =e Se we LAMS de bosuf, &\n99 sans OS) ESS =i § 99 fraiche\nsanta (frais)\n12029 COM, MRM) 26439 eRe GEM)\n=< = 7 ws Yo ltlnt coal’ ol AFA, = ET pe\nPRIX POUR LES MEMBRES", "ocr_lines": ["SPRINGLAME", "LAND SHOULOER", "CPAULEDASO", "Epaule", "anano", "dagneauesa", "SPRING LANA", "debceuf", "(congelee.", "fraiche", "sansos)", "(frais)", "b22.02/k`

— from flyer 169 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. Spring Lamb frozen boneless lamb shoulder prints 11.99/lb (26.43/kg); the DB had 9.99 — the sliced meat's rate to its left. Unclassified under its garbled name.

### Item 15844

![item 15844](images/item-15844.jpg)

- **Name (English):** None
- **Name (French):** BERETTA Bavettede snbuegneog
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 16.99
- **Printed Price:** “16.99”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 717, top 572, right 914, bottom 619, page 2
- **Full page:** [pages/flyer169-page2-f0171445e8.jpg (flyer page 2)](pages/flyer169-page2-f0171445e8.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `f38c51fe13aa0b78`
- **Raw:** `{"block_text": "MERS\n6-8 boeufangus\n200 (frais)\n\nan 77\n\n» hates ERP\n Ab3746%9 HITS A RABY)", "ocr_lines": ["BERETTA", "Bavettede", "snbuegneog", "(frais)", "/b37.46/kg"], "harvest": {"unit": "kg", "via": "crop"}}`

— from flyer 169 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Correct price. Beretta fresh Angus bavette at 16.99/lb (37.46/kg) — verified. Unclassified under its garbled name.

### Item 15854

![item 15854](images/item-15854.jpg)

- **Name (English):** None
- **Name (French):** T&Tnouilles boissonau Seleclionne
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 7.97
- **Printed Price:** “7.97”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 177, top 779, right 452, bottom 851, page 2
- **Full page:** [pages/flyer169-page2-f0171445e8.jpg (flyer page 2)](pages/flyer169-page2-f0171445e8.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.93 · item_key: `72f197386283b5fc`
- **Raw:** `{"block_text": "DS = Sia y=\nSélectionné T&T nouilles Sélectionné boisson au, ne.\nem SÉChÉCSQUS gr yujajcoréen/*=\nShandonoy oe au yuja'et fruits,\nde style CEE de la'passioni#\nve = Shanxifl g - z x RON:\nCCD MR Fo D pra aR S\n7 39 Bits meee So Bes Tips\n1.8kg/ 2kg > 1kg >\n=", "ocr_lines": ["T&Tnouilles", "boissonau", "Seleclionne", "Selectionne", "yuja coreen/", "secheesdu", "Shandong", "auyujaetfruit", "de style", "dela passion", "Shanxi", "1.8kg/2kg"], "harvest": {"unit": "each", "via": "c`

— from flyer 169 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the crop. This record merges two products (T&T Shandong/Shanxi dried noodles 1.8-2 kg, and Korean yuja tea 1 kg); the name leads with the noodles, which print 4.97 special (3.97 member). The DB had 7.97 — the tea's regular price. Now 4.97, merge recorded. Unclassified.

### Item 15858

![item 15858](images/item-15858.jpg)

- **Name (English):** None
- **Name (French):** Epinard chinois b3.70/kg Canada/Mexique
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 1.68
- **Printed Price:** “1.68”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 543, top 246, right 689, bottom 276, page 2
- **Full page:** [pages/flyer169-page2-f0171445e8.jpg (flyer page 2)](pages/flyer169-page2-f0171445e8.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/02.webp
- **Details:** confidence: 0.99 · item_key: `ecf25afbe5bae493`
- **Raw:** `{"block_text": "4 ===\n| Epinard chinois\n| 68 RER\n\n1b3704kg Canada/ Mexique", "ocr_lines": ["Epinard chinois", "b3.70/kg", "Canada/Mexique"], "harvest": {"unit": "kg", "via": "crop"}}`

— from flyer 169 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Correct. Chinese spinach (Canada/Mexico) at 1.68/lb (3.70/kg) — verified; the dual rate was resolved to the lb headline. Unclassified (the classifier gets the name with its rate text attached).

### Item 15880

![item 15880](images/item-15880.jpg)

- **Name (English):** None
- **Name (French):** T&Triza grainmoyen dequalite
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 15lb
- **Price:** 12.97
- **Printed Price:** “12.97”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 114, top 331, right 242, bottom 400, page 3
- **Full page:** [pages/flyer169-page3-47331c9aa9.jpg (flyer page 3)](pages/flyer169-page3-47331c9aa9.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/03.webp
- **Details:** confidence: 0.99 · item_key: `9d23cd9d9c1ab5ed`
- **Raw:** `{"block_text": "TaTriza a.\ngrain moyen”\nde qualité ag -\nsupericure ns\ndes E-U!\n\nRES UN", "ocr_lines": ["T&Triza", "grainmoyen", "dequalite", "superieure", "desE.-U."], "harvest": {"size": "15lb", "via": "crop"}}`

— from flyer 169 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Correct. T&T superior medium-grain rice (USA, 15 lb) at 12.97 — verified. Unclassified under its garbled name.

### Item 15914

![item 15914](images/item-15914.jpg)

- **Name (English):** None
- **Name (French):** Cyprines (surgelees)
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 10.57
- **Printed Price:** “10.57”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 353, top 282, right 599, bottom 316, page 4
- **Full page:** [pages/flyer169-page4-2a64ff6c6b.jpg (flyer page 4)](pages/flyer169-page4-2a64ff6c6b.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/04.webp
- **Details:** confidence: 0.97 · item_key: `a9bda8772a7a6d2e`
- **Raw:** `{"block_text": "Cyprines =\n| (surgelées) °", "ocr_lines": ["Cyprines", "(surgelees)"]}`

— from flyer 169 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 4. Frozen carp (400 g) prints 7.98 special (6.98 member); the DB had 10.57 — the assorted tempura platter's special price beside it. Unclassified.

### Item 15922

![item 15922](images/item-15922.jpg)

- **Name (English):** None
- **Name (French):** Valeur傅
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 639, top 907, right 739, bottom 938, page 5
- **Full page:** [pages/flyer169-page5-33cfeb1a71.jpg (flyer page 5)](pages/flyer169-page5-33cfeb1a71.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/05.webp
- **Details:** confidence: 0.99 · item_key: `3f1c13b0e7a65562`
- **Raw:** `{"block_text": "Valeur za {", "ocr_lines": ["Valeur傅"]}`

— from flyer 169 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Kept as-is. The record's name is only "Valeur" with a printed 6.99/ch; the product can't be identified from the surviving crop. Unclassified.

### Item 15927

![item 15927](images/item-15927.jpg)

- **Name (English):** None
- **Name (French):** Painthelaitthai fromagesalecroustillante/ PainTiramisucroutecroustillante
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 90g
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 670, top 496, right 930, bottom 549, page 6
- **Full page:** [pages/flyer169-page6-1d27e84a73.jpg (flyer page 6)](pages/flyer169-page6-1d27e84a73.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/06.webp
- **Details:** confidence: 0.99 · item_key: `21f57ef5908de447`
- **Raw:** `{"block_text": "Pain thé lait thaï\nfromage salé croustillante /\nPain Tiramisu croûte croustillante", "ocr_lines": ["Painthelaitthai", "fromagesalecroustillante/", "PainTiramisucroutecroustillante"], "harvest": {"size": "90g", "via": "crop"}}`

— from flyer 169 (valid 2026-10-16 → 2026-10-22)

**Item Review Analysis (Pass 1):** Correct. Thai milk-tea salted-cheese bread / tiramisu crusted bread (90 g) at 3.99 (4.43/100 g) — verified. Unclassified under its merged name.

### Item 15934

![item 15934](images/item-15934.jpg)

- **Name (English):** None
- **Name (French):** Painmarbretheau laitthai
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 5.29
- **Printed Price:** “5.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-16 → 2026-10-22
- **bbox:** left 391, top 522, right 605, bottom 543, page 6
- **Full page:** [pages/flyer169-page6-1d27e84a73.jpg (flyer page 6)](pages/flyer169-page6-1d27e84a73.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-supermarche-tt-du-16-au-22-octobre-2026/06.webp
- **Details:** confidence: 0.99 · item_key: `d34925fc29403e15`
- **Raw:** `{"block_text": "Pain marbre the au lait thaï", "ocr_lines": ["Painmarbretheau laitthai"]}`

**Item Review Analysis (Pass 1):** Correct. Thai milk-tea marble bread at 5.29 — verified. Unclassified.
