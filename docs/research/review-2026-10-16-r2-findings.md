# Visual review round 2 — findings — 2026-10-16

Same exercise as round 1, commissioned 2026-10-16 evening: 10 random
classified + 10 random unclassified items per store from current
flyers only (seed 202610162), every item judged with its flyer image
as the source of truth, then the same fix types as round 1. Pack:
`review-2026-10-16-r2/` (59 stores, 704 items, 0 missing pictures;
only Aliments Merci skipped — no current flyer).

Method addition: for every name/brand defect, the item's crop was
checked for whether the correct text is present in it —
present-but-garbled is an OCR-reading defect; absent/cut-off is a
crop/bbox defect. **Verdict on that question: the crop hypothesis is
substantially right.** Poster cases were pure crop geometry: Newon
price blocks clipped at the crop's right edge; Mayrand bboxes cover
only the spec/price column (names stored literally as 'Fresh' /
'FRAIS'); Coop Alentour sizes printed *below* the bbox (fixed, see
below); La Moisson names left-clipped. Other stores (Bonichoix,
Tradition) assemble fragment-only names although the full text sits
inside the crop — a name-assembly defect, not OCR reading.

## Image verdicts (704 items)

| verdict | count | |
|---|---|---|
| ok | 366 (52%) | |
| partial | 287 (41%) | |
| promo_only | 51 (7%) | |
| wrong_product | 0 | |

Calibration note: round 2's 'partial' is **not comparable** to
round 1's 72. OCR-store sheets show page-fragment crops by design,
and round 2 judged any fragment that did not show the whole product
as partial. It is a judging-calibration difference, not a data
regression — wrong_product went 3 → 0 and promo_only 77 → 51.

## Field issues: 445 across 352 items (round 1: 1,023)

| kind | round 2 | round 1 |
|---|---|---|
| name:wrong | 125 | 162 |
| category:missing | 87 | 45 |
| price:wrong | 81 | 101 |
| category:wrong | 42 | 103 |
| size:missing | 37 | 308 |
| unit:missing | 29 | 188 |
| size:wrong | 21 | 19 |
| unit:wrong | 18 | — |
| brand:wrong | 5 | — |
| brand:missing | — | 94 |

The harvest stage did its job: size misses collapsed 308 → 37 and
unit misses 188 → 29. What remains is dominated by name defects
(run-together OCR names) and price defects (dual-price cells,
multibuy conventions).

## Fixes applied

All stored-pool changes sit under backup `data/grocery.db.bak-20261016h`.

1. **Reclassification pass (new)** — `pipeline/reclassify.py`.
   Classifications are frozen at ingest, so round 1's rule fixes
   never reached stored items (the single largest round-2 pattern).
   The pass recomputes every stored item with the current rules:
   **175 category flips** on the pool. Dry-run flips were audited by
   transition class before the real run; the audit caught four bad
   classes (ground veal, yogurt/cheese bars, ice-cream bars,
   barcode-instruction text) that are now guarded and tested.
2. **Classifier** — 18 targeted traps and ~30 vocabulary additions
   from the sample, 10 guard remaps, 2 new specific rules
   (yogurt/cheese bars), junk-gate additions ('gift card',
   'code barres' substrings). Each sampled case was verified against
   its stored name first: **60/61 land as intended** (the one miss is
   a glued token, 'aubeurreKFI'). Ground truth: **82.3% of items /
   79.9% of signatures, up from 81.6% / 79.2%.**
3. **fields.py guards, applied** — reprocess corrected **58 stored
   sizes**: SKU-as-size on PC-banner stores, protein-callout badges
   ('23g de protéines'), stitched monsters ('11998739650g', '2.56-396L'),
   hardware load ratings stored as package sizes.
4. **Prices** — multibuy each-prices now round to cents
   (was 2.4699999999999998-style float tails); segment.py accepts
   comma-decimal multibuy totals ('2/5,99' → Bonanza Activia 10.00 →
   3.00 with the 2/5.99 condition recorded); `merged_run_is_cents`
   enabled for fruiterie-valmont and frutta-si (bananas/oranges
   6.99 → **0.69**, verified by re-fetch); **56 stored prices**
   rounded in flyer_items + price_observations.
5. **Harvest** — per-unit price references no longer pose as package
   fields: a denominator ('0,50/100 g') never fills size, and is not
   a pack item's unit (weighed goods keep it). New
   `--refresh-harvested` mode retracts/updates earlier fills:
   giant-tiger −3 wrong units, +4 blocked sizes (jam '375-500 ml',
   Activia '12 x 100 g'). Coop Alentour crop pad extended downward
   (sizes print below the bbox): +4 sizes, incl. all three sampled
   gaps ('284 g', '400 ml', '200 g'). **22 oversize harvest sizes
   cleared** ('66L' celery/potatoes/towels, '154 L'/'458l' juice
   stitches, '88L' pork feet): 15 via the reprocess caps, 7 via the
   25 L harvest cap (audit: `work/tiers/oversize-clear-2026-10-16.json`).
6. **Exclusion audit** — the stored Unclassified pool was re-checked
   against the exclusion layer: **0 matches**. Round 1's application
   plus the wired ingest already keep it clean. The round-2
   banner/slogan candidates (Metro/Super C Moi slogans, gift-card
   promos) are classifier-junk; ingest keeps junk as Unclassified
   for review, so they stay — no new deletions were sanctioned.

Pool after: **14,920 items; Unclassified 1,234 → 1,167 (8.3% → 7.8%)**.
Gates: 125 tests (was 115), ruff clean, mypy strict clean.

## Not fixed — documented mechanisms

- **Run-together OCR names** (Tau, M&M, T&T, Costco, Marché Korea,
  Frutta-Si): spaceless names defeat the tokenizer's word boundaries;
  ~a third of the residual name:wrong and several category misses.
  Per-store name-assembly work, not a rules problem.
- **Dual-price unit trap** (9+ sampled items, 7+ stores): the
  headline $/lb figure is stored with the kg reference unit (or vice
  versa). Odessa's `fold_alt()` is Odessa-only; a general fix risks
  the stores that are consistent — per-store tailored work.
- **Flipp-payload multibuy totals** (Metro, Metro Plus, Marché PA,
  Kim Phat): the wishabi payload carries only the collapsed number
  ('6.0' for '2/6$') with no multibuy text to parse. Not recoverable
  from the payload; image-based price harvest would be a new
  feature, not a fix of round-1 type.
- **9→6 glyph errors** (7+ items): stochastic per OCR run —
  re-fetches flip 1.99↔1.66 with no code change. No safe global fix.
- **Cross-cell contamination** (Wholesale Club, Uniprix merged
  cells; Provigo/Wholesale either/or items taking the other
  product's size): segmentation-level, per-store.
- **Cents-as-dollars** beyond the two configured stores, and
  garbage prices from count/format figures (Tradition 66.0/50.0,
  Esposito, Euro-Marché): the pattern is confirmed but each store's
  print layout differs; enabling `merged_run_is_cents` store by
  store on evidence is the safe path.

## Awaiting a go-ahead (unchanged from round 1)

- **monde-au-naturel tailored pass** — the round-2 sample is again
  10/10 'SPÉCIAL 15/20/25 %' badge fragments classified as vitamins
  with the % stored as price. The store yields no usable items
  until its detection is tailored, like Akhavan's was.
- **Odessa tailored pass** — 9/10 sampled unclassified items are
  origin-line fragments ('QUÉBEC | QUEBEC', 'INDONESIE'…); the
  products are lost at name assembly, before classification.
