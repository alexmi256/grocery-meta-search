# Familiprix — full product report

Store slug: `familiprix`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 2, both current (flyers 115 and 116, valid 2026-10-15 → 2026-10-21) — wishabi carries Familiprix's cycle as concurrent publications (56 items each); the sample draws from both. Older expired publications are correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown. Unclassified items exist at this store but the classified sample filled first; the store's kept pool after this morning's purge is the grocery slice of a pharmacy flyer (candy, snacks, drinks, baby) plus unclassified rows kept for review.
- **Issues found:** one misclassification — item 11829, Pure Protein bars, sat in Candy & Chocolate. The protein-bar rule never matched: the name's word order is "Protein barre" (brand-first French spelling), a token pair the rule didn't carry, so the candy rule's bare "chocolat" token won. Its ground-truth verdict is Pantry > Cereal & Breakfast. Everything else in the sample verified clean against the region renders (prices, sizes, categories), including the 77.99 Enfamil formula case and the 3.00 Merci chocolate bars.
- **Patterns:** pharmacy flyers' grocery slice is Halloween candy and snacks this cycle; the data quality from the Flipp payload is high (structured brand/size). The protein-bar miss is a word-order vocabulary gap, the same family as Adonis's singular/plural gaps.
- **Fixes applied this pass:** "protein barre" and "barre protein" added to the protein-bar rule, and the round-2 candy guard for protein-bar winners now skips names that say protein/protéine. Ground truth 12384 → 12387 items, 8271 → 8273 signatures; reclassify flipped the 2 stored instances to Cereal & Breakfast.

## Flyer 115 — valid 2026-10-15 → 2026-10-21 (6 classified items, 0 unclassified)

Source ref: `8184296` · fetched 2026-10-16T12:09:36.244Z

### Item 11792

![item 11792](images/item-11792.jpg)

- **Name (English):** None
- **Name (French):** PRINGLES, Croustilles, 24 x 19 g
- **Brand:** Pringles
- **Category (English):** Snacks, Chips & Candy > Chips & Snacks
- **Category (French):** Grignotines, croustilles et friandises > Croustilles et grignotines
- **How classified:** rule (`specific-snacks`)
- **Size:** 24 x 19 g
- **Price:** 11.99
- **Printed Price:** “11.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436561477/1791268103/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `98e0e42eb8173ece`
- **Conditions:** `{"discount": 23}`
- **Raw:** `{"id": 1046889348, "flyer_id": 8184296, "name": "PRINGLES, Croustilles, 24 x 19 g", "display_type": 1, "brand": "Pringles", "left": 5375.5, "bottom": -1741.98, "right": 5752.5, "top": -1524.98, "cutout_image_url": "http://f.wishabi.net/page_items/436561477/1791268103/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 23, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "11.99", "print`

**Item Review Analysis (Pass 1):** Correct. Pringles snack cups ("Coupes collation"), 24 x 19 g, at 11.99 (reg. 15.49) — the region is a product cutout (price payload-sourced); name, size and Chips & Snacks all match.

### Item 11814

![item 11814](images/item-11814.jpg)

- **Name (English):** None
- **Name (French):** BUBLY Eau pétillante 12 x 355 ml
- **Brand:** bubly
- **Category (English):** Drinks > Water
- **Category (French):** Boissons > Eau
- **How classified:** rule (`water`)
- **Size:** 12 x 355 ml
- **Price:** 12.00
- **Printed Price:** “12.0”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436535941/1791268090/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `d9f4658e2205d0d7`
- **Raw:** `{"id": 1046888800, "flyer_id": 8184296, "name": "BUBLY Eau pétillante 12 x 355 ml", "display_type": 1, "brand": "bubly", "left": 1704.53, "bottom": -1260.0, "right": 1885.17, "top": -1122.72, "cutout_image_url": "http://f.wishabi.net/page_items/436535941/1791268090/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "12.0", "print_`

**Item Review Analysis (Pass 1):** Correct. bubly blackberry sparkling water, 12 x 355 ml, at 12.00 — Drinks > Water is right for sparkling water; the region is a bare cutout, so the price rests on the payload.

### Item 11819

![item 11819](images/item-11819.jpg)

