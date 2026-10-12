# Stores — summary (Phase 2)

Generated 2026-10-12 from `docs/research/stores/*.yaml` — the YAML files are the
table of record; this is the human overview. Columns: flyer formats, product-search
kind, location count + harvest mechanism (API = JSON endpoint observed).

## Tier 1 — major chains (full depth) (25 stores)

| Store | Type | Website | Flyers | Search | Locations | Parent |
|---|---|---|---|---|---|---|
| Marché Adonis | ethnic-specialty | www.groupeadonis.ca | Y (html/images) | N | 16 (locator) | Metro Inc. |
| Avril Supermarché Santé | ethnic-specialty | www.avril.ca | Y (html) | Y (html) | 10 (locator) | Rolland Tanguay family (independent) |
| Brunet | pharmacy | www.brunet.ca | Y (images/json-api) | Y (html) | 180 (locator) | Metro Inc. |
| Bulk Barn | ethnic-specialty | www.bulkbarn.ca | Y (html) | N | 280 (locator) | Bulk Barn Foods Ltd. |
| Canadian Tire | gen-merch | www.canadiantire.ca | Y (html) | Y (spa) | 500 (locator) | Canadian Tire Corp. |
| Costco Wholesale | warehouse | www.costco.ca | Y (html) | Y (html) | 115 (locator) | Costco Wholesale Corp. |
| Dollarama | dollar | www.dollarama.com | N | N | 1734 (locator) | Dollarama Inc. |
| Familiprix | pharmacy | www.familiprix.com | Y (json-api/images) | Y (html) | 358 (locator) | Familiprix Inc. (independent Quebec chain; 100% owned by its member pharmacists) |
| Giant Tiger | dollar | www.gianttiger.com | Y (html) | Y (html) | 260 (locator) | Giant Tiger Stores Ltd. |
| IGA Extra | traditional | www.iga.net | Y (html/images) | Y (html) | 133 (locator) | Sobeys Inc. (Empire Company Limited) |
| IGA | traditional | www.iga.net | Y (html/images) | Y (html) | 194 (locator) | Sobeys Inc. (Empire Company Limited) |
| Jean Coutu | pharmacy | www.jeancoutu.com | Y (images/json-api) | Y (html) | 380 (locator) | Metro Inc. |
| Kim Phat | ethnic-specialty | www.kimphat.com | Y (images/json-api) | N | 5 (locator) | Sobeys Inc. (Empire Company Ltd.) - majority stake since 2018 |
| Loblaws | traditional | www.loblaws.ca | Y (html/images) | Y (spa) | 15 (locator) | Loblaw Companies Limited |
| Marche PA | traditional | www.supermarchepa.com | Y (images/json-api) | N | 5 (locator) | Independent (chain) |
| Maxi | traditional | www.maxi.ca | Y (html/images/pdf) | Y (spa) | 188 (locator) | Loblaw Companies Limited |
| Metro Plus | traditional | www.metro.ca | Y (html/images) | Y (html) | 50 (locator) | Metro Inc. |
| Metro | traditional | www.metro.ca | Y (html/images) | Y (html) | 350 (locator) | Metro Inc. |
| Pharmaprix | pharmacy | www.pharmaprix.ca | Y (html/images) | Y (spa) | 370 (locator) | Loblaw Companies Limited |
| Provigo | traditional | www.provigo.ca | Y (html/images/pdf) | Y (spa) | 300 (locator) | Loblaw Companies Limited |
| Rachelle-Béry | ethnic-specialty | www.rachellebery.ca | Y (html/images) | N | 105 (locator) | Sobeys Inc. (Empire Company Limited) |
| Super C | traditional | www.superc.ca | Y (html/images) | Y (html) | 122 (locator) | Metro Inc. |
| T&T Supermarché | ethnic-specialty | www.tntsupermarket.com | Y (html/images) | N | 2 (locator) | Loblaw Companies Limited |
| Uniprix | pharmacy | www.uniprix.com | Y (json-api/images) | N | 360 (locator) | McKesson Canada |
| Walmart | gen-merch | www.walmart.ca | Y (html) | Y (spa) | 401 (locator) | Walmart Canada |

