#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Asistente de Respuesta Rápida para WhatsApp.

Permite generar respuestas clínicas y empáticas instantáneas para cerrar consultas de pacientes.
Uso:
  python3 -m agent.whatsapp_assistant --query "precio"
  python3 -m agent.whatsapp_assistant --query "horarios"
  python3 -m agent.whatsapp_assistant --query "transferencia"
  python3 -m agent.whatsapp_assistant --query "tdah"
  python3 -m agent.whatsapp_assistant --query "tea"
  python3 -m agent.whatsapp_assistant --query "hijo"
  python3 -m agent.whatsapp_assistant --interactive
"""
from __future__ import annotations

import argparse
import sys
from typing import Dict

RESPONSES: Dict[str, str] = {
    "precio": """Hola [Nombre], qué gusto saludarte 🌿

El valor de la sesión particular de 50 minutos con la psicóloga Valentina Castro Núñez es de $45.000 CLP.

Emitimos boletas electrónicas de honorarios profesionales de psicología clínica (con código Superintendencia de Salud), las cuales son 100% reembolsables en todas las Isapres (Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres, Nueva Masvida) y Seguros Complementarios de Salud.

Dependiendo de tu plan, tu Isapre o seguro te reembolsa entre el 50% y el 80% del arancel, por lo que tu copago real puede quedar tan bajo como $12.000 - $18.000 aprox.

¿Te gustaría coordinar tu primera sesión online o presencial en Santiago?""",

    "horarios": """Hola [Nombre] ✨ Para tu primera sesión tengo disponibles estas 2 opciones esta semana:

🌿 Opción 1: Este Jueves a las 17:00 hrs.
🌿 Opción 2: Este Viernes a las 11:00 hrs.

¿Cuál de los dos horarios te acomoda mejor? (Si necesitas otro día u horario de tarde/sábado, avísame y buscamos alternativas).""",

    "fonasa": """Hola [Nombre], gracias por escribirnos 🌿

Nuestras atenciones son de carácter particular (no contamos con bono Fonasa directo por el momento). 

Sin embargo, si cuentas con algún Seguro Complementario de Salud (por trabajo o personal), puedes presentar nuestra boleta electrónica para solicitar tu reembolso.

Cuéntame, ¿el motivo de tu consulta es para ti o para tu hijo/a?""",

    "isapre": """Hola [Nombre] ✨ Sí, emitimos boletas electrónicas de honorarios con código de psicología clínica válidas para todas las Isapres (Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres, Nueva Masvida) y Seguros Complementarios.

El proceso es muy simple: al terminar cada sesión te enviamos tu boleta por correo o WhatsApp, la subes a la app de tu Isapre y te transfieren el reembolso directo a tu cuenta bancaria en pocos días.

¿Te gustaría que revisemos opciones de horarios para esta semana?""",

    "tdah": """Hola [Nombre], te doy una cálida bienvenida 🧠✨

Trabajamos desde un enfoque humanista y neuroafirmativo con personas adultas y jóvenes que sospechan o cuentan con diagnóstico de TDAH.

El objetivo del espacio no es juzgarte ni encajarte en moldes, sino ayudarte a comprender tu funcionamiento cognitivo singular, gestionar la parálisis ejecutiva/procrastinación y construir estrategias respetuosas con tu energía en tu vida cotidiana y laboral.

📍 Modalidad Online (todo Chile) y Presencial (Santiago).
💳 Boletas 100% reembolsables en Isapres y Seguros.

¿Te gustaría coordinar tu primera sesión con Valentina?""",

    "tea": """Hola [Nombre], te doy una cálida bienvenida 🌿✨

En Centro Paz brindamos acompañamiento clínico neuroafirmativo para personas adultas con sospecha o confirmación de Condición del Espectro Autista (TEA).

Trabajamos en la comprensión del perfil sensorial, la prevención del burnout autista, la descompresión del 'masking' y el fortalecimiento de la autoestima sin forzar conductas normalizantes.

¿La atención sería para ti o estás buscando orientación para algún familiar?""",

    "hijo": """Hola [Nombre], qué gusto saludarte 🌱

En Centro Paz acompañamos a niños, niñas y adolescentes con un enfoque lúdico, cálido y neuroafirmativo. Además, trabajamos en estrecha colaboración con ustedes como padres mediante sesiones de orientación continua para entregarles pautas claras de regulación emocional y crianza respetuosa sin gritos ni castigos.

Cuéntame brevemente, ¿qué edad tiene tu hijo/a y qué desafíos principales han estado experimentando en casa o el colegio?""",

    "ansiedad": """Hola [Nombre], gracias por confiar en nosotros 🌊🌿

La sobrecarga mental, el sobrepensamiento constante y la ansiedad física (pecho apretado, dificultad para desconectar) son motivos de consulta muy frecuentes.

En sesión trabajamos con herramientas integrativas y somáticas para calmar la respuesta de alarma de tu sistema nervioso y devolverte la sensación de control y bienestar.

