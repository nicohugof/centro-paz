#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Generador de Guiones de Video Corto para YouTube Shorts, TikTok y Reels.

Diseñado para producir videos verticales (9:16) de alta retención orgánica que derivan
tráfico hacia WhatsApp (+56 9 6516 3893) y el sitio web (www.centropaz.cl).
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Dict, Any

SHORTS_CATALOG: List[Dict[str, Any]] = [
    {
        "id": "short_01",
        "episode_id": "cpaz_short01_tdah",
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
        "episode_id": "cpaz_short02_isapre",
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
        "episode_id": "cpaz_short03_crianza",
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
    },
    {
        "id": "short_04",
        "episode_id": "cpaz_short04_burnout_autista",
        "platform": ["TikTok", "YouTube Shorts", "Instagram Reels"],
        "target": "Adultos en el espectro autista o con sospecha",
        "title": "Llegar a casa sin poder hablar: Burnout Autista vs Estrés común",
        "duration": "35-40 seg",
        "visual_hook_text": "¿Llegas a casa mudo/a y sin energía? Esto es Burnout Autista 🔋",
        "steps": [
            {
                "time": "0:00 - 0:04",
                "scene": "Expresión de agotamiento profundo / Texto grande",
                "audio": "¿Te pasa que después de un día normal de trabajo llegas a casa sin energía ni para responder un mensaje de texto?",
                "on_screen_text": "Agotamiento que no se quita durmiendo"
            },
            {
                "time": "0:04 - 0:15",
                "scene": "Explicación del colapso sensorial",
                "audio": "A diferencia del estrés común, el burnout autista ocurre por semanas o meses de masking y sobrecarga sensorial acumulada: ruidos, luces y demandas sociales.",
                "on_screen_text": "Masking + Sobrecarga sensorial"
            },
            {
                "time": "0:15 - 0:25",
                "scene": "Señales de alerta clínica",
                "audio": "Tus funciones ejecutivas colapsan, pierdes temporalmente habilidades y necesitas días de aislamiento en oscuridad para regularte.",
                "on_screen_text": "Pérdida temporal de habilidades"
            },
            {
                "time": "0:25 - 0:35",
                "scene": "Acompañamiento neuroafirmativo",
                "audio": "En Centro Paz realizamos evaluación y terapia con enfoque neuroafirmativo en Santiago y Online. Escríbenos directamente a WhatsApp en el enlace del perfil.",
                "on_screen_text": "Evaluación Adultos · Sesiones Online y Ñuñoa"
            }
        ],
        "hashtags": "#BurnoutAutista #AutismoAdultos #TEAAdultos #NeurodivergenciaChile #SaludMentalChile",
        "recommended_sound": "Audio ambiental lofi suave y contemplativo"
    },
    {
        "id": "short_05",
        "episode_id": "cpaz_short05_tdah_mujeres",
        "platform": ["TikTok", "YouTube Shorts", "Instagram Reels"],
        "target": "Mujeres adultas con sospecha de TDAH no diagnosticado",
        "title": "Por qué el TDAH en mujeres se diagnostica recién a los 30 años",
        "duration": "35-40 seg",
        "visual_hook_text": "Por qué te dijeron 'ansiedad' cuando en realidad era TDAH 🧠",
        "steps": [
            {
                "time": "0:00 - 0:04",
                "scene": "Pregunta reflexiva a cámara",
                "audio": "¿Pasaste años diagnosticada con ansiedad o depresión, pero sientes que la raíz de todo siempre fue la desorganización interna?",
                "on_screen_text": "¿Ansiedad o TDAH no diagnosticado?"
            },
            {
                "time": "0:04 - 0:15",
                "scene": "Diferencia de presentación en mujeres",
                "audio": "En mujeres, el TDAH rara vez se muestra como hiperactividad física. Se manifiesta como ensoñación excesiva, perfeccionismo agotador y autoexigencia extrema para compensar.",
                "on_screen_text": "Hiperactividad interna y perfeccionismo"
            },
            {
                "time": "0:15 - 0:25",
                "scene": "Punto de quiebre en la adultez",
                "audio": "El quiebre suele llegar en la universidad, la maternidad o ascensos laborales, cuando el costo de compensar supera tus fuerzas.",
                "on_screen_text": "Cuando compensar ya no alcanza"
            },
            {
                "time": "0:25 - 0:35",
                "scene": "Contacto Centro Paz",
                "audio": "Comprender tu neurotipo cambia tu vida. En Centro Paz te acompañamos. Escríbenos a WhatsApp para consultar disponibilidad de horas.",
                "on_screen_text": "WhatsApp Directo: +56 9 6516 3893"
            }
        ],
        "hashtags": "#TDAHMujeres #TDAHAdultosChile #MujeresConTDAH #SaludMentalChile #PsicologiaChile",
        "recommended_sound": "Melodía de piano cálida y empática"
    },
    {
        "id": "short_06",
        "episode_id": "cpaz_short06_rsd",
        "platform": ["TikTok", "YouTube Shorts", "Instagram Reels"],
        "target": "Adultos con TDAH y sensibilidad emocional",
        "title": "Sensibilidad al Rechazo (RSD): Por qué una crítica duele tanto",
        "duration": "35-40 seg",
        "visual_hook_text": "¿Por qué una crítica te arruina el día entero? Esto se llama RSD 💔",
        "steps": [
            {
                "time": "0:00 - 0:04",
                "scene": "Primer plano reflexivo y empático",
                "audio": "¿Te pasa que un comentario neutro en el trabajo o un mensaje sin responder te genera una angustia física real en el pecho?",
                "on_screen_text": "Dolor físico ante el rechazo percibido"
            },
            {
                "time": "0:04 - 0:15",
                "scene": "Explicación neurobiológica",
                "audio": "No eres débil ni exagerado. En personas con TDAH existe la Disforia Sensible al Rechazo o RSD: una respuesta neurológica donde el cerebro procesa la percepción de rechazo con la misma intensidad que el dolor físico.",
                "on_screen_text": "RSD: Respuesta neurológica real"
            },
            {
                "time": "0:15 - 0:25",
                "scene": "Patrón de conducta compensatoria",
                "audio": "Esto suele llevarte al perfeccionismo extremo o a complacer a todos para evitar ser juzgado, dejando tu energía en cero al final del día.",
                "on_screen_text": "Perfeccionismo y sobre-adaptación"
            },
            {
                "time": "0:25 - 0:35",
                "scene": "Cierre con acompañamiento clínico",
                "audio": "En Centro Paz te acompañamos con terapia neuroafirmativa para desarmar la culpa y regular tu sistema nervioso. Escríbenos por WhatsApp en el enlace de la bio.",
                "on_screen_text": "Terapia Neuroafirmativa · Sesiones Online y Ñuñoa"
            }
        ],
        "hashtags": "#RSDChile #SensibilidadAlRechazo #TDAHEmocional #TDAHAdultos #SaludMentalChile",
        "recommended_sound": "Audio introspectivo suave con cuerdas sutiles"
    },
    {
        "id": "short_07",
        "episode_id": "cpaz_short07_sobrecarga",
        "platform": ["TikTok", "YouTube Shorts", "Instagram Reels"],
        "target": "Adultos con hipersensibilidad sensorial, autistas y TDAH",
        "title": "Hipersensibilidad al Ruido y Sobrecarga Sensorial",
        "duration": "35 seg",
        "visual_hook_text": "¿El ruido de fondo te agota y te irrita? No es mal genio, es sobrecarga 🎧",
        "steps": [
            {
                "time": "0:00 - 0:04",
                "scene": "Gesto de sobrecarga ambiental / Ruido",
                "audio": "¿El ruido de la oficina, los centros comerciales o la masticación de alguien cerca te provocan ganas de escapar o irritabilidad repentina?",
                "on_screen_text": "¿Te satura el ruido ambiental?"
            },
            {
                "time": "0:04 - 0:15",
                "scene": "Explicación sensorial",
                "audio": "Esto no es mal carácter ni falta de paciencia. Tu cerebro no filtra los estímulos auditivos de fondo de forma automática, recibiendo todo el volumen al mismo tiempo.",
                "on_screen_text": "Filtro sensorial reducido"
            },
            {
                "time": "0:15 - 0:25",
                "scene": "Validación fisiológica",
                "audio": "Cuando el umbral se satura, tu sistema entra en respuesta de lucha o huida. Necesitas descompresión sensorial, no culparte por sentirte abrumado.",
                "on_screen_text": "Descompresión sensorial, no culpa"
            },
            {
                "time": "0:25 - 0:35",
                "scene": "Derivación clínica",
                "audio": "Aprende a mapear tu perfil sensorial y proteger tu energía. Sesiones online y en Ñuñoa con reembolso Isapre. Contáctanos al WhatsApp de la bio.",
                "on_screen_text": "Reembolso Isapre · WhatsApp: +56 9 6516 3893"
            }
        ],
        "hashtags": "#SobrecargaSensorial #MisofoniaChile #TEAAdultos #TDAHChile #Hipersensibilidad",
        "recommended_sound": "Transición de ruido caótico a silencio lofi relajante"
    },
    {
        "id": "short_08",
        "episode_id": "cpaz_short08_ansiedad_somatica",
        "platform": ["TikTok", "YouTube Shorts", "Instagram Reels"],
        "target": "Personas con tensión muscular crónica, bruxismo o molestias digestivas por estrés",
        "title": "Ansiedad Somática: Cuando el cuerpo habla lo que la mente calla",
        "duration": "35 seg",
        "visual_hook_text": "¿Opresión en el pecho o colon irritable? Así habla la ansiedad somática 🌿",
        "steps": [
            {
                "time": "0:00 - 0:04",
                "scene": "Gesto de tensión en cuello o pecho",
                "audio": "¿Sientes que mentalmente tienes todo 'bajo control', pero tu cuerpo vive con dolor de cuello, mandíbula apretada o problemas estomacales?",
                "on_screen_text": "Tensión crónica y bruxismo"
            },
            {
                "time": "0:04 - 0:15",
                "scene": "Explicación del sistema nervioso",
                "audio": "La ansiedad somática ocurre cuando sobrepensamos para resolver problemas, pero el sistema nervioso autónomo se queda atrapado en modo supervivencia.",
                "on_screen_text": "Sistema nervioso en modo supervivencia"
            },
            {
                "time": "0:15 - 0:25",
                "scene": "Regulación fisiológica",
                "audio": "Tratarla solo desde la lógica no alcanza: necesitamos técnicas de corregulación fisiológica y respiración diafragmática para activar el nervio vago.",
                "on_screen_text": "Activar el nervio vago y la calma"
            },
            {
                "time": "0:25 - 0:35",
                "scene": "Cierre Centro Paz",
                "audio": "En Centro Paz integramos cuerpo y mente con enfoque humanista y evidencia clínica. Escríbenos a WhatsApp para coordinar tu primera sesión.",
                "on_screen_text": "Sesiones Presenciales Ñuñoa y Online Chile"
            }
        ],
        "hashtags": "#AnsiedadSomatica #SaludMentalChile #NervioVago #PsicologiaClinica #BruxismoChile",
        "recommended_sound": "Música acústica calmante y frecuencias armónicas"
    },
    {
        "id": "short_09",
        "episode_id": "cpaz_short09_terapia_infantil",
        "platform": ["TikTok", "YouTube Shorts", "Instagram Reels"],
        "target": "Padres y madres con dudas sobre el proceso terapéutico infanto-juvenil",
        "title": "Por qué los niños no van al psicólogo a hablar sentados",
        "duration": "35 seg",
        "visual_hook_text": "¿Por qué en psicología infantil jugamos en vez de solo hablar? 🧸🌱",
        "steps": [
            {
                "time": "0:00 - 0:04",
                "scene": "Pregunta frecuente de padres",
                "audio": "Muchos papás se preguntan con honestidad: ¿si mi hijo va a terapia, de verdad le sirve ir a jugar?",
                "on_screen_text": "¿Por qué jugar en terapia infantil?"
            },
            {
                "time": "0:04 - 0:15",
                "scene": "El lenguaje simbólico del niño",
                "audio": "Los niños no tienen el lenguaje abstracto de un adulto para decir 'siento angustia o frustración'. Su lenguaje natural de expresión y procesamiento es el juego simbólico.",
                "on_screen_text": "El juego es el lenguaje del niño"
            },
            {
                "time": "0:15 - 0:25",
                "scene": "Beneficio clínico",
                "audio": "A través del juego proyectan vivencias complejas, ensayan soluciones de conflicto y regulan su mundo emocional en un entorno terapéutico seguro.",
                "on_screen_text": "Resolución de conflictos y regulación"
            },
            {
                "time": "0:25 - 0:35",
                "scene": "Orientación a padres",
                "audio": "Además, orientamos a los padres semana a semana con pautas prácticas para la casa. Consulta por cupos disponibles en el WhatsApp de la bio.",
                "on_screen_text": "Orientación a Padres · WhatsApp: +56 9 6516 3893"
            }
        ],
        "hashtags": "#TerapiaInfantil #PsicologiaInfantil #CrianzaRespetuosa #OrientacionAPadres #SantiagoOriente",
        "recommended_sound": "Melodía dulce y esperanzadora de piano"
    },
    {
        "id": "short_10",
        "episode_id": "cpaz_short10_dopamina",
        "platform": ["TikTok", "YouTube Shorts", "Instagram Reels"],
        "target": "Adultos y jóvenes con TDAH atrapados en el uso compulsivo de pantallas",
        "title": "El ciclo de pantallas y TDAH: Romper el bucle sin culpa",
        "duration": "35 seg",
        "visual_hook_text": "¿Atrapado en el teléfono sin poder soltarlo? Es tu dopamina 📱⚡",
        "steps": [
            {
                "time": "0:00 - 0:04",
                "scene": "Momento de scrolling automático",
                "audio": "¿Te sientas a descansar cinco minutos en el celular y de pronto pasaron dos horas sintiéndote más agotado y culpable que antes?",
                "on_screen_text": "El bucle del scrolling infinito"
            },
            {
                "time": "0:04 - 0:15",
                "scene": "Explicación neuroquímica",
                "audio": "Las pantallas entregan microdosis continuas de dopamina. Para un cerebro neurodivergente, soltar el teléfono se siente literalmente como un abismo de subestimulación física.",
                "on_screen_text": "Dopamina rápida vs Subestimulación"
            },
            {
                "time": "0:15 - 0:25",
                "scene": "Solución clínica sin castigo",
                "audio": "La culpa no ayuda. La clave está en transiciones de baja fricción: sustituir la pantalla por movimiento físico, música estimulante o temporizadores visuales.",
                "on_screen_text": "Estrategias de transición de baja fricción"
            },
            {
                "time": "0:25 - 0:35",
                "scene": "Contacto Centro Paz",
                "audio": "Aprende a gestionar tu energía con acompañamiento profesional. Boletas reembolsables en Isapre. Escríbenos a WhatsApp en el enlace del perfil.",
                "on_screen_text": "Sesiones Online y en Ñuñoa · Reembolso Isapre"
            }
        ],
        "hashtags": "#TDAHAdultos #DopaminaTDAH #Procrastinacion #SaludMentalChile #PsicologiaSantiago",
        "recommended_sound": "Beat lofi dinámico y motivador"
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


def export_markdown() -> Path:
    target = Path(__file__).resolve().parent.parent / "marketing" / "GUIONES_VIDEO_VERTICALES.md"
    lines = [
        "# 🎬 Guiones y Publicación de Video Vertical (Shorts · Reels · TikTok) — Centro Paz\n",
        "> Estructurados como insumos directos para el pipeline automatizado de **YouTube IA** (`/Proyectos/youtube-ia`) y publicación en redes. Formato vertical 9:16 (1080x1920).\n",
        "> **Atención por WhatsApp:** Gestionada **100% de forma exclusiva, personal y directa por Valentina Castro Núñez** (`+56 9 6516 3893`). No se utilizan bots ni respuestas pre-enlatadas.\n",
        "---\n"
    ]
    for s in SHORTS_CATALOG:
        ep_id = s.get("episode_id", f"cpaz_{s['id']}")
        lines.append(f"## [{s['id'].upper()}] {s['title']}\n")
        lines.append(f"- **ID en YouTube IA:** `{ep_id}`")
        lines.append(f"- **Plataformas:** {', '.join(s['platform'])}")
        lines.append(f"- **Audiencia:** {s['target']}")
        lines.append(f"- **Duración estimada:** {s['duration']}")
        lines.append(f"- **Gancho visual (texto grande al inicio):** `{s['visual_hook_text']}`")
        lines.append(f"- **Sonido recomendado:** {s['recommended_sound']}")
        lines.append(f"- **Hashtags:** `{s['hashtags']}`\n")
        lines.append("### Bloques del Video:\n")
        lines.append("| Tiempo | Texto en Pantalla | Audio / Locución Valentina |")
        lines.append("| :--- | :--- | :--- |")
        for step in s["steps"]:
            lines.append(f"| `{step['time']}` | {step['on_screen_text']} | \"{step['audio']}\" |")
        lines.append("\n### Texto para Publicar (Copy & Paste):\n")
        lines.append("**Descripción para Reels / TikTok / YouTube Shorts:**")
        lines.append(f"> {s['visual_hook_text']}\n>\n"
                     f"> ¿Te identificas con estas señales? En Centro Paz te acompañamos con un enfoque neuroafirmativo y basado en evidencia clínica.\n>\n"
                     f"> 📍 Sesiones Online (todo Chile) y Presenciales en Ñuñoa, Santiago.\n"
                     f"> 💳 Boletas electrónicas reembolsables en tu Isapre y Seguro Complementario.\n>\n"
                     f"> {s['hashtags']}\n")
        lines.append("**Comentario Fijado (Pinned Comment):**")
        lines.append(f"> 💬 ¿Quieres conversar o agendar con Valentina? Escríbenos directamente a WhatsApp: https://wa.me/56965163893\n")
        lines.append("\n---\n")

    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"✅ Guiones y copys exportados exitosamente a {target}")
    return target


def render_short(episode_id: str):
    import subprocess
    yt_ia_dir = Path(__file__).resolve().parent.parent.parent / "youtube-ia"
    if not yt_ia_dir.exists():
        print(f"❌ No se encontró el repositorio youtube-ia en {yt_ia_dir}")
        return

    print(f"\n🚀 Renderizando video vertical en YouTube IA: {episode_id}...")
    cmd = [
        "python3", "-m", "agent.pipeline",
        "--episode", episode_id,
        "--lang", "es",
        "--images", "local",
    ]
    res = subprocess.run(cmd, cwd=str(yt_ia_dir))
    if res.returncode == 0:
        out_mp4 = yt_ia_dir / "output" / f"{episode_id}_es_local.mp4"
        print(f"✅ Video generado con éxito: {out_mp4}")
    else:
        print(f"❌ Error al renderizar {episode_id} (exit code {res.returncode})")


def main():
    parser = argparse.ArgumentParser(description="Generador de guiones y puente hacia YouTube IA")
    parser.add_argument("--list", "-l", action="store_true", help="Listar todos los guiones de video")
    parser.add_argument("--export-md", action="store_true", help="Exportar catálogo a marketing/GUIONES_VIDEO_VERTICALES.md")
    parser.add_argument("--render", type=str, default=None, help="Renderizar video en YouTube IA (ej. cpaz_short01_tdah)")
    args = parser.parse_args()

    if args.render:
        render_short(args.render)
    elif args.export_md:
        export_markdown()
    else:
        display_catalog()


if __name__ == "__main__":
    main()

