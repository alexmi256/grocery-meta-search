-- Grocery meta search engine — SQLite schema (Phase 3).
-- Conventions: slug TEXT PK for stores; small vocabularies as TEXT;
-- multi-value fields as JSON TEXT; timestamps TEXT ISO-8601.

CREATE TABLE IF NOT EXISTS stores (
    slug TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    name_variants TEXT,              -- JSON array
    store_type TEXT,                 -- traditional | ethnic-specialty | warehouse | pharmacy | gen-merch | dollar | other
    footprint TEXT,                  -- island | greater | qc-confirmed | qc-unverified
    tier INTEGER,                    -- 1 | 2 | 3
    website_url TEXT,
    parent_company TEXT,
    affiliation TEXT,                -- corporate | independent-affiliate | banner-group
    excluded INTEGER NOT NULL DEFAULT 0,
    research_status TEXT,            -- complete | partial | minimal
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);
CREATE INDEX IF NOT EXISTS idx_stores_type ON stores(store_type);

CREATE TABLE IF NOT EXISTS flyer_sources (
    id INTEGER PRIMARY KEY,
    store_slug TEXT NOT NULL REFERENCES stores(slug),
    flyer_type TEXT NOT NULL DEFAULT 'weekly',
    name TEXT NOT NULL,              -- canonical source name, e.g. 'flipp'
    url TEXT,
    kind TEXT,                       -- official | aggregator
    format TEXT,                     -- html | pdf | images | json-api
    parse_friendliness TEXT,          -- high | medium | low
    fetchability TEXT,               -- http | browser-needed | blocked
    languages TEXT,                  -- JSON array
    api_config TEXT,                 -- JSON: brand tokens, store codes, endpoints
    notes TEXT
);
CREATE INDEX IF NOT EXISTS idx_flyer_sources_store ON flyer_sources(store_slug);
CREATE INDEX IF NOT EXISTS idx_flyer_sources_kind_fetch ON flyer_sources(kind, fetchability);

CREATE TABLE IF NOT EXISTS flyers (
    id INTEGER PRIMARY KEY,
    store_slug TEXT NOT NULL REFERENCES stores(slug),
    flyer_source_id INTEGER REFERENCES flyer_sources(id),
    flyer_type TEXT NOT NULL DEFAULT 'weekly',
    source_ref TEXT,                 -- source-native edition ID (FlyerKit publication ID, Flipp flyer ID)
    valid_from TEXT,                 -- ISO date
    valid_to TEXT,                   -- ISO date
    flip_weekday TEXT,
    flip_timezone TEXT NOT NULL DEFAULT 'America/Toronto',
    per_store_variant INTEGER NOT NULL DEFAULT 0,
    languages TEXT,                  -- JSON array
    archive_url TEXT,
    content_hash TEXT,
    fetch_status TEXT NOT NULL DEFAULT 'ok',  -- ok | failed | blocked
    fetched_at TEXT,
    raw TEXT,                        -- JSON: raw edition metadata
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_flyers_edition
    ON flyers(store_slug, flyer_type, COALESCE(source_ref, ''), COALESCE(valid_from, ''), COALESCE(valid_to, ''), COALESCE(flyer_source_id, -1));
CREATE INDEX IF NOT EXISTS idx_flyers_valid ON flyers(store_slug, valid_from);

CREATE TABLE IF NOT EXISTS flyer_items (
    id INTEGER PRIMARY KEY,
    flyer_id INTEGER NOT NULL REFERENCES flyers(id),
    store_slug TEXT NOT NULL,
    item_key TEXT NOT NULL,          -- stable identity for price history
    name_fr TEXT,
    name_en TEXT,
    price_text TEXT,                 -- raw as shown in the flyer
    price_value REAL,                -- parsed unit price
    price_unit TEXT,                 -- each | lb | kg | g
    valid_from TEXT,                 -- ISO date (item-level when available)
    valid_to TEXT,
    languages TEXT,                  -- JSON array
    image_url TEXT,
    image_hash TEXT,
    bbox TEXT,                       -- JSON {left, top, right, bottom, page}
    sku TEXT,
    brand TEXT,
    package_size TEXT,               -- as printed: "454 g", "2 lb", "24x60 g", "3 PCS"
    section TEXT,                    -- flyer department, signal for Phase 4
    conditions TEXT,                 -- JSON: sub-periods, limits, loyalty gating
    loyalty_gated INTEGER NOT NULL DEFAULT 0,
    raw TEXT,                        -- JSON: raw product payload
    confidence REAL NOT NULL DEFAULT 1.0,
    category TEXT NOT NULL DEFAULT 'Unclassified',
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);
CREATE INDEX IF NOT EXISTS idx_items_flyer ON flyer_items(flyer_id);
CREATE INDEX IF NOT EXISTS idx_items_key ON flyer_items(item_key);

CREATE TABLE IF NOT EXISTS price_observations (
    id INTEGER PRIMARY KEY,
    item_key TEXT NOT NULL,
    store_slug TEXT NOT NULL,
    flyer_id INTEGER REFERENCES flyers(id),
    price_value REAL,
    price_text TEXT,
    valid_from TEXT,
    valid_to TEXT,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);
CREATE INDEX IF NOT EXISTS idx_obs_key ON price_observations(item_key, valid_from);

CREATE TABLE IF NOT EXISTS item_classifications (
    item_id INTEGER PRIMARY KEY REFERENCES flyer_items(id),
    department TEXT NOT NULL,
    subcategory TEXT NOT NULL,
    method TEXT NOT NULL,            -- rule | frozen-remap | store-prior | none
    rule_id TEXT NOT NULL,
    classified_at TEXT NOT NULL
);
