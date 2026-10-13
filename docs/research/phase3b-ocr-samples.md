# circulaires.club OCR samples & edge cases (2026-10-13)

Golden samples for the Phase 3b OCR pipeline. Line dumps (RapidOCR) live in
`tests/fixtures/cc_{store}_p1_lines.json`; page images were read visually to
establish ground truth. Tests: `tests/test_ocr_segment.py`.

## marche-bonichoix p1 (1600×3549) — classic weekly flyer

Ground truth (10 items): bavette de bœuf 15.99 $/lb; combo de saucisses
fraîches 6.49; tourtière/gratin/pâté 7.44; framboises 2/5.00 (2.50 ch.);
mélange de laitues Attitude 5.99; céréales General Mills 3.33; fromage
P'tit Québec 4.97; Coke ou Pepsi 12pk 6.99; mayonnaise Hellmann's 5.97;
bière 30pk 40.99.

Pipeline result: 10/10 items. Edge cases:

- **9→6 digit confusion**: beer cents read "66" (conf 0.98) → price stored
  40.66 instead of 40.99. Tesseract can't read the stylized price font
  either (crop test). Accepted limitation; Phase 4 quarantine candidate.
- **Multibuy pair**: "2/5⁰⁰" + "2⁵⁰ Ch./ea." are two anchors for one item;
  pipeline keeps per-unit 2.50 and records the multibuy in conditions.
- **"NET WT / POIDS NET" line on the salad photo** is closer to the price
  than the real name block → stack-aware seeding (multi-line blocks win).
- **"PRIX INCROYABLE" badge** overlaps the fromage/mayo name crops;
  Tesseract reads it first → token-overlap fallback to detected lines.
- Header date line and store logo must not become name blocks (height
  window + stoplist).

## t-t (T&T) p1 (1280×1629) — dense trilingual grid

Ground truth: ~25 items (melon hami 0.68¢; chou napa 1.48; filet saumon
bio 14.98; anguille grillée 8.88; ailes de poulet 2.99; côtes levées porc
5.99; TC ravioli 2/14.97 ou 7.97/ch; Watson magret 8.97; nouilles
Nong Shim 4.97; Dan-D Pak noix 13.97/18.97 dual; riz Golden Royal Ox
21.97; dumpling festival section with ~14 more).

Pipeline result: 16 items, most prices right; name assignment in the
dense grid is the weakest of the three samples (some swapped/junk names,
e.g. melon↔chou). Settings: `name_case=any`, `price_min_h_frac=0.016`,
`bare_int_is_cents=true`. Edge cases:

- **Cents-only price "68¢"**: the ¢ glyph is not detected as a line;
  a lone full-height 2-digit fragment is treated as cents (per-store cfg).
- **Lost dollar digit**: chou "1 48" → only "48" detected, at sub-normal
  height → anchor dropped by the median-height rule rather than emitting
  a wrong 0.48.
- **"9.99" read as "6.66"** (raviolis crevettes) — same 9/6 confusion.
- **Date badges** ("10/9-10/12") parse as multibuy fragments; they fold
  into neighbouring items' alt_prices instead of creating false items.
- Chinese name translations are filtered from name candidates (CJK ratio).

## costco p1 (1600×2829) — savings book (prix_line strategy)

Ground truth (10 priced items): téléviseur Samsung 65po 1511.74;
téléviseur Mini DEL 85po 1094.99; téléviseur Mini DEL 65po 744.99;
barre de son Samsung 252.74; chandail Sierra Design 19.99; téléphone
Samsung A37 449.19; haut-parleur MX-ST4CF 300.94; ordinateur Galaxy
Book6 999.99; moniteur Odyssey G5 208.49; plancher Sutton 24.99.
Two promo cells (Lennox, pneus Michelin) have no Prix line → skipped.

Pipeline result: 10/10. Edge cases:

- **The big green number is the SAVINGS, not the price** ("ÉCONOMISEZ
  500 $"). Prices come only from small "Prix X,XX $" lines.
- **Garbled Prix amount**: laptop "999,99 $" OCR'd as "$66666" → price
  derived from the same cell: En entrepôt 1 149,99 − Économie 150,00
  = 999,99 (flagged `price_derived`, confidence 0.7).
- "$" read as "S" ("1 149,99 S") — amount regex tolerates a missing $.
- Membership banner lines above the first row must not leak into names
  (stoplist: "pas encore membre", "inscrivez-vous").
