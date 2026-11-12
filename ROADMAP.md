# Roadmap — Centro Paz

**Actualizado:** 2026-11-11 · Lanzamiento CPAZ Media OS (rama `feat/cpaz-media-os`).

## Objetivo

Sitio y contenido orgánico para captación ética, con revisión clínica humana antes de material público y atribución sin PII.

## Estado real

Activos reutilizados (`28` tópicos/infografías HTML+PNG, `11` videos MP4, Remotion) orquestados localmente por `media_os/` (SQLite WAL, Ollama local MIT, FFmpeg CLI, gate `PUBLICAR <ID>`, exportador n8n aprobado-only, atribución UTM y Dashboard Ejecutivo en `tools/cpaz_media_os_dashboard.html`). Se preserva `video_engine/public/` sin alteraciones y no hay publicación automática activa sin `AUTORIZO`.

## Pasos

1. **P0 (Completado en rama):** inventariar activos, auditar stack OSS (OpenPost/BrightBean/Postiz/Activepieces/Ollama/ComfyUI/FFmpeg) y construir núcleo local `media_os/` + suite E2E preservando `video_engine/public/` y `data/patient_intakes.json`.
2. **P1 (Completado en simulación dry-run):** piloto local E2E (`brief -> QA clínico -> aprobación PUBLICAR <ID> -> schedule -> puente n8n -> dry-run -> atribución UTM -> Dashboard`). Pendiente `AUTORIZO` para piloto en cuenta real o PR hacia `main`.
3. **P2:** calendario operativo semanal tras aprobación humana por lote (`PUBLICAR <ID>`).
4. **P3:** importar métricas reales externas (Meta Insights / Umami / GA4 sin PII) y conectar webhook n8n en Oracle previa medición de RAM y `AUTORIZO`.

El WhatsApp clínico es atención humana: Nicola OS no responde pacientes ni automatiza conversaciones de salud.

Ver [HANDOFF.md](HANDOFF.md).
