"""OCR support for image flyer sources (Phase 3b).

Hybrid approach, validated on samples 2026-10-13:

- RapidOCR (ONNX, pip) detects text lines and prices reliably on flyer
  pages, but its recognition drops spaces in all-caps blocks and mangles
  French accents.
- Tesseract (fra+eng) reads clean French with spaces/accents, but does
  not detect the giant display prices on a full page. It is used to
  re-OCR small name-block crops where it excels.
"""

from .engine import OcrLine, detect_lines, find_tesseract, ocr_crop_text

__all__ = ["OcrLine", "detect_lines", "find_tesseract", "ocr_crop_text"]
