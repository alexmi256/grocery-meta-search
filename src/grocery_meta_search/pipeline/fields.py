"""Package-size extraction from item names.

Many sources print the package size inside the product name
("FRAISES 340G", "JUS D'ORANGE 1.89L", "ŒUFS 12 UNITÉS") instead of
a structured field. extract_package_size finds that printed size so
it can live in flyer_items.package_size. Names are never modified —
the size text is copied, not cut (item keys and classification
inputs stay stable).

Per-store expectations (which stores can carry a size at all, and
how brand/size are distinguished per source) are documented in
docs/research/item-field-extraction.md.
"""

from __future__ import annotations

import re

# A quantity: "1.89", "340", "1/2", optionally with a multiplier
# prefix "6 x" / "24x" and a range prefix ("100-154 g", "125 à 200 g").
# A unit: weight, volume, length or count. "gr" is the Quebec flyer
# abbreviation for grams; count words cover pharmacy pack counts
# ("90 capsules", "24 un.", "40 comprimés") that carry no weight.
_QTY = r"\d+(?:[.,]\d+)?(?:\s*/\s*\d+)?"
_RANGE = rf"(?:{_QTY}\s*(?:[-–]|à|to)\s*)?"
_WV_UNIT = (
    r"(?:kg|mg|ml|cl|oz|lb|lbs|gr|g|l|grammes?|grams?|kilogrammes?|litres?|cm|mm|po)"
)
_COUNT_UNIT = (
    r"(?:unit[ée]s?|units?|un\.|pi[èe]ces?|pcs|sachets?|douzaine|"
    r"capsules?|comprim[ée]s?|g[ée]lules?|caplets?|tablets?)"
)
_UNIT = rf"(?:{_WV_UNIT}|{_COUNT_UNIT})"
_MULT = r"(?:\d+\s*[x×]\s*)?"
# The trailing guard is a letter lookahead, not \b: the "un."
# abbreviation ends in a dot, after which \b never matches.
_SIZE_RE = re.compile(
    rf"(?P<full>{_MULT}{_RANGE}{_QTY}\s*{_UNIT}(?![\w])"
    rf"(?:\s*/\s*{_QTY}\s*{_UNIT}(?![\w]))?)",
    re.IGNORECASE,
)
_WV_RE = re.compile(rf"(?:{_WV_UNIT})\b", re.IGNORECASE)
_BUNDLE_SEP_RE = re.compile(r"\s(?:ou|or)\s|\||\+")
# A bare count trailing a food noun ("ŒUFS 12", "BAGELS 6") is a
# package count, but bare numbers are too ambiguous to trust alone;
# only the unit-bearing forms above are extracted.

# --- Candidate guards (2026-10-16 round-2 visual review) -----------
# PC-banner OCR names append the retailer's SKU directly before the
# unit ("FILET 20058163 KG", "20821339KG"): any all-digit token of 6+
# digits inside a candidate is a SKU, not a package quantity.
_SKU_MIN_DIGITS = 6
# Protein callouts print "14G DE PROTÉINES PAR PORTION" / "10G
# PROTEIN": a size figure glued to a protein word (either side, with
# only de/of/par between) is a per-portion nutrition claim, not the
# package size (IGA skewers "23g" skewers, La Moisson seitan "14g").
_PROTEIN_AFTER_RE = re.compile(
    r"^\s*(?:de\s+|of\s+|par\s+|per\s+)?prot(?:[ée]ines?|eins?)\b", re.IGNORECASE
)
_PROTEIN_BEFORE_RE = re.compile(
    r"prot(?:[ée]ines?|eins?)\s*(?:de\s+|of\s+)?$", re.IGNORECASE
)
# Quantity plausibility caps per unit: no grocery package exceeds
# these (harvest once stored juice sizes of "154 L"/"458l" stitched
# from "1,54 L"). The litre cap stays high because hardware flyers
# print real bin/cooler capacities up to ~110 L; the grocery-only
# harvest stage applies a stricter litre bound of its own.
_QTY_CAPS = {
    "l": 120.0, "ml": 30000.0, "cl": 3000.0,
    "kg": 100.0, "g": 40000.0, "gr": 40000.0,
    "oz": 500.0, "lb": 250.0, "lbs": 250.0,
    "cm": 300.0, "mm": 3000.0, "po": 120.0,
}
_PAIR_RE = re.compile(
    r"(\d+(?:[.,]\d+)?)\s*(kg|ml|cl|oz|lbs?|gr|g|l|cm|mm|po)\b", re.IGNORECASE
)


