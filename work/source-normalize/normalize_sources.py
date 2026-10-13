#!/usr/bin/env python3
"""Source-name normalization for the 67 Phase-3 stores.

Renames every flyers.types[].sources[].name to a canonical form.
Round-trips YAML with ruamel to preserve formatting/comments.
Usage: normalize_sources.py [--apply]   (default = dry run)
"""
import glob, sys, re
from collections import Counter, defaultdict
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)  # match repo style: dash indented +2
yaml.width = 100000  # never wrap long scalars (repo files use long lines)

REPO = '/home/hatch/workspace/grocery-meta-search'
FOOTPRINTS = {'island', 'greater', 'qc-confirmed'}

# ---- aggregator renames: exact old name -> (canonical, extra note or None)
AGG = {
    'Flipp': ('flipp', None),
    'flipp': ('flipp', None),
    'RFD Montreal flyers page': ('rfd-flyers', None),
    'RFD Montreal flyers': ('rfd-flyers', None),
    'circulaires.club': ('circulaires.club', None),
    'circulairecanada.com': ('circulairecanada.com', None),
    'circulaire-en-ligne.ca': ('circulaire-en-ligne.ca', None),
    'flyerdeals.ca': ('flyerdeals.ca', None),
    'circulaires.ca': ('circulaires.ca', None),
    'flyerbox.ca': ('flyerbox.ca', None),
    'flyerca.com': ('flyerca.com', None),
    'flyerca': ('flyerca.com', None),
    'flyerseek.com': ('flyerseek.com', None),
    'circulaires.com': ('circulaires.com', None),
    'ca-mydeals365.com': ('ca-mydeals365.com', None),
    'quebectoutcompris.com': ('quebectoutcompris.com', None),
    'kimbino.ca': ('kimbino.ca', None),
    'shopping-canada.com': ('shopping-canada.com', None),
    'kaufino.com': ('kaufino.com', None),
    'pdfflyers.com': ('pdfflyers.com', None),
    'pdfflyers.com (stale)': ('pdfflyers.com', 'Marked stale in research (2026-10-12).'),
    'speciauxquebec.com': ('speciauxquebec.com', None),
    'supermarches.ca': ('supermarches.ca', None),
    'weekly-flyer.ca': ('weekly-flyer.ca', None),
    'weeklyflyer.com': ('weeklyflyer.com', None),
    'flyers-on-line.com (QC edition)': ('flyers-on-line.com', 'QC edition.'),
}

# ---- official-site platform per store slug (for any source whose name is an
# ---- official-site variant). Default when slug not listed: custom.
PLATFORM = {
    # loblaw family + Loblaw-asset builds
    'loblaws': 'loblaw', 'maxi': 'loblaw', 'provigo': 'loblaw',
    'pharmaprix': 'loblaw', 't-t': 'loblaw',
    'l-intermarche': 'loblaw',   # site is a Loblaw/Provigo creative-asset build (assetful.loblaw.ca)
    # metro-azure (Metro Inc. shared platform / Azure flyer infra)
    'metro': 'metro-azure', 'metro-plus': 'metro-azure', 'super-c': 'metro-azure',
    'jean-coutu': 'metro-azure', 'brunet': 'metro-azure',
    # shopify
    'giant-tiger': 'shopify', 'la-moisson': 'shopify', 'magasin-amira': 'shopify',
    'shop-sante': 'shopify', 'odessa-poissonnier': 'shopify',
    # wix
    'baia-dei-formaggi': 'wix', 'h-marche': 'wix', 'marche-newon': 'wix',
    '3-saisons-fruits-legumes': 'wix',
    # wordpress
    'marche-andes': 'wordpress', 'kim-phat': 'wordpress',
    'rachelle-bery': 'wordpress', 'milano-fruiterie': 'wordpress',
    'frutta-si': 'wordpress',
    # woocommerce
    'marche-fu-tai': 'woocommerce', 'marche-korea': 'woocommerce',
    'aliments-merci': 'woocommerce',
    # flyerify
    'wholesale-club': 'flyerify',
    # judgment calls: official page itself is powered by a third-party viewer
    'avril': 'reebee',            # official circulaire is Reebee-powered HTML
    'familiprix': 'flipp',        # official page embeds Flipp config/item API
    'uniprix': 'flipp',           # Flipp embed (flipp_flyer_view dataLayer events)
    'canadian-tire': 'flipp',     # official Flipp partner, Flipp-powered digital flyer
    'walmart': 'flipp',           # official Flipp partner
}

