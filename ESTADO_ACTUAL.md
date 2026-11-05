# Estado actual — Centro Paz

**Actualizado:** 2026-11-03 (Misión E2E Auditoría & Integración PR #14)

## Función

Ecosistema digital centrado al 100% en la **Página Web ([www.centropaz.cl](https://www.centropaz.cl))** como el motor principal de posicionamiento en Google (SEO / GEO / LLM Overviews), Google Ads y conversión directa de pacientes a WhatsApp.

## Evidencia actual del sistema y Auditoría PR #14

- **Pull Request #14:** [feat(seo-local): triangulación en Google Maps, directorios médicos y red de psiquiatras](https://github.com/nicohugof/centro-paz/pull/14)
  - **Rama de trabajo:** `feature/nap-consistency-docs`
  - **Estado en GitHub:** `mergeable: MERGEABLE`, `mergeStateStatus: CLEAN` (0 conflictos pendientes).
  - **Commit HEAD verificado:** `2d637cdf201063f5767ae138777ce93c7f7d7cd4`
  - **Respaldo preventivo:** Rama local `backup/pre-integration-20261103-152841` (preservando SHA `607a9d5`).
- **Estado de `main`:**
  - **SHA en origin/main:** `04556a3f8758c0b11e6973ed561f7778ca2f83dd` (sincronización automatizada de blog).
  - Integrado limpiamente en `feature/nap-consistency-docs` mediante commit `d381fbe`.
- **Resolución Técnica & Prevención de Regresiones:**
  - Se resolvió el conflicto en `llms.txt`, consolidando la dirección física unificada (`Salvador 2302, Ñuñoa`), arancel `$45.000 CLP`, Registro Oficial SIS Nº 667344 y el catálogo de especialidades.
  - Se actualizaron las plantillas generadoras en `agent/blog_generator.py` para asegurar que futuras ejecuciones desatendidas de GitHub Actions mantengan la coherencia NAP, el Registro SIS Nº 667344 y el enlace a `sanarte.html` en las 54 páginas.
- **Resultados de Suites de Pruebas Automatizadas:**
  - `agent/audit_directory_consistency.py`: **64/64 pruebas superadas (100.0%)**.
    - Coherencia de Nombre, Dirección (`Salvador 2302, Ñuñoa`) y Teléfono (`+56 9 6516 3893`).
    - Certificación del Registro Oficial SIS Nº 667344 en todos los documentos y herramientas.
    - Cero aranceles obsoletos en conflicto; $45.000 CLP certificado.
    - Herramientas `tools/asistente_google_maps.html` y `tools/registro_directorios.html` operativas y enlazadas.
  - `agent/test_full_suite_e2e.py`: **7/7 pruebas superadas (100.0%)**.
    - 54/54 páginas operativas.
    - 23/23 productos reales de San_Arte verificados.
    - 100% enlaces WhatsApp unificados.
    - 54/54 páginas con respaldo Registro SIS Nº 667344 y `og:image`.
    - 0 enlaces rotos detectados.

## Estado del Despliegue & Bloqueo Detectado

- **Mecanismo de Despliegue:** GitHub Pages en modo legado (`build_type: legacy`), configurado con fuente en rama `main` raíz (`/`).
- **Bloqueo Detectado:** En la arquitectura de GitHub Pages, cualquier merge o push directo a la rama `main` desencadena automáticamente una compilación y despliegue inmediato en producción sobre el dominio `www.centropaz.cl`.
- **Acción Tomada en Cumplimiento de la Regla de Seguridad:**
  - Dado que la misión prohíbe taxativamente desplegar a producción (*"NO se autoriza desplegar producción"* y *"Si existe despliegue automático desde main, impedirlo de forma segura y verificable antes del merge. Si no es posible garantizarlo, detener únicamente el merge y documentar el bloqueo"*), se detuvo exclusivamente el paso final de merge a `main`.
  - La rama `feature/nap-consistency-docs` queda totalmente auditada, probada, sin conflictos y lista para merge en 1 clic en cuanto se autorice formalmente el despliegue a producción.

## Siguientes Pasos Priorizados

1. **Aprobación de Despliegue a Producción:**
   - Autorizar la integración a `main` sabiendo que actualizará `www.centropaz.cl` en producción con los nuevos archivos de herramientas y la consistencia NAP.
2. **Uso Operativo del Asistente Google Maps:**
   - Abrir localmente `tools/asistente_google_maps.html` para copiar la ficha de Google Business Profile y gestionar reseñas.
3. **Triangulación en Directorios Médicos:**
   - Utilizar `tools/registro_directorios.html` para actualizar los perfiles en Doctoralia y Encuadrado.
