"""
Analítica Privacy-First y Atribución Comercial sin PII — CPAZ Media OS.

¿Qué es?
Motor local de construcción de enlaces UTM compatibles con `app.js` (`getUTMContext()`),
ingesta de métricas anónimas (locales o exportadas de Umami/GA4/Shlink) y atribución de
consultas comerciales hacia WhatsApp (`+56 9 6516 3893`).

¿Para qué lo usamos?
Medir qué tópicos, canales y piezas generan consultas reales de psicoterapia (referencia
`$45.000 CLP`) sin tocar nunca historias clínicas ni almacenar nombres, RUTs o teléfonos de pacientes.
"""

from __future__ import annotations

import json
import urllib.parse
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional

from media_os.intelligence import CANONICAL_FEE_CLP
from media_os.privacy import assert_no_pii
from media_os.storage import get_connection, utc_now_iso

BASE_SITE_URL = "https://www.centropaz.cl/"
OFFICIAL_WA_NUMBER = "56965163893"


def build_utm_links(
    *,
    topic_key: str,
    utm_source: str,
    utm_medium: str = "organic",
    utm_campaign: Optional[str] = None,
    utm_content: Optional[str] = None,
) -> Dict[str, str]:
    """Genera enlaces UTM 100% compatibles con `app.js::getUTMContext()` en `www.centropaz.cl`."""
    assert_no_pii(
        {"topic_key": topic_key, "utm_source": utm_source, "utm_campaign": utm_campaign or ""},
        field_path="utm_builder",
    )
    campaign = utm_campaign or f"cpaz_{topic_key}"
    params = {
        "utm_source": utm_source.strip().lower(),
        "utm_medium": utm_medium.strip().lower(),
        "utm_campaign": campaign.strip().lower(),
    }
    if utm_content:
        params["utm_content"] = utm_content.strip().lower()
    query = urllib.parse.urlencode(params)
    landing_url = f"{BASE_SITE_URL}?{query}"

    ref_tag = f"[Ref: {params['utm_source']} · {params['utm_campaign']}]"
    wa_text = f"Hola Valentina, me interesa consultar por psicoterapia en Centro Paz.\n\n{ref_tag}"
    whatsapp_url = f"https://wa.me/{OFFICIAL_WA_NUMBER}?text={urllib.parse.quote(wa_text)}"
    return {
        "landing_url": landing_url,
        "whatsapp_url": whatsapp_url,
        "utm_source": params["utm_source"],
        "utm_medium": params["utm_medium"],
        "utm_campaign": params["utm_campaign"],
        "utm_content": params.get("utm_content", ""),
    }


