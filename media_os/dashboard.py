"""
Dashboard Ejecutivo CPAZ Media OS (HTML Autocontenido + Servidor Local Loopback).

¿Qué es?
Consolidación visual y JSON de las 10 capacidades de CPAZ Media OS: inteligencia estratégica,
investigación, creación audiovisual, edición, calendario editorial, puerta de aprobación humana,
automatización n8n, analítica sin PII, atribución comercial y matriz de licencias OSS.

¿Para qué lo usamos?
Dar a Nicolás y Valentina una sola pantalla ejecutiva clara (estilo Apple / baja fricción TDAH)
donde auditar estado, piezas aprobadas vs pendientes y retorno atribuido sin abrir 6 herramientas.
"""

from __future__ import annotations

import html
import ipaddress
import json
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, List, Optional

_TAILSCALE_NET = ipaddress.ip_network("100.64.0.0/10")
_LOOPBACK_NET = ipaddress.ip_network("127.0.0.0/8")

from media_os.attribution import AttributionEngine
from media_os.automation import EXISTING_N8N_WORKFLOW, export_n8n_approved_schedule
from media_os.calendar import EditorialCalendar
from media_os.intelligence import OllamaAdapter, StrategicIntelligenceEngine
from media_os.privacy import assert_no_pii
from media_os.studio import MediaStudio
from media_os.storage import ROOT, utc_now_iso

DEFAULT_DASHBOARD_HTML = ROOT / "tools" / "cpaz_media_os_dashboard.html"

OSS_MATRIX_SUMMARY: List[Dict[str, str]] = [
    {"tool": "CPAZ Engine + KB", "license": "Propio CPAZ", "decision": "REUTILIZADO", "note": "28 tópicos, artículos clínicos, 28 PNGs, 11 MP4s"},
    {"tool": "Ollama (127.0.0.1)", "license": "MIT", "decision": "INTEGRADO", "note": "Adaptador local $0/mes con fallback determinista"},
    {"tool": "FFmpeg / FFprobe CLI", "license": "GPL-3.0 (CLI)", "decision": "INTEGRADO", "note": "Subproceso aislado; 0 MB RAM en reposo"},
    {"tool": "Remotion", "license": "Source-available (<=3 emp. gratis)", "decision": "REUTILIZADO", "note": "Shorts 1080x1920 con Edge-TTS + Whisper"},
    {"tool": "n8n (Oracle VPS)", "license": "Sustainable Use", "decision": "REUTILIZADO", "note": "Puente exportador filtrado a APPROVED"},
    {"tool": "Postiz", "license": "AGPL-3.0", "decision": "DESCARTADO (2-8 GB)", "note": "Solo contrato externo futuro deshabilitado"},
    {"tool": "BrightBean Studio", "license": "AGPL-3.0", "decision": "REFERENCIA / NO DUP", "note": "Evita duplicar Django+Postgres sobre SQLite"},
    {"tool": "OpenPost", "license": "AGPL-3.0", "decision": "CONTRATO FUTURO", "note": "MCP/HTTP deshabilitado por AGPL y RAM"},
    {"tool": "Activepieces", "license": "MIT + EE prop.", "decision": "DESCARTADO (2-4 GB)", "note": "Evita duplicar n8n activo en Oracle"},
    {"tool": "ComfyUI", "license": "GPL-3.0", "decision": "DESHABILITADO (16-32 GB)", "note": "Inviable en Mac 8 GB; HTML->Chrome PNG es determinista"},
]


