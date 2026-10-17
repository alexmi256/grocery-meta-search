# Uniprix — full product report

Store slug: `uniprix`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 2 current (flyer 154: 23 items; flyer 152: 1 item; both Oct 15–21), plus one empty record (153) and the expired Oct 8–14 records (28/29 empty, 30 with 19 items), correctly excluded. A pharmacy circular — the packs hold only its food corner.
- **Sample counts:** 10 classified + 0 unclassified — the food items here all carry classifiable names.
- **Issues found:** one multibuy total (Regal candies "2/7$" stored as 7.00; unit 3.50). One classifier trap worth naming: item 14844 is a fragrance set (Gladiator / Foxy / Pink Kiss / G eaux de toilette, "20% off regular price") shelved in Drinks > Water on the word "EÀU" — left as the text-only classifier's result and flagged here; it carries no dollar price, honestly, since the offer is percentage-only. The Nosh & Co. chips appear twice (14827, 14841) — the same 1.99 offer printed in two cells of the circular; both kept.
- **Fixes applied this pass:** 14852 → 3.50 with the 2-for-7 multibuy recorded.

## Flyer 152 — valid 2026-10-15 → 2026-10-21 (1 classified items, 0 unclassified)

Source ref: `8177648` · fetched 2026-10-16T12:54:16.431Z

### Item 14827

![item 14827](images/item-14827.jpg)

- **Name (English):** None
- **Name (French):** NOSH & CO. Croustilles sélectionnées
- **Brand:** Nosh & Co.
- **Category (English):** Snacks, Chips & Candy > Chips & Snacks
- **Category (French):** Grignotines, croustilles et friandises > Croustilles et grignotines
- **How classified:** rule (`specific-snacks`)
- **Size:** None
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/435973807/1790945938/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `1f6be14815b86b8e`
- **Conditions:** `{"discount": 40}`
- **Raw:** `{"id": 1045837247, "flyer_id": 8177648, "name": "NOSH & CO. Croustilles sélectionnées", "display_type": 1, "brand": "Nosh & Co.", "left": 1156.84, "bottom": -1022.36, "right": 1793.78, "top": -441.9, "cutout_image_url": "http://f.wishabi.net/page_items/435973807/1790945938/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 40, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "1.99", "`

## Flyer 154 — valid 2026-10-15 → 2026-10-21 (9 classified items, 0 unclassified)

Source ref: `8169048` · fetched 2026-10-16T12:54:16.436Z

**Item Review Analysis (Pass 1):** Correct. Nosh & Co. kettle-cooked chips (salt & vinegar / BBQ) at 1.99 (40% off) — verified. The same offer is captured again as item 14841 from a second printed cell. Chips & Snacks is right.

### Item 14837

![item 14837](images/item-14837.jpg)

- **Name (English):** None
- **Name (French):** KANDJU Candies, 700 g LINDOR Selected chocolate / Selected chocolates
- **Brand:** Kandju
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 700 g
- **Price:** 12.99
- **Printed Price:** “12.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/435970332/1790997571/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `8a6a9fe413bf65c7`
- **Raw:** `{"id": 1045415329, "flyer_id": 8169048, "name": "KANDJU Candies, 700 g LINDOR Selected chocolate / Selected chocolates", "display_type": 1, "brand": "Kandju", "left": 599.05, "bottom": -1270.9, "right": 877.92, "top": -983.38, "cutout_image_url": "http://f.wishabi.net/page_items/435970332/1790997571/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_u`

**Item Review Analysis (Pass 1):** Correct. Kandju candies (700 g tub) or Lindor selected chocolates (150 g) at 12.99 each — verified. Candy & Chocolate is right.

### Item 14838

![item 14838](images/item-14838.jpg)

- **Name (English):** None
- **Name (French):** SIMILAC Préparations pour nourrissons sélectionnées/Selected infant formulas
- **Brand:** Similac
- **Category (English):** Baby > Baby Food
- **Category (French):** Bébé > Aliments pour bébé
- **How classified:** rule (`baby-food`)
- **Size:** None
- **Price:** 49.99
- **Printed Price:** “49.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/435970489/1790997559/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `8fa802612727804c`
- **Raw:** `{"id": 1045415645, "flyer_id": 8169048, "name": "SIMILAC Préparations pour nourrissons sélectionnées/Selected infant formulas", "display_type": 1, "brand": "Similac", "left": 6937.66, "bottom": -1889.14, "right": 7525.61, "top": -1366.23, "cutout_image_url": "http://f.wishabi.net/page_items/435970489/1790997559/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:0`

**Item Review Analysis (Pass 1):** Correct. Similac selected infant formulas (360 Total Care, 584 g) at 49.99 — verified. Baby Food is right.

### Item 14841

![item 14841](images/item-14841.jpg)

- **Name (English):** None
- **Name (French):** NOSH & CO® Croustilles sélectionnées/ Selected CHips
- **Brand:** Nosh & Co.
- **Category (English):** Snacks, Chips & Candy > Chips & Snacks
- **Category (French):** Grignotines, croustilles et friandises > Croustilles et grignotines
- **How classified:** rule (`specific-snacks`)
- **Size:** None
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/435970338/1790997576/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `5cdaab6a71591d43`
- **Conditions:** `{"discount": 40}`
- **Raw:** `{"id": 1045415347, "flyer_id": 8169048, "name": "NOSH & CO® Croustilles sélectionnées/ Selected CHips", "display_type": 1, "brand": "Nosh & Co.", "left": 554.69, "bottom": -427.52, "right": 1144.68, "top": -136.16, "cutout_image_url": "http://f.wishabi.net/page_items/435970338/1790997576/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 40, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "pr`

