# Flyer Aggregators — Montreal Grocery

Research date: 2026-10-12. Directory of flyer aggregators relevant to Montreal
grocery flyers, with an eye toward Phase 3 (flyer fetch + item pipelines).

Reading guide: **Coverage** = which Montreal grocers' flyers they carry and how
complete. **Formats** = how flyers are delivered. **Bot-friendliness** = how
feasible automated fetching is. **Language** = FR/EN/bilingual.

---

## 1. Flipp — flipp.com

- **URL:** https://flipp.com (app also on iOS/Android)
- **Coverage:** The largest aggregator — 1000+ retailers across Canada/US,
  all major Montreal chains (Maxi, Provigo, Metro, Super C, IGA, Costco,
  Walmart, Jean Coutu, Pharmaprix, Uniprix, Brunet, Familiprix, Adonis, etc.).
  Note the standing caveat: Flipp's retailer footer/store directory is
  **national, not Montreal-specific** — never use it as a geography signal.
  Weak on small independent/ethnic Montreal grocers.
- **Formats:** JS-heavy interactive viewer (page images) on the web; the
  **underlying FlyerKit API returns structured JSON products** (name, price,
  images per item) — see below.
- **Underlying API:** `https://dam.flippenterprise.net/flyerkit`
  - `GET /flyerkit/store/{slug}?store_code={code}&access_token={token}` —
    store lookup
  - `GET /flyerkit/publications/{slug}?store_code={code}&access_token={token}` —
    active publications (flyers) for a store
  - `GET /flyerkit/publication/{id}/products?display_type=all&locale=en&access_token={token}` —
    all products in a flyer
  - Each retailer brand has its own `access_token` (hardcoded per brand in
    scrapers; tokens are visible in client-side configs). An open-source
    project (github.com/jonathan-pearce/grocery_flyer) actively uses this API
    to fetch structured flyer products for 25 Canadian chains (Sobeys group,
    Loblaws group, Walmart). So plain-HTTP JSON fetching works today.
- **Bot-friendliness:** Web pages are JS-heavy (needs JS or API route); the
  FlyerKit API is plain HTTPS JSON — the most machine-friendly path in this
  list. Rate limits not observed; keep request volume modest and respect it.
- **Language:** Bilingual EN/FR site (`locale` param on API).
- **Notes:** Flipp acquired its largest Canadian rival **reebee** (~Nov 2024)
  and operates it as a separate brand — reebee data likely overlaps Flipp's.
  Metro-group flyers (Metro QC, Super C, Adonis, Food Basics) also have a
  retailer-native API: `https://metrodigital-apim.azure-api.net/api`
  (`Ocp-Apim-Subscription-Key` + `Banner` headers) — retailer-direct may beat
  Flipp for Metro group. Standing rule: validate in sample before full job.

## 2. RedFlagDeals flyers — redflagdeals.com/in/montreal/flyers/

- **URL:** https://www.redflagdeals.com/in/montreal/flyers/ (valid flyer
  source per project standing rules)
- **Coverage:** Montreal-localized flyer listing (Super C, IGA, Maxi, Metro,
  Provigo, Marché Adonis, Costco, Walmart, etc.) with per-flyer validity
  dates — genuinely geographic, unlike Flipp's footer.
- **Formats:** HTML listing page (server-rendered, fetched fine with plain
  HTTP/text fetch); individual flyer detail pages open an interactive viewer
  (JS). Viewer internals not verified.
- **Underlying API:** Not verified. Requires investigation in Phase 3.
- **Bot-friendliness:** The listing page is plain-HTTP friendly. The
  alphabetical merchant directory (`/in/montreal/flyers/?order=name`)
  returned **HTTP 402 (bot protection) on 2026-10-12** — same as Phase 1
  observed. Recorded as **OUTSTANDING: needs a live-browser check** (do not
  retry automatically).
- **Language:** RFD is an English site; Quebec flyer content itself is
  French (as published by the retailer).
- **Notes:** **RFD FORUMS are discovery-only and must NEVER be listed as a
  flyer source** (standing rule). Only the flyers section counts.

## 3. circulaires.club

- **URL:** https://circulaires.club (store directory:
  https://circulaires.club/magasins/)
