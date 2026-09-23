# Estado actual — Centro Paz

**Actualizado:** 2026-09-23

## Función

Ecosistema digital y motor de captación y conversión de pacientes para Centro Paz.

## Evidencia actual del sistema

- **Sincronización Git:** Árbol de trabajo limpio y sincronizado con la rama `main` de GitHub.
- **Sitio en Producción:** [www.centropaz.cl](https://www.centropaz.cl) desplegado vía GitHub Pages con certificado SSL/TLS activo (HTTP 200).
- **Blog Clínico y Posicionamiento para Motores de IA (GEO / LLM SEO):**
  - Desplegados **28 artículos clínicos exhaustivos** en `/blog/` estructurados con datos Schema.org (`MedicalWebPage`, `FAQPage`, `Article`).
  - Estándar abierto [`llms.txt`](file:///Users/nigoku/CPAZ/llms.txt) en la raíz para indexación y citación directa por modelos de lenguaje (ChatGPT, Perplexity, Claude, Gemini).
  - Archivos [`robots.txt`](file:///Users/nigoku/CPAZ/robots.txt) y [`sitemap.xml`](file:///Users/nigoku/CPAZ/sitemap.xml) optimizados y sin restricciones para agentes rastreadores.
- **Activos Visuales y Multimedia Generados:**
  - **28 infografías de Instagram:** Formato 1080x1350 PNG renderizadas y listas en `assets/instagram/`.
  - **10 videos verticales (9:16 - 1080x1920):** Con locución neuronal chilena (`es-CL-CatalinaNeural`), subtítulos sincronizados y banda sonora en `assets/videos/`.
  - **Identidad de Marca:** Logotipo vectorial oficial (Ψ con corona de laureles) integrado en cabecera web y piezas gráficas.
- **Automatización y CLI:**
  - Panel interactivo centralizado en [`cpaz.py`](file:///Users/nigoku/CPAZ/cpaz.py) (Asistente de WhatsApp, generador de guiones, scout y renderizador).
  - Motor de publicación [`agent/auto_publisher.py`](file:///Users/nigoku/CPAZ/agent/auto_publisher.py) configurado para dos franjas horarias (12:00 CLT Feed / 18:30 CLT Video/Reel).
  - Flujo de GitHub Actions en [`.github/workflows/auto_publish.yml`](file:///Users/nigoku/CPAZ/.github/workflows/auto_publish.yml).

## Directrices Operativas Clave

- **Atención por WhatsApp:** Gestionada 100% de manera directa y exclusiva por **Valentina Castro Núñez** (`+56 9 6516 3893`). No se utilizan chatbots ni automatizaciones conversacionales que deshumanicen el contacto clínico.
- **Producción de Video:** Integrada con el motor de YouTube IA para renderizar guiones adicionales a demanda.
- **Independencia Operativa:** Centro Paz opera con infraestructura y canales de comunicación completamente independientes de otros proyectos.

## Siguientes Pasos Priorizados

1. **Configuración de Credenciales de Meta (Instagram / Facebook Graph API):**
   - Cargar `META_ACCESS_TOKEN`, `META_IG_ACCOUNT_ID` y `META_FB_PAGE_ID` en GitHub Secrets para habilitar la publicación desatendida diaria del workflow.
2. **Distribución Multicanal de Videos Cortos:**
   - Publicar el lote de 10 videos verticales en YouTube Shorts, TikTok e Instagram Reels usando los copys y llamadas a la acción de `marketing/GUIONES_VIDEO_VERTICALES.md`.
3. **Verificación y Lanzamiento de Google Business Profile (Ñuñoa):**
   - Ejecutar el playbook de `docs/GOOGLE_BUSINESS_PROFILE_NUNOA.md` para capturar la demanda local de psicólogos y neurodivergencias en la comuna.
4. **Activación de Red de Derivación Interprofesional:**
   - Establecer contacto con profesionales afines (pediatras, neurólogos, centros médicos de la zona oriente) siguiendo `docs/RED_DERIVACION_CLINICA_LOCAL.md`.
5. **Monitoreo de Conversión en WhatsApp:**
   - Evaluar métricas de agendamiento y retención con Valentina Castro Núñez.

