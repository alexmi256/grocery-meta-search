# SQLite schema sketch (Phase 2 proposal)

Proposed by Phase 2 research; to be finalized on review. Conventions: `slug`
(TEXT, lowercase-hyphenated) is the natural primary key for stores — canonical,
stable across name variants. Small fixed vocabularies use TEXT + CHECK.
Multi-value fields from the YAMLs are JSON TEXT columns for now (normalize later
only if queries demand it). All timestamps TEXT ISO-8601. `created_at` /
`updated_at` on every table (omitted below for brevity).

## stores

One row per Phase 2 YAML (`docs/research/stores/<slug>.yaml` is the seed source).

| column | type | notes |
|---|---|---|
| slug | TEXT PK | canonical id |
| name | TEXT NOT NULL | display name |
| name_variants | TEXT | JSON array |
| store_type | TEXT | traditional \| ethnic-specialty \| warehouse \| pharmacy \| gen-merch \| dollar \| other |
| footprint | TEXT | island \| greater \| qc-confirmed \| qc-unverified |
| tier | INTEGER | 1 \| 2 \| 3 |
| website_url | TEXT | |
| website_languages | TEXT | JSON array, e.g. ["fr","en"] |
| language_switch | TEXT | param \| subdomain \| path \| toggle \| n/a |
| render_tech | TEXT | ssr \| spa \| js-heavy |
| bot_protection | TEXT | none \| cloudflare \| captcha \| rate-limit \| blocked |
| parent_company | TEXT | |
| affiliation | TEXT | corporate \| independent-affiliate \| banner-group |
| banner_family | TEXT | JSON array of related banner slugs |
| research_status | TEXT | complete \| partial \| minimal |
| researched_at | TEXT | date |
| notes | TEXT | |
| excluded | INTEGER DEFAULT 0 | 1 = confirmed no Montreal presence / closed (see below) |

Index: `(parent_company)`, `(tier)`.

## flyer_sources

One row per fetchable flyer source (official site + aggregators), from each
YAML's `flyers.types[].sources[]`. Drives the Phase 3a fetch scheduler.

| column | type | notes |
|---|---|---|
| id | INTEGER PK | |
| store_slug | TEXT NOT NULL → stores.slug | |
| flyer_type | TEXT | weekly \| pharmacy \| general-merchandise \| … |
| name | TEXT | e.g. "official site", "Flipp" |
| url | TEXT | |
| kind | TEXT | official \| aggregator |
| format | TEXT | html \| pdf \| images \| json-api |
| parse_friendliness | TEXT | high \| medium \| low |
| fetchability | TEXT | http \| browser-needed \| blocked |
| languages | TEXT | JSON array |
| notes | TEXT | |

Index: `(store_slug)`, `(kind, fetchability)` — scheduler picks easy sources first.

## flyers

One row per discovered flyer edition (populated by the Phase 3a pipeline).

| column | type | notes |
|---|---|---|
| id | INTEGER PK | |
| store_slug | TEXT NOT NULL → stores.slug | |
| flyer_source_id | INTEGER → flyer_sources.id | |
| flyer_type | TEXT | |
| valid_from / valid_to | TEXT | ISO dates; flip weekday derived |
| flip_weekday | TEXT | Thursday \| Friday \| … |
| flip_timezone | TEXT | default America/Toronto |
| per_store_variant | INTEGER | 0/1 — banner flyer vs store-specific |
| location_id | INTEGER → locations.id | NULL when banner-wide |
| languages | TEXT | JSON array |
| archive_url | TEXT | where the fetched artifact lives |
| fetch_status | TEXT | ok \| failed \| blocked |
| fetched_at | TEXT | |

Index: `(store_slug, valid_from)`, `(valid_to)` — "current flyers" query.

## locations

Populated by the Phase 2b harvest (Tier 1 chains via locator APIs), not manual.

| column | type | notes |
|---|---|---|
| id | INTEGER PK | |
| store_slug | TEXT NOT NULL → stores.slug | |
| name | TEXT | e.g. "Metro Plamondon" |
| address | TEXT | |
| city | TEXT | |
| postal_code | TEXT | |
| latitude / longitude | REAL | for nearby-store queries |
| phone | TEXT | |
| hours | TEXT | JSON |
| source | TEXT | locator-api \| manual \| … |

Index: `(store_slug)`, `(latitude, longitude)` — consider an R*Tree virtual
table later for radius queries.

## product_search_configs

From each YAML's `product_search`. Drives the Phase 5 proxy search.

| column | type | notes |
|---|---|---|
| store_slug | TEXT PK → stores.slug | |
| has_search | INTEGER | 0/1 |
| url_pattern | TEXT | e.g. "…/search?q={query}" |
| location_scoped | INTEGER | 0/1 — needs store/postal code first |
| guest_ok | INTEGER | 0/1 |
| kind | TEXT | json-api \| html \| spa |
| api_notes | TEXT | observed endpoints, params |
| bot_protection | TEXT | |
| languages | TEXT | JSON array |

## ecommerce

| column | type | notes |
|---|---|---|
| store_slug | TEXT PK → stores.slug | |
| online_ordering | INTEGER | 0/1 |
| click_and_collect | INTEGER | 0/1 |
| notes | TEXT | |

## loyalty_programs

Card-gated prices are a distinct price semantic (Phase 3b must record them).

| column | type | notes |
|---|---|---|
| id | INTEGER PK | |
| store_slug | TEXT NOT NULL → stores.slug | |
| name | TEXT | e.g. "PC Optimum", "moi", "Scène+", "Familiplus" |
| card_gated_prices | INTEGER | 0/1 |
| notes | TEXT | |

## aggregators

Seeded from `docs/research/flyer-aggregators.md`.

| column | type | notes |
|---|---|---|
| id | INTEGER PK | |
| name | TEXT | e.g. "Flipp", "circulaires.club" |
| url | TEXT | |
| coverage_notes | TEXT | |
| formats | TEXT | JSON array |
| bot_friendliness | TEXT | |
| notes | TEXT | |

## Phase 3 tables (sketch only — designed in Phase 3)

- `flyer_items` — item rows scraped from a flyer: id, flyer_id → flyers.id,
  name, price, price_unit, weight, min/max quantity, languages (JSON),
  loyalty_gated (0/1), sub_period_note, product_url, image_url, category
  (default 'Unclassified'), raw_text.
- `price_observations` — (item_key, store_slug, location_id, price,
  valid_from, valid_to, source) for price tracking over time; item_key is a
  normalized name+unit fingerprint until SKU-level matching exists.

## Exclusion candidates (set `stores.excluded = 1` on approval)

Confirmed zero Montreal/Quebec presence or closed, per Phase 2 verification:
`1117-meats`, `mrakovic`, `ida-pharmacy` (Flipp national-listing artifacts);
`petit-milos` (closed/absorbed); `coop-alimentaire-montreal` (likely closed);
`sobeys` (no QC retail banner); `le-monde-au-naturel` (Trois-Rivières only);
`coop-alentour` (Sherbrooke only).
