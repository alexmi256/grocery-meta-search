# Visual review findings — 2026-10-16

Review of the regenerated sample pack (`review-2026-10-16/`, current flyers
only): **57 stores, 705 items** (520 classified + 185 unclassified), every
item judged with its flyer image as the source of truth against the stored
name / brand / category / price / size / unit. 3 stores had no current
flyer and were skipped (Aliments Merci, Marché BKR, Marché Sultan).

## The three reported problems, resolved

1. **Expired flyers in reports** — the old pack sampled all flyers: 599 of
   1,038 items (58%) sat on expired editions. The sampler now restricts to
   flyers with `valid_to >= today`; the regenerated pack contains **0
   expired items**.
2. **Size** — the `package_size` column exists (added 2026-10-16) and the
   report renders it; the gap was coverage (14.3% of items). This review
   found **308 of 705 sampled items (44%) print a size in the flyer that is
   not stored**. Fixes below raise DB coverage to 18.1% and fix the
   extractor; the rest needs a page-image harvest stage (see G1).
3. **Unit** — was stored on only 36 of 15,096 items. Flipp's unit lives in
   `post_price_text` and is now parsed (ingest + backfill: 265 items). For
   OCR stores the unit was **stripped and discarded** by the price parser;
   it is now captured at ingest (see G2).

## Image verdicts (705 items)

| verdict | count | meaning |
|---|---|---|
| ok | 553 (78%) | picture shows the stored product |
| partial | 72 (10%) | right cell, product cut off or neighbour intrudes |
| promo_only | 77 (11%) | the "item" is a promo badge / flyer furniture, not a product |
| wrong_product | 3 (0.4%) | picture shows a different product |

No displaced crops, no whole-page images, nothing unreadable: the crop
machinery (after the October bbox fix) is sound. Partials come from tight
segmentation boxes (Mayrand boxes cover the price/name column only) and
from dense grids where two products share a cell (euro-marche, frutta-si,
marche-c-t, l-intermarche, marche-axep).

## Field issues (1,023 total; 575 of 705 items have ≥1)

| group | count | what it is |
|---|---|---|
| G1 size:missing | 308 | size printed in the flyer, not stored |
| G2 unit:missing | 188 | per-lb / per-each / per-100g printed, not stored |
| G3 name:wrong | 162 | OCR garble, spaceless merges, fragments, badge names |
| G4 category:wrong + missing | 103 + 45 | token traps and vocabulary gaps |
| G5 price:wrong | 101 | fragment drops, badges/points as prices, dual-price picks |
| G6 brand:missing | 94 | brand printed, brand field empty |
| G7 size:wrong | 19 | bundle/range extraction picked the wrong variant's size |

### G1 — Size missing (308)

How the size is depicted, per source family:

- **Flipp stores** (avril, rachelle-bery, marche-ami, iga family,
  giant-tiger, walmart, …): size printed in small type **under the product
  name in the flyer cell**, or on the packaging in the product shot. It is
  **not in the Flipp payload at all** (verified: payload carries
  name/brand/price/cutout only, `text_areas` empty). Capturing it needs an
  OCR pass over each item's cell on the flyer page — the items carry exact
  page bboxes, so this is a well-defined new pipeline stage, not yet built.
- **OCR stores**: the size line is a small-type line in the cell (under the
  name at Tau/Tradition/Metro-style layouts, at the end of the name line at
  h-marche/marche-korea, on the pack at marche-pa). The segmenter rejects
  size-only lines as name candidates and never stored them. Where the size
  did reach the name or the Tesseract block text, the extractor now finds
  it (below).
- **Counts without weight** (familiprix, uniprix, brunet): "24 unités",
  "90 gélules", "80 capsules", "24 UN." — the old extractor required a
  weight/volume unit.

Fixes applied (extractor, `pipeline/fields.py`):

- units added: `gr` (Quebec abbreviation — the euro-marche "650 GR" case),
  count forms (unités/un./capsules/comprimés/gélules/caplets/tablets),
  `po` (pouces, Canadian Tire specs);
- **ranges captured whole** ("100-154 g", "125 à 200 g", "208-350 g")
  instead of the range end;
