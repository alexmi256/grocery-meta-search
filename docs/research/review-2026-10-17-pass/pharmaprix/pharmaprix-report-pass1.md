# Pharmaprix — full product report

Store slug: `pharmaprix`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 147, valid 2026-10-17 → 2026-10-22, 188 items). The Oct 10–16 edition expired the day before this review and is correctly excluded; two empty flyer records (24, 25) hold no items.
- **Sample counts:** 10 classified + 0 unclassified shown.
- **Issues found:** one price error — the Carnaby Sweet chocolate lollipops stored the 2/5$ total; the render prints "ou 2,89 $ ch.", corrected to 2.89 with the multibuy recorded. Two price-less items are honest: a PC Optimum spend-threshold points offer on Pepperidge Farm/Goldfish (no product price exists) and a "up to 25% off" Holista tea-tree-oil offer. Note on the Holista item: it's a personal-care product classified into Pantry > Oils & Vinegar on the words "huile de théier" — a text trap of the familiar kind, recorded, not changed. Everything else verified against its render.
- **Fixes applied this pass:** 14398 → 2.89 (multibuy recorded).

## Flyer 147 — valid 2026-10-17 → 2026-10-22 (10 classified items, 0 unclassified)

Source ref: `8186471` · fetched 2026-10-16T12:49:14.800Z

### Item 14384

![item 14384](images/item-14384.jpg)

- **Name (English):** None
- **Name (French):** HOLISTA Produits d'huile de théier
- **Brand:** HOLISTA
- **Category (English):** Pantry > Oils & Vinegar
- **Category (French):** Produits du garde-manger > Huile et vinaigre
- **How classified:** rule (`oils-vinegar`)
- **Size:** None
- **Price:** None
- **Printed Price:** None
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-17 → 2026-10-22
- **Image source URL:** http://f.wishabi.net/page_items/437025047/1791598938/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `dfbd0df00d6a0aba`
- **Conditions:** `{"discount": 25}`
- **Raw:** `{"id": 1047251537, "flyer_id": 8186471, "name": "HOLISTA Produits d'huile de théier", "display_type": 1, "brand": "HOLISTA", "left": 4314.51, "bottom": -699.59, "right": 4532.87, "top": -451.19, "cutout_image_url": "http://f.wishabi.net/page_items/437025047/1791598938/extra_large.jpg", "valid_from": "2026-10-17T00:00:00-04:00", "valid_to": "2026-10-22T23:59:59-04:00", "page_destination": null, "discount": 25, "available_to": "2026-10-22T23:59:59-04:00", "video_url": null, "price": "", "print_id"`

**Item Review Analysis (Pass 1):** Price honestly absent. Holista tea tree oil products at "jusqu'à 25% de rabais" — a percentage offer with no fixed price. Shelf note: this is a personal-care product sitting in Oils & Vinegar on "huile" — a text trap, recorded.

### Item 14398

![item 14398](images/item-14398.jpg)

- **Name (English):** None
- **Name (French):** CARNABY SWEET Suçon en chocolat belge en forme de fantôme ou citrouille
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 30g
- **Price:** 5.00
- **Printed Price:** “5.0”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-17 → 2026-10-22
- **Image source URL:** http://f.wishabi.net/page_items/437024581/1791598966/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `462dc2d5bb0f1070`
- **Raw:** `{"id": 1047255270, "flyer_id": 8186471, "name": "CARNABY SWEET Suçon en chocolat belge en forme de fantôme ou citrouille", "display_type": 1, "brand": null, "left": 8242.83, "bottom": -1008.85, "right": 8460.05, "top": -756.41, "cutout_image_url": "http://f.wishabi.net/page_items/437024581/1791598966/extra_large.jpg", "valid_from": "2026-10-17T00:00:00-04:00", "valid_to": "2026-10-22T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-22T23:59:59-04:00", "video_`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the render. Carnaby Sweet Belgian chocolate lollipops (ghost or pumpkin, 30 g) print "2/5 $ ou 2,89 $ ch."; the DB stored the 5.00 total. Now 2.89 with the multibuy recorded. Candy & Chocolate is right.

