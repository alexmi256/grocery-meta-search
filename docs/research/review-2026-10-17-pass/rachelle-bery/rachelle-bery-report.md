# Rachelle-Béry — full product report

Store slug: `rachelle-bery`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 2 concurrent publications (flyer 150: 51 items; flyer 149: 2 items — both valid 2026-10-15 → 2026-10-21, the Sobeys two-publication pattern). The expired Oct 8–14 pair is correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown across the two publications.
- **Issues found:** none. Every sampled render's printed price matches the DB, including the deep-discount coffee (16.97 against a 29.99 regular — the print is unambiguous).
- **Fixes applied this pass:** none needed.


## Review Analysis — Pass 2 (2026-10-17, verification after Pass 1)

- No fixes were needed in Pass 1; the packet is unchanged and the verdicts stand (Pass 1 preserved in `rachelle-bery-report-pass1.md`). Store review complete — clean.

## Flyer 149 — valid 2026-10-15 → 2026-10-21 (1 classified items, 0 unclassified)

Source ref: `8182873` · fetched 2026-10-16T12:49:19.206Z

### Item 14734

![item 14734](images/item-14734.jpg)

- **Name (English):** None
- **Name (French):** LATTE AU MATCHA LANDISH
- **Brand:** LANDISH
- **Category (English):** Drinks > Tea & Hot Drinks
- **Category (French):** Boissons > Thés et boissons chaudes
- **How classified:** rule (`tea-hot-drinks`)
- **Size:** None
- **Price:** 29.99
- **Printed Price:** “29.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436854836/1791471646/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `0a6f82897c971dbb`
- **Conditions:** `{"discount": 19}`
- **Raw:** `{"id": 1046661258, "flyer_id": 8182873, "name": "LATTE AU MATCHA LANDISH", "display_type": 1, "brand": "LANDISH", "left": 499.8, "bottom": -1149.92, "right": 999.32, "top": -832.84, "cutout_image_url": "http://f.wishabi.net/page_items/436854836/1791471646/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 19, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "29.99", "print_id": null, `

## Flyer 150 — valid 2026-10-15 → 2026-10-21 (9 classified items, 0 unclassified)

Source ref: `8183560` · fetched 2026-10-16T12:49:19.207Z

**Item Review Analysis (Pass 1):** Correct. Landish matcha latte mix (135 g) at 29.99 (reg. 36.99) — verified on the render. Tea & Hot Drinks is right.

### Item 14735

![item 14735](images/item-14735.jpg)

- **Name (English):** None
- **Name (French):** LONGES DE POISSON SAUVAGE SURGELÉES COMPLIMENTS
- **Brand:** Compliments
- **Category (English):** Frozen Food > Frozen Meat and Seafood
- **Category (French):** Produits surgelés > Viande et fruits de mer surgelés
- **How classified:** frozen-remap (`fish`)
- **Size:** 227g
- **Price:** 7.99
- **Printed Price:** “7.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436851413/1791472304/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `c82ba3631a7e2381`
- **Conditions:** `{"discount": 20}`
- **Raw:** `{"id": 1046791631, "flyer_id": 8183560, "name": "LONGES DE POISSON SAUVAGE SURGELÉES COMPLIMENTS", "display_type": 1, "brand": "Compliments", "left": 4937.64, "bottom": -1686.68, "right": 5461.49, "top": -1002.96, "cutout_image_url": "http://f.wishabi.net/page_items/436851413/1791472304/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 20, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "pri`

**Item Review Analysis (Pass 1):** Correct. Compliments frozen wild fish loins (Pacific pink salmon, 227 g) at 7.99 (reg. 9.99) — verified. Frozen Meat and Seafood is right.

### Item 14745

![item 14745](images/item-14745.jpg)

- **Name (English):** None
- **Name (French):** CAFÉ EN GRAINS BIOLOGIQUE ET ÉQUITABLE
- **Brand:** Kicking Horse Coffee
- **Category (English):** Drinks > Coffee
- **Category (French):** Boissons > Cafés
- **How classified:** rule (`coffee`)
- **Size:** 454g
- **Price:** 16.97
- **Printed Price:** “16.97”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436851385/1791472304/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `edb364e6fb8e38dd`
- **Conditions:** `{"discount": 43}`
- **Raw:** `{"id": 1046791592, "flyer_id": 8183560, "name": "CAFÉ EN GRAINS BIOLOGIQUE ET ÉQUITABLE", "display_type": 1, "brand": "Kicking Horse Coffee", "left": 822.22, "bottom": -2546.42, "right": 1614.17, "top": -1921.61, "cutout_image_url": "http://f.wishabi.net/page_items/436851385/1791472304/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 43, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "pric`

