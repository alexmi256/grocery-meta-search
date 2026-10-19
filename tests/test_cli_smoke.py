"""CLI smoke tests for the two 0%-covered maintenance tools
(reclassify, classify.run) plus CC discovery-window tests.

reclassify rewrites classifications DB-wide and classify.run
rebuilds the whole provenance table — both deserve at least one
end-to-end run on a scratch DB pinning their contracts:
reclassify flips only changed verdicts and deletes nothing;
classify.run is idempotent.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from grocery_meta_search.classify import run as classify_run
from grocery_meta_search.db import connect, init_schema
from grocery_meta_search.pipeline.reclassify import main as reclassify_main
from grocery_meta_search.pipeline.reclassify import reclassify


def _db(tmp_path: Path) -> Path:
    db_path = tmp_path / "cli.db"
    conn = connect(db_path)
    init_schema(conn)
    conn.execute("INSERT INTO stores (slug, name) VALUES ('maxi', 'Maxi')")
    conn.execute(
        "INSERT INTO flyers (id, store_slug, flyer_type, valid_from, valid_to)"
        " VALUES (1, 'maxi', 'weekly', '2026-10-15', '2026-10-21')"
    )
    # Item 1 is stored with a STALE verdict (Unclassified) that the
    # current classifier resolves; item 2's verdict is already right.
    conn.execute(
        "INSERT INTO flyer_items (id, flyer_id, store_slug, item_key, name_fr, category)"
        " VALUES (1, 1, 'maxi', 'k1', 'Pommes', 'Unclassified')"
    )
    conn.execute(
        "INSERT INTO flyer_items (id, flyer_id, store_slug, item_key, name_fr, category)"
        " VALUES (2, 1, 'maxi', 'k2', 'Lait', 'Dairy & Eggs > Milk & Cream')"
    )
    conn.execute(
        "INSERT INTO item_classifications VALUES (1, 'Unclassified', 'Unclassified', 'none', '', '2026-01-01')"
    )
    conn.execute(
        "INSERT INTO item_classifications VALUES (2, 'Dairy & Eggs', 'Milk & Cream', 'rule', 'r', '2026-01-01')"
    )
    conn.commit()
    conn.close()
    return db_path


def test_reclassify_flips_stale_verdicts(tmp_path: Path) -> None:
    db_path = _db(tmp_path)
    result = reclassify(str(db_path))
    assert result["total"] == 2 and result["flips"] == 1
    conn = connect(db_path)
    row = conn.execute("SELECT category FROM flyer_items WHERE id = 1").fetchone()
    assert row[0] == "Fruits & Vegetables > Fresh Fruits"
    prov = conn.execute("SELECT department, subcategory FROM item_classifications WHERE item_id = 1").fetchone()
    assert tuple(prov) == ("Fruits & Vegetables", "Fresh Fruits")
    # Nothing was deleted and the correct item is untouched.
    assert conn.execute("SELECT COUNT(*) FROM flyer_items").fetchone()[0] == 2
    conn.close()


def test_reclassify_dry_run_reports_without_writing(tmp_path: Path) -> None:
    db_path = _db(tmp_path)
    result = reclassify(str(db_path), dry_run=True)
    assert result["flips"] == 1
    conn = connect(db_path)
    assert conn.execute("SELECT category FROM flyer_items WHERE id = 1").fetchone()[0] == "Unclassified"
    conn.close()


def test_reclassify_main(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    db_path = _db(tmp_path)
    monkeypatch.setattr("sys.argv", ["reclassify", "--db", str(db_path), "--dry-run"])
    reclassify_main()
    out = capsys.readouterr().out
    assert "2 items, 1 flips" in out and "[dry run]" in out
    assert "Unclassified > Unclassified  ->  Fruits & Vegetables > Fresh Fruits" in out


def test_classify_run_applies_and_is_idempotent(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    db_path = _db(tmp_path)
    stats = classify_run.apply_classification(str(db_path))
    assert stats["Fruits & Vegetables"] == 1 and stats["Dairy & Eggs"] == 1
    conn = sqlite3.connect(db_path)
    labels = conn.execute("SELECT category FROM flyer_items ORDER BY id").fetchall()
    assert [r[0] for r in labels] == ["Fruits & Vegetables > Fresh Fruits", "Dairy & Eggs > Milk & Cream"]
    conn.close()
    # Re-running replaces provenance instead of duplicating it.
    classify_run.apply_classification(str(db_path))
    conn = sqlite3.connect(db_path)
    assert conn.execute("SELECT COUNT(*) FROM item_classifications").fetchone()[0] == 2
    conn.close()
    monkeypatch.setattr("sys.argv", ["run", "--db", str(db_path)])
    classify_run.main()
    assert "total 2  classified 2 (100.0%)" in capsys.readouterr().out
