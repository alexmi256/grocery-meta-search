# Marché Lian Tai — full product report

Store slug: `marche-lian-tai`. Generated from `data/grocery.db`. A sampled subset of 10 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 136, valid 2026-10-15 → 2026-10-21, 90 items). The expired Oct 8–14 edition is correctly excluded.
- **Sample counts:** 10 classified + 0 unclassified shown — classification success on this Flipp feed.
- **Issues found:** no wrong prices. The one eye-catching value is real: the squid tentacles at 118.98 are a 10 kg restaurant case priced per box ("/BTE") — the price stands; its unit is now recorded as pack instead of each. Every other sampled price verified against its render, including the live blue crabs at 1.98/lb (a 3-day special) and the oxtail at 9.98/lb.
- **Fixes applied this pass:** 13739's unit set to pack (case).

## Flyer 136 — valid 2026-10-15 → 2026-10-21 (10 classified items, 0 unclassified)

Source ref: `8189357` · fetched 2026-10-16T12:35:06.591Z

### Item 13689

![item 13689](images/item-13689.jpg)

- **Name (English):** None
- **Name (French):** KAKIS FUYU
- **Brand:** None
- **Category (English):** Fruits & Vegetables > Fresh Fruits
- **Category (French):** Fruits et légumes > Fruits frais
- **How classified:** rule (`fruits`)
- **Size:** None
- **Price:** 1.98
- **Printed Price:** “1.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437388476/1792043896/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `582e8c228e642124`
- **Raw:** `{"id": 1047711494, "flyer_id": 8189357, "name": "KAKIS FUYU", "display_type": 1, "brand": null, "left": 445.31, "bottom": -990.14, "right": 856.45, "top": -567.23, "cutout_image_url": "http://f.wishabi.net/page_items/437388476/1792043896/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "1.98", "print_id": null, "short_name": nul`

**Item Review Analysis (Pass 1):** Correct. Fuyu persimmons (Korea) at 1.98/lb — verified on the render. Fresh Fruits is right.

### Item 13694

![item 13694](images/item-13694.jpg)

- **Name (English):** None
- **Name (French):** QUEUE DE BŒUF
- **Brand:** None
- **Category (English):** Meat > Game Meat, Offals & Fowl
- **Category (French):** Viande > Viande exotique
- **How classified:** rule (`game-offal`)
- **Size:** None
- **Price:** 9.98
- **Printed Price:** “9.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437388644/1792043893/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `48f15bf52297fa36`
- **Raw:** `{"id": 1047711545, "flyer_id": 8189357, "name": "QUEUE DE BŒUF", "display_type": 1, "brand": null, "left": 4027.8, "bottom": -1247.5, "right": 4610.39, "top": -843.18, "cutout_image_url": "http://f.wishabi.net/page_items/437388644/1792043893/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "9.98", "print_id": null, "short_name":`

**Item Review Analysis (Pass 1):** Correct. Oxtail at 9.98/lb (21.96/kg) — verified. Game Meat, Offals & Fowl is the taxonomy's offal shelf.

### Item 13695

![item 13695](images/item-13695.jpg)

- **Name (English):** None
- **Name (French):** CRABES BLEUS VIVANTS
- **Brand:** None
- **Category (English):** Fish & Seafood > Shellfish
- **Category (French):** Poissons et fruits de mer > Crustacés
- **How classified:** rule (`shellfish`)
- **Size:** None
- **Price:** 1.98
- **Printed Price:** “1.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437388485/1792043903/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `1c04f6d4a1c23857`
- **Raw:** `{"id": 1047711503, "flyer_id": 8189357, "name": "CRABES BLEUS VIVANTS", "display_type": 1, "brand": null, "left": 1264.12, "bottom": -989.41, "right": 1693.9, "top": -561.12, "cutout_image_url": "http://f.wishabi.net/page_items/437388485/1792043903/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "1.98", "print_id": null, "short`

