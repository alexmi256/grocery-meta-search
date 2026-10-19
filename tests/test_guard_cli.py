"""Guard CLI + text/stamp edge cases not covered by test_guard.py:
warning_text rendering, record_warnings on malformed raw payloads,
and main() end to end (flag print, --stamp, quiet DB)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from grocery_meta_search.db import connect, init_schema
from grocery_meta_search.pipeline import guard
from grocery_meta_search.pipeline.guard import (
    ThinEditionWarning,
    record_warnings,
    warning_text,
)


def _warning() -> ThinEditionWarning:
    return ThinEditionWarning(
        store_slug="s",
        cycle_from="2026-10-15",
        cycle_to="2026-10-21",
        current=12,
        baseline=100.0,
        prior_cycles=[("2026-10-01", 100), ("2026-10-08", 100)],
    )


def test_warning_text() -> None:
    text = warning_text(_warning())
    assert "THIN EDITION s cycle 2026-10-15..2026-10-21" in text
    assert "12 items vs baseline 100" in text
    assert "2026-10-01: 100" in text


def test_record_warnings_tolerates_malformed_raw(tmp_path: Path) -> None:
    conn = connect(tmp_path / "g.db")
    init_schema(conn)
    conn.execute("INSERT INTO stores (slug, name) VALUES ('s', 'Store')")
    conn.execute(
        "INSERT INTO flyers (id, store_slug, flyer_type, valid_from, valid_to, raw)"
        " VALUES (1, 's', 'weekly', '2026-10-15', '2026-10-21', '{broken')"
    )
    conn.execute(
        "INSERT INTO flyers (id, store_slug, flyer_type, source_ref, valid_from, valid_to, raw)"
        " VALUES (2, 's', 'weekly', 'pub-b', '2026-10-15', '2026-10-21', '\"a string\"')"
    )
    conn.commit()
    record_warnings(conn, [_warning()], today="2026-10-18")
    raws = [r[0] for r in conn.execute("SELECT raw FROM flyers ORDER BY id")]
    first = json.loads(raws[0])
    assert first["thin_edition_guard"]["flagged_on"] == "2026-10-18"
    second = json.loads(raws[1])
    assert second["_source_raw"] == "a string"  # non-dict raw is preserved aside
    assert second["thin_edition_guard"]["current"] == 12
    conn.close()


def _seed_thin_db(tmp_path: Path) -> Path:
    db_path = tmp_path / "audit.db"
    conn = connect(db_path)
    init_schema(conn)
    conn.execute("INSERT INTO stores (slug, name) VALUES ('s', 'Store')")
    for valid_from, valid_to, n in (
        ("2026-10-01", "2026-10-07", 100),
        ("2026-10-08", "2026-10-14", 100),
        ("2026-10-15", "2026-10-21", 10),
    ):
        cur = conn.execute(
            "INSERT INTO flyers (store_slug, valid_from, valid_to, raw) VALUES ('s', ?, ?, '{}')",
            (valid_from, valid_to),
        )
        flyer_id = cur.lastrowid
        for i in range(n):
            conn.execute(
                "INSERT INTO flyer_items (flyer_id, store_slug, item_key) VALUES (?, 's', ?)",
                (flyer_id, f"{valid_from}-{i}"),
            )
    conn.commit()
    conn.close()
    return db_path


def test_guard_main_flags_and_stamps(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    db_path = _seed_thin_db(tmp_path)
    monkeypatch.setattr("sys.argv", ["guard", "--db", str(db_path), "--today", "2026-10-17", "--stamp"])
    guard.main()
    out = capsys.readouterr().out
    assert "THIN EDITION s" in out
    conn = connect(db_path)
    raw = conn.execute("SELECT raw FROM flyers WHERE valid_from = '2026-10-15'").fetchone()[0]
    assert "thin_edition_guard" in json.loads(raw)
    conn.close()


def test_guard_main_quiet_store(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    db_path = _seed_thin_db(tmp_path)
    monkeypatch.setattr("sys.argv", ["guard", "--db", str(db_path), "--slugs", "absent-store", "--today", "2026-10-17"])
    guard.main()
    assert "no thin editions" in capsys.readouterr().out
