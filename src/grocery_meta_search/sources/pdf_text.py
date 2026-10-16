"""Parse a flyer PDF's text layer into individual items.

Built for flyers laid out as a regular product grid where each cell
carries a big display price: a large-font dollar span with a smaller
cents span beside it (Akhavan's weekly flyer is the reference case —
36 cells in a 6x6 grid). Prices anchor the grid: cluster the price
spans, derive rows and columns from the anchor centers, then
assemble each cell's name from the small-font spans inside it.

This beats OCR for such flyers on every axis: exact names, exact
prices, and no merged cells. It is deliberately store-shaped, not
universal (per the project owner's direction): the knobs are the
minimum price font size and the pairing tolerances.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date
from typing import Any

from .base import FlyerItem

_CENTS_ONLY_RE = re.compile(r"^(\d{1,2})\s*¢$")
_DIGITS_RE = re.compile(r"^\d{1,2}$")
_UNIT_TOKENS = {"ch.", "ea.", "ch", "ea"}


@dataclass
class Span:
    text: str
    size: float
    x0: float
    y0: float
    x1: float
    y1: float

    @property
    def cx(self) -> float:
        return (self.x0 + self.x1) / 2

    @property
    def cy(self) -> float:
        return (self.y0 + self.y1) / 2


@dataclass
class Price:
    value: float
    text: str
    spans: list[Span] = field(default_factory=list)

    @property
    def cx(self) -> float:
        return sum(s.cx for s in self.spans) / len(self.spans)

    @property
    def cy(self) -> float:
        return sum(s.cy for s in self.spans) / len(self.spans)


def extract_pdf(pdf_bytes: bytes) -> tuple[list[Span], float, float, str]:
    """All text spans of page 1 (the flyer format is single-page),
    the page size in points, and the full page text."""
    import pymupdf

    doc: Any = pymupdf.open(  # type: ignore[no-untyped-call]
        stream=pdf_bytes, filetype="pdf"
    )
    page = doc[0]
    spans: list[Span] = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                x0, y0, x1, y1 = span["bbox"]
                spans.append(Span(span["text"], float(span["size"]), x0, y0, x1, y1))
    return spans, float(page.rect.width), float(page.rect.height), page.get_text()


def dedupe_spans(spans: list[Span]) -> list[Span]:
    """Drop duplicate spans — some flyer PDFs render every text run
    twice (a shadow layer with near-identical geometry, off by a
    fraction of a point)."""
    out: list[Span] = []
    for s in spans:
        dup = any(
            s.text == k.text
            and abs(s.x0 - k.x0) <= 2
            and abs(s.y0 - k.y0) <= 2
            and abs(s.x1 - k.x1) <= 2
            and abs(s.y1 - k.y1) <= 2
            for k in out
        )
        if not dup:
            out.append(s)
    return out


def find_prices(spans: list[Span], min_size: float) -> list[Price]:
    """Cluster big-font digit spans into prices.

    A price is a dollar span (largest font, 1-2 digits) with an
    optional smaller cents span immediately to its right, or a
    digit span followed by a separate ¢ span (a cents price), or
    (defensively) a lone cents span, read as that many cents.
    """
    big = [
        s
        for s in spans
        if s.size >= min_size
        and (
            _DIGITS_RE.match(s.text.strip())
            or _CENTS_ONLY_RE.match(s.text.strip())
            or s.text.strip() == "¢"
        )
    ]
    prices: list[Price] = []
    used: set[int] = set()
    # Cents prices with a separate ¢ span ("49" + "¢").
    for i, s in enumerate(big):
        if s.text.strip() != "¢":
            continue
        for j, d in enumerate(big):
            if j == i or j in used or not _DIGITS_RE.match(d.text.strip()):
                continue
            if s.x0 - 36 <= d.x1 <= s.x0 + 2 and abs(d.cy - s.cy) <= 14:
                prices.append(Price(int(d.text.strip()) / 100, f"{d.text.strip()}¢", [d, s]))
                used.update({i, j})
                break
    # Cents-only prices with the ¢ inside the span ("49¢").
    for i, s in enumerate(big):
        if i in used:
            continue
        m = _CENTS_ONLY_RE.match(s.text.strip())
        if m:
            prices.append(Price(int(m.group(1)) / 100, s.text.strip(), [s]))
            used.add(i)
    # Dollar spans: the largest size present among digit spans.
    dollars = [
        (i, s) for i, s in enumerate(big) if i not in used and _DIGITS_RE.match(s.text.strip())
    ]
    if dollars:
        top = max(s.size for _, s in dollars)
        cents_pool = [(i, s) for i, s in dollars if s.size < top]
        for i, d in dollars:
            if d.size < top:
                continue
            used.add(i)
            parts = [d]
            value = float(int(d.text.strip()))
            best: tuple[int, Span] | None = None
            for j, c in cents_pool:
                if j in used:
                    continue
                if d.x1 - 6 <= c.x0 <= d.x1 + 34 and abs(c.cy - d.cy) <= 16:
                    best = (j, c)
                    break
            if best is not None:
                used.add(best[0])
                parts.append(best[1])
                value += int(best[1].text.strip()) / 100
            text = " ".join(p.text.strip() for p in parts)
            prices.append(Price(value, text, parts))
    # Leftover digit spans (unpaired cents).
    for i, s in enumerate(big):
        if i not in used and _DIGITS_RE.match(s.text.strip()):
            prices.append(Price(int(s.text.strip()) / 100, s.text.strip(), [s]))
    return prices


def _axis_bounds(centers: list[float], limit: float) -> list[tuple[float, float]]:
    """Cell bounds along one axis from sorted anchor centers."""
    bounds: list[tuple[float, float]] = []
    for i, c in enumerate(centers):
        if i == 0:
            lo = 0.0 if len(centers) == 1 else max(0.0, c - (centers[1] - c) / 2)
        else:
            lo = (centers[i - 1] + c) / 2
        if i == len(centers) - 1:
            hi = limit if len(centers) == 1 else min(limit, c + (c - centers[i - 1]) / 2)
        else:
            hi = (c + centers[i + 1]) / 2
        bounds.append((lo, hi))
    return bounds


def _line_centers(counts: Any, threshold: float) -> list[float]:
    """Group consecutive above-threshold rows/columns into lines
    and return their center positions."""
    centers: list[float] = []
    start: int | None = None
    for i, c in enumerate(counts):
        if c > threshold and start is None:
            start = i
        elif c <= threshold and start is not None:
            centers.append((start + i - 1) / 2)
            start = None
    if start is not None:
        centers.append((start + len(counts) - 1) / 2)
    return centers


def detect_grid_cells(
    pdf_bytes: bytes, scale: float = 2.0
) -> list[tuple[float, float, float, float]] | None:
    """Detect the product grid from the flyer's printed border
    lines: render page 1, find long red horizontal lines, then the
    vertical lines between them. Returns cell rects in points,
    row-major, or None when no grid is found."""
    import io

    import numpy as np
    import pymupdf
    from PIL import Image

    doc: Any = pymupdf.open(  # type: ignore[no-untyped-call]
        stream=pdf_bytes, filetype="pdf"
    )
    page = doc[0]
    pix = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale))  # type: ignore[no-untyped-call]
    img = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
    arr = np.asarray(img).astype(int)
    red = (
        (arr[:, :, 0] >= 140)
        & (arr[:, :, 0] - arr[:, :, 1] >= 55)
        & (arr[:, :, 0] - arr[:, :, 2] >= 55)
    )
    height, width = red.shape
    h_lines = _line_centers(red.sum(axis=1), 0.5 * width)
    if len(h_lines) < 2:
        return None
    top, bottom = int(h_lines[0]), int(h_lines[-1])
    v_lines = _line_centers(red[top : bottom + 1].sum(axis=0), 0.6 * (bottom - top))
    if len(v_lines) < 2:
        return None
    cells: list[tuple[float, float, float, float]] = []
    for r in range(len(h_lines) - 1):
        for c in range(len(v_lines) - 1):
            cells.append(
                (
                    v_lines[c] / scale,
                    h_lines[r] / scale,
                    v_lines[c + 1] / scale,
                    h_lines[r + 1] / scale,
                )
            )
    return cells


def match_cells(
    prices: list[Price], cells: list[tuple[float, float, float, float]]
) -> list[tuple[Price, tuple[float, float, float, float]]]:
    """Pair each price with the cell containing its anchor (or the
    nearest cell), sorted row-major by cell position."""
    out: list[tuple[Price, tuple[float, float, float, float]]] = []
    for p in prices:
        hit = next(
            (c for c in cells if c[0] <= p.cx <= c[2] and c[1] <= p.cy <= c[3]),
            None,
        )
        if hit is None:
            hit = min(
                cells,
                key=lambda c: ((c[0] + c[2]) / 2 - p.cx) ** 2 + ((c[1] + c[3]) / 2 - p.cy) ** 2,
            )
        out.append((p, hit))
    out.sort(key=lambda pc: (round(pc[1][1]), round(pc[1][0])))
    return out


def derive_cells(
    prices: list[Price], page_w: float, page_h: float, tol: float = 30.0
) -> list[tuple[Price, tuple[float, float, float, float]]]:
    """Assign each price a grid cell (x0, y0, x1, y1) in points,
    row-major order."""

    def cluster(values: list[float]) -> list[float]:
        groups: list[list[float]] = []
        for v in sorted(values):
            if groups and v - groups[-1][-1] <= tol:
                groups[-1].append(v)
            else:
                groups.append([v])
        return [sum(g) / len(g) for g in groups]

    cols = cluster([p.cx for p in prices])
    rows = cluster([p.cy for p in prices])
    col_bounds = _axis_bounds(cols, page_w)
    row_bounds = _axis_bounds(rows, page_h)

    def nearest(centers: list[float], v: float) -> int:
        return min(range(len(centers)), key=lambda i: abs(centers[i] - v))

    cells: list[tuple[Price, tuple[float, float, float, float]]] = []
    for p in prices:
        ci = nearest(cols, p.cx)
        ri = nearest(rows, p.cy)
        x0, x1 = col_bounds[ci]
        y0, y1 = row_bounds[ri]
        cells.append((p, (x0, y0, x1, y1)))
    cells.sort(key=lambda c: (round(c[1][1]), round(c[1][0])))
    return cells


def assemble_name(
    spans: list[Span], cell: tuple[float, float, float, float], min_size: float
) -> str:
    """Join the small-font spans inside a cell into a name, line by
    line in reading order. Unit tokens of the price itself are
    dropped; sizes and per-kg annotations stay (they are product
    information, as in other sources' names)."""
    x0, y0, x1, y1 = cell
    inside = [
        s
        for s in spans
        if s.size < min_size
        and x0 - 2 <= s.cx <= x1 + 2
        and y0 - 2 <= s.cy <= y1 + 2
        and s.text.strip() not in _UNIT_TOKENS
    ]
    lines: dict[int, list[Span]] = {}
    for s in inside:
        lines.setdefault(round(s.y0 / 3), []).append(s)
    parts: list[str] = []
    for key in sorted(lines):
        words = sorted(lines[key], key=lambda s: s.x0)
        text = " ".join(w.text.strip() for w in words if w.text.strip())
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            parts.append(text)
    return " | ".join(parts)


def price_unit(spans: list[Span], price: Price) -> str:
    """'lb' when an lb. token sits right by the price, else 'each'."""
    for s in spans:
        if (
            s.text.strip() in ("lb.", "lb")
            and abs(s.cx - price.cx) <= 60
            and abs(s.cy - price.cy) <= 45
        ):
            return "lb"
    return "each"


def parse_pdf_flyer(
    pdf_bytes: bytes,
    *,
    valid_from: date,
    valid_to: date,
    image_url: str,
    price_min_size: float = 17.0,
) -> list[FlyerItem]:
    spans, page_w, page_h, _ = extract_pdf(pdf_bytes)
    spans = dedupe_spans(spans)
    prices = find_prices(spans, price_min_size)
    grid = detect_grid_cells(pdf_bytes)
    paired = match_cells(prices, grid) if grid is not None else derive_cells(prices, page_w, page_h)
    items: list[FlyerItem] = []
    for price, cell in paired:
        x0, y0, x1, y1 = cell
        items.append(
            FlyerItem(
                name_fr=assemble_name(spans, cell, price_min_size),
                price_text=price.text,
                price_value=price.value,
                price_unit=price_unit(spans, price),
                valid_from=valid_from.isoformat(),
                valid_to=valid_to.isoformat(),
                languages=["fr", "en"],
                image_url=image_url,
                bbox={
                    "left": round(x0 / page_w * 1000),
                    "top": round(y0 / page_h * 1000),
                    "right": round(x1 / page_w * 1000),
                    "bottom": round(y1 / page_h * 1000),
                    "page": 1,
                },
                raw={
                    "parser": "pdf_text",
                    "price_parts": [p.text for p in price.spans],
                    "cell_pt": [round(v, 1) for v in cell],
                },
                confidence=1.0,
            )
        )
    return items
