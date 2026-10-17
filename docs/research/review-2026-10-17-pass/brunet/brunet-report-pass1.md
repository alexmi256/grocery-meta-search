# Brunet — full product report

Store slug: `brunet`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 2, both current — flyer 51 (valid 2026-10-08 → 2026-10-21, a 2-item publication) and flyer 49 (2026-10-15 → 2026-10-21, 43 items). Brunet's Flipp presence is split into concurrent publications; together they are the store's current cycle. The DB also holds two expired editions (Oct 1–14, Oct 8–14), correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown. Zero unclassified exist on the current flyers — after this morning's purge of stored non-grocery, Brunet's kept pool is all classified grocery. The sample is candy-heavy because that is what Brunet's grocery remnant is (its flyer is mostly pharmacy stock, discarded at ingest by design).
- **Issues found:** (1) item 8795, nicotine gum, was classified as Candy & Chocolate and KEPT as grocery — when "Gommes" leads the name, the candy phrase outranks the OTC rule's "nicotine"; (2) item 8529, white petroleum jelly, was classified as Pantry > Honey, Syrups & Spreads — the word "jelly/gelée" traps it into the pantry — and also kept as grocery; both are pharmacy products that should never have survived the grocery filter, and the frozen ground truth carries token-trap verdicts for both shapes (plus "Jelly Belly" candy, same rule, also fixed); (3) item 8492's size (400 g, printed in the region) was not captured — the harvest had no rule for a single weight standing beside a count.
- **Patterns:** the surviving non-grocery leaks at pharmacy stores are no longer bulk department stock (purged this morning) but single-word traps ("gommes", "jelly") that route pharmacy products INTO grocery categories. Guard remaps keyed to unambiguous drug/product words (nicotine, vaseline, petroleum) are the right shape of fix — the words have no grocery meaning.
- **Fixes applied this pass:** guard remaps — candy + nicotine → Health & Beauty > Pharmacy; spreads + vaseline/petroleum → Health & Beauty > Personal Care; spreads + "jelly belly" → Candy & Chocolate. Ground truth 12340 → 12346 items, 8230 → 8234 signatures. Harvest: a single weight/volume candidate now beats count-only rivals (and the weight hint recognizes glued units like "400g"). Data: reclassified, then purged — 6 items deleted (8795 and 8529 at brunet, plus one more brunet item and three at familiprix/jean-coutu flipped by the same guards); brunet harvest re-run filled 8492's 400 g and 2 more sizes.

## Flyer 51 — valid 2026-10-08 → 2026-10-21 (1 classified items, 0 unclassified)

Source ref: `8161661` · fetched 2026-10-13T04:28:31.397Z

### Item 8795

![item 8795](images/item-8795.jpg)

- **Name (English):** None
- **Name (French):** Gommes de nicotine sélectionnées pour aider à cesser de fumer 30 un.
- **Brand:** Personnelle
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 30 un
- **Price:** 12.99
- **Printed Price:** “12.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-08 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/435433212/1790295855/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `f1c6730480711830`
- **Raw:** `{"id": 1043399030, "flyer_id": 8161661, "name": "Gommes de nicotine sélectionnées pour aider à cesser de fumer 30 un.", "display_type": 1, "brand": "Personnelle", "left": 5159.38, "bottom": -2487.84, "right": 5753.01, "top": -2002.14, "cutout_image_url": "http://f.wishabi.net/page_items/435433212/1790295855/extra_large.jpg", "valid_from": "2026-10-08T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", `

## Flyer 49 — valid 2026-10-15 → 2026-10-21 (9 classified items, 0 unclassified)

Source ref: `8172968` · fetched 2026-10-13T04:28:31.375Z

**Item Review Analysis (Pass 1):** REMOVED this pass. The image is Personnelle nicotine gum 2 mg ("produit pour cesser de fumer", 30 pieces, 12.99) — a smoking-cessation drug, not candy. It was kept because "Gommes" leading the name let the candy rule outrank the OTC rule's "nicotine". A guard remap now routes candy-classified nicotine products to Health & Beauty > Pharmacy, and the item was purged with the other newly non-grocery rows.

### Item 8304

![item 8304](images/item-8304.jpg)

- **Name (English):** None
- **Name (French):** Chocolats sélectionnés
- **Brand:** Irresistible
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 300g
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436305938/1790938339/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `606e1720fc693247`
- **Conditions:** `{"discount": 18}`
- **Raw:** `{"id": 1045243663, "flyer_id": 8172968, "name": "Chocolats sélectionnés", "display_type": 1, "brand": "Irresistible", "left": 8078.62, "bottom": -2297.77, "right": 8353.88, "top": -2043.98, "cutout_image_url": "http://f.wishabi.net/page_items/436305938/1790938339/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 18, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "6.99", "print_id":`

