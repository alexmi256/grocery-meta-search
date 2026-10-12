"""Generate docs/research/stores-by-capability.md: stores grouped into four
flyer x product-search tables. The per-store YAMLs are the source of truth.
Re-run after YAML changes: python3 work/gen-stores-by-capability.py"""

import glob
import os
import re

import yaml

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORES_DIR = os.path.join(BASE, "docs", "research", "stores")
OUT = os.path.join(BASE, "docs", "research", "stores-by-capability.md")


def short_url(url: str) -> str:
    url = (url or "").strip()
    url = re.sub(r"^https?://", "", url)
    return url.rstrip("/")


def cadence_label(days) -> str:
    if days == 7:
        return "weekly"
    if days == 14:
        return "biweekly"
    if isinstance(days, int) and days >= 28:
        return "monthly"
    if days:
        return f"{days}d"
    return "?"


def flyer_info(d: dict):
    f = d.get("flyers") or {}
    if not f.get("has_flyers"):
        return None
    fmts, cads = [], []
    for t in f.get("types") or []:
        for s in t.get("sources") or []:
            fmt = s.get("format")
            if fmt and fmt not in fmts:
                fmts.append(fmt)
        c = cadence_label(t.get("duration_days"))
        if c not in cads:
            cads.append(c)
    return {"formats": fmts, "cadence": cads}


def search_info(d: dict):
    p = d.get("product_search") or {}
    if not p.get("has_search"):
        return None
    return p.get("kind") or "yes"


def locations(d: dict) -> str:
    loc = d.get("locations") or {}
    n = loc.get("count_estimate")
    return str(n) if n else "?"


def excluded(d: dict) -> bool:
    return "RECOMMENDED-EXCLUDED" in (d.get("notes") or "")


def main() -> None:
    groups = {"both": [], "flyer": [], "search": [], "neither": []}
    for path in sorted(glob.glob(os.path.join(STORES_DIR, "*.yaml"))):
        if os.path.basename(path) == "_template.yaml":
            continue
        d = yaml.safe_load(open(path))
        name = d.get("name", d.get("slug", "?"))
        if excluded(d):
            name += " *"
        row = {
            "name": name,
            "type": d.get("store_type", "?"),
            "website": short_url((d.get("website") or {}).get("url", "")),
            "locations": locations(d),
            "flyer": flyer_info(d),
            "search": search_info(d),
        }
        if row["flyer"] and row["search"]:
            groups["both"].append(row)
        elif row["flyer"]:
            groups["flyer"].append(row)
        elif row["search"]:
            groups["search"].append(row)
        else:
            groups["neither"].append(row)

    for rows in groups.values():
        rows.sort(key=lambda r: r["name"].lower())

    def flyer_cell(r):
        f = r["flyer"]
        return f"{', '.join(f['formats'])} ({', '.join(f['cadence'])})"

    L = []
    L.append("# Stores by capability — flyer x product search")
    L.append("")
    L.append("Generated from `docs/research/stores/*.yaml` (the source of truth).")
    L.append("Chain vs independent is deliberately not a grouping dimension.")
    L.append("")
    total = sum(len(v) for v in groups.values())
    L.append(
        f"**{total} stores:** {len(groups['both'])} both · "
        f"{len(groups['flyer'])} flyer only · {len(groups['search'])} search only · "
        f"{len(groups['neither'])} neither."
    )
    L.append("")
    L.append("\\* flagged as exclusion candidate (recommended-excluded, pending approval).")
    L.append("")

    L.append(f"## Both — weekly flyer and product search ({len(groups['both'])})")
    L.append("")
    L.append("| Store | Type | Website | Flyer | Search | Locations |")
    L.append("|---|---|---|---|---|---|")
    for r in groups["both"]:
        L.append(f"| {r['name']} | {r['type']} | {r['website']} | {flyer_cell(r)} | {r['search']} | {r['locations']} |")
    L.append("")

    L.append(f"## Flyer only ({len(groups['flyer'])})")
    L.append("")
    L.append("| Store | Type | Website | Flyer | Locations |")
    L.append("|---|---|---|---|---|")
    for r in groups["flyer"]:
        L.append(f"| {r['name']} | {r['type']} | {r['website']} | {flyer_cell(r)} | {r['locations']} |")
    L.append("")

    L.append(f"## Product search only ({len(groups['search'])})")
    L.append("")
    L.append("| Store | Type | Website | Search | Locations |")
    L.append("|---|---|---|---|---|")
    for r in groups["search"]:
        L.append(f"| {r['name']} | {r['type']} | {r['website']} | {r['search']} | {r['locations']} |")
    L.append("")

    L.append(f"## Neither flyer nor product search ({len(groups['neither'])})")
    L.append("")
    L.append("| Store | Type | Website | Locations |")
    L.append("|---|---|---|---|")
    for r in groups["neither"]:
        L.append(f"| {r['name']} | {r['type']} | {r['website']} | {r['locations']} |")
    L.append("")

    with open(OUT, "w") as fh:
        fh.write("\n".join(L))
    print(f"wrote {OUT}: " + ", ".join(f"{k}={len(v)}" for k, v in groups.items()))


if __name__ == "__main__":
    main()
