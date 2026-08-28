#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Generador de Guiones de Video Corto para YouTube Shorts, TikTok y Reels.

Diseñado para producir videos verticales (9:16) de alta retención orgánica que derivan
tráfico hacia WhatsApp (+56 9 6516 3893) y el sitio web (www.centropaz.cl).
"""
from __future__ import annotations

import argparse
from typing import List, Dict, Any

SHORTS_CATALOG: List[Dict[str, Any]] = [
    {
        "id": "short_01",
        "platform": ["TikTok", "YouTube Shorts", "Instagram Reels"],
        "target": "Adultos con sospecha de TDAH",
        "title": "3 Señales de TDAH en Adultos que siempre confundiste con flojera",
        "duration": "35-40 seg",
        "visual_hook_text": "3 cosas que parecían flojera pero eran TDAH 🧠",
        "steps": [
            {
                "time": "0:00 - 0:03",
                "scene": "Valentina mirando a cámara con expresión empática / Texto en pantalla grande",
                "audio": "¿Sientes que tienes el potencial para hacer todo, pero te quedas paralizado/a frente a una tarea simple?",
                "on_screen_text": "Parálisis por baja dopamina"
            },
            {
                "time": "0:03 - 0:15",
                "scene": "Gesto de contar con la mano (1, 2, 3)",
                "audio": "Número 1: Procrastinación no por desinterés, sino por parálisis ejecutiva. Tu cerebro necesita un nivel mínimo de dopamina para 'arrancar'.",
                "on_screen_text": "1. Parálisis ejecutiva ≠ flojera"
            },
            {
                "time": "0:15 - 0:25",
                "scene": "Cambio de plano / Gesto de cansancio mental",
                "audio": "Número 2: Agotamiento crónico por 'masking', el esfuerzo inconsciente de sobre-adaptarte para que nadie note tu desorganización.",
                "on_screen_text": "2. Cansancio por 'Masking'"
            },
            {
                "time": "0:25 - 0:35",
                "scene": "Gesto de alivio / Calma",
                "audio": "Número 3: Hipersensibilidad al rechazo o miedo intenso a cometer un error.",
                "on_screen_text": "3. Sensibilidad al rechazo"
            },
            {
                "time": "0:35 - 0:40",
                "scene": "Tarjeta de marca con logo Centro Paz",
                "audio": "En Centro Paz te acompañamos con un enfoque 100% neuroafirmativo. Escríbenos por WhatsApp en el enlace de la bio.",
                "on_screen_text": "Sesiones Online y en Ñuñoa · Reembolso Isapre"
            }
        ],
        "hashtags": "#TDAHAdultos #TDAHChile #YouTubeShortsChile #SaludMentalChile #Neurodivergencia #PsicologiaSantiago",
        "recommended_sound": "Audio hablado claro con fondo lofi sutil (40 BPM)"
    },
    {
        "id": "short_02",
        "platform": ["TikTok", "YouTube Shorts", "Instagram Reels"],
        "target": "Pacientes con Isapre que no se atienden por costo",
        "title": "La matemática secreta del reembolso de Isapre en psicología",
        "duration": "30 seg",
        "visual_hook_text": "Cuánto pagas REALMENTE por ir al psicólogo en Chile 💳",
        "steps": [
            {
                "time": "0:00 - 0:03",
                "scene": "Mostrando boleta electrónica o calculadora en el teléfono",
                "audio": "¿Sabías que no tienes que pagar $45.000 de tu bolsillo por cada sesión de psicología?",
                "on_screen_text": "¿Cuánto cuesta realmente la terapia?"
            },
            {
                "time": "0:03 - 0:15",
                "scene": "Demostración gráfica rápida",
                "audio": "Al atenderte en Centro Paz te emitimos boleta electrónica con código de la Superintendencia de Salud. Tu Isapre (Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres) te devuelve entre el 50% y el 80%.",
                "on_screen_text": "Reembolso directo de 50% a 80%"
            },
            {
                "time": "0:15 - 0:25",
                "scene": "Texto grande con el copago final",
                "audio": "Eso significa que tu copago real puede quedar en unos $12.000 a $15.000 pesos por sesión.",
                "on_screen_text": "Copago real: ~$15.000 CLP"
            },
            {
                "time": "0:25 - 0:30",
                "scene": "CTA final",
                "audio": "Prueba nuestro simulador gratuito en www.centropaz.cl o escríbenos a WhatsApp para orientarte.",
                "on_screen_text": "WhatsApp: +56 9 6516 3893"
            }
        ],
        "hashtags": "#ReembolsoIsapre #IsapreChile #SaludMentalChile #PsicologiaChile #DatoUtilChile",
        "recommended_sound": "Efectos de sonido sutiles de 'cash register' o 'pop'"
    },
    {
        "id": "short_03",
        "platform": ["TikTok", "YouTube Shorts", "Pinterest Video"],
        "target": "Madres y Padres con hijos en edad escolar",
        "title": "Qué hacer cuando tu hijo entra en un desborde emocional intenso",
        "duration": "35 seg",
        "visual_hook_text": "Por qué decirle 'cálmate' a tu hijo empeora la rabieta 🌱",
        "steps": [
            {
                "time": "0:00 - 0:04",
                "scene": "Valentina explicando con calma",
                "audio": "Cuando un niño o niña está en plena rabieta, su corteza lógica está apagada. Intentar razonar en ese instante solo aumenta el cortisol.",
                "on_screen_text": "La corteza lógica está apagada"
            },
            {
                "time": "0:04 - 0:18",
                "scene": "Demostración de los 3 pasos de corregulación",
                "audio": "Aplica estos 3 pasos: 1. Baja tu tono de voz y la iluminación. 2. Ofrécele tu presencia física segura sin forzar el contacto. 3. Valida lo que siente: 'Veo que esto es muy difícil para ti'.",
                "on_screen_text": "1. Baja estímulos · 2. Presencia · 3. Valida"
            },
            {
                "time": "0:18 - 0:28",
                "scene": "Enfoque clínico",
                "audio": "La conversación y las normas se enseñan después, cuando su sistema nervioso vuelve a la calma.",
                "on_screen_text": "Corregulación antes de educar"
            },
            {
                "time": "0:28 - 0:35",
                "scene": "Descarga gratuita",
                "audio": "Descarga gratis nuestra Guía de 7 Claves en PDF en el link de la bio o pídela por WhatsApp.",
                "on_screen_text": "Guía en PDF Gratis en www.centropaz.cl"
            }
        ],
        "hashtags": "#CrianzaRespetuosa #PsicologiaInfantil #MaternidadChile #PaternidadConsciente #OrientacionAPadres",
        "recommended_sound": "Música acústica cálida y reflexiva"
    }
]


def display_catalog():
    print("\n" + "=" * 70)
    print(" 🎬 CENTRO PAZ — CATÁLOGO DE VIDEOS CORTOS (YOUTUBE SHORTS, TIKTOK, REELS)")
    print("=" * 70 + "\n")
    for s in SHORTS_CATALOG:
        print(f"📌 [{s['id'].upper()}] {s['title']}")
        print(f"   🎯 Plataformas: {', '.join(s['platform'])} | Audiencia: {s['target']}")
        print(f"   ⏱️ Duración: {s['duration']}")
        print(f"   👁️ Gancho en pantalla: {s['visual_hook_text']}")
        print("   📜 Guion por bloques:")
        for step in s["steps"]:
            print(f"      [{step['time']}] {step['on_screen_text']}")
            print(f"         🗣️ \"{step['audio']}\"")
        print(f"   🎵 Sonido sugerido: {s['recommended_sound']}")
        print(f"   🏷️ Hashtags: {s['hashtags']}")
        print("-" * 70)


def main():
    parser = argparse.ArgumentParser(description="Generador de guiones para YouTube Shorts y TikTok")
    parser.add_argument("--list", "-l", action="store_true", help="Listar todos los guiones de video")
    args = parser.parse_args()
    display_catalog()


if __name__ == "__main__":
    main()
