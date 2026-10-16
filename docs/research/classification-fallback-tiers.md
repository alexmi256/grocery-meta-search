# Classification fallback tiers + exclusion rules — experiment (2026-10-16)

Question from Alex: (1) were dedicated *exclusion* rules (positively
identifying non-grocery items) ever tried? (2) implement the proposed
fallback tiers as an experiment — tier 1 crop re-OCR, tier 2 local
embedding vote, tier 3 (AI vision) as a stub only.

## Short answers

1. **No.** What existed: non-grocery *departments* (Pet / Household /
   Health & Beauty / Baby Care) whose vocabularies were built to assign
   subcategories, not to maximize exclusion recall; a junk gate for
   promo/banner lines; and the ingest rule that discards items
   classified into those departments. Merchandise matching no rule at
   all landed in Unclassified and stayed in the review pool.
2. **Exclusion works and is worth adopting. Tiers 1 and 2 fail their
   sample tests.** Tier 3 remains a stub; its subset is accounted below.

Prototypes live in `work/tiers/` (gitignored): `exclusion.py`,
`tier1.py`, `tier2.py`, `tiers.py` (the chain), `tier3_subset.json`.

## The unclassified pool (ground-truth composition)

1,427 items (1,090 signatures) are Unclassified after the current
classifier. Judged composition:

| Ground truth | Items | Share |
|---|---|---|
| Unclassified (junk / furniture / fragments) | 725 | 51% |
| Grocery (vocabulary misses — must NOT exclude) | 431 | 30% |
| Non-grocery (excludable merchandise) | 271 | 19% |

## Exclusion prototype

Design: runs **only** on the unclassified pool; never overrides a
positive classification. Layers: merchandise phrase list (durables,
auto, sports, paper/household consumables ingest discards anyway,
hair-care phrasing, supplement dosage forms), flyer-furniture rules
(`banner`-led names, exact short furniture names like `halal`,
`triangle rewards`), boilerplate-dominance with a no-food-vocabulary
gate, and a spaceless-merged-token layer keyed on merchandise
substrings with a food-substring veto.

Iteration lesson: v1's naive "long spaceless token = garble" rule fired
on real groceries — Metro-style OCR merges product names exactly the
same way (`LaitdeCocoClassiqueBio`, `CheddarmarbreKirklandSignature`).
It was replaced by the substring layer in v2.

**Result (v2): 212 items excluded — 15% of the pool, 21% of the
excludable part — with 0 false fires on grocery ground truth (0/432).**
Furniture rules contributed most (109), then merchandise phrases (45),
boilerplate (42), merged-token and supplement layers (16). The
remaining excludable pool is one-off fragments and uniquely worded
durables; each further point costs more vocabulary at rising risk.

Effect: exclusion does not change classification accuracy. It shrinks
the pool that tiers 1–3 (and human review) must process, at zero
measured grocery cost. Adoption would mean: at ingest, unclassified
items matching an exclusion rule are recorded as excluded (with
reason) instead of entering the review subset — a pool-hygiene change,
to be approved before wiring in.

## Tier 1 — crop / product-image re-OCR

Method: 320 sampled weak DB items (160 Flipp product images, 160
bbox-cropped flyer cells), OCR with the project RapidOCR engine,
recovered text re-run through the text rules (alone and appended to
the name). Runtime ≈ 2 s/item (page downloads dominate).

On the 180 sampled items whose ground truth is a real category:

| Outcome | Share |
|---|---|
| Rescued (exact category) | 15% |
| Classified into a wrong category | 26% |
| Still unclassified | 52% |
| No OCR possible | 7% |

Crops beat direct images (20% vs 11% rescue) — the weak pool's Flipp
images are mostly promo clippings, and recovered text is dominated by
flyer boilerplate (`FORMAT ÉCONO`, coupon slogans), which also causes
the 26% wrong-category inventions (on junk items it invents categories
26% of the time too). Short names (≤3 tokens) rescue slightly better
(21%) but invent just as much (32%). **Verdict: fails as a standalone
tier; at best a corroborating vote, not worth its runtime as built.**

## Tier 2 — CLIP nearest-neighbour vote

Method: CLIP ViT-B/32 (ONNX, local CPU; 352 MB model) image embeddings;
reference set = 1,079 confidently rule-classified items' product
images (≤12/category, 99 categories); vote = similarity-weighted
majority of the 5 nearest reference images. Targets: the 304 tier-1
sample items with images.

| Mode | Real-GT items (168) | Junk-GT items (136) |
|---|---|---|
| Any vote: exact hit | 14 (8%) | — |
| Any vote: wrong / invented | 154 (92%) | 136 invented (100%) |
| High consensus (≥4/5 agree) | fires on 7: 2 hit, 5 wrong | fires on 13, all invented |
| Department-level (any vote) | 35 (21%) | — |

**Verdict: fails.** 112 fine-grained subcategories are too many for
image NN on flyer imagery (Frozen Meals vs Prepared Meals entrees are
visually identical), and the reference domain (clean Flipp product
shots) mismatches the target domain (flyer cells with prices and
banners). The model itself is cheap to run (~1,400 images embedded in
~5 min CPU) — accuracy, not cost, is the blocker.

## Tier 3 — stub and final accounting

Tier 3 (AI vision model) is a stub by decision: `tiers.py` chains
exclusion → tier1 hook → tier2 hook → tier3 stub; the tier 1/2 hooks
are pass-throughs because their prototypes failed validation, and
tier 3 returns nothing. Items reaching it stay Unclassified.

| Stage | Items remaining |
|---|---|
| Unclassified pool | 1,427 |
| After exclusion (−212) | 1,215 |
| Tier-3 subset (979 signatures) | **1,215** |

The subset is written to `work/tiers/tier3_subset.json`. Bottom line:
exclusion is the only validated win of this experiment (−15% pool,
zero grocery loss). The remaining pool is dominated by fragments,
foreign-language names, and OCR merges that neither re-OCR nor image
embeddings resolve — the realistic options for it remain (a) tier-3
AI vision at real per-item cost, or (b) accepting it as the standing
human-review subset.

## Addendum (2026-10-16, later)

Per Alex's decision, the tier 1 and tier 2 prototypes were removed
(code, image caches, OCR cache, and the 352 MB CLIP model deleted).
The fallback chain is now **exclusion → tier-3 stub** only
(`work/tiers/tiers.py` + `exclusion.py`); the tier-3 subset is
unchanged at 1,215 items / 979 signatures. Review documents resume
as the mechanism for inspecting results and guiding corrections.
