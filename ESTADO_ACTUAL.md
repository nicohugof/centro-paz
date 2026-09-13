# Estado actual — Centro Paz

**Actualizado:** 2026-09-12

## Función

Ecosistema digital y motor de captación de pacientes de Centro Paz.

## Evidencia actual

- La copia activa está limpia y coincide con GitHub en `main`.
- Se eliminaron las ramas remotas de features ya mergeadas (`cursor/*`).
- El sitio en producción [www.centropaz.cl](https://www.centropaz.cl) responde HTTP 200 con GitHub Pages activo.
- Sistema de Blog Clínico desplegado en `/blog/` con 28 artículos estructurados con Schema JSON-LD (`MedicalWebPage`, `FAQPage`, `Article`) optimizado para motores de búsqueda conversacional de Inteligencia Artificial (ChatGPT Search, Perplexity, Gemini, Claude) y Google.
- Implementado el estándar abierto [`llms.txt`](file:///Users/nigoku/Proyectos/centro-paz/llms.txt) en la raíz para citación directa por modelos de lenguaje.
- `robots.txt` y `sitemap.xml` actualizados para permitir y priorizar crawlers de IA (`GPTBot`, `PerplexityBot`, `ClaudeBot`, `Google-Extended`).
- Workflow de GitHub Actions (`.github/workflows/auto_publish.yml`) configurado con cron diario (12:00 CLT / 15:00 UTC) para publicación 100% desatendida en blog y redes sociales (Meta Graph API).
- Pack Semana 1 en fase de cierre y Pack Semana 2 empaquetado en `marketing/pack-semana-2026-09-15/`.
- Playbooks de captación directa añadidos: Ficha Google Maps Ñuñoa (`docs/GOOGLE_BUSINESS_PROFILE_NUNOA.md`), Red de derivación interprofesional (`docs/RED_DERIVACION_CLINICA_LOCAL.md`) y Respuestas rápidas de WhatsApp Business (`docs/WHATSAPP_RESPUESTAS_RAPIDAS.md`).

## Directrices Operativas Clave

- **Atención por WhatsApp:** Atendido 100% de forma exclusiva y personal por **Valentina Castro Núñez** (`+56 9 6516 3893`). No se integran bots que simulen ser la psicóloga; se preserva la calidez humana, la confidencialidad y el secreto profesional.
- **Producción de Videos:** Se delega al pipeline automatizado de **YouTube IA** (`/Proyectos/youtube-ia`), alimentándose de los guiones clínicos en [`marketing/GUIONES_VIDEO_VERTICALES.md`](file:///Users/nigoku/Proyectos/centro-paz/marketing/GUIONES_VIDEO_VERTICALES.md).
- **Separación total de Ironcross:** Negocio clínico independiente, sin canales de WhatsApp compartidos ni cruces operativos.

## Próximo control

Monitorear el flujo de pacientes que llegan al WhatsApp de Valentina y avanzar en la prueba de generación de videos cortos desde YouTube IA.

