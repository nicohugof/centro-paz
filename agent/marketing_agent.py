#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Agente de Marketing Autónomo y Adquisición de Pacientes.

Uso:
  python3 -m agent.marketing_agent --calendar          (Muestra la parrilla de contenidos de 14 días)
  python3 -m agent.marketing_agent --reels             (Muestra guiones virales de Reels/TikTok)
  python3 -m agent.marketing_agent --render-posts      (Renderiza todas las 14 piezas gráficas a PNG)
  python3 -m agent.marketing_agent --export-json       (Exporta payload maestro listo para n8n o webhook)
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path
from agent import content_engine

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "assets" / "instagram"

CHROME_CANDIDATES = [
    os.environ.get("CHROME_BIN", ""),
    "/usr/bin/google-chrome",
    "/usr/bin/google-chrome-stable",
    "/usr/local/bin/google-chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/snap/bin/chromium",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]


def find_chrome() -> str | None:
    for path in CHROME_CANDIDATES:
        if path and Path(path).exists():
            return path
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"):
        found = shutil.which(name)
        if found:
            return found
    return None


def print_banner() -> None:
    print("\n" + "=" * 70)
    print(" 🌿 CENTRO PAZ (CPAZ) — AGENTE DE ADQUISICIÓN Y MARKETING DIGITAL")
    print(f" 👩‍⚕️ Terapeuta: {content_engine.BRAND['therapist']} ({content_engine.BRAND['title']})")
    print(f" 📲 WhatsApp: {content_engine.BRAND['phone_display']} | Web: {content_engine.BRAND['web']}")
    print("=" * 70 + "\n")


def display_calendar() -> None:
    cal_w1 = content_engine.get_weekly_calendar(week=1)
    cal_w2 = content_engine.get_weekly_calendar(week=2)

    print("📅 PARRILLA DE CONTENIDO DE ALTA CONVERSIÓN (14 DÍAS):\n")
    print("─── SEMANA 1: CONCIENCIA, OBJECIONES Y ACCESO ───")
    for item in cal_w1:
        print(f"📌 [Post {item['id']:02d} · {item['dia']}] — {item['tipo']}")
        print(f"   Título: {item['titulo']}")
        print(f"   Gancho: {item['gancho']}")
        print(f"   Hashtags: {item['hashtags']}")
        print("-" * 70)

    print("\n─── SEMANA 2: PROFUNDIZACIÓN, PARENTALIDAD Y CONVERSIÓN ───")
    for item in cal_w2:
        print(f"📌 [Post {item['id']:02d} · {item['dia']}] — {item['tipo']}")
        print(f"   Título: {item['titulo']}")
        print(f"   Gancho: {item['gancho']}")
        print(f"   Hashtags: {item['hashtags']}")
        print("-" * 70)


def display_reels() -> None:
    reels = content_engine.get_reels_catalog()
    print("🎬 GUIONES DE REELS & TIKTOK DE ALTA RETENCIÓN (ALGORITMO ORGANICO):\n")
    for r in reels:
        print(f"🎥 [{r['title']}] · Duración estimada: {r['duration']}")
        print(f"   👁️ Gancho Visual: {r['hook_visual']}")
        print(f"   🗣️ Gancho Auditivo: \"{r['hook_audio']}\"")
        print("   🧠 Desarrollo:")
        for pt in r["development"]:
            print(f"      • {pt}")
        print(f"   🎯 CTA: {r['cta']}")
        print(f"   🎵 Audio sugerido: {r['recommended_audio']}")
        print("-" * 70)


def render_all_posts() -> None:
    print("🎨 Renderizando todas las piezas gráficas de Instagram a PNG (1080x1350)...")
    chrome_bin = find_chrome()

    if not chrome_bin:
        print("⚠️ No se encontró Chrome/Chromium. Instálalo o define CHROME_BIN.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    html_files = sorted(OUTPUT_DIR.glob("*.html"))

    if not html_files:
        print("No hay archivos HTML en assets/instagram/")
        return

    success_count = 0
    for html_p in html_files:
        png_p = html_p.with_suffix(".png")
        print(f"  → Renderizando {html_p.name} a {png_p.name}...")
        file_url = html_p.resolve().as_uri()
        cmd = [
            chrome_bin,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            "--window-size=1080,1350",
            f"--screenshot={png_p}",
            file_url,
        ]
        try:
            subprocess.run(cmd, check=True, capture_output=True, timeout=60)
            print(f"    ✓ Creado: {png_p.name} ({png_p.stat().st_size // 1024} KB)")
            success_count += 1
        except Exception as e:
            err = ""
            if isinstance(e, subprocess.CalledProcessError) and e.stderr:
                err = e.stderr.decode("utf-8", errors="ignore")[:400]
            print(f"    ❌ Error renderizando {html_p.name}: {e} {err}")

    print(f"\n✅ {success_count}/{len(html_files)} piezas gráficas generadas exitosamente en assets/instagram/")


def export_n8n_json() -> None:
    cal_w1 = content_engine.get_weekly_calendar(week=1)
    cal_w2 = content_engine.get_weekly_calendar(week=2)
    catalog = content_engine.get_all_catalog()
    reels = content_engine.get_reels_catalog()

    out_file = ROOT / "agent" / "n8n_marketing_payload.json"
    data = {
        "brand": content_engine.BRAND,
        "lead_magnet_pdf": "https://www.centropaz.cl/guia_7_claves_regulacion_centro_paz.pdf",
        "posts_catalog": catalog,
        "calendar_week_1": cal_w1,
        "calendar_week_2": cal_w2,
        "reels_scripts": reels,
        "status": "ready_for_dispatch"
    }
    out_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✅ Payload extendido exportado para n8n en: {out_file}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Centro Paz Marketing Agent")
    parser.add_argument("--calendar", action="store_true", help="Mostrar calendario de 14 días de publicaciones")
    parser.add_argument("--reels", action="store_true", help="Mostrar guiones virales de Reels y TikTok")
    parser.add_argument("--render-posts", action="store_true", help="Renderizar imágenes de Instagram a PNG")
    parser.add_argument("--export-json", action="store_true", help="Exportar JSON maestro para n8n")
    args = parser.parse_args()

    print_banner()

    if args.calendar:
        display_calendar()
    if args.reels:
        display_reels()
    if args.render_posts:
        render_all_posts()
    if args.export_json:
        export_n8n_json()

    if not any(vars(args).values()):
        display_calendar()
        print("\n💡 Tip: Ejecuta con --reels para ver guiones de video, --render-posts para generar PNGs, o --export-json para n8n.\n")


if __name__ == "__main__":
    main()

