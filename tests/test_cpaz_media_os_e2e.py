"""
Suite E2E Real de CPAZ Media OS (Centro Paz).

Valida con ejecutores y artefactos reales:
1. Firewall de privacidad clínica (Ley N° 19.628) y aislamiento absoluto de `data/patient_intakes.json`.
2. Reutilización de `content_engine` + `blog_clinical_knowledge`, QA clínico y adaptador `Ollama` (MIT).
3. Estudio audiovisual con `ffprobe` + `ffmpeg` CLI reales y protección de `video_engine/public/`.
4. Calendario editorial, máquina de estados y gate obligatorio `PUBLICAR <ID>` / `AUTORIZO`.
5. Puente de automatización `n8n` (aprobado-only) y publicadores desacoplados dry-run.
6. Atribución UTM compatible con `app.js`, analítica anónima y Dashboard Ejecutivo HTML.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from media_os.attribution import AttributionEngine, build_utm_links
from media_os.automation import export_n8n_approved_schedule
from media_os.calendar import ApprovalRequiredError, EditorialCalendar
from media_os.cli import run_demo_e2e
from media_os.dashboard import (
    _is_allowed_client_ip,
    build_executive_snapshot,
    create_dashboard_server,
    render_dashboard_html,
)
from media_os.intelligence import OllamaAdapter, StrategicIntelligenceEngine, run_clinical_qa
from media_os.privacy import PrivacyViolationError, assert_no_pii, assert_path_not_clinical
from media_os.publishers import (
    DryRunLocalPublisher,
    ExternalOSSPublisherContract,
    MetaGraphPublisherAdapter,
)
from media_os.studio import ComfyUIAdapter, MediaStudio, ROOT, UnsafeOutputPathError


def test_privacy_firewall_and_clinical_isolation():
    # Bloquea RUT, teléfono ajeno y claves clínicas
    with pytest.raises(PrivacyViolationError):
        assert_no_pii({"texto": "Paciente RUT 12.345.678-K consulta"})
    with pytest.raises(PrivacyViolationError):
        assert_no_pii({"phone": "+56 9 8765 4321"})
    with pytest.raises(PrivacyViolationError):
        assert_no_pii({"ficha_clinica": "reservada"})
    with pytest.raises(PrivacyViolationError):
        assert_path_not_clinical(ROOT / "data" / "patient_intakes.json")

    # Permite explícitamente canales públicos oficiales de Centro Paz
    assert_no_pii(
        {
            "cta": "WhatsApp oficial +56 9 6516 3893 o contacto.centropaz@gmail.com",
            "web": "https://wa.me/56965163893",
        }
    )

    # Garantía estática: ningún módulo en media_os/ lee patient_intakes ni patient_intake_manager
    media_os_files = [
        p for p in (ROOT / "media_os").glob("*.py") if p.name != "privacy.py"
    ]
    for py_file in media_os_files:
        src = py_file.read_text(encoding="utf-8")
        assert "patient_intake" not in src, f"{py_file.name} no debe referenciar datos clínicos"


def test_intelligence_qa_and_ollama_adapter(tmp_path):
    db_file = tmp_path / "intel.db"
    engine = StrategicIntelligenceEngine(db_path=db_file)

    audit = engine.audit_existing_knowledge()
    assert audit["topics_count"] >= 28
    assert audit["clinical_articles_count"] >= 28
    assert audit["reels_scripts_count"] >= 7
    assert audit["brand_fee_clp"] == 45000

    # QA Clínico bloquea promesas prohibidas o aranceles obsoletos
    bad_qa = run_clinical_qa(
        title="Cura definitiva en 1 sesión",
        caption="Valor $40.000 con diagnóstico definitivo en reel.",
        require_cta=True,
    )
    assert not bad_qa.passed
    assert any("prohibida" in issue.lower() for issue in bad_qa.issues)
    assert any("arancel" in issue.lower() for issue in bad_qa.issues)

    # Verifica fallback determinista limpio si endpoint Ollama no responde
    offline_adapter = OllamaAdapter(base_url="http://127.0.0.1:59999", timeout_sec=0.3)
    offline_engine = StrategicIntelligenceEngine(db_path=db_file, generator=offline_adapter)
    brief = offline_engine.generate_strategic_brief("tdah_adultos", use_llm=True)
    assert brief["topic_key"] == "tdah_adultos"
    assert brief["source_engine"] == "cpaz-kb-deterministic"
    assert brief["qa"]["passed"] is True
    assert brief["clinical_foundation_present"] is True

    # Si Ollama local corre activamente en el Mac, prueba inferencia real local ($0/mes)
    live_ollama = OllamaAdapter(timeout_sec=15.0)
    if live_ollama.is_available():
        live_engine = StrategicIntelligenceEngine(db_path=db_file, generator=live_ollama)
        live_brief = live_engine.generate_strategic_brief("reembolso_isapre", use_llm=True)
        assert live_brief["source_engine"] in ("ollama-local", "cpaz-kb-deterministic")
        assert live_brief["strategic_summary"]


def test_audiovisual_studio_real_ffmpeg_and_public_protection(tmp_path):
    studio = MediaStudio(exports_dir=tmp_path)
    caps = studio.capabilities()
    assert caps["ffmpeg_bin"], "ffmpeg debe estar disponible en PATH"
    assert caps["ffprobe_bin"], "ffprobe debe estar disponible en PATH"

    inv = studio.inventory_existing_assets()
    assert inv["instagram_png_count"] >= 28
    assert inv["videos_mp4_count"] >= 10
    assert "voice_short01.mp3" in inv["protected_video_engine_public"]

    public_voice = ROOT / "video_engine" / "public" / "voice_short01.mp3"
    before_sha = hashlib.sha256(public_voice.read_bytes()).hexdigest()

    # Protección estricta contra escritura en video_engine/public/
    sample_mp4 = ROOT / "assets" / "videos" / "cpaz_short01_tdah.mp4"
    with pytest.raises(UnsafeOutputPathError):
        studio.extract_thumbnail(sample_mp4, output_image=ROOT / "video_engine" / "public" / "forbidden.jpg")

    # FFprobe real sobre el video existente
    probe = studio.probe_video(sample_mp4)
    assert probe["duration_sec"] > 5.0
    assert probe["width"] > 0 and probe["height"] > 0
    assert probe["is_vertical_short"] is True

    # FFmpeg CLI real: miniatura + recorte breve en tmp_path
    thumb = studio.extract_thumbnail(sample_mp4, output_image=tmp_path / "thumb.jpg", at_sec=1.0)
    assert Path(thumb["thumbnail_path"]).exists() and thumb["size_bytes"] > 1000

    clip = studio.create_preview_clip(
        sample_mp4, output_mp4=tmp_path / "clip.mp4", start_sec=0.0, duration_sec=1.2
    )
    assert Path(clip["clip_path"]).exists()
    assert 0.8 <= clip["duration_sec"] <= 2.2

    # ComfyUI deshabilitado por política
    comfy = ComfyUIAdapter().generate_image({"prompt": "ilustración calma"})
    assert comfy["executed"] is False and comfy["status"] == "disabled_by_policy"

    # Confirmar archivo público sin cambios
    after_sha = hashlib.sha256(public_voice.read_bytes()).hexdigest()
    assert before_sha == after_sha


def test_editorial_approval_gate_publishers_and_n8n_bridge(tmp_path):
    db_file = tmp_path / "editorial.db"
    cal = EditorialCalendar(db_path=db_file)
    seeded = cal.seed_from_weekly_plan(week=1, channel="instagram")
    assert len(seeded) == 7

    target = seeded[0]
    pending = seeded[1]

    # Prohibido programar, publicar o aprobar sin pasar QA + token exacto
    with pytest.raises(ApprovalRequiredError):
        cal.schedule_item(target["item_id"], scheduled_for="2026-11-12T12:00:00-03:00")
    with pytest.raises(ApprovalRequiredError):
        DryRunLocalPublisher(calendar=cal).publish(target)
    with pytest.raises(ApprovalRequiredError):
        cal.approve_item(target["item_id"], approval_token=f"NO AUTORIZO {target['item_id']}")

    # Flujo válido: QA -> PUBLICAR <ID> -> Schedule
    cal.run_qa(target["item_id"])
    approved = cal.approve_item(
        target["item_id"],
        approval_token=f"PUBLICAR {target['item_id']}",
        reviewer="Nicolas",
    )
    assert approved["status"] == "APPROVED"
    scheduled = cal.schedule_item(approved["item_id"], scheduled_for="2026-11-12T12:00:00-03:00")
    assert scheduled["status"] == "SCHEDULED"

    # Exportador n8n incluye solo los aprobados y excluye los 6 borradores restantes
    export_file = tmp_path / "n8n_schedule.json"
    export_res = export_n8n_approved_schedule(cal, output_file=export_file)
    assert export_res["approved_count"] == 1
    assert export_res["excluded_unapproved_count"] == 6
    exported_ids = {item["item_id"] for item in json.loads(export_file.read_text())["items"]}
    assert exported_ids == {scheduled["item_id"]}
    assert pending["item_id"] not in exported_ids

    # Contrato AGPL documentado para Postiz sin habilitar
    postiz_contract = ExternalOSSPublisherContract(target_platform="postiz").build_dispatch_contract(scheduled)
    assert postiz_contract["enabled"] is False
    assert postiz_contract["license"] == "AGPL-3.0"

    # Publicador Meta envuelto falla cerrado si allow_live=True y simula si allow_live=False
    with pytest.raises(PermissionError):
        MetaGraphPublisherAdapter(calendar=cal, allow_live=True).publish(scheduled)

    meta_dry = MetaGraphPublisherAdapter(calendar=cal, allow_live=False).publish(scheduled)
    assert meta_dry["ok"] is True
    assert meta_dry["receipt"]["network_call_executed"] is False
    assert meta_dry["item"]["status"] == "PUBLISHED_DRYRUN"


def test_utm_attribution_full_e2e_and_dashboard(tmp_path):
    db_file = tmp_path / "e2e_full.db"
    utm = build_utm_links(
        topic_key="tdah_adultos",
        utm_source="instagram",
        utm_medium="organic",
        utm_campaign="sem1_tdah",
        utm_content="post_01",
    )
    assert "utm_source=instagram" in utm["landing_url"]
    assert "wa.me/56965163893" in utm["whatsapp_url"]

    attr = AttributionEngine(db_path=db_file)
    # Importador externo rechaza fila con PII
    with pytest.raises(PrivacyViolationError):
        attr.import_external_aggregates(
            [{"topic_key": "tdah_adultos", "patient_name": "Juan", "impressions": 100, "clicks": 10}]
        )

    imported = attr.import_external_aggregates(
        [{"topic_key": "tdah_adultos", "channel": "web", "utm_campaign": "sem1_tdah", "impressions": 800, "clicks": 40}],
        source_system="umami",
    )
    assert imported == 1

    # Flujo completo E2E sobre la misma DB aislada
    res = run_demo_e2e(
        db_path=db_file,
        use_llm=False,
        n8n_output_file=tmp_path / "demo_n8n.json",
        dashboard_output_path=tmp_path / "demo_dashboard.html",
    )
    assert res["published_dryrun_status"] == "PUBLISHED_DRYRUN"
    assert res["n8n_approved_count"] == 1
    assert res["attribution_totals"]["bookings"] >= 1
    assert res["attribution_totals"]["estimated_value_clp"] >= 45000

    # Render dashboard en tmp_path y validar ausencia de PII + métricas reales
    snap = build_executive_snapshot(db_path=db_file, probe_videos=True)
    dash_path = render_dashboard_html(snap, output_path=tmp_path / "dashboard.html")
    html_text = dash_path.read_text(encoding="utf-8")
    assert "CPAZ Media OS" in html_text
    assert "667344" in html_text
    assert "AGPL-3.0" in html_text
    assert "+56 9 6516 3893" in html_text
    assert "fichas clínicas y datos de pacientes aislados" in html_text


def test_dashboard_server_tailscale_and_client_guard(tmp_path):
    import threading
    import urllib.request

    # Rechaza 0.0.0.0, IPs públicas y Tailscale sin opt-in explícito
    with pytest.raises(ValueError):
        create_dashboard_server(host="0.0.0.0", port=0)
    with pytest.raises(ValueError):
        create_dashboard_server(host="8.8.8.8", port=0, allow_tailscale=True)
    with pytest.raises(ValueError):
        create_dashboard_server(host="100.109.254.61", port=0, allow_tailscale=False)

    assert _is_allowed_client_ip("100.89.124.62") is True
    assert _is_allowed_client_ip("127.0.0.1") is True
    assert _is_allowed_client_ip("8.8.8.8") is False

    srv = create_dashboard_server(
        db_path=tmp_path / "srv.db",
        host="127.0.0.1",
        port=0,
        output_path=tmp_path / "served.html",
    )
    port = srv.server_address[1]
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=5) as resp:
            assert resp.status == 200
            body = resp.read().decode("utf-8")
            assert "CPAZ Media OS" in body
        # /api/snapshot sin autenticación debe responder 401 Unauthorized
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(f"http://127.0.0.1:{port}/api/snapshot", timeout=5)
        assert exc_info.value.code == 401

        # /api/snapshot con cabecera Authorization válida responde 200 OK
        req_snap = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/snapshot",
            headers={"Authorization": f"Bearer {srv.session_token}"},
        )
        with urllib.request.urlopen(req_snap, timeout=5) as resp:
            assert resp.status == 200
            snap = json.loads(resp.read().decode("utf-8"))
            assert snap["identity"]["sis_registration"] == "667344"
    finally:
        srv.shutdown()
        srv.server_close()


def test_dashboard_server_post_endpoints_and_batch_calendar(tmp_path):
    import threading
    import urllib.error
    import urllib.request
    from media_os import cli as media_os_cli

    db_file = tmp_path / "post_test.db"
    srv = create_dashboard_server(
        db_path=db_file,
        host="127.0.0.1",
        port=0,
        output_path=tmp_path / "served_post.html",
    )
    port = srv.server_address[1]
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        # 1. POST /api/seed
        auth_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {srv.session_token}",
        }
        req_seed = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/seed",
            data=b"{}",
            headers=auth_headers,
            method="POST",
        )
        with urllib.request.urlopen(req_seed, timeout=5) as resp:
            assert resp.status == 200
            data = json.loads(resp.read().decode("utf-8"))
            assert data["ok"] is True
            assert data["count"] == 28

        # 2. POST /api/qa-all
        req_qa = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/qa-all",
            data=b"{}",
            headers=auth_headers,
            method="POST",
        )
        with urllib.request.urlopen(req_qa, timeout=5) as resp:
            assert resp.status == 200
            data = json.loads(resp.read().decode("utf-8"))
            assert data["ok"] is True
            assert data["results"]["passed"] == 28

        first_item_id = data["results"]["items"][0]["item_id"]

        # 3. POST /api/approve rechaza token inválido (HTTP 400)
        req_bad_approve = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/approve",
            data=json.dumps({"item_id": first_item_id, "approval_token": "NO AUTORIZO"}).encode("utf-8"),
            headers=auth_headers,
            method="POST",
        )
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(req_bad_approve, timeout=5)
        assert exc_info.value.code == 400

        # 4. POST /api/approve con token válido
        req_good_approve = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/approve",
            data=json.dumps({
                "item_id": first_item_id,
                "approval_token": f"PUBLICAR {first_item_id}",
                "reviewer": "Nicolas",
            }).encode("utf-8"),
            headers=auth_headers,
            method="POST",
        )
        with urllib.request.urlopen(req_good_approve, timeout=5) as resp:
            assert resp.status == 200
            data = json.loads(resp.read().decode("utf-8"))
            assert data["ok"] is True
            assert data["item"]["status"] == "APPROVED"

        # 5. POST /api/export-n8n (la pieza aprobada debe estar en la cola)
        req_export = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/export-n8n",
            data=b"{}",
            headers=auth_headers,
            method="POST",
        )
        with urllib.request.urlopen(req_export, timeout=5) as resp:
            assert resp.status == 200
            data = json.loads(resp.read().decode("utf-8"))
            assert data["ok"] is True
            assert data["result"]["approved_count"] == 1

        # 6. POST /api/publish-dryrun sobre pieza aprobada
        req_pub = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/publish-dryrun",
            data=json.dumps({"item_id": first_item_id}).encode("utf-8"),
            headers=auth_headers,
            method="POST",
        )
        with urllib.request.urlopen(req_pub, timeout=5) as resp:
            assert resp.status == 200
            data = json.loads(resp.read().decode("utf-8"))
            assert data["ok"] is True
            assert data["result"]["item"]["status"] == "PUBLISHED_DRYRUN"

    finally:
        srv.shutdown()
        srv.server_close()

    # 7. Validar CLI seed y qa-all sobre una DB temporal
    cli_db = tmp_path / "cli_test.db"
    cal = EditorialCalendar(db_path=cli_db)
    seeded = cal.seed_all_topics()
    assert len(seeded) == 28
    qa_res = cal.run_qa_all()
    assert qa_res["total"] == 28 and qa_res["passed"] == 28


def test_dashboard_server_security_protections(tmp_path):
    import threading
    import urllib.error
    import urllib.request

    db_file = tmp_path / "sec_test.db"
    srv = create_dashboard_server(
        db_path=db_file,
        host="127.0.0.1",
        port=0,
        output_path=tmp_path / "served_sec.html",
    )
    port = srv.server_address[1]
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    auth_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {srv.session_token}",
    }
    try:
        # 1. Cabeceras de seguridad en GET
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=5) as resp:
            assert resp.headers.get("X-Content-Type-Options") == "nosniff"
            assert resp.headers.get("X-Frame-Options") == "DENY"
            assert "Content-Security-Policy" in resp.headers

        # 2. Protección contra DNS Rebinding (Host no autorizado) -> HTTP 403
        req_rebinding = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/snapshot",
            headers={"Host": "attacker-rebinding.com:8765"},
        )
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(req_rebinding, timeout=5)
        assert exc_info.value.code == 403

        # 3. Protección contra llamadas cross-site (Sec-Fetch-Site: cross-site) -> HTTP 403
        req_cross_site = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/seed",
            data=b"{}",
            headers={**auth_headers, "Sec-Fetch-Site": "cross-site"},
            method="POST",
        )
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(req_cross_site, timeout=5)
        assert exc_info.value.code == 403

        # 4. Protección contra CSRF (Origin malicioso) -> HTTP 403
        req_bad_origin = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/seed",
            data=b"{}",
            headers={**auth_headers, "Origin": "https://malicious-website.com"},
            method="POST",
        )
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(req_bad_origin, timeout=5)
        assert exc_info.value.code == 403

        # 5. Protección contra Payload excesivo (> 64 KB) -> HTTP 413
        req_oversized = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/seed",
            data=b"x" * 70000,
            headers=auth_headers,
            method="POST",
        )
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(req_oversized, timeout=5)
        assert exc_info.value.code == 413

        # 6. Sanitización y validación estricta de item_id en /api/approve -> HTTP 400
        req_malformed_item = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/approve",
            data=json.dumps({"item_id": "' OR 1=1;--", "approval_token": "PUBLICAR test"}).encode("utf-8"),
            headers=auth_headers,
            method="POST",
        )
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(req_malformed_item, timeout=5)
        assert exc_info.value.code == 400

        # 7. Rechazo de Referer no autorizado -> HTTP 403
        req_bad_referer = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/seed",
            data=b"{}",
            headers={**auth_headers, "Referer": "https://evil-attacker.com/page"},
            method="POST",
        )
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(req_bad_referer, timeout=5)
        assert exc_info.value.code == 403

        # 8. Rechazo de Content-Type no JSON en POST (mitiga HTML forms simples) -> HTTP 415
        req_bad_ct = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/seed",
            data=b"dummy=1",
            headers={"Content-Type": "application/x-www-form-urlencoded", "Authorization": f"Bearer {srv.session_token}"},
            method="POST",
        )
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(req_bad_ct, timeout=5)
        assert exc_info.value.code == 415

        # 9. Método OPTIONS no permitido (CORS preflight cerrado) -> HTTP 405
        req_options = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/seed",
            method="OPTIONS",
        )
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(req_options, timeout=5)
        assert exc_info.value.code == 405

        # 10. Rutas no existentes -> HTTP 404
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(f"http://127.0.0.1:{port}/unknown_route", timeout=5)
        assert exc_info.value.code == 404

        # 11. Autenticación: POST sin cabecera de autenticación -> HTTP 401
        req_no_auth = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/seed",
            data=b"{}",
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(req_no_auth, timeout=5)
        assert exc_info.value.code == 401

        # 12. Autenticación: POST con Bearer token falso -> HTTP 401
        req_bad_token = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/seed",
            data=b"{}",
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer token_falso_invalido_1234567890",
            },
            method="POST",
        )
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(req_bad_token, timeout=5)
        assert exc_info.value.code == 401

        # 13. Seguridad de Parámetros en URL: GET /api/snapshot con ?token=... debe ser RECHAZADO (HTTP 401)
        # Demuestra que no se transmiten ni aceptan secretos en query strings de URLs
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(f"http://127.0.0.1:{port}/api/snapshot?token={srv.session_token}", timeout=5)
        assert exc_info.value.code == 401

        # 14. Flujo de Login Seguro: POST /api/login con token erróneo -> HTTP 401
        req_bad_login = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/login",
            data=json.dumps({"token": "incorrect_token_xyz"}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(req_bad_login, timeout=5)
        assert exc_info.value.code == 401

        # 15. Flujo de Login Seguro: POST /api/login con token válido -> HTTP 200 y Cookie HttpOnly SameSite=Strict
        req_good_login = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/login",
            data=json.dumps({"token": srv.session_token}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req_good_login, timeout=5) as resp:
            assert resp.status == 200
            login_data = json.loads(resp.read().decode("utf-8"))
            assert login_data["ok"] is True
            csrf_token = login_data["csrf_token"]
            assert csrf_token and len(csrf_token) >= 16
            assert srv.session_token not in login_data.values()

            cookie_header = resp.headers.get("Set-Cookie") or ""
            assert "cpaz_session=" in cookie_header
            assert "SameSite=Strict" in cookie_header
            assert "HttpOnly" in cookie_header
            assert srv.session_token not in cookie_header

            # Extraer cookie de sesión
            session_cookie = cookie_header.split(";")[0].strip()

        # 16. Acceso Autenticado vía Cookie: GET / con Cookie válida sirve el dashboard autenticado
        req_auth_cookie = urllib.request.Request(
            f"http://127.0.0.1:{port}/",
            headers={"Cookie": session_cookie},
        )
        with urllib.request.urlopen(req_auth_cookie, timeout=5) as resp:
            assert resp.status == 200
            dash_body = resp.read().decode("utf-8")
            assert "28 Temas" in dash_body or "CPAZ Media OS" in dash_body
            assert f'meta name="cpaz-csrf-token" content="{csrf_token}"' in dash_body
            assert "cpaz-session-token" not in dash_body
            assert srv.session_token not in dash_body

            # CSP con nonce dinámico y sin 'unsafe-inline' en script-src
            csp_val = resp.headers.get("Content-Security-Policy") or ""
            assert "script-src 'self' 'nonce-" in csp_val
            script_csp_part = csp_val.split("script-src")[1].split(";")[0]
            assert "'unsafe-inline'" not in script_csp_part

        # 17. GET sin autenticación no expone tokens en metaetiqueta
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=5) as resp:
            login_body = resp.read().decode("utf-8")
            assert 'meta name="cpaz-csrf-token" content=""' in login_body
            assert "cpaz-session-token" not in login_body
            assert srv.session_token not in login_body

        # 18. Mutaciones con sesión Cookie requieren validación de X-CSRF-Token
        # A) Sin cabecera X-CSRF-Token -> HTTP 403
        req_no_csrf = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/seed",
            data=b"{}",
            headers={"Content-Type": "application/json", "Cookie": session_cookie},
            method="POST",
        )
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(req_no_csrf, timeout=5)
        assert exc_info.value.code == 403

        # B) Con cabecera X-CSRF-Token válida -> HTTP 200
        req_with_csrf = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/seed",
            data=b"{}",
            headers={
                "Content-Type": "application/json",
                "Cookie": session_cookie,
                "X-CSRF-Token": csrf_token,
            },
            method="POST",
        )
        with urllib.request.urlopen(req_with_csrf, timeout=5) as resp:
            assert resp.status == 200
            seed_data = json.loads(resp.read().decode("utf-8"))
            assert seed_data["ok"] is True

        # 19. Cierre de sesión seguro: POST /api/logout invalida la cookie y sesión
        req_logout = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/logout",
            data=b"{}",
            headers={
                "Content-Type": "application/json",
                "Cookie": session_cookie,
                "X-CSRF-Token": csrf_token,
            },
            method="POST",
        )
        with urllib.request.urlopen(req_logout, timeout=5) as resp:
            assert resp.status == 200
            logout_cookie = resp.headers.get("Set-Cookie") or ""
            assert "Max-Age=0" in logout_cookie

        # Posterior intento de acceso con sesión cerrada a /api/snapshot -> HTTP 401
        req_post_logout = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/snapshot",
            headers={"Cookie": session_cookie},
        )
        with pytest.raises(urllib.error.HTTPError) as exc_info:
            urllib.request.urlopen(req_post_logout, timeout=5)
        assert exc_info.value.code == 401

    finally:
        srv.shutdown()
        srv.server_close()

    # 20. Verificaciones de seguridad a nivel de librerías y transiciones de estado
    from media_os.calendar import _validate_approval_token
    assert _validate_approval_token("", "PUBLICAR test") is False
    assert _validate_approval_token(None, "PUBLICAR test") is False
    assert _validate_approval_token("test_id", "") is False
    assert _validate_approval_token("test_id", None) is False

    # Validar que DryRunLocalPublisher falle cerrado ante item nulo o malformado
    from media_os.publishers import DryRunLocalPublisher, ApprovalRequiredError
    cal = EditorialCalendar(db_path=db_file)
    pub = DryRunLocalPublisher(calendar=cal)
    with pytest.raises(ApprovalRequiredError):
        pub.publish(None)
    with pytest.raises(ApprovalRequiredError):
        pub.publish({})

    # 21. Verificación de aislamiento en disco: build_dashboard_html en memoria no altera el archivo estático
    from media_os.dashboard import build_dashboard_html, DEFAULT_DASHBOARD_HTML
    static_before = DEFAULT_DASHBOARD_HTML.read_text(encoding="utf-8") if DEFAULT_DASHBOARD_HTML.exists() else ""
    snap = build_executive_snapshot(db_path=db_file, probe_videos=False)
    mem_html = build_dashboard_html(snap, csrf_token="test_csrf_token_in_memory_12345")
    assert "test_csrf_token_in_memory_12345" in mem_html
    if DEFAULT_DASHBOARD_HTML.exists():
        static_after = DEFAULT_DASHBOARD_HTML.read_text(encoding="utf-8")
        assert "test_csrf_token_in_memory_12345" not in static_after
        assert static_after == static_before




