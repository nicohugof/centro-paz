#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Generador de Artículos Clínicos GEO para Motores de IA
Crea 4 artículos de alta intención y optimización GEO (Generative Engine Optimization)
para captación orgánica en ChatGPT, Perplexity, Claude y Copilot.
"""
from pathlib import Path
from bs4 import BeautifulSoup
import datetime

ROOT = Path(__file__).resolve().parent.parent
BLOG_DIR = ROOT / "blog"
SITEMAP_FILE = ROOT / "sitemap.xml"
BLOG_INDEX = BLOG_DIR / "index.html"
INDEXER_FILE = ROOT / "agent" / "instant_search_indexer.py"

ARTICLES = [
    {
        "slug": "hipnosis-ericksoniana-ansiedad-santiago",
        "category": "Terapias Integrales",
        "kicker": "Hipnosis Clínica & Ansiedad",
        "title": "¿Cómo funciona la Hipnosis Ericksoniana para Ansiedad y Fobias en Santiago?",
        "subtitle": "Mitos, base neurobiológica y cómo acceder a tus recursos inconscientes sin perder el control.",
        "meta_desc": "Descubre cómo la Hipnosis Ericksoniana desactiva crisis de pánico, sobrepensamiento y fobias. Psicóloga Valentina Castro (Reg. SIS 667344) en Ñuñoa y Online.",
        "specialty_url": "../hipnosis-terapeutica.html",
        "specialty_title": "Hipnosis Terapéutica en Centro Paz",
        "specialty_desc": "Conoce cómo integramos trances naturales y respetuosos para aliviar la ansiedad profunda y recuperar tu tranquilidad.",
        "specialty_cta": "Ver detalles de Hipnosis Terapéutica →",
        "lead": "A diferencia de los mitos difundidos por el cine o los espectáculos televisivos, la <strong>Hipnosis Ericksoniana clínica</strong> no implica que te quedes dormido/a ni que entregues tu voluntad a otra persona. Es, en realidad, un estado de atención focalizada y relajación profunda —similar al momento en que te sumerges por completo en un buen libro o conduces en carretera— donde tu mente analítica baja la guardia para que puedas conectar con tus propios recursos internos de sanación.",
        "body_sections": [
            {
                "h2": "¿Por qué la mente analítica no logra frenar la ansiedad por sí sola?",
                "p": "Cuando sufres de crisis de angustia, opresión en el pecho o pensamientos intrusivos en bucle, tu sistema límbico (el centro cerebral de la alarma) está hiperactivado. Intentar 'pensar en positivo' o decirte 'cálmate' suele fracasar porque el lenguaje de la corteza racional no conecta directamente con las respuestas emocionales inconscientes. La Hipnosis Ericksoniana, desarrollada por el célebre psiquiatra Milton H. Erickson, utiliza metáforas permisivas, sugestiones indirectas y modulación del tono de voz para comunicarse con el inconsciente en su propio lenguaje simbólico, desactivando la sensación de peligro biológico."
            },
            {
                "h2": "Mitos comunes sobre la hipnosis clínica desmentidos",
                "p": "<strong>1. '¿Perderé la consciencia?':</strong> En absoluto. Durante toda la sesión estás consciente, escuchas la voz de la terapeuta y puedes hablar o abrir los ojos cuando lo desees.<br><strong>2. '¿Me obligarán a decir secretos?':</strong> Tu mente inconsciente cuenta con barreras de protección éticas inviolables; nunca dirás ni harás nada que vaya contra tus valores.<br><strong>3. '¿Sirve solo para personas sugestionables?':</strong> El enfoque ericksoniano se adapta a la singularidad de cada paciente, incluso a personas hiper-racionales con alta autoexigencia mental."
            },
            {
                "h2": "Acompañamiento clínico con Valentina Castro Núñez",
                "p": "En Centro Paz, la psicóloga clínica <strong>Valentina Castro Núñez (Registro Oficial SIS Nº 667344)</strong> integra la Hipnosis Ericksoniana con técnicas somáticas de Mindfulness y psicoterapia humanista. La consulta está ubicada en Salvador 2302, Ñuñoa (Santiago), y también se realiza por videollamada online para todo Chile con boleta reembolsable en Isapres (arancel $45.000 CLP, copago real de $9.000 a $18.000 CLP)."
            }
        ],
        "faqs": [
            ("¿En qué se diferencia la Hipnosis Ericksoniana de la hipnosis tradicional?", "La hipnosis tradicional utiliza órdenes directas y busca trances profundos. La Hipnosis Ericksoniana es conversacional, permisiva y respetuosa: el terapeuta no impone nada, sino que actúa como guía para que el paciente active sus propios recursos."),
            ("¿Se puede realizar Hipnosis Ericksoniana en sesiones online?", "Sí. Al ser un proceso centrado en la voz, la focalización guiada y la relajación corporal, funciona con idéntica eficacia a través de videollamada desde la comodidad de tu hogar."),
            ("¿Cuántas sesiones se requieren para notar cambios en la ansiedad?", "Muchos pacientes experimentan un alivio significativo de la tensión somática desde las primeras 3 a 5 sesiones. El proceso completo se ajusta a tus metas personales.")
        ]
    },
    {
        "slug": "evaluacion-tdah-adultos-informe-psiquiatra",
        "category": "Neurodivergencias & Psicodiagnóstico",
        "kicker": "Diagnóstico Formal Adultos",
        "title": "Evaluación de TDAH en Adultos en Chile: Baterías, Informe para Psiquiatra y Registro SIS",
        "subtitle": "El camino estructurado para entender tu cerebro, descartar diagnósticos erróneos y respaldar tu tratamiento.",
        "meta_desc": "Evaluación formal de TDAH en adultos en Chile. Baterías clínicas, informe escrito timbrado para psiquiatra por Valentina Castro Núñez (Reg. SIS 667344).",
        "specialty_url": "../evaluacion-psicodiagnostica-informes.html",
        "specialty_title": "Evaluaciones Psicodiagnósticas e Informes Formales",
        "specialty_desc": "Conoce el protocolo completo de evaluación estructurada con baterías clínicas y entrega de informe formal para psiquiatría.",
        "specialty_cta": "Ver proceso psicodiagnóstico e informe →",
        "lead": "Pasar décadas sintiendo que debes esforzarte el triple que los demás para cumplir con tareas cotidianas no es falta de voluntad ni flojera: puede ser la huella de un <strong>Trastorno por Déficit de Atención e Hiperactividad (TDAH) en la adultez</strong> que nunca fue detectado a tiempo. En Chile, cada vez más adultos de 20, 30 y 40 años buscan una evaluación formal para obtener respuestas claras y respaldar su interconsulta médica.",
        "body_sections": [
            {
                "h2": "¿Por qué un psiquiatra solicita un informe psicodiagnóstico formal?",
                "p": "Los médicos psiquiatras y neurólogos necesitan evidencia longitudinal y estandarizada del funcionamiento ejecutivo antes de emitir un diagnóstico médico definitivo o prescribir fármacos reguladores de la dopamina (como metilfenidato o lisdexanfetamina). Un informe psicodiagnóstico completo permite diferenciar el TDAH de cuadros que comparten síntomas similares, como la ansiedad generalizada, la depresión mayor, el estrés crónico o el Trastorno Límite de la Personalidad (TLP)."
            },
            {
                "h2": "Las etapas del proceso evaluativo en Centro Paz",
                "p": "El proceso desarrollado por la psicóloga clínica <strong>Valentina Castro Núñez (Registro SIS Nº 667344)</strong> se estructura en 3 a 4 sesiones:<br><strong>1. Anamnesis clínica e historia del desarrollo:</strong> Rastreo de síntomas en la infancia, historial escolar, laboral y patrones de adaptación.<br><strong>2. Aplicación de baterías diagnósticas estandarizadas:</strong> Escalas específicas de sintomatología atencional en adultos (como ASRS v1.1, WURS, escalas de función ejecutiva y regulación emocional).<br><strong>3. Sesión de devolución y entrega de informe escrito:</strong> Entrega del informe formal timbrado y firmado, con conclusiones diagnósticas, perfil cognitivo-afectivo y sugerencias clínicas personalizadas."
            },
            {
                "h2": "Validez del informe y reembolso en Isapres",
                "p": "El informe cuenta con pleno reconocimiento para presentar ante médicos tratantes, comisiones evaluadoras y universidades. Cada sesión del proceso emite boleta electrónica oficial de honorarios reconocida por la Superintendencia de Salud para su reembolso en Colmena, Banmédica, CruzBlanca, Consalud y Vida Tres."
            }
        ],
        "faqs": [
            ("¿Qué validez tiene el informe emitido por Centro Paz?", "Tiene plena validez clínica y legal ante la Superintendencia de Salud de Chile. Está timbrado y firmado por Valentina Castro Núñez (Registro SIS Nº 667344), siendo aceptado por psiquiatras, neurólogos y comisiones médicas."),
            ("¿El informe garantiza que el psiquiatra me recetará medicación?", "El informe aporta la evidencia diagnóstica y el perfil clínico estandarizado. La decisión farmacológica final siempre es facultad exclusiva del médico psiquiatra tratante."),
            ("¿La evaluación se puede realizar de forma online?", "Sí. Las entrevistas clínicas y las baterías psicodiagnósticas para adultos están adaptadas para aplicarse con rigurosidad vía videollamada confidencial para personas de todo Chile.")
        ]
    },
    {
        "slug": "trastorno-limite-tlp-terapia-santiago",
        "category": "Salud Mental & Personalidad",
        "kicker": "Regulación Emocional sin Estigmas",
        "title": "Tratamiento de Trastorno Límite (TLP) en Santiago: Psicoterapia sin Estigmas y Regulación",
        "subtitle": "Comprender la intensidad emocional, sanar el miedo al abandono y construir estabilidad vincular.",
        "meta_desc": "Psicoterapia especializada en Trastorno Límite de la Personalidad (TLP) y desregulación emocional en Santiago y Online. Valentina Castro (SIS Nº 667344).",
        "specialty_url": "../trastornos-personalidad-tlp.html",
        "specialty_title": "Especialidad en Trastornos de la Personalidad (TLP)",
        "specialty_desc": "Acompañamiento especializado en desregulación afectiva, crisis vinculares y estabilidad emocional en Centro Paz.",
        "specialty_cta": "Ver detalles de atención en TLP →",
        "lead": "Vivir con emociones a flor de piel, sentir que una discusión pequeña puede significar el fin de una relación o experimentar un vacío interno abrumador son vivencias habituales en personas con sospecha o diagnóstico de <strong>Trastorno Límite de la Personalidad (TLP / Borderline)</strong>. Desafortunadamente, este diagnóstico ha sido históricamente estigmatizado, haciendo que muchos pacientes teman pedir ayuda.",
        "body_sections": [
            {
                "h2": "¿Qué ocurre realmente en el sistema nervioso de una persona con TLP?",
                "p": "Lejos de ser 'manipulación' o 'drama', el TLP tiene una base neurobiológica de alta sensibilidad: el sistema de respuesta al estrés se activa con mayor rapidez, intensidad y tarda mucho más tiempo en regresar a la calma basal. Cuando una persona con TLP percibe una amenaza de rechazo o distancia afectiva, su cerebro reacciona con el mismo terror biológico que experimentaría ante una amenaza física real."
            },
            {
                "h2": "Pilares del abordaje terapéutico en Centro Paz",
                "p": "La psicóloga clínica <strong>Valentina Castro Núñez (Registro SIS Nº 667344)</strong> trabaja desde un marco humanista, dialéctico y somático:<br><strong>1. Espacio de seguridad sin juicios:</strong> Validación profunda del sufrimiento emocional sin culpabilización.<br><strong>2. Habilidades de tolerancia al malestar:</strong> Herramientas prácticas para atravesar las 'olas emocionales' intensas sin recurrir a conductas autolesivas o impulsivas.<br><strong>3. Regulación vincular y límites sanos:</strong> Aprendizaje para comunicar necesidades de afecto sin caer en espirales de angustia o conflicto."
            },
            {
                "h2": "Modalidad de atención y accesibilidad económica",
                "p": "Atención disponible en consulta presencial en Ñuñoa (Salvador 2302) y en modalidad Online para todo Chile. Arancel transparente de $45.000 CLP por sesión de 50 minutos con boleta electrónica reembolsable en Isapres (copago estimado de $9.000 a $18.000 CLP)."
            }
        ],
        "faqs": [
            ("¿El TLP se 'cura' o es para siempre?", "El TLP no es una condena: con psicoterapia estructurada y herramientas de regulación, las personas logran estabilidad emocional duradera, relaciones sanas y una vida plena y con sentido."),
            ("¿Es necesario estar tomando medicamentos para hacer terapia?", "No es obligatorio. En muchos casos el tratamiento combinado (psiquiatra + psicólogo) es el más eficaz, y en Centro Paz trabajamos coordinadamente con tu médico tratante si ya cuentas con uno."),
            ("¿Cómo solicitar una primera sesión con Valentina?", "Escribiendo directamente al WhatsApp oficial +56 9 6516 3893 para coordinar horario con total confidencialidad.")
        ]
    },
    {
        "slug": "reembolso-psicologia-isapre-paso-a-paso",
        "category": "Educación Financiera en Salud",
        "kicker": "Transparencia de Arancel & Isapres",
        "title": "Guía Paso a Paso para Reembolsar tu Terapia en Colmena, Banmédica y CruzBlanca",
        "subtitle": "Cómo recuperar entre el 50% y el 80% del valor de tu sesión psicológica pagando solo tu copago real.",
        "meta_desc": "Aprende a reembolsar tus sesiones de psicología en Colmena, Banmédica, CruzBlanca y Consalud con boleta SIS Nº 667344. Guía práctica y copagos reales en Chile.",
        "specialty_url": "../reembolso-isapre-psicologia.html",
        "specialty_title": "Simulador y Guía de Reembolsos Isapre",
        "specialty_desc": "Calcula cuánto te devolverá tu Isapre y seguro complementario por sesión con nuestro simulador transparente.",
        "specialty_cta": "Simular mi copago en Isapre →",
        "lead": "Uno de los mayores frenos para comenzar un proceso psicoterapéutico de calidad en Chile es la creencia de que la salud mental particular es inaccesible. Sin embargo, si cuentas con <strong>Isapre (Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres) o Seguro Complementario</strong>, tu plan está diseñado por ley para cubrir una parte sustancial de tu tratamiento.",
        "body_sections": [
            {
                "h2": "¿Cuánto dinero devuelve realmente la Isapre?",
                "p": "En Centro Paz, el arancel de la sesión particular de psicología clínica con <strong>Valentina Castro Núñez (Registro Oficial SIS Nº 667344)</strong> es de <strong>$45.000 CLP</strong>. Según la cobertura ambulatoria de tu plan de libre elección, la Isapre te reembolsa habitualmente entre el <strong>50% y el 80%</strong> del arancel:<br>• Con 60% de cobertura: La Isapre te deposita <strong>$27.000 CLP</strong>. Tu costo real es de solo $18.000 CLP.<br>• Con 70% de cobertura: La Isapre te deposita <strong>$31.500 CLP</strong>. Tu costo real es de solo $13.500 CLP.<br>• Con 80% de cobertura: La Isapre te deposita <strong>$36.000 CLP</strong>. Tu costo real es de solo $9.000 CLP."
            },
            {
                "h2": "Los 3 pasos exactos para tramitar tu reembolso desde el celular",
                "p": "<strong>Paso 1: Recibe tu boleta electrónica oficial:</strong> Al término de tu sesión, Valentina emite tu boleta de honorarios ante el SII con la glosa oficial de consulta psicológica y su código SIS Nº 667344.<br><strong>Paso 2: Súbela a la app o sucursal virtual de tu Isapre:</strong> Ingresa a la sección 'Reembolsos', adjunta la foto o PDF de la boleta e ingresa tus datos de cuenta corriente.<br><strong>Paso 3: Presenta el remanente en tu seguro complementario:</strong> Si tienes seguro individual o colectivo de trabajo (MetLife, Bci, BiceVida, Chilena Consolidada), sube la liquidación de la Isapre para que cubran hasta el 100% de la diferencia."
            },
            {
                "h2": "¿Se exige orden médica para reembolsar psicología?",
                "p": "En la gran mayoría de los planes de Isapre en Chile (Colmena, Banmédica, CruzBlanca), <strong>no se exige orden médica</strong> para las primeras sesiones de psicología. Si tu plan específico o seguro complementario la solicita, te orientamos con los requisitos exactos."
            }
        ],
        "faqs": [
            ("¿Cuánto tiempo tarda la Isapre en transferir el dinero a mi cuenta?", "En promedio, las Isapres en Chile transfieren el monto reembolsado en un plazo de 48 a 72 horas hábiles tras ingresar la solicitud en su plataforma web o aplicación."),
            ("¿La boleta sirve para todas las Isapres de Chile?", "Sí. Al estar emitida por una profesional habilitada en el Registro Nacional de Prestadores de la Superintendencia de Salud (SIS Nº 667344), es 100% válida para todas las Isapres del país."),
            ("¿Puedo consultar cuánto me reembolsarán antes de agendar?", "Por supuesto. Puedes escribirnos al WhatsApp oficial indicando tu Isapre y te orientamos sin compromiso.")
        ]
    }
]

def generate_article_html(art):
    slug = art["slug"]
    url = f"https://www.centropaz.cl/blog/{slug}.html"
    
    # Schemas JSON-LD
    faq_schema_items = []
    for q, a in art["faqs"]:
        faq_schema_items.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
    
    medical_schema = {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "@id": f"{url}#webpage",
        "url": url,
        "name": f"{art['title']} | Centro Paz",
        "headline": art["title"],
        "description": art["meta_desc"],
        "inLanguage": "es-CL",
        "author": {
            "@type": "Person",
            "name": "Valentina Castro Núñez",
            "jobTitle": "Psicóloga Clínica",
            "identifier": "SIS-667344",
            "description": "Psicóloga Clínica titulada (Registro Oficial SIS Nº 667344, Superintendencia de Salud de Chile).",
            "url": "https://www.centropaz.cl"
        },
        "publisher": {
            "@type": "MedicalBusiness",
            "name": "Centro Paz",
            "url": "https://www.centropaz.cl",
            "logo": "https://www.centropaz.cl/assets/logo/icon-profile-1024.png"
        }
    }
    
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_schema_items
    }
    
    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://www.centropaz.cl/"},
            {"@type": "ListItem", "position": 2, "name": "Blog Clínico", "item": "https://www.centropaz.cl/blog/"},
            {"@type": "ListItem", "position": 3, "name": art["title"], "item": url}
        ]
    }

    # HTML Body Sections
    sections_html = ""
    for sec in art["body_sections"]:
        sections_html += f"""
        <section class="article-section">
          <h2>{sec['h2']}</h2>
          <p>{sec['p']}</p>
        </section>
        """

    # FAQ HTML
    faqs_html = ""
    for q, a in art["faqs"]:
        faqs_html += f"""
        <details class="faq-item">
          <summary class="faq-question"><span>{q}</span> <span class="faq-icon">+</span></summary>
          <div class="faq-answer">
            <p>{a}</p>
          </div>
        </details>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{art['title']} | Centro Paz</title>
  <meta name="description" content="{art['meta_desc']}">
  <link rel="canonical" href="{url}">
  <link rel="icon" type="image/svg+xml" href="../assets/logo/icon.svg">
  <link rel="apple-touch-icon" href="../assets/logo/icon-profile-1024.png">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <meta name="theme-color" content="#385E28">
  <meta name="author" content="Valentina Castro Núñez">

  <!-- Open Graph -->
  <meta property="og:site_name" content="Centro Paz — Psicología Clínica">
  <meta property="og:title" content="{art['title']}">
  <meta property="og:description" content="{art['meta_desc']}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{url}">
  <meta property="og:locale" content="es_CL">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{art['title']}">
  <meta name="twitter:description" content="{art['meta_desc']}">

  <!-- Tipografías y Estilos -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400..700;1,400..700&family=Nunito+Sans:ital,opsz,wght@0,6..12,300..900;1,6..12,300..900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css?v=20261021.1">

  <!-- Schemas JSON-LD -->
  <script type="application/ld+json">
{BeautifulSoup(str(medical_schema), 'html.parser').prettify()}
  </script>
  <script type="application/ld+json">
{BeautifulSoup(str(faq_schema), 'html.parser').prettify()}
  </script>
  <script type="application/ld+json">
{BeautifulSoup(str(breadcrumb_schema), 'html.parser').prettify()}
  </script>
