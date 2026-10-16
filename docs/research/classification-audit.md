# Classification audit — ground-truth review (2026-10-16)

Method: every distinct item signature in the DB (10,362 sigs covering
15,096 items; near-duplicate names collapsed) was read and judged by
hand against the PC Express taxonomy we adopted. Disagreements were
recorded with a pattern tag (`work/ground-truth/verdicts.json`, 3,869
entries). 63 sigs (97 items) are unjudgeable OCR merges/fragments and
are excluded from scoring. Verdict category names were normalized to
the exact `taxonomy.py` labels before scoring.

## (a) Current correctness

| Metric | Score |
|---|---|
| Items (weighted) | **66.3%** (9,945 / 14,999) |
| Signatures (unweighted) | **63.3%** (6,524 / 10,299) |
| Items the classifier did classify | 72.2% (9,335 / 12,936) |
| Items left Unclassified | 2,063 — only 610 (30%) are genuinely unclassifiable |

So roughly **1 in 3 items carries the wrong category**, and the
single biggest failure is not wrong answers but missing ones: 1,453
Unclassified items (70% of that bucket) are ordinary products the
rules never matched.

Worst categories by wrong items:

| Category | Wrong / total | Note |
|---|---|---|
| Unclassified | 1,453 / 2,063 | vocabulary gaps, see plan step 2 |
| Health & Beauty > Personal Care | 569 / 1,857 | OTC medicines belong in Pharmacy |
| Fruits & Vegetables > Fresh Vegetables | 323 / 952 | canned goods, snacks filed as fresh |
| Deli > Deli Meat | 225 / 421 | ~137 items are pasta (pâtes/pâté trap) |
| Fruits & Vegetables > Fresh Fruits | 162 / 668 | token traps (pomme, citron, miel) |
| Fish & Seafood > Fish | 155 / 279 | `bar` = sea bass vs snack bars; fish sauce |
| Health & Beauty > Pharmacy | 128 / 433 | vitamins/supplements belong in Vitamins |
| Frozen > Frozen Meals | 114 / 199 | pizzas, raw meat, dips filed as meals |
| Health & Beauty > Vitamins & Supplements | 68 / 68 | 100% wrong: OCR banner fragments |
| Pantry > Easy Meals & Sides | 74 / 106 | broth/bouillon belong with soups |

## (b) Mismatch patterns (by wrong items)

1. **dept — plain wrong department (3,110 items).** Systematic swaps:
   OTC medicines in Personal Care instead of Pharmacy (241 items);
   vitamins/probiotics/melatonin in Pharmacy instead of Vitamins
   (103); facial/body cleansers in Household Cleaning (63); olive oil
   in Canned & Pickled instead of Oils & Vinegar (41); broth in Easy
   Meals instead of Salads & Soups (50); canned tomatoes/beans in
   Fresh Vegetables (60); sliced deli meats in fresh Meat subcats.
2. **token-trap — homonyms and brand names (457).** `bar/barre`
   (sea bass vs snack bars), `lait` (chocolat au lait, breast pumps,
   Milk-Bone), `eau` (eau de toilette, melon d'eau), `pain` (soap
   bars, toasters, "pain relief"), `pâtes` vs `pâté` (~137 items),
   `cidre` vinegar, `scotch` tape, `doré` (bakery brand, golden kiwis),
   `pomme` (shower heads, deer apples, AirPods), `citron` (dish soap),
   `miel` (Honeycrisp), `sirop` (cough syrup), `levure` (Canesten),
   `lentilles` (contact-lens solution), `huile` (motor oil, lip oil),
   Old Spice brand bundles filed as spices.
3. **ethnic — vocabulary gaps (390).** Korean (tteok/topokki,
   gochujang, kimchi), Filipino (tocino, longanisa, banana ketchup),
   Middle Eastern and South Asian terms the rules don't know.
4. **frozen — frozen form missed (235).** Bagel Bites, breaded
   fish/chicken, dumplings, spring rolls, Eggo waffles filed as fresh;
   plus frozen-subcategory chaos (pizza and raw meat inside
   Frozen Meals).
