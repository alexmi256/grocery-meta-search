# OCR page-image fixtures

The six per-store segmentation tests replay captured RapidOCR lines
(`*_lines.json`, committed) over the real flyer **page image**:

| Fixture | Test | Source edition (page) |
|---|---|---|
| `odessa_p2.jpg`, `odessa_p3.jpg`, `odessa_p7.jpg`, `odessa_p12.jpg` | `test_odessa_names.py` | Odessa Poissonnier, circulaires.club, *8–21 Oct 2026* (pp. 2, 3, 7, 12) |
| `costco_p3.jpg` | `test_costco_titles.py` | Costco, circulaires.club, *28 Sep–25 Oct 2026* (p. 3) |
| `monde_p2.webp` | `test_monde_name_cells.py` | Le Monde au Naturel, circulaires.club, *1–31 Oct 2026* (p. 2) |
| `palumbo_p1.jpg` | `test_palumbo_names.py` | Intermarché Palumbo, circulaires.club, *15–21 Oct 2026* (p. 1) |
| `frutta_p1.jpg` | `test_frutta_red_grid.py` | Frutta Si, circulaires.club, *15–21 Oct 2026* (p. 1) |
| `pa_nature_p1.jpg` | `test_pa_nature_chalkboard.py` | PA Nature (flyerbox), *12–25 Oct 2026* (p. 1) |

The images are **not committed** (repo rule: no flyer images in git),
so a fresh clone has none and the tests would error on a missing file.
Instead each test **skips** with a clear reason when its image, or a
toolchain piece it needs, is absent (`tests/ocr_fixtures.py`). Fetch
the images below to actually run them.

## Fetching the images

`circulaires.club` serves each edition's pages as
`/images/<edition-slug>/<NN>.webp` (full resolution), where the edition
slug is the path segment of its sitemap URL. For example:

```bash
curl -sL -o tests/fixtures/odessa_p2.jpg \
  https://circulaires.club/images/circulaire-odessa-poissonnier-du-8-au-21-octobre-2026/02.webp
```

The `.jpg` names are converted from the source webp (RGB, quality 92);
PIL reads either format. PA Nature's page is discovered at runtime from
the flyerbox listing (`sources/official.py: _flyerbox`); its page 1 is
the first signed `na.leafletscdn.com/thumbor/…/ca/data/75/144988/0.jpg`
URL, fetched with `curl` (the CDN rejects the stdlib HTTP client — see
`classify/store_report.py: _download`).

Exact production widths, which the captured line coordinates depend on:

| Fixture | Width × height (as fetched) |
|---|---|
| odessa p2/p3/p7/p12 | 993×1320, 1020×1320, 1020×1320, 1001×1280 |
| costco p3 | 1600×2441 |
| monde p2 | 1600×2186 |
| palumbo p1 | 1020×1305 |
| frutta p1 | 832×1849 |
| pa_nature p1 | 1550×1911 |

## Toolchain requirements

- **RapidOCR** — `red_grid` and `chalkboard` re-detect lines on crops.
  Provided by `rapidocr-onnxruntime` (see `requirements.txt`).
- **OpenCV (`cv2`)** — the colour-gated strategies (`name_cells`,
  `red_grid`, `chalkboard`, Palumbo's green-ink gate). Arrives with
  `rapidocr-onnxruntime`.
- **Tesseract 5 with the French traineddata (`fra`)** — the name
  re-OCR runs `-l fra+eng`; without `fra` it silently returns `None`
  and assembled names lose their accents. Install with
  `apt install tesseract-ocr-fra`, or point `TESSDATA_PREFIX` at a
  directory that holds `fra.traineddata`.

These tests therefore also depend on the installed Tesseract model;
a differently-provisioned machine can produce slightly different OCR
for the re-OCR steps (see the note in `test_palumbo_names.py`).
