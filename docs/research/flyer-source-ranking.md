# Flyer source ranking — Phase 3

Generated from `docs/research/stores/*.yaml` (67 Phase-3 stores).
Score = coverage × ease. Ease is evidence-weighted: the Flipp FlyerKit
probe (2026-10-12, verified live) and worker findings override raw YAML aggregates.

## Aggregator identity corrections (2026-10-12)

- **reebee → flipp**: reebee.com now redirects to flipp.com (acquisition complete).
- **circulaires.ca = circulaires.com**: same operator (redirects); SEO-placeholder
  pages with no dated editions — low value, recommend YAML cleanup merging them.
- **pdfflyers.com**: dead for QC (redirects to US WeeklyAd.io).
- **supermarches.ca**: now a news portal, no flyer directory — verify before building.
- **weekly-flyer.ca**: abandoned (previews stuck at April 2026).

## Probe result (2026-10-12, live)

Flipp FlyerKit (`dam.flippenterprise.net/flyerkit`) VERIFIED working for Maxi
(326 products) and IGA (421): structured JSON (name, price, image, SKU, bbox),
validity dates at flyer AND item level, `locale=fr` works. Per-brand static
access tokens published in github.com/jonathan-pearce/grocery_flyer.
**Metro group has no FlyerKit token** — Metro QC / Super C / Adonis / Jean Coutu /
Brunet are served by the separate Metro Digital Azure API (needs key probe).
Full notes: `work/flyerkit-probe.md`.

## Ranked sources

