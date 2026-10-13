"""Seed the SQLite DB from the per-store YAML research files.

Usage:
    PYTHONPATH=src .venv/bin/python -m grocery_meta_search.seed --db DB --slugs S
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path
from typing import Any

import yaml

from .db import connect, init_schema

RESEARCH_DIR = Path(__file__).resolve().parents[2] / "docs" / "research" / "stores"


def _as_json(value: Any) -> str | None:
    if value is None:
        return None
    return json.dumps(value, ensure_ascii=False)


def seed_store(conn: sqlite3.Connection, data: dict[str, Any]) -> str:
    slug = str(data["slug"])
    conn.execute(
        """
        INSERT INTO stores (slug, name, name_variants, store_type, footprint, tier,
                            website_url, parent_company, affiliation, excluded,
                            research_status, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(slug) DO UPDATE SET
            name=excluded.name, name_variants=excluded.name_variants,
            store_type=excluded.store_type, footprint=excluded.footprint, tier=excluded.tier,
            website_url=excluded.website_url, parent_company=excluded.parent_company,
            affiliation=excluded.affiliation, excluded=excluded.excluded,
            research_status=excluded.research_status, notes=excluded.notes,
            updated_at=strftime('%Y-%m-%dT%H:%M:%fZ', 'now')
        """,
        (
            slug,
            data.get("name"),
            _as_json(data.get("name_variants")),
            data.get("store_type"),
            data.get("footprint"),
            data.get("tier"),
            data.get("website_url"),
            data.get("parent_company"),
            data.get("affiliation"),
            1 if data.get("excluded") else 0,
            data.get("research_status"),
            data.get("notes"),
        ),
    )
    return slug


def seed_flyer_sources(
    conn: sqlite3.Connection,
    slug: str,
    data: dict[str, Any],
    brand_configs: dict[str, dict[str, Any]],
) -> int:
    count = 0
    for flyer_type in (data.get("flyers") or {}).get("types", []):
        ftype = flyer_type.get("type", "weekly")
        for src in flyer_type.get("sources", []):
            name = (src.get("name") or "").strip().lower()
            api_config = brand_configs.get(slug) if name == "flipp" else None
            conn.execute(
                """
                INSERT INTO flyer_sources
                    (store_slug, flyer_type, name, url, kind, format,
                     parse_friendliness, fetchability, languages, api_config, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    slug,
                    ftype,
                    name,
                    src.get("url"),
                    src.get("kind"),
                    src.get("format"),
                    src.get("parse_friendliness"),
                    src.get("fetchability"),
                    _as_json(src.get("languages")),
                    _as_json(api_config),
                    src.get("notes"),
                ),
            )
            count += 1
    return count


def seed(
    db_path: Path,
    slugs: list[str] | None = None,
    brands_path: Path | None = None,
) -> dict[str, int]:
    brand_configs: dict[str, dict[str, Any]] = {}
    if brands_path and brands_path.exists():
        brand_configs = json.loads(brands_path.read_text(encoding="utf-8"))

    conn = connect(db_path)
    init_schema(conn)
    stats = {"stores": 0, "sources": 0}
    for yaml_path in sorted(RESEARCH_DIR.glob("*.yaml")):
        if yaml_path.name == "_template.yaml":
            continue
        data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        slug = str(data.get("slug", ""))
        if slugs and slug not in slugs:
            continue
        seed_store(conn, data)
        stats["stores"] += 1
        stats["sources"] += seed_flyer_sources(conn, slug, data, brand_configs)
    conn.commit()
    conn.close()
    return stats


def main() -> None:
    parser = argparse.ArgumentParser(description="Seed the DB from YAML research files.")
    parser.add_argument("--db", required=True, type=Path)
    parser.add_argument("--slugs", default="", help="comma-separated store slugs (default: all)")
    parser.add_argument("--brands", default=None, type=Path, help="flipp_brands.json path")
    args = parser.parse_args()
    slugs = [s.strip() for s in args.slugs.split(",") if s.strip()] or None
    stats = seed(args.db, slugs, args.brands)
    print(f"seeded {stats['stores']} stores, {stats['sources']} flyer sources -> {args.db}")


if __name__ == "__main__":
    main()
