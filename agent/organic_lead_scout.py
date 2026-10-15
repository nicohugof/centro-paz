#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Scout de Oportunidades y Generador de Respuestas Orgánicas.

Genera respuestas de alto valor, psicoeducativas y con profunda calidez humana para
interactuar de forma orgánica en foros y comunidades públicas de Chile:
- Reddit: r/chile, r/Santiago, r/MentalHealthChile
- Facebook Groups: Vecinos Ñuñoa, Plaza Ñuñoa, Datos Providencia, Comunidad Las Condes/La Reina
- Redes sociales: X (Twitter), hilos de salud mental

Enfocado en las 4 especialidades clínicas oficiales de la Psicóloga Valentina Castro Núñez:
1. Ansiedad, taquicardias y crisis de angustia
2. Depresión, desánimo y duelo
3. Trastorno Límite de la Personalidad (TLP) y regulación emocional
4. Psicodiagnósticos con informe clínico formal para psiquiatras
"""
from __future__ import annotations

import argparse
import sys
from typing import Dict, Any, List, Optional


ORGANIC_TEMPLATES: Dict[str, Dict[str, Any]] = {
    "ansiedad_crisis_angustia": {
        "titulo": "Ansiedad, Taquicardias y Crisis de Angustia / Pánico",
        "categoria": "ansiedad",
        "comunidades_recomendadas": [
            "Reddit r/chile (posts de 'me dio una crisis de pánico', 'siento taquicardias')",
            "Reddit r/Santiago (preguntas sobre salud mental y urgencias de angustia)",
            "Grupos de Facebook Ñuñoa / Providencia (solicitud de psicóloga para crisis de pánico)"
        ],
        "keywords": [
            "ansiedad", "crisis", "panico", "pánico", "taquicardia", "angustia",
            "ahogo", "pecho", "sobrepensar", "desesperacion", "nervios", "palpitaciones"
        ],
        "consejo_publicacion": (
            "Primero valida lo que la persona siente. Las taquicardias asustan mucho "
            "porque simulan un infarto; el valor está en explicar la alarma biológica simpática "
            "antes de ofrecer cualquier contacto."
        ),
        "texto": """Hola. Lamento mucho que estés pasando por esto; las crisis de angustia y las taquicardias son experiencias profundamente agotadoras y dan mucho miedo, sobre todo cuando sientes opresión en el pecho o la sensación de perder el control.

Si ya descartaste con un médico general o cardiólogo algún tema físico, ten la tranquilidad de que lo que sientes es tu sistema nervioso simpático activando una respuesta de "alarma biológica" de sobrevivencia (hiperventilación y adrenalina), no un peligro real para tu vida. Algo que ayuda en el momento exacto de la crisis es el suspiro fisiológico: dos inhalaciones cortas por la nariz y una exhalación muy larga y lenta por la boca; esto le envía una señal fisiológica directa al nervio vago para desacelerar las pulsaciones.

Para trabajarlo de raíz con herramientas cognitivas y somáticas, te recomiendo con total confianza a la psicóloga clínica Valentina Castro Núñez, directora de Centro Paz en Ñuñoa (atiende presencial a pasos de Metro Chile España / Plaza Ñuñoa y online para todo Chile). Ella se especializa justamente en desregulación del sistema nervioso, ataques de pánico y ansiedad generalizada con un trato muy cálido, libre de juicios y sin patologizar.

Además, emite boleta electrónica con código de psicología clínica reembolsable en todas las Isapres (Colmena, Banmédica, CruzBlanca, Consalud, etc.) y seguros complementarios, por lo que el copago final queda bastante accesible.