**Item Review Analysis (Pass 1):** Correct. Live blue crabs at 1.98/lb (3-day special, Oct 16-18) — verified. Shellfish is right.

### Item 13715

![item 13715](images/item-13715.jpg)

- **Name (English):** None
- **Name (French):** DOLE JUS D'ANANAS
- **Brand:** Dole
- **Category (English):** Drinks > Juice
- **Category (French):** Boissons > Jus
- **How classified:** rule (`juice`)
- **Size:** 1.36L
- **Price:** 4.58
- **Printed Price:** “4.58”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437388821/1792043902/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `b41a7c4119790c8a`
- **Raw:** `{"id": 1047711610, "flyer_id": 8189357, "name": "DOLE JUS D'ANANAS", "display_type": 1, "brand": "Dole", "left": 6482.41, "bottom": -2536.31, "right": 6820.7, "top": -2144.17, "cutout_image_url": "http://f.wishabi.net/page_items/437388821/1792043902/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "4.58", "print_id": null, "shor`

**Item Review Analysis (Pass 1):** Correct. Dole pineapple juice (1.36 L) at 4.58 — verified. Juice is right.

### Item 13721

![item 13721](images/item-13721.jpg)

- **Name (English):** None
- **Name (French):** SOC D'ÉPAULE DE PORC DÉSOSSÉ
- **Brand:** None
- **Category (English):** Meat > Pork & Ham
- **Category (French):** Viande > Porc et jambon
- **How classified:** rule (`pork-ham`)
- **Size:** None
- **Price:** 2.98
- **Printed Price:** “2.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437388643/1792043893/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `164056f9dd102c7f`
- **Raw:** `{"id": 1047711542, "flyer_id": 8189357, "name": "SOC D'ÉPAULE DE PORC DÉSOSSÉ", "display_type": 1, "brand": null, "left": 3439.72, "bottom": -1247.51, "right": 4028.25, "top": -848.47, "cutout_image_url": "http://f.wishabi.net/page_items/437388643/1792043893/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "2.98", "print_id": nu`

**Item Review Analysis (Pass 1):** Correct. Boneless pork shoulder butt at 2.98/lb (6.56/kg) — verified. Pork & Ham is right.

### Item 13729

![item 13729](images/item-13729.jpg)

- **Name (English):** None
- **Name (French):** POISSON LUNEUR
- **Brand:** VIVA SEA
- **Category (English):** Fish & Seafood > Fish
- **Category (French):** Poissons et fruits de mer > Poisson
- **How classified:** rule (`fish`)
- **Size:** 500g
- **Price:** 2.98
- **Printed Price:** “2.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437388791/1792043891/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `3d8648d99b5fb073`
- **Raw:** `{"id": 1047711649, "flyer_id": 8189357, "name": "POISSON LUNEUR", "display_type": 1, "brand": "VIVA SEA", "left": 7261.26, "bottom": -2043.81, "right": 7680.48, "top": -1567.19, "cutout_image_url": "http://f.wishabi.net/page_items/437388791/1792043891/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "2.98", "print_id": null, "sh`

**Item Review Analysis (Pass 1):** Correct. Luneur moonfish (Viva Sea, 500 g) at 2.98 — verified. Fish is right.

### Item 13730

![item 13730](images/item-13730.jpg)

- **Name (English):** None
- **Name (French):** CREVETTES PEELÉES CUItes
- **Brand:** Cool Ocean
- **Category (English):** Fish & Seafood > Shrimp
- **Category (French):** Poissons et fruits de mer > Crevette
- **How classified:** rule (`shrimp`)
- **Size:** 500G
- **Price:** 10.88
- **Printed Price:** “10.88”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437388796/1792043896/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `cbedb0ac34359f2b`
- **Raw:** `{"id": 1047711654, "flyer_id": 8189357, "name": "CREVETTES PEELÉES CUItes", "display_type": 1, "brand": "Cool Ocean", "left": 7684.06, "bottom": -2527.44, "right": 8104.44, "top": -2049.96, "cutout_image_url": "http://f.wishabi.net/page_items/437388796/1792043896/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "10.88", "print_i`