- **Name (English):** None
- **Name (French):** Mars Petites Joies assortiment de 95 friandises assorties format collation 1kg
- **Brand:** Mars
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 1kg
- **Price:** 21.99
- **Printed Price:** “21.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436536123/1791268098/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `ccf5686948e053ba`
- **Conditions:** `{"discount": 19}`
- **Raw:** `{"id": 1046889323, "flyer_id": 8184296, "name": "Mars Petites Joies assortiment de 95 friandises assorties format collation 1kg", "display_type": 1, "brand": "Mars", "left": 5651.07, "bottom": -776.91, "right": 5839.28, "top": -451.38, "cutout_image_url": "http://f.wishabi.net/page_items/436536123/1791268098/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 19, "available_to": "2026-10-21T23:59:59-04:00", "`

**Item Review Analysis (Pass 1):** Correct. Mars assorted fun-size candies, 95 count (1 kg box), at 21.99 (reg. 26.99) — Candy & Chocolate; the name's "Petites Joies" is the line's French fun-size wording.

### Item 11829

![item 11829](images/item-11829.jpg)

- **Name (English):** None
- **Name (French):** Pure Protein barre sans gluten chocolat de luxe 6x50g
- **Brand:** Pure Protein
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 6x50g
- **Price:** 12.29
- **Printed Price:** “12.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436536562/1791268100/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `027c2871354a9029`
- **Conditions:** `{"discount": 29}`
- **Raw:** `{"id": 1046889447, "flyer_id": 8184296, "name": "Pure Protein barre sans gluten chocolat de luxe 6x50g", "display_type": 1, "brand": "Pure Protein", "left": 6508.56, "bottom": -2386.25, "right": 6703.4, "top": -2093.64, "cutout_image_url": "http://f.wishabi.net/page_items/436536562/1791268100/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 29, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null`

**Item Review Analysis (Pass 1):** Fixed this pass. Pure Protein chocolate deluxe bars, 6 x 50 g, at 12.29 (reg. 17.29) — image verifies product and price. It was classified Candy & Chocolate because the protein-bar rule lacked the "protein barre" word order; phrases added and the item reclassified to Pantry > Cereal & Breakfast, its ground-truth verdict.

### Item 11832

![item 11832](images/item-11832.jpg)

- **Name (English):** None
- **Name (French):** KELLOGG'S, Minis carrés aux Rice Krispies, 40 unités
- **Brand:** Kellogg's
- **Category (English):** Pantry > Cereal & Breakfast
- **Category (French):** Produits du garde-manger > Céréales et petits-déjeuners
- **How classified:** rule (`cereal-breakfast`)
- **Size:** 40 unités
- **Price:** 9.99
- **Printed Price:** “9.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436536104/1791268088/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `0daa2947e5abbc0d`
- **Conditions:** `{"discount": 15}`
- **Raw:** `{"id": 1046889260, "flyer_id": 8184296, "name": "KELLOGG'S, Minis carrés aux Rice Krispies, 40 unités", "display_type": 1, "brand": "Kellogg's", "left": 5784.7, "bottom": -1223.05, "right": 6056.81, "top": -878.37, "cutout_image_url": "http://f.wishabi.net/page_items/436536104/1791268088/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 15, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "pr`

**Item Review Analysis (Pass 1):** Correct. Kellogg's Rice Krispies Minis squares, 40 units, at 9.99 (reg. 11.79) — Cereal & Breakfast; image verifies.

### Item 11834

![item 11834](images/item-11834.jpg)

- **Name (English):** None
- **Name (French):** ORIGINAL Guimauves avec enrobage chocolate 250 g
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 250 g
- **Price:** 11.49
- **Printed Price:** “11.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436536109/1791268090/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `1bec99b0b39367d3`
- **Conditions:** `{"discount": 28}`
- **Raw:** `{"id": 1046889278, "flyer_id": 8184296, "name": "ORIGINAL Guimauves avec enrobage chocolate 250 g", "display_type": 1, "brand": null, "left": 4924.9, "bottom": -2510.11, "right": 5154.91, "top": -2135.82, "cutout_image_url": "http://f.wishabi.net/page_items/436536109/1791268090/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 28, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "11.`

## Flyer 116 — valid 2026-10-15 → 2026-10-21 (4 classified items, 0 unclassified)

Source ref: `8184318` · fetched 2026-10-16T12:09:36.296Z

**Item Review Analysis (Pass 1):** Correct. Original "Mallow Bats" chocolate-coated marshmallows, 250 g, at 11.49 (reg. 15.99) — Candy & Chocolate; the payload name drops the product's "Mallow Bats" line but carries the description faithfully.