**Item Review Analysis (Pass 1):** Correct. Nosh & Co. kettle-cooked chips at 1.99 — the same offer as item 14827, printed in a second cell; both captures kept. Chips & Snacks is right.

### Item 14844

![item 14844](images/item-14844.jpg)

- **Name (English):** None
- **Name (French):** GLADIATOR, FOXY, PINK KISS, G EÀU
- **Brand:** None
- **Category (English):** Drinks > Water
- **Category (French):** Boissons > Eau
- **How classified:** rule (`water`)
- **Size:** None
- **Price:** None
- **Printed Price:** None
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/435970387/1790997562/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `42db9901b15a165e`
- **Conditions:** `{"discount": 20}`
- **Raw:** `{"id": 1045415544, "flyer_id": 8169048, "name": "GLADIATOR, FOXY, PINK KISS, G EÀU", "display_type": 1, "brand": null, "left": 4266.23, "bottom": -2506.98, "right": 4589.28, "top": -2184.63, "cutout_image_url": "http://f.wishabi.net/page_items/435970387/1790997562/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 20, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "", "print_id": nu`

**Item Review Analysis (Pass 1):** Classifier trap, left as-is. Fragrances (Gladiator, Foxy, Pink Kiss, G — eaux de toilette) at "20% off regular price"; the classifier shelved them in Drinks > Water on "EÀU". No dollar price exists on the offer, so the price-less state is honest. Flagged in the header.

### Item 14845

![item 14845](images/item-14845.jpg)

- **Name (English):** None
- **Name (French):** CONFISERIES REGAL Citrouilles en chocolat/ Chocolate pumpkins
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** None
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/435970443/1790997558/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `ba1aeead9546c06e`
- **Raw:** `{"id": 1045415620, "flyer_id": 8169048, "name": "CONFISERIES REGAL Citrouilles en chocolat/ Chocolate pumpkins", "display_type": 1, "brand": null, "left": 5778.88, "bottom": -1282.8, "right": 6139.05, "top": -836.19, "cutout_image_url": "http://f.wishabi.net/page_items/435970443/1790997558/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null,`

**Item Review Analysis (Pass 1):** Correct. Regal chocolate pumpkins at 6.99 — verified. (The 50-count Mars/Hershey assortment boxes printed above the pumpkins belong to item 14848's offer family.) Candy & Chocolate is right.

### Item 14848

![item 14848](images/item-14848.jpg)

- **Name (English):** None
- **Name (French):** HERSHEY'S, MARS, EFFEM Friandises sélectionnées/Selected candies
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** None
- **Price:** 13.99
- **Printed Price:** “13.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/435970453/1790997564/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `61be17194b645c4f`
- **Raw:** `{"id": 1045415629, "flyer_id": 8169048, "name": "HERSHEY'S, MARS, EFFEM Friandises sélectionnées/Selected candies", "display_type": 1, "brand": null, "left": 5777.97, "bottom": -836.43, "right": 6137.62, "top": -595.71, "cutout_image_url": "http://f.wishabi.net/page_items/435970453/1790997564/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": nu`

**Item Review Analysis (Pass 1):** Correct. Hershey's / Mars / Effem selected candies (50 fun-size) at 13.99 — verified. Candy & Chocolate is right.

### Item 14852

![item 14852](images/item-14852.jpg)

- **Name (English):** None
- **Name (French):** CONFISESRIES REGAL Friandises sélectionnées/Selected candies
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** None
- **Price:** 7.00
- **Printed Price:** “7.0”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/435970335/1790997574/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `37dd577ce89958fb`
- **Raw:** `{"id": 1045415338, "flyer_id": 8169048, "name": "CONFISESRIES REGAL Friandises sélectionnées/Selected candies", "display_type": 1, "brand": null, "left": 879.5, "bottom": -1269.06, "right": 1140.13, "top": -985.53, "cutout_image_url": "http://f.wishabi.net/page_items/435970335/1790997574/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from the render. Regal selected candies (Lotsa Fizz / Power Poppers) print "2/7$"; the DB stored the 7.00 total. Now 3.50 with the multibuy recorded. Candy & Chocolate is right.

### Item 14853

![item 14853](images/item-14853.jpg)

- **Name (English):** None
- **Name (French):** NERDS Friandises sélectionnées/Selected candies
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** None
- **Price:** 11.99
- **Printed Price:** “11.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/435970450/1790997562/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `a3a79616796d623b`
- **Raw:** `{"id": 1045415626, "flyer_id": 8169048, "name": "NERDS Friandises sélectionnées/Selected candies", "display_type": 1, "brand": null, "left": 6586.75, "bottom": -423.79, "right": 6897.52, "top": -90.89, "cutout_image_url": "http://f.wishabi.net/page_items/435970450/1790997562/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "11.9`

**Item Review Analysis (Pass 1):** Correct. Nerds selected candies (22 pouches) at 11.99 — verified. Candy & Chocolate is right.

### Item 14858

![item 14858](images/item-14858.jpg)

- **Name (English):** None
- **Name (French):** ESKA Eau de source naturelle/Natural spring water
- **Brand:** Eska
- **Category (English):** Drinks > Water
- **Category (French):** Boissons > Eau
- **How classified:** rule (`water`)
- **Size:** 24×500ml
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/435970315/1790997557/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `d7f6059c2ece60dc`
- **Raw:** `{"id": 1045415279, "flyer_id": 8169048, "name": "ESKA Eau de source naturelle/Natural spring water", "display_type": 1, "brand": "Eska", "left": 267.32, "bottom": -2116.87, "right": 509.94, "top": -1838.53, "cutout_image_url": "http://f.wishabi.net/page_items/435970315/1790997557/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": `

**Item Review Analysis (Pass 1):** Correct. Eska natural spring water (24 x 500 ml) at 3.99 — verified. Water is right.
