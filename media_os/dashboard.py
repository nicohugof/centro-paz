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
import os
import re
import secrets
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import parse_qs, urlparse

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


def build_dashboard_html(
    snapshot: Dict[str, Any],
    *,
    session_token: str = "",
) -> str:
    tot = snapshot["attribution"]["totals"]
    cal = snapshot["calendar_summary"]
    kb = snapshot["knowledge_audit"]
    rt = snapshot["runtime"]
    inv = snapshot["assets_inventory"]

    pending_rows = []
    items = snapshot.get("editorial_items", [])
    for item in items:
        badge_cls = "ok" if item["status"] in ("APPROVED", "SCHEDULED", "PUBLISHED_DRYRUN") else (
            "warn" if item["status"] == "CLINICAL_QA" else "muted"
        )
        token_cmd = item.get("approval_token") or f"PUBLICAR {item['item_id']}"
        pending_rows.append(
            f"<tr data-status='{html.escape(item['status'])}' data-search='{html.escape((item['item_id'] + ' ' + item['title'] + ' ' + item['channel'] + ' ' + item['status']).lower())}'>"
            f"<td><code>{html.escape(item['item_id'])}</code></td>"
            f"<td><strong>{html.escape(item['title'][:58])}</strong></td>"
            f"<td>{html.escape(item['channel'])} / {html.escape(item['format_type'])}</td>"
            f"<td><span class='badge {badge_cls}'>{html.escape(item['status'])}</span></td>"
            f"<td>{'✅ SI' if item['qa_passed'] else '⚠️ PEND'}</td>"
            f"<td>"
            f"<div class='action-cell'>"
            f"<button type='button' class='btn-copy' onclick='copyCmd(\"{html.escape(token_cmd)}\")' title='Copiar comando al portapapeles'>📋 Copiar</button>"
            f"<code>{html.escape(token_cmd)}</code>"
            f"</div>"
            f"</td>"
            f"</tr>"
        )
    if not pending_rows:
        pending_rows.append("<tr class='empty-row'><td colspan='6'>Sin piezas cargadas aún en calendario local. Haz clic en <strong>\"Poblar 28 Temas\"</strong> para inicializar.</td></tr>")

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
  <meta name="cpaz-session-token" content="{html.escape(session_token)}" />
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
    .table-toolbar {{
      display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between;
      gap: 12px; margin-bottom: 14px; padding-bottom: 12px; border-bottom: 1px solid var(--border);
    }}
    .search-box {{ flex: 1; min-width: 220px; }}
    .search-input {{
      width: 100%; padding: 8px 12px; border: 1px solid var(--border); border-radius: 8px;
      font-size: 0.88rem; outline: none; transition: border-color 0.2s; box-sizing: border-box;
    }}
    .search-input:focus {{ border-color: var(--accent); }}
    .filter-pills {{ display: flex; flex-wrap: wrap; gap: 6px; }}
    .pill {{
      background: #eef1ef; border: 1px solid var(--border); border-radius: 999px;
      padding: 4px 10px; font-size: 0.78rem; font-weight: 600; cursor: pointer; color: var(--ink);
      transition: all 0.15s ease;
    }}
    .pill:hover {{ background: #e0e8e3; }}
    .pill.active {{ background: var(--accent); color: #fff; border-color: var(--accent); }}
    .ops-actions {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .btn-ops {{
      background: var(--accent); color: #ffffff; border: none; border-radius: 8px;
      padding: 6px 12px; font-size: 0.8rem; font-weight: 600; cursor: pointer;
      transition: opacity 0.15s ease;
    }}
    .btn-ops:hover {{ opacity: 0.9; }}
    .btn-ops.secondary {{ background: #eef1ef; color: var(--ink); border: 1px solid var(--border); }}
    .btn-ops.secondary:hover {{ background: #e0e8e3; }}
    .action-cell {{ display: flex; align-items: center; gap: 6px; }}
    .btn-copy {{
      background: #f0f4f1; border: 1px solid var(--border); border-radius: 6px;
      padding: 3px 8px; font-size: 0.75rem; font-weight: 600; cursor: pointer; color: var(--accent);
      white-space: nowrap; transition: background 0.15s;
    }}
    .btn-copy:hover {{ background: var(--accent-soft); }}
    .toast {{
      visibility: hidden; min-width: 250px; background-color: #1b2420; color: #fff;
      text-align: center; border-radius: 8px; padding: 12px 18px; position: fixed;
      z-index: 1000; left: 50%; bottom: 30px; transform: translateX(-50%); font-size: 0.88rem;
      box-shadow: 0 4px 14px rgba(0,0,0,0.2); opacity: 0; transition: opacity 0.3s, visibility 0.3s;
    }}
    .toast.show {{ visibility: visible; opacity: 1; }}
    .toast.error {{ background-color: #b02a37; }}
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
      <div class="table-toolbar">
        <div class="search-box">
          <input type="text" id="searchInput" class="search-input" placeholder="🔍 Filtrar por tema, ID, canal o estado..." oninput="filterTable()" />
        </div>
        <div class="filter-pills">
          <button type="button" class="pill active" onclick="setFilter('ALL', this)">Todos ({len(items)})</button>
          <button type="button" class="pill" onclick="setFilter('DRAFT', this)">Borradores ({cal.get('DRAFT', 0)})</button>
          <button type="button" class="pill" onclick="setFilter('CLINICAL_QA', this)">QA ({cal.get('CLINICAL_QA', 0)})</button>
          <button type="button" class="pill" onclick="setFilter('APPROVED', this)">Aprobados ({cal.get('APPROVED', 0)})</button>
          <button type="button" class="pill" onclick="setFilter('PUBLISHED_DRYRUN', this)">Dry-Run ({cal.get('PUBLISHED_DRYRUN', 0)})</button>
        </div>
        <div class="ops-actions">
          <button type="button" class="btn-ops" onclick="runApi('/api/seed', 'Poblando 28 tópicos...')">📥 Poblar 28 Temas</button>
          <button type="button" class="btn-ops" onclick="runApi('/api/qa-all', 'Auditando QA clínico...')">🩺 Auditar QA</button>
          <button type="button" class="btn-ops" onclick="runApi('/api/export-n8n', 'Exportando n8n...')">🚀 Exportar n8n</button>
          <button type="button" class="btn-ops secondary" onclick="location.reload()">🔄 Refrescar</button>
        </div>
      </div>
      <table id="editorialTable">
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
  <div id="toast" class="toast"></div>
  <script id="cpaz-media-os-snapshot" type="application/json">{safe_json}</script>
  <script>
    let currentStatusFilter = 'ALL';
    function showToast(msg, isError = false) {{
      const t = document.getElementById('toast');
      t.textContent = msg;
      t.className = 'toast show' + (isError ? ' error' : '');
      setTimeout(() => {{ t.className = 'toast'; }}, 3200);
    }}

    function copyCmd(cmd) {{
      if (navigator.clipboard && navigator.clipboard.writeText) {{
        navigator.clipboard.writeText(cmd).then(() => {{
          showToast('Copiado al portapapeles: ' + cmd);
        }}).catch(() => {{
          fallbackCopy(cmd);
        }});
      }} else {{
        fallbackCopy(cmd);
      }}
    }}

    function fallbackCopy(text) {{
      const ta = document.createElement('textarea');
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
      showToast('Copiado al portapapeles: ' + text);
    }}

    function setFilter(status, btn) {{
      currentStatusFilter = status;
      document.querySelectorAll('.filter-pills .pill').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      filterTable();
    }}

    function filterTable() {{
      const query = (document.getElementById('searchInput').value || '').toLowerCase().trim();
      const rows = document.querySelectorAll('#editorialTable tbody tr:not(.empty-row)');
      rows.forEach(tr => {{
        const text = tr.getAttribute('data-search') || '';
        const status = tr.getAttribute('data-status') || '';
        const matchesQuery = !query || text.includes(query);
        const matchesFilter = currentStatusFilter === 'ALL' || status === currentStatusFilter;
        tr.style.display = (matchesQuery && matchesFilter) ? '' : 'none';
      }});
    }}

    async function runApi(endpoint, loadingMsg) {{
      if (window.location.protocol === 'file:') {{
        alert('El dashboard está abierto como archivo estático (file://).\\nPara ejecutar acciones interactivas en vivo, inicia el servidor con:\\npython3 cpaz.py (opción M) o python3 -m media_os.cli serve');
        return;
      }}
      showToast(loadingMsg);
      const metaToken = document.querySelector('meta[name="cpaz-session-token"]');
      const sessionToken = metaToken ? (metaToken.getAttribute('content') || '') : '';
      try {{
        const res = await fetch(endpoint, {{
          method: 'POST',
          headers: {{
            'Content-Type': 'application/json',
            'X-CPAZ-Action': 'media-os-dashboard',
            'X-CPAZ-Session-Token': sessionToken,
            'Authorization': 'Bearer ' + sessionToken
          }},
          body: JSON.stringify({{}})
        }});
        const data = await res.json();
        if (data.ok) {{
          showToast('Operación exitosa');
          setTimeout(() => location.reload(), 900);
        }} else {{
          showToast('Error: ' + (data.error || 'Fallo desconocido'), true);
        }}
      }} catch (err) {{
        showToast('Error de red al conectar con el servidor local: ' + err.message, true);
      }}
    }}
  </script>
</body>
</html>
"""
    return html_doc


def render_dashboard_html(
    snapshot: Dict[str, Any],
    *,
    output_path: Optional[Path | str] = None,
    session_token: str = "",
) -> Path:
    dest = Path(output_path) if output_path else DEFAULT_DASHBOARD_HTML
    dest.parent.mkdir(parents=True, exist_ok=True)
    html_doc = build_dashboard_html(snapshot, session_token=session_token)
    dest.write_text(html_doc, encoding="utf-8")
    return dest


MAX_BODY_BYTES = 64 * 1024  # 64 KB límite estricto para mitigar ataques de denegación de servicio


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


def _is_allowed_origin(origin: Optional[str]) -> bool:
    if not origin:
        return True
    parsed = urlparse(origin)
    host = (parsed.hostname or "").lower()
    if host in ("127.0.0.1", "localhost", "::1"):
        return True
    return _is_tailscale_host(host)


def _validate_host_header(host_header: Optional[str], *, allow_tailscale: bool) -> bool:
    if not host_header:
        return True
    bare_host = host_header.split(":")[0].strip().lower()
    if bare_host in ("127.0.0.1", "localhost", "::1"):
        return True
    if allow_tailscale and _is_tailscale_host(bare_host):
        return True
    return False


def create_dashboard_server(
    *,
    db_path: Optional[Path | str] = None,
    host: str = "127.0.0.1",
    port: int = 8765,
    allow_tailscale: bool = False,
    output_path: Optional[Path | str] = None,
    session_token: Optional[str] = None,
) -> ThreadingHTTPServer:
    if _is_loopback_host(host):
        pass
    elif allow_tailscale and _is_tailscale_host(host):
        pass
    else:
        raise ValueError(
            "Host no permitido: solo se acepta loopback (127.0.0.1) o IP privada Tailscale (100.64.0.0/10 con allow_tailscale=True)."
        )

    active_token = session_token or os.getenv("CPAZ_MEDIA_OS_SESSION_TOKEN") or secrets.token_hex(24)

    class _Handler(BaseHTTPRequestHandler):
        def _send_security_headers(self) -> None:
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("X-Frame-Options", "DENY")
            self.send_header(
                "Content-Security-Policy",
                "default-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'",
            )
            self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")

        def do_OPTIONS(self) -> None:  # noqa: N802
            self.send_response(405)
            self._send_security_headers()
            self.send_header("Allow", "GET, POST")
            self.end_headers()

        def do_GET(self) -> None:  # noqa: N802
            client_ip = self.client_address[0] if self.client_address else ""
            if not _is_allowed_client_ip(client_ip):
                self.send_error(403, "Solo acceso privado loopback o Tailscale.")
                return

            if not _validate_host_header(self.headers.get("Host"), allow_tailscale=allow_tailscale):
                self.send_error(403, "Host no autorizado (protección anti DNS rebinding activa).")
                return

            # Si el cliente proviene de Tailscale, exigir token de autenticación
            try:
                addr = ipaddress.ip_address(client_ip)
                is_tailscale_client = addr in _TAILSCALE_NET
            except ValueError:
                is_tailscale_client = False

            if is_tailscale_client:
                auth_header = self.headers.get("Authorization") or ""
                token_header = self.headers.get("X-CPAZ-Session-Token") or ""
                query_token = ""
                if "?" in self.path:
                    parsed_q = parse_qs(self.path.split("?", 1)[1])
                    query_token = parsed_q.get("token", [""])[0]
                bearer = auth_header[7:].strip() if auth_header.startswith("Bearer ") else ""
                presented = bearer or token_header or query_token
                if not secrets.compare_digest(presented, active_token):
                    self.send_error(401, "Acceso privado Tailscale requiere token de sesión (?token=<token> o cabecera Authorization).")
                    return

            clean_path = self.path.split("?")[0].rstrip("/") or "/"
            snap = build_executive_snapshot(db_path=db_path, probe_videos=False)
            if clean_path == "/api/snapshot":
                body = json.dumps(snap, ensure_ascii=False, indent=2).encode("utf-8")
                self.send_response(200)
                self._send_security_headers()
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return

            if clean_path in ("/", "/index.html"):
                if output_path:
                    html_path = render_dashboard_html(snap, output_path=output_path, session_token=active_token)
                    body = html_path.read_bytes()
                else:
                    body = build_dashboard_html(snap, session_token=active_token).encode("utf-8")
                self.send_response(200)
                self._send_security_headers()
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return

            self.send_error(404, f"Ruta no encontrada: {clean_path}")

        def do_POST(self) -> None:  # noqa: N802
            client_ip = self.client_address[0] if self.client_address else ""
            if not _is_allowed_client_ip(client_ip):
                self.send_error(403, "Solo acceso privado loopback o Tailscale.")
                return

            if not _validate_host_header(self.headers.get("Host"), allow_tailscale=allow_tailscale):
                self.send_error(403, "Host no autorizado (protección anti DNS rebinding activa).")
                return

            # Autenticación criptográfica obligatoria en todos los endpoints POST
            auth_header = self.headers.get("Authorization") or ""
            token_header = self.headers.get("X-CPAZ-Session-Token") or ""
            bearer = auth_header[7:].strip() if auth_header.startswith("Bearer ") else ""
            presented_token = bearer or token_header
            if not secrets.compare_digest(presented_token, active_token):
                self.send_error(401, "Autenticación requerida: token de sesión inválido o ausente.")
                return

            # Mitigación CSRF y Cross-Origin: rechazar explícitamente orígenes ajenos y Sec-Fetch-Site cross-site
            if self.headers.get("Sec-Fetch-Site") == "cross-site":
                self.send_error(403, "Petición cross-site bloqueada por política CSRF.")
                return

            origin = self.headers.get("Origin")
            if origin and not _is_allowed_origin(origin):
                self.send_error(403, "Origen HTTP no autorizado (protección anti-CSRF activa).")
                return

            referer = self.headers.get("Referer")
            if referer and not _is_allowed_origin(referer):
                self.send_error(403, "Referer HTTP no autorizado (protección anti-CSRF activa).")
                return

            clean_path = self.path.split("?")[0].rstrip("/")
            valid_endpoints = (
                "/api/seed",
                "/api/qa-all",
                "/api/approve",
                "/api/publish-dryrun",
                "/api/export-n8n",
            )
            if clean_path not in valid_endpoints:
                self.send_error(404, f"Endpoint no encontrado: {clean_path}")
                return

            content_type = (self.headers.get("Content-Type") or "").split(";")[0].strip().lower()
            if content_type and content_type != "application/json":
                self.send_error(415, "Tipo de contenido no soportado. Se exige application/json.")
                return

            content_length_str = self.headers.get("Content-Length")
            if content_length_str is not None:
                try:
                    length = int(content_length_str)
                    if length < 0:
                        self.send_error(400, "Content-Length inválido.")
                        return
                    if length > MAX_BODY_BYTES:
                        self.send_error(413, "Cuerpo de solicitud excede el límite permitido (64 KB).")
                        return
                except ValueError:
                    self.send_error(400, "Content-Length inválido.")
                    return
            else:
                length = 0

            raw_body = self.rfile.read(length) if length > 0 else b"{}"
            try:
                payload = json.loads(raw_body.decode("utf-8")) if raw_body else {}
            except Exception:
                payload = {}

            from media_os.calendar import EditorialCalendar, ApprovalRequiredError
            from media_os.publishers import DryRunLocalPublisher
            from media_os.automation import export_n8n_approved_schedule

            cal_inst = EditorialCalendar(db_path=db_path)

            try:
                if self.path.startswith("/api/seed"):
                    created = cal_inst.seed_all_topics()
                    resp = {"ok": True, "action": "seed", "count": len(created), "items": created}
                elif self.path.startswith("/api/qa-all"):
                    results = cal_inst.run_qa_all()
                    resp = {"ok": True, "action": "qa-all", "results": results}
                elif self.path.startswith("/api/approve"):
                    item_id = str(payload.get("item_id", "")).strip()
                    if not re.match(r"^[a-zA-Z0-9_-]{3,64}$", item_id):
                        raise ValueError(f"Identificador de ítem inválido: '{item_id}'.")
                    token = str(payload.get("approval_token", ""))[:128].strip()
                    reviewer = str(payload.get("reviewer", "Nicolas"))[:64].strip()
                    reason = str(payload.get("reason", "Aprobación desde Dashboard CPAZ"))[:256].strip()
                    item = cal_inst.approve_item(item_id, approval_token=token, reviewer=reviewer, reason=reason)
                    resp = {"ok": True, "action": "approve", "item": item}
                elif self.path.startswith("/api/publish-dryrun"):
                    item_id = str(payload.get("item_id", "")).strip()
                    if not re.match(r"^[a-zA-Z0-9_-]{3,64}$", item_id):
                        raise ValueError(f"Identificador de ítem inválido: '{item_id}'.")
                    item = cal_inst.get_item(item_id)
                    if not item:
                        raise KeyError(f"Pieza no encontrada: {item_id}")
                    pub = DryRunLocalPublisher(calendar=cal_inst)
                    res = pub.publish(item)
                    resp = {"ok": True, "action": "publish-dryrun", "result": res}
                elif self.path.startswith("/api/export-n8n"):
                    res = export_n8n_approved_schedule(cal_inst)
                    resp = {"ok": True, "action": "export-n8n", "result": res}
                else:
                    self.send_error(404, f"Endpoint no encontrado: {self.path}")
                    return

                assert_no_pii(resp, field_path="api_post_response")
                out_bytes = json.dumps(resp, ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self._send_security_headers()
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Content-Length", str(len(out_bytes)))
                self.end_headers()
                self.wfile.write(out_bytes)
            except (ApprovalRequiredError, KeyError, ValueError) as err:
                err_resp = {"ok": False, "error": str(err)}
                out_bytes = json.dumps(err_resp, ensure_ascii=False).encode("utf-8")
                self.send_response(400)
                self._send_security_headers()
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Content-Length", str(len(out_bytes)))
                self.end_headers()
                self.wfile.write(out_bytes)
            except Exception:
                err_resp = {"ok": False, "error": "Error interno del servidor."}
                out_bytes = json.dumps(err_resp, ensure_ascii=False).encode("utf-8")
                self.send_response(500)
                self._send_security_headers()
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Content-Length", str(len(out_bytes)))
                self.end_headers()
                self.wfile.write(out_bytes)

        def log_message(self, format: str, *args: Any) -> None:  # noqa: A002
            return

    srv = ThreadingHTTPServer((host, port), _Handler)
    srv.session_token = active_token  # type: ignore[attr-defined]
    return srv


def serve_loopback(
    *,
    db_path: Optional[Path | str] = None,
    host: str = "127.0.0.1",
    port: int = 8765,
    allow_tailscale: bool = False,
    session_token: Optional[str] = None,
) -> None:
    server = create_dashboard_server(
        db_path=db_path,
        host=host,
        port=port,
        allow_tailscale=allow_tailscale,
        session_token=session_token,
    )
    print(f"CPAZ Media OS Dashboard en http://{host}:{port} (Token de sesión: {getattr(server, 'session_token', '')})")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
