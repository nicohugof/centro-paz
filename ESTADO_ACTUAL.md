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
- Packs Semanales estructurados: Pack Semana 1 (2026-09-08), Pack Semana 2 (2026-09-15) y Pack Semana 3 (2026-09-22) empaquetados en `marketing/` con copys, infografías, JSON n8n y asignación de video diario.
- Playbooks de captación directa añadidos: Ficha Google Maps Ñuñoa (`docs/GOOGLE_BUSINESS_PROFILE_NUNOA.md`) y Red de derivación interprofesional (`docs/RED_DERIVACION_CLINICA_LOCAL.md`).
- Pipeline de video vertical integrado con YouTube IA: **10 videos cortos generados en resolución 9:16 (1080x1920)** con voz chilena empática (`es-CL-CatalinaNeural`), banda sonora adaptativa y subtítulos sincronizados, listos para YouTube Shorts, Reels y TikTok con textos y comentarios fijados hacia WhatsApp y el hub móvil `/links`.
- Identidad visual unificada con el **Nuevo Logotipo Oficial de Centro Paz** (símbolo de Psicología Ψ abrazado por ramas de laurel en verde oliva y bosque): generado en formatos de alta resolución (`assets/logo/icon-profile-1024.png`, `lockup-1200.png`, `icon.svg`), integrado en la barra de navegación web (`index.html`) y aplicado a las **28 piezas gráficas completas de Instagram** (`assets/instagram/*.html` y `assets/instagram/*.png` a 1080x1350).
- Comando puente operativo implementado: `python3 -m agent.video_shorts_generator --render <id>` para compilar videos a demanda.

## Directrices Operativas Clave

- **Atención por WhatsApp:** Atendida 100% de forma exclusiva, personal y directa por **Valentina Castro Núñez** (`+56 9 6516 3893`). No se utilizan bots conversacionales ni respuestas automatizadas/prefabricadas: Valentina lidera toda la relación y triaje humano con clientes y pacientes nuevos, preservando la calidez clínica, la empatía y el secreto profesional.
- **Producción de Videos:** Se delega al pipeline automatizado de **YouTube IA** (`/Proyectos/youtube-ia`), alimentándose de los guiones clínicos en [`marketing/GUIONES_VIDEO_VERTICALES.md`](file:///Users/nigoku/Proyectos/centro-paz/marketing/GUIONES_VIDEO_VERTICALES.md).
- **Separación total de Ironcross:** Negocio clínico independiente, sin canales de WhatsApp compartidos ni cruces operativos.

## Próximo control

Monitorear el flujo de pacientes que llegan al WhatsApp de Valentina y distribuir los videos cortos generados en YouTube Shorts, Reels y TikTok siguiendo los copys de [`marketing/GUIONES_VIDEO_VERTICALES.md`](file:///Users/nigoku/Proyectos/centro-paz/marketing/GUIONES_VIDEO_VERTICALES.md).

