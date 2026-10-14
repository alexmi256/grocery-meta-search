# Product categories by store

Research date: 2026-10-14. Purpose: inventory the product category
taxonomies of every store in the dataset that offers product search
(81 stores), as raw material for designing our own grocery
classification (Phase 4). Categories were captured by navigating each
store's live shop in a browser.

Conventions:

- **Food and grocery categories only.** Non-food departments
  (household, beauty, pharmacy, pet, baby care, etc.) are excluded;
  each store notes in one line that they exist. Baby *food* is kept.
- Labels are **verbatim** as published. Where a site publishes both
  languages, labels are given as `FR | EN`. Single-language stores
  keep their published language; an English/French gloss in
  `[brackets]` is our translation, given for top-level categories.
- Subcategories are listed inline, separated by `;`. "Voir Tous /
  See All" catch-all entries are dropped.
- Taxonomy shapes found: **tree** (2–3 levels), **flat** (one list of
  collections/categories), **none** (shop exists but has no category
  structure, or no shop at all), **blocked** (catalog behind login).
- Shared platforms mean shared taxonomies: PC Express (Loblaw),
  Metro's platform, Sobeys/Voilà, and stor.ai are each documented
  once, with per-store differences noted.

## Coverage summary

| Result | Stores |
|---|---|
| Full tree (2–3 levels) | Maxi/Provigo/Loblaws (PC Express), Metro/Metro Plus/Super C, IGA family, Sobeys (Voilà), Walmart, Costco, Tau, Mayrand, Lipa's, Fooderie, Épicure, Marché Korea, Aliments Merci, Vrac en Folie, GD Supermarché, La Mer, La Moisson, Sabor Latino, Saint-Vincent, Monde au Naturel, Olives Olives, Les 3 Gourmets |
| Flat list only | Akhavan, Bonanza, Odessa, Berchicci, Baia (Restomate), Latina (Panierdachat), Bazaar, Amira, Mrakovic, La Marguerite, La Vieille Europe, Johnny Prosciutto, Le Capitaine, Marché des Saveurs, Vrac et Bio, Shop Santé, Familiprix, Jean Coutu, Pharmaprix, M&M, Avril (top-levels), Canadian Tire (one nested list), SAQ, Carlota, En Tout K, Birri, Ayke, Ferme Hill Head, Chacun son arôme, Jardins de Stéphanie, Jardins Sauvages (brochure groupings), Potager Mont-Rouge, Au Jardin des Noix |
| No categories / no catalog | Hova Ranch (flat product list), Marché Sheng Tai (flyer only), Intermarché Palumbo (flyer only), Marché C&T (flyer only; extra store outside the search scope), Sublime Asperge (info page), Pastificio Sacchetto (brochure groupings only), Les Jardins d'Arlington (CSA/login), Jardins Mil'Herbes (in-person only), Chez Michel (non-food: Christmas trees), Dollarama (no e-commerce), Brunet (no shop; delivery via Uber Eats/DoorDash) |
| Blocked | Bio Locaux / Épicerie Loco (shop on BocoBoco, members-only login) |
| Partial | Brouette Maraîchère (shop closed until Jan 2027; menu captured), IGA "Épicerie" department subcategories (flyout not expandable) |

---

## Shared platform taxonomies

### PC Express (Loblaw) — Maxi, Provigo, Loblaws, Wholesale Club

