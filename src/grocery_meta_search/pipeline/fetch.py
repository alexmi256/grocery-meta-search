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
from datetime import UTC
from pathlib import Path
from typing import Any

from ..classify.exclusion import exclusion_reason
from ..classify.rules import classify_item
from ..classify.taxonomy import UNCLASSIFIED, category_label, is_grocery
from ..db import connect, init_schema
from ..ocr.engine import detect_lines, detect_lines_banded, upscale_for_ocr
from ..ocr.segment import OcrStoreConfig, segment_page
from ..sources.base import FlyerEdition, FlyerItem
from ..sources.circulaires_club import CirculairesClubClient, CirculairesClubError
from ..sources.flipp import BrandConfig, FlyerKitClient, FlyerKitError
from ..sources.flipp_search import FlippSearchClient, FlippSearchError, SearchConfig
from ..sources.official import (
    OfficialClient,
    OfficialConfig,
    OfficialError,
    load_official_configs,
    parse_fr_validity,
    render_pdf_pages,
)
from .fields import extract_package_size

_CC_CONFIG_PATH = Path(__file__).parent.parent / "sources" / "circulaires_club_config.json"
_cc_client: CirculairesClubClient | None = None

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


def get_cc_source(conn: sqlite3.Connection, store_slug: str) -> sqlite3.Row | None:
    row = conn.execute(
        "SELECT * FROM flyer_sources WHERE store_slug = ? AND name = 'circulaires.club'"
        " AND api_config IS NOT NULL LIMIT 1",
        (store_slug,),
    ).fetchone()
    assert row is None or isinstance(row, sqlite3.Row)
    return row


def _cc_ocr_config(store_slug: str) -> OcrStoreConfig:
    overrides: dict[str, Any] = {}
    if _CC_CONFIG_PATH.exists():
        data = json.loads(_CC_CONFIG_PATH.read_text(encoding="utf-8"))
        overrides = data.get(store_slug, {})
    valid = set(OcrStoreConfig.__dataclass_fields__)
    return OcrStoreConfig(**{k: v for k, v in overrides.items() if k in valid})


def _shared_cc_client() -> CirculairesClubClient:
    global _cc_client
    if _cc_client is None:
        _cc_client = CirculairesClubClient()
    return _cc_client


def _download_image(page_url: str, min_width: int = 1600) -> Any:
    """Download one flyer page image, upscaled for OCR."""
    import io

    import requests
    from PIL import Image

    resp = requests.get(
        page_url,
        timeout=60,
        headers={"User-Agent": "Mozilla/5.0 (compatible; grocery-meta-search/0.1)"},
    )
    resp.raise_for_status()
    opened = Image.open(io.BytesIO(resp.content))
    opened.load()
    return upscale_for_ocr(opened.convert("RGB"), min_width=min_width)


def _ocr_page(
    image: Any,
    ocr_cfg: OcrStoreConfig,
    page_url: str,
    page_number: int,
    valid_from: str,
    valid_to: str,
) -> list[FlyerItem]:
    lines = detect_lines_banded(image) if image.height > 2800 else detect_lines(image)
    items: list[FlyerItem] = []
    for item in segment_page(image, lines, ocr_cfg, page_url=page_url, page_number=page_number):
        item.valid_from = valid_from
        item.valid_to = valid_to
        items.append(item)
    return items


def fetch_store_cc(
    conn: sqlite3.Connection, src: sqlite3.Row, store_slug: str, cfg_data: dict[str, Any]
) -> dict[str, Any]:
    """Fetch a store's flyers from circulaires.club and OCR the pages."""
    report: dict[str, Any] = {"store": store_slug, "editions": 0, "items": 0}
    client = _shared_cc_client()
    ocr_cfg = _cc_ocr_config(store_slug)
    try:
        cc_editions = client.fetch_current_editions(list(cfg_data["cc_slugs"]))
    except CirculairesClubError as exc:
        report["error"] = str(exc)
        return report
    editions: list[FlyerEdition] = []
    for cc_edition in cc_editions:
        items: list[FlyerItem] = []
        for page_number, page_url in enumerate(cc_edition.page_images, start=1):
            try:
                image = _download_image(page_url)
            except Exception as exc:  # one bad page should not sink the edition
                report.setdefault("page_errors", []).append(f"{page_url}: {exc}")
                continue
            items.extend(
                _ocr_page(
                    image,
                    ocr_cfg,
                    page_url,
                    page_number,
                    cc_edition.valid_from.isoformat(),
                    cc_edition.valid_to.isoformat(),
                )
            )
        editions.append(
            FlyerEdition(
                valid_from=cc_edition.valid_from.isoformat(),
                valid_to=cc_edition.valid_to.isoformat(),
                flyer_type=cc_edition.flyer_type,
                source_ref=cc_edition.edition_ref,
                languages=["fr"],
                raw={"cc_slug": cc_edition.cc_slug, "page_url": cc_edition.page_url},
                items=items,
            )
        )
    return store_editions(conn, src, store_slug, editions, report)