Puedes mirar su perfil y enfoque en www.centropaz.cl o escribirle directo a su WhatsApp de coordinación (+56 9 6516 3893). Mucho ánimo, la ansiedad se puede comprender y desarmar paso a paso."""
    },

    "depresion_desanimo_duelo": {
        "titulo": "Depresión, Desánimo Profundo y Procesos de Duelo",
        "categoria": "depresion",
        "comunidades_recomendadas": [
            "Reddit r/chile (hilos de desahogo, 'no tengo ganas de nada', 'perdí a alguien')",
            "Reddit r/Santiago (búsqueda de terapeutas humanos y pacientes)",
            "Grupos de Facebook comunales (hilos de apoyo y recomendaciones terapéuticas)"
        ],
        "keywords": [
            "depresion", "depresión", "desanimo", "desánimo", "duelo", "tristeza",
            "vacio", "vacío", "anhedonia", "bajon", "bajón", "sin energia", "llanto", "perdida", "pérdida"
        ],
        "consejo_publicacion": (
            "Nunca digas 'todo va a estar bien' ni des consejos simplistas de productividad. "
            "Valida la fatiga emocional y el ritmo personal del doliente."
        ),
        "texto": """Hola. Te mando un abrazo grande. La sensación de vacío, el desánimo persistente y el duelo duelen de una forma silenciosa que quienes no lo han vivido rara vez entienden. Es importante que sepas que esto no es falta de voluntad, debilidad ni flojera; muchas veces la mente y el cuerpo entran en un estado de repliegue y fatiga profunda cuando han sostenido demasiado dolor o sobrecarga durante mucho tiempo.

En estos momentos lo último que sirve es la presión de 'ponerse positivo' o forzarse a funcionar al 100%. Lo que realmente ayuda es un espacio terapéutico compasivo donde puedas soltar la carga sin tener que fingir que estás bien, procesando el duelo o la tristeza a tu propio ritmo.

Te sugiero consultar con la psicóloga Valentina Castro Núñez en Centro Paz. Valentina trabaja desde un enfoque humanista e integrativo muy cercano y respetuoso, acompañando cuadros depresivos, pérdidas afectivas y momentos de crisis vital con mucha contención y sin apuros.

Tiene consulta presencial en Ñuñoa (cerca de Plaza Ñuñoa y Metro Chile España) y también modalidad online para todo el país. Emite boletas reembolsables en Isapre (Colmena, CruzBlanca, Banmédica, Consalud, etc.) y seguro complementario para aliviar el costo.

Puedes conocer su trabajo en www.centropaz.cl o escribirle directamente por WhatsApp al +56 9 6516 3893 para coordinar o resolver cualquier duda. No tienes que cargar con todo esto a solas."""
    },

    "tlp_regulacion_emocional": {
        "titulo": "Trastorno Límite de la Personalidad (TLP / Borderline) y Regulación Emocional",
        "categoria": "tlp",
        "comunidades_recomendadas": [
            "Reddit r/chile (consultas por psicólogos especialistas en TLP o desregulación severa)",
            "Comunidades de salud mental en Chile y foros de neurodivergencia",
            "Grupos comunitarios de Facebook en Santiago"
        ],
        "keywords": [
            "tlp", "borderline", "personalidad", "regulacion", "regulación", "desborde",
            "inestabilidad", "emocional", "vacio", "abandono", "sensibilidad", "hipersensible", "bipolar"
        ],
        "consejo_publicacion": (
            "Desestigmatiza el TLP de entrada. Muchas personas con TLP han sido maltratadas o "
            "rechazadas en consultas de salud mental. Resalta el encuadre seguro y la escucha libre de juicios."
        ),
        "texto": """Hola. Encontrar un buen profesional para Trastorno Límite de la Personalidad (TLP / Borderline) o desregulación emocional intensa puede ser muy frustrante en Chile, porque lamentablemente todavía existe mucho prejuicio y profesionales que patologizan el dolor en vez de acompañar.

Vivir con TLP significa procesar los estímulos emocionales a un volumen mucho más alto que el promedio: la hipersensibilidad ante la desconexión o el temor al rechazo no son 'mañas' ni dramatismo, sino heridas y patrones de apego que necesitan herramientas concretas de autorregulación somática, tolerancia al malestar y estabilización vincular.

Te recomiendo con mucha certeza a la psicóloga clínica Valentina Castro Núñez, directora de Centro Paz. Valentina trabaja con enfoque integrativo, neuroafirmativo y libre de estigmas, especializada en desregulación emocional severa, acompañamiento en TLP y fortalecimiento de la identidad personal. Su encuadre se caracteriza por una calidez real donde no te vas a sentir juzgado/a ni encasillado/a en una etiqueta.

