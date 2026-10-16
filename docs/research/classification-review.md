# Classification review — PC Express taxonomy

Generated from `data/grocery.db` (15060 items, 12978 classified = 86.2%). 10 random items per store (seed 20261015), each with its picture, stored details and assigned category.

Taxonomy: PC Express departments/subcategories as documented in [product-categories.md](product-categories.md), minus the attribute-based *Natural and Organic* department, plus Baby / Pet / Household / Health & Beauty buckets for non-food flyer items. Method `rule` = a named keyword rule fired; `frozen-remap` = fresh hit remapped by a frozen marker; `store-prior` = no rule matched, fell back to the store's trade.

| Store | Items | Classified |
|---|---:|---:|
| Akhavan | 19 | 84% |
| Aliments Merci | 29 | 62% |
| Avril Supermarché Santé | 183 | 79% |
| Brunet | 596 | 100% |
| Bulk Barn | 9 | 100% |
| Canadian Tire | 799 | 25% |
| Coop Alentour | 33 | 85% |
| Costco Wholesale | 85 | 15% |
| Euro Marché | 99 | 85% |
| Familiprix | 968 | 100% |
| Fruiterie Valmont | 54 | 54% |
| Fruits & Légumes 3 Saisons | 6 | 50% |
| Giant Tiger | 53 | 83% |
| H Marché | 27 | 93% |
| IGA | 827 | 93% |
| IGA Express / Mini | 827 | 93% |
| IGA Extra | 852 | 92% |
| Jean Coutu | 730 | 100% |
| Kim Phat | 303 | 92% |
| L'Intermarché | 149 | 91% |
| L'intermarché Palumbo | 8 | 100% |
| La Moisson Supermarché Santé | 58 | 88% |
| Le Marché Esposito | 84 | 86% |
| Le Monde au Naturel | 70 | 100% |
| Les Marchés Tau | 37 | 51% |
| Les Marchés Tradition | 157 | 83% |
| M&M Food Market | 133 | 100% |
| Marche PA | 194 | 91% |
| Marché Adonis | 373 | 93% |
| Marché Ami | 167 | 96% |
| Marché Andes | 4 | 100% |
| Marché Axep | 151 | 90% |
| Marché BKR | 14 | 50% |
| Marché Bonanza | 30 | 17% |
| Marché Bonichoix | 144 | 87% |
| Marché C&T | 92 | 80% |
| Marché Frutta Si | 27 | 93% |
| Marché Fu Tai | 83 | 80% |
| Marché Korea | 273 | 83% |
| Marché Lian Tai | 222 | 88% |
| Marché Newon | 180 | 80% |
| Marché Richelieu | 214 | 96% |
| Marché Sheng Tai | 88 | 82% |
| Marché Sultan | 29 | 24% |
| Maxi | 581 | 96% |
| Mayrand Food Group | 37 | 24% |
| Metro | 840 | 87% |
| Metro Plus | 840 | 87% |
| Milano Fruiterie | 15 | 67% |
| Odessa Poissonnier | 28 | 100% |
| Pharmaprix | 788 | 100% |
| Provigo | 377 | 93% |
| Rachelle-Béry | 140 | 85% |
| Shop Santé | 32 | 28% |
| Super C | 501 | 91% |
| T&T Supermarché | 153 | 44% |
| Uniprix | 279 | 100% |
| Walmart | 785 | 77% |
| Wholesale Club | 181 | 75% |
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

### 1. Tortillas fraîches

