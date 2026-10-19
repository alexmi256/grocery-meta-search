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
from grocery_meta_search.pipeline.multibuy import main as multibuy_main
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
    # Ingest writes one price observation per priced item
    # (pipeline/fetch.py: insert_items); mirror that here so the
    # write-back's history sync is exercised.
    if price is not None:
        conn.execute(
            "INSERT INTO price_observations"
            " (item_key, store_slug, flyer_id, price_value, price_text, valid_from, valid_to)"
            " VALUES (?, 'test-mb', 1, ?, ?, '2026-10-15', '2026-10-21')",
            (f"k{item_id}", price, f"{price:.2f}"),
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
    assert stats == {"recovered": 1, "reconciled": 0}
    row = conn.execute(
        "SELECT price_value, unit_quantity, unit_measurement, conditions, raw FROM flyer_items WHERE id = 1"
    ).fetchone()
    assert row[0] == 1.29
    # The derived unit pair follows the multibuy condition, exactly as
    # ingest splits one: count items, measurement 'multiple'.
    assert (row[1], row[2]) == (2.0, "multiple")
    assert json.loads(row[3])["multibuy"] == {"count": 2, "total": 1.99}
    prov = json.loads(row[4])["multibuy_recovery"]
    assert prov == {"via": "image", "unit": 1.29, "count": 2, "total": 1.99}
    # The price history carries the corrected unit price, not the
    # collapsed bundle total.
    obs = conn.execute("SELECT price_value FROM price_observations WHERE item_key = 'k1'").fetchone()
    assert obs[0] == 1.29
    # Idempotent: the corrected price no longer equals the payload
    # (and the condition exists), so a second pass recovers nothing
    # and has nothing left to reconcile.
    assert multibuy_store(conn, "test-mb", cache_dir=tmp_path) == {"recovered": 0, "reconciled": 0}
    conn.close()


def test_reconcile_heals_pre_fix_recovery(tmp_path: Path) -> None:
    """A row recovered before the write-back synced everything (unit
    pair left at 1/'each', observation at the bundle total) is repaired
    from its provenance on the next store pass, without re-OCR."""
    conn = _db(tmp_path)
    _item(conn, 1, price=1.29, payload=1.99, conditions={"multibuy": {"count": 2, "total": 1.99}})
    prov = {"via": "image", "unit": 1.29, "count": 2, "total": 1.99}
    conn.execute(
        "UPDATE flyer_items SET raw = ? WHERE id = 1",
        (json.dumps({"price": 1.99, "multibuy_recovery": prov}),),
    )
    conn.execute("UPDATE price_observations SET price_value = 1.99 WHERE item_key = 'k1'")
    conn.commit()

    stats = multibuy_store(conn, "test-mb", cache_dir=tmp_path)
    assert stats == {"recovered": 0, "reconciled": 1}
    row = conn.execute("SELECT price_value, unit_quantity, unit_measurement FROM flyer_items WHERE id = 1").fetchone()
    assert row[0] == 1.29  # the item's price is never touched
    assert (row[1], row[2]) == (2.0, "multiple")
    obs = conn.execute("SELECT price_value FROM price_observations WHERE item_key = 'k1'").fetchone()
    assert obs[0] == 1.29
    # Healed: a second pass finds nothing to write.
    assert multibuy_store(conn, "test-mb", cache_dir=tmp_path) == {"recovered": 0, "reconciled": 0}
    conn.close()


def test_reconcile_heals_hand_corrected_multibuy(tmp_path: Path) -> None:
    """The campaign's hand-corrected offers carry conditions.multibuy but
    no provenance, and keep the pre-correction unit pair plus an
    observation at the bundle total. A store pass heals both."""
    conn = _db(tmp_path)
    _item(conn, 1, price=1.29, payload=1.99, conditions={"multibuy": {"count": 2, "total": 1.99}})
    conn.execute("UPDATE price_observations SET price_value = 1.99 WHERE item_key = 'k1'")
    conn.commit()

    assert multibuy_store(conn, "test-mb", cache_dir=tmp_path) == {"recovered": 0, "reconciled": 1}
    row = conn.execute("SELECT price_value, unit_quantity, unit_measurement FROM flyer_items WHERE id = 1").fetchone()
    assert row[0] == 1.29  # the hand-corrected price stands
    assert (row[1], row[2]) == (2.0, "multiple")
    obs = conn.execute("SELECT price_value FROM price_observations WHERE item_key = 'k1'").fetchone()
    assert obs[0] == 1.29
    conn.close()


def test_reconcile_uses_provenance_count_when_condition_missing(tmp_path: Path) -> None:
    """If conditions lost its multibuy block, the provenance record still
    carries the count the pair is recomputed from."""
    conn = _db(tmp_path)
    _item(conn, 1, price=1.29, payload=1.99)
    prov = {"via": "image", "unit": 1.29, "count": 3, "total": 3.87}
    conn.execute(
        "UPDATE flyer_items SET raw = ? WHERE id = 1",
        (json.dumps({"price": 1.99, "multibuy_recovery": prov}),),
    )
    conn.execute("UPDATE price_observations SET price_value = 1.99 WHERE item_key = 'k1'")
    conn.commit()

    assert multibuy_store(conn, "test-mb", cache_dir=tmp_path) == {"recovered": 0, "reconciled": 1}
    row = conn.execute("SELECT unit_quantity, unit_measurement FROM flyer_items WHERE id = 1").fetchone()
    assert (row[0], row[1]) == (3.0, "multiple")
    conn.close()


def test_reconcile_skips_ambiguous_observation(tmp_path: Path) -> None:
    """item_key hashes name + price_unit only, so two same-flyer items can
    share it. With more than one matching observation the recovered
    item's history row is ambiguous: the unit pair is still fixed, but
    no observation is rewritten (the sibling's must not be touched)."""
    conn = _db(tmp_path)
    _item(conn, 1, price=1.29, payload=1.99, conditions={"multibuy": {"count": 2, "total": 1.99}})
    conn.execute(
        "INSERT INTO price_observations (item_key, store_slug, flyer_id, price_value, price_text, valid_from, valid_to)"
        " VALUES ('k1', 'test-mb', 1, 1.99, '1.99', '2026-10-15', '2026-10-21')"
    )
    conn.commit()

    assert multibuy_store(conn, "test-mb", cache_dir=tmp_path) == {"recovered": 0, "reconciled": 1}
    row = conn.execute("SELECT unit_quantity, unit_measurement FROM flyer_items WHERE id = 1").fetchone()
    assert (row[0], row[1]) == (2.0, "multiple")
    prices = conn.execute("SELECT price_value FROM price_observations WHERE item_key = 'k1' ORDER BY id").fetchall()
    assert [r[0] for r in prices] == [1.29, 1.99]  # neither rewritten
    conn.close()


def test_reconcile_leaves_unit_pair_for_garbled_count(tmp_path: Path) -> None:
    """A count above 100 is OCR garble, not an offer (split_unit's own
    guard): the pair is left alone rather than forced to 1/'each', while
    the history still mirrors the item's price."""
    conn = _db(tmp_path)
    _item(conn, 1, price=1.29, payload=1.99, conditions={"multibuy": {"count": 15998, "total": 1.99}})
    conn.execute("UPDATE flyer_items SET unit_quantity = 100.0, unit_measurement = 'gram' WHERE id = 1")
    conn.execute("UPDATE price_observations SET price_value = 1.99 WHERE item_key = 'k1'")
    conn.commit()

    assert multibuy_store(conn, "test-mb", cache_dir=tmp_path) == {"recovered": 0, "reconciled": 1}
    row = conn.execute("SELECT unit_quantity, unit_measurement FROM flyer_items WHERE id = 1").fetchone()
    assert (row[0], row[1]) == (100.0, "gram")  # untouched
    obs = conn.execute("SELECT price_value FROM price_observations WHERE item_key = 'k1'").fetchone()
    assert obs[0] == 1.29
    conn.close()


def test_reconcile_only_mode_skips_recovery(tmp_path: Path) -> None:
    """recover=False repairs existing multibuy rows but never runs the
    image-recovery candidate pass (nothing downloaded or OCR'd)."""
    conn = _db(tmp_path)
    _item(conn, 1, price=1.99, payload=1.99)  # would be a recovery candidate
    _seed_cache(tmp_path, 1, SHIMEJI)
    _item(conn, 2, price=1.29, payload=1.99, conditions={"multibuy": {"count": 2, "total": 1.99}})
    conn.execute("UPDATE price_observations SET price_value = 1.99 WHERE item_key = 'k2'")
    conn.commit()

    stats = multibuy_store(conn, "test-mb", cache_dir=tmp_path, recover=False)
    assert stats == {"recovered": 0, "reconciled": 1}
    prices = conn.execute("SELECT price_value FROM flyer_items ORDER BY id").fetchall()
    assert [r[0] for r in prices] == [1.99, 1.29]  # item 1 was not recovered
    row = conn.execute("SELECT unit_quantity, unit_measurement FROM flyer_items WHERE id = 2").fetchone()
    assert (row[0], row[1]) == (2.0, "multiple")
    conn.close()


def test_cli_reconcile_reaches_store_not_enabled(tmp_path: Path, capsys: Any) -> None:
    """--reconcile accepts a store absent from multibuy_config.json, so
    hand-corrected offers at stores that must not run image recovery
    (jean-coutu here) can be healed."""
    conn = _db(tmp_path)
    conn.execute("INSERT INTO stores (slug, name) VALUES ('jean-coutu', 'Jean Coutu')")
    conn.execute(
        "INSERT INTO flyers (id, store_slug, flyer_type, valid_from, valid_to)"
        " VALUES (2, 'jean-coutu', 'weekly', '2026-10-15', '2026-10-21')"
    )
    conn.execute(
        "INSERT INTO flyer_items (id, flyer_id, store_slug, item_key, name_fr, price_value,"
        " unit_quantity, unit_measurement, conditions, raw, valid_from, valid_to)"
        " VALUES (1, 2, 'jean-coutu', 'k1', 'X', 1.29, 1.0, 'each',"
        ' \'{"multibuy": {"count": 2, "total": 1.99}}\', \'{"price": 1.99}\','
        " '2026-10-15', '2026-10-21')"
    )
    conn.execute(
        "INSERT INTO price_observations (item_key, store_slug, flyer_id, price_value)"
        " VALUES ('k1', 'jean-coutu', 2, 1.99)"
    )
    conn.commit()
    conn.close()

    assert multibuy_main(["--db", str(tmp_path / "mb.db"), "--slugs", "jean-coutu", "--reconcile"]) == 0
    assert "jean-coutu: 1 multibuy rows reconciled" in capsys.readouterr().out
    conn = connect(tmp_path / "mb.db")
    assert conn.execute("SELECT unit_measurement FROM flyer_items WHERE id = 1").fetchone()[0] == "multiple"
    obs = conn.execute("SELECT price_value FROM price_observations WHERE item_key = 'k1'").fetchone()
    assert obs[0] == 1.29
    conn.close()


def test_candidate_gates(tmp_path: Path) -> None:
    conn = _db(tmp_path)
    _item(conn, 1, price=1.29, payload=1.99)  # already corrected by hand: price != payload
    _item(conn, 2, price=1.99, payload=1.99, conditions={"multibuy": {"count": 2, "total": 1.99}})
    # ...whose derived unit pair already matches the condition, so the
    # reconcile has nothing to write.
    conn.execute("UPDATE flyer_items SET unit_quantity = 2.0, unit_measurement = 'multiple' WHERE id = 2")
    _item(conn, 3, price=1.99, payload=1.99, image_url="https://example.test/cutout.jpg")
    _item(conn, 4, price=1.99, payload=None)  # no payload price in raw
    _item(conn, 5, price=None, payload=1.99)  # no stored price
    _item(conn, 6, price=1.99, payload=1.99)  # candidate, but no badge in the render
    for item_id in (1, 2, 3, 4, 5):
        _seed_cache(tmp_path, item_id, SHIMEJI)
    _seed_cache(tmp_path, 6, "CHAMPIGNONS SHIMEJI BLANCS 1,99/CH")
    stats = multibuy_store(conn, "test-mb", cache_dir=tmp_path)
    assert stats == {"recovered": 0, "reconciled": 0}
    prices = conn.execute("SELECT price_value FROM flyer_items ORDER BY id").fetchall()
    assert [r[0] for r in prices] == [1.29, 1.99, 1.99, 1.99, None, 1.99]
    conn.close()
