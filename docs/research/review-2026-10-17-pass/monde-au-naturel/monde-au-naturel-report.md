# Le Monde au Naturel — full product report

Store slug: `monde-au-naturel`. Generated from `data/grocery.db`. A sampled subset of 1 items stored for this store (random sample, see the review index), with all stored details and a locally downloaded picture (bbox crop from the flyer page; full pages under `pages/`).


## Review Analysis — Pass 1 (2026-10-17)

- **Flyers in this review:** 1 (flyer 78, valid 2026-10-01 → 2026-10-31 — a month-long catalogue).
- **Sample counts:** 1 classified + 0 unclassified — the edition holds exactly ONE item in total. That is the finding, and the page images explain it.
- **Issues found:** this catalogue prints no prices at all. Every product carries a "SPÉCIAL 15 %" leaf badge (page 6 shows nine products — keto puddings and plant-based jellies — all badged the same way); the offers are percentage discounts, not dollar prices. The single stored item is a badge artifact: it read the badge's "15" as a $15.00 price on a "KETO PUDDING". There is nothing else to capture — the earlier rounds' "badge fragments" at this store were the same phenomenon. The phantom item is deleted. Whether to list this store's products price-less (name-only records from a percentage-off catalogue) is a product decision — flagged for Alex; it is the real shape of the "tailored pass" question here, since there are no prices for a tailored detector to find.
- **Fixes applied this pass:** item 10546 deleted (percentage badge stored as a price). The flyer now holds zero items, which is the honest state for a price-less catalogue under the current model.


## Review Analysis — Pass 2 (2026-10-17, verification after Pass 1 fixes)

- The phantom item is deleted (flyer 78 now holds 0 items, verified in the DB); the sampler no longer produces items for this store, so this annotated Pass 1 report stands as the record (preserved identically in `monde-au-naturel-report-pass1.md`). Store review complete — the open decision (list the catalogue's products price-less, or leave the store empty) is Alex's.

## Flyer 78 — valid 2026-10-01 → 2026-10-31 (1 classified items, 0 unclassified)

Source ref: `circulaire-le-monde-au-naturel-alimentation-du-1-au-31-octobre-2026` · fetched 2026-10-13T18:17:49.251Z

### Item 10546

![item 10546](images/item-10546.jpg)

- **Name (English):** None
- **Name (French):** “KETO PUDDING POUDING CETO
- **Brand:** None
- **Category (English):** Dairy & Eggs > Desserts & Doughs
- **Category (French):** Produits laitiers et œufs > Desserts et pâtes
- **How classified:** rule (`dairy-desserts-doughs`)
- **Size:** None
- **Price:** 15.00
- **Printed Price:** “15”
- **Unit quantity:** 1.0
- **Unit measurement:** each
- **Item validity:** 2026-10-01 → 2026-10-31
- **bbox:** left 776, top 261, right 951, bottom 317, page 6
- **Full page:** [pages/flyer78-page6-430a5ec16d.jpg (flyer page 6)](pages/flyer78-page6-430a5ec16d.jpg)
- **Image source URL:** https://circulaires.club/images/circulaire-le-monde-au-naturel-alimentation-du-1-au-31-octobre-2026/06.webp
- **Details:** confidence: 0.99 · item_key: `525dd1354820b912`
- **Raw:** `{"block_text": "“KETO PUDDING\n POUDING CETO", "ocr_lines": ["KETO PUDDING", "POUDING CETO"]}`

**Item Review Analysis (Pass 1):** DELETED — not a priced product. The crop shows a Simply Delish keto pudding box under a "SPÉCIAL 15 %" badge; the stored 15.00 is the badge's percentage read as dollars. The catalogue prints no dollar prices (see the header), so no correct price exists to substitute.
