"""
Persistencia SQLite WAL Local para CPAZ Media OS (Separada 100% de fichas clínicas).

¿Qué es?
Capa mínima de almacenamiento local usando `sqlite3` estándar con modo WAL (`busy_timeout=5000`)
y permisos privados (`0700` carpeta, `0600` base de datos).

¿Para qué lo usamos?
Evita levantar servidores PostgreSQL/Redis adicionales de 2-4 GB (Postiz/Activepieces)
manteniendo persistencia transaccional para investigación, calendario editorial, auditoría de
aprobaciones `PUBLICAR <ID>`, métricas anónimas y atribución de consultas comerciales.
"""

from __future__ import annotations

import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, Optional

from media_os.privacy import assert_path_not_clinical

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MEDIA_OS_DB = ROOT / "data" / "media_os" / "media_os.db"


def resolve_db_path(db_path: Optional[Path | str] = None) -> Path:
    if db_path is not None:
        target = Path(db_path)
    else:
        env = os.getenv("CPAZ_MEDIA_OS_DB_PATH")
        target = Path(env) if env else DEFAULT_MEDIA_OS_DB
    assert_path_not_clinical(target)
    return target


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _ensure_private_paths(db_file: Path) -> None:
    db_file.parent.mkdir(parents=True, exist_ok=True)
    try:
        os.chmod(db_file.parent, 0o700)
    except OSError:
        pass
    if db_file.exists():
        try:
            os.chmod(db_file, 0o600)
        except OSError:
            pass


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS research_briefs (
            brief_id TEXT PRIMARY KEY,
            topic_key TEXT NOT NULL,
            audience TEXT NOT NULL,
            objective TEXT NOT NULL,
            source_engine TEXT NOT NULL,
            brief_json TEXT NOT NULL,
            qa_passed INTEGER NOT NULL,
            qa_notes_json TEXT NOT NULL,
            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS editorial_items (
            item_id TEXT PRIMARY KEY,
            topic_key TEXT NOT NULL,
            title TEXT NOT NULL,
            channel TEXT NOT NULL,
            format_type TEXT NOT NULL,
            caption TEXT NOT NULL,
            media_path TEXT NOT NULL,
            utm_url TEXT NOT NULL,
            status TEXT NOT NULL,
            qa_passed INTEGER NOT NULL DEFAULT 0,
            qa_issues_json TEXT NOT NULL DEFAULT '[]',
            scheduled_for TEXT,
            approval_token TEXT,
            approved_by TEXT,
            approved_at TEXT,
            published_at TEXT,
            publish_receipt_json TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE INDEX IF NOT EXISTS idx_editorial_status ON editorial_items(status);
        CREATE INDEX IF NOT EXISTS idx_editorial_topic ON editorial_items(topic_key);

        CREATE TABLE IF NOT EXISTS approval_audit (
            audit_id TEXT PRIMARY KEY,
            item_id TEXT NOT NULL,
            decision TEXT NOT NULL,
            approval_token TEXT NOT NULL,
            reviewer TEXT NOT NULL,
            reason TEXT NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY(item_id) REFERENCES editorial_items(item_id)
        );

        CREATE TABLE IF NOT EXISTS content_metrics (
            metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id TEXT,
            topic_key TEXT NOT NULL,
            channel TEXT NOT NULL,
            utm_campaign TEXT NOT NULL,
            impressions INTEGER NOT NULL DEFAULT 0,
            clicks INTEGER NOT NULL DEFAULT 0,
            saves INTEGER NOT NULL DEFAULT 0,
            shares INTEGER NOT NULL DEFAULT 0,
            source_system TEXT NOT NULL DEFAULT 'cpaz_local',
            recorded_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS attribution_inquiries (
            inquiry_id TEXT PRIMARY KEY,
            utm_source TEXT NOT NULL,
            utm_medium TEXT NOT NULL,
            utm_campaign TEXT NOT NULL,
            utm_content TEXT NOT NULL,
            topic_key TEXT NOT NULL,
            inquiry_channel TEXT NOT NULL,
            converted_booking INTEGER NOT NULL DEFAULT 0,
            estimated_value_clp INTEGER NOT NULL DEFAULT 0,
            recorded_at TEXT NOT NULL
        );
        """
    )


@contextmanager
def get_connection(db_path: Optional[Path | str] = None, *, write: bool = False) -> Iterator[sqlite3.Connection]:
    target = resolve_db_path(db_path)
    _ensure_private_paths(target)
    conn = sqlite3.connect(str(target), timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode = WAL;")
    conn.execute("PRAGMA busy_timeout = 5000;")
    conn.execute("PRAGMA foreign_keys = ON;")
    init_schema(conn)
    _ensure_private_paths(target)
    try:
        if write:
            conn.execute("BEGIN IMMEDIATE;")
        yield conn
        if write:
            conn.commit()
    except Exception:
        if write and conn.in_transaction:
            conn.rollback()
        raise
    finally:
        conn.close()