| Rank | Source | Stores | Formats (typical) | Fetch | FR | Dated | Ease | Score | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `circulaires.club` | 45 | images | http | Y | Y | 9.5 | 427.5 | dated image editions, plain HTTP, FR |
<!-- stores: adonis, akhavan, avril, brunet, bulk-barn, canadian-tire, coop-alentour, costco, euro-marche, familiprix, fruiterie-valmont, frutta-si, giant-tiger, iga, intermarche-palumbo, jean-coutu, kim-phat, l-intermarche, la-moisson, marche-ami, marche-axep, marche-bonanza, marche-bonichoix, marche-esposito, marche-fu-tai, marche-lian-tai, marche-newon, marche-pa, marche-richelieu, marche-sheng-tai, marches-tau, marches-tradition, maxi, metro, mm-food-market, monde-au-naturel, odessa-poissonnier, pharmaprix, provigo, rachelle-bery, shop-sante, super-c, t-t, uniprix, walmart -->
| 2 | `flipp` | 25 | json-api | http | Y | Y | 14 | 350 | VERIFIED json-api/high/http/FR/dated via live probe |
<!-- stores: adonis, avril, brunet, canadian-tire, familiprix, giant-tiger, iga, iga-express, iga-extra, jean-coutu, kim-phat, loblaws, marche-ami, marche-lian-tai, marche-pa, marche-richelieu, maxi, metro, pharmaprix, provigo, rachelle-bery, shop-sante, super-c, uniprix, walmart -->
| 3 | `circulaire-en-ligne.ca` | 29 | images | http | Y | ? | 9 | 261 | html/images hubs; some entries are prose articles (variable) |
<!-- stores: adonis, akhavan, coop-alentour, euro-marche, l-intermarche, la-moisson, loblaws, marche-ami, marche-axep, marche-bonichoix, marche-c-t, marche-esposito, marche-newon, marche-pa, marche-richelieu, marches-tau, marches-tradition, maxi, mayrand, metro, mm-food-market, monde-au-naturel, odessa-poissonnier, pharmaprix, provigo, rachelle-bery, super-c, uniprix, walmart -->
| 4 | `circulairecanada.com` | 20 | images | http | Y | ? | 6 | 120 | AI prose articles, no brand hubs — low value |
<!-- stores: adonis, familiprix, frutta-si, iga, jean-coutu, l-intermarche, marche-ami, marche-bonichoix, marche-pa, marches-tradition, maxi, metro, metro-plus, mm-food-market, pharmaprix, provigo, rachelle-bery, super-c, uniprix, walmart -->
| 5 | `official:custom` | 23 | html | http | ? | ? | 5 | 115 | heterogeneous one-offs — NOT one source; per-store last resort |
<!-- stores: adonis, bulk-barn, coop-alentour, costco, euro-marche, fruiterie-valmont, iga, iga-express, iga-extra, intermarche-palumbo, marche-ami, marche-axep, marche-bonanza, marche-bonichoix, marche-c-t, marche-pa, marche-sa-et-fils, marches-tau, marches-tradition, mayrand, pa-nature, premiere-moisson, voisin -->
| 6 | `flyerbox.ca` | 10 | images | http | Y | ? | 8 | 80 | images, http, FR |
<!-- stores: bulk-barn, canadian-tire, iga, loblaws, marche-pa, maxi, metro, pa-nature, t-t, walmart -->
| 7 | `circulaires.com` | 19 | images | http | Y | ? | 4 | 76 | SAME OPERATOR as circulaires.ca; SEO placeholders, no dated editions |
<!-- stores: kim-phat, l-intermarche, la-moisson, loblaws, marche-ami, marche-axep, marche-bkr, marche-bonanza, marche-bonichoix, marche-c-t, marche-esposito, marche-fu-tai, marche-lian-tai, marche-newon, marche-pa, marche-richelieu, marche-sheng-tai, marche-sultan, mayrand -->
| 8 | `rfd-flyers` | 8 | html | http | ? | ? | 8 | 64 | listing page http-friendly; viewer JS; ?order=name is 402 |
<!-- stores: adonis, frutta-si, iga, metro, mm-food-market, pa-nature, super-c, wholesale-club -->
| 9 | `flyerseek.com` | 8 | html | http | ? | ? | 8 | 64 | html, http |
<!-- stores: iga, jean-coutu, maxi, metro, mm-food-market, pharmaprix, t-t, walmart -->
| 10 | `flyerdeals.ca` | 8 | html | http | ? | ? | 8 | 64 | html, http |
<!-- stores: marche-bonanza, marche-c-t, mayrand, metro, provigo, t-t, walmart, wholesale-club -->
| 11 | `official:metro-azure` | 5 | html | http | ? | ? | 12 | 60 | structured JSON API per research; key probe still needed |
<!-- stores: brunet, jean-coutu, metro, metro-plus, super-c -->
| 12 | `circulaires.ca` | 11 | images | http | Y | ? | 4 | 44 | SAME OPERATOR as circulaires.com; SEO placeholders, no dated editions |
<!-- stores: kim-phat, l-intermarche, la-moisson, marche-ami, marche-axep, marche-bonichoix, marche-esposito, marche-lian-tai, marche-richelieu, marche-sheng-tai, marche-sultan -->
| 13 | `flyers-on-line.com` | 7 | images | http | ? | ? | 6 | 42 | images/low, http |
<!-- stores: marches-tau, marches-tradition, mayrand, mm-food-market, pa-nature, uniprix, wholesale-club -->
| 14 | `flyerca.com` | 5 | images | http | ? | ? | 8 | 40 | html, http |
<!-- stores: bulk-barn, giant-tiger, jean-coutu, super-c, t-t -->
| 15 | `official:shopify` | 5 | html | http | ? | ? | 8 | 40 | one fetch pattern per platform; usually html/images |
<!-- stores: giant-tiger, la-moisson, magasin-amira, odessa-poissonnier, shop-sante -->
| 16 | `kimbino.ca` | 5 | images | http | Y | ? | 7.5 | 37.5 | images, http, FR |
<!-- stores: costco, loblaws, mm-food-market, t-t, walmart -->
| 17 | `official:wordpress` | 5 | images | http | ? | ? | 7 | 35 | one fetch pattern per platform; often images/low |
<!-- stores: frutta-si, kim-phat, marche-andes, milano-fruiterie, rachelle-bery -->
| 18 | `official:flipp` | 4 | json-api | browser-needed | ? | ? | 8 | 32 | embeds Flipp viewer; FlyerKit token likely exists — verify per brand |
<!-- stores: canadian-tire, familiprix, uniprix, walmart -->
| 19 | `official:wix` | 4 | images | http | ? | ? | 7 | 28 | one fetch pattern per platform; often images/low |
<!-- stores: 3-saisons-fruits-legumes, baia-dei-formaggi, h-marche, marche-newon -->
| 20 | `official:woocommerce` | 3 | pdf | http | ? | ? | 8 | 24 | one fetch pattern per platform; usually html/images |
<!-- stores: aliments-merci, marche-fu-tai, marche-korea -->
| 21 | `supermarches.ca` | 6 | html | http | Y | ? | 3 | 18 | NOW A NEWS PORTAL (2026-10-12) — verify before building |
<!-- stores: brunet, canadian-tire, familiprix, iga, jean-coutu, maxi -->
| 22 | `ca-mydeals365.com` | 3 | html | http | ? | Y | 6 | 18 | per-edition articles, no stable hub |
<!-- stores: costco, mayrand, mm-food-market -->
| 23 | `speciauxquebec.com` | 2 | images | http | Y | Y | 7 | 14 | images, http, FR, dated |
<!-- stores: rachelle-bery, walmart -->
| 24 | `kaufino.com` | 2 | images | http | ? | ? | 6 | 12 | images, http; coverage unverified for QC |
<!-- stores: loblaws, marche-c-t -->
| 25 | `weeklyflyer.com` | 2 | images | http | ? | ? | 6 | 12 | images, http |
<!-- stores: loblaws, wholesale-club -->
| 26 | `quebectoutcompris.com` | 2 | pdf | http | ? | ? | 5 | 10 | pdf, currently no active editions |
<!-- stores: maxi, provigo -->
| 27 | `official:flyerify` | 1 | html | http | ? | ? | 9.5 | 9.5 | structured flyer platform (html/images) |
<!-- stores: wholesale-club -->
| 28 | `official:reebee` | 1 | html | http | ? | ? | 6 | 6 | Reebee-powered HTML; reebee.com now redirects to flipp.com — verify |
<!-- stores: avril -->
| 29 | `pdfflyers.com` | 3 | images | http | ? | ? | 2 | 6 | DEAD for QC (redirects to US WeeklyAd.io) |
<!-- stores: epicure-market, loblaws, marches-tau -->
| 30 | `official:loblaw` | 6 | html | blocked | ? | ? | 1 | 6 | Akamai-BLOCKED — never build; use flipp for these stores |
<!-- stores: l-intermarche, loblaws, maxi, pharmaprix, provigo, t-t -->
| 31 | `shopping-canada.com` | 1 | html | http | ? | ? | 5 | 5 | directory, thin flyer coverage |
<!-- stores: marche-fu-tai -->
| 32 | `official:instagram` | 1 | images | browser-needed | ? | ? | 3 | 3 | manual/heavy fetch |
<!-- stores: akhavan -->
| 33 | `official:email` | 1 | html | http | ? | ? | 3 | 3 | manual |
<!-- stores: costco -->
| 34 | `weekly-flyer.ca` | 1 | images | http | ? | ? | 2 | 2 | ABANDONED (previews stuck at April 2026) |
<!-- stores: pharmaprix -->

