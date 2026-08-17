#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Asistente de Respuesta Rápida para WhatsApp.

Permite generar respuestas clínicas y empáticas instantáneas para cerrar consultas.
Uso:
  python3 -m agent.whatsapp_assistant --query "precio"
  python3 -m agent.whatsapp_assistant --query "fonasa"
  python3 -m agent.whatsapp_assistant --query "isapre"
  python3 -m agent.whatsapp_assistant --query "hijo"
  python3 -m agent.whatsapp_assistant --query "tdah"
  python3 -m agent.whatsapp_assistant --interactive
"""
import sys
import argparse

RESPONSES = {
    "precio": """Hola [Nombre], qué gusto saludarte 🌿

El valor de la sesión particular de 50 minutos es de $45.000 CLP.

Emitimos boletas de honorarios profesionales de psicología clínica, las cuales son 100% reembolsables en todas las Isapres (Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres) y Seguros Complementarios de Salud. 

Dependiendo de tu plan, tu Isapre o seguro te reembolsa entre el 50% y el 80% del arancel, por lo que tu copago real puede quedar tan bajo como $15.000 - $20.000 aprox.

¿Te gustaría coordinar tu primera sesión online o presencial en Santiago?""",

    "fonasa": """Hola [Nombre], gracias por escribirnos 🌿

Nuestras atenciones son de carácter particular (no contamos con bono Fonasa directo por el momento). 

Sin embargo, si cuentas con algún Seguro Complementario de Salud (por trabajo o personal), puedes presentar nuestra boleta electrónica para solicitar tu reembolso.

Cuéntame, ¿el motivo de tu consulta es para ti o para algún familiar?""",

    "isapre": """Hola [Nombre] ✨ Sí, emitimos boletas electrónicas de honorarios con código de psicología clínica válidas para todas las Isapres (Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres, etc.) y Seguros Complementarios.

El proceso es muy simple: al terminar cada sesión te enviamos tu boleta por correo o WhatsApp, la subes a la app de tu Isapre y te transfieren el reembolso directo a tu cuenta en pocos días.

¿Te gustaría que revisemos disponibilidad de horarios para esta semana?""",

    "tdah": """Hola [Nombre], te doy una cálida bienvenida 🧠✨

Trabajamos desde un enfoque humanista y neuroafirmativo en personas adultas y jóvenes que sospechan o cuentan con diagnóstico de TDAH o TEA.

El objetivo del espacio no es encajarte en moldes, sino ayudarte a comprender tu funcionamiento singular, gestionar la sobrecarga/procrastinación y construir estrategias respetuosas con tu energía en tu vida diaria y laboral.

¿La sesión sería en modalidad online (todo Chile) o presencial en Santiago?""",

    "hijo": """Hola [Nombre], qué gusto saludarte 🌱

En Centro Paz acompañamos a niños y adolescentes con un enfoque lúdico, cálido y seguro, trabajando en conjunto con ustedes como padres mediante sesiones de orientación continua para entregarles pautas claras de regulación y crianza respetuosa en el hogar.

Cuéntame brevemente, ¿qué edad tiene tu hijo/a y qué desafíos principales han estado experimentando?""",

    "seguimiento": """Hola [Nombre], ¿cómo estás? 🌿

Te escribo para saber si pudiste revisar la información o si tienes alguna duda sobre la modalidad de atención y los reembolsos con Isapres.

Te comparto con mucho cariño nuestra Guía Gratuita en PDF de '7 Claves de Regulación Emocional y Sensorial' por si te sirve de apoyo.

Quedo muy atenta si deseas que coordinemos un horario para esta semana ✨"""
}


def get_response(topic: str) -> str:
    topic = topic.lower()
    for key, text in RESPONSES.items():
        if key in topic:
            return text
    # Si no coincide exactamente, busca palabras clave
    if any(w in topic for w in ["arancel", "valor", "cuanto", "cobran", "costo"]):
        return RESPONSES["precio"]
    if any(w in topic for w in ["reembolso", "seguro", "isapre"]):
        return RESPONSES["isapre"]
    if any(w in topic for w in ["nino", "niño", "hija", "hijo", "padres", "crianza"]):
        return RESPONSES["hijo"]
    if any(w in topic for w in ["tea", "tdah", "autismo", "neurodivergencia"]):
        return RESPONSES["tdah"]
    if any(w in topic for w in ["recordatorio", "guia", "pdf", "despues"]):
        return RESPONSES["seguimiento"]
    return RESPONSES["precio"]


def interactive_mode():
    print("\n" + "=" * 60)
    print(" 🌿 CENTRO PAZ — ASISTENTE DE WHATSAPP (RESPUESTA RÁPIDA)")
    print(" Escribe una palabra clave (ej. 'precio', 'tdah', 'hijo', 'isapre', 'fonasa') o 'salir'")
    print("=" * 60 + "\n")
    while True:
        try:
            query = input("💬 Pregunta del paciente > ").strip()
            if query.lower() in ["salir", "exit", "quit"]:
                break
            if not query:
                continue
            resp = get_response(query)
            print("\n" + "-" * 50)
            print("📋 RESPUESTA LISTA PARA COPIAR Y PEGAR:\n")
            print(resp)
            print("-" * 50 + "\n")
        except (KeyboardInterrupt, EOFError):
            break


def main():
    parser = argparse.ArgumentParser(description="Asistente de respuestas de WhatsApp para Centro Paz")
    parser.add_argument("--query", "-q", type=str, help="Palabra clave o consulta del paciente")
    parser.add_argument("--interactive", "-i", action="store_true", help="Modo interactivo en consola")
    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    elif args.query:
        print(get_response(args.query))
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