**Item Review Analysis (Pass 1):** Correct. Cooked peeled shrimp, tail-on (500 g) at 10.88 — verified. Shrimp is right.

### Item 13739

![item 13739](images/item-13739.jpg)

- **Name (English):** None
- **Name (French):** TENTACULES DE CALMAR
- **Brand:** None
- **Category (English):** Fish & Seafood > Squid & Octopus
- **Category (French):** Poissons et fruits de mer > Calmar et pieuvre
- **How classified:** rule (`squid-octopus`)
- **Size:** None
- **Price:** 118.98
- **Printed Price:** “118.98”
- **Unit quantity:** 1.0
- **Unit measurement:** pack
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437388883/1792043892/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `1dabe447bfc06795`
- **Raw:** `{"id": 1047711668, "flyer_id": 8189357, "name": "TENTACULES DE CALMAR", "display_type": 1, "brand": null, "left": 9399.55, "bottom": -1991.02, "right": 9796.27, "top": -1720.13, "cutout_image_url": "http://f.wishabi.net/page_items/437388883/1792043892/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "118.98", "print_id": null, "`

**Item Review Analysis (Pass 1):** Price correct as printed — a case price. Squid tentacles, size 90/120, sold as a 10 kg restaurant case at 118.98 per box ("/BTE"); the unit is now recorded as pack. Squid & Octopus is right (contrast Palumbo's unclassified "tentacules de calamars" — the glued plural name form was the blocker there).

### Item 13744

![item 13744](images/item-13744.jpg)

- **Name (English):** None
- **Name (French):** BOULETTES DE BŒUF À LA CORIANDRE
- **Brand:** Chef Shuo
- **Category (English):** Meat > Beef
- **Category (French):** Viande > Bœuf
- **How classified:** rule (`beef`)
- **Size:** 228G
- **Price:** 4.98
- **Printed Price:** “4.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437388808/1792043906/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `d79e9586052ead1b`
- **Raw:** `{"id": 1047711666, "flyer_id": 8189357, "name": "BOULETTES DE BŒUF À LA CORIANDRE", "display_type": 1, "brand": "Chef Shuo", "left": 7322.4, "bottom": -436.54, "right": 7852.02, "top": -4.29, "cutout_image_url": "http://f.wishabi.net/page_items/437388808/1792043906/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "4.98", "print_`

**Item Review Analysis (Pass 1):** Correct. Chef Shuo beef balls with cilantro (228 g) at 4.98 — verified. Beef is right.

### Item 13757

![item 13757](images/item-13757.jpg)

- **Name (English):** None
- **Name (French):** SAUCE DE SOJA
- **Brand:** Marca Pina
- **Category (English):** Pantry > Condiments
- **Category (French):** Produits du garde-manger > Condiments et garnitures
- **How classified:** rule (`condiments`)
- **Size:** 1000ML
- **Price:** 1.98
- **Printed Price:** “1.98”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** http://f.wishabi.net/page_items/437388961/1792043896/extra_large.jpg
- **Details:** confidence: 1.00 · item_key: `2984212395c053df`
- **Raw:** `{"id": 1047711700, "flyer_id": 8189357, "name": "SAUCE DE SOJA", "display_type": 1, "brand": "Marca Pina", "left": 10265.2, "bottom": -1318.85, "right": 10677.6, "top": -957.94, "cutout_image_url": "http://f.wishabi.net/page_items/437388961/1792043896/extra_large.jpg", "valid_from": "2026-10-15T00:00:00-04:00", "valid_to": "2026-10-21T23:59:59-04:00", "page_destination": null, "discount": null, "available_to": "2026-10-21T23:59:59-04:00", "video_url": null, "price": "1.98", "print_id": null, "sh`

**Item Review Analysis (Pass 1):** Correct. Marca Pina soy sauce (1000 ml) at 1.98 — verified. Condiments is right.