- **Coverage:** **The best Quebec long-tail coverage found.** 182 Quebec
  merchants with per-merchant current-flyer archives. All majors (IGA, Metro,
  Maxi, Super C, Provigo, Costco, Walmart) **plus** small/ethnic Montreal
  grocers nobody else aggregates: Kim Phat, Marché C&T, Marché Newon, Marché
  Fu Tai, Marché Lian Tai, Marché Ocean Plus, Marché Ariya, Adonis, Akhavan,
  Aubut, L'Intermarché, Intermarché Palumbo, Marché Richelieu, Marchés
  Tradition, Mayrand, Panier Extra, Supermarché PA, Fruiterie 440, Le Jardin
  Mobile, La Moisson, La Manne Épicerie Santé, Marchés TAU, Le Marché
  Végétarien, etc. "88 circulaires from 56 merchants" were listed for a single
  coming week — good freshness.
- **Formats:** Page images in a zoom viewer (not OCR'd/text on site). No PDF
  or structured data observed.
- **URL patterns (stable, useful for Phase 3):**
  - `/magasins/` — full merchant directory
  - `/semaine/{du-D-au-D-mois-AAAA}/` — weekly index
  - `/semaine-prochaine/` — next-week preview
  - `/circulaire/{circulaire-store-du-D-au-D-mois-AAAA}/` — per-flyer page
    with validity dates, page count, category, related flyers
- **Underlying API:** None observed; HTML only.
- **Bot-friendliness:** Pages are **server-rendered HTML** — the directory
  and flyer pages fetched cleanly with plain text fetches. High confidence a
  plain-HTTP crawl of `/magasins/` → per-flyer pages works. Flyer page
  images themselves would need separate fetching (image URLs not visible in
  text extraction; check with a real HTTP fetch in Phase 3).
- **Language:** French only (FR). No English version observed.
- **Notes:** A La Moisson flyer was found here in Phase 1 — the site appears
  to be the source of record for several small Quebec grocers' digital
  flyers. Strong candidate as **the** Phase 3 source for long-tail Montreal
  grocers.

## 4. raddar — raddar.ca (successor of Publisac)

- **URL:** https://www.publisac.ca/ now serves raddar (TC Transcontinental).
  Press: May 2026 announced national rollout.
- **Coverage:** TC Transcontinental's platform — includes Metro (3-year deal
  renewed Dec 2025 explicitly covers Metro participation in raddar) and other
  retailers that print in the raddar bundle. Quebec-rooted; national as of
  June 2026.
- **Formats:** Digital platform plus **direct PDF downloads observed**:
  `https://print.raddar.ca/pdfs/V059.PDF` (per-edition PDFs). If flyer PDFs
  are directly fetchable by URL, this is the cleanest PDF pipeline of any
  aggregator.
- **Underlying API:** Not investigated.
- **Bot-friendliness:** Unknown — needs a Phase 3 check (verify flyer
  listing pages and PDF URL patterns are stable/fetchable).
- **Language:** Bilingual FR/EN expected (TC Transcontinental).
- **Notes:** Publisac branding retired; anything referencing publisac.ca as
  a flyer source should now point at raddar.

## 5. flyerbox.ca

- **URL:** https://www.flyerbox.ca (e.g. http://flyerbox.ca/fr/iga/)
- **Coverage:** National Canadian, not Quebec-specific. Grocery category
  includes IGA, Metro, Maxi, Provigo, Super C, Sobeys, Loblaws, Walmart,
  No Frills, Food Basics, FreshCo, T&T, Adonis, PA Supermarché, Oceans, etc.
  Per-store pages link out to **per-city pages** (e.g. "IGA Montréal", "IGA
  Laval") — genuinely geographic.
- **Formats:** Page-image viewer; images served via `na.leafletscdn.com`
  (thumbor CDN URLs), e.g.
  `https://na.leafletscdn.com/thumbor/.../ca/data/11/logo.png`. Logo/image
  asset pattern suggests an underlying data feed (`/ca/data/{id}/...`).
- **Underlying API:** Not confirmed; the `leafletscdn.com/ca/data/{id}/`
  path pattern is worth probing in Phase 3.
- **Bot-friendliness:** Pages fetched with plain text fetch (server-rendered
  HTML). Likely plain-HTTP friendly.
- **Language:** Bilingual FR/EN (`/fr/`, `/en/` paths).
- **Notes:** Part of the Leaflets CDN network (sibling sites in other
  countries). City-specific pages are a plus for Montreal targeting, but
  coverage is major-chains only — Flipp covers the same ground with a real
  API.

## 6. supermarches.ca

- **URL:** https://www.supermarches.ca ("Centre des spéciaux")
- **Coverage:** Quebec supermarkets and pharmacies (IGA, Metro, Maxi,
  Provigo, Super C, Jean Coutu, Brunet, Familiprix, Uniprix, ...).
- **Formats:** **Structured item data in server-rendered HTML** — effectively
  pre-parsed flyer items: description, format/size, brand, origin, price,
  unit (/ch.), validity start/end dates, store, and source ("Circ. - Mag." =
  circulaire). Searchable by category tree with paginated results
  (`pages/default.asp?cid=...&cid2=...&t=...`).
- **Underlying API:** None observed; the `default.asp` pages are the
  interface (classic ASP, parameter-driven — stable and scrapeable URL
  patterns).
- **Bot-friendliness:** Fully server-rendered HTML tables — plain HTTP
  fetching should work well. No bot protection observed.
- **Language:** French only (FR).
- **Notes:** This is the closest thing to a ready-made structured flyer-item
  feed from an aggregator. It is item-level (no flyer images), so it suits
  price comparison but not flyer-page display. Excellent complement to Flipp
  for Quebec chains.

## 7. circulairecanada.com

- **URL:** https://www.circulairecanada.com (per-flyer URLs like
  `/p/circulaire-maxi/`)
