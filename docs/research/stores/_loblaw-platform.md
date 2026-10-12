# Shared Loblaw platform notes (researched 2026-10-12)

Applies to: provigo, maxi, loblaws, t-t, pharmaprix. Recorded once here;
each `<slug>.yaml` cross-references this file.

## Bot protection (verified via direct probes 2026-10-12)

- provigo.ca, maxi.ca, loblaws.ca, tntsupermarket.com: Akamai edge
  "Access Denied" (errors.edgesuite.net, e.g. Reference #18.e972cd17…)
  for ALL automated clients tried: desktop Chrome UA, Googlebot UA,
  iPhone Safari UA, plain curl. Root path redirects observed before the
  block: maxi.ca → /fr, provigo.ca → /fr, loblaws.ca → /en
  (path-based language, geo/IP-defaulted). No render-tech determination
  possible from this network for these four sites.
- pharmaprix.ca: homepage fetchable over plain HTTP (200, ~959 KB);
  deeper paths are selectively blocked — /flyer (301 → /flyer?lang=fr →
  403) returns Akamai 403 even to a text-render fetch service.
  Headers: Server istio-envoy, x-queueit-connector: akamai,
  X-Akamai-Transformed present.
- tntsupermarket.com/store-flyer?location=bc: Akamai 403 to curl, but
  retrievable via a text-render fetch (structured per-item HTML obtained).

## pharmaprix.ca stack (verified from homepage HTML)

- Next.js SSR: `<script id="__NEXT_DATA__">` with getServerSideProps
  (gssp), buildId observed `n8QGlsD8IaWVWhME5Joqb` (2026-10-12; rotates).
  locales [en, fr], defaultLocale en. Language switch = query param
  (?lang=fr); /fr/flyer 301s to /flyer?lang=fr.
- CMS-driven pages: pageProps.viewDefinitionResults (headless "view
  definition" CMS). Digital pharmacy on subdomain mypharmacy.pharmaprix.ca.
- Shared Loblaw DAM: dis-prod.assetful.loblaw.ca
  (…/content/dam/loblaw-companies-limited/…).
- JSON-LD present on homepage (application/ld+json).
- Shop: /shop/categories/<Name>/<name>/c/<id> with PLP query params
  ?sort=relevance|newest&page=1&showInStock=true&promotions=Sale —
  evidence of a structured product catalog behind the shop.

## Official flyer endpoints (observed)

- pharmaprix.ca/flyer?lang=fr ("Circulaire" in site nav) — blocked (403).
- tntsupermarket.com/store-flyer?location=bc — fetchable via text-render;
  per-item structured HTML (name, −% discount, sale price, regular price,
  unit). Location-scoped regions: bc confirmed; gta/ab implied by
  aggregator regional flyers (QC variant unconfirmed).
- provigo.ca / maxi.ca / loblaws.ca official flyer path: unconfirmed
  (sites blocked). Legacy system (pre-2020s) was eflyer.<banner>.ca image
  tiles; current viewer format unknown — needs live-browser check.

## Store locators (observed patterns)

- maxi.ca/store-locator/details/<id> (confirmed via directory listing).
  Same pattern presumed for provigo.ca, loblaws.ca (unconfirmed).
- Pharmaprix: store detail pages at stores.pharmaprix.ca/fr/store/<id>
  AND www.pharmaprix.ca/fr/stores/<id>-<slug> (both patterns observed in
  the wild). Locator landing page unconfirmed.

## E-commerce / loyalty (shared)

- PC Express (pcexpress.ca): click-and-collect + delivery platform shared
  by Loblaws, Maxi, Provigo (737+ locations, 2024). NOT T&T.
  Pharmaprix/Shoppers available for rapid delivery via DoorDash
  Marketplace; pharmaprix.ca has integrated /shop + shopping bag.
- PC Optimum: loyalty program for Provigo, Maxi, Loblaws, Pharmaprix.
  Member-gated flyer prices ("prix membre" vs non-member) observed in
  Maxi flyers; points-multiplier events (20x) in Pharmaprix flyers.
- T&T runs its OWN loyalty (free rewards cards, 20 points per $20
  spend) — NOT PC Optimum. No PC Express participation.
