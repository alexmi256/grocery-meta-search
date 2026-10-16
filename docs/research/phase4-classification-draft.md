# DRAFT — Phase 4 classification: proposed category tree + kickoff plan

**Status: draft for user review. Nothing here is applied.** The proposal
below is derived from `product-categories.md` (81 stores, committed
`d48e528`) and verified against the live database (checked 2026-10-14).

## Why this shape

- The six majors (PC Express, Metro, Sobeys/IGA, Walmart, Costco, Giant
  Tiger) converge on the same ~12 department skeleton, plus two
  cross-cutting re-slices everyone maintains in parallel: international/
  world foods (by cuisine) and dietary/attribute (organic, plant-based,
  gluten-free, halal, kosher). → **One primary department + attribute
  tags** matches how the industry actually organizes this
  (observation 1).
- Cheese sits inside Dairy at PC Express/Metro and apart at IGA/Costco
  (observation 2). **Pick Dairy** — the PC Express/Metro convention, and
  two of our three biggest chains.
- Pantry is the universal deep node with near-identical subcategories
  across chains (observation 3) — the level-2 template below is lifted
  from it.
- Prepared food is first-class everywhere (observation 4); flyer items
  need it.
- Ethnic/world and dietary attributes are stored as **flags, not
  categories** (observations 5, 7) — Merci's "Pâtes Biologique / Pâtes en
  Vrac" variants are the long-tail proof.
- Flat, noisy source labels below the chains cannot be trusted as a
  taxonomy (observation 6) — mapping must tolerate dupes and POS-code
  noise.

## Proposed primary departments (FR | EN)

1. Fruits et légumes | Produce
2. Viande et volaille | Meat & Poultry
3. Poissons et fruits de mer | Seafood
4. Produits laitiers et œufs | Dairy & Eggs — incl. Fromage/Cheese
   (one home, per above)
5. Boulangerie | Bakery
6. Charcuterie et plats préparés | Deli & Prepared
7. Garde-manger | Pantry — level 2: Conserves et marinés; Essentiels de
   cuisson/pâtisserie; Pâtes, riz et grains; Condiments et sauces;
   Épices et assaisonnements; Huiles et vinaigres; Soupes et bouillons;
   Céréales et déjeuner; Miel, sirops et tartinades; Repas faciles et
   accompagnements
8. Grignotines et friandises | Snacks & Candy
9. Boissons | Beverages
10. Surgelés | Frozen
11. Bières et vins | Beer & Wine (QC grocery scope; SAQ stays its own thing)
12. Non alimentaire | Non-food — quarantine bucket for the Phase 3
   deferred "skip non-grocery items" step

## Proposed attribute tags (flags, not departments)

- Biologique / Organic; Végétalien / Vegan; Végétarien / Vegetarian;
  Sans gluten / Gluten-free; Halal; Casher / Kosher
- En vrac / Bulk; Format économique / Value pack;
  Prêt-à-manger / Ready-to-eat; Prêt-à-cuire / Ready-to-cook
- Cuisine: est-asiatique, sud-asiatique, moyen-orientale, latine,
  européenne, afro-caribéenne, philippine

## Warm start already in the data (verified 2026-10-14)

- **2,397 items** (the 6 FlyerKit-token stores — maxi 318, iga 452,
  provigo 216, walmart 494, iga-express 452, iga-extra 465) already
  carry Google product-taxonomy labels l3/l4 in their `raw` JSON
  (e.g. Food Items > Snack Foods; Fruits & Vegetables > Canned &
  Prepared Beans; Bakery > Donuts; Condiments & Sauces > Salad
  Dressing). `item_categories` is stored per item — nothing to re-fetch.
- **2,300 items** carry Flipp's own FR section labels (`categories`):
  Boulangerie, Garde-Manger, Fruits et légumes, Viandes, Fromagerie,
  Charcuterie et Plats Cuisinés, Congelés, Collations, Friandises,
  Boissons, Produits Laitiers et Oeufs — nearly our department names
  verbatim, plus ready-made **non-food flags** (Vêtements,
  Électroménagers, Beauté, Pharmacie-OTC, Jouets, HBA...).
- So group 1 of Phase 4 is a **mapping-table build**: (Flipp label,
  Google l3/l4) → our department + tags, validated on a sample — not a
  from-scratch classifier.

## Mapping-table quirks already spotted (verified 2026-10-14)

- **"Scene+" (327 items) leaks into Flipp `categories`** — the loyalty
  program name rides along as a category label on IGA items. Exclude it
  from the mapping table entirely (same failure class as the Phase 3
  loyalty-heuristic fix).
- **Three overlapping pantry labels**: Épicerie 502, Garde-Manger 160,
  Épicerie de base 74 — all one department (Garde-manger). Épicerie
  is also the single most common Flipp label overall.
- **Dupe/typo dairy labels**: "Produit laitiers" 132 (missing s) vs
  "Produits Laitiers et Oeufs" 67 — same department.
- **Walmart publishes EN labels**: Beverages 130, Deli / HMR 13,
  Alcohol 4 — the mapping table needs EN→FR handling, not just FR.
- **Manual-review pile**: "Dames saisonnier", "Remplacement de repas à
  domicile", "Deli / HMR", "Produits chimiques" — ambiguous or
  non-food-ish; quarantine, don't guess.
- **Google l3 core is tight**: Meat, Seafood & Eggs 310, Fruits &
  Vegetables 300, Dairy Products 148, Prepared Foods 127, Bakery 108,
  Condiments & Sauces 108, Snack Foods 107, Coffee 107, Beer 64, Frozen
  Desserts & Novelties 54, Grains, Rice & Cereal 51, Dips & Spreads 49,
  Cooking & Baking Ingredients 49, Candy & Chocolate 44. 147 distinct
  l4 labels total — the mapping table is bounded, not open-ended.
- **Non-food quarantine signal is strong on both sides**: Flipp —
  HBA 51, Animalerie 29, Santé et beauté 30, Beauté 12, Vêtements 6,
  Électroménagers 6, Pharmacie-OTC 5, Jouets 2; Google l3 — Cosmetics
  37, Cat Supplies 34, Baby & Toddler Food 28, Party Supplies 27,
  Fitness & Nutrition 37. These map straight to the Non alimentaire
  bucket with high confidence, no classifier needed.
- **Groups 2–3 have no category signal to map**: the 12 Flipp
  search-API stores keep only name/brand/price/text_areas in `raw`;
  the circulaires.club OCR stores keep only block_text/ocr_lines.
  Both are item-name matching, not table mapping — and strictly
  higher confidence thresholds.

## Proposed kickoff (sample-first, per standing rule)

1. Build the Flipp-label/Google-l3 mapping tables against the draft
   tree above.
2. Classify a sample of ~200 items from the 6 FlyerKit stores; user
   audits the sample (same vision-audit protocol as the OCR review).
3. Roll out group by group: Flipp search-API stores (name heuristics +
   the search endpoint's own categories where present), then OCR
   groups (item-name matching, stricter confidence).
4. Write to `flyer_items.category` + `confidence`; low-confidence and
   non-food land in the quarantine bucket, not the tree.

Current DB state: 11,506 items across 95 flyers, all `category =
'Unclassified'` (schema ready: `category`, `confidence`, `section`).