### Item 14402

![item 14402](images/item-14402.jpg)

- **Name (English):** None
- **Name (French):** PEPPERIDGE FARM Biscuits ou GOLDFISH craquelins cuits au four
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** None
- **Price:** None
- **Printed Price:** None
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-17 → 2026-10-22
- **Image source URL:** http://f.wishabi.net/page_items/437025172/1791598974/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `ae1db125baa1f758`
- **Raw:** `{"id": 1047256611, "flyer_id": 8186471, "name": "PEPPERIDGE FARM Biscuits ou GOLDFISH craquelins cuits au four", "display_type": 1, "brand": null, "left": 9409.88, "bottom": -2162.74, "right": 9567.46, "top": -1940.55, "cutout_image_url": "http://f.wishabi.net/page_items/437025172/1791598974/extra_large.jpg", "valid_from": "2026-10-17T00:00:00-04:00", "valid_to": "2026-10-22T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-22T23:59:59-04:00", "video_url": nul`

**Item Review Analysis (Pass 1):** Price honestly absent. The render is a PC Optimum points offer ("Dépensez 10$ et obtenez 4000 pts") on Pepperidge Farm cookies or Goldfish crackers — no product price is printed. Crackers & Cookies is right.

### Item 14412

![item 14412](images/item-14412.jpg)

- **Name (English):** None
- **Name (French):** NUTELLA B-READY (6), KIND HEALTHY GRAINS (5) ou Barres déjeuner (4)
- **Brand:** Nutella
- **Category (English):** Pantry > Honey, Syrups & Spreads
- **Category (French):** Produits du garde-manger > Miel, sirops et tartinades
- **How classified:** rule (`honey-spreads`)
- **Size:** None
- **Price:** 4.49
- **Printed Price:** “4.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-17 → 2026-10-22
- **Image source URL:** http://f.wishabi.net/page_items/437026031/1791598984/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `1d60fb5e60c1a220`
- **Raw:** `{"id": 1047263485, "flyer_id": 8186471, "name": "NUTELLA B-READY (6), KIND HEALTHY GRAINS (5) ou Barres déjeuner (4)", "display_type": 1, "brand": "Nutella", "left": 24523.6, "bottom": -449.89, "right": 24747.1, "top": -196.1, "cutout_image_url": "http://f.wishabi.net/page_items/437026031/1791598984/extra_large.jpg", "valid_from": "2026-10-17T00:00:00-04:00", "valid_to": "2026-10-22T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-22T23:59:59-04:00", "video_u`

**Item Review Analysis (Pass 1):** Correct. Nutella B-Ready (6), Kind Healthy Grains (5) or breakfast bars (4) at 4.49 + taxes — verified. (Shelved under Honey, Syrups & Spreads on the Nutella lead name.)

### Item 14435

![item 14435](images/item-14435.jpg)

- **Name (English):** None
- **Name (French):** BARILLA Pâtes (410 g), CLOVER LEAF huîtres ou moules fumées (85 g)
- **Brand:** None
- **Category (English):** Pantry > Pasta & Pasta Sauce
- **Category (French):** Produits du garde-manger > Pâtes et sauces
- **How classified:** rule (`specific-pasta`)
- **Size:** 410 g
- **Price:** 2.49
- **Printed Price:** “2.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-17 → 2026-10-22
- **Image source URL:** http://f.wishabi.net/page_items/437023450/1791598953/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `e3e3a517ffa9047e`
- **Raw:** `{"id": 1047253875, "flyer_id": 8186471, "name": "BARILLA Pâtes (410 g), CLOVER LEAF huîtres ou moules fumées (85 g)", "display_type": 1, "brand": null, "left": 6968.71, "bottom": -2121.02, "right": 7192.31, "top": -1818.81, "cutout_image_url": "http://f.wishabi.net/page_items/437023450/1791598953/extra_large.jpg", "valid_from": "2026-10-17T00:00:00-04:00", "valid_to": "2026-10-22T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-22T23:59:59-04:00", "video_url"`

