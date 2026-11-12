"""
Calendario Editorial y Puerta Obligatoria de Aprobación — CPAZ Media OS.

¿Qué es?
Máquina de estados persistida en SQLite WAL (`DRAFT -> CLINICAL_QA -> APPROVED -> SCHEDULED -> PUBLISHED_DRYRUN | REJECTED`)
con registro inmutable en `approval_audit`.

¿Para qué lo usamos?
Garantiza el cumplimiento estricto de `No publicar contenido sin aprobación`: ninguna pieza puede
programarse, exportarse a n8n ni enviarse a un adaptador de publicación sin QA clínico válido y
una confirmación explícita `PUBLICAR <ITEM_ID>` o `AUTORIZO <ITEM_ID>`.
"""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional

from agent import content_engine
from media_os.intelligence import run_clinical_qa
from media_os.privacy import assert_no_pii
from media_os.storage import get_connection, utc_now_iso

VALID_CHANNELS = ("instagram", "facebook", "tiktok", "threads", "blog")
VALID_FORMATS = ("feed_png", "reel_mp4", "thread", "community_post", "article")


class ApprovalRequiredError(PermissionError):
    """Error lanzado al intentar programar, exportar o publicar contenido sin aprobación vigente."""


def _validate_approval_token(item_id: str, approval_token: str) -> bool:
    raw = (approval_token or "").strip()
    if not raw:
        return False
    # Rechaza explícitamente negaciones
    if re.search(r"\b(?:no\s+autorizo|no\s+publicar|cancelar|rechazar)\b", raw, flags=re.IGNORECASE):
        return False
    pattern = re.compile(rf"^(?:PUBLICAR|AUTORIZO)\s+{re.escape(item_id)}$", re.IGNORECASE)
    return bool(pattern.match(raw))


