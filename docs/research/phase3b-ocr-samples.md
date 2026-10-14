# circulaires.club OCR samples & edge cases (2026-10-13)

Golden samples for the Phase 3b OCR pipeline. Line dumps (RapidOCR) live in
`tests/fixtures/cc_{store}_p1_lines.json`; page images were read visually to
establish ground truth. Tests: `tests/test_ocr_segment.py`.

## Round 2 (2026-10-13 evening): low-yield store fixes

First-pass yields were near zero for 6 stores. All diagnosed visually +
with line-level debug (`work/cc-check/debug_page.py`); fixes are a mix of
segmentation features and per-store configs. New fixtures:
`cc_odessa_p2_lines.json`, `cc_palumbo_p1_lines.json`.

- **Low-res pages** (Odessa 993px, Palumbo 1020px, Frutta Si 832px):
  pipeline now upscales pages to ≥1600px wide before OCR
  (`upscale_for_ocr`); relative-fraction configs are unaffected.
- **Odessa** (magazine layout, 2 products/page): prices print as
  "10⁹⁹ $/lb" and OCR returns junk-glued lines ("1099 S/6", "2423 8/kg*")
  that the fragment parser rejected. Fixes: merged-run scan of tall
  non-digitish lines, per-fragment token recovery when a cluster fails
  to parse whole, `bare_int_anchor=false` (the "RABAIS 8 $" badges are
  discounts, not prices), `name_max_h_frac=0.032` (names are tall on
  low-res pages). Known miss: goberge "8⁹⁹" reads "099" → 0.99 stored
  as alt price (true $/lb price), 19.82 $/kg is primary.
- **Palumbo** (dense 1-pager): names sit ABOVE prices with the next
  product's name just below each price → nearest-neighbour swapped
  names. Fixes: `name_position=above`, `match_dx_weight=2.5` (column
  preference), `block_min_overlap_frac=0.25` (a wide detection box —
  "HARICOTSBLANCS" 50→486 — bridged two product columns),
  dual-anchor same-box pre-fold. Result 7/8 products correct; wart:
  the oil sometimes takes its regular price (14.99) as primary when
  the sale anchor's name seed is the "CEDAR" bottle-brand line.
- **Bulk Barn** (diagonal grid: name top-left, price circle
  bottom-right): added `name_position=above_left` (correct name's
  centre is always left of the price centre); stoplist for the
  "était/was" reg-price lines and "DE RABAIS" banners. 6/6 on p1.
- **Tau**: `name_case=any` + `bare_int_anchor=false` (kills the
  "ÉCONOMISEZ 27 $" badge item). p1: 2 → 11 items.
- **Valmont**: `name_case=any` + cents. p1: ~4 → 15 items. Remaining
  errors are glyph confusions: "99"→"66" (10.99→10.66, 5.99→5.66),
  "2/7$"→"2.17" ("/" read as ".1"), "2/99¢"→"21.99", and a lone "14"
  dollar fragment read as 0.14 under bare_int_is_cents. Phase 4
  quarantine candidates (price outliers), not fixable in segmentation.
- **Frutta Si**: grid prices' dollar digits are invisible to the
  detector at any tried enhancement (only superscript cents are found,
  often misread "99"→"66"). Upscaling recovers the hero prices:
  ~7 correct items/page of ~35. Documented limitation; a cents-anchor
  dollar-crop recovery is a Phase 4 candidate.
- **Shop Santé**: genuinely sparse lookbook (1 product/page, small
  price tags) + the site serves 1×1 placeholder webps for pages 4 and
  11 of the current edition. Pipeline handles both fine; no config.
- **La Moisson**: low yield is genuine (mostly %-off promos, almost
  no priced items).

## marche-bonichoix p1 (1600×3549) — classic weekly flyer

Ground truth (10 items): bavette de bœuf 15.99 $/lb; combo de saucisses
fraîches 6.49; tourtière/gratin/pâté 7.44; framboises 2/5.00 (2.50 ch.);
mélange de laitues Attitude 5.99; céréales General Mills 3.33; fromage
P'tit Québec 4.97; Coke ou Pepsi 12pk 6.99; mayonnaise Hellmann's 5.97;
bière 30pk 40.99.

Pipeline result: 10/10 items. Edge cases:

- **9→6 digit confusion**: beer cents read "66" (conf 0.98) → price stored
  40.66 instead of 40.99. Tesseract can't read the stylized price font
  either (crop test). Accepted limitation; Phase 4 quarantine candidate.
- **Multibuy pair**: "2/5⁰⁰" + "2⁵⁰ Ch./ea." are two anchors for one item;
  pipeline keeps per-unit 2.50 and records the multibuy in conditions.
- **"NET WT / POIDS NET" line on the salad photo** is closer to the price
  than the real name block → stack-aware seeding (multi-line blocks win).
- **"PRIX INCROYABLE" badge** overlaps the fromage/mayo name crops;
  Tesseract reads it first → token-overlap fallback to detected lines.
- Header date line and store logo must not become name blocks (height
  window + stoplist).

