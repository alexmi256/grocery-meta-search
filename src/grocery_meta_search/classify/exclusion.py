"""Exclusion (negative) rules for the unclassified pool.

Runs ONLY on items the text classifier left Unclassified (wired into
ingest 2026-10-16 on Alex's approval; prototype validated in
docs/research/classification-fallback-tiers.md: 212 of 1,427 pool items
excluded, 0 false fires on grocery ground truth). Purpose: keep
confidently non-grocery items out of the database — merchandise, flyer
furniture, structural garble — with the reason recorded in the ingest
stats. It never overrides a classification: any rule-vocabulary token
in the name vetoes exclusion except for the hand-vetted merchandise
phrases, whose specificity stands alone.

Layers:
  E1  merchandise phrases (durable goods, appliances, household
      consumables that ingest discards anyway)
  E0  flyer furniture (banner-led names, exact short furniture names)
  E1b supplement dosage forms (coffee capsules protected)
  E3b spaceless OCR merges carrying a merchandise substring and no
      food substring
  E2  boilerplate dominance with zero rule vocabulary
  E3  symbol/digit-heavy garble with zero rule vocabulary
"""

from __future__ import annotations

from . import rules

# ── E1: merchandise / non-food phrases (normalized, token phrases) ──────
_MERCH: tuple[str, ...] = (
    # durables, tools, auto, sports, home improvement
    "haltere", "dumbbell", "pneu", "pneus", "pirelli", "support mural",
    "supports muraux", "televiseur", "haut parleur", "bac a ordures",
    "bacs a ordures", "revetement de sol", "carreaux en mousse",
    "mousse d etancheite", "scelleuse sous vide", "machine a glace",
    "friteuse a air", "air fryer", "huile a moteur", "motor oil",
    "chauffe mains", "hand warmer", "valise", "suitcase",
    "tondeuse a gazon", "lawn mower", "souffleuse", "snow blower",
    "generateur", "generatrice", "perceuse", "scie circulaire",
    "compresseur", "nettoyeur haute pression", "pressure washer",
    "housse de moto", "cale de roue", "antigel", "antifreeze",
    "lave glace", "washer fluid", "batterie de voiture",
    "gril de jardin", "barbecue au propane", "foyer exterieur",
    "piscine", "spa gonflable", "trampoline", "balancoire",
    "jouet", "jouets", "toy", "toys", "puzzle", "lego",
    "velo", "bicycle", "casque de velo", "patins", "skates",
    "hockey", "balle de golf", "golf balls", "tente de camping",
    "sac de couchage", "sleeping bag", "glaciere rigide",
    # kitchen/home durables phrased as appliances
    "machine a cafe", "coffee maker", "melangeur sur socle",
    "robot culinaire", "food processor", "grille pain", "toaster",
    "four a micro ondes", "microwave", "aspirateur", "vacuum",
    "ventilateur", "air climatisé", "climatiseur", "humidificateur",
    "deshumidificateur", "purificateur d air",
    # paper/household consumables that ingest discards anyway
    "papier d aluminium", "aluminium foil", "papier parchemin",
    "papier ciré", "essuie tout", "paper towels", "papier hygienique",
    "toilet paper", "mouchoirs", "facial tissue", "lingettes",
    "wipes", "serviettes hygieniques", "tampons", "couches",
    "diapers", "litiere", "cat litter",
    # kimchi-adjacent care: none of these are grocery words in flyer names
    "oreiller", "pillow", "poubelle", "trash can", "secateurs",
    "etagere", "etageres", "shelving", "remise de jardin", "garden shed",
    "verrou", "lock", "gants de travail", "work gloves", "chandail",
    "sweater", "pantalon", "manteau", "winter coat", "matelas", "mattress",
    "bureau assis debout", "standing desk", "lampe", "lamp",
    "rideaux", "curtains", "miroir", "mirror", "cadre photo",
    "coussin decoratif", "serviette de bain", "bath towel",
    "drap", "literie", "bedding", "couette", "duvet",
    # hair / beauty care phrasing
    "coiffant", "capillaire", "demelant", "shampooing", "shampoo",
    "revitalisant capillaire", "masque capillaire", "pour cheveux",
    # supplements in dosage form (coffee capsules protected in E1b)
    "gelules", "softgels",
)