# extra context notes for official:custom stores
CUSTOM_NOTES = {
    'iga': 'Sobeys/IGA platform (iga.net/circulaire); no finer platform id.',
    'iga-express': 'Shared IGA flyer; Sobeys/IGA platform (iga.net).',
    'iga-extra': 'Sobeys/IGA platform (iga.net/circulaire); no finer platform id.',
    'voisin': 'Sobeys depanneur banner (mon-voisin.com); platform unverified.',
    'marche-bonichoix': 'Per-store Circulaire links; Metro-affiliated banner; platform unverified.',
    'marches-tradition': 'Per-store Circulaire links; Metro-affiliated banner; platform unverified.',
    'marche-axep': 'Loblaw-affiliated banner group; flyer platform unverified.',
    'marche-pa': 'New official site has no flyer section yet; platform unverified.',
    'marche-bonanza': 'Weekly circulaire published as homepage content; platform unverified.',
    'intermarche-palumbo': 'Homepage "Our Best Deals" structured HTML; platform unverified.',
    'pa-nature': 'Weekly "Nos speciaux" / "Les vedettes de la semaine" section on pa-nature.supermarchepa.com.',
    'costco': 'Proprietary costco.ca (MUI/React) Warehouse Savings section.',
    'adonis': 'Proprietary JS-driven viewer (groupeadonis.ca/circulaire).',
    'bulk-barn': 'Plain static HTML deals page.',
    'marche-ami': 'Banner-wide weekly flyer; platform unverified.',
    'marche-c-t': 'Per-store bilingual weekly circulaire; platform unverified.',
    'marche-sa-et-fils': 'Homepage Promotions section (product cards); platform unverified.',
    'marches-tau': 'Official "Circulaires" section; exact stack unverified.',
    'mayrand': 'Bilingual PDF flyer hosted on HubSpot CDN.',
    'premiere-moisson': 'Store-scoped circulaire (postal-code branch picker); platform unverified.',
    'euro-marche': 'Bare static PHP page; platform unverified.',
    'coop-alentour': 'Circulaire advertised on site; fetch path not captured; platform unverified.',
    'fruiterie-valmont': 'Per-location JPG circulaires at /circulaires/; platform unverified.',
}

STAMP = '2026-10-12'


def load_tolerant(f):
    """ruamel round-trip load; fall back to PyYAML on duplicate-key files
    (tolerates them like the original research tooling did)."""
    try:
        with open(f) as fh:
            return yaml.load(fh)
    except Exception:
        import yaml as pyyaml
        with open(f) as fh:
            return pyyaml.safe_load(fh)


def phase3_files():
    out = []
    for f in glob.glob(f'{REPO}/docs/research/stores/*.yaml'):
        if f.endswith('_template.yaml'):
            continue
        d = load_tolerant(f)
        if (d.get('footprint') in FOOTPRINTS
                and (d.get('flyers') or {}).get('has_flyers') is True):
            out.append((f, d))
    return sorted(out, key=lambda x: x[0])


# ---- canonical sets (for idempotency: already-canonical names pass through)
CANONICAL_AGG = set(v[0] for v in AGG.values())
CANONICAL_OFF_PLATFORMS = {'loblaw', 'flyerify', 'metro-azure', 'shopify', 'wix',
                            'woocommerce', 'wordpress', 'square', 'custom',
                            'instagram', 'email', 'reebee', 'flipp'}
CANONICAL = CANONICAL_AGG | {f'official:{p}' for p in CANONICAL_OFF_PLATFORMS}


