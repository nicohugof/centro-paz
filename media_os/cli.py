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


def interactive_menu(db_path: Optional[Path | str] = None) -> None:
    import subprocess

    while True:
        print("\n" + "=" * 72)
        print(" 🧠 CPAZ MEDIA OS — PANEL EJECUTIVO LOCAL")
        print(" 📍 Aislamiento Clínico Ley 19.628 (0 PII) | Gate: PUBLICAR <ID>")
        print("=" * 72)
        print(" 1. 📊 Ver Snapshot Ejecutivo (KPIs, Calendario, Atribución, Matriz OSS)")
        print(" 2. 📥 Poblar Calendario Editorial (28 Tópicos Clínicos)")
        print(" 3. 🩺 Ejecutar QA Clínico Automático (Reglas de arancel, SIS y afirmaciones)")
        print(" 4. ✅ Aprobar Pieza Editorial (Token estricto: PUBLICAR <ID>)")
        print(" 5. 🚀 Simular Publicación Dry-Run (Verificación desacoplada sin redes vivas)")
        print(" 6. 📤 Exportar Cola de Contenido para n8n (Solo piezas APPROVED)")
        print(" 7. 🎨 Generar y Abrir Dashboard HTML en Navegador")
        print(" 8. 🌐 Iniciar Servidor Web Local Loopback (http://127.0.0.1:8765)")
        print(" 0. 🚪 Volver al Menú Principal")
        print("=" * 72)

        try:
            choice = input("👉 Elige una opción (0-8): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n")
            break

        cal = EditorialCalendar(db_path=db_path)

        if choice == "1":
            snap = build_executive_snapshot(db_path=db_path, probe_videos=False)
            cal_sum = snap["calendar_summary"]
            tot = snap["attribution"]["totals"]
            print("\n--- RESUMEN EJECUTIVO CPAZ MEDIA OS ---")
            print(f"Piezas en Calendario: Total {cal_sum['TOTAL']} | Aprobadas: {cal_sum['APPROVED']} | Dry-Run: {cal_sum['PUBLISHED_DRYRUN']} | QA: {cal_sum['CLINICAL_QA']} | Draft: {cal_sum['DRAFT']}")
            print(f"Atribución Comercial: {tot['inquiries']} consultas UTM | {tot['bookings']} reservas est. | Proy: ${tot['estimated_value_clp']:,} CLP")
            print(f"Runtime Local: Ollama {'ON' if snap['runtime']['ollama_available'] else 'OFF (fallback)'} | FFmpeg {'OK' if snap['runtime']['ffmpeg_ready'] else 'NO'}")
        elif choice == "2":
            print("\n📥 Poblando las 4 semanas de contenido clínico (28 temas)...")
            created = cal.seed_all_topics()
            print(f"✅ Se cargaron/verificaron {len(created)} piezas en borrador en el calendario editorial.")
        elif choice == "3":
            print("\n🩺 Ejecutando auditoría de QA clínico sobre piezas...")
            results = cal.run_qa_all()
            print(f"✅ Auditoría completada: {results['passed']}/{results['total']} piezas aprobaron todos los criterios clínicos.")
            if results["failed"] > 0:
                print(f"⚠️ {results['failed']} piezas requieren revisión de arancel o registro SIS.")
        elif choice == "4":
            item_id = input("Ingresa el ID de la pieza a aprobar (ej: itm-w1-d1): ").strip()
            if not item_id:
                print("Operación cancelada.")
                continue
            token = input(f"Confirma token exacto [PUBLICAR {item_id}]: ").strip()
            try:
                cal.approve_item(item_id, approval_token=token)
                print(f"✅ Pieza '{item_id}' APROBADA exitosamente.")
            except Exception as e:
                print(f"❌ Error de aprobación: {e}")
        elif choice == "5":
            item_id = input("Ingresa el ID de la pieza para simulación dry-run: ").strip()
            item = cal.get_item(item_id)
            if not item:
                print(f"❌ Pieza '{item_id}' no encontrada.")
                continue
            try:
                pub = DryRunLocalPublisher(calendar=cal)
                res = pub.publish(item)
                print(f"✅ Simulación completada para '{item_id}'. Estado: {res['item']['status']}")
            except Exception as e:
                print(f"❌ Error al publicar dry-run: {e}")
        elif choice == "6":
            print("\n📤 Exportando piezas aprobadas para n8n...")
            res = export_n8n_approved_schedule(cal)
            print(f"✅ Exportación completada en: {res['export_file']} ({res['approved_count']} piezas listas).")
        elif choice == "7":
            snap = build_executive_snapshot(db_path=db_path, probe_videos=False)
            out_file = render_dashboard_html(snap)
            print(f"✅ Dashboard generado en: {out_file}")
            try:
                subprocess.run(["open", str(out_file)], check=False)
            except Exception:
                pass
        elif choice == "8":
            print("\n🌐 Levantando servidor local en http://127.0.0.1:8765 ... (Ctrl+C para volver)")
            try:
                serve_loopback(db_path=db_path, host="127.0.0.1", port=8765)
            except KeyboardInterrupt:
                print("\n🛑 Servidor detenido.")
        elif choice in ("0", "volver", "q", "exit"):
            break
        else:
            print("⚠️ Opción no válida.")


def main(argv: Optional[list[str]] = None) -> int:
    import sys

    effective_args = sys.argv[1:] if argv is None else argv
    if not effective_args or (len(effective_args) == 1 and effective_args[0] == "menu"):
        interactive_menu()
        return 0

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

    p_seed = sub.add_parser("seed", help="Puebla el calendario editorial con los 28 tópicos clínicos")
    p_seed.add_argument("--weeks", type=int, nargs="*", default=[1, 2, 3, 4], help="Semanas a poblar (1 a 4)")
    p_seed.add_argument("--channel", default="instagram", help="Canal de distribución")

    p_qa = sub.add_parser("qa-all", help="Ejecuta auditoría clínica automática sobre piezas")
    p_qa.add_argument("--status", default=None, help="Filtrar por estado (ej: DRAFT)")

    sub.add_parser("menu", help="Submenú interactivo en terminal para Nico")
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
    if args.command == "seed":
        cal = EditorialCalendar()
        weeks_tuple = tuple(args.weeks)
        res = cal.seed_all_topics(channel=args.channel, weeks=weeks_tuple)
        print(json.dumps({"seeded_count": len(res), "items": res}, indent=2, ensure_ascii=False))
        return 0
    if args.command == "qa-all":
        cal = EditorialCalendar()
        res = cal.run_qa_all(status_filter=args.status)
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
