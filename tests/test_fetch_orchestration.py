"""Fetch orchestration tests: source dispatch, edition skipping,
and the post-fetch stage wiring (harvest / multibuy / thin guard).

All source clients are faked — no network, no OCR. The point is the
pipeline glue in pipeline/fetch.py: the code that decides which
source serves a store, stores editions idempotently, and runs the
repair stages without ever failing the fetch.
"""

from __future__ import annotations

import sqlite3
from datetime import date
from types import SimpleNamespace
from typing import Any

import pytest

from grocery_meta_search.db import connect, init_schema
from grocery_meta_search.pipeline import fetch
from grocery_meta_search.pipeline.fetch import (
    fetch_store,
    insert_items,
    store_editions,
    upsert_edition,
)
from grocery_meta_search.sources.base import FlyerEdition, FlyerItem
from grocery_meta_search.sources.metrodigital import MetroDigitalConfig, MetroDigitalError


def _conn() -> sqlite3.Connection:
    conn = connect(":memory:")
    init_schema(conn)
    return conn


def _add_store(conn: sqlite3.Connection, slug: str) -> None:
    conn.execute("INSERT INTO stores (slug, name) VALUES (?, ?)", (slug, slug.title()))


def _add_source(conn: sqlite3.Connection, slug: str, name: str, api_config: str | None) -> sqlite3.Row:
    conn.execute(
        "INSERT INTO flyer_sources (store_slug, flyer_type, name, api_config) VALUES (?, 'weekly', ?, ?)",
        (slug, name, api_config),
    )
    row = conn.execute("SELECT * FROM flyer_sources WHERE store_slug = ? AND name = ?", (slug, name)).fetchone()
    assert row is not None
    return row


def _edition(ref: str = "E1", items: list[FlyerItem] | None = None) -> FlyerEdition:
    return FlyerEdition(
        valid_from="2026-10-15",
        valid_to="2026-10-21",
        source_ref=ref,
        languages=["fr"],
        items=items if items is not None else [FlyerItem(name_fr="Pommes", price_text="2.50", price_value=2.5)],
    )


# ── edition storage ─────────────────────────────────────────────────


def test_upsert_edition_new_then_existing() -> None:
    conn = _conn()
    _add_store(conn, "maxi")
    src = _add_source(conn, "maxi", "flipp", "{}")
    first_id, is_new = upsert_edition(conn, "maxi", int(src["id"]), _edition())
    assert is_new
    again_id, is_new_again = upsert_edition(conn, "maxi", int(src["id"]), _edition())
    assert not is_new_again and again_id == first_id
    other_id, is_new_other = upsert_edition(conn, "maxi", int(src["id"]), _edition(ref="E2"))
    assert is_new_other and other_id != first_id
    conn.close()


def test_store_editions_skips_already_stored() -> None:
    conn = _conn()
    _add_store(conn, "maxi")
    src = _add_source(conn, "maxi", "flipp", "{}")
    report: dict[str, Any] = {"store": "maxi", "editions": 0, "items": 0}
    store_editions(conn, src, "maxi", [_edition()], report)
    assert report["editions"] == 1 and report["items"] == 1
    # A second fetch of the same edition counts the edition but
    # inserts nothing (the skip that makes re-fetching safe).
    store_editions(conn, src, "maxi", [_edition()], report)
    assert report["editions"] == 2 and report["items"] == 1
    assert conn.execute("SELECT COUNT(*) FROM flyer_items").fetchone()[0] == 1
    conn.close()


def test_insert_items_rounds_price_and_fills_size_from_name() -> None:
    conn = _conn()
    _add_store(conn, "maxi")
    conn.execute(
        "INSERT INTO flyers (id, store_slug, flyer_type, valid_from, valid_to)"
        " VALUES (1, 'maxi', 'weekly', '2026-10-15', '2026-10-21')"
    )
    items = [
        FlyerItem(name_fr="Jus d'orange 1.89L", price_value=2.4699999999999998),
        FlyerItem(name_fr="Pommes", price_value=1.0, package_size="3 lb"),
    ]
    assert insert_items(conn, 1, "maxi", items) == 2
    rows = conn.execute("SELECT price_value, package_size FROM flyer_items ORDER BY id").fetchall()
    assert rows[0][0] == 2.47  # float tail rounded at the DB boundary
    assert rows[0][1] is not None and "1.89" in rows[0][1]  # size extracted from the name
    assert rows[1][1] == "3 lb"  # producer-supplied size wins
    conn.close()


