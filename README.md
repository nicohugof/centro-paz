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
├── index.html                           # Landing page completa y responsive
├── privacidad.html                      # Política de privacidad (Ley 19.628 + secreto profesional)
├── 404.html                             # Página de error para GitHub Pages
├── robots.txt / sitemap.xml             # SEO básico
├── styles.css                           # Sistema de diseño CSS y variables de marca
├── app.js                               # Motor de triaje, simulador de Isapres y screener
├── CNAME                                # Configuración de dominio www.centropaz.cl
├── guia_7_claves_regulacion_centro_paz.html # Plantilla HTML del Lead Magnet
├── guia_7_claves_regulacion_centro_paz.pdf  # PDF descargable para enviar por WhatsApp
├── protocolo_captacion_whatsapp.md      # Playbook de atención y cierre de pacientes por WhatsApp
├── estrategia_adquisicion_redes.md      # Estrategia de contenidos, reels y SEO local
├── README.md                            # Documentación maestra del proyecto
├── assets/
│   └── instagram/
│       ├── post_01_tdah_adultos.png     # Pieza 1: TDAH en Adultos (1080x1350)
│       ├── post_02_reembolso_isapre.png # Pieza 2: Reembolso Isapre (1080x1350)
│       └── post_03_crianza_regulacion.png # Pieza 3: Crianza Respetuosa (1080x1350)
└── agent/
    ├── __init__.py
    ├── content_engine.py                # Motor de copys, ganchos y hashtags
    ├── marketing_agent.py               # CLI para generar calendarios y renderizar imágenes
    └── n8n_marketing_payload.json       # Payload estructurado para bots / n8n / webhooks
```

---

## 🤖 Uso del Agente de Marketing Autónomo

El agente permite automatizar la generación de calendarios y renderizado de imágenes:

```bash
# 1. Ver la parrilla semanal de contenidos con copys y hashtags
python3 -m agent.marketing_agent --calendar

# 2. Re-renderizar todas las piezas gráficas a PNG de alta resolución (1080x1350)
#    Usa Chrome/Chromium en Linux, macOS o Windows (o la variable CHROME_BIN)
python3 -m agent.marketing_agent --render-posts

# 3. Exportar el JSON actualizado para n8n / webhooks
python3 -m agent.marketing_agent --export-json

# 4. Probar conexión Meta Graph API (requiere token en agent/meta_config.json)
python3 -m agent.auto_publisher --test-connection
```

---

## 📞 Protocolo de Conversión Rápida de Pacientes

1. **Recepción en WhatsApp:** Saludo cálido + validación del motivo de consulta.
2. **Derribar la barrera del precio:** Explicar el reembolso de Isapre (copago real estimado entre $15.000 y $20.000 CLP).
3. **Ofrecer 2 opciones de horario concretas:** *"Tengo disponibilidad este jueves a las 17:00 o viernes a las 11:00. ¿Cuál te acomoda mejor?"*
4. **Seguimiento a las 24 horas:** Enviar la *Guía Gratuita de Regulación Sensorial en PDF* como aporte de valor a quienes no hayan confirmado.

---

© 2026 Centro Paz (CPAZ) · Valentina Castro Núñez.
