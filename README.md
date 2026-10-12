# Grocery Meta Search

A meta search engine for grocery and food items in Montreal — Flipp-style
flyer search plus proxied product search across grocery stores, with price tracking.

## Status

**Phase 1 in progress** — discovering grocery stores with a physical presence in Montreal.

## Plan

See [docs/PHASES.md](docs/PHASES.md) for the full 7-phase plan.

## Engineering standards

- Git for version tracking; Markdown for notes and research (`docs/`)
- Python 3.11+, SQLite
- `ruff` (lint), `mypy --strict` (type checking), `pytest` (tests)

## Layout

- `src/grocery_meta_search/` — application code
- `tests/` — pytest suite
- `docs/phases/` — per-phase notes and deliverables
- `docs/research/` — research notes and raw findings