class AttributionEngine:
    """Registra analítica anónima y atribución de consultas comerciales sin información clínica."""

    def __init__(self, db_path: Optional[Path | str] = None) -> None:
        self.db_path = db_path

    def record_content_metrics(
        self,
        *,
        topic_key: str,
        channel: str,
        utm_campaign: str,
        impressions: int,
        clicks: int,
        saves: int = 0,
        shares: int = 0,
        item_id: Optional[str] = None,
        source_system: str = "cpaz_local",
    ) -> None:
        payload = {
            "item_id": item_id,
            "topic_key": topic_key,
            "channel": channel,
            "utm_campaign": utm_campaign,
            "source_system": source_system,
        }
        assert_no_pii(payload, field_path="content_metrics")
        with get_connection(self.db_path, write=True) as conn:
            conn.execute(
                """
                INSERT INTO content_metrics (
                    item_id, topic_key, channel, utm_campaign,
                    impressions, clicks, saves, shares, source_system, recorded_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item_id,
                    topic_key,
                    channel,
                    utm_campaign,
                    int(impressions),
                    int(clicks),
                    int(saves),
                    int(shares),
                    source_system,
                    utc_now_iso(),
                ),
            )

    def record_commercial_inquiry(
        self,
        *,
        utm_source: str,
        utm_campaign: str,
        topic_key: str,
        utm_medium: str = "organic",
        utm_content: str = "cta",
        inquiry_channel: str = "whatsapp_web_cta",
        converted_booking: bool = False,
    ) -> str:
        """
        Registra una consulta comercial anónima (conteo y campaña UTM) con bloqueo estricto de PII.
        """
        payload = {
            "utm_source": utm_source,
            "utm_medium": utm_medium,
            "utm_campaign": utm_campaign,
            "utm_content": utm_content,
            "topic_key": topic_key,
            "inquiry_channel": inquiry_channel,
        }
        assert_no_pii(payload, field_path="commercial_inquiry")
        inq_id = f"inq-{uuid.uuid4().hex[:10]}"
        est_value = CANONICAL_FEE_CLP if converted_booking else 0
        with get_connection(self.db_path, write=True) as conn:
            conn.execute(
                """
                INSERT INTO attribution_inquiries (
                    inquiry_id, utm_source, utm_medium, utm_campaign, utm_content,
                    topic_key, inquiry_channel, converted_booking, estimated_value_clp, recorded_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    inq_id,
                    utm_source.strip().lower(),
                    utm_medium.strip().lower(),
                    utm_campaign.strip().lower(),
                    utm_content.strip().lower(),
                    topic_key.strip(),
                    inquiry_channel.strip(),
                    1 if converted_booking else 0,
                    est_value,
                    utc_now_iso(),
                ),
            )
        return inq_id

    def import_external_aggregates(self, json_records: List[Dict[str, Any]], *, source_system: str = "umami") -> int:
        """Importa métricas agregadas externas (Umami / GA4 / Shlink) validando 0 PII por fila."""
        imported = 0
        for row in json_records:
            assert_no_pii(row, field_path=f"external_import.{source_system}")
            self.record_content_metrics(
                topic_key=str(row["topic_key"]),
                channel=str(row.get("channel", "web")),
                utm_campaign=str(row.get("utm_campaign", row["topic_key"])),
                impressions=int(row.get("impressions", 0)),
                clicks=int(row.get("clicks", 0)),
                saves=int(row.get("saves", 0)),
                shares=int(row.get("shares", 0)),
                item_id=row.get("item_id"),
                source_system=source_system,
            )
            imported += 1
        return imported

    def get_attribution_summary(self) -> Dict[str, Any]:
        with get_connection(self.db_path) as conn:
            m_tot = conn.execute(
                """
                SELECT COALESCE(SUM(impressions), 0) AS impressions,
                       COALESCE(SUM(clicks), 0) AS clicks,
                       COALESCE(SUM(saves), 0) AS saves,
                       COALESCE(SUM(shares), 0) AS shares
                FROM content_metrics
                """
            ).fetchone()
            i_tot = conn.execute(
                """
                SELECT COUNT(*) AS inquiries,
                       COALESCE(SUM(converted_booking), 0) AS bookings,
                       COALESCE(SUM(estimated_value_clp), 0) AS est_revenue_clp
                FROM attribution_inquiries
                """
            ).fetchone()
            by_topic_rows = conn.execute(
                """
                SELECT topic_key,
                       COUNT(*) AS inquiries,
                       COALESCE(SUM(converted_booking), 0) AS bookings,
                       COALESCE(SUM(estimated_value_clp), 0) AS est_revenue_clp
                FROM attribution_inquiries
                GROUP BY topic_key
                ORDER BY inquiries DESC, bookings DESC
                """
            ).fetchall()
            by_channel_rows = conn.execute(
                """
                SELECT channel,
                       COALESCE(SUM(impressions), 0) AS impressions,
                       COALESCE(SUM(clicks), 0) AS clicks,
                       COALESCE(SUM(saves), 0) AS saves
                FROM content_metrics
                GROUP BY channel
                ORDER BY clicks DESC
                """
            ).fetchall()

        impressions = int(m_tot["impressions"])
        clicks = int(m_tot["clicks"])
        inquiries = int(i_tot["inquiries"])
        bookings = int(i_tot["bookings"])
        ctr_pct = round((clicks / impressions) * 100.0, 2) if impressions else 0.0
        inquiry_conv_pct = round((inquiries / clicks) * 100.0, 2) if clicks else 0.0

        return {
            "totals": {
                "impressions": impressions,
                "clicks": clicks,
                "saves": int(m_tot["saves"]),
                "shares": int(m_tot["shares"]),
                "ctr_pct": ctr_pct,
                "inquiries": inquiries,
                "bookings": bookings,
                "inquiry_per_click_pct": inquiry_conv_pct,
                "estimated_value_clp": int(i_tot["est_revenue_clp"]),
            },
            "by_topic": [dict(r) for r in by_topic_rows],
            "by_channel": [dict(r) for r in by_channel_rows],
            "privacy_guarantee": "zero_pii_clinical_isolated",
        }
