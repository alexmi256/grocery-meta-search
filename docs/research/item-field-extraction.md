# Item field extraction — per-store registry

Added 2026-10-16 with the `package_size` column. For every live
store: can its items carry a package size at all, and how are
**brand** and **size** distinguished for that store's source?

`package_size` is the size as printed for the product: a weight
("454 g", "2 lb", "18,14 LB"), a volume ("1.89 L", "750 ML"), a
multi-pack ("12X341/355 ML", "24x60 g") or a count ("3 PCS",
"14 SACHETS"). Qualitative formats ("format familial") are not
sizes. The pipeline fills the column at ingest
(`pipeline/fields.py`): from the parser's structured field when
the source provides one, else by extracting the printed size from
the item name. Names are never modified — the size text is copied,
not cut. Backfill/repair: `python -m
grocery_meta_search.pipeline.fields --db data/grocery.db`.

## How each source family distinguishes the fields

### Flipp (FlyerKit API + Flipp search API) — 25 stores
- **Brand:** structured field in the API payload, stored in
  `brand` for most stores (46–94% of items). Exceptions: the
  Metro-group banners (metro, metro-plus: 0%) and super-c (13%)
  serve short display names without a brand field.
- **Size:** not a structured field. FlyerKit long marketing names
  (maxi, provigo) print the size in the name — extracted at ingest
  (80–83% fill). Flipp-search short display names (metro,
  rachelle-bery, marche-ami, marche-richelieu...) print no size:
  0% — the size exists only on the retailer's product page, which
  is Phase 5 territory, not the flyer.

### circulaires.club (page images + OCR) — 24 stores
- **Brand:** not separable. OCR merges brand and product text
  into one name string; no reliable typographic split exists in
  these page images. `brand` stays empty.
- **Size:** extracted from the OCR'd name when the flyer prints
  one (0–39% by store; M&M Food Market and the AXEP banners print
  sizes in names, produce-heavy fruiteries price per lb instead).

### Official platforms (OCR kinds: wix, woocommerce, wordpress, custom, flyerify, flyerbox, circulaires.com)
- **Brand:** not separable (same OCR situation as CC), except
  where the platform is structured (woo_specials product feeds
  carry no brand either).
- **Size:** from the name when printed. Marché Korea is the
  outlier at 91%: its catalog-style names almost always end with
  the size ("285G", "100g"). C&T and Mayrand print per-lb prices
  and few package sizes (0%).

### Official PDF text layer (`pdf_text`) — akhavan
- **Brand:** distinguished typographically at parse time (brand
  is printed in red); stored in `brand` (54% of the store's items
  — the rest are the old OCR edition and no-brand butcher items).
- **Size:** distinguished typographically (small regular type);
  stored directly in `package_size` by the parser (61%).

## Measured fill rates (2026-10-16, after reprocessing)

| Store | Source | Items | Brand % | Size % |
|---|---|--:|--:|--:|
| 3-saisons-fruits-legumes | official:wix | 6 | 0 | 0 |
| adonis | flipp | 373 | 52 | 1 |
| akhavan | official:akhavan | 55 | 54 | 61 |
| aliments-merci | official:woocommerce | 29 | 0 | 3 |
| avril | flipp | 183 | 87 | 0 |
| brunet | flipp | 596 | 94 | 0 |
| bulk-barn | circulaires.club | 9 | 0 | 0 |
| canadian-tire | flipp | 799 | 63 | 5 |
| coop-alentour | circulaires.club | 33 | 0 | 6 |
| costco | circulaires.club | 85 | 0 | 5 |
| euro-marche | circulaires.club | 99 | 0 | 0 |
| familiprix | flipp | 968 | 91 | 38 |
| fruiterie-valmont | circulaires.club | 54 | 0 | 11 |
| frutta-si | circulaires.club | 27 | 0 | 7 |
| giant-tiger | flipp | 53 | 69 | 5 |
| h-marche | official:wix | 27 | 0 | 14 |
| iga | flipp | 827 | 78 | 2 |
| iga-express | flipp | 827 | 78 | 2 |
| iga-extra | flipp | 852 | 78 | 2 |
| intermarche-palumbo | circulaires.club | 8 | 0 | 12 |
| jean-coutu | flipp | 730 | 78 | 1 |
| kim-phat | flipp | 303 | 46 | 0 |
| l-intermarche | circulaires.club | 149 | 0 | 32 |
| la-moisson | circulaires.club | 58 | 0 | 10 |
| marche-ami | flipp | 167 | 67 | 0 |
| marche-andes | official:wordpress | 4 | 0 | 0 |
| marche-axep | circulaires.club | 151 | 0 | 33 |
| marche-bkr | aggregator:circulaires.com | 14 | 0 | 42 |
| marche-bonanza | circulaires.club | 30 | 0 | 0 |
| marche-bonichoix | circulaires.club | 144 | 0 | 4 |
| marche-c-t | official:custom | 92 | 0 | 0 |
| marche-esposito | circulaires.club | 84 | 0 | 2 |
| marche-fu-tai | circulaires.club | 83 | 0 | 2 |
| marche-korea | official:woocommerce | 273 | 0 | 91 |
| marche-lian-tai | flipp | 222 | 52 | 0 |
| marche-newon | circulaires.club | 180 | 0 | 5 |
| marche-pa | flipp | 194 | 54 | 1 |
| marche-richelieu | flipp | 214 | 61 | 0 |
| marche-sheng-tai | circulaires.club | 88 | 0 | 4 |
| marche-sultan | aggregator:circulaires.com | 29 | 0 | 0 |
| marches-tau | circulaires.club | 37 | 0 | 2 |
| marches-tradition | circulaires.club | 157 | 0 | 3 |
| maxi | flipp | 581 | 81 | 80 |
| mayrand | official:custom | 37 | 0 | 0 |
| metro | flipp | 840 | 0 | 0 |
| metro-plus | flipp | 840 | 0 | 0 |
| milano-fruiterie | official:wordpress | 15 | 0 | 0 |
| mm-food-market | circulaires.club | 133 | 0 | 39 |
| monde-au-naturel | circulaires.club | 70 | 0 | 0 |
| odessa-poissonnier | circulaires.club | 28 | 0 | 3 |
| pa-nature | aggregator:flyerbox | 3 | 0 | 0 |
| pharmaprix | flipp | 788 | 64 | 29 |
| provigo | flipp | 377 | 77 | 83 |
| rachelle-bery | flipp | 140 | 87 | 0 |
| shop-sante | circulaires.club | 32 | 0 | 9 |
| super-c | flipp | 501 | 13 | 0 |
| t-t | circulaires.club | 153 | 0 | 3 |
| uniprix | flipp | 279 | 85 | 5 |
| walmart | flipp | 785 | 76 | 8 |
| wholesale-club | official:flyerify | 181 | 0 | 20 |

Totals: 15,096 items; brand on 7,841 (52%); package_size on
2,161 (14%) after the 2026-10-16 reprocessing (32 from structured
payloads, 2,129 extracted from names).