5. **subcat — right department, wrong subcategory (230).**
6. **promo — non-products classified as products (198).** Loyalty
   banners, "Plus taxes", points offers, web-UI artifacts ("En savoir
   plus Button"), category header lines. Reverse case: real products
   dismissed into junk categories (Halloween candy in Home Goods).
7. **prepared (149)** — platters, poké, tartares, rotisserie items
   filed as raw ingredients.
8. **bundle (137)** — multi-product lines keyed on a later product
   instead of the first-named one.
9. **form (79)** — mixes and doughs filed as finished products
   (cake mix → Cakes, chocolate chips → Candy, Jell-O powder →
   Spreads).
10. **nonfood (49)** — appliances and hardware inside food
    categories (toasters, drills, log splitters, Halloween decor).

Taxonomy note: our adopted taxonomy has **no Soup subcat and no
Pasta & Noodles subcat** — ground truth therefore puts all soups in
Prepared Meals > Salads & Soups and all pasta in Pantry > Pasta &
Pasta Sauce. Adding subcats is a taxonomy decision for the owner,
not assumed here.

## (c) Plan to raise correctness (no changes made yet)

Ordered by expected item recovery. Every step is validated by
re-running classification and re-scoring against this ground truth;
a step ships only if the score improves without regressions
elsewhere.

1. **Junk/promo filter at ingest** (~200+ items, and it cleans the
   Vitamins category entirely): drop lines matching banner/UI/header
   patterns before classification; extend the OCR-fragment heuristics
   (ALL-CAPS fragments, punctuation-only, store-name-only lines).
2. **Unclassified vocabulary pass** (~1,000 of the 1,453 missed items):
   add the plain product words the review surfaced — crème/bologne/
   sauces/pomelo/dinde variants, plus a general-merchandise word list
   (tires, tools, furniture, appliances → Home Goods) so Walmart /
   Canadian Tire non-food stops sitting in Unclassified and is
   correctly discarded at ingest instead of kept.
3. **Health & Beauty rebalance** (~450 items): OTC vocabulary →
   Pharmacy; supplement vocabulary (vitamins, probiotics, melatonin,
   collagen, protein) → Vitamins & Supplements; facial/body
   "nettoyant" → Personal Care, not Cleaning & Laundry.
4. **pâtes/pâté disambiguation** (~137 items): accent-aware token
   split plus a pasta-form word list (spaghetti, penne, lasagne…)
   ordered before the pâté/deli rules.
5. **Homonym guards** (~450 items): negative-context tokens for the
   trap list in pattern 2 (e.g. `bar` + chocolate/granola context,
   `huile` + moteur/à lèvres context, brand blocklist for Old Spice
   in Spices).
6. **Frozen pass** (~235 items): widen frozen markers (surgelé/
   congelé variants, "keep frozen"), brand priors for frozen lines
   (McCain, Michelina's, Hungry-Man), and evict pizza/raw meat/dips
   from Frozen Meals into their frozen subcats.
7. **Form rules** (~300 items): mixes/doughs/baking chocolate →
   Baking Essentials; broth/bouillon → Salads & Soups; coffee
   creamer out of Coffee; mac & cheese dinners out of Cheese.
8. **Ethnic vocabulary packs** (~390 items): Korean, Filipino,
   Middle Eastern, South Asian term lists, in that order.
9. **First-product anchoring for bundles** (~137 items): prefer the
   rule whose match starts earliest in the name.
10. **Prepared/platter rules** (~170 items): plateau/tartare/poké/
    rotisserie patterns → Prepared Meals or Deli, not raw Meat/Fish.

Estimate if steps 1–10 land at the fix rate of the Akhavan round:
overall item accuracy 66% → **~88–92%**, classified-item accuracy
72% → **~93%**. The residual is OCR garble that no rule can save;
that belongs to per-store detection work, not classification.

Ground truth is frozen at `work/ground-truth/` (corpus + verdicts +
score) so every future rule change gets a regression number.

## Addendum — implementation results (2026-10-16, approved same day)

All 10 steps implemented (commits 8888d7e..final), plus two engine
changes: a junk gate (banner/header/UI lines return Unclassified
before rules or store priors apply) and position-bucket match
ranking (matches within the first two tokens win, then rule order —
the first-named product wins a bundle). Frozen markers are now
token-based, so "décongelé" (thawed) no longer remaps to Frozen.

| Metric | Before | After |
|---|---|---|
| Items correct (ground truth) | 66.3% | **81.5%** |
| Signatures correct | 63.3% | **79.0%** |
| DB Unclassified | 2,067 (13.7%) | 1,430 (9.5%) |
| DB classified coverage | 86.3% | 90.5% |

Below the ~88–92% estimate: the residual is dominated by one-item
tails (general merchandise and OTC brand names, ~185 + ~50 items),
genuinely ambiguous names (instant vs dry "nouilles", sliced vs
whole ham — indistinguishable from the name alone), and OCR garble.
Further gains need per-store detection work, not more rules.

The Vitamins & Supplements category went from 68/68 wrong (banner
fragments) to 177 real items. 296 DB items are now flagged `junk`.

Language split (FR/EN), tested as suggested: no measurable effect.
Only 245 of 15,096 items carry genuinely different French and
English names (most sources store the same display name in both
fields; Akhavan is the exception), and the three split variants
scored identically (80.7%) to the combined classifier on the ground
truth. The cross-language traps that did exist (EN "potato chips"
outvoting FR "croustilles") were fixed by specific phrases and the
position-bucket ranking instead. Not implemented.
