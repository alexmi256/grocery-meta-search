# Classification review — PC Express taxonomy

Generated from `data/grocery.db` (11506 items, 9424 classified = 81.9%). 10 random items per store (seed 20261015), each with its picture, stored details and assigned category.

Taxonomy: PC Express departments/subcategories as documented in [product-categories.md](product-categories.md), minus the attribute-based *Natural and Organic* department, plus Baby / Pet / Household / Health & Beauty buckets for non-food flyer items. Method `rule` = a named keyword rule fired; `frozen-remap` = fresh hit remapped by a frozen marker; `store-prior` = no rule matched, fell back to the store's trade.

| Store | Items | Classified |
|---|---:|---:|
| Akhavan | 19 | 84% |
| Aliments Merci | 29 | 62% |
| Avril Supermarché Santé | 112 | 65% |
| Brunet | 596 | 100% |
| Bulk Barn | 6 | 100% |
| Canadian Tire | 734 | 18% |
| Coop Alentour | 22 | 77% |
| Costco Wholesale | 85 | 15% |
| Euro Marché | 60 | 75% |
| Familiprix | 831 | 100% |
| Fruiterie Valmont | 43 | 42% |
| Fruits & Légumes 3 Saisons | 5 | 40% |
| Giant Tiger | 29 | 69% |
| H Marché | 16 | 88% |
| IGA | 467 | 87% |
| IGA Express / Mini | 467 | 87% |
| IGA Extra | 481 | 86% |
| Jean Coutu | 730 | 100% |
| Kim Phat | 166 | 85% |
| L'Intermarché | 81 | 83% |
| L'intermarché Palumbo | 7 | 100% |
| La Moisson Supermarché Santé | 35 | 80% |
| Le Marché Esposito | 43 | 72% |
| Le Monde au Naturel | 70 | 100% |
| Les Marchés Tau | 37 | 51% |
| Les Marchés Tradition | 157 | 83% |
| M&M Food Market | 70 | 100% |
| Marche PA | 194 | 91% |
| Marché Adonis | 373 | 93% |
| Marché Ami | 89 | 92% |
| Marché Andes | 2 | 100% |
| Marché Axep | 82 | 82% |
| Marché BKR | 14 | 50% |
| Marché Bonanza | 28 | 11% |
| Marché Bonichoix | 144 | 87% |
| Marché C&T | 59 | 69% |
| Marché Frutta Si | 14 | 86% |
| Marché Fu Tai | 47 | 64% |
| Marché Korea | 162 | 71% |
| Marché Lian Tai | 132 | 80% |
| Marché Newon | 114 | 68% |
| Marché Richelieu | 117 | 93% |
| Marché Sheng Tai | 54 | 70% |
| Marché Sultan | 29 | 24% |
| Maxi | 326 | 92% |
| Mayrand Food Group | 37 | 24% |
| Metro | 790 | 87% |
| Metro Plus | 790 | 87% |
| Milano Fruiterie | 15 | 67% |
| Odessa Poissonnier | 28 | 100% |
| Pharmaprix | 594 | 100% |
| Provigo | 217 | 88% |
| Rachelle-Béry | 87 | 76% |
| Shop Santé | 32 | 28% |
| Super C | 501 | 91% |
| T&T Supermarché | 112 | 23% |
| Uniprix | 247 | 100% |
| Walmart | 553 | 67% |
| Wholesale Club | 122 | 62% |
| Épicerie PA Nature | 3 | 33% |

## Akhavan (`akhavan`)

### 1. BLENTILLES ROUGES MENTIÈRES AKHAVAN ls WHOLE RED LENTILS

![item 9774](classification-review-assets/item-9774.jpg)

- **Category:** Pantry > Dried Beans, Vegetables & Grains (FR: Produits du garde-manger > Haricots secs, légumes et grains)
- **How classified:** rule (`beans-grains`)
- **Price:** 99.00 $ · as printed: “99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 2. BETTERAVES | e0%, BEETS

