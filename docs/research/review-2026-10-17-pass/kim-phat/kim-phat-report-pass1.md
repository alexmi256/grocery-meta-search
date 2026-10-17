# Kim Phat — full product report

Store slug: `kim-phat`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 125, valid 2026-10-15 → 2026-10-21, 137 items). The expired Oct 8–14 edition is correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown — classification success on the Flipp feed.
- **Issues found — the multibuy-total pattern, concentrated:** Kim Phat's flyer prices half its specials as "2 POUR X$" with the single price printed beside it, and the Flipp payload collapses each such offer to its total. Four of the ten sampled items stored the total as the unit price: seasoning packets 3.00 (real: 1.69 each, 2 for 3.00), Yum Yum chips 5.00 (real: 2.99 each, 2 for 5.00), shimeji mushrooms 1.99 (real: 1.29 each, 2 for 1.99), Samyang ramen cups 2.99 (real: 1.99 each, 2 for 2.99). All four are corrected from their renders, with the multibuy recorded in each item's conditions — the same treatment as the Jean Coutu wafers. The underlying limit is documented (the payload carries only the collapsed number; recovery needs the render, which is what this review supplies item by item). At this store the pattern is not a tail — it is the flyer's house style, so Kim Phat prices deserve a standing caveat until a render-based recovery exists.
- **Verified correct, including the eye-catching ones:** the Redpath fine sugar at 29.99 is a 20 kg bag price per sack (reg. 38) — right. The Watson Ridge wings and Crystal fondue balls are frozen products whose stored names carry no frozen marker (it lives in the description text) — a text-only limit, noted on the items.
- **Fixes applied this pass:** 4 prices corrected with multibuys recorded (13085 → 1.69, 13095 → 2.99, 13100 → 1.29, 13168 → 1.99).

## Flyer 125 — valid 2026-10-15 → 2026-10-21 (10 classified items, 0 unclassified)

Source ref: `8187928` · fetched 2026-10-16T12:18:40.560Z

### Item 13076

![item 13076](images/item-13076.jpg)

- **Name (English):** None
- **Name (French):** NOUILLES INSTANTANÉES AU TONKOTSU NISSIN
- **Brand:** Nissin
- **Category (English):** Pantry > Easy Meals & Sides
- **Category (French):** Produits du garde-manger > Mets faciles et accompagnements
- **How classified:** rule (`specific-instant-noodles`)
- **Size:** 5X100G
- **Price:** 3.29
- **Printed Price:** “3.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437236768/1791947775/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `d1ff030e7c33f468`
- **Conditions:** `{"discount": 34}`
- **Raw:** `{"id": 1047462199, "flyer_id": 8187928, "name": "NOUILLES INSTANTANÉES AU TONKOTSU NISSIN", "display_type": 1, "brand": "Nissin", "left": 1118.71, "bottom": -2346.49, "right": 1510.47, "top": -1960.17, "cutout_image_url": "http://f.wishabi.net/page_items/437236768/1791947775/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 34, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "3.29",`

**Item Review Analysis (Pass 1):** Correct. Nissin instant tonkotsu noodles (5 x 100 g) at 3.29 (reg. 4.99) — verified on the render. Easy Meals & Sides is right.

### Item 13085

![item 13085](images/item-13085.jpg)

- **Name (English):** None
- **Name (French):** ÉPICES 4 ELEPHANTS
- **Brand:** 4 ELEPHANTS
- **Category (English):** Pantry > Spices & Seasonings
- **Category (French):** Produits du garde-manger > Épices et assaisonnements
- **How classified:** rule (`spices`)
- **Size:** 85G
- **Price:** 3.00
- **Printed Price:** “3.0”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437236788/1791947774/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `dee7a66a89c084db`
- **Raw:** `{"id": 1047462244, "flyer_id": 8187928, "name": "ÉPICES 4 ELEPHANTS", "display_type": 1, "brand": "4 ELEPHANTS", "left": 2645.68, "bottom": -1420.42, "right": 2996.85, "top": -1015.3, "cutout_image_url": "http://f.wishabi.net/page_items/437236788/1791947774/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "3.0", "print_id": null`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the render. 4 Elephants seasoning packets (85 g) print "2 POUR 3$" at 1.69 each; the DB stored the 3.00 total. Now 1.69 with the multibuy recorded. Spices & Seasonings is right.

### Item 13095

![item 13095](images/item-13095.jpg)

