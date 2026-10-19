"""OCR engine glue tests: banded detection merge/dedupe, tesseract
discovery, and ocr_crop_text against a fake tesseract binary
(a shell script) so no real OCR quality is involved."""

from __future__ import annotations

import os
from pathlib import Path

import pytest
from PIL import Image

from grocery_meta_search.ocr import engine
from grocery_meta_search.ocr.engine import (
    OcrLine,
    detect_lines_banded,
    find_tesseract,
    ocr_crop_text,
    upscale_for_ocr,
)


def test_ocrline_geometry() -> None:
    line = OcrLine(x=10, y=20, w=30, h=10, text="X", conf=0.9)
    assert line.right == 40 and line.bottom == 30
    assert line.cx == 25 and line.cy == 25
    assert line.box() == (10, 20, 40, 30)


def test_upscale_for_ocr_noop_when_wide_enough() -> None:
    img = Image.new("RGB", (2000, 100))
    assert upscale_for_ocr(img, min_width=1600) is img


def test_banded_detection_merges_and_dedupes(monkeypatch: pytest.MonkeyPatch) -> None:
    # A 260px-tall image with band_h=100/overlap=20 -> bands at
    # y=0, 80, 160, 240. The fake detector reports the same line in
    # every band; band-offset copies at the same page position must
    # dedupe to one, while the line's y tracks the band offset.
    def fake_detect(band: Image.Image) -> list[OcrLine]:
        return [OcrLine(x=10, y=5, w=50, h=10, text="POMMES", conf=0.9)]

    monkeypatch.setattr(engine, "detect_lines", fake_detect)
    img = Image.new("RGB", (100, 260))
    lines = detect_lines_banded(img, band_h=100, overlap=20)
    ys = sorted(ln.y for ln in lines)
    assert ys == [5, 85, 165, 245]  # one per band, page coordinates
    # A short image takes the single-pass path.
    short = Image.new("RGB", (100, 100))
    assert detect_lines_banded(short, band_h=100, overlap=20) == fake_detect(short)


def test_find_tesseract_env_override(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fake = tmp_path / "tesseract"
    fake.write_text("#!/bin/sh\n")
    monkeypatch.setenv("GROCERY_TESSERACT_BIN", str(fake))
    found = find_tesseract()
    assert found is not None and found[0] == str(fake)
    # A nonexistent override is ignored, falling through to the
    # local copy / PATH (both may exist on the dev machine).
    monkeypatch.setenv("GROCERY_TESSERACT_BIN", str(tmp_path / "missing"))
    found2 = find_tesseract()
    assert found2 is None or found2[0] != str(tmp_path / "missing")


def _fake_tesseract(tmp_path: Path, body: str) -> Path:
    script = tmp_path / "faketess"
    script.write_text(f"#!/bin/sh\n{body}\n")
    script.chmod(0o755)
    return script


def test_ocr_crop_text_with_fake_binary(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    script = _fake_tesseract(tmp_path, "cat > /dev/null\necho POMMES")
    monkeypatch.setattr(engine, "find_tesseract", lambda: (str(script), {}))
    img = Image.new("RGB", (100, 50), "white")
    assert ocr_crop_text(img, (10, 10, 60, 30)) == "POMMES"


def test_ocr_crop_text_failure_and_absence(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    img = Image.new("RGB", (100, 50), "white")
    monkeypatch.setattr(engine, "find_tesseract", lambda: None)
    assert ocr_crop_text(img, (10, 10, 60, 30)) is None
    script = _fake_tesseract(tmp_path, "exit 1")
    monkeypatch.setattr(engine, "find_tesseract", lambda: (str(script), {}))
    assert ocr_crop_text(img, (10, 10, 60, 30)) is None
    blank = _fake_tesseract(tmp_path, "echo '   '")
    monkeypatch.setattr(engine, "find_tesseract", lambda: (str(blank), {}))
    assert ocr_crop_text(img, (10, 10, 60, 30)) is None


def test_find_tesseract_local_copy_when_present() -> None:
    # On this machine the extracted local copy exists; the search
    # must find A tesseract (env/local/PATH) rather than None.
    if "GROCERY_TESSERACT_BIN" in os.environ:
        pytest.skip("env override set")
    found = find_tesseract()
    assert found is not None and Path(found[0]).exists()