class EditorialCalendar:
    """Administra el ciclo de vida completo de piezas editoriales de Centro Paz."""

    def __init__(self, db_path: Optional[Path | str] = None) -> None:
        self.db_path = db_path

    def create_draft(
        self,
        *,
        topic_key: str,
        title: str,
        channel: str,
        format_type: str,
        caption: str,
        media_path: str,
        utm_url: str,
        item_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        if channel not in VALID_CHANNELS:
            raise ValueError(f"Canal inválido '{channel}'. Permitidos: {VALID_CHANNELS}")
        if format_type not in VALID_FORMATS:
            raise ValueError(f"Formato inválido '{format_type}'. Permitidos: {VALID_FORMATS}")

        assert_no_pii(
            {
                "topic_key": topic_key,
                "title": title,
                "caption": caption,
                "media_path": media_path,
                "utm_url": utm_url,
            },
            field_path="editorial_draft",
        )

        eid = item_id or f"cpaz-{uuid.uuid4().hex[:8]}"
        now = utc_now_iso()
        with get_connection(self.db_path, write=True) as conn:
            conn.execute(
                """
                INSERT INTO editorial_items (
                    item_id, topic_key, title, channel, format_type, caption,
                    media_path, utm_url, status, qa_passed, qa_issues_json,
                    created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'DRAFT', 0, '[]', ?, ?)
                """,
                (eid, topic_key, title.strip(), channel, format_type, caption.strip(), media_path, utm_url, now, now),
            )
        return self.get_item(eid)  # type: ignore[return-value]

    def seed_from_weekly_plan(self, *, week: int = 1, channel: str = "instagram") -> List[Dict[str, Any]]:
        """Importa los 7 tópicos semanales ya existentes de `content_engine` como borradores `DRAFT`."""
        plan = content_engine.get_weekly_calendar(week=week)
        created: List[Dict[str, Any]] = []
        existing = {item["topic_key"] for item in self.list_items(limit=200)}
        for entry in plan:
            tkey = entry["topic_key"]
            if tkey in existing:
                continue
            item = self.create_draft(
                topic_key=tkey,
                title=entry["titulo"],
                channel=channel,
                format_type="feed_png",
                caption=entry["copy"],
                media_path=f"assets/instagram/post_{entry['id']:02d}_{tkey}.png",
                utm_url=f"https://www.centropaz.cl/?utm_source={channel}&utm_medium=organic&utm_campaign=sem{week}_{tkey}",
            )
            created.append(item)
        return created

    def run_qa(self, item_id: str) -> Dict[str, Any]:
        item = self.get_item(item_id)
        if not item:
            raise KeyError(f"Pieza editorial '{item_id}' no encontrada.")
        qa = run_clinical_qa(title=item["title"], caption=item["caption"], require_cta=True)
        new_status = "CLINICAL_QA" if qa.passed else "DRAFT"
        now = utc_now_iso()
        with get_connection(self.db_path, write=True) as conn:
            conn.execute(
                """
                UPDATE editorial_items
                SET qa_passed = ?, qa_issues_json = ?, status = ?, updated_at = ?
                WHERE item_id = ?
                """,
                (1 if qa.passed else 0, json.dumps(qa.issues, ensure_ascii=False), new_status, now, item_id),
            )
        updated = self.get_item(item_id)
        assert updated is not None
        updated["qa_warnings"] = qa.warnings
        return updated

    def approve_item(
        self,
        item_id: str,
        *,
        approval_token: str,
        reviewer: str = "Nicolas",
        reason: str = "Revisión clínica y marca aprobada",
    ) -> Dict[str, Any]:
        item = self.get_item(item_id)
        if not item:
            raise KeyError(f"Pieza editorial '{item_id}' no encontrada.")
        if not item["qa_passed"]:
            qa_check = self.run_qa(item_id)
            if not qa_check["qa_passed"]:
                raise ApprovalRequiredError(
                    f"La pieza '{item_id}' no aprobó QA clínico: {'; '.join(qa_check['qa_issues'])}"
                )
        if not _validate_approval_token(item_id, approval_token):
            raise ApprovalRequiredError(
                f"Token de autorización inválido. Se exige formato exacto 'PUBLICAR {item_id}' o 'AUTORIZO {item_id}'."
            )

        now = utc_now_iso()
        audit_id = f"aud-{uuid.uuid4().hex[:10]}"
        with get_connection(self.db_path, write=True) as conn:
            conn.execute(
                """
                UPDATE editorial_items
                SET status = 'APPROVED',
                    approval_token = ?,
                    approved_by = ?,
                    approved_at = ?,
                    updated_at = ?
                WHERE item_id = ?
                """,
                (approval_token.strip(), reviewer.strip(), now, now, item_id),
            )
            conn.execute(
                """
                INSERT INTO approval_audit (audit_id, item_id, decision, approval_token, reviewer, reason, created_at)
                VALUES (?, ?, 'APPROVED', ?, ?, ?, ?)
                """,
                (audit_id, item_id, approval_token.strip(), reviewer.strip(), reason.strip(), now),
            )
        return self.get_item(item_id)  # type: ignore[return-value]

    def reject_item(
        self,
        item_id: str,
        *,
        reviewer: str = "Nicolas",
        reason: str = "Ajustar tono o enfoque clínico",
    ) -> Dict[str, Any]:
        item = self.get_item(item_id)
        if not item:
            raise KeyError(f"Pieza editorial '{item_id}' no encontrada.")
        now = utc_now_iso()
        audit_id = f"aud-{uuid.uuid4().hex[:10]}"
        with get_connection(self.db_path, write=True) as conn:
            conn.execute(
                """
                UPDATE editorial_items
                SET status = 'REJECTED', approval_token = NULL, approved_by = NULL, updated_at = ?
                WHERE item_id = ?
                """,
                (now, item_id),
            )
            conn.execute(
                """
                INSERT INTO approval_audit (audit_id, item_id, decision, approval_token, reviewer, reason, created_at)
                VALUES (?, ?, 'REJECTED', 'REJECTED', ?, ?, ?)
                """,
                (audit_id, item_id, reviewer.strip(), reason.strip(), now),
            )
        return self.get_item(item_id)  # type: ignore[return-value]

    def schedule_item(self, item_id: str, *, scheduled_for: str) -> Dict[str, Any]:
        item = self.get_item(item_id)
        if not item:
            raise KeyError(f"Pieza editorial '{item_id}' no encontrada.")
        if item["status"] not in ("APPROVED", "SCHEDULED") or not item["approval_token"]:
            raise ApprovalRequiredError(
                f"Bloqueado: '{item_id}' está en estado '{item['status']}'. Requiere aprobación explícita 'PUBLICAR {item_id}'."
            )
        if not _validate_approval_token(item_id, item["approval_token"]):
            raise ApprovalRequiredError(f"Token de aprobación corrupto o inválido para '{item_id}'.")

        now = utc_now_iso()
        with get_connection(self.db_path, write=True) as conn:
            conn.execute(
                """
                UPDATE editorial_items
                SET status = 'SCHEDULED', scheduled_for = ?, updated_at = ?
                WHERE item_id = ?
                """,
                (scheduled_for.strip(), now, item_id),
            )
        return self.get_item(item_id)  # type: ignore[return-value]

    def mark_dryrun_published(self, item_id: str, receipt: Dict[str, Any]) -> Dict[str, Any]:
        item = self.get_item(item_id)
        if not item:
            raise KeyError(f"Pieza editorial '{item_id}' no encontrada.")
        if item["status"] not in ("APPROVED", "SCHEDULED") or not item["approval_token"]:
            raise ApprovalRequiredError(
                f"Bloqueado: '{item_id}' requiere aprobación explícita previa antes de simular publicación."
            )
        now = utc_now_iso()
        with get_connection(self.db_path, write=True) as conn:
            conn.execute(
                """
                UPDATE editorial_items
                SET status = 'PUBLISHED_DRYRUN',
                    published_at = ?,
                    publish_receipt_json = ?,
                    updated_at = ?
                WHERE item_id = ?
                """,
                (now, json.dumps(receipt, ensure_ascii=False), now, item_id),
            )
        return self.get_item(item_id)  # type: ignore[return-value]

    def get_item(self, item_id: str) -> Optional[Dict[str, Any]]:
        with get_connection(self.db_path) as conn:
            row = conn.execute("SELECT * FROM editorial_items WHERE item_id = ?", (item_id,)).fetchone()
        return self._row_to_dict(row) if row else None

    def list_items(self, *, status: Optional[str] = None, limit: int = 100) -> List[Dict[str, Any]]:
        with get_connection(self.db_path) as conn:
            if status:
                rows = conn.execute(
                    "SELECT * FROM editorial_items WHERE status = ? ORDER BY created_at DESC LIMIT ?",
                    (status, limit),
                ).fetchall()
            else:
                rows = conn.execute(
                    "SELECT * FROM editorial_items ORDER BY created_at DESC LIMIT ?",
                    (limit,),
                ).fetchall()
        return [self._row_to_dict(r) for r in rows]

    def summary_counts(self) -> Dict[str, int]:
        with get_connection(self.db_path) as conn:
            rows = conn.execute(
                "SELECT status, COUNT(*) AS cnt FROM editorial_items GROUP BY status"
            ).fetchall()
        counts = {
            "DRAFT": 0,
            "CLINICAL_QA": 0,
            "APPROVED": 0,
            "SCHEDULED": 0,
            "PUBLISHED_DRYRUN": 0,
            "REJECTED": 0,
        }
        for r in rows:
            counts[r["status"]] = int(r["cnt"])
        counts["TOTAL"] = sum(counts.values())
        return counts

    @staticmethod
    def _row_to_dict(row: Any) -> Dict[str, Any]:
        return {
            "item_id": row["item_id"],
            "topic_key": row["topic_key"],
            "title": row["title"],
            "channel": row["channel"],
            "format_type": row["format_type"],
            "caption": row["caption"],
            "media_path": row["media_path"],
            "utm_url": row["utm_url"],
            "status": row["status"],
            "qa_passed": bool(row["qa_passed"]),
            "qa_issues": json.loads(row["qa_issues_json"] or "[]"),
            "scheduled_for": row["scheduled_for"],
            "approval_token": row["approval_token"],
            "approved_by": row["approved_by"],
            "approved_at": row["approved_at"],
            "published_at": row["published_at"],
            "publish_receipt": json.loads(row["publish_receipt_json"]) if row["publish_receipt_json"] else None,
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
        }
