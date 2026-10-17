# Jean Coutu — full product report

Store slug: `jean-coutu`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 2 current publications (flyer 42: 6 items; flyer 43: 47 items — both Oct 15–21), the wishabi concurrent-publication pattern seen at Familiprix and Brunet. Three further records span the window with 0 items (empty publications). Expired editions correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown; 0 unclassified exist in the cycle. The sample is Halloween-candy heavy because that is this pharmacy's post-purge grocery remnant (same character as Brunet).
- **Issues found:** (1) Selection wafers (7709) stored 3.00 — the payload collapsed the printed "2/3$ ou 1.50 l'un" multibuy into its total; corrected to 1.50 with the multibuy recorded in the item's conditions, from the render. (2) ⚠ FLAGGED for Alex, NOT changed: the Freddo chocolate pumpkins (7864) sit in Fresh Vegetables on "citrouilles". The frozen ground truth carries SIX chocolate-pumpkin entries — including this exact item — with Fresh Vegetables as their adjudicated verdict, so per the campaign's GT discipline the classifier is left alone and no guard was added; flipping it would fight the GT. If those verdicts were machine-frozen rather than human-adjudicated, the GT entries themselves are the thing to revisit.
- **Fixes applied this pass:** 7709's price corrected (3.00 → 1.50) with its multibuy condition recorded.

## Flyer 42 — valid 2026-10-15 → 2026-10-21 (1 classified items, 0 unclassified)

Source ref: `8180792` · fetched 2026-10-13T04:28:28.242Z

### Item 7648

![item 7648](images/item-7648.jpg)

- **Name (English):** None
- **Name (French):** Selection Croustilles
- **Brand:** Selection
- **Category (English):** Snacks, Chips & Candy > Chips & Snacks
- **Category (French):** Grignotines, croustilles et friandises > Croustilles et grignotines
- **How classified:** rule (`specific-snacks`)
- **Size:** 24x16g
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436743746/1791423698/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `0fdf485e33054456`
- **Conditions:** `{"discount": 13}`
- **Raw:** `{"id": 1046439956, "flyer_id": 8180792, "name": "Selection Croustilles", "display_type": 1, "brand": "Selection", "left": 3872.97, "bottom": -571.08, "right": 4475.29, "top": -317.75, "cutout_image_url": "http://f.wishabi.net/page_items/436743746/1791423698/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 13, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "6.99", "print_id": null,`

## Flyer 43 — valid 2026-10-15 → 2026-10-21 (9 classified items, 0 unclassified)

Source ref: `8180777` · fetched 2026-10-13T04:28:28.246Z

**Item Review Analysis (Pass 1):** Correct. Selection chips, 24 x 16 g snack bags, at 6.99 per pack (reg. 7.99) — verified on the render. Chips & Snacks is right.

### Item 7679

![item 7679](images/item-7679.jpg)

- **Name (English):** None
- **Name (French):** PRINGLES Croustilles
- **Brand:** Pringles
- **Category (English):** Snacks, Chips & Candy > Chips & Snacks
- **Category (French):** Grignotines, croustilles et friandises > Croustilles et grignotines
- **How classified:** rule (`specific-snacks`)
- **Size:** 24x19g
- **Price:** 12.99
- **Printed Price:** “12.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436741897/1791422978/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `89482031f2297af1`
- **Conditions:** `{"discount": 13}`
- **Raw:** `{"id": 1046438550, "flyer_id": 8180777, "name": "PRINGLES Croustilles", "display_type": 1, "brand": "Pringles", "left": 4894.93, "bottom": -1543.56, "right": 5186.89, "top": -1282.25, "cutout_image_url": "http://f.wishabi.net/page_items/436741897/1791422978/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 13, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "12.99", "print_id": null`

**Item Review Analysis (Pass 1):** Correct. Pringles snack cups, 24 x 19 g, at 12.99 (reg. 14.99) — verified. Chips & Snacks is right.

### Item 7697

![item 7697](images/item-7697.jpg)

