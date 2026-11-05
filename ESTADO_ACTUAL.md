# Estado actual — Centro Paz

**Actualizado:** 2026-11-05 (PR #14 Integrado y Desplegado en Producción)

## Función

Ecosistema digital centrado al 100% en la **Página Web ([www.centropaz.cl](https://www.centropaz.cl))** como el motor principal de posicionamiento en Google (SEO / GEO / LLM Overviews), Google Ads y conversión directa de pacientes a WhatsApp.

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
