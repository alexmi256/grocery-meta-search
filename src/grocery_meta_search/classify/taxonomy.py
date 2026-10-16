"""The adopted taxonomy: PC Express (Loblaw) grocery departments and
subcategories, as published on maxi.ca (see
docs/research/product-categories.md), with two adjustments:

- The "Natural and Organic" department is dropped: it is an
  attribute re-slice, not a product category (per the project owner's
  call — organic/vegan/gluten-free attributes are out of scope).
- Four non-grocery buckets mirror PC Express's other top-level
  departments so non-food flyer items still get exactly one category.

Keys are the English labels; FR labels ride along for display.
"""

from __future__ import annotations

# department_en -> (department_fr, {subcategory_en: subcategory_fr})
TAXONOMY: dict[str, tuple[str, dict[str, str]]] = {
    "Fruits & Vegetables": (
        "Fruits et légumes",
        {
            "Fresh Vegetables": "Légumes frais",
            "Fresh Fruits": "Fruits frais",
            "Packaged Salads & Dressing": "Salades préemballées et vinaigrettes",
            "Herbs": "Fines herbes",
            "Fresh Cut Fruits & Vegetables": "Fruits et légumes fraîchement coupés",
            "Dried Fruits & Nuts": "Fruits séchés et noix",
            "Fresh Juice & Smoothies": "Jus frais et smoothies",
        },
    ),
    "Dairy & Eggs": (
        "Produits laitiers et œufs",
        {
            "Milk & Cream": "Lait et crème",
            "Egg & Egg Substitutes": "Œufs et succédanés d'œufs",
            "Butter & Spreads": "Beurre et tartinades",
            "Cheese": "Fromage",
            "Yogurt": "Yogourt",
            "Desserts & Doughs": "Desserts et pâtes",
            "Sour Cream & Dips": "Crème sure et trempettes",
            "Lactose Free": "Sans lactose",
            "Non-Dairy Milk Alternatives": "Laits non laitiers",
        },
    ),
    "Pantry": (
        "Produits du garde-manger",
        {
            "Canned & Pickled": "Produits en conserve et marinés",
            "Baking Essentials": "Essentiels de cuisson",
            "Pasta & Pasta Sauce": "Pâtes et sauces",
            "Easy Meals & Sides": "Mets faciles et accompagnements",
            "Cereal & Breakfast": "Céréales et petits-déjeuners",
            "Honey, Syrups & Spreads": "Miel, sirops et tartinades",
            "Rice": "Riz",
            "Oils & Vinegar": "Huile et vinaigre",
            "Condiments": "Condiments et garnitures",
            "Spices & Seasonings": "Épices et assaisonnements",
            "Dried Beans, Vegetables & Grains": "Haricots secs, légumes et grains",
            "Bulk Nuts and Candy": "Produits en vrac",
        },
    ),
    "International Foods": (
        "Aliments internationaux",
        {
            "East Asian Foods": "Aliments de l'Asie de l'Est",
            "South Asian Foods": "Aliments de l'Asie du Sud",
            "Afro-Caribbean Foods": "Aliments afro-caribéens",
            "Halal Foods": "Aliments halal",
            "Kosher Foods": "Aliments casher",
            "Middle Eastern Foods": "Aliments du Moyen-Orient",
            "Filipino Foods": "Aliments des Philippines",
            "European Foods": "Aliments européens",
            "Latin American Foods": "Aliments d'Amérique latine",
        },
    ),
    "Meat": (
        "Viande",
        {
            "Chicken & Turkey": "Poulet et dinde",
            "Beef": "Bœuf",
            "Sausages": "Saucisses",
            "Bacon": "Bacon",
            "Hot Dogs": "Saucisses hot-dog",
            "Pork & Ham": "Porc et jambon",
            "Lamb & Veal": "Agneau et veau",
            "Kebabs & Marinated Meat": "Brochettes et viande marinée",
            "Game Meat, Offals & Fowl": "Viande exotique",
            "Plant-Based Meat Alternatives": "Substituts de viande à base de plantes",
        },
    ),
    "Fish & Seafood": (
        "Poissons et fruits de mer",
        {
            "Shrimp": "Crevette",
            "Salmon": "Saumon",
            "Fish": "Poisson",
            "Smoked Fish": "Poisson fumé",
            "Seafood Appetizers": "Hors-d'œuvre aux produits de la mer",
            "Shellfish": "Crustacés",
            "Squid & Octopus": "Calmar et pieuvre",
        },
    ),
    "Snacks, Chips & Candy": (
        "Grignotines, croustilles et friandises",
        {
            "Chips & Snacks": "Croustilles et grignotines",
            "Candy & Chocolate": "Friandises et chocolats",
            "Crackers & Cookies": "Craquelins et biscuits",
            "Snack Cakes": "Petits gâteaux à grignoter",
        },
    ),
    "Drinks": (
        "Boissons",
        {
            "Juice": "Jus",
            "Coffee": "Cafés",
            "Tea & Hot Drinks": "Thés et boissons chaudes",
            "Soft Drinks": "Boissons gazeuses",
            "Water": "Eau",
            "Soy, Rice & Almond Drinks": "Boissons au soja, au riz et aux amandes",
            "Sports & Energy": "Boissons énergisantes et pour sportifs",
            "Drink Mixes": "Mélanges pour boissons",
            "Non-alcoholic drinks": "Boissons non alcoolisées",
        },
    ),
    "Frozen Food": (
        "Produits surgelés",
        {
            "Ice Cream & Frozen Desserts": "Crèmes glacées et desserts glacés",
            "Frozen Fruit & Vegetables": "Fruits et légumes surgelés",
            "Frozen Meat and Seafood": "Viande et fruits de mer surgelés",
            "Frozen Meals, Entrees & Sides": "Repas, plats principaux et accompagnements",
            "Frozen Pizza": "Pizzas surgelées",
            "Frozen Appetizers & Snacks": "Entrées et collations surgelés",
            "Frozen Bakery & Breakfast": "Boulangerie et déjeuner surgelés",
            "Frozen Beverages & Ice": "Boissons glacées et glace",
            "Frozen Meatless Alternatives": "Substituts sans viande surgelés",
        },
    ),
    "Deli": (
        "Charcuterie",
        {
            "Deli Meat": "Charcuterie",
            "Deli Cheese": "Charcuteries et fromages",
            "Antipasto, Dips & Spreads": "Antipasti, trempettes et tartinades",
            "Crackers & Condiments": "Craquelins et condiments",
            "Vegan & Vegetarian": "Végétalien et végétarien",
            "Lunch & Snack Kits": "Boites-repas",
            "Party Trays": "Plateaux de réception",
        },
    ),
    "Bakery": (
        "Boulangerie",
        {
            "Bread": "Pain",
            "Buns & Rolls": "Petits pains",
            "Cookies, Muffins & Desserts": "Biscuits, muffins et desserts",
            "Bagels, Croissants & English Muffins": "Bagels, croissants et muffins anglais",
            "Wraps, Flatbread & Pizza Crust": "Roulés, pains plats et croûtes à pizza",
            "Cakes": "Gâteaux",
        },
    ),
    "Prepared Meals": (
        "Repas préparés",
        {
            "Fresh Pasta & Sauce": "Pâtes fraîches et sauces",
            "Entrees & Appetizers": "Plats principaux et apéritifs",
            "Salads & Soups": "Salades et soupes",
            "Sandwiches": "Sandwichs",
            "Sushi": "Sushis",
            "Fries & Sides": "Frites et accompagnements",
            "Pizza": "Pizzas",
            "Quiches & Pies": "Quiches et pâtés",
            "Snacks & Dips": "Collations et trempettes",
        },
    ),
    "Beer & Wine": (
        "Bières et vins",
        {
            "Beer": "Bières",
            "Wine": "Vins",
            "Cider & Coolers": "Cidres et coolers",
            "Spirits": "Spiritueux",
        },
    ),
    # Non-grocery buckets (PC Express top-nav departments).
    "Baby": ("Bébé", {"Baby Food": "Aliments pour bébé", "Baby Care": "Soins pour bébé"}),
    "Pet": (
        "Animaux",
        {"Pet Food": "Nourriture pour animaux", "Pet Supplies": "Articles pour animaux"},
    ),
    "Household": (
        "Maison",
        {
            "Cleaning & Laundry": "Entretien et lessive",
            "Paper & Storage": "Papier et rangement",
            "Home Goods": "Articles pour la maison",
        },
    ),
    "Health & Beauty": (
        "Santé et beauté",
        {
            "Personal Care": "Soins personnels",
            "Vitamins & Supplements": "Vitamines et suppléments",
            "Pharmacy": "Pharmacie",
        },
    ),
}

UNCLASSIFIED = "Unclassified"


def category_label(department_en: str, subcategory_en: str) -> str:
    return f"{department_en} > {subcategory_en}"


def category_label_fr(department_en: str, subcategory_en: str) -> str:
    dept = TAXONOMY.get(department_en)
    if dept is None:
        return category_label(department_en, subcategory_en)
    return f"{dept[0]} > {dept[1].get(subcategory_en, subcategory_en)}"