**Item Review Analysis (Pass 1):** Correct. Barilla pasta (410 g) or Clover Leaf smoked oysters/mussels (85 g) at 2.49 — verified. Pasta & Pasta Sauce leads the combined name.

### Item 14441

![item 14441](images/item-14441.jpg)

- **Name (English):** None
- **Name (French):** LOU'S KITCHEN Rôti de bœuf braisé au jus entièrement cuit Jus (375 g) ou SCHNEIDERS PEPPERETTES (250 g - 375 g)
- **Brand:** None
- **Category (English):** Meat > Beef
- **Category (French):** Viande > Bœuf
- **How classified:** rule (`beef`)
- **Size:** 375 g
- **Price:** 10.99
- **Printed Price:** “10.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-17 → 2026-10-22
- **Image source URL:** http://f.wishabi.net/page_items/437023459/1791598958/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `09d3911b3599b40b`
- **Raw:** `{"id": 1047254121, "flyer_id": 8186471, "name": "LOU'S KITCHEN Rôti de bœuf braisé au jus entièrement cuit Jus (375 g) ou SCHNEIDERS PEPPERETTES (250 g - 375 g)", "display_type": 1, "brand": null, "left": 6971.12, "bottom": -698.88, "right": 7192.5, "top": -449.86, "cutout_image_url": "http://f.wishabi.net/page_items/437023459/1791598958/extra_large.jpg", "valid_from": "2026-10-17T00:00:00-04:00", "valid_to": "2026-10-22T23:59:59-04:00", "page_destination": null, "discount": null, "available_to"`

**Item Review Analysis (Pass 1):** Correct. Lou's Kitchen fully cooked beef pot roast au jus (375 g) or Schneiders pepperettes (250-375 g) at 10.99 — verified. Beef leads the combined name.

### Item 14442

![item 14442](images/item-14442.jpg)

- **Name (English):** None
- **Name (French):** BEN & JERRY'S Crème glacée Ice Cream
- **Brand:** Ben & Jerry's
- **Category (English):** Frozen Food > Ice Cream & Frozen Desserts
- **Category (French):** Produits surgelés > Crèmes glacées et desserts glacés
- **How classified:** rule (`ice-cream`)
- **Size:** 473mL
- **Price:** 6.50
- **Printed Price:** “6.5”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-17 → 2026-10-22
- **Image source URL:** http://f.wishabi.net/page_items/437023472/1791598965/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `a1e5cd4a77005407`
- **Raw:** `{"id": 1047254492, "flyer_id": 8186471, "name": "BEN & JERRY'S Crème glacée Ice Cream", "display_type": 1, "brand": "Ben & Jerry's", "left": 6970.27, "bottom": -449.59, "right": 7195.21, "top": -225.7, "cutout_image_url": "http://f.wishabi.net/page_items/437023472/1791598965/extra_large.jpg", "valid_from": "2026-10-17T00:00:00-04:00", "valid_to": "2026-10-22T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-22T23:59:59-04:00", "video_url": null, "price": "6.5"`

**Item Review Analysis (Pass 1):** Correct. Ben & Jerry's ice cream (473 ml) at 6.50 + taxes — verified (the 3000 pts is a buy-2 points bonus, not the price). Ice Cream & Frozen Desserts is right.

### Item 14478

![item 14478](images/item-14478.jpg)

