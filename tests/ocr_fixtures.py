"""Requirements for the page-image OCR fixture tests.

Six per-store segmentation tests (Odessa, Costco, Monde au Naturel,
Intermarche Palumbo, PA Nature, Frutta Si) replay captured RapidOCR
lines over the real flyer *page image*. The images are committed (see
``AGENTS.md``: fixtures are the sanctioned exception to the
no-images-in-git rule), and the strategies also need the OCR toolchain
the pipeline uses — cv2 for the colour gates, Tesseract with the
French traineddata for the name re-OCR, and RapidOCR for the
red-grid/chalkboard vote passes.

Each helper below skips with a clear reason when a requirement is
missing, so the suite stays green on a checkout that predates the
fixtures or a machine without the OCR stack instead of erroring on a
missing file or import. ``tests/fixtures/README.md`` lists each
fixture's source and how to provision the toolchain.
"""

from __future__ import annotations

import functools
import importlib.util
import os
import subprocess
from pathlib import Path

import pytest

FIXTURES = Path(__file__).with_name("fixtures")


def fixture_image(name: str) -> Path:
    """Path to a page-image fixture, or skip if it is not present."""
    path = FIXTURES / name
    if not path.exists():
        pytest.skip(f"missing fixture image {name!r} — see tests/fixtures/README.md to fetch it")
    return path


def require_cv2() -> None:
    """The colour-gated strategies (name_cells, red_grid, chalkboard,
    Palumbo's green-ink gate) import cv2 lazily."""
    if importlib.util.find_spec("cv2") is None:
        pytest.skip("OpenCV (cv2) is not installed (needed by this colour-gated strategy)")


def require_rapidocr() -> None:
    """red_grid / chalkboard re-detect lines on crops with RapidOCR."""
    if importlib.util.find_spec("rapidocr_onnxruntime") is None:
        pytest.skip("rapidocr-onnxruntime is not installed (needed by this OCR strategy)")


@functools.lru_cache(maxsize=1)
def _french_ocr_available() -> bool:
    from grocery_meta_search.ocr.engine import find_tesseract

    found = find_tesseract()
    if found is None:
        return False
    binary, extra_env = found
    env = dict(os.environ)
    env.update(extra_env)
    try:
        proc = subprocess.run([binary, "--list-langs"], capture_output=True, text=True, env=env, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return False
    return proc.returncode == 0 and "fra" in proc.stdout.split()


def require_french_ocr() -> None:
    """The name re-OCR runs Tesseract with ``-l fra+eng``; without the
    French traineddata it silently returns None and the assembled
    names lose their accents."""
    if not _french_ocr_available():
        pytest.skip("Tesseract with the French ('fra') traineddata is required (see tests/fixtures/README.md)")