- **Name (English):** None
- **Name (French):** CROUSTILLES YUM YUM
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Chips & Snacks
- **Category (French):** Grignotines, croustilles et friandises > Croustilles et grignotines
- **How classified:** rule (`specific-snacks`)
- **Size:** None
- **Price:** 5.00
- **Printed Price:** “5.0”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437236773/1791947764/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `c6ebad5bf789bc6a`
- **Raw:** `{"id": 1047462211, "flyer_id": 8187928, "name": "CROUSTILLES YUM YUM", "display_type": 1, "brand": null, "left": 1573.71, "bottom": -1001.53, "right": 1929.04, "top": -589.77, "cutout_image_url": "http://f.wishabi.net/page_items/437236773/1791947764/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "5.0", "print_id": null, "short`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the render. Yum Yum chips (170-200 g) print "2 POUR 5$" at 2.99 each; the DB stored 5.00. Now 2.99 with the multibuy recorded. Chips & Snacks is right.

### Item 13097

![item 13097](images/item-13097.jpg)

- **Name (English):** None
- **Name (French):** GÂTEAU AJI
- **Brand:** AJI
- **Category (English):** Bakery > Cakes
- **Category (French):** Boulangerie > Gâteaux
- **How classified:** rule (`cakes`)
- **Size:** 330G
- **Price:** 3.29
- **Printed Price:** “3.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437236784/1791947771/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `d3f0d6e2f33e6cc3`
- **Conditions:** `{"discount": 18}`
- **Raw:** `{"id": 1047462235, "flyer_id": 8187928, "name": "GÂTEAU AJI", "display_type": 1, "brand": "AJI", "left": 1831.48, "bottom": -581.8, "right": 2107.61, "top": -142.25, "cutout_image_url": "http://f.wishabi.net/page_items/437236784/1791947771/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 18, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "3.29", "print_id": null, "short_name": nul`

**Item Review Analysis (Pass 1):** Correct. Aji cakes (330 g, multiple varieties) at 3.29 (reg. 3.99) — verified. Bakery > Cakes is right.

### Item 13100

![item 13100](images/item-13100.jpg)

- **Name (English):** None
- **Name (French):** CHAMPIGNONS SHIMEJI BLANCS
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437237030/1791947769/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `972c832a8d729fb7`
- **Raw:** `{"id": 1047462270, "flyer_id": 8187928, "name": "CHAMPIGNONS SHIMEJI BLANCS", "display_type": 1, "brand": null, "left": 3070.29, "bottom": -1419.03, "right": 3575.59, "top": -959.36, "cutout_image_url": "http://f.wishabi.net/page_items/437237030/1791947769/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "1.99", "print_id": null`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the render. White shimeji mushrooms print "2 POUR 1.99" at 1.29 each; the DB stored 1.99. Now 1.29 with the multibuy recorded. Fresh Vegetables is right.

### Item 13120

![item 13120](images/item-13120.jpg)

- **Name (English):** None
- **Name (French):** BOULETTES DE VIANDE/POISSON CRYSTAL
- **Brand:** Crystal
- **Category (English):** Prepared Meals > Entrees & Appetizers
- **Category (French):** Repas préparés > Plats principaux et apéritifs
- **How classified:** rule (`entrees`)
- **Size:** None
- **Price:** 8.49
- **Printed Price:** “8.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437237057/1791947778/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `4abae337fb6ee4b9`
- **Conditions:** `{"discount": 15}`
- **Raw:** `{"id": 1047462330, "flyer_id": 8187928, "name": "BOULETTES DE VIANDE/POISSON CRYSTAL", "display_type": 1, "brand": "Crystal", "left": 5051.55, "bottom": -1637.14, "right": 5375.44, "top": -1278.53, "cutout_image_url": "http://f.wishabi.net/page_items/437237057/1791947778/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 15, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "8.49", "pr`

**Item Review Analysis (Pass 1):** Correct price. Crystal frozen meat/fish balls for fondue (410-454 g) at 8.49 each — verified. The frozen marker sits in the description, not the stored name, so no frozen remap fired; Entrees & Appetizers stands as the text-only result.

### Item 13129

![item 13129](images/item-13129.jpg)

