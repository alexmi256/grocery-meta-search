"""fields.reprocess tests: the package_size/price_unit repair pass.

Pins the policy: structured raw sizes are authoritative and never
overwritten; name/block-derived sizes are recomputed under the
current extraction policy; values the guards now reject are cleared
(and their harvest provenance goes with them); units fill from the
raw Flipp post_price_text; dry-run writes nothing.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

import pytest

from grocery_meta_search.db import connect, init_schema
from grocery_meta_search.pipeline.fields import (
    extract_package_size,
    main,
    reprocess,
)
from grocery_meta_search.prices import parse_price_text


def _db(tmp_path: Path) -> Path:
    db_path = tmp_path / "fields.db"
    conn = connect(db_path)
    init_schema(conn)
    conn.execute("INSERT INTO stores (slug, name) VALUES ('maxi', 'Maxi')")
    conn.execute(
        "INSERT INTO flyers (id, store_slug, flyer_type, valid_from, valid_to)"
        " VALUES (1, 'maxi', 'weekly', '2026-10-15', '2026-10-21')"
    )
    conn.commit()
    conn.close()
    return db_path


def _item(
    db_path: Path,
    item_id: int,
    *,
    name_fr: str,
    package_size: str | None = None,
    price_unit: str | None = None,
    raw: dict[str, Any] | None = None,
) -> None:
    conn = connect(db_path)
    conn.execute(
        "INSERT INTO flyer_items (id, flyer_id, store_slug, item_key, name_fr,"
        " package_size, price_unit, raw) VALUES (?, 1, 'maxi', ?, ?, ?, ?, ?)",
        (item_id, f"k{item_id}", name_fr, package_size, price_unit, json.dumps(raw or {})),
    )
    conn.commit()
    conn.close()


def _stored(db_path: Path, item_id: int) -> tuple[Any, Any, dict[str, Any]]:
    conn = connect(db_path)
    row = conn.execute("SELECT package_size, price_unit, raw FROM flyer_items WHERE id = ?", (item_id,)).fetchone()
    conn.close()
    return row[0], row[1], json.loads(row[2])


def test_fill_origins_raw_name_block(tmp_path: Path) -> None:
    db_path = _db(tmp_path)
    _item(db_path, 1, name_fr="Jus d'orange 1,89 l")
    _item(db_path, 2, name_fr="Produit", raw={"size": "500 g"})
    _item(db_path, 3, name_fr="Produit", raw={"block_text": "PRODUIT 750 ml"})
    _item(db_path, 4, name_fr="Produit sans taille")
    stats = reprocess(str(db_path))
    st = stats["maxi"]
    assert st["total"] == 4 and st["set"] == 3
    assert st["from_name"] == 1 and st["from_raw"] == 1 and st["from_block"] == 1
    assert _stored(db_path, 1)[0] == extract_package_size("Jus d'orange 1,89 l")
    assert _stored(db_path, 2)[0] == "500 g"
    assert _stored(db_path, 3)[0] == "750 ml"
    assert _stored(db_path, 4)[0] is None


def test_stored_size_corrected_and_structured_kept(tmp_path: Path) -> None:
    db_path = _db(tmp_path)
    _item(db_path, 1, name_fr="Lait 2 litres", package_size="1 l")  # stale -> corrected
    _item(db_path, 2, name_fr="Café 750 ml", package_size="500 g", raw={"size": "500 g"})
    stats = reprocess(str(db_path))
    assert stats["maxi"]["corrected"] == 1
    assert _stored(db_path, 1)[0] == extract_package_size("Lait 2 litres")
    assert _stored(db_path, 2)[0] == "500 g"  # structured raw size wins, untouched


def test_rejected_size_cleared_with_its_provenance(tmp_path: Path) -> None:
    db_path = _db(tmp_path)
    _item(
        db_path,
        1,
        name_fr="Gaufres protéines 19 g",
        package_size="19 g",
        raw={"harvest": {"size": "19 g", "via": "image"}},
    )
    stats = reprocess(str(db_path))
    assert stats["maxi"]["corrected"] == 1
    size, _, raw = _stored(db_path, 1)
    assert size is None
    assert "size" not in raw["harvest"] and raw["harvest"]["via"] == "image"


def test_unit_filled_from_post_price_text(tmp_path: Path) -> None:
    db_path = _db(tmp_path)
    _item(db_path, 1, name_fr="Pommes", raw={"post_price_text": "/lb 4,39$/kg"})
    _item(db_path, 2, name_fr="Lait", price_unit="each", raw={"post_price_text": "/lb"})
    stats = reprocess(str(db_path))
    _, unit = parse_price_text("/lb 4,39$/kg")
    assert unit is not None
    assert _stored(db_path, 1)[1] == unit
    assert _stored(db_path, 2)[1] == "each"  # existing unit untouched
    assert stats["maxi"]["unit_set"] == 2  # both rows carry a unit afterwards


def test_dry_run_and_idempotency(tmp_path: Path) -> None:
    db_path = _db(tmp_path)
    _item(db_path, 1, name_fr="Jus d'orange 1,89 l")
    stats = reprocess(str(db_path), dry_run=True)
    assert stats["maxi"]["set"] == 1
    assert _stored(db_path, 1)[0] is None  # counted, not written
    reprocess(str(db_path))
    assert _stored(db_path, 1)[0] is not None
    again = reprocess(str(db_path))
    assert again["maxi"]["corrected"] == 0 and again["maxi"]["set"] == 1


def test_main_prints_per_store_and_total(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    db_path = _db(tmp_path)
    _item(db_path, 1, name_fr="Jus d'orange 1,89 l")
    monkeypatch.setattr("sys.argv", ["fields", "--db", str(db_path), "--dry-run"])
    main()
    out = capsys.readouterr().out
    assert "maxi" in out and "TOTAL" in out and "[dry run]" in out


def test_reprocess_tolerates_malformed_raw(tmp_path: Path) -> None:
    db_path = _db(tmp_path)
    conn = sqlite3.connect(db_path)
    conn.execute(
        "INSERT INTO flyer_items (id, flyer_id, store_slug, item_key, name_fr, raw)"
        " VALUES (1, 1, 'maxi', 'k1', 'Jus 1,89 l', '{not json')"
    )
    conn.commit()
    conn.close()
    stats = reprocess(str(db_path))
    assert stats["maxi"]["from_name"] == 1  # fell back to the name