Sites: [maxi.ca](https://www.maxi.ca), [provigo.ca](https://www.provigo.ca),
[loblaws.ca](https://www.loblaws.ca), [wholesaleclub.ca](https://www.wholesaleclub.ca)

Maxi, Provigo and Loblaws share one identical 14-department taxonomy
(Loblaws adds a 15th, Beer & Wine / Vins et bières — Ontario alcohol).
Wholesale Club runs the same catalog through a condensed 10-department
"Food" grouping (see its note below). Departments (FR | EN) with
subcategories:

- **Fruits et légumes | Fruits & Vegetables** — Légumes frais / Fresh Vegetables; Fruits frais / Fresh Fruits; Salades préemballées et vinaigrettes / Packaged Salads & Dressing; Fines herbes / Herbs; Fruits et légumes fraîchement coupés / Fresh Cut Fruits & Vegetables; Fruits séchés et noix / Dried Fruits & Nuts; Jus frais et smoothies / Fresh Juice & Smoothies
- **Produits laitiers et œufs | Dairy & Eggs** — Lait et crème / Milk & Cream; Œufs et succédanés d'œufs / Egg & Egg Substitutes; Beurre et tartinades / Butter & Spreads; Fromage / Cheese; Yogourt / Yogurt; Desserts et pâtes / Desserts & Doughs; Crème sure et trempettes / Sour Cream & Dips; Sans lactose / Lactose Free; Laits non laitiers / Non-Dairy Milk Alternatives
- **Produits du garde-manger | Pantry** — Produits en conserve et marinés / Canned & Pickled; Essentiels de cuisson / Baking Essentials; Pâtes et sauces / Pasta & Pasta Sauce; Mets faciles et accompagnements / Easy Meals & Sides; Céréales et petits-déjeuners / Cereal & Breakfast; Miel, sirops et tartinades / Honey, Syrups & Spreads; Riz / Rice; Huile et vinaigre / Oils & Vinegar; Condiments et garnitures / Condiments; Épices et assaisonnements / Spices & Seasonings; Haricots secs, légumes et grains / Dried Beans, Vegetables & Grains; Produits en vrac / Bulk Nuts and Candy
- **Aliments internationaux | International Foods** — two-level: Aliments de l'Asie de l'Est / East Asian Foods (Épicerie est-asiatique; Charcuterie, tofu et boulangerie; Surgelés; Fruits et légumes; Nouilles, riz et produits de garde-manger; Collations et boissons); Aliments de l'Asie du Sud / South Asian Foods (Épicerie sud-asiatique; Produits laitiers, charcuterie et boulangerie; Repas, desserts et légumes surgelés; Fruits et légumes; Produits de garde-manger et épices; Collations et boissons); Aliments afro-caribéens / Afro-Caribbean Foods (Surgelés; Fruits, légumes et boulangerie; Produits de garde-manger; Collations et boissons); Aliments halal / Halal Foods (Produits laitiers et produits de garde-manger; Viande, charcuterie et surgelés); Aliments casher / Kosher Foods (Viande, charcuterie et surgelés; Produits de garde-manger; Collations et boissons); Aliments du Moyen-Orient / Middle Eastern Foods (Aliments frais et surgelés; Produits de garde-manger; Collations et boissons); Aliments des Philippines / Filipino Foods (Fruits, légumes et surgelés; Nouilles, riz et produits de garde-manger; Collations et boissons); Aliments européens / European Foods; Aliments d'Amérique latine / Latin American Foods. (Some cuisine branches also contain non-food "Maison, santé et beauté" leaves — excluded.)
- **Viande | Meat** — Poulet et dinde / Chicken & Turkey; Bœuf / Beef; Saucisses / Sausages; Bacon; Saucisses hot-dog / Hot Dogs; Porc et jambon / Pork & Ham; Agneau et veau / Lamb & Veal; Brochettes et viande marinée / Kebabs & Marinated Meat; Viande exotique / Game Meat, Offals & Fowl; Substituts de viande à base de plantes / Plant-Based Meat Alternatives; Charcuterie / Deli Meat
- **Poissons et fruits de mer | Fish & Seafood** — Crevette / Shrimp; Saumon / Salmon; Poisson / Fish; Poisson fumé / Smoked Fish; Hors-d'œuvre aux produits de la mer / Seafood Appetizers; Crustacés / Shellfish; Calmar et pieuvre / Squid & Octopus
- **Grignotines, croustilles et friandises | Snacks, Chips & Candy** — Croustilles et grignotines / Chips & Snacks; Friandises et chocolats / Candy & Chocolate; Craquelins et biscuits / Crackers & Cookies; Petits gâteaux à grignoter / Snack Cakes; Produits en vrac / Bulk Nuts and Candy
- **Boissons | Drinks** — Jus / Juice; Cafés / Coffee; Thés et boissons chaudes / Tea & Hot Drinks; Boissons gazeuses / Soft Drinks; Eau / Water; Boissons au soja, au riz et aux amandes / Soy, Rice & Almond Drinks; Boissons énergisantes et pour sportifs / Sports & Energy; Mélanges pour boissons / Drink Mixes; Boissons non alcoolisées / Non-alcoholic drinks
- **Produits surgelés | Frozen Food** — Crèmes glacées et desserts glacés / Ice Cream & Frozen Desserts; Fruits et légumes surgelés / Frozen Fruit & Vegetables; Viande et fruits de mer surgelés / Frozen Meat and Seafood; Repas, plats principaux et accompagnements / Frozen Meals, Entrees & Sides; Pizzas surgelées / Frozen Pizza; Entrées et collations surgelés / Frozen Appetizers & Snacks; Boulangerie et déjeuner surgelés / Frozen Bakery & Breakfast; Boissons glacées et glace / Frozen Beverages & Ice; Substituts sans viande surgelés / Frozen Meatless Alternatives
- **Naturels et biologiques | Natural and Organic** — a cross-cutting re-slice of the whole store: Céréales, tartinades et sirops; Boulangerie; Condiments, sauces et huiles; Collations, croustilles et friandises; Produits laitiers et œufs; Boissons; Produits surgelés; Produits de cuisson et épices; Produits en conserve; Pâtes et plats d'accompagnement; Barres et protéines (plus non-food leaves — excluded)
- **Charcuterie | Deli** — Charcuterie / Deli Meat; Charcuteries et fromages / Deli Cheese; Antipasti, trempettes et tartinades / Antipasto, Dips & Spreads; Craquelins et condiments / Crackers & Condiments; Végétalien et végétarien / Vegan & Vegetarian; Boites-repas / Lunch & Snack Kits; Plateaux de réception / Party Trays
- **Boulangerie | Bakery** — Pain / Bread; Petits pains / Buns & Rolls; Biscuits, muffins et desserts / Cookies, Muffins & Desserts; Bagels, croissants et muffins anglais / Bagels, Croissants & English Muffins; Roulés, pains plats et croûtes à pizza / Wraps, Flatbread & Pizza Crust; Gâteaux / Cakes
- **Repas préparés | Prepared Meals** — Pâtes fraîches et sauces / Fresh Pasta & Sauce; Plats principaux et apéritifs / Entrees & Appetizers; Salades et soupes / Salads & Soups; Sandwichs / Sandwiches; Sushis / Sushi; Frites et accompagnements / Fries & Sides; Pizzas / Pizza; Quiches et pâtés / Quiches & Pies; Collations et trempettes / Snacks & Dips
- Non-food on the same sites: Bébé, Animaux et Maison / Baby, Pet & Home; Boutique de fleurs / Floral Shop; Pharmacie; Joe Fresh.

**Wholesale Club delta:** the same PC Express catalog grouped under
Départements → Alimentation | Food with 10 departments: Produits
laitiers et œufs; Viande; Fruits & légumes; Boulangerie; Poissons et
fruits de mer; Garde-manger; Grignotines, croustilles et friandises;
Charcuterie; Boissons; Produits surgelés (EN mirrors). Department
pages list the same "aisle" subcategories as Maxi (dairy verified in
both languages). Category URL codes are identical across languages —
one underlying catalog.

### Metro platform — Metro, Metro Plus, Super C

Sites: [metro.ca](https://www.metro.ca), [superc.ca](https://www.superc.ca)

One taxonomy for all three banners (Super C verified identical,
including subcategories; Super C only swaps two non-food departments).
16 food departments under "Allées | Aisles" (FR | EN):

- **Fruits et légumes | Fruits & Vegetables** — Fruits / Fresh Fruit; Légumes / Vegetables; Fines herbes fraîches / Fresh Herbs; Salades et légumes pour sautés emballés / Packaged Salads & Stir Fry; Fruits et légumes coupés / Cut Fruits & Vegetables; Fruits et légumes biologiques / Organic Fruits & Vegetables; Fruits et noix séchés / Dried Fruits & Nuts; Végétalien et végétarien / Vegan & Vegetarian
- **Produits laitiers et œufs | Dairy & Eggs** — Laits, Crèmes et Beurres / Milk, Cream & Butter; Oeufs / Eggs; Yogourts / Yogurt; Fromages emballés / Packaged Cheese; Fromages fins / Deli Cheese; Crèmes sures et trempettes / Sour Cream & Dips; Desserts et pâtes réfrigérés / Chilled Desserts & Dough
- **Garde-Manger | Pantry** — Ingrédients pour cuisson et préparation / Baking Ingredients; Aliments en conserve et en pot / Canned & Jarred; Céréales, tartinades et sirops / Cereals, Spreads & Syrups; Condiments et garnitures / Condiments & Toppings; Fines herbes, épices et sauces / Herbs, Spices & Sauces; Huiles et vinaigres / Oils & Vinegars; Gastronomie internationale / World Cuisine; Plats d'accompagnements [sic] / Sides; Pâtes, riz et fèves / Pasta, Rice & Beans
- **Plats Cuisinés | Cooked Meals** — Prêt-à-manger / Ready-to-Eat; Prêt-à-cuire / Ready-to-Cook; Format économique / Value Pack; Végé / Vegetarian
- **Format Économique | Value Pack** — Marché frais / Fresh Market; Non périssable / Non-perishable; Surgelé / Frozen (plus non-food leaves)
- **Boissons | Beverages** — Café, Thés et boissons chaudes / Coffee, Tea & Hot Drinks; Jus et boissons / Juices & Drinks; Boissons gazeuses / Soft Drinks; Boissons sportives et énergisantes / Sports & Energy Drinks; Eau / Water; Thés et cafés glacés / Iced Tea & Coffee; Mélanges pour boissons / Drink Mixes; Boissons au soja, au riz et aux amandes / Soy, Rice & Nut Beverages; Boissons non alcoolisées / Non-Alcoholic Beverages
- **Bières et vins | Beer & Wine** — Vins, cocktails et coolers / Wines, Cocktails & Coolers; Bières et cidres / Beer & Cider
- **Viandes et volailles | Meat & Poultry** — Bœuf et veau / Beef & Veal; Poulet et dinde / Chicken & Turkey; Porc / Pork; Agneau et gibier / Lamb & Game Meat; Saucisses et bacon / Sausages & Bacon; Viandes préparées et marinées / Marinated & Prepared Meat; Viandes surgelées / Frozen Meat
- **Aliments végétariens et végétaliens | Vegan & Vegetarian Food** — Tofu, tempeh et autres protéines / Tofu, Tempeh & Other Protein; Boissons / Beverages; Garde-Manger / Pantry; Collations / Snacks; Réfrigéré / Refrigerated; Surgelés / Frozen
- **Épicerie Biologique | Organic Groceries** — cross-cutting re-slice: Fruits et légumes; Pains et pâtisseries; Viandes, volailles et poisson; Œufs, produits laitiers et substituts; Garde-manger; Collations, craquelins et chocolats; Jus et boissons biologiques; Produits surgelés biologiques; Aliments végétaliens et végétariens
- **Collations | Snacks** — Collations salées / Salty Snacks; Collations sucrées et bonbons / Sweet Snacks & Candy; Noix, graines et fruits / Nuts, Seeds & Fruit
- **Produits surgelés | Frozen** — Entrées et collations / Appetizers & Snacks; Boulangerie / Bakery; Boissons et glace / Beverages & Ice; Pour le déjeuner / Breakfast Foods; Fruits et légumes / Fruit & Vegetables; Crème glacée et friandises / Ice Cream & Treats; Poissons et fruits de mer / Fish & Seafood; Viandes et volailles / Meat & Poultry; Repas et plats d'accompagnement / Meals & Sides; Pizzas et pâtes / Pizza & Pasta
- **Pains et pâtisseries | Bread & Bakery Products** — Pains frais et baguettes / Freshly Baked Bread & Baguettes; Pains emballés / Packaged Bread; Pains à hamburger et petits pains / Buns & Rolls; Tortillas et pains plats / Tortillas & Flat Breads; Viennoiseries, muffins et bagels / Muffins, Bagels & Baked Goods; Desserts et pâtisseries / Desserts & Pastries
- **Charcuteries et plats préparés | Deli & Prepared Meals** — Charcuteries / Deli Meats; Antipasti, trempettes et pâtés / Antipasto, Dips & Pâtés; Plats prêts-à-manger et accompagnements / Ready Meals & Sides; Pizzas, pâtes et sauces fraîches / Fresh Pizza, Pasta & Sauces; Plateaux / Platters
- **Poissons et fruits de mer | Fish & Seafood** — Poissons frais / Fresh Fish; Fruits de mer frais / Fresh Seafood; Poissons et fruits de mer surgelés / Frozen Fish & Seafood; Poissons et fruits de mer préparés / Prepared Fish & Seafood
- **Cuisine du monde | World Cuisine** — Asiatique / Asian; Amérique Latine / Latin; Indienne / Indian; Méditerranéenne / Mediterranean; Autres produits internationaux / Other International Products
- Non-food: Entretien ménager, Bébé, Soins et beauté, Animaux, Pharmacie; plus the Nature's Signature wellness brand (mostly non-food).

### Sobeys / Voilà — Sobeys (and the IGA family, sibling taxonomy)

Sites: [sobeys.com](https://www.sobeys.com) → shop at [voila.ca](https://voila.ca);
[iga.ca](https://www.iga.ca) (covers IGA, IGA Extra, IGA Express; fulfilled
via "Voilà par IGA"). Sobeys' own footprint is qc-unverified in our
dataset (kept for expansion research); IGA is the Quebec face of the
same platform family.

**Voilà** (EN; storefront is English-first). Browse tree:

- **Fresh Fruits & Vegetables** — Fresh Fruits; Fresh Vegetables; Fresh Cut Fruits & Vegetables; Fresh Packaged Salads & Dressing; Fresh Herbs; Refrigerated Juices, Smoothies & Kombucha; Fresh Organic Fruits; Fresh Organic Vegetables
- **Meat & Seafood**; **Dairy & Eggs**; **Cheese**; **Bread & Bakery**; **Deli**; **Prepared Meals & Sides**; **Frozen Foods**; **Snacks & Candy**; **Beverages**; **Alcohol**; **Plant Based**; **International Foods** (top-levels; only two expanded below)
- **Pantry** — Cereal & Breakfast Foods; Spreads, Syrup & Honey; Crackers, Cookies & Desserts; Baking; Pasta, Noodles & Sauce; Rice, Grains & Legumes; Condiments; Spices & Seasoning; Marinades & Sauces; Oils, Vinegars & Salad Dressing; Canned & Pickled; Soup & Broth; Easy Prep Meals & Sides
- Merchandising top-levels also exist: Compliments, Panache (house brands), Les Prêts-à-cuire, Value Size. Non-food: Household Products, Health & Beauty, Baby, Pets, Floral & Garden.

**IGA** (FR | EN; subcategories in FR, EN verified as 1:1 translations).
Differs from Metro's taxonomy — Sobeys lineage. Note cheese sits
under Fromages et Charcuterie, not Dairy:

- **Épicerie | Grocery** — subcategories not capturable (flyout is a direct link behind an overlay)
- **Pain et boulangerie | Bread & Bakery** — Pain; Petits pains et pains michettes; Bagels; Muffins anglais; Muffins; Wraps, pita et pains plats; Desserts et pâtisseries; Pains et pâtisseries sans gluten
- **Fromages et Charcuterie | Cheese & Deli** — Fromages; Charcuterie; Hummus; Gelée de charcuterie; Craquelins pour charcuterie; Kits et ingrédients pour pizza; Plateaux pour fêtes
- **Viande | Meat** — Bœuf et veau; Poulet; Dinde; Agneau; Burgers; Porc; Hot-dogs et saucisses; Charcuterie; Bacon
- **Fruits de mer | Seafood** — Poisson; Fruits de mer surgelés; Sushi
- **Fruits et Légumes | Fruits & Vegetables** — Fruits; Légumes; Fruits et légumes coupés; Salades et vinaigrettes emballées; Herbes; Jus réfrigérés, smoothies et kombucha
- **Produits à base de plantes | Plant-Based** — Alternatives à la viande; Soupers et entrées à base de plantes; Laits et crèmes non laitiers; Fromages non laitiers; Beurre non laitier; Yogourts non laitiers; Trempettes et condiments non laitiers; Desserts glacés non laitiers; Tofu; Burgers végétariens; Soja
- **Produits laitiers et Œufs | Dairy & Eggs** — Lait; Crème et crème à café; Beurre et margarine; Yogourt; Crème sure; Crème fouettée; Œufs
- **Garde-manger | Pantry** — Céréales et déjeuner; Tartinades sirop et miel; Craquelins biscuits et desserts; Ingrédients pour cuisson et pâtisserie; Pâtes nouilles et sauces; Riz grains et légumineuses; Condiments; Épices et assaisonnements; Marinades et sauces; Huiles vinaigres et vinaigrettes; Conserves et aliments marinés; Soupes et bouillons; Repas et accompagnements prêts à cuisiner
- **Collations et Bonbons | Snacks & Candy** — Bonbons et Chocolats; Croustilles; Maïs soufflé; Barres énergétiques granola et céréales; Galettes de riz; Noix graines et mélanges montagnards; Fruits séchés; Viande séchée (Jerky); Pouding et gelées; Collations aux fruits; Coupes de fruits; Biscuits et craquelins
- **Bières, Vin et Cidre | Beer, Wine & Cider** — Bière; Vin; Cidres; Mélanges pour cocktails; Boissons rafraîchissantes (Coolers)
- **Boissons | Drinks** — Café; Thé et boissons chaudes; Eau; Boissons gazeuses; Thé glacé et limonade; Kombucha et bien-être; Boissons énergisantes et de sport
- **Surgelés | Frozen** — Repas surgelés, plats principaux et accompagnements; Apéritifs et collations surgelés; Pizza surgelée; Viande et fruits de mer surgelés; Fruits et légumes surgelés; Crème glacée et friandises; Pain et déjeuner surgelés; Boissons surgelées et glace
- **Prêt-à-manger | Ready To Eat** — Plats et accompagnements prêts-à-manger; Soupes; Sushis; Sandwichs, sous-marins et wraps; Salades; Kits pour dîners et collations; Pâtes fraîches et sauce à pâtes; Pizza
- **Produits internationaux et locaux | International & Local Foods** — Asiatique de l'Est; Asiatique du Sud; Caraïbes; Européen; Latin; Moyen-Orient
- Non-food: Maison, Santé et Beauté, Bébé, Animaux, Pharmacie, Fleurs et Jardin, etc.

### stor.ai — Lipa's Kosher Supermarket, Fooderie Kosher Market

Sites: [lipassupermarket.com](https://www.lipassupermarket.com),
[fooderiemarket.com](https://www.fooderiemarket.com). Both run stor.ai
and share the same core taxonomy skeleton (EN). Lipa's departments:

- **Lipa's Prepared Food** (Fooderie equivalent: Deli & Meals + Pizza & Sushi counters)
- **Bread & Bakery**
- **Fresh Produce** — Fresh Fruit (Apples; Bananas; Citrus Fruit; Grapes; Mangoes; Melons & Watermelons; Peaches, Apricots & Plums; Pears; Tropical Fruit); Fresh Cut Fruits; Fruit Platters; Fresh Vegetables (Main Vegetables; Legumes; Mushrooms; Potatoes & Sweet Potatoes; Root Vegetables; Squash & Pumpkin); Fresh Cut Vegetables; Greens & Herbs (Fresh Salads; Lettuce & Leaves; Herbs); Dried Fruit & Nuts (Dried Fruit; Nuts & Seeds)
- **Cereal & Breakfast**
- **Grocery** — Basic Products (Flour & Sugar; Oil & Cooking Sprays; Salt; Spices & Seasonings; Condiments & Relishes; Vinegar & Cooking Wine; Breadcrumbs & Stuffing; Sweeteners); Baking Needs (Baking Chocolate & Chips; Icing & Toppings; Jello & Pudding; Baking Mixes; Pie Fillings; Baking Nuts & Seeds; Baking Essentials & Extracts; Cookie Crumbs & Pie Crusts); Spreads (Peanut Butter; Honey; Jams & Preserves; Syrups; Tahini); Canned & Jarred Foods (Canned Tomatoes & Pastes; Canned Fish & Tuna; Canned Ready Meals; Cooking Sauces & Salsa; Salad Dressings & Toppings; Canned Olives & Pickles; Canned Vegetables; Canned Beans & Peas; Canned Fruit; Applesauce); Pasta, Grains & Beans (Pasta & Spaghetti; Rice & Couscous; Grains & Seeds; Beans & Peas); Soups, Stocks & Croutons; Instant Meals & Mixes (Instant Meals; Cooking Mixes; Noodles & Soups); World Foods (Asian; Mexican & Hispanic)
- **Dairy & Eggs**; **Deli**; **Frozen**; **Meat, Poultry & Fish**; **Health & Specialty Diets**; **Beverages**; **Snacks & Sweets**
- Non-food: Paper, Laundry & Cleaning; Health & Beauty; Baby; Houseware & Leisure.

Fooderie expands the same skeleton further (Frozen splits into
Frozen Meals / Frozen Food / Ice Cream & Ices; Beverages into
Beverages / Hot Beverages / Alcohol; Snacks & Sweets into Cookies &
Crackers / Candy & Chocolate / Chips & Snacks / Fruit & Nut Snacks;
plus holiday departments like Tishrei Holidays) — evidence that
stor.ai's tree is a template each store extends.


---

## National chains with their own taxonomies

### Walmart — [walmart.ca](https://www.walmart.ca)

Own platform; FR | EN pairs published. Grocery tree:

- **Fruits & vegetables | Fruits et légumes** — Fresh fruits / Fruits frais; Fresh vegetables / Légumes frais; Fresh salads, dressings & toppings; Pre-cut fruits & vegetables; Fresh juice & kombucha; Plant-based proteins & tofu
- **Dairy & eggs | Produits laitiers et œufs** — Milk / Lait; Cheese / Fromage; Yogurt / Yogourt; Cream & creamers; Butter & margarine / Beurre et margarine; Eggs & egg substitutes / Œufs et substituts d'œufs
- **Meat & seafood | Viande et fruits de mer** — Fresh chicken & turkey; Fresh beef; Fresh pork; Fresh fish & seafood; Fresh sausages; Hot dogs
- **Pantry food | Produits d'épicerie sèche** — Dry pasta & noodles; Rice & grains; Dried beans, lentils and peas; Cereal & breakfast; Canned food; Baking ingredients & supplies; Easy meals & instant sides; Sauces, spices & marinades
- **Frozen foods | Aliments surgelés** — Frozen meat & seafood; Frozen meals & sides; Ice cream shop; Frozen pizza; Frozen pasta & noodles; Frozen appetizers; Frozen fries & potatoes; Frozen breakfast; Frozen vegetables; Frozen fruit; Frozen bakery & dessert; Frozen cakes & pies; Frozen meat pies & patties; Frozen drinks & ice; Frozen Halal food; Frozen plant-based food
- **Bread & bakery | Boulangerie-pâtisserie** — White & whole wheat bread; Rye bread; Whole grain bread; Sourdough bread; Italian bread; Gluten-free bread; Bakery snacks & treats; Muffins; Croissants & pastries; Cakes & cupcakes; Bakery cookies; Donuts; Hamburger & hotdog buns; Bagels & english muffins; Tortillas, naan & pita; Global bakery; Baked in store
- **Snacks & candy | Collations et bonbons** — Chips; Chocolates; Cookies; Crackers; Granola & snack bars; Popcorn & kernels; Candy; Trail mixes, nuts & more; Salsa & dips; Applesauce & fruit cups; Fruit snacks; International snacks; Pudding & jelly snacks; Snack cakes; Jerky & dried meat snacks; Rice cakes; Bulk snacks
- **Drinks | Boissons** — Soft drinks; Juice; Water; Coffee; Tea; Hot chocolate; Kombucha & more drinks; Energy drinks; Sports & electrolyte drinks; Drink mixes; Non-alcoholic drinks
- **Deli & fresh prepared meals | Charcuteries et repas préparés frais** — Deli meat; Fresh meals & sides; Deli cheese; Hummus, dips & spreads; Party trays & platters; Lunch kits & snacks; Fresh pasta & sauce; Fresh entrees & sides; Potato & pasta salads; Fresh appetizers & pies; Rotisserie chicken; Sliced ham; Sliced chicken & turkey; Meat trios & value packs; Italian meats; Pepperoni; Kolbassas & dry sausages; Feta, Ricotta & soft cheese; Aged cheddar; Havarti, gouda & swiss; Fresh dips; Fresh hummus & spreads
- **International foods | Aliments du monde** — Indian & South Asian; Chinese & East Asian; Caribbean & African; Middle Eastern; Italian & European; Mexican & Latin American; Thai & Filipino; Global produce; International snacks; All Halal; All Kosher
- **Lifestyle & dietary needs | Style de vie et besoins alimentaires** — attribute-style cross-cut: High protein; Halal; Organic; Plant-based; No antibiotics; Keto-friendly; Kosher; No added sugars; Sodium conscious; Lactose-free; Gluten-free; Peanut-free
- Extensive non-food departments exist.

### Costco — [costco.ca](https://www.costco.ca)

"Grocery & Household | Épicerie et maison" (FR | EN pairs):

- **Snacks, Candy & Nuts | Collations, friandises et noix** — Candy; Chocolates; Cookies; Crackers; Fruit & Nuts; Gum & Mints; Jerky & Meat Snacks; Nutrition & Snack Bars; Popcorn; Chips & Pretzels; Snack Cakes; Trail & Snack Mix
- **Pantry & Dry Goods | Garde-manger et aliments secs** — Baking; Canned & Jarred Foods; Cereal; Emergency Food Kits; Maple & Flavoured Syrup; Oils & Vinegars; Pasta; Rice, Grains & Packaged Food; Soups; Spices, Seasoning & Sauces; Spreads & Butters
- **Meat & Seafood | Viande et fruits de mer** — Beef / Bœuf; Bison, Lamb & Game Meat; Fish & Seafood / Poissons et fruits de mer; Pork / Porc; Poultry / Volaille
- **Water & Beverages | Eau et boissons** — Cocoa & Drink Mixes; Coffee; Energy & Sports Drinks; Juice; Non-alcoholic; Shelf Stable Drinks; Soda & Soft Drinks; Tea; Water; Wine & Beer Kits
- **Coffee | Café** — Ground Coffee; K-Cups & Coffee Pods; Whole Bean Coffee
- **Deli & Prepared Meals | Charcuterie et repas préparés** — Deli Meat; Prepared Meals & Appetizers
- **Bakery | Boulangerie** — Pastries
- **Cheese | Fromages** (leaf)
- **Gourmet Food | Cuisine gastronomique** — Gourmet Meat & Seafood; Gourmet Poultry; Gourmet Fish & Seafood; Gourmet Deli & Prepared Meals; Caviar; Gourmet Cheese; Gourmet Cookies; Gourmet Pantry & Dry Goods
- **Organic | Biologique**, **Vegan Foods | Aliments végétaliens** (attribute leaves); **International Foods | Cuisine du Monde** (leaf); **Kirkland Signature** (house brand); **Gift Baskets | Paniers-cadeaux** (food baskets)
- Non-food sits inside the same "Grocery & Household" area (paper, cleaning, pet, health & beauty, baby) plus the rest of the warehouse.

### Giant Tiger — [gianttiger.com](https://www.gianttiger.com)

Shopify-like collections; EN captured — the French site's navigation
failed to load during the visit, so FR labels are unavailable
(noted as a site defect, 2026-10-14). Grocery menu:

- **Pantry** — Breakfast; Baking Supplies; Oils, Vinegars, & Spices; Pasta & Pasta Sauce; Soups; Rice; Canned & Pickled; Sauces & Seasonings
- **Snacks, Chips & Candy** — Chips & Popcorn; Chocolate & Candy; Granola Bars & Snacks; Cookies & Crackers; Dried Fruit; Jerky & Nuts; Gum & Mints
- **Drinks** — Soda & Soft Drinks; Energy Drinks; Juice; Coffee & Tea; Water & Sparkling Water; Powder & Mixers
- **Fruits & Vegetables** — Fresh Fruits; Fresh Vegetables; Herbs; Salads
- **Meat & Seafood** — Beef; Chicken & Turkey; Bacon; Sausages & Hot Dogs; Pork; Deli Meat; Meat Alternatives; Fish
- **Dairy & Eggs** — Milk & Cream; Eggs; Yogurt; Sour Cream & Cream Cheese; Butter & Spread; Cheese
- **Bakery** — Bagels; Bread & Buns; Cakes; Wraps & Pitas; Pastries & Muffins
- **Frozen** — Frozen Vegetables & Fruits; Ice Cream & Desserts; Frozen Meat & Seafood; Frozen Pizza; Frozen Meals & Sides
- **International Food** (leaf). Non-food departments are extensive.

### Canadian Tire — [canadiantire.ca](https://www.canadiantire.ca)

No food department. Food lives nested under Home | Maison →
**Snacks & Beverages | Collations et boissons**: Coffee / Café;
Nespresso Pods / Capsules Nespresso; Chocolate / Chocolat; Keurig
Coffee Pods; Candy / Bonbons; Chips / Croustilles; Snack Mixes; Nuts
& Beef Jerky; Drinks / Boissons; Pantry / Garde manger; seasonal
candy (Halloween, Christmas); Ground Coffee; Coffee Pods; Pectin &
Mixes. The site is otherwise entirely non-food.

### SAQ — [saq.com](https://www.saq.com)

Alcohol only (beverages). FR | EN tree:

- **Vin | Wine** — Vin blanc / White wine; Vin rouge / Red wine; Vin rosé / Rosé; Vin nature / Natural wines; Vin orange / Orange wines; Vin de dessert / Dessert wines
- **Spiritueux | Spirits** — Scotch et whisky / Scotch and whisky; Liqueur et crème / Liqueur and cream; Gin; Rhum / Rum; Vodka; Téquila / Tequila; Cognac et brandy / Cognac and brandy
- **Champagne et mousseux | Champagne and sparkling wine**; **Prêt-à-boire | Ready-to-drink**; **Apéritif | Aperitif**; **Porto et vin fortifié | Port and fortified wine**; **Saké | Sake**; **Soju**; **Cidre | Cider**; **Bière | Beer**; **Hydromel | Honey Wine**; **Importations privées | Private imports**
- Cross-cutting sections: Espace Québec (Quebec products), Les alternatifs | Alternatives (0,5 % et moins / 0.5% or less, low-alcohol, small formats).

### M&M Food Market — [mmfoodmarket.com](https://www.mmfoodmarket.com) / [lesalimentsmm.com](https://www.lesalimentsmm.com)

Flat taxonomy, FR | EN pairs: Appetizers / Hors-d'œuvre; Butcher /
Boucherie; Prepared Meals / Mets cuisinés; Seafood / Poissonnerie;
Single Serve / Portions individuelles; Desserts; Gluten-Free / Sans
gluten; Sides / Accompagnements; Vegetables / Légumes; Bakery /
Boulangerie; Pantry Essentials / Essentiels du garde-manger. Special
diets (cross-cutting): Gluten-Free, Vegan / Végétalien, Vegetarian /
Végétarien, Halal. (Frozen-food specialist: most categories are
frozen by default.)

### Mayrand — [mayrand.ca](https://mayrand.ca)

Custom storefront (Empire/Sobeys family), FR (EN toggle). Top levels:
Fruits et légumes [Produce]; Boucherie [Butcher]; Produits laitiers
[Dairy]; Charcuterie [Deli]; Poissonnerie [Seafood]; Boisson
[Beverages]; Surgelé [Frozen]; Boulangerie [Bakery]; and a deep
**Épicerie** [Grocery] tree (3 levels, richest of any independent):

- Autre; Bar laitier (Sirop barbotine et lait frappé; Garniture et sauce; Cornet et coupe); Biscuit et craquelin (Biscuit et gâteau; Craquelin et biscotte); Condiment (Ketchup; Mayonnaise; Relish; Moutarde; Sauce condiment); Confiserie (Bonbon; Barre de chocolat; Chocolat; Nougat); Confiture et tartinade (Gelée et confiture; Beurre d'arachide; Tartinade; Miel et sirop); Croustille et grignotine (Croustille; Grignotine); Céréales et barre (Gruau et granola; Céréales; Barre de céréales); Farine, semoule et chapelure (Farine et chapelure; Farine de spécialité); Fruit en conserve (Compote; Fruits en conserve et gelées); Huile et vinaigre (Huile d'olive; Vinaigre balsamique; Vinaigre; Huile); Ingrédient de pâtisserie (Mélange à pâtisserie; Fécule et gélatine; Levure et additif; Garniture; Glaçage et décoration; Shortening et saindoux; Chocolat et cacao à cuisson; Arôme et colorant); Légume en conserve (Légumes; Légumineuses); Marinade (Olive; Cornichon et oignon; Légumes marinés; Câpre; Piment; Panettone); Poisson et viande en conserve (Poisson en conserve); Pâtes (Pâtes alimentaires; Nouilles; Gnocchi); Riz et grain (Grain de spécialité; Riz et orge; Haricot et maïs; Lentille; Pois; Quinoa; Couscous); Sauce (Sauce pour pâtes; Sauce pizza; Sauce déshydratée; Sauce préparée; Sauce pour marinade); Soupe et bouillon (Soupe; Bouillon); Mets préparé; Sucre (Cassonnade; Substitut de sucre; Sucre d'érable); Tomate en conserve (Coulis de tomates; Pâte de tomates; Sauce tomate); Vinaigrette et Croûton (Croûton; Vinaigrette et sauce à salade); Épice, sel et poivre (Épice; Sel; Poivre)
- Non-food departments: Article de cuisine, Entretien, Emballage, Équipement.

### Avril — [avril.ca](https://www.avril.ca)

Health supermarket; flat FR | EN pairs under Épicerie | Grocery:
Garde-manger / Pantry; Farines, légumineuses et grains / Grains,
Flours and Legumes; Fruits et légumes biologiques / Organic Fruits
and Vegetables; Produits laitiers et œufs / Dairy Products and Eggs;
Substituts de produits laitiers / Dairy Alternatives; Viandes et
substituts / Meat and Substitutes; Poissons et substituts / Fish and
Substitutes; Boulangerie / Bakery; Prêt-à-manger / Ready-to-eat;
Boissons / Beverages; Bières et vins / Beers and Wines. Dietary
filters throughout (sans gluten, sans lactose, végane, cétogène…).
Non-food: Suppléments, Bébés et mamans, Beauté, Maison.

### Marchés Tau — [marchestau.com](https://marchestau.com)

Organic chain; FR | EN pairs:

- **Bakery / Boulangerie** — Breads & Bagels / Pains et bagels; Bagels et pain surgelé [frozen bagels & bread]; Tortillas & Flat Breads / Tortillas & Pains Plats
- **Beverages / Breuvages** — Non-Dairy Alternatives / Alternatives non laitières; Coffee, Tea & Stimulants / Café, Thé & Stimulants; Water & Coconut Water / Eau & Eau de Coco; Juice / Jus
- **Snacks / Collations** — Candy & Fruit Snacks / Bonbons et Fruits Collations; Chips & Popcorn / Chips et pop-corn; Chocolates & Desserts / Chocolats et Desserts; Energy & Protein Snacks / Collations énergétiques et protéinés; Crackers & Biscuits / Craquelins et biscuits; Nuts, Seeds & Dried Fruit / Noix, graines et fruits secs
- **Organic Fruits & Vegetables / Fruits & légumes Bio** — Organic Fruits / Fruits bio; Frozen Organic Fruits and Vegetables / Fruits et légumes bio surgelés; Organic Vegetables / Légumes bio
- **Pantry / Garde-Manger** — Canned & Jarred Foods / Aliments en conserve et en pot; Broths & Soups / Bouillons et soupes; Cereals & Oatmeal / Céréales & Gruau; Herbs, Spices & Seasonings / Herbes, épices et assaisonnements; Oils & Vinegars / Huiles et vinaigres; Pasta, Rice & Beans / Pâtes, riz et haricots; Baking & Grains / Pâtisserie & Céréales; Sauces; Spreads and Sweeteners / Tartinades et édulcorants; Dressings & Condiments / Vinaigrettes et condiments
- **Frozen Products / Produits congelés** — Frozen Desserts / Desserts surgelés; Pizza & French Fries / Pizzas et frites; Fish & Seafood / Poissons et fruits de mer; Meals & Side Dishes / Repas et plats d'accompagnement; Meat & Poultry / Viande et Volaille
- **Bulk Products / Produits en vrac** — Grains & Legumes / Céréales & Légumineuses; Chocolate & Sweets / Chocolat et Bonbons; Flours / Farines; Herbs & Spices / Herbes et épices; Nuts & Dried Fruit / Noix et fruits secs
- **Refrigerated Products / Produits réfrigérés** — Condiments / Assaisonnement; Butters & Spreads / Beurres et pâtes à tartiner; Cheese / Fromage; Milk & Cream / Lait & Crème; Eggs / Oeufs; Non-Dairy Products / Produits non laitiers; Salads & Soups / Salades et soupes; Meat & Cold Cuts / Viande et charcuterie; Dairy & Vegan Yogourts / Yaourt laitier et végétalien
- **Baby and Toddler / Bébé et tout-petit** — Baby Food only (rest non-food). Non-food: animal care, cosmetics, household, supplements.

### Pharmaprix — [pharmaprix.ca](https://www.pharmaprix.ca)

Shoppers Drug Mart platform (not PC Express). One small grocery
section (FR | EN): **Épicerie et boissons | Grocery & Beverages** —
Barres et biscuits / Bars & Cookies; Boissons / Beverages; Bonbons et
chocolats / Candy & Chocolates; Conserves et aliments emballés /
Canned & Packed Foods; Céréales / Cereals; Croustilles et collations
salées / Chips & Salty Snacks; Café et thé / Coffee & Tea; Condiments
et pâtes à tartiner / Condiments & Spreads. Everything else is
pharmacy/beauty/household.

### Jean Coutu — [jeancoutu.com](https://www.jeancoutu.com)

One food department (FR | EN): **Confiserie et épicerie |
Confectionery and grocery** — Alimentation / Grocery; Grignotines /
Snacks; Arachides et noix / Peanuts and nuts; Breuvages / Beverages;
Bébé / Baby Food; Chocolat / Chocolate; Gomme à mâcher / Chewing gum;
Bonbons / Candy; Coffrets-cadeaux / Gift sets; Surgelés / Frozen
foods; Barre collation / granola / Snack/granola bar. All other Shop
departments are non-food.

### Familiprix — [familiprix.com](https://www.familiprix.com)

Pharmacy; food corners only (FR | EN): **Aliments et breuvages |
Food and Beverages** — Breuvage / Beverage (Boissons isothoniques /
Isothonic Drinks; Eau / Water; Jus, cocktails et boissons / Juices,
Cocktails and Drinks; Café / Coffee); Collations / Snacks
(Croustilles / Chips; Noix et arachides / Nuts and Peanuts; Barre
collation / Snack Bar). **Confiserie et fêtes | Sweets and Birthday**
— Confiserie saisonnière / Seasonal Candies; Confiserie / Candy.
Plus Suppléments de repas / Meal supplements (health-adjacent).

### Dollarama — [dollarama.com](https://www.dollarama.com)

No e-commerce and no category browsing: corporate site only; same-day
delivery is outsourced to DoorDash/Instacart. No taxonomy of its own.

### Brunet — [brunet.ca](https://www.brunet.ca)

No food category taxonomy: pharmacy services site (Santé / Bien-être
/ Photo); online shopping only via Uber Eats/DoorDash "Livraison
express".


---

## Independent and specialty stores

### Akhavan — [akhavanfood.com](https://akhavanfood.com) (WooCommerce, EN)

Flat, no subcategories: SEASONAL PRODUCTS; BEANS & GRAINS; HERBAL
WATERS; CANNED FOODS; COOKIES & SNACKS; DRIED FRUITS; DRIED
VEGETABLES; GENERAL GROCERIES; JAMS & MOLASSES; NUTS & SEEDS; OIL &
VINEGAR; OLIVES & PICKLES; RICE & FLOURS; SPICES & SAFFRONS; SUGARS;
TEA & HERBS. (COSMETIC & CLEANING and KITCHEN & BBQ excluded.)

### Aliments Merci — [alimentsmerci.com](https://alimentsmerci.com) (WooCommerce, FR)

Deep tree (via the public Store API). Top levels [EN gloss]:
Boulangerie [Bakery]; Breuvages [Beverages]; Café [Coffee]; Cuisines
du monde [World cuisines]; Épicerie [Grocery]; Épices, Herbes et Thés
[Spices, herbs & teas]; Fruits et légumes [Produce]; Fruits séchés et
noix [Dried fruit & nuts]; Produits réfrigérés [Refrigerated].

- **Boulangerie** — Farine, Semoule et Grain Sans Gluten; Farines, Semoule et Grain; Farines, Semoules et Grains biologique; Fécules, Levures et Gélifiants; Pain; Sirops et Essences; Sucres et Édulcorants (+ Biologique)
- **Breuvages** — Boissons & kombuchas; Boissons Végétales; Eaux; Jus; Jus biologiques; Lait
- **Café** — Café de Céréales et Substituts; Café Héritage; Café Lenoir & Lacroix; Café Santana (brand-named categories)
- **Cuisines du monde** — Sauces asiatique; Sauces et Pestos; Sauces Indienne; Sauces Piquantes
- **Épicerie** — Miel et dérivés; Grignotines; Vinaigre et Vinaigrette; Algues; Beurre de Noix (+ Biologique); Biscuits & Desserts; Bonbons; Céréales (biologique / Sans Gluten / Vrac); Chocolat et Cacao (+ Vrac); Collations; Compotes et Purées; Condiments et Marinades; Confitures; Couscous & Quinoa; Craquelins & Galettes (bio / Sans Gluten); Croustilles; Huile d'Olive (+ Biologique); Huile de Coco; Huile Végétale; Lait de Coco; Légumineuse (Biologique / en conserve / en Vrac); Olives; Pâtes (Biologique / en Vrac / Sans Gluten); Poisson et fruit de mer; Protéines Végétales et Tofu; Riz (Biologique / en Vrac); Soupes et Bouillons; Tomates (+ Biologique). Note: several API category names embed internal POS codes (e.g. "3600 Grignotines") — data-quality artifact of the store's own catalog.
- **Épices, Herbes et Thés** — Épices Vrac Biologique; Épices, Herbes et Piments (+ Biologique / en Vrac); Herbes Médicinales (+ Biologique / en Vrac); Sel; Thés et Tisanes (+ Biologique / en Vrac)
- **Fruits et légumes** — Légumes et Fruits en conserves (only)
- **Fruits séchés et noix** — Fruits Séchés (Biologique / Format Détail); Noix et Graines (Biologique / en Vrac / Format Détail)
- **Produits réfrigérés** — Prêt-à-Manger
- Excluded: Produits nettoyants; Soin personnel et aromathérapie. Attribute variants (biologique, sans gluten, en vrac) recur as separate categories instead of filters.

### Ayke — [ayke.ca](https://ayke.ca) (WooCommerce)

Single-product store: one category, Sirop d'érable [Maple syrup].

### Baia dei Formaggi — [labaiadeiformaggi.com](https://www.labaiadeiformaggi.com) (Wix; shop on Restomate)

Flat bilingual tabs (FR / EN published): Fromage / Cheese;
Charcuterie / Deli; Huile d'Olive / Olive Oil; Olives; Vinaigre
balsamique / Balsamic vinegar; Sauce Tomate / Tomato Sauce; Tomates;
Sauces piquantes / Hot Sauces; Pâtes fraîches / Fresh Pasta; Pâtes
sèches / Dry pasta; Pâtes divers / Miscellaneous Pasta; Riz / Rice;
Pain / Bread; Antipasti; Casse-Croûte / Snacks; Confitures / Jams;
Breuvages / Beverages; Autres produits populaires / Other popular
products. (Online ordering was temporarily paused at visit time.)

### Berchicci — [store.berchicci.ca](https://store.berchicci.ca) (OpenCart, EN)

Flat: Special of the Month; Pasta and Rice; Tomatoes; Olive Oil;
Cheese and Deli; Coffee; Snacks; Seasonal Products; Balsamic
Vinegars; Gluten Free; Beverages; Condiments; Jams; Chocolate;
Candies; Biscuits; Fish; Gift Baskets; Baking Essentials;
Sauce-Pesto; Olives; Vegetables; Sale. (Soaps, Accessories excluded.)

### Bio Locaux / Épicerie Loco — [epicerieloco.ca](https://www.epicerieloco.ca)

**Blocked:** the shop runs on BocoBoco (bocoboco.ca), a members-only
weekly-order platform; the catalog and its categories are not visible
to guests. Not documentable without an account.

### Birri — [birri.ca](https://www.birri.ca) (Wix Stores, FR)

Flat: Légumes [Vegetables]; Fruits; Fines Herbes et Aromates [Herbs
& aromatics]; Surprises!

### Boucherie Nordest — [boucherienordest.com](https://boucherienordest.com) (Shopify, FR)

- **Boeuf** [Beef] — Les coupes tendres; Les coupes économiques; Les coupes transformées; Les coupes savoureuses (subcategories by cut style — unique among the butchers)
- Agneau [Lamb]; Poulet [Chicken]; Porc [Pork]; Boîte [Boxes — boîtes familiales]; Prêt à manger [Ready-to-eat]; Saucisse [Sausages — "Saucisses et charcuteries"]. Épicerie is an info page, not a collection.

### Boucherie Saint-Vincent — [saint-vincentbio.com](https://www.saint-vincentbio.com) (WooCommerce, FR)

Organic butcher; every category carries the "biologique" qualifier.
Menu tree: **Formats économiques** — Panier viandes bio; Pièce
entière & quartier. **Épicerie bio** (direct). **Viandes rouges** —
Boeuf biologique; Veau biologique; Agneau biologique; Abat
biologique. **Viandes blanches** — Porc biologique. **Volailles** —
Oeuf biologique; Canard biologique; Dinde biologique; Oie
biologique; Pintade biologique; Poulet biologique. **Charcuterie** —
Charcuterie biologique; Fond biologique; Marinade biologique;
Prêt-à-manger biologique; Saucisse biologique. The flat category
registry adds: Lapin biologique, Panier légumes bio, Panier vedette,
Spécialités des fêtes, Promotions. (Home delivery via the Maturin
marketplace.)

### Brouette Maraîchère — [labrouettemaraichere.com](https://www.labrouettemaraichere.com) (Shopify, FR)

Shop closed until January 2027 (notice on site); catalogue menu
captured. Flat, plants/seeds (food-growing, not groceries): Plants
potagers; Fines herbes; Fleurs; Arbustes Fruitiers; Nouveauté 2026;
Herboristerie; Plants pollinisateurs; Permaculture; Semences.

### Carlota Boulangerie — [carlota-boulangerie.square.site](https://carlota-boulangerie.square.site) (Square)

Flat: Pan Dulce; Tamales; Pan De Muerto; Épicerie; Desserts maison;
Nos Collaborations. (Boutique cadeaux and Ateliers are non-food.)

### Chez Michel — [sapinchezmichel.com](https://sapinchezmichel.com) (Shopify)

Non-food store (Christmas trees, wreaths, accessories). No food
taxonomy — its Phase 2 "search" flag comes from its Square/Shopify
product search over trees.

### En Tout K — [entoutk.ca](https://entoutk.ca) (Wix Stores, FR)

Shop not yet selling at visit time; category list visible. Flat:
Canneberges; Lavande; Érable; Fromages et yogourt; Produits de la
brebis; Huiles et graines végétales; Bleuets; Thés et tisannes;
Produits du terroir; Boisson. (Soap/body-care and souvenir sections
excluded.)

### Épicerie du Bazaar — [bazaarfood.ca](https://www.bazaarfood.ca) (Wix Stores, FR)

Flat, no subcategories: ÉPICERIE; HYDROLATS; THÉ & INFUSIONS; CRÈME
GLACÉE; CORNICHONS; BOISSONS; CANETTES; RIZ; CONFITURES; PÂTISSERIE;
NOIX; CHARCUTERIE; SOLDES. Homepage tiles add Repas Préparés, Fruits
Secs. (Équipements de Cuisine excluded.)

### Épicerie Latina / Chez Latina — [chezlatina.com](https://www.chezlatina.com) (shop on Panierdachat, FR)

Flat: Pâtisseries Latina; Surgelés Latina; BBQ À GRILLER; Boucherie;
Poissonnerie; Soupes; Sauces pour pâtes; Repas en pots; Créations
Latina — Cuit sous vide; Fonds et bouillons Latina; Quiches,
tourtières et pâtés; Sandwichs; Salades; Charcuterie; Baguette et
pain; Produits laitiers et fromages; Fruits et légumes; Boissons.

### Épicure Market — [shopepicure.ca](https://shopepicure.ca) (Shopify, EN)

Full tree, 18 departments [FR glosses for top levels]:

- **Fresh Fruits** [Fruits frais] — Berries; Melons; Apples; Tropical Fruits
- **Fresh Vegetables** [Légumes frais] — Herbs; Roots Vegetables; Leafy Greens; Vegetables
- **Smoked/Fresh fish & seafood** — Smoked Fish; fresh Wild Fish; Dry Fish; frozen fish
- **Fresh Meat & Poultry** — Beef; Lamb; Pork; Veal; Bacon & Sausages; Poultry; exotic meat
- **Hot/cold beverages & Alcohol** — Coffee & Tea; Herbs & Flowers; Cocoa; Energy Drinks; Juices; Soft Drinks; Water; Beer & Cider; Drink Mixes; Iced Tea & Lemonade; Mineral Water; Refrigerated Juices; Vegetable Juices; Wines; Ice Coffee; Almond/Soy beverages
- **Bread, Buns & Baked Goods** — Tortillas & Tacos; Bagels; Breads; Pitas; Lavash
- **Canned & Packaged Goods** — Beans & Legumes; Dried Vegetables; Asian Products; Soups & Broths; Packaged meat; Packaged Fish & Seafood; Condensed & Skim Milk/Coconut; Packaged Vegetarian; Pudding & Jello
- **Dairy Products** — Butter & Margarine; Eggs; Yogourts; Almond & Soy Beverages; Cream; Milk; Kefir; Milk Shake Drinks; Packaged Cheese; Vegan
- **Pasta, Rice, Grain & Sauces** — Gnocchi; Couscous; Grains & Wheat; Pasta; Rice & Corn; Buckwheat; Sauces & Paste; Salsas / Mexican Products; Tomato Sauces & Pastes; Quinoa; Instant Noodles, Ramen Bowls & Ready Meals; Beans & Peas
- **Deli & Ready to Eat** — Deli Meats; Epicure Signature buffet; Olives; Organic Deli Meats; Tofu; Cheeses; Dips & Spreads; Patties; Sandwiches; Sauces; Soups
- **Nuts & Dried Fruit** — Nuts; Chickpeas & Corn; Seeds; Organic Nuts; Organic Dried Fruit; Nuts & Fruit Mix; Dried Fruits
- **Deserts, Snacks & Crackers** [sic] — Cereal, Granola & Oats; Bagged Snacks; Cookies; Gum & Candies; Rice Cakes; Cakes & Pastries; Chocolate & Marzepan; Crackers; Granola & misc Bars; Wafers; Dry Bread Rings; Gingerbread Cookies; Marshmallow & Jelly; Halva; Sugar Free; Vegan
- **Jams, Syrups, Honey & Butters** — Nut Butters; Syrop & Honey; Jams & Jellies; Fruits; Chocolate & Sweet Spreads
- **Condiments, Oils & Vinegars** — Dips & Spreads; Oils; Pesto; Salad Dressings; Vinegars & Lemon Juice; Condiments; Olive Oils; Sauces
- **Marinated & Pickled Vegetables** — Pickles; Marinated Salads/Spreads; Marinated mushrooms; sauerkraut; Olives & Cappers; Marinated & Pickled Vegetables
- **Frozen Products** — Dinners; Ice Cream; Bakery; Fish & Seafood; Fruits & Berries; Juices; Pizzas; Vegetables; ice; Snacks & Cheesecake; Dumplings & Perogies; Vegan; Meat
- **baking Ingredients, Salt, Spices and Sugar** — Flours & Mixes; Breadcrumbs & Croutons; Salad Dressings; Sugars & Substitutes; Spices & Seasonings; baking ingredients; Salt; Waffer Sheets & Fillo Shells; Pudding & Jello; Dry Bouillon & Sauce Mix
- **Organic** (cross-cutting) — Dairy; Meat & Poultry; Bakery; Deli & Cheeses; Groceries; Nuts & Fruits; Beverages; Snacks
- Excluded: Health & Beauty, Household Items.

### Euro Market — [euro-market.ca](https://euro-market.ca) (Shopify, bilingual; EN recorded)

Mirrors the Les 3 Gourmets structure (same "sweet/salty grocery"
pattern): **Salty grocery store** — Herbs, spices and seasonings;
Kitchen aid and prepared sauces; Sauces and condiments; Broths and
soups; Cooked dishes and canned vegetables; Canned fish; Pasta,
puree, rice and cereals; Everything for the aperitif. **Sweet
groceries** — Cookies and cakes; Breakfast; Cafés, chocolate powder,
teas and infusions; Compotes, fruit salads and dessert creams; Pastry
aid; Sugars and sweeteners. **Candy and chocolates** — Candy;
Chocolates; Chewing gums. **Drinks** — Soft drinks and silts [sic];
Flat juice and drinks; Syrups and concentrated; Alcohol-free beers
and drinks; Waters. **Surgelés** — Surgelés - Glaces; Surgelés -
Salé. **Babies and toddlers** — Meals and compotes for babies (rest
non-food). Excluded: Hygiene and body care, Household products.

### Ferme Hill Head Chili — [fermehillheadchili.ca](https://www.fermehillheadchili.ca) (Square Online, FR)

Flat: semences [seeds]; sauces; autre produits transformés [other
processed products]; précommande de plants de piments et tomates
[plant pre-orders].

### Fines Herbes Patrick Lauzon / Chacun son arôme — [chacunsonarome.com](https://chacunsonarome.com) (WooCommerce, FR)

Flat: Fines herbes déhydratées; Herbes salées; Sauces au piments
forts; Huiles aromatisées; Plants de fines herbes; Plants de légumes.

### GD Supermarché — [gdsupermarche.com](https://gdsupermarche.com) (OpenCart, EN)

- **Vegetables**; **Fruits** (leaves)
- **Meat** — Beef & Veal; Chicken & Turkey; Pork; Lamb; Sausages & Bacon; Duck & Rabbit (plus a prepared BBQ-to-go line)
- **Fish & Seafood** — Fresh Fish; Chilled seafood
- **Snacks** — pastry; Chips, Biscuits & Cakes; Ice cream; Instant Drinks & Beverages; jelly (plus seasonal festival leaves)
- **Dairy & Egg** — Milk & Cream; Eggs; Yogurt; Butter & Cheese
- **Frozen Foods** — Staple food (dumplings, steamed buns); Other Frozen Foods
- **Hotpot** (leaf — a category concept absent from Western taxonomies)
- **Soy Products** — Tofu; Soy Drinks; Bean Paste
- **Flour & Dried Food** — Scented Tea; Soup stock, groceries; Noodle & Flour; Smoked Foods & Pickled Foods
- **Spice & Sauce** — Cooking Wine, soy sauce, vinegar, oil; Flavored Sauce; Pickled Vegetables
- **Instant Food** — Instant Noodles; noodle, rice noodle
- Seasonal leaves: Moon Cake; Special Spring Festival goods. Excluded: Household & Protective Equipment, Beauty & Health.

### Hova Ranch — [hovaranch.com](https://hovaranch.com) (WooCommerce, FR)

No categories: flat list of 8 products (meat boxes, eggs, gift
certificate). The "Naturel / Nourri à l'herbe / Sans hormone /
Pâturage" tiles are attribute badges, not categories.

### Intermarché Palumbo — [marchepalumbo.com](https://www.marchepalumbo.com)

No online shop (marketing/flyer site; "Departments" is a dead nav
label). No category tree.

### Jardins Mil'Herbes — [milherbes.com](https://milherbes.com) (WordPress.com)

No online shop (in-person kiosk at Marché Jean-Talon). Informational
groupings only: "Plants bio" (nursery plants), "Fruits & légumes bio"
(flat seasonal list).

### Johnny Prosciutto — [johnnyprosciutto.com](https://johnnyprosciutto.com) (WooCommerce, EN)

Flat, product-form categories: Promotions; Volume Pricing; Artisanal
Prosciutto; Artisanal Sopressatas; Artisanal Dry Cured Sausages;
Artisanal Dry Cured Capocollo; Artisanal Dry Cured Lonzino; Artisanal
Salami; Artisanal Pancetta; Specialty Cheese; Vacuum Sliced Products;
Vacuum Sealed Fresh Sausages; Olives; Condiments; HandCrafted
Tarallis. (Merchandise excluded.)

### La Marguerite — [lamarguerite.ca](https://www.lamarguerite.ca) (Shopify, EN)

Kosher caterer/grocer; flat collections: Signature Platters; Gourmet
Lunch Box; Salads & Vinaigrettes; Gourmet Grocery; Sandwiches &
Signature Salads; Soups; Sushi; Side Dishes; Fish; Chinese; Meats;
Chicken; Bakery & Viennoiserie; Gourmet Desserts; Cookies; Frozen.

### La Moisson — [lamoisson.com](https://lamoisson.com) (Shopify, FR)

Two-level tree under "Épicerie" [EN glosses for top levels]:

- **Préférences Alimentaires** [Dietary preferences — cross-cutting] — Cétogène; Intolérance au gluten; Végane; Biologique; Sans allergènes
- **Aliments Frais** [Fresh foods] — Viandes; Boulangerie; Produits laitiers & Oeufs; Prêt-à-manger
- **Garde-Manger** [Pantry] — Collations; Craquelins & Croustilles; Soupes & Bouillons; Céréales & Granolas; Farines & Préparations; Légumineuses; Graines, Noix & Fruits séchés; Épices & Assaisonnements; Huiles & Vinaigres; Sucres & Édulcorants; Confitures, Tartinades & Beurres; Friandises, Chocolats & Gommes; Barres & Biscuits; Condiments, Sauces & Conserves; Pâtes, Riz & Grains entiers
- **Cafés, Thés & Tisanes** [Coffee & tea] — Cafés; Thés & Tisanes; Boissons Chaudes
- **Boissons** [Beverages] — Jus & Smoothies; Eaux & Eaux pétillantes; Boissons végétales; Boissons gazeuses & Boissons énergisantes; Kombucha & Infusions; Bières, Vins & Spiritueux
- **Aliments Surgelés** [Frozen] — Fruits & Légumes; Boulangerie; Desserts; Plats cuisinés; Pizza; Smoothies
- **Bébé & Enfant** [Baby & kids — food]
- Excluded top-levels: Suppléments, Soins & Beauté, Maison, Animaux.

### La Vieille Europe — [lavieilleeurope.com](https://lavieilleeurope.com) (Shopify, EN; FR toggle)

Flat collections (parenthetical = the collection's own description):
Coffee & Tea (Coffee Beans, Tea, Matcha, Accessories); Condiments
(Oils, Vinegar, Sauces, Mustards); Preserves (Spreads, Jams,
Preserves, Honey); Pantry (Pasta, Rice, Canned Goods, Spices); Treats
(Chocolate, Biscuits, Sweets, Candy); Bar & Mixology (Bitters,
Liqueurs, Soda, Juice); Hors d'oeuvre (Antipasti, Snacks, Crackers,
Chips); Cheese; Curated gifts. (Self-Care excluded.)

### Le Baobab — [lebaobab.store](https://lebaobab.store) (WooCommerce, FR)

- **Alimentation** [Food] — Céréales; Viandes et poissons; Produits surgelés; Épices et assaisonnements; Produits secs; Boissons; Produits en conserve
- Legacy top-levels also present: Groceries; Juice; Non classé; Vedettes. Excluded: Produits de beauté (large — 373 products), Livres et médias, Vêtements, Accessoires, Décoration.

### Le Capitaine — [lecapitaine.ca](https://lecapitaine.ca) (Shopify, EN)

Farm producer (eggs/honey/maple): **EGGS** — Brown Eggs; White Eggs;
Free Range Eggs; Free Run Eggs; Double Yolk Eggs; Duck Eggs; Guinea
Fowl Eggs. **HONEY** — Clover; Wild Flowers; Buckwheat; Blueberry;
Churned; Pollen; Pure Royal Jelly. **MAPLE SYRUP** (flat);
**BUCKWHEAT** (flat).

### Le Marché des Saveurs du Québec — [lemarchedessaveurs.com](https://www.lemarchedessaveurs.com) (Shopify, FR)

- **Épicerie fine** [Fine grocery] — Produits saisonniers; Caramels et tartinades; Champignons; Condiments; Confiserie, biscuits & chocolats; Confitures et tartinades; Épices; Érable; Granola; Moutardes, sauces piquantes; Miels; Pesto, sauce, bouillon; Salsa, tapenade et craquelins; Vinaigres, huiles, vinaigrettes et mayonnaises
- **Boucherie** [Butcher] — Terrines, charcuteries, confits et gelées
- **À boire** [Drinks] — Infusions
- **Fromagerie** [Cheese]; **Coffrets cadeaux** [Gift boxes]. Excluded: Cosmétique, Livres, Carte Cadeau.

### Le Monde au Naturel — [mondenaturel.ca](https://mondenaturel.ca) + [shop.mondenaturel.ca](https://shop.mondenaturel.ca) (Shopify, FR)

Main site groups "Épicerie santé" as: Farines, céréales et grains
biologiques; Huiles, vinaigres et condiments naturels; Boissons
végétales, thés et tisanes; Collations santé, barres et noix
biologiques; Sucres naturels, sirops d'érable et miel. Shop "Épicerie"
submenu: Alimentation; Aromates; Boulangerie; Breuvages; Clienteles;
En-cas; Déjeuner; Friandises; Germinations; Pré-emballés; Produits
alimentaires de base; Semences; Tartinades. (Suppléments, Soins/
beauté, Produits ménagers are the store's larger non-food side.)

### Le Potager Mont-Rouge — [potagermont-rouge.ca](https://www.potagermont-rouge.ca) (Square Online, FR)

Flat: Paniers thématiques; Idées repas; Produits laitiers; Viande;
Oeufs et compléments; Fines herbes et épices; Mets transformés;
Produits d'érable; Desserts; Miel Lussier; Conserves et marinades;
Confitures; Gelées; Légumineuses; Cidre McKeown. (Cueillette de
pommes is a U-pick activity; Savon et Gel excluded.)

### Les 3 Gourmets — [epicerie-les3gourmets.ca](https://www.epicerie-les3gourmets.ca) (Shopify, EN)

- **Sweet groceries** — Rusks; Toasted Bread Spreads, Cereals and Cereal bars; Cookies and Cakes; Candy; Chocolates; Jams, Compotes, and Creams; Syrups and Concentrates; Sugars, Flours, Coulis and Cake Preparations
- **Salty groceries** — Kitchen help; Crisps and appetizers; Condiments and Sauces; Canned vegetables; Canned Fish; Oils, Vinegars and Dressings; Pasta, Rice, Purees and starches; Ready meals; Soups and Croutons
- **Refreshing drinks** — Fruit soft drinks; Plates of fruit drinks [sic]; Soy drinks; Soft drinks; Coffees, Teas and Hot Drinks; Mineral Waters and Spring Waters; Fruit and vegetable juices
- **Fresh** — Cheese; Fresh products
- **Fresh frozen** — Desserts; Frozen meals
- Leaf categories: Spices; Gluten Free. (Babies — partial; Hygiene and beauty excluded.) The sweet/salty/drinks split recurs at Euro Market — a French fine-grocery pattern.

### Les Jardins d'Arlington — [jardinsdarlington.ca](https://jardinsdarlington.ca) (WordPress)

No online catalog: CSA baskets and sourdough baskets via a
members-only login. No taxonomy.

### Les Jardins de Stéphanie — [les-jardins-de-stephanie.panierdachat.app](https://les-jardins-de-stephanie.panierdachat.app) (Panierdachat, FR)

Boutique structure: Produits à la carte; Forfait paniers et
abonnements; Achat en gros ou semi-gros. Product groupings announced:
Légumes; Fruits; Herbes et épices fraîches; Divers (œufs, sauces,
tofu). (Nesting under "Produits à la carte" unverified.)

### Les Jardins Sauvages — [jardinssauvages.com](https://jardinssauvages.com) (WordPress; shop via Tixigo)

Main-site product groupings (FR): CONSERVE ET SÉCHÉS [Preserves &
dried]; PRÊT-À-MANGER, SAUCES ET PLATS CUISINÉS CONGELÉS SOUS VIDE
[Ready-to-eat & frozen cooked meals]; LÉGUMES SAUVAGES CONGELÉS
[Frozen wild vegetables]; PRODUITS FRAIS EN SAISON [Fresh seasonal];
KOMBUCHAS ET SODAS; GUIDE DE PRODUITS TRANSFORMÉS. Wholesale:
Conserves à la caisse; En vrac pour les chefs. The Tixigo ordering
catalog had no service dates available and could not be enumerated.


### Magasin Amira — [magasinamira.ca](https://magasinamira.ca) (Shopify, FR)

Flat and messy: 100+ collections mixing categories, promotions and
non-food. Food collections (verbatim): ASSAISONNEMENT; Biscuits,
Collation & craquelins; Boissons froids; Bouillon; Boulangerie;
CHOCOLAT; Chocolat & bonbon; Chocolat dubai; Condiments, huiles &
vinaigre; Confitures, sirop & miel; Couscous & pates; Dattes et
figue; Desserts; EPICERIE SUCRÉE; Épicerie; Epices & Herbes; Extrait,
Essence & colorant; FRUIT EGYPTIENNE; Fruits & legumes; Ingrédients
pour cuisson; Lait concentre; Legumes secs & semoule; Legumes secs,
riz & semoule; Melanges & collation; Molasses & Syrups; Olives &
marinades; PATISSERIES ORIENTALES; Poissons & fruits de mer; Poudre
vanille, cacao, pate, mahlab & autres; Produits en conserve; Produits
Frais; Produits laitier, fromage & charcuterie; Produits surgeles;
Sel & sucre; Tahina & Halvah; Vrac; EAU ZAMZAM 1L. Cautionary example
of an unmaintained taxonomy: duplicates (two "Legumes secs"
variants, three chocolate variants), ALL-CAPS/Title-case mixing, and
promo collections ("flyer 23/07", "FIFA COUPE DU MONDE 2026")
interleaved with real categories.

### Marché Andes — [marcheandes.com](https://www.marcheandes.com) (WooCommerce, FR/ES)

- **Boissons** — Boisson en poudre
- **Garde-manger** — Assaisonnements; Biscuiterie; BONBONS + SUCRERIES; Café/Chocolat; collations salées; Farines; Haricots; Mais grains et autres; Panela/Sucre/Édulcorants; Pâtisserie; Piments et conserves; Riz; Sauces; Soup [sic]; Thé/Tisanes; TORTILLAS / TOSTADAS / NACHOS; YERBA MATE
- Header departments also exist: Boulangerie, Boucherie, Prêt Pour Emporter; the homepage carousel shows Congelés (not an API category). (Maison/Nettoyage excluded.)

### Marché Bonanza — [bonanzalalumiere.com](https://bonanzalalumiere.com) (Shopify, FR/EN)

Flat department collections: Boulangerie; Charcuteries et épicerie
fine; Fromages fins; Fruits; Légumes; Nos spéciaux; Produits
réfrigérés; Produits surgelés; Prêt-à-manger; Saisonnier; Viandes,
volailles et poissons; Épicerie. (Plus a "Marques" brand directory.)

### Marché C&T — [marchect.ca](https://www.marchect.ca)

Marketing site only (flyers); no online shop, no taxonomy. Included
because it was swept as an extra — it is not one of the 81
search-capable stores.

### Marché Fu Tai — [marchefutai.ca](http://www.marchefutai.ca) (OpenCart, EN)

Same store group/platform as Lian Tai: **GROCERY** — Juice & Drink;
Bread; Oil, Salt, Sauce, Vinegar; Rice and Noodles; Snack Series;
Instant Noodles. **FROZEN** (leaf). **VEGETABLES & FRUITS** — Fruits;
Vegetables. **MEAT & FISH** (leaf). (DAILY SUPPLIES excluded.)

### Marché Korea — [marchekorea.com](https://marchekorea.com) (WooCommerce)

Full tree via the public Store API (92 categories). Labels are
published Korean + French; English glosses are ours:

- **간식 Collations** [Snacks] — 과자 쿠키 Biscuits Cookies; 디저트 Desserts; 사탕/초콜릿 Bonbons chocolats; 젤리-곤약젤리 Gelées / konjac jelly
- **과일/야채 Fruits et légumes** [Produce] — 과일 Fruits; 말린 과일과 채소 Fruits, légumes séchés; 채소 Légumes
- **그로서리 Épicerie** [Grocery] — Autres produits; 김/미역 Algues séchées [seaweed]; 떡 Gâteaux de riz [rice cakes]; 즉석 조리 상품 Plats préparés (즉석 국과 소스류 Soupes et sauces préparées; 즉석 조리 밥/죽 Riz préparé); 통조림 Aliments en conserve; 파우더 Poudres; 향신료/양념 Épices et assaisonnements
- **냉장/냉동 Réfrigérés / surgelés** [Refrigerated / Frozen] — 냉동 Surgelés (Natto et fèves de soja; Riz surgelé; Pains et gâteaux de riz surgelés; Légumes surgelés; Soupes surgelées; Nouilles surgelées; 만두류 Dumplings; 브랜드 김치 Brand Kimchi; 어묵/게맛살 Gâteaux de poisson); 냉장 Réfrigérés (Soupes réfrigérées; Nouilles réfrigérées; Légumes marinés; 두부/유부 Tofu; Saucisses de poisson)
- **면류 Nouilles** [Noodles] — 건조면 Nouilles Séchées; 봉지라면 Nouilles instantanées en sachet; 실온보관 국수 Nouilles température ambiante; 컵라면 Nouilles instantanées en tasse
- **빵/베이커리 Pain** [Bread & bakery] (leaf)
- **생선/해산물 Fruits de mer** [Seafood] — Dried Fish, Seafood; Frozen Fish, Seafood; Prepared Fish, Seafood; Snacks (these four in EN on the site)
- **쌀/곡물류 Riz** [Rice & grains] — 잡곡 Riz et céréales mélangés; 백미 Riz Blanc
- **요구르트/우유 Dairy** — Dairy; Yogurt, Probiotics (EN on site)
- **음료 Beverages** — Coffee; Dairy; Drink Mixes; Health Drinks; Juice, Soda; Plant-Based; Tea; WATER (EN on site)
- **장류/소스 Sauces** — Cooking Wine; Instant Sauce Mix, Powder; Marinade; Oil; Paste; Red Pepper Powder; Salt, Sugar, Dry Seasoning; Seasoning Sauce, Dressing; Sesame Seeds; Soy Sauces; Syrup, Spread; Vinegar (EN on site)
- **정육/계란** [Meat & eggs] — 계란 [Eggs]; 닭/오리 [Chicken, duck]; 돼지고기 [Pork]; 소고기 [Beef]
- **한국식품 HOMEMADE** — 도시락 [Lunch boxes]; 반찬가게 [Side-dish shop]; 카페테리아 [Cafeteria]; 할매김치 HALMAE KIMCHI
- Excluded: 생활용품 Articles ménagers (Beauty, Health, Household, Kitchenware).

### Marché Lian Tai — [marcheliantai.ca](https://www.marcheliantai.ca) (OpenCart, EN)

**GROCERY** — Bread; Oil, Salt, Sauce, Vinegar; Rice and Noodles;
Snack Series; Instant Noodles. **FROZEN** (leaf). **VEGETABLES &
FRUITS** — Fruits; Vegetables. **MEAT & FISH** (leaf). (DAILY
SUPPLIES excluded.)

### Marché Sheng Tai — [marcheshengtai.ca](https://www.marcheshengtai.ca)

No online shop: homepage flyer display only ("Current Special" +
featured products). No category structure — its Phase 2 search flag
does not correspond to a product catalog.

### Mrakovic — [mrakovic.com](https://mrakovic.com) (Shopify, EN)

Flat collections: Grocery; Sweets; Spreads; Mrakovic Products;
Frozen Foods; Dairy; Butcher Shop; Baking Goods; Deli; Ready-to-go
Meals. (Personal Care Production, Merchandise excluded.) Footprint
qc-unverified in our dataset.

### Odessa Poissonnier — [odessapoissonnier.com](https://odessapoissonnier.com) (Shopify, FR)

Flat collections: Plateaux; Sushis; Prêt-à-manger; Poissons; Fruits
de mer; Épicerie. (Accessoires & ustensiles excluded.)

### Olives Olives — [oliveolives.com](https://www.oliveolives.com) (WooCommerce, FR; EN version exists)

- **Huiles d'olive** [Olive oils] — POUR TOUS LES JOURS [everyday]; GRANDS CRUS; BIOLOGIQUES [organic]; AROMATISÉES [flavoured]
- **Vinaigres** [Vinegars] — Vinaigres de vin et de fruit; Vinaigres balsamiques; Vinaigres de Xérès [sherry]
- **Garde-manger** [Pantry] — Olives; Tapenades; Accompagnements
- (Cadeaux / Maison & Cadeaux are gift sections — excluded.)

### Pastificio Sacchetto — [pastificio.ca](https://www.pastificio.ca)

Brochure site, no online shop. Product groupings on the fresh-pasta
page: Stuffed pasta; Special pasta; Long pasta; Short pasta; Sheet
pasta.

### Poissonnerie La Mer — [lamer.ca](https://www.lamer.ca) (Shopify, FR)

- **Poissons** [Fish] — POISSONS FRAIS; POISSONS CONGELÉS; POISSONS ENTIERS; FILETS & DARNES; SAUMON; THON
- **Fruits de Mer** [Seafood] — CALMARS & PIEUVRE; CRABE; CRUSTACÉS; CRABE DES NEIGES; CREVETTES; FRUITS DE MER CONGELÉS; HOMARD; HUÎTRES; LANGOUSTINES; MOLLUSQUES; MOULES; OURSINS; PALOURDES; PÉTONCLES
- **Prêt à manger** [Ready-to-eat] — CAVIARS; PLATEAUX DE FRUITS DE MER; PRODUITS FUMÉS; PRODUITS MAISON; SALADES DE FRUITS DE MER
- **Épicerie** (leaf). ("Recettes" is articles, not a category.)

### Sabor Latino — [saborlatino.ca](https://saborlatino.ca) (WooCommerce, FR)

- **ALIMENTS** [Foods] — Huile; Sucre, panela et édulcorants; Céréales; Chocolat, café et thé; Mélanger pour le thé glacé et les boissons; Produits en conserve; Grains; Farines et mélanges à préparer; Produits laitiers et œufs; Pâtes; Pâtisserie; Sel; Sauces épices et condiments; Suppléments; Tortillas; Boissons; Boulangerie
- Top-levels: BOISSONS; VIANDE, POULET, PORC ET POISSON; SURGELÉS; FRUITS ET LÉGUMES; PRODUITS LAITIERS ET ŒUFS; BOULANGERIE; GÂTEAUX, BISCUITS, SUCRERIES ET SNACKS; VINS ET BIÈRES. Nav also groups "Réfrigérés et congelés". (PRODUITS NETTOYANTS, USTENSILES DE CUISINE, ARTICLES POUR ANIMAUX excluded.)

### Shop Santé — [shopsante.ca](https://shopsante.ca) (Shopify, FR)

Food lives under "Fringales & Épicerie" [Snacks & grocery], flat:
Aliments faibles en glucides [Low-carb foods]; Barres protéinées;
Biscuits protéinés; Collations protéinées; Sirops et sauces sans
sucre; Boissons énergisantes; Breuvages protéinés; Croustilles
protéinées; Bonbons sans sucre. The rest of the store is supplements
(non-food).

### Sublime Asperge — [lasublimeasperge.com](https://www.lasublimeasperge.com) (Wix)

No online shop: the "Boutique" page describes the physical farm
store. No taxonomy.

### Au Jardin des Noix — [aujardindesnoix.com](https://www.aujardindesnoix.com) (Square Online, FR)

Sidebar categories: Nos produits → Paniers Cadeaux; Semences [Seeds];
Produits amis; Brunch. (Experiences, gifts/books, shows and events
are non-food.)

---

## Observations for designing our own taxonomy (Phase 4 input)

1. **The majors converge.** PC Express, Metro, Sobeys/IGA, Walmart,
   Costco and Giant Tiger all use the same ~12 department skeleton:
   Produce, Meat, Seafood, Dairy & Eggs, Bakery, Deli/Prepared,
   Pantry, Snacks & Candy, Beverages, Frozen — plus two cross-cutting
   re-slices almost everyone maintains in parallel: **International/
   World foods** (by cuisine) and **dietary/attribute** (organic,
   plant-based, gluten-free, halal, kosher). A classification scheme
   with one primary department + attribute tags matches how the
   industry actually organizes this.
2. **Cheese placement varies** (inside Dairy at PC Express/Metro;
   its own department at IGA/Voilà/Costco) — pick one and map the
   other.
3. **"Pantry/Garde-manger" is the universal deep node**: every full
   taxonomy explodes it into canned, baking, pasta/rice/grains,
   condiments, spices, oils & vinegars, soups, spreads, cereal. The
   subcategories are strikingly similar across chains — a ready-made
   template for our level 2.
4. **Prepared food is first-class everywhere** (Repas préparés,
   Plats cuisinés, Deli & Meals, Prêt-à-manger) and flyer items will
   need it.
5. **Specialty stores classify by product form or origin, not
   department**: butchers by species/cut, fish markets by species,
   fine grocers by sweet/salty (Les 3 Gourmets, Euro Market), ethnic
   grocers by cuisine-specific concepts with no Western equivalent
   (Hotpot at GD, Yerba Mate at Andes, banchan/Homemade at Marché
   Korea). Our taxonomy needs an "ethnic/world" attribute rather
   than forcing these into departments.
6. **Flat is the long-tail norm**: most independents have 5–20 flat
   collections and no hierarchy. Any mapping we build must accept
   flat, noisy source labels (see Amira's duplicates and Merci's
   POS-code-embedded names) — source labels cannot be trusted as a
   clean taxonomy anywhere below the chains.
7. **Attribute-as-category is common** (organic/vegan/gluten-free as
   departments or separate categories, e.g. Merci's "Pâtes
   Biologique / Pâtes en Vrac" variants). Our model should store
   these as flags, not categories — Phase 4 will need to split them
   out of source labels.
8. Coverage caveats: IGA's "Épicerie" department subcategories could
   not be captured; Giant Tiger's FR labels were unavailable (site
   defect); Brouette Maraîchère's shop is closed until 2027;
   Épicerie Loco's catalog is login-walled.
