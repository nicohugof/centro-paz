#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Asistente de Respuesta Rápida y Cierre Humano para Valentina.

Permite a Valentina o al equipo seleccionar el contexto de la consulta recibida
y copiar en 1 segundo la respuesta humana óptima para maximizar la tasa de agendamiento.
"""

RESPONSES = {
    "1": {
        "title": "🧠 TDAH / TEA Adultos (Sospecha tardía, sobrecarga o funciones ejecutivas)",
        "script": (
            "Hola [Nombre] 🌿 Qué gusto saludarte. Soy Valentina Castro, psicóloga clínica de Centro Paz.\n\n"
            "Leí tu mensaje sobre tu consulta por TDAH/Neurodivergencia. Quiero transmitirte mucha tranquilidad: "
            "en sesión trabajamos desde un enfoque neuroafirmativo y compasivo, enfocado en darte estrategias reales "
            "para tu día a día (parálisis ejecutiva, sobrecarga y regulación), sin juicios ni imposición de moldes rígidos.\n\n"
            "💳 Arancel e Isapre: La sesión de 50 minutos tiene un valor de $45.000 CLP y te entrego la boleta electrónica "
            "con código de psicología clínica para que reembolses en tu Isapre (Colmena, CruzBlanca, Banmédica, Consalud, etc.) "
            "y Seguro Complementario. En promedio, el copago real que asumes queda entre $9.000 y $15.000 CLP.\n\n"
            "Atiendo en modalidad Presencial en Ñuñoa (cerca de Metro Chile España / Plaza Ñuñoa) y Online para todo Chile.\n\n"
            "Para coordinar tu primera sesión esta semana, ¿te acomodaría más:\n"
            "1. Jueves a las 17:00 hrs (Presencial u Online)\n"
            "2. Sábado a las 11:00 hrs (Presencial u Online)?\n\n"
            "Quedo muy atenta para reservarte el espacio. Un abrazo cálido ✨"
        )
    },
    "2": {
        "title": "📍 Consulta Presencial en Ñuñoa (Adultos / Ansiedad / Estrés)",
        "script": (
            "Hola [Nombre] 🌿 Muchas gracias por contactarte. Soy Valentina Castro, psicóloga clínica de Centro Paz.\n\n"
            "Qué bueno que diste este paso. Nuestra consulta presencial está ubicada en un espacio muy acogedor y tranquilo "
            "en Ñuñoa, a pasos de la estación Metro Chile España y Plaza Ñuñoa, ideal para desconectar y tener un momento seguro para ti.\n\n"
            "💳 Arancel: $45.000 CLP por sesión de 50 minutos con boleta electrónica para reembolso directo en tu Isapre y seguro.\n\n"
            "Tengo estos dos espacios disponibles para tu ingreso presencial:\n"
            "1. Miércoles a las 18:00 hrs\n"
            "2. Viernes a las 16:30 hrs\n\n"
            "¿Cuál de estas alternativas te queda más cómoda para agendar?"
        )
    },
    "3": {
        "title": "🧸 Infanto-Juvenil & Crianza (Padres consultando por hijos o colegio)",
        "script": (
            "Hola [Nombre] 🌿 Qué gusto saludarte. Soy Valentina Castro, psicóloga clínica de Centro Paz.\n\n"
            "Comprendo perfectamente lo desafiante que puede ser acompañar los momentos de desborde emocional o "
            "las sugerencias de evaluación del colegio. En Centro Paz trabajamos la psicoterapia infantil de forma presencial "
            "a través del juego en nuestra sala clínica de Ñuñoa, combinada siempre con sesiones continuas de orientación "
            "respetuosa para ustedes como madres/padres.\n\n"
            "Si la atención es para un/a joven (12+ años), también disponemos de modalidad Online para todo Chile.\n\n"
            "💳 La sesión es de $45.000 CLP con boleta reembolsable en Isapres y elaboramos los informes requeridos para el colegio/PIE.\n\n"
            "¿Te gustaría que coordinemos una primera sesión de evaluación e ingreso esta semana? Cuéntame qué días u horarios les acomodan mejor en familia."
        )
    },
    "4": {
        "title": "💳 Consulta Directa por Valores y Reembolso Isapre / Seguros",
        "script": (
            "Hola [Nombre] 🌿 Te saluda Valentina Castro, psicóloga clínica de Centro Paz.\n\n"
            "Te detallo con total transparencia el valor de atención:\n"
            "• Arancel por sesión individual (50 min): $45.000 CLP.\n"
            "• Boleta de Honorarios: Emitimos boleta electrónica oficial del SII con código de psicología clínica inmediatamente al terminar la sesión.\n"
            "• Reembolso Isapre: Válida para todas las Isapres (Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres) que reembolsan entre el 60% y 80%.\n"
            "• Copago estimado: Terminas pagando aproximadamente entre $9.000 y $15.000 CLP de tu bolsillo.\n"
            "• Seguro Complementario: Si tu empresa tiene seguro colectivo (Bice, MetLife, Consorcio), puedes ingresar la liquidación para un segundo reembolso.\n\n"
            "¿Te gustaría revisar disponibilidad para agendar tu primera sesión? Cuéntame si buscas modalidad Online o Presencial en Ñuñoa."
        )
    }
}

def interactive_responder():
    print("\n" + "=" * 75)
    print(" 🌿 ASISTENTE DE RESPUESTA RÁPIDA DE WHATSAPP (CIERRE HUMANO VALENTINA)")
    print("=" * 75)
    print("Selecciona el tipo de consulta recibida en WhatsApp:\n")
    for k, v in RESPONSES.items():
        print(f" {k}. {v['title']}")
    print(" 0. Volver")
    print("=" * 75)

    choice = input("\n👉 Selecciona una opción (1-4): ").strip()
    if choice in RESPONSES:
        item = RESPONSES[choice]
        name = input("\n👤 Nombre del paciente (o presiona Enter para '[Nombre]'): ").strip()
        script = item["script"]
        if name:
            script = script.replace("[Nombre]", name)
        
        print("\n" + "—" * 75)
        print("📋 MENSAJE LISTO PARA COPIAR Y ENVIAR POR WHATSAPP:")
        print("—" * 75)
        print(script)
        print("—" * 75)
        print("💡 Consejo Clínico: Responder en menos de 15 minutos multiplica por 5 la tasa de agendamiento.\n")
        input("Presiona Enter para continuar...")
    elif choice == "0":
        return

if __name__ == "__main__":
    interactive_responder()