- **Name (English):** None
- **Name (French):** CADBURY Chocolates
- **Brand:** Cadbury
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** None
- **Price:** 18.99
- **Printed Price:** “18.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436741900/1791422979/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `15cc2e0b02594349`
- **Conditions:** `{"discount": 21}`
- **Raw:** `{"id": 1046438562, "flyer_id": 8180777, "name": "CADBURY Chocolates", "display_type": 1, "brand": "Cadbury", "left": 5188.74, "bottom": -1790.87, "right": 5470.32, "top": -1551.1, "cutout_image_url": "http://f.wishabi.net/page_items/436741900/1791422979/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 21, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "18.99", "print_id": null, "s`

**Item Review Analysis (Pass 1):** Correct. Cadbury Favourites snack bars, pack of 90 (993 g), at 18.99 (reg. 23.99) — verified. Candy & Chocolate is right.

### Item 7709

![item 7709](images/item-7709.jpg)

- **Name (English):** None
- **Name (French):** Selection Gaufrettes
- **Brand:** Selection
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** 200g
- **Price:** 3.00
- **Printed Price:** “3.0”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436741482/1791422982/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `d90d48b8e0470867`
- **Raw:** `{"id": 1046438780, "flyer_id": 8180777, "name": "Selection Gaufrettes", "display_type": 1, "brand": "Selection", "left": 8354.1, "bottom": -1020.86, "right": 8641.42, "top": -767.56, "cutout_image_url": "http://f.wishabi.net/page_items/436741482/1791422982/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "3.0", "print_id": null,`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the render. Selection vanilla wafers (200 g) print "2/3$ ou 1.50 l'un"; the payload stored the 2-for total (3.00) as the price. Now 1.50 with the multibuy (2 for 3.00) recorded in the conditions. Crackers & Cookies is right.

### Item 7736

![item 7736](images/item-7736.jpg)

- **Name (English):** None
- **Name (French):** IRRESISTIBLE Keurig Café
- **Brand:** Irresistible
- **Category (English):** Drinks > Coffee
- **Category (French):** Boissons > Cafés
- **How classified:** rule (`coffee`)
- **Size:** None
- **Price:** 12.99
- **Printed Price:** “12.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436741789/1791422976/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `0c4ba6f7d2578bc5`
- **Conditions:** `{"discount": 38}`
- **Raw:** `{"id": 1046438427, "flyer_id": 8180777, "name": "IRRESISTIBLE Keurig Café", "display_type": 1, "brand": "Irresistible", "left": 2883.5, "bottom": -1405.85, "right": 3448.88, "top": -1110.2, "cutout_image_url": "http://f.wishabi.net/page_items/436741789/1791422976/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 38, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "12.99", "print_id"`

**Item Review Analysis (Pass 1):** Correct. Irresistible K-Cups (30, Colombian or breakfast blend) at 12.99 (reg. 20.99) — verified. Coffee is right.

### Item 7764

![item 7764](images/item-7764.jpg)

- **Name (English):** None
- **Name (French):** MAYNARDS Régals-Éclair Friandises
- **Brand:** Maynards
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 562g
- **Price:** 10.49
- **Printed Price:** “10.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436741258/1791422983/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `afe98a650f8e8b3f`
- **Conditions:** `{"discount": 5}`
- **Raw:** `{"id": 1046438367, "flyer_id": 8180777, "name": "MAYNARDS Régals-Éclair Friandises", "display_type": 1, "brand": "Maynards", "left": 862.26, "bottom": -2251.43, "right": 1135.53, "top": -1889.3, "cutout_image_url": "http://f.wishabi.net/page_items/436741258/1791422983/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 5, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "10.49", "print`

**Item Review Analysis (Pass 1):** Correct. Maynards fun-treats candies, pack of 45 (562 g), at 10.49 (reg. 10.99) — verified. Candy & Chocolate is right.

### Item 7789

![item 7789](images/item-7789.jpg)

