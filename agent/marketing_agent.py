#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Agente de Marketing Autónomo y Adquisición de Pacientes.

Uso:
  python3 -m agent.marketing_agent --calendar          (Muestra la parrilla de contenidos semanal)
  python3 -m agent.marketing_agent --render-posts      (Renderiza todas las piezas gráficas para Instagram)
  python3 -m agent.marketing_agent --export-json       (Exporta payload listo para n8n o webhook)
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path
from agent import content_engine

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "assets" / "instagram"


def print_banner() -> None:
    print("\n" + "=" * 65)
    print(" 🌿 CENTRO PAZ (CPAZ) — AGENTE DE ADQUISICIÓN Y MARKETING")
    print(f" 👩‍⚕️ Terapeuta: {content_engine.BRAND['therapist']} ({content_engine.BRAND['title']})")
    print(f" 📲 WhatsApp: {content_engine.BRAND['phone']} | Web: {content_engine.BRAND['web']}")
    print("=" * 65 + "\n")


def display_calendar() -> None:
    calendar = content_engine.get_weekly_calendar()
    print("📅 PARRILLA SEMANAL DE CONTENIDO DE ALTA CONVERSIÓN:\n")
    for item in calendar:
        print(f"📌 [{item['dia']}] — {item['tipo']}")
        print(f"   Título: {item['titulo']}")
        print(f"   Gancho: {item['gancho']}")
        print(f"   Hashtags: {item['hashtags']}")
        print("-" * 65)


def render_all_posts() -> None:
    print("🎨 Renderizando piezas gráficas de Instagram a PNG (1080x1350)...")
    chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    if not Path(chrome_bin).exists():
        print("⚠️ No se encontró Google Chrome en /Applications/Google Chrome.app. Revisa la ruta.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    html_files = list(OUTPUT_DIR.glob("*.html"))

    if not html_files:
        print("No hay archivos HTML en assets/instagram/")
        return

    for html_p in html_files:
        png_p = html_p.with_suffix(".png")
        print(f"  → Renderizando {html_p.name} a {png_p.name}...")
        cmd = [
            chrome_bin,
            "--headless",
            "--disable-gpu",
            "--window-size=1080,1350",
            f"--screenshot={png_p}",
            "--hide-scrollbars",
            str(html_p)
        ]
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"    ✓ Creado: {png_p.name} ({png_p.stat().st_size // 1024} KB)")
        except Exception as e:
            print(f"    ❌ Error renderizando {html_p.name}: {e}")

    print("\n✅ Todas las piezas gráficas han sido generadas en assets/instagram/")


def export_n8n_json() -> None:
    calendar = content_engine.get_weekly_calendar()
    out_file = ROOT / "agent" / "n8n_marketing_payload.json"
    data = {
        "brand": content_engine.BRAND,
        "weekly_calendar": calendar,
        "lead_magnet_pdf": str(ROOT / "guia_7_claves_regulacion_centro_paz.pdf"),
        "status": "ready_for_dispatch"
    }
    out_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✅ Payload exportado para n8n en: {out_file}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Centro Paz Marketing Agent")
    parser.add_argument("--calendar", action="store_true", help="Mostrar calendario semanal de posts")
    parser.add_argument("--render-posts", action="store_true", help="Renderizar imágenes de Instagram a PNG")
    parser.add_argument("--export-json", action="store_true", help="Exportar JSON para n8n")
    args = parser.parse_args()

    print_banner()

    if args.calendar or not any(vars(args).values()):
        display_calendar()
    if args.render_posts:
        render_all_posts()
    if args.export_json:
        export_n8n_json()


if __name__ == "__main__":
    main()
