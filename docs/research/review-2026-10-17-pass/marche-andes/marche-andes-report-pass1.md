# Marché Andes — full product report

Store slug: `marche-andes`. Generated from `data/grocery.db`. A sampled subset of 2 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 129, valid 2026-10-15 → 2026-10-21). This store's "flyer" is its WooCommerce specials list (source kind `woo_specials`): the edition holds exactly the 2 products the shop currently lists on special, and the previous edition likewise held 2 — a genuinely tiny specials list, not a capture failure.
- **Sample counts:** 2 classified + 0 unclassified — the whole edition.
- **Issues found:** none in the data carried. Both items' product shots match their names and categories, and the prices are the shop's structured sale prices. Brand and size are empty for both: the specials feed exposes name + price only, while the packs print Noel / 294 g and 403 g on their photos — a source-structure limit of the same family as the short-name Flipp stores (harvest is not enabled here; the store has no page bboxes). Recorded, not fixed.
- **Fixes applied this pass:** none needed.

## Flyer 129 — valid 2026-10-15 → 2026-10-21 (2 classified items, 0 unclassified)

Source ref: `specials-2026-10-15` · fetched 2026-10-16T12:22:44.440Z

### Item 13380

![item 13380](images/item-13380.webp)

- **Name (English):** None
- **Name (French):** Biscuits DUCALES
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** None
- **Price:** 2.89
- **Printed Price:** “2.89”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://www.marcheandes.com/wp-content/uploads/2025/08/Biscuits_Ducales_Sachet.webp
- **Details:** SKU: 4367 · confidence: 1.00 · item_key: `0ae0d4265177cdca`
- **Conditions:** `{"regular_price": 3.29}`
- **Raw:** `{"woo_id": 9038, "permalink": "https://www.marcheandes.com/produit/galletas-ducales-bolsa/"}`

**Item Review Analysis (Pass 1):** Correct. Ducales crackers (Noel, 294 g on the pack) at 2.89 from the shop's specials feed — shot matches. Crackers & Cookies is right; brand/size are absent because the feed doesn't carry them (see header).

### Item 13381

![item 13381](images/item-13381.webp)

- **Name (English):** None
- **Name (French):** Biscuits FESTIVAL CITRON
- **Brand:** None
- **Category (English):** Snacks, Chips & Candy > Crackers & Cookies
- **Category (French):** Grignotines, croustilles et friandises > Craquelins et biscuits
- **How classified:** rule (`crackers-cookies`)
- **Size:** None
- **Price:** 4.19
- **Printed Price:** “4.19”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-15 → 2026-10-21
- **Image source URL:** https://www.marcheandes.com/wp-content/uploads/2025/08/Biscuits_Festival_Citron.webp
- **Details:** SKU: 6898 · confidence: 1.00 · item_key: `bd181c9af176fd19`
- **Raw:** `{"woo_id": 9035, "permalink": "https://www.marcheandes.com/produit/galletas-festival-limon/"}`

**Item Review Analysis (Pass 1):** Correct. Festival lemon sandwich cookies (Noel, 403 g on the pack) at 4.19 — shot matches. Crackers & Cookies is right; same feed limit on brand/size.
