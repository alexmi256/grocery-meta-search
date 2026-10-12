# Phase 2 — Store deep-dives

## Objective

For each of the 123 Phase 1 stores, research the details needed to design the
database and to build the Phase 3 (flyer fetch + scrape) and Phase 5 (web search)
pipelines.

## Method rules (standing)

- RFD forums = store discovery only, NOT a reliable flyer/item source.
  RFD's Montreal flyers page (`redflagdeals.com/in/montreal/flyers/`) is a valid source.
- When a new store surfaces, check for parent-company relationships.
- No blank website without genuine investigation
  (official site → social → directory → "none found" with reason).
- Bilingual: check FR and EN variants of sites, flyers, and search.

## Tiers (effort follows pipeline value)

- **Tier 1** — major chains with flyers AND product search (~20–25). Full depth:
  every field in the YAML template.
- **Tier 2** — smaller chains/banners with flyers but limited or no search.
  Medium depth: website, flyers, locations mechanism, parent/affiliation;
  search section minimal.
- **Tier 3** — independents / single stores. Minimal record: website or social,
  flyers (usually none), the single location, no search section.

## Per-store fields

See `docs/research/stores/_template.yaml`. The YAML files are the table of record;
`docs/research/stores.md` carries a compact summary table for humans.

## Deliverables

1. `docs/research/stores/<slug>.yaml` — one per store (123), tiered depth.
2. `docs/research/stores.md` — compact summary table in tiered sections.
3. `docs/research/flyer-aggregators.md` — aggregator directory: coverage, formats,
   bot-friendliness, notes (Flipp, RFD flyers, circulaires.club, others found).
4. SQLite schema sketch — proposed by research, finalized after review.
5. Location harvesting (Phase 2b follow-up): Tier 1 chains → programmatic harvest
   via documented locator APIs into `data/locations/<slug>.json` with lat/lng.

## Analysis notes folded in (approved 2026-10-12)

- Flip weekday + timezone per flyer (QC grocery norm: Thursday, America/Toronto).
- Affiliation type (corporate vs independent affiliate) decides one-flyer vs many.
- Render tech / underlying JSON APIs and bot protection per source.
- Flyer archive availability (backfill + scraper testing).
- Flyer types per store (weekly grocery vs pharmacy vs general merchandise).
- Structured data in flyer HTML (JSON-LD / microdata).
- Loyalty-card-gated prices are a distinct price semantic.
- Search detail: location-scoped? guest OK? JSON API vs HTML? language toggle?
- E-commerce / click & collect presence as a proxy for structured product data.
- Canonical store slugs; machine-readable YAML as the DB seed source.
