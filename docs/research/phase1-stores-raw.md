# Phase 1 — Raw Store Discovery List (Montreal)

**Date:** 2026-10-12
**Status:** raw research output — Phase 1 only (list). Not yet DB-loaded or location-verified.
**Scope decision (user, 2026-10-12):** include everything that sells food — all 123 stores in scope
(122 + Marché Axep added in the 2026-10-12 refinement pass).
Geography default: Greater Montreal; `footprint` tags allow island-only filtering later.

## Method

Research tracks:
1. **flipp** — Flipp store listings for Montreal (note: Flipp's Montreal store pages are JS-heavy and
   could not be fetched directly; coverage comes from search-indexed Flipp Montreal pages plus Flipp's
   retailer footer, which may be national rather than Montreal-specific).
2. **rfd** — RedFlagDeals FORUMS "grocery round-up (Quebec)" weekly series. **FORUMS ARE DISCOVERY-ONLY:**
   per user correction (2026-10-12), RFD forums are not a reliable or consistent source for flyers and
   items. The exact thread (#2828330) was not fetchable; entries come from adjacent weeks of the same
   series (Jun–Sep 2026 editions), which use a stable banner set.
3. **rfd-flyers** — RFD's Montreal flyers page (redflagdeals.com/in/montreal/flyers/) — a VALID flyer
   source per user correction (2026-10-12). Base page fetched 2026-10-12; featured flyers were Costco,
   Super C, IGA, Maxi, Metro, Walmart, Provigo, Marche Adonis (all already listed). The alphabetical
   `?order=name` merchant directory could not be fetched (HTTP 402 bot protection) — needs a
   live-browser check in Phase 2. The user's spot-check found AXEP there, which led to adding
   Marché Axep and resolving the L'Intermarché parent company.
4. **fr-search** — French-language web searches (`circulaires épicerie Montréal`, `supermarchés Montréal`, etc.).
5. **en-search** — English-language web searches (`Montreal grocery store flyers`, national-chain location verification).
6. **ethnic-search** — Bilingual searches targeting ethnic, specialty, and independent grocers.
7. **url-fill** — 2026-10-12 refinement: targeted per-store web searches to fill missing website URLs
   (user: a store with a flyer almost certainly has a website).

## Tags

- **store_type:** `traditional` = traditional grocery chain | `ethnic-specialty` = ethnic & specialty grocer |
  `warehouse` = warehouse club | `pharmacy` = pharmacy | `gen-merch` = general merchandise |
  `dollar` = dollar & discount | `other`
- **footprint:** `island` = Montreal island | `greater` = Greater Montreal (Laval, South Shore, North Shore) |
  `qc-confirmed` = Quebec-wide with confirmed Montreal presence | `qc-unverified` = Quebec-wide, Montreal presence unverified.

## Stores

| # | Name | Variants | store_type | footprint | Parent company | Website | Sources |
|---|---|---|---|---|---|---|---|
| 1 | Metro | — | traditional | qc-confirmed | Metro Inc. | metro.ca | flipp, rfd, fr-search, en-search |
| 2 | Metro Plus | — | traditional | qc-confirmed | Metro Inc. | metro.ca | fr-search |
| 3 | Super C | — | traditional | qc-confirmed | Metro Inc. | metro.ca | rfd, fr-search, en-search |
| 4 | IGA | — | traditional | qc-confirmed | Sobeys Inc. (Empire) | iga.net / iga.ca | rfd, fr-search, en-search |
| 5 | IGA Extra | — | traditional | qc-confirmed | Sobeys Inc. (Empire) | iga.net | rfd, fr-search |
| 6 | IGA Express / Mini | — | other | qc-confirmed | Sobeys Inc. (Empire) | iga.net | fr-search |
| 7 | Provigo | — | traditional | qc-confirmed | Loblaw Companies | provigo.ca | rfd, fr-search, en-search |
| 8 | Maxi | Maxi & Cie | traditional | qc-confirmed | Loblaw Companies | maxi.ca | rfd, fr-search, en-search |
| 9 | Loblaws | — | traditional | qc-confirmed | Loblaw Companies | loblaws.ca | en-search |
| 10 | Marché Richelieu | — | traditional | qc-confirmed | Metro Inc. (banner) | marcherichelieu.ca | fr-search, ethnic-search, en-search |
| 11 | Les Marchés Tradition | — | traditional | qc-unverified | Sobeys Inc. (Empire) | marchestradition.com | flipp, fr-search, en-search, ethnic-search |
| 12 | Marché Bonichoix | — | traditional | qc-unverified | Sobeys Inc. (Empire) | bonichoix.com | fr-search, en-search, ethnic-search |
| 13 | L'Intermarché | — | traditional | qc-confirmed | AXEP (Loblaw-affiliated banner group) | lintermarche.ca | fr-search, ethnic-search, rfd-flyers |
| 14 | Marché Ami | — | traditional | qc-confirmed | Metro Inc. (banner) | marcheami.ca | fr-search |
| 15 | Marché PA | PA (RFD shorthand) | traditional | island | Independent (chain) | supermarchepa.com | rfd, fr-search, en-search |
| 16 | Intermarché Palumbo | Marché Palumbo | traditional | greater | Palumbo family (independent) | marchepalumbo.com | ethnic-search |
| 17 | Le Marché Esposito | — | traditional | island | Independent (chain of 2) | lemarcheesposito.ca | ethnic-search |
| 18 | Segal's Market | — | traditional | island | Independent (single) | https://www.facebook.com/2012417038809524 | fr-search, en-search |
| 19 | Marché Bonanza | Bonanza Lalumière | traditional | island | Independent | bonanzalalumiere.com | fr-search |
| 20 | 5 Saisons | — | ethnic-specialty | island | Metro Inc. | none found | ethnic-search |
| 21 | Sobeys | — | traditional | qc-unverified | Sobeys Inc. (Empire) | sobeys.com | flipp, en-search |
| 22 | Marché Adonis | Adonis Market (EN) | ethnic-specialty | greater | Metro Inc. (100% since 2017) | groupeadonis.ca | flipp, rfd, fr-search, en-search, ethnic-search |
| 23 | Kim Phat | KP (RFD shorthand) | ethnic-specialty | greater | contested — see notes | kimphat.com | rfd, fr-search, en-search, ethnic-search |
| 24 | T&T Supermarché | T&T Supermarket | ethnic-specialty | greater | Loblaw Companies (since 2009) | tntsupermarket.com | fr-search, en-search, ethnic-search |
| 25 | Marché C&T | — | ethnic-specialty | greater | Independent (chain of 3+) | marchect.ca | rfd, fr-search, ethnic-search |
| 26 | Marché Newon | — | ethnic-specialty | island | Independent (single) | marchenewon.com | fr-search, ethnic-search |
| 27 | G&D Supermarket | — | ethnic-specialty | island | Independent (single) | gdsupermarche.com | ethnic-search |
| 28 | Marché Kim Hour | — | ethnic-specialty | island | Independent (single) | https://www.facebook.com/170794359599794 | ethnic-search |
| 29 | Marché Kim-Po | — | ethnic-specialty | island | Independent (single) | marchekimpo.ca | ethnic-search |
| 30 | Marché Oriental (St-Denis) | — | ethnic-specialty | island | Independent (single) | orientalstdenis.ca | ethnic-search |
| 31 | Épicerie Heng Heng Chanchaya | — | ethnic-specialty | island | Independent (single) | none found | ethnic-search |
| 32 | Marché Duc Thanh | — | ethnic-specialty | island | Independent (single) | https://www.facebook.com/100772778660036 | ethnic-search |
| 33 | H Marché | Marché Oriental Jang Teu | ethnic-specialty | island | H Mart (Korean chain) | hmartmontreal.com | ethnic-search |
| 34 | Épicerie Coréenne et Japonaise | — | ethnic-specialty | island | Independent (single) | none found | ethnic-search |
| 35 | Marché Lian Tai | — | ethnic-specialty | island | Independent (single) | marcheliantai.ca | fr-search |
| 36 | Marché Fu Tai | — | ethnic-specialty | island | Independent (single) | marchefutai.ca | fr-search |
| 37 | Marché Sheng Tai | — | ethnic-specialty | island | Independent (single) | marcheshengtai.ca | fr-search |
| 38 | Marché Victoria Orientale | — | ethnic-specialty | island | Independent (single) | https://www.facebook.com/marchevictoria/ | fr-search, ethnic-search |
| 39 | South Indian Spices | — | ethnic-specialty | island | Independent (single) | none found | fr-search, ethnic-search |
| 40 | Marché Lavaniya | — | ethnic-specialty | island | Independent (single) | marche-lavaniya.business.site | ethnic-search |
| 41 | Marché 786 | — | ethnic-specialty | island | Independent (single) | marche786.ca | ethnic-search |
| 42 | Magasin Amira | — | ethnic-specialty | island | Independent | magasinamira.ca | fr-search |
| 43 | Marché BKR | — | ethnic-specialty | island | Independent | marche-bkr-laurentien.business.site | fr-search |
| 44 | Marché Sultan | — | ethnic-specialty | island | Independent | https://www.instagram.com/marchesultan.mtl | fr-search |
| 45 | Marché Tharsini | — | ethnic-specialty | island | Independent | https://m.facebook.com/pages/category/Supermarket/Marche-Tharsini-1904387439873150 | fr-search |
| 46 | Akhavan | — | ethnic-specialty | island | Independent (family chain of 2) | akhavanfood.com | ethnic-search |
| 47 | Délices du Maghreb | — | ethnic-specialty | island | Independent (single) | delicesdumaghreb.ca | ethnic-search |
| 48 | Magazin Istanbul | — | ethnic-specialty | island | Independent (single) | none found | ethnic-search |
| 49 | Épicerie Du Bazaar | — | ethnic-specialty | island | Independent (single) | bazaarfood.ca | ethnic-search |
| 50 | Épicerie Africaine de Montréal | — | ethnic-specialty | island | Independent (single) | epicerie-africaine-de-montreal.business.site | ethnic-search |
| 51 | Le Baobab | — | ethnic-specialty | island | Independent (single) | lebaobab.store | ethnic-search |
| 52 | Milano Fruiterie | — | ethnic-specialty | island | Independent (single) | milanofruiterie.com | fr-search, ethnic-search |
| 53 | Berchicci | — | ethnic-specialty | island | Independent importer (single) | store.berchicci.ca | ethnic-search |
| 54 | Baia dei Formaggi | — | ethnic-specialty | island | Independent (single) | labaiadeiformaggi.com | ethnic-search |
| 55 | Johnny Prosciutto | — | ethnic-specialty | island | Independent (single) | johnnyprosciutto.com | ethnic-search |
| 56 | Les Aliments Roma | — | ethnic-specialty | island | Independent producer (single) | alimentsroma.com | ethnic-search |
| 57 | Marché SA et Fils | — | ethnic-specialty | island | Independent (single) | saetfils.ca | ethnic-search |
| 58 | Boucherie Épicerie Soares et Fils | — | ethnic-specialty | island | Independent (single) | lesfillessoares.com | fr-search, ethnic-search |
| 59 | Chouricor | — | ethnic-specialty | island | Independent (single) | https://www.facebook.com/186622011348467 | fr-search, ethnic-search |
| 60 | Le Petit Milos | — | ethnic-specialty | island | Independent (single) | none found | ethnic-search |
| 61 | Sabor Latino | — | ethnic-specialty | island | Independent (chain of 2) | saborlatino.ca | ethnic-search |
| 62 | Marché Latino Asu Mare | — | ethnic-specialty | island | Independent (single) | asumare.ca | ethnic-search |
| 63 | Marché Latino La Bendición | — | ethnic-specialty | island | Independent (single) | marche-bendicion.poi.place | ethnic-search |
| 64 | Marché Andes | — | ethnic-specialty | island | Independent | marcheandes.com | fr-search |
| 65 | Marché Lima Limon | — | ethnic-specialty | island | Independent | marchelimalimon.ca | fr-search |
| 66 | Épicerie Latina | — | ethnic-specialty | island | Independent | chezlatina.com | fr-search |
| 67 | Meli-Melo Essentiel | — | ethnic-specialty | island | Independent (single) | none found | ethnic-search |
| 68 | Épicerie Costa | — | ethnic-specialty | island | Independent (single) | none found | ethnic-search |
| 69 | Lipa's Kosher Market | — | ethnic-specialty | island | Independent (single) | lipassupermarket.com | ethnic-search |
| 70 | The Fooderie Kosher Market | — | ethnic-specialty | island | Independent (single) | fooderiemarket.com | ethnic-search |
| 71 | Paradise Kosher | — | ethnic-specialty | greater | Independent (single) | paradisekosher.com | ethnic-search |
| 72 | One Stop Kosher | — | ethnic-specialty | island | Independent (single) | none found | ethnic-search |
| 73 | Kosher Quality | — | ethnic-specialty | island | Independent (single) | none found | ethnic-search |
| 74 | La Marguerite | — | ethnic-specialty | island | Independent (single) | lamarguerite.ca | ethnic-search |
| 75 | Cité Cacher | — | ethnic-specialty | island | Independent (single) | none found | ethnic-search |
| 76 | Bentzy's Food Depot | — | ethnic-specialty | island | Independent (single) | bentzysfood.com | ethnic-search |
| 77 | Euro-Deli Batory | — | ethnic-specialty | island | Independent (single) | eurodelibatory.ca | ethnic-search |
| 78 | Zytynsky's Deli | — | ethnic-specialty | island | Independent (single) | https://www.facebook.com/zytynskydeli/ | ethnic-search |
| 79 | Euro Marché | Euro Marche | ethnic-specialty | greater | Independent (family chain ~7) | euromarche.ca | flipp, ethnic-search |
| 80 | Rachelle-Béry | — | ethnic-specialty | qc-confirmed | Sobeys Inc. (Empire) | rachellebery.ca | fr-search, ethnic-search, en-search |
| 81 | Avril Supermarché Santé | — | ethnic-specialty | greater | Independent (Rolland Tanguay family) | avril.ca | fr-search, en-search, ethnic-search |
| 82 | Les Marchés Tau | — | ethnic-specialty | greater | Independent (chain of 5) | marchestau.com | fr-search, ethnic-search |
| 83 | La Moisson Supermarché Santé | — | ethnic-specialty | qc-unverified | Independent (single) | lamoisson.com | fr-search, ethnic-search |
| 84 | Première Moisson | — | ethnic-specialty | qc-confirmed | Metro Inc. (75%) | premieremoisson.com | fr-search |
| 85 | Poissonnerie La Mer | — | ethnic-specialty | island | Independent | lamer.ca | fr-search |
| 86 | Odessa Poissonnier | — | ethnic-specialty | island | Independent | odessapoissonnier.com | fr-search |
| 87 | Étoile Waldman | — | ethnic-specialty | island | Independent | etoilewaldman.ca | fr-search |
| 88 | Sami Fruits | — | ethnic-specialty | island | Independent | samifruits.com | fr-search |
| 89 | Fruiterie Valmont | Valmont | ethnic-specialty | island | Independent | val-mont.ca | fr-search |
| 90 | Fruits & Légumes 3 Saisons | — | ethnic-specialty | greater | Independent | marche3saisons.com | fr-search |
| 91 | Bulk Barn | — | ethnic-specialty | greater | Bulk Barn Foods Ltd. | bulkbarn.ca | en-search |
| 92 | 1117 Meats and Pantry | — | ethnic-specialty | island | Independent | none found | flipp |
| 93 | Mrakovic | Balkan butcher/deli | ethnic-specialty | island | Independent | none found | flipp |
| 94 | Shop Santé | Shop Sante | ethnic-specialty | island | Independent | shopsante.ca | flipp |
| 95 | La Vieille Europe | — | ethnic-specialty | island | Independent | lavieilleeurope.com | fr-search |
| 96 | Épicerie Les 3 Gourmets | — | ethnic-specialty | island | Independent | epicerie-les3gourmets.ca | fr-search |
| 97 | Costco Wholesale | — | warehouse | greater | Costco Wholesale Corp. | costco.com | flipp, fr-search, en-search |
| 98 | Mayrand Food Group | — | warehouse | greater | Mayrand (acquisition by Empire/Sobeys pending, announced Apr 2026) | mayrand.ca | en-search |
| 99 | Jean Coutu | — | pharmacy | qc-confirmed | Metro Inc. | jeancoutu.com | fr-search, en-search, flipp(rfd-flyers) |
| 100 | Brunet | — | pharmacy | qc-confirmed | Metro Inc. | brunet.ca | fr-search |
| 101 | Pharmaprix | — | pharmacy | qc-confirmed | Loblaw Companies (Shoppers Drug Mart banner) | pharmaprix.ca | flipp, en-search |
| 102 | Uniprix | — | pharmacy | qc-confirmed | Uniprix Inc. (Quebec co-op) | uniprix.com | en-search |
| 103 | Familiprix | — | pharmacy | qc-confirmed | Independent (Quebec chain) | familiprix.com | fr-search |
| 104 | I.D.A. | I.D.A. Prescription Centre | pharmacy | qc-unverified | — | guardian-ida-remedysrx.ca | flipp |
| 105 | Walmart | WM (RFD shorthand) | gen-merch | qc-confirmed | Walmart Canada | walmart.ca | flipp, rfd, en-search |
| 106 | Canadian Tire | CT (RFD shorthand; gift-card deals) | gen-merch | qc-confirmed | Canadian Tire Corp. | canadiantire.ca | flipp, rfd |
| 107 | Dollarama | — | dollar | qc-confirmed | Dollarama Inc. | dollarama.com | fr-search, en-search |
| 108 | Giant Tiger | Tigre Géant | dollar | qc-confirmed | Giant Tiger Stores Ltd. | gianttiger.com | flipp, rfd, fr-search, en-search |
| 109 | Marché Atwater | — | other | island | Corp. de gestion des marchés publics de Montréal | marchespublics-mtl.com | en-search |
| 110 | Marché Jean-Talon | — | other | island | Corp. de gestion des marchés publics de Montréal | marchespublics-mtl.com | en-search |
| 111 | Marché Maisonneuve | — | other | island | Corp. de gestion des marchés publics de Montréal | marchespublics-mtl.com | en-search |
| 112 | Voisin | — | other | qc-confirmed | Sobeys Inc. (dépanneur banner — not full grocery) | mon-voisin.com | ethnic-search |
| 113 | La Coop Alimentaire Montréal | — | other | island | Cooperative (independent) | lacoopalimentaire.ca | en-search |
| 114 | Bio Locaux | — | other | island | Coopérative CAPÉ | cape.coop | en-search |
| 115 | 3 Paniers | — | other | island | Carrefour Solidaire | carrefoursolidaire.org | en-search |
| 116 | Marché Solidaire Frontenac | — | other | island | Carrefour Solidaire | carrefoursolidaire.org | en-search |
| 117 | Épicerie Le Détour | — | other | island | Independent (solidarity) | epicerieledetour.org | fr-search |
| 118 | Épicerie Vrac & Bio | — | other | island | Independent | epicerievracetbio.com | fr-search |
| 119 | Vrac En Folie | — | other | island | Independent | vracenfolie.com | fr-search |
| 120 | Le Monde au Naturel | — | other | qc-unverified | Independent | mondenaturel.ca | fr-search |
| 121 | Coop Alentour | — | other | qc-unverified | Cooperative | coopalentour.ca | fr-search |
| 122 | L'Épicerie | Epicier.ca | other | island | Independent (delivery-only; no confirmed physical storefront) | epicier.ca | fr-search |
| 123 | Marché Axep | AXEP | traditional | qc-confirmed | Loblaw-affiliated banner group (independent owners) | axep.ca | rfd-flyers |

## Excluded — verified no Montreal/Quebec presence

| Name | Parent | Reason |
|---|---|---|
| No Frills | Loblaw Companies | Ontario+West only; appears on Flipp's national footer but no QC stores (store-locator data). Loblaw's QC discount is Maxi. |
| Food Basics | Metro Inc. | Ontario-only discount banner; Metro's QC discount is Super C. |
| Real Canadian Superstore | Loblaw Companies | No Quebec locations; Maxi & Cie / large Provigo fill that segment in QC. |
| FreshCo | Sobeys Inc. | Not in Quebec (ON/AB/BC/MB/SK/Atlantic only). |
| Dollar Tree | Dollar Tree Inc. | Not in Quebec (7 provinces only); Dollarama covers QC dollar-store segment. |
| Fortinos | Loblaw Companies | GTA only. |
| Longo's | Empire/Sobeys (51%) | GTA only. |

## Conflicts / needs verification in Phase 2

- **Kim Phat:** one source claims Sobeys majority stake since 2018; two other sources list it as
  independent. Treat as independent pending verification.
- **L'Intermarché:** RESOLVED 2026-10-12 — L'Intermarché is a brand of the AXEP banner group
  (axep.ca describes "un groupe de marques locales" including L'Intermarché, Freshmart, SuperValu,
  Shop Easy; the site carries the AXEP weekly flyer and a store locator). AXEP is a Loblaw-affiliated
  banner of independent grocers (~110 stores in Quebec, incl. 5 on Montreal island + 3 in Laval).
  Earlier "Metro-affiliated" claims were wrong.
- **Marché Maktaris** (Côte-des-Neiges): gourmet food shop, focus unconfirmed — dropped pending verification.
- **I.D.A.:** appears in Flipp's retailer list; banner site is guardian-ida-remedysrx.ca (McKesson)
  but no Quebec/Montreal I.D.A. presence found (Ontario/Western Canada only) — likely a Flipp
  national-footer artifact.
- **1117 Meats and Pantry / Mrakovic:** listed by Flipp as Montreal flyer merchants, but web search
  only finds same-named businesses in the Toronto area — possible Flipp national-listing artifacts or
  misidentifications; needs verification before Phase 2.
- **Le Petit Milos:** was Estiatorio Milos's specialty food shop on Av. du Parc; no standalone site
  found, appears closed or absorbed by the restaurant.
- **La Coop Alimentaire Montréal:** one directory listing marks the Jean-Talon E location permanently
  closed — worth verifying in Phase 2.
- **Marché Sheng Tai:** listed as island but the store is in Dollard-des-Ormeaux (still on-island,
  footprint tag stands).
- **Flipp listings for No Frills / Food Basics / Real Canadian Superstore / FreshCo:** confirmed by
  store-locator data to be national-footer artifacts with no Quebec stores — do not trust Flipp's
  retailer footer as Montreal-specific.
- **Sobeys (banner):** Sobeys Québec HQ is in Montréal-Nord, but the retail focus in Quebec is the IGA
  banner; standalone Sobeys-banner stores in Montreal not verified.
- **La Moisson:** flyer found on circulaires.club but historically located in Sainte-Thérèse (North Shore);
  Montreal-island presence unverified.
- **Marché Bonichoix / Les Marchés Tradition / Rachelle-Béry:** Quebec-wide banners with Montreal
  presence partially unverified (Yellow Pages hits for Bonichoix were all off-island).

## Gaps noticed

- **RFD exact thread (#2828330):** could not be fetched directly (not search-indexed yet); stores came
  from adjacent weeks of the same series. A live-browser check would confirm the exact Oct 8–14 list.
- **Website URLs:** filled 2026-10-12 via targeted per-store searches (66 URLs added across three
  research batches). Rows marked `none found` have no discoverable web presence; `Facebook only` /
  `Instagram only` rows have no official site (fallback URL recorded per user instruction). One
  directory-listing fallback: Marché BKR (Google Business site), Marché Latino La Bendición (poi.place).
- **Greek grocery segment is thin:** only Le Petit Milos surfaced; Greek needs largely served via
  Adonis/other Mediterranean grocers.
- **Long tail of single-store independents:** more small independents exist (e.g. Alimentation
  Blanchette, Marché Lobo, Frugal); Phase 2 can expand.
- **No "Marché Central" grocery store found** — only the Marché Central area; likely not a banner.
- **Name collision:** "Marché Oriental" (7101 Rue St-Denis) and "Marché Oriental Jang Teu"
  (H Marché/H Mart, 3 stores) are different businesses sharing a name.
- **RFD thread shorthand** (useful when parsing round-up posts in later phases): SupC=Super C,
  Pro=Provigo, Ado=Adonis, Met=Metro, GT=Giant Tiger, WM=Walmart, PA=Marché PA, KP=Kim Phat,
  CT=Canadian Tire. The weekly series covers MAXI, SUPER C, IGA, PROVIGO, METRO, ADONIS,
  Marché PA, WALMART, GIANT TIGER weekly; KIM PHAT and C&T added Thursdays.
