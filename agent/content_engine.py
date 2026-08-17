"""
Motor de Contenidos Clínicos y Copywriting de Alta Conversión para Centro Paz (CPAZ).
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import List, Dict

BRAND = {
    "name": "Centro Paz",
    "therapist": "Valentina Castro Núñez",
    "title": "Psicóloga Clínica",
    "approach": "Humanista e Integrativo (Especialista en Neurodivergencias e Infanto-Juvenil)",
    "phone": "+56965163893",
    "email": "contacto.centropaz@gmail.com",
    "instagram": "@centropaz.cl",
    "tiktok": "@centropaz.cl",
    "web": "https://www.centropaz.cl",
    "isapres": "Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres y Seguros Complementarios",
}

HASHTAGS_BASE = [
    "#CentroPaz", "#PsicologiaChile", "#PsicologaClinica", "#SaludMentalChile",
    "#TerapiaOnlineChile", "#ReembolsoIsapre", "#ValentinaCastroPsicologa"
]

TOPICS = {
    "tdah_adultos": {
        "kicker": "Neurodivergencias en Adultos",
        "title": "¿Y si ese cansancio crónico no es flojera, sino TDAH tardío?",
        "hook": "¿Siempre te dijeron que eras 'demasiado disperso' o que no te esforzabas lo suficiente?",
        "points": [
            "Procrastinación paralizante ante tareas que parecen simples para otros.",
            "Agotamiento crónico por 'masking' (forzarte a encajar y compensar el doble).",
            "Sensibilidad aguda al rechazo o miedo constante a equivocarte.",
            "Hipersensibilidad sensorial (ruidos, luces, sobreestimulación)."
        ],
        "category": "Neurodivergencias",
        "caption": """¿Te pasa que quieres empezar mil cosas y sientes una pared invisible que te frena? 🧠✨

Muchas personas adultas descubren su neurodivergencia (TDAH o TEA) después de los 25 o 30 años, tras décadas de sentirse "diferentes" o sobrecargadas sin entender por qué.

En Centro Paz no buscamos encajarte en moldes ni juzgarte: trabajamos desde un enfoque neuroafirmativo para ayudarte a comprender tu funcionamiento singular y construir estrategias reales para tu vida cotidiana y laboral.

📍 Sesiones online (todo Chile) y presenciales (Santiago).
💳 Boletas 100% reembolsables en Isapres y Seguros Complementarios.

👉 ¿Te gustaría agendar una primera sesión? Haz clic en el enlace de nuestra biografía o escríbenos directo por WhatsApp al +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#TDAHAdultos", "#TDAHChile", "#NeurodivergenciaChile", "#AutismoAdultos", "#TEAChile"]
    },
    "reembolso_isapre": {
        "kicker": "Claridad y Cobertura",
        "title": "Cómo reembolsar tus sesiones de psicología en 3 pasos",
        "hook": "¿Sabías que tu Isapre o Seguro puede cubrir entre el 50% y el 80% de tu terapia?",
        "points": [
            "1. Asistes a tu sesión online o presencial con Valentina.",
            "2. Al terminar recibes tu boleta electrónica de honorarios profesionales.",
            "3. La subes a la app de tu Isapre y recibes el depósito directo en tu cuenta bancaria."
        ],
        "category": "Reembolsos",
        "caption": """Cuidar tu salud mental no tiene por qué ser una carga económica abrumadora 🌿💳

En Centro Paz emitimos boletas electrónicas de honorarios profesionales con código de psicología clínica válidas para:
✨ Todas las Isapres (Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres, Nueva Masvida).
✨ Seguros Complementarios de Salud (MetLife, Bice, Bci, etc.).

El copago real puede quedar tan bajo como $15.000 por sesión según tu plan.

👉 Usa el simulador de reembolsos en nuestra web (link en bio) o escríbenos por WhatsApp al +56 9 6516 3893 para orientarte con tu cobertura.""",
        "hashtags": HASHTAGS_BASE + ["#ReembolsoPsicologia", "#IsapreColmena", "#IsapreBanmedica", "#IsapreCruzBlanca", "#CopagoPsicologia"]
    },
    "crianza_regulacion": {
        "kicker": "Infancia & Crianza",
        "title": "Una rabieta intensa no es manipulación: es sobrecarga sensorial",
        "hook": "Cuando un niño/a se desborda, no busca molestarte: su sistema nervioso colapsó.",
        "points": [
            "Evita el 'cálmate ya': durante el desborde la corteza lógica está apagada.",
            "Baja luces y ruidos ambientales para descomprimir la sobrecarga sensorial.",
            "Valida con calma: 'Veo que esto te sobrepasó, estoy aquí contigo'."
        ],
        "category": "Crianza Respetuosa",
        "caption": """Criar a un hijo/a con desafíos de regulación emocional o características neurodivergentes puede ser agotador cuando no se tienen las herramientas adecuadas 🌱🤍

El castigo o el aislamiento en momentos de desborde aumentan la angustia. Lo que ayuda es la corregulación: prestarle tu calma hasta que su sistema nervioso vuelva al equilibrio.

En Centro Paz acompañamos a niños, niñas y adolescentes, y brindamos orientación continua a padres para construir un hogar en calma y sin gritos.

👉 Para coordinar una primera sesión de orientación infanto-juvenil, encuéntranos en el link de la biografía o al WhatsApp +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#CrianzaRespetuosa", "#PsicologiaInfantil", "#TEAInfantil", "#TDAHInfantil", "#OrientacionAPadres"]
    }
}


def get_weekly_calendar() -> List[Dict]:
    """Genera una parrilla semanal completa de 5 publicaciones de alta conversión."""
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    keys = list(TOPICS.keys())
    calendar = []
    
    types = [
        ("Educación & Validación (Neurodivergencias)", "tdah_adultos"),
        ("Derribador de Objeción (Reembolso Isapre)", "reembolso_isapre"),
        ("Orientación a Padres & Crianza", "crianza_regulacion"),
        ("Autocuidado & Límites en Adultos", "tdah_adultos"),
        ("Llamado directo a Agendamiento", "reembolso_isapre")
    ]
    
    for i, (theme, key) in enumerate(types):
        topic = TOPICS[key]
        calendar.append({
            "dia": days[i],
            "tipo": theme,
            "titulo": topic["title"],
            "gancho": topic["hook"],
            "copy": topic["caption"],
            "hashtags": " ".join(topic["hashtags"])
        })
    return calendar
