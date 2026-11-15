# Estado actual — Centro Paz

**Actualizado:** 2026-11-11 (Lanzamiento CPAZ Media OS en rama `feat/cpaz-media-os` + PR #14 activo en producción)

## Función

Ecosistema digital centrado al 100% en la **Página Web ([www.centropaz.cl](https://www.centropaz.cl))** como el motor principal de posicionamiento en Google (SEO / GEO / LLM Overviews), Google Ads y conversión directa de pacientes a WhatsApp, ahora coordinado internamente en desarrollo por **CPAZ Media OS** (`media_os/`).

## CPAZ Media OS (Rama `feat/cpaz-media-os`, sin mergear ni publicar sin `AUTORIZO`)

- **Arquitectura mínima verificada ([`docs/MEDIA_OS_ARQUITECTURA_Y_COMPARATIVA.md`](docs/MEDIA_OS_ARQUITECTURA_Y_COMPARATIVA.md)):** Auditoría comparativa de OpenPost (`AGPL-3.0`), BrightBean Studio (`AGPL-3.0`), Postiz (`AGPL-3.0`, descartado por 2-8 GB RAM), Activepieces (descartado para no duplicar `n8n`), Ollama (`MIT`, integrado local), ComfyUI (`GPL-3.0`, deshabilitado en Mac 8 GB), FFmpeg (`CLI` subprocess), Remotion (`video_engine/` reutilizado), Mixpost Lite, Umami y Shlink.
- **Módulos locales implementados (`media_os/`):** firewall PII Ley 19.628 ([`media_os/privacy.py`](media_os/privacy.py)), SQLite WAL ([`media_os/storage.py`](media_os/storage.py)), inteligencia & QA clínico ([`media_os/intelligence.py`](media_os/intelligence.py)), estudio A/V `ffprobe`/`ffmpeg` ([`media_os/studio.py`](media_os/studio.py)), calendario editorial + gate `PUBLICAR <ID>` ([`media_os/calendar.py`](media_os/calendar.py)), publicadores dry-run/desacoplados ([`media_os/publishers.py`](media_os/publishers.py)), puente n8n aprobado-only ([`media_os/automation.py`](media_os/automation.py)), atribución UTM sin PII ([`media_os/attribution.py`](media_os/attribution.py)) y Dashboard Ejecutivo ([`tools/cpaz_media_os_dashboard.html`](tools/cpaz_media_os_dashboard.html)).
- **Capacidades Operativas e Interactivas Validadas:**
  - Calendario Editorial poblado con los **28 tópicos clínicos** oficiales.
  - Auditoría de **QA Clínico 28/28 PASS** (verificación de arancel $45.000 CLP, Registro SIS Nº 667344 y ausencia de afirmaciones prohibidas).
  - **Submenú interactivo en terminal** (`cpaz.py` opción `M` o `python3 -m media_os.cli`) para gestión en 1 paso: ver snapshot, poblar temas, auditar QA, aprobar (`PUBLICAR <ID>`), simular dry-run, exportar a n8n y abrir dashboard.
  - **Dashboard Ejecutivo Web Interactivo** con botones de copiado rápido (`📋 Copiar "PUBLICAR <ID>"`), buscador y filtros de estado, endpoints locales blindados (`/api/snapshot`, `/api/login`, `/api/logout`, `/api/seed`, `/api/qa-all`, `/api/approve`, `/api/publish-dryrun`, `/api/export-n8n`):
    * **Sesiones de Navegador en Cookie HttpOnly:** Autenticación de navegador gobernada 100% por cookies `HttpOnly; SameSite=Strict`, eliminando cualquier token de sesión del DOM o del alcance de JavaScript.
    * **Token CSRF Independiente:** Endpoints mutantes (`POST`) ejecutados desde el navegador exigen validación de token CSRF (`X-CSRF-Token`) generado por el servidor y enlazado a la sesión en memoria.
    * **Compatibilidad Dual CLI/API:** Soporte preservado para herramientas de línea de comandos mediante cabecera `Authorization: Bearer <master_token>`.
    * **CSP Estricto con Nonce Criptográfico:** `script-src 'self' 'nonce-{nonce}'`, eliminando `'unsafe-inline'` para anular vectores de inyección XSS.
    * **Expiración y Revocación de Sesión:** Administrador de sesiones `SessionManager` con TTL (8h) y endpoint `/api/logout` que destruye la sesión y borra la cookie.
    * **Defensa Perimetral:** Anti-CSRF (`Sec-Fetch-Site`, `Origin`, `Referer`), anti-DNS Rebinding, método CORS `OPTIONS` bloqueado (405), límite de 64 KB en payload y descarte absoluto de tokens en parámetros URL (`?token=`).
  - **Acceso Permanente y Residente Local:** Servidor loopback en `http://127.0.0.1:8765/` gestionado por `scripts/media_os_service.sh` y automatizado mediante LaunchAgent de macOS (`~/Library/LaunchAgents/cl.centropaz.media_os.plist`) con credencial segura en `~/.cpaz/media_os_token` (0600) y acceso directo `.webloc` en el escritorio para guardado en favoritos.
  - **Suite de Pruebas Automatizadas:** `pytest`: **9/9 PASS** (21 verificaciones exhaustivas de seguridad HTTP, control de acceso, rotación de nonce CSP, TTL y regresión funcional; total de **80 pruebas automatizadas** en el repositorio junto a `agent/audit_directory_consistency.py` [64/64] y `agent/test_full_suite_e2e.py` [7/7]).
  - **Integridad Criptográfica y Clínica:** Los 28 contenidos se encuentran en estado `CLINICAL_QA` con sus 28 recursos gráficos PNG verificados físicamente e indexados en [`docs/INTEGRITY_MANIFEST_PR15.json`](docs/INTEGRITY_MANIFEST_PR15.json), auditados de forma automática en [`tests/test_integrity_manifest.py`](tests/test_integrity_manifest.py).
  - **Modelo de Seguridad Local:** Perímetro blindado contra ataques de red y navegador (CSRF, DNS Rebinding, XSS); se delimita que los procesos locales ejecutados bajo el mismo UID escapan a las defensas de la capa de aplicación y dependen del aislamiento del sistema operativo.
- **Resguardo clínico e integridad:** `video_engine/public/`, `data/patient_intakes.json`, las 54 páginas HTML y cuentas externas permanecen intactos y sin publicación en vivo. Ready para revisión humana en PR #15.

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