def build_executive_snapshot(
    *,
    db_path: Optional[Path | str] = None,
    probe_videos: bool = False,
) -> Dict[str, Any]:
    intel = StrategicIntelligenceEngine(db_path=db_path)
    studio = MediaStudio()
    calendar = EditorialCalendar(db_path=db_path)
    attribution = AttributionEngine(db_path=db_path)
    ollama = OllamaAdapter()

    kb_audit = intel.audit_existing_knowledge()
    assets = studio.inventory_existing_assets()
    caps = studio.capabilities()
    counts = calendar.summary_counts()
    items = calendar.list_items(limit=50)
    briefs = intel.list_briefs(limit=10)
    attr_summary = attribution.get_attribution_summary()

    probed_sample = []
    if probe_videos and assets["videos"]:
        for vid in assets["videos"][:3]:
            try:
                probed_sample.append(studio.probe_video(vid["path"]))
            except Exception as exc:
                probed_sample.append({"file": vid["name"], "error": str(exc)})

    snapshot = {
        "generated_at": utc_now_iso(),
        "identity": {
            "center": "Centro Paz",
            "therapist": "Valentina Castro Núñez",
            "sis_registration": "667344",
            "official_whatsapp": "+56 9 6516 3893",
            "fee_clp": 45000,
            "domain": "www.centropaz.cl",
            "privacy_isolation": "Ley 19.628 — fichas clínicas y datos de pacientes aislados",
        },
        "runtime": {
            "ollama_available": ollama.is_available(),
            "ollama_model": ollama.model,
            "ffmpeg_ready": bool(caps["ffmpeg_bin"]),
            "ffprobe_ready": bool(caps["ffprobe_bin"]),
            "remotion_ready": bool(caps["remotion_dir_exists"]),
            "n8n_workflow_present": EXISTING_N8N_WORKFLOW.exists(),
            "comfyui_enabled": False,
            "live_social_publishing_enabled": False,
        },
        "knowledge_audit": kb_audit,
        "assets_inventory": {
            "instagram_png_count": assets["instagram_png_count"],
            "instagram_html_count": assets["instagram_html_count"],
            "videos_mp4_count": assets["videos_mp4_count"],
            "protected_video_engine_public": assets["protected_video_engine_public"],
            "probed_videos_sample": probed_sample,
        },
        "calendar_summary": counts,
        "editorial_items": items,
        "recent_briefs": briefs,
        "attribution": attr_summary,
        "oss_matrix": OSS_MATRIX_SUMMARY,
    }
    assert_no_pii(snapshot, field_path="dashboard_snapshot")
    return snapshot


