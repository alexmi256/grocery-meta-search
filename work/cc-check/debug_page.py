"""Debug one circulaires.club page: fragments, anchors, name cands, items.

Usage: debug_page.py <store-slug> <page-number> [config-json-overrides]
Uses the store's config from circulaires_club_config.json plus optional
overrides. Detected lines (on the upscaled image, as in production) are
cached in work/cc-check/<slug>-pN-up-lines.json.
"""

import io
import json
import sqlite3
import sys
from pathlib import Path

import requests
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from grocery_meta_search.ocr.engine import OcrLine, detect_lines, upscale_for_ocr  # noqa: E402
from grocery_meta_search.ocr.segment import (  # noqa: E402
    OcrStoreConfig,
    _is_digitish,
    _price_core,
    find_price_anchors,
    name_candidates,
    segment_page,
)
from grocery_meta_search.pipeline.fetch import _cc_ocr_config  # noqa: E402
from grocery_meta_search.sources.circulaires_club import CirculairesClubClient  # noqa: E402

WORK = Path(__file__).resolve().parent


def main() -> None:
    slug, page_no = sys.argv[1], int(sys.argv[2])
    overrides = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
    cache = WORK / f"{slug}-p{page_no}-up-lines.json"
    db = sqlite3.connect(str(ROOT / "data" / "grocery.db"))
    cfg_json = db.execute(
        "select api_config from flyer_sources where store_slug=? and name='circulaires.club' "
        "and api_config is not null limit 1",
        (slug,),
    ).fetchone()[0]
    cc_slugs = json.loads(cfg_json)["cc_slugs"]
    client = CirculairesClubClient()
    eds = client.fetch_current_editions(cc_slugs)
    edition = eds[0]
    url = edition.page_images[page_no - 1]
    print(f"edition {edition.edition_ref} page {page_no}: {url}")
    img = Image.open(io.BytesIO(requests.get(url, timeout=60).content)).convert("RGB")
    img = upscale_for_ocr(img)
    if cache.exists():
        data = json.loads(cache.read_text())
        lines = [OcrLine(**d) for d in data["lines"]]
    else:
        lines = detect_lines(img)
        cache.write_text(
            json.dumps(
                {
                    "w": img.width,
                    "h": img.height,
                    "lines": [
                        {"x": l.x, "y": l.y, "w": l.w, "h": l.h, "text": l.text, "conf": l.conf}
                        for l in lines
                    ],
                }
            )
        )
    print(f"page {img.width}x{img.height}, {len(lines)} lines")
    base = _cc_ocr_config(slug)
    cfg = OcrStoreConfig(**{**base.__dict__, **overrides})
    print(f"cfg: {cfg}")
    min_h = cfg.price_min_h_frac * img.height
    print(f"--- tall lines (h>={min_h:.0f}) digitish-core check ---")
    for ln in lines:
        if ln.h >= min_h and ln.conf >= 0.5:
            core = _price_core(ln.text)
            print(f"  h={ln.h:5.0f} x={ln.x:5.0f} y={ln.y:5.0f} digitish={_is_digitish(core)} core={core!r} raw={ln.text!r}")
    anchors = find_price_anchors(lines, img.width, img.height, cfg)
    print(f"--- anchors ({len(anchors)}) ---")
    for a in anchors:
        print(f"  {a.price_text} = {a.value} conf={a.conf:.2f} box={tuple(round(v) for v in a.box)}")
    cands = name_candidates(lines, img.height, cfg)
    print(f"--- name candidates ({len(cands)}) ---")
    for cn in cands[:40]:
        print(f"  h={cn.h:4.0f} y={cn.y:5.0f} x={cn.x:5.0f} {cn.text!r}")
    items = segment_page(img, lines, cfg, page_url=url, page_number=page_no)
    print(f"--- items ({len(items)}) ---")
    for it in items:
        print(f"  {it.price_value!s:>7}  {(it.name_fr or '')[:70]}")


if __name__ == "__main__":
    main()
