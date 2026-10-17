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

from PIL import Image

from ..sources.base import FlyerItem
from .engine import OcrLine, ocr_crop_text

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

    price_strategy: str = "anchor"  # "anchor" | "prix_line" | "name_cells"
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


def _name_from_text(block_text: str | None, fallback_lines: list[OcrLine]) -> str:
    """Product name: leading all-caps run of the clean block text.

    Falls back to the detected lines when the re-OCR text shares no token
    with them (its crop picked up a neighbouring badge or photo text).
    """
    fallback = "\n".join(ln.text for ln in fallback_lines)
    source = block_text if block_text else fallback
    name_lines: list[str] = []
    for raw in source.splitlines():
        line = raw.strip()
        if not line:
            continue
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
    anchors = find_price_anchors(lines, page_w, page_h, cfg)
    cands = _dedupe_candidates(name_candidates(lines, page_h, cfg))
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
            name = _name_from_text(block_text, grown)
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
