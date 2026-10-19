"""Multibuy store-loop tests: candidate gating, recovery write-back
with provenance, per-item idempotency.

Fully hermetic: the cell renders and their cached OCR text are
pre-seeded in the cache dir, so neither network nor OCR runs; the
extractor itself runs for real on a real campaign fixture text.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

from grocery_meta_search.db import connect, init_schema
from grocery_meta_search.pipeline.multibuy import multibuy_store

WISHABI = "https://images.wishabi.net/cell/x.jpg"
SHIMEJI = "2POUR 199 CHAMPIGNONS SHIMEJI BLANCS PRODUIT DE CHINE 1,29/CH WHITE SHIMEJI MUSHROOMS REG.1,49/CH"


def _db(tmp_path: Path) -> sqlite3.Connection:
    conn = connect(tmp_path / "mb.db")
    init_schema(conn)
    conn.execute("INSERT INTO stores (slug, name) VALUES ('test-mb', 'Test MB')")
    conn.execute(
        "INSERT INTO flyers (id, store_slug, flyer_type, valid_from, valid_to)"
        " VALUES (1, 'test-mb', 'weekly', '2026-10-15', '2026-10-21')"
    )
    return conn


def _item(
    conn: sqlite3.Connection,
    item_id: int,
    *,
    price: float | None,
    payload: float | None,
    image_url: str | None = WISHABI,
    conditions: dict[str, Any] | None = None,
) -> None:
    raw: dict[str, Any] = {} if payload is None else {"price": payload}
    conn.execute(
        "INSERT INTO flyer_items (id, flyer_id, store_slug, item_key, name_fr,"
        " price_value, image_url, conditions, raw, valid_from, valid_to)"
        " VALUES (?, 1, 'test-mb', ?, 'Produit', ?, ?, ?, ?, '2026-10-15', '2026-10-21')",
        (
            item_id,
            f"k{item_id}",
            price,
            image_url,
            json.dumps(conditions or {}),
            json.dumps(raw),
        ),
    )
    conn.commit()


def _seed_cache(cache_dir: Path, item_id: int, text: str) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    (cache_dir / f"{item_id}.jpg").write_bytes(b"fake")
    (cache_dir / f"{item_id}.txt").write_text(text, encoding="utf-8")


def test_recovery_writes_unit_price_and_provenance(tmp_path: Path) -> None:
    conn = _db(tmp_path)
    _item(conn, 1, price=1.99, payload=1.99)  # payload collapsed to the bundle total
    _seed_cache(tmp_path, 1, SHIMEJI)
    stats = multibuy_store(conn, "test-mb", cache_dir=tmp_path)
    assert stats == {"recovered": 1}
    row = conn.execute("SELECT price_value, conditions, raw FROM flyer_items WHERE id = 1").fetchone()
    assert row[0] == 1.29
    assert json.loads(row[1])["multibuy"] == {"count": 2, "total": 1.99}
    prov = json.loads(row[2])["multibuy_recovery"]
    assert prov == {"via": "image", "unit": 1.29, "count": 2, "total": 1.99}
    # Idempotent: the corrected price no longer equals the payload
    # (and the condition exists), so a second pass recovers nothing.
    assert multibuy_store(conn, "test-mb", cache_dir=tmp_path) == {"recovered": 0}
    conn.close()


def test_candidate_gates(tmp_path: Path) -> None:
    conn = _db(tmp_path)
    _item(conn, 1, price=1.29, payload=1.99)  # already corrected by hand: price != payload
    _item(conn, 2, price=1.99, payload=1.99, conditions={"multibuy": {"count": 2, "total": 1.99}})
    _item(conn, 3, price=1.99, payload=1.99, image_url="https://example.test/cutout.jpg")
    _item(conn, 4, price=1.99, payload=None)  # no payload price in raw
    _item(conn, 5, price=None, payload=1.99)  # no stored price
    _item(conn, 6, price=1.99, payload=1.99)  # candidate, but no badge in the render
    for item_id in (1, 2, 3, 4, 5):
        _seed_cache(tmp_path, item_id, SHIMEJI)
    _seed_cache(tmp_path, 6, "CHAMPIGNONS SHIMEJI BLANCS 1,99/CH")
    stats = multibuy_store(conn, "test-mb", cache_dir=tmp_path)
    assert stats == {"recovered": 0}
    prices = conn.execute("SELECT price_value FROM flyer_items ORDER BY id").fetchall()
    assert [r[0] for r in prices] == [1.29, 1.99, 1.99, 1.99, None, 1.99]
    conn.close()
