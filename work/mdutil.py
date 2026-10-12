"""Shared markdown rendering helpers for the doc generators."""

import re

_NON_URLS = {"", "none found", "n/a", "na", "-", "--", "—", "none"}


def md_link(raw: str, max_display: int = 40) -> str:
    """Render a URL as a clickable markdown link: [display](href).

    Adds an https:// scheme when missing. Non-URL values (e.g. "none found")
    are returned as plain text so they never become broken links.
    """
    raw = (raw or "").strip()
    if raw.lower() in _NON_URLS:
        return "—" if raw == "" else raw
    href = raw if re.match(r"(?i)^https?://", raw) else "https://" + raw
    if not re.match(r"(?i)^https?://[^/\s]*\.[^/\s]+", href):
        return raw  # not actually a URL — leave as plain text
    display = re.sub(r"(?i)^https?://", "", href).rstrip("/")
    display = display.replace("|", "\\|")
    if len(display) > max_display:
        display = display[: max_display - 1] + "…"
    return f"[{display}]({href})"
