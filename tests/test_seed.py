"""Seed-from-YAML tests (sample stores only)."""

from pathlib import Path

from grocery_meta_search.db import connect
from grocery_meta_search.seed import seed

BRANDS = Path(__file__).parent.parent / "src" / "grocery_meta_search" / "sources" / "flipp_brands.json"


def test_seed_sample_stores(tmp_path: Path) -> None:
    db_path = tmp_path / "test.db"
    stats = seed(db_path, ["maxi", "iga", "provigo"], BRANDS)
    assert stats["stores"] == 3
    assert stats["sources"] > 3

    conn = connect(db_path)
    slugs = {r[0] for r in conn.execute("SELECT slug FROM stores")}
    assert slugs == {"maxi", "iga", "provigo"}
    flipp = conn.execute("SELECT store_slug, api_config FROM flyer_sources WHERE name = 'flipp'").fetchall()
    assert {r[0] for r in flipp} == {"maxi", "iga", "provigo"}
    assert all(r[1] and "access_token" in r[1] for r in flipp)
    conn.close()