- **Coverage:** Major chains (IGA, Maxi, Super C, L'Intermarché, ...).
- **Formats:** **AI-written text summaries of flyers** — per-flyer articles
  listing highlighted products and prices in prose. Machine-readable text,
  but editorialized (not complete item lists, may contain errors).
- **Underlying API:** None.
- **Bot-friendliness:** Plain HTML, fetchable.
- **Language:** French only (FR).
- **Notes:** Useful as a cross-check / discovery aid; not a primary data
  source (incomplete, paraphrased). Treat prices from here as unverified.

## 8. Glouton — glouton.app

- **URL:** https://www.glouton.app (web + mobile app)
- **Coverage:** Quebec grocery chains (IGA, Maxi, Metro, Provigo, Super C;
  expanding to specialty/regional grocers). 150k+ monthly users.
- **Formats:** App/web UI with deal scores (1–10) per flyer special; uses
  AI + manual review to import flyer specials weekly (they hire humans to
  supervise the import).
- **Underlying API:** Not investigated; no public API confirmed.
- **Bot-friendliness:** Unknown — app-first; web may have bot protection.
- **Language:** French-first, bilingual per job postings (FR/EN).
- **Notes:** Not a flyer *source* for Phase 3 so much as a competitor /
  methodology reference (deal scoring). Worth watching, not fetching.

## 9. Other aggregators discovered (lower priority, not deep-dived)

Mostly national/international flyer-farm sites with thinner Quebec
coverage; several are template sites (possibly same operator). Listed for
completeness:

- **yflyers.com** — Canada flyers (Toronto/Montreal/Vancouver/Ottawa pages)
- **circulars.ca** — Canadian stores flyers/deals/coupons
- **weeklyflyer.com** — Canadian grocery flyers, "near me"
- **clubflyers.ca** / **flipflyers.ca** — Canadian store flyers + coupons
- **tiendeo.ca** — Tiendeo's Canadian edition (international flyer network)
- **kimbino.ca** — Kimbino Canada (international network)
- **kupino.ca** — flyers updated daily
- **ca-flyers.com** ("Canadian Flyers"), **flyers-canada.com**,
  **flyerify.com** (US+CA), **flyers-on-line.com**, **lastnut.com**,
  **save.ca**
- **circulaires.com** — Quebec, region-parameterized
  (`?region=Bas-Saint-Laurent`) — may be worth a look if circulaires.club
  has gaps
- **circulaire.eu** / **circulaireca.com** — Quebec-focused circulaire sites

---

## Assessment: most promising Phase 3 flyer sources

1. **Flipp's FlyerKit API** (`dam.flippenterprise.net`) — structured JSON
   products per flyer, covers all major chains, already proven by an active
   open-source scraper. Best primary source for major-chain flyers.
2. **supermarches.ca** — pre-parsed structured flyer *items* for Quebec
   chains, server-rendered HTML, no bot protection observed. Best
   complement for Quebec item-level data.
3. **circulaires.club** — server-rendered, 182 Quebec merchants incl. the
   ethnic/specialty long tail no one else aggregates; stable URL patterns.
   Best source for long-tail Montreal grocers (page images → OCR/parse).
4. **RFD Montreal flyers page** — valid Montreal-localized listing, plain
   HTTP friendly; keep as discovery/backup. `?order=name` directory is
   **OUTSTANDING** (HTTP 402; needs live-browser check in Phase 2).
5. **raddar** — investigate in Phase 3: direct flyer PDFs (`print.raddar.ca`)
   would be the cleanest PDF pipeline if URL patterns are stable.

Standing rules observed: RFD forums never used as a flyer source; no commits
made. Refinement validation (sample-first) applies to any pipeline work
built on these.
