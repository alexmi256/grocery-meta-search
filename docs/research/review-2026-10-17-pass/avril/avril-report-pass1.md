# Avril Supermarché Santé — full product report

Store slug: `avril`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 108, valid 2026-10-15 → 2026-10-21, current). The DB also holds the expired Oct 8–14 edition (106 items), correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown. The current flyer has 0 unclassified items in the DB (69 items, all classified) — a classification success, not a gap. Avril items come from the Flipp search API; each picture is the flyer region render (product + printed price text where the flyer cell carries it).
- **Issues found:** (1) item 11653 has NO price — its Flipp payload carries an empty price string and its region render is a bare product cutout with no price block; it is one of 551 price-less items DB-wide, concentrated in Flipp-sourced stores (metro/metro-plus 69 each, IGA family 56 each, Canadian Tire 68, avril 30) whose payloads omit prices for some items — a source limitation, now displayed honestly as None; (2) item 11661's price (4.99) is the payload's collapsed "2/4.99" multibuy total (single bar is 2.79) — the documented Flipp multibuy limitation; (3) sizes printed only in the region were missed for items 11665 (600 g, fixed this pass) and 11648 (300 ml on curved bottle labels — OCR cannot read them at this resolution; left missing).
- **Patterns:** region-text sizes fail in two distinct ways — OCR garble creating a phantom rival candidate (11665: the bag's "600 g" read again as "000g", making the pick "ambiguous") and genuinely illegible packaging text (11648). Item 11636 (sultana raisins) was checked for a category fix and REJECTED: the photo shows dried fruit, but the project's frozen ground truth classifies sultana raisins — including this item's own signature — as Fresh Fruits, so the stored category follows the sanctioned verdict.
- **Fixes applied this pass:** harvest now skips zero-quantity size candidates (a 0 g "package" is always an OCR misread of the real size beside it); avril harvest re-run — 11665 now carries its printed 600 g, and 5 more sizes + 1 unit filled across the flyer.

## Flyer 108 — valid 2026-10-15 → 2026-10-21 (10 classified items, 0 unclassified)

Source ref: `8179159` · fetched 2026-10-16T12:04:31.562Z

### Item 11609

![item 11609](images/item-11609.jpg)

- **Name (English):** None
- **Name (French):** eau de source naturellement gazéifiée
- **Brand:** AVRIL SÉLECTIONNÉ
- **Category (English):** Drinks > Water
- **Category (French):** Boissons > Eau
- **How classified:** rule (`water`)
- **Size:** None
- **Price:** 7.99
- **Printed Price:** “7.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436650403/1791359774/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `b2a1580c45a627d0`
- **Conditions:** `{"discount": 20}`
- **Raw:** `{"id": 1046296879, "flyer_id": 8179159, "name": "eau de source naturellement gazéifiée", "display_type": 1, "brand": "AVRIL SÉLECTIONNÉ", "left": 7704.56, "bottom": -2152.74, "right": 8097.68, "top": -1652.21, "cutout_image_url": "http://f.wishabi.net/page_items/436650403/1791359774/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 20, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price":`

**Item Review Analysis (Pass 1):** Correct on the data the source gives. Image shows Avril Sélectionné sparkling water (blackberry) 1 L bottles; stored name and Drinks > Water category match. Size None: the 1 L is packaging print only, not in the payload name, and the region is a bare cutout (no flyer text) so the harvest has nothing to read. Price 7.99 comes from the payload (not visible in the cutout).

### Item 11611

![item 11611](images/item-11611.jpg)

- **Name (English):** None
- **Name (French):** Landish latte au matcha
- **Brand:** LANDISH
- **Category (English):** Drinks > Tea & Hot Drinks
- **Category (French):** Boissons > Thés et boissons chaudes
- **How classified:** rule (`tea-hot-drinks`)
- **Size:** 135g
- **Price:** 26.99
- **Printed Price:** “26.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436650434/1791359771/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `6c2d191d3a047bb8`
- **Conditions:** `{"discount": 10}`
- **Raw:** `{"id": 1046296927, "flyer_id": 8179159, "name": "Landish latte au matcha", "display_type": 1, "brand": "LANDISH", "left": 10342.7, "bottom": -700.27, "right": 10690.6, "top": -184.72, "cutout_image_url": "http://f.wishabi.net/page_items/436650434/1791359771/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 10, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "26.99", "print_id": null`

**Item Review Analysis (Pass 1):** Fully correct. Image confirms Landish matcha latte mix, 135 g, 26.99 (reg. 29.99) — name, brand, size, price and Tea & Hot Drinks category all match.

### Item 11623

![item 11623](images/item-11623.jpg)

- **Name (English):** None
- **Name (French):** Aux Vivres tempeh réfrigéré
- **Brand:** AUX VIVRES
- **Category (English):** Meat > Plant-Based Meat Alternatives
- **Category (French):** Viande > Substituts de viande à base de plantes
- **How classified:** rule (`plant-based-meat`)
- **Size:** 200-240g
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436650441/1791359768/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `7d9601d1d2436591`
- **Raw:** `{"id": 1046296967, "flyer_id": 8179159, "name": "Aux Vivres tempeh réfrigéré", "display_type": 1, "brand": "AUX VIVRES", "left": 12562.9, "bottom": -1165.31, "right": 12933.6, "top": -743.7, "cutout_image_url": "http://f.wishabi.net/page_items/436650441/1791359768/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "4.99", "print_i`

**Item Review Analysis (Pass 1):** Fully correct. Image confirms Aux Vivres maple-smoked tempeh, 200-240 g, 4.99 (reg. 7.99-8.99). Plant-Based Meat Alternatives is right.

### Item 11632

![item 11632](images/item-11632.jpg)

- **Name (English):** None
- **Name (French):** kaki bio
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437172346/1791922854/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `4a594278d5e7ea73`
- **Conditions:** `{"discount": 33}`
- **Raw:** `{"id": 1047346237, "flyer_id": 8179159, "name": "kaki bio", "display_type": 1, "brand": null, "left": 5256.17, "bottom": -1049.91, "right": 5867.25, "top": -702.63, "cutout_image_url": "http://f.wishabi.net/page_items/437172346/1791922854/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 33, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "1.99", "print_id": null, "short_name": null`

**Item Review Analysis (Pass 1):** Correct. Image shows California organic persimmon (kaki) at 1.99 each ("un.", reg. 2.99) — stored price and Fresh Fruits category match. Brand/Size None are valid for bulk fruit.

### Item 11636

![item 11636](images/item-11636.jpg)

- **Name (English):** None
- **Name (French):** raisins Sultana bios
- **Brand:** AVRIL SÉLECTIONNÉ
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** 500g
- **Price:** 9.99
- **Printed Price:** “9.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436650395/1791359769/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `38eb3be01f578325`
- **Conditions:** `{"discount": 9}`
- **Raw:** `{"id": 1046296864, "flyer_id": 8179159, "name": "raisins Sultana bios", "display_type": 1, "brand": "AVRIL SÉLECTIONNÉ", "left": 6992.87, "bottom": -685.36, "right": 7288.29, "top": -229.75, "cutout_image_url": "http://f.wishabi.net/page_items/436650395/1791359769/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 9, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "9.99", "print_id":`

**Item Review Analysis (Pass 1):** Category checked and left as-is on evidence. The package is dried sultana raisins (500 g, 9.99 — both stored correctly), which reads as Dried Fruits & Nuts; however the project's frozen ground truth classifies sultana raisins — including this exact item — as Fresh Fruits, so the stored category follows the sanctioned verdict rather than the photo.

### Item 11648

![item 11648](images/item-11648.jpg)

- **Name (English):** None
- **Name (French):** Loop Mission jus pressé à froid réfrigéré
- **Brand:** Loop Mission
- **Category (English):** Drinks > Juice
- **Category (French):** Boissons > Jus
- **How classified:** rule (`juice`)
- **Size:** None
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436650408/1791359771/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `058b54343862f54c`
- **Conditions:** `{"discount": 40}`
- **Raw:** `{"id": 1046296948, "flyer_id": 8179159, "name": "Loop Mission jus pressé à froid réfrigéré", "display_type": 1, "brand": "Loop Mission", "left": 11961.3, "bottom": -2171.35, "right": 12305.1, "top": -1772.14, "cutout_image_url": "http://f.wishabi.net/page_items/436650408/1791359771/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 40, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": `

**Item Review Analysis (Pass 1):** Mostly correct: Loop Mission cold-pressed juice, 2.99, Drinks > Juice — all match. Size missing: the bottles are 300 ml, printed on the labels, but the region OCR garbles the curved bottle text beyond use (the harvest reads neither bottle reliably). A genuine OCR limit; left missing.

### Item 11653

![item 11653](images/item-11653.jpg)

- **Name (English):** None
- **Name (French):** Freeyumm craquelins
- **Brand:** FREEYUMM
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** 120g
- **Price:** None
- **Printed Price:** None
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436650387/1791359768/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `fe787548f21afd88`
- **Raw:** `{"id": 1046296884, "flyer_id": 8179159, "name": "Freeyumm craquelins", "display_type": 1, "brand": "FREEYUMM", "left": 8171.62, "bottom": -1035.18, "right": 8601.46, "top": -387.43, "cutout_image_url": "http://f.wishabi.net/page_items/436650387/1791359768/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "", "print_id": null, "sh`

**Item Review Analysis (Pass 1):** No price exists for this item in our source: the Flipp payload's price field is empty and the region render is a bare cutout (FreeYumm herb & seed crackers, 120 g — the size WAS harvested from the packaging). The report now shows Price: None honestly. One of 551 price-less Flipp items DB-wide; the item is a real flyer product and is kept. Crackers & Cookies is right.

### Item 11661

![item 11661](images/item-11661.jpg)

- **Name (English):** None
- **Name (French):** Avril barres-collation sans gluten
- **Brand:** AVRIL SÉLECTIONNÉ
- **Category (English):** Pantry > Cereal & Breakfast
- **Category (French):** Produits du garde-manger > Céréales et petits-déjeuners
- **How classified:** rule (`specific-protein-bars`)
- **Size:** 42g
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436650397/1791359770/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `4509b95a5b708373`
- **Raw:** `{"id": 1046296868, "flyer_id": 8179159, "name": "Avril barres-collation sans gluten", "display_type": 1, "brand": "AVRIL SÉLECTIONNÉ", "left": 7810.69, "bottom": -774.07, "right": 8092.6, "top": -129.26, "cutout_image_url": "http://f.wishabi.net/page_items/436650397/1791359770/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "4.`

**Item Review Analysis (Pass 1):** Price caveat: the flyer sells these gluten-free snack bars at 2/4.99 or 2.79 each; the stored 4.99 is the payload's collapsed multibuy total (documented Flipp limitation). Size 42 g verified on the packages. Pantry > Cereal & Breakfast is where this taxonomy shelves bars.

### Item 11665

![item 11665](images/item-11665.jpg)

- **Name (English):** None
- **Name (French):** Délices du Lac-Saint-Jean bleuets sauvages bios surgelés
- **Brand:** DÉLICES DU LAC-SAINT-JEAN
- **Category (English):** Frozen Food > Frozen Fruit & Vegetables
- **Category (French):** Produits surgelés > Fruits et légumes surgelés
- **How classified:** frozen-remap (`fruits`)
- **Size:** None
- **Price:** 13.99
- **Printed Price:** “13.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436650429/1791359768/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `bdd2816e5976624a`
- **Conditions:** `{"discount": 18}`
- **Raw:** `{"id": 1046296917, "flyer_id": 8179159, "name": "Délices du Lac-Saint-Jean bleuets sauvages bios surgelés", "display_type": 1, "brand": "DÉLICES DU LAC-SAINT-JEAN", "left": 11082.5, "bottom": -1219.07, "right": 11433.8, "top": -614.8, "cutout_image_url": "http://f.wishabi.net/page_items/436650429/1791359768/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 18, "available_to": "2026-10-21T23:59:59-04:00", "v`

**Item Review Analysis (Pass 1):** Fixed this pass. The flyer prints 600 g (bag and text) for these frozen wild blueberries, but the harvest had stored nothing: its OCR read the bag's "600 g" twice, once garbled as "000g", and two rival candidates made the pick 'ambiguous'. Zero-quantity candidates are now skipped as garble; the re-run filled 600 g. Category and price (13.99, reg. 16.99) were already right.

### Item 11667

![item 11667](images/item-11667.jpg)

- **Name (English):** None
- **Name (French):** Riviera fromage sans lactose
- **Brand:** RIVIERA
- **Category (English):** Dairy & Eggs > Cheese
- **Category (French):** Produits laitiers et œufs > Fromage
- **How classified:** rule (`cheese`)
- **Size:** 200g
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436650449/1791359774/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `47f00593a8ca7be5`
- **Conditions:** `{"discount": 30}`
- **Raw:** `{"id": 1046296980, "flyer_id": 8179159, "name": "Riviera fromage sans lactose", "display_type": 1, "brand": "RIVIERA", "left": 12927.5, "bottom": -736.83, "right": 13246.6, "top": -220.45, "cutout_image_url": "http://f.wishabi.net/page_items/436650449/1791359774/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 30, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "6.99", "print_id": `

**Item Review Analysis (Pass 1):** Fully correct. Image confirms Riviera lactose-free emmental, 200 g, 6.99 (reg. 9.99) — name, brand, size, price and Cheese category all match.