- **Name (English):** None
- **Name (French):** RIO MARE Thon pâle entier (3 x 80 g), CLOVER LEAF ou GOLD SEAL saumon sockeye sauvage rouge du Pacifique (213 g)
- **Brand:** None
- **Category (English):** Pantry > Canned & Pickled
- **Category (French):** Produits du garde-manger > Produits en conserve et marinés
- **How classified:** rule (`specific-canned-fish`)
- **Size:** 3 x 80 g
- **Price:** 7.49
- **Printed Price:** “7.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-17 → 2026-10-22
- **Image source URL:** http://f.wishabi.net/page_items/437024207/1791598951/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `0189dd9b35db5028`
- **Raw:** `{"id": 1047252975, "flyer_id": 8186471, "name": "RIO MARE Thon pâle entier (3 x 80 g), CLOVER LEAF ou GOLD SEAL saumon sockeye sauvage rouge du Pacifique (213 g)", "display_type": 1, "brand": null, "left": 5750.25, "bottom": -1452.37, "right": 5973.26, "top": -1199.5, "cutout_image_url": "http://f.wishabi.net/page_items/437024207/1791598951/extra_large.jpg", "valid_from": "2026-10-17T00:00:00-04:00", "valid_to": "2026-10-22T23:59:59-04:00", "page_destination": null, "discount": null, "available_`

**Item Review Analysis (Pass 1):** Correct. Rio Mare solid light tuna (3 x 80 g) or Clover Leaf / Gold Seal wild red sockeye salmon (213 g) at 7.49 — verified. Canned & Pickled is right.

### Item 14570

![item 14570](images/item-14570.jpg)

- **Name (English):** None
- **Name (French):** WONDERFUL Pistaches écalées
- **Brand:** Wonderful
- **Category (English):** Fruits & Vegetables > Dried Fruits & Nuts
- **Category (French):** Fruits et légumes > Fruits séchés et noix
- **How classified:** rule (`dried-fruits-nuts`)
- **Size:** None
- **Price:** 8.99
- **Printed Price:** “8.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-17 → 2026-10-22
- **Image source URL:** http://f.wishabi.net/page_items/437026035/1791598986/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `0a60d50be23b7eee`
- **Raw:** `{"id": 1047263540, "flyer_id": 8186471, "name": "WONDERFUL Pistaches écalées", "display_type": 1, "brand": "Wonderful", "left": 24008.9, "bottom": -1808.01, "right": 24376.8, "top": -1509.1, "cutout_image_url": "http://f.wishabi.net/page_items/437026035/1791598986/extra_large.jpg", "valid_from": "2026-10-17T00:00:00-04:00", "valid_to": "2026-10-22T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-22T23:59:59-04:00", "video_url": null, "price": "8.99", "print_i`

**Item Review Analysis (Pass 1):** Correct. Wonderful shelled pistachios (155-170 g) at 8.99 + taxes — verified. Dried Fruits & Nuts is right.

### Item 14572

![item 14572](images/item-14572.jpg)

- **Name (English):** None
- **Name (French):** CRISPERS CRAQUELINS CUITS AU FOUR ou MÉLI-MÉLO MÉLANGE COLLATION
- **Brand:** CRISPERS
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** 145g
- **Price:** 2.00
- **Printed Price:** “2.0”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-17 → 2026-10-22
- **Image source URL:** http://f.wishabi.net/page_items/437026038/1791598988/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `e03b761a8f1b6d59`
- **Raw:** `{"id": 1047263577, "flyer_id": 8186471, "name": "CRISPERS CRAQUELINS CUITS AU FOUR ou MÉLI-MÉLO MÉLANGE COLLATION", "display_type": 1, "brand": "CRISPERS", "left": 23914.4, "bottom": -2428.55, "right": 24302.6, "top": -2127.93, "cutout_image_url": "http://f.wishabi.net/page_items/437026038/1791598988/extra_large.jpg", "valid_from": "2026-10-17T00:00:00-04:00", "valid_to": "2026-10-22T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-22T23:59:59-04:00", "video_`

**Item Review Analysis (Pass 1):** Correct. Crispers baked crackers or Bits & Bites snack mix (145 g) at 2.00 + taxes (limit 6; 2.75 after limit) — verified. Crackers & Cookies is right.
