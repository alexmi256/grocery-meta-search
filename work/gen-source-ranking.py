"""Generate docs/research/flyer-source-ranking.md: canonical flyer sources
ranked by coverage x ease, with a recommended build order and a per-store
single recommended source (one-source-per-store policy).
Re-run: python3 work/gen-source-ranking.py (after YAML changes)."""

import glob
import os
import re

import yaml

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORES_DIR = os.path.join(BASE, "docs", "research", "stores")
OUT = os.path.join(BASE, "docs", "research", "flyer-source-ranking.md")

# Ease overrides grounded in probe evidence / worker findings.
# (format, parse, fetch) as (points, rationale); validity/fr from data.
EASE = {
    # Verified by live probe 2026-10-12: structured JSON products, validity
    # dates at flyer+item level, locale=fr works (Maxi 326 / IGA 421 products).
    "flipp": (14, "VERIFIED json-api/high/http/FR/dated via live probe"),
    # Retailer-native structured API per research (needs key probe).
    "official:metro-azure": (12, "structured JSON API per research; key probe still needed"),
    "official:flyerify": (9.5, "structured flyer platform (html/images)"),
    "circulaires.club": (9.5, "dated image editions, plain HTTP, FR"),
    "circulaire-en-ligne.ca": (9, "html/images hubs; some entries are prose articles (variable)"),
    "rfd-flyers": (8, "listing page http-friendly; viewer JS; ?order=name is 402"),
    "official:shopify": (8, "one fetch pattern per platform; usually html/images"),
    "official:woocommerce": (8, "one fetch pattern per platform; usually html/images"),
    "official:wordpress": (7, "one fetch pattern per platform; often images/low"),
    "official:wix": (7, "one fetch pattern per platform; often images/low"),
    "flyerbox.ca": (8, "images, http, FR"),
    "flyerdeals.ca": (8, "html, http"),
    "flyerseek.com": (8, "html, http"),
    "flyerca.com": (8, "html, http"),
    "kimbino.ca": (7.5, "images, http, FR"),
    "speciauxquebec.com": (7, "images, http, FR, dated"),
    "circulairecanada.com": (6, "AI prose articles, no brand hubs — low value"),
    "flyers-on-line.com": (6, "images/low, http"),
    "ca-mydeals365.com": (6, "per-edition articles, no stable hub"),
    "kaufino.com": (6, "images, http; coverage unverified for QC"),
    "weeklyflyer.com": (6, "images, http"),
    "official:custom": (5, "heterogeneous one-offs — NOT one source; per-store last resort"),
    "quebectoutcompris.com": (5, "pdf, currently no active editions"),
    "shopping-canada.com": (5, "directory, thin flyer coverage"),
    "circulaires.ca": (4, "SAME OPERATOR as circulaires.com; SEO placeholders, no dated editions"),
    "circulaires.com": (4, "SAME OPERATOR as circulaires.ca; SEO placeholders, no dated editions"),
    "supermarches.ca": (3, "NOW A NEWS PORTAL (2026-10-12) — verify before building"),
    "official:instagram": (3, "manual/heavy fetch"),
    "official:email": (3, "manual"),
    "official:reebee": (6, "Reebee-powered HTML; reebee.com now redirects to flipp.com — verify"),
    "pdfflyers.com": (2, "DEAD for QC (redirects to US WeeklyAd.io)"),
    "weekly-flyer.ca": (2, "ABANDONED (previews stuck at April 2026)"),
    # Never recommend: official site is Akamai-blocked; use flipp instead.
    "official:loblaw": (1, "Akamai-BLOCKED — never build; use flipp for these stores"),
    # Official pages embedding the Flipp viewer — brand likely has a FlyerKit token.
    "official:flipp": (8, "embeds Flipp viewer; FlyerKit token likely exists — verify per brand"),
}

# Display overrides: probe/evidence-corrected cells for the ranked table
# (raw YAML aggregates describe the Flipp web viewer, not the verified API).
DISPLAY_OVERRIDE = {
    "flipp": {"fmt": "json-api", "fetch": "http", "fr": True, "dated": True},
}