def get_official_source(
    conn: sqlite3.Connection, store_slug: str, source_name: str
) -> sqlite3.Row | None:
    row = conn.execute(
        "SELECT * FROM flyer_sources WHERE store_slug = ? AND name = ? LIMIT 1",
        (store_slug, source_name),
    ).fetchone()
    assert row is None or isinstance(row, sqlite3.Row)
    return row


def get_or_create_official_source(conn: sqlite3.Connection, cfg: OfficialConfig) -> sqlite3.Row:
    """Group-4 stores were never seeded into flyer_sources; create the row."""
    row = get_official_source(conn, cfg.slug, cfg.source_name)
    if row is not None:
        return row
    fmt = {
        "image_page": "images",
        "pdf_page": "pdf",
        "pdf_text": "pdf",
        "woo_specials": "json-api",
        "flyerify": "html",
        "circulaires": "images",
        "flyerbox": "images",
    }[cfg.kind]
    source_kind = "aggregator" if cfg.source_name.startswith("aggregator:") else "official"
    conn.execute(
        """
        INSERT INTO flyer_sources
            (store_slug, flyer_type, name, url, kind, format, fetchability, languages)
        VALUES (?, ?, ?, ?, ?, ?, 'http', ?)
        """,
        (
            cfg.slug,
            cfg.flyer_type,
            cfg.source_name,
            cfg.page_url,
            source_kind,
            fmt,
            json.dumps(cfg.languages, ensure_ascii=False),
        ),
    )
    conn.commit()
    created = get_official_source(conn, cfg.slug, cfg.source_name)
    assert created is not None
    return created


_official_configs: dict[str, OfficialConfig] | None = None


def _get_official_config(store_slug: str) -> OfficialConfig | None:
    global _official_configs
    if _official_configs is None:
        _official_configs = load_official_configs()
    return _official_configs.get(store_slug)


def _official_ocr_config(cfg: OfficialConfig) -> OcrStoreConfig:
    valid = set(OcrStoreConfig.__dataclass_fields__)
    return OcrStoreConfig(**{k: v for k, v in cfg.ocr.items() if k in valid})


def fetch_store_official(
    conn: sqlite3.Connection, store_slug: str, cfg: OfficialConfig
) -> dict[str, Any]:
    """Fetch a store's flyer from its official platform (group 4)."""
    from datetime import date as date_cls

    import requests

    report: dict[str, Any] = {"store": store_slug, "editions": 0, "items": 0}
    src = get_or_create_official_source(conn, cfg)
    try:
        official_editions = OfficialClient().fetch_editions(cfg)
    except OfficialError as exc:
        report["error"] = str(exc)
        return report
    ocr_cfg = _official_ocr_config(cfg)
    editions: list[FlyerEdition] = []
    for off in official_editions:
        items: list[FlyerItem] = list(off.items)
        valid_from, valid_to = off.valid_from.isoformat(), off.valid_to.isoformat()
        pages: list[tuple[str, Any]] = []
        if off.pdf_url is not None:
            try:
                resp = requests.get(
                    off.pdf_url,
                    timeout=120,
                    headers={"User-Agent": "Mozilla/5.0 (compatible; grocery-meta-search/0.1)"},
                )
                resp.raise_for_status()
                for n, image in enumerate(render_pdf_pages(resp.content), start=1):
                    pages.append((f"{off.pdf_url}#page={n}", upscale_for_ocr(image)))
            except Exception as exc:
                report.setdefault("page_errors", []).append(f"{off.pdf_url}: {exc}")
        for page_url in off.page_images:
            try:
                min_width = int(cfg.image.get("upscale_min_width", 2000))
                pages.append((page_url, _download_image(page_url, min_width=min_width)))
            except Exception as exc:  # one bad page should not sink the edition
                report.setdefault("page_errors", []).append(f"{page_url}: {exc}")
        first_lines = None
        if pages and cfg.kind in ("image_page", "pdf_page"):
            # Many official flyers print their real validity on page 1; it
            # beats every fallback (fetch week, URL month).
            first_image = pages[0][1]
            first_lines = (
                detect_lines_banded(first_image)
                if first_image.height > 2800
                else detect_lines(first_image)
            )
            rng = parse_fr_validity(" ".join(ln.text for ln in first_lines), date_cls.today())
            if rng is not None:
                valid_from, valid_to = rng[0].isoformat(), rng[1].isoformat()
        for page_number, (page_ref, image) in enumerate(pages, start=1):
            if page_number == 1 and first_lines is not None:
                for item in segment_page(
                    image, first_lines, ocr_cfg, page_url=page_ref, page_number=1
                ):
                    item.valid_from, item.valid_to = valid_from, valid_to
                    items.append(item)
            else:
                items.extend(_ocr_page(image, ocr_cfg, page_ref, page_number, valid_from, valid_to))
        editions.append(
            FlyerEdition(
                valid_from=valid_from,
                valid_to=valid_to,
                flyer_type=off.flyer_type,
                source_ref=off.source_ref,
                languages=off.languages,
                raw={"kind": cfg.kind, "page_url": cfg.page_url},
                items=items,
            )
        )
    return store_editions(conn, src, store_slug, editions, report)