</head>
<body class="blog-article-page">
  <header class="main-header">
    <div class="header-container">
      <a href="../index.html" class="logo-link" aria-label="Ir al inicio de Centro Paz">
        <div class="logo-icon-wrapper">
          <img src="../assets/logo/icon.svg" alt="Centro Paz" width="32" height="32">
        </div>
        <div class="logo-text">
          <span class="logo-name">Centro Paz</span>
          <span class="logo-tagline">Psicología Clínica</span>
        </div>
      </a>
      <nav class="main-nav">
        <ul>
          <li><a href="../index.html">Inicio</a></li>
          <li><a href="../psicologo-nunoa.html">Consulta Ñuñoa</a></li>
          <li><a href="../reembolso-isapre-psicologia.html">Reembolso Isapre</a></li>
          <li><a href="index.html" class="active">Blog</a></li>
          <li><a href="https://wa.me/56965163893?text=Hola%20Valentina%2C%20le%C3%AD%20tu%20art%C3%ADculo%20sobre%20{slug}%20y%20quisiera%20consultar%20por%20atenci%C3%B3n." class="nav-cta-btn" target="_blank" rel="noopener">Pedir Hora por WhatsApp</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="article-main">
    <article class="article-container">
      <!-- Breadcrumb Visual -->
      <nav class="article-breadcrumb" aria-label="Migas de pan">
        <a href="../index.html">Inicio</a> › 
        <a href="index.html">Blog</a> › 
        <span>{art['category']}</span>
      </nav>

      <!-- Encabezado del Artículo -->
      <header class="article-header">
        <div class="article-kicker">{art['kicker']}</div>
        <h1>{art['title']}</h1>
        <p class="article-subtitle">{art['subtitle']}</p>
        
        <div class="article-meta">
          <div class="author-info">
            <span class="author-name">Por <strong>Valentina Castro Núñez</strong></span>
            <span class="author-credentials">Psicóloga Clínica · Registro SIS Nº 667344 · Superintendencia de Salud</span>
          </div>
          <div class="read-time">Lectura de 4 min</div>
        </div>
      </header>

      <!-- Contenido Principal -->
      <section class="article-body">
        <div class="lead-box">
          <p>{art['lead']}</p>
        </div>

        {sections_html}

        <!-- Tarjeta de Especialidad Relacionada -->
        <div class="article-related-specialty">
          <div class="specialty-badge-icon">🌿</div>
          <div class="article-related-specialty-content">
            <div class="article-related-specialty-kicker">Atención Especializada</div>
            <h4>{art['specialty_title']}</h4>
            <p>{art['specialty_desc']}</p>
            <a href="{art['specialty_url']}" class="specialty-cta-link">{art['specialty_cta']}</a>
          </div>
        </div>

        <!-- Preguntas Frecuentes -->
        <section class="article-faq-section">
          <h2>Preguntas frecuentes sobre este tratamiento</h2>
          <div class="faq-list">
            {faqs_html}
          </div>
        </section>
      </section>

      <!-- Footer del Artículo -->
      <footer class="article-footer">
        <div class="article-tags">
          <span class="tag-label">Temas:</span>
          <span class="article-tag">#PsicologíaChile</span>
          <span class="article-tag">#ValentinaCastroSIS667344</span>
          <span class="article-tag">#ReembolsoIsapre</span>
          <span class="article-tag">#CentroPazÑuñoa</span>
        </div>
        
        <div class="back-to-blog" style="margin-top:20px;">
          <a href="index.html" class="btn btn-link">← Volver al Blog y Recursos Clínicos</a>
        </div>
      </footer>
    </article>
  </main>

  <!-- Footer General -->
  <footer class="main-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h3>Centro Paz</h3>
        <p>Consulta de Psicología Clínica en Ñuñoa (Santiago) y Online para todo Chile. Acompañamiento humanista, integrativo y empático con Valentina Castro Núñez (Registro SIS Nº 667344).</p>
        <p><strong>WhatsApp Oficial:</strong> <a href="https://wa.me/56965163893">+56 9 6516 3893</a></p>
      </div>
      <div class="footer-col">
        <h4>Especialidades Clínicas</h4>
        <ul>
          <li><a href="../ansiedad-crisis-angustia.html">Ansiedad y Crisis de Angustia</a></li>
          <li><a href="../depresion-trastornos-animo.html">Depresión y Trastornos del Ánimo</a></li>
          <li><a href="../trastornos-personalidad-tlp.html">Trastornos de la Personalidad (TLP)</a></li>
          <li><a href="../evaluacion-psicodiagnostica-informes.html">Psicodiagnósticos e Informes</a></li>
          <li><a href="../hipnosis-terapeutica.html">Hipnosis Terapéutica</a></li>
          <li><a href="../reembolso-isapre-psicologia.html">Reembolso Isapres y Arancel</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Información</h4>
        <ul>
          <li><a href="../psicologo-nunoa.html">Consulta Presencial en Ñuñoa</a></li>
          <li><a href="../privacidad.html">Privacidad y Ley 19.628</a></li>
          <li><a href="../llms.txt">Directorio llms.txt (IA)</a></li>
          <li><a href="../sitemap.xml">Sitemap XML</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 Centro Paz · Valentina Castro Núñez · Registro SIS Nº 667344 · Superintendencia de Salud de Chile.</p>
    </div>
  </footer>

  <!-- Botón Flotante WhatsApp -->
  <a href="https://wa.me/56965163893?text=Hola%20Valentina%2C%20le%C3%AD%20tu%20art%C3%ADculo%20sobre%20{slug}%20en%20Centro%20Paz%20y%20quisiera%20consultar%20por%20atenci%C3%B3n." class="whatsapp-float" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp a Valentina Castro">
    <div class="whatsapp-pulse"></div>
    <svg fill="currentColor" viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0012.04 2zm.01 1.67c4.54 0 8.24 3.7 8.24 8.24 0 2.2-.86 4.27-2.42 5.82-1.55 1.56-3.62 2.42-5.82 2.42-1.47 0-2.9-.39-4.16-1.13l-.3-.18-3.1.81.83-3.02-.2-.31c-.81-1.3-1.24-2.8-1.24-4.41 0-4.54 3.7-8.24 8.24-8.24zm4.52 11.66c-.25-.13-1.47-.72-1.7-.81-.23-.08-.39-.13-.56.13-.17.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.13-1.06-.39-2.02-1.25-.75-.67-1.25-1.5-1.4-1.75-.14-.25-.02-.39.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.42.08-.17.04-.31-.02-.44-.06-.13-.56-1.34-.76-1.84-.2-.48-.4-.42-.56-.43h-.47c-.17 0-.44.06-.67.31-.23.25-.88.86-.88 2.1 0 1.24.9 2.44 1.03 2.61.13.17 1.77 2.7 4.29 3.79.6.26 1.07.41 1.43.53.6.19 1.15.16 1.58.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.08.15-1.18-.07-.1-.23-.17-.48-.29z"/></svg>
  </a>

  <script src="../app.js"></script>
