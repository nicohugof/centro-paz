# 🌐 Estrategia de Adquisición Omnicanal — Centro Paz (CPAZ)

Este documento define la arquitectura de contenidos para maximizar el tráfico orgánico y derivación de pacientes hacia WhatsApp (**`+56 9 6516 3893`**) a través de múltiples plataformas:

1. **Instagram (`@centropaz.cl`)**
2. **TikTok (`@centropaz.cl`)**
3. **Facebook (`Centro Paz`)**
4. **Threads (`@centropaz.cl`) & X (Twitter)**

---

## 🎯 Embudo Omnicanal de Alta Conversión

```text
┌────────────────────────────────────────────────────────┐
│                   DESCUBRIMIENTO (TOFU)                 │
│   • TikTok & Reels: Videos de 30-40s (Ganchos virales) │
│   • Threads / X: Micro-hilos de debate clínico          │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│                  VALIDACIÓN CLÍNICA (MOFU)             │
│   • Instagram / Facebook Feed: Infografías (1080x1350)  │
│   • Artículos y casos clínicos sin testimonios falsos  │
│   • Simulador de reembolsos Isapre en www.centropaz.cl │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│                    CONVERSIÓN (BOFU)                   │
│   • Stories (09:00 y 21:00) con llamado directo        │
│   • Descarga de Guía de 7 Claves en PDF por WhatsApp   │
│   • Cierre personalizado con Valentina en WhatsApp     │
└────────────────────────────────────────────────────────┘
```

---

## 📡 Endpoints JSON Públicos para Automatización (n8n / Webhooks)

* **Matriz Omnicanal Completa:** [`https://www.centropaz.cl/multiplatform_content_n8n.json`](https://www.centropaz.cl/multiplatform_content_n8n.json)
* **Parrilla Semanal de 28 slots:** [`https://www.centropaz.cl/parrilla_semanal_n8n.json`](https://www.centropaz.cl/parrilla_semanal_n8n.json)
* **Lead Magnet PDF:** [`https://www.centropaz.cl/guia_7_claves_regulacion_centro_paz.pdf`](https://www.centropaz.cl/guia_7_claves_regulacion_centro_paz.pdf)

---

## 🎬 Formatos por Canal

### 1. TikTok & Instagram Reels (Short-form Video)
* **Objetivo:** Alcance masivo orgánico en personas adultas con sospecha de TDAH/TEA y padres.
* **Estructura del guion (30-40s):**
  - **0-3s (Gancho visual + auditivo):** Pregunta que activa la identificación (ej. *"¿Por qué procrastinas tareas simples si de verdad quieres hacerlas?"*).
  - **3-25s (Desarrollo clínico):** Explicación de la parálisis de la función ejecutiva o la sobrecarga sensorial.
  - **25-35s (CTA claro):** *"En Centro Paz te acompañamos. Link a WhatsApp en nuestra biografía."*

### 2. Threads & X (Twitter)
* **Objetivo:** Posicionamiento como referentes clínicos en neurodivergencias e Isapres en Chile.
* **Formato:** Micro-hilos de 3 publicaciones (Problema ➡️ Explicación neuroafirmativa ➡️ Enlace a WhatsApp/Web).

### 3. Facebook Page & Comunidades
* **Objetivo:** Tráfico calificado de padres y adultos en grupos de salud mental y colegios.
* **Formato:** Post narrativo extenso con emojis clínicos + llamado a descargar la Guía PDF por WhatsApp.

---

## 🛠️ Comandos del Agente

```bash
# Ver la matriz omnicanal en consola:
python3 -m agent.marketing_agent --multiplatform

# Ver todos los guiones de video para TikTok/Reels:
python3 -m agent.marketing_agent --reels

# Exportar todos los JSONs actualizados para n8n:
python3 -m agent.marketing_agent --export-json
```
