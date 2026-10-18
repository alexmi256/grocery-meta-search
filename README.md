# Grocery Meta Search

A Flipp-style meta search engine for grocery and food items in the
Greater Montreal area. It discovers store flyers, ingests the
advertised items into a local SQLite database, classifies them
against the PC Express taxonomy, and tracks prices across weekly
flyer cycles. Later phases add proxied product search across store
websites and quality-of-life features (favorites, distance
filtering).

## Status

- **Phase 1 — store discovery: complete.** 245 Montreal-area
  stores researched; 67 carry a flyer or product-search source.
- **Phase 2 — store details: complete.** Websites, flyer sources,
  locations and banners recorded per store (`docs/research/` holds
  one YAML research file per store).
- **Phase 3 — flyer pipeline: live.** 60 stores ingest weekly
  flyers into the database (~6,300 items per cycle) from four
  source families (below). Seven stores are deferred (no usable
  flyer source).
- **Phase 4 — classification: live.** Text-only bilingual
  classifier over the PC Express taxonomy (17 departments, 112
  subcategories); measured at ~83% against a hand-labelled ground
  truth of 15,000 items. Refinement is continuous.
- **Phases 5–7 — planned:** proxied store web search, then QoL
  features. See [docs/PHASES.md](docs/PHASES.md).

## How it works

One flyer source per store. The fetch pipeline
(`pipeline/fetch.py`) dispatches each store to its source:

| Source | Stores | Mechanism |
|---|---|---|
| Flipp (FlyerKit + search API) | Loblaw/Sobeys chains, Walmart, pharmacies, independents | Structured payloads via Flipp's public APIs |
| Metro Digital API | Adonis, Metro, Metro Plus, Super C | Metro's own flyer platform API; credentials read from each banner's public app config at fetch time — see [docs/research/metrodigital-source.md](docs/research/metrodigital-source.md) |
| circulaires.club | Independent grocers, ethnic markets | Page images + OCR (RapidOCR detection + Tesseract) with per-store segmentation settings |
| Official sites | Costco, PA Nature, Marché Andes, BKR, Sultan, … | Per-store kinds: PDF text, page images + OCR, WooCommerce specials, flyer viewers |

After ingest, three repair/verification stages run per store where
enabled:

- **Page harvest** — fills package sizes / price units that exist
  only in the flyer image, by OCR-ing the item's own cell.
- **Multibuy recovery** — Flipp payloads collapse "2 pour 6$"
  offers into the bundle total; this stage OCRs the item's cell
  render and restores the printed unit price + multibuy terms
  under strict arithmetic gates. (Metro Digital stores carry
  multibuy structure natively and skip both OCR stages.)
- **Thin-edition guard** — flags a fetch that silently captured a
  fraction of an edition, by comparing the cycle against the
  store's own recent cycles.

Every stage is evidence-gated per store and keeps provenance in
the item's `raw` JSON. OCR stores get per-store tailored
segmentation where the generic pass falls short (chalkboard,
red-grid, name-cell and channel-title layouts are all handled as
store-specific strategies).

## Quick start

```bash
python -m venv .venv
.venv/bin/pip install -r requirements-dev.txt  # runtime + dev tools
# (runtime only: pip install -r requirements.txt; or `uv sync`)
# Seed the store/source registry from the research files
PYTHONPATH=src .venv/bin/python -m grocery_meta_search.seed \
  --db data/grocery.db \
  --brands src/grocery_meta_search/sources/flipp_brands.json \
  --search-merchants src/grocery_meta_search/sources/flipp_search_merchants.json \
  --cc-stores src/grocery_meta_search/sources/circulaires_club_stores.json
# Fetch current flyers (run stores sequentially, never in parallel)
PYTHONPATH=src .venv/bin/python -m grocery_meta_search.pipeline.fetch \
  --db data/grocery.db --slugs metro,adonis,super-c
```

Other pipeline commands (same `--db` shape): `pipeline.harvest`,
`pipeline.multibuy`, `pipeline.reclassify` (re-apply the
classifier to stored items), `pipeline.guard` (thin-edition
audit), and `classify.review_sample` (generate a per-store visual
review pack: sampled items + flyer crops for offline inspection).

## Engineering standards

- Python 3.11+, SQLite, git; Markdown for all notes and research.
- `ruff` (lint), `mypy --strict`, `pytest` — all three must pass.
- Sample-first: scraper or classifier changes are validated on a
  sample (or a scratch database) before they touch the full pool.
- Backups before any destructive database operation; mass changes
  are scoped and counted before they run.

## Layout

- `src/grocery_meta_search/` — application code
  (`sources/`, `pipeline/`, `classify/`, `ocr/`)
- `tests/` — pytest suite, including per-store fixture tests
  built from saved flyer samples
- `docs/phases/` — per-phase plans and deliverables
- `docs/research/` — research notes: source investigations,
  classification audits, per-store review passes
- `data/` — the SQLite database and its backups (git-ignored)
- `work/` — scratch databases, OCR caches, experiment files
  (git-ignored)

## Notes on data and credentials

The database and flyer-image archives are local working data and
are not part of this repository. No credentials are stored in the
repo: the Metro Digital source reads each banner's public
frontend config at fetch time, and the remaining sources use
public, unauthenticated endpoints.
