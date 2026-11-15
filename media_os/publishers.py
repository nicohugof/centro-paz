"""
Adaptadores Desacoplados de Publicación en Redes — CPAZ Media OS.

¿Qué es?
Protocolo `PublisherAdapter` y sus implementaciones desacopladas:
1. `DryRunLocalPublisher` (activo por defecto, cero tráfico a redes externas ni APIs pagadas).
2. `MetaGraphPublisherAdapter` (envoltura segura sobre `agent.auto_publisher` bloqueada si `allow_live=False`).
3. `ExternalOSSPublisherContract` (contratos deshabilitados para Postiz, OpenPost y BrightBean Studio con auditoría AGPL-3.0).

¿Para qué lo usamos?
Permite cambiar o sumar publicadores sin reescribir calendario ni reglas clínicas, imponiendo siempre
la compuerta `ApprovalRequiredError` antes de emitir cualquier salida.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Protocol

from agent import auto_publisher
from media_os.calendar import ApprovalRequiredError, EditorialCalendar, _validate_approval_token


class PublisherAdapter(Protocol):
    adapter_name: str

    def publish(self, item: Dict[str, Any]) -> Dict[str, Any]:
        ...


def _assert_item_approved_for_publish(item: Optional[Dict[str, Any]]) -> None:
    if not isinstance(item, dict) or not item:
        raise ApprovalRequiredError("Publicación bloqueada: la pieza editorial no existe o es nula.")
    if item.get("status") not in ("APPROVED", "SCHEDULED"):
        raise ApprovalRequiredError(
            f"Publicación bloqueada: '{item.get('item_id')}' está en estado '{item.get('status')}' (exige APPROVED/SCHEDULED)."
        )
    if not item.get("qa_passed"):
        raise ApprovalRequiredError(f"Publicación bloqueada: '{item.get('item_id')}' no aprobó QA clínico.")
    token = str(item.get("approval_token") or "")
    if not _validate_approval_token(str(item.get("item_id")), token):
        raise ApprovalRequiredError(
            f"Publicación bloqueada: falta token explícito 'PUBLICAR {item.get('item_id')}' o 'AUTORIZO {item.get('item_id')}'."
        )


@dataclass
class DryRunLocalPublisher:
    """Publicador por defecto 100% seguro: valida aprobación y registra recibo local sin llamadas HTTP externas."""

    calendar: EditorialCalendar
    adapter_name: str = "dry-run-local"

    def publish(self, item: Dict[str, Any]) -> Dict[str, Any]:
        _assert_item_approved_for_publish(item)
        receipt = {
            "mode": "dry_run",
            "adapter": self.adapter_name,
            "channel": item["channel"],
            "format_type": item["format_type"],
            "media_path": item["media_path"],
            "utm_url": item["utm_url"],
            "approval_token": item["approval_token"],
            "network_call_executed": False,
        }
        updated = self.calendar.mark_dryrun_published(item["item_id"], receipt)
        return {"ok": True, "receipt": receipt, "item": updated}


@dataclass
class MetaGraphPublisherAdapter:
    """
    Envoltura desacoplada sobre `agent/auto_publisher.py`.
    `allow_live=False` por diseño mientras no exista autorización explícita + credenciales Meta configuradas.
    """

    calendar: EditorialCalendar
    allow_live: bool = False
    adapter_name: str = "meta-graph-wrapped"

    def publish(self, item: Dict[str, Any]) -> Dict[str, Any]:
        _assert_item_approved_for_publish(item)
        if not self.allow_live:
            receipt = {
                "mode": "dry_run_meta_preview",
                "adapter": self.adapter_name,
                "channel": item["channel"],
                "existing_posts_catalog_size": len(auto_publisher.POSTS_CATALOG),
                "existing_videos_catalog_size": len(auto_publisher.VIDEOS_CATALOG),
                "network_call_executed": False,
                "reason": "Publicación en vivo deshabilitada sin AUTORIZO explícito y credenciales activas.",
            }
            updated = self.calendar.mark_dryrun_published(item["item_id"], receipt)
            return {"ok": True, "receipt": receipt, "item": updated}

        raise PermissionError(
            "Envío real a Meta Graph API bloqueado hasta confirmación humana directa en producción."
        )


@dataclass
class ExternalOSSPublisherContract:
    """
    Contrato desacoplado de integración futura para Postiz, OpenPost o BrightBean Studio.
    Inactivo por defecto por consumo de RAM y obligaciones de licencia AGPL-3.0.
    """

    target_platform: str  # 'postiz' | 'openpost' | 'brightbean-studio'
    license_name: str = "AGPL-3.0"
    enabled: bool = False
    endpoint_url: str = ""

    def build_dispatch_contract(self, item: Dict[str, Any]) -> Dict[str, Any]:
        _assert_item_approved_for_publish(item)
        return {
            "target_platform": self.target_platform,
            "license": self.license_name,
            "enabled": self.enabled,
            "requires_agpl_source_disclosure_if_saas": True,
            "payload": {
                "external_id": item["item_id"],
                "channel": item["channel"],
                "caption_with_utm": f"{item['caption']}\n\n{item['utm_url']}",
                "media_path": item["media_path"],
                "scheduled_for": item.get("scheduled_for"),
            },
        }