def test_insert_items_exclusion_counting() -> None:
    conn = _conn()
    _add_store(conn, "maxi")
    conn.execute(
        "INSERT INTO flyers (id, store_slug, flyer_type, valid_from, valid_to)"
        " VALUES (1, 'maxi', 'weekly', '2026-10-15', '2026-10-21')"
    )
    items = [
        # Unclassified by the classifier, confidently merchandise to
        # the exclusion layer: discarded and counted by reason.
        FlyerItem(name_fr="Cadre photo 8x10", price_value=9.99),
        FlyerItem(name_fr="Pommes", price_value=1.0),
    ]
    stats: dict[str, Any] = {}
    assert insert_items(conn, 1, "maxi", items, stats) == 1
    assert stats["excluded"] == 1
    assert stats["excluded_reasons"] == {"merch:cadre photo": 1}
    conn.close()


# ── dispatch ────────────────────────────────────────────────────────


def test_fetch_store_without_source_reports_error() -> None:
    conn = _conn()
    _add_store(conn, "ghost-store")
    report = fetch_store(conn, "ghost-store")
    assert report["editions"] == 0 and report["items"] == 0
    assert "no flipp source" in report["error"]
    conn.close()


class _FakeMetroDigitalClient:
    editions: list[FlyerEdition] = []

    def fetch_store_editions(self, cfg: MetroDigitalConfig) -> list[FlyerEdition]:
        return list(type(self).editions)


def _md_config(monkeypatch: pytest.MonkeyPatch, slug: str = "test-md") -> None:
    monkeypatch.setattr(
        fetch,
        "_metrodigital_configs",
        {slug: MetroDigitalConfig(slug=slug, config_url="https://example.test/app.json", store_id=1)},
    )
    monkeypatch.setattr(fetch, "MetroDigitalClient", _FakeMetroDigitalClient)