## Tier 2 — banners / small chains (medium depth) (17 stores)

| Store | Type | Website | Flyers | Search | Locations | Parent |
|---|---|---|---|---|---|---|
| Euro Marché | ethnic-specialty | euromarche.ca | Y (images) | N | 6 (locator) | Independent (family chain) |
| H Marché | ethnic-specialty | www.hmartmontreal.com | N | N | 3 (locator) | H Mart |
| IGA Express / Mini | other | www.iga.net | Y (images) | Y (html) | (locator) | Sobeys Inc. (Sobeys Québec / Empire Company Ltd.) |
| L'intermarché Palumbo | traditional | www.marchepalumbo.com | Y (html/images) | Y (html) | 5 (locator) | Palumbo family (independent) |
| L'Intermarché | traditional | lintermarche.ca | Y (images) | N | (?) | AXEP (Loblaw-affiliated banner group) |
| La Moisson Supermarché Santé | ethnic-specialty | lamoisson.com | Y (images/html) | Y (html) | 1 (locator) | Independent (single store) |
| Marché Ami | traditional | marcheami.ca | Y (images) | N | 187 (?) | Metro Inc. |
| Marché Axep | traditional | axep.ca | Y (images) | N | 22 (?) | AXEP (Loblaw-affiliated banner group) |
| Marché Bonichoix | traditional | www.bonichoix.com | Y (images) | N | 42 (locator) | Sobeys Inc. (Sobeys Québec / Empire Company Ltd.) |
| Marché C&T | ethnic-specialty | www.marchect.ca | Y (html/images) | N | 4 (locator) | Independent (family-owned chain) |
| Marché Richelieu | traditional | www.marcherichelieu.ca | Y (images) | N | 63 (locator) | Metro Inc. |
| Les Marchés Tau | ethnic-specialty | marchestau.com | Y (html/images) | Y (html) | 6 (locator) | Independent (chain of 6) |
| Les Marchés Tradition | traditional | www.marchestradition.com | Y (images) | N | 75 (locator) | Sobeys Inc. (Sobeys Québec / Empire Company Ltd.) |
| Mayrand Food Group | warehouse | mayrand.ca | Y (pdf/html) | Y (html) | 4 (locator) | Empire Company Limited (via Sobeys Inc.) |
| Première Moisson | ethnic-specialty | premieremoisson.com | Y (html) | N | 25 (locator) | Metro Inc. |
| Shop Santé | ethnic-specialty | shopsante.ca | Y (html/images) | Y (html) | 50 (locator) | Shop Santé Inc. |
| Sobeys (banner) | traditional | www.sobeys.com | N | Y (html) | 0 (?) | Sobeys Inc. (Empire Company Ltd.) |

## Tier 3 — independents (minimal) (81 stores)