METRO_GROUP = {"metro", "metro-plus", "super-c", "jean-coutu", "brunet"}
LOBLAW_GROUP = {"loblaws", "maxi", "provigo", "pharmaprix", "t-t", "l-intermarche"}
NEVER = {"official:loblaw", "pdfflyers.com", "weekly-flyer.ca"}


def load():
    recs = []
    for f in sorted(glob.glob(os.path.join(STORES_DIR, "*.yaml"))):
        if f.endswith("_template.yaml"):
            continue
        d = yaml.safe_load(open(f))
        if d.get("footprint") in {"island", "greater", "qc-confirmed"} and (
            d.get("flyers") or {}
        ).get("has_flyers"):
            recs.append(d)
    return recs


def sources_of(d):
    out = {}
    for t in (d.get("flyers") or {}).get("types") or []:
        for s in t.get("sources") or []:
            out.setdefault(s.get("name"), s)
    return out


def recommend(d, cov_sources):
    slug = d["slug"]
    srcs = sources_of(d)
    cands = [n for n in srcs if n not in NEVER]
    if slug in METRO_GROUP and "official:metro-azure" in srcs:
        return "official:metro-azure", "Metro-group native API (structured); probe key first"
    if slug == "adonis" and "flipp" in srcs:
        return "flipp", "aggregator path (no FlyerKit token for Metro group; Azure may also work)"
    if slug in LOBLAW_GROUP and "flipp" in srcs:
        return "flipp", "official:loblaw is Akamai-blocked; FlyerKit verified pattern"
    if "flipp" in cands:
        return "flipp", "verified structured JSON API"
    if not cands:
        return "—", "NO VIABLE SOURCE (only blocked/dead sources recorded) — re-check before Phase 3"
    # best remaining by ease
    best = max(cands, key=lambda n: EASE.get(n, (5, ""))[0])
    return best, EASE.get(best, (5, ""))[1]


