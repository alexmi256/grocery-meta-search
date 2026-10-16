# Page-harvest stage — design, store matrix, validation

Built 2026-10-16 on Alex's commission, following the visual review
(`review-2026-10-16-findings.md`, groups G1/G2): 273 of 308 sampled
missing sizes (and most Flipp unit misses) exist **only in the flyer
page image** — the Flipp payload carries no size text (verified:
`text_areas` empty, no size field), and the OCR segmenter drops
size-only lines. This stage OCRs each affected item's flyer cell and
fills `package_size` / `price_unit`.

## Which stores need it — the determination

For every store with a current flyer: (a) the share of current items
already carrying a size/unit, and (b) the review samples proving the
flyer *prints* the field (an item can only be harvested if the flyer
depicts it). A store is enabled when coverage is low AND the samples
show the field printed. Config: `sources/harvest_config.json`
(store-level; presence enables, `fields` selects size/unit, `pad`
overrides crop padding).

**Enabled (49 stores).** The big gaps: metro / metro-plus (417 items
each, 1% sized, 11/20 sampled misses), super-c (250, 0%), iga family
(~360 each, 5–6%), marche-pa (194, 1%), adonis (193, 2%), pharmaprix
(784, 30% — counts print on packaging), walmart (232, 9%), jean-coutu
(400, 1%), brunet (332, 3%), plus the OCR family where the size line is
printed but dropped at segmentation: marches-tau (3% sized, 15/20
sampled misses — size under the price in nearly every cell),
marches-tradition, marche-bonichoix, marche-ami, marche-richelieu,
marche-lian-tai, kim-phat, t-t (9 size + 7 unit of 10), milano-fruiterie
(unit on 14/14 sampled — per-100 g house style), euro-marche,
marche-esposito, marche-newon, marche-fu-tai, marche-c-t,
marche-sheng-tai, fruiterie-valmont, frutta-si, h-marche, mayrand,
odessa-poissonnier, marche-sultan, marche-bkr, la-moisson, shop-sante,
coop-alentour, marche-axep, l-intermarche, avril, rachelle-bery,
familiprix, uniprix, giant-tiger, canadian-tire, costco,
mm-food-market, wholesale-club, bulk-barn (unit only).

**Not enabled, with reasons:**
- akhavan — structured pdf_text source already sets size (89%) and
  unit (100%).
- maxi, provigo — 91% / 87% sized from names; sampled misses 1 and 3.
  Not worth the OCR pass.
- marche-korea — 92% sized, and its items carry no bbox/image region
  (structured Woo source).
- marche-andes — no bbox, no cell image (2 items).
- pa-nature — chalkboard flyer; OCR does not read its prices, let alone
  its sizes (3 items).
- monde-au-naturel — no current items (source broken, see findings).
- intermarche-palumbo, marche-bonanza, 3-saisons — 1–2 items each,
  negligible.

## How it works (`pipeline/harvest.py`)

Per item, decided by shape (`mode: auto`):

- **Flipp-shaped items** (image_url on wishabi): the item image is the
  flyer's cell-region render — it contains the printed text block
  (super-c: "132 g, choix varié" sits in the image) — or the product
  cutout, whose label often prints the size (IGA Nutella: "725 g" on
  the jar). OCR the item image directly; no page fetch or geometry
  needed. (The Flipp page geometry in flyers.raw is therefore not
  needed for harvest.)
- **OCR items**: crop the flyer page at the item's normalized bbox and
  OCR the crop. PDF flyers (mayrand) render their page first.

Extraction policy (conservative — an empty field beats a wrong one):
- size fills only when the cell yields exactly one distinct size, or
  several that the fields policy resolves to a weight/volume while all
  rivals are counts ("60-70 UNITÉS" beside "907 g"); descending ranges
  are rejected as OCR garble.
- unit fills only when exactly one distinct price unit appears.
- Only missing fields are filled; provenance is recorded in the item's
  raw JSON (`harvest: {size|unit, via: image|crop}`).

