"""OCR engines: RapidOCR line detection + Tesseract crop recognition."""

from __future__ import annotations

import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from PIL import Image

_LOCAL_TESS_ROOT = Path.home() / "workspace" / "tools" / "tess" / "root"


@dataclass
class OcrLine:
    """One detected text line with its bounding box (pixels)."""

    x: float
    y: float
    w: float
    h: float
    text: str
    conf: float

    @property
    def right(self) -> float:
        return self.x + self.w

    @property
    def bottom(self) -> float:
        return self.y + self.h

    @property
    def cx(self) -> float:
        return self.x + self.w / 2

    @property
    def cy(self) -> float:
        return self.y + self.h / 2

    def box(self) -> tuple[float, float, float, float]:
        return (self.x, self.y, self.right, self.bottom)


_engine: Any = None


def _rapidocr() -> Any:
    global _engine
    if _engine is None:
        from rapidocr_onnxruntime import RapidOCR  # type: ignore[import-untyped]

        _engine = RapidOCR()
    return _engine


def detect_lines(image: Image.Image) -> list[OcrLine]:
    """Run RapidOCR detection+recognition over a full flyer page."""
    import numpy as np

    result, _ = _rapidocr()(np.asarray(image.convert("RGB")))
    lines: list[OcrLine] = []
    for box, text, conf in result or []:
        xs = [float(p[0]) for p in box]
        ys = [float(p[1]) for p in box]
        lines.append(
            OcrLine(
                x=min(xs),
                y=min(ys),
                w=max(xs) - min(xs),
                h=max(ys) - min(ys),
                text=text,
                conf=float(conf),
            )
        )
    return lines


def detect_lines_banded(
    image: Image.Image, band_h: int = 2000, overlap: int = 200
) -> list[OcrLine]:
    """Detect lines on a very tall page by horizontal bands.

    RapidOCR downsamples large inputs internally, which makes small
    text on 4000px+ pages undetectable. Bands are detected separately
    and merged back into page coordinates; lines found in an overlap
    zone are deduplicated on (text, position).
    """
    if image.height <= band_h + overlap:
        return detect_lines(image)
    merged: list[OcrLine] = []
    seen: set[tuple[str, int, int]] = set()
    y = 0
    while y < image.height:
        band = image.crop((0, y, image.width, min(image.height, y + band_h)))
        for ln in detect_lines(band):
            key = (ln.text, round(ln.x / 8), round((ln.y + y) / 8))
            if key in seen:
                continue
            seen.add(key)
            merged.append(OcrLine(x=ln.x, y=ln.y + y, w=ln.w, h=ln.h, text=ln.text, conf=ln.conf))
        y += band_h - overlap
    return merged


def find_tesseract() -> tuple[str, dict[str, str]] | None:
    """Locate a tesseract binary. Returns (path, extra_env) or None.

    Search order: $GROCERY_TESSERACT_BIN, the locally extracted copy
    under ~/workspace/tools/tess (survives VM replacement), then PATH.
    """
    override = os.environ.get("GROCERY_TESSERACT_BIN")
    if override and Path(override).exists():
        return override, _tess_env_for(Path(override))
    local = _LOCAL_TESS_ROOT / "usr" / "bin" / "tesseract"
    if local.exists():
        return str(local), _tess_env_for(local)
    on_path = shutil.which("tesseract")
    if on_path:
        return on_path, {}
    return None


def _tess_env_for(binary: Path) -> dict[str, str]:
    """Env needed by a locally extracted (non-installed) tesseract."""
    root = binary.parent.parent.parent  # .../root/usr/bin/tesseract -> .../root
    lib = root / "usr" / "lib" / "x86_64-linux-gnu"
    tessdata = root / "usr" / "share" / "tesseract-ocr" / "5" / "tessdata"
    env: dict[str, str] = {}
    if lib.exists():
        env["LD_LIBRARY_PATH"] = str(lib)
    if tessdata.exists():
        env["TESSDATA_PREFIX"] = str(tessdata)
    return env


def upscale_for_ocr(
    image: Image.Image, min_width: int = 1600, max_scale: float = 2.0
) -> Image.Image:
    """Upscale low-resolution flyer pages before OCR.

    Some circulaires.club pages are served at 800-1000px wide; the OCR
    detector misses glyphs at that size. Fractions in the segmentation
    config are relative, so upscaling is segmentation-neutral and also
    improves the Tesseract name crops.
    """
    if image.width >= min_width:
        return image
    scale = min(min_width / image.width, max_scale)
    return image.resize(
        (round(image.width * scale), round(image.height * scale)),
        Image.Resampling.LANCZOS,
    )


def ocr_crop_text(
    image: Image.Image,
    box: tuple[float, float, float, float],
    *,
    psm: int = 6,
    lang: str = "fra+eng",
    upscale: int = 2,
    pad: int = 8,
) -> str | None:
    """Re-OCR one cropped region with Tesseract. None when unavailable."""
    found = find_tesseract()
    if found is None:
        return None
    binary, extra_env = found
    x0, y0, x1, y1 = box
    crop = image.crop(
        (
            max(0, int(x0) - pad),
            max(0, int(y0) - pad),
            min(image.width, int(x1) + pad),
            min(image.height, int(y1) + pad),
        )
    )
    if upscale > 1:
        crop = crop.resize((crop.width * upscale, crop.height * upscale), Image.Resampling.LANCZOS)
    env = dict(os.environ)
    env.update(extra_env)
    try:
        proc = subprocess.run(
            [binary, "stdin", "stdout", "-l", lang, "--psm", str(psm)],
            input=_png_bytes(crop),
            capture_output=True,
            env=env,
            timeout=60,
            check=True,
        )
    except (subprocess.SubprocessError, OSError):
        return None
    text = proc.stdout.decode("utf-8", errors="replace")
    return text.strip() or None


def _png_bytes(image: Image.Image) -> bytes:
    import io

    buf = io.BytesIO()
    image.save(buf, format="PNG")
    return buf.getvalue()
