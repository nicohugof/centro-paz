#!/usr/bin/env python3
"""
Generador de los posts 15 al 28 para Centro Paz.
Crea los archivos HTML en assets/instagram/ con diseño profesional para Instagram (1080x1350).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "assets" / "instagram"

NEW_POSTS_DATA = [
    {
        "id": 15,
        "key": "tdah_mujeres",
        "category": "Neurodivergencias",
        "kicker": "Diagnóstico Tardío",
        "title_html": "¿Por qué el <span>TDAH en mujeres</span> se descubre 10 años más tarde?",
        "points": [
            ("✦", "<strong>Manifestación internalizada:</strong> Menos hiperactividad física, más sobrepensamiento, desorganización y ansiedad silenciosa."),
            ("✦", "<strong>Hiper-compensación (Masking):</strong> Ser 'la niña perfecta y autoexigente' a costa de un desgaste emocional inmenso."),
            ("✦", "<strong>Diagnósticos previos erróneos:</strong> Años tratada por depresión o ansiedad sin abordar la raíz neurobiológica."),
            ("✦", "<strong>Terapia neuroafirmativa:</strong> Comprenderte sin culpa y construir estrategias adaptadas a tu energía.")
        ],
        "footer_title": "Atención Neuroafirmativa Adultos",
        "footer_sub": "Sesiones online y presenciales en Ñuñoa · Reembolso Isapre"
    },
    {
        "id": 16,
        "key": "sobrecarga_sensorial_ruido",
        "category": "Regulación Sensorial",
        "kicker": "Sistema Nervioso",
        "title_html": "Hipersensibilidad al ruido: <span>no es mal genio</span>, es tu sistema nervioso",
        "points": [
            ("✦", "<strong>Sobrecarga auditiva:</strong> Sonidos de masticación, teclados, conversaciones cruzadas que provocan dolor o ira súbita."),
            ("✦", "<strong>Amígdala en alerta:</strong> Tu cerebro procesa el estímulo ambiental como una amenaza física real."),
            ("✦", "<strong>El mito de 'acostumbrarse':</strong> Forzarte a tolerarlo solo produce agotamiento y desregulación."),
            ("✦", "<strong>Acomodaciones sensoriales:</strong> Aprender a proteger tus sentidos sin culpa en el trabajo y el hogar.")
        ],
        "footer_title": "Terapia y Regulación Sensorial",
        "footer_sub": "Valentina Castro Núñez · Psicóloga Clínica"
    },
    {
        "id": 17,
        "key": "reembolso_seguros_cobertura",
        "category": "Cobertura & Isapres",
        "kicker": "Finanzas & Salud",
        "title_html": "Cómo combinar <span>Isapre + Seguro</span> para pagar el mínimo en terapia",
        "points": [
            ("✦", "<strong>Paso 1:</strong> Asistes a tu sesión en Centro Paz y recibes tu boleta electrónica oficial."),
            ("✦", "<strong>Paso 2:</strong> Subes la boleta a tu Isapre (Colmena, Banmédica, CruzBlanca) ➡️ Te reembolsan 50% a 70%."),
            ("✦", "<strong>Paso 3:</strong> Subes el comprobante de liquidación a tu Seguro Complementario ➡️ Te cubren el restante."),
            ("✦", "<strong>Resultado real:</strong> Tu copago final puede quedar tan bajo como $8.000 a $12.000 por sesión.")
        ],
        "footer_title": "Simulador de Reembolso Web",
        "footer_sub": "Boletas 100% electrónicas · Código Superintendencia de Salud"
    },
    {
        "id": 18,
        "key": "hiperfoco_burnout",
        "category": "TDAH en Adultos",
        "kicker": "Gestión de Energía",
        "title_html": "El ciclo del <span>Hiperfoco</span>: De la genialidad al colapso en 48 hrs",
        "points": [
            ("✦", "<strong>Fase 1 (Obsesión productiva):</strong> 10 horas seguidas trabajando sin comer, sin tomar agua ni ir al baño."),
            ("✦", "<strong>Fase 2 (Caída de dopamina):</strong> La novedad se apaga y la tarea se vuelve insoportablemente tediosa."),
            ("✦", "<strong>Fase 3 (Culpa y agotamiento):</strong> Cansancio extremo y sensación de 'no ser constante'."),
            ("✦", "<strong>Estrategia clínica:</strong> Aprender a poner pausas fisiológicas antes de agotar la reserva de dopamina.")
        ],
        "footer_title": "TDAH en Adultos · Estrategias Reales",
        "footer_sub": "Online para todo Chile y Presencial en Ñuñoa"
    },
    {
        "id": 19,
        "key": "crianza_rutinas_flexibles",
        "category": "Crianza Respetuosa",
        "kicker": "Hogar en Calma",
        "title_html": "Rutinas visuales para niños <span>sin batallas diarias</span> ni gritos",
        "points": [
            ("✦", "<strong>Anticipación gráfica:</strong> Los cerebros infantiles procesan imágenes 10 veces más rápido que instrucciones verbales repetidas."),
            ("✦", "<strong>Transiciones respetuosas:</strong> Avisos a los 10 y 5 minutos antes de cambiar de actividad."),
            ("✦", "<strong>Opciones limitadas:</strong> Dar 2 alternativas válidas ('¿Quieres ponerte la polera azul o la verde?') devuelve el sentido de control."),
            ("✦", "<strong>Orientación a padres:</strong> Acompañamiento clínico para diseñar rutinas personalizadas a tu familia.")
        ],
        "footer_title": "Orientación a Padres & Familias",
        "footer_sub": "Terapia Infanto-Juvenil · Centro Paz"
    },
    {
        "id": 20,
        "key": "comunicacion_asertiva_limites",
        "category": "Bienestar Adultos",
        "kicker": "Salud Emocional",
        "title_html": "Aprender a decir <span>'No tengo la energía'</span> sin pedir perdón",
        "points": [
            ("✦", "<strong>El 'Sí' por complacencia:</strong> Aceptar compromisos por miedo a defraudar agota tu batería social."),
            ("✦", "<strong>Límites como autocuidado:</strong> Un límite no es un ataque hacia el otro, es una protección hacia ti."),
            ("✦", "<strong>Frases asertivas:</strong> 'Me encantaría acompañarte, pero hoy necesito descansar en casa'."),
            ("✦", "<strong>Trabajo en terapia:</strong> Desactivar la culpa asociada a priorizar tu bienestar mental.")
        ],
        "footer_title": "Terapia Individual para Adultos",
        "footer_sub": "Espacio seguro, cálido y confidencial"
    },
    {
        "id": 21,
        "key": "tdah_rechazo_rsd",
        "category": "TDAH & Emociones",
        "kicker": "Sensibilidad Emocional",
        "title_html": "Sensibilidad al Rechazo (RSD): <span>Por qué una crítica duele tanto</span>",
        "points": [
            ("✦", "<strong>Dolor físico real:</strong> En el cerebro con TDAH la percepción de rechazo o crítica activa centros de dolor físico."),
            ("✦", "<strong>Reacción intensa:</strong> Miedo desmedido a haber molestado a alguien o necesidad compulsiva de disculparse."),
            ("✦", "<strong>Parálisis social:</strong> Evitar postular a trabajos o iniciar proyectos por temor al juicio ajeno."),
            ("✦", "<strong>Regulación en consulta:</strong> Herramientas somáticas y cognitivas para desescalar la alarma interna.")
        ],
        "footer_title": "Acompañamiento Neuroafirmativo",
        "footer_sub": "Valentina Castro Núñez · Psicóloga Clínica"
    },
    {
        "id": 22,
        "key": "primera_consulta_nunoa",
        "category": "Consulta Ñuñoa",
        "kicker": "Atención Presencial",
        "title_html": "¿Cómo es una sesión <span>presencial en Ñuñoa</span> en Centro Paz?",
        "points": [
            ("✦", "<strong>Ubicación accesible:</strong> Sector Plaza Ñuñoa / Metro Chile España, con fácil conectividad y estacionamiento."),
            ("✦", "<strong>Ambiente de calma sensorial:</strong> Iluminación cálida, bajo ruido y sillones diseñados para tu comodidad."),
            ("✦", "<strong>Enfoque cercano:</strong> Sin bata blanca ni juicios: una conversación humana de 50 minutos centrada en ti."),
            ("✦", "<strong>Boleta reembolsable:</strong> Entrega inmediata para reembolso en todas las Isapres.")
        ],
        "footer_title": "Consulta Presencial en Ñuñoa",
        "footer_sub": "Agenda tu hora por WhatsApp: +56 9 6516 3893"
    },
    {
        "id": 23,
        "key": "terapia_infantil_juego",
        "category": "Infanto-Juvenil",
        "kicker": "Psicología Infantil",
        "title_html": "En terapia infantil <span>el juego</span> es la herramienta más rigurosa",
        "points": [
            ("✦", "<strong>El lenguaje natural del niño:</strong> Los niños no procesan sus angustias hablando, las expresan jugando y dibujando."),
            ("✦", "<strong>Espacio seguro y libre:</strong> Permite elaborar miedos, frustraciones y dinámicas escolares sin presión."),
            ("✦", "<strong>Alianza con la familia:</strong> Sesiones periódicas con los padres para entregar pautas concretas para el hogar."),
            ("✦", "<strong>Enfoque neuroafirmativo:</strong> Respeto absoluto al ritmo y singularidad de cada niño o niña.")
        ],
        "footer_title": "Terapia Infanto-Juvenil & Crianza",
        "footer_sub": "Centro Paz · Ñuñoa y Online"
    },
    {
        "id": 24,
        "key": "ansiedad_somatica_cuerpo",
        "category": "Ansiedad Adultos",
        "kicker": "Cuerpo & Mente",
        "title_html": "Cuando la ansiedad <span>se siente en el cuerpo</span>: Terapia integrativa",
        "points": [
            ("✦", "<strong>Síntomas somáticos:</strong> Pecho apretado, bruxismo, nudo en la garganta o problemas digestivos sin causa médica."),
            ("✦", "<strong>Tu sistema nervioso en alarma:</strong> El cuerpo retiene la tensión antes de que la mente pueda procesarla."),
            ("✦", "<strong>Más allá de 'pensar positivo':</strong> Técnicas de estimulación del nervio vago y enraizamiento propioceptivo."),
            ("✦", "<strong>Recuperar la calma:</strong> Aprende a escuchar las señales de tu cuerpo antes de llegar al límite.")
        ],
        "footer_title": "Terapia Somática e Integrativa",
        "footer_sub": "Online y Presencial en Santiago Oriente"
    },
    {
        "id": 25,
        "key": "isapre_licencia_boletas",
        "category": "Educación Financiera",
        "kicker": "Guía Práctica",
        "title_html": "Boletas de Psicología: <span>Todo lo que debes saber</span> para tu Isapre",
        "points": [
            ("✦", "<strong>Requisito clave:</strong> Boleta electrónica de honorarios con RUT profesional acreditado en la SIS."),
            ("✦", "<strong>Código de prestación:</strong> Código oficial de psicoterapia clínica reconocido por todas las Isapres."),
            ("✦", "<strong>Plazo de reembolso:</strong> Subes el PDF a la app de tu Isapre y recibes el abono en tu cuenta en 3 a 5 días hábiles."),
            ("✦", "<strong>Sin trámites engorrosos:</strong> Te enviamos tu boleta lista al finalizar cada sesión.")
        ],
        "footer_title": "Transparencia en Aranceles",
        "footer_sub": "Centro Paz · www.centropaz.cl"
    },
    {
        "id": 26,
        "key": "desconexion_tecnologica_tdah",
        "category": "TDAH & Hábitos",
        "kicker": "Dopamina & Pantallas",
        "title_html": "La trampa del <span>Doomscrolling</span> en cerebros con TDAH",
        "points": [
            ("✦", "<strong>Búsqueda de dopamina barata:</strong> Las redes sociales entregan micro-recompensas inmediatas que atrapan al cerebro TDAH."),
            ("✦", "<strong>La parálisis nocturna:</strong> Quedarte 2 horas en la cama mirando el celular sabiendo que debes dormir."),
            ("✦", "<strong>Por qué la fuerza de voluntad falla:</strong> Se necesita rediseño de fricción ambiental (dejar el cargador fuera del dormitorio)."),
            ("✦", "<strong>Estrategias de desconexión:</strong> Recuperar tu descanso sin castigarte.")
        ],
        "footer_title": "Regulación de Hábitos en TDAH",
        "footer_sub": "Acompañamiento profesional en Centro Paz"
    },
    {
        "id": 27,
        "key": "padres_regulacion_propia",
        "category": "Crianza Consciente",
        "kicker": "Regla del Oxígeno",
        "title_html": "No puedes regular a tu hijo si <span>tu sistema está en alarma</span>",
        "points": [
            ("✦", "<strong>Neuronas espejo:</strong> Los niños sienten la tensión de sus padres antes de escuchar sus palabras."),
            ("✦", "<strong>La pausa de 5 segundos:</strong> Inhalar profundo y relajar los hombros antes de intervenir en un conflicto."),
            ("✦", "<strong>Cuidar al cuidador:</strong> La crianza exige espacios propios de descarga y acompañamiento psicológico."),
            ("✦", "<strong>Espacio para padres:</strong> Orientación clínica empática para mamás y papás en Centro Paz.")
        ],
        "footer_title": "Orientación a Padres & Crianza",
        "footer_sub": "Psicóloga Valentina Castro Núñez"
    },
    {
        "id": 28,
        "key": "autocuidado_fin_de_semana",
        "category": "Autocuidado Adultos",
        "kicker": "Pausa Consciente",
        "title_html": "Descanso pasivo vs. <span>Descanso Sensorial</span>: Cómo reponer energía",
        "points": [
            ("✦", "<strong>Descanso pasivo:</strong> Estar en el sillón mirando series (aún hay estímulos visuales y auditivos continuos)."),
            ("✦", "<strong>Descanso sensorial real:</strong> Silencio, luces bajas, ropa holgada y cero demandas sociales."),
            ("✦", "<strong>Validar tus necesidades:</strong> Decidir un domingo de baja estimulación es medicina preventiva para tu mente."),
            ("✦", "<strong>Inicia tu proceso:</strong> 50 minutos semanales dedicados a tu salud emocional en Centro Paz.")
        ],
        "footer_title": "Bienestar Emocional e Integrativo",
        "footer_sub": "Sesiones Online y Presenciales en Ñuñoa · Reembolso Isapre"
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,700;1,500;1,700&family=Nunito+Sans:wght@400;600;700;800&display=swap');
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      width: 1080px; height: 1350px; background: #FAF6F3;
      font-family: 'Nunito Sans', sans-serif; color: #2B2B2B;
      padding: 72px 80px; display: flex; flex-direction: column;
      justify-content: space-between; position: relative; overflow: hidden;
    }}
    .header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 36px; }}
    .brand {{ display: flex; align-items: center; gap: 16px; }}
    .logo-badge {{
      width: 56px; height: 56px; border-radius: 50%; background: #F0D9DE;
      display: flex; align-items: center; justify-content: center;
      font-family: 'Lora', serif; font-size: 26px; font-weight: 700; color: #7A2E3A;
    }}
    .brand-name {{ font-family: 'Lora', serif; font-size: 24px; font-weight: 700; color: #5C1F29; }}
    .brand-sub {{ font-size: 13px; text-transform: uppercase; letter-spacing: 2px; color: #4A6E60; font-weight: 700; }}
    .tag-category {{ background: #F0D9DE; color: #7A2E3A; padding: 8px 20px; border-radius: 40px; font-size: 16px; font-weight: 700; }}
    .kicker {{ font-size: 20px; text-transform: uppercase; letter-spacing: 3px; color: #7A2E3A; font-weight: 800; margin-bottom: 14px; }}
    h1 {{ font-family: 'Lora', Georgia, serif; font-size: 48px; line-height: 1.18; color: #5C1F29; margin-bottom: 28px; }}
    h1 span {{ background: #F0D9DE; padding: 0 8px; border-radius: 8px; }}
    .content-box {{
      background: #FFFFFF; border: 2px solid #EFE4DE; border-radius: 24px;
      padding: 30px 34px; box-shadow: 0 10px 30px rgba(122, 46, 58, 0.05); margin-bottom: 28px;
    }}
    .item-row {{ display: flex; align-items: flex-start; gap: 16px; margin-bottom: 16px; font-size: 19.5px; color: #2B2B2B; line-height: 1.4; }}
    .item-row:last-child {{ margin-bottom: 0; }}
    .bullet-icon {{ color: #7A2E3A; font-size: 22px; margin-top: 2px; }}
    .footer-cta {{
      background: #7A2E3A; color: #FFF; border-radius: 20px;
      padding: 24px 32px; display: flex; justify-content: space-between; align-items: center;
    }}
    .footer-cta-text h3 {{ font-family: 'Lora', serif; font-size: 22px; color: #FFF; margin-bottom: 4px; }}
    .footer-cta-text p {{ font-size: 15px; color: #F0D9DE; }}
    .wa-pill {{ background: #25D366; color: #FFF; padding: 12px 24px; border-radius: 40px; font-weight: 700; font-size: 17px; }}
  </style>
</head>
<body>
  <div>
    <div class="header">
      <div class="brand">
        <div class="logo-badge">CP</div>
        <div>
          <div class="brand-name">Centro Paz</div>
          <div class="brand-sub">Psicología Clínica</div>
        </div>
      </div>
      <div class="tag-category">{category}</div>
    </div>

    <div class="kicker">{kicker}</div>
    <h1>{title_html}</h1>

    <div class="content-box">
{points_html}
    </div>
  </div>

  <div class="footer-cta">
    <div class="footer-cta-text">
      <h3>{footer_title}</h3>
      <p>{footer_sub}</p>
    </div>
    <div class="wa-pill">
      <span>📲 Link en Bio</span>
    </div>
  </div>
</body>
</html>
"""


def generate_html_files():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    created = []
    for item in NEW_POSTS_DATA:
        filename = f"post_{item['id']:02d}_{item['key']}.html"
        filepath = OUTPUT_DIR / filename

        points_html = []
        for bullet, text in item["points"]:
            points_html.append(
                f'      <div class="item-row">\n'
                f'        <span class="bullet-icon">{bullet}</span>\n'
                f'        <span>{text}</span>\n'
                f'      </div>'
            )

        html_content = HTML_TEMPLATE.format(
            category=item["category"],
            kicker=item["kicker"],
            title_html=item["title_html"],
            points_html="\n".join(points_html),
            footer_title=item["footer_title"],
            footer_sub=item["footer_sub"],
        )
        filepath.write_text(html_content, encoding="utf-8")
        created.append(filename)
        print(f"✓ Creado: {filename}")

    print(f"\n🎉 {len(created)} nuevos archivos HTML generados en assets/instagram/")


if __name__ == "__main__":
    generate_html_files()
