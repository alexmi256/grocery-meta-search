"""Review-tooling smoke tests: store_report.generate, the original
review.generate, and review_sample.main end to end on a tiny DB.

Downloads are faked at each module's seam; rendering, sampling,
index and zip assembly run for real.
"""

from __future__ import annotations

import json
import zipfile
from pathlib import Path

import pytest
from PIL import Image

from grocery_meta_search.classify import review, review_sample, store_report
from grocery_meta_search.db import connect, init_schema

PAGE_URL = "https://pages.test/flyer.jpg"
DIRECT_URL = "https://images.wishabi.net/cell/direct.jpg"
FAIL_URL = "https://images.wishabi.net/cell/fail.jpg"
BBOX = json.dumps({"left": 100, "top": 100, "right": 500, "bottom": 500, "page": 1})


def _write_jpg(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", (200, 200), "white").save(path, format="JPEG")


def _fake_download(url: str, dest: Path) -> bool:
    if "fail" in url:
        return False
    _write_jpg(dest)
    return True


def _db(tmp_path: Path) -> Path:
    db_path = tmp_path / "rev.db"
    conn = connect(db_path)
    init_schema(conn)
    conn.execute("INSERT INTO stores (slug, name) VALUES ('test-rev', 'Test Rev')")
    conn.execute("INSERT INTO stores (slug, name) VALUES ('old-rev', 'Old Rev')")
    conn.execute(
        "INSERT INTO flyers (id, store_slug, source_ref, flyer_type, valid_from, valid_to)"
        " VALUES (1, 'test-rev', 'ref-1', 'weekly', '2026-10-15', '2026-12-31')"
    )
    conn.execute(
        "INSERT INTO flyers (id, store_slug, source_ref, flyer_type, valid_from, valid_to)"
        " VALUES (2, 'old-rev', 'ref-2', 'weekly', '2026-09-01', '2026-10-01')"
    )
    items = [
        # (id, flyer, store, name, category, image_url, bbox)
        (1, 1, "test-rev", "Pommes", "Fruits & Vegetables > Fresh Fruits", PAGE_URL, BBOX),
        (2, 1, "test-rev", "Lait", "Dairy & Eggs > Milk", DIRECT_URL, None),
        (3, 1, "test-rev", "Mystère", "Unclassified", FAIL_URL, None),
        (4, 2, "old-rev", "Vieux produit", "Pantry > Rice", DIRECT_URL, None),
    ]
    for item_id, flyer_id, slug, name, category, url, bbox in items:
        conn.execute(
            "INSERT INTO flyer_items (id, flyer_id, store_slug, item_key, name_fr,"
            " price_value, price_text, image_url, bbox, category, raw, conditions,"
            " valid_from, valid_to)"
            " VALUES (?, ?, ?, ?, ?, 2.50, '2.50', ?, ?, ?, '{}', '{}', '2026-10-15', '2026-12-31')",
            (item_id, flyer_id, slug, f"k{item_id}", name, url, bbox, category),
        )
        dept, _, sub = category.partition(" > ")
        conn.execute(
            "INSERT INTO item_classifications VALUES (?, ?, ?, 'rule', 'r1', '2026-10-18T00:00:00')",
            (item_id, dept, sub or dept),
        )
    conn.commit()
    conn.close()
    return db_path


# ── store_report.generate ───────────────────────────────────────────


def test_store_report_end_to_end(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    db_path = _db(tmp_path)
    monkeypatch.setattr(store_report, "_download", _fake_download)
    out = tmp_path / "report"
    stats = store_report.generate(str(db_path), "test-rev", out)
    assert stats["items"] == 3
    assert stats["crops"] == 1 and stats["direct"] == 1 and stats["missing"] == 1
    assert stats["pages"] == 1
    md = (out / "test-rev-report.md").read_text(encoding="utf-8")
    assert "# Test Rev — full product report" in md
    assert "(2 classified items, 1 unclassified)" in md
    assert "## Unclassified items — kept for review" in md
    assert "- **Name (French):** Pommes" in md
    assert "- **Size:** None" in md  # missing fields render, not omitted
    assert "- **Category (French):**" in md
    assert "*(no picture could be downloaded)*" in md
    assert (out / "images" / "item-1.jpg").exists()  # the bbox crop
    assert (out / "images" / "item-2.jpg").exists()  # the direct image


def test_store_report_latest_only_and_only_ids(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    db_path = _db(tmp_path)
    monkeypatch.setattr(store_report, "_download", _fake_download)
    stats = store_report.generate(str(db_path), "test-rev", tmp_path / "r2", only_ids={2})
    assert stats["items"] == 1
    md = (tmp_path / "r2" / "test-rev-report.md").read_text(encoding="utf-8")
    assert "Lait" in md and "Pommes" not in md


def test_store_report_unknown_store(tmp_path: Path) -> None:
    db_path = _db(tmp_path)
    with pytest.raises(SystemExit, match="unknown store"):
        store_report.generate(str(db_path), "nope", tmp_path / "r3")


# ── review.generate (original sampler) ──────────────────────────────


def test_review_generate_smoke(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    db_path = _db(tmp_path)
    monkeypatch.chdir(tmp_path)  # its page cache is CWD-relative
    page = tmp_path / "page.jpg"
    _write_jpg(page)
    monkeypatch.setattr(review, "_fetch_page", lambda url, cd: page)
    out = tmp_path / "review.md"
    stats = review.generate(str(db_path), out, tmp_path / "assets", seed=3, per_store=10)
    md = out.read_text(encoding="utf-8")
    assert "# Classification review" in md
    assert "4 items" in md and "3 classified = 75.0%" in md
    assert "Pommes" in md and "Vieux produit" in md
    assert stats["crops"] + stats["direct"] + stats["missing"] >= 3


# ── review_sample.main (the current pack builder) ───────────────────


def test_review_sample_main_with_zip(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    db_path = _db(tmp_path)
    monkeypatch.setattr(store_report, "_download", _fake_download)
    out_dir = tmp_path / "pack"
    zip_path = tmp_path / "pack.zip"
    monkeypatch.setattr(
        "sys.argv",
        [
            "review_sample",
            "--db",
            str(db_path),
            "--out-dir",
            str(out_dir),
            "--seed",
            "7",
            "--today",
            "2026-10-18",
            "--zip",
            str(zip_path),
        ],
    )
    review_sample.main()
    index = (out_dir / "README.md").read_text(encoding="utf-8")
    assert "test-rev" in index and "2 classified + 1 unclassified" in index
    # old-rev has items but only an expired flyer: listed as skipped.
    assert "no current flyer — skipped" in index and "old-rev" in index
    assert (out_dir / "test-rev" / "test-rev-report.md").exists()
    with zipfile.ZipFile(zip_path) as zf:
        names = zf.namelist()
    assert any(n.endswith("README.md") for n in names)
    assert any(n.endswith("test-rev-report.md") for n in names)
