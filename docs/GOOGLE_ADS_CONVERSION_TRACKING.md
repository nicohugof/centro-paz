# Centro Paz (CPAZ) — Manual de Medición de Conversiones & Google Ads

Este documento establece la arquitectura, taxonomía de eventos y procedimiento técnico paso a paso para medir conversiones, optimizar pujas en **Google Ads Search** y registrar la atribución exacta de pacientes captados a través de `www.centropaz.cl`.

---

## 1. Arquitectura de Medición y Flujo de Datos

```
                                  [ Paciente en Google Search ]
                                                │
                                                ▼ (Clic en Anuncio / Búsqueda Orgánica)
                                  [ www.centropaz.cl (Web 2.0) ]
                                                │
          ┌─────────────────────────────────────┴─────────────────────────────────────┐
          │                                                                           │
          ▼ (Interacciones en Web)                                                    ▼ (Clic en WhatsApp)
  [ Eventos de Comportamiento ]                                                [ Evento Principal: generate_lead ]
  • complete_triage                                                            • Valor: $45.000 CLP
  • calculate_reimbursement                                                    • Destino: +56 9 6516 3893
  • filter_library                                                             • Atención: Valentina Castro (100% Humana)
          │                                                                           │
          └─────────────────────────────────────┬─────────────────────────────────────┘
                                                │
                                                ▼
                                    [ window.dataLayer / gtag ]
                                                │
                      ┌─────────────────────────┴─────────────────────────┐
                      │                                                   │
                      ▼                                                   ▼
         [ Google Analytics 4 (GA4) ]                           [ Google Ads Tag (AW-) ]
         • Eventos de sesión y engagement                       • Conversión Primaria: Clic WhatsApp
         • Audiencias de remarketing                            • Optimización Smart Bidding (Target CPA / Max Conversions)
```

---

## 2. Taxonomía de Eventos Técnicos Implementados en `app.js`

La capa de aplicación cuenta con un despachador unificado (`trackCPAZEvent`) que envía los eventos en paralelo a `window.dataLayer` y a `gtag()`:

### A. Conversión Principal (Macro-Conversión)

| Nombre del Evento | Parámetros Enviados | Criterio de Activación | Rol en Google Ads |
| :--- | :--- | :--- | :--- |
| `generate_lead` | `lead_type: "whatsapp"`<br>`lead_source: string`<br>`element_text: string`<br>`value: 45000`<br>`currency: "CLP"` | Clic en cualquier botón que dirija a WhatsApp (+56 9 6516 3893). | **Acción Principal de Conversión** (Bidding). |

### B. Micro-Conversiones (Intención y Engagement)

| Nombre del Evento | Parámetros Enviados | Criterio de Activación | Rol en Analítica |
| :--- | :--- | :--- | :--- |
| `complete_triage` | `triage_target`<br>`triage_reason`<br>`triage_modality`<br>`triage_schedule` | Paciente completa los 3 pasos del orientador y ve la recomendación clínica. | Medición de fricción del embudo y calificación de intención. |
| `calculate_reimbursement` | `isapre`<br>`with_insurance`<br>`estimated_copay`<br>`estimated_reimburse` | Paciente selecciona su Isapre o activa Seguro Complementario. | Medición de interés económico y viabilidad de arancel. |

---

## 3. Configuración Paso a Paso en Plataformas de Google

### Paso 1: Instalación de Etiquetas en `index.html` y Blog

Inserta tu identificador de Google Analytics 4 (`G-XXXXXXXXXX`) y Google Ads (`AW-XXXXXXXXXX`) dentro de la etiqueta `<head>`:

```html
<!-- Google Tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  // Configuración GA4
  gtag('config', 'G-XXXXXXXXXX');
  // Configuración Google Ads (Reemplazar con tu ID de conversión)
  gtag('config', 'AW-XXXXXXXXXX');
</script>
```

---

### Paso 2: Marcar `generate_lead` como Conversión en Google Analytics 4 (GA4)

