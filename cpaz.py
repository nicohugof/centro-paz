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
    print(" 1. ⚡  Ejecutar Rutina Operativa Diaria (Tablero + Embudos + Ping IndexNow)")
    print(" 2. 🛡️  Ejecutar Auditoría Integral del Consejo (37 páginas + Schemas + Links)")
    print(" 3. 🔍  Ejecutar Auditoría Técnica SEO & GEO para Motores de IA")
    print(" 4. 🌐  Regenerar Biblioteca Clínica (28 guías, llms.txt, robots.txt, sitemap)")
    print(" 5. 🚀  Lanzar Servidor Web Local para Prueba de Conversiones (http://localhost:8000)")
    print(" 6. 💬  Asistente Rápido de WhatsApp (Protocolo de Cierre Humano para Valentina)")
    print(" 7. 🎯  Tablero Clínico de Ingresos y Meta de 100 Pacientes (Seguimiento Real)")
    print(" 8. 📊  Ver Playbooks de Crecimiento (Google Ads, Encuadrado, Mapas, Alianzas)")
    print(" 9. 🎨  Renderizar las 28 Infografías a PNG (1080x1350)")
    print(" 0. 🚪  Salir")
    print("=" * 75 + "\n")


def main():
    while True:
        try:
            print_menu()
            choice = input("👉 Selecciona una opción (0-9): ").strip()
            if choice == "1":
                from agent import daily_clinic_routine
                daily_clinic_routine.run_daily_routine()
            elif choice == "2":
                from agent import audit_consejo
                audit_consejo.run_comprehensive_audit()
            elif choice == "3":
                from agent import seo_audit_engine
                seo_audit_engine.audit_html_files()
            elif choice == "4":
                blog_generator.build_all()
            elif choice == "5":
                print("\n🚀 Iniciando servidor local en http://localhost:8000 ...")
                print("💡 Abre http://localhost:8000/?debug=true en tu navegador para probar el tracking.")
                print("⌨️  Presiona Ctrl+C para detener el servidor.\n")
                try:
                    subprocess.run([sys.executable, "-m", "http.server", "8000"])
                except KeyboardInterrupt:
                    print("\n🛑 Servidor local detenido.")
            elif choice == "6":
                from agent import fast_whatsapp_responder
                fast_whatsapp_responder.interactive_responder()
            elif choice == "7":
                from agent import patient_intake_manager
                patient_intake_manager.interactive_intake()
            elif choice == "8":
                print("\n📖 Archivos de Estrategia Publicitaria y Crecimiento:")
                print("  • Plan 100 Pacientes:      docs/PLAN_100_PACIENTES_VALENTINA.md")
                print("  • Dictamen del Consejo:    docs/DICTAMEN_CONSEJO_ESTRATEGIA_100_PACIENTES.md")
                print("  • Playbook Google Ads:     docs/GOOGLE_ADS_SEARCH_PLAYBOOK.md")
                print("  • Medición Conversiones:   docs/GOOGLE_ADS_CONVERSION_TRACKING.md")
                print("  • Perfil Google Maps:      docs/FICHA_GOOGLE_BUSINESS_PROFILE_LISTA.md")
                print("  • Perfil Encuadrado:       docs/PERFIL_ENCUADRADO_DOCTORALIA_VALENTINA.md")
                print("  • Directorio Alianzas:     docs/DIRECTORIO_MAESTRO_ALIANZAS_NUNOA.md\n")
            elif choice == "9":
                marketing_agent.render_all_posts()
            elif choice in ["0", "salir", "exit", "quit", "q"]:
                print("\n🌿 Centro Paz en operación continua. Hasta pronto.\n")
                break
            else:
                print("⚠️ Opción no válida. Ingresa un número del 0 al 9.")
        except (KeyboardInterrupt, EOFError):
            print("\n\n🌿 Sesión finalizada.")
            break


if __name__ == "__main__":
    main()