**Item Review Analysis (Pass 1):** Correct. Organic fair-trade coffee beans (Kicking Horse decaf, 454 g) at 16.97 (reg. 29.99) — verified. Coffee is right.

### Item 14750

![item 14750](images/item-14750.jpg)

- **Name (English):** None
- **Name (French):** COMPLIMENTS BIOLOGIQUE BEURRE BIOLOGIQUE
- **Brand:** COMPLIMENTS BIOLOGIQUE
- **Category (English):** Dairy & Eggs > Butter & Spreads
- **Category (French):** Produits laitiers et œufs > Beurre et tartinades
- **How classified:** rule (`butter`)
- **Size:** 250g
- **Price:** 6.99
- **Printed Price:** “6.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436851431/1791472304/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `c6fcee02beb46374`
- **Conditions:** `{"discount": 10}`
- **Raw:** `{"id": 1046791683, "flyer_id": 8183560, "name": "COMPLIMENTS BIOLOGIQUE BEURRE BIOLOGIQUE", "display_type": 1, "brand": "COMPLIMENTS BIOLOGIQUE", "left": 9852.92, "bottom": -1995.11, "right": 10375.72, "top": -1434.61, "cutout_image_url": "http://f.wishabi.net/page_items/436851431/1791472304/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 10, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null,`

**Item Review Analysis (Pass 1):** Correct. Compliments organic butter (salted, 250 g) at 6.99 (reg. 7.79) — verified. Butter & Spreads is right.

### Item 14759

![item 14759](images/item-14759.jpg)

- **Name (English):** None
- **Name (French):** BOISSON À BASE DE PLANTES BIOLOGIQUE OATLY AVOINE
- **Brand:** LY!
- **Category (English):** Dairy & Eggs > Non-Dairy Milk Alternatives
- **Category (French):** Produits laitiers et œufs > Laits non laitiers
- **How classified:** rule (`non-dairy-milk`)
- **Size:** 1L
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436851408/1791472306/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `02c6cfd32c07ee4b`
- **Conditions:** `{"discount": 23}`
- **Raw:** `{"id": 1046791652, "flyer_id": 8183560, "name": "BOISSON À BASE DE PLANTES BIOLOGIQUE OATLY AVOINE", "display_type": 1, "brand": "LY!", "left": 6571.42, "bottom": -1967.56, "right": 7098.65, "top": -1420.44, "cutout_image_url": "http://f.wishabi.net/page_items/436851408/1791472306/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 23, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "`

**Item Review Analysis (Pass 1):** Correct. Oatly organic barista oat drink (946 ml / 1 L) at 4.99 (reg. 6.49) — verified. Non-Dairy Milk Alternatives is right.

### Item 14761

![item 14761](images/item-14761.jpg)

- **Name (English):** None
- **Name (French):** TOFU ÉPIK EATS Général Tao
- **Brand:** EPIK EATS
- **Category (English):** Meat > Plant-Based Meat Alternatives
- **Category (French):** Viande > Substituts de viande à base de plantes
- **How classified:** rule (`plant-based-meat`)
- **Size:** None
- **Price:** 7.99
- **Printed Price:** “7.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436851390/1791472304/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `65de0462b2d86b02`
- **Conditions:** `{"discount": 27}`
- **Raw:** `{"id": 1046791615, "flyer_id": 8183560, "name": "TOFU ÉPIK EATS Général Tao", "display_type": 1, "brand": "EPIK EATS", "left": 3297.93, "bottom": -2548.0, "right": 3824.1, "top": -1750.51, "cutout_image_url": "http://f.wishabi.net/page_items/436851390/1791472304/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 27, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "7.99", "print_id": `

**Item Review Analysis (Pass 1):** Correct. Epik Eats General Tao tofu (255 g) at 7.99 (reg. 10.99) — verified. Plant-Based Meat Alternatives is right.

### Item 14767

![item 14767](images/item-14767.jpg)

