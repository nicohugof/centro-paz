"""
CLI Unificada de CPAZ Media OS (`python3 -m media_os.cli`).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Optional

from agent import content_engine
from media_os.attribution import AttributionEngine, build_utm_links
from media_os.automation import export_n8n_approved_schedule
from media_os.calendar import EditorialCalendar
from media_os.dashboard import build_executive_snapshot, render_dashboard_html, serve_loopback
from media_os.intelligence import StrategicIntelligenceEngine
from media_os.publishers import DryRunLocalPublisher
from media_os.studio import MediaStudio, ROOT


def run_demo_e2e(
    db_path: Optional[Path | str] = None,
    *,
    use_llm: bool = False,
    n8n_output_file: Optional[Path | str] = None,
    dashboard_output_path: Optional[Path | str] = None,
) -> dict:
    intel = StrategicIntelligenceEngine(db_path=db_path)
    studio = MediaStudio()
    calendar = EditorialCalendar(db_path=db_path)
    attribution = AttributionEngine(db_path=db_path)

    # 1-2. Inteligencia + Investigación Clínica
    brief = intel.generate_strategic_brief("tdah_adultos", use_llm=use_llm)

    # 3-4. Estudio Audiovisual (ffprobe real sobre video existente sin tocar video_engine/public)
    sample_mp4 = ROOT / "assets" / "videos" / "cpaz_short01_tdah.mp4"
    probe = studio.probe_video(sample_mp4) if sample_mp4.exists() else {}

    # 5-6. Calendario Editorial + Gate PUBLICAR <ID> + Publicación Dry-Run
    utm = build_utm_links(
        topic_key="tdah_adultos",
        utm_source="instagram",
        utm_medium="organic",
        utm_campaign="piloto_tdah_media_os",
        utm_content="reel_01",
    )
    topic = content_engine.TOPICS["tdah_adultos"]
    draft = calendar.create_draft(
        topic_key="tdah_adultos",
        title=topic["title"],
        channel="instagram",
        format_type="reel_mp4",
        caption=topic["caption"],
        media_path="assets/videos/cpaz_short01_tdah.mp4",
        utm_url=utm["landing_url"],
    )
    qa_item = calendar.run_qa(draft["item_id"])
    approved = calendar.approve_item(
        qa_item["item_id"],
        approval_token=f"PUBLICAR {qa_item['item_id']}",
        reviewer="Nicolas",
        reason="Piloto E2E CPAZ Media OS verificado",
    )
    scheduled = calendar.schedule_item(approved["item_id"], scheduled_for="2026-11-12T18:30:00-03:00")

    # 7. Puente n8n aprobado-only
    n8n_export = export_n8n_approved_schedule(calendar, output_file=n8n_output_file)

    # Publicación dry-run desacoplada
    pub_res = DryRunLocalPublisher(calendar=calendar).publish(scheduled)

    # 8-9. Analítica y Atribución Comercial sin PII
    attribution.record_content_metrics(
        item_id=scheduled["item_id"],
        topic_key="tdah_adultos",
        channel="instagram",
        utm_campaign=utm["utm_campaign"],
        impressions=1450,
        clicks=86,
        saves=42,
        shares=19,
    )
    attribution.record_commercial_inquiry(
        utm_source="instagram",
        utm_campaign=utm["utm_campaign"],
        topic_key="tdah_adultos",
        utm_content="reel_01",
        converted_booking=True,
    )

    # 10. Dashboard Ejecutivo HTML
    snap = build_executive_snapshot(db_path=db_path, probe_videos=True)
    html_out = render_dashboard_html(snap, output_path=dashboard_output_path)

    return {
        "brief_id": brief["brief_id"],
        "source_engine": brief["source_engine"],
        "video_probed": probe.get("file"),
        "video_duration_sec": probe.get("duration_sec"),
        "item_id": scheduled["item_id"],
        "published_dryrun_status": pub_res["item"]["status"],
        "n8n_approved_count": n8n_export["approved_count"],
        "attribution_totals": snap["attribution"]["totals"],
        "dashboard_html": str(html_out),
    }


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="CPAZ Media OS CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("audit", help="Audita base clínica, activos, FFmpeg/Ollama y matriz OSS")
    p_brief = sub.add_parser("brief", help="Genera brief estratégico sin PII")
    p_brief.add_argument("topic_key", default="tdah_adultos", nargs="?")
    p_brief.add_argument("--llm", action="store_true", help="Usar Ollama local si está activo")

    p_probe = sub.add_parser("probe-media", help="Inspecciona un video con ffprobe real")
    p_probe.add_argument("path", nargs="?", default="assets/videos/cpaz_short01_tdah.mp4")

    p_app = sub.add_parser("approve", help="Aprueba una pieza con PUBLICAR <ID>")
    p_app.add_argument("item_id")
    p_app.add_argument("--token", required=True, help="Debe ser exactamente 'PUBLICAR <ID>'")

    p_pub = sub.add_parser("publish-dryrun", help="Simula publicación de una pieza aprobada")
    p_pub.add_argument("item_id")

    sub.add_parser("export-n8n", help="Exporta cola n8n filtrada a piezas APPROVED/SCHEDULED")

    p_demo = sub.add_parser("demo-e2e", help="Ejecuta piloto E2E local seguro (dry-run)")
    p_demo.add_argument("--llm", action="store_true")

    sub.add_parser("dashboard", help="Renderiza tools/cpaz_media_os_dashboard.html")
    p_srv = sub.add_parser("serve", help="Levanta servidor local loopback o Tailscale privado")
    p_srv.add_argument("--host", default="127.0.0.1")
    p_srv.add_argument("--port", type=int, default=8765)
    p_srv.add_argument("--tailscale", action="store_true", help="Permite enlace privado en red Tailscale 100.64.0.0/10")

    args = parser.parse_args(argv)

    if args.command == "audit":
        snap = build_executive_snapshot(probe_videos=True)
        print(json.dumps(snap, indent=2, ensure_ascii=False))
        return 0
    if args.command == "brief":
        res = StrategicIntelligenceEngine().generate_strategic_brief(args.topic_key, use_llm=args.llm)
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0
    if args.command == "probe-media":
        target = Path(args.path)
        if not target.is_absolute():
            target = ROOT / target
        res = MediaStudio().probe_video(target)
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0
    if args.command == "approve":
        cal = EditorialCalendar()
        res = cal.approve_item(args.item_id, approval_token=args.token)
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0
    if args.command == "publish-dryrun":
        cal = EditorialCalendar()
        item = cal.get_item(args.item_id)
        if not item:
            raise SystemExit(f"Pieza no encontrada: {args.item_id}")
        res = DryRunLocalPublisher(calendar=cal).publish(item)
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0
    if args.command == "export-n8n":
        res = export_n8n_approved_schedule(EditorialCalendar())
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0
    if args.command == "demo-e2e":
        res = run_demo_e2e(use_llm=args.llm)
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0
    if args.command == "dashboard":
        snap = build_executive_snapshot(probe_videos=True)
        path = render_dashboard_html(snap)
        print(f"Dashboard actualizado en: {path}")
        return 0
    if args.command == "serve":
        serve_loopback(host=args.host, port=args.port, allow_tailscale=args.tailscale)
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