- **weight/volume beats count** ("CREVETTES 60-70 UNITÉS 907 g" → 907 g);
- **bundles: first product's size wins** ("(800 g) ou (907 g)" → 800 g) —
  the old last-match-wins systematically stored the *second* product's
  size (Pharmaprix, Provigo, M&M Food Market samples);
- extraction also runs over the OCR `block_text` when the name has no
  size (recovers e.g. Mayrand's "2.84 L").

Result on the production DB: coverage **2,161 → 2,729 items (18.1%)**
(+568 fills), plus **390 stored values corrected** under the new policy.
Of the 308 sampled missing sizes, 35 are now filled from name/block text;
the remaining 273 exist only in the flyer page image (Flipp cells and
small-type blocks outside the name block) — they are the input spec for
the page-harvest stage. Of the 19 sampled wrong sizes (G7), 12 changed to
the corrected value; 7 are variety-range cases where the name-level size
cannot identify the pictured variant.

### G2 — Unit missing (188)

Depiction is remarkably consistent: the unit prints **with the price** —
trailing the amount ("2,95 $/KG", "3,99 ch."), as a standalone line under
the price (euro-marche "CH/EA"), tucked under the cents (same store),
inside the price badge (kim-phat "/LB", milano "/100gr"), or right of the
price (uniprix "CH./EA.", t-t "/ch"). Per-100g pricing is Milano's house
style and appears at Adonis ("88¢ le 100 g") and Odessa ("$/100 g").

Root cause (OCR stores): `ocr/segment.py` had a regex whose only job was
to **strip** the unit suffix so the amount could anchor — the stripped
unit was thrown away, and `FlyerItem.price_unit` was never set.

Fix (segmenter): price anchors now capture the unit from the price cluster
text, from a standalone unit line right of / below / tucked under the
price (three geometry cases, euro-marche geometry measured on the real
page), and default to `each` for multibuy anchors. Canonical values:
`lb`, `kg`, `each`, `100g`, `box`. Verified on fixtures (la-moisson badges
"$ / KG" → kg, "$ / UN" → each) and live (below).

**Verified live** (same current editions re-fetched with the fixed
segmenter into a scratch DB; production had unit on 0 items for all
three): euro-marche **38/50 items (76%)** carry a unit (35 each, 3 lb),
marche-sheng-tai **43/54 (80%)** (28 each, 13 lb, 2 box — its "/BTE"
per-box prices included), fruiterie-valmont **29/35 (83%)** (23 each,
3 lb, 3 per-100g), odessa-poissonnier **14/26 (54%)**. The misses are
prices whose unit line OCR never emitted as a readable line (garbled
"$/KC"-style reads) — an OCR-quality residue, not a parser gap.

For Flipp stores the unit backfill from `post_price_text` stands at 265
items; remaining Flipp unit misses (Metro-group flyer-payload items,
Adonis promo pricing) print the unit only in the page image — same
page-harvest stage as G1.

### G3 — Name wrong (162)

Families: spaceless OCR merges ("Plancherflottant stratifie",
"CREVETTES BLAND DUPACIFIQU"), small-print garble (marche-bonichoix,
shop-sante, marche-esposito names carry bracket/pipe junk), fragments and
badge text stored as names (Mayrand "TOP", "MOM PRICE" = misread
"WOW PRICE"; monde fragments), two-cell merges (marche-c-t triples,
marche-axep, l-intermarche), brand-in-name at Odessa ("SEA-RAY INDE" =
brand + origin, product dropped).

No single fix: name quality is per-store OCR tuning (Alex's standing
direction). The systemic piece — merged cells on dense grids — is a
segmentation-anchor problem shared with G5. Documented per store below.

### G4 — Category wrong/missing (148)

Image-verified token traps fixed in `classify/rules.py` (each verified
against the item image; ground-truth score 81.5% → **81.6%** of items,
79.0% → 79.2% of signatures — no regression):

- "RÔTI DE BAS DE PALETTE DÉSOSSÉ" Unclassified → Meat > Beef (×3 IGA
  banners; phrase `bas de palette` added)
- "DORÉ TEL QUEL FRAIS" (kim-phat pickerel) → Fish & Seafood > Fish
- "concombre de mer/demer" (t-t sea cucumber) → Fish (was Fresh Vegetables)
- "spaghetti squash" / acorn / butternut (walmart) → Fresh Vegetables
  (was Pasta & Pasta Sauce)
- "BARBE À PAPA" / cotton candy (Akhavan) → Candy & Chocolate (was Baking)
- "BRONCHOPHAN sirop" (uniprix cough syrup) → Pharmacy (was Honey & Syrups)
- "POIS MANGE-TOUT" (maxi snow peas) → Fresh Vegetables (guard remap vs
  the `sucre` Baking trap)
- "DAL MOLISE MOZZA RELLA" (milano) → Cheese (was South Asian — `dal` trap)
- "kaak au lait" (adonis) → Bakery > Bread (was Milk & Cream)
- "Honey Butter Chips" (marche-korea) → Chips & Snacks (guard remap)
- "MINI-BARRES NESTLÉ" (provigo) → Candy & Chocolate (was Unclassified)
- "BEURRES DE GRAINES & TAHINI" (la-moisson) removed from the junk list —
  it is a real Nuts To You product (→ Butter & Spreads)

14 of the 148 sampled category issues changed in the DB (the targeted
traps); Unclassified fell 1,430 → 1,420 DB-wide. The remaining 134 are
mostly **not text-fixable**: canned vs fresh with no text marker (canned
San Marzano tomatoes read as Fresh Vegetables at Mayrand and Milano —
only the can in the image tells), store-prior judgement calls (Brunet
supplements), and one-item vocabulary tails (shop-sante supplement brand
names). This matches the earlier ceiling analysis for text-only
classification.

### G5 — Price wrong (101)

Sub-causes, in order of damage:

1. **Lone-integer anchors** — a cents fragment whose dollar digit OCR
   missed becomes a whole-dollar price ("4,99" → 66.0 at bonichoix,
   "7,99" → 99 at esposito, "4,98" → 98 at newon, "2,88" → 2 at fu-tai),
   discount badges become prices (monde-au-naturel: **every** price was a
   "SPÉCIAL 15/20/25%" badge), loyalty points become prices (tradition
   "100 PTS" → 55/90/95). In these flyer templates real prices always
   carry cents. **Fix:** `bare_int_anchor: false` in the per-store OCR
   config for marche-bonichoix, marches-tradition, monde-au-naturel,
   marche-esposito, marche-newon, marche-fu-tai, l-intermarche and
   euro-marche (precedent: marches-tau, odessa already had it).
   **Verified live:** bonichoix bare-int prices 5 → 0 (items 79 → 73),
   tradition 11 → 1 (items 84 → 80). Monde-au-naturel drops to 0 items:
   its prices *never* anchored except as badges — the store needs a
   tailored detection pass (its flyer prices sit in the product cells in a
   style the anchor strategy does not read); until then it returns
   nothing rather than 70 wrong prices.
2. **Dual-price $/lb + $/kg** (Odessa): the small $/kg reference anchored
   first and won the name; the advertised $/lb price folded as an alt.
   **Fix:** when a folding price is kg/lb-related (ratio ≈ 2.2046) to the
   stored one and is the smaller figure, it is promoted to main.
   **Verified on the fixture and live:** tilapia 24.23 ($/kg) → main
   10.99 $/lb, alt 24.23. One live case (halibut) still picks the $/kg
   figure because its $/lb anchor claimed a neighbouring fragment line
   first — name-matching, documented for Odessa's tailored pass.
3. **Glyph errors**: 9→6 in cents (h-marche 4.99→4.66 ×3, esposito
   3.99→3.66) — known RapidOCR font confusion, per-store; not fixable in
   the parser without risking real 66¢ prices.
4. **Neighbour prices / merged cells** (frutta-si, marche-c-t,
   mm-food-market, wholesale-club 98.80): same segmentation family as G3.
5. **Multibuy semantics differ by source**: Flipp stores the bundle total
   (metro "3/7$" → 7.0, kim-phat badges), the OCR segmenter stores the
   per-unit price with the deal in `conditions.multibuy`. The deal terms
   are preserved in both; harmonising the headline value is a Phase 5
   display decision, not a parse bug. One real bug in this family:
   rachelle-bery stored the small "1,50 l'unité" line and lost the "2/3,00"
   headline.
6. **Chalkboard prices** (pa-nature): all 3 sampled prices wrong,
   including "50.50" read off a "50% MORE PROTEIN" claim. Known hard
   store; tailored pass or exclusion decision needed.

### G6 — Brand missing (94)

- **super-c (12/20) and wholesale-club (12/13)**: the Flipp payload for
  these banners carries `brand: null` (verified in raw) although the name
  and package carry it (Heinz, Excel, Nestlé). rachelle-bery/uniprix/
  walmart payloads do carry brand. Per-banner payload difference; the
  brand is recoverable only from the name (first-token heuristics are
  unsafe) or the page image.
- **la-moisson (10/11)**: every cell prints a brand line *above* the
  product name (Oatly, Gusta, Camino…); the segmenter's name-growing
  starts at the product line. Per-store fix: extend the name block one
  line up for this store and split it as brand — documented, not yet built.
- **marche-korea (10/11)**: brand is the first token of the (clean) name
  (NISHIKI, SAMYANG, HAITAI…); never split into the brand field. Same for
  marche-andes. A known-brand dictionary split would work here; the
  store's names are consistent enough to make it safe — documented.

### G7 — Promo/furniture items (77 promo_only)

Flyer furniture ingested as items: loyalty banners, section headers,
recipe cards (IGA "Voir la recette" classified Meat > Beef), gift-card
panels (pharmaprix stored an Optimum "Valeur de 10$" as a price),
certification strips. Many sit in Unclassified, correctly harmless; some
carry prices/categories. The validated exclusion layer
(`classification-fallback-tiers.md`, 212 items, 0 false fires) targets
exactly this pool and is still awaiting the go-ahead to wire into ingest.

## Fixes applied — summary

| fix | where | verified by |
|---|---|---|
| Sampler: current flyers only | `classify/review_sample.py` | pack v2: 0 expired of 705 |
| Flipp unit from `post_price_text` | `sources/flipp.py` + backfill | unit coverage 36 → 265 items |
| OCR unit capture (cluster text + nearby unit lines + multibuy default) | `ocr/segment.py` | new tests; live re-fetch (below) |
| Dual-price $/lb promotion | `ocr/segment.py` fold logic | odessa fixture + live tilapia |
| `bare_int_anchor: false` ×8 stores | `sources/circulaires_club_config.json` | live: bonichoix 5→0, tradition 11→1 bare-int prices |
| Size extractor v2 (gr/counts/ranges/bundle-first/block-text) + correction pass | `pipeline/fields.py` | +568 fills, 390 corrections; 6 new tests |
| 12 category traps + 2 guard remaps + 1 junk-list removal | `classify/rules.py` | GT 81.5→81.6%; all 12 cases re-checked in DB |
| Full suite | — | 99 tests green, ruff + mypy strict clean |

Live verification (scratch re-fetches of the same current editions,
fixed code vs production): bonichoix bare-int prices 5 → 0, tradition
11 → 1, monde-au-naturel 70 garbage items → 0 (flag suppresses its
badge-only anchors; store awaits a tailored pass); unit capture
euro-marche 0 → 38/50, sheng-tai 0 → 43/54, valmont 0 → 29/35, odessa
0 → 14/26 with the tilapia $/lb promotion confirmed on the live flyer
(main 10.99 $/lb, alt 24.23 $/kg). Kim-phat's live re-fetch was not run
(its seed needs the Flipp-search merchant config); its "/LB"-in-badge
depiction is covered by the anchor unit tests.

## Per-store results

Columns: items sampled · ok / partial / promo_only / wrong_product ·
top issues. Detail notes follow for stores with distinctive problems.

| store | n | ok | partial | promo | wrong | top issues |
|---|---|---|---|---|---|---|
| 3-saisons-fruits-legumes | 1 | 1 | 0 | 0 | 0 | unit:missing 1 |
| adonis | 20 | 19 | 0 | 1 | 0 | unit:missing 9, category:missing 9, size:missing 6 |
| akhavan | 10 | 10 | 0 | 0 | 0 | category:wrong 1 |
| avril | 11 | 10 | 0 | 1 | 0 | size:missing 7, category:wrong 1 |
| brunet | 12 | 10 | 0 | 2 | 0 | size:missing 7, category:wrong 3, name:wrong 1 |
| bulk-barn | 3 | 3 | 0 | 0 | 0 | unit:missing 3 |
| canadian-tire | 11 | 8 | 1 | 2 | 0 | size:missing 8, category:wrong 2, unit:missing 2 |
| coop-alentour | 10 | 10 | 0 | 0 | 0 | size:missing 8, category:wrong 2, unit:missing 2 |
| costco | 20 | 17 | 3 | 0 | 0 | name:wrong 14, size:missing 4, brand:missing 3 |
| euro-marche | 10 | 2 | 8 | 0 | 0 | unit:missing 9, size:missing 8, name:wrong 5 |
| familiprix | 10 | 10 | 0 | 0 | 0 | size:missing 5, unit:missing 1 |
| fruiterie-valmont | 10 | 9 | 1 | 0 | 0 | unit:missing 8, price:wrong 3, name:wrong 2 |
| frutta-si | 11 | 4 | 7 | 0 | 0 | unit:missing 7, size:missing 6, price:wrong 5 |
| giant-tiger | 10 | 10 | 0 | 0 | 0 | size:missing 9, unit:missing 5 |
| h-marche | 10 | 9 | 1 | 0 | 0 | unit:missing 9, size:missing 6, price:wrong 4 |
| iga | 14 | 10 | 0 | 4 | 0 | size:missing 3, category:wrong 1, category:missing 1 |
| iga-express | 14 | 11 | 0 | 3 | 0 | size:missing 10, category:missing 1 |
| iga-extra | 14 | 11 | 0 | 3 | 0 | size:missing 8, category:missing 1 |
| intermarche-palumbo | 1 | 1 | 0 | 0 | 0 | unit:missing 1, name:missing 1 |
| jean-coutu | 20 | 11 | 0 | 9 | 0 | size:missing 3, category:wrong 2, unit:missing 1 |
| kim-phat | 11 | 11 | 0 | 0 | 0 | size:missing 5, unit:missing 5, category:wrong 1 |
| l-intermarche | 10 | 7 | 3 | 0 | 0 | size:missing 4, price:wrong 4, name:wrong 4 |
| la-moisson | 11 | 10 | 1 | 0 | 0 | brand:missing 10, name:wrong 2, size:missing 1 |
| marche-ami | 10 | 10 | 0 | 0 | 0 | size:missing 8, unit:missing 2 |
| marche-andes | 2 | 2 | 0 | 0 | 0 | brand:missing 2, size:missing 1 |
| marche-axep | 10 | 5 | 5 | 0 | 0 | size:missing 5, unit:missing 5, brand:missing 3 |
| marche-bonanza | 2 | 1 | 1 | 0 | 0 | brand:missing 2, price:wrong 1, unit:missing 1 |
| marche-bonichoix | 20 | 19 | 1 | 0 | 0 | category:wrong 11, name:wrong 10, size:missing 9 |
| marche-c-t | 10 | 9 | 1 | 0 | 0 | unit:missing 8, name:wrong 8, price:wrong 3 |
| marche-esposito | 10 | 10 | 0 | 0 | 0 | unit:missing 10, name:wrong 9, size:missing 5 |
| marche-fu-tai | 10 | 9 | 0 | 0 | 1 | name:wrong 7, unit:missing 7, price:wrong 3 |
| marche-korea | 11 | 11 | 0 | 0 | 0 | brand:missing 10, category:wrong 7, name:wrong 1 |
| marche-lian-tai | 10 | 9 | 1 | 0 | 0 | unit:missing 8, size:missing 5, price:wrong 3 |
| marche-newon | 10 | 10 | 0 | 0 | 0 | unit:missing 9, price:wrong 5, name:wrong 4 |
| marche-pa | 16 | 16 | 0 | 0 | 0 | size:missing 13, category:wrong 8, unit:missing 3 |
| marche-richelieu | 13 | 10 | 1 | 2 | 0 | size:missing 7, unit:missing 3, category:wrong 2 |
| marche-sheng-tai | 12 | 11 | 1 | 0 | 0 | unit:missing 9, size:missing 6, name:wrong 5 |
| marches-tau | 20 | 17 | 2 | 1 | 0 | size:missing 15, name:wrong 6, category:missing 6 |
| marches-tradition | 20 | 16 | 2 | 2 | 0 | price:wrong 11, size:missing 10, name:wrong 7 |
| maxi | 12 | 12 | 0 | 0 | 0 | category:wrong 1, size:wrong 1, category:missing 1 |
| mayrand | 20 | 6 | 10 | 3 | 1 | name:wrong 11, size:missing 7, unit:missing 4 |
| metro | 20 | 14 | 2 | 4 | 0 | size:missing 11, category:missing 6, unit:missing 2 |
| metro-plus | 20 | 12 | 3 | 5 | 0 | size:missing 11, category:missing 5, unit:missing 2 |
| milano-fruiterie | 14 | 14 | 0 | 0 | 0 | unit:missing 14, size:missing 5, brand:missing 4 |
| mm-food-market | 19 | 8 | 2 | 9 | 0 | name:wrong 9, size:missing 5, size:wrong 3 |
| monde-au-naturel | 20 | 0 | 3 | 17 | 0 | price:wrong 20, name:wrong 8, brand:missing 2 |
| odessa-poissonnier | 19 | 9 | 10 | 0 | 0 | unit:missing 10, price:wrong 6, name:wrong 4 |
| pa-nature | 3 | 3 | 0 | 0 | 0 | price:wrong 3, brand:missing 2, name:wrong 2 |
| pharmaprix | 12 | 10 | 0 | 2 | 0 | size:wrong 5, brand:missing 4, size:missing 3 |
| provigo | 11 | 11 | 0 | 0 | 0 | size:wrong 3, category:missing 1 |
| rachelle-bery | 10 | 10 | 0 | 0 | 0 | size:missing 9, category:wrong 1, unit:missing 1 |
| shop-sante | 20 | 20 | 0 | 0 | 0 | size:missing 15, name:wrong 13, category:wrong 11 |
| super-c | 20 | 13 | 0 | 7 | 0 | brand:missing 12, size:missing 9, category:wrong 3 |
| t-t | 10 | 8 | 2 | 0 | 0 | name:wrong 9, size:missing 8, unit:missing 7 |
| uniprix | 10 | 10 | 0 | 0 | 0 | unit:missing 10, size:missing 4, category:wrong 1 |
| walmart | 12 | 11 | 0 | 0 | 1 | size:missing 6, category:wrong 3 |
| wholesale-club | 13 | 13 | 0 | 0 | 0 | brand:missing 12, size:missing 8, category:wrong 4 |

### Store notes

- **akhavan** — cleanest store in the review (10/10 ok, 1 category error,
  fixed). The pdf_text tailored pipeline is the quality benchmark.
- **monde-au-naturel** — store-level price breakdown: the anchor strategy
  reads only the "SPÉCIAL %" badge; all 70 stored prices were badge
  percentages. Now returns 0 items with `bare_int_anchor: false` until a
  tailored pass reads its cell prices. 17/20 sampled "items" were badge
  fragments.
- **odessa-poissonnier** — dual-price promotion fixed (above); unit
  capture now lands on half the items. Names keep brand+origin and drop
  the product ("SEA-RAY INDE"); origin fragments ("QUÉBEC", "INDONESIE")
  still become items. One garbage multibuy parse ("15998/4001.00" →
  0.25) survives — a `prix_line`-style artefact in the anchor parser worth
  its own look. Tailored pass recommended.
- **mayrand** — boxes cover the price/name column only, so crops are
  faithful but partial (10/20); 5/20 items are badge/fragment names
  ("TOP", "Fresh", "MOM PRICE"); unit and size print in every cell
  ("/lb", "907 g", "2.84 L") — unit now captured at ingest, size needs the
  small-type block harvested (page-harvest stage). Its pdf_page source
  would suit a pdf_text-style tailored parser like Akhavan's.
- **marches-tradition / marche-bonichoix** — same flyer template family:
  lone-int prices and points-poisoning fixed by config; bonichoix also
  has the worst small-print name garble of the CC stores (9/10 sampled
  unclassified items are obvious products with unreadable names).
- **euro-marche / frutta-si** — densest grids in the set: neighbour
  intrusion in 8/10 and 7/11 crops, cross-product name/price swaps at
  frutta-si. Segmentation anchors on prices, not product regions; a
  cell-grid pass is the tailored fix for this template.
- **costco** — prix_line strategy is sound (17/20 ok); names carry
  spaceless merges (14/20) from the savings-book OCR; two-product cell
  merged once (price 12.99 belongs to one, name to both). All 10 sampled
  unclassified items have obvious categories (electronics, flooring,
  cheese, cleaners) — they are real products, just not groceries.
- **shop-sante** — worst name garble (supplement brand/product lines:
  "WMEGA 3 + D3 ETE"); all 10 sampled unclassified items are obvious
  supplements whose names are fragments. Vocabulary cannot fix names
  that were never read; per-store OCR settings are the lever.
- **marches-tau / marches-tradition / metro** — house layout prints the
  size **under the price** in nearly every cell: the single most
  harvestable size pattern for the page-harvest stage.
- **la-moisson** — brand line above every name, never parsed (G6);
  one junk-gate misfire fixed (seed butter, G4).
- **super-c / wholesale-club** — Flipp payload brand is null for these
  banners (G6); super-c also ingested a "$15 de rabais" app ad as a
  priced item.
- **mm-food-market** — 9/19 sampled items are price-badge fragments
  ("Plus taxes", "Prix pour 1") — correctly junk/Unclassified; one
  "50% de rabais" banner stored as price 50.0 (the lone-int family, but
  this store's config keeps bare ints for its real $ prices — needs the
  badge stoplist extended instead).
- **pa-nature** — chalkboard flyer: 3/3 prices wrong. Tailored OCR or
  accept-and-flag; no parser change fixes handwriting-style digits.
- **marche-korea** — clean product shots, sizes captured well; brand
  never split (G6); rice-cake items split between Bakery > Cakes and
  Pantry > Rice (both wrong — tteok belongs with East Asian / prepared
  rice products; a `tteok`/rice-cake phrase is the fix, needs a taxonomy
  call on the target subcategory).
- **t-t** — "/ch" units in small type after every price (now captured);
  names are OCR fragments ("concombre demer" — whose category the new
  phrase fixes anyway); multi-price cells (46.97/3lb + 59.97/ch) store
  one price with no marker of the second.
- **walmart** — one retailer-side image mismatch (squash item shows a
  mango photo — Walmart's own product image, not our crop); "spaghetti
  squash" category fixed.
- **canadian-tire** — one real crop defect: item 11673's crop holds only
  the cell's header line (bbox too shallow for text-anchored cells);
  specs print in the name line ("48 un.", "18,9 L", "10 po") — `po` now
  extracts; price *ranges* ("22,99-229,99") stored as single prices.
- **iga family** — Flipp shots carry no prices (data-only fields were
  verified); a recipe card was ingested as a product (G7); member-price
  badges ("PRIX MEMBRE") print with no loyalty flag stored — Flipp
  payload gap, same family as G6.
- **jean-coutu / brunet / familiprix / uniprix / pharmaprix** — pharmacy
  banners are clean on images; their gaps are counts-as-sizes (fixed in
  the extractor), bundle sizes (fixed), and store-prior judgement calls
  (Brunet supplements → Personal Care) that need a prior review, not rules.
- **3-saisons, bulk-barn, intermarche-palumbo, marche-andes,
  marche-bonanza** — tiny samples (1-3 items each); only the universal
  unit/size misses appear.

## Not fixed, and why

- **273 sampled sizes + most Flipp unit misses**: the data exists only in
  the flyer page image. Fix = a page-harvest stage (OCR each Flipp/OCR
  item's cell region for size/unit lines). The depictions are documented
  above per store, which is the spec for that stage.
- **Name garble/merges (162)**: per-store OCR tuning territory; the
  levers are known per store (small-print OCR at bonichoix/shop-sante,
  cell-grid segmentation at euro-marche/frutta-si, name-block growth at
  la-moisson/odessa) but each is its own tailored job.
- **134 category issues**: image-only distinctions and vocabulary tails;
  text classification is at its measured ceiling (81.6% GT).
- **77 promo items**: the exclusion layer that removes them is validated
  and awaiting approval to wire into ingest.
- **monde-au-naturel**: returns nothing until its tailored pass exists —
  preferable to 70 wrong prices, but it is a store outage to schedule.