def _protein_callout(text: str, start: int, end: int) -> bool:
    """True when the match at [start, end) is glued to a protein word."""
    if _PROTEIN_AFTER_RE.match(text[end : end + 30]):
        return True
    return bool(_PROTEIN_BEFORE_RE.search(text[max(0, start - 20) : start]))


def _implausible(full: str) -> bool:
    for qty, unit in _PAIR_RE.findall(full):
        cap = _QTY_CAPS.get(unit.lower())
        if cap is not None and float(qty.replace(",", ".")) > cap:
            return True
    return False


def size_value_is_valid(value: str) -> bool:
    """Value-level guards (SKU digits, quantity caps) on a stored size.

    Protein context needs the surrounding text, so it is not checked
    here — see _iter_valid_sizes.
    """
    if any(len(tok) >= _SKU_MIN_DIGITS for tok in re.findall(r"\d+", value)):
        return False
    return not _implausible(value)


def _iter_valid_sizes(text: str) -> list[re.Match[str]]:
    """_SIZE_RE matches that survive the round-2 guards."""
    out = []
    for m in _SIZE_RE.finditer(text):
        full = m.group("full")
        if not size_value_is_valid(full):
            continue
        # Protein callouts are weight claims; a count beside a protein
        # product line ("GAUFRES PROTÉINES 8 UN.") is a real pack count.
        if _WV_RE.search(full) and _protein_callout(text, m.start("full"), m.end("full")):
            continue
        out.append(m)
    return out


def _stored_size_rejected(
    stored: str, *texts: str | None
) -> bool:
    """True when a stored size should be cleared under current policy:
    it fails the value-level guards outright, or it appears among the
    raw candidates of the item's own texts but the guarded iterator
    rejects it there (e.g. a protein callout). Harvest-filled values
    do not appear in the names, so they are left to the harvest
    stage's own provenance."""
    if not size_value_is_valid(stored):
        return True
    norm = re.sub(r"\s+", " ", stored).strip(" ,.-").lower()
    for text in texts:
        if not text:
            continue
        raw = {
            re.sub(r"\s+", " ", m.group("full")).strip(" ,.-").lower()
            for m in _SIZE_RE.finditer(text)
        }
        if norm in raw:
            valid = {
                re.sub(r"\s+", " ", m.group("full")).strip(" ,.-").lower()
                for m in _iter_valid_sizes(text)
            }
            return norm not in valid
    return False


