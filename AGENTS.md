# AGENTS.md — working on grocery-meta-search

Guidance for any agent (or contributor) working in this repo. The
human's standing rules live here; follow them even when a task
doesn't repeat them.

## The project in one paragraph

Montreal grocery flyer meta-search: per-store flyer sources feed a
fetch pipeline that stores items in SQLite, classifies them
against the PC Express taxonomy, and repairs known source defects
(harvest, multibuy recovery) under strict per-store gates. Quality
is verified visually, store by store, against the flyer images.

## Non-negotiables

- **One flyer source per store.** No multi-source parsing without
  a very good reason (cross-checking validity dates is the
  sanctioned exception).
- **Sample first.** Any scraper, OCR or classifier change is
  validated on a sample or a scratch DB before it runs against the
  production pool. Save edge cases as test fixtures.
- **Confirm before destruction.** Before any mass deletion or
  DB-wide write: present the scope (what matches, how many items,
  which stores), state what stays, take a backup
  (`cp data/grocery.db data/grocery.db.bak-<yyyymmdd>-<tag>`),
  and wait for explicit approval. Backups stay on disk, never in
  git.
- **Unclassified is kept.** Unclassified items are never silently
  discarded. The only discard paths are: classified non-grocery
  departments (via `is_grocery`), the approved exclusion rules
  (`classify/exclusion.py`, Unclassified-only), and classifier
  junk (`method='junk'`).
- **No hand-correcting items as a fix.** The pipeline runs
  continuously; fixes are programmatic and store-specific where
  the store's layout demands it.
- **Run fetches sequentially, never in parallel.** Parallel
  refreshes degraded silently in the past (network timeouts under
  load, "ok" fetches storing partial editions). Smaller batches;
  verify counts after.
- **Check writes landed.** After any DB mutation, re-query and
  confirm counts before reporting success.
- **Ground truth before category changes.** The frozen corpus
  (`work/ground-truth/`) and its verdicts file adjudicate
  classification disputes — read the verdicts, not just the
  corpus category field.

## Engineering gates

Every change must pass, with exit codes checked unpiped
(a `| tail` masks failures):

```bash
.venv/bin/ruff check src tests
.venv/bin/mypy src            # strict
.venv/bin/python -m pytest tests/ -q
```

Two fixture tests are slow (~2 min each: PA chalkboard, Frutta Si
red-grid) and are routinely skipped during iteration with
`--ignore=tests/test_pa_chalkboard.py --ignore=tests/test_frutta_red_grid.py`;
run the full suite before calling a change done.

## Code conventions

- Per-store behaviour is config, not branches: OCR overrides in
  `sources/circulaires_club_config.json` / `official_stores.json`,
  stage enablement in `sources/harvest_config.json` /
  `sources/multibuy_config.json`, Metro Digital stores in
  `sources/metrodigital_stores.json`. Several config files are
  single-line-per-entry JSON — make surgical string edits, don't
  reformat them.
- Classifications are frozen at ingest; `pipeline/reclassify.py`
  is the sanctioned way to apply classifier changes to stored
  items. Guard remaps at the end of `classify_item`
  (`classify/rules.py`) are the sanctioned fix pattern for
  classifier traps — check the ground truth first.
- Store editions are skipped if already stored: re-fetching an
  edition means deleting the flyer first, in FK order —
  `price_observations` → `item_classifications` → `flyer_items`
  → `flyers`.
- Provenance goes in the item's `raw` JSON (`raw["harvest"]`,
  `raw["multibuy_recovery"]`, …), never in new ad-hoc columns.
- Credentials never enter the repo. Metro Digital keys are read
  from the banners' public app configs at fetch time; nothing
  secret is committed, logged, or printed.

## Layout reminders

- `data/` and `work/` are git-ignored working state (database,
  backups, caches, scratch DBs). Don't commit images, page-source
  dumps, or review-pack archives; the Markdown research notes in
  `docs/research/` are the durable record.
- Flyer research for a store lives in its YAML under
  `docs/research/`; narrative findings in the Markdown notes
  beside it. Update the note when a store's source or behaviour
  changes (see `docs/research/metrodigital-source.md` for the
  expected shape).

## Montreal specifics

- Store and flyer research runs in French and English; store
  names, item names and categories are bilingual in the data.
- Loyalty programs: Maxi/Provigo = PC Optimum, IGA = Scène+,
  Metro = Moi.
- RedFlagDeals forums are a discovery source only, never a flyer
  source; RFD's Montreal flyers page is a valid flyer source.
