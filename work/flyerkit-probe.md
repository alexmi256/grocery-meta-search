# Flipp FlyerKit API probe — 2026-10-12 (sample-first)

Target: `https://dam.flippenterprise.net/flyerkit` — structured JSON flyer products over plain HTTPS.
Probed with curl only (9 requests total across maxi + iga + store-code lookups). No rate limiting observed.

## Token acquisition

- Tokens are **per-brand static strings** (UUID-shaped, no auth flow).
- Published in the open-source scraper `github.com/jonathan-pearce/grocery_flyer`
  (`fetchers/flipp.py`, brand portfolios; README documents the endpoints).
- Metro is NOT in the FlyerKit portfolio — Metro group (Metro QC, Super C, Adonis,
  Food Basics) uses the separate **Metro Digital API** (`metrodigital-apim.azure-api.net`;
  `Ocp-Apim-Subscription-Key` + `Banner` headers, credentials also published in that
  repo's `fetchers/azure.py` or fetched at runtime from each brand's `.../config/app.json`).
  Metro on FlyerKit was not probed (no token exists for it there).

Tokens used (from that repo, verified live below):

| Brand | Flipp slug | access_token |
|---|---|---|
| Maxi | `maxi` | `75a33b973cc2e856dd0f2cd629d80a19` |
| IGA | `igaquebec` | `692be3f8ba9e9247dc13d064cb89e7f9` |

## Store codes (required by publications endpoint)

Store codes found in that repo's published data (`data/<brand>/stores.parquet`):

- Maxi Montreal (Jean Talon): `4558`
- IGA Montreal: `5924`

## Working requests

### 1. Store lookup (optional; validates store_code)

```bash
curl -s "https://dam.flippenterprise.net/flyerkit/store/maxi?locale=en&access_token=75a33b973cc2e856dd0f2cd629d80a19&store_code=4558"
```

### 2. Active publications for a store

```bash
curl -s "https://dam.flippenterprise.net/flyerkit/publications/maxi?languages%5B%5D=en&locale=en&access_token=75a33b973cc2e856dd0f2cd629d80a19&store_code=4558"
curl -s "https://dam.flippenterprise.net/flyerkit/publications/igaquebec?languages%5B%5D=fr&locale=fr&access_token=692be3f8ba9e9247dc13d064cb89e7f9&store_code=5924"
```

### 3. Products for one publication (display_type=all, FR or EN locale)

```bash
# Maxi weekly flyer (2026-10-08 → 2026-10-14), 326 products
curl -s "https://dam.flippenterprise.net/flyerkit/publication/8172751/products?display_type=all&locale=fr&access_token=75a33b973cc2e856dd0f2cd629d80a19"
# IGA Québec weekly flyer (2026-10-08 → 2026-10-14), 421 products
curl -s "https://dam.flippenterprise.net/flyerkit/publication/8176847/products?display_type=all&locale=fr&access_token=692be3f8ba9e9247dc13d064cb89e7f9"
```

## Verification results (all confirmed live)

- (a) **Structured products: YES.** Returns a JSON array of product objects with
  `name`, `price_text`, `pre_price_text`, `post_price_text` (e.g. `'+ tx'`),
  `image_url` (f.wishabi.net CDN), `sku`, `brand`, `categories`, `item_categories`,
  `sale_story`, `page` (flyer page number), `left/top/right/bottom` (item bbox on
  page image), `in_store_only`, `description`, `disclaimer_text`, `sub_items`.
- (b) **Validity dates: YES — both levels.** Publications carry `valid_from`,
  `valid_to` (ISO timestamps with -04:00 offset), `available_from/to`, `pdf_url`
  (archivable PDF), `sfml_url`, `name` + `external_display_name` ("Weekly Flyer -
  Valid Thursday, October 8 - Wednesday, October 14"). Products carry per-item
  `valid_from`/`valid_to` dates + timestamps.
- (c) **French locale: YES.** `locale=fr` accepted; IGA's weekly flyer is itself
  published with `locale: fr` ("Québec – Circulaire Hebdomadaire"). FR and EN
  calls return the same item count and schema. Maxi product names are bilingual
  (FR-first) regardless of locale.
- (d) **Exact URLs/params:** above. Note the odd-but-required `languages[]=en`
  param on the publications endpoint; products endpoint takes only
  `display_type=all`, `locale`, `access_token`.

## Sample outputs (2026-10-12)

- Maxi pub 8172751 (en): 326 products; e.g. `CROUSTILLES PRINGLES | POTATO CHIPS`,
  price `2.50`, page 15, sku `21003832_EA`.
- IGA pub 8176847 (fr): 421 products; e.g. `ESSUIE-TOUT BOUNTY`, price `9.99`.
- 30/326 Maxi products have empty `price_text` (recipe/brand ads, e.g. "RMN Kraft
  Philadelphia Thanksgiving 2026") — plan for items without prices.

## Caveats / not probed

- Tokens could be rotated by Flipp at any time; treat them as disposable.
- Metro on FlyerKit: not applicable (separate API, credentials published in the
  scraper repo but not probed here).
- Products bbox values are on a large/unusual coordinate scale (e.g.
  `left=28263.3, top=-1626.63`); mapping to page images needs calibration later.
- Card-gated "prix membre" pricing exists on these banners' flyers; the products
  response has `original_price` and `sale_story` fields that may encode it —
  needs a member-price flyer spot check in Phase 3.
