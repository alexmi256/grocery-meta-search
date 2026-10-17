"""Bilingual item names.

Wishabi/Flipp payloads often carry one combined name with the French
and English versions joined by ' | ' ("COULIS DE TOMATE BELGUSTO |
BELGUSTO TOMATO PASSATA"). Split those into name_fr / name_en so each
language is stored in its own field (Alex, 2026-10-17). The order in
the payloads is French first in every observed case; a light language
score guards against an English-first payload.
"""
from __future__ import annotations

import re
import unicodedata

_FR_WORDS = {
    "de", "des", "du", "la", "le", "les", "au", "aux", "et", "à", "en",
    "pour", "avec", "sans", "ou", "sur", "frais", "fraîche", "fraiche",
}
_EN_WORDS = {
    "the", "and", "with", "of", "or", "for", "fresh", "style", "size",
    "original", "family",
}
_ACCENT_RE = re.compile(r"[àâäéèêëîïôöûüç]")
_WORD_RE = re.compile(r"[a-zàâäéèêëîïôöûüç']+")


def _french_score(text: str) -> int:
    words = _WORD_RE.findall(text.lower())
    score = 3 * len(_ACCENT_RE.findall(text))
    score += 2 * sum(1 for w in words if w in _FR_WORDS)
    score -= 2 * sum(1 for w in words if w in _EN_WORDS)
    return score


def split_bilingual_name(name: str | None) -> tuple[str | None, str | None]:
    """Split a combined 'FR | EN' name into (name_fr, name_en).

    Returns (name, None) when there is no separator — the caller then
    falls back to its locale-based assignment for single names.
    """
    if not name or "|" not in name:
        return (name or None), None
    # NFC so accented letters score the same however they were encoded.
    name = unicodedata.normalize("NFC", name)
    parts = [p.strip() for p in name.split("|")]
    parts = [p for p in parts if p]
    if len(parts) < 2:
        return (parts[0] if parts else None), None
    first, second = parts[0], " | ".join(parts[1:])
    if _french_score(second) > _french_score(first):
        return second, first
    return first, second
