# Phase 3 — Flyer pipelines

## Objective

Build the two chained pipelines that run daily: (3a) fetch the latest flyers
per store, (3b) scrape items from flyers into the database.

## Approved scope (user, 2026-10-12)

- **Phase 3: greater Montreal area stores with a flyer — 67 stores.**
  (footprint island/greater/qc-confirmed AND flyers.has_flyers=true)
- Future phases (5+): greater Montreal stores with a flyer OR product search — 108.
- The 7 exclusion candidates stay flagged as-is in the research data; the research
  stands, and scope filtering handles them downstream.

## Source selection policy (user, 2026-10-12)

- **One source per store**: the source with the easiest-to-extract data for both
  the flyer itself and its items (record the choice in `flyer_sources`).
- Do NOT parse the same flyer edition from multiple sources without a very good
  reason — no duplicate parsing pipelines per store.
- Sanctioned multi-source use: cross-checking a flyer's **validity period** when
  the primary source's dates are ambiguous or missing (e.g. aggregator lists
  explicit dates the official viewer omits).

## Key research inputs (from Phase 2)

- **Primary flyer source for majors: Flipp's FlyerKit JSON API**
  (`dam.flippenterprise.net/flyerkit`) — structured products over plain HTTPS,
  proven by an open-source scraper covering 25 Canadian chains. Bilingual via
  `locale` param.
- **Official sites mostly bot-walled**: Loblaw group behind Akamai, Walmart behind
  PerimeterX, Canadian Tire behind Akamai → use aggregators there. Exceptions with
  directly scrapable official flyers: T&T (structured HTML), Marché BKR
  (circulaires.com), Familiprix (JSON API).
- **Per-banner flip config, not one global cron**: Thursday norm, but T&T flips
  Friday, Pharmaprix Saturday, Costco 14-day cycles, La Moisson biweekly.
  Scheduler reads flip_weekday/flip_timezone/duration_days from research.
- **Affiliate banners need per-banner fetching** (Metro/Sobeys/AXEP groups);
  C&T and Première Moisson confirmed per-store flyer variants.
- **Card-gated prices are a distinct price semantic** (PC Optimum, Scène+,
  Familiplus) — record loyalty_gated on items.
- **Probe before building**: Giant Tiger Shopify `/search/suggest.json`,
  Jean Coutu/Brunet Azure Functions flyer endpoints, `api.metro.ca`,
  Épicure `/search/suggest.json`.
- Flyer aggregator directory: `docs/research/flyer-aggregators.md`.
- Per-store source/format/fetchability: `docs/research/stores/<slug>.yaml`
  → seed table `flyer_sources` (schema: `docs/research/schema-sketch.md`).

## Pipeline 3a — flyer fetching

### Edition identity
Key each edition by (store_slug, flyer_type, valid_from, valid_to). Re-running the
fetcher on an already-stored edition is a no-op, never a duplicate.

### Change detection
Hash every fetched artifact (PDF/image bytes; normalized JSON/HTML for structured
sources). If a stored edition's hash changes mid-week, version it and re-queue it
for scraping rather than duplicating or ignoring it.

### Validity parsing
Parse explicit dates first ("8–14 oct", "du 8 au 14 octobre"). Fallbacks, in
order: flip-weekday + fetch date inference; cross-checking other sources'
validity listings (the sanctioned multi-source use). All dates in
America/Toronto.

### Scheduling
Per-banner flip config drives the daily chain; retries with backoff on failure.
Missing editions are normal before flip time — not errors.

### Provenance & storage
Every flyer records: source URL, fetched_at, content hash, fetch_status.
Artifacts live under `data/flyers/<store_slug>/<edition_id>/` (`archive_url`).

### Language versions
Fetch EN and FR editions where both exist (often the same fetch with a locale
param). Bilingual single-edition flyers are recorded once with languages=[fr,en].

### Per-store variants
For banners with per-store flyers (C&T, Première Moisson), fetch the Greater
Montreal locations' editions and dedupe byte-identical ones.

### Politeness
Rate limits per host, a real user-agent, robots.txt respected. Never route
around a bot wall — switch to the sanctioned source instead.

## Pipeline 3b — item scraping

