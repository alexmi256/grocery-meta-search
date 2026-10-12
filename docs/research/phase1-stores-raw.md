# Phase 1 — Raw Store Discovery List (Montreal)

**Date:** 2026-10-12
**Status:** raw research output — Phase 1 only (list). Not yet DB-loaded or location-verified.

## Method

Four parallel research tracks:
1. **flipp** — Flipp store listings for Montreal (note: Flipp's Montreal store pages are JS-heavy and
   could not be fetched directly; coverage comes from search-indexed Flipp Montreal pages plus Flipp's
   retailer footer, which may be national rather than Montreal-specific).
2. **rfd** — RedFlagDeals "Week of 8th–14th October grocery round-up (Quebec)" weekly series.
   The exact thread (#2828330) was not fetchable; entries come from adjacent weeks of the same series
   (Jun–Sep 2026 editions), which use a stable banner set.
3. **fr-search** — French-language web searches (`circulaires épicerie Montréal`, `supermarchés Montréal`, etc.).
4. **en-search** — English-language web searches (`Montreal grocery store flyers`, national-chain location verification).
5. **ethnic-search** — Bilingual searches targeting ethnic, specialty, and independent grocers.

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
| 11 | Les Marchés Tradition | — | traditional | qc-unverified | Sobeys Inc. (Empire) | — | flipp, fr-search, en-search, ethnic-search |
| 12 | Marché Bonichoix | — | traditional | qc-unverified | Sobeys Inc. (Empire) | bonichoix.com | fr-search, en-search, ethnic-search |
| 13 | L'Intermarché | — | traditional | qc-confirmed | contested — see notes | — | fr-search, ethnic-search |
| 14 | Marché Ami | — | traditional | qc-confirmed | Metro Inc. (banner) | — | fr-search |
| 15 | Marché PA | PA (RFD shorthand) | traditional | island | Independent (chain) | — | rfd, fr-search, en-search |
| 16 | Intermarché Palumbo | Marché Palumbo | traditional | greater | Palumbo family (independent) | marchepalumbo.com | ethnic-search |
| 17 | Le Marché Esposito | — | traditional | island | Independent (chain of 2) | lemarcheesposito.ca | ethnic-search |
| 18 | Segal's Market | — | traditional | island | Independent (single) | — | fr-search, en-search |
| 19 | Marché Bonanza | Bonanza Lalumière | traditional | island | Independent | bonanzalalumiere.com | fr-search |
| 20 | 5 Saisons | — | ethnic-specialty | island | Metro Inc. | — | ethnic-search |
| 21 | Sobeys | — | traditional | qc-unverified | Sobeys Inc. (Empire) | — | flipp, en-search |
| 22 | Marché Adonis | Adonis Market (EN) | ethnic-specialty | greater | Metro Inc. (100% since 2017) | groupeadonis.ca | flipp, rfd, fr-search, en-search, ethnic-search |
| 23 | Kim Phat | KP (RFD shorthand) | ethnic-specialty | greater | contested — see notes | kimphat.com | rfd, fr-search, en-search, ethnic-search |
| 24 | T&T Supermarché | T&T Supermarket | ethnic-specialty | greater | Loblaw Companies (since 2009) | — | fr-search, en-search, ethnic-search |
| 25 | Marché C&T | — | ethnic-specialty | greater | Independent (chain of 3+) | marchect.ca | rfd, fr-search, ethnic-search |
| 26 | Marché Newon | — | ethnic-specialty | island | Independent (single) | marchenewon.com | fr-search, ethnic-search |
| 27 | G&D Supermarket | — | ethnic-specialty | island | Independent (single) | gdsupermarche.com | ethnic-search |
| 28 | Marché Kim Hour | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 29 | Marché Kim-Po | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 30 | Marché Oriental (St-Denis) | — | ethnic-specialty | island | Independent (single) | orientalstdenis.ca | ethnic-search |
| 31 | Épicerie Heng Heng Chanchaya | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 32 | Marché Duc Thanh | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 33 | H Marché | Marché Oriental Jang Teu | ethnic-specialty | island | H Mart (Korean chain) | hmartmontreal.com | ethnic-search |
| 34 | Épicerie Coréenne et Japonaise | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 35 | Marché Lian Tai | — | ethnic-specialty | island | Independent (single) | — | fr-search |
| 36 | Marché Fu Tai | — | ethnic-specialty | island | Independent (single) | — | fr-search |
| 37 | Marché Sheng Tai | — | ethnic-specialty | island | Independent (single) | — | fr-search |
| 38 | Marché Victoria Orientale | — | ethnic-specialty | island | Independent (single) | — | fr-search, ethnic-search |
| 39 | South Indian Spices | — | ethnic-specialty | island | Independent (single) | — | fr-search, ethnic-search |
| 40 | Marché Lavaniya | — | ethnic-specialty | island | Independent (single) | marche-lavaniya.business.site | ethnic-search |
| 41 | Marché 786 | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 42 | Magasin Amira | — | ethnic-specialty | island | Independent | — | fr-search |
| 43 | Marché BKR | — | ethnic-specialty | island | Independent | — | fr-search |
| 44 | Marché Sultan | — | ethnic-specialty | island | Independent | — | fr-search |
| 45 | Marché Tharsini | — | ethnic-specialty | island | Independent | — | fr-search |
| 46 | Akhavan | — | ethnic-specialty | island | Independent (family chain of 2) | akhavanfood.com | ethnic-search |
| 47 | Délices du Maghreb | — | ethnic-specialty | island | Independent (single) | delicesdumaghreb.ca | ethnic-search |
| 48 | Magazin Istanbul | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 49 | Épicerie Du Bazaar | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 50 | Épicerie Africaine de Montréal | — | ethnic-specialty | island | Independent (single) | epicerie-africaine-de-montreal.business.site | ethnic-search |
| 51 | Le Baobab | — | ethnic-specialty | island | Independent (single) | lebaobab.store | ethnic-search |
| 52 | Milano Fruiterie | — | ethnic-specialty | island | Independent (single) | milanofruiterie.com | fr-search, ethnic-search |
| 53 | Berchicci | — | ethnic-specialty | island | Independent importer (single) | store.berchicci.ca | ethnic-search |
| 54 | Baia dei Formaggi | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 55 | Johnny Prosciutto | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 56 | Les Aliments Roma | — | ethnic-specialty | island | Independent producer (single) | alimentsroma.com | ethnic-search |
| 57 | Marché SA et Fils | — | ethnic-specialty | island | Independent (single) | saetfils.ca | ethnic-search |
| 58 | Boucherie Épicerie Soares et Fils | — | ethnic-specialty | island | Independent (single) | lesfillessoares.com | fr-search, ethnic-search |
| 59 | Chouricor | — | ethnic-specialty | island | Independent (single) | — | fr-search, ethnic-search |
| 60 | Le Petit Milos | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 61 | Sabor Latino | — | ethnic-specialty | island | Independent (chain of 2) | saborlatino.ca | ethnic-search |
| 62 | Marché Latino Asu Mare | — | ethnic-specialty | island | Independent (single) | asumare.ca | ethnic-search |
| 63 | Marché Latino La Bendición | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 64 | Marché Andes | — | ethnic-specialty | island | Independent | marcheandes.com | fr-search |
| 65 | Marché Lima Limon | — | ethnic-specialty | island | Independent | marchelimalimon.ca | fr-search |
| 66 | Épicerie Latina | — | ethnic-specialty | island | Independent | — | fr-search |
| 67 | Meli-Melo Essentiel | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 68 | Épicerie Costa | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 69 | Lipa's Kosher Market | — | ethnic-specialty | island | Independent (single) | lipassupermarket.com | ethnic-search |
| 70 | The Fooderie Kosher Market | — | ethnic-specialty | island | Independent (single) | fooderiemarket.com | ethnic-search |
| 71 | Paradise Kosher | — | ethnic-specialty | greater | Independent (single) | paradisekosher.com | ethnic-search |
| 72 | One Stop Kosher | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 73 | Kosher Quality | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 74 | La Marguerite | — | ethnic-specialty | island | Independent (single) | lamarguerite.ca | ethnic-search |
| 75 | Cité Cacher | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 76 | Bentzy's Food Depot | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 77 | Euro-Deli Batory | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 78 | Zytynsky's Deli | — | ethnic-specialty | island | Independent (single) | — | ethnic-search |
| 79 | Euro Marché | Euro Marche | ethnic-specialty | greater | Independent (family chain ~7) | euromarche.ca | flipp, ethnic-search |
| 80 | Rachelle-Béry | — | ethnic-specialty | qc-confirmed | Sobeys Inc. (Empire) | rachellebery.ca | fr-search, ethnic-search, en-search |
| 81 | Avril Supermarché Santé | — | ethnic-specialty | greater | Independent (Rolland Tanguay family) | avril.ca | fr-search, en-search, ethnic-search |
| 82 | Les Marchés Tau | — | ethnic-specialty | greater | Independent (chain of 5) | marchestau.com | fr-search, ethnic-search |
| 83 | La Moisson Supermarché Santé | — | ethnic-specialty | qc-unverified | Independent (single) | lamoisson.com | fr-search, ethnic-search |
| 84 | Première Moisson | — | ethnic-specialty | qc-confirmed | Metro Inc. (75%) | — | fr-search |
| 85 | Poissonnerie La Mer | — | ethnic-specialty | island | Independent | lamer.ca | fr-search |
| 86 | Odessa Poissonnier | — | ethnic-specialty | island | Independent | odessapoissonnier.com | fr-search |
| 87 | Étoile Waldman | — | ethnic-specialty | island | Independent | etoilewaldman.ca | fr-search |
| 88 | Sami Fruits | — | ethnic-specialty | island | Independent | samifruits.com | fr-search |
| 89 | Fruiterie Valmont | Valmont | ethnic-specialty | island | Independent | — | fr-search |
| 90 | Fruits & Légumes 3 Saisons | — | ethnic-specialty | island | Independent | — | fr-search |
| 91 | Bulk Barn | — | ethnic-specialty | greater | Bulk Barn Foods Ltd. | bulkbarn.ca | en-search |
| 92 | 1117 Meats and Pantry | — | ethnic-specialty | island | Independent | — | flipp |
| 93 | Mrakovic | Balkan butcher/deli | ethnic-specialty | island | Independent | — | flipp |
| 94 | Shop Santé | Shop Sante | ethnic-specialty | island | Independent | — | flipp |
| 95 | La Vieille Europe | — | ethnic-specialty | island | Independent | — | fr-search |
| 96 | Épicerie Les 3 Gourmets | — | ethnic-specialty | island | Independent | epicerie-les3gourmets.ca | fr-search |
| 97 | Costco Wholesale | — | warehouse | greater | Costco Wholesale Corp. | costco.com | flipp, fr-search, en-search |
| 98 | Mayrand Food Group | — | warehouse | greater | Mayrand (acquisition by Empire/Sobeys pending, announced Apr 2026) | — | en-search |
| 99 | Jean Coutu | — | pharmacy | qc-confirmed | Metro Inc. | jeancoutu.com | fr-search, en-search, flipp(rfd-flyers) |
| 100 | Brunet | — | pharmacy | qc-confirmed | Metro Inc. | — | fr-search |
| 101 | Pharmaprix | — | pharmacy | qc-confirmed | Loblaw Companies (Shoppers Drug Mart banner) | pharmaprix.ca | flipp, en-search |
| 102 | Uniprix | — | pharmacy | qc-confirmed | Uniprix Inc. (Quebec co-op) | — | en-search |
| 103 | Familiprix | — | pharmacy | qc-confirmed | Independent (Quebec chain) | — | fr-search |
| 104 | I.D.A. | I.D.A. Prescription Centre | pharmacy | qc-unverified | — | — | flipp |
| 105 | Walmart | WM (RFD shorthand) | gen-merch | qc-confirmed | Walmart Canada | — | flipp, rfd, en-search |
| 106 | Canadian Tire | CT (RFD shorthand; gift-card deals) | gen-merch | qc-confirmed | Canadian Tire Corp. | — | flipp, rfd |
| 107 | Dollarama | — | dollar | qc-confirmed | Dollarama Inc. | — | fr-search, en-search |
| 108 | Giant Tiger | Tigre Géant | dollar | qc-confirmed | Giant Tiger Stores Ltd. | gianttiger.com | flipp, rfd, fr-search, en-search |
| 109 | Marché Atwater | — | other | island | Corp. de gestion des marchés publics de Montréal | — | en-search |
| 110 | Marché Jean-Talon | — | other | island | Corp. de gestion des marchés publics de Montréal | — | en-search |
| 111 | Marché Maisonneuve | — | other | island | Corp. de gestion des marchés publics de Montréal | — | en-search |
| 112 | Voisin | — | other | qc-confirmed | Sobeys Inc. (dépanneur banner — not full grocery) | — | ethnic-search |
| 113 | La Coop Alimentaire Montréal | — | other | island | Cooperative (independent) | — | en-search |
| 114 | Bio Locaux | — | other | island | Coopérative CAPÉ | — | en-search |
| 115 | 3 Paniers | — | other | island | Carrefour Solidaire | — | en-search |
| 116 | Marché Solidaire Frontenac | — | other | island | Carrefour Solidaire | — | en-search |
| 117 | Épicerie Le Détour | — | other | island | Independent (solidarity) | — | fr-search |
| 118 | Épicerie Vrac & Bio | — | other | island | Independent | epicerievracetbio.com | fr-search |
| 119 | Vrac En Folie | — | other | island | Independent | — | fr-search |
| 120 | Le Monde au Naturel | — | other | qc-unverified | Independent | — | fr-search |
| 121 | Coop Alentour | — | other | qc-unverified | Cooperative | — | fr-search |
| 122 | L'Épicerie | Epicier.ca | other | island | Independent (delivery-only; no confirmed physical storefront) | epicier.ca | fr-search |

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
- **L'Intermarché:** one source says independent banner formerly Metro-affiliated; another says
  Loblaw/Provigo-affiliated banner. Affiliation unverified.
- **Marché Maktaris** (Côte-des-Neiges): gourmet food shop, focus unconfirmed — dropped pending verification.
- **I.D.A.:** appears in Flipp's retailer list but may be a national-footer artifact (I.D.A. is
  primarily an Ontario pharmacy network); no Montreal presence confirmed.
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
- **Website URLs:** filled only where seen verbatim in tool results; ~50 rows still lack a URL.
  Phase 2 store-locator lookups will fill these.
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
