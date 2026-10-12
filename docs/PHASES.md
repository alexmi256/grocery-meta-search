# Project Phases

## Phase 1 — Discover grocery stores

Find all grocery stores with a physical presence in Montreal. Starting points:
Flipp, the RedFlagDeals Quebec grocery round-up thread, plus additional EN/FR
web searches (Montreal is French-primary; national chains have EN+FR sites).
Deliverable: a list of all grocery stores.

## Phase 2 — Store details

For each store, at minimum:

- Website?
- Flyers / weekly promos? (site-linked flyers, plus flyer search engines like Flipp — discover others)
- Flyer sources, duration of each flyer, file formats (prefer HTML, PDF fallback)
- Product search bar? (key for later phases)
- Physical locations (address + latitude/longitude for nearby-store display)
- Parent company (e.g. Loblaw owns Provigo, Maxi, No Frills, … — shared site layouts likely)

Think about DB organization while researching. Present results as a markdown table in docs.

## Phase 3 — Flyer pipelines

**3a. Flyer fetching.** Get the latest flyers per store. Prefer easy-to-parse
sources (HTML); handle multiple concurrent flyers per store. Record each flyer's
validity period and language — fetch both EN and FR versions where they exist
(Montreal is French-primary; some flyers are bilingual). Group fetch methods
shared across stores / flyer engines.

**3b. Item scraping.** Scrape items from flyers into the DB. Handle each file
format the sources offer; visually scrape image-only flyers. Per item, at minimum:

- Name, price, price validity period (derived from flyer, with sub-period checks
  like weekend-only deals), languages
- Follow product links to the store site for SKU, category, regular price
- Price unit, item weight, min/max quantity when available

Classification is deferred: every item is hardcoded as `Unclassified` for now
(TODO). Chain 3a+3b to run daily.

## Phase 4 — Refinement + item classification

Refine Phase 3; implement item classification (skip non-grocery items).

## Phase 5 — Store web search

Research and implement proxied item search across stores that support product search.

## Phase 6 — Web-search refinement

## Phase 7 — Quality of life

Favorite stores, distance-based filtering, etc.