### Item identity & price history
The same product recurs weekly — daily runs must build price *history*, not piles
of duplicates. Compute a stable `item_key` per (store, product):
`sha1(store_slug + "|" + normalized_name + "|" + price_unit)`, where
normalized_name is lowercased, whitespace-collapsed, punctuation-stripped
(accents kept). Feeds `price_observations`; SKU replaces the fingerprint when a
product link yields one.

### Cross-language dedup (approach)
One item row carries both languages: `name_fr`, `name_en` (either nullable).
- Separate EN/FR editions of one flyer: match items across versions by same
  page/position + image hash; tie-break on price+unit+validity. Merge, don't duplicate.
- Bilingual single flyers: split dual-language names on `/` patterns
  ("Pommes / Apples"); when inseparable, store the raw string in the matching
  language field and leave the other null.
- `item_key` uses the French name when present, else English (Montreal-primary).

### Price parsing (Quebec formats)
Handle `5,99 $`, `2/5$`, `$/lb` vs `$/kg`, "avec carte", "à l'achat de 2".
Compute effective unit price for quantity offers (`2/$5` → $2.50). Keep the raw
price string alongside the parsed value.

### Evidence: images, bboxes, raw text
Per item store: the item image (content-hashed for dedup), its bounding box on
the source page (for image/PDF flyers), and the raw text/HTML snippet. Enables
user-facing display, later re-OCR, re-parsing after parser improvements, and
human verification. HTML flyers: images come from markup. Image-only flyers:
detect product regions on the page. PDFs: text layer when present, vision
fallback when the PDF is image-wrapped.

### Confidence & quarantine
Every scraped field carries a confidence score (critical for OCR-derived data).
Below-threshold items go to a quarantine queue with reasons — never silently
into the DB. Track per-store parse quality over time.

### Conditions & flags
Generalize "weekend-only" to a conditions extraction: sub-periods, "jusqu'à
épuisement", "limite de X", minimum-quantity ("à l'achat de 2"), loyalty-gated.
One flags model, not special cases.

### Flyer section capture
Record which flyer section/department each item came from (produce, dairy,
meat…). Nearly free at scrape time; the strongest future signal for Phase 4
classification.

### Was/now prices
Capture regular price alongside sale price ("était 7,99 $") and derive the
discount. Follow product links for SKU, category, regular price when available.

### OCR
Image-only flyers need French-trained OCR (tesseract `fra`, bilingual `fra+eng`).
English-only OCR on French flyers is a silent accuracy killer.

### Quantities & units
Price unit (each vs weight), item weight/size, min/max quantity — scrape when
present, null otherwise. Never invent.

## Cross-cutting

### Testing
Golden-sample tests per source: one saved flyer edition + hand-verified expected
items, run in CI. Parser unit tests for Quebec price formats, bilingual names,
and condition flags.

### Sample-first store onboarding
The standing rule applies: each new store's scraper is validated on a sample
edition before it joins the daily run. No silent bulk onboarding.

### Cost control
67 stores weekly; vision/OCR is the expensive path. Prefer structured sources
(FlyerKit returns products as JSON — no scraping needed), reserve vision for
image-only flyers, cache aggressively.

### Orchestration
Daily chain with per-store state (last edition seen), retries + backoff, and
alerts when a store's flyer is missing for two consecutive cycles — silent gaps
destroy price history. Backfill support for historical editions.

### Retention
Keep price observations indefinitely (that's the product). Raw artifacts and page
images may expire on a policy (e.g. 90 days) — quarantine evidence excepted.

## Schema notes

Build from `docs/research/schema-sketch.md`: `stores`, `flyer_sources`
(scheduler reads `(kind, fetchability)` to pick the easiest source),
`flyers`, `locations`, plus Phase 3 tables `flyer_items` (with `name_fr`,
`name_en`, `loyalty_gated`, `conditions` JSON, `section`, `image_hash`,
`bbox`, `raw_text`, `confidence`, `category` default `'Unclassified'`) and
`price_observations` (keyed by `item_key`).

## Deferred to Phase 4

Item classification (category hardcoded `Unclassified`; skipping non-grocery
items comes later, using the captured flyer sections as signal).
