#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Centro de Comando Operativo y Adquisición de Pacientes.

Ejecutar:
  python3 cpaz.py
"""
from __future__ import annotations

import sys
import subprocess
from agent import whatsapp_assistant, video_shorts_generator, organic_lead_scout, marketing_agent, blog_generator


def print_menu():
    print("\n" + "=" * 75)
    print(" 🌿 CENTRO PAZ (CPAZ) — PANEL DE COMANDO WEB 2.0 & CAPTACIÓN DE PACIENTES")
    print(" 📍 Ñuñoa (Santiago) & Online para todo Chile")
    print(" 📲 WhatsApp Oficial: +56 9 6516 3893 | Web: www.centropaz.cl")
    print("=" * 75)
    print(" 1. 🛡️  Ejecutar Auditoría Integral del Consejo (37 páginas + Schemas + Links)")
    print(" 2. 🔍  Ejecutar Auditoría Técnica SEO & GEO para Motores de IA")
    print(" 3. 🌐  Regenerar Biblioteca Clínica (28 guías, llms.txt, robots.txt, sitemap)")
    print(" 4. 🚀  Lanzar Servidor Web Local para Prueba de Conversiones (http://localhost:8000)")
    print(" 5. 💬  Asistente Rápido de WhatsApp (Protocolo de Cierre Humano para Valentina)")
    print(" 6. 📊  Ver Playbook de Google Ads Search & Plan 100 Pacientes")
    print(" 7. 🎨  Renderizar las 28 Infografías a PNG (1080x1350)")
    print(" 8. 📡  Exportar Payloads para n8n")
    print(" 0. 🚪  Salir")
    print("=" * 75 + "\n")


def main():
    while True:
        try:
            print_menu()
            choice = input("👉 Selecciona una opción (0-8): ").strip()
            if choice == "1":
                from agent import audit_consejo
                audit_consejo.run_comprehensive_audit()
            elif choice == "2":
                from agent import seo_audit_engine
                seo_audit_engine.audit_html_files()
            elif choice == "3":
                blog_generator.build_all()
            elif choice == "4":
                print("\n🚀 Iniciando servidor local en http://localhost:8000 ...")
                print("💡 Abre http://localhost:8000/?debug=true en tu navegador para probar el tracking.")
                print("⌨️  Presiona Ctrl+C para detener el servidor.\n")
                try:
                    subprocess.run([sys.executable, "-m", "http.server", "8000"])
                except KeyboardInterrupt:
                    print("\n🛑 Servidor local detenido.")
            elif choice == "5":
                whatsapp_assistant.interactive_mode()
            elif choice == "6":
                print("\n📖 Archivos de Estrategia Publicitaria y Crecimiento:")
                print("  • Plan 100 Pacientes:      docs/PLAN_100_PACIENTES_VALENTINA.md")
                print("  • Playbook Google Ads:     docs/GOOGLE_ADS_SEARCH_PLAYBOOK.md")
                print("  • Medición Conversiones:   docs/GOOGLE_ADS_CONVERSION_TRACKING.md")
                print("  • Perfil Google Maps:      docs/GOOGLE_BUSINESS_PROFILE_NUNOA.md\n")
            elif choice == "7":
                marketing_agent.render_all_posts()
            elif choice == "8":
                marketing_agent.export_n8n_json()
            elif choice in ["0", "salir", "exit", "quit", "q"]:
                print("\n🌿 Centro Paz en operación continua. Hasta pronto.\n")
                break
            else:
                print("⚠️ Opción no válida. Ingresa un número del 0 al 8.")
        except (KeyboardInterrupt, EOFError):
            print("\n\n🌿 Sesión finalizada.")
            break


if __name__ == "__main__":
    main()