def reprocess(db_path: str, dry_run: bool = False) -> dict[str, dict[str, int]]:
    """Fill flyer_items.package_size for existing items: first
    from a structured raw payload (pdf_text items), then by
    extracting the printed size from the item's names. Also fills
    flyer_items.price_unit from the raw Flipp post_price_text
    ("/lb 4,39$/kg") for items whose unit was never parsed.
    Sizes that came from name/block extraction (no structured raw
    size) are recomputed under the current extraction policy, so a
    policy change corrects values it previously got wrong (bundle
    first-product rule, range capture); structured sizes are never
    overwritten. Idempotent; returns per-store counters."""
    import json

    from ..db import connect, init_schema
    from ..prices import parse_price_text

    conn = connect(db_path)
    init_schema(conn)
    stats: dict[str, dict[str, int]] = {}
    rows = conn.execute(
        "SELECT id, store_slug, name_fr, name_en, raw, package_size, price_unit"
        " FROM flyer_items"
    ).fetchall()
    for row in rows:
        st = stats.setdefault(
            row["store_slug"],
            {"total": 0, "set": 0, "from_raw": 0, "from_name": 0,
             "from_block": 0, "corrected": 0, "unit_set": 0},
        )
        st["total"] += 1
        if row["price_unit"]:
            st["unit_set"] += 1
        elif row["raw"]:
            try:
                data = json.loads(row["raw"])
            except Exception:
                data = None
            if isinstance(data, dict) and data.get("post_price_text"):
                _, unit = parse_price_text(str(data["post_price_text"]))
                if unit:
                    st["unit_set"] += 1
                    if not dry_run:
                        conn.execute(
                            "UPDATE flyer_items SET price_unit=? WHERE id=?",
                            (unit, row["id"]),
                        )
        raw_data: dict[str, object] | None = None
        if row["raw"]:
            try:
                parsed = json.loads(row["raw"])
            except Exception:
                parsed = None
            if isinstance(parsed, dict):
                raw_data = parsed
        if row["package_size"]:
            st["set"] += 1
            if not (raw_data and raw_data.get("size")):
                # Name/block-derived size: recompute under the current
                # policy and correct the stored value when it changes.
                new_size = extract_package_size(row["name_fr"], row["name_en"])
                if new_size is None and raw_data and raw_data.get("block_text"):
                    new_size = extract_package_size(str(raw_data["block_text"]))
                if new_size and new_size != row["package_size"]:
                    st["corrected"] += 1
                    if not dry_run:
                        conn.execute(
                            "UPDATE flyer_items SET package_size=? WHERE id=?",
                            (new_size, row["id"]),
                        )
                elif new_size is None and _stored_size_rejected(
                    row["package_size"], row["name_fr"], row["name_en"],
                    str(raw_data["block_text"])
                    if raw_data and raw_data.get("block_text")
                    else None,
                ):
                    # The stored value is a candidate the current
                    # guards actively reject (SKU digits, protein
                    # callout, implausible quantity) and no valid
                    # alternative exists: clear it rather than keep
                    # a value the policy now disowns. A harvest
                    # provenance pointing at the cleared value goes
                    # with it.
                    st["corrected"] += 1
                    if not dry_run:
                        hv_raw = raw_data.get("harvest") if raw_data else None
                        if (
                            raw_data is not None
                            and isinstance(hv_raw, dict)
                            and hv_raw.get("size") == row["package_size"]
                        ):
                            hv = dict(hv_raw)
                            del hv["size"]
                            raw_data["harvest"] = hv
                            conn.execute(
                                "UPDATE flyer_items SET package_size=NULL, raw=?"
                                " WHERE id=?",
                                (json.dumps(raw_data, ensure_ascii=False), row["id"]),
                            )
                        else:
                            conn.execute(
                                "UPDATE flyer_items SET package_size=NULL WHERE id=?",
                                (row["id"],),
                            )
            continue
        size: str | None = None
        origin = ""
        if raw_data and raw_data.get("size"):
            size, origin = str(raw_data["size"]), "from_raw"
        if size is None:
            size = extract_package_size(row["name_fr"], row["name_en"])
            origin = "from_name" if size else ""
        if size is None and raw_data and raw_data.get("block_text"):
            # OCR items: the Tesseract name-block text can retain a size
            # line the assembled name dropped.
            size = extract_package_size(str(raw_data["block_text"]))
            origin = "from_block" if size else ""
        if size:
            st[origin] += 1
            st["set"] += 1
            if not dry_run:
                conn.execute(
                    "UPDATE flyer_items SET package_size=? WHERE id=?",
                    (size, row["id"]),
                )
    if not dry_run:
        conn.commit()
    conn.close()
    return stats


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--db", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    stats = reprocess(args.db, args.dry_run)
    total = {"total": 0, "set": 0, "from_raw": 0, "from_name": 0,
             "from_block": 0, "corrected": 0}
    for slug in sorted(stats):
        st = stats[slug]
        for k in total:
            total[k] += st[k]
        print(
            f"{slug:28} {st['set']:5}/{st['total']:<5} "
            f"(raw {st['from_raw']}, name {st['from_name']}, block {st['from_block']}, "
            f"corrected {st['corrected']})"
        )
    print(
        f"{'TOTAL':28} {total['set']:5}/{total['total']:<5} "
        f"(raw {total['from_raw']}, name {total['from_name']}, block {total['from_block']}, "
        f"corrected {total['corrected']})"
        + ("  [dry run]" if args.dry_run else "")
    )



def find_package_sizes(text: str | None) -> list[str]:
    """All printed-size matches in a text, whitespace-normalized.

    Used by the page-harvest stage (pipeline/harvest.py), which applies
    its own ambiguity policy over the full match set of an item's cell
    instead of the single-name selection in extract_package_size.
    """
    if not text:
        return []
    return [
        re.sub(r"\s+", " ", m.group("full")).strip(" ,.-")
        for m in _iter_valid_sizes(text)
    ]


def extract_package_size(*names: str | None) -> str | None:
    """Return the printed package size found in a name, or None.

    Selection among several candidates (2026-10-16 visual review):
    weight/volume matches beat count-only matches ("CREVETTES 60-70
    UNITÉS 907 g" is a 907 g pack); within a class, the LAST match
    wins for single-product names (sizes print at the end: "RIZ
    BASMATI 2 lb"), but when the name bundles several products
    ("... (800 g) ou ... (907 g)") the FIRST product's size wins —
    the item is pictured and priced as the first-named product.
    """
    for name in names:
        if not name:
            continue
        matches = _iter_valid_sizes(name)
        if not matches:
            continue
        wv = [m for m in matches if _WV_RE.search(m.group("full"))]
        pool = wv or matches
        chosen = pool[-1]
        if len(pool) > 1:
            between = name[pool[0].end("full") : pool[-1].start("full")]
            if _BUNDLE_SEP_RE.search(between):
                chosen = pool[0]
        text = chosen.group("full")
        return re.sub(r"\s+", " ", text).strip(" ,.-")
    return None

if __name__ == "__main__":
    main()
