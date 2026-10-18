# Metro Digital source (2026-10-18)

Adonis, Metro, Metro Plus and Super C switched from the Flipp
search API to Metro's own digital flyer platform
(`metrodigital-apim.azure-api.net`), the structured API behind the
banners' flyer web apps. Commissioned by Alex after he spotted the
API in the groupeadonis.ca flyer page's network traffic; approach
cross-checked against the open-source grocery_flyer project
([github.com/Jonathan-Pearce/grocery_flyer](https://github.com/Jonathan-Pearce/grocery_flyer)),
which scrapes the same platform (their store-id sweeps and banner
configs confirmed ours).

## How it works

- Each banner's flyer SPA (circulaire.metro.ca,
  circulaire.superc.ca, circulaire.groupeadonis.ca) publishes a
  public runtime config at `/config/app.json` containing the API
  base, banner id and subscription key — the frontend credentials
  every visitor's browser uses. The source reads them at fetch
  time; no credentials live in this repo, so platform key rotation
  is a non-event.
- `GET /api/flyers/{store_id}/{locale}?date=<today>` lists the
  store's active publications (title, dates, page count).
  `GET /api/pages/{title}/{store_id}/{locale}/` returns all pages;
  products are the block payloads with `actionType == "Product"`.
  The /en/ and /fr/ payloads are byte-identical (every field is
  bilingual in one response).
- Per-store settings (config URL, one Montreal-area store id,
  locale) live in `sources/metrodigital_stores.json`. Banner
  flyers are chain-wide, so the chosen store only anchors the
  lookup: Adonis 21937 (Sauvé), Metro 380 (Avenue du Parc),
  Metro Plus 381 (Wilderton), Super C 443 (Atwater). Metro and
  Metro Plus carry the same publications under both rows, as they
  did on Flipp.
- Implementation: `sources/metrodigital.py`, dispatched in
  `pipeline/fetch.py` ahead of Flipp for configured slugs; tests in
  `tests/test_metrodigital.py` (fixture includes the dict-form
  click-region values the platform emits).
- The October 2026 probe of this platform used the POST
  `/api/Pages/{job}/{store}/{locale}/search` endpoint, which hung;
  the GET pages endpoint the SPA itself uses is the reliable path
  (the grocery_flyer project uses the POST; both return the same
  product dicts).

## Field mapping notes

- Names: `productFr` → name_fr; `productEn` or `bodyEn` → name_en
  (bodyFr usually holds the size/variant line, not a name).
- Prices: `salePrice` → price_value; `promoUnit` normalized to the
  price_unit vocabulary (`/lb` → lb, `le 100 g` → 100g, `ch.` →
  each); `alternatePrice` (the dual rate, e.g. $/kg twin of a $/lb
  price) and `regularPrice` go to conditions; native
  `mainCategoryEn/Fr` are stored in conditions for the future
  store-native category mapping.
- **Multibuy is structural**: `priceQuantity >= 2` means salePrice
  is the bundle total ("2 pour 6$"); the single price is printed
  as an "ou 3,49 l'unité" / "ou 17,09 +tx la caisse" phrase in
  alternatePrice or the promo-unit text. The mapper stores the
  printed single price (else total/count) and sets
  conditions.multibuy {count, total} — the same semantics as the
  Flipp image-recovery stage, which is now disabled for these
  stores, as is page harvest (sizes come from bodyFr via the
  standard extractor: Adonis 67%, Metro 81%, Super C 87%
  coverage vs 49–56% from OCR harvest on Flipp data).
- Pack counts printed as the promo unit ("6 un.") become
  package_size + conditions.pack_count, not a rate unit.
- A few products per flyer carry no price at all in the payload
  (coupon/"save $X" tiles, oyster cases at Metro) — stored
  price-less, as with Monde's discount items.
- Click regions (percent coordinates, occasionally dict-form
  `{source, parsedValue}`) become the item bbox on the 1000 grid.

## Results (same cycle, Oct 15–21, 2026, vs the Flipp capture)

| store | items Flipp → API | EN names | sizes | SKUs | multibuy |
|---|---|---|---|---|---|
| adonis | 190 → 281 | 120 → 259 | 94 → 188 | 0 → 281 | 0 → 35 |
| metro | 373 → 531 | 306 → 487 | 212 → 432 | 0 → 531 | 15 → 71 |
| metro-plus | 373 → 531 | 306 → 487 | 212 → 432 | 0 → 531 | 12 → 71 |
| super-c | 229 → 293 | 227 → 290 | 135 → 254 | 0 → 293 | 1 → 7 |

The API counts are *products* (unique SKUs); Flipp counts were
flyer *cells* (multi-product cells merge into one item), so the
gains are granularity plus genuinely fuller coverage — Metro's
API serves three concurrent publications (main 84043, supplements
84043B and 84043M) where Flipp exposed the same three editions
with fewer items each.

Caveats: the flyers endpoint lists only currently-active
publications, so the next cycle's edition is no longer captured a
few days early the way Flipp exposed it. Jean Coutu and Brunet are
Metro-owned but do not run this platform (no SPA config at any
candidate host) and stay on Flipp. Production switch: backup
`data/grocery.db.bak-20261018-metrodigital`; the four stores'
Flipp editions were deleted and refetched (281 / 531 / 531 / 293
items, matching the scratch-DB experiment exactly). The client
retries GETs with backoff — the APIM path stalls occasionally
under burst load (all four stores timed out once during testing,
then fetched in seconds).