# ── E2: boilerplate tokens (flyer furniture) ────────────────────────────
_BOILER: frozenset[str] = frozenset([
    "certains", "certaines", "banner", "prix", "price", "prices", "plus",
    "taxes", "taxe", "moi", "points", "offre", "offres", "economisez",
    "save", "savings", "produit", "produits", "marque", "service",
    "carte", "cadeau", "achat", "fabrique", "au", "canada", "nous",
    "vous", "les", "des", "une", "aux", "tout", "tous", "ici", "fall",
    "automne", "saison", "nouveau", "nouvelle", "chez", "votre", "vos",
    "notre", "magasin", "succursales", "participantes", "selected",
    "types", "varieties", "reg",
])

_VOCAB: frozenset[str] = frozenset(rules._INDEX.keys())

# Short names that are flyer furniture, never products.
_FURNITURE_EXACT: frozenset[str] = frozenset(
    {"halal", "familial", "pts", "big", "sale", "special", "non nettoye",
     "non netoye", "liquide", "au canada", "toujours frais", "triangle rewards",
     "preparéau", "prepareau", "abriqué", "abrique", "wm clark"}
)

# Substrings searched inside long spaceless (OCR-merged) tokens.
_MERCH_SUBSTR: tuple[str, ...] = (
    "essuie", "nettoyant", "chandail", "oreiller", "poubelle", "matelas",
    "pantalon", "serviette", "lingette", "shampooing", "vitamine",
    "collagen", "pneu", "valise", "aspirateur",
)
_FOOD_SUBSTR: tuple[str, ...] = (
    "lait", "fromage", "cheddar", "poulet", "boeuf", "porc", "saumon",
    "salade", "fruit", "chocolat", "brioche", "beurre", "canneberge",
    "citrouille", "ravioli", "guacamole", "coco", "crevette", "dinde",
    "bouillon", "pommes", "fraise", "banane", "tomate", "oignon",
)

_DOSAGE_TOKENS: frozenset[str] = frozenset(
    {"capsules", "comprimes", "gelules", "softgels"}
)
_COFFEE_TOKENS: frozenset[str] = frozenset({"cafe", "coffee", "nespresso", "dolce"})


def _has_vocab(tokens: list[str]) -> bool:
    return any(t in _VOCAB for t in tokens)


def exclusion_reason(
    name_fr: str | None, name_en: str | None, brand: str | None
) -> str | None:
    """Return a reason string if the item is confidently non-grocery."""
    text = " ".join(t for t in (name_fr, name_en, brand) if t)
    norm = rules.normalize(text)
    tokens = norm.split()
    if not tokens:
        return "empty"
    joined = " " + norm + " "

    # E1 — merchandise phrases stand alone.
    for phrase in _MERCH:
        if f" {phrase} " in joined or norm == phrase:
            return f"merch:{phrase}"

    # E0 — furniture: banner-led names and exact short furniture names.
    if tokens and tokens[0] == "banner":
        return "furniture:banner"
    if norm in _FURNITURE_EXACT:
        return "furniture:exact"
    # Legal-footer phrases: a name carrying the flyer's terms-and-stock
    # boilerplate is the footer itself, never a product (Bonanza review,
    # 2026-10-17: the whole footer formed an item with a stolen price).
    if "epuisement des stocks" in norm or "while supplies last" in norm:
        return "furniture:footer"

    # E1b — supplement dosage forms (protect coffee capsules).
    token_set = set(tokens)
    if token_set & _DOSAGE_TOKENS and not token_set & _COFFEE_TOKENS:
        return "supplement-form"

    # E3b — spaceless merged tokens: merchandise substring, no food substring.
    for t in tokens:
        if (
            len(t) >= 14
            and " " not in t
            and any(s in t for s in _MERCH_SUBSTR)
            and not any(s in t for s in _FOOD_SUBSTR)
        ):
            return "garble:merch-merged"

    if _has_vocab(tokens):
        return None

    # E2 — boilerplate dominance, no food vocabulary at all.
    content = [t for t in tokens if len(t) >= 3 and not t.isdigit()]
    if content and sum(1 for t in content if t in _BOILER) / len(content) >= 0.6:
        return "boilerplate"

    # E3 — structural garble: symbol/digit heavy names with no vocab.
    alpha = sum(c.isalpha() for c in norm)
    if alpha and (len(norm) - alpha) / max(len(norm), 1) > 0.45 and len(tokens) <= 6:
        return "garble:symbols"
    return None