### Item 11864

![item 11864](images/item-11864.jpg)

- **Name (English):** None
- **Name (French):** Enfamil A+ Préparation à base de lait enrichie de fer pour nourrissons 0-12 mois Liquide concentré ajouter de l'eau 12x385ml
- **Brand:** Enfamil A+
- **Category (English):** Baby > Baby Food
- **Category (French):** Bébé > Aliments pour bébé
- **How classified:** rule (`baby-food`)
- **Size:** 12x385ml
- **Price:** 77.99
- **Printed Price:** “77.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436536042/1791268093/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `4d6de2874dea7683`
- **Raw:** `{"id": 1046892343, "flyer_id": 8184318, "name": "Enfamil A+ Préparation à base de lait enrichie de fer pour nourrissons 0-12 mois Liquide concentré ajouter de l'eau 12x385ml", "display_type": 1, "brand": "Enfamil A+", "left": 4276.19, "bottom": -1849.41, "right": 4461.49, "top": -1589.2, "cutout_image_url": "http://f.wishabi.net/page_items/436536042/1791268093/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount`

**Item Review Analysis (Pass 1):** Correct. Enfamil A+ concentrated liquid infant formula, 12 x 385 ml case, at 77.99 (reg. 82.99) — Baby > Baby Food is this taxonomy's shelf for formula; image verifies product, format and price.

### Item 11869

![item 11869](images/item-11869.jpg)

- **Name (English):** None
- **Name (French):** NERDS Gummy Clusters, Friandise, 22 unités
- **Brand:** Nerds
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 22 unités
- **Price:** 11.99
- **Printed Price:** “11.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436561476/1791268102/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `3b5a27b134aa9c37`
- **Conditions:** `{"discount": 8}`
- **Raw:** `{"id": 1046892912, "flyer_id": 8184318, "name": "NERDS Gummy Clusters, Friandise, 22 unités", "display_type": 1, "brand": "Nerds", "left": 5141.5, "bottom": -1428.98, "right": 5397.5, "top": -1220.98, "cutout_image_url": "http://f.wishabi.net/page_items/436561476/1791268102/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 8, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "11.99", `

**Item Review Analysis (Pass 1):** Correct. Nerds Gummy Clusters, 22 units, at 11.99 — Candy & Chocolate (payload-sourced price; product line is a standard Halloween assortment).

### Item 11897

![item 11897](images/item-11897.jpg)

- **Name (English):** None
- **Name (French):** KINDER Figurine en chocolat au lait avec une couche crémeuse au lait à l'intérieur
- **Brand:** Kinder
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`specific-chocolate-eggs`)
- **Size:** None
- **Price:** 5.49
- **Printed Price:** “5.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436536107/1791268089/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `d20ba1c6f8c815dd`
- **Conditions:** `{"discount": 15}`
- **Raw:** `{"id": 1046892701, "flyer_id": 8184318, "name": "KINDER Figurine en chocolat au lait avec une couche crémeuse au lait à l'intérieur", "display_type": 1, "brand": "Kinder", "left": 5723.45, "bottom": -2137.1, "right": 6039.9, "top": -1884.86, "cutout_image_url": "http://f.wishabi.net/page_items/436536107/1791268089/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 15, "available_to": "2026-10-21T23:59:59-04:`

**Item Review Analysis (Pass 1):** Correct. Kinder milk-chocolate figurine with crispy layer at 5.49 — Candy & Chocolate.

### Item 11914

![item 11914](images/item-11914.jpg)

- **Name (English):** None
- **Name (French):** Merci barres de chocolat au lait 100g
- **Brand:** Merci
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 100g
- **Price:** 3.00
- **Printed Price:** “3.0”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436535918/1791268091/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `1ee33fb6a1d48c5b`
- **Conditions:** `{"discount": 33}`
- **Raw:** `{"id": 1046891562, "flyer_id": 8184318, "name": "Merci barres de chocolat au lait 100g", "display_type": 1, "brand": "Merci", "left": 1248.6, "bottom": -773.08, "right": 1622.63, "top": -548.95, "cutout_image_url": "http://f.wishabi.net/page_items/436535918/1791268091/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 33, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "3.0", "print_`

**Item Review Analysis (Pass 1):** Correct. Merci milk chocolate bars, 4 x 25 g (= the stored 100 g), at 3.00 (reg. 4.49) — image verifies the price badge "3$"; Candy & Chocolate is right.
