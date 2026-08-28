#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Centro de Comando Operativo y Adquisición de Pacientes.

Ejecutar:
  python3 cpaz.py
"""
from __future__ import annotations

import sys
import subprocess
from agent import whatsapp_assistant, video_shorts_generator, organic_lead_scout, marketing_agent


def print_menu():
    print("\n" + "=" * 70)
    print(" 🌿 CENTRO PAZ (CPAZ) — PANEL DE CONTROL Y ADQUISICIÓN DE PACIENTES")
    print(" 📍 Ñuñoa (Santiago) & Online para todo Chile")
    print(" 📲 WhatsApp Oficial: +56 9 6516 3893 | Web: www.centropaz.cl")
    print("=" * 70)
    print(" 1. 💬 Asistente Rápido de WhatsApp (Cierre de Pacientes · Valentina)")
    print(" 2. 🎬 Generador de Guiones de Video (YouTube Shorts / TikTok / Reels)")
    print(" 3. 🔍 Scout de Respuestas Orgánicas (Comunidades y Foros)")
    print(" 4. 📅 Ver Parrilla de Contenidos y Matriz Omnicanal")
    print(" 5. 🎨 Renderizar las 14 Infografías a PNG (1080x1350)")
    print(" 6. 📡 Exportar Payloads Actualizados para n8n y Redes Sociales")
    print(" 0. 🚪 Salir")
    print("=" * 70 + "\n")


def main():
    while True:
        try:
            print_menu()
            choice = input("👉 Selecciona una opción (0-6): ").strip()
            if choice == "1":
                whatsapp_assistant.interactive_mode()
            elif choice == "2":
                video_shorts_generator.display_catalog()
            elif choice == "3":
                organic_lead_scout.main()
            elif choice == "4":
                marketing_agent.display_multiplatform()
                marketing_agent.display_calendar()
            elif choice == "5":
                marketing_agent.render_all_posts()
            elif choice == "6":
                marketing_agent.export_n8n_json()
            elif choice in ["0", "salir", "exit", "quit", "q"]:
                print("\n🌿 Hasta pronto. Centro Paz en operación continua.\n")
                break
            else:
                print("⚠️ Opción no válida. Ingresa un número del 0 al 6.")
        except (KeyboardInterrupt, EOFError):
            print("\n\n🌿 Sesión finalizada.")
            break


if __name__ == "__main__":
    main()