Atiende de manera presencial en Ñuñoa (a pasos de Metro Chile España / Plaza Ñuñoa) y también vía online para cualquier región. Las sesiones cuentan con boleta de honorarios para reembolso en Isapres (Colmena, Banmédica, CruzBlanca, Consalud, etc.) y seguros complementarios de salud.

Puedes revisar la propuesta clínica en www.centropaz.cl o hablar directamente con ella por WhatsApp al +56 9 6516 3893. Mereces un espacio seguro donde te sientas validado/a."""
    },

    "psicodiagnostico_informe_psiquiatria": {
        "titulo": "Psicodiagnósticos Clínicos e Informes Formales para Psiquiatras",
        "categoria": "psicodiagnostico",
        "comunidades_recomendadas": [
            "Reddit r/chile (gente buscando 'evaluación psicodiagnóstica para psiquiatra')",
            "Reddit r/Santiago (solicitudes de informes psicológicos clínicos formales)",
            "Grupos de Facebook comunales y grupos universitarios de Santiago"
        ],
        "keywords": [
            "psicodiagnostico", "psicodiagnóstico", "informe", "psiquiatra", "evaluacion",
            "evaluación", "bateria", "batería", "test", "peritaje", "interconsulta", "licencia", "diagnostico", "diagnóstico"
        ],
        "consejo_publicacion": (
            "Enfatiza el rigor técnico del informe, la aplicación de baterías formales "
            "y la validez clínica para el psiquiatra tratante o interconsulta médica."
        ),
        "texto": """Hola! Si tu psiquiatra o médico tratante te solicitó una evaluación psicodiagnóstica con informe formal, es fundamental que el proceso lo realice un psicólogo clínico acreditado y mediante baterías estructuradas de evaluación, para que el documento tenga plena validez técnica y diagnóstica en tu interconsulta.

Un buen proceso psicodiagnóstico toma generalmente entre 3 y 4 sesiones: incluye entrevistas clínicas en profundidad, aplicación de pruebas psicométricas/proyectivas validadas según tu motivo de consulta (rasgos de personalidad, funcionamiento afectivo, sintomatología del ánimo o desregulación) y una sesión final de devolución con entrega del informe clínico detallado por escrito.

En Centro Paz (Ñuñoa / Online), la psicóloga clínica Valentina Castro Núñez realiza este servicio con altos estándares técnicos para derivaciones e interconsultas psiquiátricas. Su informe entrega un perfil exhaustivo de personalidad, hipótesis clínica estructurada y sugerencias específicas de tratamiento interdisciplinario que los psiquiatras valoran mucho por su claridad.

La consulta presencial queda en el sector de Plaza Ñuñoa / Metro Chile España (Línea 3) y también se realiza evaluación online cuando la batería lo permite. Las sesiones se emiten con boleta de psicología clínica reembolsable en Isapres y seguros complementarios de salud.

Puedes consultar por disponibilidad y plazos de entrega del informe en www.centropaz.cl o directo por WhatsApp al +56 9 6516 3893."""
    },

    "reembolso_isapre_fonasa": {
        "titulo": "Cómo Reembolsar Sesiones de Psicología en Isapre y Seguros Complementarios",
        "categoria": "reembolso",
        "comunidades_recomendadas": [
            "Reddit r/chile (preguntas tipo '¿cómo se reembolsa el psicólogo en Colmena/CruzBlanca?')",
            "Reddit r/Santiago (dudas sobre copagos y coberturas de salud mental)",
            "Comunidades de vecinos y foros de finanzas personales en Chile"
        ],
        "keywords": [
            "isapre", "reembolso", "fonasa", "seguro", "complementario", "precio",
            "arancel", "boleta", "copago", "colmena", "cruzblanca", "banmedica", "consalud"
        ],
        "consejo_publicacion": (
            "Aclara los 3 pasos exactos con lenguaje administrativo claro chileno. "
            "El valor está en explicar cómo llegar a un copago real de $9.000 - $18.000."
        ),
        "texto": """Hola! El trámite para reembolsar psicoterapia en Isapres y seguros complementarios en Chile es súper directo si tu profesional cumple con los requisitos del sistema de salud:

1. El profesional debe ser psicólogo/a clínico/a titulado/a y estar inscrito en el Registro Nacional de Prestadores Individuales de la Superintendencia de Salud (SIS).
2. Tras la sesión, te emite una Boleta de Honorarios Electrónica del SII con el código de prestación de psicología clínica.
3. Subes el archivo PDF de la boleta a la app o sucursal virtual de tu Isapre (Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres, etc.). Te reembolsan entre el 50% y el 80% del arancel según tu plan, depositado directo a tu cuenta corriente/RUT en 48 a 72 horas.
4. Si tienes Seguro Complementario (por trabajo o particular), subes la liquidación de la Isapre y te cubren un porcentaje adicional, dejando un copago final muy bajo (habitualmente entre $9.000 y $18.000 CLP).

En Centro Paz (consulta presencial en Ñuñoa y online para todo Chile), la psicóloga clínica Valentina Castro Núñez entrega boletas autorizadas aptas para todos estos reembolsos. En su sitio web www.centropaz.cl tienen orientación para consultar tu plan, o puedes consultar directo a su WhatsApp +56 9 6516 3893."""
    },

    "psicologo_nunoa_providencia": {
        "titulo": "Recomendación Geográfica: Consulta Presencial Ñuñoa / Providencia / Metro Chile España",
        "categoria": "geografico",
        "comunidades_recomendadas": [
            "Grupos de Facebook: Datos Ñuñoa, Vecinos Plaza Ñuñoa, Comunidad Providencia",
            "Reddit r/Santiago (búsquedas tipo 'busco psicólogo presencial en Santiago Oriente')",
            "Recomendaciones en foros locales"
        ],
        "keywords": [
            "ñuñoa", "nunoa", "providencia", "presencial", "chile españa", "santiago",
            "plaza ñuñoa", "metro", "la reina", "macul", "consulta"
        ],
        "consejo_publicacion": (
            "Enfocado en cercanía física, conectividad (Metro L3 Chile España) y ambiente acogedor."
        ),
        "texto": """Hola vecino/a! Si buscas atención psicológica presencial en el sector oriente, te recomiendo a la psicóloga clínica Valentina Castro Núñez en Centro Paz.

Su consulta está ubicada en Ñuñoa, en una zona muy tranquila y conectada a pasos de la estación de Metro Chile España (Línea 3) y Plaza Ñuñoa. Es un espacio privado, cálido y pensado para que puedas conversar con absoluta tranquilidad. 

Valentina atiende adultos y se especializa en ansiedad y ataques de pánico, cuadros depresivos, regulación emocional (TLP) y evaluaciones psicodiagnósticas para psiquiatras. Emite boletas electrónicas de honorarios con código clínico reembolsables en todas las Isapres y seguros complementarios de salud.