**Item Review Analysis (Pass 1):** Correct. Irresistible selected chocolates (chocolate almonds pictured), 300 g, 6.99 (reg. 8.49) — name, size, price and Candy & Chocolate category all match the region.

### Item 8337

![item 8337](images/item-8337.jpg)

- **Name (English):** None
- **Name (French):** WERTHER'S Bonbons sélectionnés
- **Brand:** Werther's
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 245g
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436305921/1790938330/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `6fa7b5e5556c7767`
- **Conditions:** `{"discount": 12}`
- **Raw:** `{"id": 1045243646, "flyer_id": 8172968, "name": "WERTHER'S Bonbons sélectionnés", "display_type": 1, "brand": "Werther's", "left": 8921.25, "bottom": -1027.82, "right": 9206.41, "top": -775.94, "cutout_image_url": "http://f.wishabi.net/page_items/436305921/1790938330/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 12, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "4.99", "print_`

**Item Review Analysis (Pass 1):** Correct. Werther's Original caramel hard candies, 245 g, 4.99 (reg. 5.69) — all stored values match.

### Item 8338

![item 8338](images/item-8338.jpg)

- **Name (English):** None
- **Name (French):** LINDT Chocolats sélectionnés
- **Brand:** Lindt
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 300g
- **Price:** 14.49
- **Printed Price:** “14.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436305933/1790938337/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `857387182c193f83`
- **Conditions:** `{"discount": 19}`
- **Raw:** `{"id": 1045243658, "flyer_id": 8172968, "name": "LINDT Chocolats sélectionnés", "display_type": 1, "brand": "Lindt", "left": 8922.63, "bottom": -1271.62, "right": 9207.53, "top": -1029.46, "cutout_image_url": "http://f.wishabi.net/page_items/436305933/1790938337/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 19, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "14.49", "print_id":`

**Item Review Analysis (Pass 1):** Correct. Lindt Swiss Classic hazelnut milk chocolate, 300 g, 14.49 (reg. 17.99-18.49; the "125 points" badge is loyalty promo, not price) — all match.

### Item 8364

![item 8364](images/item-8364.jpg)

- **Name (English):** None
- **Name (French):** FREDDO Chocolats sélectionnés
- **Brand:** FREDDO
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 240g
- **Price:** 8.49
- **Printed Price:** “8.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436305925/1790938332/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `257d8f5756412ff9`
- **Conditions:** `{"discount": 15}`
- **Raw:** `{"id": 1045243650, "flyer_id": 8172968, "name": "FREDDO Chocolats sélectionnés", "display_type": 1, "brand": "FREDDO", "left": 8642.15, "bottom": -516.93, "right": 8925.21, "top": -303.71, "cutout_image_url": "http://f.wishabi.net/page_items/436305925/1790938332/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 15, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "8.49", "print_id": `

**Item Review Analysis (Pass 1):** Correct. Freddo caramel chocolates, 240 g, 8.49 (reg. 9.99) — all match.

### Item 8421

![item 8421](images/item-8421.jpg)

- **Name (English):** None
- **Name (French):** BABY GOURMET Purées pour bébés sélectionnées
- **Brand:** BABY GOURMET
- **Category (English):** Baby > Baby Food
- **Category (French):** Bébé > Aliments pour bébé
- **How classified:** rule (`baby-food`)
- **Size:** 92-128ml
- **Price:** 2.29
- **Printed Price:** “2.29”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436306006/1790938344/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `41968d11cc1f43bd`
- **Conditions:** `{"discount": 23}`
- **Raw:** `{"id": 1045243702, "flyer_id": 8172968, "name": "BABY GOURMET Purées pour bébés sélectionnées", "display_type": 1, "brand": "BABY GOURMET", "left": 10077.8, "bottom": -513.83, "right": 10354.9, "top": -253.41, "cutout_image_url": "http://f.wishabi.net/page_items/436306006/1790938344/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 23, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price":`

**Item Review Analysis (Pass 1):** Correct with a price-form note: Baby Gourmet baby purées, 92-128 ml. The flyer prices them as a range (2.29 à 2.99 across varieties); the stored 2.29 is the payload's figure (the range's low end). Baby > Baby Food is right (baby food is grocery in this taxonomy).

### Item 8475