- **Name (English):** None
- **Name (French):** OATBOX GRANOLA OU GRUAU AU FRIGO BIOLOGIQUES
- **Brand:** OATBOX
- **Category (English):** Pantry > Cereal & Breakfast
- **Category (French):** Produits du garde-manger > Céréales et petits-déjeuners
- **How classified:** rule (`cereal-breakfast`)
- **Size:** 300g
- **Price:** 4.99
- **Printed Price:** “4.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436851430/1791472309/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `237725c366d3f062`
- **Conditions:** `{"discount": 29}`
- **Raw:** `{"id": 1046791679, "flyer_id": 8183560, "name": "OATBOX GRANOLA OU GRUAU AU FRIGO BIOLOGIQUES", "display_type": 1, "brand": "OATBOX", "left": 9283.37, "bottom": -1152.02, "right": 9813.45, "top": -186.06, "cutout_image_url": "http://f.wishabi.net/page_items/436851430/1791472309/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 29, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "4.9`

**Item Review Analysis (Pass 1):** Correct. Oatbox organic granola or overnight oats (280-300 g) at 4.99 (reg. 6.99) — verified. Cereal & Breakfast is right.

### Item 14772

![item 14772](images/item-14772.jpg)

- **Name (English):** None
- **Name (French):** LES FILLES FATTOUSH MÉLASSE DE GRENADE
- **Brand:** LES FILLES FATTOUSH
- **Category (English):** Pantry > Baking Essentials
- **Category (French):** Produits du garde-manger > Essentiels de cuisson
- **How classified:** rule (`baking`)
- **Size:** 200ml
- **Price:** 15.99
- **Printed Price:** “15.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436851444/1791472305/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `14c02fa7a0802d61`
- **Conditions:** `{"discount": 6}`
- **Raw:** `{"id": 1046791700, "flyer_id": 8183560, "name": "LES FILLES FATTOUSH MÉLASSE DE GRENADE", "display_type": 1, "brand": "LES FILLES FATTOUSH", "left": 11484.23, "bottom": -1968.37, "right": 12284.72, "top": -1421.8, "cutout_image_url": "http://f.wishabi.net/page_items/436851444/1791472305/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 6, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "pric`

**Item Review Analysis (Pass 1):** Correct. Les Filles Fattoush pomegranate molasses (200 ml) at 15.99 (reg. 16.99) — verified. (Shelved under Baking Essentials.)

### Item 14775

![item 14775](images/item-14775.jpg)

- **Name (English):** None
- **Name (French):** CHAPELURE DE RIZ PANERISO
- **Brand:** Paneriso
- **Category (English):** Pantry > Baking Essentials
- **Category (French):** Produits du garde-manger > Essentiels de cuisson
- **How classified:** rule (`baking`)
- **Size:** 500g
- **Price:** 7.79
- **Printed Price:** “7.79”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436851432/1791472305/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `7e6b2220dfb5aded`
- **Conditions:** `{"discount": 13}`
- **Raw:** `{"id": 1046791685, "flyer_id": 8183560, "name": "CHAPELURE DE RIZ PANERISO", "display_type": 1, "brand": "Paneriso", "left": 10921.75, "bottom": -1435.23, "right": 11448.28, "top": -877.25, "cutout_image_url": "http://f.wishabi.net/page_items/436851432/1791472305/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 13, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "7.79", "print_id":`

**Item Review Analysis (Pass 1):** Correct. Paneriso rice bread crumbs (500 g) at 7.79 (reg. 8.99) — verified. Baking Essentials is right.

### Item 14782

![item 14782](images/item-14782.jpg)

- **Name (English):** None
- **Name (French):** LES FILLES FATTOUSH HOUMOUS
- **Brand:** LES FILLES FATTOUSH
- **Category (English):** Deli > Antipasto, Dips & Spreads
- **Category (French):** Charcuterie > Antipasti, trempettes et tartinades
- **How classified:** rule (`dips-spreads-deli`)
- **Size:** 210g
- **Price:** 6.49
- **Printed Price:** “6.49”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/436851449/1791472309/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `b80a93821a71a422`
- **Conditions:** `{"discount": 7}`
- **Raw:** `{"id": 1046791709, "flyer_id": 8183560, "name": "LES FILLES FATTOUSH HOUMOUS", "display_type": 1, "brand": "LES FILLES FATTOUSH", "left": 12289.24, "bottom": -872.87, "right": 13077.73, "top": -328.72, "cutout_image_url": "http://f.wishabi.net/page_items/436851449/1791472309/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": 7, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "6.49", `

**Item Review Analysis (Pass 1):** Correct. Les Filles Fattoush hummus (210 g) at 6.49 (reg. 6.99) — verified. Antipasto, Dips & Spreads is right.
