"""Pipeline 3a (sample): fetch latest flyers for stores into SQLite.

Currently supports the Flipp FlyerKit source (group 1). Per-store brand config
(access token, store code) comes from the flyer_sources.api_config column,
populated by the seed step from flipp_brands.json.

Usage:
    PYTHONPATH=src .venv/bin/python -m grocery_meta_search.pipeline.fetch \\
        --db data/grocery.db --slugs maxi,iga,provigo
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
from pathlib import Path
from typing import Any

from ..db import connect, init_schema
from ..sources.base import FlyerEdition, FlyerItem
from ..sources.flipp import BrandConfig, FlyerKitClient, FlyerKitError

_WS_RE = re.compile(r"\s+")


def normalize_name(name: str | None) -> str:
    return _WS_RE.sub(" ", (name or "").strip().lower())


def item_key(store_slug: str, item: FlyerItem) -> str:
    """Stable identity for an item across flyer editions (price history)."""
    name = normalize_name(item.name_fr or item.name_en)
    unit = item.price_unit or ""
    digest = hashlib.sha1(f"{store_slug}|{name}|{unit}".encode()).hexdigest()
    return digest[:16]


def get_flipp_source(conn: sqlite3.Connection, store_slug: str) -> sqlite3.Row | None:
    row = conn.execute(
        "SELECT * FROM flyer_sources WHERE store_slug = ? AND name = 'flipp' LIMIT 1",
        (store_slug,),
    ).fetchone()
    assert row is None or isinstance(row, sqlite3.Row)
    return row


def upsert_edition(
    conn: sqlite3.Connection,
    store_slug: str,
    source_id: int,
    edition: FlyerEdition,
) -> tuple[int, bool]:
    """Insert the edition if new. Returns (flyer_id, is_new)."""
    row = conn.execute(
        """
        SELECT id FROM flyers
        WHERE store_slug = ? AND flyer_type = ?
          AND COALESCE(valid_from, '') = COALESCE(?, '')
          AND COALESCE(valid_to, '') = COALESCE(?, '')
          AND COALESCE(flyer_source_id, -1) = COALESCE(?, -1)
        """,
        (store_slug, edition.flyer_type, edition.valid_from, edition.valid_to, source_id),
    ).fetchone()
    if row:
        return int(row["id"]), False
    cur = conn.execute(
        """
        INSERT INTO flyers (store_slug, flyer_source_id, flyer_type, valid_from, valid_to,
                            languages, fetch_status, raw)
        VALUES (?, ?, ?, ?, ?, ?, 'ok', ?)
        """,
        (
            store_slug,
            source_id,
            edition.flyer_type,
            edition.valid_from,
            edition.valid_to,
            json.dumps(edition.languages, ensure_ascii=False),
            json.dumps(edition.raw, ensure_ascii=False),
        ),
    )
    flyer_id = cur.lastrowid
    assert flyer_id is not None
    return flyer_id, True


def insert_items(
    conn: sqlite3.Connection, flyer_id: int, store_slug: str, items: list[FlyerItem]
) -> int:
    count = 0
    for item in items:
        key = item_key(store_slug, item)
        conn.execute(
            """
            INSERT INTO flyer_items
                (flyer_id, store_slug, item_key, name_fr, name_en, price_text,
                 price_value, price_unit, valid_from, valid_to, languages,
                 image_url, bbox, sku, brand, conditions, loyalty_gated, raw, confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                flyer_id,
                store_slug,
                key,
                item.name_fr,
                item.name_en,
                item.price_text,
                item.price_value,
                item.price_unit,
                item.valid_from,
                item.valid_to,
                json.dumps(item.languages, ensure_ascii=False),
                item.image_url,
                json.dumps(item.bbox, ensure_ascii=False) if item.bbox else None,
                item.sku,
                item.brand,
                json.dumps(item.conditions, ensure_ascii=False),
                1 if item.loyalty_gated else 0,
                json.dumps(item.raw, ensure_ascii=False),
                item.confidence,
            ),
        )
        if item.price_value is not None:
            conn.execute(
                """
                INSERT INTO price_observations
                    (item_key, store_slug, flyer_id, price_value, price_text, valid_from, valid_to)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    key,
                    store_slug,
                    flyer_id,
                    item.price_value,
                    item.price_text,
                    item.valid_from,
                    item.valid_to,
                ),
            )
        count += 1
    return count


def fetch_store(
    conn: sqlite3.Connection, client: FlyerKitClient, store_slug: str
) -> dict[str, Any]:
    """Fetch active flyers for one store. Returns a small report dict."""
    report: dict[str, Any] = {"store": store_slug, "editions": 0, "items": 0}
    src = get_flipp_source(conn, store_slug)
    if src is None or not src["api_config"]:
        report["error"] = "no flipp source with api_config"
        return report
    cfg_data = json.loads(src["api_config"])
    cfg = BrandConfig(
        store_slug=store_slug,
        brand_slug=cfg_data["brand_slug"],
        access_token=cfg_data["access_token"],
        store_code=cfg_data["store_code"],
    )
    try:
        editions = client.fetch_store_editions(cfg)
    except FlyerKitError as exc:
        report["error"] = str(exc)
        return report
    for edition in editions:
        flyer_id, is_new = upsert_edition(conn, store_slug, int(src["id"]), edition)
        report["editions"] += 1
        if is_new:
            report["items"] += insert_items(conn, flyer_id, store_slug, edition.items)
        else:
            report["skipped"] = report.get("skipped", 0) + len(edition.items)
    conn.commit()
    return report


def run(db_path: Path, slugs: list[str]) -> list[dict[str, Any]]:
    conn = connect(db_path)
    init_schema(conn)
    client = FlyerKitClient()
    reports = [fetch_store(conn, client, slug) for slug in slugs]
    conn.close()
    return reports


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch latest flyers (pipeline 3a).")
    parser.add_argument("--db", required=True, type=Path)
    parser.add_argument("--slugs", required=True, help="comma-separated store slugs")
    args = parser.parse_args()
    slugs = [s.strip() for s in args.slugs.split(",") if s.strip()]
    for report in run(args.db, slugs):
        err = f" ERROR: {report['error']}" if report.get("error") else ""
        print(f"{report['store']}: {report['editions']} editions, {report['items']} items{err}")


if __name__ == "__main__":
    main()