![item 8475](images/item-8475.jpg)

- **Name (English):** None
- **Name (French):** LINDT, GHIRARDELLI Chocolats sélectionnés
- **Brand:** Lindt
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** 50-138g
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436305761/1790938327/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `ea7f838ecbc61db8`
- **Conditions:** `{"discount": 33}`
- **Raw:** `{"id": 1045243175, "flyer_id": 8172968, "name": "LINDT, GHIRARDELLI Chocolats sélectionnés", "display_type": 1, "brand": "Lindt", "left": 590.98, "bottom": -1836.24, "right": 857.38, "top": -1578.52, "cutout_image_url": "http://f.wishabi.net/page_items/436305761/1790938327/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 33, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "5.99", "`

**Item Review Analysis (Pass 1):** Correct. Lindt/Ghirardelli selected chocolates, 50-138 g, 5.99 ("3$ de rabais", reg. 8.99) — stored size range and price match.

### Item 8477

![item 8477](images/item-8477.jpg)

- **Name (English):** None
- **Name (French):** SELECTION Croustilles sélectionnées
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
- **Image source URL:** http://f.wishabi.net/page_items/436305769/1790938332/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `d7cce8fb3b1abbf8`
- **Conditions:** `{"discount": 17}`
- **Raw:** `{"id": 1045243195, "flyer_id": 8172968, "name": "SELECTION Croustilles sélectionnées", "display_type": 1, "brand": "Selection", "left": 287.03, "bottom": -2261.84, "right": 570.15, "top": -1934.65, "cutout_image_url": "http://f.wishabi.net/page_items/436305769/1790938332/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 17, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "6.99", "pr`

**Item Review Analysis (Pass 1):** Correct. Selection classic potato chips, 24 x 16 g Halloween box, 6.99 (reg. 8.39) — stored size "24x16g" and Chips & Snacks category match.

### Item 8492

![item 8492](images/item-8492.jpg)

- **Name (English):** None
- **Name (French):** REGAL Bonbons sélectionnés
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Candy & Chocolate
- **Category (French):** Grignotines, croustilles et friandises > Friandises et chocolats
- **How classified:** rule (`candy-chocolate`)
- **Size:** None
- **Price:** 5.99
- **Printed Price:** “5.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436305944/1790938343/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `1925ca7e5171617b`
- **Conditions:** `{"discount": 14}`
- **Raw:** `{"id": 1045243669, "flyer_id": 8172968, "name": "REGAL Bonbons sélectionnés", "display_type": 1, "brand": null, "left": 8350.86, "bottom": -303.11, "right": 8640.81, "top": -111.65, "cutout_image_url": "http://f.wishabi.net/page_items/436305944/1790938343/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 14, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "5.99", "print_id": null, "`

**Item Review Analysis (Pass 1):** Fixed this pass. Regal selected candies (Dubble Bubble Pops + Rainbow Chewies), 5.99 (reg. 6.99) — price and category were right; the printed size "400 g, 60 un." was missing because the harvest had no rule for one weight beside a count. The new single-weight rule filled 400 g on re-run. Brand None in the DB although REGAL is the flyer's header word — the payload brand field was empty; the name carries it. Minor.

### Item 8529

![item 8529](images/item-8529.jpg)

- **Name (English):** None
- **Name (French):** Selected white petroleum jelly
- **Brand:** Personelle
- **Category (English):** Pantry > Honey, Syrups & Spreads
- **Category (French):** Produits du garde-manger > Miel, sirops et tartinades
- **How classified:** rule (`honey-spreads`)
- **Size:** 375g
- **Price:** 3.99
- **Printed Price:** “3.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436305934/1790938337/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `a69696e52661c979`
- **Raw:** `{"id": 1045243659, "flyer_id": 8172968, "name": "Selected white petroleum jelly", "display_type": 1, "brand": "Personelle", "left": 8920.46, "bottom": -2301.97, "right": 9198.28, "top": -2050.59, "cutout_image_url": "http://f.wishabi.net/page_items/436305934/1790938337/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "3.99", "pr`

**Item Review Analysis (Pass 1):** REMOVED this pass. Personelle white petroleum jelly, 375 g, 3.99 — a skin-care product the word "jelly" had classified as Pantry > Honey, Syrups & Spreads and kept as grocery. Guard remap (vaseline/petroleum in a spreads classification → Health & Beauty > Personal Care) plus purge removed it. Side note: its English payload name was stored in the French name field — wishabi sometimes serves a single English name for this flyer; recorded as a source quirk.