- **Name (English):** None
- **Name (French):** AILES DE POULET SAUCÉES WATSON RIDGE
- **Brand:** Watson Ridge
- **Category (English):** Meat > Chicken & Turkey
- **Category (French):** Viande > Poulet et dinde
- **How classified:** rule (`chicken-turkey`)
- **Size:** 475G
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437237050/1791947772/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `b3a03298f3841a1f`
- **Conditions:** `{"discount": 8}`
- **Raw:** `{"id": 1047462314, "flyer_id": 8187928, "name": "AILES DE POULET SAUCÉES WATSON RIDGE", "display_type": 1, "brand": "Watson Ridge", "left": 5034.06, "bottom": -876.15, "right": 5286.2, "top": -494.49, "cutout_image_url": "http://f.wishabi.net/page_items/437237050/1791947772/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 8, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "5.99", "`

**Item Review Analysis (Pass 1):** Correct price. Watson Ridge frozen sauced chicken wings (475 g, fully cooked) at 5.99 (reg. 6.49) — verified. Classified as fresh Chicken & Turkey because "congelées" appears only in the description text — the documented text-only limit (the same product at IGA Express, whose name carries the marker, lands in Frozen).

### Item 13140

![item 13140](images/item-13140.jpg)

- **Name (English):** None
- **Name (French):** SUCRE FIN REDPATH
- **Brand:** Redpath
- **Category (English):** Pantry > Baking Essentials
- **Category (French):** Produits du garde-manger > Essentiels de cuisson
- **How classified:** rule (`baking`)
- **Size:** None
- **Price:** 29.99
- **Printed Price:** “29.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437237080/1791947776/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `8e0d6800a4812b59`
- **Conditions:** `{"discount": 21}`
- **Raw:** `{"id": 1047462384, "flyer_id": 8187928, "name": "SUCRE FIN REDPATH", "display_type": 1, "brand": "Redpath", "left": 7090.27, "bottom": -771.24, "right": 7548.37, "top": -477.84, "cutout_image_url": "http://f.wishabi.net/page_items/437237080/1791947776/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 21, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "29.99", "print_id": null, "sho`

**Item Review Analysis (Pass 1):** Correct — the eye-catching price is real: Redpath fine sugar in a 20 kg sack at 29.99 per bag (reg. 38). Baking Essentials is right.

### Item 13168

![item 13168](images/item-13168.jpg)

- **Name (English):** None
- **Name (French):** RAMEN MEPTANG (BŒUF/PALOURDE/POULET) SAMYANG
- **Brand:** Samyang
- **Category (English):** Pantry > Easy Meals & Sides
- **Category (French):** Produits du garde-manger > Mets faciles et accompagnements
- **How classified:** rule (`easy-meals`)
- **Size:** None
- **Price:** 2.99
- **Printed Price:** “2.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437237160/1791947781/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `2a656afc2b10e499`
- **Raw:** `{"id": 1047462542, "flyer_id": 8187928, "name": "RAMEN MEPTANG (BŒUF/PALOURDE/POULET) SAMYANG", "display_type": 1, "brand": "Samyang", "left": 9868.18, "bottom": -808.91, "right": 10210.6, "top": -307.48, "cutout_image_url": "http://f.wishabi.net/page_items/437237160/1791947781/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "2`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the render. Samyang MEP ramen cups (110 g) print "2 POUR 2.99" at 1.99 each; the DB stored 2.99. Now 1.99 with the multibuy recorded. Easy Meals & Sides is right.

### Item 13205

![item 13205](images/item-13205.jpg)

- **Name (English):** None
- **Name (French):** SAUCE GYOZA (ORIGINAL/PIQUANTE) SUKINA
- **Brand:** Sukina
- **Category (English):** International Foods > East Asian Foods
- **Category (French):** Aliments internationaux > Aliments de l'Asie de l'Est
- **How classified:** rule (`east-asian`)
- **Size:** None
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437236782/1791947770/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `4e3948e5269ce9fc`
- **Conditions:** `{"discount": 25}`
- **Raw:** `{"id": 1047462231, "flyer_id": 8187928, "name": "SAUCE GYOZA (ORIGINAL/PIQUANTE) SUKINA", "display_type": 1, "brand": "Sukina", "left": 1573.4, "bottom": -1420.28, "right": 1832.5, "top": -1013.45, "cutout_image_url": "http://f.wishabi.net/page_items/437236782/1791947770/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 25, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "3.99", "pr`

**Item Review Analysis (Pass 1):** Correct. Sukina gyoza sauce (230 ml, original/spicy) at 3.99 (reg. 5.29) — verified. East Asian Foods is right.
