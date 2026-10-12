"""Generate docs/research/stores.md summary table from per-store YAMLs."""
import glob
import os
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mdutil import md_link

STORES_DIR = "/home/hatch/workspace/grocery-meta-search/docs/research/stores"
OUT = "/home/hatch/workspace/grocery-meta-search/docs/research/stores.md"

TIER_NAMES = {1: "Tier 1 — major chains (full depth)", 2: "Tier 2 — banners / small chains (medium depth)", 3: "Tier 3 — independents (minimal)"}


def flyer_cell(d):
    f = d.get("flyers") or {}
    if not f.get("has_flyers"):
        return "N"
    fmts = []
    for t in f.get("types") or []:
        for s in t.get("sources") or []:
            fmt = s.get("format")
            if fmt and fmt not in fmts:
                fmts.append(fmt)
    return "Y (" + "/".join(fmts) + ")" if fmts else "Y"


def search_cell(d):
    s = d.get("product_search") or {}
    if not s.get("has_search"):
        return "N"
    kind = s.get("kind") or ""
    return f"Y ({kind})" if kind else "Y"


def loc_cell(d):
    loc = d.get("locations") or {}
    n = loc.get("count_estimate")
    mech = "API" if loc.get("locator_api") else ("locator" if loc.get("locator_url") else "?")
    return f"{n} ({mech})" if n is not None else f"({mech})"


def esc(s):
    return str(s).replace("|", "\\|")


recs = []
for path in sorted(glob.glob(f"{STORES_DIR}/*.yaml")):
    if path.endswith("_template.yaml"):
        continue
    d = yaml.safe_load(open(path))
    recs.append(d)

lines = [
    "# Stores — summary (Phase 2)",
    "",
    "Generated 2026-10-12 from `docs/research/stores/*.yaml` — the YAML files are the",
    "table of record; this is the human overview. Columns: flyer formats, product-search",
    "kind, location count + harvest mechanism (API = JSON endpoint observed).",
    "",
]
for tier in (1, 2, 3):
    batch = [d for d in recs if d.get("tier") == tier]
    lines.append(f"## {TIER_NAMES[tier]} ({len(batch)} stores)")
    lines.append("")
    lines.append("| Store | Type | Website | Flyers | Search | Locations | Parent |")
    lines.append("|---|---|---|---|---|---|---|")
    for d in batch:
        web = md_link((d.get("website") or {}).get("url"))
        lines.append(
            "| " + " | ".join([
                esc(d.get("name")),
                esc(d.get("store_type")),
                esc(web),
                esc(flyer_cell(d)),
                esc(search_cell(d)),
                esc(loc_cell(d)),
                esc(d.get("parent_company") or ""),
            ]) + " |"
        )
    lines.append("")

open(OUT, "w").write("\n".join(lines))
print(f"wrote {OUT} ({len(recs)} stores)")
