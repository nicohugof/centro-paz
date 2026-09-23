# 🌿 Centro Paz (CPAZ) — Ecosistema Digital y Motor de Captación de Pacientes

Centro Paz es un centro de psicología clínica enfocado en acompañamiento humanista e integrativo, con especialidad en **Adultos**, **Neurodivergencias (TEA y TDAH)** y **Terapia Infanto-Juvenil con Orientación a Padres**.

---

## 📋 Ficha Técnica del Negocio

| Parámetro | Valor Oficial |
| :--- | :--- |
| **Nombre del Centro** | Centro Paz (CPAZ) |
| **Terapeuta y Fundadora** | **Valentina Castro Núñez** · Psicóloga Clínica |
| **Registro Profesional** | Registro Superintendencia de Salud de Chile (SIS) |
| **Enfoque Clínico** | Humanista, Integrativo y Neuroafirmativo |
| **Modalidad de Atención** | Online (Todo Chile) y Presencial (Santiago, Chile) |
| **WhatsApp Oficial** | `+56 9 6516 3893` (Link: `https://wa.me/56965163893`) |
| **Correo Electrónico** | `contacto.centropaz@gmail.com` |
| **Sitio Web Oficial** | [https://www.centropaz.cl](https://www.centropaz.cl) / [GitHub Pages](https://nicohugof.github.io/centro-paz/) |
| **Instagram** | [@centropaz.cl](https://instagram.com/centropaz.cl) |
| **TikTok** | [@centropaz.cl](https://tiktok.com/@centropaz.cl) |
| **Facebook** | [Centro Paz](https://www.facebook.com/profile.php?id=61593207820690) |
| **Arancel de Referencia** | $45.000 CLP por sesión particular (Boleta 100% reembolsable) |
| **Cobertura / Isapres** | Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres, Nueva Masvida y Seguros Complementarios |

---

## 🎯 Especialidades Clínicas Activas

1. **👤 Terapia Individual para Adultos:**
   - Manejo de ansiedad, estrés y sobrecarga mental.
   - Autoestima, autoconocimiento y bienestar emocional.
   - Acompañamiento en transiciones vitales y toma de decisiones.

2. **🧠 Neurodivergencias (TEA y TDAH en Adultos e Infancia):**
   - Perspectiva neuroafirmativa (sin juicios ni encasillamientos).
   - Sospecha y diagnóstico tardío en personas adultas.
   - Regulación sensorial, prevención del agotamiento (*burnout / masking*) y estrategias para la vida diaria y laboral.

3. **🌱 Terapia Infanto-Juvenil & Orientación a Padres:**
   - Acompañamiento lúdico y cálido a niños y adolescentes.
   - Manejo de desbordes emocionales, tolerancia a la frustración y autoestima escolar/social.
   - **Orientación continua a padres:** Pautas concretas de contención y crianza respetuosa sin gritos ni castigos.

*(Nota: Quedaron excluidas explícitamente las áreas de terapia de pareja, terapia de trauma y terapia familiar sistémica).*

---

## 🎨 Identidad Visual y Marca

* **Colores de Marca:**
  - `Burdeo Profundo`: `#7A2E3A` (Color primario, botones principales, titulares)
  - `Rosado Empolvado`: `#F0D9DE` (Fondos de tarjetas, insignias, acentos suaves)
  - `Verde Salvia`: `#A9C4B8` (Toques de calma y crecimiento)
  - `Celeste Pálido`: `#CFE3E8` (Detalles complementarios)
  - `Fondo Crema`: `#FAF6F3` (Fondo general del sitio web)
* **Tipografías:**
  - Titulares: *Lora* (Serif elegante, cercana y profesional)
  - Texto principal: *Nunito Sans* (Sans-serif limpia, moderna y de alta legibilidad)

---

## 💻 Arquitectura del Proyecto y Archivos

```text
/Users/nigoku/CPAZ/
├── index.html                           # Landing page completa, responsive y optimizada para SEO
├── privacidad.html                      # Política de privacidad (Ley 19.628 + secreto profesional)
├── links.html                           # Hub de enlaces para biografía móvil de redes sociales (/links)
├── 404.html                             # Página de error para GitHub Pages
├── robots.txt / sitemap.xml             # Directivas de indexación para buscadores y bots de IA
├── llms.txt                             # Resumen clínico estructurado para modelos de lenguaje (LLMs)
├── styles.css                           # Sistema de diseño CSS y variables de marca
├── app.js                               # Motor de triaje, simulador de Isapres y screener
├── cpaz.py                              # Panel de control CLI interactivo
├── CNAME                                # Dominio personalizado www.centropaz.cl
├── blog/                                # 28 artículos clínicos estructurados con Schema.org
├── docs/                                # Playbooks operativos y guías de derivación clínica
├── marketing/                           # Packs semanales de contenido, guiones de video y copys
├── assets/
│   ├── logo/                            # Logotipo oficial (símbolo Ψ y laureles) en SVG y PNG
│   ├── videos/                          # 10 videos verticales (9:16) con audio sintético en chileno
│   └── instagram/                       # 28 infografías cuadradas y verticales (1080x1350 PNG)
└── agent/
    ├── __init__.py
    ├── auto_publisher.py                # Publicador automático multi-slot para Meta Graph API
    ├── blog_clinical_knowledge.py       # Corpus de conocimiento clínico estructurado
    ├── blog_generator.py                # Generador estático del blog, sitemap y llms.txt
    ├── content_engine.py                # Motor de copys, ganchos y hashtags
    ├── marketing_agent.py               # Herramientas de visualización y exportación de marketing
    ├── organic_lead_scout.py            # Scout de respuestas orgánicas en comunidades
    ├── video_shorts_generator.py        # Generador de videos y subtítulos con Azure Neural TTS
    └── whatsapp_assistant.py            # Asistente de respuestas rápidas para Valentina
```

---

## 🤖 Uso del Centro de Control y Agentes

Puedes interactuar directamente con el ecosistema a través del CLI unificado o comandos específicos:

```bash
# 1. Iniciar el panel central interactivo
python3 cpaz.py

# 2. Reconstruir todo el Blog Clínico, sitemap.xml y llms.txt
python3 agent/blog_generator.py

# 3. Simular publicación automática en redes sociales (Dry Run)
PYTHONPATH=. python3 -m agent.auto_publisher --slot auto --dry-run

# 4. Ver el catálogo de guiones de video vertical
python3 -m agent.video_shorts_generator --catalog
```

---

## 📞 Protocolo de Conversión Rápida de Pacientes

1. **Recepción en WhatsApp:** Saludo cálido + validación del motivo de consulta.
2. **Derribar la barrera del precio:** Explicar el reembolso de Isapre (copago real estimado entre $15.000 y $20.000 CLP).
3. **Ofrecer 2 opciones de horario concretas:** *"Tengo disponibilidad este jueves a las 17:00 o viernes a las 11:00. ¿Cuál te acomoda mejor?"*
4. **Seguimiento a las 24 horas:** Enviar la *Guía Gratuita de Regulación Sensorial en PDF* como aporte de valor a quienes no hayan confirmado.

---

© 2026 Centro Paz (CPAZ) · Valentina Castro Núñez.
