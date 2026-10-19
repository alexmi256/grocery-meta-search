"""Harvest store-loop tests: candidate selection, fills with
provenance, dry-run, and the refresh path that retracts stale fills.

OCR is faked at the _ocr_lines seam and page downloads at
_fetch_page; the extraction logic itself runs for real.
"""

from __future__ import annotations

import json
import sqlite3
from datetime import date
from pathlib import Path
from typing import Any

import pytest
from PIL import Image

from grocery_meta_search.db import connect, init_schema
from grocery_meta_search.pipeline import harvest
from grocery_meta_search.pipeline.harvest import harvest_store

TODAY = date(2026, 10, 18)
WISHABI = "https://images.wishabi.net/cell/abc.jpg"


def _db(tmp_path: Path) -> sqlite3.Connection:
    conn = connect(tmp_path / "hv.db")
    init_schema(conn)
    conn.execute("INSERT INTO stores (slug, name) VALUES ('test-hv', 'Test HV')")
    conn.execute(
        "INSERT INTO flyers (id, store_slug, flyer_type, valid_from, valid_to)"
        " VALUES (1, 'test-hv', 'weekly', '2026-10-15', '2026-10-21')"
    )
    return conn


def _item(
    conn: sqlite3.Connection,
    item_id: int,
    *,
    name: str = "Produit",
    image_url: str | None = WISHABI,
    package_size: str | None = None,
    price_unit: str | None = None,
    raw: dict[str, Any] | None = None,
) -> None:
    conn.execute(
        "INSERT INTO flyer_items (id, flyer_id, store_slug, item_key, name_fr,"
        " image_url, package_size, price_unit, raw, conditions, valid_from, valid_to)"
        " VALUES (?, 1, 'test-hv', ?, ?, ?, ?, ?, ?, '{}', '2026-10-15', '2026-10-21')",
        (
            item_id,
            f"k{item_id}",
            name,
            image_url,
            package_size,
            price_unit,
            json.dumps(raw or {}),
        ),
    )
    conn.commit()


@pytest.fixture(autouse=True)
def _config(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(harvest, "load_harvest_configs", lambda: {"test-hv": {}})


def _png_sized(url: str, cache_dir: Path) -> Path:
    """Encode the item in the image width so the OCR fake can answer
    per item — harvest_store OCRs items on a thread pool, so a shared
    iterator would assign texts nondeterministically."""
    width = 20 if "one" in url else 30
    path = cache_dir / f"p{width}.png"
    Image.new("RGB", (width, width), "white").save(path)
    return path


def test_fill_size_and_unit_with_provenance(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _db(tmp_path)
    _item(conn, 1, name="Savon", image_url="https://images.wishabi.net/cell/one.jpg")
    _item(conn, 2, name="Pommes", image_url="https://images.wishabi.net/cell/two.jpg")
    monkeypatch.setattr(harvest, "_fetch_page", _png_sized)
    monkeypatch.setattr(
        harvest,
        "_ocr_lines",
        lambda img: ["Savon liquide", "500 ml"] if img.width == 20 else ["Pommes", "3,99/lb"],
    )
    stats = harvest_store(conn, "test-hv", today=TODAY, cache_dir=tmp_path)
    assert stats["filled_size"] == 1 and stats["filled_unit"] == 1
    rows = conn.execute("SELECT package_size, price_unit, raw FROM flyer_items ORDER BY id").fetchall()
    assert rows[0][0] == "500 ml" and rows[0][1] is None
    assert rows[1][0] is None and rows[1][1] == "lb"
    prov = json.loads(rows[0][2])["harvest"]
    assert prov["size"] == "500 ml" and prov["via"] == "image"
    # The split unit pair stays in sync with the filled price_unit.
    pair = conn.execute("SELECT unit_quantity, unit_measurement FROM flyer_items WHERE id = 2").fetchone()
    assert tuple(pair) == (1.0, "pound")
    conn.close()


def _png(cache_dir: Path) -> Path:
    path = cache_dir / "page.png"
    Image.new("RGB", (20, 20), "white").save(path)
    return path


def test_no_plan_no_image_and_ambiguous(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _db(tmp_path)
    _item(conn, 1, image_url=None)  # no image, no bbox -> no plan
    _item(conn, 2, image_url="https://images.wishabi.net/missing.jpg")  # download fails
    _item(conn, 3, name="Mystère")  # OCR finds nothing usable
    monkeypatch.setattr(harvest, "_fetch_page", lambda url, cd: None if "missing" in url else _png(cd))
    monkeypatch.setattr(harvest, "_ocr_lines", lambda img: ["Produit générique"])
    stats = harvest_store(conn, "test-hv", today=TODAY, cache_dir=tmp_path)
    assert stats["items"] == 3
    assert stats["no_plan"] == 1 and stats["no_image"] == 1 and stats["ambiguous"] == 1
    assert stats["filled_size"] == 0 and stats["filled_unit"] == 0
    conn.close()


def test_dry_run_counts_but_does_not_write(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _db(tmp_path)
    _item(conn, 1)
    monkeypatch.setattr(harvest, "_fetch_page", lambda url, cd: _png(cd))
    monkeypatch.setattr(harvest, "_ocr_lines", lambda img: ["Savon", "500 ml"])
    stats = harvest_store(conn, "test-hv", today=TODAY, cache_dir=tmp_path, dry_run=True)
    assert stats["filled_size"] == 1
    row = conn.execute("SELECT package_size FROM flyer_items WHERE id = 1").fetchone()
    assert row[0] is None
    conn.close()


def test_unconfigured_store_is_a_noop(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _db(tmp_path)
    _item(conn, 1)
    monkeypatch.setattr(harvest, "load_harvest_configs", lambda: {})
    stats = harvest_store(conn, "test-hv", today=TODAY, cache_dir=tmp_path)
    assert stats["items"] == 0 and stats["filled_size"] == 0
    conn.close()


def test_refresh_retracts_and_updates_only_harvested_fields(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _db(tmp_path)
    # Harvested before with a wrong size; the fresh extraction differs.
    _item(
        conn,
        1,
        package_size="999 g",
        image_url="https://images.wishabi.net/cell/one.jpg",
        raw={"harvest": {"size": "999 g", "via": "image"}},
    )
    # Harvested before; the fresh extraction finds nothing -> clear.
    _item(
        conn,
        2,
        package_size="750 g",
        image_url="https://images.wishabi.net/cell/two.jpg",
        raw={"harvest": {"size": "750 g", "via": "image"}},
    )
    # Producer-supplied size (no harvest provenance): never touched.
    _item(conn, 3, package_size="1 kg", raw={"price": 3.0})
    monkeypatch.setattr(harvest, "_fetch_page", _png_sized)
    monkeypatch.setattr(
        harvest,
        "_ocr_lines",
        lambda img: ["Produit", "250 g"] if img.width == 20 else ["Produit générique"],
    )
    stats = harvest_store(conn, "test-hv", today=TODAY, cache_dir=tmp_path, refresh_harvested=True)
    assert stats["items"] == 2  # only provenance-carrying items are re-extracted
    assert stats["changed_size"] == 1 and stats["cleared_size"] == 1
    rows = conn.execute("SELECT id, package_size, raw FROM flyer_items ORDER BY id").fetchall()
    assert rows[0][1] == "250 g" and json.loads(rows[0][2])["harvest"]["size"] == "250 g"
    assert rows[1][1] is None and "harvest" not in json.loads(rows[1][2])
    assert rows[2][1] == "1 kg"
    conn.close()
