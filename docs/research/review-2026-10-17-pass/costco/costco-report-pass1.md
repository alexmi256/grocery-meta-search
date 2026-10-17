# Costco Wholesale — full product report

Store slug: `costco`. Generated from `data/grocery.db`. A sampled subset of 20 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 173, valid 2026-09-28 → 2026-10-25) — Costco's warehouse savings booklet runs four weeks; it is the current edition and the only one in the DB. The sample shows 10 classified + 10 unclassified of 69 items.
- **How this source reads:** Costco items are parsed from the booklet pages by the prix_line layout (the price row anchors each product; the name is stitched from the product LABEL's OCR text). The booklet also prints a clean title under each photo ("Craquelins à la farine d'amande… Simple Mills, 482 g"), which the parser does not use — the label text is what carries sizes, at the cost of garbled, word-glued names. That trade-off is this source's standing character and most findings below trace to it.
- **Issues found:** four classified items were in wrong departments, each with an adjudicated ground-truth verdict: cookie-butter (speculoos) mousse as Dairy > Butter & Spreads (verdict: Pantry > Spreads), Liquid I.V. electrolyte sachets as Pantry > Baking Essentials (verdict: Drinks > Sports & Energy), ginger wellness shots as Fresh Fruits (verdict: Drinks > Juice), and an all-in-one nutritional shake as Candy & Chocolate via the word "fudge" (verdict: Health & Beauty > Pharmacy — not grocery at all). One unclassified item (16390) is almond-flour crackers whose label stitch lost the word "craquelins", leaving the salt line to classify it as Spices. One genuine grocery item sits unclassified behind a fully glued name (16380, Lotus Biscoff cookies).
- **Patterns:** warehouse-booklet products are disproportionately supplements, sports drinks and imported specialties — exactly the vocabulary edges of a grocery classifier. Every fix here is a product-word phrase or a narrow guard; the glued-name misses are the documented run-together OCR limit (phrase matching needs token boundaries), re-confirmed on 16380: the new "biscoff" phrase classifies any normally spaced Biscoff name but cannot reach inside "BiscuitsBiscoffdeLotus".
- **Fixes applied this pass:** spreads vocabulary (speculoos, cookie butter, beurre de biscuit), cookies vocabulary (biscoff), sports-drinks vocabulary (hydration multiplier, liquid i v), a wellness-shots guard (Fresh Fruits + "shots" → Drinks > Juice) and an all-in-one-shake guard (Candy + shake/tout-en-un → Health & Beauty > Pharmacy). Ground truth 12376 → 12382 items, 8264 → 8269 signatures. Data: 4 items flipped to their verdict categories; the shake was purged as non-grocery.

## Flyer 173 — valid 2026-09-28 → 2026-10-25 (10 classified items, 10 unclassified)

Source ref: `circulaire-costco-du-28-septembre-au-25-octobre-2026` · fetched 2026-10-17T15:35:58.670Z

### Item 16378

![item 16378](images/item-16378.jpg)

- **Name (English):** None
- **Name (French):** CHOCOLAT CHAUD SimplementchocolatchaudCarnationde
- **Brand:** None
- **Category (English):** Drinks > Tea & Hot Drinks
- **Category (French):** Boissons > Thés et boissons chaudes
- **How classified:** rule (`tea-hot-drinks`)
- **Size:** None
- **Price:** 12.99
- **Printed Price:** “12,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 759, top 365, right 991, bottom 637, page 3
- **Full page:** [pages/flyer173-page3-5e2dbe9df5.jpg (flyer page 3)](pages/flyer173-page3-5e2dbe9df5.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/03.webp
- **Details:** confidence: 0.85 · item_key: `837d5ce7438d4641`
- **Raw:** `{"strategy": "prix_line", "price_derived": false}`

**Item Review Analysis (Pass 1):** Correct in substance. Carnation hot chocolate at 12.99 — Tea & Hot Drinks is the taxonomy's hot-drinks shelf. The name is label-OCR stitch ("Simplement chocolat chaud Carnation de…" glued) — garbled but searchable; size missing (the label text read carries none).

### Item 16379

![item 16379](images/item-16379.jpg)

- **Name (English):** None
- **Name (French):** COOKIE BUTTER MOUSSE MOUSSEAUSPECULOOS 6x76g2.58o=NET454g11
- **Brand:** None
- **Category (English):** Dairy & Eggs > Butter & Spreads
- **Category (French):** Produits laitiers et œufs > Beurre et tartinades
- **How classified:** rule (`butter`)
- **Size:** 6×76g
- **Price:** 10.99
- **Printed Price:** “10,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 260, top 713, right 491, bottom 957, page 3
- **Full page:** [pages/flyer173-page3-5e2dbe9df5.jpg (flyer page 3)](pages/flyer173-page3-5e2dbe9df5.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/03.webp
- **Details:** confidence: 0.85 · item_key: `92ca6c37db5164f6`
- **Raw:** `{"strategy": "prix_line", "price_derived": false, "harvest": {"size": "6×76g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Fixed this pass. Speculoos cookie-butter mousse cups (6 x 76 g) at 10.99 — the word "butter" had shelved a dessert spread product in Dairy > Butter & Spreads; the ground-truth verdict is Pantry > Honey, Syrups & Spreads. "speculoos"/"cookie butter" phrases added to the spreads rule; reclassified.

### Item 16385

![item 16385](images/item-16385.jpg)

- **Name (English):** None
- **Name (French):** Legumes-racinesgrillesalaflamme
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 14.99
- **Printed Price:** “14,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 510, top 199, right 739, bottom 454, page 4
- **Full page:** [pages/flyer173-page4-c5ec7dc04c.jpg (flyer page 4)](pages/flyer173-page4-c5ec7dc04c.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/04.webp
- **Details:** confidence: 0.85 · item_key: `321aba2dcb22a818`
- **Raw:** `{"strategy": "prix_line", "price_derived": false}`

**Item Review Analysis (Pass 1):** Accepted as-is. Puravida flame-grilled root vegetables, 1.8 kg bag, at 14.99 (18.99 − 4.00) — the crop verifies the price and product. Stored as Fresh Vegetables; the bag is a freezer product, but nothing readable in the name or label says "surgelé", and the frozen remap needs that marker — a text-only limit, recorded. Size 1.8 kg is printed in the booklet text but not in the label-derived name, so it is not stored.

### Item 16389

![item 16389](images/item-16389.jpg)

- **Name (English):** None
- **Name (French):** Butter Chicken PREMUMCKINSAUCERIMESAUCEDECUSSO Poulet au beurre
- **Brand:** None
- **Category (English):** Prepared Meals > Entrees & Appetizers
- **Category (French):** Repas préparés > Plats principaux et apéritifs
- **How classified:** rule (`specific-prepared-chicken`)
- **Size:** None
- **Price:** 7.99
- **Printed Price:** “7,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 510, top 576, right 741, bottom 925, page 4
- **Full page:** [pages/flyer173-page4-c5ec7dc04c.jpg (flyer page 4)](pages/flyer173-page4-c5ec7dc04c.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/04.webp
- **Details:** confidence: 0.70 · item_key: `1e65c51fd58dd9d8`
- **Raw:** `{"strategy": "prix_line", "price_derived": true}`

**Item Review Analysis (Pass 1):** Correct. Butter chicken with sauce at 7.99 — Prepared Meals > Entrees & Appetizers is right; the name is label stitch with OCR garble ("PREMUMCKINSAUCE…"), price verified in the booklet row.

### Item 16390

![item 16390](images/item-16390.jpg)

- **Name (English):** None
- **Name (French):** Riendartifciel -FARINED'AMANDE Sel demer finement moulu
- **Brand:** None
- **Category (English):** Pantry > Spices & Seasonings
- **Category (French):** Produits du garde-manger > Épices et assaisonnements
- **How classified:** rule (`spices`)
- **Size:** 482g
- **Price:** 9.99
- **Printed Price:** “9,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 760, top 522, right 991, bottom 927, page 4
- **Full page:** [pages/flyer173-page4-c5ec7dc04c.jpg (flyer page 4)](pages/flyer173-page4-c5ec7dc04c.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/04.webp
- **Details:** confidence: 0.70 · item_key: `af0f8079fa7d745e`
- **Raw:** `{"strategy": "prix_line", "price_derived": true, "harvest": {"size": "482g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Wrong category from a headless name — documented, not forced. The crop shows the product is Simple Mills almond-flour CRACKERS with sea salt (482 g, 9.99 = 12.99 − 3.00), but the label stitch dropped the word "Craquelins", leaving "farine d'amande / sel de mer" to classify it as Spices & Seasonings. No safe phrase fixes a name whose product noun is absent; the durable fix would be parsing the booklet's clean title line instead of the label — noted as a possible future improvement for this source, not built here.

### Item 16391

![item 16391](images/item-16391.jpg)

- **Name (English):** None
- **Name (French):** Croustilles nature Ruffles
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Chips & Snacks
- **Category (French):** Grignotines, croustilles et friandises > Croustilles et grignotines
- **How classified:** rule (`specific-snacks`)
- **Size:** 612g
- **Price:** 5.99
- **Printed Price:** “5,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 260, top 24, right 492, bottom 290, page 5
- **Full page:** [pages/flyer173-page5-67e78ddb10.jpg (flyer page 5)](pages/flyer173-page5-67e78ddb10.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/05.webp
- **Details:** confidence: 0.85 · item_key: `b0743cf71ffc50df`
- **Raw:** `{"strategy": "prix_line", "price_derived": false, "harvest": {"size": "612g", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Ruffles plain chips, 612 g at 5.99 — name (clean this time), size, price and Chips & Snacks all verified.

### Item 16392

![item 16392](images/item-16392.jpg)

- **Name (English):** None
- **Name (French):** Gruaurapide Quaker
- **Brand:** None
- **Category (English):** Pantry > Cereal & Breakfast
- **Category (French):** Produits du garde-manger > Céréales et petits-déjeuners
- **How classified:** rule (`cereal-breakfast`)
- **Size:** 5,16 kg
- **Price:** 8.99
- **Printed Price:** “8,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 9, top 66, right 242, bottom 299, page 5
- **Full page:** [pages/flyer173-page5-67e78ddb10.jpg (flyer page 5)](pages/flyer173-page5-67e78ddb10.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/05.webp
- **Details:** confidence: 0.85 · item_key: `f18959366ada8bc7`
- **Raw:** `{"strategy": "prix_line", "price_derived": false, "harvest": {"size": "5,16 kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Correct. Quaker quick oats, 5.16 kg at 8.99 — Cereal & Breakfast; name is glued label text ("Gruau rapide Quaker") but values are right.

### Item 16406

![item 16406](images/item-16406.jpg)

- **Name (English):** None
- **Name (French):** SHOTSWEBIEN-ETRE INGERE-CITRON-CAOTTE ANSIEPITOUEC30
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 14.99
- **Printed Price:** “14,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 260, top 722, right 491, bottom 971, page 6
- **Full page:** [pages/flyer173-page6-65e3cb24fa.jpg (flyer page 6)](pages/flyer173-page6-65e3cb24fa.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/06.webp
- **Details:** confidence: 0.85 · item_key: `8fbfb9ec32ece69f`
- **Raw:** `{"strategy": "prix_line", "price_derived": false}`

**Item Review Analysis (Pass 1):** Fixed this pass. Bottled ginger-lemon-carrot wellness shots (30) at 14.99 — Fresh Fruits via the produce words; the ground-truth verdict for this signature is Drinks > Juice. A scoped guard (Fresh Fruits winner + "shots") now remaps it; reclassified.

### Item 16410

![item 16410](images/item-16410.jpg)

- **Name (English):** None
- **Name (French):** All-in-One Shake Boisson tout-en-un Boisson tout-en-unFudge au chocolat de
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 2kg
- **Price:** 63.99
- **Printed Price:** “63,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 759, top 44, right 991, bottom 300, page 7
- **Full page:** [pages/flyer173-page7-a97a238b21.jpg (flyer page 7)](pages/flyer173-page7-a97a238b21.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/07.webp
- **Details:** confidence: 0.85 · item_key: `05020f01fb6c65b3`
- **Raw:** `{"strategy": "prix_line", "price_derived": false, "harvest": {"size": "2kg", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Fixed this pass (removed from grocery). Good Protein all-in-one shake, chocolate fudge, 2 kg at 63.99 — "fudge au chocolat" had shelved a nutritional shake powder in Candy & Chocolate. The verdict is Health & Beauty > Pharmacy; a guard (candy winner + shake + tout-en-un/all-in-one) routes it there, and it was purged as non-grocery.

### Item 16412

![item 16412](images/item-16412.jpg)

- **Name (English):** None
- **Name (French):** HYDRATION MULTIPLIER' SUGAR-FREE/SANS SUCRE ElectrolytesHydrationMultiplierdeLiquid
- **Brand:** None
- **Category (English):** Pantry > Baking Essentials
- **Category (French):** Produits du garde-manger > Essentiels de cuisson
- **How classified:** rule (`baking`)
- **Size:** None
- **Price:** 29.99
- **Printed Price:** “29,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 260, top 393, right 491, bottom 640, page 7
- **Full page:** [pages/flyer173-page7-a97a238b21.jpg (flyer page 7)](pages/flyer173-page7-a97a238b21.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/07.webp
- **Details:** confidence: 0.85 · item_key: `10326a2944ea7d6a`
- **Raw:** `{"strategy": "prix_line", "price_derived": false}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 173 (valid 2026-09-28 → 2026-10-25)

**Item Review Analysis (Pass 1):** Fixed this pass. Liquid I.V. Hydration Multiplier electrolyte sachets (30, sugar-free) at 29.99 (39.99 − 10.00) — the crop verifies product and price. It had classified as Pantry > Baking Essentials; "hydration multiplier"/"liquid i v" phrases in the sports-drinks rule now put it in Drinks > Sports & Energy, per the verdict.

### Item 16356

![item 16356](images/item-16356.jpg)

- **Name (English):** None
- **Name (French):** Televiseur4KMiniDELM72Hde85pode
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 1094.99
- **Printed Price:** “1094,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 260, top 162, right 490, bottom 388, page 1
- **Full page:** [pages/flyer173-page1-c72ac33fa6.jpg (flyer page 1)](pages/flyer173-page1-c72ac33fa6.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/01.webp
- **Details:** confidence: 0.85 · item_key: `0705f2ed90acad05`
- **Raw:** `{"strategy": "prix_line", "price_derived": false}`

— from flyer 173 (valid 2026-09-28 → 2026-10-25)

**Item Review Analysis (Pass 1):** Correctly Unclassified, kept: a 4K TV at 1,094.99 — warehouse merchandise outside the grocery vocabulary.

### Item 16363

![item 16363](images/item-16363.jpg)

- **Name (English):** None
- **Name (French):** PlancherflottantstratifieSuttonavec sous-couchepreassemblee fabrique au Canada
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 24.99
- **Printed Price:** “24,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 760, top 862, right 990, bottom 974, page 1
- **Full page:** [pages/flyer173-page1-c72ac33fa6.jpg (flyer page 1)](pages/flyer173-page1-c72ac33fa6.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/01.webp
- **Details:** confidence: 0.85 · item_key: `04425509aaa72bfe`
- **Raw:** `{"strategy": "prix_line", "price_derived": false}`

— from flyer 173 (valid 2026-09-28 → 2026-10-25)

**Item Review Analysis (Pass 1):** Correctly Unclassified, kept: Sutton laminate flooring at 24.99 — merchandise.

### Item 16364

![item 16364](images/item-16364.jpg)

- **Name (English):** None
- **Name (French):** Nettoyeurhumide Clean+Wash Hygiene
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 499.99
- **Printed Price:** “499,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 10, top 170, right 241, bottom 307, page 2
- **Full page:** [pages/flyer173-page2-b60e561441.jpg (flyer page 2)](pages/flyer173-page2-b60e561441.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/02.webp
- **Details:** confidence: 0.85 · item_key: `238b351a92fbe101`
- **Raw:** `{"strategy": "prix_line", "price_derived": false}`

— from flyer 173 (valid 2026-09-28 → 2026-10-25)

**Item Review Analysis (Pass 1):** Correctly Unclassified, kept: a Clean+Wash wet cleaner appliance at 499.99 — merchandise.

### Item 16380

![item 16380](images/item-16380.jpg)

- **Name (English):** None
- **Name (French):** BiscuitsBiscoffdeLotus
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 8.99
- **Printed Price:** “8,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** kilogram
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 10, top 711, right 242, bottom 970, page 3
- **Full page:** [pages/flyer173-page3-5e2dbe9df5.jpg (flyer page 3)](pages/flyer173-page3-5e2dbe9df5.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/03.webp
- **Details:** confidence: 0.85 · item_key: `33d0bb637d31dcb6`
- **Raw:** `{"strategy": "prix_line", "price_derived": false, "harvest": {"unit": "kg", "via": "crop"}}`

— from flyer 173 (valid 2026-09-28 → 2026-10-25)

**Item Review Analysis (Pass 1):** Genuine grocery stuck unclassified: Lotus Biscoff cookies at 8.99, behind the fully glued OCR name "BiscuitsBiscoffdeLotus" — phrase matching needs token boundaries, so even the new "biscoff" phrase cannot reach it. The documented run-together limit; kept for review.

### Item 16384

![item 16384](images/item-16384.jpg)

- **Name (English):** None
- **Name (French):** Patesimperiaux auporcMinh Nd'article1210029
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 9.99
- **Printed Price:** “9,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 261, top 196, right 490, bottom 454, page 4
- **Full page:** [pages/flyer173-page4-c5ec7dc04c.jpg (flyer page 4)](pages/flyer173-page4-c5ec7dc04c.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/04.webp
- **Details:** confidence: 0.85 · item_key: `789e1fc57232d123`
- **Raw:** `{"strategy": "prix_line", "price_derived": false}`

— from flyer 173 (valid 2026-09-28 → 2026-10-25)

**Item Review Analysis (Pass 1):** Unclassified on garble: Minh pork spring rolls ("Pates imperiaux au porc" — pâtés impériaux with the article number stitched in) at 9.99. The mangled first word defeats the prepared/frozen phrases. Kept for review.

### Item 16396

![item 16396](images/item-16396.jpg)

- **Name (English):** None
- **Name (French):** Alimentstaxable CRISPYICROUSTILLANTES 15x40gBARS/BARRESNET640g
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 640g
- **Price:** 14.99
- **Printed Price:** “14,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 260, top 289, right 492, bottom 640, page 5
- **Full page:** [pages/flyer173-page5-67e78ddb10.jpg (flyer page 5)](pages/flyer173-page5-67e78ddb10.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/05.webp
- **Details:** confidence: 0.85 · item_key: `d328b4427852fc93`
- **Raw:** `{"strategy": "prix_line", "price_derived": false}`

— from flyer 173 (valid 2026-09-28 → 2026-10-25)

**Item Review Analysis (Pass 1):** Unclassified: crispy snack bars (15 x 40 g, stored size 640 g is inconsistent with 15 x 40 g = 600 g — the size stitch picked up a neighbouring number) at 14.99. Name too garbled ("Aliments taxable CRISPY…") for the bar rules, which are deliberately guarded after round-2 collateral damage. Kept for review; the size is suspect.

### Item 16398

![item 16398](images/item-16398.jpg)

- **Name (English):** None
- **Name (French):** Detergentalessive liquide HEOriginal de
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 17.49
- **Printed Price:** “17,49 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 509, top 748, right 741, bottom 970, page 5
- **Full page:** [pages/flyer173-page5-67e78ddb10.jpg (flyer page 5)](pages/flyer173-page5-67e78ddb10.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/05.webp
- **Details:** confidence: 0.85 · item_key: `cef9434409968a48`
- **Raw:** `{"strategy": "prix_line", "price_derived": false}`

— from flyer 173 (valid 2026-09-28 → 2026-10-25)

**Item Review Analysis (Pass 1):** Unclassified: liquid laundry detergent (HE, "Detergent a lessive" glued) at 17.49 — a household product the glued name keeps out of the cleaning rules; either way it is not grocery. Kept for review.

### Item 16416

![item 16416](images/item-16416.jpg)

- **Name (English):** None
- **Name (French):** RIFILLIRCHARGE REFILL|RECHARGE Savonliquidepourlesmainsalaloes
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 2×2,36L
- **Price:** 11.49
- **Printed Price:** “11,49 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 10, top 82, right 241, bottom 310, page 8
- **Full page:** [pages/flyer173-page8-62f0e335e3.jpg (flyer page 8)](pages/flyer173-page8-62f0e335e3.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/08.webp
- **Details:** confidence: 0.85 · item_key: `07fbdeb6b961ab58`
- **Raw:** `{"strategy": "prix_line", "price_derived": false, "harvest": {"size": "2×2,36L", "via": "crop"}}`

— from flyer 173 (valid 2026-09-28 → 2026-10-25)

**Item Review Analysis (Pass 1):** Unclassified: liquid hand-soap refill (2 x 2.36 L stored) at 11.49 — personal-care product behind a glued bilingual name. Not grocery; kept for review.

### Item 16419

![item 16419](images/item-16419.jpg)

- **Name (English):** None
- **Name (French):** 18CARRIDGE/CARTOUCHES1RAZOR/ASOIR RasoirFusion5ProGlidedeGillette avec18
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 55.99
- **Printed Price:** “55,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 10, top 359, right 241, bottom 640, page 8
- **Full page:** [pages/flyer173-page8-62f0e335e3.jpg (flyer page 8)](pages/flyer173-page8-62f0e335e3.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/08.webp
- **Details:** confidence: 0.85 · item_key: `75816b357e613b25`
- **Raw:** `{"strategy": "prix_line", "price_derived": false}`

— from flyer 173 (valid 2026-09-28 → 2026-10-25)

**Item Review Analysis (Pass 1):** Correctly Unclassified, kept: Gillette Fusion5 razor cartridges (18) at 55.99 — merchandise.

### Item 16423

![item 16423](images/item-16423.jpg)

- **Name (English):** None
- **Name (French):** 10Bilion/milliards 14ENOESTRAINS/ Pournesanteintestinle
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** 150capsules
- **Price:** 25.99
- **Printed Price:** “25,99 $”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-09-28 → 2026-10-25
- **bbox:** left 10, top 705, right 241, bottom 969, page 8
- **Full page:** [pages/flyer173-page8-62f0e335e3.jpg (flyer page 8)](pages/flyer173-page8-62f0e335e3.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-costco-du-28-septembre-au-25-octobre-2026/08.webp
- **Details:** confidence: 0.85 · item_key: `49499c015730c569`
- **Raw:** `{"strategy": "prix_line", "price_derived": false, "harvest": {"size": "150capsules", "via": "crop"}}`

**Item Review Analysis (Pass 1):** Unclassified: a probiotic (10 billion, 150 capsules, gut health) at 25.99 — the label stitch is too garbled to carry the word "probiotique" ("14ENOESTRAINS"…), so the vitamins rule cannot see it. A supplement in substance; kept for review.
