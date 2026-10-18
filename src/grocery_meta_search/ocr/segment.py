"""Flyer page segmentation: price anchors + name lines -> items.

Strategy ``anchor`` (most flyers): prices are the visual anchors — tall
digit glyphs. Cluster price fragments (dollars + superscript cents),
parse the value, then grow a name-line set outward from the line nearest
the price and re-OCR that region with Tesseract for clean text.

Strategy ``prix_line`` (Costco savings book): the big number is the
*discount*, not the price. The real price is a small ``Prix 1 234,56 $``
line; names are the text lines in the same grid cell above it.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Any

from PIL import Image

from ..sources.base import FlyerItem
from .engine import OcrLine, detect_lines, ocr_crop_text

# Lines that are never product names, in any store.
DEFAULT_STOPLIST = (
    r"net\s*wt",
    r"poids net",
    r"prix reg",
    r"prix incroyable",
    r"circulaire",
    r"entrepot et en ligne",
    r"n[o°]\s*d['’]?\s*article",
    r"valide du",
    r"economisez",
    r"aussi offert",
    r"offert pour livraison",
    r"en entrepot",
    r"ecofrais",
    r"^\s*economie\b",
    r"20\d{2}",  # dates (validity lines)
    r"pas encore membre",
    r"inscrivez-vous",
)

_DETAIL_LINE_RE = re.compile(
    r"(reg\.|regular|\$/kg|\$/lb|selection variee|assorted|produit du|product of"
    r"|^\d+\s*(g|kg|ml|l|oz|lb)\b|^\d+\s*x\s*\d+)",
    re.IGNORECASE,
)
_SIZE_ONLY_RE = re.compile(
    r"\d\s*(g|kg|ml|l|oz|lb)\b(?:[\s\-/]*\d+\s*(?:g|kg|ml|l|oz|lb)\b)?",
    re.IGNORECASE,
)
_CJK_RE = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")
_AMOUNT_RE = re.compile(r"(\d[\d\s]*),(\d{2})\s*\$?")
_DIGITS_RE = re.compile(r"^[\d/.,$¢%\s]+$")
# Trailing unit on a price line: "2,95 $/KG", "0,99 $/lb", "3,99 ch.",
# "499s/ch" (Odessa renders $ as s), "1,40 $/1b" (OCR misread of /lb).
# Stripped before the digitish check so the amount itself can anchor;
# size-only lines ("4,43 l", "227 g") do not match and are still rejected.
_PRICE_UNIT_RE = re.compile(
    r"\s*(?:/\s*(?:lb|1b|kg|un|ch|ea|l|sac|100\s*g(?:r)?)\b|s\s*/\s*ch\.?|(?<=\d)\s*(?:ch|lb|kg)\.?)\s*\*?\s*$",
    re.IGNORECASE,
)
_PRICE_TRAIL_RE = re.compile(r"\s*[*$¢]\s*$")
_PRICE_LEAD_RE = re.compile(r"^\s*[$¢]\s*")
_PRICE_S_TRAIL_RE = re.compile(r"(?<=\d)\s*[sS]\s*$")  # $ misread as S: "4,40S", "4S"


def _price_core(text: str) -> str:
    """Amount part of a price line, with unit suffix and $ stripped."""
    core = _PRICE_LEAD_RE.sub("", text.strip().replace("／", "/"))
    core = _PRICE_UNIT_RE.sub("", core)
    core = _PRICE_TRAIL_RE.sub("", core)
    core = _PRICE_S_TRAIL_RE.sub("", core)
    return core.strip()


@dataclass
class OcrStoreConfig:
    """Per-store OCR tuning. Fractions are relative to page height."""

    price_strategy: str = "anchor"  # "anchor" | "prix_line" | "name_cells" | "chalkboard"
    name_case: str = "caps"  # "caps" | "any"
    name_position: str = "any"  # "any" | "above" | "above_left" | "below"
    price_min_h_frac: float = 0.02
    name_min_h_frac: float = 0.004
    name_max_h_frac: float = 0.02
    block_y_gap_frac: float = 0.016
    block_x_gap_frac: float = 0.02  # stacking tolerance: allowed negative x-overlap
    block_min_overlap_frac: float = 0.0  # >0: a line joins a block only if this
    # fraction of its width overlaps the block's x-extent (wide detection
    # boxes otherwise bridge neighbouring product columns)
    match_max_dist_frac: float = 0.24  # of page width
    match_dx_weight: float = 1.0  # >1: prefer names in the price's column
    seed_overlap_bonus: float = 0.0  # px bonus when a name candidate's
    # x-extent overlaps the price anchor's (grid flyers: the name sits
    # directly above its price, the neighbour's name may be nearer)
    min_line_conf: float = 0.7
    tesseract_psm: int = 6
    bare_int_is_cents: bool = False  # T&T renders "68¢" with no dollar part
    merged_run_is_cents: bool = False  # "79¢" merged into one run "799" (3 Saisons)
    bare_int_anchor: bool = True  # False: a bare whole number is never a price (Odessa badges)
    ignore_below_frac: float = 1.0  # ignore name lines below this page fraction (legal footers)
    name_green_gate: bool = False  # True: name candidates must be printed
    # in green ink (Palumbo: display names are green, packaging label
    # text sitting nearer the price is not)
    name_lines_verify: bool = False  # True: drop re-OCR block lines that
    # share no content with the detected lines (Palumbo: the WOW badge
    # intrudes into the block crop and garbles its last line)
    pair_rate_anchors: bool = False  # True: merge same-line price pairs
    # into the leftmost (headline) anchor, the rest become alt prices
    # (Odessa: '10,99 $/lb  24,23 $/kg*' prints headline + rate on one
    # line; unpaired, the rate anchors its own item and steals names)
    stoplist: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        # Configs loaded from JSON carry stoplist as a list; the matching
        # code concatenates it with a tuple.
        self.stoplist = tuple(self.stoplist)


@dataclass
class PriceAnchor:
    value: float
    price_text: str
    box: tuple[float, float, float, float]
    conf: float
    multibuy: tuple[int, float] | None = None  # (count, total price)
    unit: str | None = None  # "lb" | "kg" | "each" | "100g" | "box"
    alt_texts: tuple[str, ...] = ()  # rate prints merged into this
    # anchor by the headline/rate pair merge (Odessa)


# Unit printed with a price: trailing on the price line itself
# ("2,95 $/KG", "3,99 ch.", "499s/ch") or as a standalone line beside /
# below the price ("CH/EA" under euro-marche prices, "/LB" right of
# kim-phat badges, "le 100 g" under adonis tags). The amount parser
# strips these suffixes to anchor; capture the unit before it is lost.
_UNIT_IN_TEXT_RE = re.compile(
    r"/\s*(100\s*g(?:r)?|lb|1b|kg|ch|ea|un|bte)\b"
    r"|\bs\s*/\s*(ch|lb)\b"
    r"|(?<=[\d.,])\s*(ch|ea)\.?\s*$"
    r"|le\s*(100\s*g(?:r)?)\b",
    re.IGNORECASE,
)
_UNIT_LINE_RE = re.compile(
    r"^\s*(?:/\s*(100\s*g(?:r)?|lb|kg|ch|ea|un|bte|bo[iî]te)\.?"
    r"|i\s*(kg|lb)"
    r"|le\s*100\s*g|ch\s*/\s*ea\.?|ch\.?|ea\.?|l['’]unit[ée])\s*$",
    re.IGNORECASE,
)


def _canon_unit(token: str) -> str:
    t = re.sub(r"[\s.]", "", token.lower())
    if t in ("lb", "1b"):
        return "lb"
    if t == "kg":
        return "kg"
    if t in ("100g", "100gr"):
        return "100g"
    if t in ("bte", "boite", "boîte"):
        return "box"
    return "each"  # ch, ea, un, l'unité


def _unit_in_text(text: str) -> str | None:
    m = _UNIT_IN_TEXT_RE.search(text)
    if m:
        token = next(g for g in m.groups() if g)
        return _canon_unit(token)
    m = _UNIT_LINE_RE.match(text)
    if m:
        token = next((g for g in m.groups() if g), None)
        if token:
            # Slash forms ("/lb") and the OCR slash-misread "IKG"/"ILB"
            # (a whole line that is just the misread unit).
            return _canon_unit(token)
        if "100" in text:
            return "100g"  # "le 100 g" standalone line
        return "each"  # "ch." / "ea." / "l'unité" standalone line
    return None


def _nearby_unit(lines: list[OcrLine], box: tuple[float, float, float, float],
                 page_w: int, page_h: int) -> str | None:
    """Unit from a standalone unit line printed right of or below a price."""
    best: tuple[float, str] | None = None
    for ln in lines:
        unit = _unit_in_text(ln.text)
        if unit is None or not _UNIT_LINE_RE.match(ln.text.strip()):
            continue
        y_overlap = min(ln.bottom, box[3]) - max(ln.y, box[1])
        x_overlap = min(ln.right, box[2]) - max(ln.x, box[0])
        dist: float | None = None
        # Right of the price: the unit line may overlap the price box's
        # right edge (the box spans dollars+cents fragments; "/lb" prints
        # immediately after the cents — euro-marche, kim-phat).
        if y_overlap >= 0.4 * ln.h and -0.4 * ln.w <= ln.x - box[2] <= 0.06 * page_w:
            dist = max(0.0, ln.x - box[2])
        elif (
            # Tucked at the price's bottom-right corner, right-aligned
            # with the cents (euro-marche "CH/EA" under the cents).
            abs(ln.right - box[2]) <= 0.04 * page_w
            and ln.x >= box[0] - 0.02 * page_w
            and (
                y_overlap >= 0.2 * ln.h
                or -0.35 * ln.h
                <= ln.y - box[3]
                <= 0.85 * (box[3] - box[1]) + 0.004 * page_h
            )
        ):
            dist = 500.0 + abs(ln.right - box[2])
        elif (
            x_overlap >= 0.3 * ln.w
            and 0 <= ln.y - box[3] <= 0.8 * (box[3] - box[1]) + 0.004 * page_h
        ):
            dist = 1000.0 + (ln.y - box[3])  # below the price (weaker)
        if dist is not None and (best is None or dist < best[0]):
            best = (dist, unit)
    return best[1] if best else None


def _squash(text: str) -> str:
    """Lowercase, strip accents and all whitespace (stoplist matching)."""
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"[\s'’]+", "", text)


def _stop_match(text: str, patterns: tuple[str, ...]) -> bool:
    squashed = _squash(text)
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
        literal = _squash(re.sub(r"[^a-z0-9 ]", " ", pattern))
        if literal and len(literal) >= 5 and literal in squashed:
            return True
    return False


def _is_digitish(text: str) -> bool:
    t = text.strip()
    if not t or not _DIGITS_RE.match(t):
        return False
    digits = sum(c.isdigit() for c in t)
    return digits >= 1 and digits / max(len(t), 1) >= 0.5


def _is_caps(text: str) -> bool:
    letters = [c for c in text if c.isalpha()]
    return len(letters) >= 3 and sum(1 for c in letters if c.isupper()) / len(letters) > 0.8


def _parse_one_price(t: str) -> tuple[float, str] | None:
    """Parse one cleaned price text ("15.99", "1599", "7.97") -> (value, text)."""
    t = t.replace(",", ".").rstrip("/-").strip()
    if re.fullmatch(r"\d+\.\d{2}", t):
        return float(t), t
    if re.fullmatch(r"\d{3,4}", t):  # merged dollars+cents: "1599", "744"
        return int(t[:-2]) + int(t[-2:]) / 100, f"{t[:-2]}.{t[-2:]}"
    return None


def _split_dual_prices(texts: list[str]) -> list[tuple[float, str]] | None:
    """Two sale/regular prices glued in one cluster ("24992999", ["1499","1699"]).

    M&M-style layouts print member price + regular price side by side; OCR
    merges them into one line or two adjacent digitish fragments that the
    normal dollars+cents parse rejects. Returns both prices (sale first)
    when every fragment is independently a full price, else None.
    """
    if len(texts) == 1 and re.fullmatch(r"\d{8}", texts[0]):
        t = texts[0]
        halves = [t[:4], t[4:]]
    elif len(texts) == 2:
        halves = list(texts)
    else:
        return None
    parsed = [_parse_one_price(h) for h in halves]
    if any(p is None for p in parsed):
        return None
    return [p for p in parsed if p is not None]


def _parse_fragment_value(
    texts: list[str], raw_joined: str = "", merged_run_is_cents: bool = False
) -> tuple[float, str, tuple[int, float] | None] | None:
    """Parse clustered price fragments into (value, price_text, multibuy)."""
    joined = "".join(texts)
    m = re.fullmatch(r"(\d+)/\$?(\d+(?:[.,]\d{1,2})?)", joined)
    if m and (len(texts) == 1 or ("." not in m.group(2) and "," not in m.group(2))):
        # "2/500" -> 2 for 5.00; "2/$5" -> 2 for 5.00; "2/11" -> 2 for 11.00.
        # A decimal total ("2/5,99$") is trusted only as a single OCR
        # token: in a multi-fragment cluster the digits after the slash
        # may be a NEIGHBOUR's complete price glued to a complete
        # multibuy token (palumbo: "2/$5" + "6.99" -> "2/56.99").
        count, total_raw = int(m.group(1)), m.group(2)
        if count > 100:
            # A neighbouring price line glued into the cluster
            # ("8 99 8/6.00" -> count 8998): no flyer sells bundles of
            # thousands; the parse is garble. Mirrors the >100 multibuy
            # rejection in prices.split_unit.
            return None
        if "," in total_raw or "." in total_raw:
            # Quebec decimal comma: "2/5,99$" -> total 5.99 (round-2
            # review: the digits-only form missed every comma total,
            # and a neighbour's price won the cell instead).
            total = float(total_raw.replace(",", "."))
        elif len(total_raw) >= 3:
            total = int(total_raw[:-2]) + int(total_raw[-2:]) / 100
        elif "¢" in raw_joined:
            total = int(total_raw) / 100  # "2/99¢" -> 2 for 0.99
        else:
            total = float(total_raw)
        return total / count, f"{count}/{total:.2f}", (count, total)
    if len(texts) == 1:
        t = texts[0].replace(",", ".").rstrip("/-")
        m_pct = re.fullmatch(r"(\d{1,3})%", t)
        if m_pct and ("/" in raw_joined or "¢" in raw_joined):
            # OCR reads the cents glyph as '%' on some display fonts
            # ("87¢" -> "87%", 3-saisons apples at 87¢/lb beside the
            # "1,92 $/kg" equivalent). The cluster-context gate (a unit
            # slash or ¢ in the cluster's raw text) keeps standalone
            # discount badges ("25%") from anchoring.
            cents = int(m_pct.group(1))
            return cents / 100, f"0.{cents:02d}", None
        if re.fullmatch(r"\d+\.\d{2}", t):
            return float(t), t, None
        if re.fullmatch(r"\d{3,4}", t):  # merged dollars+cents: "1599", "744"
            if (
                merged_run_is_cents
                and len(t) == 3
                and t.endswith("9")
                and ("¢" in raw_joined or "%" in raw_joined)
            ):
                # A cents display ("79¢") whose ¢ glyph merged into the
                # run as a trailing 9: the value is the first two digits.
                # Gated on the cluster still carrying the ¢/% glyph
                # somewhere (valmont review, 2026-10-17): ungated, this
                # branch corrupted every merged dollar price ending in
                # 9 ("7.99" -> 0.79, "3.29" -> 0.32, "3.59" -> 0.35),
                # which is far more common than a true cents merge.
                return int(t[:2]) / 100, f"0.{t[:2]}", None
            return int(t[:-2]) + int(t[-2:]) / 100, f"{t[:-2]}.{t[-2:]}", None
        if re.fullmatch(r"\d{1,2}", t):  # whole dollars, or cents (see cfg)
            return float(t), t, None
        return None
    if len(texts) == 2:  # dollars + cents fragments: "6" + "49"
        d, c = texts
        if re.fullmatch(r"\d+", d) and re.fullmatch(r"\d{2}", c):
            return int(d) + int(c) / 100, f"{d}.{c}", None
    return None


_MERGED_RUN_RE = re.compile(r"^\s*(\d{3,4})(?![\d.,])")


def _scan_merged_run(text: str) -> tuple[float, str] | None:
    """Price token at the start of a tall non-digitish line.

    Odessa renders "10⁹⁹ $/lb" and OCR returns one line "1099 S/6": the
    amount is the leading merged digit run and the rest is unit junk. The
    junk must contain a price marker ($, /, ¢) so addresses, phone
    numbers and dates at the start of a line do not qualify.
    """
    m = _MERGED_RUN_RE.match(text)
    if not m:
        return None
    rest = text[m.end() :]
    if not any(ch in rest for ch in "$/¢"):
        return None
    return _parse_one_price(m.group(1))


def _parse_fragment_token(
    core: str, raw: str = ""
) -> tuple[float, str, tuple[int, float] | None] | None:
    """Recover a price from one fragment whose cluster did not parse whole.

    Either the fragment parses on its own (multibuy "2/$5", merged "2423")
    or its first whitespace-separated token is a full price ("2423 8" ->
    24.23; "099 8/1" -> 0.99, the dollar digit itself misread).
    """
    single = _parse_fragment_value([core], raw_joined=raw or core)
    if single is not None:
        return single
    parts = core.split()
    if len(parts) > 1:
        parsed = _parse_one_price(parts[0])
        if parsed is not None:
            return parsed[0], parsed[1], None
    return None


def find_price_anchors(
    lines: list[OcrLine], page_w: int, page_h: int, cfg: OcrStoreConfig
) -> list[PriceAnchor]:
    min_h = cfg.price_min_h_frac * page_h
    frags = [
        ln
        for ln in lines
        if ln.h >= min_h and ln.conf >= 0.5 and _is_digitish(_price_core(ln.text))
    ]
    frags.sort(key=lambda z: (z.y, z.x))
    clusters: list[list[OcrLine]] = []
    for frag in frags:
        placed = False
        for cluster in clusters:
            for member in cluster:
                y_overlap = min(frag.bottom, member.bottom) - max(frag.y, member.y)
                x_gap = max(0, max(frag.x, member.x) - min(frag.right, member.right))
                if y_overlap > 0.3 * min(frag.h, member.h) and x_gap < 0.09 * page_w:
                    cluster.append(frag)
                    placed = True
                    break
            if placed:
                break
        if not placed:
            clusters.append([frag])
    anchors: list[PriceAnchor] = []
    parsed_clusters: list[tuple[list[OcrLine], float, str, tuple[int, float] | None]] = []
    for cluster in clusters:
        cluster.sort(key=lambda z: z.x)
        cleaned = [_price_core(c.text.strip()) for c in cluster]
        dual = _split_dual_prices(cleaned)
        if dual is not None:
            for value, price_text in dual:
                parsed_clusters.append((cluster, value, price_text, None))
            continue
        parsed = _parse_fragment_value(
            cleaned,
            raw_joined="".join(c.text for c in cluster),
            merged_run_is_cents=cfg.merged_run_is_cents,
        )
        if parsed is not None:
            parsed_clusters.append((cluster, *parsed))
            continue
        # Recovery: the cluster as a whole did not parse — OCR glued unit
        # junk or a garbled sibling fragment onto a good price ("2423 8",
        # "099 8/1" clustered with "1982"). Recover a token per fragment.
        for member in cluster:
            token = _parse_fragment_token(
                _price_core(member.text.strip()),
                raw="".join(c.text for c in cluster),
            )
            if token is not None:
                parsed_clusters.append(([member], *token))
    # Tall lines that never became fragments can still carry a price as a
    # leading merged digit run followed by unit junk ("1099 S/6").
    frag_ids = {id(f) for f in frags}
    for ln in lines:
        if id(ln) in frag_ids or ln.h < min_h or ln.conf < 0.5:
            continue
        scanned = _scan_merged_run(ln.text)
        if scanned is not None:
            parsed_clusters.append(([ln], scanned[0], scanned[1], None))
    if not parsed_clusters:
        return anchors
    heights = sorted(max(c.h for c in cl) for cl, *_ in parsed_clusters)
    median_h = heights[len(heights) // 2]
    for cluster, value, price_text, multibuy in parsed_clusters:
        cluster_h = max(c.h for c in cluster)
        lone_int = (
            multibuy is None
            and value == int(value)
            and 0 < value < 100
            and len(cluster) == 1
            and len(_price_core(cluster[0].text.strip())) <= 2
        )
        if lone_int and cluster_h < 0.7 * median_h:
            # Sub-size lone digits are usually a price fragment whose dollar
            # digit OCR missed (e.g. "1 48" -> "48"): skip rather than guess.
            continue
        if lone_int and not cfg.bare_int_is_cents and not cfg.bare_int_anchor:
            # Store config: real prices always carry cents, so a bare whole
            # number is a discount badge ("RABAIS 8 $") or a stray digit.
            continue
        if lone_int and cfg.bare_int_is_cents:
            value = value / 100
            price_text = f"{value:.2f}"
        box = (
            min(c.x for c in cluster),
            min(c.y for c in cluster),
            max(c.right for c in cluster),
            max(c.bottom for c in cluster),
        )
        unit: str | None = None
        for c in cluster:
            unit = _unit_in_text(c.text)
            if unit:
                break
        if unit is None:
            unit = _nearby_unit(lines, box, page_w, page_h)
        if unit is None and multibuy is not None:
            unit = "each"  # "2/500" prices are per-item deals
        anchors.append(
            PriceAnchor(
                value=value,
                price_text=price_text,
                box=box,
                conf=min(c.conf for c in cluster),
                multibuy=multibuy,
                unit=unit,
            )
        )
    return anchors


def name_candidates(lines: list[OcrLine], page_h: int, cfg: OcrStoreConfig) -> list[OcrLine]:
    """Lines that may belong to a product name block."""
    patterns = DEFAULT_STOPLIST + cfg.stoplist
    cands: list[OcrLine] = []
    for line in lines:
        if line.y > cfg.ignore_below_frac * page_h:
            continue
        if not (cfg.name_min_h_frac * page_h <= line.h <= cfg.name_max_h_frac * page_h):
            continue
        if line.conf < cfg.min_line_conf:
            continue
        text = line.text.strip()
        if len([c for c in text if c.isalpha()]) < 3:
            continue
        if _CJK_RE.search(text) and len(_CJK_RE.findall(text)) / max(len(text), 1) > 0.3:
            continue
        if cfg.name_case == "caps" and not _is_caps(text):
            continue
        if _is_digitish(text) or _SIZE_ONLY_RE.fullmatch(text):
            continue
        if _stop_match(text, patterns):
            continue
        cands.append(line)
    return cands


def _edge_gaps(
    a: tuple[float, float, float, float], b: tuple[float, float, float, float]
) -> tuple[float, float]:
    dx = max(0.0, max(a[0], b[0]) - min(a[2], b[2]))
    dy = max(0.0, max(a[1], b[1]) - min(a[3], b[3]))
    return dx, dy


def _edge_dist(a: tuple[float, float, float, float], b: tuple[float, float, float, float]) -> float:
    dx, dy = _edge_gaps(a, b)
    return float((dx * dx + dy * dy) ** 0.5)


def _match_dist(
    a: tuple[float, float, float, float], b: tuple[float, float, float, float], dx_weight: float
) -> float:
    """Edge distance with horizontal gaps weighted (column preference)."""
    dx, dy = _edge_gaps(a, b)
    return float(((dx_weight * dx) ** 2 + dy**2) ** 0.5)


def _boxes_near(a: OcrLine, b: OcrLine) -> bool:
    """True when two lines substantially overlap (same text detected twice)."""
    y_overlap = min(a.bottom, b.bottom) - max(a.y, b.y)
    x_overlap = min(a.right, b.right) - max(a.x, b.x)
    return y_overlap > 0.4 * min(a.h, b.h) and x_overlap > 0.2 * min(a.w, b.w)


def _dedupe_candidates(cands: list[OcrLine]) -> list[OcrLine]:
    """Drop lower-confidence duplicates of the same text in the same spot.

    RapidOCR sometimes emits the same line twice with slightly different
    spacing ("Pommesdeterre augratin supremes" vs "Pommes deterre
    augratinsupremes"); without dedup, dual price anchors each claim one
    copy and the product is extracted twice.
    """
    kept: list[OcrLine] = []
    for ln in sorted(cands, key=lambda z: (-z.conf, z.y, z.x)):
        if any(_shares_content(ln.text, k.text) and _boxes_near(ln, k) for k in kept):
            continue
        kept.append(ln)
    return kept


def _line_box(line: OcrLine) -> tuple[float, float, float, float]:
    return (line.x, line.y, line.right, line.bottom)


def _grow_name_lines(
    anchor: PriceAnchor,
    cands: list[OcrLine],
    claimed: set[int],
    stack: dict[int, int],
    page_w: int,
    page_h: int,
    cfg: OcrStoreConfig,
) -> list[OcrLine]:
    """Seed = nearest unclaimed candidate (stack-aware); grow by stacking."""
    max_dist = cfg.match_max_dist_frac * page_w
    available = [ln for ln in cands if id(ln) not in claimed]
    if not available:
        return []

    def seed_score(line: OcrLine) -> float:
        score = _match_dist(anchor.box, _line_box(line), cfg.match_dx_weight) - 35 * min(
            stack.get(id(line), 0), 3
        )
        if cfg.seed_overlap_bonus > 0:
            overlap = min(line.right, anchor.box[2]) - max(line.x, anchor.box[0])
            if overlap > 0:
                score -= cfg.seed_overlap_bonus
        return score

    seed = min(available, key=seed_score)
    if _match_dist(anchor.box, _line_box(seed), cfg.match_dx_weight) > max_dist:
        return []
    selected = [seed]
    max_gap = cfg.block_y_gap_frac * page_h
    changed = True
    while changed:
        changed = False
        ux0 = min(s.x for s in selected)
        ux1 = max(s.right for s in selected)
        for line in available:
            if line in selected or id(line) in claimed:
                continue
            if _edge_dist(anchor.box, _line_box(line)) > max_dist:
                continue
            if cfg.block_min_overlap_frac > 0:
                u_overlap = min(line.right, ux1) - max(line.x, ux0)
                if u_overlap < cfg.block_min_overlap_frac * line.w:
                    continue
            for sel in selected:
                y_gap = max(line.y - sel.bottom, sel.y - line.bottom)
                x_overlap = min(line.right, sel.right) - max(line.x, sel.x)
                if y_gap <= max_gap and x_overlap > -cfg.block_x_gap_frac * page_w:
                    selected.append(line)
                    changed = True
                    break
    return sorted(selected, key=lambda z: (z.y, z.x))


def _stack_counts(
    cands: list[OcrLine], page_w: int, page_h: int, cfg: OcrStoreConfig
) -> dict[int, int]:
    """How many other candidates stack vertically with each candidate."""
    max_gap = cfg.block_y_gap_frac * page_h
    counts: dict[int, int] = {}
    for line in cands:
        n = 0
        for other in cands:
            if other is line:
                continue
            y_gap = max(other.y - line.bottom, line.y - other.bottom)
            x_overlap = min(line.right, other.right) - max(line.x, other.x)
            if y_gap <= max_gap and x_overlap > -cfg.block_x_gap_frac * page_w:
                n += 1
        counts[id(line)] = n
    return counts


def _tokens(text: str) -> set[str]:
    squashed = _squash(text)
    return {t for t in re.split(r"[^a-z0-9]+", squashed) if len(t) >= 3}


def _shares_content(a: str, b: str) -> bool:
    """True when two OCR texts share a long common substring (same content,
    possibly different spacing/accents)."""
    import difflib

    sa, sb = _squash(a), _squash(b)
    if not sa or not sb:
        return False
    match = difflib.SequenceMatcher(None, sa, sb).find_longest_match(0, len(sa), 0, len(sb))
    return match.size >= 7


def _line_shares_content(line: str, fallback: str) -> bool:
    """Per-line variant of _shares_content for the re-OCR verify: a
    short line ('GRANDE', 6 chars) can never reach the 7-char bar, so
    the bar scales with the line's own length — a short line must be
    (nearly) fully contained in the detected lines, a long one needs
    the usual long common run. 'G RAN DE Eh' squashes to 'grandeh':
    its longest run in '...parmesanrapegrande' is 6 < 7, dropped."""
    import difflib

    sa, sb = _squash(line), _squash(fallback)
    if not sa or not sb:
        return False
    match = difflib.SequenceMatcher(None, sa, sb).find_longest_match(
        0, len(sa), 0, len(sb)
    )
    return match.size >= min(7, max(4, len(sa) - 1))


def _name_from_text(
    block_text: str | None,
    fallback_lines: list[OcrLine],
    *,
    verify_lines: bool = False,
) -> str:
    """Product name: leading all-caps run of the clean block text.

    Falls back to the detected lines when the re-OCR text shares no token
    with them (its crop picked up a neighbouring badge or photo text).
    With verify_lines, that check applies per line: a re-OCR line
    sharing no content with the detected lines is a badge/photo
    intrusion and is dropped.
    """
    fallback = "\n".join(ln.text for ln in fallback_lines)
    source = block_text if block_text else fallback
    dropped = False
    name_lines: list[str] = []
    for raw in source.splitlines():
        line = raw.strip()
        if not line:
            continue
        if verify_lines and block_text and not _line_shares_content(line, fallback):
            dropped = True
            continue  # badge/photo intrusion in the re-OCR crop
        if not name_lines and not _is_caps(line):
            continue  # skip garbled/badge lead-in lines before the name
        if name_lines and (not _is_caps(line) or _DETAIL_LINE_RE.search(line)):
            break
        if _DETAIL_LINE_RE.search(line) and name_lines:
            break
        name_lines.append(line)
        if len(name_lines) >= 5:
            break
    name = re.sub(r"\s+", " ", " ".join(name_lines)).strip(" .|")
    if block_text and dropped:
        # The re-OCR crop was partly intruded on; the detected lines
        # are the cleaner source for the whole name.
        from_lines = _name_from_text(None, fallback_lines)
        if from_lines:
            return from_lines
    if block_text and name and not _shares_content(name, fallback):
        return _name_from_text(None, fallback_lines)
    return name


def _name_from_lines_any(lines: list[OcrLine]) -> str:
    """Name for mixed-case layouts (T&T): first stacked lines, sans details."""
    parts: list[str] = []
    for line in lines:
        text = line.text.strip()
        if _DETAIL_LINE_RE.search(text) and parts:
            break
        parts.append(text)
        if len(parts) >= 3:
            break
    return re.sub(r"\s+", " ", " ".join(parts)).strip(" .|")


def segment_page(
    image: Image.Image,
    lines: list[OcrLine],
    cfg: OcrStoreConfig,
    *,
    page_url: str,
    page_number: int,
) -> list[FlyerItem]:
    """Extract items from one flyer page."""
    page_w, page_h = image.size
    if cfg.price_strategy == "prix_line":
        return _segment_prix_line(image, lines, cfg, page_url, page_number)
    if cfg.price_strategy == "name_cells":
        return _segment_name_cells(image, lines, cfg, page_url, page_number)
    if cfg.price_strategy == "chalkboard":
        return _segment_chalkboard(image, lines, cfg, page_url, page_number)
    if cfg.price_strategy == "red_grid":
        return _segment_red_grid(image, lines, cfg, page_url, page_number)
    anchors = find_price_anchors(lines, page_w, page_h, cfg)
    if cfg.pair_rate_anchors:
        anchors = _merge_rate_pairs(anchors, page_w)
    return _items_from_anchors(image, lines, cfg, anchors, page_url, page_number)


def _merge_rate_pairs(
    anchors: list[PriceAnchor], page_w: int
) -> list[PriceAnchor]:
    """Merge same-line headline+rate anchor pairs (Odessa).

    The catalogue prints the headline price and a smaller unit rate
    on one line ('10,99 $/lb  24,23 $/kg*'). As separate anchors the
    rate forms its own item and steals the name block. Anchors whose
    boxes overlap vertically by at least half the smaller height and
    sit within 0.30 page widths horizontally merge into the LEFTMOST
    anchor (the headline prints first); the merged anchors' price
    texts ride along as alt prices.
    """
    def paired(a: PriceAnchor, b: PriceAnchor) -> bool:
        y_overlap = min(a.box[3], b.box[3]) - max(a.box[1], b.box[1])
        smaller_h = min(a.box[3] - a.box[1], b.box[3] - b.box[1])
        x_gap = max(a.box[0] - b.box[2], b.box[0] - a.box[2])
        return (
            smaller_h > 0
            and y_overlap >= 0.5 * smaller_h
            and x_gap <= 0.30 * page_w
        )

    groups: list[list[PriceAnchor]] = []
    for anchor in anchors:
        for group in groups:
            if any(paired(anchor, member) for member in group):
                group.append(anchor)
                break
        else:
            groups.append([anchor])
    merged: list[PriceAnchor] = []
    for group in groups:
        if len(group) == 1:
            merged.append(group[0])
            continue
        host = min(group, key=lambda a: a.box[0])
        host.alt_texts = (
            *host.alt_texts,
            *(
                a.price_text
                for a in sorted(group, key=lambda a: a.box[0])
                if a is not host
            ),
        )
        merged.append(host)
    return merged


def _line_green_ink(image: Image.Image, ln: OcrLine) -> float:
    """Fraction of a line's ink pixels that are green.

    Palumbo's display names print in the chain's dark green while
    packaging label text (black, red, white-on-photo) sits nearer the
    price and wins plain nearest-line seeding. Measured on the
    2026-10-15 page: display lines score 0.64-0.94, label lines
    0.00-0.05.
    """
    import cv2
    import numpy as np

    arr = np.asarray(image)
    x0, y0 = max(0, int(ln.x)), max(0, int(ln.y))
    x1 = min(arr.shape[1], int(ln.right))
    y1 = min(arr.shape[0], int(ln.bottom))
    if x1 <= x0 or y1 <= y0:
        return 0.0
    hsv = cv2.cvtColor(arr[y0:y1, x0:x1], cv2.COLOR_RGB2HSV)
    ink = (hsv[:, :, 2] < 205) | (hsv[:, :, 1] > 70)
    if not ink.any():
        return 0.0
    green = (
        (hsv[:, :, 0] >= 50)
        & (hsv[:, :, 0] <= 95)
        & (hsv[:, :, 1] >= 70)
        & (hsv[:, :, 2] >= 35)
    )
    return float((green & ink).sum() / max(int(ink.sum()), 1))


def _items_from_anchors(
    image: Image.Image,
    lines: list[OcrLine],
    cfg: OcrStoreConfig,
    anchors: list[PriceAnchor],
    page_url: str,
    page_number: int,
) -> list[FlyerItem]:
    """Pair price anchors with name blocks (the 'anchor' strategy
    body, shared with the chalkboard strategy whose anchors come
    from detected price boards instead of OCR lines)."""
    page_w, page_h = image.size
    cands = _dedupe_candidates(name_candidates(lines, page_h, cfg))
    if cfg.name_green_gate:
        cands = [ln for ln in cands if _line_green_ink(image, ln) >= 0.4]
    stack = _stack_counts(cands, page_w, page_h, cfg)

    claimed: set[int] = set()
    line_owner: dict[int, FlyerItem] = {}
    _item_anchor_box: dict[int, tuple[float, float, float, float]] = {}
    items: list[FlyerItem] = []

    def positioned(anchor: PriceAnchor) -> list[OcrLine]:
        """Name candidates on the configured side of the price anchor.

        Some layouts (Palumbo) stack name / photo / price vertically with
        the *next* product's name just below this price; unrestricted
        nearest-neighbour matching then swaps names between products.
        """
        if cfg.name_position == "above":
            return [ln for ln in cands if ln.bottom <= anchor.box[1] + 0.01 * page_h]
        if cfg.name_position == "above_left":
            # Diagonal layouts (Bulk Barn): the name sits at the top-left
            # of the product cell, the price at the bottom-right; the
            # neighbouring column's name is nearer but its centre is to
            # the RIGHT of the price centre.
            anchor_cx = (anchor.box[0] + anchor.box[2]) / 2
            return [
                ln
                for ln in cands
                if ln.bottom <= anchor.box[1] + 0.01 * page_h and ln.cx <= anchor_cx + 0.05 * page_w
            ]
        if cfg.name_position == "below":
            return [ln for ln in cands if ln.y >= anchor.box[3] - 0.01 * page_h]
        return cands

    def fold_alt(item: FlyerItem, anchor: PriceAnchor) -> None:
        """Fold a second price for an item into alt_prices.

        Dual $/lb + $/kg printing (Odessa): the $/kg reference often
        anchors first because it sits with the name, but the $/lb
        figure is the advertised price — when the pair is kg/lb-related
        (ratio ~2.2046) and the incoming price is the smaller ($/lb)
        one, promote it to main and demote the $/kg figure to alt.
        """
        alts = item.conditions.setdefault("alt_prices", [])
        if not isinstance(alts, list):
            return
        box = _item_anchor_box.get(id(item))
        if (
            item.price_value
            and anchor.value < item.price_value
            and 2.15 <= item.price_value / anchor.value <= 2.26
            and (
                item.price_unit == "kg"
                or (
                    box is not None
                    and (anchor.box[3] - anchor.box[1]) > (box[3] - box[1])
                )
            )
        ):
            if item.price_text:
                alts.append(item.price_text)
            item.price_value = anchor.value
            item.price_text = anchor.price_text
            item.price_unit = anchor.unit or "lb"
        else:
            alts.append(anchor.price_text)

    def anchor_priority(anchor: PriceAnchor) -> float:
        pool = positioned(anchor)
        if not pool:
            return float("inf")
        return min(
            _match_dist(anchor.box, _line_box(ln), cfg.match_dx_weight)
            - 35 * min(stack.get(id(ln), 0), 3)
            for ln in pool
        )

    for anchor in sorted(anchors, key=anchor_priority):
        # Dual pricing (sale + regular in one cluster) yields two anchors
        # with the same box: fold the later one into the existing item.
        twin = next(
            (o for o in items if _edge_dist(anchor.box, _item_anchor_box[id(o)]) <= 0.01 * page_w),
            None,
        )
        if twin is not None:
            fold_alt(twin, anchor)
            continue
        grown = _grow_name_lines(anchor, positioned(anchor), claimed, stack, page_w, page_h, cfg)
        if not grown:
            # Maybe a second price for an item already extracted (multibuy
            # or dual price sharing one name block): fold into alt prices.
            near = [
                ln
                for ln in cands
                if _edge_dist(anchor.box, _line_box(ln)) <= cfg.match_max_dist_frac * page_w
            ]
            for line in near:
                owner = line_owner.get(id(line))
                if owner is not None:
                    fold_alt(owner, anchor)
                    break
            continue
        for line in grown:
            claimed.add(id(line))
        bx = (
            min(ln.x for ln in grown),
            min(ln.y for ln in grown),
            max(ln.right for ln in grown),
            max(ln.bottom for ln in grown),
        )
        block_text = ocr_crop_text(image, bx, psm=cfg.tesseract_psm)
        if cfg.name_case == "any":
            name = _name_from_lines_any(grown)
        else:
            name = _name_from_text(
                block_text, grown, verify_lines=cfg.name_lines_verify
            )
        if not name:
            continue
        # Dual-price fold: member + regular price in one badge grow
        # near-identical names from adjacent anchors. Merge into the
        # existing item (lower price wins as the main price) instead of
        # duplicating the product.
        dup_of: FlyerItem | None = None
        for other in items:
            if (
                _shares_content(name, other.name_fr or "")
                and _edge_dist(anchor.box, _item_anchor_box[id(other)]) <= 0.06 * page_w
            ):
                dup_of = other
                break
        if dup_of is not None:
            alts = dup_of.conditions.setdefault("alt_prices", [])
            if isinstance(alts, list):
                if anchor.value < (dup_of.price_value or float("inf")):
                    old_value = dup_of.price_value
                    if dup_of.price_text:
                        alts.append(dup_of.price_text)
                    dup_of.price_value = anchor.value
                    dup_of.price_text = anchor.price_text
                    if (
                        old_value
                        and 2.15 <= old_value / anchor.value <= 2.26
                        and dup_of.price_unit == "kg"
                    ):
                        # kg/lb dual pair: the smaller figure is $/lb.
                        dup_of.price_unit = anchor.unit or "lb"
                else:
                    alts.append(anchor.price_text)
            for line in grown:
                claimed.add(id(line))
                line_owner[id(line)] = dup_of
            continue
        region = (
            min(anchor.box[0], bx[0]),
            min(anchor.box[1], bx[1]),
            max(anchor.box[2], bx[2]),
            max(anchor.box[3], bx[3]),
        )
        conditions: dict[str, object] = {}
        if anchor.multibuy:
            count, total = anchor.multibuy
            conditions["multibuy"] = {"count": count, "total": total}
        if anchor.alt_texts:
            conditions["alt_prices"] = list(anchor.alt_texts)
        item = FlyerItem(
            name_fr=name,
            price_text=anchor.price_text,
            price_value=anchor.value,
            price_unit=anchor.unit,
            image_url=page_url,
            bbox={
                "left": round(region[0] / page_w * 1000),
                "top": round(region[1] / page_h * 1000),
                "right": round(region[2] / page_w * 1000),
                "bottom": round(region[3] / page_h * 1000),
                "page": page_number,
            },
            conditions=conditions,
            languages=["fr"],
            raw={"block_text": block_text, "ocr_lines": [ln.text for ln in grown]},
            confidence=round(min(anchor.conf, 0.99), 2),
        )
        items.append(item)
        _item_anchor_box[id(item)] = anchor.box
        for line in grown:
            line_owner[id(line)] = item
    return items


def _segment_name_cells(
    image: Image.Image,
    lines: list[OcrLine],
    cfg: OcrStoreConfig,
    page_url: str,
    page_number: int,
) -> list[FlyerItem]:
    """Monde au Naturel: the catalogue prints no dollar prices.

    Each product sits in a green-framed cell: photo on top, the name in
    white caps on a solid green band across the cell's bottom, and a
    leaf badge (``SPÉCIAL n %``) at the top-right corner. Detect the
    cells by their green colour, OCR the band for the name, read the
    badge percent from the page's OCR lines, and emit price-less items
    (Alex's call, 2026-10-17: list the products without prices).
    """
    import cv2
    import numpy as np

    page_w, page_h = image.size
    bgr = cv2.cvtColor(np.array(image.convert("RGB")), cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array([35, 80, 80]), np.array([90, 255, 255]))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cells: list[tuple[int, int, int, int]] = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        # A product cell is about a quarter of the page wide; the cover
        # art, the full-width footer and the photo frames fall outside.
        if 0.18 * page_w < w < 0.38 * page_w and 0.10 * page_h < h < 0.30 * page_h:
            cells.append((x, y, w, h))
    cells.sort(key=lambda b: (round(b[1] / (0.08 * page_h)), b[0]))

    def badge_percent(cell: tuple[int, int, int, int]) -> int | None:
        x, y, w, _h = cell
        for ln in lines:
            # The leaf badge overlaps the cell's top-right corner; its
            # digits line starts around 0.6 of the cell width in.
            if not (x + 0.55 * w <= ln.x <= x + w + 0.08 * page_w):
                continue
            if not (y - 0.02 * page_h <= ln.y <= y + 0.10 * page_h):
                continue
            m = re.fullmatch(r"\s*(\d{1,2})\s*%?\s*", ln.text)
            if m and 5 <= int(m.group(1)) <= 60:
                return int(m.group(1))
        return None

    items: list[FlyerItem] = []
    for cell in cells:
        x, y, w, h = cell
        band = (x + 6, y + int(0.62 * h), x + w - 6, y + h - 4)
        text = ocr_crop_text(image, band, psm=cfg.tesseract_psm)
        if not text:
            continue
        name_lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        # A sliver of the photo's packaging text can ride the band's
        # top edge ("RES" off a box flap): drop a short leading line.
        if len(name_lines) > 1 and len(re.sub(r"[^A-Za-zÀ-ÿ]", "", name_lines[0])) <= 4:
            name_lines = name_lines[1:]
        name = re.sub(r"\s+", " ", " ".join(name_lines)).strip(" .|")
        if len(name) < 8 or not any(c.isalpha() for c in name):
            continue
        conditions: dict[str, object] = {}
        pct = badge_percent(cell)
        if pct is not None:
            conditions["discount_percent"] = pct
        items.append(
            FlyerItem(
                name_fr=name,
                image_url=page_url,
                bbox={
                    "left": round(x / page_w * 1000),
                    "top": round(y / page_h * 1000),
                    "right": round((x + w) / page_w * 1000),
                    "bottom": round((y + h) / page_h * 1000),
                    "page": page_number,
                },
                conditions=conditions,
                languages=["fr"],
                raw={"strategy": "name_cells", "band_text": text},
                confidence=0.85,
            )
        )
    return items


def _detect_board_boxes(
    image: Image.Image, vmax: int
) -> list[tuple[int, int, int, int]]:
    """Dark chalkboard interiors on a PA Nature page.

    The boards are near-black rectangles (wood frame excluded); a
    stricter threshold (vmax=60) isolates the board core from photo
    shadows, a looser one (110) gives a slightly larger box — pooled
    OCR reads differ per box, so both are used downstream.
    """
    import cv2
    import numpy as np

    page_w, page_h = image.size
    bgr = cv2.cvtColor(np.array(image.convert("RGB")), cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array([0, 0, 0]), np.array([180, 110, vmax]))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((9, 15), np.uint8))
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

    def dark_frac(box: tuple[int, int, int, int]) -> float:
        x, y, w, h = box
        interior = gray[y : y + h, x : x + w]
        return float((interior <= 110).mean()) if interior.size else 0.0

    def mask_fill(box: tuple[int, int, int, int]) -> float:
        x, y, w, h = box
        region = mask[y : y + h, x : x + w]
        return float((region > 0).mean()) if region.size else 0.0

    cands: list[tuple[float, tuple[int, int, int, int]]] = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if 0.17 * page_w < w < 0.36 * page_w and 0.03 * page_h < h < 0.07 * page_h and w / h < 5.5:
            # Two neighbouring boards can fuse into one wide blob
            # (their dark surrounds touch under a light product).
            # Split at the palest vertical valley in the middle span.
            profile = np.asarray((gray[y : y + h, x : x + w] <= 110).mean(axis=0), dtype=float)
            mid = profile[w // 4 : 3 * w // 4]
            if len(mid) and float(np.min(mid)) < 0.35:
                cut = w // 4 + int(np.argmin(mid))
                for half in ((x, y, cut, h), (x + cut, y, w - cut, h)):
                    hw = half[2]
                    if not (0.07 * page_w < hw < 0.17 * page_w and 1.3 < hw / h < 3.0):
                        continue
                    if mask_fill(half) < 0.40 or dark_frac(half) < 0.5:
                        continue
                    cands.append((mask_fill(half), half))
                continue
        if not (0.07 * page_w < w < 0.17 * page_w and 0.03 * page_h < h < 0.07 * page_h):
            continue
        if not (1.3 < w / h < 3.0):
            continue
        fill = cv2.contourArea(contour) / (w * h)
        if fill < 0.40:
            continue
        # A board's interior is solidly dark; a dense block of printed
        # name text (bold caps) also contours like a board but its box
        # is mostly pale page with dark strokes.
        if dark_frac((x, y, w, h)) < 0.5:
            continue
        cands.append((fill, (x, y, w, h)))
    boxes: list[tuple[int, int, int, int]] = []
    for _fill, box in sorted(cands, reverse=True):
        x, y, w, h = box
        overlap = False
        for bx, by, bw, bh in boxes:
            ix = max(0, min(x + w, bx + bw) - max(x, bx))
            iy = max(0, min(y + h, by + bh) - max(y, by))
            if ix * iy > 0.4 * min(w * h, bw * bh):
                overlap = True
                break
        if not overlap:
            boxes.append(box)
    return boxes


def _board_tokens(
    image: Image.Image, box: tuple[int, int, int, int], tag: str
) -> list[tuple[str, float, str]]:
    """OCR one chalkboard crop several ways; pool the tokens.

    The chalk digits are outline glyphs filled with hatching: plain
    OCR loses them. Fusing the hatch strokes with a morphological
    close (two kernel sizes) and reading with RapidOCR, plus one
    Tesseract read, gives partially-overlapping evidence; the parser
    votes across all of it. Returns (text, centre-x fraction, box tag)
    triples; the tag lets the parser trust the tightest box most.
    """
    import cv2
    import numpy as np

    x, y, w, h = box
    crop = image.crop((x, y, x + w, y + h))
    big = crop.resize((w * 4, h * 4), Image.Resampling.LANCZOS)
    tokens: list[tuple[str, float, str]] = []
    inverted = Image.fromarray(255 - np.array(big)).convert("RGB")
    for ln in detect_lines(inverted):
        tokens.append((ln.text, ln.cx / big.width, tag))
    gray = cv2.cvtColor(np.array(big), cv2.COLOR_RGB2GRAY)
    _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    for kernel in (9, 13, 17, 21):
        fused = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, np.ones((kernel, kernel), np.uint8))
        fused_img = Image.fromarray(255 - fused).convert("RGB")
        for ln in detect_lines(fused_img):
            tokens.append((ln.text, ln.cx / big.width, tag))
        if kernel == 17:
            text = ocr_crop_text(fused_img, (0, 0, fused_img.width, fused_img.height), psm=6)
            if text:
                tokens.append((text.replace("\n", " "), -1.0, tag))
    return tokens


def _parse_board_tokens(
    tokens: list[tuple[str, float, str]], box: tuple[int, int, int, int]
) -> PriceAnchor | None:
    """Vote the pooled board tokens into one price anchor.

    Multibuy boards print 'n/m$'; price boards print big dollar
    digits left, superscript cents right, '/lb' under the cents.
    Evidence weights: 4-digit merged runs count double (they carry
    dollars+cents together); Tesseract tokens (cx = -1) count half.
    A price needs a dollars figure and a cents figure; a lone cents
    read is not enough (a wrong price is worse than a missed board).
    """
    from collections import Counter

    def weight(cx: float) -> int:
        return 1 if cx < 0 else 2  # Tesseract reads count half

    unit: str | None = None
    for text, _cx, _tag in tokens:
        low = text.lower()
        if "kg" in low:
            unit = "kg"
        elif "100g" in low.replace(" ", "") or "/100" in low:
            unit = "100g"
        elif re.search(r"/\s*[1l]?b|^[1l]b$|^b$", low.strip()):
            unit = "lb"

    has_dollar = any("$" in text for text, _cx, _tag in tokens)
    pair_votes: Counter[tuple[int, float]] = Counter()
    count_votes: Counter[int] = Counter()
    total_votes: Counter[float] = Counter()
    lone_digits: list[tuple[int, float, int, str]] = []  # (digit, cx, weight, box tag)
    pair2: list[tuple[int, float, int]] = []  # slash-lost pairs (count, total, weight)
    for text, cx, tag in tokens:
        wgt = weight(cx)
        if re.search(r"/\s*100", text):
            continue  # '/100g' unit print is not a multibuy pair
        m = re.search(r"(\d{1,2})\s*/\s*(\d{1,2}(?:[.,]\d{2})?)", text)
        if m:
            total_f = float(m.group(2).replace(",", "."))
            pair_votes[(int(m.group(1)), total_f)] += wgt + (1 if "$" in text else 0)
            continue
        m = re.search(r"(\d{1,2})\s*/\s*$", text.strip())
        if m:
            count_votes[int(m.group(1))] += wgt
            continue
        digits = re.sub(r"\D", "", text)
        # A multibuy total read as a lone digit counts only from the
        # tighter boxes (the loosest crop imports neighbouring print)
        # and only in the board's right half, where the total prints.
        if len(digits) == 1 and tag in ("b1", "b2") and 0.35 < cx < 0.85:
            lone_digits.append((int(digits), cx, wgt, tag))
        elif len(digits) == 2 and "/" not in text and 0.2 < cx < 0.8:
            pair2.append((int(digits[0]), float(digits[1]), wgt))
    if pair_votes or count_votes or has_dollar:
        for count2, total2, wgt2 in pair2:
            pair_votes[(count2, total2)] += wgt2
    if pair_votes or (count_votes and has_dollar):
        if pair_votes:
            # The chalk '3' splits its votes across misreads (0/2/8/9),
            # so the winning total is the weighted median of all total
            # evidence (full pairs + lone total digits), not the
            # argmax; the count takes the mode.
            count = Counter(
                {c: sum(v for (cc, _t), v in pair_votes.items() if cc == c) for c, _t in pair_votes}
            ).most_common(1)[0][0]
            pool: Counter[float] = Counter()
            for (cc, tt), v in pair_votes.items():
                if cc == count:
                    pool[tt] += v
            # Lone total digits: the tight box counts at full weight;
            # the looser box counts only when it corroborates a digit
            # the tight box also read (it imports stray strokes).
            b1_seen = {d for d, _cx, _w, tg in lone_digits if tg == "b1"}
            for digit, _cx, wgt, tg in lone_digits:
                if tg == "b1" or digit in b1_seen:
                    pool[float(digit)] += wgt
            total_weights = sorted(pool.items())
            half = sum(w for _t, w in total_weights) / 2
            acc = 0.0
            total = total_weights[-1][0]
            for t, w in total_weights:
                acc += w
                if acc >= half:
                    total = t
                    break
            count_votes[count] += 2
            total_votes[total] += 2
        if count_votes and not total_votes:
            count = count_votes.most_common(1)[0][0]
            b1_seen = {d for d, _cx, _w, tg in lone_digits if tg == "b1"}
            for digit, cx, wgt, tg in lone_digits:
                if cx > 0.35 and (tg == "b1" or digit in b1_seen):
                    total_votes[float(digit)] += wgt
            if not total_votes or total_votes.most_common(1)[0][1] < 2:
                return None
            total = total_votes.most_common(1)[0][0]
        elif count_votes:
            count = count_votes.most_common(1)[0][0]
            total = total_votes.most_common(1)[0][0]
        else:
            return None
        if count < 2 or total <= 0:
            return None
        return PriceAnchor(
            value=round(total / count, 2),
            price_text=f"{count}/{total:g}$",
            box=(float(box[0]), float(box[1]), float(box[0] + box[2]), float(box[1] + box[3])),
            conf=0.8,
            multibuy=(count, float(total)),
            unit=unit,
        )

    dollar_votes: Counter[int] = Counter()
    primary_votes: Counter[int] = Counter()
    cents_votes: Counter[int] = Counter()
    separate_cents: Counter[int] = Counter()
    for text, cx, _tag in tokens:
        digits = re.sub(r"\D", "", text)
        if len(digits) == 2 and cx >= 0.5 and "/" not in text and "$" not in text:
            separate_cents[int(digits)] += weight(cx)
        elif len(digits) == 2 and cx < 0 and _tag == "b1":
            # A Tesseract full-crop read ('99%') is real cents evidence.
            separate_cents[int(digits)] += 1
    cents_mode = separate_cents.most_common(1)[0][0] if sum(separate_cents.values()) >= 4 else None
    run_all: Counter[tuple[int, int]] = Counter()
    run_primary: Counter[tuple[int, int]] = Counter()
    runs3: list[tuple[str, int]] = []
    for text, cx, _tag in tokens:
        wgt = weight(cx)
        digits = re.sub(r"\D", "", text)
        if "/" in text or "$" in text or not digits:
            continue
        if len(digits) == 4:
            dollar_votes[int(digits[:2])] += 2 * wgt
            primary_votes[int(digits[:2])] += 2 * wgt
            cents_votes[int(digits[2:])] += 2 * wgt
            run_all[(int(digits[:2]), int(digits[2:]))] += 2 * wgt
            run_primary[(int(digits[:2]), int(digits[2:]))] += 2 * wgt
        elif len(digits) == 3:
            runs3.append((digits, wgt))
        elif len(digits) == 2 and cx >= 0.5:
            cents_votes[int(digits)] += wgt
        elif len(digits) <= 2 and 0 <= cx < 0.5:
            # A 2-digit token equal to the cents mode, sitting centre
            # ('D99'), is the cents with a garbage prefix glyph, not
            # a dollars figure.
            if len(digits) == 2 and cents_mode is not None and int(digits) == cents_mode:
                continue
            dollar_votes[int(digits)] += wgt
            primary_votes[int(digits)] += wgt
        elif len(digits) == 1 and 0.4 <= cx < 0.65:
            # A lone dollar digit whose OCR line spanned the whole
            # board (the cents read as their own line elsewhere):
            # weak dollars evidence, half the usual weight.
            dollar_votes[int(digits)] += 1
            primary_votes[int(digits)] += 1
    # A 3-digit run is ambiguous: '149' can be $1.49 or $14.9x with
    # the two cents glyphs fused into one blob ('99' reads as a
    # single '9', '2', '0'...). Vote it both ways; the second reading
    # uses the separately-read cents as the cents figure.
    for digits, wgt in runs3:
        dollar_votes[int(digits[0])] += wgt
        primary_votes[int(digits[0])] += wgt
        cents_votes[int(digits[1:])] += wgt
        run_all[(int(digits[0]), int(digits[1:]))] += wgt
        run_primary[(int(digits[0]), int(digits[1:]))] += wgt
        if cents_mode is not None:
            dollar_votes[int(digits[:2])] += wgt
            cents_votes[cents_mode] += wgt
            run_all[(int(digits[:2]), cents_mode)] += wgt
    # A token that read the WHOLE price in one run ('1199', '899')
    # is the strongest evidence on the board: when full runs carry
    # enough weight, they decide the price outright and the fragment
    # votes (a split '11' read as five lone '1's) cannot swamp them.
    if run_all:
        (run_dollars, run_cents), run_weight = sorted(
            run_all.items(),
            key=lambda kv: (kv[1], run_primary.get(kv[0], 0)),
            reverse=True,
        )[0]
        if run_weight >= 4:
            # Same fused-cents trap as the fragment path: a '3999'
            # run can be '3.99' with the cents fused on twice.
            if (
                run_dollars >= 20
                and run_cents >= 90
                and run_dollars % 10 == run_cents // 10
                and dollar_votes.get(run_dollars // 10, 0) >= 2
            ):
                run_dollars //= 10
            return PriceAnchor(
                value=run_dollars + run_cents / 100,
                price_text=f"{run_dollars}.{run_cents:02d}",
                box=(float(box[0]), float(box[1]), float(box[0] + box[2]), float(box[1] + box[3])),
                conf=0.85,
                unit=unit,
            )
    if not cents_votes:
        return None
    # Cents-only boards ('99¢/lb') print the ¢ glyph; a dollars board
    # whose dollar digit was lost does not, and must stay unparsed
    # rather than collapse to the cents figure. The two cents glyphs
    # themselves read as lone '9' tokens, so junk dollars votes made
    # only of the cents digit (or 0) do not disqualify the board.
    junk_dollars_only = cents_mode is not None and all(
        d in (0, cents_mode // 10) for d in dollar_votes
    )
    if not dollar_votes or junk_dollars_only:
        if cents_mode is not None and any("¢" in t or "%" in t for t, _c, _g in tokens):
            return PriceAnchor(
                value=cents_mode / 100,
                price_text=f"{cents_mode}¢",
                box=(float(box[0]), float(box[1]), float(box[0] + box[2]), float(box[1] + box[3])),
                conf=0.8,
                unit=unit,
            )
        return None
    cents_ranked = sorted(
        cents_votes.items(), key=lambda kv: (kv[1], separate_cents.get(kv[0], 0)), reverse=True
    )
    cents = cents_ranked[0][0]
    dollars = sorted(
        dollar_votes.items(), key=lambda kv: (kv[1], primary_votes.get(kv[0], 0)), reverse=True
    )[0][0]
    # Pages with small superscript cents fuse the dollar digit with
    # the first cents glyph: '3.99' reads as dollars=39. When the
    # winning figure's second digit is the cents mode's first digit
    # and its first digit has real support of its own, the fused
    # reading is the true one.
    if dollars >= 20 and cents_mode is not None and dollars % 10 == cents_mode // 10:
        first = dollars // 10
        if dollar_votes.get(first, 0) * 2 >= dollar_votes[dollars]:
            dollars = first
    if cents_votes[cents] < 4 and not separate_cents:
        return None
    return PriceAnchor(
        value=dollars + cents / 100,
        price_text=f"{dollars}.{cents:02d}",
        box=(float(box[0]), float(box[1]), float(box[0] + box[2]), float(box[1] + box[3])),
        conf=0.8,
        unit=unit,
    )


def _min_cost_assignment(costs: list[list[float]]) -> list[tuple[int, int]]:
    """Min-cost bipartite assignment (Hungarian algorithm, O(n^3)).

    Rectangular input is padded to square with dummy nodes at cost
    ``_ASSIGN_DUMMY``; pairs landing on a dummy are dropped.
    """
    n = len(costs)
    m = len(costs[0]) if n else 0
    if n == 0 or m == 0:
        return []
    size = max(n, m)
    a = [[_ASSIGN_DUMMY] * (size + 1) for _ in range(size + 1)]
    for i in range(n):
        for j in range(m):
            a[i + 1][j + 1] = costs[i][j]
    u = [0.0] * (size + 1)
    v = [0.0] * (size + 1)
    p = [0] * (size + 1)
    way = [0] * (size + 1)
    for i in range(1, size + 1):
        p[0] = i
        j0 = 0
        minv = [float("inf")] * (size + 1)
        used = [False] * (size + 1)
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = float("inf")
            j1 = 0
            for j in range(1, size + 1):
                if used[j]:
                    continue
                cur = a[i0][j] - u[i0] - v[j]
                if cur < minv[j]:
                    minv[j] = cur
                    way[j] = j0
                if minv[j] < delta:
                    delta = minv[j]
                    j1 = j
            for j in range(size + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while j0:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
    return [(p[j] - 1, j - 1) for j in range(1, size + 1) if 0 < p[j] <= n and j <= m]


_ASSIGN_DUMMY = 700.0
_ASSIGN_BIG = 1e7


def _levenshtein(a: str, b: str) -> int:
    """Edit distance, early-exit above 2 (only small distances matter)."""
    if abs(len(a) - len(b)) > 2:
        return 3
    row = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        new = [i]
        best = i
        for j, cb in enumerate(b, start=1):
            v = min(row[j] + 1, new[j - 1] + 1, row[j - 1] + (ca != cb))
            new.append(v)
            best = min(best, v)
        if best > 2:
            return 3
        row = new
    return row[-1]


def _name_blocks(
    image: Image.Image, lines: list[OcrLine], cfg: OcrStoreConfig
) -> list[tuple[tuple[float, float, float, float], list[OcrLine]]]:
    """Cluster name-candidate lines into blocks (stacked lines that
    x-overlap, or lines sharing a text row). A block must sit on the
    page's white background — name blocks do; packaging print and
    wooden signs do not — which keeps product-label text out."""
    import cv2
    import numpy as np

    page_w, page_h = image.size
    hsv_full = cv2.cvtColor(np.array(image.convert("RGB")), cv2.COLOR_RGB2HSV)

    def line_is_pale(ln: OcrLine) -> bool:
        x0, y0 = max(0, int(ln.x) - 2), max(0, int(ln.y) - 2)
        x1, y1 = min(page_w, int(ln.right) + 2), min(page_h, int(ln.bottom) + 2)
        region = hsv_full[y0:y1, x0:x1]
        if region.size == 0:
            return False
        pale = ((region[:, :, 2] >= 175) & (region[:, :, 1] <= 75)).mean()
        return bool(pale >= 0.45)

    cands = [
        ln for ln in _dedupe_candidates(name_candidates(lines, page_h, cfg)) if line_is_pale(ln)
    ]
    parent = list(range(len(cands)))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    max_gap = cfg.block_y_gap_frac * page_h
    for i, a in enumerate(cands):
        for j, b in enumerate(cands):
            if j <= i:
                continue
            y_gap = max(b.y - a.bottom, a.y - b.bottom)
            x_overlap = min(a.right, b.right) - max(a.x, b.x)
            y_overlap = min(a.bottom, b.bottom) - max(a.y, b.y)
            x_gap = max(b.x - a.right, a.x - b.right)
            stacked = y_gap <= max_gap and x_overlap > 0.1 * min(a.w, b.w)
            same_row = y_overlap > 0.5 * min(a.h, b.h) and x_gap <= 0.015 * page_w
            if stacked or same_row:
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
    groups: dict[int, list[OcrLine]] = {}
    for i, line in enumerate(cands):
        groups.setdefault(find(i), []).append(line)

    hsv = cv2.cvtColor(np.array(image.convert("RGB")), cv2.COLOR_RGB2HSV)
    blocks: list[tuple[tuple[float, float, float, float], list[OcrLine]]] = []
    for members in groups.values():
        alpha = sum(1 for ln in members for c in ln.text if c.isalpha())
        longest = max((len(re.sub(r"[^A-Za-zÀ-ÿ]", "", ln.text)) for ln in members), default=0)
        if alpha < 10 or longest < 8:
            continue  # sign fragments and stray label words, not names
        if len(members) == 1:
            # A lone line that (fuzzily) just says "biologique" is one
            # of the wooden signs hung on the photos, not a name.
            squashed = re.sub(r"[^a-z]", "", members[0].text.lower())
            if _levenshtein(squashed, "biologique") <= 2 or _levenshtein(
                squashed, "biologiques"
            ) <= 2:
                continue
        members.sort(key=lambda z: (z.y, z.x))
        box = (
            min(ln.x for ln in members),
            min(ln.y for ln in members),
            max(ln.right for ln in members),
            max(ln.bottom for ln in members),
        )
        if box[2] - box[0] < 0.07 * page_w:
            continue  # bottle-label fragments, narrower than any name
        x0, y0, x1, y1 = (int(box[0]), int(box[1]), int(box[2]), int(box[3]))
        region = hsv[y0:y1, x0:x1]
        if region.size == 0:
            continue
        # PA's page is cream linen, not white: pale + desaturated.
        near_white = ((region[:, :, 2] >= 175) & (region[:, :, 1] <= 75)).mean()
        if near_white < 0.45:
            continue
        blocks.append((box, members))
    return blocks


def _segment_chalkboard(
    image: Image.Image,
    lines: list[OcrLine],
    cfg: OcrStoreConfig,
    page_url: str,
    page_number: int,
) -> list[FlyerItem]:
    """PA Nature: prices live on printed chalkboards (hatched chalk
    digits) that page-level OCR cannot read. Detect the boards by
    colour, OCR each board crop with fused-stroke variants, and vote
    the reads into price anchors. Pairing anchors to name blocks is
    a global min-cost assignment: greedy nearest-neighbour claiming
    swaps names here (the almonds name sits closer to the beef
    board than to its own), but the global optimum does not."""
    # The board voting is tuned at the source's native width
    # (flyerbox serves 1550px); the fetch pipeline upscales pages to
    # 2000px, which changes the OCR token pool enough to flip votes.
    # Pin the working scale so production matches the tuning.
    if image.size[0] > 1700:
        factor = 1550 / image.size[0]
        image = image.resize(
            (1550, round(image.size[1] * factor)), Image.Resampling.LANCZOS
        )
        lines = [
            OcrLine(
                x=ln.x * factor,
                y=ln.y * factor,
                w=ln.w * factor,
                h=ln.h * factor,
                text=ln.text,
                conf=ln.conf,
            )
            for ln in lines
        ]
    page_w, page_h = image.size
    cores = _detect_board_boxes(image, vmax=60)
    loose = _detect_board_boxes(image, vmax=110)
    anchors: list[PriceAnchor] = []
    for core in cores:
        x, y, w, h = core
        ew, eh = int(w * 1.10), int(h * 1.24)
        box1 = (x - (ew - w) // 2, y - (eh - h) // 2, ew, eh)
        tokens = _board_tokens(image, box1, "b1")
        partner = next(
            (
                lb
                for lb in loose
                if abs(lb[0] - x) < 0.03 * page_w
                and abs(lb[1] - y) < 0.03 * page_h
                and lb[2] < 1.6 * w
                and lb[3] < 1.6 * h
            ),
            core,
        )
        pw, ph = int(partner[2] * 1.30), int(partner[3] * 1.42)
        box2 = (
            partner[0] - (pw - partner[2]) // 2,
            partner[1] - (ph - partner[3]) // 2,
            pw,
            ph,
        )
        if box2 != box1:
            tokens += _board_tokens(image, box2, "b2")
        qw, qh = int(partner[2] * 1.15), int(partner[3] * 1.15)
        box3 = (
            partner[0] - (qw - partner[2]) // 2,
            partner[1] - (qh - partner[3]) // 2,
            qw,
            qh,
        )
        if box3 != box1 and box3 != box2:
            tokens += _board_tokens(image, box3, "b3")
        anchor = _parse_board_tokens(tokens, box1)
        if anchor is not None:
            anchors.append(anchor)
    blocks = _name_blocks(image, lines, cfg)
    if not anchors or not blocks:
        return []
    cap = 0.45 * page_w

    def pair_cost(anchor: PriceAnchor, block_box: tuple[float, float, float, float]) -> float:
        dist = _match_dist(anchor.box, block_box, cfg.match_dx_weight)
        anchor_cy = (anchor.box[1] + anchor.box[3]) / 2
        block_cy = (block_box[1] + block_box[3]) / 2
        # PA layout: the name prints in the upper part of the product
        # cell, the board in the lower part — a block centred below
        # its board is the NEXT row's name, never this product's.
        if dist > cap or block_cy > anchor_cy + 0.02 * page_h:
            return _ASSIGN_BIG
        if abs(block_cy - anchor_cy) > 0.21 * page_h:
            return _ASSIGN_BIG
        return dist

    costs = [[pair_cost(anchor, block_box) for block_box, _m in blocks] for anchor in anchors]
    items: list[FlyerItem] = []
    for ai, bi in _min_cost_assignment(costs):
        if costs[ai][bi] >= _ASSIGN_BIG:
            continue
        anchor = anchors[ai]
        block_box, members = blocks[bi]
        block_text = ocr_crop_text(
            image,
            (int(block_box[0]), int(block_box[1]), int(block_box[2]), int(block_box[3])),
            psm=cfg.tesseract_psm,
        )
        if cfg.name_case == "any":
            name = _name_from_lines_any(members)
        else:
            name = _name_from_text(block_text, members)
        if not name:
            continue
        region = (
            min(anchor.box[0], block_box[0]),
            min(anchor.box[1], block_box[1]),
            max(anchor.box[2], block_box[2]),
            max(anchor.box[3], block_box[3]),
        )
        conditions: dict[str, object] = {}
        if anchor.multibuy:
            count, total = anchor.multibuy
            conditions["multibuy"] = {"count": count, "total": total}
        items.append(
            FlyerItem(
                name_fr=name,
                price_text=anchor.price_text,
                price_value=anchor.value,
                price_unit=anchor.unit,
                image_url=page_url,
                bbox={
                    "left": round(region[0] / page_w * 1000),
                    "top": round(region[1] / page_h * 1000),
                    "right": round(region[2] / page_w * 1000),
                    "bottom": round(region[3] / page_h * 1000),
                    "page": page_number,
                },
                conditions=conditions,
                languages=["fr"],
                raw={"strategy": "chalkboard", "block_text": block_text},
                confidence=round(min(anchor.conf, 0.99), 2),
            )
        )
    return items


def _tess_mask_text(mask_img: Image.Image, psm: int) -> str:
    """Tesseract on a pre-binarized crop (black ink on white)."""
    import io
    import os
    import subprocess

    from .engine import find_tesseract

    found = find_tesseract()
    if found is None:
        return ""
    binary, extra_env = found
    buf = io.BytesIO()
    mask_img.save(buf, format="PNG")
    env = dict(os.environ)
    env.update(extra_env)
    try:
        proc = subprocess.run(
            [binary, "stdin", "stdout", "--psm", str(psm),
             "-c", "tessedit_char_whitelist=0123456789/$%."],
            input=buf.getvalue(), capture_output=True, env=env, timeout=30,
        )
    except (subprocess.SubprocessError, OSError):
        return ""
    return proc.stdout.decode("utf-8", errors="replace").strip()


def _red_clusters(image: Image.Image) -> list[list[tuple[int, int, int, int]]]:
    """Group red glyph blobs into price clusters (Frutta Si layout).

    Prices print as big red digits (dollars full height, cents
    superscript right) on a yellow page. Red connected components of
    glyph size, clustered by baseline overlap + horizontal gap, give
    one cluster per printed price — immune to the black per-kg
    reference print and name text that poisoned line-based anchors.
    """
    import cv2
    import numpy as np

    arr = np.array(image.convert("RGB"))
    page_h, page_w = arr.shape[:2]
    hsv = cv2.cvtColor(arr, cv2.COLOR_RGB2HSV)
    mask = (
        ((hsv[..., 0] <= 12) | (hsv[..., 0] >= 168))
        & (hsv[..., 1] >= 100)
        & (hsv[..., 2] >= 70)
    ).astype(np.uint8)
    n, _lab, stats, _cent = cv2.connectedComponentsWithStats(mask * 255, connectivity=8)
    blobs: list[tuple[int, int, int, int]] = []
    for i in range(1, n):
        x, y, w, h, area = (int(v) for v in stats[i])
        fill = area / (w * h) if w * h else 0.0
        # Glyph ink fills 25-92% of its box; photo regions and label
        # bars are near-solid and drop out here.
        if (
            6 <= h <= 0.035 * page_h
            and 3 <= w <= 0.06 * page_w
            and area >= 25
            and 0.25 <= fill <= 0.92
        ):
            blobs.append((x, y, w, h))
    blobs.sort(key=lambda b: (b[1], b[0]))
    parent = list(range(len(blobs)))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i in range(len(blobs)):
        for j in range(i + 1, len(blobs)):
            a, b = blobs[i], blobs[j]
            vov = min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1])
            gap = max(b[0] - (a[0] + a[2]), a[0] - (b[0] + b[2]))
            if vov > 0.35 * min(a[3], b[3]) and gap < 0.031 * page_w:
                parent[find(i)] = find(j)
    groups: dict[int, list[tuple[int, int, int, int]]] = {}
    for i, b in enumerate(blobs):
        groups.setdefault(find(i), []).append(b)
    out: list[list[tuple[int, int, int, int]]] = []
    for g in groups.values():
        y0 = min(b[1] for b in g)
        y1 = max(b[1] + b[3] for b in g)
        if len(g) >= 2 and (y1 - y0) >= 0.011 * page_h:
            out.append(sorted(g, key=lambda b: b[0]))
    out.sort(key=lambda g: (min(b[1] for b in g), min(b[0] for b in g)))
    return out


def _mask_crop(mask: Any, blobs: list[tuple[int, int, int, int]], pad: int = 3) -> Image.Image:
    import numpy as np

    x0 = max(0, min(b[0] for b in blobs) - pad)
    y0 = max(0, min(b[1] for b in blobs) - pad)
    x1 = max(b[0] + b[2] for b in blobs) + pad
    y1 = max(b[1] + b[3] for b in blobs) + pad
    ink = mask[y0:y1, x0:x1]
    img = Image.fromarray(((1 - ink) * 255).astype(np.uint8))
    return img.resize((img.width * 6, img.height * 6), Image.Resampling.LANCZOS)


def _split_wide_blob(
    mask: Any, blob: tuple[int, int, int, int]
) -> list[tuple[int, int, int, int]]:
    """Split a fused two-digit blob at its palest vertical valley."""
    import numpy as np

    x, y, w, h = blob
    ink = mask[y : y + h, x : x + w]
    col = ink.sum(axis=0)
    lo, hi = w // 4, (3 * w) // 4
    if hi <= lo:
        return [blob]
    cut = lo + int(np.argmin(col[lo:hi]))
    if col[cut] > 0.35 * h:
        return [blob]
    return [(x, y, cut, h), (x + cut, y, w - cut, h)]


def _read_digit_group(
    mask: Any, blobs: list[tuple[int, int, int, int]], page_w: int
) -> dict[str, int]:
    """Voted digit-string candidates for one glyph group.

    Sources: whole-group Tesseract crops (psm 7/8), a per-blob
    concatenation, and — for an over-wide blob, two fused digits —
    a valley-split interpretation alongside the unsplit one. Reads
    of any length 1-2 are kept with their vote weights; the caller
    assembles dollars/cents pairs from the cross product, so an
    ambiguous group length does not kill a good read.
    """
    votes: dict[str, int] = {}

    def add(s: str, wgt: int) -> None:
        if 1 <= len(s) <= 2:
            votes[s] = votes.get(s, 0) + wgt

    group_img = _mask_crop(mask, blobs)
    for psm in (7, 8):
        add(re.sub(r"\D", "", _tess_mask_text(group_img, psm)), 2)

    def per_blob(pieces: list[tuple[int, int, int, int]]) -> str:
        out = []
        for p in pieces:
            d = re.sub(r"\D", "", _tess_mask_text(_mask_crop(mask, [p]), 10))
            if not d:
                d = re.sub(r"\D", "", _tess_mask_text(_mask_crop(mask, [p]), 8))
            out.append(d[:1] if d else "")
        return "".join(out) if all(len(d) == 1 for d in out) else ""

    add(per_blob(blobs), 2)
    wide = [b for b in blobs if b[2] >= 0.04 * page_w]
    if wide:
        pieces: list[tuple[int, int, int, int]] = []
        for b in blobs:
            pieces.extend(_split_wide_blob(mask, b) if b in wide else [b])
        if len(pieces) > len(blobs):
            add(per_blob(pieces), 1)
    return votes


def _pick_digits(votes: dict[str, int]) -> str | None:
    """Most-voted candidate; None on a tie (wrong price is worse)."""
    if not votes:
        return None
    best = max(votes.values())
    winners = [c for c, n in votes.items() if n == best]
    return winners[0] if len(winners) == 1 else None


_PER_KG_RE = re.compile(r"(\d{1,3})[.,](\d{2,3})\s*/\s*kg", re.IGNORECASE)
_MULTIBUY_RE = re.compile(r"(\d{1,2})\s*/\s*(\d{1,2}(?:[.,]\d{2})?)")


def _segment_red_grid(
    image: Image.Image,
    lines: list[OcrLine],
    cfg: OcrStoreConfig,
    page_url: str,
    page_number: int,
) -> list[FlyerItem]:
    """Frutta Si: red price clusters as anchors, names from lines.

    The dense grid defeated line-based anchors (per-kg reference
    print formed rival anchors and names paired one slot off). Red
    glyph clusters are unambiguous; the printed per-kg reference
    under each /lb price validates the read (price x 2.2046).
    """
    import cv2
    import numpy as np

    page_w, page_h = image.size
    arr = np.array(image.convert("RGB"))
    hsv = cv2.cvtColor(arr, cv2.COLOR_RGB2HSV)
    mask = (
        ((hsv[..., 0] <= 12) | (hsv[..., 0] >= 168))
        & (hsv[..., 1] >= 100)
        & (hsv[..., 2] >= 70)
    ).astype(np.uint8)

    def kg_ref(box: tuple[float, float, float, float]) -> float | None:
        for ln in lines:
            # The reference prints under the price, but OCR may merge
            # it into the price's own line; any line overlapping the
            # price band vertically counts.
            spans = ln.bottom > box[1] and ln.y <= box[3] + 0.02 * page_h
            if spans and ln.x < box[2] and ln.right > box[0]:
                m = _PER_KG_RE.search(ln.text)
                if m:
                    return float(f"{m.group(1)}.{m.group(2)}")
        return None

    def unit_for(box: tuple[float, float, float, float]) -> str | None:
        found: set[str] = set()
        for ln in lines:
            if ln.y >= box[3] + 0.014 * page_h or ln.bottom <= box[1] - 0.004 * page_h:
                continue
            if ln.x > box[2] + 0.07 * page_w or ln.right < box[0] - 4:
                continue
            # 'lb' misread by OCR as 'Ib' / '1b' (the price font's l).
            if re.search(r"(?<![a-zA-Z])[iIl1]b(?![a-zA-Z])", ln.text):
                found.add("lb")
                continue
            if _PER_KG_RE.search(ln.text):
                if re.search(r"\blb\b", ln.text, re.IGNORECASE):
                    found.add("lb")
                continue
            unit = _unit_in_text(ln.text)
            if unit and unit != "kg":
                found.add(unit)
        if "lb" in found:
            return "lb"
        if "100g" in found:
            return "100g"
        return None

    def line_fragments(
        box: tuple[float, float, float, float],
    ) -> tuple[dict[str, int], dict[str, int], dict[tuple[str, str], int]]:
        """Digit votes from the page OCR lines overlapping a cluster.

        RapidOCR reads the big price glyphs well at page level; its
        lines carry the dollars, the cents, or a fused run ('1099').
        Position maps a short run to its side; a fused run votes as
        a (dollars, cents) pair. Per-kg reference lines are excluded
        (they belong to kg_ref, and their digits would poison votes).
        """
        d_votes: dict[str, int] = {}
        c_votes: dict[str, int] = {}
        pair_votes: dict[tuple[str, str], int] = {}
        mid = box[0] + 0.45 * (box[2] - box[0])
        for ln in lines:
            # The line's centre must sit in the glyph band: packaging
            # print just above the price ('156ml' on a can) otherwise
            # leaks digit runs into the cents votes.
            if not (box[1] - 0.002 * page_h <= ln.cy <= box[3] + 0.006 * page_h):
                continue
            if ln.x > box[2] + 0.02 * page_w or ln.right < box[0] - 0.012 * page_w:
                continue
            text = _PER_KG_RE.sub(" ", ln.text)
            if "/" in text:
                continue
            for run in re.findall(r"\d+", text):
                if len(run) >= 3:
                    for k in (1, 2):
                        if len(run) - k == 2:
                            d, c = run[:k], run[k:]
                            d_votes[d] = d_votes.get(d, 0) + 1
                            c_votes[c] = c_votes.get(c, 0) + 1
                            pair_votes[(d, c)] = pair_votes.get((d, c), 0) + 1
                elif ln.cx < mid:
                    d_votes[run] = d_votes.get(run, 0) + 1
                else:
                    c_votes[run] = c_votes.get(run, 0) + 1
        return d_votes, c_votes, pair_votes

    anchors: list[PriceAnchor] = []
    multibuy_clusters: list[tuple[tuple[int, int, int, int], int, float]] = []
    cluster_list = _red_clusters(image)
    cluster_boxes = [
        (min(b[0] for b in g), min(b[1] for b in g)) for g in cluster_list
    ]
    for blobs in cluster_list:
        x0 = min(b[0] for b in blobs)
        y0 = min(b[1] for b in blobs)
        x1 = max(b[0] + b[2] for b in blobs)
        y1 = max(b[1] + b[3] for b in blobs)
        box = (float(x0), float(y0), float(x1), float(y1))
        whole = _tess_mask_text(_mask_crop(mask, blobs), 6) + " " + _tess_mask_text(
            _mask_crop(mask, blobs), 11
        )
        mb = _MULTIBUY_RE.search(whole)
        max_h = max(b[3] for b in blobs)
        base = max(b[1] + b[3] for b in blobs)
        tall_top = min(b[1] for b in blobs if b[3] >= 0.78 * max_h)
        tall = [b for b in blobs if b[3] >= 0.78 * max_h and base - (b[1] + b[3]) <= 4]
        # Cents glyphs sit superscript: top near the dollars' top,
        # bottom well above the baseline. Other short blobs (photo
        # labels bleeding into the cluster) fail one of the two tests.
        short = [
            b
            for b in blobs
            if b not in tall
            and b[1] <= tall_top + 0.55 * max_h
            and b[1] + b[3] <= base - 0.12 * max_h
        ]
        short.sort(key=lambda b: b[0])
        if len(short) > 2:
            short = sorted(short, key=lambda b: b[1])[:2]
            short.sort(key=lambda b: b[0])
        if not tall:
            continue
        d_votes = _read_digit_group(mask, tall, page_w)
        c_votes = _read_digit_group(mask, short, page_w) if short else {}
        ld, lc, lp = line_fragments(box)
        for k, v in ld.items():
            d_votes[k] = d_votes.get(k, 0) + v
        for k, v in lc.items():
            c_votes[k] = c_votes.get(k, 0) + v
        # RapidOCR on the cropped cluster (the price glyphs at 3x):
        # a third read source, position-mapped like the page lines.
        crop = image.crop(
            (max(0, x0 - 4), max(0, y0 - 4), min(page_w, x1 + 4), min(page_h, y1 + 4))
        ).resize(((x1 - x0 + 8) * 3, (y1 - y0 + 8) * 3), Image.Resampling.LANCZOS)
        crop_mid = crop.width * (0.45 * (x1 - x0) + 4) / (x1 - x0 + 8)
        crop_lb = False
        for ln in detect_lines(crop):
            if re.search(r"(?<![a-zA-Z])[iIl1]b(?![a-zA-Z])", ln.text):
                crop_lb = True
            text = _PER_KG_RE.sub(" ", ln.text)
            if "/" in text:
                continue
            for run in re.findall(r"\d+", text):
                if len(run) >= 3:
                    for split_at in (1, 2):
                        if len(run) - split_at == 2:
                            d, c = run[:split_at], run[split_at:]
                            d_votes[d] = d_votes.get(d, 0) + 1
                            c_votes[c] = c_votes.get(c, 0) + 1
                            lp[(d, c)] = lp.get((d, c), 0) + 1
                elif ln.cx < crop_mid:
                    d_votes[run] = d_votes.get(run, 0) + 2
                else:
                    c_votes[run] = c_votes.get(run, 0) + 2
        # Narrow-blob prior: in this price font only '1' is a thin
        # vertical bar (~12px vs 22-27px for other digits), and OCR
        # engines systematically drop it as a rule line. A tall group
        # of nothing but narrow bars can only read as ones.
        if tall and all(b[2] <= 0.017 * page_w for b in tall):
            ones = "1" * len(tall)
            d_votes[ones] = d_votes.get(ones, 0) + 3
        ref = kg_ref(box)
        value: float | None = None
        pairs = {
            (d, c): d_votes[d] + c_votes[c] + 2 * lp.get((d, c), 0)
            for d in d_votes
            for c in c_votes
            if len(c) == 2 and 1 <= len(d) <= 2 and int(d) <= 30
        }
        if pairs:
            if ref is not None:
                matching = [
                    p for p in pairs if abs((int(p[0]) + int(p[1]) / 100) * 2.2046 - ref) <= 0.06
                ]
                if len(matching) == 1:
                    d_win, c_win = matching[0]
                    value = int(d_win) + int(c_win) / 100
                elif len(matching) > 1:
                    d_win, c_win = max(matching, key=lambda p: pairs[p])
                    value = int(d_win) + int(c_win) / 100
                else:
                    # No voted pair fits the reference (the cents
                    # glyphs flip 9->6 in every engine on some
                    # prices): trust the reference when its dollars
                    # agree with a voted dollars read.
                    implied = round(ref / 2.2046 * 100)
                    imp_pair = (str(implied // 100), f"{implied % 100:02d}")
                    if imp_pair[0] in d_votes:
                        value = implied / 100
            if value is None:
                best = max(pairs.values())
                winners = [p for p, s in pairs.items() if s == best]
                if len(winners) > 1:
                    # Tie-break: a pair some engine read as one fused
                    # run ('1099') beats independently-voted halves.
                    top = max(lp.get(p, 0) for p in winners)
                    winners = [p for p in winners if lp.get(p, 0) == top]
                if len(winners) == 1 and best >= 3:
                    d_win, c_win = winners[0]
                    value = int(d_win) + int(c_win) / 100
        elif (
            (
                (len(short) == 1 and short[0][2] <= 0.016 * page_w)
                or (
                    not short
                    and any(b[2] <= 0.016 * page_w for b in blobs if b not in tall)
                )
            )
            and not any(
                len(s) == 2 and s != _pick_digits({k: v for k, v in d_votes.items() if len(k) == 2})
                for s in c_votes
            )
        ):
            # Cents-only price ('69¢'): the tall digits are the cents
            # and the single narrow short blob is the ¢ glyph itself.
            # A 'cents' vote equal to the dollars read is the same
            # glyphs seen twice (a line spanning the whole price),
            # not independent cents evidence.
            cand = {s: v for s, v in d_votes.items() if len(s) == 2}
            picked = _pick_digits(cand)
            if ref is not None:
                implied = round(ref / 2.2046 * 100)
                implied_s = f"{implied:02d}"
                if implied_s in cand:
                    value = implied / 100
                else:
                    near = [
                        s
                        for s in cand
                        if sum(a != b for a, b in zip(s, implied_s, strict=True)) == 1
                    ]
                    if len(near) == 1:
                        value = implied / 100
            elif picked is not None:
                value = int(picked) / 100
        if (
            value is None
            and ref is not None
            and len(tall) == 1
            and not any(int(k) <= 30 for k in d_votes)
        ):
            # Single unreadable dollar glyph (fused with the photo
            # above it) but a clean per-kg reference whose implied
            # cents are corroborated by a cents read: the reference
            # determines the dollars (ref = $/lb x 2.2046). A second
            # cluster in the same column just below means this blob
            # is label noise above the real price — no rescue then.
            implied = round(ref / 2.2046 * 100)
            imp_cents = f"{implied % 100:02d}"
            below = any(
                abs(bx - x0) <= 0.05 * page_w and 0 < by - y0 <= 0.045 * page_h
                for bx, by in cluster_boxes
                if (bx, by) != (x0, y0)
            )
            if not below and any(k[:1] == imp_cents[:1] for k in c_votes):
                value = implied / 100
        if value is None:
            if mb and int(mb.group(1)) >= 2:
                multibuy_clusters.append(
                    ((x0, y0, x1, y1), int(mb.group(1)), float(mb.group(2).replace(",", ".")))
                )
            continue
        anchors.append(
            PriceAnchor(
                value=value,
                price_text=f"{value:.2f}",
                box=box,
                conf=0.9,
                unit=unit_for(box) or ("lb" if crop_lb else None),
            )
        )
    # Attach multibuy clusters to the main price at their left.
    for (mx0, my0, mx1, my1), count, total in multibuy_clusters:
        host = None
        for a in anchors:
            if (
                abs(a.box[1] - my0) <= 0.012 * page_h
                and 0 < mx0 - a.box[2] <= 0.17 * page_w
                and (host is None or a.box[2] > host.box[2])
            ):
                host = a
        if host is not None and count >= 2 and total > 0:
            host.multibuy = (count, total)
        elif count >= 2 and total > 0:
            anchors.append(
                PriceAnchor(
                    value=total / count,
                    price_text=f"{count}/{total:g}$",
                    box=(float(mx0), float(my0), float(mx1), float(my1)),
                    conf=0.85,
                    multibuy=(count, total),
                )
            )
    anchors.sort(key=lambda a: (a.box[1], a.box[0]))
    return _items_from_anchors(image, lines, cfg, anchors, page_url, page_number)


def _segment_prix_line(
    image: Image.Image,
    lines: list[OcrLine],
    cfg: OcrStoreConfig,
    page_url: str,
    page_number: int,
) -> list[FlyerItem]:
    """Costco-style: price from 'Prix X,XX $' lines, name from the cell above."""
    page_w, page_h = image.size
    patterns = DEFAULT_STOPLIST + cfg.stoplist
    items: list[FlyerItem] = []
    labels = [ln for ln in lines if ln.text.strip().lower() == "prix"]
    amount_lines = [
        ln for ln in lines if _AMOUNT_RE.search(ln.text) and not ln.text.strip().startswith("-")
    ]
    all_amounts = [ln for ln in lines if _AMOUNT_RE.search(ln.text)]
    # Column tops for the name band: a cell's name lines lie between
    # the previous same-column 'Prix' label and this one. The old
    # fixed 30%-of-page band reached 2-3 cells up on tall coupon
    # pages and merged neighbouring products into one name.
    labels_by_col: dict[int, list[OcrLine]] = {}
    for lab in labels:
        labels_by_col.setdefault(round(lab.x / (0.05 * page_w)), []).append(lab)
    band_top_of: dict[int, float] = {}
    for col_labels in labels_by_col.values():
        prev_bottom: float | None = None
        for lab in sorted(col_labels, key=lambda z: z.y):
            band_top_of[id(lab)] = (
                prev_bottom if prev_bottom is not None else lab.y - 0.30 * page_h
            )
            prev_bottom = lab.bottom
    derived = False
    for label in labels:
        row = [
            a
            for a in amount_lines
            if abs(a.cy - label.cy) < 0.01 * page_h
            and label.x < a.x <= label.x + 0.27 * page_w
        ]
        derived = False
        if row:
            amount = min(row, key=lambda a: abs(a.cy - label.cy))
            m = _AMOUNT_RE.search(amount.text)
            if not m:
                continue
            value = int(m.group(1).replace(" ", "")) + int(m.group(2)) / 100
        else:
            # The Prix amount itself was garbled: derive it from the
            # "En entrepot" amount minus the "Economie" amount above.
            # Amounts are right-aligned inside the cell (label is at left).
            above = sorted(
                (
                    a
                    for a in all_amounts
                    if label.x - 0.02 * page_w <= a.x <= label.x + 0.27 * page_w
                    and label.y - 0.05 * page_h <= a.y < label.y
                ),
                key=lambda a: a.y,
            )
            if len(above) < 2:
                continue
            vals: list[float] = []
            for a in above[-2:]:
                mm = _AMOUNT_RE.search(a.text)
                if not mm:
                    vals = []
                    break
                vals.append(int(mm.group(1).replace(" ", "")) + int(mm.group(2)) / 100)
            if len(vals) != 2 or vals[0] <= vals[1]:
                continue
            value = round(vals[0] - vals[1], 2)
            amount = above[-1]
            derived = True
        band_x0, band_x1 = label.x - 0.02 * page_w, amount.right + 0.02 * page_w
        band_top = band_top_of.get(id(label), label.y - 0.30 * page_h)
        cands = [
            ln
            for ln in lines
            if band_x0 <= ln.cx <= band_x1
            and band_top <= ln.y < label.y
            and len([c for c in ln.text if c.isalpha()]) >= 4
            and not _stop_match(ln.text, patterns)
            and not _AMOUNT_RE.search(ln.text)
        ]
        if not cands:
            continue
        cands.sort(key=lambda z: z.y)
        name_lines = [ln.text.strip() for ln in cands if len(ln.text.strip()) > 12]
        if not name_lines:
            name_lines = [max(cands, key=lambda z: len(z.text)).text.strip()]
        name = re.sub(r"\s+", " ", " ".join(name_lines[:3])).strip()
        if not name:
            continue
        region = (
            min([label.x] + [ln.x for ln in cands]),
            min(ln.y for ln in cands),
            amount.right,
            amount.bottom,
        )
        items.append(
            FlyerItem(
                name_fr=name,
                price_text=f"{value:.2f}".replace(".", ",") + " $",
                price_value=value,
                image_url=page_url,
                bbox={
                    "left": round(region[0] / page_w * 1000),
                    "top": round(region[1] / page_h * 1000),
                    "right": round(region[2] / page_w * 1000),
                    "bottom": round(region[3] / page_h * 1000),
                    "page": page_number,
                },
                languages=["fr"],
                raw={"strategy": "prix_line", "price_derived": derived},
                confidence=0.7 if derived else 0.85,
            )
        )
    return items
