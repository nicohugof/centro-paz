"""
Puente de Automatización Desacoplado (n8n Existente / Webhook Compatible) — CPAZ Media OS.

¿Qué es?
Exportador de colas y contratos webhook compatibles con la instancia existente de `n8n` en Oracle
(`agent/n8n_cpaz_workflow.json`) y flujos externos, sin instalar `Activepieces` (ahorra 2-4 GB RAM).

¿Para qué lo usamos?
Evitar duplicar motores de automatización y garantizar que únicamente piezas en estado
`APPROVED` o `SCHEDULED` con token de aprobación vigente puedan ingresar a una cola automática.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from media_os.calendar import EditorialCalendar, _validate_approval_token
from media_os.privacy import assert_path_not_clinical
from media_os.storage import ROOT, utc_now_iso

EXISTING_N8N_WORKFLOW = ROOT / "agent" / "n8n_cpaz_workflow.json"
DEFAULT_EXPORT_FILE = ROOT / "data" / "media_os" / "n8n_approved_schedule.json"


def export_n8n_approved_schedule(
    calendar: EditorialCalendar,
    *,
    output_file: Optional[Path | str] = None,
) -> Dict[str, Any]:
    """
    Construye y exporta la parrilla aprobada compatible con n8n (`n8n_cpaz_workflow.json`).
    Excluye determinísticamente todo ítem `DRAFT`, `CLINICAL_QA`, `REJECTED` o sin token válido.
    """
    all_items = calendar.list_items(limit=500)
    approved_queue: List[Dict[str, Any]] = []
    excluded_count = 0

    for item in all_items:
        is_eligible = (
            item["status"] in ("APPROVED", "SCHEDULED")
            and bool(item["qa_passed"])
            and _validate_approval_token(item["item_id"], str(item.get("approval_token") or ""))
        )
        if is_eligible:
            approved_queue.append(
                {
                    "item_id": item["item_id"],
                    "topic_key": item["topic_key"],
                    "channel": item["channel"],
                    "format_type": item["format_type"],
                    "title": item["title"],
                    "caption": item["caption"],
                    "media_path": item["media_path"],
                    "utm_url": item["utm_url"],
                    "scheduled_for": item.get("scheduled_for"),
                    "approval_token": item["approval_token"],
                    "approved_by": item["approved_by"],
                }
            )
        else:
            excluded_count += 1

    payload = {
        "schema": "cpaz-media-os/n8n-approved-schedule-v1",
        "generated_at": utc_now_iso(),
        "n8n_workflow_reference": str(EXISTING_N8N_WORKFLOW.relative_to(ROOT)),
        "workflow_exists": EXISTING_N8N_WORKFLOW.exists(),
        "automation_engine": "n8n-existing-oracle (activepieces omitted to save 2-4GB RAM)",
        "approved_count": len(approved_queue),
        "excluded_unapproved_count": excluded_count,
        "items": approved_queue,
    }

    dest = Path(output_file) if output_file else DEFAULT_EXPORT_FILE
    assert_path_not_clinical(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    try:
        os.chmod(dest, 0o600)
    except OSError:
        pass
    payload["export_path"] = str(dest)
    return payload