![item 9786](classification-review-assets/item-9786.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 3. PRUNE HAJ a ‘ QUES HAJ HASSANI

![item 9782](classification-review-assets/item-9782.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 4. RIT RES ANA RE | EAU DES CHICOREE | ? TUBA à CHICORY WATER

![item 9783](classification-review-assets/item-9783.jpg)

- **Category:** Drinks > Water (FR: Boissons > Eau)
- **How classified:** rule (`water`)
- **Price:** 66.00 $ · as printed: “66”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 5. KASHK (CORNICHONS AL’AIL!| CORNICHON MÉLANGÉ SOMAYEHMN HYDERABADI MEHRAN (= MEHRAN KASHK ‘GARLIC HYDERABADI PICKLE MIXED HYDERABADI PICKLE

![item 9768](classification-review-assets/item-9768.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 6. FENUGREC AKHAVAN FENUGREEK

![item 9781](classification-review-assets/item-9781.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 99.00 $ · as printed: “99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 7. GRENOBLE NOIX:

![item 9784](classification-review-assets/item-9784.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 8. ft SIROP DE MENTHE = KAMBIZ}

![item 9780](classification-review-assets/item-9780.jpg)

- **Category:** Fruits & Vegetables > Herbs (FR: Fruits et légumes > Fines herbes)
- **How classified:** rule (`herbs-fresh`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 9. AUS DE NAVET FORT a DOGANAY HOT TURNIP JUICE

![item 9777](classification-review-assets/item-9777.jpg)

- **Category:** Drinks > Juice (FR: Boissons > Jus)
- **How classified:** rule (`juice`)
- **Price:** 99.00 $ · as printed: “99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 10. MELANGE || CONFITURE DE CARROT| MEHRAN 181| BADI PICKLE M }f x à CARROT JAM QAN = CP, 260 a

![item 9771](classification-review-assets/item-9771.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

## Aliments Merci (`aliments-merci`)

### 1. Made Good Un choixdecarresvaries

![item 11141](https://alimentsmerci.com/wp-content/uploads/2026/09/Circulaire-SEPTEMBRE26VV.pdf#page=3)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-09-04 → 2026-09-30 · flyer page 3
- **Details:** OCR/extraction confidence: 0.97

### 2. ALIMENTSMERCI Tranchesd'ananassechees

![item 11151](https://alimentsmerci.com/wp-content/uploads/2026/09/Circulaire-SEPTEMBRE26VV.pdf#page=4)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.89 $ · as printed: “1.89”
- **Flyer validity:** 2026-09-04 → 2026-09-30 · flyer page 4
- **Details:** OCR/extraction confidence: 0.93

### 3. AUXVIVRES WrapDragon/WrapTempehBBQ WrapVege-Pate

![item 11138](https://alimentsmerci.com/wp-content/uploads/2026/09/Circulaire-SEPTEMBRE26VV.pdf#page=2)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 15.00 $ · as printed: “15”
- **Flyer validity:** 2026-09-04 → 2026-09-30 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 4. POMMECROQUANTE FAIT DE VRAIS FRUITS

![item 11137](https://alimentsmerci.com/wp-content/uploads/2026/09/Circulaire-SEPTEMBRE26VV.pdf#page=2)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.00 $ · as printed: “2.00”
- **Flyer validity:** 2026-09-04 → 2026-09-30 · flyer page 2
- **Details:** OCR/extraction confidence: 0.82

### 5. QuePasa-Croustilles de mais biologique (variees)

![item 11143](https://alimentsmerci.com/wp-content/uploads/2026/09/Circulaire-SEPTEMBRE26VV.pdf#page=3)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 5.59 $ · as printed: “5.59”
- **Flyer validity:** 2026-09-04 → 2026-09-30 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 6. gateau d'anniversaire BARRESx24g Made Good

![item 11145](https://alimentsmerci.com/wp-content/uploads/2026/09/Circulaire-SEPTEMBRE26VV.pdf#page=3)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-09-04 → 2026-09-30 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 7. reg.3,99$ ch./each MERENATURE Lait de CocoLEGERBio

![item 11147](https://alimentsmerci.com/wp-content/uploads/2026/09/Circulaire-SEPTEMBRE26VV.pdf#page=4)

- **Category:** Dairy & Eggs > Milk & Cream (FR: Produits laitiers et œufs > Lait et crème)
- **How classified:** rule (`milk-cream`)
- **Price:** 99.00 $ · as printed: “99”
- **Flyer validity:** 2026-09-04 → 2026-09-30 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 8. FOUSDEIILE Kombucha Biologique/Mangue/Vivace

![item 11148](https://alimentsmerci.com/wp-content/uploads/2026/09/Circulaire-SEPTEMBRE26VV.pdf#page=4)

- **Category:** Drinks > Non-alcoholic drinks (FR: Boissons > Boissons non alcoolisées)
- **How classified:** rule (`non-alcoholic`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-09-04 → 2026-09-30 · flyer page 4
- **Details:** OCR/extraction confidence: 0.98 · other printed prices: 3.99

### 9. MERENATURE Haricot pinto bio

![item 11146](https://alimentsmerci.com/wp-content/uploads/2026/09/Circulaire-SEPTEMBRE26VV.pdf#page=4)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-09-04 → 2026-09-30 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 10. MERENATURE Haricot rouge bio

![item 11150](https://alimentsmerci.com/wp-content/uploads/2026/09/Circulaire-SEPTEMBRE26VV.pdf#page=4)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 49.00 $ · as printed: “49”
- **Flyer validity:** 2026-09-04 → 2026-09-30 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

## Avril Supermarché Santé (`avril`)

### 1. RiceWorks croustilles de riz sans gluten

![item 2618](http://f.wishabi.net/page_items/435976740/1790751807/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Chips & Snacks (FR: Grignotines, croustilles et friandises > Croustilles et grignotines)
- **How classified:** rule (`chips-snacks`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: RICE WORKS · OCR/extraction confidence: 1.00

### 2. D-mannose et canneberge

![item 2541](http://f.wishabi.net/page_items/435976769/1790751808/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 49.99 $ · as printed: “49.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: NEW ROOTS HERBAL · OCR/extraction confidence: 1.00

### 3. Pro du bio et du probio

![item 2613](http://f.wishabi.net/page_items/436037110/1790751817/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 4. chou-fleur bio

![item 2575](http://f.wishabi.net/page_items/436616196/1791315759/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 5. Biobon végépâtés bios réfrigérés

![item 2599](http://f.wishabi.net/page_items/435976703/1790751806/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 9.99 $ · as printed: “9.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: BIOBON · OCR/extraction confidence: 1.00

### 6. farine tout usage sans gluten bio

![item 2621](http://f.wishabi.net/page_items/436616901/1791311027/extra_large.jpg)

- **Category:** Pantry > Baking Essentials (FR: Produits du garde-manger > Essentiels de cuisson)
- **How classified:** rule (`baking`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: CUISINE L'ANGÉLIQUE · OCR/extraction confidence: 1.00

### 7. Produits de noix de cajou fermentée bios réfrigérés

![item 2519](http://f.wishabi.net/page_items/436939610/1791558777/extra_large.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-11
- **Details:** brand: Nuts for Cheese · OCR/extraction confidence: 1.00

### 8. pâtes bios

![item 2582](http://f.wishabi.net/page_items/436616902/1791311027/extra_large.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: FELICETTI · OCR/extraction confidence: 1.00

### 9. beurre d'amandes crémeux bio

![item 2535](http://f.wishabi.net/page_items/436624660/1791309739/extra_large.jpg)

- **Category:** Pantry > Honey, Syrups & Spreads (FR: Produits du garde-manger > Miel, sirops et tartinades)
- **How classified:** rule (`specific-nut-butters`)
- **Price:** 17.99 $ · as printed: “17.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: AVRIL SÉLECTIONNÉ · OCR/extraction confidence: 1.00

### 10. avril cultivé

![item 2596](http://f.wishabi.net/page_items/436035081/1790751814/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: avril · OCR/extraction confidence: 1.00

## Brunet (`brunet`)

### 1. HALLS Pastilles sélectionnées

![item 8515](http://f.wishabi.net/page_items/436305918/1790938328/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 3.50 $ · as printed: “3.5”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Halls · OCR/extraction confidence: 1.00

### 2. JAMIESON Produits naturels sélectionnés

![item 8306](http://f.wishabi.net/page_items/436306030/1790938338/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Jamieson · OCR/extraction confidence: 1.00

### 3. MOI

![item 8597](http://f.wishabi.net/page_items/436537869/1791230730/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 4. ELASTOPLAST Pansements sélectionnés

![item 8481](http://f.wishabi.net/page_items/436305907/1790938344/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 5.19 $ · as printed: “5.19”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Elastoplast · OCR/extraction confidence: 1.00

### 5. EOS Produits sélectionnés

![item 8514](http://f.wishabi.net/page_items/436305969/1790938339/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: EOS · OCR/extraction confidence: 1.00

### 6. COLGATE Produits dentaires sélectionnés

![item 8638](http://f.wishabi.net/page_items/435452498/1790327192/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 9.49 $ · as printed: “9.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Colgate · OCR/extraction confidence: 1.00

### 7. AVÈNE Produits sélectionnés

![item 8418](http://f.wishabi.net/page_items/436306024/1790938334/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Avène · OCR/extraction confidence: 1.00

### 8. DUPUIS Gamme complete

![item 8262](http://f.wishabi.net/page_items/436253973/1790878595/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 26.99 $ · as printed: “26.99”
- **Flyer validity:** 2026-10-01 → 2026-10-14
- **Details:** brand: Dupuis · OCR/extraction confidence: 1.00

### 9. WATIER Perfection Sérum teinté révélateur d'éclat

![item 8284](http://f.wishabi.net/page_items/436253950/1790878595/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 62.00 $ · as printed: “62.0”
- **Flyer validity:** 2026-10-01 → 2026-10-14
- **Details:** brand: WATIER · OCR/extraction confidence: 1.00

### 10. CLAIROL Gamme complète

![item 8239](http://f.wishabi.net/page_items/436253971/1790878593/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 9.99 $ · as printed: “9.99”
- **Flyer validity:** 2026-10-01 → 2026-10-14
- **Details:** brand: Clairol · OCR/extraction confidence: 1.00

## Bulk Barn (`bulk-barn`)

### 1. Bonbons Skittles Originaux Skittles

![item 11101](classification-review-assets/item-11101.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 2.41 $ · as printed: “2.41”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 2. Gros flocons d'avoine Rolled Oats Large Fiake

![item 11100](classification-review-assets/item-11100.jpg)

- **Category:** Pantry > Cereal & Breakfast (FR: Produits du garde-manger > Céréales et petits-déjeuners)
- **How classified:** rule (`cereal-breakfast`)
- **Price:** 0.29 $ · as printed: “0.29”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 3. Cajous entiers Rotis asec etnon sales Whole Cashews

![item 11102](classification-review-assets/item-11102.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 2.32 $ · as printed: “2.32”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 4. Arachides au barbecue et aromedefumee Smokehouse BBQ Peanuts

![item 11097](classification-review-assets/item-11097.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 5. Raisins secs Thompson Thompson Raisins

![item 11099](classification-review-assets/item-11099.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 1.00 $ · as printed: “1.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 6. Jujubes super tendres Dare Super Soft Ju Jubes

![item 11098](classification-review-assets/item-11098.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 0.50 $ · as printed: “0.50”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

## Canadian Tire (`canadian-tire`)

### 1. Cric hybride à profil bas, 3 tonnes

![item 3132](http://f.wishabi.net/page_items/436182292/1790921842/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 239.99 $ · as printed: “239.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: MotoMaster · OCR/extraction confidence: 1.00

### 2. Certaines balles de golf

![item 2682](http://f.wishabi.net/page_items/436307035/1790921850/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 29.99 $ · as printed: “29.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 3. Gagnez de l'Argent CTMD*. Obtenez des offres de prime. Inscrivez-vous pour échanger.

![item 2741](http://f.wishabi.net/page_items/436306821/1790921809/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 4. Produits de nettoyage et d'esthétique automobile. Certaines types.

![item 2694](http://f.wishabi.net/page_items/436182497/1790921824/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 9.34 $ · as printed: “9.34”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 5. Meuble de rangement, 2 cubes. Blanc.

![item 2819](http://f.wishabi.net/page_items/436177497/1790921788/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 49.99 $ · as printed: “49.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: CANVAS · OCR/extraction confidence: 1.00

### 6. Machine à espresso Stilosa

![item 3170](http://f.wishabi.net/page_items/436305531/1790921807/extra_large.jpg)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** 129.99 $ · as printed: “129.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 7. RABAIS 10$

![item 2662](http://f.wishabi.net/page_items/436174829/1790883109/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Castrol · OCR/extraction confidence: 1.00

### 8. Ultimate Lithium 4 AAA or Max 6 9V Alkaline Batteries

![item 3075](http://f.wishabi.net/page_items/436180165/1790921822/extra_large.jpg)

- **Category:** Household > Home Goods (FR: Maison > Articles pour la maison)
- **How classified:** rule (`household-goods`)
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 9. Certaines housses de moto et cale de roue

![item 3195](http://f.wishabi.net/page_items/436307198/1790921851/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 56.69 $ · as printed: “56.69”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 10. Ens. de clés

![item 2832](http://f.wishabi.net/page_items/436180035/1790921823/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 21.99 $ · as printed: “21.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Mastercraft · OCR/extraction confidence: 1.00

## Coop Alentour (`coop-alentour`)

### 1. TEINTURE DRASTIX BIO

![item 10858](classification-review-assets/item-10858.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 21.25 $ · as printed: “21.25”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.89

### 2. PAIN MULTIGRAINS SEIGLE, KAMUT RAISINS OU MAIS AVEC MILLET BIO

![item 10843](classification-review-assets/item-10843.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 5.49 $ · as printed: “5.49”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.95

### 3. MILLEPERTUIS 400 MG

![item 10857](classification-review-assets/item-10857.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 16.49 $ · as printed: “16.49”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.91

### 4. CÉLERI EN FEUILLE BIO > NT RTS 2

![item 10860](classification-review-assets/item-10860.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.49 $ · as printed: “2.49”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.89

### 5. POUMONS, BRONCHES ET SINUS SAINS

![item 10848](classification-review-assets/item-10848.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 23.89 $ · as printed: “23.89”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.91

### 6. ÉCHALOTE FRANÇAISE BIO

![item 10851](classification-review-assets/item-10851.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.25 $ · as printed: “2.25”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.92

### 7. LEVURE NUTRITIONNELLE EN FLOCONS

![item 10850](classification-review-assets/item-10850.jpg)

- **Category:** Pantry > Baking Essentials (FR: Produits du garde-manger > Essentiels de cuisson)
- **How classified:** rule (`baking`)
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.93

### 8. KOMBUCHA SAVEURS ASSORTIES

![item 10849](classification-review-assets/item-10849.jpg)

- **Category:** Drinks > Non-alcoholic drinks (FR: Boissons > Boissons non alcoolisées)
- **How classified:** rule (`non-alcoholic`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.94

### 9. COLLATION SAVEURS ASSORTIES

![item 10845](classification-review-assets/item-10845.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 5.49 $ · as printed: “5.49”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.91

### 10. FLUX-O-BILE

![item 10854](classification-review-assets/item-10854.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 24.59 $ · as printed: “24.59”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.93

## Costco Wholesale (`costco`)

### 1. Ensembledemitainesdecuisine Grille-paina4 tranches Cuisinart

![item 9808](classification-review-assets/item-9808.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 19.99 $ · as printed: “19,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 2
- **Details:** OCR/extraction confidence: 0.85

### 2. Cricarebords surbaisses d'une capacitede

![item 9803](classification-review-assets/item-9803.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 139.99 $ · as printed: “139,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 2
- **Details:** OCR/extraction confidence: 0.85

### 3. Sauce pourpoulet aubeurreKFI Ndarticle1359722

![item 9830](classification-review-assets/item-9830.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 7.99 $ · as printed: “7,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 4
- **Details:** OCR/extraction confidence: 0.70

### 4. Chandailenmolletona fermeturea glissierepleine longueur SierraDesign talles P a TTG

![item 9795](classification-review-assets/item-9795.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 19.99 $ · as printed: “19,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 1
- **Details:** OCR/extraction confidence: 0.85

### 5. RechargesEasyRolldeDiaperGenie

![item 9872](classification-review-assets/item-9872.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 21.99 $ · as printed: “21,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 8
- **Details:** OCR/extraction confidence: 0.85

### 6. NettoyantpourcuvetteAdvanced deLysol

![item 9840](classification-review-assets/item-9840.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 10.99 $ · as printed: “10,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 5
- **Details:** OCR/extraction confidence: 0.85

### 7. All-in-One Shake Boisson tout-en-un Boisson tout-en-unFudge au chocolat de

![item 9856](classification-review-assets/item-9856.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 63.99 $ · as printed: “63,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 7
- **Details:** OCR/extraction confidence: 0.85

### 8. Assortiment demini-barresDairyMilkde

![item 9836](classification-review-assets/item-9836.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 15.99 $ · as printed: “15,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 5
- **Details:** OCR/extraction confidence: 0.85

### 9. COOKIE BUTTER MOUSSE MOUSSEAUSPECULOOS 6x76g2.58o=NET454g11

![item 9821](classification-review-assets/item-9821.jpg)

- **Category:** Dairy & Eggs > Butter & Spreads (FR: Produits laitiers et œufs > Beurre et tartinades)
- **How classified:** rule (`butter`)
- **Price:** 11.99 $ · as printed: “11,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 3
- **Details:** OCR/extraction confidence: 0.85

### 10. SELEFCAIONNGZ 400SHEETSIFEULES Feuilles assouplissantesBounce

![item 9843](classification-review-assets/item-9843.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 12.99 $ · as printed: “12,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 5
- **Details:** OCR/extraction confidence: 0.85

## Euro Marché (`euro-marche`)

### 1. DÉTERGENT À LESSIVE OLD DUTCH y LAUNDRY f DETERGENT 4

![item 9915](classification-review-assets/item-9915.jpg)

- **Category:** Household > Cleaning & Laundry (FR: Maison > Entretien et lessive)
- **How classified:** rule (`household-cleaning`)
- **Price:** 2.00 $ · as printed: “2/4.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 2. BTE "= — MIEL DE FLEURS DE LA GRÈCE «a ILIOS BLOSSOM

![item 9920](classification-review-assets/item-9920.jpg)

- **Category:** Pantry > Honey, Syrups & Spreads (FR: Produits du garde-manger > Miel, sirops et tartinades)
- **How classified:** rule (`honey-spreads`)
- **Price:** 4.29 $ · as printed: “4.29”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.98

### 3. CH/EA

![item 9905](classification-review-assets/item-9905.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 4. SAC / BAG

![item 9933](classification-review-assets/item-9933.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 5. CAFÉ ESPRESSO,

![item 9922](classification-review-assets/item-9922.jpg)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** 2.50 $ · as printed: “2/5.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 6. YOGOURT ACTIVIA 650 GR OU DANINO GO

![item 9876](classification-review-assets/item-9876.jpg)

- **Category:** Dairy & Eggs > Yogurt (FR: Produits laitiers et œufs > Yogourt)
- **How classified:** rule (`yogurt`)
- **Price:** 3.33 $ · as printed: “3/9.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.98

### 7. JUS 100% PUR RÉFRIGÉRÉ VOIR VARIÉTÉS EN MAGASIN DEL MONTE

![item 9894](classification-review-assets/item-9894.jpg)

- **Category:** Drinks > Juice (FR: Boissons > Jus)
- **How classified:** rule (`juice`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.95

### 8. CH/EA

![item 9889](classification-review-assets/item-9889.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.86

### 9. FROMAGE RICOTTA ITALIANA SAPUTO ITALIAN

![item 9878](classification-review-assets/item-9878.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 15.99 $ · as printed: “15.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.95

### 10. CAROTTES DU/FROM QUEBEC CARROTS

![item 9931](classification-review-assets/item-9931.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.50 $ · as printed: “2/5.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

## Familiprix (`familiprix`)

### 1. NICORETTE Gomme de nicotine

![item 3954](http://f.wishabi.net/page_items/435804248/1790661159/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 12.99 $ · as printed: “12.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Nicorette · OCR/extraction confidence: 1.00

### 2. Biomedic comprimé soulagement pour les jambes 30un

![item 3666](http://f.wishabi.net/page_items/435804925/1790661166/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 14.99 $ · as printed: “14.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Biomedic · OCR/extraction confidence: 1.00

### 3. HUGGIES Lingettes pour bébé

![item 3495](http://f.wishabi.net/page_items/435804049/1790661139/extra_large.jpg)

- **Category:** Baby > Baby Care (FR: Bébé > Soins pour bébé)
- **How classified:** rule (`baby-care`)
- **Price:** 21.49 $ · as printed: “21.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Huggies · OCR/extraction confidence: 1.00

### 4. BYLY Antisudorifiques ou déodorants

![item 3608](http://f.wishabi.net/page_items/435804995/1790661161/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: BYLY · OCR/extraction confidence: 1.00

### 5. GRAVOL ou GASTROVOL

![item 3843](http://f.wishabi.net/page_items/435804444/1790661147/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 6. Maybelline New York Fit Me camouflant #10 Clair 6.8ml

![item 4000](http://f.wishabi.net/page_items/435859845/1790661174/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 10.99 $ · as printed: “10.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: MAYBELLINE NEW YORK · OCR/extraction confidence: 1.00

### 7. CASCADES

![item 4071](http://f.wishabi.net/page_items/435870806/1790661148/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 5.88 $ · as printed: “5.88”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Cascades · OCR/extraction confidence: 1.00

### 8. Canesten comprimé confort + crème externe 3 jours

![item 3811](http://f.wishabi.net/page_items/435804131/1790661143/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 17.49 $ · as printed: “17.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: CANESTEN · OCR/extraction confidence: 1.00

### 9. PUPPA

![item 3879](http://f.wishabi.net/page_items/435859848/1790661176/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Pupa Milano · OCR/extraction confidence: 1.00

### 10. VITOLI Produits sélectionnés

![item 3761](http://f.wishabi.net/page_items/435804908/1790661158/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Vitoli · OCR/extraction confidence: 1.00

## Fruiterie Valmont (`fruiterie-valmont`)

### 1. Choux-fleursblancs,mauves ouoranges Quebec

![item 11071](classification-review-assets/item-11071.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 2. chopine Tomatesmedley Mexique

![item 11069](classification-review-assets/item-11069.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.50 $ · as printed: “2/5.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.82

### 3. Sepato ICONOMISEZ PLUSDE

![item 11090](classification-review-assets/item-11090.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.00 $ · as printed: “2/12.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.95

### 4. CafesGustavo Auchoix-600g

![item 11065](classification-review-assets/item-11065.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 0.14 $ · as printed: “0.14”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 5. Cannebergesfraiches Quebec

![item 11080](classification-review-assets/item-11080.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.50 $ · as printed: “2/5.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.80

### 6. Pates,feuilletesouquiches Plaisirs Gastronomiquesou jambonGoldLabel

![item 11054](classification-review-assets/item-11054.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 7. Citrouillesoranges Quebec

![item 11081](classification-review-assets/item-11081.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.66 $ · as printed: “3.66”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 8. ConfituresVergerDuVillage Auchoix-200ml Jusqu'aepuisement desstocks

![item 11061](classification-review-assets/item-11061.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 21.99 $ · as printed: “21.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 9. Bleuets Perou

![item 11079](classification-review-assets/item-11079.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 10. Fromageschampignons ettruffe, classique,leger,original ou aux pommes Oka,St-Paulinregulierou

![item 11084](classification-review-assets/item-11084.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 7.00 $ · as printed: “2/14.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.94

## Fruits & Légumes 3 Saisons (`3-saisons-fruits-legumes`)

### 1. PRODUIT IMPORTE

![item 11109](classification-review-assets/item-11109.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.75

### 2. SANS LACTOSE SANG OLUTEN

![item 11105](classification-review-assets/item-11105.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.89

### 3. COURGES D'AUTOMNE DES CO EE

![item 11108](classification-review-assets/item-11108.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 0.79 $ · as printed: “0.79”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.74

### 4. PAQUET DE.5

![item 11107](classification-review-assets/item-11107.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.96

### 5. BOCCONCINI

![item 11106](classification-review-assets/item-11106.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.92

## Giant Tiger (`giant-tiger`)

### 1. Oignons jaunes

![item 4217](http://f.wishabi.net/page_items/436671013/1791318429/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 0.88 $ · as printed: “0.88”
- **Flyer validity:** 2026-10-07 → 2026-10-13
- **Details:** OCR/extraction confidence: 1.00

### 2. Poulet entier frais

![item 4200](http://f.wishabi.net/page_items/436671004/1791318425/extra_large.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 9.97 $ · as printed: “9.97”
- **Flyer validity:** 2026-10-07 → 2026-10-13
- **Details:** OCR/extraction confidence: 1.00

### 3. Bacon Smoke House Gold Label

![item 4214](http://f.wishabi.net/page_items/436670992/1791318419/extra_large.jpg)

- **Category:** Meat > Bacon (FR: Viande > Bacon)
- **How classified:** rule (`bacon`)
- **Price:** 3.47 $ · as printed: “3.47”
- **Flyer validity:** 2026-10-07 → 2026-10-13
- **Details:** brand: Smoke House · OCR/extraction confidence: 1.00

### 4. Ananas

![item 4216](http://f.wishabi.net/page_items/436671003/1791318424/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 1.88 $ · as printed: “1.88”
- **Flyer validity:** 2026-10-07 → 2026-10-13
- **Details:** OCR/extraction confidence: 1.00

### 5. Fromage Boursin

![item 4209](http://f.wishabi.net/page_items/436264069/1791299939/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 4.97 $ · as printed: “4.97”
- **Flyer validity:** 2026-10-07 → 2026-10-13
- **Details:** brand: Boursin · OCR/extraction confidence: 1.00

### 6. Céréales Cheerios General Mills

![item 4190](http://f.wishabi.net/page_items/436264072/1791299941/extra_large.jpg)

- **Category:** Pantry > Cereal & Breakfast (FR: Produits du garde-manger > Céréales et petits-déjeuners)
- **How classified:** rule (`cereal-breakfast`)
- **Price:** 3.47 $ · as printed: “3.47”
- **Flyer validity:** 2026-10-07 → 2026-10-13
- **Details:** brand: General Mills · OCR/extraction confidence: 1.00

### 7. LES BAS PRIX

![item 4212](http://f.wishabi.net/page_items/436671009/1791318428/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-07 → 2026-10-13
- **Details:** OCR/extraction confidence: 1.00

### 8. Pommes Mcintosh ou Cortland en sac, 3 lb

![item 4191](http://f.wishabi.net/page_items/436264074/1791299942/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 3.97 $ · as printed: “3.97”
- **Flyer validity:** 2026-10-07 → 2026-10-13
- **Details:** OCR/extraction confidence: 1.00

### 9. Garniture fouettée Cool Whip Kraft

![item 4207](http://f.wishabi.net/page_items/436264064/1791299935/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.97 $ · as printed: “3.97”
- **Flyer validity:** 2026-10-07 → 2026-10-13
- **Details:** brand: Kraft · OCR/extraction confidence: 1.00

### 10. Oignons verts

![item 4210](http://f.wishabi.net/page_items/436506950/1791299944/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.44 $ · as printed: “1.44”
- **Flyer validity:** 2026-10-07 → 2026-10-13
- **Details:** OCR/extraction confidence: 1.00

## H Marché (`h-marche`)

### 1. SALTED HAIRTAIL FISH SABRE SALE

![item 11154](classification-review-assets/item-11154.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 10.99 $ · as printed: “10.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.95

### 2. SALTED SEA TROUT MAIGRE SALE

![item 11156](classification-review-assets/item-11156.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.98

### 3. SAVE

![item 11163](classification-review-assets/item-11163.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 0.00 $ · as printed: “0”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.58

### 4. SP) NOUILLES DE PATATE DOUCE MOELLEUSES (DANGMYEON) SP) CHEWY GLASS NOODLES (DANGMYEON)

![item 11162](classification-review-assets/item-11162.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

### 5. DW) RIZ COLLANT SSEN COOK DW) SSEN COOK STICKY RICE

![item 11168](classification-review-assets/item-11168.jpg)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 21.99 $ · as printed: “21.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 7
- **Details:** OCR/extraction confidence: 0.99

### 6. KOREAN =" PANCAKE

![item 11158](classification-review-assets/item-11158.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.10 $ · as printed: “2.10”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 7. MMS) CRAQUELINS DE RIZ AU BLE ENTIER MMS) WHOLE WHEAT RICE CRACKERS

![item 11159](classification-review-assets/item-11159.jpg)

- **Category:** Snacks, Chips & Candy > Crackers & Cookies (FR: Grignotines, croustilles et friandises > Craquelins et biscuits)
- **How classified:** rule (`crackers-cookies`)
- **Price:** 23.29 $ · as printed: “23.29”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 8. NP) GORAESA BROCHETTES DE GALETTES DE POISSON NP) GORAESA FISH CAKE SKEWERS

![item 11167](classification-review-assets/item-11167.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 6.49 $ · as printed: “6.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 7
- **Details:** OCR/extraction confidence: 0.99

### 9. BONELESS SALTED MACKEREL MAQUEREAU SALE SANS ARETES

![item 11155](classification-review-assets/item-11155.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.98

### 10. HT) BOISSON AU RAISIN BONGBONG HT) GRAPE BONGBONG

![item 11169](classification-review-assets/item-11169.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 7
- **Details:** OCR/extraction confidence: 0.90

## IGA (`iga`)

### 1. NOURRITURE POUR CHATS WHISKAS

![item 402](https://f.wishabi.net/page_pdf_images/24244979/41a1bef0-be1b-11f1-84e0-beb1c385ff76/x_large)

- **Category:** Pet > Pet Food (FR: Animaux > Nourriture pour animaux)
- **How classified:** rule (`pet`)
- **Price:** 16.99 $ · as printed: “16.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Whiskas · SKU: 00000_000000005849643125 · OCR/extraction confidence: 1.00 · “12 x 75 g Rég. 17,99$ à 18,99$”

### 2. BOISSON SPORTIVE GATORADE

![item 649](https://f.wishabi.net/page_pdf_images/24244979/24e55d80-be1b-11f1-84e0-beb1c385ff76/x_large)

- **Category:** Drinks > Sports & Energy (FR: Boissons > Boissons énergisantes et pour sportifs)
- **How classified:** rule (`sports-energy`)
- **Price:** 4.00 $ · as printed: “4.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Gatorade · SKU: 00000_000000005557742100 · OCR/extraction confidence: 1.00 · “710 mL Bouteille consignée”

### 3. OIGNONS JAUNES BIOLOGIQUES

![item 477](https://f.wishabi.net/page_items/436514100/1791212691/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.97 $ · as printed: “2.97”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: C0003338360001 · OCR/extraction confidence: 1.00 · “Produit du Québec 907 g”

### 4. JAMBON FUMÉ OLYMEL

![item 670](https://f.wishabi.net/page_pdf_images/24244974/2a85bf32-be1b-11f1-8b28-8ad3174fa92b/x_large)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 3.19 $ · as printed: “3.19”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Olymel · SKU: 00000_000000028064000000 · OCR/extraction confidence: 1.00 · “Forêt-Noire, À l'ancienne Reg. 17,19$/lb 14,47 $/lb”

### 5. CROUSTADE AUX POMMES COMPLIMENTS

![item 761](https://f.wishabi.net/page_items/434446851/1790001197/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 10.99 $ · as printed: “10.99”
- **Flyer validity:** 2026-09-24 → 2026-10-14
- **Details:** brand: Compliments · SKU: 00000_000000005574257522 · OCR/extraction confidence: 1.00 · “680 g”

### 6. FRIANDISES HERSHEY'S, REESE'S

![item 629](https://f.wishabi.net/page_pdf_images/24244977/3443bfa6-be1b-11f1-9f85-362af39aa6ef/x_large)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 8.49 $ · as printed: “8.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Reese's · SKU: 00000_000000005660076975 · OCR/extraction confidence: 1.00 · “(25) Rég. 9,99$ à 11,99$”

### 7. CANNEBERGES FRAÎCHES

![item 387](https://f.wishabi.net/page_items/436319155/1790932035/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 5.00 $ · as printed: “5.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 00000_000000087655800013 · OCR/extraction confidence: 1.00 · “Produit du Québec Canada no 1 (340 g)”

### 8. HORS-D'OEUVRE SURGELÉS COMPLIMENTS

![item 615](https://f.wishabi.net/page_pdf_images/24244975/26b2e678-be1b-11f1-a82d-c24c0e6864af/x_large)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Compliments · SKU: 00000_000000005574258262 · OCR/extraction confidence: 1.00 · “252 à/to 500 g Rég. 6,49$ à 12,99$”

### 9. NOURRITURE POUR CHATS SHEBA

![item 457](https://f.wishabi.net/page_pdf_images/24244979/42b2f480-be1b-11f1-84e0-beb1c385ff76/x_large)

- **Category:** Pet > Pet Food (FR: Animaux > Nourriture pour animaux)
- **How classified:** rule (`pet`)
- **Price:** 16.99 $ · as printed: “16.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Sheba · SKU: 00000_000000005849645772 · OCR/extraction confidence: 1.00 · “12 x 75 g Rég. 17,99$ à 18,99$”

### 10. CAFÉ EN GRAINS OU MOULU LAVAZZA

![item 701](https://f.wishabi.net/page_pdf_images/24244969/26803160-be1b-11f1-b4c4-72daea333c71/x_large)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** 13.99 $ · as printed: “13.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: LavAzza · SKU: 00000_000000004195300481 · OCR/extraction confidence: 1.00 · “340 g Rég. 18,99$ à 19,99$”

## IGA Express / Mini (`iga-express`)

### 1. MÉLANGE À CHOCOLAT CHAUD COMPLIMENTS

![item 1723](https://f.wishabi.net/page_pdf_images/24244968/1b5bdc76-be1b-11f1-80e6-ca9effa18111/x_large)

- **Category:** Drinks > Tea & Hot Drinks (FR: Boissons > Thés et boissons chaudes)
- **How classified:** rule (`tea-hot-drinks`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Compliments · SKU: 00000_000000005574251029 · OCR/extraction confidence: 1.00 · “500 g Rég. 6,99$ à 7,49$”

### 2. Pommes + cheddar

![item 2012](https://f.wishabi.net/page_items/434446830/1790001202/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** —
- **Flyer validity:** 2026-09-24 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00 · “Le mariage du fromage fondant et de la pomme croquante est un grand classique.”

### 3. SALAMI TOUT BOEUF TRANCHÉ LESTERS

![item 1765](https://f.wishabi.net/page_pdf_images/24244974/21f0369a-be1b-11f1-8b28-8ad3174fa92b/x_large)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Lesters · OCR/extraction confidence: 1.00 · “150 g”

### 4. TREMPETTE LE GREC

![item 1873](https://f.wishabi.net/page_pdf_images/24244972/2ac3cbb0-be1b-11f1-8a67-9eb96c5310cd/x_large)

- **Category:** Deli > Antipasto, Dips & Spreads (FR: Charcuterie > Antipasti, trempettes et tartinades)
- **How classified:** rule (`dips-spreads-deli`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: LE GREC · SKU: 00000_000000081013500820 · OCR/extraction confidence: 1.00 · “(280 g) Sélection variée”

### 5. POMMES CORTLAND

![item 1983](https://f.wishabi.net/page_pdf_images/24244970/1dfbfd1c-be1b-11f1-889a-4aef5d10a223/x_large)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 00000_000000000000004104 · OCR/extraction confidence: 1.00 · “Produit du Québec Canada no 1 2,18 $/kg”

### 6. POMMES EMPIRE OU McINTOSH

![item 1729](https://f.wishabi.net/page_items/436319135/1790932030/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 00000_000000000000004124 · OCR/extraction confidence: 1.00 · “Produits du Québec Canada no 1”

### 7. MIEL NATUREL LE MIEL D'ÉMILIE

![item 1854](https://f.wishabi.net/page_pdf_images/24244977/2c2cde38-be1b-11f1-9f85-362af39aa6ef/x_large)

- **Category:** Pantry > Honey, Syrups & Spreads (FR: Produits du garde-manger > Miel, sirops et tartinades)
- **How classified:** rule (`honey-spreads`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Le Miel D'Émilie · SKU: 00000_000000006653619375 · OCR/extraction confidence: 1.00 · “375 g”

### 8. COURGES

![item 1990](https://f.wishabi.net/page_items/436877322/1791493252/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.47 $ · as printed: “1.47”
- **Flyer validity:** 2026-09-24 → 2026-10-14
- **Details:** SKU: 00000_000000000000003142 · OCR/extraction confidence: 1.00 · “Produits du Québec Sélection variée”

### 9. PAIN TRANCHÉ, PAINS À HOT-DOG OU À HAMBURGER R OU BAGELS BIOLOGIQUES INEWA

![item 1804](https://f.wishabi.net/page_pdf_images/24244977/3227666e-be1b-11f1-9f85-362af39aa6ef/x_large)

- **Category:** Meat > Hot Dogs (FR: Viande > Saucisses hot-dog)
- **How classified:** rule (`hot-dogs`)
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Inéwa · SKU: 00000_000000081174000061 · OCR/extraction confidence: 1.00 · “500 à 680 g Sélection variée”

### 10. RADIS 3 COULEURS OU RADIS ROUGES DE SERRE LE CIEL

![item 1589](https://f.wishabi.net/page_pdf_images/24244972/27d5c692-be1b-11f1-8a67-9eb96c5310cd/x_large)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Name (EN):** MINI- CONCOMBRES SANS PÉPINS
- **Price:** 5.00 $ · as printed: “5.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: LE CIEL · SKU: 00000_000000028418100000 · OCR/extraction confidence: 1.00 · “Produit du Québec (908 g)”

## IGA Extra (`iga-extra`)

### 1. POIS TENDRES LE SIEUR

![item 2155](https://f.wishabi.net/page_pdf_images/24244964/1a3daaea-be1b-11f1-b44d-16e5c68bac17/x_large)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: LESIEUR · SKU: 00000_000000019056901160 · OCR/extraction confidence: 1.00 · “(398 mL) Sélection variée Rég. 2,49$ à 2,69$”

### 2. SALADE C'EST PRÊT!

![item 2355](https://f.wishabi.net/page_pdf_images/24244975/1fc8fb5e-be1b-11f1-a82d-c24c0e6864af/x_large)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: C'EST PRÊT! · SKU: 00000_000000005881400950 · OCR/extraction confidence: 1.00 · “454 g Sélection variée”

### 3. COURGES

![item 2475](https://f.wishabi.net/page_pdf_images/24275231/48d29222-c356-11f1-b105-66e1eb9c06d4/x_large)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.47 $ · as printed: “1.47”
- **Flyer validity:** 2026-09-24 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00 · “Produits du Québec Sélection variée 2,88 $/kg”

### 4. MUFFINS COMPLIMENTS

![item 2483](https://f.wishabi.net/page_items/434446852/1790001198/extra_large.jpg)

- **Category:** Bakery > Cookies, Muffins & Desserts (FR: Boulangerie > Biscuits, muffins et desserts)
- **How classified:** rule (`bakery-cookies-muffins`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-09-24 → 2026-10-14
- **Details:** brand: Compliments · SKU: 00000_000000006882013607 · OCR/extraction confidence: 1.00 · “400 g”

### 5. BREUVAGE LAITIER OU BREUVAGE LAITIER AU CHOCOLAT NATREL

![item 2220](https://f.wishabi.net/page_pdf_images/24244977/2f44f9c0-be1b-11f1-9f85-362af39aa6ef/x_large)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Natrel · SKU: 00000_000000006442025501 · loyalty-gated price · OCR/extraction confidence: 1.00 · “0%, 1%, 2%, 3,25% M.G.”

### 6. KETCHUP AUX TOMATES COMPLIMENTS

![item 2446](https://f.wishabi.net/page_pdf_images/24244978/255f5720-be1b-11f1-ad44-fee36c7f22ec/x_large)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 4.49 $ · as printed: “4.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Compliments · SKU: 00000_000000005574254574 · OCR/extraction confidence: 1.00 · “1 L”

### 7. SAUCE AU PIMENT McILHENNY CO. TABASCO

![item 2202](https://f.wishabi.net/page_items/436319104/1790932025/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: McILHENNY CO. TABASCO · SKU: 00000_000000001121000003 · OCR/extraction confidence: 1.00 · “57 mL Reg. 3,99$ à 4,19$”

### 8. COUCHES PAMPERS

![item 2457](https://f.wishabi.net/page_pdf_images/24244979/38db4d18-be1b-11f1-84e0-beb1c385ff76/x_large)

- **Category:** Baby > Baby Care (FR: Bébé > Soins pour bébé)
- **How classified:** rule (`baby-care`)
- **Price:** 28.99 $ · as printed: “28.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Pampers · SKU: 00000_000000003700074969 · OCR/extraction confidence: 1.00 · “48 à 116 Sélection variée Rég. 34,99$ à 38,99$”

### 9. BROSSE À DENTS COLGATE (1) OU DENTIFRICE COLGATE (70 à 150 mL)

![item 2373](https://f.wishabi.net/page_pdf_images/24244979/240e21d0-be1b-11f1-84e0-beb1c385ff76/x_large)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Colgate · SKU: 00000_000000005800014210 · OCR/extraction confidence: 1.00 · “Sélection variée Rég. 4,49$ à 6,29$”

### 10. CEURS D'ARTICHAUTS KIM PHAT

![item 2182](https://f.wishabi.net/page_pdf_images/24244965/1b850b96-be1b-11f1-a0cc-8ef849044dbe/x_large)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 4.49 $ · as printed: “4.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: KIM PHAT · SKU: 00000_000000062879000115 · OCR/extraction confidence: 1.00 · “356 mL Rég. 5,29$ à 5,49$”

## Jean Coutu (`jean-coutu`)

### 1. NIVEA Lotions pour le corps sélectionnées

![item 7760](http://f.wishabi.net/page_items/436741249/1791422976/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 8.49 $ · as printed: “8.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Nivea · OCR/extraction confidence: 1.00

### 2. LAURA SECORD Récolte Fruitée Bonbons, 200 g, DÉSIR NOIR Assortiment de chocolats 207 g

![item 8173](http://f.wishabi.net/page_items/436073241/1790818391/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 3. SYSTANE Produits de soins pour les yeux sélectionnés

![item 7586](http://f.wishabi.net/page_items/436743602/1791423684/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 4. Cross Signal Encounters

![item 7654](http://f.wishabi.net/page_items/436743752/1791423704/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 5. HERTEL Produits nettoyants sélectionnés

![item 7653](http://f.wishabi.net/page_items/436743738/1791423690/extra_large.jpg)

- **Category:** Household > Cleaning & Laundry (FR: Maison > Entretien et lessive)
- **How classified:** rule (`household-cleaning`)
- **Price:** 2.77 $ · as printed: “2.77”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Hertel · OCR/extraction confidence: 1.00

### 6. URIAGE

![item 8135](http://f.wishabi.net/page_items/436073141/1790818379/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: URIAGE · OCR/extraction confidence: 1.00

### 7. Selection Friandises sélectionnées

![item 7670](http://f.wishabi.net/page_items/436741471/1791422976/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 2.29 $ · as printed: “2.29”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Selection · OCR/extraction confidence: 1.00

### 8. BENEFIBER Produits sélectionnés

![item 7896](http://f.wishabi.net/page_items/436820075/1791424631/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-28
- **Details:** brand: Benefiber · OCR/extraction confidence: 1.00

### 9. MESSAGE IMPORTANT

![item 7563](http://f.wishabi.net/page_items/436333974/1790921602/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 10. JUICY COUTURE Fragrances et formats sélectionnés

![item 7680](http://f.wishabi.net/page_items/436741447/1791422992/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Juicy Couture · OCR/extraction confidence: 1.00

## Kim Phat (`kim-phat`)

### 1. POITRINE DE DINDE FUMÉE DALI EXPRESS

![item 4255](http://f.wishabi.net/page_items/436675083/1791333593/extra_large.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 2.79 $ · as printed: “2.79”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Deli Express · OCR/extraction confidence: 1.00

### 2. SAUCE GUACAMOLE ET SERRANO ZAASCHILA

![item 4353](http://f.wishabi.net/page_items/436675111/1791333597/extra_large.jpg)

- **Category:** Deli > Antipasto, Dips & Spreads (FR: Charcuterie > Antipasti, trempettes et tartinades)
- **How classified:** rule (`dips-spreads-deli`)
- **Price:** 2.69 $ · as printed: “2.69”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Zaaschila · OCR/extraction confidence: 1.00

### 3. FARINE POUR BANH CUON VINH THUAN

![item 4227](http://f.wishabi.net/page_items/436675113/1791333598/extra_large.jpg)

- **Category:** Pantry > Baking Essentials (FR: Produits du garde-manger > Essentiels de cuisson)
- **How classified:** rule (`baking`)
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Vinh Thuan · OCR/extraction confidence: 1.00

### 4. MASQUE POUR LES YEUX PUREDERM

![item 4329](http://f.wishabi.net/page_items/436675188/1791333606/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 5. GÂTEAU TIRAMISU ELITE SWEETS

![item 4296](http://f.wishabi.net/page_items/436675213/1791333604/extra_large.jpg)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Elite Sweets · OCR/extraction confidence: 1.00

### 6. FLANC DE BŒUF

![item 4309](http://f.wishabi.net/page_items/436675199/1791333594/extra_large.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 7.88 $ · as printed: “7.88”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 7. POMME GALA

![item 4245](http://f.wishabi.net/page_items/436675138/1791333604/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 1.28 $ · as printed: “1.28”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 8. EAU VITAMINÉE GLACEAU

![item 4232](http://f.wishabi.net/page_items/436675104/1791333592/extra_large.jpg)

- **Category:** Drinks > Water (FR: Boissons > Eau)
- **How classified:** rule (`water`)
- **Price:** 4.79 $ · as printed: “4.79”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: glaceau · OCR/extraction confidence: 1.00

### 9. FILET DE TILAPIA FRAIS

![item 4363](http://f.wishabi.net/page_items/436674850/1791333594/extra_large.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 10. RIZ FRIT BULDAK CONGELÉ SAMYANG

![item 4263](http://f.wishabi.net/page_items/436675092/1791333599/extra_large.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** frozen-remap (`rice`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Samyang · OCR/extraction confidence: 1.00

## L'Intermarché (`l-intermarche`)

### 1. TOMATES PC® — CERTAINES VARIETES,

![item 10749](classification-review-assets/item-10749.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 2. 2 AT +3 VIANDE

![item 10804](classification-review-assets/item-10804.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 7
- **Details:** OCR/extraction confidence: 0.93

### 3. ARACHIDES GRILLÉES À SEC PC“ CERTAINES VARIÉTÉS

![item 10786](classification-review-assets/item-10786.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 5.49 $ · as printed: “5.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.96

### 4. COCKTAIL AUX CANNEBERGES BOISSONS GAZEUSES COCA-COLA, OCEAN SPRAY OÙ DE TOMATESET CANADA DRY, PEPSI OU DR. PEPPER DE PALOURDES CLAMATO MOTT'S, CERTAINES VARIÉTÉS CERTAINES VARIÉTÉS, 1,89 L (CONSIGNE) 6 X 710 ML (CONSIGNE) JUICE OR COCKTAIL SOFT DRINKS

![item 10773](classification-review-assets/item-10773.jpg)

- **Category:** Beer & Wine > Cider & Coolers (FR: Bières et vins > Cidres et coolers)
- **How classified:** rule (`cider-coolers`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.92

### 5. YOGOURT PROBIOTIQUES ACTIVIA LAIT PROTÉINÉ SANS LACTOSE CERTAINES VARIÉTÉS NATREL PLUS

![item 10746](classification-review-assets/item-10746.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 6. FRUITS SURGELÉS SANS NOM® NATURELLEMENT IMPARFAITS"C CERTAINES VARIÉTÉS

![item 10775](classification-review-assets/item-10775.jpg)

- **Category:** Frozen Food > Frozen Fruit & Vegetables (FR: Produits surgelés > Fruits et légumes surgelés)
- **How classified:** frozen-remap (`fruits`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 7. PÂTES ALIMENTAIRES ITALPASTA

![item 10780](classification-review-assets/item-10780.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 6.68 $ · as printed: “6.68”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.58

### 8. BIÈRE DÉSALCOOLISÉE PC” CERTAINES VARIÉTÉS

![item 10729](classification-review-assets/item-10729.jpg)

- **Category:** Beer & Wine > Beer (FR: Bières et vins > Bières)
- **How classified:** rule (`beer`)
- **Price:** 8.29 $ · as printed: “8.29”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.96

### 9. LA HaL AML'AL A a LL LÀ À CERTAINES VARIÉTÉS

![item 10777](classification-review-assets/item-10777.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 5.79 $ · as printed: “5.79”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 10. BOEUF HACHÉ MAIGRE EMBALLAGE FAMILIAL

![item 10768](classification-review-assets/item-10768.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 66.00 $ · as printed: “66”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

## L'intermarché Palumbo (`intermarche-palumbo`)

### 1. TRIO VIANDE HACHÉE MINCEMEAT TRIO BOEUF, VEAU, PORC

![item 10996](classification-review-assets/item-10996.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 2. FROMAGE CREMA BEL PAESE

![item 11002](classification-review-assets/item-11002.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 2.50 $ · as printed: “2/5.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 6.99

### 3. POISCHICHES 8B HARICOTS BLANCS GIGI 580ML

![item 11000](classification-review-assets/item-11000.jpg)

- **Category:** Pantry > Dried Beans, Vegetables & Grains (FR: Produits du garde-manger > Haricots secs, légumes et grains)
- **How classified:** rule (`beans-grains`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 2.49

### 4. STEAK T-BONE

![item 11001](classification-review-assets/item-11001.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 5. EXTRA BRIE OU CAMEMBERT

![item 10998](classification-review-assets/item-10998.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 6. HUILE DE TOURNESOL SALMA OU CEDAR “a

![item 10999](classification-review-assets/item-10999.jpg)

- **Category:** Pantry > Oils & Vinegar (FR: Produits du garde-manger > Huile et vinaigre)
- **How classified:** rule (`oils-vinegar`)
- **Price:** 14.99 $ · as printed: “14.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 7. POIVRONS

![item 10997](classification-review-assets/item-10997.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

## La Moisson Supermarché Santé (`la-moisson`)

### 1. QUÉBEC CORIANDRE BIO

![item 10811](classification-review-assets/item-10811.jpg)

- **Category:** Fruits & Vegetables > Herbs (FR: Fruits et légumes > Fines herbes)
- **How classified:** rule (`herbs-fresh`)
- **Price:** 1.95 $ · as printed: “1.95”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.92

### 2. SOUPES GOURMANDES CLASSIQUES

![item 10824](classification-review-assets/item-10824.jpg)

- **Category:** Prepared Meals > Salads & Soups (FR: Repas préparés > Salades et soupes)
- **How classified:** rule (`salads-soups`)
- **Price:** 7.95 $ · as printed: “7.95”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.92

### 3. NEWZEALAND MANUKA HONEY LOZENGES PASTILLES AU MIEL DEMANUKA

![item 10821](classification-review-assets/item-10821.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 11.95 $ · as printed: “11.95”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.93

### 4. BURRITOS & REPAS PRÊTS À MANGER VÉGÉTARIENS & VÉGANES ME" Ne PROTÉINES 20 g

![item 10814](classification-review-assets/item-10814.jpg)

- **Category:** Prepared Meals > Entrees & Appetizers (FR: Repas préparés > Plats principaux et apéritifs)
- **How classified:** rule (`entrees`)
- **Price:** 4.65 $ · as printed: “4.65”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.97

### 5. RAVIOLIS SURGELÉS À BASE DE PLANTES

![item 10820](classification-review-assets/item-10820.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 12.15 $ · as printed: “12.15”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 6. MEXIQUE KIWI EN SAC 1LBS

![item 10809](classification-review-assets/item-10809.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 4.95 $ · as printed: “4.95”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.91

### 7. RIZ & GALETTES DE RIZ BRUN

![item 10839](classification-review-assets/item-10839.jpg)

- **Category:** Snacks, Chips & Candy > Crackers & Cookies (FR: Grignotines, croustilles et friandises > Craquelins et biscuits)
- **How classified:** rule (`crackers-cookies`)
- **Price:** 5.15 $ · as printed: “5.15”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 7
- **Details:** OCR/extraction confidence: 0.94

### 8. GRAINES BIO

![item 10842](classification-review-assets/item-10842.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 9.75 $ · as printed: “9.75”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 7
- **Details:** OCR/extraction confidence: 0.88

### 9. THON, SAUMON & SARDINES EN CONSERVE

![item 10837](classification-review-assets/item-10837.jpg)

- **Category:** Pantry > Canned & Pickled (FR: Produits du garde-manger > Produits en conserve et marinés)
- **How classified:** rule (`specific-canned`)
- **Price:** 5.35 $ · as printed: “5.35”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 7
- **Details:** OCR/extraction confidence: 0.92

### 10. MEXIQUE BANANE BIO

![item 10810](classification-review-assets/item-10810.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.95 $ · as printed: “2.95”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.95

## Le Marché Esposito (`marche-esposito`)

### 1. GA SALSA OLD DUTCH a

![item 10081](classification-review-assets/item-10081.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 4.25 $ · as printed: “2/8.50”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.98

### 2. CH./EA

![item 10103](classification-review-assets/item-10103.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 49.00 $ · as printed: “49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 3. POIVRONS ROUGESJAUNE OUTORANGE DUIQUEBEC IN 2 [RED yYELLOW/ORVORANGE| PEPPERS D FROMIQUEBEC \#

![item 10092](classification-review-assets/item-10092.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 4. COTELETTES/DELONGE PORC CENTRE (FORMAT FAMILIAL) PCENTERTCUT; PORK(LOIN|CHOPS|(FAMILY/PACK) L'ILATUC

![item 10074](classification-review-assets/item-10074.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 5.39 $ · as printed: “5.39”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.93

### 5. HUILE[D{OLIVEJEXTRATVIERGE | EXTRANVIRGIN OLIVE OIL

![item 10068](classification-review-assets/item-10068.jpg)

- **Category:** Pantry > Canned & Pickled (FR: Produits du garde-manger > Produits en conserve et marinés)
- **How classified:** rule (`canned-pickled`)
- **Price:** 2.71 $ · as printed: “2.71”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.91

### 6. N TRANCHES D POUR SANDWICH

![item 10099](classification-review-assets/item-10099.jpg)

- **Category:** Prepared Meals > Sandwiches (FR: Repas préparés > Sandwichs)
- **How classified:** rule (`sandwiches`)
- **Price:** 99.00 $ · as printed: “99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 7. POIVRONS{SHISHITO PRODUIT/IMPORTE BR SHISHITOJPERRERS = IMPBORTED)PRODUCT, ACH BAG

![item 10096](classification-review-assets/item-10096.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 99.00 $ · as printed: “99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 8. SALAMI) SOPRESSATA DOUX UMILD}SALAMI;SOPRESSATA

![item 10069](classification-review-assets/item-10069.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 15.87 $ · as printed: “15.87”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.82

### 9. FILET, DE PORC PORK(FILET

![item 10078](classification-review-assets/item-10078.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.95

### 10. SIQLIAN OLIVE OIL MAESTRI OLEARI = HUILE D“OLIVE|EXTRA VIERGE EXTRA VIRGINIOLIVE/OIL!

![item 10080](classification-review-assets/item-10080.jpg)

- **Category:** Pantry > Canned & Pickled (FR: Produits du garde-manger > Produits en conserve et marinés)
- **How classified:** rule (`canned-pickled`)
- **Price:** 6.66 $ · as printed: “6.66”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.69

## Le Monde au Naturel (`monde-au-naturel`)

### 1. SPÉCIAL

![item 10527](classification-review-assets/item-10527.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 15.00 $ · as printed: “15”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 2. SPECIAL

![item 10517](classification-review-assets/item-10517.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 20.00 $ · as printed: “20”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 3. SPECIAL

![item 10529](classification-review-assets/item-10529.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 15.00 $ · as printed: “15”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 4. SPÉCIAL

![item 10574](classification-review-assets/item-10574.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 15.00 $ · as printed: “15”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 9
- **Details:** OCR/extraction confidence: 0.99

### 5. SPÉCIAL

![item 10539](classification-review-assets/item-10539.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 20.00 $ · as printed: “20”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 6. "SPECIAL

![item 10532](classification-review-assets/item-10532.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 15.00 $ · as printed: “15”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 7. SPÉCIAL

![item 10521](classification-review-assets/item-10521.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 20.00 $ · as printed: “20”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 8. SPECIAL MADE GOOD HSRNINGS

![item 10511](classification-review-assets/item-10511.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 15.00 $ · as printed: “15”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 9. SPECIAL

![item 10544](classification-review-assets/item-10544.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 20.00 $ · as printed: “20”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 10. SPÉCIAL

![item 10526](classification-review-assets/item-10526.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 15.00 $ · as printed: “15”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

## Les Marchés Tau (`marches-tau`)

### 1. OLIVEITUP OLIVESDENOYAUTEES FRAICHES

![item 11047](classification-review-assets/item-11047.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-05 → 2026-11-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.86

### 2. LABALOCCHINA RIZITALIEN ITALIAN RICE

![item 11036](classification-review-assets/item-11036.jpg)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-05 → 2026-11-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.97 · other printed prices: 12.99

### 3. NPN 80125057 MATURAL HEALTH PRODUCT NEWCHAPTER

![item 11017](classification-review-assets/item-11017.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 59.99 $ · as printed: “59.99”
- **Flyer validity:** 2026-10-05 → 2026-11-15 · flyer page 1
- **Details:** OCR/extraction confidence: 0.97

### 4. O'MER THONSAUVAGEALBACORE WILDALBACORETUNA

![item 11020](classification-review-assets/item-11020.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.50 $ · as printed: “2/7.00”
- **Flyer validity:** 2026-10-05 → 2026-11-15 · flyer page 1
- **Details:** OCR/extraction confidence: 0.98

### 5. ACRAMENT'BON ACRASDELEGUMES VEGETABLESACRAS

![item 11043](classification-review-assets/item-11043.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 10.00 $ · as printed: “10.00”
- **Flyer validity:** 2026-10-05 → 2026-11-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 6. Abenakis FARINE FLOUR

![item 11019](classification-review-assets/item-11019.jpg)

- **Category:** Pantry > Baking Essentials (FR: Produits du garde-manger > Essentiels de cuisson)
- **How classified:** rule (`baking`)
- **Price:** 4.49 $ · as printed: “4.49”
- **Flyer validity:** 2026-10-05 → 2026-11-15 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 7. YOU POINTS BONIS BONUSPOINTS

![item 11042](classification-review-assets/item-11042.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 9.99 $ · as printed: “9.99”
- **Flyer validity:** 2026-10-05 → 2026-11-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.95

### 8. mitsoh PEMMICAN STRIP

![item 11045](classification-review-assets/item-11045.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-05 → 2026-11-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 9. SPRAY MAL DEGORGE SORE THROAT SPRAY A.Vogel

![item 11026](classification-review-assets/item-11026.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 39.66 $ · as printed: “39.66”
- **Flyer validity:** 2026-10-05 → 2026-11-15 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 10. PIE CRUST DUINKERKEN CROUTEA

![item 11044](classification-review-assets/item-11044.jpg)

- **Category:** Dairy & Eggs > Desserts & Doughs (FR: Produits laitiers et œufs > Desserts et pâtes)
- **How classified:** rule (`dairy-desserts-doughs`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-05 → 2026-11-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

## Les Marchés Tradition (`marches-tradition`)

### 1. FROMAGE COMPLIMENTS CHEESE

![item 10490](classification-review-assets/item-10490.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 11.29 $ · as printed: “11.29”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 7
- **Details:** OCR/extraction confidence: 0.99

### 2. BRACELETS FRIANDISES SLUSHPOPS（650 SLUSHPOPS（72g) TREATS

![item 10392](classification-review-assets/item-10392.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 6.68 $ · as printed: “6.68”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 3. GÂTEAU AU FROMAGE SURGELÉ | RICARDO FROZEN CHEESECAKE

![item 10419](classification-review-assets/item-10419.jpg)

- **Category:** Frozen Food > Frozen Bakery & Breakfast (FR: Produits surgelés > Boulangerie et déjeuner surgelés)
- **How classified:** frozen-remap (`specific-cheesecake`)
- **Price:** 23.99 $ · as printed: “23.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 7
- **Details:** OCR/extraction confidence: 0.99

### 4. BOEUF FRAIS POUR FONDUE CHINOISE OU RACLETTE STERLING SILVER FRESH BEEF FOR CHINESE

![item 10369](classification-review-assets/item-10369.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 15.66 $ · as printed: “15.66”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 5. COLA

![item 10477](classification-review-assets/item-10477.jpg)

- **Category:** Drinks > Soft Drinks (FR: Boissons > Boissons gazeuses)
- **How classified:** rule (`soft-drinks`)
- **Price:** 2.00 $ · as printed: “2/4.00”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 6
- **Details:** OCR/extraction confidence: 0.97

### 6. EAU DE SOURCE GAZÉIFIÉE MAISON PERRIER

![item 10406](classification-review-assets/item-10406.jpg)

- **Category:** Drinks > Water (FR: Boissons > Eau)
- **How classified:** rule (`water`)
- **Price:** 6.62 $ · as printed: “6.62”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.98

### 7. FROMAGE OKA AGROPUR

![item 10402](classification-review-assets/item-10402.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 8. PEPPERONI CASERTA ROMA PEPPERONI CASERTA

![item 10500](classification-review-assets/item-10500.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 8
- **Details:** OCR/extraction confidence: 0.99

### 9. PAPIER HYGIÉNIQUE ROYALE BATHROOM TISSUE

![item 10473](classification-review-assets/item-10473.jpg)

- **Category:** Household > Paper & Storage (FR: Maison > Papier et rangement)
- **How classified:** rule (`household-paper`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

### 10. FARINE FLOUR

![item 10475](classification-review-assets/item-10475.jpg)

- **Category:** Pantry > Baking Essentials (FR: Produits du garde-manger > Essentiels de cuisson)
- **How classified:** rule (`baking`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

## M&M Food Market (`mm-food-market`)

### 1. Crevettesaupanko

![item 10937](classification-review-assets/item-10937.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** store-prior
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 8
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 26.99, 17.99, 19.99

### 2. Pommesdeterre augratin supremes

![item 10885](classification-review-assets/item-10885.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** store-prior
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.97 · other printed prices: 9.99

### 3. FettuccineAlfredoauxcrevettes

![item 10919](classification-review-assets/item-10919.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** store-prior
- **Price:** 21.99 $ · as printed: “21.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 7
- **Details:** OCR/extraction confidence: 0.98 · other printed prices: 24.99

### 4. 9-13UNITES|300g Medaillons de petoncles bardes debacon

![item 10935](classification-review-assets/item-10935.jpg)

- **Category:** Fish & Seafood > Shellfish (FR: Poissons et fruits de mer > Crustacés)
- **How classified:** rule (`shellfish`)
- **Price:** 17.99 $ · as printed: “17.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 8
- **Details:** OCR/extraction confidence: 0.97

### 5. BoeufStroganov

![item 10923](classification-review-assets/item-10923.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** store-prior
- **Price:** 22.99 $ · as printed: “22.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 7
- **Details:** OCR/extraction confidence: 0.99

### 6. Melange defleurons gourmet300g

![item 10940](classification-review-assets/item-10940.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** store-prior
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 9
- **Details:** OCR/extraction confidence: 0.99

### 7. Wonton

![item 10889](classification-review-assets/item-10889.jpg)

- **Category:** International Foods > East Asian Foods (FR: Aliments internationaux > Aliments de l'Asie de l'Est)
- **How classified:** rule (`east-asian`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 8. 6UNITES|318g Pelures depommes de terre farcies

![item 10896](classification-review-assets/item-10896.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** store-prior
- **Price:** 12.99 $ · as printed: “12.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.96 · other printed prices: 14.99

### 9. Poulet au parmesan etspaghetti907g

![item 10922](classification-review-assets/item-10922.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 7
- **Details:** OCR/extraction confidence: 0.97 · other printed prices: 21.99

### 10. Boulettesdebceuf alitalienne 130-140UNITES

![item 10906](classification-review-assets/item-10906.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** store-prior
- **Price:** 12.99 $ · as printed: “12.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.76 · other printed prices: 17.99, 12.99, 17.99

## Marche PA (`marche-pa`)

### 1. BISQUE D'HOMARD FERRER | Lobster Bisque

![item 4760](http://f.wishabi.net/page_items/436667710/1791319629/extra_large.jpg)

- **Category:** Fish & Seafood > Shellfish (FR: Poissons et fruits de mer > Crustacés)
- **How classified:** rule (`shellfish`)
- **Price:** 7.49 $ · as printed: “7.49”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** brand: FERRER · OCR/extraction confidence: 1.00

### 2. POITRINE DE POULET CUITE OU FUMÉE | Cooked or Smoked Chicken Breast

![item 4773](http://f.wishabi.net/page_items/436667758/1791319634/extra_large.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 1.89 $ · as printed: “1.89”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** brand: Maple Lodge Farms · OCR/extraction confidence: 1.00

### 3. MANGUES ATAULFO

![item 4752](http://f.wishabi.net/page_items/436667693/1791319629/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 4.00 $ · as printed: “4.0”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** OCR/extraction confidence: 1.00

### 4. FRAMBOISES | Raspberries

![item 4749](http://f.wishabi.net/page_items/436667686/1791319634/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 4.00 $ · as printed: “4.0”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** OCR/extraction confidence: 1.00

### 5. CHAMPIGNONS BLANC | White Mushrooms

![item 4686](http://f.wishabi.net/page_items/436672315/1791322429/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 3.00 $ · as printed: “3.0”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** OCR/extraction confidence: 1.00

### 6. MERLAN FRAIS | Fresh Whiting

![item 4718](http://f.wishabi.net/page_items/436667730/1791319637/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** OCR/extraction confidence: 1.00

### 7. VITAMINE D3, CURCUMA, MAGNÉSIUM OU ASHWACHILL SUKU

![item 4646](http://f.wishabi.net/page_items/436672383/1791322439/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 16.99 $ · as printed: “16.99”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** brand: SUKU · OCR/extraction confidence: 1.00

### 8. FROMAGE AU LAIT DE CHÈVRE DEMI-AFFINÉ | Cheese

![item 4789](http://f.wishabi.net/page_items/436667755/1791319631/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** OCR/extraction confidence: 1.00

### 9. PETITES LENTILLES TACHETÉES FONCÉES DUNYA HARVEST | Lentils

![item 4693](http://f.wishabi.net/page_items/436672369/1791322441/extra_large.jpg)

- **Category:** Pantry > Dried Beans, Vegetables & Grains (FR: Produits du garde-manger > Haricots secs, légumes et grains)
- **How classified:** rule (`beans-grains`)
- **Price:** 2.49 $ · as printed: “2.49”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** brand: Dunya Harvest · OCR/extraction confidence: 1.00

### 10. BISCUITS AU BEURRE LA GALETTE ST MICHEL | Butter Cookies

![item 4754](http://f.wishabi.net/page_items/436667767/1791319627/extra_large.jpg)

- **Category:** Dairy & Eggs > Butter & Spreads (FR: Produits laitiers et œufs > Beurre et tartinades)
- **How classified:** rule (`butter`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** brand: St Michel · OCR/extraction confidence: 1.00

## Marché Adonis (`adonis`)

### 1. FROMAGE BLANC PUCK | PUCK WHITE CHEESE

![item 7190](http://f.wishabi.net/page_items/436316635/1791013138/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Puck · OCR/extraction confidence: 1.00

### 2. HARD SQUASH | COURGES DURES

![item 7229](http://f.wishabi.net/page_items/436316582/1791013135/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 3. TOMATES ROUGES DE SERRE | RED GREENHOUSE BEEF TOMATOES

![item 7354](http://f.wishabi.net/page_items/436891190/1791519998/extra_large.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 4. FRAISES | STRAWBERRIES

![item 7256](http://f.wishabi.net/page_items/436526883/1791221472/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 3.88 $ · as printed: “3.88”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 5. BIFTECK DE FILET MIGNON DE BOEUF RÉGULIER OU MARINÉ | REGULAR OR MARINATED BEEF TENDERLOIN STEAK

![item 7200](http://f.wishabi.net/page_items/436316609/1791013134/extra_large.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 23.99 $ · as printed: “23.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 6. YOGOURT GREC OU YOGOURT MÉDITERRANÉE LIBERTÉ | LIBERTÉ MÉDITERRANÉE YOGURT

![item 7177](http://f.wishabi.net/page_items/436316529/1791013129/extra_large.jpg)

- **Category:** Dairy & Eggs > Yogurt (FR: Produits laitiers et œufs > Yogourt)
- **How classified:** rule (`yogurt`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Liberté · OCR/extraction confidence: 1.00

### 7. FILETS DE TILAPIA BLUE TIDE | BLUE TIDE TILAPIA FILLETS

![item 7313](http://f.wishabi.net/page_items/436526844/1791221461/extra_large.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: BLUE TIDE · OCR/extraction confidence: 1.00

### 8. POMMES DE TERRE JAUNES, BLANCHES OU ROUGES | YELLOW, WHITE & RED POTATOES

![item 7252](http://f.wishabi.net/page_items/436316585/1791013137/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 9. FROMAGE À LA CRÈME PHILADELPHIA OU SINGLES DE KRAFT | PHILADELPHIA CREAM CHEESE SPREAD OR KRAFT SINGLES

![item 7399](http://f.wishabi.net/page_items/436891116/1791519991/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 3.97 $ · as printed: “3.97”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: PHILADELPHIA | KRAFT · OCR/extraction confidence: 1.00

### 10. PÂTES ALIMENTAIRES PRIMO | PRIMO PASTAS

![item 7184](http://f.wishabi.net/page_items/436316536/1791013135/extra_large.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 1.67 $ · as printed: “1.67”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Primo · OCR/extraction confidence: 1.00

## Marché Ami (`marche-ami`)

### 1. saumon du Pacifique Coupes du marché High Liner

![item 4425](http://f.wishabi.net/page_items/436183836/1790836060/extra_large.jpg)

- **Category:** Fish & Seafood > Salmon (FR: Poissons et fruits de mer > Saumon)
- **How classified:** rule (`salmon`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: HIGH LINER® · OCR/extraction confidence: 1.00

### 2. Bavette de boeuf Irrésistible

![item 4414](http://f.wishabi.net/page_items/436183833/1790836059/extra_large.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 3. repas Michelina's

![item 4470](http://f.wishabi.net/page_items/436183873/1790836060/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Michelina's · OCR/extraction confidence: 1.00

### 4. WALLAROO TRAIL

![item 4407](http://f.wishabi.net/page_items/436183818/1790836065/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: WALLAROO TRAIL · OCR/extraction confidence: 1.00

### 5. mélange à soupe Lipton, Knorr

![item 4445](http://f.wishabi.net/page_items/436183892/1790836060/extra_large.jpg)

- **Category:** Prepared Meals > Salads & Soups (FR: Repas préparés > Salades et soupes)
- **How classified:** rule (`salads-soups`)
- **Price:** 2.39 $ · as printed: “2.39”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Lipton · OCR/extraction confidence: 1.00

### 6. poulet de grain Mieux-être Naturalia

![item 4423](http://f.wishabi.net/page_items/436183840/1790836062/extra_large.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: NATURALIA · OCR/extraction confidence: 1.00

### 7. filets de saumon Atlantique frais

![item 4401](http://f.wishabi.net/page_items/436183798/1790836060/extra_large.jpg)

- **Category:** Fish & Seafood > Salmon (FR: Poissons et fruits de mer > Saumon)
- **How classified:** rule (`salmon`)
- **Price:** 9.99 $ · as printed: “9.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 8. tarte Boulangerie St-Donat

![item 4429](http://f.wishabi.net/page_items/436183902/1790836065/extra_large.jpg)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: St Donat · OCR/extraction confidence: 1.00

### 9. Crevettes et pétoncles Irrésistible

![item 4424](http://f.wishabi.net/page_items/436183853/1790836069/extra_large.jpg)

- **Category:** Fish & Seafood > Shrimp (FR: Poissons et fruits de mer > Crevette)
- **How classified:** rule (`shrimp`)
- **Price:** 10.99 $ · as printed: “10.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Irresistible · OCR/extraction confidence: 1.00

### 10. champignons blancs

![item 4390](http://f.wishabi.net/page_items/436183808/1790836065/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

## Marché Andes (`marche-andes`)

### 1. Biscuits DUCALES

![item 11103](https://www.marcheandes.com/wp-content/uploads/2025/08/Biscuits_Ducales_Sachet.webp)

- **Category:** Snacks, Chips & Candy > Crackers & Cookies (FR: Grignotines, croustilles et friandises > Craquelins et biscuits)
- **How classified:** rule (`crackers-cookies`)
- **Price:** 2.89 $ · as printed: “2.89”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 4367 · OCR/extraction confidence: 1.00 · regular price 3.29

### 2. Biscuits FESTIVAL CITRON

![item 11104](https://www.marcheandes.com/wp-content/uploads/2025/08/Biscuits_Festival_Citron.webp)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 4.19 $ · as printed: “4.19”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 6898 · OCR/extraction confidence: 1.00

## Marché Axep (`marche-axep`)

### 1. PÂTE RÉFRIGÉRÉE POUR CROISSANTS, CREME 5% - 15%, 473 ML SAUCISSES, PIZZA, BISCUITS OU 15 - 35%, 237 ML QUÉBON DE CAMPAGNE OU PETITS PAINS CERTAINES VARIÉTÉS FEUILLETÉS PILLSBURY CREAM CERTAINES VARIÉTÉS, 200 - 391 G 2069522600 EA/20606578_EA

![item 9973](classification-review-assets/item-9973.jpg)

- **Category:** Bakery > Bagels, Croissants & English Muffins (FR: Boulangerie > Bagels, croissants et muffins anglais)
- **How classified:** rule (`specific-audit-fixes`)
- **Price:** 2.29 $ · as printed: “2.29”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 2. CAFEINTERNATIONAL DELIGHT 946 ML, JUS,LIMONADEOU BOISSONAUXFRUITS TROPICANA1,36L

![item 10003](classification-review-assets/item-10003.jpg)

- **Category:** Drinks > Juice (FR: Boissons > Jus)
- **How classified:** rule (`juice`)
- **Price:** 4.29 $ · as printed: “4.29”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 3. BOISSONS GAZEUSES COCA-COLA, PEPSI OU CANADA DRY CERTAINES VARIÉTÉS

![item 9963](classification-review-assets/item-9963.jpg)

- **Category:** Drinks > Soft Drinks (FR: Boissons > Boissons gazeuses)
- **How classified:** rule (`soft-drinks`)
- **Price:** 8.29 $ · as printed: “8.29”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.94

### 4. PLATS CUISINES OU REPAS SURGELÉ PC”° OU MENU BLEU“C SURGELES, CERTAINES VARIETES

![item 9953](classification-review-assets/item-9953.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** frozen-remap (`entrees`)
- **Price:** 10.99 $ · as printed: “10.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 5. ASSIETTES EN PAPIER POUR ASSIETTES EN PAPIER POUR ESSUIE-TOUT SANS NOM® LE DÉJEUNER OÙ LE DÎNER LE DÎNER SANS NOM® 6 = 18 ROUL. SANS NOM® 40 UN. PAPER TOWELS 40 UN. PAPER PLATES 21636329 EA

![item 9997](classification-review-assets/item-9997.jpg)

- **Category:** Household > Paper & Storage (FR: Maison > Papier et rangement)
- **How classified:** rule (`household-paper`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.98

### 6. GARNITURE POUR SALADE 100 G OU CROUTONS 140 G PC” CERTAINES VARIÉTÉS SALAD TOPPER OR CROUTONS

![item 10025](classification-review-assets/item-10025.jpg)

- **Category:** Prepared Meals > Salads & Soups (FR: Repas préparés > Salades et soupes)
- **How classified:** rule (`salads-soups`)
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

### 7. COCKTAIL AUX CANNEBERGES BOISSONS GAZEUSES COCA-COLA, OCEAN SPRAY OU DE TOMATESET CANADA DRY, PEPSI OU DR. PEPPER DE PALOURDES CLAMATO MOTT'S, CERTAINES VARIÉTÉS CERTAINES VARIÉTÉS, 1,89 L (CONSIGNE) 6 X 710 ML (CONSIGNE) JUICE OR COCKTAIL SOFT DRINKS

![item 10000](classification-review-assets/item-10000.jpg)

- **Category:** Beer & Wine > Cider & Coolers (FR: Bières et vins > Cidres et coolers)
- **How classified:** rule (`cider-coolers`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.91

### 8. FRUITS SURGELÉS SANS NOM® NATURELLEMENT IMPARFAITS"C CERTAINES VARIÉTÉS

![item 10002](classification-review-assets/item-10002.jpg)

- **Category:** Frozen Food > Frozen Fruit & Vegetables (FR: Produits surgelés > Fruits et légumes surgelés)
- **How classified:** frozen-remap (`fruits`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 9. CHOU VERT OU ROUGE

![item 9978](classification-review-assets/item-9978.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.81

### 10. ROLD GOLD

![item 10027](classification-review-assets/item-10027.jpg)

- **Category:** Snacks, Chips & Candy > Chips & Snacks (FR: Grignotines, croustilles et friandises > Croustilles et grignotines)
- **How classified:** rule (`chips-snacks`)
- **Price:** 4.49 $ · as printed: “4.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 7
- **Details:** OCR/extraction confidence: 0.99

## Marché BKR (`marche-bkr`)

### 1. INGREDIENTS INGREDID

![item 11485](classification-review-assets/item-11485.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 0.01 $ · as printed: “2192/20.28”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.97

### 2. LA VACHE QUI RIT FROMAGE u48P

![item 11494](classification-review-assets/item-11494.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 14.99 $ · as printed: “14.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

### 3. SHISH TAOUK AU CHOIX

![item 11492](classification-review-assets/item-11492.jpg)

- **Category:** Meat > Kebabs & Marinated Meat (FR: Viande > Brochettes et viande marinée)
- **How classified:** rule (`kebabs-marinated`)
- **Price:** 15.99 $ · as printed: “15.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 4. NAMOURA

![item 11484](classification-review-assets/item-11484.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 14.99 $ · as printed: “14.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 5. HAMMOUD BOISSON AU CHOIX 2L

![item 11490](classification-review-assets/item-11490.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 6. HALIBNA POUDRE DE LAIT 900G

![item 11495](classification-review-assets/item-11495.jpg)

- **Category:** Dairy & Eggs > Milk & Cream (FR: Produits laitiers et œufs > Lait et crème)
- **How classified:** rule (`milk-cream`)
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

### 7. AL AFIA FEUILLE DE VIGNE 45uG

![item 11491](classification-review-assets/item-11491.jpg)

- **Category:** International Foods > Middle Eastern Foods (FR: Aliments internationaux > Aliments du Moyen-Orient)
- **How classified:** rule (`middle-eastern`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 8. OLIVE NOIRE FACON GRECE 1KG

![item 11483](classification-review-assets/item-11483.jpg)

- **Category:** Pantry > Canned & Pickled (FR: Produits du garde-manger > Produits en conserve et marinés)
- **How classified:** rule (`canned-pickled`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 9. EPAULE D'AGNEU

![item 11493](classification-review-assets/item-11493.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 10. DELISH SOUPE AU CHOIX 60G

![item 11486](classification-review-assets/item-11486.jpg)

- **Category:** Prepared Meals > Salads & Soups (FR: Repas préparés > Salades et soupes)
- **How classified:** rule (`salads-soups`)
- **Price:** 0.79 $ · as printed: “0.79”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

## Marché Bonanza (`marche-bonanza`)

### 1. PQTDE

![item 10058](classification-review-assets/item-10058.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 3
- **Details:** OCR/extraction confidence: 0.96

### 2. NOSHEURES SHA2IH SHA2IH SHA2IH SHA18H SHA1SH SHAISH SHAISH D'OUVERTURE

![item 10051](classification-review-assets/item-10051.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.69 $ · as printed: “3.69”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 3. AURRA ALUCRA AEELRA

![item 10052](classification-review-assets/item-10052.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 4. PAQUIT

![item 10040](classification-review-assets/item-10040.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.79 $ · as printed: “3.79”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 5. IERICATE

![item 10043](classification-review-assets/item-10043.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 6. PAQUITO

![item 10037](classification-review-assets/item-10037.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 7. GROS

![item 10061](classification-review-assets/item-10061.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.66 $ · as printed: “6.66”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 3
- **Details:** OCR/extraction confidence: 0.88

### 8. MEZE

![item 10042](classification-review-assets/item-10042.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.29 $ · as printed: “3.29”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 9. CASHEWS

![item 10053](classification-review-assets/item-10053.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 10. CONGELE

![item 10048](classification-review-assets/item-10048.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

## Marché Bonichoix (`marche-bonichoix`)

### 1. CANNEBERGES FRAÎCHES

![item 9645](classification-review-assets/item-9645.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 2. SANDWICHS FARCIS C'EST PRET! STUFFED SANDWICHES

![item 9764](classification-review-assets/item-9764.jpg)

- **Category:** Prepared Meals > Sandwiches (FR: Repas préparés > Sandwichs)
- **How classified:** rule (`sandwiches`)
- **Price:** 3.50 $ · as printed: “2/7.00”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 7
- **Details:** OCR/extraction confidence: 0.95

### 3. LÉGUMES GÉANT VERT (341 où 394 OU POIS TENDRES LE SIEUR (398 mL) VEGETABLES OR

![item 9639](classification-review-assets/item-9639.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 4. SALE

![item 9674](classification-review-assets/item-9674.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.64 $ · as printed: “6.64”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.88

### 5. LITIÈRE AGGLOMÉRANTE @ POUR CHATS CAT'S PRIDE CLUMPING CAT LITTER

![item 9728](classification-review-assets/item-9728.jpg)

- **Category:** Pet > Pet Food (FR: Animaux > Nourriture pour animaux)
- **How classified:** rule (`pet`)
- **Price:** 12.99 $ · as printed: “12.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 6. CHARCUTERIES TRANCHÉES GASPÉSIEN

![item 9723](classification-review-assets/item-9723.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 66.00 $ · as printed: “66”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 4
- **Details:** OCR/extraction confidence: 0.50

### 7. LAIT ÉVAPORÉ CARNATION EVAPORATED MILK

![item 9673](classification-review-assets/item-9673.jpg)

- **Category:** Dairy & Eggs > Milk & Cream (FR: Produits laitiers et œufs > Lait et crème)
- **How classified:** rule (`milk-cream`)
- **Price:** 49.00 $ · as printed: “49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 8. RIZ PRÉCUIT MINUTE RICE PRECOOKED RICE

![item 9744](classification-review-assets/item-9744.jpg)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 9. CIARK L CLASSIQUE] SIROP D'ÉRABL!

![item 9765](classification-review-assets/item-9765.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 4.49 $ · as printed: “4.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 7
- **Details:** OCR/extraction confidence: 0.99

### 10. MARGARINE À on VEGETABLE OIL _ 468% D'HUILE VÉGÉTALE —

![item 9686](classification-review-assets/item-9686.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

## Marché C&T (`marche-c-t`)

### 1. Vermicelle de Riz de jiangmen DoubleSwallowBrandJiangmen RiceVermicelli400gx30

![item 11590](classification-review-assets/item-11590.jpg)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 42.00 $ · as printed: “42.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 2. Aubergine Eggplant

![item 11588](classification-review-assets/item-11588.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.83

### 3. ORIGINAL FDRBAT

![item 11569](classification-review-assets/item-11569.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.59 $ · as printed: “3.59”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.94

### 4. GeleedeViandeBouilli de Salade d'algues Palourde Bebe Congelés

![item 11574](classification-review-assets/item-11574.jpg)

- **Category:** Frozen Food > Frozen Meat and Seafood (FR: Produits surgelés > Viande et fruits de mer surgelés)
- **How classified:** frozen-remap (`shellfish`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.93 · other printed prices: 1.00

### 5. Raisin Shine Muscat Grapes

![item 11550](classification-review-assets/item-11550.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 3.51 $ · as printed: “3.51”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 5.05, 2.84, 1.29

### 6. SALSA

![item 11570](classification-review-assets/item-11570.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 0.00 $ · as printed: “00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.97

### 7. QueuedeBoeufDecongele Thawed Oxtail

![item 11541](classification-review-assets/item-11541.jpg)

- **Category:** Frozen Food > Frozen Meat and Seafood (FR: Produits surgelés > Viande et fruits de mer surgelés)
- **How classified:** frozen-remap (`game-offal`)
- **Price:** 19.82 $ · as printed: “19.82”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 8.99

### 8. Doré Jaune Pickerel

![item 11539](classification-review-assets/item-11539.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 11.00 $ · as printed: “11.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 9. Darnes de Carpea grosse tete Big head carp Steak

![item 11538](classification-review-assets/item-11538.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 8.80 $ · as printed: “8.80”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.98

### 10. THOROUG

![item 11578](classification-review-assets/item-11578.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 31.99 $ · as printed: “31.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

## Marché Frutta Si (`frutta-si`)

### 1. Patate douce Sweet potato Grandeur/Size

![item 11005](classification-review-assets/item-11005.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 0.89 $ · as printed: “0.89”
- **Flyer validity:** 2026-10-06 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 2. Saucisses Soc de porc desosse Italiennes maison

![item 11013](classification-review-assets/item-11013.jpg)

- **Category:** Meat > Sausages (FR: Viande > Saucisses)
- **How classified:** rule (`sausages`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-13 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 3. Cathedral City San Daniele Cheddar

![item 11014](classification-review-assets/item-11014.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-13 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 4. Primo Pates assorties

![item 11016](classification-review-assets/item-11016.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 0.85 $ · as printed: “0.85”
- **Flyer validity:** 2026-10-13 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 5. Patates Potatoes 10lbs

![item 11004](classification-review-assets/item-11004.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 20.99 $ · as printed: “20.99”
- **Flyer validity:** 2026-10-06 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.95

### 6. Pamplemousse Oranges Grapefruit

![item 11010](classification-review-assets/item-11010.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-13 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.98

### 7. Pamplemousse Oranges Grapefruit

![item 11003](classification-review-assets/item-11003.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-06 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.98

### 8. Patates Potatoes 10lbs

![item 11011](classification-review-assets/item-11011.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 20.99 $ · as printed: “20.99”
- **Flyer validity:** 2026-10-13 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.95

### 9. Cathedral City San Daniele Cheddar

![item 11007](classification-review-assets/item-11007.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-06 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 10. Patate douce Sweet potato Grandeur/Size

![item 11012](classification-review-assets/item-11012.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 0.89 $ · as printed: “0.89”
- **Flyer validity:** 2026-10-13 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

## Marché Fu Tai (`marche-fu-tai`)

### 1. - CREME ÉPAISSE

![item 10138](classification-review-assets/item-10138.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 62.00 $ · as printed: “62”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.64

### 2. VIANDEIDE! PAUOURDE CONGEUÉE FES SEVEN BASKETS)

![item 10106](classification-review-assets/item-10106.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.98 $ · as printed: “2.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 1
- **Details:** OCR/extraction confidence: 0.74 · other printed prices: 4.68

### 3. CHOCOLATE CHIP

![item 10149](classification-review-assets/item-10149.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 3.49 $ · as printed: “2/6.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 5
- **Details:** OCR/extraction confidence: 0.88

### 4. CHAMPIGNONS ENOKI

![item 10113](classification-review-assets/item-10113.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 0.99 $ · as printed: “2/1.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 5. POULET ÉPICÉ SZECHUAN

![item 10139](classification-review-assets/item-10139.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 9.98 $ · as printed: “9.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.90

### 6. BEURRE D'ARACHIDE CRÉMEUX FREAK KRAFT

![item 10137](classification-review-assets/item-10137.jpg)

- **Category:** Pantry > Honey, Syrups & Spreads (FR: Produits du garde-manger > Miel, sirops et tartinades)
- **How classified:** rule (`specific-nut-butters`)
- **Price:** 9.00 $ · as printed: “9”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.96

### 7. SERIESDE DUMPLINGS AUXLEGUMES POONG

![item 10144](classification-review-assets/item-10144.jpg)

- **Category:** Prepared Meals > Entrees & Appetizers (FR: Repas préparés > Plats principaux et apéritifs)
- **How classified:** rule (`entrees`)
- **Price:** 5.88 $ · as printed: “5.88”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 8. POISSON GRILLÉ AVEC SEL ET POIVRE

![item 10135](classification-review-assets/item-10135.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 88.00 $ · as printed: “88”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.59

### 9. POIVRONS VERTS

![item 10120](classification-review-assets/item-10120.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 8.60 $ · as printed: “8.60”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.88 · other printed prices: 1.28

### 10. 6 PIECES CROISSANT ALA CREME AU CACAO Wp A+ÉEE SHIBABA

![item 10133](classification-review-assets/item-10133.jpg)

- **Category:** Bakery > Bagels, Croissants & English Muffins (FR: Boulangerie > Bagels, croissants et muffins anglais)
- **How classified:** rule (`specific-audit-fixes`)
- **Price:** 2.88 $ · as printed: “2.88”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.71

## Marché Korea (`marche-korea`)

### 1. MYUNSARANG Jjajangmyun 면사랑 짜장면 300g

![item 11423](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/04/%EB%A9%B4%EC%82%AC%EB%9E%91-%EC%A7%9C%EC%9E%A5%EB%A9%B4.png?fit=500%2C500&ssl=1)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 8802039310059 · OCR/extraction confidence: 1.00 · regular price 5.99

### 2. GREEN FOOD Bâton de riz (citrouille) 쌀과자 단호박맛 40G

![item 11336](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/08/%EB%8B%A8%ED%98%B8%EB%B0%95%EB%A7%9B.png?fit=500%2C500&ssl=1)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 8809480060069 · OCR/extraction confidence: 1.00 · regular price 3.29

### 3. WAFU Sauce de sésame 와푸 참깨소스 480ML

![item 11386](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/06/Black-And-White-Minimalist-Typography-Personal-Logo-500-x-500-px-5.png?fit=500%2C500&ssl=1)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 831048000284 · OCR/extraction confidence: 1.00 · regular price 9.99

### 4. WOOMTREE Pâte de wasabi (pour la viande) 움트리 육류 생와사비랑 120g

![item 11331](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/08/%EC%9B%80%ED%8A%B8%EB%A6%AC-%EC%9C%A1%EB%A5%98.png?fit=500%2C500&ssl=1)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 8801558500286 · OCR/extraction confidence: 1.00 · regular price 6.99

### 5. DAESANG Pâte à tartiner au beurre de haricots 복음자리 앙버터 스프레드 120g

![item 11412](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/04/%EB%8C%80%EC%83%81-%EC%95%99%EB%B2%84%ED%84%B0.png?fit=500%2C500&ssl=1)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 8805999603957 · OCR/extraction confidence: 1.00 · regular price 4.49

### 6. DAESANG Confiture fraise 대상 복음자리 딸기 잼 100G

![item 11417](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/04/%EB%B3%B5%EC%9D%8C%EC%9E%90%EB%A6%AC-%EB%94%B8%EA%B8%B0.png?fit=500%2C500&ssl=1)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 805999601045 · OCR/extraction confidence: 1.00 · regular price 3.29

### 7. ProteeOne Soupe Proteine au Saveur Ramen 프로티원 단백질스프 라면맛 45g x 5

![item 11365](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/06/Black-And-White-Minimalist-Typography-Personal-Logo-500-x-500-px-12-2.png?fit=500%2C500&ssl=1)

- **Category:** Pantry > Easy Meals & Sides (FR: Produits du garde-manger > Mets faciles et accompagnements)
- **How classified:** rule (`easy-meals`)
- **Price:** 9.99 $ · as printed: “9.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00 · regular price 18.99

### 8. WOOMTREE Sauce mala 움트리 마라소스 440G

![item 11396](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/05/%EC%9B%80%ED%8A%B8%EB%A6%AC-%EB%A7%88%EB%9D%BC.png?fit=500%2C500&ssl=1)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 8801558300848 · OCR/extraction confidence: 1.00 · regular price 7.99

### 9. HOJEONGGA Yakgwa au riz gluant sesamen noir  호정가 흑임자 약과 455g

![item 11341](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/02/%ED%98%B8%EC%A0%95%EA%B3%BC-%ED%9D%91%EC%9E%84%EC%9E%90%EC%95%BD%EA%B3%BC-455g.png?fit=500%2C500&ssl=1)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 8804624072021 · OCR/extraction confidence: 1.00 · regular price 7.99

### 10. GOMPYO Melange pour gateau Hot Cake 곰표 핫케잌 가루 500g

![item 11343](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/05/%EA%B3%B0%ED%91%9C-%ED%95%AB%EC%BC%80%EC%9E%8C%EA%B0%80%EB%A3%A8-500g.png?fit=500%2C500&ssl=1)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 2.29 $ · as printed: “2.29”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 8801176252017 · OCR/extraction confidence: 1.00 · regular price 3.59

## Marché Lian Tai (`marche-lian-tai`)

### 1. TENTACULES DE CALMAR

![item 4547](http://f.wishabi.net/page_items/436836566/1791438974/extra_large.jpg)

- **Category:** Fish & Seafood > Squid & Octopus (FR: Poissons et fruits de mer > Calmar et pieuvre)
- **How classified:** rule (`squid-octopus`)
- **Price:** 118.98 $ · as printed: “118.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 2. MÉLANGE À CROÛTE CROUSTILLANTE POUR Frites

![item 4566](http://f.wishabi.net/page_items/436836598/1791438979/extra_large.jpg)

- **Category:** Prepared Meals > Fries & Sides (FR: Repas préparés > Frites et accompagnements)
- **How classified:** rule (`fries-sides`)
- **Price:** 6.98 $ · as printed: “6.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: AJ · OCR/extraction confidence: 1.00

### 3. POISSON PORGY

![item 4581](http://f.wishabi.net/page_items/436836517/1791438979/extra_large.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 1.98 $ · as printed: “1.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 4. SAUCE DE SOJA

![item 4511](http://f.wishabi.net/page_items/436836526/1791438976/extra_large.jpg)

- **Category:** Pantry > Condiments (FR: Produits du garde-manger > Condiments et garnitures)
- **How classified:** rule (`condiments`)
- **Price:** 4.98 $ · as printed: “4.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 5. VIANDE D'AGNEAU AVEC PEAU

![item 4584](http://f.wishabi.net/page_items/436836493/1791438982/extra_large.jpg)

- **Category:** Meat > Lamb & Veal (FR: Viande > Agneau et veau)
- **How classified:** rule (`lamb-veal`)
- **Price:** 8.88 $ · as printed: “8.88”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 6. POUSSE D'AIL

![item 4482](http://f.wishabi.net/page_items/436836504/1791438977/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.98 $ · as printed: “1.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 7. YUCHOI

![item 4548](http://f.wishabi.net/page_items/436836567/1791438975/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 29.98 $ · as printed: “29.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 8. CACAHUÈTES ROUGES QUATRE

![item 4586](http://f.wishabi.net/page_items/436836496/1791438984/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.98 $ · as printed: “6.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: GUXIN · OCR/extraction confidence: 1.00

### 9. VIN DE RIZ DU GUANGDONG POUR LA CUISINE

![item 4514](http://f.wishabi.net/page_items/436836542/1791438987/extra_large.jpg)

- **Category:** Beer & Wine > Wine (FR: Bières et vins > Vins)
- **How classified:** rule (`wine`)
- **Price:** 3.58 $ · as printed: “3.58”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: SHI WAN · OCR/extraction confidence: 1.00

### 10. BISCUIT AUX AMANDES

![item 4553](http://f.wishabi.net/page_items/436836581/1791438986/extra_large.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 7.88 $ · as printed: “7.88”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

## Marché Newon (`marche-newon`)

### 1. ELLE PS COMBO/SAUCE SOJARVINAIGRE

![item 10167](classification-review-assets/item-10167.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 98.00 $ · as printed: “98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 2. NISSIN NOUILLE CHOIX VARIE

![item 10228](classification-review-assets/item-10228.jpg)

- **Category:** Pantry > Easy Meals & Sides (FR: Produits du garde-manger > Mets faciles et accompagnements)
- **How classified:** rule (`easy-meals`)
- **Price:** 98.00 $ · as printed: “98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 3. GZ). PAIN VAPEUR CHOIX VARIE

![item 10207](classification-review-assets/item-10207.jpg)

- **Category:** Bakery > Bread (FR: Boulangerie > Pain)
- **How classified:** rule (`bread`)
- **Price:** 98.00 $ · as printed: “98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 4. VISA

![item 10231](classification-review-assets/item-10231.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 9.98 $ · as printed: “9.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 5. HUJTR ILLE/XL OYSTER IN SHELL/

![item 10200](classification-review-assets/item-10200.jpg)

- **Category:** Fish & Seafood > Shellfish (FR: Poissons et fruits de mer > Crustacés)
- **How classified:** rule (`shellfish`)
- **Price:** 98.00 $ · as printed: “98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 6. BLANCHE TEE 40.50%

![item 10209](classification-review-assets/item-10209.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 9999.66 $ · as printed: “9999.66”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.91

### 7. ROGERS LANTIC SUCRE GRANULE ROGERS GRANULATED SUGAR

![item 10253](classification-review-assets/item-10253.jpg)

- **Category:** Pantry > Baking Essentials (FR: Produits du garde-manger > Essentiels de cuisson)
- **How classified:** rule (`baking`)
- **Price:** 2.98 $ · as printed: “2.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 8. PU DATTES CHINOISES

![item 10256](classification-review-assets/item-10256.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 9.98 $ · as printed: “9.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 2.98, 10.88

### 9. SUGAR

![item 10254](classification-review-assets/item-10254.jpg)

- **Category:** Pantry > Baking Essentials (FR: Produits du garde-manger > Essentiels de cuisson)
- **How classified:** rule (`baking`)
- **Price:** 58.00 $ · as printed: “58”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 10. IF EAU DE NOIX COCO IF COCONUT WATER

![item 10252](classification-review-assets/item-10252.jpg)

- **Category:** Drinks > Water (FR: Boissons > Eau)
- **How classified:** rule (`water`)
- **Price:** 19.88 $ · as printed: “19.88”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

## Marché Richelieu (`marche-richelieu`)

### 1. croustilles Irrésistible | Irrésistible potato chips

![item 4892](http://f.wishabi.net/page_items/436171206/1790832569/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Irresistible · OCR/extraction confidence: 1.00

### 2. ketchup aux tomates French's | French's ketchup

![item 4896](http://f.wishabi.net/page_items/436171177/1790832566/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: French's · OCR/extraction confidence: 1.00

### 3. maïs soufflé Impérial | Impérial popcorn

![item 4800](http://f.wishabi.net/page_items/436171213/1790832574/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Chips & Snacks (FR: Grignotines, croustilles et friandises > Croustilles et grignotines)
- **How classified:** rule (`specific-popcorn`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Imperial · OCR/extraction confidence: 1.00

### 4. BAVETTE DE VEAU FAMILLE FONTAINE | FONTAINE FAMILY VEAL

![item 4858](http://f.wishabi.net/page_items/436171141/1790832581/extra_large.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 13.99 $ · as printed: “13.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Famille Fontaine · OCR/extraction confidence: 1.00

### 5. sandwichs assortis | assorted sandwiches, economic pack

![item 4818](http://f.wishabi.net/page_items/436171164/1790832576/extra_large.jpg)

- **Category:** Prepared Meals > Sandwiches (FR: Repas préparés > Sandwichs)
- **How classified:** rule (`sandwiches`)
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 6. melon d'eau sans pépins | seedless watermelon

![item 4869](http://f.wishabi.net/page_items/436171160/1790832574/extra_large.jpg)

- **Category:** Drinks > Water (FR: Boissons > Eau)
- **How classified:** rule (`water`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 7. BIÈRE LABATT, MOLSON, SLEEMAN | BEER

![item 4839](http://f.wishabi.net/page_items/436171110/1790832567/extra_large.jpg)

- **Category:** Beer & Wine > Beer (FR: Bières et vins > Bières)
- **How classified:** rule (`beer`)
- **Price:** 32.29 $ · as printed: “32.29”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 8. BAGELS STYLE MONTRÉAL | MONTRÉAL STYLE BAGELS

![item 4875](http://f.wishabi.net/page_items/436171145/1790832565/extra_large.jpg)

- **Category:** Bakery > Bagels, Croissants & English Muffins (FR: Boulangerie > Bagels, croissants et muffins anglais)
- **How classified:** rule (`bagels-croissants`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 9. jus ou nectar Selection | Selection juice or nectar

![item 4820](http://f.wishabi.net/page_items/436171217/1790832576/extra_large.jpg)

- **Category:** Drinks > Juice (FR: Boissons > Jus)
- **How classified:** rule (`juice`)
- **Price:** 1.79 $ · as printed: “1.79”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Selection · OCR/extraction confidence: 1.00

### 10. FRAMBOISES, MÛRES | RASPBERRIES, BLACKBERRIES

![item 4801](http://f.wishabi.net/page_items/436171174/1790832570/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

## Marché Sheng Tai (`marche-sheng-tai`)

### 1. POINTE DE SURLONGE DE BOEUF

![item 10293](classification-review-assets/item-10293.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 7.98 $ · as printed: “7.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 2. CREVETTES BLANCHES

![item 10282](classification-review-assets/item-10282.jpg)

- **Category:** Fish & Seafood > Shrimp (FR: Poissons et fruits de mer > Crevette)
- **How classified:** rule (`shrimp`)
- **Price:** 2.00 $ · as printed: “2/4.00”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.95

### 3. 4850 SOURCES BLVD, DOLLARD-DES ORMEAUX, QUEBEC H8Y 3C7

![item 10275](classification-review-assets/item-10275.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.08 $ · as printed: “3.08”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 1
- **Details:** OCR/extraction confidence: 0.67

### 4. SERIES DE GATEAU DE RIZ 5 BEA REG:47:99

![item 10307](classification-review-assets/item-10307.jpg)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 5.98 $ · as printed: “5.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.81

### 5. SERIES DE SHUMAI DE RIZ RAS RÉG.: 8.99

![item 10308](classification-review-assets/item-10308.jpg)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 68.00 $ · as printed: “68”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.82

### 6. ATWANDOHO

![item 10303](classification-review-assets/item-10303.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.98 $ · as printed: “2.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 7. ) j BQULETTES 100:

![item 10294](classification-review-assets/item-10294.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.98 $ · as printed: “3.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 10/3.98

### 8. 4850 SOURCES BLVD, DOLLARD-DES ORMEAUX, QUEBEC H8Y 3C7

![item 10290](classification-review-assets/item-10290.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.00 $ · as printed: “2/6.00”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.94

### 9. PETIT TONNA BRNSS RÉG.: 4.99

![item 10318](classification-review-assets/item-10318.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.58 $ · as printed: “3.58”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.97

### 10. ANANAS ENTIER

![item 10300](classification-review-assets/item-10300.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 1.98 $ · as printed: “1.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

## Marché Sultan (`marche-sultan`)

### 1. Ideal Flan Preparafonenpoucre pour

![item 11456](classification-review-assets/item-11456.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.93

### 2. Tahini

![item 11457](classification-review-assets/item-11457.jpg)

- **Category:** Pantry > Honey, Syrups & Spreads (FR: Produits du garde-manger > Miel, sirops et tartinades)
- **How classified:** rule (`honey-spreads`)
- **Price:** 7.49 $ · as printed: “7.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 6.66

### 3. COURSELIBRE

![item 11481](classification-review-assets/item-11481.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 9.99 $ · as printed: “9.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.97 · other printed prices: 18.99

### 4. Sukay

![item 11466](classification-review-assets/item-11466.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 5. aysan' JALAPENO TURSUSU

![item 11477](classification-review-assets/item-11477.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.91 · other printed prices: 66.01

### 6. SPECIALFINE GRANULATEN SUGAR

![item 11454](classification-review-assets/item-11454.jpg)

- **Category:** Pantry > Baking Essentials (FR: Produits du garde-manger > Essentiels de cuisson)
- **How classified:** rule (`baking`)
- **Price:** 3.29 $ · as printed: “3.29”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.63

### 7. PHOENICIA

![item 11473](classification-review-assets/item-11473.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.49 $ · as printed: “2.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.93 · other printed prices: 1.99

### 8. SEL DE TABLE

![item 11480](classification-review-assets/item-11480.jpg)

- **Category:** Pantry > Spices & Seasonings (FR: Produits du garde-manger > Épices et assaisonnements)
- **How classified:** rule (`spices`)
- **Price:** 6.61 $ · as printed: “6.61”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.74

### 9. Arome Choclal

![item 11460](classification-review-assets/item-11460.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.68 $ · as printed: “6.68”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.91 · other printed prices: 6.66

### 10. COOHSm6.mUTES

![item 11471](classification-review-assets/item-11471.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

## Maxi (`maxi`)

### 1. BOISSON DE MALT ALCOOLISÉE BULLES DE NUIT, 750 mL

![item 217](https://f.wishabi.net/page_pdf_images/24243307/e4b96fbe-bddc-11f1-92b0-5666795408c2/x_large)

- **Category:** Beer & Wine > Cider & Coolers (FR: Bières et vins > Cidres et coolers)
- **How classified:** rule (`cider-coolers`)
- **Price:** 7.00 $ · as printed: “7.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Bulles de Nuit · SKU: 21114619_EA · OCR/extraction confidence: 1.00 · “voir sélection en magasin bouteilles”

### 2. FRUITS SURGELÉS PCMD, 300-600 G

![item 11](https://f.wishabi.net/page_pdf_images/24243383/bee6ed7c-bddf-11f1-8135-964e96f5df87/x_large)

- **Category:** Frozen Food > Frozen Fruit & Vegetables (FR: Produits surgelés > Fruits et légumes surgelés)
- **How classified:** frozen-remap (`fruits`)
- **Price:** 4.00 $ · as printed: “4.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: PC · SKU: 20312227_EA · OCR/extraction confidence: 1.00 · “Certaines variétés”

### 3. POUDING BELSOY, 4x125 g

![item 188](https://f.wishabi.net/page_pdf_images/24243262/d0a2b2ce-bddc-11f1-92b0-5666795408c2/x_large)

- **Category:** Dairy & Eggs > Desserts & Doughs (FR: Produits laitiers et œufs > Desserts et pâtes)
- **How classified:** rule (`dairy-desserts-doughs`)
- **Price:** 4.50 $ · as printed: “4.50”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: BELSOY · SKU: 20151398003_EA · OCR/extraction confidence: 1.00 · “certaines variétés”

### 4. PRÉPARATION EN POUDRE POUR NOURRISSONS PRO ADVANCE SIMILAC, ÉTAPE 1 OU 2, 837/859 G

![item 209](https://f.wishabi.net/page_pdf_images/24243289/d6fbd0ce-bddc-11f1-9651-42cd2c0133c3/x_large)

- **Category:** Baby > Baby Food (FR: Bébé > Aliments pour bébé)
- **How classified:** rule (`baby-food`)
- **Price:** 55.00 $ · as printed: “55.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Similac · SKU: 21436985_EA · OCR/extraction confidence: 1.00 · “Certaines variétés”

### 5. LAIT FINEMENT FILTRÉ NATREL, 2 L

![item 54](https://f.wishabi.net/page_pdf_images/24243267/eb6cf272-bddc-11f1-a648-b259641cfd59/x_large)

- **Category:** Dairy & Eggs > Milk & Cream (FR: Produits laitiers et œufs > Lait et crème)
- **How classified:** rule (`milk-cream`)
- **Price:** 4.77 $ · as printed: “4.77”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Natrel · SKU: 20301315004_EA · OCR/extraction confidence: 1.00 · “certaines variétés”

### 6. PAPIER HYGIÉNIQUE CHARMIN 8=24 ROULEAUX OU ESSUIE-TOUT BOUNTY 3=6 ROULEAUX | BATHROOM TISSUE OR PAPER TOWELS

![item 206](https://f.wishabi.net/page_pdf_images/24243293/e8b25a9a-bddc-11f1-9d37-12f6bb1b2a41/x_large)

- **Category:** Household > Paper & Storage (FR: Maison > Papier et rangement)
- **How classified:** rule (`household-paper`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: CHARMIN | BOUNTY · SKU: 21670159_EA · OCR/extraction confidence: 1.00 · “certaines variétés selected varieties”

### 7. TABLETTES FORMAT COLLATION CADBURY, 90 UN.

![item 259](https://f.wishabi.net/page_pdf_images/24243262/d19af880-bddc-11f1-92b0-5666795408c2/x_large)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 16.99 $ · as printed: “16.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Cadbury · SKU: 21736021_EA · OCR/extraction confidence: 1.00

### 8. BARRES DE CHOCOLAT CADBURY | CHOCOLATE BARS, 80-105 G

![item 279](https://f.wishabi.net/page_pdf_images/24243298/e11ff8be-bddc-11f1-9083-8e0b0163410d/x_large)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 2.25 $ · as printed: “2.25”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Cadbury · SKU: 21648577_EA · loyalty-gated price · OCR/extraction confidence: 1.00 · “certaines variétés selected varieties”

### 9. FILET DE SAUMON DE L'ATLANTIQUE FRAIS

![item 314](https://f.wishabi.net/page_pdf_images/24243383/ab3a5cfa-bddf-11f1-8135-964e96f5df87/x_large)

- **Category:** Fish & Seafood > Salmon (FR: Poissons et fruits de mer > Saumon)
- **How classified:** rule (`salmon`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-11
- **Details:** SKU: 20339767_KG · OCR/extraction confidence: 1.00 · “19,82/kg”

### 10. DUO DE PAINS GADOUA | DUO BREAD, 2X675 G

![item 269](https://f.wishabi.net/page_pdf_images/24243257/025454da-bddd-11f1-9e67-ce216e6cd4c1/x_large)

- **Category:** Bakery > Bread (FR: Boulangerie > Pain)
- **How classified:** rule (`bread`)
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Gadoua · SKU: 20300271_EA · OCR/extraction confidence: 1.00 · “certaines variétés selected varieties”

## Mayrand Food Group (`mayrand`)

### 1. 2.00$/each

![item 11503](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=1)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.00 $ · as printed: “2/4.00”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 2. Fresh

![item 11510](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=2)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 8.80 $ · as printed: “8.80”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 2
- **Details:** OCR/extraction confidence: 0.92

### 3. Natrel RYCREA

![item 11526](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=5)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.10 $ · as printed: “2.10”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 5
- **Details:** OCR/extraction confidence: 0.94

### 4. Bianco di Napoli Fire-roasted crushed or diced

![item 11520](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=4)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.49 $ · as printed: “6.49”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 5. Olymel

![item 11530](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=5)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 59.99 $ · as printed: “59.99”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 6. Platinum

![item 11536](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=6)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 26.75 $ · as printed: “26.75”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 6
- **Details:** OCR/extraction confidence: 0.97

### 7. TreStelle PARMIGIANO REGGIANO

![item 11517](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=3)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 8. BIG

![item 11519](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=3)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 9. TARTEAUX BLEUETS SAUVAGES

![item 11521](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=4)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 5.59 $ · as printed: “5.59”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 4
- **Details:** OCR/extraction confidence: 0.98

### 10. Reg.price:49.49$

![item 11529](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=5)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 49.42 $ · as printed: “49.42”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

## Metro (`metro`)

### 1. LAIT FINEMENT FILTRÉ NATREL | NATREL FINE-FILTERED MILK

![item 6409](http://f.wishabi.net/page_items/436826191/1791433303/extra_large.jpg)

- **Category:** Dairy & Eggs > Milk & Cream (FR: Produits laitiers et œufs > Lait et crème)
- **How classified:** rule (`milk-cream`)
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 2. CROÛTONS GRISSOL | GRISSOL CROUTONS

![item 6520](http://f.wishabi.net/page_items/436191237/1791211417/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.49 $ · as printed: “2.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 3. COUSCOUS TIPIAK | TIPIAK COUSCOUS

![item 6273](http://f.wishabi.net/page_items/436826184/1791433298/extra_large.jpg)

- **Category:** Pantry > Dried Beans, Vegetables & Grains (FR: Produits du garde-manger > Haricots secs, légumes et grains)
- **How classified:** rule (`beans-grains`)
- **Price:** 10.49 $ · as printed: “10.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 4. MÉLANGE DE SALADE ATTITUDE | ATTITUDE SALAD MIX OR FOLIA CRUNCHY LETTUCE

![item 5940](http://f.wishabi.net/page_items/436825671/1791442101/extra_large.jpg)

- **Category:** Fruits & Vegetables > Packaged Salads & Dressing (FR: Fruits et légumes > Salades préemballées et vinaigrettes)
- **How classified:** rule (`packaged-salads`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 5. BIÈRE BORÉALE | BEER

![item 6380](http://f.wishabi.net/page_items/436189452/1790831098/extra_large.jpg)

- **Category:** Beer & Wine > Beer (FR: Bières et vins > Bières)
- **How classified:** rule (`beer`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 6. FRIANDISES CHOCOLATÉES FREDDO | FREDDO CHOCOLATE TREATS

![item 6061](http://f.wishabi.net/page_items/436825944/1791442109/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 8.49 $ · as printed: “8.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 7. TORTILLAS POM | POM TORTILLAS

![item 6392](http://f.wishabi.net/page_items/436826169/1791433287/extra_large.jpg)

- **Category:** Bakery > Wraps, Flatbread & Pizza Crust (FR: Boulangerie > Roulés, pains plats et croûtes à pizza)
- **How classified:** rule (`wraps-flatbread`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 8. CRETONS NOREL | NOREL CRETONS

![item 6157](http://f.wishabi.net/page_items/436825827/1791488346/extra_large.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 9. POUDINGS DE SOYA BELSOY | BELSOY SOYA PUDDING CUPS

![item 6221](http://f.wishabi.net/page_items/436826129/1791433074/extra_large.jpg)

- **Category:** Dairy & Eggs > Desserts & Doughs (FR: Produits laitiers et œufs > Desserts et pâtes)
- **How classified:** rule (`dairy-desserts-doughs`)
- **Price:** 13.00 $ · as printed: “13.0”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 10. RADIS EN FEUILLES | TOP RADISHES

![item 6300](http://f.wishabi.net/page_items/436191306/1791211332/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.77 $ · as printed: “1.77”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

## Metro Plus (`metro-plus`)

### 1. FIGUES FRAÎCHES | FRESH FIGS

![item 9560](http://f.wishabi.net/page_items/436191084/1791211291/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 13.99 $ · as printed: “13.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 2. BEURRE PRÉSIDENT | PRÉSIDENT BUTTER

![item 8884](http://f.wishabi.net/page_items/436825891/1791442116/extra_large.jpg)

- **Category:** Dairy & Eggs > Butter & Spreads (FR: Produits laitiers et œufs > Beurre et tartinades)
- **How classified:** rule (`butter`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 3. DINER HEALTHY CHOICE | HEALTHY CHOICE DINNER

![item 9049](http://f.wishabi.net/page_items/436825895/1791442097/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 4. PAIN PARISIEN | PARISIAN BREAD

![item 8921](http://f.wishabi.net/page_items/436825799/1791442098/extra_large.jpg)

- **Category:** Bakery > Bread (FR: Boulangerie > Pain)
- **How classified:** rule (`bread`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 5. CLIQUEZ ICI

![item 9434](http://f.wishabi.net/page_items/436511949/1791211408/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 6. CAISSE DE 12 CANETTES

![item 8986](http://f.wishabi.net/page_items/436825967/1791442100/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 27.99 $ · as printed: “27.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 7. BIFTECKS DE HAUT DE SURLIÈGE (BOEUF) | BONELESS TOP SIRLOIN

![item 8962](http://f.wishabi.net/page_items/436825747/1791442105/extra_large.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 8. PRUNEAUX DÉNOYAUTÉS IRRÉSISTIBLE | IRRÉSISTIBLE PITTED PRUNES

![item 8993](http://f.wishabi.net/page_items/436826005/1791488259/extra_large.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 10.99 $ · as printed: “10.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 9. GROS ANANAS TROPICAL GOLD, ANANAS DÉCORTIQUÉ | TROPICAL GOLD LARGE PINEAPPLE OR CORED PINEAPPLE

![item 9546](http://f.wishabi.net/page_items/436189015/1790831099/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 10. RAISINS SULTANA IRRÉSISTIBLE | IRRÉSISTIBLE SULTANA RAISINS

![item 8992](http://f.wishabi.net/page_items/436826003/1791488258/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

## Milano Fruiterie (`milano-fruiterie`)

### 1. FOURCHEESERISOTTO TRUFFLERISOTTO

![item 11112](classification-review-assets/item-11112.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.95

### 2. RIB STEAK PRIME BOEUF

![item 11123](classification-review-assets/item-11123.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 65.99 $ · as printed: “65.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.97

### 3. TOMATES ENTIÈRE PELÉES LA SAN MARZANO

![item 11118](classification-review-assets/item-11118.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.87

### 4. PECORINO ROMANO PRODUIT ITALIEN

![item 11120](classification-review-assets/item-11120.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 3.59 $ · as printed: “3.59”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.87 · other printed prices: 35.90

### 5. JAMBON SERRANO 24 MOIS PRODUIT ESPAGNOL

![item 11113](classification-review-assets/item-11113.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.85 · other printed prices: 69.90

### 6. DAL MOLISE BOULES MOZZA RELLA

![item 11117](classification-review-assets/item-11117.jpg)

- **Category:** International Foods > South Asian Foods (FR: Aliments internationaux > Aliments de l'Asie du Sud)
- **How classified:** rule (`south-asian`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.88

### 7. HUILEO'OLIVE EXTRAVIERGE EXTRAVIRGIN OLIVEOIL

![item 11110](classification-review-assets/item-11110.jpg)

- **Category:** Pantry > Canned & Pickled (FR: Produits du garde-manger > Produits en conserve et marinés)
- **How classified:** rule (`canned-pickled`)
- **Price:** 39.99 $ · as printed: “39.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.93

### 8. MURCAS

![item 11111](classification-review-assets/item-11111.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.93

### 9. RÔTI DE PALETTE

![item 11121](classification-review-assets/item-11121.jpg)

- **Category:** International Foods > South Asian Foods (FR: Aliments internationaux > Aliments de l'Asie du Sud)
- **How classified:** rule (`south-asian`)
- **Price:** 24.99 $ · as printed: “24.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.90

### 10. POIREAUX

![item 11124](classification-review-assets/item-11124.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.89

## Odessa Poissonnier (`odessa-poissonnier`)

### 1. ROULEAUX IMPERIAUX HOMARD ET CREVETTE

![item 10988](classification-review-assets/item-10988.jpg)

- **Category:** Fish & Seafood > Shrimp (FR: Poissons et fruits de mer > Crevette)
- **How classified:** rule (`shrimp`)
- **Price:** 0.00 $ · as printed: “15998/4.00”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 10
- **Details:** OCR/extraction confidence: 0.74 · other printed prices: 1.00

### 2. ÎLES-DE-LA-MADELEINE | MAGDALEN ISLANDS

![item 10985](classification-review-assets/item-10985.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** store-prior
- **Price:** 69.99 $ · as printed: “69.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 8
- **Details:** OCR/extraction confidence: 0.89 · other printed prices: 15.42

### 3. QUÉBEC | QUEBEC

![item 10976](classification-review-assets/item-10976.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** store-prior
- **Price:** 32.99 $ · as printed: “32.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 5
- **Details:** OCR/extraction confidence: 0.71

### 4. FILET DE TILAPIA 7/9 7/9 TILAPIA FILLET

![item 10968](classification-review-assets/item-10968.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 24.23 $ · as printed: “24.23”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 2
- **Details:** OCR/extraction confidence: 0.91 · other printed prices: 10.99

### 5. L'ENSEMBLE D'OUVERTURE À HUÎTRES

![item 10974](classification-review-assets/item-10974.jpg)

- **Category:** Fish & Seafood > Shellfish (FR: Poissons et fruits de mer > Crustacés)
- **How classified:** rule (`shellfish`)
- **Price:** 29.99 $ · as printed: “29.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 4
- **Details:** OCR/extraction confidence: 0.90

### 6. SEA-RAY INDE

![item 10982](classification-review-assets/item-10982.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** store-prior
- **Price:** 26.99 $ · as printed: “26.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 7
- **Details:** OCR/extraction confidence: 0.78

### 7. INDONESIE | INDONESIA

![item 10978](classification-review-assets/item-10978.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** store-prior
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 6
- **Details:** OCR/extraction confidence: 0.86 · other printed prices: 26.43

### 8. QUÉBEC | QUEBEC

![item 10984](classification-review-assets/item-10984.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** store-prior
- **Price:** 9.99 $ · as printed: “9.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 8
- **Details:** OCR/extraction confidence: 0.91

### 9. PETIT COUTEAU À HUÎTRE

![item 10975](classification-review-assets/item-10975.jpg)

- **Category:** Fish & Seafood > Shellfish (FR: Poissons et fruits de mer > Crustacés)
- **How classified:** rule (`shellfish`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 4
- **Details:** OCR/extraction confidence: 0.89

### 10. CAVIAR DE LOMPE ROUGE OU NOIR

![item 10995](classification-review-assets/item-10995.jpg)

- **Category:** Fish & Seafood > Seafood Appetizers (FR: Poissons et fruits de mer > Hors-d'œuvre aux produits de la mer)
- **How classified:** rule (`seafood-appetizers`)
- **Price:** 10.99 $ · as printed: “10.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 12
- **Details:** OCR/extraction confidence: 0.84

## Pharmaprix (`pharmaprix`)

### 1. ESTROVEN Produits pour la ménopause

![item 5069](http://f.wishabi.net/page_items/436043536/1790796937/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 24.99 $ · as printed: “24.99”
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** brand: Estroven · OCR/extraction confidence: 1.00

### 2. OLAY TOTAL EFFECTS Nettoyants pour le visage (150 mL), WHIP ou REGENERIST hydratants faciaux Produits sélectionnés

![item 5128](http://f.wishabi.net/page_items/436041387/1790796900/extra_large.jpg)

- **Category:** Household > Cleaning & Laundry (FR: Maison > Entretien et lessive)
- **How classified:** rule (`household-cleaning`)
- **Price:** —
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** OCR/extraction confidence: 1.00

### 3. NUTELLA Tartinade de noisettes ou beurre d'arachide

![item 5005](http://f.wishabi.net/page_items/436040321/1790796924/extra_large.jpg)

- **Category:** Pantry > Honey, Syrups & Spreads (FR: Produits du garde-manger > Miel, sirops et tartinades)
- **How classified:** rule (`specific-nut-butters`)
- **Price:** 9.29 $ · as printed: “9.29”
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** brand: Nutella · OCR/extraction confidence: 1.00

### 4. PC Frozen Vegetables

![item 5139](http://f.wishabi.net/page_items/436040307/1790796913/extra_large.jpg)

- **Category:** Frozen Food > Frozen Fruit & Vegetables (FR: Produits surgelés > Fruits et légumes surgelés)
- **How classified:** frozen-remap (`vegetables`)
- **Price:** 4.49 $ · as printed: “4.49”
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** brand: PC · OCR/extraction confidence: 1.00

### 5. Étape 1: Enregistrer ce code-barres pour le scanner en magasin ou Utilisez le code en ligne chez pharmaprix.ca OCFAM20

![item 5509](http://f.wishabi.net/page_items/436747405/1791385520/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-13 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 6. ONE4ALL MERCI BEAUCOUP Carte-cadeau

![item 5294](http://f.wishabi.net/page_items/436041434/1790796908/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 10.00 $ · as printed: “10.0”
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** brand: One4All · OCR/extraction confidence: 1.00

### 7. MUCINEX Comprimés pour la congestion bronchique

![item 4981](http://f.wishabi.net/page_items/436042124/1790796910/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 25.99 $ · as printed: “25.99”
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** brand: Mucinex · OCR/extraction confidence: 1.00

### 8. PC Frappés de substitut de repas ultra

![item 5070](http://f.wishabi.net/page_items/436043530/1790796932/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 25.00 $ · as printed: “25.0”
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** OCR/extraction confidence: 1.00

### 9. LIFE BRAND Chaussettes pour personnes atteintes du diabète

![item 5209](http://f.wishabi.net/page_items/436043086/1790796942/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 20.00 $ · as printed: “20.0”
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** brand: Life Brand · OCR/extraction confidence: 1.00

### 10. BECEL Margarine (400 g - 454 g) or SAPUTO Mozzarella Cheese (300 g - 340 g)

![item 5007](http://f.wishabi.net/page_items/436044801/1790796928/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 5.00 $ · as printed: “5.0”
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** OCR/extraction confidence: 1.00

## Provigo (`provigo`)

### 1. MAGRET DE CANARD | DUCK BREAST MAGRET

![item 953](https://f.wishabi.net/page_pdf_images/24242916/a63f449c-bdd8-11f1-8135-964e96f5df87/x_large)

- **Category:** Meat > Game Meat, Offals & Fowl (FR: Viande > Viande exotique)
- **How classified:** rule (`game-offal`)
- **Price:** 17.00 $ · as printed: “17.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 20106206_KG · OCR/extraction confidence: 1.00 · “37,48/KG”

### 2. FRAMBOISES | RASPBERRIES, 170 G

![item 811](https://f.wishabi.net/page_pdf_images/24242916/94ab6e0e-bdd8-11f1-8135-964e96f5df87/x_large)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 4.00 $ · as printed: “4.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 20128938001_EA · OCR/extraction confidence: 1.00 · “PRODUIT DU MEXIQUE OU DU CANADA”

### 3. OKA, 190 G

![item 904](https://f.wishabi.net/page_items/436272686/1790899167/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 9.00 $ · as printed: “9.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: OKA · SKU: 21690170_EA · OCR/extraction confidence: 1.00

### 4. GROSSES CREVETTES BLANCHES DU PACIFIQUE PC | PC® PACIFIC LARGE WHITE SHRIMP, 31-40 PAR LB, 400 G

![item 834](https://f.wishabi.net/page_items/437038958/1791569037/extra_large.jpg)

- **Category:** Fish & Seafood > Shrimp (FR: Poissons et fruits de mer > Crevette)
- **How classified:** rule (`shrimp`)
- **Price:** 9.00 $ · as printed: “9.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: President's Choice · SKU: 20789931_EA · OCR/extraction confidence: 1.00 · “CERTAIN VARIETIES, SURGELÉES”

### 5. OÎKOS® PRO™, 650 G

![item 992](https://f.wishabi.net/page_items/436272662/1790899173/extra_large.jpg)

- **Category:** Dairy & Eggs > Yogurt (FR: Produits laitiers et œufs > Yogourt)
- **How classified:** rule (`yogurt`)
- **Price:** 7.50 $ · as printed: “7.50”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Oikos · SKU: 21757458_EA · OCR/extraction confidence: 1.00 · “Certaines variétés”

### 6. COURONNE DE BROCOLI | BROCCOLI CROWN

![item 931](https://f.wishabi.net/page_items/436272577/1790899177/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.50 $ · as printed: “1.50”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 21121560001_EA · OCR/extraction confidence: 1.00 · “PRODUIT DES É.-U. OU MEXIQUE”

### 7. ACTIVIA, 12 X 100 G

![item 872](https://f.wishabi.net/page_items/436280005/1790899176/extra_large.jpg)

- **Category:** Dairy & Eggs > Yogurt (FR: Produits laitiers et œufs > Yogourt)
- **How classified:** rule (`yogurt`)
- **Price:** 7.00 $ · as printed: “7.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 20303412001_EA · OCR/extraction confidence: 1.00 · “certaines variétés”

### 8. NETTOYANTS TOUT USAGE LYSOL, 650 ML, NETTOYANT TOUT USAGE, 1,2 L, NETTOYANTS POUR SALLES DE BAIN, 538-680 G/950 ML, NETTOYANT POUR CUVETTES, 710 ML OU DÉGRAISSANT PUISSANT, 650 ML | LYSOL ALL-PURPOSE CLEANERS, MULTI SURFACE CLEANER, BATHROOM CLEANERS

![item 965](https://f.wishabi.net/page_pdf_images/24242919/9bb1e91c-bdd8-11f1-af65-2af86f0adfcd/x_large)

- **Category:** Household > Cleaning & Laundry (FR: Maison > Entretien et lessive)
- **How classified:** rule (`household-cleaning`)
- **Price:** 10.00 $ · as printed: “10.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Lysol · SKU: 20309873002_EA · OCR/extraction confidence: 1.00 · “TOILET BOWL CLEANER OR POWER DEGREASER CERTAINES VARIÉTÉS”

### 9. SAUCE AUX CANNEBERGES OCEAN SPRAY | OCEAN SPRAY CRANBERRY SAUCE, 348 ML

![item 796](https://f.wishabi.net/page_pdf_images/24242919/93c40c94-bdd8-11f1-af65-2af86f0adfcd/x_large)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.50 $ · as printed: “2.50”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Ocean Spray · SKU: 20022893001_EA · OCR/extraction confidence: 1.00 · “CERTAINES VARIÉTÉS”

### 10. TULIPES D'AUTOMNE | FALL TULIPS, 15 TIGES

![item 863](https://f.wishabi.net/page_pdf_images/24242916/9ca6ee76-bdd8-11f1-8135-964e96f5df87/x_large)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 18.00 $ · as printed: “18.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 20547693_EA · OCR/extraction confidence: 1.00 · “TAXES APPLICABLES”

## Rachelle-Béry (`rachelle-bery`)

### 1. En savoir plus

![item 5595](http://f.wishabi.net/page_items/436319976/1790917640/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 2. BIO EAU D'ÉRABLE PÉTILLANTE BIOLOGIQUE MAPLE 3

![item 5587](http://f.wishabi.net/page_items/436247073/1790917637/extra_large.jpg)

- **Category:** Drinks > Water (FR: Boissons > Eau)
- **How classified:** rule (`water`)
- **Price:** 5.00 $ · as printed: “5.0”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: MAPLE 3 · OCR/extraction confidence: 1.00

### 3. GÉLIFIÉS MULTI-VITAMINES COMPLIMENTS

![item 5566](http://f.wishabi.net/page_items/436247058/1790917639/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 17.99 $ · as printed: “17.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Compliments · OCR/extraction confidence: 1.00

### 4. Je m'abonne

![item 5543](http://f.wishabi.net/page_items/436319958/1790917643/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 5. SPRAY MAL DE GORGE A. VOGEL

![item 5549](http://f.wishabi.net/page_items/436247034/1790917636/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 15.99 $ · as printed: “15.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: A. VOGEL · OCR/extraction confidence: 1.00

### 6. LAIT BIOLOGIQUE NUTRINOR

![item 5550](http://f.wishabi.net/page_items/436247035/1790917637/extra_large.jpg)

- **Category:** Dairy & Eggs > Milk & Cream (FR: Produits laitiers et œufs > Lait et crème)
- **How classified:** rule (`milk-cream`)
- **Price:** 6.49 $ · as printed: “6.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: NUTRINOR · OCR/extraction confidence: 1.00

### 7. DRAINAFLORE PLUS SUPER DIET

![item 5516](http://f.wishabi.net/page_items/436249687/1790917720/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 46.99 $ · as printed: “46.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: SUPERDIET · OCR/extraction confidence: 1.00

### 8. SPRAY MAL DE GORGE A. VOGEL

![item 5513](http://f.wishabi.net/page_items/436249697/1790917726/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 15.99 $ · as printed: “15.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: A.Vogel · OCR/extraction confidence: 1.00

### 9. SAUMON FUMÉ SURGELÉ FUMOIRS GOSSELIN

![item 5564](http://f.wishabi.net/page_items/436247051/1790917640/extra_large.jpg)

- **Category:** Frozen Food > Frozen Meat and Seafood (FR: Produits surgelés > Viande et fruits de mer surgelés)
- **How classified:** frozen-remap (`smoked-fish`)
- **Price:** 9.99 $ · as printed: “9.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: FUMOIRS GOSSELIN · OCR/extraction confidence: 1.00

### 10. SIMILI-VIANDE HACHÉ OU STEAK À BASE DE PLANTES BEYOND MEAT

![item 5557](http://f.wishabi.net/page_items/436247054/1790917642/extra_large.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Beyond Meat · OCR/extraction confidence: 1.00

## Shop Santé (`shop-sante`)

### 1. HUILE DE CAMELINE EN VAPORISATEUR PRET. TSF

![item 10584](classification-review-assets/item-10584.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 9.94 $ · as printed: “9.94”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 3
- **Details:** OCR/extraction confidence: 0.59

### 2. BOISSON PROTÉINÉE LEAN BODY LABRADA | 500 ML

![item 10608](classification-review-assets/item-10608.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 5.49 $ · as printed: “5.49”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 16
- **Details:** OCR/extraction confidence: 0.99

### 3. CONTRÔLE MÉTABOLIQUE AKTIV | 120 CAPSULES

![item 10611](classification-review-assets/item-10611.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 49.99 $ · as printed: “49.99”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 17
- **Details:** OCR/extraction confidence: 0.91

### 4. VANDAL PRE-WORK (tig VNDL PROJECT

![item 10599](classification-review-assets/item-10599.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 39.99 $ · as printed: “39.99”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 14
- **Details:** OCR/extraction confidence: 0.95

### 5. BOUCHÉES PROTÉINÉES PROBITES | 1006

![item 10596](classification-review-assets/item-10596.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 12
- **Details:** OCR/extraction confidence: 0.97

### 6. THAVAGE PRE-WORKOUT CBUM

![item 10586](classification-review-assets/item-10586.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 49.99 $ · as printed: “49.99”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 6
- **Details:** OCR/extraction confidence: 0.97

### 7. LOADED PROTEIN | RYSE

![item 10597](classification-review-assets/item-10597.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 79.99 $ · as printed: “79.99”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 13
- **Details:** OCR/extraction confidence: 0.91

### 8. OMEGA 3 EPA-DHA | XPN

![item 10593](classification-review-assets/item-10593.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 40.79 $ · as printed: “40.79”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 10
- **Details:** OCR/extraction confidence: 0.99

### 9. CRÉATINE MONOHYDRATE

![item 10601](classification-review-assets/item-10601.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 22.99 $ · as printed: “22.99”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 14
- **Details:** OCR/extraction confidence: 0.99

### 10. SOURCE 7 PROTÉINE RULE ONE

![item 10613](classification-review-assets/item-10613.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 39.00 $ · as printed: “39”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 18
- **Details:** OCR/extraction confidence: 0.76

## Super C (`super-c`)

### 1. poires Rocha | Rocha pears

![item 6989](http://f.wishabi.net/page_items/436265017/1790897778/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 9.99 $ · as printed: “9.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 2. AROMATISANT D'EAU MIO | MIO WATER ENHANCER

![item 6795](http://f.wishabi.net/page_items/436856792/1791480276/extra_large.jpg)

- **Category:** Drinks > Water (FR: Boissons > Eau)
- **How classified:** rule (`water`)
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 3. pommes de terre Cavendish | Cavendish potatoes

![item 6908](http://f.wishabi.net/page_items/436072483/1790863959/extra_large.jpg)

- **Category:** Frozen Food > Frozen Appetizers & Snacks (FR: Produits surgelés > Entrées et collations surgelés)
- **How classified:** rule (`specific-frozen-fries-brands`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 4. BIÈRE CORONA EXTRA, MODELO ESPECIAL, HEINEKEN | BEER

![item 6666](http://f.wishabi.net/page_items/436856712/1791480277/extra_large.jpg)

- **Category:** Beer & Wine > Beer (FR: Bières et vins > Bières)
- **How classified:** rule (`beer`)
- **Price:** 77.48 $ · as printed: “77.48”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 5. sirop de maïs Crown | Crown corn syrup

![item 6804](http://f.wishabi.net/page_items/436856906/1791548848/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 6. mini concombres | mini cucumbers

![item 7124](http://f.wishabi.net/page_items/436072517/1790803393/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.88 $ · as printed: “2.88”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 7. cretons Norel | Norel cretons

![item 7022](http://f.wishabi.net/page_items/436072639/1790803387/extra_large.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 8. PÂTÉ À SANDWICH PARIS PÂTÉ | PARIS PÂTÉ SANDWICH SPREAD

![item 6840](http://f.wishabi.net/page_items/436856815/1791480281/extra_large.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 9. Chez Super C il y a pleine de façons d'économiser nos recrues

![item 6650](http://f.wishabi.net/page_items/436856950/1791480273/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 10. SIROP D'ÉRABLE IRRÉSISTIBLE | IRRÉSISTIBLE MAPLE SYRUP

![item 6690](http://f.wishabi.net/page_items/436856688/1791480273/extra_large.jpg)

- **Category:** Pantry > Honey, Syrups & Spreads (FR: Produits du garde-manger > Miel, sirops et tartinades)
- **How classified:** rule (`honey-spreads`)
- **Price:** 5.55 $ · as printed: “5.55”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

## T&T Supermarché (`t-t`)

### 1. Noixdecoco Thailande

![item 10652](classification-review-assets/item-10652.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 0.48 $ · as printed: “0.48”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 2. Pousses bokchoyde shanghai

![item 10631](classification-review-assets/item-10631.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.68 $ · as printed: “3.68”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 3. Dan-DPaknoix Dan-DPak果仁

![item 10622](classification-review-assets/item-10622.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 4.97 $ · as printed: “4.97”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 4. GoldenKing geleed'herbe enconserve

![item 10711](classification-review-assets/item-10711.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.69 $ · as printed: “2.69”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

### 5. Ailettede poulet (congelee)

![item 10649](classification-review-assets/item-10649.jpg)

- **Category:** Frozen Food > Frozen Meat and Seafood (FR: Produits surgelés > Viande et fruits de mer surgelés)
- **How classified:** frozen-remap (`chicken-turkey`)
- **Price:** 0.66 $ · as printed: “0.66”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 6. Cotedeporc rotieala cajun

![item 10703](classification-review-assets/item-10703.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 11.49 $ · as printed: “11.49”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 7. laniereepicee style changsha/ tofusechepuant

![item 10684](classification-review-assets/item-10684.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 8.00 $ · as printed: “8.00”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 8. Pilondinde fumerabais

![item 10705](classification-review-assets/item-10705.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 9. Lotteboisson milkis Ich

![item 10664](classification-review-assets/item-10664.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 0.60 $ · as printed: “0.60”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.98

### 10. Hereford boeufsale

![item 10722](classification-review-assets/item-10722.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.97 $ · as printed: “1.97”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 6
- **Details:** OCR/extraction confidence: 0.96

## Uniprix (`uniprix`)

### 1. Annabelle Maquillage sélectionné

![item 5655](http://f.wishabi.net/page_items/434320790/1789813529/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Annabelle · OCR/extraction confidence: 1.00

### 2. DEGREE Antisudorifiques ou déodorants pour le corps sélectionnés

![item 5606](http://f.wishabi.net/page_items/434312418/1789813191/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 8.49 $ · as printed: “8.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Degree · OCR/extraction confidence: 1.00

### 3. PEPTO-BISMOL Bismuth, 350 ml, 480 ml, 48

![item 5675](http://f.wishabi.net/page_items/434320659/1789813536/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 13.99 $ · as printed: “13.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Pepto-Bismol · OCR/extraction confidence: 1.00

### 4. SCOTTIES Mouchoirs Tissues Boîtes Boxes, 9

![item 5776](http://f.wishabi.net/page_items/434320383/1789813532/extra_large.jpg)

- **Category:** Household > Paper & Storage (FR: Maison > Papier et rangement)
- **How classified:** rule (`household-paper`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Scotties · OCR/extraction confidence: 1.00

### 5. Ibuprofène/Ibuprofen 200 mg, 24

![item 5673](http://f.wishabi.net/page_items/434320737/1789813529/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Option + · OCR/extraction confidence: 1.00

### 6. RICOLA Pastilles sélectionnées

![item 5651](http://f.wishabi.net/page_items/434312464/1789813197/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Ricola · OCR/extraction confidence: 1.00

### 7. PHILIPS, CONAIR Produits sélectionnés/ Selected products

![item 5801](http://f.wishabi.net/page_items/434320494/1789813542/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: PHILIPS | CONAIR · OCR/extraction confidence: 1.00

### 8. CHLORASEPTIC Vaporisateurs sélectionnés/ Selected sprays

![item 5693](http://f.wishabi.net/page_items/434320666/1789813541/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 8.79 $ · as printed: “8.79”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Chloraseptic · OCR/extraction confidence: 1.00

### 9. SENOKOT Laxatifs naturels sélectionnés/ Selected natural laxatives

![item 5817](http://f.wishabi.net/page_items/434320646/1789813529/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 16.99 $ · as printed: “16.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Senokot® · OCR/extraction confidence: 1.00

### 10. VITALUX ADVANCED Suppléments pour la santé des yeux sélectionnés

![item 5791](http://f.wishabi.net/page_items/434320714/1789813531/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Vitalux · OCR/extraction confidence: 1.00

## Walmart (`walmart`)

### 1. Shampooing ou revitalisant Density Booster Hair Expertise de L'Oréal Paris

![item 1223](https://f.wishabi.net/page_pdf_images/24238150/faf5c254-bd47-11f1-abd9-9a298766b113/x_large)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 8.97 $ · as printed: “8.97”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: L'oreal paris · SKU: 431LX4S0TQ4Y · OCR/extraction confidence: 1.00 · “Chac. 150 - 200 ml. N° 50772967.”

### 2. Tortillas POM

![item 1195](https://f.wishabi.net/page_pdf_images/24238105/fa036b76-bd47-11f1-aa3c-aac67d9fbd3f/x_large)

- **Category:** Bakery > Wraps, Flatbread & Pizza Crust (FR: Boulangerie > Roulés, pains plats et croûtes à pizza)
- **How classified:** rule (`wraps-flatbread`)
- **Price:** 2.68 $ · as printed: “2.68”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: POM · SKU: 6000197208321 · OCR/extraction confidence: 1.00 · “18 cm (7 po) Paq. de 10. Variétés sélectionnées. 340 g. #8111544”

### 3. Ens. 2 pièces PL Kids pour tout-petits garçons

![item 1419](https://f.wishabi.net/page_pdf_images/24275210/59fbf35c-c353-11f1-a84c-facdb62eeaa5/x_large)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 14.99 $ · as printed: “14.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 6WP3BH8Z4HM5 · OCR/extraction confidence: 1.00 · “Sold by Marketplace Seller and Fullfilled by Walmart”

### 4. Emb. varié de nourriture humide Gems de Fancy Feast pour chats Purina

![item 1240](https://f.wishabi.net/page_pdf_images/24238136/fd06971c-bd47-11f1-a0b4-c61bfd1c88ec/x_large)

- **Category:** Pet > Pet Food (FR: Animaux > Nourriture pour animaux)
- **How classified:** rule (`pet`)
- **Price:** 15.93 $ · as printed: “15.93”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Purina · SKU: 2HYWX9IZIK39 · OCR/extraction confidence: 1.00 · “16 x 57 g. Le paq. Variétés sélectionnées. N° 51027938.”

### 5. Café moulu Verona ou Pike Place de Starbucks

![item 1042](https://f.wishabi.net/page_pdf_images/24270832/83d2fca6-c2a5-11f1-ae53-7e6ee4500018/x_large)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** 30.97 $ · as printed: “30.97”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Starbucks · SKU: 6000202651460 · OCR/extraction confidence: 1.00 · “Chac. 907 g. N° 31138750.”

### 6. Gâteries à lécher PurrPops de Bonkers d'Halloween pour chats

![item 1500](https://f.wishabi.net/page_pdf_images/24264120/7151aa1c-c1cb-11f1-81f1-9ad89418c142/x_large)

- **Category:** Pet > Pet Food (FR: Animaux > Nourriture pour animaux)
- **How classified:** rule (`pet`)
- **Price:** 1.98 $ · as printed: “1.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: BONKERS · SKU: 3D8JHWB4X0DI · OCR/extraction confidence: 1.00 · “Chac. 5,6 g. N° 51108747.”

### 7. FR_1242x210_Flash Deals 40-3

![item 1327](https://f.wishabi.net/page_items/436882005/1791496275/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 8. Carottes rouges indiennes

![item 1056](https://f.wishabi.net/page_pdf_images/24270608/13b0f900-c2a0-11f1-8cd7-c246eb8beba2/x_large)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.98 $ · as printed: “1.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 6000208405880 · OCR/extraction confidence: 1.00 · “Chac. Produit de Chine. N° 50600786.”

### 9. Boîtes de mouchoirs Scotties 2 ou 3 épaisseurs

![item 1517](https://f.wishabi.net/page_pdf_images/24238111/f8091852-bd47-11f1-8856-f6b3ce06635b/x_large)

- **Category:** Household > Paper & Storage (FR: Maison > Papier et rangement)
- **How classified:** rule (`household-paper`)
- **Price:** 19.97 $ · as printed: “19.97”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Scotties · SKU: 10185446 · OCR/extraction confidence: 1.00 · “Chac. Variétés sélectionnées. N° 418728.”

### 10. Café glacé Starbucks

![item 1015](https://f.wishabi.net/page_pdf_images/24238105/f034e4e4-bd47-11f1-aa3c-aac67d9fbd3f/x_large)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** 6.98 $ · as printed: “6.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Starbucks · SKU: 6000201072081 · OCR/extraction confidence: 1.00 · “Chac. Variétés sélectionnées. 1,18 l - 1,42 l. N°50438981”

## Wholesale Club (`wholesale-club`)

### 1. BŒUF SÉCHÉ JUMBO SUCRÉ ET ÉPICÉ JACK LINK’S

![item 11274](classification-review-assets/item-11274.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 30.99 $ · as printed: “30.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 17
- **Details:** OCR/extraction confidence: 0.88 · other printed prices: 30.99

### 2. PURE BASMATI . BASMATI PUR

![item 11257](classification-review-assets/item-11257.jpg)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 16.99 $ · as printed: “16.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 15
- **Details:** OCR/extraction confidence: 0.97

### 3. CHOUX DE BRUXELLES SANS NOM® NATURELLEMENT IMPARFAITS™ PRODUIT DES PAYS-BAS OU DES E.-U

![item 11225](classification-review-assets/item-11225.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 6.49 $ · as printed: “6.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 12
- **Details:** OCR/extraction confidence: 0.95

### 4. USTENSILES JETABLES TOUCH CERTAINES VARIÉTÉS

![item 11289](classification-review-assets/item-11289.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 39.99 $ · as printed: “39.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 19
- **Details:** OCR/extraction confidence: 0.95 · other printed prices: 21.99

### 5. FORMAT INDIVIDUELLE SKITTLES Le CERTAINES VARIÉTÉS

![item 11209](classification-review-assets/item-11209.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 39.99 $ · as printed: “39.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 10
- **Details:** OCR/extraction confidence: 0.97

### 6. WRIGLEY'S OU EXCEL MINTS CERTAINES VARIÉTÉS

![item 11268](classification-review-assets/item-11268.jpg)

- **Category:** Fruits & Vegetables > Herbs (FR: Fruits et légumes > Fines herbes)
- **How classified:** rule (`herbs-fresh`)
- **Price:** 27.99 $ · as printed: “27.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 17
- **Details:** OCR/extraction confidence: 0.88 · other printed prices: 154.49

### 7. PREPAREAU CANADA

![item 11237](classification-review-assets/item-11237.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.98 $ · as printed: “3.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 13
- **Details:** OCR/extraction confidence: 0.97

### 8. 4 BARRES DE CHOCOLAT OU CONFISERIES GRAND FORMAT HERSHEY'S, OH HENRY! OU REESE'S CERTAINES VARIETES, 16-24 UN. CHOCOLATE OR CANDY

![item 11178](classification-review-assets/item-11178.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 14.99 $ · as printed: “14.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.96

### 9. BARRES DE CHOCOLAT FORMAT INDIVIDUEL CERTAINES VARIETES,48 UN. CHOCOLATE SINGLE SIZE

![item 11199](classification-review-assets/item-11199.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 58.99 $ · as printed: “58.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 9
- **Details:** OCR/extraction confidence: 0.94

### 10. PILONS DE PS nd TR POULET HALAL | | MINA

![item 11259](classification-review-assets/item-11259.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 46.99 $ · as printed: “46.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 15
- **Details:** OCR/extraction confidence: 0.97

## Épicerie PA Nature (`pa-nature`)

### 1. JUS OASIS

![item 11498](classification-review-assets/item-11498.jpg)

- **Category:** Drinks > Juice (FR: Boissons > Jus)
- **How classified:** rule (`juice`)
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-12 → 2026-10-25 · flyer page 2
- **Details:** OCR/extraction confidence: 0.85

### 2. HORE PROTEIN ADPASUGAR

![item 11499](classification-review-assets/item-11499.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 50.50 $ · as printed: “50.50”
- **Flyer validity:** 2026-10-12 → 2026-10-25 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 3. BLANCS/BIOLOGIQUES | PT

![item 11497](classification-review-assets/item-11497.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-12 → 2026-10-25 · flyer page 1
- **Details:** OCR/extraction confidence: 0.83
