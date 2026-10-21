#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Asistente de Respuesta Rápida y Cierre Humano para Valentina.

Permite a Valentina o al equipo seleccionar el contexto de la consulta recibida
y copiar en 1 segundo la respuesta humana óptima para maximizar la tasa de agendamiento.
"""

RESPONSES = {
    "1": {
        "title": "🌊 Ansiedad y Crisis de Angustia (Ataques de pánico, taquicardia, opresión, sobrepensamiento)",
        "script": (
            "Hola [Nombre] 🌿 Qué gusto saludarte. Soy Valentina Castro, psicóloga clínica de Centro Paz.\n\n"
            "Leí tu mensaje sobre las crisis de angustia y taquicardia. Quiero transmitirte mucha tranquilidad: "
            "la ansiedad es una respuesta adaptativa del sistema nervioso simpático (alarma biológica) que podemos "
            "aprender a regular con herramientas somáticas y cognitivas respetuosas, sin juzgar lo que sientes.\n\n"
            "💳 Arancel e Isapre: La sesión de 50 minutos tiene un valor de $45.000 CLP y te entrego de inmediato la boleta "
            "electrónica con código de psicología clínica para que reembolses en tu Isapre (Colmena, CruzBlanca, Banmédica, "
            "Consalud, Vida Tres) y Seguro Complementario. En promedio, el copago real queda entre $9.000 y $18.000 CLP.\n\n"
            "Atiendo en modalidad Presencial en Ñuñoa (cerca de Metro Chile España / Plaza Ñuñoa) y Online para todo Chile.\n\n"
            "Para coordinar tu ingreso esta semana, ¿te acomodaría más:\n"
            "1. Jueves a las 17:00 hrs (Presencial u Online)\n"
            "2. Sábado a las 11:00 hrs (Presencial u Online)?\n\n"
            "Quedo muy atenta para reservarte el espacio. Un abrazo cálido ✨"
        )
    },
    "2": {
        "title": "🌱 Depresión y Trastornos del Ánimo (Desánimo profundo, falta de motivación, anhedonia, duelos)",
        "script": (
            "Hola [Nombre] 🌿 Te saluda Valentina Castro, psicóloga clínica de Centro Paz.\n\n"
            "Comprendo profundamente lo agotador y solitario que puede sentirse sostener el desánimo, el cansancio y la falta de energía. "
            "En Centro Paz construimos un espacio seguro, gradual y compasivo, sin presiones ni exigencias de 'estar bien rápido', enfocado en validar "
            "tu momento y reconectar paso a paso con tu vitalidad.\n\n"
            "💳 Arancel e Isapre: $45.000 CLP por sesión con boleta electrónica para reembolso directo en tu Isapre y seguro complementario "
            "(copago real promedio: $9.000 a $18.000 CLP).\n\n"
            "Disponemos de atención Presencial en Ñuñoa y Online vía videollamada para todo Chile.\n\n"
            "¿Te gustaría que agendemos tu sesión inicial? Tengo disponibles estos horarios esta semana:\n"
            "1. Miércoles a las 18:00 hrs\n"
            "2. Viernes a las 16:30 hrs\n\n"
            "Cuéntame cuál te sienta mejor para coordinar."
        )
    },
    "3": {
        "title": "🧩 Trastornos de la Personalidad / TLP (Inestabilidad emocional, desregulación afectiva, vínculos)",
        "script": (
            "Hola [Nombre] 🌿 Qué gusto saludarte, soy Valentina Castro, psicóloga clínica de Centro Paz.\n\n"
            "Entiendo perfectamente lo abrumador que puede ser experimentar emociones de tan alta intensidad, el temor al abandono o al rechazo "
            "y las oscilaciones en los vínculos. Trabajamos desde un encuadre terapéutico integrativo y profundamente empático, libre de etiquetas "
            "estigmatizantes, para ayudarte a desarrollar tolerancia al malestar, autorregulación emocional y estabilidad relacional.\n\n"
            "💳 Arancel: $45.000 CLP (50 min) con boleta reembolsable en todas las Isapres (copago estimado: $9.000 a $18.000 CLP).\n\n"
            "Atiendo de forma Presencial en Ñuñoa (Plaza Ñuñoa) y Online para todo el país.\n\n"
            "Para tu primera sesión, ¿qué opción te acomoda mejor:\n"
            "1. Jueves a las 18:00 hrs\n"
            "2. Sábado a las 10:30 hrs?"
        )
    },
    "4": {
        "title": "📋 Evaluaciones Psicodiagnósticas e Informes Formales (Derivación médica / psiquiatría)",
        "script": (
            "Hola [Nombre] 🌿 Te saluda Valentina Castro, psicóloga clínica de Centro Paz (acreditada por la Superintendencia de Salud - SIS).\n\n"
            "Respecto a tu consulta por la evaluación psicodiagnóstica: realizamos un proceso técnico y formal de 3 a 4 sesiones clínicas "
            "donde aplicamos baterías estandarizadas (psicométricas y proyectivas según interconsulta), con sesión de devolución y entrega de "
            "informe formal exhaustivo firmado para tu médico psiquiatra o institución requirente.\n\n"
            "💳 Arancel: $45.000 CLP por sesión de evaluación con boleta reembolsable en Isapre y seguros complementarios.\n\n"
            "Modalidad: Presencial en Ñuñoa u Online (según la naturaleza de las baterías solicitadas).\n\n"
            "¿Te parece que coordinemos la primera sesión de entrevista clínica e inicio de batería esta semana?"
        )
    },
    "5": {
        "title": "💳 Consulta Directa por Valores, Reembolso Isapre y Proximidad Ñuñoa",
        "script": (
            "Hola [Nombre] 🌿 Te saluda Valentina Castro, psicóloga clínica de Centro Paz.\n\n"
            "Te detallo con total transparencia los valores y condiciones de atención:\n"
            "• Arancel por sesión individual (50 min): $45.000 CLP.\n"
            "• Boleta de Honorarios: Emitimos boleta electrónica oficial del SII con código de psicología clínica inmediatamente al terminar cada sesión.\n"
            "• Reembolso Isapre: Válida para todas las Isapres (Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres) que reembolsan habitualmente entre el 60% y 80%.\n"
            "• Copago estimado: Terminas pagando aproximadamente entre $9.000 y $18.000 CLP de tu bolsillo (promedio ~$12.000 CLP).\n"
            "• Seguro Complementario: Si cuentas con póliza colectiva o individual, puedes ingresar la liquidación para un segundo reembolso.\n"
            "• Ubicación: Consulta presencial en Ñuñoa (a pasos de Metro Chile España / Plaza Ñuñoa) y Online para todo Chile.\n\n"
            "¿Te gustaría que revisemos opciones de horario para agendar tu primera sesión esta semana?"
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

    choice = input("\n👉 Selecciona una opción (1-5): ").strip()
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
