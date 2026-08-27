"""
Motor de Contenidos Clínicos y Copywriting de Alta Conversión para Centro Paz (CPAZ).
"""
from __future__ import annotations

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
    "facebook": "https://www.facebook.com/profile.php?id=61593207820690",
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
    },
    "masking": {
        "kicker": "Agotamiento Invisible",
        "title": "El costo invisible del masking: llegar a casa sin energía ni para hablar",
        "hook": "¿Llegas a casa después del trabajo sintiendo que no te queda energía ni para hablar?",
        "points": [
            "Forzar gestos, tono de voz y contacto visual para 'pasar desapercibido'.",
            "Reprimir incomodidades sensoriales (ruidos, luces, ropa, olores) durante horas.",
            "El colapso llega en privado: mutismo, irritabilidad o necesidad de aislamiento.",
            "El descanso no alcanza porque el sistema nervioso estuvo en alerta todo el día."
        ],
        "category": "Neurodivergencias",
        "caption": """¿Llegas a casa después del trabajo o reuniones sintiendo que no te queda energía ni para hablar? 🧠

El "masking" es el esfuerzo consciente o inconsciente de forzar gestos, reprimir incomodidades sensoriales y actuar "como los demás esperan" para no ser juzgado/a.

En Centro Paz te acompañamos a construir un espacio seguro donde puedas desenmascarar con tranquilidad y proteger tu salud mental.

📍 Sesiones online y presenciales con boleta reembolsable en Isapres y Seguros.
👉 Agenda en el enlace de la bio o al WhatsApp +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#Masking", "#AutismoAdultos", "#TEAChile", "#BurnoutAutista", "#NeurodivergenciaChile"]
    },
    "terapia_online": {
        "kicker": "Acceso desde todo Chile",
        "title": "Terapia online con la misma rigurosidad clínica, desde tu espacio de calma",
        "hook": "Atenderte desde tu habitación reduce la ansiedad y elimina los tiempos de traslado.",
        "points": [
            "Misma duración (50 minutos) y confidencialidad que una sesión presencial.",
            "Boleta electrónica válida para reembolso en Isapre y seguro complementario.",
            "Ideal si vives fuera de Santiago o tu sistema nervioso agradece menos transiciones.",
            "Solo necesitas un espacio privado y conexión estable."
        ],
        "category": "Modalidad",
        "caption": """Atenderte desde tu habitación o espacio de calma reduce la ansiedad y elimina los tiempos de traslado 💻🌿

La terapia online cuenta con la misma rigurosidad y efectividad clínica, y recibes tu boleta electrónica exactamente igual para reembolsar en tu Isapre o Seguro.

👉 Encuentra el acompañamiento que necesitas en www.centropaz.cl (Link en Bio).""",
        "hashtags": HASHTAGS_BASE + ["#TerapiaOnline", "#PsicologiaOnlineChile", "#SaludMentalDigital"]
    },
    "evaluacion_infantil": {
        "kicker": "Infancia & Escuela",
        "title": "¿Cuándo consultar con una psicóloga infantil?",
        "hook": "Los desbordes frecuentes y la hipersensibilidad no son 'mala conducta': son un pedido de ayuda.",
        "points": [
            "Desbordes intensos difíciles de calmar, incluso en casa.",
            "Hipersensibilidad a ruidos, texturas, luces o cambios de rutina.",
            "El colegio sugiere evaluación por atención, adaptación o regulación.",
            "Tú como mamá o papá necesitas pautas claras, no más culpa."
        ],
        "category": "Infanto-Juvenil",
        "caption": """¿Cuándo es momento de consultar con una psicóloga infantil? 🌱

Desbordes intensos frecuentes, hipersensibilidad a ruidos o texturas, y dificultades de adaptación escolar son señales de que tu hijo/a necesita apoyo y tú como mamá o papá necesitas pautas clínicas claras.

👉 Contáctanos por WhatsApp al +56 9 6516 3893 para coordinar una primera sesión de orientación.""",
        "hashtags": HASHTAGS_BASE + ["#PsicologiaInfantil", "#OrientacionAPadres", "#TDAHInfantil", "#TEAInfantil"]
    },
    "autocuidado_adultos": {
        "kicker": "Primer paso",
        "title": "Pedir ayuda no es debilidad: es cuidar tu sistema nervioso",
        "hook": "No tienes que poder con todo sola/o.",
        "points": [
            "50 minutos a la semana dedicados 100% a ti.",
            "Espacio sin juicios, con Valentina Castro Núñez.",
            "Herramientas concretas para ansiedad, límites y sobrecarga.",
            "Boleta reembolsable: el copago puede quedar cerca de $15.000."
        ],
        "category": "Captación",
        "caption": """Pedir ayuda profesional no es debilidad: es reconocer que tu salud mental y tu bienestar importan ✨

50 minutos a la semana dedicados 100% a ti, con la psicóloga Valentina Castro Núñez.

👉 Da el primer paso hoy. Agenda en www.centropaz.cl o al WhatsApp +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#Autocuidado", "#PedirAyuda", "#TerapiaAdultosChile"]
    }
}


def get_weekly_calendar() -> List[Dict]:
    """Genera una parrilla semanal de 7 publicaciones alineada al catálogo visual."""
    plan = [
        ("Lunes", "Educación & Validación (Neurodivergencias)", "tdah_adultos"),
        ("Martes", "Derribador de Objeción (Reembolso Isapre)", "reembolso_isapre"),
        ("Miércoles", "Orientación a Padres & Crianza", "crianza_regulacion"),
        ("Jueves", "Agotamiento Invisible (Masking)", "masking"),
        ("Viernes", "Acceso (Terapia Online)", "terapia_online"),
        ("Sábado", "Infancia: cuándo consultar", "evaluacion_infantil"),
        ("Domingo", "Llamado a agendar (Autocuidado)", "autocuidado_adultos"),
    ]
    calendar = []
    for day, theme, key in plan:
        topic = TOPICS[key]
        calendar.append({
            "dia": day,
            "tipo": theme,
            "titulo": topic["title"],
            "gancho": topic["hook"],
            "copy": topic["caption"],
            "hashtags": " ".join(topic["hashtags"]),
            "topic_key": key,
        })
    return calendar