Runs at ingest (fetch_store, for enabled stores; a harvest failure
never fails the fetch) and standalone for backfills. Downloads + OCR
are parallelised (6 threads); DB writes stay serial.

## Validation (sample-first, image as truth)

Dry runs (30 candidates each): Tau +17 size/+1 unit, super-c +16/+3,
metro +11 size/+6 unit — fill rate ≈ 50% of candidates, 0 missing
images. Then 20 harvested values were checked against their cell
images:

- **Correct: 16.5/20.** All 8 super-c fills (132 g rice, 907 g dates,
  750 ml juice…), Tau's under-price sizes (156–198 G chips, 355 ML,
  500–650 G yogurt), metro's Hellmann's 710–890 ml, Pringles 456 g,
  mango "l'unité" → each.
- **Wrong: 3.5/20, in three classes.**
  1. *Neighbour intrusion (2, both Tau crops):* the judging crop's
     +35% top padding reached into the cell above and imported its
     size line. **Fixed:** harvest crops pad up only 8% (down 20% —
     sizes print under the price). After the fix, the shrimp item
     fills its own "300 G"; the other case persists because the
     item's bbox itself merges two products at segmentation
     (upstream defect, not harvest's).
  2. *OCR garble (1.5):* metro cheese — two format ranges stitched
     into a descending "250-220g". **Fixed:** descending ranges are
     rejected; the item now correctly stays empty. Blueberries:
     "Cat. No 1, 170 g" merged into "1.170g" — digits right, form
     corrupt; left as a known artefact.
  3. *Dual-price unit (1):* metro grapes print "3,99/lb" headline
     with "8,80/kg" reference; OCR caught the kg line only and filled
     unit=kg. Same family as the Odessa trap; position/typography
     disambiguation is future per-store work.

Post-fix precision ≈ 88% on the checked sample, with the policy
preferring empty over wrong everywhere it can detect doubt.

## Backfill (2026-10-16, backup `data/grocery.db.bak-20261016g`)

6,119 candidates across the 49 enabled stores → **+2,402 package
sizes and +655 price units** (2,821 items carry harvest provenance).
Current-flyer coverage after the backfill: **size 54.6%** of 6,702
items (DB-wide 2,729 → 5,128 values), **unit 12.0%** on current items
(DB-wide 265 → 935). Biggest wins: metro +231 size/+50 unit and
metro-plus the same again (identical flyer), iga family ≈ +510 sizes,
marche-pa +110/+16, adonis +99/+39, brunet +145, super-c +142/+6,
pharmaprix +140, kim-phat +62/+24, lian-tai +45/+45, and in the re-run
(below) tradition +37, bonichoix +32, esposito +18 size/+30 unit,
newon +25/+42, milano units +15/15 (its per-100 g style finally
recorded).

Two operational incidents, both fixed and re-run to completion:

1. **Cache race (round 1):** page fetches were not single-flight —
   worker threads fetching the same page URL wrote the same cache
   file concurrently and corrupted each other's reads, and the
   failure was cached for the whole run. Every single-page crop store
   lost all its items (tradition, bonichoix, euro-marche, t-t, …) and
   two image stores lost some (iga 22, iga-extra 66). Fix: page
   fetches are single-flight under a lock with one retry; the 27
   affected stores were re-run (+305 size, +350 unit).
2. **flyerify.com transient failure:** wholesale-club's page host
   failed every fetch during both parallel runs but answered
   immediately afterwards (rate limiting under load is the likely
   cause; not reproducible since). Solo re-run: +2 size, +32 unit —
   its sizes were already in names; the units were the real gap.

Residual known error classes (from validation, unchanged): fills from
bboxes that merge two products at segmentation; dual-price unit
references (kg where lb is the headline); rare OCR digit merges
("1.170g"). All are recorded with `via` provenance so a later audit
can isolate harvested values.