![item 2571](http://f.wishabi.net/page_items/435976781/1790751808/extra_large.jpg)

- **Category:** Bakery > Wraps, Flatbread & Pizza Crust (FR: Boulangerie > Roulés, pains plats et croûtes à pizza)
- **How classified:** rule (`wraps-flatbread`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: NUTRI-DÉLICE · OCR/extraction confidence: 1.00

### 2. café aux champignons adaptogènes

![item 11612](http://f.wishabi.net/page_items/436650391/1791359770/extra_large.jpg)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: MUSHUP CAFÉ · OCR/extraction confidence: 1.00

### 3. La Milanaise farine blanche tout usage non blanchie bio

![item 11660](http://f.wishabi.net/page_items/436650374/1791359767/extra_large.jpg)

- **Category:** Pantry > Baking Essentials (FR: Produits du garde-manger > Essentiels de cuisson)
- **How classified:** rule (`baking`)
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: La Milanaise · OCR/extraction confidence: 1.00

### 4. Sur la marque Botanica

![item 2526](http://f.wishabi.net/page_items/435976778/1790751816/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Botanica · OCR/extraction confidence: 1.00

### 5. Pommes Honeycrisp ou Royal Gala bios

![item 11626](http://f.wishabi.net/page_items/437176841/1791910440/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: QUÉBEC · OCR/extraction confidence: 1.00

### 6. Brine Co. cornichons

![item 2558](http://f.wishabi.net/page_items/435976735/1790751808/extra_large.jpg)

- **Category:** Pantry > Canned & Pickled (FR: Produits du garde-manger > Produits en conserve et marinés)
- **How classified:** rule (`canned-pickled`)
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Brine Co. · OCR/extraction confidence: 1.00

### 7. Vita Coco lait de coco bio

![item 2527](http://f.wishabi.net/page_items/435976757/1790751807/extra_large.jpg)

- **Category:** Pantry > Canned & Pickled (FR: Produits du garde-manger > Produits en conserve et marinés)
- **How classified:** rule (`specific-coconut-milk`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Vita Coco · OCR/extraction confidence: 1.00

### 8. Freeyumm craquelins

![item 11653](http://f.wishabi.net/page_items/436650387/1791359768/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Crackers & Cookies (FR: Grignotines, croustilles et friandises > Craquelins et biscuits)
- **How classified:** rule (`crackers-cookies`)
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: FREEYUMM · OCR/extraction confidence: 1.00

### 9. mélange à latte superaliment caramel salé bio

![item 2581](http://f.wishabi.net/page_items/436616905/1791311030/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Blume · OCR/extraction confidence: 1.00

### 10. Savon à mains

![item 2529](http://f.wishabi.net/page_items/435976754/1790751808/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 5.49 $ · as printed: “5.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Nature Clean · OCR/extraction confidence: 1.00

## Brunet (`brunet`)

### 1. MOI

![item 8597](http://f.wishabi.net/page_items/436537869/1791230730/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 2. ELASTOPLAST Pansements sélectionnés

![item 8481](http://f.wishabi.net/page_items/436305907/1790938344/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 5.19 $ · as printed: “5.19”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Elastoplast · OCR/extraction confidence: 1.00

### 3. EOS Produits sélectionnés

![item 8514](http://f.wishabi.net/page_items/436305969/1790938339/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: EOS · OCR/extraction confidence: 1.00

### 4. COLGATE Produits dentaires sélectionnés

![item 8638](http://f.wishabi.net/page_items/435452498/1790327192/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 9.49 $ · as printed: “9.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Colgate · OCR/extraction confidence: 1.00

### 5. AVÈNE Produits sélectionnés

![item 8418](http://f.wishabi.net/page_items/436306024/1790938334/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Avène · OCR/extraction confidence: 1.00

### 6. DUPUIS Gamme complete

![item 8262](http://f.wishabi.net/page_items/436253973/1790878595/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 26.99 $ · as printed: “26.99”
- **Flyer validity:** 2026-10-01 → 2026-10-14
- **Details:** brand: Dupuis · OCR/extraction confidence: 1.00

### 7. WATIER Perfection Sérum teinté révélateur d'éclat

![item 8284](http://f.wishabi.net/page_items/436253950/1790878595/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 62.00 $ · as printed: “62.0”
- **Flyer validity:** 2026-10-01 → 2026-10-14
- **Details:** brand: WATIER · OCR/extraction confidence: 1.00

### 8. CLAIROL Gamme complète

![item 8239](http://f.wishabi.net/page_items/436253971/1790878593/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 9.99 $ · as printed: “9.99”
- **Flyer validity:** 2026-10-01 → 2026-10-14
- **Details:** brand: Clairol · OCR/extraction confidence: 1.00

### 9. BUCKLEY'S Produits sélectionnés pour le soulagement complet des symptômes du rhume, de la grippe et de la toux

![item 8788](http://f.wishabi.net/page_items/435433232/1790295857/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 8.29 $ · as printed: “8.29”
- **Flyer validity:** 2026-10-08 → 2026-10-21
- **Details:** brand: Buckley's · OCR/extraction confidence: 1.00

### 10. SPONGE TOWELS Essuie-tout

![item 8688](http://f.wishabi.net/page_items/435452350/1790327186/extra_large.jpg)

- **Category:** Household > Cleaning & Laundry (FR: Maison > Entretien et lessive)
- **How classified:** rule (`household-cleaning`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Sponge Towels · OCR/extraction confidence: 1.00

## Bulk Barn (`bulk-barn`)

### 1. Tranches de mangues sechees Non sucrees Dried Mango Slices

![item 11668](classification-review-assets/item-11668.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 3.88 $ · as printed: “3.88”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 2. Raisins secs Thompson Thompson Raisins

![item 11099](classification-review-assets/item-11099.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 1.00 $ · as printed: “1.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 3. Arachides au barbecue et aromedefumee Smokehouse BBQ Peanuts

![item 11097](classification-review-assets/item-11097.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 4. Cajous entiers Rotis asec etnon sales Whole Cashews

![item 11102](classification-review-assets/item-11102.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 2.32 $ · as printed: “2.32”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 5. Bonbons Skittles Originaux Skittles

![item 11101](classification-review-assets/item-11101.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 2.41 $ · as printed: “2.41”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 6. Gros flocons d'avoine Rolled Oats Large Fiake

![item 11100](classification-review-assets/item-11100.jpg)

- **Category:** Pantry > Cereal & Breakfast (FR: Produits du garde-manger > Céréales et petits-déjeuners)
- **How classified:** rule (`cereal-breakfast`)
- **Price:** 0.29 $ · as printed: “0.29”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 7. Jujubes super tendres Dare Super Soft Ju Jubes

![item 11098](classification-review-assets/item-11098.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 0.50 $ · as printed: “0.50”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 8. Noix melangees avec arachides Rotiesetsalees Mixed Nuts with Peanuts

![item 11670](classification-review-assets/item-11670.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 2.47 $ · as printed: “2.47”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 2.06

### 9. Friandises Reese's Pieces Originales Reese's Pieces

![item 11669](classification-review-assets/item-11669.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 2.26 $ · as printed: “2.26”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

## Canadian Tire (`canadian-tire`)

### 1. Jeu de 30 lumières étoilées orange à DEL NOMA, 10 pi. NOMA

![item 11675](http://f.wishabi.net/page_items/436898269/1791518194/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: NOMA · OCR/extraction confidence: 1.00

### 2. Produits de nettoyage et d'esthétique automobile. Certaines types.

![item 2694](http://f.wishabi.net/page_items/436182497/1790921824/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 9.34 $ · as printed: “9.34”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 3. Meuble de rangement, 2 cubes. Blanc.

![item 2819](http://f.wishabi.net/page_items/436177497/1790921788/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 49.99 $ · as printed: “49.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: CANVAS · OCR/extraction confidence: 1.00

### 4. Machine à espresso Stilosa

![item 3170](http://f.wishabi.net/page_items/436305531/1790921807/extra_large.jpg)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** 129.99 $ · as printed: “129.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 5. RABAIS 10$

![item 2662](http://f.wishabi.net/page_items/436174829/1790883109/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Castrol · OCR/extraction confidence: 1.00

### 6. Ultimate Lithium 4 AAA or Max 6 9V Alkaline Batteries

![item 3075](http://f.wishabi.net/page_items/436180165/1790921822/extra_large.jpg)

- **Category:** Household > Home Goods (FR: Maison > Articles pour la maison)
- **How classified:** rule (`household-goods`)
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 7. Certaines housses de moto et cale de roue

![item 3195](http://f.wishabi.net/page_items/436307198/1790921851/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 56.69 $ · as printed: “56.69”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 8. Tabouret de bar Canvas

![item 11717](http://f.wishabi.net/page_items/436751762/1791518193/extra_large.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 89.99 $ · as printed: “89.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: CANVAS · OCR/extraction confidence: 1.00

### 9. Ens. de clés

![item 2832](http://f.wishabi.net/page_items/436180035/1790921823/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 21.99 $ · as printed: “21.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Mastercraft · OCR/extraction confidence: 1.00

### 10. Certains ens. d'accessoires

![item 3108](http://f.wishabi.net/page_items/436180519/1790921830/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 11.98 $ · as printed: “11.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

## Coop Alentour (`coop-alentour`)

### 1. MULTI UNE PAR JOUR AVEC FER SUPRÊME

![item 10844](classification-review-assets/item-10844.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 40.89 $ · as printed: “40.89”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.90

### 2. AVOCAT BIO

![item 11743](classification-review-assets/item-11743.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 1
- **Details:** OCR/extraction confidence: 0.91

### 3. LAIT DE COCO BIO

![item 11744](classification-review-assets/item-11744.jpg)

- **Category:** Pantry > Canned & Pickled (FR: Produits du garde-manger > Produits en conserve et marinés)
- **How classified:** rule (`specific-coconut-milk`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 1
- **Details:** OCR/extraction confidence: 0.89

### 4. BEURRE DE TAHINI BIO

![item 11745](classification-review-assets/item-11745.jpg)

- **Category:** Dairy & Eggs > Butter & Spreads (FR: Produits laitiers et œufs > Beurre et tartinades)
- **How classified:** rule (`butter`)
- **Price:** 12.99 $ · as printed: “12.99”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 1
- **Details:** OCR/extraction confidence: 0.91

### 5. CÉLERI EN FEUILLE BIO > NT RTS 2

![item 10860](classification-review-assets/item-10860.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.49 $ · as printed: “2.49”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.89

### 6. POUMONS, BRONCHES ET SINUS SAINS

![item 10848](classification-review-assets/item-10848.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 23.89 $ · as printed: “23.89”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.91

### 7. CANNEBERGE BIO

![item 10861](classification-review-assets/item-10861.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 3.75 $ · as printed: “3.75”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.93

### 8. ÉCHALOTE FRANÇAISE BIO

![item 10851](classification-review-assets/item-10851.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.25 $ · as printed: “2.25”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.92

### 9. ESA KOMBUCHA SAVEURS ASSORTIES

![item 11736](classification-review-assets/item-11736.jpg)

- **Category:** Drinks > Non-alcoholic drinks (FR: Boissons > Boissons non alcoolisées)
- **How classified:** rule (`non-alcoholic`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 1
- **Details:** OCR/extraction confidence: 0.87

### 10. LEVURE NUTRITIONNELLE EN FLOCONS

![item 10850](classification-review-assets/item-10850.jpg)

- **Category:** Pantry > Baking Essentials (FR: Produits du garde-manger > Essentiels de cuisson)
- **How classified:** rule (`baking`)
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.93

## Costco Wholesale (`costco`)

### 1. Papierhygieniquea2épaisseursPurex PremiumouCashmerePremium 40×250feuilles

![item 9839](classification-review-assets/item-9839.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 21.49 $ · as printed: “21,49 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 5
- **Details:** OCR/extraction confidence: 0.85

### 2. Ensembledemitainesdecuisine Grille-paina4 tranches Cuisinart

![item 9808](classification-review-assets/item-9808.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 19.99 $ · as printed: “19,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 2
- **Details:** OCR/extraction confidence: 0.85

### 3. 10Bilion/milliards CHEWABLE/A CROQUER 14ENOESTRAINS/

![item 9874](classification-review-assets/item-9874.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 13.49 $ · as printed: “13,49 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 8
- **Details:** OCR/extraction confidence: 0.85

### 4. Cricarebords surbaisses d'une capacitede

![item 9803](classification-review-assets/item-9803.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 139.99 $ · as printed: “139,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 2
- **Details:** OCR/extraction confidence: 0.85

### 5. Sauce pourpoulet aubeurreKFI Ndarticle1359722

![item 9830](classification-review-assets/item-9830.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 7.99 $ · as printed: “7,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 4
- **Details:** OCR/extraction confidence: 0.70

### 6. Chandailenmolletona fermeturea glissierepleine longueur SierraDesign talles P a TTG

![item 9795](classification-review-assets/item-9795.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 19.99 $ · as printed: “19,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 1
- **Details:** OCR/extraction confidence: 0.85

### 7. 18CARRIDGE/CARTOUCHES1RAZOR/ASOIR RasoirFusion5ProGlidedeGillette avec18

![item 9870](classification-review-assets/item-9870.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 55.99 $ · as printed: “55,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 8
- **Details:** OCR/extraction confidence: 0.85

### 8. NettoyantpourcuvetteAdvanced deLysol

![item 9840](classification-review-assets/item-9840.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 10.99 $ · as printed: “10,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 5
- **Details:** OCR/extraction confidence: 0.85

### 9. All-in-One Shake Boisson tout-en-un Boisson tout-en-unFudge au chocolat de

![item 9856](classification-review-assets/item-9856.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 63.99 $ · as printed: “63,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 7
- **Details:** OCR/extraction confidence: 0.85

### 10. Assortiment demini-barresDairyMilkde

![item 9836](classification-review-assets/item-9836.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 15.99 $ · as printed: “15,99 $”
- **Flyer validity:** 2026-09-28 → 2026-10-25 · flyer page 5
- **Details:** OCR/extraction confidence: 0.85

## Euro Marché (`euro-marche`)

### 1. JAMBON CUIT ITALIEN IMP. DITALIE Se» PROSCIUTTO a \\ €

![item 9906](classification-review-assets/item-9906.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.98

### 2. AVOCATS HASS < DU MEXIQUE AVOCADOS FROM +;

![item 9928](classification-review-assets/item-9928.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 0.06 $ · as printed: “169/10.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.93

### 3. © CH/EA YOGOURT & VOIR VARIÉTÉS EN MAGASIN

![item 11765](classification-review-assets/item-11765.jpg)

- **Category:** Dairy & Eggs > Yogurt (FR: Produits laitiers et œufs > Yogourt)
- **How classified:** rule (`yogurt`)
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 4. 7 CH/EA JUS DE FRUITS VOIR VARIÉTÉS

![item 11776](classification-review-assets/item-11776.jpg)

- **Category:** Drinks > Juice (FR: Boissons > Jus)
- **How classified:** rule (`juice`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 5. BAGUETTE DORÉE AMIENS # à — BAGUETTE, oN)

![item 9934](classification-review-assets/item-9934.jpg)

- **Category:** Bakery > Bread (FR: Boulangerie > Pain)
- **How classified:** rule (`bread`)
- **Price:** 1.50 $ · as printed: “2/3.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 6. POMMES GALA DES É.-U. GALA APPLES FROM

![item 9935](classification-review-assets/item-9935.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 7. POIRES BARTLETT DES É.-U. PEARS FROM

![item 11779](classification-review-assets/item-11779.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 1.33 $ · as printed: “3/4.00”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 5
- **Details:** OCR/extraction confidence: 0.97

### 8. HUILE D'OLIVE EXTRA VIERGE REGINA

![item 9877](classification-review-assets/item-9877.jpg)

- **Category:** Pantry > Canned & Pickled (FR: Produits du garde-manger > Produits en conserve et marinés)
- **How classified:** rule (`canned-pickled`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.94

### 9. CAPSULES} CAFFE \ BORBONE | ESPRESSO | COFFEE

![item 9913](classification-review-assets/item-9913.jpg)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.95

### 10. CH/EA

![item 9902](classification-review-assets/item-9902.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

## Familiprix (`familiprix`)

### 1. CHRISTIE, Oreo, Mini biscuits-sandwichs au chocolat, 20 x 25 g

![item 3398](http://f.wishabi.net/page_items/435804859/1790661160/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Christie · OCR/extraction confidence: 1.00

### 2. DOVE Soins capillaires

![item 4094](http://f.wishabi.net/page_items/435804415/1790661149/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Dove · OCR/extraction confidence: 1.00

### 3. NICORETTE Gomme de nicotine

![item 3954](http://f.wishabi.net/page_items/435804248/1790661159/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 12.99 $ · as printed: “12.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Nicorette · OCR/extraction confidence: 1.00

### 4. Biomedic comprimé soulagement pour les jambes 30un

![item 3666](http://f.wishabi.net/page_items/435804925/1790661166/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 14.99 $ · as printed: “14.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Biomedic · OCR/extraction confidence: 1.00

### 5. HUGGIES Lingettes pour bébé

![item 3495](http://f.wishabi.net/page_items/435804049/1790661139/extra_large.jpg)

- **Category:** Baby > Baby Care (FR: Bébé > Soins pour bébé)
- **How classified:** rule (`baby-care`)
- **Price:** 21.49 $ · as printed: “21.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Huggies · OCR/extraction confidence: 1.00

### 6. BYLY Antisudorifiques ou déodorants

![item 3608](http://f.wishabi.net/page_items/435804995/1790661161/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: BYLY · OCR/extraction confidence: 1.00

### 7. GRAVOL ou GASTROVOL

![item 3843](http://f.wishabi.net/page_items/435804444/1790661147/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 8. Maybelline New York Fit Me camouflant #10 Clair 6.8ml

![item 4000](http://f.wishabi.net/page_items/435859845/1790661174/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 10.99 $ · as printed: “10.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: MAYBELLINE NEW YORK · OCR/extraction confidence: 1.00

### 9. CASCADES

![item 4071](http://f.wishabi.net/page_items/435870806/1790661148/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 5.88 $ · as printed: “5.88”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Cascades · OCR/extraction confidence: 1.00

### 10. Canesten comprimé confort + crème externe 3 jours

![item 3811](http://f.wishabi.net/page_items/435804131/1790661143/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 17.49 $ · as printed: “17.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: CANESTEN · OCR/extraction confidence: 1.00

## Fruiterie Valmont (`fruiterie-valmont`)

### 1. cheddar Fromagesrapesparmesan, fort,Tex-MexouLe Gratine

![item 11086](classification-review-assets/item-11086.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 5.00 $ · as printed: “2/10.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.87

### 2. Bleuets Perou

![item 11079](classification-review-assets/item-11079.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 3. Choux-fleursblancs,mauves ouoranges Quebec

![item 11071](classification-review-assets/item-11071.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 4. Celeris Quebec

![item 11928](classification-review-assets/item-11928.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.66 $ · as printed: “1.66”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 5. chopine Tomatesmedley Mexique

![item 11069](classification-review-assets/item-11069.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.50 $ · as printed: “2/5.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.82

### 6. Citrouille orange Quebec

![item 11927](classification-review-assets/item-11927.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 7. Poireaux Quebec

![item 11930](classification-review-assets/item-11930.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 8. Sepato ICONOMISEZ PLUSDE

![item 11090](classification-review-assets/item-11090.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.00 $ · as printed: “2/12.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.95

### 9. CafesGustavo Auchoix-600g

![item 11065](classification-review-assets/item-11065.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 0.14 $ · as printed: “0.14”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 10. Cannebergesfraiches Quebec

![item 11080](classification-review-assets/item-11080.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.50 $ · as printed: “2/5.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.80

## Fruits & Légumes 3 Saisons (`3-saisons-fruits-legumes`)

### 1. OKA

![item 11596](classification-review-assets/item-11596.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.81 · other printed prices: 2/6.00

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

### 5. PRODUIT IMPORTE

![item 11109](classification-review-assets/item-11109.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.75

### 6. BOCCONCINI

![item 11106](classification-review-assets/item-11106.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.92

## Giant Tiger (`giant-tiger`)

### 1. Mini pommes de terre Steam & Go 1 lb

![item 11969](http://f.wishabi.net/page_items/436855094/1791521201/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 0.97 $ · as printed: “0.97”
- **Flyer validity:** 2026-10-14 → 2026-10-20
- **Details:** OCR/extraction confidence: 1.00

### 2. Friandises format collation Hershey's

![item 11948](http://f.wishabi.net/page_items/436855096/1791521203/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 10.97 $ · as printed: “10.97”
- **Flyer validity:** 2026-10-14 → 2026-10-20
- **Details:** brand: Sour Patch · OCR/extraction confidence: 1.00

### 3. Les Fermes Cavendish Rondelles d'oignon

![item 11953](http://f.wishabi.net/page_items/436855188/1791521204/extra_large.jpg)

- **Category:** Frozen Food > Frozen Appetizers & Snacks (FR: Produits surgelés > Entrées et collations surgelés)
- **How classified:** rule (`specific-frozen-fries-brands`)
- **Price:** 7.97 $ · as printed: “7.97”
- **Flyer validity:** 2026-10-14 → 2026-10-20
- **Details:** brand: Cavendish Farms · OCR/extraction confidence: 1.00

### 4. Pâté d'accompagnement Knorr

![item 4196](http://f.wishabi.net/page_items/436264065/1791299937/extra_large.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 1.74 $ · as printed: “1.74”
- **Flyer validity:** 2026-10-07 → 2026-10-13
- **Details:** brand: Knorr · OCR/extraction confidence: 1.00

### 5. Salade Massibec

![item 4201](http://f.wishabi.net/page_items/436264070/1791299940/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.97 $ · as printed: “2.97”
- **Flyer validity:** 2026-10-07 → 2026-10-13
- **Details:** brand: Massibec · OCR/extraction confidence: 1.00

### 6. Bologne ou pain de viande simili-poulet Gaspésien

![item 11967](http://f.wishabi.net/page_items/436855183/1791521200/extra_large.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 3.47 $ · as printed: “3.47”
- **Flyer validity:** 2026-10-14 → 2026-10-20
- **Details:** brand: Gaspésien · OCR/extraction confidence: 1.00

### 7. Bacon Smoke House Gold Label

![item 4214](http://f.wishabi.net/page_items/436670992/1791318419/extra_large.jpg)

- **Category:** Meat > Bacon (FR: Viande > Bacon)
- **How classified:** rule (`bacon`)
- **Price:** 3.47 $ · as printed: “3.47”
- **Flyer validity:** 2026-10-07 → 2026-10-13
- **Details:** brand: Smoke House · OCR/extraction confidence: 1.00

### 8. Sauce Franco-American

![item 4211](http://f.wishabi.net/page_items/436670998/1791318422/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 0.77 $ · as printed: “0.77”
- **Flyer validity:** 2026-10-07 → 2026-10-13
- **Details:** brand: Franco-American · OCR/extraction confidence: 1.00

### 9. Tranches style cheddar Black Diamond

![item 11963](http://f.wishabi.net/page_items/436855090/1791521197/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 3.33 $ · as printed: “3.33”
- **Flyer validity:** 2026-10-14 → 2026-10-20
- **Details:** brand: Black Diamond · OCR/extraction confidence: 1.00

### 10. Simply Orange

![item 11959](http://f.wishabi.net/page_items/436855182/1791521199/extra_large.jpg)

- **Category:** Drinks > Juice (FR: Boissons > Jus)
- **How classified:** rule (`juice`)
- **Price:** 4.47 $ · as printed: “4.47”
- **Flyer validity:** 2026-10-14 → 2026-10-20
- **Details:** brand: Simply Orange · OCR/extraction confidence: 1.00

## H Marché (`h-marche`)

### 1. BONELESS SALTED MACKEREL MAQUEREAU SALE SANS ARETES

![item 11155](classification-review-assets/item-11155.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.98

### 2. CJHS S7= 4506 CJ) CHAPELURE BEKSUL CJ) BEKSUL BREAD CRUMBS

![item 11981](classification-review-assets/item-11981.jpg)

- **Category:** Bakery > Bread (FR: Boulangerie > Pain)
- **How classified:** rule (`bread`)
- **Price:** 3.66 $ · as printed: “3.66”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 7
- **Details:** OCR/extraction confidence: 0.99

### 3. SALTED SEA TROUT MAIGRE SALE

![item 11156](classification-review-assets/item-11156.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.98

### 4. SALTED SEA TROUT MAIGRE SALE

![item 11973](classification-review-assets/item-11973.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 2
- **Details:** OCR/extraction confidence: 0.98

### 5. CRD) PETITS ANCHOIS SÉCHÉS (JIRI) CRD) SMALL DRIED ANCHOVIES (JIRI)

![item 11979](classification-review-assets/item-11979.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 8.29 $ · as printed: “8.29”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 7
- **Details:** OCR/extraction confidence: 0.99

### 6. SALTED HAIRTAIL FISH SABRE SALE

![item 11154](classification-review-assets/item-11154.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 10.99 $ · as printed: “10.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.95

### 7. MMS) CRAQUELINS DE RIZ AU BLE ENTIER MMS) WHOLE WHEAT RICE CRACKERS

![item 11159](classification-review-assets/item-11159.jpg)

- **Category:** Snacks, Chips & Candy > Crackers & Cookies (FR: Grignotines, croustilles et friandises > Craquelins et biscuits)
- **How classified:** rule (`crackers-cookies`)
- **Price:** 23.29 $ · as printed: “23.29”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 8. NH) RIZ BYEOLCHEONJ! DE HADONG NH) HADONG BYEOLCHEONJI RICE

![item 11978](classification-review-assets/item-11978.jpg)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 36.99 $ · as printed: “36.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

### 9. SALTED HAIRTAIL FISH SABRE SALE

![item 11971](classification-review-assets/item-11971.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 10.99 $ · as printed: “10.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 2
- **Details:** OCR/extraction confidence: 0.95

### 10. HC) LANIÈRES DE GOBERGE SÉCHÉE (HWANGTAE) HC) DRIED POLLOCK STRIPS (HWANGTAE)

![item 11975](classification-review-assets/item-11975.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 24.66 $ · as printed: “24.66”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

## IGA (`iga`)

### 1. SAVON OU SHAMPOING POUR BÉBÉ COMPLIMENTS

![item 631](https://f.wishabi.net/page_pdf_images/24244979/454a12aa-be1b-11f1-84e0-beb1c385ff76/x_large)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Compliments · OCR/extraction confidence: 1.00 · “500 mL Rég. 5,99$ à 6,29$”

### 2. CAFÉ MELITTA

![item 708](https://f.wishabi.net/page_pdf_images/24244969/27726b24-be1b-11f1-b4c4-72daea333c71/x_large)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Melitta · SKU: 00000_000000005543753404 · OCR/extraction confidence: 1.00 · “30 Rég. 25,49$ à 26,99$”

### 3. POITRINE DE POULET PORTUGAIS FRAIS RICARDO

![item 661](https://f.wishabi.net/page_pdf_images/24244973/28daa076-be1b-11f1-97d4-feafecf88833/x_large)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Ricardo · SKU: 00000_000000026665700000 · OCR/extraction confidence: 1.00 · “Désossée, assaisonnée et avec peau 26,43 $/kg Rég. 27,99$/kg”

### 4. BÂTONNETS DE FROMAGE BLACK DIAMOND FICELLO

![item 446](https://f.wishabi.net/page_pdf_images/24244978/2bfaa5d0-be1b-11f1-ad44-fee36c7f22ec/x_large)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Black Diamond · SKU: 00000_000000006820088922 · OCR/extraction confidence: 1.00 · “(8) Rég. 6,29$ à 6,79$”

### 5. service magasin fruits et legumes

![item 410](https://f.wishabi.net/page_items/436335346/1790932037/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00 · “Arrivages frais tous les jours pour s'étonner. Vos yeux serviront.”

### 6. HUÎTRES BEAUSOLEIL COCKTAIL

![item 478](https://f.wishabi.net/page_items/436319100/1790932030/extra_large.jpg)

- **Category:** Fish & Seafood > Shellfish (FR: Poissons et fruits de mer > Crustacés)
- **How classified:** rule (`shellfish`)
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 00000_000000022918100000 · OCR/extraction confidence: 1.00 · “Du Nouveau-Brunswick”

### 7. BOISSON À BASE DE PLANTES BIOLOGIQUE NATURA

![item 12160](https://f.wishabi.net/page_pdf_images/24268535/60382e78-c274-11f1-96ba-aad9f7bf7024/x_large)

- **Category:** Dairy & Eggs > Non-Dairy Milk Alternatives (FR: Produits laitiers et œufs > Laits non laitiers)
- **How classified:** rule (`non-dairy-milk`)
- **Price:** 2.79 $ · as printed: “2.79”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** SKU: 00000_000000006366751100 · OCR/extraction confidence: 1.00 · “946 ml Sélection variée Rég. 3,69$ à 4,19$”

### 8. FRIANDISES QUÉRICO

![item 628](https://f.wishabi.net/page_pdf_images/24244977/32dbe558-be1b-11f1-9f85-362af39aa6ef/x_large)

- **Category:** Snacks, Chips & Candy > Chips & Snacks (FR: Grignotines, croustilles et friandises > Croustilles et grignotines)
- **How classified:** rule (`chips-snacks`)
- **Price:** 6.49 $ · as printed: “6.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Pretzel · SKU: 00000_000000080442801424 · OCR/extraction confidence: 1.00 · “Mélange de bonbons Halloween 1 kg”

### 9. PAINS GARNIS C'EST PRÊT!

![item 12202](https://f.wishabi.net/page_pdf_images/24268541/52ca40fa-c274-11f1-a07c-0ef9fcbcc086/x_large)

- **Category:** Bakery > Bread (FR: Boulangerie > Pain)
- **How classified:** rule (`bread`)
- **Price:** 4.49 $ · as printed: “4.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: C'EST PRÊT! · SKU: 00000_000000028368600000 · OCR/extraction confidence: 1.00 · “Simili-crabe épicé, Goberge et crevettes Emballage de 2”

### 10. MUFFINS SAVEURS DU FOUR Fait avec COFFEE CRISP

![item 12119](https://f.wishabi.net/page_pdf_images/24268542/612eb8ce-c274-11f1-95a7-8a3f53363a22/x_large)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** 6.49 $ · as printed: “6.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** SKU: 00000_000000028390200000 · OCR/extraction confidence: 1.00 · “Emballage de 4”

## IGA Express / Mini (`iga-express`)

### 1. CORNICHONS OU BETTERAVES MARINÉES STRUB'S

![item 1684](https://f.wishabi.net/page_pdf_images/24244978/27c16b34-be1b-11f1-ad44-fee36c7f22ec/x_large)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Strub's · SKU: 00000_000000006777319026 · OCR/extraction confidence: 1.00 · “750 mL ou 1 L Sélection variée Rég. 5,79$ à 6,79$”

### 2. BISCUITS SAVEURS DU FOUR

![item 12451](https://f.wishabi.net/page_items/436766325/1791427532/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Crackers & Cookies (FR: Grignotines, croustilles et friandises > Craquelins et biscuits)
- **How classified:** rule (`crackers-cookies`)
- **Price:** 6.49 $ · as printed: “6.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Saveurs du Four · SKU: 00000_000000075752805486 · OCR/extraction confidence: 1.00 · “Fait avec COFFEE CRISP Emballage de 10”

### 3. CRÈME GLACÉE NATREL SANS LACTOSE (473 mL), MOCHI À LA CRÈME GLACÉE NATREL (6 x 35 mL), CRÈMIER À CAFÉ NATREL (1 L) OU CRÈME SURE SEALTEST (500 mL)

![item 1824](https://f.wishabi.net/page_pdf_images/24244977/3946a284-be1b-11f1-9f85-362af39aa6ef/x_large)

- **Category:** Frozen Food > Ice Cream & Frozen Desserts (FR: Produits surgelés > Crèmes glacées et desserts glacés)
- **How classified:** rule (`ice-cream`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Natrel · OCR/extraction confidence: 1.00 · “(si applicable) Reg. 5,29$ à 7,99$”

### 4. SODA SOLLY'S

![item 12624](https://f.wishabi.net/page_pdf_images/24268545/834f265a-c274-11f1-9ee5-9acc78cb8fd5/x_large)

- **Category:** Drinks > Soft Drinks (FR: Boissons > Boissons gazeuses)
- **How classified:** rule (`soft-drinks`)
- **Price:** 2.49 $ · as printed: “2.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** SKU: 00000_000000069124526002 · OCR/extraction confidence: 1.00 · “355 mL Canette consignée Sélection variée Rég. 2,79$ à 2,99$”

### 5. BIÈRE BUDWEISER

![item 1883](https://f.wishabi.net/page_pdf_images/24244978/2e2d5528-be1b-11f1-ad44-fee36c7f22ec/x_large)

- **Category:** Beer & Wine > Beer (FR: Bières et vins > Bières)
- **How classified:** rule (`beer`)
- **Price:** 44.99 $ · as printed: “44.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Budweiser · SKU: 00000_000000006206733546 · OCR/extraction confidence: 1.00 · “30 x 355 mL”

### 6. YOGOURT GREC COMPLIMENTS

![item 1966](https://f.wishabi.net/page_pdf_images/24244977/2943ee14-be1b-11f1-9f85-362af39aa6ef/x_large)

- **Category:** Dairy & Eggs > Yogurt (FR: Produits laitiers et œufs > Yogourt)
- **How classified:** rule (`yogurt`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Compliments · SKU: 00000_000000005574255049 · OCR/extraction confidence: 1.00 · “650 g Rég. 6,99$ à 7,49$”

### 7. BOISSON GAZEUSE COMPLIMENTS

![item 12494](https://f.wishabi.net/page_items/436766343/1791427531/extra_large.jpg)

- **Category:** Drinks > Soft Drinks (FR: Boissons > Boissons gazeuses)
- **How classified:** rule (`soft-drinks`)
- **Price:** 8.79 $ · as printed: “8.79”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Compliments · OCR/extraction confidence: 1.00 · “12 x 355 ml Canettes consignées Rég. 9,99$ à 10,49$”

### 8. POMMES ROYAL GALA

![item 1894](https://f.wishabi.net/page_pdf_images/24244970/240ec6bc-be1b-11f1-889a-4aef5d10a223/x_large)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 00000_000000000000004173 · OCR/extraction confidence: 1.00 · “Produit du Québec Canada no 1”

### 9. CÉRÉALES OU SUBSTITUT DE REPAS

![item 12455](https://f.wishabi.net/page_items/436765789/1791427519/extra_large.jpg)

- **Category:** Pantry > Cereal & Breakfast (FR: Produits du garde-manger > Céréales et petits-déjeuners)
- **How classified:** rule (`cereal-breakfast`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Kellogg's · OCR/extraction confidence: 1.00 · “SELECTION VARIÉE 450 à 650 g 317 à 778 g”

### 10. FRIANDISES REGAL TIGER POPS

![item 12355](https://f.wishabi.net/page_pdf_images/24268545/68167262-c274-11f1-9ee5-9acc78cb8fd5/x_large)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 12.99 $ · as printed: “12.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: TIGER POPS · SKU: 00000_000000066257220232 · OCR/extraction confidence: 1.00 · “Suçons 200”

## IGA Extra (`iga-extra`)

### 1. POMMES EMPIRE OU McINTOSH

![item 2082](https://f.wishabi.net/page_items/436319135/1790932030/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 00000_000000000000004124 · OCR/extraction confidence: 1.00 · “Produits du Québec Canada no 1”

### 2. BIÈRE BUDWEISER

![item 2280](https://f.wishabi.net/page_pdf_images/24244978/2e2d5528-be1b-11f1-ad44-fee36c7f22ec/x_large)

- **Category:** Beer & Wine > Beer (FR: Bières et vins > Bières)
- **How classified:** rule (`beer`)
- **Price:** 44.99 $ · as printed: “44.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Budweiser · SKU: 00000_000000006206733546 · OCR/extraction confidence: 1.00 · “30 x 355 mL”

### 3. CRÈME GLACÉE PANACHE (1 L) OU FRIANDISES GLACÉES* COMPLIMENTS, PANACHE OU CHAPMAN'S

![item 12869](https://f.wishabi.net/page_pdf_images/24268531/6aa3f25c-c274-11f1-934f-9e7dacbebb42/x_large)

- **Category:** Frozen Food > Ice Cream & Frozen Desserts (FR: Produits surgelés > Crèmes glacées et desserts glacés)
- **How classified:** rule (`ice-cream`)
- **Name (EN):** COMPLIMENTS, PANACHE OU CHAPMAN'S ICE CREAM OR FROZEN TREATS*
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** SKU: 00000_000000006294200328 · OCR/extraction confidence: 1.00 · “Sélection variée Rég. 5,79$ à 7,49$”

### 4. CREVETTES SAUVAGES D'ARGENTINE CRUES SURGELÉES MARINA DEL REY

![item 2409](https://f.wishabi.net/page_items/436319094/1790932036/extra_large.jpg)

- **Category:** Frozen Food > Frozen Meat and Seafood (FR: Produits surgelés > Viande et fruits de mer surgelés)
- **How classified:** frozen-remap (`shrimp`)
- **Price:** 16.99 $ · as printed: “16.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: MARINA DEL REY · SKU: 00000_000000087242500229 · OCR/extraction confidence: 1.00 · “Grosseur 13-15P 454 g”

### 5. FÈVES COMPLIMENTS

![item 13052](https://f.wishabi.net/page_pdf_images/24268544/59f5b5a8-c274-11f1-8248-8a02ca7e33cb/x_large)

- **Category:** Pantry > Dried Beans, Vegetables & Grains (FR: Produits du garde-manger > Haricots secs, légumes et grains)
- **How classified:** rule (`beans-grains`)
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Compliments · SKU: 00000_000000005574257178 · OCR/extraction confidence: 1.00 · “398 mL Sélection variée Rég. 2,29$ à 2,49$”

### 6. MICHELOB ULTRA BIÈRE

![item 2374](https://f.wishabi.net/page_pdf_images/24244979/2a9d995e-be1b-11f1-84e0-beb1c385ff76/x_large)

- **Category:** Beer & Wine > Beer (FR: Bières et vins > Bières)
- **How classified:** rule (`beer`)
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Michelob · SKU: 00000_000000006206754747 · OCR/extraction confidence: 1.00 · “12 x 355 mL Canettes consignées Rég. 25,49$ à 26,99$”

### 7. CREVETTES SAUVAGES CRUES D'ARGENTINE SURGELÉES Faciles à décortiquer MARINA DEL REY

![item 12906](https://f.wishabi.net/page_pdf_images/24268530/59896c68-c274-11f1-be97-3e102d04e6b0/x_large)

- **Category:** Frozen Food > Frozen Meat and Seafood (FR: Produits surgelés > Viande et fruits de mer surgelés)
- **How classified:** frozen-remap (`shrimp`)
- **Price:** 12.99 $ · as printed: “12.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: MARINA DEL REY · SKU: 00000_000000087242500166 · OCR/extraction confidence: 1.00 · “Grosseur 20-30 Size 680 g”

### 8. THON PÂLE LISTAO OU AROMATISÉ CLOVER LEAF

![item 2334](https://f.wishabi.net/page_pdf_images/24244978/26457368-be1b-11f1-ad44-fee36c7f22ec/x_large)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 4.00 $ · as printed: “4.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Clover Leaf · SKU: 00000_000000006136243430 · OCR/extraction confidence: 1.00 · “85 ou 170 g Sélection variée”

### 9. CAFÉ EN GRAINS OU MOULU BIOLOGIQUES ET ÉQUITABLES KICKING HORSE

![item 2283](https://f.wishabi.net/page_pdf_images/24244969/202edb2c-be1b-11f1-b4c4-72daea333c71/x_large)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** 27.97 $ · as printed: “27.97”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: KICKING HORSE · SKU: 00000_000000062907070038 · OCR/extraction confidence: 1.00 · “708 ou 850 g Sélection variée Rég. 39,99$ à 41,99$”

### 10. YOGOURT LIBERTÉ CLASSIQUE (650g), MÉDITERRANÉE (500g) OU YOPLAIT SOURCE PROTÉINES (650g)

![item 12886](https://f.wishabi.net/page_pdf_images/24268543/623a7cda-c274-11f1-b3b8-26c84f172ddc/x_large)

- **Category:** Dairy & Eggs > Yogurt (FR: Produits laitiers et œufs > Yogourt)
- **How classified:** rule (`yogurt`)
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Liberté · OCR/extraction confidence: 1.00 · “Yogourt 9 % MG NATURE (650 g) CERISE NOIRE (500 g) classique liberté méditerranée”

## Jean Coutu (`jean-coutu`)

### 1. SYSTANE Produits de soins pour les yeux sélectionnés

![item 7586](http://f.wishabi.net/page_items/436743602/1791423684/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 2. Cross Signal Encounters

![item 7654](http://f.wishabi.net/page_items/436743752/1791423704/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 3. HERTEL Produits nettoyants sélectionnés

![item 7653](http://f.wishabi.net/page_items/436743738/1791423690/extra_large.jpg)

- **Category:** Household > Cleaning & Laundry (FR: Maison > Entretien et lessive)
- **How classified:** rule (`household-cleaning`)
- **Price:** 2.77 $ · as printed: “2.77”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Hertel · OCR/extraction confidence: 1.00

### 4. URIAGE

![item 8135](http://f.wishabi.net/page_items/436073141/1790818379/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: URIAGE · OCR/extraction confidence: 1.00

### 5. Selection Friandises sélectionnées

![item 7670](http://f.wishabi.net/page_items/436741471/1791422976/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 2.29 $ · as printed: “2.29”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Selection · OCR/extraction confidence: 1.00

### 6. BENEFIBER Produits sélectionnés

![item 7896](http://f.wishabi.net/page_items/436820075/1791424631/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-28
- **Details:** brand: Benefiber · OCR/extraction confidence: 1.00

### 7. MESSAGE IMPORTANT

![item 7563](http://f.wishabi.net/page_items/436333974/1790921602/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 8. JUICY COUTURE Fragrances et formats sélectionnés

![item 7680](http://f.wishabi.net/page_items/436741447/1791422992/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Juicy Couture · OCR/extraction confidence: 1.00

### 9. PERSONNELLE Savons à mains sélectionnés

![item 7656](http://f.wishabi.net/page_items/436743741/1791423693/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Personnelle · OCR/extraction confidence: 1.00

### 10. CASHMERE

![item 8051](http://f.wishabi.net/page_items/436072959/1790818378/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 10.99 $ · as printed: “10.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Cashmere · OCR/extraction confidence: 1.00

## Kim Phat (`kim-phat`)

### 1. ESSENCE DE MUCINE D'ESCARGOT CONCENTRÉE 96

![item 4236](http://f.wishabi.net/page_items/436675116/1791333600/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 14.99 $ · as printed: “14.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Cosrx · OCR/extraction confidence: 1.00

### 2. DATTES ROUGES SÉCHÉES MERLIN

![item 4292](http://f.wishabi.net/page_items/436675190/1791333608/extra_large.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 3. SAUCE PIQUANTE AUX HARICOTS NOIRS

![item 13178](http://f.wishabi.net/page_items/437237128/1791947770/extra_large.jpg)

- **Category:** Pantry > Dried Beans, Vegetables & Grains (FR: Produits du garde-manger > Haricots secs, légumes et grains)
- **How classified:** rule (`beans-grains`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: LGM · OCR/extraction confidence: 1.00

### 4. RAVIOLIS AU PORC ET AUX FRUITS DE MER FOONG'S KITCHEN

![item 13130](http://f.wishabi.net/page_items/437237056/1791947777/extra_large.jpg)

- **Category:** Fish & Seafood > Shellfish (FR: Poissons et fruits de mer > Crustacés)
- **How classified:** rule (`shellfish`)
- **Price:** 4.49 $ · as printed: “4.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Foong's Kitchen · OCR/extraction confidence: 1.00

### 5. CHOUX TAÏWANAIS

![item 4374](http://f.wishabi.net/page_items/436675168/1791333601/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 17.99 $ · as printed: “17.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 6. LOBOK (DAIKON CHINOIS)

![item 13090](http://f.wishabi.net/page_items/437237038/1791947775/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 0.69 $ · as printed: “0.69”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 7. GLUTAMATE DE SODIUM TASTIE

![item 4272](http://f.wishabi.net/page_items/436675163/1791333597/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 44.99 $ · as printed: “44.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: TASTIE · OCR/extraction confidence: 1.00

### 8. AUBERGINE CHINOISE

![item 4247](http://f.wishabi.net/page_items/436675132/1791333598/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 9. CHOUX NAPPA

![item 13199](http://f.wishabi.net/page_items/437237069/1791947767/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 23.99 $ · as printed: “23.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 10. FLANC DE BŒUF

![item 4309](http://f.wishabi.net/page_items/436675199/1791333594/extra_large.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 7.88 $ · as printed: “7.88”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

## L'Intermarché (`l-intermarche`)

### 1. ESSUIE-TOUT SANS NOM® 6 = 18 ROUL. PAPER TOWELS

![item 10771](classification-review-assets/item-10771.jpg)

- **Category:** Household > Paper & Storage (FR: Maison > Papier et rangement)
- **How classified:** rule (`household-paper`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.98

### 2. FROMAGE BOCCONCINI, FETA OU PARMESAN, RICOTTA SAPUTO CERTAINES VARIETES

![item 13248](classification-review-assets/item-13248.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 3. BOISSON GAZEUSE PC” 2 L (CONSIGNE) OÙ JUS OASIS, DEL MONTE OÙ ARIZONA

![item 13223](classification-review-assets/item-13223.jpg)

- **Category:** Drinks > Soft Drinks (FR: Boissons > Boissons gazeuses)
- **How classified:** rule (`soft-drinks`)
- **Price:** 1.00 $ · as printed: “1”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 4. POULET ENTIER FORMAT FAMILIAL WHOLE CHICKEN

![item 10766](classification-review-assets/item-10766.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 5. PISTACHES PC® OU MENU BLEU PC® MINI-POMMES DE TERRE PC” PRODUIT DES É.-U. 680 G OU FLEURONS DE BROCOLI

![item 13227](classification-review-assets/item-13227.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 6. CHAMPIGNONS PC? OU PC? BIOLOGIQUES"

![item 13237](classification-review-assets/item-13237.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.49 $ · as printed: “2.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 7. EAU PÉTILLANTE +. é x EAU PÉTILLANTE PC“ 12 X 355 ML OU BOISSON PÉTILLANTE SANPELLEGRINO

![item 10731](classification-review-assets/item-10731.jpg)

- **Category:** Drinks > Water (FR: Boissons > Eau)
- **How classified:** rule (`water`)
- **Price:** 5.49 $ · as printed: “5.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 8. MINI-MUFFINS PC® 336 G OU MINI- GATEAUX SCHOOL SAFE 280 - 296 G OU MINI-BARRES LITTLE BITES 96 G CERTAINES VARIETES

![item 13230](classification-review-assets/item-13230.jpg)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 9. PLATS CUISINES WONG WING CERTAINES VARIETES, SURGELES

![item 13213](classification-review-assets/item-13213.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** frozen-remap (`entrees`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.87

### 10. VIANDE TRANCHÉE PC" SPLENDIDO CERTAINES VARIÉTÉS, 100 G SLICED MEATS 21049131 EA/21050405 EA

![item 10757](classification-review-assets/item-10757.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 5.99 $ · as printed: “5.99”
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

### 2. POISCHICHES 8B HARICOTS BLANCS GIGI 580ML

![item 11000](classification-review-assets/item-11000.jpg)

- **Category:** Pantry > Dried Beans, Vegetables & Grains (FR: Produits du garde-manger > Haricots secs, légumes et grains)
- **How classified:** rule (`beans-grains`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 2.49

### 3. POITRINE DE POULET DESOSSEE BONELESS CHICKEN

![item 13073](classification-review-assets/item-13073.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 4. FROMAGE CREMA BEL PAESE

![item 11002](classification-review-assets/item-11002.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 2.50 $ · as printed: “2/5.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 6.99

### 5. STEAK T-BONE

![item 11001](classification-review-assets/item-11001.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 6. POIVRONS

![item 10997](classification-review-assets/item-10997.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 7. HUILE DE TOURNESOL SALMA OU CEDAR “a

![item 10999](classification-review-assets/item-10999.jpg)

- **Category:** Pantry > Oils & Vinegar (FR: Produits du garde-manger > Huile et vinaigre)
- **How classified:** rule (`oils-vinegar`)
- **Price:** 14.99 $ · as printed: “14.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 8. EXTRA BRIE OU CAMEMBERT

![item 10998](classification-review-assets/item-10998.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

## La Moisson Supermarché Santé (`la-moisson`)

### 1. NEWZEALAND MANUKA HONEY LOZENGES PASTILLES AU MIEL DEMANUKA

![item 10821](classification-review-assets/item-10821.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 11.95 $ · as printed: “11.95”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.93

### 2. TABLETTES DE CHOCOLAT & CHOCOLAT

![item 10840](classification-review-assets/item-10840.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 7.65 $ · as printed: “7.65”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 7
- **Details:** OCR/extraction confidence: 0.92

### 3. BURRITOS & REPAS PRÊTS À MANGER VÉGÉTARIENS & VÉGANES ME" Ne PROTÉINES 20 g

![item 10814](classification-review-assets/item-10814.jpg)

- **Category:** Prepared Meals > Entrees & Appetizers (FR: Repas préparés > Plats principaux et apéritifs)
- **How classified:** rule (`entrees`)
- **Price:** 4.65 $ · as printed: “4.65”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.97

### 4. TARTINES BIO & SANS GLUTEN & BIO

![item 10832](classification-review-assets/item-10832.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.45 $ · as printed: “6.45”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 6
- **Details:** OCR/extraction confidence: 0.89

### 5. QUÉBEC CORIANDRE BIO

![item 10811](classification-review-assets/item-10811.jpg)

- **Category:** Fruits & Vegetables > Herbs (FR: Fruits et légumes > Fines herbes)
- **How classified:** rule (`herbs-fresh`)
- **Price:** 1.95 $ · as printed: “1.95”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.92

### 6. RAVIOLIS SURGELÉS À BASE DE PLANTES

![item 10820](classification-review-assets/item-10820.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 12.15 $ · as printed: “12.15”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 7. SOUPES PRÊTES À MANGER BIOLOGIQUES

![item 10815](classification-review-assets/item-10815.jpg)

- **Category:** Prepared Meals > Salads & Soups (FR: Repas préparés > Salades et soupes)
- **How classified:** rule (`salads-soups`)
- **Price:** 4.95 $ · as printed: “4.95”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.96

### 8. MEXIQUE BANANE BIO

![item 10810](classification-review-assets/item-10810.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.95 $ · as printed: “2.95”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.95

### 9. QUÉBEC ; PERSIL FRISE/ITALIEN BIO

![item 10812](classification-review-assets/item-10812.jpg)

- **Category:** Fruits & Vegetables > Herbs (FR: Fruits et légumes > Fines herbes)
- **How classified:** rule (`herbs-fresh`)
- **Price:** 1.95 $ · as printed: “1.95”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.94

### 10. 70% CACAO

![item 10827](classification-review-assets/item-10827.jpg)

- **Category:** Pantry > Baking Essentials (FR: Produits du garde-manger > Essentiels de cuisson)
- **How classified:** rule (`baking`)
- **Price:** 4.85 $ · as printed: “4.85”
- **Flyer validity:** 2026-10-01 → 2026-10-15 · flyer page 5
- **Details:** OCR/extraction confidence: 0.92

## Le Marché Esposito (`marche-esposito`)

### 1. TORTILLAS \VARIETES'EN’MAGASIN TORTILLAS VARIETY IN STORE 297GR, 334GR

![item 13526](classification-review-assets/item-13526.jpg)

- **Category:** Bakery > Wraps, Flatbread & Pizza Crust (FR: Boulangerie > Roulés, pains plats et croûtes à pizza)
- **How classified:** rule (`wraps-flatbread`)
- **Price:** 49.00 $ · as printed: “49”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 2. RODOLFIRES En. SAUCE|POUR(PATES ja VARIETESIEN'MAGASIN PASTAYSAUCE

![item 13503](classification-review-assets/item-13503.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 3
- **Details:** OCR/extraction confidence: 0.89

### 3. BARILLATSANSIGLUTEN DR PATESJALIMENTAIRES ls VARIETES/EN MAGASIN! PAST LE AVES VARIETY-IN STORE

![item 10087](classification-review-assets/item-10087.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.98

### 4. AUTRICIEN FROMAGE EMMENTAL EMMENTALER CHEESE

![item 10075](classification-review-assets/item-10075.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 9.99 $ · as printed: “9.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 5. [COMPLIMENTS jPOUDRE|POUR’GELEE OVARIETES EN/MAGASIN JELLY/POWDER ER VARIETY{IN/STORE

![item 13517](classification-review-assets/item-13517.jpg)

- **Category:** Pantry > Honey, Syrups & Spreads (FR: Produits du garde-manger > Miel, sirops et tartinades)
- **How classified:** rule (`honey-spreads`)
- **Price:** 2.49 $ · as printed: “2.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 6. COMPLIMENTS FRUITS/SURGELES VARIETES|EN|MAG/ FROZEN[FRUITS VARIETY{INISTORE

![item 13512](classification-review-assets/item-13512.jpg)

- **Category:** Frozen Food > Frozen Fruit & Vegetables (FR: Produits surgelés > Fruits et légumes surgelés)
- **How classified:** frozen-remap (`fruits`)
- **Price:** 5.79 $ · as printed: “5.79”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 7. MASTROÏEE > MES CAROCOLLO)DOUX(OU/FORT MILDJORTHOT CAPOCOLLO] ACLVAAUC DA

![item 10077](classification-review-assets/item-10077.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 8. CH./EA

![item 10094](classification-review-assets/item-10094.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 99.00 $ · as printed: “99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 9. N TRANCHES D POUR SANDWICH

![item 10099](classification-review-assets/item-10099.jpg)

- **Category:** Prepared Meals > Sandwiches (FR: Repas préparés > Sandwichs)
- **How classified:** rule (`sandwiches`)
- **Price:** 99.00 $ · as printed: “99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 10. FILET, DE PORC PORK(FILET

![item 10078](classification-review-assets/item-10078.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.95

## Le Monde au Naturel (`monde-au-naturel`)

### 1. SPECIAL

![item 10517](classification-review-assets/item-10517.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 20.00 $ · as printed: “20”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 2. SPECIAL

![item 10529](classification-review-assets/item-10529.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 15.00 $ · as printed: “15”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 3. SPÉCIAL

![item 10574](classification-review-assets/item-10574.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 15.00 $ · as printed: “15”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 9
- **Details:** OCR/extraction confidence: 0.99

### 4. SPÉCIAL

![item 10539](classification-review-assets/item-10539.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 20.00 $ · as printed: “20”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 5. "SPECIAL

![item 10532](classification-review-assets/item-10532.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 15.00 $ · as printed: “15”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 6. SPÉCIAL

![item 10521](classification-review-assets/item-10521.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 20.00 $ · as printed: “20”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 7. MADE GOOD

![item 10512](classification-review-assets/item-10512.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 15.00 $ · as printed: “15”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 8. SPECIAL

![item 10544](classification-review-assets/item-10544.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 20.00 $ · as printed: “20”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 9. SPÉCIAL

![item 10526](classification-review-assets/item-10526.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 15.00 $ · as printed: “15”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 10. SPECIAL

![item 10558](classification-review-assets/item-10558.jpg)

- **Category:** Health & Beauty > Vitamins & Supplements (FR: Santé et beauté > Vitamines et suppléments)
- **How classified:** store-prior
- **Price:** 15.00 $ · as printed: “15”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 7
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

### 1. 12-13UNITES|340g Crevettesal'ail

![item 14341](classification-review-assets/item-14341.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 24.99

### 2. Poulet popcorn

![item 10895](classification-review-assets/item-10895.jpg)

- **Category:** Snacks, Chips & Candy > Chips & Snacks (FR: Grignotines, croustilles et friandises > Croustilles et grignotines)
- **How classified:** rule (`specific-popcorn`)
- **Price:** 14.99 $ · as printed: “14.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 3. PIZZETTASMARGHERITAAL'ITALIENNE 2UNITES360g

![item 10963](classification-review-assets/item-10963.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** store-prior
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 11
- **Details:** OCR/extraction confidence: 0.98

### 4. Pizzamargherita sans gluten

![item 14336](classification-review-assets/item-14336.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** store-prior
- **Price:** 16.99 $ · as printed: “16.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 4
- **Details:** OCR/extraction confidence: 0.94 · other printed prices: 17.99

### 5. Boulettes debceuf al'italienne 130-140UNITES

![item 14321](classification-review-assets/item-14321.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** store-prior
- **Price:** 16.99 $ · as printed: “16.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 17.99

### 6. Paindeviandesupremestylemaison

![item 14344](classification-review-assets/item-14344.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** store-prior
- **Price:** 17.99 $ · as printed: “17.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 5
- **Details:** OCR/extraction confidence: 0.98 · other printed prices: 19.99

### 7. Nouilles ramen au porc chashu

![item 10902](classification-review-assets/item-10902.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.98

### 8. Style Louisiane

![item 14319](classification-review-assets/item-14319.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** store-prior
- **Price:** 12.99 $ · as printed: “12.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 9. Fromage en grains pane

![item 14355](classification-review-assets/item-14355.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 6.68 $ · as printed: “6.68”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 9.99

### 10. Painplat style doubleburger aufromageetaubacon

![item 14327](classification-review-assets/item-14327.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** store-prior
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 12.99, 11.99, 12.99

## Marche PA (`marche-pa`)

### 1. MERLAN FRAIS | Fresh Whiting

![item 4718](http://f.wishabi.net/page_items/436667730/1791319637/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** OCR/extraction confidence: 1.00

### 2. MANGUES ATAULFO

![item 4752](http://f.wishabi.net/page_items/436667693/1791319629/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 4.00 $ · as printed: “4.0”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** OCR/extraction confidence: 1.00

### 3. VITAMINE D3, CURCUMA, MAGNÉSIUM OU ASHWACHILL SUKU

![item 4646](http://f.wishabi.net/page_items/436672383/1791322439/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 16.99 $ · as printed: “16.99”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** brand: SUKU · OCR/extraction confidence: 1.00

### 4. FROMAGE AU LAIT DE CHÈVRE DEMI-AFFINÉ | Cheese

![item 4789](http://f.wishabi.net/page_items/436667755/1791319631/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** OCR/extraction confidence: 1.00

### 5. PETITES LENTILLES TACHETÉES FONCÉES DUNYA HARVEST | Lentils

![item 4693](http://f.wishabi.net/page_items/436672369/1791322441/extra_large.jpg)

- **Category:** Pantry > Dried Beans, Vegetables & Grains (FR: Produits du garde-manger > Haricots secs, légumes et grains)
- **How classified:** rule (`beans-grains`)
- **Price:** 2.49 $ · as printed: “2.49”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** brand: Dunya Harvest · OCR/extraction confidence: 1.00

### 6. BISCUITS AU BEURRE LA GALETTE ST MICHEL | Butter Cookies

![item 4754](http://f.wishabi.net/page_items/436667767/1791319627/extra_large.jpg)

- **Category:** Dairy & Eggs > Butter & Spreads (FR: Produits laitiers et œufs > Beurre et tartinades)
- **How classified:** rule (`butter`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** brand: St Michel · OCR/extraction confidence: 1.00

### 7. FROMAGE COMTÉ AFFINÉ 6 MOIS PRÉSIDENT | Cheese

![item 4632](http://f.wishabi.net/page_items/436672357/1791322430/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** brand: Président® · OCR/extraction confidence: 1.00

### 8. FILLETS DE THON LISTAO FUMÉS FANARI | Smoked Skipjack Tuna Fillets

![item 4652](http://f.wishabi.net/page_items/436672350/1791322437/extra_large.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** brand: FANARI · OCR/extraction confidence: 1.00

### 9. JUS FRUITÉ | Juice

![item 4714](http://f.wishabi.net/page_items/436667734/1791319625/extra_large.jpg)

- **Category:** Drinks > Juice (FR: Boissons > Jus)
- **How classified:** rule (`juice`)
- **Price:** 2.29 $ · as printed: “2.29”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** brand: fruite · OCR/extraction confidence: 1.00

### 10. BOEUF HACHÉ MAIGRE FRAIS | Fresh Lean Ground Beef

![item 4665](http://f.wishabi.net/page_items/436672344/1791322432/extra_large.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-12 → 2026-10-18
- **Details:** OCR/extraction confidence: 1.00

## Marché Adonis (`adonis`)

### 1. BIFTECK DE FILET MIGNON DE BOEUF RÉGULIER OU MARINÉ | REGULAR OR MARINATED BEEF TENDERLOIN STEAK

![item 7200](http://f.wishabi.net/page_items/436316609/1791013134/extra_large.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 23.99 $ · as printed: “23.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 2. YOGOURT GREC OU YOGOURT MÉDITERRANÉE LIBERTÉ | LIBERTÉ MÉDITERRANÉE YOGURT

![item 7177](http://f.wishabi.net/page_items/436316529/1791013129/extra_large.jpg)

- **Category:** Dairy & Eggs > Yogurt (FR: Produits laitiers et œufs > Yogourt)
- **How classified:** rule (`yogurt`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Liberté · OCR/extraction confidence: 1.00

### 3. FILETS DE TILAPIA BLUE TIDE | BLUE TIDE TILAPIA FILLETS

![item 7313](http://f.wishabi.net/page_items/436526844/1791221461/extra_large.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: BLUE TIDE · OCR/extraction confidence: 1.00

### 4. POMMES DE TERRE JAUNES, BLANCHES OU ROUGES | YELLOW, WHITE & RED POTATOES

![item 7252](http://f.wishabi.net/page_items/436316585/1791013137/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 5. FROMAGE À LA CRÈME PHILADELPHIA OU SINGLES DE KRAFT | PHILADELPHIA CREAM CHEESE SPREAD OR KRAFT SINGLES

![item 7399](http://f.wishabi.net/page_items/436891116/1791519991/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 3.97 $ · as printed: “3.97”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: PHILADELPHIA | KRAFT · OCR/extraction confidence: 1.00

### 6. PÂTES ALIMENTAIRES PRIMO | PRIMO PASTAS

![item 7184](http://f.wishabi.net/page_items/436316536/1791013135/extra_large.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 1.67 $ · as printed: “1.67”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Primo · OCR/extraction confidence: 1.00

### 7. LAIT AU CHOCOLAT OU LAIT BABEURRE BEATRICE | BEATRICE CHOCOLATE MILK OR BUTTERMILK

![item 7302](http://f.wishabi.net/page_items/436526854/1791221463/extra_large.jpg)

- **Category:** Dairy & Eggs > Milk & Cream (FR: Produits laitiers et œufs > Lait et crème)
- **How classified:** rule (`milk-cream`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Beatrice · OCR/extraction confidence: 1.00

### 8. FRAISES | STRAWBERRIES

![item 7256](http://f.wishabi.net/page_items/436526883/1791221472/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 3.88 $ · as printed: “3.88”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 9. Saputo bocconcini ou feta

![item 7481](http://f.wishabi.net/page_items/436891274/1791520003/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Saputo · OCR/extraction confidence: 1.00

### 10. HARD SQUASH | COURGES DURES

![item 7229](http://f.wishabi.net/page_items/436316582/1791013135/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

## Marché Ami (`marche-ami`)

### 1. craquelins Goldfish Pepperidge Farm

![item 13336](http://f.wishabi.net/page_items/436614400/1791348005/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Crackers & Cookies (FR: Grignotines, croustilles et friandises > Craquelins et biscuits)
- **How classified:** rule (`crackers-cookies`)
- **Price:** 2.49 $ · as printed: “2.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Pepperidge Farm · OCR/extraction confidence: 1.00

### 2. Vinaigrette Le Grec

![item 4430](http://f.wishabi.net/page_items/436183894/1790836061/extra_large.jpg)

- **Category:** Pantry > Condiments (FR: Produits du garde-manger > Condiments et garnitures)
- **How classified:** rule (`condiments`)
- **Price:** 4.49 $ · as printed: “4.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: LE GREC · OCR/extraction confidence: 1.00

### 3. bifteck de contre-filet

![item 4462](http://f.wishabi.net/page_items/436183846/1790836065/extra_large.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 18.99 $ · as printed: “18.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 4. mets chinois Wong Wing

![item 4419](http://f.wishabi.net/page_items/436183838/1790836061/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Wong Wing · OCR/extraction confidence: 1.00

### 5. yogourt crémeux Yoplait

![item 13303](http://f.wishabi.net/page_items/436614395/1791348001/extra_large.jpg)

- **Category:** Dairy & Eggs > Yogurt (FR: Produits laitiers et œufs > Yogourt)
- **How classified:** rule (`yogurt`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Yoplait · OCR/extraction confidence: 1.00

### 6. crème sure Sealtest

![item 4464](http://f.wishabi.net/page_items/436183887/1790836066/extra_large.jpg)

- **Category:** Dairy & Eggs > Sour Cream & Dips (FR: Produits laitiers et œufs > Crème sure et trempettes)
- **How classified:** rule (`sour-cream`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Sealtest · OCR/extraction confidence: 1.00

### 7. côtes de dos de porc frais

![item 4396](http://f.wishabi.net/page_items/436183804/1790836063/extra_large.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 8. pommes de terre frites McCain

![item 13361](http://f.wishabi.net/page_items/436614470/1791348001/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 5.49 $ · as printed: “5.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: McCain · OCR/extraction confidence: 1.00

### 9. Ritz

![item 4395](http://f.wishabi.net/page_items/436183797/1790836060/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Crackers & Cookies (FR: Grignotines, croustilles et friandises > Craquelins et biscuits)
- **How classified:** rule (`crackers-cookies`)
- **Price:** 2.33 $ · as printed: “2.33”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Christie · OCR/extraction confidence: 1.00

### 10. Côtelettes de porc frais

![item 4426](http://f.wishabi.net/page_items/436183837/1790836061/extra_large.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 4.49 $ · as printed: “4.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

## Marché Andes (`marche-andes`)

### 1. Biscuits FESTIVAL CITRON

![item 13381](https://www.marcheandes.com/wp-content/uploads/2025/08/Biscuits_Festival_Citron.webp)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 4.19 $ · as printed: “4.19”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** SKU: 6898 · OCR/extraction confidence: 1.00

### 2. Biscuits DUCALES

![item 11103](https://www.marcheandes.com/wp-content/uploads/2025/08/Biscuits_Ducales_Sachet.webp)

- **Category:** Snacks, Chips & Candy > Crackers & Cookies (FR: Grignotines, croustilles et friandises > Craquelins et biscuits)
- **How classified:** rule (`crackers-cookies`)
- **Price:** 2.89 $ · as printed: “2.89”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 4367 · OCR/extraction confidence: 1.00 · regular price 3.29

### 3. Biscuits DUCALES

![item 13380](https://www.marcheandes.com/wp-content/uploads/2025/08/Biscuits_Ducales_Sachet.webp)

- **Category:** Snacks, Chips & Candy > Crackers & Cookies (FR: Grignotines, croustilles et friandises > Craquelins et biscuits)
- **How classified:** rule (`crackers-cookies`)
- **Price:** 2.89 $ · as printed: “2.89”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** SKU: 4367 · OCR/extraction confidence: 1.00 · regular price 3.29

### 4. Biscuits FESTIVAL CITRON

![item 11104](https://www.marcheandes.com/wp-content/uploads/2025/08/Biscuits_Festival_Citron.webp)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 4.19 $ · as printed: “4.19”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 6898 · OCR/extraction confidence: 1.00

## Marché Axep (`marche-axep`)

### 1. POISSON SANS NOM® CERTAINES VARIÉTÉS, SURGELÉ

![item 13447](classification-review-assets/item-13447.jpg)

- **Category:** Frozen Food > Frozen Meat and Seafood (FR: Produits surgelés > Viande et fruits de mer surgelés)
- **How classified:** frozen-remap (`fish`)
- **Price:** 5.49 $ · as printed: “5.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

### 2. RÔTI FRANÇAIS DE BŒUF D'INTÉRIEUR* FRENCH BEEF ROAST FROM INSIDE ROUND*

![item 13397](classification-review-assets/item-13397.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 7.66 $ · as printed: “7.66”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 2
- **Details:** OCR/extraction confidence: 0.97

### 3. CARRÉS 400 - 450 G OU MACARONS BROWNIES DÉLICES DU MARCHÉ"C

![item 13400](classification-review-assets/item-13400.jpg)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 4. LA LaL ARM'L'AL A L l2a1' L" LL LÀ À CERTAINES VARIÉTÉS

![item 10004](classification-review-assets/item-10004.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 5.79 $ · as printed: “5.79”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 5. SALADE RESER'S CERTAINES VARIÉTÉS SALAD MORVAN A CA

![item 9993](classification-review-assets/item-9993.jpg)

- **Category:** Prepared Meals > Salads & Soups (FR: Repas préparés > Salades et soupes)
- **How classified:** rule (`salads-soups`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 6. CROUSTILLES YUM YUM CERTAINES VARIÉTÉS

![item 13450](classification-review-assets/item-13450.jpg)

- **Category:** Snacks, Chips & Candy > Chips & Snacks (FR: Grignotines, croustilles et friandises > Croustilles et grignotines)
- **How classified:** rule (`chips-snacks`)
- **Price:** 2.00 $ · as printed: “2”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

### 7. YOGOURT PROBIOTIQUES ACTIVIA LAIT PROTÉINÉ SANS LACTOSE CERTAINES VARIÉTÉS NATREL PLUS

![item 9972](classification-review-assets/item-9972.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 8. CHARCUTERIE TRANCHÉE COPPA OU PANCETTA ROMA CERTAINES VARIÉTÉS, 100 G SLICED DEL! MEAT

![item 13412](classification-review-assets/item-13412.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 9. TROUSSES-REPAS OU TROUSSES- COLLATION SCHNEIDERS CERTAINES VARIETES

![item 13418](classification-review-assets/item-13418.jpg)

- **Category:** Deli > Lunch & Snack Kits (FR: Charcuterie > Boites-repas)
- **How classified:** rule (`lunch-kits`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 10. GÂTEAU DELICES DU MARCHÉ"C CERTAINES VARIÉTÉS

![item 9980](classification-review-assets/item-9980.jpg)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 12.99 $ · as printed: “12.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

## Marché BKR (`marche-bkr`)

### 1. DELISH SOUPE AU CHOIX 60G

![item 11486](classification-review-assets/item-11486.jpg)

- **Category:** Prepared Meals > Salads & Soups (FR: Repas préparés > Salades et soupes)
- **How classified:** rule (`salads-soups`)
- **Price:** 0.79 $ · as printed: “0.79”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 2. AL AFIA MELANGES D'HUILE OLIVE 2L

![item 11489](classification-review-assets/item-11489.jpg)

- **Category:** Pantry > Canned & Pickled (FR: Produits du garde-manger > Produits en conserve et marinés)
- **How classified:** rule (`canned-pickled`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 3. AL AFIA FEUILLE DE VIGNE 45uG

![item 11491](classification-review-assets/item-11491.jpg)

- **Category:** International Foods > Middle Eastern Foods (FR: Aliments internationaux > Aliments du Moyen-Orient)
- **How classified:** rule (`middle-eastern`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 4. SHISH TAOUK AU CHOIX

![item 11492](classification-review-assets/item-11492.jpg)

- **Category:** Meat > Kebabs & Marinated Meat (FR: Viande > Brochettes et viande marinée)
- **How classified:** rule (`kebabs-marinated`)
- **Price:** 15.99 $ · as printed: “15.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 5. MAKDOUCE

![item 11496](classification-review-assets/item-11496.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

### 6. BASTERMA

![item 11487](classification-review-assets/item-11487.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 34.99 $ · as printed: “34.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 7. NAMOURA

![item 11484](classification-review-assets/item-11484.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 14.99 $ · as printed: “14.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 8. HAMMOUD BOISSON AU CHOIX 2L

![item 11490](classification-review-assets/item-11490.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 9. INGREDIENTS INGREDID

![item 11485](classification-review-assets/item-11485.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 0.01 $ · as printed: “2192/20.28”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.97

### 10. LA VACHE QUI RIT FROMAGE u48P

![item 11494](classification-review-assets/item-11494.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 14.99 $ · as printed: “14.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

## Marché Bonanza (`marche-bonanza`)

### 1. CONGELE

![item 10048](classification-review-assets/item-10048.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 2. PQTDE

![item 10057](classification-review-assets/item-10057.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.66 $ · as printed: “6.66”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 3
- **Details:** OCR/extraction confidence: 0.74

### 3. OCCONCIN

![item 10036](classification-review-assets/item-10036.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.29 $ · as printed: “3.29”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 4. NOSHEURES SHA2IH SHA2IH SHA2IH SHA18H SHA1SH SHAISH SHAISH D'OUVERTURE

![item 10051](classification-review-assets/item-10051.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.69 $ · as printed: “3.69”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 5. MUTTI MUTTI

![item 10035](classification-review-assets/item-10035.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.98

### 6. PQTDE

![item 10058](classification-review-assets/item-10058.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 3
- **Details:** OCR/extraction confidence: 0.96

### 7. PAQUIT

![item 10040](classification-review-assets/item-10040.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.79 $ · as printed: “3.79”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 8. CONGELÉ

![item 10047](classification-review-assets/item-10047.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 5.99, 15.99

### 9. AURRA

![item 10055](classification-review-assets/item-10055.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.65 $ · as printed: “6.65”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 3
- **Details:** OCR/extraction confidence: 0.68

### 10. CHAPMANS PREMI

![item 10046](classification-review-assets/item-10046.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-07 → 2026-10-13 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

## Marché Bonichoix (`marche-bonichoix`)

### 1. LAIT ÉVAPORÉ CARNATION EVAPORATED MILK

![item 9673](classification-review-assets/item-9673.jpg)

- **Category:** Dairy & Eggs > Milk & Cream (FR: Produits laitiers et œufs > Lait et crème)
- **How classified:** rule (`milk-cream`)
- **Price:** 49.00 $ · as printed: “49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 2. RIZ PRÉCUIT MINUTE RICE PRECOOKED RICE

![item 9744](classification-review-assets/item-9744.jpg)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 3. CIARK L CLASSIQUE] SIROP D'ÉRABL!

![item 9765](classification-review-assets/item-9765.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 4.49 $ · as printed: “4.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 7
- **Details:** OCR/extraction confidence: 0.99

### 4. MARGARINE À on VEGETABLE OIL _ 468% D'HUILE VÉGÉTALE —

![item 9686](classification-review-assets/item-9686.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

### 5. ZELOCONS DE VIANDE IS AUCISSE VIENNOISE 7 MAPLE LEAF 7 FLAKES OF MEAT OR À VIENNA SAUSAGE

![item 9755](classification-review-assets/item-9755.jpg)

- **Category:** Meat > Sausages (FR: Viande > Saucisses)
- **How classified:** rule (`sausages`)
- **Price:** 86.87 $ · as printed: “86.87”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 7
- **Details:** OCR/extraction confidence: 0.51

### 6. FRUITS DEL MONTE FRUITS

![item 9676](classification-review-assets/item-9676.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 7. BACON PRÉCUIT MAPLE LEAF READY CRISP PRECOOKED BACON

![item 9758](classification-review-assets/item-9758.jpg)

- **Category:** Meat > Bacon (FR: Viande > Bacon)
- **How classified:** rule (`bacon`)
- **Price:** 8.49 $ · as printed: “8.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 7
- **Details:** OCR/extraction confidence: 0.99

### 8. AILES VE PUULE! VU BUULREES = DE POITRINE DE POULET PANÉES SURGELÉES FLAMINGO FROZEN CHICKEN WINGS OR FROZEN

![item 9642](classification-review-assets/item-9642.jpg)

- **Category:** Frozen Food > Frozen Meat and Seafood (FR: Produits surgelés > Viande et fruits de mer surgelés)
- **How classified:** frozen-remap (`chicken-turkey`)
- **Price:** 14.99 $ · as printed: “14.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 9. BARRES VAL NATURE PROTÉINES, SUCRÉES

![item 9634](classification-review-assets/item-9634.jpg)

- **Category:** Pantry > Baking Essentials (FR: Produits du garde-manger > Essentiels de cuisson)
- **How classified:** rule (`baking`)
- **Price:** 2.87 $ · as printed: “2.87”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 10. MAYONNAISE HELLMANN'S MAYONNAISE

![item 9628](classification-review-assets/item-9628.jpg)

- **Category:** Pantry > Condiments (FR: Produits du garde-manger > Condiments et garnitures)
- **How classified:** rule (`condiments`)
- **Price:** 5.97 $ · as printed: “5.97”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

## Marché C&T (`marche-c-t`)

### 1. Squid Rings热

![item 13476](classification-review-assets/item-13476.jpg)

- **Category:** Fish & Seafood > Squid & Octopus (FR: Poissons et fruits de mer > Calmar et pieuvre)
- **How classified:** rule (`squid-octopus`)
- **Price:** 2.50 $ · as printed: “2/5.00”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 4
- **Details:** OCR/extraction confidence: 0.98

### 2. ea/ch ea/ch Nouilles de riz

![item 11559](classification-review-assets/item-11559.jpg)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 0.00 $ · as printed: “2993/4.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.86

### 3. Saucearomatisee aux huitres panda Lkk Panda Oyster

![item 13480](classification-review-assets/item-13480.jpg)

- **Category:** Fish & Seafood > Shellfish (FR: Poissons et fruits de mer > Crustacés)
- **How classified:** rule (`shellfish`)
- **Price:** 45.99 $ · as printed: “45.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 4. Chou chinois nappa Napa Cabbage

![item 13483](classification-review-assets/item-13483.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 25.99 $ · as printed: “25.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 5. NSE'

![item 11560](classification-review-assets/item-11560.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 17.99 $ · as printed: “17.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 6. Citron Lemon

![item 11549](classification-review-assets/item-11549.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 3.51 $ · as printed: “3.51”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 7. Racine Ail Gingembre Patate

![item 13457](classification-review-assets/item-13457.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 3.51 $ · as printed: “3.51”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 3.51

### 8. Reg:1.99 JeuneCanardCongele Frozen Young Duck

![item 11542](classification-review-assets/item-11542.jpg)

- **Category:** Frozen Food > Frozen Meat and Seafood (FR: Produits surgelés > Viande et fruits de mer surgelés)
- **How classified:** frozen-remap (`game-offal`)
- **Price:** 13.99 $ · as printed: “13.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 9. Doré Jaune Pickerel

![item 11539](classification-review-assets/item-11539.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 11.00 $ · as printed: “11.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 10. SeriesdeBiscuits Kimchi de chou A-Taste;Brand Cookies Cabbagekimchi

![item 13469](classification-review-assets/item-13469.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 26.05 $ · as printed: “192/5000.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 2
- **Details:** OCR/extraction confidence: 0.85 · other printed prices: 099.99

## Marché Frutta Si (`frutta-si`)

### 1. Pamplemousse Oranges Grapefruit

![item 11010](classification-review-assets/item-11010.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-13 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.98

### 2. Pomme GoldenetRusset Apple

![item 11936](classification-review-assets/item-11936.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 13.99 $ · as printed: “13.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 3. Pamplemousse Oranges Grapefruit

![item 11003](classification-review-assets/item-11003.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-06 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.98

### 4. Poitrine de poulet desossee Bonelesschickenbreast

![item 11942](classification-review-assets/item-11942.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 3.99

### 5. Cathedral City San Daniele Cheddar

![item 11007](classification-review-assets/item-11007.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-06 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 6. Primo Pate detomate Tomatopaste

![item 11937](classification-review-assets/item-11937.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 18.00 $ · as printed: “3/53.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.86

### 7. Aqua Star Crevette crue Raw shrimp

![item 11945](classification-review-assets/item-11945.jpg)

- **Category:** Fish & Seafood > Shrimp (FR: Poissons et fruits de mer > Crevette)
- **How classified:** rule (`shrimp`)
- **Price:** 66.61 $ · as printed: “66.61”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.97

### 8. Jalsberg Fromage Cheese

![item 11939](classification-review-assets/item-11939.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 9. Orgoglio Tomates entieres peles

![item 11935](classification-review-assets/item-11935.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 10.99 $ · as printed: “10.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 10. del biscotto IRipieni Biscuits noisettes

![item 11946](classification-review-assets/item-11946.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 0.68 $ · as printed: “0.68”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.86

## Marché Fu Tai (`marche-fu-tai`)

### 1. MELON D’HIVERS

![item 13536](classification-review-assets/item-13536.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 0.88 $ · as printed: “0.88”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 2. SAUCE AUX HUITRES DE QUALITE SUPERIEURE A ESISH

![item 13545](classification-review-assets/item-13545.jpg)

- **Category:** Fish & Seafood > Shellfish (FR: Poissons et fruits de mer > Crustacés)
- **How classified:** rule (`shellfish`)
- **Price:** 3.58 $ · as printed: “3.58”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 4
- **Details:** OCR/extraction confidence: 0.96

### 3. INTESTIN DE PORC

![item 10127](classification-review-assets/item-10127.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 2.98 $ · as printed: “2.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.79 · other printed prices: 9

### 4. “CHOCOLAT NESTUE) NESQUIRI

![item 13527](classification-review-assets/item-13527.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 15.88 $ · as printed: “15.88”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 1
- **Details:** OCR/extraction confidence: 0.79

### 5. DE PORC D SOSSÉ

![item 10124](classification-review-assets/item-10124.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 2.98 $ · as printed: “2.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.84

### 6. JARRET DE BOEUF SANS 0S

![item 13540](classification-review-assets/item-13540.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 6.88 $ · as printed: “6.88”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 3
- **Details:** OCR/extraction confidence: 0.95

### 7. CÔTES COURTES DE BŒUF

![item 13542](classification-review-assets/item-13542.jpg)

- **Category:** Meat > Beef (FR: Viande > Bœuf)
- **How classified:** rule (`beef`)
- **Price:** 6.98 $ · as printed: “6.98”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 8. ~~. CHAIR D'HUÎTRE op CUITE CONGELE

![item 10141](classification-review-assets/item-10141.jpg)

- **Category:** Frozen Food > Frozen Meat and Seafood (FR: Produits surgelés > Viande et fruits de mer surgelés)
- **How classified:** frozen-remap (`shellfish`)
- **Price:** 5.58 $ · as printed: “5.58”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 5
- **Details:** OCR/extraction confidence: 0.92

### 9. PANIER DE PE CONCOMBRES/

![item 13532](classification-review-assets/item-13532.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.49 $ · as printed: “2/2.98”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 10. CALAMARS FRAIS

![item 10129](classification-review-assets/item-10129.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.98 $ · as printed: “6.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.95

## Marché Korea (`marche-korea`)

### 1. GOMPYO Farine de blé 곰표 밀가루 2.5KG

![item 11395](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/05/%EA%B3%B0%ED%91%9C-%EB%B0%80%EA%B0%80%EB%A3%A8-2.5kg.png?fit=500%2C500&ssl=1)

- **Category:** Pantry > Baking Essentials (FR: Produits du garde-manger > Essentiels de cuisson)
- **How classified:** rule (`baking`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 8801176101193 · OCR/extraction confidence: 1.00 · regular price 8.99

### 2. JONGGA Rice Cake Sliced Type 순쌀 떡국떡 1KG

![item 11440](https://i0.wp.com/marchekorea.com/wp-content/uploads/2024/12/%EC%88%9C%EC%82%B4.png?fit=500%2C500&ssl=1)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 8801024944552 · OCR/extraction confidence: 1.00 · regular price 6.99

### 3. DONGWON Riz brun germé 쎈쿡 발아현미밥 195G

![item 13587](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/08/%EC%8E%88%EC%BF%A1-%EB%B0%9C%EC%95%84%ED%98%84%EB%AF%B8%EB%B0%A5.png?fit=500%2C500&ssl=1)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** SKU: 8801047170822 · OCR/extraction confidence: 1.00 · regular price 2.99

### 4. RNR Pain aux saveur café 알앤알 커피맛 커피콩빵 90G

![item 13618](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/06/%EC%BB%A4%ED%94%BC%EC%BD%A9%EB%B9%B5-%EC%BB%A4%ED%94%BC.png?fit=500%2C500&ssl=1)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** SKU: 8809716530809 · OCR/extraction confidence: 1.00 · regular price 3.99

### 5. DONGWON Sauce de Topokki Mala 동원 하루미 마라 떡볶이양념 130g

![item 11369](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/06/Black-And-White-Minimalist-Typography-Personal-Logo-500-x-500-px-8-3.png?fit=500%2C500&ssl=1)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 8801047206071 · OCR/extraction confidence: 1.00 · regular price 2.29

### 6. HBAF Mais Souffle Lait Sale HBAF 소금우유 팝콘 80g

![item 13624](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/06/HBAF-%EC%86%8C%EA%B8%88%EC%9A%B0%EC%9C%A0.png?fit=500%2C500&ssl=1)

- **Category:** Snacks, Chips & Candy > Chips & Snacks (FR: Grignotines, croustilles et friandises > Croustilles et grignotines)
- **How classified:** rule (`specific-popcorn`)
- **Price:** 1.50 $ · as printed: “1.50”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** SKU: 8800279450252 · OCR/extraction confidence: 1.00 · regular price 2.79

### 7. WOOMTREE Mélange à friture de tempura 움트리 튀김가루 1kg

![item 11310](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/09/%EC%9B%80%ED%8A%B8%EB%A6%AC-%ED%8A%80%EA%B9%80%EA%B0%80%EB%A3%A8.png?fit=500%2C500&ssl=1)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 8801558202128 · OCR/extraction confidence: 1.00 · regular price 4.99

### 8. DONGWON Sweet Redbean Porridge with Chestnuts 밤단팥죽 285G

![item 11443](https://i0.wp.com/marchekorea.com/wp-content/uploads/2024/12/%EB%B0%A4%EB%8B%A8%ED%8C%A5%EC%A3%BD.png?fit=500%2C500&ssl=1)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 8801047161653 · OCR/extraction confidence: 1.00 · regular price 3.99

### 9. ITOEN Iced Jasmine Green Tea 500ML

![item 13628](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/06/%EA%B3%A8%EB%93%A0-%EC%9E%90%EC%8A%A4%EB%AF%BC.png?fit=500%2C500&ssl=1)

- **Category:** Drinks > Tea & Hot Drinks (FR: Boissons > Thés et boissons chaudes)
- **How classified:** rule (`tea-hot-drinks`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** SKU: 835143006950 · OCR/extraction confidence: 1.00 · regular price 3.49

### 10. CG Mini maïs classique 클래식농원 미니 찰옥수수 300g

![item 11374](https://i0.wp.com/marchekorea.com/wp-content/uploads/2026/06/124.png?fit=500%2C500&ssl=1)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 8809446420883 · OCR/extraction confidence: 1.00 · regular price 4.29

## Marché Lian Tai (`marche-lian-tai`)

### 1. BANANE FRITE CONGELÉE

![item 13679](http://f.wishabi.net/page_items/437388884/1792043892/extra_large.jpg)

- **Category:** Frozen Food > Frozen Fruit & Vegetables (FR: Produits surgelés > Fruits et légumes surgelés)
- **How classified:** frozen-remap (`fruits`)
- **Price:** 88.00 $ · as printed: “88.0”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 2. CREVETTES BLANCHES P&D CR

![item 13711](http://f.wishabi.net/page_items/437388803/1792043902/extra_large.jpg)

- **Category:** Fish & Seafood > Shrimp (FR: Poissons et fruits de mer > Crevette)
- **How classified:** rule (`shrimp`)
- **Price:** 5.28 $ · as printed: “5.28”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Cool Ocean · OCR/extraction confidence: 1.00

### 3. MAQUEREAU FRAÎCHE

![item 13725](http://f.wishabi.net/page_items/437388646/1792043895/extra_large.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 2.98 $ · as printed: “2.98”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 4. BISCUIT AUX AMANDES

![item 4553](http://f.wishabi.net/page_items/436836581/1791438986/extra_large.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 7.88 $ · as printed: “7.88”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 5. ALGUES SÉCHÉE ASSAISONNÉE

![item 4504](http://f.wishabi.net/page_items/436836536/1791438983/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 7.98 $ · as printed: “7.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: WANG KOREA · OCR/extraction confidence: 1.00

### 6. CRABES BLEUS VIVANTS

![item 13695](http://f.wishabi.net/page_items/437388485/1792043903/extra_large.jpg)

- **Category:** Fish & Seafood > Shellfish (FR: Poissons et fruits de mer > Crustacés)
- **How classified:** rule (`shellfish`)
- **Price:** 1.98 $ · as printed: “1.98”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 7. DUMPLINGS DE CREVETTES ET DE PORC

![item 4583](http://f.wishabi.net/page_items/436836481/1791438976/extra_large.jpg)

- **Category:** Fish & Seafood > Shrimp (FR: Poissons et fruits de mer > Crevette)
- **How classified:** rule (`shrimp`)
- **Price:** 5.98 $ · as printed: “5.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: CHEF SHUO · OCR/extraction confidence: 1.00

### 8. NOIX GRILLÉE

![item 13701](http://f.wishabi.net/page_items/437388820/1792043901/extra_large.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 4.98 $ · as printed: “4.98”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: SUN FUNG · OCR/extraction confidence: 1.00

### 9. SÉRIES DE SAUCISSES RED 'N JUICY

![item 4569](http://f.wishabi.net/page_items/436836602/1791438982/extra_large.jpg)

- **Category:** Meat > Sausages (FR: Viande > Saucisses)
- **How classified:** rule (`sausages`)
- **Price:** 8.88 $ · as printed: “8.88”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: RED 'N JUICY · OCR/extraction confidence: 1.00

### 10. RAISINS KYOHO

![item 4588](http://f.wishabi.net/page_items/436836482/1791438977/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 9.98 $ · as printed: “9.98”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

## Marché Newon (`marche-newon`)

### 1. POITRINE DE PORC PORK BELLY/ #8 ty

![item 10155](classification-review-assets/item-10155.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 3.48 $ · as printed: “3.48”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 1
- **Details:** OCR/extraction confidence: 0.77

### 2. SUPER-Q. NOUILLE DE | FECULE DE MAIS CORNSTARCH STICKS/

![item 13768](classification-review-assets/item-13768.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.25 $ · as printed: “4/5.00”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 3. MALVLIFLD JLE LE POIVRE/LARGE/ | SALTAND PEPPER

![item 10191](classification-review-assets/item-10191.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.79

### 4. HYGRADE. SALICISSES FUMES. SMOKED SAUSAGE/BBO/ ORIGINAL /450G

![item 13790](classification-review-assets/item-13790.jpg)

- **Category:** Meat > Sausages (FR: Viande > Saucisses)
- **How classified:** rule (`sausages`)
- **Price:** 88.00 $ · as printed: “88”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 5. MELON D'HIVER WINTER MELONÆ/T

![item 10233](classification-review-assets/item-10233.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 68.00 $ · as printed: “68”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.99

### 6. AILEDE POULET CHICKEN WINGS

![item 13802](classification-review-assets/item-13802.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 2.69 $ · as printed: “2.69”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 4
- **Details:** OCR/extraction confidence: 0.80

### 7. PILONS DE POULE FRITES f FRIED CHICKEN DRUMSTICKS

![item 10195](classification-review-assets/item-10195.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.88

### 8. CALAMAR FRAIS FRESH SQUID/

![item 10157](classification-review-assets/item-10157.jpg)

- **Category:** Fish & Seafood > Squid & Octopus (FR: Poissons et fruits de mer > Calmar et pieuvre)
- **How classified:** rule (`squid-octopus`)
- **Price:** 6.98 $ · as printed: “6.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 1
- **Details:** OCR/extraction confidence: 0.90

### 9. FOODIEJOIE TREMELLE EN FUSEAU

![item 10260](classification-review-assets/item-10260.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.98 $ · as printed: “3.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 10. G2W.RIZ SUCRE SUPERIEUR

![item 10217](classification-review-assets/item-10217.jpg)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 58.00 $ · as printed: “58”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

## Marché Richelieu (`marche-richelieu`)

### 1. Découvrez notre offre de fromages

![item 4838](http://f.wishabi.net/page_items/436171119/1790832571/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 2. AMUSE-GUEULE ROLD GOLD | ROLD GOLD SNACKS

![item 13925](http://f.wishabi.net/page_items/436667657/1791359122/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Chips & Snacks (FR: Grignotines, croustilles et friandises > Croustilles et grignotines)
- **How classified:** rule (`chips-snacks`)
- **Price:** 8.50 $ · as printed: “8.5”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Rold Gold · OCR/extraction confidence: 1.00

### 3. CÔTES DE DOS DE PORC CUITES IRRÉSISTIBLE | IRRÉSISTIBLE COOKED PORK BACK RIBS

![item 13878](http://f.wishabi.net/page_items/436667575/1791359125/extra_large.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 10.99 $ · as printed: “10.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Irresistible · OCR/extraction confidence: 1.00

### 4. EAU DE SOURCE SELECTION | SELECTION SPRING WATER

![item 13881](http://f.wishabi.net/page_items/436667660/1791359124/extra_large.jpg)

- **Category:** Drinks > Water (FR: Boissons > Eau)
- **How classified:** rule (`water`)
- **Price:** 1.79 $ · as printed: “1.79”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Selection · OCR/extraction confidence: 1.00

### 5. SAUMON SAUVAGE DU PACIFIQUE COUPES DU MARCHÉ HIGH LINER | HIGH LINER MARKET CUTS WILD PACIFIC SALMON

![item 13862](http://f.wishabi.net/page_items/436667585/1791359122/extra_large.jpg)

- **Category:** Fish & Seafood > Salmon (FR: Poissons et fruits de mer > Saumon)
- **How classified:** rule (`salmon`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: HIGH LINER® · OCR/extraction confidence: 1.00

### 6. tomates Selection | Selection tomatoes

![item 4914](http://f.wishabi.net/page_items/436171216/1790832576/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.19 $ · as printed: “2.19”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Selection · OCR/extraction confidence: 1.00

### 7. crème de tomates Campbell's | Campbell's tomato cream

![item 4897](http://f.wishabi.net/page_items/436171178/1790832567/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Campbell's · OCR/extraction confidence: 1.00

### 8. ESCALOPES DE VEAU FAMILLE FONTAINE | FONTAINE FAMILY VEAL CUTLETS

![item 4863](http://f.wishabi.net/page_items/436171135/1790832576/extra_large.jpg)

- **Category:** Meat > Lamb & Veal (FR: Viande > Agneau et veau)
- **How classified:** rule (`lamb-veal`)
- **Price:** 24.99 $ · as printed: “24.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 9. GROSSE MANGUE ROUGE | LARGE RED MANGO

![item 13849](http://f.wishabi.net/page_items/436667613/1791359122/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.79 $ · as printed: “2.79”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 10. CAPSULES DE CAFÉ STARBUCKS | STARBUCKS CAPSULES

![item 4821](http://f.wishabi.net/page_items/436171189/1790832575/extra_large.jpg)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** 12.99 $ · as printed: “12.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

## Marché Sheng Tai (`marche-sheng-tai`)

### 1. "GÂTEAUAU)DURIAN) MUSANG KING] NES

![item 10280](classification-review-assets/item-10280.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.25 $ · as printed: “2/4.50”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.97

### 2. AUGUESIGRILUÉES POURISUSHI[COREEN

![item 10281](classification-review-assets/item-10281.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.00 $ · as printed: “2/2.00”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 2
- **Details:** OCR/extraction confidence: 0.92

### 3. NOUILLES COREENNES D. EPICEES AU POULET SERGE | REG: 8.90

![item 10315](classification-review-assets/item-10315.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 3.68 $ · as printed: “3.68”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.86

### 4. SERIES © D'AUBEPINES CONFITES VKHBEAP AI

![item 10266](classification-review-assets/item-10266.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.98 $ · as printed: “3.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 1
- **Details:** OCR/extraction confidence: 0.69

### 5. > VIEILLE NOIX DE COCO

![item 13952](classification-review-assets/item-13952.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 1.49 $ · as printed: “2/2.98”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 6. “RIZ'ERIT AVEC “MeHARICOTS NEY NERTS RÉG.: 4.99

![item 10291](classification-review-assets/item-10291.jpg)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 4.98 $ · as printed: “4.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 7. TOFU TAMAGO

![item 13942](classification-review-assets/item-13942.jpg)

- **Category:** Meat > Plant-Based Meat Alternatives (FR: Viande > Substituts de viande à base de plantes)
- **How classified:** rule (`plant-based-meat`)
- **Price:** 0.58 $ · as printed: “0.58”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 2
- **Details:** OCR/extraction confidence: 0.89

### 8. BOULE DE SÉSAME EN PATE DE

![item 13927](classification-review-assets/item-13927.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 3.48 $ · as printed: “3.48”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 1
- **Details:** OCR/extraction confidence: 0.77

### 9. CRABE COUPÉ CONGELÉ

![item 10268](classification-review-assets/item-10268.jpg)

- **Category:** Frozen Food > Frozen Meat and Seafood (FR: Produits surgelés > Viande et fruits de mer surgelés)
- **How classified:** frozen-remap (`shellfish`)
- **Price:** 17.98 $ · as printed: “17.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 1
- **Details:** OCR/extraction confidence: 0.74

### 10. CHOCO PIE SL VAD |e RÉG.: 5.49+TX

![item 10312](classification-review-assets/item-10312.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 10.98 $ · as printed: “10.98”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.60

## Marché Sultan (`marche-sultan`)

### 1. FORMULECONCENTREE Selection

![item 11467](classification-review-assets/item-11467.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.66 $ · as printed: “1.66”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 2. Tahini

![item 11457](classification-review-assets/item-11457.jpg)

- **Category:** Pantry > Honey, Syrups & Spreads (FR: Produits du garde-manger > Miel, sirops et tartinades)
- **How classified:** rule (`honey-spreads`)
- **Price:** 7.49 $ · as printed: “7.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 6.66

### 3. Sukay

![item 11466](classification-review-assets/item-11466.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 4. ROMAINE Hearts

![item 11470](classification-review-assets/item-11470.jpg)

- **Category:** Fruits & Vegetables > Packaged Salads & Dressing (FR: Fruits et légumes > Salades préemballées et vinaigrettes)
- **How classified:** rule (`packaged-salads`)
- **Price:** 2.49 $ · as printed: “2.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.89

### 5. VIERGE

![item 11475](classification-review-assets/item-11475.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 66.91 $ · as printed: “66.91”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.86 · other printed prices: 13.99

### 6. COOHSm6.mUTES

![item 11471](classification-review-assets/item-11471.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 7. PHOENICIA

![item 11473](classification-review-assets/item-11473.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.49 $ · as printed: “2.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 5
- **Details:** OCR/extraction confidence: 0.93 · other printed prices: 1.99

### 8. YEA

![item 11479](classification-review-assets/item-11479.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 6
- **Details:** OCR/extraction confidence: 0.91 · other printed prices: 4.99

### 9. FARINI IRICMAE

![item 11455](classification-review-assets/item-11455.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.90

### 10. Tarhana Cipsi

![item 11459](classification-review-assets/item-11459.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.66 $ · as printed: “6.66”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 1
- **Details:** OCR/extraction confidence: 0.94 · other printed prices: 7.49

## Maxi (`maxi`)

### 1. VIN WALLAROO TRAIL ROUGE OU BLANC, 4 L

![item 14059](https://f.wishabi.net/page_pdf_images/24270272/de067f74-c294-11f1-a088-42a364ddfdee/x_large)

- **Category:** Beer & Wine > Wine (FR: Bières et vins > Vins)
- **How classified:** rule (`wine`)
- **Price:** 44.00 $ · as printed: “44.00”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: WALLAROO TRAIL · SKU: 21105607_EA · OCR/extraction confidence: 1.00 · “en magasin”

### 2. NOURRITURE HUMIDE POUR CHATS FRISKIES, 32 un.

![item 325](https://f.wishabi.net/page_pdf_images/24243273/d93eef6a-bddc-11f1-bb51-aab2a51a417c/x_large)

- **Category:** Pet > Pet Food (FR: Animaux > Nourriture pour animaux)
- **How classified:** rule (`pet`)
- **Price:** 28.50 $ · as printed: “28.50”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Friskies · SKU: 21186868_C01 · OCR/extraction confidence: 1.00 · “certaines variétés”

### 3. PURÉE DE MANGUE QUALITY | MANGO PULP, 850 G

![item 14126](https://f.wishabi.net/page_pdf_images/24270222/8c7a8a98-c293-11f1-aab8-8282a61c6b19/x_large)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Quality · SKU: 20670426001_EA · OCR/extraction confidence: 1.00 · “Certaines variétés selected varieties”

### 4. BONBONS MEGA MONDOUX, 1,5 kg

![item 52](https://f.wishabi.net/page_pdf_images/24243262/d44056f2-bddc-11f1-92b0-5666795408c2/x_large)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 14.99 $ · as printed: “14.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: MONDOUX · SKU: 21451401_EA · OCR/extraction confidence: 1.00

### 5. EAU DE SOURCE NATURELLE NAYA, 28X500 ML

![item 14194](https://f.wishabi.net/page_pdf_images/24270272/d7b26ef8-c294-11f1-a088-42a364ddfdee/x_large)

- **Category:** Drinks > Water (FR: Boissons > Eau)
- **How classified:** rule (`water`)
- **Price:** 4.77 $ · as printed: “4.77”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** SKU: 20122584_C28 · OCR/extraction confidence: 1.00 · “Consigne”

### 6. BARRES FORMAT COLLATION ASSORTIES ET FRIANDISES NESTLÉ, 12 UN.

![item 14200](https://f.wishabi.net/page_pdf_images/24270231/95f4179c-c293-11f1-bb13-c6d122032495/x_large)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Nestle · OCR/extraction confidence: 1.00

### 7. SOUS-MARINS POL-O-BIC, 720 G

![item 14064](https://f.wishabi.net/page_pdf_images/24270218/897c4a70-c293-11f1-b679-2e599553d05e/x_large)

- **Category:** Prepared Meals > Sandwiches (FR: Repas préparés > Sandwichs)
- **How classified:** rule (`sandwiches`)
- **Price:** 9.55 $ · as printed: “9.55”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: POL-O-BIC · SKU: 21359609_EA · loyalty-gated price · OCR/extraction confidence: 1.00 · “Certaines Variétés”

### 8. CORIANDRE | CILANTRO

![item 97](https://f.wishabi.net/page_pdf_images/24243280/de5d88c6-bddc-11f1-b56a-1e61a36b3d67/x_large)

- **Category:** Fruits & Vegetables > Herbs (FR: Fruits et légumes > Fines herbes)
- **How classified:** rule (`herbs-fresh`)
- **Price:** 1.79 $ · as printed: “1.79”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 20091825001_EA · OCR/extraction confidence: 1.00 · “produit du Canada product of Canada”

### 9. DARNE DE THON JAUNE SAUVAGE, 92 G OU SAUMON STEELHEAD, FUMÉ 50 G

![item 14171](https://f.wishabi.net/page_pdf_images/24270215/87fe97e8-c293-11f1-a260-f22ab89aad65/x_large)

- **Category:** Fish & Seafood > Salmon (FR: Poissons et fruits de mer > Saumon)
- **How classified:** rule (`salmon`)
- **Price:** 2.00 $ · as printed: “2.00”
- **Flyer validity:** 2026-10-01 → 2026-10-30
- **Details:** SKU: 21694839_EA · OCR/extraction confidence: 1.00 · “certaines variétés, surgelés”

### 10. GARNITURE POUR TARTE 540 ML OU PURÉE DE CITROUILLE 796 ML E. D. SMITH

![item 218](https://f.wishabi.net/page_pdf_images/24243302/e02f4766-bddc-11f1-a95e-26445e70e673/x_large)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 4.50 $ · as printed: “4.50”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: E.D. SMITH · SKU: 20297753001_EA · OCR/extraction confidence: 1.00 · “certaines variétés”

## Mayrand Food Group (`mayrand`)

### 1. PAMILYPARMS ANELIALS

![item 11534](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=6)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 19.99 $ · as printed: “19.99”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 6
- **Details:** OCR/extraction confidence: 0.98

### 2. BIG

![item 11519](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=3)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 3. Simonne Frozen

![item 11523](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=4)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 4
- **Details:** OCR/extraction confidence: 0.97

### 4. San Marzano CATEGORIE DE CHOIX Tomates

![item 11528](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=5)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 8.49 $ · as printed: “8.49”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 5. 2.00$/each

![item 11503](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=1)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.00 $ · as printed: “2/4.00”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 6. Reg.price:29.99$/kg

![item 11513](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=2)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 13.60 $ · as printed: “13.60”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 2
- **Details:** OCR/extraction confidence: 0.94

### 7. Fresh

![item 11502](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=1)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.59 $ · as printed: “6.59”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 1
- **Details:** OCR/extraction confidence: 0.98

### 8. 2.00$/each

![item 11518](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=3)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.00 $ · as printed: “2/4.00”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 9. FRAIS

![item 11504](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=1)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 11.49 $ · as printed: “11.49”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 1
- **Details:** OCR/extraction confidence: 0.81

### 10. GRILL-X

![item 11533](https://mayrand.ca/hubfs/Circulaire%20du%2014%20au%2020%20octobre%202026%20EN%20VFF.pdf#page=6)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 8.49 $ · as printed: “8.49”
- **Flyer validity:** 2026-10-14 → 2026-10-20 · flyer page 6
- **Details:** OCR/extraction confidence: 0.98

## Metro (`metro`)

### 1. BEIGNES

![item 14252](http://f.wishabi.net/page_items/436825612/1791489069/extra_large.jpg)

- **Category:** Bakery > Cookies, Muffins & Desserts (FR: Boulangerie > Biscuits, muffins et desserts)
- **How classified:** rule (`bakery-cookies-muffins`)
- **Price:** 6.49 $ · as printed: “6.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 2. PRUNEAUX DÉNOYAUTÉS IRRÉSISTIBLE | IRRÉSISTIBLE PITTED PRUNES

![item 6003](http://f.wishabi.net/page_items/436826005/1791488259/extra_large.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 10.99 $ · as printed: “10.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 3. CROISSANTS 100 % BEURRE | 100% BUTTER CROISSANTS

![item 14256](http://f.wishabi.net/page_items/436825613/1791489070/extra_large.jpg)

- **Category:** Bakery > Bagels, Croissants & English Muffins (FR: Boulangerie > Bagels, croissants et muffins anglais)
- **How classified:** rule (`specific-audit-fixes`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 4. GROS ANANAS TROPICAL GOLD, ANANAS DÉCORTIQUÉ | TROPICAL GOLD LARGE PINEAPPLE OR CORED PINEAPPLE

![item 6556](http://f.wishabi.net/page_items/436189015/1790831099/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 5. RAISINS SULTANA IRRÉSISTIBLE | IRRÉSISTIBLE SULTANA RAISINS

![item 6002](http://f.wishabi.net/page_items/436826003/1791488258/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 6. PAMPLEMOUSSE ROSE BIOLOGIQUE

![item 6006](http://f.wishabi.net/page_items/436826010/1791488262/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 2.77 $ · as printed: “2.77”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 7. GOÛTER AU POUDING KOZY SHACK | KOZY SHACK PUDDING CUPS

![item 6369](http://f.wishabi.net/page_items/436191243/1791211420/extra_large.jpg)

- **Category:** Dairy & Eggs > Desserts & Doughs (FR: Produits laitiers et œufs > Desserts et pâtes)
- **How classified:** rule (`dairy-desserts-doughs`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 8. PÂTÉS IMPÉRIAUX WONG WING | WONG WING FROZEN EGG ROLLS

![item 6492](http://f.wishabi.net/page_items/436191298/1791211277/extra_large.jpg)

- **Category:** Frozen Food > Frozen Meals, Entrees & Sides (FR: Produits surgelés > Repas, plats principaux et accompagnements)
- **How classified:** frozen-remap (`deli-meat`)
- **Price:** 16.00 $ · as printed: “16.0”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 9. FÈVES AU LARD CLARK | CLARK PORK AND BEANS

![item 6047](http://f.wishabi.net/page_items/436825906/1791442103/extra_large.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 2.29 $ · as printed: “2.29”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 10. MOUTARDE MAILLE | MAILLE MUSTARD

![item 6353](http://f.wishabi.net/page_items/436191342/1791211394/extra_large.jpg)

- **Category:** Pantry > Condiments (FR: Produits du garde-manger > Condiments et garnitures)
- **How classified:** rule (`condiments`)
- **Price:** 8.49 $ · as printed: “8.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

## Metro Plus (`metro-plus`)

### 1. LAITUE DUO GEN V | GEN V DUO LETTUCE

![item 8851](http://f.wishabi.net/page_items/436825675/1791442104/extra_large.jpg)

- **Category:** Fruits & Vegetables > Packaged Salads & Dressing (FR: Fruits et légumes > Salades préemballées et vinaigrettes)
- **How classified:** rule (`packaged-salads`)
- **Price:** 3.98 $ · as printed: “3.98”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 2. POMMES CORTLAND, MCINTOSH, SPARTAN OU EMPIRE | APPLES

![item 8952](http://f.wishabi.net/page_items/436825733/1791442104/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 3. CRETONS GASPÉSIEN | GASPÉSIEN CRETONS

![item 9327](http://f.wishabi.net/page_items/436189331/1790831095/extra_large.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 5.49 $ · as printed: “5.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 4. SALADE SELECTION | SELECTION SALAD

![item 9207](http://f.wishabi.net/page_items/436193264/1791209755/extra_large.jpg)

- **Category:** Prepared Meals > Salads & Soups (FR: Repas préparés > Salades et soupes)
- **How classified:** rule (`salads-soups`)
- **Price:** 6.00 $ · as printed: “6.0”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 5. PÊCHES, PAMPLEMOUSSES, MANDARINES OU MÉLANGE DE CERISES TRUE FRUIT | TRUE FRUIT FRUITS

![item 9476](http://f.wishabi.net/page_items/436191323/1791211353/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 9.99 $ · as printed: “9.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 6. TARTINADE LOTUS BISCOFF | LOTUS BISCOFF SPREAD

![item 9391](http://f.wishabi.net/page_items/436826182/1791433297/extra_large.jpg)

- **Category:** Pantry > Honey, Syrups & Spreads (FR: Produits du garde-manger > Miel, sirops et tartinades)
- **How classified:** rule (`honey-spreads`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 7. BARRES DE CHOCOLAT NESTLÉ | NESTLÉ CHOCOLATE BARS

![item 9095](http://f.wishabi.net/page_items/436825936/1791442103/extra_large.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 8. GROS ANANAS TROPICAL GOLD

![item 8859](http://f.wishabi.net/page_items/436825715/1791488226/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 9. SAUCISSES PORC-BOEUF LAFLEUR | LAFLEUR PORK-BEEF SAUSAGES

![item 9031](http://f.wishabi.net/page_items/436825673/1791442102/extra_large.jpg)

- **Category:** Meat > Sausages (FR: Viande > Saucisses)
- **How classified:** rule (`sausages`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 10. NOIX DE MACADAMIA CRUES IRRÉSISTIBLE | IRRRÉSISTIBLE RAW MACADAMIA NUTS

![item 9293](http://f.wishabi.net/page_items/436191321/1791211351/extra_large.jpg)

- **Category:** Fruits & Vegetables > Dried Fruits & Nuts (FR: Fruits et légumes > Fruits séchés et noix)
- **How classified:** rule (`dried-fruits-nuts`)
- **Price:** 9.99 $ · as printed: “9.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

## Milano Fruiterie (`milano-fruiterie`)

### 1. POIREAUX

![item 11124](classification-review-assets/item-11124.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.89

### 2. POIRE ROCHA PORTUGAL

![item 11115](classification-review-assets/item-11115.jpg)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 19.90 $ · as printed: “19.90”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 1.99

### 3. BROCHETTE DE LEGUMES MARINÉS

![item 11122](classification-review-assets/item-11122.jpg)

- **Category:** Meat > Kebabs & Marinated Meat (FR: Viande > Brochettes et viande marinée)
- **How classified:** rule (`kebabs-marinated`)
- **Price:** 1.69 $ · as printed: “1.69”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.94 · other printed prices: 16.90

### 4. TOMATES ENTIÈRE PELÉES LA SAN MARZANO

![item 11118](classification-review-assets/item-11118.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 2.99 $ · as printed: “2.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.87

### 5. JAMBON SERRANO 24 MOIS PRODUIT ESPAGNOL

![item 11113](classification-review-assets/item-11113.jpg)

- **Category:** Meat > Pork & Ham (FR: Viande > Porc et jambon)
- **How classified:** rule (`pork-ham`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.85 · other printed prices: 69.90

### 6. RÔTI DE PALETTE

![item 11121](classification-review-assets/item-11121.jpg)

- **Category:** International Foods > South Asian Foods (FR: Aliments internationaux > Aliments de l'Asie du Sud)
- **How classified:** rule (`south-asian`)
- **Price:** 24.99 $ · as printed: “24.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.90

### 7. FOURCHEESERISOTTO TRUFFLERISOTTO

![item 11112](classification-review-assets/item-11112.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 4.99 $ · as printed: “4.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.95

### 8. PECORINO ROMANO PRODUIT ITALIEN

![item 11120](classification-review-assets/item-11120.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 3.59 $ · as printed: “3.59”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.87 · other printed prices: 35.90

### 9. PRINCIPE MORTADELLA PISTACHE

![item 11116](classification-review-assets/item-11116.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.59 $ · as printed: “2.59”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.90 · other printed prices: 25.90

### 10. HUILEO'OLIVE EXTRAVIERGE EXTRAVIRGIN OLIVEOIL

![item 11110](classification-review-assets/item-11110.jpg)

- **Category:** Pantry > Canned & Pickled (FR: Produits du garde-manger > Produits en conserve et marinés)
- **How classified:** rule (`canned-pickled`)
- **Price:** 39.99 $ · as printed: “39.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 1
- **Details:** OCR/extraction confidence: 0.93

## Odessa Poissonnier (`odessa-poissonnier`)

### 1. L'ENSEMBLE D'OUVERTURE À HUÎTRES

![item 10974](classification-review-assets/item-10974.jpg)

- **Category:** Fish & Seafood > Shellfish (FR: Poissons et fruits de mer > Crustacés)
- **How classified:** rule (`shellfish`)
- **Price:** 29.99 $ · as printed: “29.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 4
- **Details:** OCR/extraction confidence: 0.90

### 2. ARGENTINE | ARGENTINA

![item 10986](classification-review-assets/item-10986.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** store-prior
- **Price:** 17.99 $ · as printed: “17.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 8
- **Details:** OCR/extraction confidence: 0.93 · other printed prices: 3.96

### 3. PLANCHE À HUÎTRES

![item 10972](classification-review-assets/item-10972.jpg)

- **Category:** Fish & Seafood > Shellfish (FR: Poissons et fruits de mer > Crustacés)
- **How classified:** rule (`shellfish`)
- **Price:** 16.99 $ · as printed: “16.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 4
- **Details:** OCR/extraction confidence: 0.81

### 4. ÎLES-DE-LA-MADELEINE | MAGDALEN ISLANDS

![item 10979](classification-review-assets/item-10979.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** store-prior
- **Price:** 59.98 $ · as printed: “59.98”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 6
- **Details:** OCR/extraction confidence: 0.85 · other printed prices: 9.98

### 5. ÎLES-DE-LA-MADELEINE | MAGDALEN ISLANDS

![item 10970](classification-review-assets/item-10970.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** store-prior
- **Price:** 1.69 $ · as printed: “1.69”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 3
- **Details:** OCR/extraction confidence: 0.80 · other printed prices: 29.99, 1.67

### 6. KIKKOMAN

![item 10993](classification-review-assets/item-10993.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** store-prior
- **Price:** 5.49 $ · as printed: “5.49”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 12
- **Details:** OCR/extraction confidence: 0.90

### 7. FILET DE FLÉTAN

![item 10977](classification-review-assets/item-10977.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 72.73 $ · as printed: “72.73”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 5
- **Details:** OCR/extraction confidence: 0.83

### 8. AZUME

![item 10991](classification-review-assets/item-10991.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** store-prior
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 11
- **Details:** OCR/extraction confidence: 0.86

### 9. ASSIETTE DE CREVETTES D'ARGENTINE

![item 10987](classification-review-assets/item-10987.jpg)

- **Category:** Fish & Seafood > Shrimp (FR: Poissons et fruits de mer > Crevette)
- **How classified:** rule (`shrimp`)
- **Price:** 24.99 $ · as printed: “24.99”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 9
- **Details:** OCR/extraction confidence: 0.85

### 10. ROULEAUX IMPERIAUX HOMARD ET CREVETTE

![item 10988](classification-review-assets/item-10988.jpg)

- **Category:** Fish & Seafood > Shrimp (FR: Poissons et fruits de mer > Crevette)
- **How classified:** rule (`shrimp`)
- **Price:** 0.00 $ · as printed: “15998/4.00”
- **Flyer validity:** 2026-10-08 → 2026-10-21 · flyer page 10
- **Details:** OCR/extraction confidence: 0.74 · other printed prices: 1.00

## Pharmaprix (`pharmaprix`)

### 1. L. Tampons composés à 100 % de fibres biologiques 100% Organic Tampons (18), KOTEX protège-dessous (68 - 240) ou serviettes (20 - 44)

![item 5356](http://f.wishabi.net/page_items/436041402/1790796912/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** OCR/extraction confidence: 1.00

### 2. LIFE BRAND Calcium Antacid Tablets

![item 5077](http://f.wishabi.net/page_items/436043090/1790796944/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** brand: Life Brand · OCR/extraction confidence: 1.00

### 3. LIFE BRAND Pansements

![item 5464](http://f.wishabi.net/page_items/436043087/1790796942/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** brand: Life Brand · OCR/extraction confidence: 1.00

### 4. HARIBO Friandises (170 g - 175 g)

![item 5229](http://f.wishabi.net/page_items/436043615/1790796935/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 7.00 $ · as printed: “7.0”
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** brand: Haribo · OCR/extraction confidence: 1.00

### 5. BISQUICK Mélange 1.13 kg ou QUAKER gruau instantané

![item 14472](http://f.wishabi.net/page_items/437026007/1791598969/extra_large.jpg)

- **Category:** Pantry > Cereal & Breakfast (FR: Produits du garde-manger > Céréales et petits-déjeuners)
- **How classified:** rule (`cereal-breakfast`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-17 → 2026-10-22
- **Details:** OCR/extraction confidence: 1.00

### 6. BUBBLE T. CALGON ou KERI Produits pour le bain

![item 4924](http://f.wishabi.net/page_items/436044560/1790796961/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** brand: Calgon · OCR/extraction confidence: 1.00

### 7. GILLETTE VENUS Tondeuse douce pour la peau et les poils pubiens

![item 5192](http://f.wishabi.net/page_items/436044103/1790796931/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 51.99 $ · as printed: “51.99”
- **Flyer validity:** 2026-10-10 → 2026-10-16
- **Details:** brand: Gillette · OCR/extraction confidence: 1.00

### 8. STARBUCKS Cartouches de café K-Cup (10), NABOB ou STARBUCKS café moulu (340 g)

![item 14471](http://f.wishabi.net/page_items/437026005/1791598968/extra_large.jpg)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-17 → 2026-10-22
- **Details:** OCR/extraction confidence: 1.00

### 9. WHISPS Croustilles au fromage

![item 14569](http://f.wishabi.net/page_items/437026020/1791598977/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-17 → 2026-10-22
- **Details:** brand: Whisps · OCR/extraction confidence: 1.00

### 10. COCA-COLA ou PEPSI Boissons (2 L)

![item 14407](http://f.wishabi.net/page_items/437025666/1791598988/extra_large.jpg)

- **Category:** Drinks > Soft Drinks (FR: Boissons > Boissons gazeuses)
- **How classified:** rule (`soft-drinks`)
- **Price:** 3.19 $ · as printed: “3.19”
- **Flyer validity:** 2026-10-17 → 2026-10-22
- **Details:** OCR/extraction confidence: 1.00

## Provigo (`provigo`)

### 1. LANIÈRES DE POULET À LA CORÉENNE, 361-530 G | KOREAN CHICKEN STRIPS

![item 14583](https://f.wishabi.net/page_pdf_images/24279167/925fd7b2-c3f9-11f1-b0af-52bcfe54fe95/x_large)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 9.00 $ · as printed: “9.00”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: WHERE FLAVOUR MEETS GREAT CHICKEN · SKU: 21022536_EA · OCR/extraction confidence: 1.00 · “COMBO INDIVIDUEL DE 6 MORCEAUX DE POULET AVEC POMMES DE TERRE EN QUARTIERS CERTAINES VARIÉTÉS”

### 2. HUILE D'OLIVE SANS NOM® | NO NAME® OLIVE OIL, 750 ML

![item 927](https://f.wishabi.net/page_pdf_images/24242914/955ec8a0-bdd8-11f1-8fd6-d6b8222fe362/x_large)

- **Category:** Pantry > Canned & Pickled (FR: Produits du garde-manger > Produits en conserve et marinés)
- **How classified:** rule (`canned-pickled`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: SANS NOM · SKU: 20047715_EA · OCR/extraction confidence: 1.00 · “CERTAINES VARIÉTÉS”

### 3. MAGRET DE CANARD | DUCK BREAST MAGRET

![item 953](https://f.wishabi.net/page_pdf_images/24242916/a63f449c-bdd8-11f1-8135-964e96f5df87/x_large)

- **Category:** Meat > Game Meat, Offals & Fowl (FR: Viande > Viande exotique)
- **How classified:** rule (`game-offal`)
- **Price:** 17.00 $ · as printed: “17.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 20106206_KG · OCR/extraction confidence: 1.00 · “37,48/KG”

### 4. PIZZA PC COLLECTION NOIRE | PC® BLACK LABEL PIZZA, 370-440 G

![item 957](https://f.wishabi.net/page_pdf_images/24242919/952582fc-bdd8-11f1-af65-2af86f0adfcd/x_large)

- **Category:** Prepared Meals > Pizza (FR: Repas préparés > Pizzas)
- **How classified:** rule (`pizza-prepared`)
- **Price:** 8.00 $ · as printed: “8.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: PC · SKU: 21531415_EA · OCR/extraction confidence: 1.00 · “CERTAINES VARIÉTÉS SURGELÉS”

### 5. ANANAS ENTIER | WHOLE PINEAPPLE, CH.

![item 821](https://f.wishabi.net/page_pdf_images/24242916/a15feaa8-bdd8-11f1-8135-964e96f5df87/x_large)

- **Category:** Fruits & Vegetables > Fresh Fruits (FR: Fruits et légumes > Fruits frais)
- **How classified:** rule (`fruits`)
- **Price:** 5.00 $ · as printed: “5.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 20119813001_EA · OCR/extraction confidence: 1.00 · “PRODUIT DU COSTA RICA”

### 6. PATATES DOUCES | SWEET POTATOES, SAC DE 5 LB

![item 807](https://f.wishabi.net/page_pdf_images/24242914/97f54b34-bdd8-11f1-8fd6-d6b8222fe362/x_large)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 4.50 $ · as printed: “4.50”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 20697331001_EA · OCR/extraction confidence: 1.00 · “PRODUIT DU CANADA”

### 7. DÉTERGENT À VAISSELLE PALMOLIVE | PALMOLIVE HAND DISH DETERGENT, 591/828 ML

![item 1010](https://f.wishabi.net/page_pdf_images/24242919/9e7559ae-bdd8-11f1-af65-2af86f0adfcd/x_large)

- **Category:** Household > Cleaning & Laundry (FR: Maison > Entretien et lessive)
- **How classified:** rule (`household-cleaning`)
- **Price:** 2.00 $ · as printed: “2.00”
- **Flyer validity:** 2026-09-24 → 2026-10-14
- **Details:** brand: Palmolive · SKU: 20861400_EA · OCR/extraction confidence: 1.00 · “CERTAINES VARIÉTÉS”

### 8. MONSIEUR GUSTAV DOUBLE CRÈME CAMEMBERT, 125 G

![item 929](https://f.wishabi.net/page_pdf_images/24242923/ad031af6-bdd8-11f1-9f1a-063f73259631/x_large)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 6.00 $ · as printed: “6.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Monsieur Gustav · SKU: 21619307_EA · OCR/extraction confidence: 1.00

### 9. PRETZEL CRISPS® DE SNACK FACTORY® SAVEUR CHOCOLAT AU LAIT ET CARAMEL ET CHOCOLAT NOIR DRIZZLERS™, 155 G

![item 985](https://f.wishabi.net/page_pdf_images/24242923/b3b3362e-bdd8-11f1-9f1a-063f73259631/x_large)

- **Category:** Dairy & Eggs > Milk & Cream (FR: Produits laitiers et œufs > Lait et crème)
- **How classified:** rule (`milk-cream`)
- **Price:** 8.00 $ · as printed: “8.00”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Snack Factory · SKU: 21576333_EA · OCR/extraction confidence: 1.00 · “Certaines variétés”

### 10. TARTES DÉLICES DU MARCHÉ | FARMER'S MARKET™ PIES, 580 G-1 KG

![item 808](https://f.wishabi.net/page_pdf_images/24242917/954e44e4-bdd8-11f1-9083-8e0b0163410d/x_large)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 9.50 $ · as printed: “9.50”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Farmer's Market · SKU: 21297359_EA · OCR/extraction confidence: 1.00 · “CERTAINES VARIÉTÉS”

## Rachelle-Béry (`rachelle-bery`)

### 1. TONYS CHOCOLONELY CHOCOLAT

![item 14780](http://f.wishabi.net/page_items/436851437/1791472308/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 7.49 $ · as printed: “7.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Tony's Chocolonely · OCR/extraction confidence: 1.00

### 2. LANDISH LATTE AU MATCHA

![item 14754](http://f.wishabi.net/page_items/436851407/1791472306/extra_large.jpg)

- **Category:** Drinks > Tea & Hot Drinks (FR: Boissons > Thés et boissons chaudes)
- **How classified:** rule (`tea-hot-drinks`)
- **Price:** 29.99 $ · as printed: “29.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: LANDISH · OCR/extraction confidence: 1.00

### 3. PROTÉINES VÉGÉTALES VEGA

![item 5536](http://f.wishabi.net/page_items/436247032/1790917634/extra_large.jpg)

- **Category:** Meat > Plant-Based Meat Alternatives (FR: Viande > Substituts de viande à base de plantes)
- **How classified:** rule (`plant-based-meat`)
- **Price:** 18.99 $ · as printed: “18.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Vega · OCR/extraction confidence: 1.00

### 4. TRE STELLE FROMAGE RICOTTA

![item 14758](http://f.wishabi.net/page_items/436851417/1791472307/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Tre Stelle · OCR/extraction confidence: 1.00

### 5. Bannière Produits d'ici

![item 5592](http://f.wishabi.net/page_items/436319982/1790917642/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 6. PAIN MICHE ARHOMA

![item 14765](http://f.wishabi.net/page_items/436851419/1791472309/extra_large.jpg)

- **Category:** Bakery > Bread (FR: Boulangerie > Pain)
- **How classified:** rule (`bread`)
- **Price:** 5.49 $ · as printed: “5.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: ARHOMA · OCR/extraction confidence: 1.00

### 7. TEINTURE HARMONIC ARTS

![item 5590](http://f.wishabi.net/page_items/436247089/1790917639/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** rule (`beauty`)
- **Price:** 18.99 $ · as printed: “18.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: HARMONIC ARTS · OCR/extraction confidence: 1.00

### 8. FALAFELS ET SAUCE TAHINI LES FILLES FATTOUSH

![item 14783](http://f.wishabi.net/page_items/436851445/1791472306/extra_large.jpg)

- **Category:** Pantry > Honey, Syrups & Spreads (FR: Produits du garde-manger > Miel, sirops et tartinades)
- **How classified:** rule (`honey-spreads`)
- **Price:** 8.49 $ · as printed: “8.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: LES FILLES FATTOUSH · OCR/extraction confidence: 1.00

### 9. GÉLIFIÉS DE MÉLATONINE COMPLIMENTS

![item 5526](http://f.wishabi.net/page_items/436247037/1790917638/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 17.99 $ · as printed: “17.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Compliments · OCR/extraction confidence: 1.00

### 10. En savoir plus

![item 5595](http://f.wishabi.net/page_items/436319976/1790917640/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

## Shop Santé (`shop-sante`)

### 1. BOISSON PROTÉINÉE LEAN BODY LABRADA | 500 ML

![item 10608](classification-review-assets/item-10608.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 5.49 $ · as printed: “5.49”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 16
- **Details:** OCR/extraction confidence: 0.99

### 2. HUILE DE CAMELINE EN VAPORISATEUR PRET. TSF

![item 10584](classification-review-assets/item-10584.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 9.94 $ · as printed: “9.94”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 3
- **Details:** OCR/extraction confidence: 0.59

### 3. THAVAGE PRE-WORKOUT CBUM

![item 10586](classification-review-assets/item-10586.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 49.99 $ · as printed: “49.99”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 6
- **Details:** OCR/extraction confidence: 0.97

### 4. LIVERIREVIVE 120 CAPSULESIREG:79.99

![item 10592](classification-review-assets/item-10592.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 69.99 $ · as printed: “69.99”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 10
- **Details:** OCR/extraction confidence: 0.95

### 5. 40 PORTIONS

![item 10587](classification-review-assets/item-10587.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 34.99 $ · as printed: “34.99”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 6
- **Details:** OCR/extraction confidence: 0.89

### 6. SOURCE 7 PROTÉINE RULE ONE

![item 10613](classification-review-assets/item-10613.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 39.00 $ · as printed: “39”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 18
- **Details:** OCR/extraction confidence: 0.76

### 7. ME | j £NEAGY DRINK BOISSON ENERGISANTE 2

![item 10607](classification-review-assets/item-10607.jpg)

- **Category:** Drinks > Sports & Energy (FR: Boissons > Boissons énergisantes et pour sportifs)
- **How classified:** rule (`sports-energy`)
- **Price:** 3.49 $ · as printed: “3.49”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 16
- **Details:** OCR/extraction confidence: 0.99

### 8. SUPERFOODS + GREENS 4

![item 10591](classification-review-assets/item-10591.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 37.99 $ · as printed: “37.99”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 9
- **Details:** OCR/extraction confidence: 0.99

### 9. MINTBARS D'HALLOWEEN SAVEURS MIXTES | UNREAL | X26

![item 10605](classification-review-assets/item-10605.jpg)

- **Category:** Household > Home Goods (FR: Maison > Articles pour la maison)
- **How classified:** rule (`household-goods`)
- **Price:** 29.99 $ · as printed: “29.99”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 15
- **Details:** OCR/extraction confidence: 0.87

### 10. Et DE CRÉATINE | ALLMAX

![item 10600](classification-review-assets/item-10600.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 26.99 $ · as printed: “26.99”
- **Flyer validity:** 2026-10-01 → 2026-10-31 · flyer page 14
- **Details:** OCR/extraction confidence: 0.97

## Super C (`super-c`)

### 1. friandises glacées Nestlé | Nestlé frozen treats

![item 6996](http://f.wishabi.net/page_items/436072474/1790863951/extra_large.jpg)

- **Category:** Frozen Food > Ice Cream & Frozen Desserts (FR: Produits surgelés > Crèmes glacées et desserts glacés)
- **How classified:** rule (`ice-cream`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Nestle · OCR/extraction confidence: 1.00

### 2. GÂTEAU | CAKE

![item 6831](http://f.wishabi.net/page_items/436856892/1791548841/extra_large.jpg)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 6.99 $ · as printed: “6.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 3. bière Heineken | beer

![item 7062](http://f.wishabi.net/page_items/436072552/1790803390/extra_large.jpg)

- **Category:** Beer & Wine > Beer (FR: Bières et vins > Bières)
- **How classified:** rule (`beer`)
- **Price:** 27.99 $ · as printed: “27.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 4. FROMAGE TRANCHÉ SAPUTO | SAPUTO SLICED CHEESE

![item 6750](http://f.wishabi.net/page_items/436856758/1791480278/extra_large.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 5. SELECTION poisson

![item 6652](http://f.wishabi.net/page_items/436856767/1791480284/extra_large.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 10.00 $ · as printed: “10.0”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Selection · OCR/extraction confidence: 1.00

### 6. MOI

![item 6790](http://f.wishabi.net/page_items/436856727/1791480271/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** —
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 7. bière Michelob Ultra, Rickard's, Unibroue

![item 6992](http://f.wishabi.net/page_items/436072472/1790863949/extra_large.jpg)

- **Category:** Beer & Wine > Beer (FR: Bières et vins > Bières)
- **How classified:** rule (`beer`)
- **Price:** 44.24 $ · as printed: “44.24”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** OCR/extraction confidence: 1.00

### 8. CÉRÉALES CROQUE NATURE QUAKER | QUAKER HARVEST CRUNCH CEREAL

![item 6787](http://f.wishabi.net/page_items/436856864/1791480280/extra_large.jpg)

- **Category:** Pantry > Cereal & Breakfast (FR: Produits du garde-manger > Céréales et petits-déjeuners)
- **How classified:** rule (`cereal-breakfast`)
- **Price:** 10.49 $ · as printed: “10.49”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 9. LÉGUMINEUSES CEDAR | CEDAR LEGUMES

![item 6743](http://f.wishabi.net/page_items/436856846/1791480277/extra_large.jpg)

- **Category:** Fruits & Vegetables > Fresh Vegetables (FR: Fruits et légumes > Légumes frais)
- **How classified:** rule (`vegetables`)
- **Price:** 1.69 $ · as printed: “1.69”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 10. céréales Kellogg's | Kellogg's cereal

![item 7043](http://f.wishabi.net/page_items/436072705/1790803389/extra_large.jpg)

- **Category:** Pantry > Cereal & Breakfast (FR: Produits du garde-manger > Céréales et petits-déjeuners)
- **How classified:** rule (`cereal-breakfast`)
- **Price:** 3.97 $ · as printed: “3.97”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Kellogg's · OCR/extraction confidence: 1.00

## T&T Supermarché (`t-t`)

### 1. GoldenKing geleed'herbe enconserve

![item 10711](classification-review-assets/item-10711.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 2.69 $ · as printed: “2.69”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 6
- **Details:** OCR/extraction confidence: 0.99

### 2. Pearlriver魚 bridge vandoise

![item 10668](classification-review-assets/item-10668.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 3.87 $ · as printed: “3.87”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 3. CanardDemi& Poulet Demi Combo

![item 14814](classification-review-assets/item-14814.jpg)

- **Category:** Meat > Chicken & Turkey (FR: Viande > Poulet et dinde)
- **How classified:** rule (`chicken-turkey`)
- **Price:** 26.99 $ · as printed: “26.99”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 5
- **Details:** OCR/extraction confidence: 0.99

### 4. Vinda debarbouillette suspendue

![item 10661](classification-review-assets/item-10661.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 11.97 $ · as printed: “11.97”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 5. coffee cafe glacelait vietnamien

![item 14821](classification-review-assets/item-14821.jpg)

- **Category:** Drinks > Coffee (FR: Boissons > Cafés)
- **How classified:** rule (`coffee`)
- **Price:** 4.59 $ · as printed: “4.59”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 7
- **Details:** OCR/extraction confidence: 0.99

### 6. Danisa biscuitsau beurre

![item 10717](classification-review-assets/item-10717.jpg)

- **Category:** Dairy & Eggs > Butter & Spreads (FR: Produits laitiers et œufs > Beurre et tartinades)
- **How classified:** rule (`butter`)
- **Price:** 3.47 $ · as printed: “3.47”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 6
- **Details:** OCR/extraction confidence: 0.98

### 7. +laxes

![item 10672](classification-review-assets/item-10672.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 8. Dan-DPaknoix Dan-DPak果仁

![item 10622](classification-review-assets/item-10622.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 4.97 $ · as printed: “4.97”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 1
- **Details:** OCR/extraction confidence: 0.99

### 9. T&T-tartelette auxceufsala portugaise

![item 14796](classification-review-assets/item-14796.jpg)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 5.97 $ · as printed: “5.97”
- **Flyer validity:** 2026-10-16 → 2026-10-22 · flyer page 3
- **Details:** OCR/extraction confidence: 0.99

### 10. Sunity gelee 150mlx5

![item 10694](classification-review-assets/item-10694.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 5.87 $ · as printed: “5.87”
- **Flyer validity:** 2026-10-09 → 2026-10-15 · flyer page 4
- **Details:** OCR/extraction confidence: 0.80

## Uniprix (`uniprix`)

### 1. THRIVE Aides pour cesser de fumer sélectionnées

![item 5619](http://f.wishabi.net/page_items/434312456/1789813201/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 11.99 $ · as printed: “11.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Thrive · OCR/extraction confidence: 1.00

### 2. NOSH & CO.® Mais soufflés ou friandises sélectionnés/Selected popcorn or candies

![item 14833](http://f.wishabi.net/page_items/435970440/1790997556/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Chips & Snacks (FR: Grignotines, croustilles et friandises > Croustilles et grignotines)
- **How classified:** rule (`specific-popcorn`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Nosh & Co. · OCR/extraction confidence: 1.00

### 3. ZARBEES Sirops sélectionnés

![item 5599](http://f.wishabi.net/page_items/434312444/1789813195/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 8.99 $ · as printed: “8.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Zarbee's · OCR/extraction confidence: 1.00

### 4. PREMIÈRE RÉPONSE Produits sélectionnés

![item 5819](http://f.wishabi.net/page_items/434320652/1789813532/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 20.00 $ · as printed: “20.0”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: PREMIÈRE RÉPONSE · OCR/extraction confidence: 1.00

### 5. PROFOOT Produits sélectionnés/ Selected products

![item 5755](http://f.wishabi.net/page_items/434320709/1789813528/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Profoot · OCR/extraction confidence: 1.00

### 6. HERSHEY'S, MARS, EFFEM Friandises sélectionnées/Selected candies

![item 14848](http://f.wishabi.net/page_items/435970453/1790997564/extra_large.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 13.99 $ · as printed: “13.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** OCR/extraction confidence: 1.00

### 7. LAURA SECORD Tablettes de chocolat sélectionnées/Selected chocolate bars

![item 14849](http://f.wishabi.net/page_items/435970441/1790997557/extra_large.jpg)

- **Category:** Fish & Seafood > Fish (FR: Poissons et fruits de mer > Poisson)
- **How classified:** rule (`fish`)
- **Price:** 3.99 $ · as printed: “3.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Laura Secord · OCR/extraction confidence: 1.00

### 8. Crèmes antifongiques sélectionnées

![item 5630](http://f.wishabi.net/page_items/434312457/1789813202/extra_large.jpg)

- **Category:** Health & Beauty > Pharmacy (FR: Santé et beauté > Pharmacie)
- **How classified:** rule (`pharmacy`)
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Option + · OCR/extraction confidence: 1.00

### 9. TENA Protections pour les fuites urinaires sélectionnées/ Selected bladder leak protections

![item 5715](http://f.wishabi.net/page_items/434320486/1789813537/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** 7.99 $ · as printed: “7.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Tena · OCR/extraction confidence: 1.00

### 10. OPTION+ Produits de premiers soins sélectionnés

![item 5799](http://f.wishabi.net/page_items/434320730/1789813540/extra_large.jpg)

- **Category:** Health & Beauty > Personal Care (FR: Santé et beauté > Soins personnels)
- **How classified:** store-prior
- **Price:** —
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Option + · OCR/extraction confidence: 1.00

## Walmart (`walmart`)

### 1. Paq. de 3 biberons Naturel Avent de Philips à tétine Natural Response

![item 1321](https://f.wishabi.net/page_items/436884263/1791500716/extra_large.jpg)

- **Category:** Baby > Baby Care (FR: Bébé > Soins pour bébé)
- **How classified:** rule (`baby-care`)
- **Price:** 19.97 $ · as printed: “19.97”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Philips Avent · SKU: 1S2KME1R5JSE · OCR/extraction confidence: 1.00 · “Chac. Variétés Sélectionnées.”

### 2. Balderson cheddar ou Mon marché fraîcheur double cream brie

![item 14913](https://f.wishabi.net/page_pdf_images/24270707/ddde30a2-c2a1-11f1-b4bb-6e73685caa31/x_large)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Name (EN):** Cheddar Balderson
- **Price:** 6.67 $ · as printed: “6.67”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Balderson · SKU: 6000205483611 · OCR/extraction confidence: 1.00 · “Chac. Variétés et formats sélectionnés. N° 31397272.”

### 3. Solution de rinçage orale TheraBreath

![item 1348](https://f.wishabi.net/page_pdf_images/24238120/f1377c26-bd47-11f1-aed6-0e270a77ac40/x_large)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 13.47 $ · as printed: “13.47”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: TheraBreath · SKU: 5VGESSN4PJTT · OCR/extraction confidence: 1.00 · “Chac. Varietes sélectionnées. 473 ml. N° 50952745.”

### 4. Craquelins Goldfish

![item 14901](https://f.wishabi.net/page_pdf_images/24270707/e0be2fe8-c2a1-11f1-b4bb-6e73685caa31/x_large)

- **Category:** Snacks, Chips & Candy > Crackers & Cookies (FR: Grignotines, croustilles et friandises > Craquelins et biscuits)
- **How classified:** rule (`crackers-cookies`)
- **Price:** 2.24 $ · as printed: “2.24”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Goldfish · SKU: 205533 · OCR/extraction confidence: 1.00 · “Chac. Variétés et formats sélectionnés. N° 9208457.”

### 5. Biscuits Milk-Bone pour chiens

![item 1446](https://f.wishabi.net/page_pdf_images/24238136/0163115a-bd48-11f1-a0b4-c61bfd1c88ec/x_large)

- **Category:** Pet > Pet Food (FR: Animaux > Nourriture pour animaux)
- **How classified:** rule (`pet`)
- **Price:** 3.97 $ · as printed: “3.97”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Milk-Bone · SKU: 10036328 · OCR/extraction confidence: 1.00 · “Chac. Variétés et formats sélectionnés N° 30082955.”

### 6. Plat d'accompagnement Reser's

![item 1182](https://f.wishabi.net/page_pdf_images/24238091/edef64f2-bd47-11f1-b90b-c6a4b476a126/x_large)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 6.24 $ · as printed: “6.24”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** brand: Reser's · SKU: 6000191289483 · OCR/extraction confidence: 1.00 · “Chac. Variétés sélectionnées. 567 - 680 g. N° 30319323.”

### 7. Matelas orthopédique grand lit Hercules de Ultraflex

![item 1408](https://f.wishabi.net/page_items/436882016/1791496279/extra_large.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 411.19 $ · as printed: “411.19”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 38X35L1HEH87 · OCR/extraction confidence: 1.00 · “Sold by Marketplace Seller and Fullfilled by Walmart”

### 8. Amara organic smoothie melts or fruit bites

![item 14882](https://f.wishabi.net/page_pdf_images/24286863/61a78efc-c6fc-11f1-a24a-deb625417ed2/x_large)

- **Category:** Drinks > Juice (FR: Boissons > Jus)
- **How classified:** rule (`juice`)
- **Price:** 4.47 $ · as printed: “4.47”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: AMARA · SKU: 3B0NH6EPM9QW · OCR/extraction confidence: 1.00 · “Each. Selected flavours. N° 312833348.”

### 9. Vaissele ou linge de cuisine d'automne

![item 1170](https://f.wishabi.net/page_pdf_images/24238138/fa17da7a-bd47-11f1-8b88-8a0f26ba5685/x_large)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 4.97 $ · as printed: “4.97”
- **Flyer validity:** 2026-10-08 → 2026-10-14
- **Details:** SKU: 5ZIZKEKT4VZ9 · OCR/extraction confidence: 1.00 · “Chac. N° 51038169”

### 10. Dessert Brar's

![item 14870](https://f.wishabi.net/page_pdf_images/24282669/dfc7752e-c51a-11f1-8cf8-46d0f523916a/x_large)

- **Category:** International Foods > South Asian Foods (FR: Aliments internationaux > Aliments de l'Asie du Sud)
- **How classified:** rule (`south-asian`)
- **Name (EN):** Brar's rasmalai
- **Price:** 9.27 $ · as printed: “9.27”
- **Flyer validity:** 2026-10-15 → 2026-10-21
- **Details:** brand: Brar's · SKU: 6000196034795 · OCR/extraction confidence: 1.00 · “Chac. Variétés et formats sélectionnés. N° 30392188.”

## Wholesale Club (`wholesale-club`)

### 1. COLLATION SE SAVOUREUSE KURKURE a CERTAINES VARIETES

![item 11249](classification-review-assets/item-11249.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 41.99 $ · as printed: “41.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 15
- **Details:** OCR/extraction confidence: 0.98

### 2. CHARCUTERIES TRANCHÉES ROYAL CERTAINES VARIÉTÉS

![item 15117](classification-review-assets/item-15117.jpg)

- **Category:** Deli > Deli Meat (FR: Charcuterie > Charcuterie)
- **How classified:** rule (`deli-meat`)
- **Price:** 16.29 $ · as printed: “16.29”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 11
- **Details:** OCR/extraction confidence: 0.95

### 3. ‘PREPARE AU CANADA

![item 11191](classification-review-assets/item-11191.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 35.99 $ · as printed: “35.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 8
- **Details:** OCR/extraction confidence: 0.95

### 4. PURE BASMATI . BASMATI PUR

![item 11257](classification-review-assets/item-11257.jpg)

- **Category:** Pantry > Rice (FR: Produits du garde-manger > Riz)
- **How classified:** rule (`rice`)
- **Price:** 16.99 $ · as printed: “16.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 15
- **Details:** OCR/extraction confidence: 0.97

### 5. MACARONI AU FROMAGE SANS NOM®

![item 11243](classification-review-assets/item-11243.jpg)

- **Category:** Dairy & Eggs > Cheese (FR: Produits laitiers et œufs > Fromage)
- **How classified:** rule (`cheese`)
- **Price:** 1.49 $ · as printed: “1.49”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 14
- **Details:** OCR/extraction confidence: 0.99

### 6. PETITS GÂTEAUX VACHON CERTAINES VARIÉTÉS

![item 15114](classification-review-assets/item-15114.jpg)

- **Category:** Bakery > Cakes (FR: Boulangerie > Gâteaux)
- **How classified:** rule (`cakes`)
- **Price:** 5.99 $ · as printed: “5.99”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 10
- **Details:** OCR/extraction confidence: 0.95

### 7. PRODUIT DU CANADA,

![item 11222](classification-review-assets/item-11222.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 41.99 $ · as printed: “41.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 11
- **Details:** OCR/extraction confidence: 0.97

### 8. PEPSI

![item 15095](classification-review-assets/item-15095.jpg)

- **Category:** Drinks > Soft Drinks (FR: Boissons > Boissons gazeuses)
- **How classified:** rule (`soft-drinks`)
- **Price:** 2.75 $ · as printed: “2.75”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99 · other printed prices: 1.99

### 9. PAPIER HYGIÉNIQUE CHARMIN 24 ROUL. = 96 ROUL. OÙ ESSUIE-TOUT BOUNTY 8 ROUL. = 24 ROUL. BATHROOM TISSUE

![item 11173](classification-review-assets/item-11173.jpg)

- **Category:** Household > Paper & Storage (FR: Maison > Papier et rangement)
- **How classified:** rule (`household-paper`)
- **Price:** 22.99 $ · as printed: “22.99”
- **Flyer validity:** 2026-10-08 → 2026-10-14 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 10. CHOCOLAT EN SACHETS NESTLÉ | CERTAINES VARIÉTÉS, 76 - 203 G CELLO POUCHES CHOCOLATE 21079071 _EA/21708176 EA

![item 15101](classification-review-assets/item-15101.jpg)

- **Category:** Snacks, Chips & Candy > Candy & Chocolate (FR: Grignotines, croustilles et friandises > Friandises et chocolats)
- **How classified:** rule (`candy-chocolate`)
- **Price:** 4.69 $ · as printed: “4.69”
- **Flyer validity:** 2026-10-15 → 2026-10-21 · flyer page 7
- **Details:** OCR/extraction confidence: 0.97

## Épicerie PA Nature (`pa-nature`)

### 1. HORE PROTEIN ADPASUGAR

![item 11499](classification-review-assets/item-11499.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 50.50 $ · as printed: “50.50”
- **Flyer validity:** 2026-10-12 → 2026-10-25 · flyer page 4
- **Details:** OCR/extraction confidence: 0.99

### 2. BLANCS/BIOLOGIQUES | PT

![item 11497](classification-review-assets/item-11497.jpg)

- **Category:** **Unclassified**
- **How classified:** none
- **Price:** 1.99 $ · as printed: “1.99”
- **Flyer validity:** 2026-10-12 → 2026-10-25 · flyer page 1
- **Details:** OCR/extraction confidence: 0.83

### 3. JUS OASIS

![item 11498](classification-review-assets/item-11498.jpg)

- **Category:** Drinks > Juice (FR: Boissons > Jus)
- **How classified:** rule (`juice`)
- **Price:** 0.99 $ · as printed: “0.99”
- **Flyer validity:** 2026-10-12 → 2026-10-25 · flyer page 2
- **Details:** OCR/extraction confidence: 0.85