def render_dashboard_html(
    snapshot: Dict[str, Any],
    *,
    output_path: Optional[Path | str] = None,
) -> Path:
    dest = Path(output_path) if output_path else DEFAULT_DASHBOARD_HTML
    dest.parent.mkdir(parents=True, exist_ok=True)

    tot = snapshot["attribution"]["totals"]
    cal = snapshot["calendar_summary"]
    kb = snapshot["knowledge_audit"]
    rt = snapshot["runtime"]
    inv = snapshot["assets_inventory"]

    pending_rows = []
    for item in snapshot["editorial_items"][:12]:
        badge_cls = "ok" if item["status"] in ("APPROVED", "SCHEDULED", "PUBLISHED_DRYRUN") else (
            "warn" if item["status"] == "CLINICAL_QA" else "muted"
        )
        pending_rows.append(
            f"<tr>"
            f"<td><code>{html.escape(item['item_id'])}</code></td>"
            f"<td>{html.escape(item['title'][:58])}</td>"
            f"<td>{html.escape(item['channel'])} / {html.escape(item['format_type'])}</td>"
            f"<td><span class='badge {badge_cls}'>{html.escape(item['status'])}</span></td>"
            f"<td>{'SI' if item['qa_passed'] else 'PEND'}</td>"
            f"<td><code>{html.escape(item['approval_token'] or 'PUBLICAR ' + item['item_id'])}</code></td>"
            f"</tr>"
        )
    if not pending_rows:
        pending_rows.append("<tr><td colspan='6'>Sin piezas cargadas aún en calendario local.</td></tr>")

    topic_rows = []
    for t in snapshot["attribution"]["by_topic"][:8]:
        topic_rows.append(
            f"<tr>"
            f"<td>{html.escape(t['topic_key'])}</td>"
            f"<td>{t['inquiries']}</td>"
            f"<td>{t['bookings']}</td>"
            f"<td>${t['est_revenue_clp']:,} CLP</td>"
            f"</tr>"
        )
    if not topic_rows:
        topic_rows.append("<tr><td colspan='4'>Sin consultas atribuidas registradas aún.</td></tr>")

    oss_rows = []
    for row in snapshot["oss_matrix"]:
        oss_rows.append(
            f"<tr>"
            f"<td><strong>{html.escape(row['tool'])}</strong></td>"
            f"<td><code>{html.escape(row['license'])}</code></td>"
            f"<td>{html.escape(row['decision'])}</td>"
            f"<td>{html.escape(row['note'])}</td>"
            f"</tr>"
        )

    safe_json = json.dumps(snapshot, ensure_ascii=False).replace("</", "<\\/")

    html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CPAZ Media OS — Dashboard Ejecutivo</title>
  <style>
    :root {{
      --bg: #f6f8f6;
      --card: #ffffff;
      --ink: #1b2420;
      --muted: #5a6a61;
      --accent: #2c6e58;
      --accent-soft: #e7f3ee;
      --border: #dde5df;
      --warn-bg: #fff5e1;
      --warn-ink: #8a5600;
      --ok-bg: #e3f5ec;
      --ok-ink: #155c3e;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.45;
      padding: 24px;
    }}
    .wrap {{ max-width: 1180px; margin: 0 auto; }}
    header {{
      display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-start;
      gap: 16px; background: var(--card); border: 1px solid var(--border);
      border-radius: 16px; padding: 20px 24px; margin-bottom: 20px;
    }}
    h1 {{ margin: 0 0 6px 0; font-size: 1.55rem; color: var(--accent); }}
    .sub {{ margin: 0; color: var(--muted); font-size: 0.92rem; }}
    .guard-banner {{
      background: var(--accent-soft); border: 1px solid #b9dacb; color: #164837;
      border-radius: 12px; padding: 10px 14px; font-size: 0.86rem; font-weight: 600;
    }}
    .grid {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 14px; margin-bottom: 20px;
    }}
    .kpi {{
      background: var(--card); border: 1px solid var(--border); border-radius: 14px;
      padding: 16px 18px;
    }}
    .kpi-label {{ font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.04em; color: var(--muted); }}
    .kpi-val {{ font-size: 1.65rem; font-weight: 700; margin: 6px 0 4px 0; color: var(--ink); }}
    .kpi-sub {{ font-size: 0.82rem; color: var(--muted); }}
    .panel {{
      background: var(--card); border: 1px solid var(--border); border-radius: 16px;
      padding: 18px 22px; margin-bottom: 18px; overflow-x: auto;
    }}
    .panel h2 {{ margin: 0 0 12px 0; font-size: 1.1rem; color: var(--accent); }}
    table {{ width: 100%; border-collapse: collapse; font-size: 0.88rem; }}
    th, td {{ text-align: left; padding: 9px 10px; border-bottom: 1px solid var(--border); vertical-align: top; }}
    th {{ color: var(--muted); font-weight: 600; font-size: 0.8rem; text-transform: uppercase; }}
    .badge {{
      display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 0.75rem; font-weight: 700;
    }}
    .badge.ok {{ background: var(--ok-bg); color: var(--ok-ink); }}
    .badge.warn {{ background: var(--warn-bg); color: var(--warn-ink); }}
    .badge.muted {{ background: #eef1ef; color: #47544d; }}
    footer {{ text-align: center; color: var(--muted); font-size: 0.82rem; margin-top: 24px; }}
    code {{ background: #f1f4f2; padding: 2px 5px; border-radius: 5px; font-size: 0.82em; }}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div>
        <h1>CPAZ Media OS — Dashboard Ejecutivo</h1>
        <p class="sub">
          Centro Paz · Valentina Castro Núñez (SIS Nº 667344) · Salvador 2302, Ñuñoa &amp; Online Chile ·
          WhatsApp +56 9 6516 3893 · Arancel $45.000 CLP · www.centropaz.cl
        </p>
        <p class="sub">Actualizado: <code>{html.escape(snapshot['generated_at'])}</code></p>
      </div>
      <div class="guard-banner">
        Gate Activo: Sin publicación en vivo ni cuentas conectadas sin AUTORIZO · Aislamiento Clínico Ley 19.628 (0 PII)
      </div>
    </header>

    <section class="grid">
      <div class="kpi">
        <div class="kpi-label">Activos Reutilizados</div>
        <div class="kpi-val">{kb['topics_count']} / {inv['videos_mp4_count']}</div>
        <div class="kpi-sub">{inv['instagram_png_count']} PNGs + {kb['reels_scripts_count']} guiones Reels + {kb['clinical_articles_count']} artículos</div>
      </div>
      <div class="kpi">
        <div class="kpi-label">Aprobados / Calendario</div>
        <div class="kpi-val">{cal['APPROVED'] + cal['SCHEDULED'] + cal['PUBLISHED_DRYRUN']} / {cal['TOTAL']}</div>
        <div class="kpi-sub">Dry-run: {cal['PUBLISHED_DRYRUN']} · QA pend: {cal['CLINICAL_QA']} · Drafts: {cal['DRAFT']}</div>
      </div>
      <div class="kpi">
        <div class="kpi-label">Consultas Comerciales UTM</div>
        <div class="kpi-val">{tot['inquiries']}</div>
        <div class="kpi-sub">CTR {tot['ctr_pct']}% · Reservas est. {tot['bookings']} · Proy. ${tot['estimated_value_clp']:,} CLP</div>
      </div>
      <div class="kpi">
        <div class="kpi-label">Runtime Local ($0/mes)</div>
        <div class="kpi-val">{'Ollama ON' if rt['ollama_available'] else 'Fallback KB'}</div>
        <div class="kpi-sub">FFmpeg: {'OK' if rt['ffmpeg_ready'] else 'NO'} · n8n JSON: {'OK' if rt['n8n_workflow_present'] else 'NO'} · ComfyUI: OFF</div>
      </div>
    </section>

    <section class="panel">
      <h2>1. Calendario Editorial y Puerta de Aprobación Humana (PUBLICAR &lt;ID&gt;)</h2>
      <table>
        <thead>
          <tr><th>ID</th><th>Título</th><th>Canal / Formato</th><th>Estado</th><th>QA Clínico</th><th>Comando Autorización</th></tr>
        </thead>
        <tbody>{''.join(pending_rows)}</tbody>
      </table>
    </section>

    <section class="panel">
      <h2>2. Atribución Comercial por Tópico (Estrictamente Sin PII)</h2>
      <table>
        <thead>
          <tr><th>Tópico</th><th>Consultas UTM</th><th>Reservas Estimadas</th><th>Valor Referencial ($45.000 CLP)</th></tr>
        </thead>
        <tbody>{''.join(topic_rows)}</tbody>
      </table>
    </section>

    <section class="panel">
      <h2>3. Matriz de Integración OSS y Auditoría de Licencias</h2>
      <table>
        <thead>
          <tr><th>Componente</th><th>Licencia</th><th>Decisión</th><th>Justificación Arquitectónica</th></tr>
        </thead>
        <tbody>{''.join(oss_rows)}</tbody>
      </table>
    </section>

    <footer>
      CPAZ Media OS · Principio Rector: Investigar antes de construir · Integrar antes de duplicar · Medir antes de afirmar · Optimizar antes de escalar.
    </footer>
  </div>
  <script id="cpaz-media-os-snapshot" type="application/json">{safe_json}</script>
</body>
</html>
"""
    dest.write_text(html_doc, encoding="utf-8")
    return dest


def _is_loopback_host(host: str) -> bool:
    if host in ("127.0.0.1", "localhost", "::1"):
        return True
    try:
        return ipaddress.ip_address(host) in _LOOPBACK_NET
    except ValueError:
        return False


def _is_tailscale_host(host: str) -> bool:
    try:
        return ipaddress.ip_address(host) in _TAILSCALE_NET
    except ValueError:
        return False


def _is_allowed_client_ip(client_ip: str) -> bool:
    if client_ip in ("::1", "localhost"):
        return True
    try:
        addr = ipaddress.ip_address(client_ip)
        return addr.is_loopback or (addr in _TAILSCALE_NET)
    except ValueError:
        return False


def create_dashboard_server(
    *,
    db_path: Optional[Path | str] = None,
    host: str = "127.0.0.1",
    port: int = 8765,
    allow_tailscale: bool = False,
    output_path: Optional[Path | str] = None,
) -> ThreadingHTTPServer:
    if _is_loopback_host(host):
        pass
    elif allow_tailscale and _is_tailscale_host(host):
        pass
    else:
        raise ValueError(
            "Host no permitido: solo se acepta loopback (127.0.0.1) o IP privada Tailscale (100.64.0.0/10 con allow_tailscale=True)."
        )

    class _Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            client_ip = self.client_address[0] if self.client_address else ""
            if not _is_allowed_client_ip(client_ip):
                self.send_error(403, "Solo acceso privado loopback o Tailscale.")
                return

            snap = build_executive_snapshot(db_path=db_path, probe_videos=False)
            if self.path.startswith("/api/snapshot"):
                body = json.dumps(snap, ensure_ascii=False, indent=2).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return

            html_path = render_dashboard_html(snap, output_path=output_path)
            body = html_path.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, format: str, *args: Any) -> None:  # noqa: A002
            return

    return ThreadingHTTPServer((host, port), _Handler)


def serve_loopback(
    *,
    db_path: Optional[Path | str] = None,
    host: str = "127.0.0.1",
    port: int = 8765,
    allow_tailscale: bool = False,
) -> None:
    server = create_dashboard_server(
        db_path=db_path,
        host=host,
        port=port,
        allow_tailscale=allow_tailscale,
    )
    print(f"CPAZ Media OS Dashboard en http://{host}:{port} (Ctrl+C para detener)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