## Recommended build order

1. **flipp (FlyerKit)** — ~20 stores. Verified structured JSON; no scraping
   step needed for 3b. Sample-first: maxi, iga, provigo.
2. **official:metro-azure** — 5 stores (metro, metro-plus, super-c,
   jean-coutu, brunet) + adonis candidate. Probe the API key first;
   structured JSON expected.
3. **circulaires.club** — 45 stores. Dated image editions over plain HTTP,
   FR. The long-tail workhorse (OCR path for 3b).
4. **Official platform groups** — one fetch pattern each: official:shopify (5),
   official:wordpress (5), official:wix (4), official:woocommerce (3),
   official:flyerify (1).
5. **Gap-fill aggregators** — rfd-flyers, circulaire-en-ligne.ca, flyerbox.ca,
   flyerdeals.ca, flyerseek.com, flyerca.com, kimbino.ca.
6. **official:custom one-offs** — per-store, last.
7. **Do not build**: official:loblaw (Akamai-blocked — use flipp),
   pdfflyers.com (dead), weekly-flyer.ca (abandoned), circulaires.ca/.com
   (SEO placeholders), supermarches.ca (verify — now a news portal).

## Per-store recommended source (one source per store)

| Store | Recommended source | Why |
|---|---|---|
| Akhavan | `circulaires.club` | dated image editions, plain HTTP, FR |
| Aliments Merci | `official:woocommerce` | one fetch pattern per platform; usually html/images |
| Avril Supermarché Santé | `flipp` | verified structured JSON API |
| Baia dei Formaggi | `official:wix` | one fetch pattern per platform; often images/low |
| Brunet | `official:metro-azure` | Metro-group native API (structured); probe key first |
| Bulk Barn | `circulaires.club` | dated image editions, plain HTTP, FR |
| Canadian Tire | `flipp` | verified structured JSON API |
| Coop Alentour | `circulaires.club` | dated image editions, plain HTTP, FR |
| Costco Wholesale | `circulaires.club` | dated image editions, plain HTTP, FR |
| Epicure Market | `—` | NO VIABLE SOURCE (only blocked/dead sources recorded) — re-check before Phase 3 |
| Euro Marché | `circulaires.club` | dated image editions, plain HTTP, FR |
| Familiprix | `flipp` | verified structured JSON API |
| Fruiterie Valmont | `circulaires.club` | dated image editions, plain HTTP, FR |
| Fruits & Légumes 3 Saisons | `official:wix` | one fetch pattern per platform; often images/low |
| Giant Tiger | `flipp` | verified structured JSON API |
| H Marché | `official:wix` | one fetch pattern per platform; often images/low |
| IGA | `flipp` | verified structured JSON API |
| IGA Express / Mini | `flipp` | verified structured JSON API |
| IGA Extra | `flipp` | verified structured JSON API |
| Jean Coutu | `official:metro-azure` | Metro-group native API (structured); probe key first |
| Kim Phat | `flipp` | verified structured JSON API |
| L'Intermarché | `circulaires.club` | dated image editions, plain HTTP, FR |
| L'intermarché Palumbo | `circulaires.club` | dated image editions, plain HTTP, FR |
| La Moisson Supermarché Santé | `circulaires.club` | dated image editions, plain HTTP, FR |
| Le Marché Esposito | `circulaires.club` | dated image editions, plain HTTP, FR |
| Le Monde au Naturel | `circulaires.club` | dated image editions, plain HTTP, FR |
| Les Marchés Tau | `circulaires.club` | dated image editions, plain HTTP, FR |
| Les Marchés Tradition | `circulaires.club` | dated image editions, plain HTTP, FR |
| Loblaws | `flipp` | official:loblaw is Akamai-blocked; FlyerKit verified pattern |
| M&M Food Market | `circulaires.club` | dated image editions, plain HTTP, FR |
| Magasin Amira | `official:shopify` | one fetch pattern per platform; usually html/images |
| Marche PA | `flipp` | verified structured JSON API |
| Marché Adonis | `flipp` | aggregator path (no FlyerKit token for Metro group; Azure may also work) |
| Marché Ami | `flipp` | verified structured JSON API |
| Marché Andes | `official:wordpress` | one fetch pattern per platform; often images/low |
| Marché Axep | `circulaires.club` | dated image editions, plain HTTP, FR |
| Marché BKR | `circulaires.com` | SAME OPERATOR as circulaires.ca; SEO placeholders, no dated editions |
| Marché Bonanza | `circulaires.club` | dated image editions, plain HTTP, FR |
| Marché Bonichoix | `circulaires.club` | dated image editions, plain HTTP, FR |
| Marché C&T | `circulaire-en-ligne.ca` | html/images hubs; some entries are prose articles (variable) |
| Marché Frutta Si | `circulaires.club` | dated image editions, plain HTTP, FR |
| Marché Fu Tai | `circulaires.club` | dated image editions, plain HTTP, FR |
| Marché Korea | `official:woocommerce` | one fetch pattern per platform; usually html/images |
| Marché Lian Tai | `flipp` | verified structured JSON API |
| Marché Newon | `circulaires.club` | dated image editions, plain HTTP, FR |
| Marché Richelieu | `flipp` | verified structured JSON API |
| Marché SA et Fils | `official:custom` | heterogeneous one-offs — NOT one source; per-store last resort |
| Marché Sheng Tai | `circulaires.club` | dated image editions, plain HTTP, FR |
| Marché Sultan | `circulaires.ca` | SAME OPERATOR as circulaires.com; SEO placeholders, no dated editions |
| Maxi | `flipp` | official:loblaw is Akamai-blocked; FlyerKit verified pattern |
| Mayrand Food Group | `circulaire-en-ligne.ca` | html/images hubs; some entries are prose articles (variable) |
| Metro | `official:metro-azure` | Metro-group native API (structured); probe key first |
| Metro Plus | `official:metro-azure` | Metro-group native API (structured); probe key first |
| Milano Fruiterie | `official:wordpress` | one fetch pattern per platform; often images/low |
| Odessa Poissonnier | `circulaires.club` | dated image editions, plain HTTP, FR |
| Pharmaprix | `flipp` | official:loblaw is Akamai-blocked; FlyerKit verified pattern |
| Première Moisson | `official:custom` | heterogeneous one-offs — NOT one source; per-store last resort |
| Provigo | `flipp` | official:loblaw is Akamai-blocked; FlyerKit verified pattern |
| Rachelle-Béry | `flipp` | verified structured JSON API |
| Shop Santé | `flipp` | verified structured JSON API |
| Super C | `official:metro-azure` | Metro-group native API (structured); probe key first |
| T&T Supermarché | `circulaires.club` | dated image editions, plain HTTP, FR |
| Uniprix | `flipp` | verified structured JSON API |
| Voisin | `official:custom` | heterogeneous one-offs — NOT one source; per-store last resort |
| Walmart | `flipp` | verified structured JSON API |
| Wholesale Club | `official:flyerify` | structured flyer platform (html/images) |
| Épicerie PA Nature | `rfd-flyers` | listing page http-friendly; viewer JS; ?order=name is 402 |
