# Estado actual — Centro Paz

**Actualizado:** 2026-11-11 (Lanzamiento CPAZ Media OS en rama `feat/cpaz-media-os` + PR #14 activo en producción)

## Función

Ecosistema digital centrado al 100% en la **Página Web ([www.centropaz.cl](https://www.centropaz.cl))** como el motor principal de posicionamiento en Google (SEO / GEO / LLM Overviews), Google Ads y conversión directa de pacientes a WhatsApp, ahora coordinado internamente en desarrollo por **CPAZ Media OS** (`media_os/`).

## CPAZ Media OS (Rama `feat/cpaz-media-os`, sin mergear ni publicar sin `AUTORIZO`)

- **Arquitectura mínima verificada ([`docs/MEDIA_OS_ARQUITECTURA_Y_COMPARATIVA.md`](docs/MEDIA_OS_ARQUITECTURA_Y_COMPARATIVA.md)):** Auditoría comparativa de OpenPost (`AGPL-3.0`), BrightBean Studio (`AGPL-3.0`), Postiz (`AGPL-3.0`, descartado por 2-8 GB RAM), Activepieces (descartado para no duplicar `n8n`), Ollama (`MIT`, integrado local), ComfyUI (`GPL-3.0`, deshabilitado en Mac 8 GB), FFmpeg (`CLI` subprocess), Remotion (`video_engine/` reutilizado), Mixpost Lite, Umami y Shlink.
- **Módulos locales implementados (`media_os/`):** firewall PII Ley 19.628 ([`media_os/privacy.py`](media_os/privacy.py)), SQLite WAL ([`media_os/storage.py`](media_os/storage.py)), inteligencia & QA clínico ([`media_os/intelligence.py`](media_os/intelligence.py)), estudio A/V `ffprobe`/`ffmpeg` ([`media_os/studio.py`](media_os/studio.py)), calendario editorial + gate `PUBLICAR <ID>` ([`media_os/calendar.py`](media_os/calendar.py)), publicadores dry-run/desacoplados ([`media_os/publishers.py`](media_os/publishers.py)), puente n8n aprobado-only ([`media_os/automation.py`](media_os/automation.py)), atribución UTM sin PII ([`media_os/attribution.py`](media_os/attribution.py)) y Dashboard Ejecutivo ([`tools/cpaz_media_os_dashboard.html`](tools/cpaz_media_os_dashboard.html)).
- **Resguardo clínico e integridad:** `video_engine/public/`, `data/patient_intakes.json`, las 54 páginas HTML y cuentas externas permanecen intactos y sin publicación en vivo.

## Evidencia actual del sistema y Cierre de PR #14

- **Pull Request #14:** [feat(seo-local): triangulación en Google Maps, directorios médicos y red de psiquiatras](https://github.com/nicohugof/centro-paz/pull/14)
  - **Estado:** **MERGEADO** exitosamente en `main`.
  - **Commit de integración en main:** `0b525f1ac7868e73edf960aa01cb52b5ade27350`
  - **Rama de origen:** `feature/nap-consistency-docs`
  - **Respaldo preventivo:** Rama local `backup/pre-integration-20261103-152841` (preservando SHA `607a9d5`).
- **Estado de `main`:**
  - Árbol de trabajo sincronizado con `origin/main`.
  - Cero conflictos, 100% limpio y homologado.
- **Resultados de Suites de Pruebas Automatizadas en `main`:**
  - `agent/audit_directory_consistency.py`: **64/64 pruebas superadas (100.0%)**.
    - Coherencia NAP: Nombre ("Centro Paz" + "Valentina Castro"), Dirección (`Salvador 2302, Ñuñoa`) y Teléfono (`+56 9 6516 3893`).
    - Certificación del Registro Oficial SIS Nº 667344 en todos los documentos y herramientas.
    - Arancel unificado de $45.000 CLP sin discrepancias.
    - Herramientas `tools/asistente_google_maps.html` y `tools/registro_directorios.html` operativas.
  - `agent/test_full_suite_e2e.py`: **7/7 pruebas superadas (100.0%)**.
    - 54/54 páginas operativas.
    - 23/23 productos reales de San_Arte verificados.
    - 100% de enlaces WhatsApp unificados a +56 9 6516 3893.
    - 54/54 páginas con respaldo Registro SIS Nº 667344 y `og:image`.
    - 0 enlaces rotos detectados.
- **Despliegue a Producción:**
  - Compilación automática en curso y completada en GitHub Pages para el dominio [www.centropaz.cl](https://www.centropaz.cl).

## Siguientes Pasos Priorizados

1. **Uso Operativo del Asistente Google Maps:**
   - Abrir localmente `tools/asistente_google_maps.html` para copiar la ficha de Google Business Profile y gestionar reseñas de pacientes por WhatsApp.
2. **Triangulación en Directorios Médicos:**
   - Utilizar `tools/registro_directorios.html` para verificar y sincronizar los perfiles de Valentina en Doctoralia, Encuadrado y RedSalud / SaludVitale.
3. **Campaña de Derivación Psiquiátrica:**
   - Utilizar `docs/KIT_DERIVACION_PSIQUIATRAS_SANTIAGO.md` y `docs/PLANTILLAS_CONTACTO_PSIQUIATRAS.md` para iniciar contacto con psiquiatras del sector oriente (Ñuñoa, Providencia, Las Condes).
