# Épicerie PA Nature — full product report

Store slug: `pa-nature`. Generated from `data/grocery.db`. A sampled subset of 3 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 104, valid 2026-10-12 → 2026-10-25 — a two-week flyer; the printed window on page 1 matches).
- **Sample counts:** 1 classified + 2 unclassified — that is the WHOLE edition: 3 items. Page 1 alone offers ~10 priced products (bavette 17.99/lb, coffee capsules 2.99, almonds 6.99, salmon 14.99/lb, pasta and canned tomatoes at 3/5$, Oka 9.99/lb, grapes and tomatoes 2.99/lb, mushrooms 2/3$) and the flyer runs several pages. Capture here is ~5 %: the chalkboard price boards defeat the OCR price anchors, as documented since onboarding (harvest is not enabled for this store for the same reason). Fixing capture needs a tailored pass for the chalkboard boards — a decision for Alex, not attempted here.
- **Issues found in the 3 captured items:** all three prices were wrong. The mushrooms and the Oasis juice both print "2/3$" boards; both stored wrong values (1.99, 0.99). The third item's name and price are both garble built from the milk cartons' own claims ("50% MORE PROTEIN / NO SUGAR ADDED" → name "HORE PROTEIN ADPASUGAR", price 50.50); the product is Lactantia UltraPūr milk 1.5 L at 5.99, corrected.
- **Fixes applied this pass:** 11497 → 1.50, 11498 → 1.50 (each with the 2/3$ multibuy recorded), 11499 → 5.99.

## Flyer 104 — valid 2026-10-12 → 2026-10-25 (1 classified items, 2 unclassified)

Source ref: `flyerbox-144988` · fetched 2026-10-14T17:38:34.560Z

### Item 11498

![item 11498](images/item-11498.jpg)

- **Name (English):** None
- **Name (French):** JUS OASIS
- **Brand:** None
- **Category (English):** Drinks > Juice
- **Category (French):** Boissons > Jus
- **How classified:** rule (`juice`)
- **Size:** 960ml
- **Price:** 0.99
- **Printed Price:** “0.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-12 → 2026-10-25
- **bbox:** left 602, top 715, right 831, bottom 754, page 2
- **Full page:** [pages/flyer104-page2-98d124f75a.jpg (flyer page 2)](pages/flyer104-page2-98d124f75a.jpg)
- **Image source URL:** https://na.leafletscdn.com/thumbor/ExkqokucTTYoZ_zztN1GcD1SB0s=/0x0/filters:format(webp):quality(65)/ca/data/75/144988/1.jpg?t=1791806187
- **Details:** confidence: 0.85 · item_key: `a97e8a73e16407c1`
- **Raw:** `{"block_text": "yet Wius OASIS\nJUS OASIS\nJuice\n\n=A 960ml", "ocr_lines": ["JUSOASIS", "POMME"]}`

## Unclassified items — kept for review

The classifier could not assign these items a category. They are kept in the database (not discarded) so a human can review them and improve the rules.

— from flyer 104 (valid 2026-10-12 → 2026-10-25)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 2. Oasis juice (960 ml) prints a "2/3$" chalkboard — the 2.99 board visible in its crop belongs to the Fontaine Santé hummus beside it. Now 1.50 with the multibuy recorded. Juice is right.

### Item 11497

![item 11497](images/item-11497.jpg)

- **Name (English):** PT
- **Name (French):** BLANCS/BIOLOGIQUES
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 1.99
- **Printed Price:** “1.99”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-12 → 2026-10-25
- **bbox:** left 506, top 857, right 769, bottom 926, page 1
- **Full page:** [pages/flyer104-page1-d11d9d2e6c.jpg (flyer page 1)](pages/flyer104-page1-d11d9d2e6c.jpg)
- **Image source URL:** https://na.leafletscdn.com/thumbor/9BFOacsUdrpOwb446EwRL7jt7pQ=/0x0/filters:format(webp):quality(65)/ca/data/75/144988/0.jpg?t=1791806187
- **Details:** confidence: 0.83 · item_key: `4c567bce0bcaaa4c`
- **Raw:** `{"block_text": "M CE j ROE CHEZ nous à\nÀ er\n\nke CHAMPIGNONS a\nBLANCS/BIOLOGIQUES | PT", "ocr_lines": ["DE CHEZ NOUS", "CHAMPIGNONS", "BLANCSBIOLOGIQUES"]}`

— from flyer 104 (valid 2026-10-12 → 2026-10-25)

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 1. Organic white mushrooms (8 oz) print "2/3$"; the DB had 1.99 (the 2.99/lb board in the crop is the vine tomatoes'). Now 1.50 with the multibuy recorded. Unclassified under its truncated name.

### Item 11499

![item 11499](images/item-11499.jpg)

- **Name (English):** None
- **Name (French):** HORE PROTEIN ADPASUGAR
- **Brand:** None
- **Category (English):** Unclassified
- **Category (French):** Non classé
- **How classified:** none
- **Size:** None
- **Price:** 50.50
- **Printed Price:** “50.50”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-12 → 2026-10-25
- **bbox:** left 420, top 643, right 542, bottom 692, page 4
- **Full page:** [pages/flyer104-page4-c9082f54f1.jpg (flyer page 4)](pages/flyer104-page4-c9082f54f1.jpg)
- **Image source URL:** https://na.leafletscdn.com/thumbor/p2yHj3XKMaiaZmkUpkVF-Tj_lII=/0x0/filters:format(webp):quality(65)/ca/data/75/144988/3.jpg?t=1791806187
- **Details:** confidence: 0.99 · item_key: `6f323baa7cdab59b`
- **Raw:** `{"block_text": ">\nHORE\nPROTEIN\nADPASUGAR |\nNO ino «", "ocr_lines": ["HORE", "PROTEIN", "SUGAR", "ADDED"]}`

**Item Review Analysis (Pass 1):** PRICE CORRECTED from page 4. The product is Lactantia UltraPūr milk (1.5 L) at 5.99; the stored name is the cartons' claim text ("50% MORE PROTEIN / NO SUGAR ADDED") OCR-garbled, and 50.50 was assembled from the same "50%". Now 5.99. Unclassified.