def map_source(slug, name):
    """Return (canonical_name, [note fragments to append])."""
    if name in CANONICAL:
        return name, []  # already normalized (idempotent re-run)
    if name in AGG:
        return AGG[name][0], ([AGG[name][1]] if AGG[name][1] else [])
    if name == 'member email handout':
        return 'official:email', [f"Source renamed {STAMP}: 'member email handout'."]
    if name.startswith('Instagram @marcheakhavan'):
        return 'official:instagram', [f"Source renamed {STAMP}: '{name}'."]
    if name.startswith('official') or name.startswith('flyerify'):
        plat = PLATFORM.get(slug, 'custom')
        notes = []
        if name != 'official site':
            notes.append(f"Source renamed {STAMP}: '{name}'.")
        if plat == 'custom':
            extra = CUSTOM_NOTES.get(slug, 'Platform unverified.')
            notes.append(f"official:custom ({extra})")
        elif slug in ('avril', 'familiprix', 'uniprix', 'canadian-tire', 'walmart',
                      'l-intermarche', 't-t'):
            notes.append(f"Platform call {STAMP}: see normalization report for evidence.")
        return f'official:{plat}', notes
    raise ValueError(f'UNMAPPED source name: {name!r} (store {slug})')


def append_note(src, fragments):
    frags = [f for f in fragments if f]
    if not frags:
        return
    cur = (src.get('notes') or '').strip()
    add = ' '.join(frags)
    src['notes'] = f'{cur} {add}'.strip() if cur else add


def merge_sources(group):
    """Merge >1 sources sharing a canonical name within one flyer type."""
    base = group[0]
    for other in group[1:]:
        ourl = (other.get('url') or '').strip()
        burl = (base.get('url') or '').strip()
        if ourl and ourl != burl:
            append_note(base, [f'Merged duplicate source (same canonical name); alternate URL: {ourl}.'])
        onotes = (other.get('notes') or '').strip()
        if onotes:
            append_note(base, [f'Merged note: {onotes}'])
        for field in ('kind', 'format', 'parse_friendliness', 'fetchability'):
            if not (base.get(field) or '').strip() and (other.get(field) or '').strip():
                base[field] = other[field]
        langs = list(base.get('languages') or []) + [l for l in (other.get('languages') or [])
                                                     if l not in (base.get('languages') or [])]
        if langs:
            base['languages'] = langs
    return base


def process(files, apply):
    changes = []
    merges = []
    canon_counts = defaultdict(set)   # canonical -> set of slugs
    for path, d in files:
        slug = d.get('slug')
        dirty = False
        for t in (d.get('flyers') or {}).get('types') or []:
            srcs = t.get('sources') or []
            # rename
            for s in srcs:
                old = s.get('name')
                new, note_frags = map_source(slug, old)
                if new != old:
                    changes.append((slug, t.get('type'), old, new))
                    s['name'] = new
                    append_note(s, note_frags)
                    dirty = True
                elif note_frags:
                    append_note(s, note_frags)
                    dirty = True
            # dedupe by canonical name within this type
            seen = {}
            order = []
            for s in srcs:
                n = s.get('name')
                if n not in seen:
                    seen[n] = [s]
                    order.append(n)
                else:
                    seen[n].append(s)
            new_srcs = []
            for n in order:
                g = seen[n]
                if len(g) > 1:
                    merges.append((slug, t.get('type'), n, len(g)))
                    new_srcs.append(merge_sources(g))
                    dirty = True
                else:
                    new_srcs.append(g[0])
            t['sources'] = new_srcs
            for n in order:
                canon_counts[n].add(slug)
        if dirty and apply:
            with open(path, 'w') as fh:
                yaml.dump(d, fh)
    return changes, merges, canon_counts


def main():
    apply = '--apply' in sys.argv
    files = phase3_files()
    print(f'Phase-3 stores: {len(files)}')
    changes, merges, counts = process(files, apply)
    print(f'{"APPLIED" if apply else "DRY RUN"}: {len(changes)} renames, {len(merges)} merges')
    for slug, typ, old, new in changes:
        print(f'  RENAME [{slug}/{typ}] {old!r} -> {new!r}')
    for slug, typ, name, k in merges:
        print(f'  MERGE  [{slug}/{typ}] {k}x -> {name!r}')
    print('\nCanonical source -> store count:')
    for name in sorted(counts):
        print(f'  {len(counts[name]):3d}  {name}')


if __name__ == '__main__':
    main()
