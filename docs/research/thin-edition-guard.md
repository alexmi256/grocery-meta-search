# Thin-edition guard

`src/grocery_meta_search/pipeline/guard.py` — flags flyer cycles whose
stored item count collapsed versus the store's own recent cycles.

## Why it exists

On 2026-10-17, Marché Bonanza's current flyer held 2 items in the
database; the real edition has 26. Diagnosis: the 2026-10-16 refresh
ran stores in parallel under load, network timeouts silently truncated
the fetch, and the partial edition was stored with `fetch_status`
'ok'. Because `store_editions()` skips editions that are already
stored, nothing ever topped it up. A solo-fetch audit of all 27
suspect stores found **11 partially captured stores** (Bonanza 2/26,
Canadian Tire 65/302, T&T 41/130, Walmart 232/322, Valmont 11/35,
Marché C&T 33/58, Fu Tai 36/56, Sheng Tai 34/52, Wholesale Club
58/85, Euro Marché 39/50, Coop Alentour 11/16); all were repaired by
deleting the edition and re-fetching solo.

The lesson: **fetch success status cannot detect a partial capture —
only the item count can.** The guard automates that count check.

## What it does

After every store fetch (and on demand, see below), the guard:

1. Groups the store's flyers into **cycles** by `valid_from`. All
   publications starting the same day are one cycle; their item
   counts are summed. (Uniprix runs 3 concurrent publications;
   Walmart runs a weekly plus a long special — both aggregate
   correctly under this rule.)
2. For each cycle still valid today, computes a **baseline**: the
   median item total of the up-to-3 most recent earlier cycles.
3. **Flags** the cycle when both hold:
   - current total < `RATIO` (0.5) × baseline, and
   - the absolute shortfall is at least `MIN_DROP` (10) items
     (so tiny stores with 1–5-item cycles don't trip on noise).

The guard is **advisory**. It never fails a fetch, never deletes or
changes items, and never re-fetches on its own. When it flags, it:

- appends a `WARNING: THIN EDITION …` line to the fetch report, e.g.
  `THIN EDITION marche-bonanza cycle 2026-10-14..2026-10-20: 2 items vs baseline 27 (prior cycles 2026-10-07: 27) — verify with a solo re-fetch`
- stamps every flyer of the thin cycle: its `raw` JSON gains a
  `thin_edition_guard` record (`flagged_on`, `current`, `baseline`,
  `prior_cycles`), so flags are queryable later, e.g.
  `SELECT store_slug FROM flyers WHERE raw LIKE '%thin_edition_guard%'`.

Constants (`RATIO`, `BASELINE_CYCLES`, `MIN_DROP`) live at the top of
`guard.py`.

## Standalone audit

To check a database without fetching (e.g. after a big refresh):

```
PYTHONPATH=src .venv/bin/python -m grocery_meta_search.pipeline.guard \
    --db data/grocery.db [--slugs a,b] [--today YYYY-MM-DD] [--stamp]
```

Prints one line per flagged cycle, or `no thin editions`. `--stamp`
also writes the `thin_edition_guard` records (the fetch path always
stamps).

## Responding to a warning

A warning means "verify", not "the data is wrong":

1. Solo-fetch the store into a scratch DB and compare edition totals
   (the audit method of 2026-10-17; script pattern in
   `work/tiers/audit_sweep.py`).
2. If the solo fetch stores substantially more, the production
   edition is a partial capture. Repair: back up the DB, delete the
   edition's rows in FK order (`price_observations` by flyer_id →
   `item_classifications` by item_id → `flyer_items` → `flyers`),
   re-fetch the store solo, confirm the count matches the solo run.
3. If the solo fetch matches production, the cycle is genuinely
   smaller (rotating publications, seasonal flyers) — no action.

## Validation (2026-10-17)

- 8 unit tests (`tests/test_guard.py`): aggregation across
  publications, collapse flags, normal variance passes, no-history
  passes, tiny-store floor, expired cycles ignored, zero-item cycle
  flags, raw stamping.
- **Incident replay**: run against the pre-repair backup
  (`grocery.db.bak-20261017`), the guard flags 5 of the 11 partial
  stores — the catastrophic ones (Bonanza 2 vs 27, Valmont 11 vs 43,
  Canadian Tire 65 vs 698, T&T 41 vs 110, Walmart 232 vs 510).
- **Post-repair production**: the only flags are Canadian Tire (302),
  Familiprix (137) and Uniprix (32) — all three verified complete by
  solo fetch. Their baselines are inflated onboarding cycles (698 /
  831 / 246 items: onboarding stacked several captures/publications
  under one `valid_from`). These false warnings wash out as normal
  cycles accumulate into the median-of-3 — Canadian Tire's baseline
  becomes 302 once two normal cycles are in its history.

## Limits

- **It catches collapses, not moderate degradation.** Euro Marché at
  78% of baseline, Marché C&T at 56%, Coop at ~69% were all partial
  captures the guard does not flag. The solo-fetch audit remains the
  thorough check; the guard is the cheap always-on tripwire.
- **No baseline, no flag.** A store's first stored cycle can be
  partial without tripping anything.
- **Rotating publications can trip it legitimately.** Pharmacies whose
  publication mix changes week to week (Uniprix) may warn on a full
  capture; verify before repairing (step 1 above).
- **A thin cycle left unrepaired enters later baselines.** The
  median-of-3 tolerates one poisoned prior; two in a row lower the
  bar. Repair flagged editions promptly.
