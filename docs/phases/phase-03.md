# Phase 3 — Flyer pipelines

## Objective

Build the two chained pipelines that run daily: (3a) fetch the latest flyers
per store, (3b) scrape items from flyers into the database.

## Approved scope (user, 2026-10-12)

- **Phase 3: greater Montreal area stores that have a flyer — 67 stores.**
  (footprint island/greater/qc-confirmed AND flyers.has_flyers=true)
- Future phases (5+): greater Montreal stores with a flyer OR product search — 108.
- The 7 exclusion candidates stay flagged as-is in the research data; the research
  stands, and scope filtering handles them downstream.

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

## Pipeline 3a — flyer fetching (per user's spec)

- Prefer easy-to-parse sources (HTML/JSON API); handle multiple concurrent flyers
  per store; capture validity period + language for each; fetch EN and FR versions
  where both exist; group shared fetch methods (Flipp FlyerKit, circulaires.com,
  Shopify/WooCommerce patterns).

## Pipeline 3b — item scraping (per user's spec)

- Handle each source format; visually scrape image-only flyers (OCR/vision).
- Per item: name, price, price validity (from flyer + sub-period checks like
  weekend-only), languages; follow product links for SKU/category/regular price;
  price unit, weight, min/max quantity when available.
- Category hardcoded `Unclassified` for now (classification deferred to Phase 4).