def fetch_store_flyerkit(
    conn: sqlite3.Connection, src: sqlite3.Row, store_slug: str, cfg_data: dict[str, Any]
) -> dict[str, Any]:
    report: dict[str, Any] = {"store": store_slug, "editions": 0, "items": 0}
    cfg = BrandConfig(
        store_slug=store_slug,
        brand_slug=cfg_data["brand_slug"],
        access_token=cfg_data["access_token"],
        store_code=cfg_data["store_code"],
        flyer_type_filter=cfg_data.get("flyer_type_filter"),
    )
    try:
        editions = FlyerKitClient().fetch_store_editions(cfg)
    except FlyerKitError as exc:
        report["error"] = str(exc)
        return report
    return store_editions(conn, src, store_slug, editions, report)


def fetch_store_search(
    conn: sqlite3.Connection, src: sqlite3.Row, store_slug: str, cfg_data: dict[str, Any]
) -> dict[str, Any]:
    report: dict[str, Any] = {"store": store_slug, "editions": 0, "items": 0}
    cfg = SearchConfig(
        store_slug=store_slug,
        merchant_name=cfg_data["merchant_name"],
        postal_code=cfg_data["postal_code"],
    )
    try:
        editions = FlippSearchClient().fetch_store_editions(cfg)
    except FlippSearchError as exc:
        report["error"] = str(exc)
        return report
    return store_editions(conn, src, store_slug, editions, report)


def store_editions(
    conn: sqlite3.Connection,
    src: sqlite3.Row,
    store_slug: str,
    editions: list[FlyerEdition],
    report: dict[str, Any],
) -> dict[str, Any]:
    for edition in editions:
        flyer_id, is_new = upsert_edition(conn, store_slug, int(src["id"]), edition)
        report["editions"] += 1
        if is_new:
            stats: dict[str, Any] = {}
            report["items"] += insert_items(conn, flyer_id, store_slug, edition.items, stats)
            report["discarded"] = report.get("discarded", 0) + stats.get("discarded", 0)
            report["excluded"] = report.get("excluded", 0) + stats.get("excluded", 0)
        else:
            report["skipped"] = report.get("skipped", 0) + len(edition.items)
    conn.commit()
    return report


def fetch_store(conn: sqlite3.Connection, store_slug: str) -> dict[str, Any]:
    """Fetch active flyers for one store. Returns a small report dict.

    After the source fetch, stores enabled in harvest_config.json get
    the page-harvest stage (pipeline/harvest.py): sizes/units that
    exist only in the flyer image are OCR'd from each item's cell and
    filled in. A harvest failure never fails the fetch.
    """
    report = _fetch_store_sources(conn, store_slug)
    if not report.get("error"):
        from .harvest import harvest_store, load_harvest_configs

        if store_slug in load_harvest_configs():
            try:
                stats = harvest_store(conn, store_slug)
                if stats["filled_size"] or stats["filled_unit"]:
                    report["harvested"] = (
                        f"+{stats['filled_size']} size, "
                        f"+{stats['filled_unit']} unit (page harvest)"
                    )
            except Exception as exc:  # noqa: BLE001 — report, never fail the fetch
                report["harvest_error"] = str(exc)
    return report