- **Name (English):** None
- **Name (French):** NAYA Eau de source naturelle
- **Brand:** Naya
- **Category (English):** Drinks > Water
- **Category (French):** Boissons > Eau
- **How classified:** rule (`water`)
- **Size:** 20x500ml
- **Price:** 3.49
- **Printed Price:** “3.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436741794/1791422979/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `96ebefe047870d7d`
- **Conditions:** `{"discount": 46}`
- **Raw:** `{"id": 1046438438, "flyer_id": 8180777, "name": "NAYA Eau de source naturelle", "display_type": 1, "brand": "Naya", "left": 2883.12, "bottom": -1707.71, "right": 3175.45, "top": -1406.7, "cutout_image_url": "http://f.wishabi.net/page_items/436741794/1791422979/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 46, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "3.49", "print_id": nu`

**Item Review Analysis (Pass 1):** Correct. Naya spring water, 20 x 500 ml, at 3.49 per pack (reg. 6.49, plus deposit) — verified. Water is right.

### Item 7806

![item 7806](images/item-7806.jpg)

- **Name (English):** None
- **Name (French):** MARS Petites Joies Chocolats
- **Brand:** Mars
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 05kg
- **Price:** 15.49
- **Printed Price:** “15.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436741908/1791422984/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `cfc60075d0b03dfb`
- **Conditions:** `{"discount": 18}`
- **Raw:** `{"id": 1046438591, "flyer_id": 8180777, "name": "MARS Petites Joies Chocolats", "display_type": 1, "brand": "Mars", "left": 4627.43, "bottom": -504.77, "right": 5077.06, "top": -128.58, "cutout_image_url": "http://f.wishabi.net/page_items/436741908/1791422984/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 18, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "15.49", "print_id": nu`

**Item Review Analysis (Pass 1):** Correct. Mars fun-size chocolate packs (65 or 90 pieces) at 15.49 (reg. 18.99-19.99) — verified. Candy & Chocolate is right.

### Item 7864

![item 7864](images/item-7864.jpg)

- **Name (English):** None
- **Name (French):** FREDDO Citrouilles en chocolat au caramel
- **Brand:** FREDDO
- **Category (English):** Fruits & Vegetables > Fresh Vegetables
- **Category (French):** Fruits et légumes > Légumes frais
- **How classified:** rule (`vegetables`)
- **Size:** None
- **Price:** 13.99
- **Printed Price:** “13.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436741664/1791422977/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `6eac107745b5f9e8`
- **Conditions:** `{"discount": 13}`
- **Raw:** `{"id": 1046438906, "flyer_id": 8180777, "name": "FREDDO Citrouilles en chocolat au caramel", "display_type": 1, "brand": "FREDDO", "left": 11539.8, "bottom": -1951.75, "right": 12101.3, "top": -1627.14, "cutout_image_url": "http://f.wishabi.net/page_items/436741664/1791422977/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 13, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "13.99`

**Item Review Analysis (Pass 1):** FLAGGED, not changed (see header). Freddo chocolate-covered caramel pumpkins (65 pieces, 390 g) at 13.99 — price verified on the render. The Fresh Vegetables placement follows "citrouilles", and the frozen GT adjudicates this exact item (and five sibling chocolate-pumpkin entries) to Fresh Vegetables, so the classifier is left as-is pending Alex's call on the GT entries.

### Item 7873

![item 7873](images/item-7873.jpg)

- **Name (English):** None
- **Name (French):** MEGA Assortiment de bonbons
- **Brand:** Mega
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 1,8kg
- **Price:** 14.49
- **Printed Price:** “14.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436741907/1791422983/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `01f14cf6a38e0e1f`
- **Conditions:** `{"discount": 19}`
- **Raw:** `{"id": 1046438588, "flyer_id": 8180777, "name": "MEGA Assortiment de bonbons", "display_type": 1, "brand": "Mega", "left": 5079.61, "bottom": -505.59, "right": 5413.17, "top": -163.26, "cutout_image_url": "http://f.wishabi.net/page_items/436741907/1791422983/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 19, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "14.49", "print_id": nul`

**Item Review Analysis (Pass 1):** Correct. Mega assorted candies (1.8 kg) at 14.49 (reg. 17.99) — verified. Candy & Chocolate is right.