Puedes ver más detalles del espacio y su metodología en www.centropaz.cl o escribir directo al WhatsApp de coordinación de horas (+56 9 6516 3893)."""
    }
}


def get_organic_reply(topic: str) -> Dict[str, Any]:
    """
    Busca la plantilla más pertinente en base a una consulta o palabra clave.
    """
    t = topic.strip().lower()
    
    # 1. Búsqueda exacta por clave
    if t in ORGANIC_TEMPLATES:
        return ORGANIC_TEMPLATES[t]
        
    # 2. Búsqueda parcial por clave
    for k, v in ORGANIC_TEMPLATES.items():
        if k in t or t in k:
            return v
            
    # 3. Búsqueda por keywords específicas de las 4 especialidades
    # Ansiedad y pánico
    if any(w in t for w in ["ansiedad", "panico", "pánico", "taquicardia", "angustia", "ahogo", "pecho", "palpitacion", "palpitación"]):
        return ORGANIC_TEMPLATES["ansiedad_crisis_angustia"]
        
    # Depresión y duelo
    if any(w in t for w in ["depresion", "depresión", "desanimo", "desánimo", "duelo", "tristeza", "vacio", "vacío", "anhedonia", "bajon", "bajón"]):
        return ORGANIC_TEMPLATES["depresion_desanimo_duelo"]
        
    # TLP y desregulación emocional
    if any(w in t for w in ["tlp", "borderline", "personalidad", "regulacion", "regulación", "desborde", "inestabilidad", "emocional"]):
        return ORGANIC_TEMPLATES["tlp_regulacion_emocional"]
        
    # Psicodiagnóstico e informes
    if any(w in t for w in ["psicodiagnostico", "psicodiagnóstico", "informe", "psiquiatra", "evaluacion", "evaluación", "bateria", "batería", "test"]):
        return ORGANIC_TEMPLATES["psicodiagnostico_informe_psiquiatria"]
        
    # Reembolsos
    if any(w in t for w in ["isapre", "reembolso", "fonasa", "seguro", "precio", "arancel", "boleta", "copago"]):
        return ORGANIC_TEMPLATES["reembolso_isapre_fonasa"]
        
    # Zona geográfica
    if any(w in t for w in ["ñuñoa", "nunoa", "providencia", "presencial", "chile españa", "santiago", "oriente"]):
        return ORGANIC_TEMPLATES["psicologo_nunoa_providencia"]
        
    # Fallback por defecto a ansiedad (motivo de consulta #1 en Chile)
    return ORGANIC_TEMPLATES["ansiedad_crisis_angustia"]


def print_template_block(key: str, data: Dict[str, Any]) -> None:
    print("\n" + "=" * 76)
    print(f"📌 CLAVE: {key}")
    print(f"🎯 ESPECIALIDAD / TEMA: {data['titulo']}")
    print(f"🏷️  CATEGORÍA: {data['categoria'].upper()}")
    print("-" * 76)
    print("📍 DÓNDE RESPONDER (COMUNIDADES OBJETIVO):")
    for com in data["comunidades_recomendadas"]:
        print(f"   • {com}")
    print("\n💡 TIP CLÍNICO Y ESTRATÉGICO:")
    print(f"   {data['consejo_publicacion']}")
    print("\n📋 TEXTO LISTO PARA COPIAR Y PEGAR:")
    print("-" * 76)
    print(data["texto"])
    print("=" * 76 + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Centro Paz (CPAZ) — Scout de Oportunidades y Generador de Respuestas Orgánicas"
    )
    parser.add_argument(
        "--query", "-q",
        type=str,
        help="Tema o palabra clave (ej: ansiedad, panico, depresion, duelo, tlp, informe, isapre, nunoa)"
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Muestra todas las plantillas completas listas para copiar y pegar"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="Lista los temas y especialidades disponibles en el catálogo"
    )
    args = parser.parse_args()

    if args.list:
        print("\n" + "=" * 70)
        print("  CATÁLOGO DE PLANTILLAS ORGÁNICAS — CENTRO PAZ (VALENTINA CASTRO)")
        print("=" * 70)
        for k, v in ORGANIC_TEMPLATES.items():
            print(f"• {k:<34} -> {v['titulo']}")
        print("=" * 70)
        print("Uso: python3 agent/organic_lead_scout.py -q <tema> o --all\n")
        return

    if args.query:
        match = get_organic_reply(args.query)
        # Find key
        matched_key = next((k for k, v in ORGANIC_TEMPLATES.items() if v == match), "resultado")
        print_template_block(matched_key, match)
        return

    # Si no se pasó argumento o se solicitó --all, mostramos todas
    print("\n" + "#" * 76)
    print("  CENTRO PAZ (CPAZ) — SCOUT DE CAPTACIÓN ORGÁNICA A $0 CLP")
    print("  Especialidades oficiales de la Psicóloga Valentina Castro Núñez")
    print("#" * 76)
    for k, v in ORGANIC_TEMPLATES.items():
        print_template_block(k, v)


if __name__ == "__main__":
    main()