def main():
    recs = load()
    cov = {}
    dated = {}
    fr = {}
    for d in recs:
        for t in (d.get("flyers") or {}).get("types") or []:
            for s in t.get("sources") or []:
                n = s.get("name")
                cov.setdefault(n, set()).add(d["slug"])
                if "fr" in (s.get("languages") or []):
                    fr[n] = True
                u = s.get("url") or ""
                if re.search(r"20\d\d|octobre|septembre|novembre|du-\d|au-\d", u, re.I):
                    dated[n] = True

    ranked = sorted(
        cov, key=lambda n: -(len(cov[n]) * EASE.get(n, (5, ""))[0])
    )

    L = []
    L.append("# Flyer source ranking — Phase 3")
    L.append("")
    L.append("Generated from `docs/research/stores/*.yaml` (67 Phase-3 stores).")
    L.append("Score = coverage × ease. Ease is evidence-weighted: the Flipp FlyerKit")
    L.append("probe (2026-10-12, verified live) and worker findings override raw YAML aggregates.")
    L.append("")
    L.append("## Aggregator identity corrections (2026-10-12)")
    L.append("")
    L.append("- **reebee → flipp**: reebee.com now redirects to flipp.com (acquisition complete).")
    L.append("- **circulaires.ca = circulaires.com**: same operator (redirects); SEO-placeholder")
    L.append("  pages with no dated editions — low value, recommend YAML cleanup merging them.")
    L.append("- **pdfflyers.com**: dead for QC (redirects to US WeeklyAd.io).")
    L.append("- **supermarches.ca**: now a news portal, no flyer directory — verify before building.")
    L.append("- **weekly-flyer.ca**: abandoned (previews stuck at April 2026).")
    L.append("")
    L.append("## Probe result (2026-10-12, live)")
    L.append("")
    L.append("Flipp FlyerKit (`dam.flippenterprise.net/flyerkit`) VERIFIED working for Maxi")
    L.append("(326 products) and IGA (421): structured JSON (name, price, image, SKU, bbox),")
    L.append("validity dates at flyer AND item level, `locale=fr` works. Per-brand static")
    L.append("access tokens published in github.com/jonathan-pearce/grocery_flyer.")
    L.append("**Metro group has no FlyerKit token** — Metro QC / Super C / Adonis / Jean Coutu /")
    L.append("Brunet are served by the separate Metro Digital Azure API (needs key probe).")
    L.append("Full notes: `work/flyerkit-probe.md`.")
    L.append("")
    L.append("## Ranked sources")
    L.append("")
    L.append("| Rank | Source | Stores | Formats (typical) | Fetch | FR | Dated | Ease | Score | Notes |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    for i, n in enumerate(ranked, 1):
        ease, why = EASE.get(n, (5, "unrated"))
        # typical format/fetch from data
        fmts, fts, frs = [], [], []
        for d in recs:
            for s in sources_of(d).values():
                pass
        # recompute simply
        from collections import Counter
        fc, pc, hc = Counter(), Counter(), Counter()
        for d in recs:
            for t in (d.get("flyers") or {}).get("types") or []:
                for s in t.get("sources") or []:
                    if s.get("name") == n:
                        if s.get("format"): fc[s["format"]] += 1
                        if s.get("parse_friendliness"): pc[s["parse_friendliness"]] += 1
                        if s.get("fetchability"): hc[s["fetchability"]] += 1
        fmt = fc.most_common(1)[0][0] if fc else "?"
        fet = hc.most_common(1)[0][0] if hc else "?"
        ov = DISPLAY_OVERRIDE.get(n, {})
        fmt = ov.get("fmt", fmt)
        fet = ov.get("fetch", fet)
        frv = "Y" if ov.get("fr", fr.get(n)) else "?"
        dav = "Y" if ov.get("dated", dated.get(n)) else "?"
        score = round(len(cov[n]) * ease, 1)
        slugs = ", ".join(sorted(cov[n]))
        L.append(
            f"| {i} | `{n}` | {len(cov[n])} | {fmt} | {fet} | "
            f"{frv} | {dav} | "
            f"{ease} | {score} | {why} |"
        )
        L.append(f"<!-- stores: {slugs} -->")
    L.append("")
    L.append("## Recommended build order")
    L.append("")
    L.append("1. **flipp (FlyerKit)** — ~20 stores. Verified structured JSON; no scraping")
    L.append("   step needed for 3b. Sample-first: maxi, iga, provigo.")
    L.append("2. **official:metro-azure** — 5 stores (metro, metro-plus, super-c,")
    L.append("   jean-coutu, brunet) + adonis candidate. Probe the API key first;")
    L.append("   structured JSON expected.")
    L.append("3. **circulaires.club** — 45 stores. Dated image editions over plain HTTP,")
    L.append("   FR. The long-tail workhorse (OCR path for 3b).")
    L.append("4. **Official platform groups** — one fetch pattern each: official:shopify (5),")
    L.append("   official:wordpress (5), official:wix (4), official:woocommerce (3),")
    L.append("   official:flyerify (1).")
    L.append("5. **Gap-fill aggregators** — rfd-flyers, circulaire-en-ligne.ca, flyerbox.ca,")
    L.append("   flyerdeals.ca, flyerseek.com, flyerca.com, kimbino.ca.")
    L.append("6. **official:custom one-offs** — per-store, last.")
    L.append("7. **Do not build**: official:loblaw (Akamai-blocked — use flipp),")
    L.append("   pdfflyers.com (dead), weekly-flyer.ca (abandoned), circulaires.ca/.com")
    L.append("   (SEO placeholders), supermarches.ca (verify — now a news portal).")
    L.append("")
    L.append("## Per-store recommended source (one source per store)")
    L.append("")
    L.append("| Store | Recommended source | Why |")
    L.append("|---|---|---|")
    for d in sorted(recs, key=lambda x: x.get("name", "").lower()):
        src, why = recommend(d, cov)
        L.append(f"| {d.get('name')} | `{src}` | {why} |")
    L.append("")

    with open(OUT, "w") as fh:
        fh.write("\n".join(L))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