| Store | Type | Website | Flyers | Search | Locations | Parent |
|---|---|---|---|---|---|---|
| 1117 Meats and Pantry | ethnic-specialty | www.1117mp.com | N | N | 1 (?) |  |
| 3 Paniers | other | carrefoursolidaire.org/activites/… | N | N | 1 (?) | Carrefour Solidaire (opérée par Marché Frontenac, OBNL) |
| Fruits & Légumes 3 Saisons | ethnic-specialty | www.marche3saisons.com | N | N | 1 (?) |  |
| 5 Saisons | other | www.les5saisons.ca | N | N | 1 (?) | Metro Inc. |
| Akhavan | ethnic-specialty | akhavanfood.com | N | Y (html) | 2 (?) |  |
| Les Aliments Roma | ethnic-specialty | alimentsroma.com | N | N | 1 (?) |  |
| Marché Latino Asu Mare | ethnic-specialty | asumare.ca | N | N | 1 (?) |  |
| Baia dei Formaggi | ethnic-specialty | www.labaiadeiformaggi.com | N | N | 1 (?) |  |
| Bentzy's Food Depot | ethnic-specialty | www.bentzysfood.com | N | N | 1 (?) |  |
| Berchicci | ethnic-specialty | store.berchicci.ca | N | N | 1 (?) | Importation Berchicci Ltée |
| Bio Locaux | other | cape.coop | N | N | 1 (?) | CAPÉ — Coopérative pour l'agriculture de proximité écologique |
| Chouricor | ethnic-specialty | www.facebook.com/186622011348467 | N | N | 1 (?) |  |
| Cité Cacher | ethnic-specialty | www.facebook.com/572569476146105 | N | N | 1 (?) |  |
| Coop Alentour | other | coopalentour.ca | Y (html) | N | 1 (?) |  |
| La Coop Alimentaire Montréal | other | lacoopalimentaire.ca | N | N | 1 (?) |  |
| Délices du Maghreb | ethnic-specialty | www.delicesdumaghreb.ca | N | N | 1 (?) |  |
| Épicerie Africaine de Montréal | ethnic-specialty | epicerie-africaine-de-montreal.bu… | N | N | 1 (?) |  |
| Épicerie Coréenne et Japonaise | ethnic-specialty |  | N | N | 1 (?) |  |
| Épicerie Costa | ethnic-specialty |  | N | N | 1 (?) |  |
| Épicerie Du Bazaar | ethnic-specialty | www.bazaarfood.ca | N | Y (html) | 1 (?) |  |
| Épicerie Latina | ethnic-specialty | www.chezlatina.com | N | N | 2 (?) |  |
| Épicerie Le Détour | other | epicerieledetour.org | N | N | 1 (?) |  |
| L'Épicerie (l'épicier) | other | epicier.ca | N | N | 0 (?) |  |
| Étoile Waldman | ethnic-specialty | www.etoilewaldman.ca | N | N | 1 (?) |  |
| Euro-Deli Batory | ethnic-specialty | eurodelibatory.ca | N | N | 1 (?) |  |
| The Fooderie Kosher Market | ethnic-specialty | www.fooderiemarket.com | N | N | 1 (?) |  |
| Marché Solidaire Frontenac | other | carrefoursolidaire.org | N | N | 1 (?) | Carrefour Solidaire (opérée par Marché Frontenac, OBNL) |
| Fruiterie Valmont | ethnic-specialty | www.val-mont.ca | N | N | 1 (?) |  |
| G&D Supermarket | ethnic-specialty | gdsupermarche.com | N | N | 1 (?) |  |
| Épicerie Heng Heng Chanchaya | ethnic-specialty |  | N | N | 1 (?) |  |
| I.D.A. | pharmacy | www.guardian-ida-remedysrx.ca | N | N | 0 (?) | McKesson Canada |
| Johnny Prosciutto | ethnic-specialty | johnnyprosciutto.com | N | N | 1 (?) |  |
| Kosher Quality | ethnic-specialty | kosher-quality-bakery-ltd.busines… | N | N | 1 (?) |  |
| Marché Latino La Bendición | ethnic-specialty | marche-bendicion.poi.place | N | N | 1 (?) |  |
| La Marguerite | ethnic-specialty | www.lamarguerite.ca | N | N | 1 (?) |  |
| La Vieille Europe | ethnic-specialty | lavieilleeurope.com | N | N | 1 (?) |  |
| Le Baobab | ethnic-specialty | lebaobab.store | N | N | 1 (?) |  |
| Épicerie Les 3 Gourmets | ethnic-specialty | www.epicerie-les3gourmets.ca | N | N | 1 (?) |  |
| Lipa's Kosher Market | ethnic-specialty | www.lipassupermarket.com | N | N | 1 (?) |  |
| Magasin Amira | ethnic-specialty | magasinamira.ca | N | Y (html) | 1 (?) |  |
| Magazin Istanbul | ethnic-specialty |  | N | N | 1 (?) |  |
| Marché 786 | ethnic-specialty | marche786.ca | N | N | 1 (?) |  |
| Marché Andes | ethnic-specialty | www.marcheandes.com | N | N | 1 (?) |  |
| Marché Atwater | other | www.marchespublics-mtl.com/marche… | N | N | 1 (?) | Corporation de gestion des marchés publics de Montréal |
| Marché BKR | ethnic-specialty | marche-bkr-laurentien.business.si… | N | N | 1 (?) |  |
| Marché Bonanza | ethnic-specialty | bonanzalalumiere.com | N | N | 1 (?) |  |
| Marché Duc Thanh | ethnic-specialty | www.facebook.com/100772778660036 | N | N | 1 (?) |  |
| Le Marché Esposito | ethnic-specialty | lemarcheesposito.ca | Y (html) | N | 6 (?) |  |
| Marché Fu Tai | ethnic-specialty | www.marchefutai.ca | Y (html) | N | 1 (?) |  |
| Marché Jean-Talon | other | www.marchespublics-mtl.com | N | N | 1 (?) | Corporation de gestion des marchés publics de Montréal |
| Marché Kim Hour | ethnic-specialty | www.facebook.com/170794359599794 | N | N | 1 (?) |  |
| Marché Kim-Po | ethnic-specialty | www.marchekimpo.ca | N | N | 1 (?) |  |
| Marché Lavaniya | ethnic-specialty | marche-lavaniya.business.site | N | N | 1 (?) |  |
| Marché Lian Tai | ethnic-specialty | www.marcheliantai.ca | Y (html) | Y (html) | 1 (?) |  |
| Marché Lima Limon | ethnic-specialty | marchelimalimon.ca | N | N | 1 (?) |  |
| Marché Maisonneuve | other | www.marchespublics-mtl.com | N | N | 1 (?) | Corporation de gestion des marchés publics de Montréal |
| Marché Newon | ethnic-specialty | www.marchenewon.com | N | N | 2 (?) |  |
| Marché Oriental (St-Denis) | ethnic-specialty | orientalstdenis.ca | N | N | 1 (?) |  |
| Marché SA et Fils | ethnic-specialty | www.saetfils.ca | Y (html) | N | 1 (?) |  |
| Marché Sheng Tai | ethnic-specialty | www.marcheshengtai.ca | Y (html) | Y (html) | 1 (?) |  |
| Marché Sultan | ethnic-specialty | www.instagram.com/marchesultan.mtl | N | N | 1 (?) |  |
| Marché Tharsini | ethnic-specialty | m.facebook.com/pages/category/Sup… | N | N | 1 (?) |  |
| Marché Victoria Orientale | ethnic-specialty | www.facebook.com/marchevictoria | N | N | 1 (?) |  |
| Meli-Melo Essentiel | ethnic-specialty | www.facebook.com/marchemelimelo.c… | N | N | 1 (?) |  |
| Milano Fruiterie | ethnic-specialty | milanofruiterie.ca | N | N | 1 (?) |  |
| Le Monde au Naturel | other | mondenaturel.ca | Y (images) | Y (html) | 1 (?) |  |
| Mrakovic Meat and Deli | ethnic-specialty | mrakovic.com | N | N | 2 (?) |  |
| Odessa Poissonnier | ethnic-specialty | odessapoissonnier.com | N | N | 5 (?) |  |
| One Stop Kosher | ethnic-specialty |  | N | N | 1 (?) |  |
| Paradise Kosher | ethnic-specialty | www.paradisekosher.com | N | N | 1 (?) |  |
| Le Petit Milos | ethnic-specialty |  | N | N | 0 (?) | Estiatorio Milos (absorbed) |
| Poissonnerie La Mer | ethnic-specialty | www.lamer.ca | N | N | 2 (?) |  |
| Sabor Latino | ethnic-specialty | saborlatino.ca | N | N | 2 (?) |  |
| Sami Fruits | ethnic-specialty | samifruits.com | N | N | 4 (?) |  |
| Segal's Market | traditional | www.facebook.com/2012417038809524 | N | N | 1 (?) |  |
| Boucherie Épicerie Soares et Fils | ethnic-specialty | www.lesfillessoares.com | N | N | 1 (?) |  |
| South Indian Spices | ethnic-specialty |  | N | N | 1 (?) |  |
| Voisin | other | www.mon-voisin.com | Y (html) | N | 70 (locator) | Sobeys (Sobeys Québec — secteur Multi-surfaces et Pétrole) |
| Vrac En Folie | other | www.vracenfolie.com | N | Y (html) | 1 (?) |  |
| Épicerie Vrac & Bio | other | epicerievracetbio.com | N | Y (html) | 1 (?) |  |
| Zytynsky's Deli | ethnic-specialty | www.facebook.com/zytynskydeli | N | N | 1 (?) |  |