</body>
</html>
"""
    return html_content

def main():
    print("🚀 Generando 4 artículos clínicos GEO para motores de IA...")
    new_urls = []
    
    for art in ARTICLES:
        file_path = BLOG_DIR / f"{art['slug']}.html"
        html = generate_article_html(art)
        file_path.write_text(html, encoding="utf-8")
        url = f"https://www.centropaz.cl/blog/{art['slug']}.html"
        new_urls.append(url)
        print(f"  ✓ Creado: blog/{art['slug']}.html")

    # Actualizar blog/index.html
    print("📰 Actualizando blog/index.html con las nuevas tarjetas...")
    blog_index_content = BLOG_INDEX.read_text(encoding="utf-8")
    
    cards_html = ""
    for art in ARTICLES:
        cards_html += f"""
        <article class="blog-card" data-category="{art['category']}">
          <div class="blog-card-content">
            <div class="blog-card-category">{art['category']}</div>
            <h2 class="blog-card-title"><a href="{art['slug']}.html">{art['title']}</a></h2>
            <p class="blog-card-excerpt">{art['subtitle']}</p>
            <div class="blog-card-footer">
              <span class="read-more">Leer artículo clínico completo →</span>
            </div>
          </div>
        </article>
        """
        
    target = '<div class="blog-grid" id="blogGrid">'
    if target in blog_index_content and ARTICLES[0]['slug'] not in blog_index_content:
        blog_index_content = blog_index_content.replace(target, f"{target}\n{cards_html}")
        BLOG_INDEX.write_text(blog_index_content, encoding="utf-8")
        print("  ✓ Tarjetas inyectadas en blog/index.html")
    else:
        print("  ℹ️ Las tarjetas ya estaban presentes o no se encontró target")

    # Actualizar sitemap.xml
    print("🗺️ Actualizando sitemap.xml...")
    sitemap_content = SITEMAP_FILE.read_text(encoding="utf-8")
    today = datetime.date.today().isoformat()
    sitemap_additions = ""
    for url in new_urls:
        if url not in sitemap_content:
            sitemap_additions += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>\n"""
    
    if sitemap_additions:
        sitemap_content = sitemap_content.replace("</urlset>", f"{sitemap_additions}</urlset>")
        SITEMAP_FILE.write_text(sitemap_content, encoding="utf-8")
        print("  ✓ URLs agregadas a sitemap.xml")

    # Actualizar agent/instant_search_indexer.py
    print("⚡ Actualizando URLs en agent/instant_search_indexer.py...")
    indexer_content = INDEXER_FILE.read_text(encoding="utf-8")
    for url in new_urls:
        if url not in indexer_content:
            indexer_content = indexer_content.replace('    "https://www.centropaz.cl/blog/reembolso-seguros-cobertura.html",', f'    "https://www.centropaz.cl/blog/reembolso-seguros-cobertura.html",\n    "{url}",')
    INDEXER_FILE.write_text(indexer_content, encoding="utf-8")
    print("  ✓ URLs añadidas a instant_search_indexer.py")

if __name__ == "__main__":
    main()