## t-t (T&T) p1 (1280×1629) — dense trilingual grid

Ground truth: ~25 items (melon hami 0.68¢; chou napa 1.48; filet saumon
bio 14.98; anguille grillée 8.88; ailes de poulet 2.99; côtes levées porc
5.99; TC ravioli 2/14.97 ou 7.97/ch; Watson magret 8.97; nouilles
Nong Shim 4.97; Dan-D Pak noix 13.97/18.97 dual; riz Golden Royal Ox
21.97; dumpling festival section with ~14 more).

Pipeline result: 16 items, most prices right; name assignment in the
dense grid is the weakest of the three samples (some swapped/junk names,
e.g. melon↔chou). Settings: `name_case=any`, `price_min_h_frac=0.016`,
`bare_int_is_cents=true`. Edge cases:

- **Cents-only price "68¢"**: the ¢ glyph is not detected as a line;
  a lone full-height 2-digit fragment is treated as cents (per-store cfg).
- **Lost dollar digit**: chou "1 48" → only "48" detected, at sub-normal
  height → anchor dropped by the median-height rule rather than emitting
  a wrong 0.48.
- **"9.99" read as "6.66"** (raviolis crevettes) — same 9/6 confusion.
- **Date badges** ("10/9-10/12") parse as multibuy fragments; they fold
  into neighbouring items' alt_prices instead of creating false items.
- Chinese name translations are filtered from name candidates (CJK ratio).

## costco p1 (1600×2829) — savings book (prix_line strategy)

Ground truth (10 priced items): téléviseur Samsung 65po 1511.74;
téléviseur Mini DEL 85po 1094.99; téléviseur Mini DEL 65po 744.99;
barre de son Samsung 252.74; chandail Sierra Design 19.99; téléphone
Samsung A37 449.19; haut-parleur MX-ST4CF 300.94; ordinateur Galaxy
Book6 999.99; moniteur Odyssey G5 208.49; plancher Sutton 24.99.
Two promo cells (Lennox, pneus Michelin) have no Prix line → skipped.

Pipeline result: 10/10. Edge cases:

- **The big green number is the SAVINGS, not the price** ("ÉCONOMISEZ
  500 $"). Prices come only from small "Prix X,XX $" lines.
- **Garbled Prix amount**: laptop "999,99 $" OCR'd as "$66666" → price
  derived from the same cell: En entrepôt 1 149,99 − Économie 150,00
  = 999,99 (flagged `price_derived`, confidence 0.7).
- "$" read as "S" ("1 149,99 S") — amount regex tolerates a missing $.
- Membership banner lines above the first row must not leak into names
  (stoplist: "pas encore membre", "inscrivez-vous").

## Group 4 — official platforms (2026-10-14)

New source kinds in `sources/official.py`: `image_page` (Wix and generic
extractors), `pdf_page` (pymupdf render → OCR), `woo_specials`
(WooCommerce Store API, structured), `flyerify` (offer discovery → page
images). Page-1 OCR validity (FR range parser) overrides fallbacks.

Edge cases found:

- **Spaceless validity headers**: RapidOCR drops spaces in caps text, so
  Milano's header is one token run "CIRCULAIREVALIDEDU08AU21OCTOBRE
  2026". `parse_fr_validity` retries with all spaces squashed.
- **Cents glyph merged into the digit run** (3 Saisons): "79¢" detects
  as a single tall line "799" → parsed as 7.99 without help. Per-store
  `merged_run_is_cents` rule: a 3-digit run ending in 9 is dollars-less
  cents (first two digits). Cross-checked against the printed $/kg line
  (0.79/lb ≈ 1.74/kg ✓).
- **Very tall pages defeat the detector** (Wholesale Club ~6100px,
  H Mart 5470px): RapidOCR downsamples internally, only ~60 lines
  survive. `detect_lines_banded` slices the page into 2000px bands with
  overlap, detects per band, merges + dedupes.
- **Cloudflare bot cookie hangs follow-up requests** (Marché Korea Woo
  API): first request in a session ~1s, second request carrying the
  `__cf_bm` cookie times out at 120s. Fix: clear cookies before every
  page request.
- **Superscript prices lose the dollar digit** (Aliments Merci PDF):
  "7⁴⁹$" sometimes clusters as "49" alone → stored as 49.0 instead of
  7.49. Names are right; ~half of page 1 prices affected. Phase 4
  quarantine candidate.
- **Vendor flap inserts have no prices** (Wholesale Club pp. 2-3):
  points-promo inserts ("OBTENEZ 15 000 pts") correctly yield ~0 items.
- **Price-less new-arrival posters** (Marché Korea weekly flyer page):
  the posters carry no prices at all; the store's priced content is its
  WooCommerce sale catalog (162 products) — onboarded via `woo_specials`
  instead.
- **Stale flyer not imported** (Baia dei Formaggi): the specials page
  still shows an Italian Father's Day edition valid June 17 - July 1,
  2026. Config kept; nothing imported with fabricated dates.