¿Prefieres atención online desde la comodidad de tu hogar o presencial en Santiago?""",

    "modalidad": """Hola [Nombre] 🌿 Atendemos en dos modalidades con la misma rigurosidad clínica:

💻 Modalidad Online: Por videollamada segura, desde cualquier lugar de Chile. Ideal si buscas comodidad y evitar traslados.
🛋️ Modalidad Presencial: En consulta clínica en Santiago en un ambiente cuidado, acogedor y confidencial.

Ambas modalidades reciben la misma boleta electrónica reembolsable en Isapres. ¿Cuál prefieres tú?""",

    "transferencia": """¡Perfecto, [Nombre]! Queda reservado tu horario 🌿

Para confirmar la sesión, puedes realizar la transferencia de los $45.000 CLP a los siguientes datos:

🏦 Banco: [Banco]
📄 Tipo de cuenta: [Cuenta Corriente / Vista]
🔢 Número de cuenta: [XXXXXXXX]
👤 Titular: Valentina Castro Núñez
🆔 RUT: [XX.XXX.XXX-X]
✉️ Correo: contacto.centropaz@gmail.com

Al terminar la sesión te emitiremos tu boleta de honorarios profesional para el reembolso inmediato en tu Isapre o seguro.

Por favor envíame el comprobante por este medio una vez realizada. ¡Nos vemos! ✨""",

    "seguimiento": """Hola [Nombre], ¿cómo estás? 🌿

Te escribo para saber si pudiste revisar la información o si tienes alguna duda pendiente sobre la atención y los reembolsos con Isapres.

Te comparto con mucho cariño nuestra Guía Gratuita en PDF de '7 Claves de Regulación Emocional y Sensorial' por si te es de utilidad.

Quedo muy atenta si deseas que busquemos un horario para esta semana ✨"""
}


def get_response(topic: str) -> str:
    t = topic.lower().strip()
    for key, text in RESPONSES.items():
        if key in t:
            return text

    if any(w in t for w in ["arancel", "valor", "cuanto", "cobran", "costo", "precio"]):
        return RESPONSES["precio"]
    if any(w in t for w in ["horario", "hora", "cuando", "dia", "cita", "disponibilidad"]):
        return RESPONSES["horarios"]
    if any(w in t for w in ["pago", "transferir", "cuenta", "banco", "datos", "transferencia", "rut"]):
        return RESPONSES["transferencia"]
    if any(w in t for w in ["reembolso", "seguro", "isapre", "colmena", "banmedica", "cruzblanca", "consalud"]):
        return RESPONSES["isapre"]
    if any(w in t for w in ["nino", "niño", "hija", "hijo", "padres", "crianza", "colegio"]):
        return RESPONSES["hijo"]
    if any(w in t for w in ["tdah", "concentracion", "procrastinacion", "distraccion"]):
        return RESPONSES["tdah"]
    if any(w in t for w in ["tea", "autismo", "autista", "masking", "sensorial", "burnout"]):
        return RESPONSES["tea"]
    if any(w in t for w in ["ansiedad", "estres", "panico", "angustia", "sobrepensar"]):
        return RESPONSES["ansiedad"]
    if any(w in t for w in ["online", "presencial", "donde", "ubicacion", "direccion"]):
        return RESPONSES["modalidad"]
    if any(w in t for w in ["recordatorio", "guia", "pdf", "despues", "seguimiento"]):
        return RESPONSES["seguimiento"]

    return RESPONSES["precio"]


def interactive_mode() -> None:
    print("\n" + "=" * 65)
    print(" 🌿 CENTRO PAZ — ASISTENTE CLÍNICO DE WHATSAPP (RESPUESTA RÁPIDA)")
    print(" Temas: precio · horarios · isapre · tdah · tea · hijo · ansiedad · transferencia")
    print(" Escribe una consulta o palabra clave ('salir' para terminar)")
    print("=" * 65 + "\n")
    while True:
        try:
            query = input("💬 Consulta del paciente > ").strip()
            if query.lower() in ["salir", "exit", "quit", "q"]:
                break
            if not query:
                continue
            resp = get_response(query)
            print("\n" + "-" * 55)
            print("📋 RESPUESTA LISTA PARA COPIAR Y PEGAR EN WHATSAPP:\n")
            print(resp)
            print("-" * 55 + "\n")
        except (KeyboardInterrupt, EOFError):
            break


def main() -> None:
    parser = argparse.ArgumentParser(description="Asistente de respuestas de WhatsApp para Centro Paz")
    parser.add_argument("--query", "-q", type=str, help="Palabra clave o consulta del paciente")
    parser.add_argument("--interactive", "-i", action="store_true", help="Modo interactivo en consola")
    args = parser.parse_args()

    if args.query:
        print(get_response(args.query))
    else:
        interactive_mode()


if __name__ == "__main__":
    main()

