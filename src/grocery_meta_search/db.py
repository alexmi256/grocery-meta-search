"""SQLite database helpers."""

from __future__ import annotations

import sqlite3
from pathlib import Path

SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def connect(db_path: str | Path) -> sqlite3.Connection:
    """Open a SQLite connection with sane defaults."""
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    """Create all tables (idempotent) and apply additive migrations."""
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    _migrate(conn)
    conn.commit()


# Additive column migrations for databases created before the column
# existed: (table, column, DDL type). CREATE TABLE in schema.sql
# already carries them for fresh databases.
_MIGRATIONS = [
    ("flyer_items", "package_size", "TEXT"),
    ("flyer_items", "unit_quantity", "REAL NOT NULL DEFAULT 1"),
    ("flyer_items", "unit_measurement", "TEXT NOT NULL DEFAULT 'each'"),
]


def _migrate(conn: sqlite3.Connection) -> None:
    for table, column, ddl in _MIGRATIONS:
        cols = {row[1] for row in conn.execute(f"PRAGMA table_info({table})")}
        if cols and column not in cols:
            conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {ddl}")