def test_fetch_store_metrodigital_dispatch(monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _conn()
    _add_store(conn, "test-md")
    _md_config(monkeypatch)
    _FakeMetroDigitalClient.editions = [_edition()]
    report = fetch_store(conn, "test-md")
    assert report["editions"] == 1 and report["items"] == 1 and "error" not in report
    # The source row is created on first use and reused afterwards.
    fetch_store(conn, "test-md")
    rows = conn.execute("SELECT COUNT(*) FROM flyer_sources WHERE name = 'metrodigital'").fetchone()
    assert rows[0] == 1
    assert conn.execute("SELECT COUNT(*) FROM flyer_items").fetchone()[0] == 1
    conn.close()


def test_fetch_store_metrodigital_error_is_reported(monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _conn()
    _add_store(conn, "test-md")
    _md_config(monkeypatch)

    class Boom:
        def fetch_store_editions(self, cfg: MetroDigitalConfig) -> list[FlyerEdition]:
            raise MetroDigitalError("api down")

    monkeypatch.setattr(fetch, "MetroDigitalClient", Boom)
    report = fetch_store(conn, "test-md")
    assert report["items"] == 0 and report["error"] == "api down"
    conn.close()


def test_fetch_store_flipp_search_dispatch(monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _conn()
    _add_store(conn, "test-flipp")
    _add_source(conn, "test-flipp", "flipp", '{"merchant_name": "test", "postal_code": "H0H0H0"}')
    seen: dict[str, Any] = {}

    class FakeSearchClient:
        def fetch_store_editions(self, cfg: Any) -> list[FlyerEdition]:
            seen["cfg"] = cfg
            return [_edition()]

    monkeypatch.setattr(fetch, "FlippSearchClient", FakeSearchClient)
    report = fetch_store(conn, "test-flipp")
    assert report["items"] == 1 and "error" not in report
    assert seen["cfg"].merchant_name == "test" and seen["cfg"].postal_code == "H0H0H0"
    conn.close()


def test_fetch_store_cc_dispatch_with_page_error(monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _conn()
    _add_store(conn, "test-cc")
    _add_source(conn, "test-cc", "circulaires.club", '{"cc_slugs": ["test-cc"]}')
    cc_edition = SimpleNamespace(
        cc_slug="test-cc",
        edition_ref="ref-1",
        flyer_type="weekly",
        valid_from=date(2026, 10, 15),
        valid_to=date(2026, 10, 21),
        page_url="https://example.test/flyer",
        page_images=["https://example.test/p1.jpg", "https://example.test/p2.jpg"],
    )

    class FakeCCClient:
        def fetch_current_editions(self, slugs: list[str]) -> list[Any]:
            assert slugs == ["test-cc"]
            return [cc_edition]

    monkeypatch.setattr(fetch, "_shared_cc_client", lambda: FakeCCClient())
    monkeypatch.setattr(
        fetch,
        "_download_image",
        lambda url: (_ for _ in ()).throw(RuntimeError("boom")) if "p2" in url else object(),
    )
    monkeypatch.setattr(
        fetch,
        "_ocr_page",
        lambda *a, **k: [FlyerItem(name_fr="Pommes", price_value=1.0)],
    )
    report = fetch_store(conn, "test-cc")
    assert report["items"] == 1 and "error" not in report
    assert len(report["page_errors"]) == 1 and "p2" in report["page_errors"][0]
    conn.close()


# ── the other source families ───────────────────────────────────────


def test_fetch_store_cc_error_is_reported(monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _conn()
    _add_store(conn, "test-cc")
    _add_source(conn, "test-cc", "circulaires.club", '{"cc_slugs": ["test-cc"]}')

    class BoomCC:
        def fetch_current_editions(self, slugs: list[str]) -> list[Any]:
            raise fetch.CirculairesClubError("cc down")

    monkeypatch.setattr(fetch, "_shared_cc_client", lambda: BoomCC())
    report = fetch_store(conn, "test-cc")
    assert report["items"] == 0 and report["error"] == "cc down"
    conn.close()


def test_fetch_store_search_error_is_reported(monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _conn()
    _add_store(conn, "test-flipp")
    _add_source(conn, "test-flipp", "flipp", '{"merchant_name": "t", "postal_code": "H0H"}')

    class BoomSearch:
        def fetch_store_editions(self, cfg: Any) -> list[FlyerEdition]:
            raise fetch.FlippSearchError("search down")

    monkeypatch.setattr(fetch, "FlippSearchClient", BoomSearch)
    report = fetch_store(conn, "test-flipp")
    assert report["items"] == 0 and report["error"] == "search down"
    conn.close()


def test_fetch_store_flyerkit_dispatch_and_error(monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _conn()
    _add_store(conn, "test-kit")
    _add_source(
        conn,
        "test-kit",
        "flipp",
        '{"brand_slug": "b", "access_token": "t", "store_code": "1"}',
    )

    class FakeKit:
        def fetch_store_editions(self, cfg: Any) -> list[FlyerEdition]:
            assert cfg.brand_slug == "b" and cfg.store_code == "1"
            return [_edition()]

    monkeypatch.setattr(fetch, "FlyerKitClient", FakeKit)
    report = fetch_store(conn, "test-kit")
    assert report["items"] == 1 and "error" not in report

    class BoomKit:
        def fetch_store_editions(self, cfg: Any) -> list[FlyerEdition]:
            raise fetch.FlyerKitError("kit down")

    monkeypatch.setattr(fetch, "FlyerKitClient", BoomKit)
    _add_store(conn, "test-kit2")
    _add_source(conn, "test-kit2", "flipp", '{"brand_slug": "b", "access_token": "t", "store_code": "2"}')
    report2 = fetch_store(conn, "test-kit2")
    assert report2["items"] == 0 and report2["error"] == "kit down"
    conn.close()


def test_fetch_store_official_dispatch(monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _conn()
    _add_store(conn, "test-off")
    from grocery_meta_search.sources.official import OfficialConfig, OfficialEdition

    cfg = OfficialConfig(slug="test-off", kind="woo_specials", source_name="official:test", page_url="https://x.test")
    monkeypatch.setattr(fetch, "_official_configs", {"test-off": cfg})
    edition = OfficialEdition(
        valid_from=date(2026, 10, 15),
        valid_to=date(2026, 10, 21),
        flyer_type="weekly",
        source_ref="off-1",
        languages=["fr"],
        items=[FlyerItem(name_fr="Pommes", price_value=1.5)],
    )

    class FakeOfficial:
        def fetch_editions(self, cfg_: Any) -> list[OfficialEdition]:
            return [edition]

    monkeypatch.setattr(fetch, "OfficialClient", FakeOfficial)
    report = fetch_store(conn, "test-off")
    assert report["items"] == 1 and "error" not in report
    # Source row created by the fetch; a second fetch reuses it.
    fetch_store(conn, "test-off")
    rows = conn.execute("SELECT COUNT(*) FROM flyer_sources WHERE name = 'official:test'").fetchone()
    assert rows[0] == 1
    conn.close()


def test_fetch_store_official_error_is_reported(monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _conn()
    _add_store(conn, "test-off")
    from grocery_meta_search.sources.official import OfficialConfig, OfficialError

    cfg = OfficialConfig(slug="test-off", kind="woo_specials", source_name="official:test", page_url="https://x.test")
    monkeypatch.setattr(fetch, "_official_configs", {"test-off": cfg})

    class BoomOfficial:
        def fetch_editions(self, cfg_: Any) -> list[Any]:
            raise OfficialError("official down")

    monkeypatch.setattr(fetch, "OfficialClient", BoomOfficial)
    report = fetch_store(conn, "test-off")
    assert report["items"] == 0 and report["error"] == "official down"
    conn.close()


# ── ocr glue + CLI ──────────────────────────────────────────────────


def test_ocr_page_stamps_validity(monkeypatch: pytest.MonkeyPatch) -> None:
    from PIL import Image

    monkeypatch.setattr(fetch, "detect_lines", lambda img: [])
    monkeypatch.setattr(
        fetch,
        "segment_page",
        lambda *a, **k: [FlyerItem(name_fr="Pommes", price_value=1.0)],
    )
    items = fetch._ocr_page(
        Image.new("RGB", (10, 10)), fetch.OcrStoreConfig(), "https://x/p.jpg", 3, "2026-10-15", "2026-10-21"
    )
    assert len(items) == 1
    assert items[0].valid_from == "2026-10-15" and items[0].valid_to == "2026-10-21"


def test_download_image_upscales(monkeypatch: pytest.MonkeyPatch) -> None:
    import io

    from PIL import Image

    buf = io.BytesIO()
    Image.new("RGB", (100, 50), "white").save(buf, format="PNG")

    class Resp:
        content = buf.getvalue()

        def raise_for_status(self) -> None:
            return None

    monkeypatch.setattr("requests.get", lambda *a, **k: Resp())
    img = fetch._download_image("https://x.test/p.png", min_width=150)
    assert img.width == 150  # scaled up toward min_width
    # The scale is capped at 2x (engine.upscale_for_ocr max_scale):
    img2 = fetch._download_image("https://x.test/p.png", min_width=4000)
    assert img2.width == 200


def test_run_and_main(monkeypatch: pytest.MonkeyPatch, tmp_path: Any, capsys: Any) -> None:
    from pathlib import Path

    from grocery_meta_search.seed import seed

    db_path = Path(tmp_path) / "run.db"
    seed(db_path, ["maxi"], None, None, None)
    _md_config(monkeypatch, slug="maxi")
    _FakeMetroDigitalClient.editions = [_edition()]
    reports = fetch.run(db_path, ["maxi"])
    assert reports[0]["items"] == 1
    monkeypatch.setattr("sys.argv", ["fetch", "--db", str(db_path), "--slugs", "maxi"])
    fetch.main()
    out = capsys.readouterr().out
    assert "maxi: 1 editions, 0 items" in out  # edition already stored -> skipped


# ── post-fetch stage wiring ─────────────────────────────────────────


def test_fetch_store_harvest_wiring_and_failure(monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _conn()
    _add_store(conn, "test-md")
    _md_config(monkeypatch)
    _FakeMetroDigitalClient.editions = [_edition()]
    import grocery_meta_search.pipeline.harvest as harvest_mod

    monkeypatch.setattr(harvest_mod, "load_harvest_configs", lambda: {"test-md": {}})
    monkeypatch.setattr(
        harvest_mod,
        "harvest_store",
        lambda conn_, slug: {"filled_size": 3, "filled_unit": 1},
    )
    report = fetch_store(conn, "test-md")
    assert report["harvested"] == "+3 size, +1 unit (page harvest)"

    def boom(conn_: Any, slug: str) -> dict[str, int]:
        raise RuntimeError("ocr exploded")

    monkeypatch.setattr(harvest_mod, "harvest_store", boom)
    _FakeMetroDigitalClient.editions = [_edition(ref="E2")]
    report2 = fetch_store(conn, "test-md")
    assert report2["items"] == 1 and report2["harvest_error"] == "ocr exploded"
    conn.close()


def test_fetch_store_multibuy_and_guard_wiring(monkeypatch: pytest.MonkeyPatch) -> None:
    conn = _conn()
    _add_store(conn, "test-md")
    _md_config(monkeypatch)
    _FakeMetroDigitalClient.editions = [_edition()]
    import grocery_meta_search.pipeline.guard as guard_mod
    import grocery_meta_search.pipeline.multibuy as multibuy_mod

    monkeypatch.setattr(multibuy_mod, "load_multibuy_configs", lambda: {"test-md": {}})
    monkeypatch.setattr(multibuy_mod, "multibuy_store", lambda conn_, slug: {"recovered": 2})
    recorded: list[Any] = []
    monkeypatch.setattr(guard_mod, "evaluate_store", lambda conn_, slug: ["W1"])
    monkeypatch.setattr(guard_mod, "record_warnings", lambda conn_, ws: recorded.extend(ws))
    monkeypatch.setattr(guard_mod, "warning_text", lambda w: f"warn:{w}")
    report = fetch_store(conn, "test-md")
    assert report["multibuy"] == "2 multibuy offers recovered (image recovery)"
    assert report["thin_warning"] == "warn:W1"
    assert recorded == ["W1"]
    conn.close()