1. Ingresa a [analytics.google.com](https://analytics.google.com/).
2. Ve a **Administrador** (ícono de engranaje abajo a la izquierda) > **Visualización de datos** > **Eventos**.
3. En la lista de eventos, busca `generate_lead` (aparecerá tras el primer clic en la web, o puedes crearlo manualmente con el botón *Crear evento*).
4. Activa el interruptor **Marcar como conversión**.

---

### Paso 3: Vincular GA4 con Google Ads

1. En GA4, ve a **Administrador** > **Vinculaciones de productos** > **Vinculaciones de Google Ads**.
2. Haz clic en **Vincular** y selecciona tu cuenta de Google Ads (número de 10 dígitos).
3. Habilita las opciones:
   - *Habilitar la publicidad personalizada*.
   - *Habilitar el etiquetado automático (Auto-tagging)*.

---

### Paso 4: Importar la Conversión en Google Ads

1. Ingresa a [ads.google.com](https://ads.google.com/).
2. Ve a **Objetivos** > **Conversiones** > **Resumen**.
3. Haz clic en **Nueva acción de conversión**.
4. Selecciona **Importar** > **Propiedades de Google Analytics (GA4)** > **Web**.
5. Selecciona el evento `generate_lead` y haz clic en **Importar y continuar**.
6. Configura la acción importada:
   - **Objetivo y optimización de la acción:** Contacto / Cliente potencial (Acción Principal para optimización de pujas).
   - **Valor:** Asignar $45.000 CLP (o el valor de arancel de sesión).
   - **Recuento:** *Una sola* (si un mismo usuario hace clic 3 veces en WhatsApp durante la misma sesión, se cuenta como 1 lead único).
   - **Ventana de conversión post-clic:** 30 días.
   - **Modelo de atribución:** Basado en datos (*Data-driven*).

---

### Paso 5: Verificación y QA (Control de Calidad)

1. Abre `https://www.centropaz.cl/?debug=true` en Google Chrome.
2. Abre la consola de desarrollo (`F12` o `Cmd + Option + J`).
3. Haz clic en el botón de WhatsApp del Hero, del Orientador o de la Calculadora de Isapre.
4. En la consola verás el log en tiempo real:
   ```json
   [CPAZ Analytics] Event: generate_lead {
     event: "generate_lead",
     lead_type: "whatsapp",
     lead_source: "hero",
     element_text: "Conversar por WhatsApp",
     value: 45000,
     currency: "CLP"
   }
   ```
5. En Google Analytics 4, ve a **Administrador** > **DebugView** para confirmar la recepción en vivo del evento.

---

## 4. Glosario Técnico

### 1. Google Tag Manager (GTM)
* **¿Qué es?** Un sistema de gestión de etiquetas que permite desplegar, actualizar y gestionar fragmentos de código JavaScript (etiquetas de analítica, píxeles de conversión y scripts de seguimiento) desde una interfaz web sin requerir modificaciones continuas en el código fuente del servidor o repositorio.
* **¿Para qué lo usamos?** Para centralizar el envío de eventos de la web hacia múltiples plataformas (Google Ads, GA4, Meta) de forma modular, ordenada y sin alterar la lógica de negocio ni sobrecargar el tiempo de carga del sitio.

### 2. Google Analytics 4 (GA4)
* **¿Qué es?** La plataforma de medición y analítica web de Google basada íntegramente en un modelo de datos orientado a eventos y parámetros (a diferencia del antiguo Universal Analytics basado en sesiones e hits).
* **¿Para qué lo usamos?** Para entender el comportamiento y procedencia de los usuarios en `centropaz.cl`: qué canales traen más tráfico, qué artículos clínicos se leen por más tiempo, cómo interactúan con el orientador y cuántos visitantes terminan iniciando contacto en WhatsApp.

### 3. DataLayer (Capa de Datos)
* **¿Qué es?** Un objeto estructurado en memoria de JavaScript (`window.dataLayer = []`) que funciona como canal intermediario seguro entre la aplicación web y las herramientas de medición. Almacena pares clave-valor sobre el contexto del usuario y las acciones que ejecuta.
* **¿Para qué lo usamos?** Para desacoplar el diseño visual del tracking. Si modificamos un botón o cambiamos el texto, los eventos de conversión continúan disparándose de forma robusta y confiable a través del objeto `dataLayer`.

### 4. Smart Bidding (Pujas Inteligentes)
* **¿Qué es?** Un subconjunto de estrategias de puja automatizadas de Google Ads que utilizan algoritmos de aprendizaje automático (*machine learning*) para optimizar las ofertas en cada subasta individual en tiempo real (por ejemplo, *Maximizar conversiones* o *CPA objetivo*).
* **¿Para qué lo usamos?** Para que el algoritmo de Google Ads priorice mostrar los anuncios a personas que buscan psicólogo en Ñuñoa o TDAH y que poseen mayor probabilidad real de hacer clic en WhatsApp y agendar sesión, optimizando el presupuesto publicitario.

### 5. Conversiones Mejoradas (Enhanced Conversions)
* **¿Qué es?** Una función de Google Ads que complementa las etiquetas de conversión tradicionales capturando datos de primera parte generados por el usuario de forma encriptada (hashing unidireccional SHA-256) para recuperar conversiones que no pudieron medirse mediante cookies de terceros.
* **¿Para qué lo usamos?** Para proteger la exactitud de los informes de rendimiento ante bloqueadores de anuncios o restricciones de privacidad de navegadores como Safari (ITP).

---

## 5. Política de Privacidad & Criterio Ético en Salud Mental

1. **Privacidad Médica Rigurosa:** Ningún dato clínico sensible (motivo de consulta detallado, antecedentes de salud, diagnósticos previos) es enviado a Google ni a terceros.
2. **Eventos Agregados:** Los eventos de analítica solo registran categorías generales de interés (`adulto`, `infantil`, `isapre`) y el hecho técnico de hacer clic hacia WhatsApp.
3. **Conversación 100% Humana:** Al llegar a WhatsApp, el paciente entra en un canal privado de atención directa con la profesional **Valentina Castro Núñez**, resguardando el secreto profesional y la ética clínica.