def _fetch_store_sources(conn: sqlite3.Connection, store_slug: str) -> dict[str, Any]:
    cc_src = get_cc_source(conn, store_slug)
    if cc_src is not None:
        return fetch_store_cc(conn, cc_src, store_slug, json.loads(cc_src["api_config"]))
    official_cfg = _get_official_config(store_slug)
    if official_cfg is not None:
        return fetch_store_official(conn, store_slug, official_cfg)
    src = get_flipp_source(conn, store_slug)
    if src is None or not src["api_config"]:
        return {
            "store": store_slug,
            "editions": 0,
            "items": 0,
            "error": "no flipp source with api_config",
        }
    cfg_data = json.loads(src["api_config"])
    if "brand_slug" in cfg_data:
        return fetch_store_flyerkit(conn, src, store_slug, cfg_data)
    if "merchant_name" in cfg_data:
        return fetch_store_search(conn, src, store_slug, cfg_data)
    return {
        "store": store_slug,
        "editions": 0,
        "items": 0,
        "error": f"unknown api_config shape: {sorted(cfg_data)}",
    }


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
          AND COALESCE(source_ref, '') = COALESCE(?, '')
          AND COALESCE(valid_from, '') = COALESCE(?, '')
          AND COALESCE(valid_to, '') = COALESCE(?, '')
          AND COALESCE(flyer_source_id, -1) = COALESCE(?, -1)
        """,
        (
            store_slug,
            edition.flyer_type,
            edition.source_ref,
            edition.valid_from,
            edition.valid_to,
            source_id,
        ),
    ).fetchone()
    if row:
        return int(row["id"]), False
    cur = conn.execute(
        """
        INSERT INTO flyers (store_slug, flyer_source_id, flyer_type, source_ref,
                            valid_from, valid_to, languages, fetch_status, raw)
        VALUES (?, ?, ?, ?, ?, ?, ?, 'ok', ?)
        """,
        (
            store_slug,
            source_id,
            edition.flyer_type,
            edition.source_ref,
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
    conn: sqlite3.Connection,
    flyer_id: int,
    store_slug: str,
    items: list[FlyerItem],
    stats: dict[str, Any] | None = None,
) -> int:
    """Insert one edition's items, classifying each on the way in.

    Grocery items are kept with their category label plus a
    classification provenance row. Items classified as non-grocery
    (Pet, Household, Health & Beauty, Baby Care) are discarded and
    counted in stats["discarded"] when a stats dict is supplied.
    Unclassified items are KEPT (category 'Unclassified') for human
    review — an inconclusive classification is not evidence that an
    item is not grocery (2026-10-16 decision) — UNLESS the exclusion
    layer (classify/exclusion.py) confidently identifies them as
    merchandise, flyer furniture or garble; those are discarded and
    counted in stats["excluded"] with per-reason counts in
    stats["excluded_reasons"] (wired 2026-10-16 on Alex's approval;
    validated at 0 false fires on grocery ground truth, the 7 apparent
    fires all being ground-truth labelling noise).
    """
    from datetime import datetime

    now = datetime.now(UTC).isoformat(timespec="seconds")
    count = 0
    for item in items:
        dept, sub, method, rule_id = classify_item(
            item.name_fr, item.name_en, item.brand, store_slug
        )
        if dept != UNCLASSIFIED and not is_grocery(dept, sub):
            if stats is not None:
                stats["discarded"] = stats.get("discarded", 0) + 1
            continue
        if dept == UNCLASSIFIED:
            reason = exclusion_reason(item.name_fr, item.name_en, item.brand)
            if reason is not None:
                if stats is not None:
                    stats["excluded"] = stats.get("excluded", 0) + 1
                    reasons = stats.setdefault("excluded_reasons", {})
                    reasons[reason] = reasons.get(reason, 0) + 1
                continue
        label = UNCLASSIFIED if dept == UNCLASSIFIED else category_label(dept, sub)
        key = item_key(store_slug, item)
        cur = conn.execute(
            """
            INSERT INTO flyer_items
                (flyer_id, store_slug, item_key, name_fr, name_en, price_text,
                 price_value, price_unit, valid_from, valid_to, languages,
                 image_url, bbox, sku, brand, package_size, conditions, loyalty_gated, raw,
                 confidence, category)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                item.package_size
                or extract_package_size(item.name_fr, item.name_en),
                json.dumps(item.conditions, ensure_ascii=False),
                1 if item.loyalty_gated else 0,
                json.dumps(item.raw, ensure_ascii=False),
                item.confidence,
                label,
            ),
        )
        conn.execute(
            "INSERT INTO item_classifications VALUES (?,?,?,?,?,?)",
            (cur.lastrowid, dept, sub, method, rule_id, now),
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


def run(db_path: Path, slugs: list[str]) -> list[dict[str, Any]]:
    conn = connect(db_path)
    init_schema(conn)
    reports = [fetch_store(conn, slug) for slug in slugs]
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
        disc = (
            f", {report['discarded']} discarded as non-grocery" if report.get("discarded") else ""
        )
        if report.get("excluded"):
            disc += f", {report['excluded']} excluded (furniture/merch/garble)"
        if report.get("harvested"):
            disc += f", {report['harvested']}"
        print(
            f"{report['store']}: {report['editions']} editions, {report['items']} items{disc}{err}"
        )


if __name__ == "__main__":
    main()
