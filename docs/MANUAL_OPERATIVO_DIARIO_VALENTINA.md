# 🌿 Centro Paz — Manual Operativo Diario de 1 Página para Valentina Castro

Este documento resume el protocolo operativo diario en 3 pasos para gestionar las consultas de pacientes de **Centro Paz** (`www.centropaz.cl`), maximizar la tasa de agendamiento en WhatsApp y alcanzar la meta de **100 pacientes en atención activa**.

---

## 1. El Flujo Operativo Diario en 3 Pasos

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                      RUTINA DIARIA DE CAPTACIÓN & GESTIÓN DE PACIENTES                          │
└────────────────────────────────┬────────────────────────────────────────────────────────────────┘
                                 │
      ┌──────────────────────────┼──────────────────────────┐
      │                          │                          │
      ▼                          ▼                          ▼
[ 1. MAÑANA: CONTROL ]     [ 2. DÍA: WHATSAPP ]       [ 3. CIERRE: TABLERO ]
Abrir terminal y ejecutar: Responder en < 15 min      Registrar al nuevo paciente
`python3 cpaz.py` (Op. 1)  con doble horario e Isapre en el CRM (Opción 7).
```

---

## 2. Protocolo de Atención en WhatsApp (Tiempo Crítico: < 15 Minutos)

Cuando un paciente escriba desde la web (con su mensaje precargado de triaje o desde las landing pages de especialidad), responde utilizando la siguiente estructura de 3 bloques adaptada a las **4 especialidades clínicas actuales**:

### Bloque 1: Saludo y Validación Empática (Por Especialidad)

* **Estructura Base:**
  > *"Hola [Nombre] 🌿 Qué gusto saludarte. Soy Valentina Castro, psicóloga clínica de Centro Paz. Leí que buscas atención para [Ansiedad / Depresión / TLP / Psicodiagnóstico] en modalidad [Presencial en Ñuñoa / Online]. Me alegra mucho que hayas dado este paso."*

* **Plantillas Rápidas según Motivo de Consulta:**
  1. **Ansiedad y Crisis de Angustia:**
     > *"Hola [Nombre] 🌿 Qué gusto saludarte. Soy Valentina Castro, psicóloga clínica de Centro Paz. Leí tu mensaje sobre las crisis de angustia y taquicardia. Quiero transmitirte mucha tranquilidad: la ansiedad es una alarma biológica que podemos aprender a regular con herramientas somáticas y cognitivas respetuosas. Me alegra que hayas dado este paso."*
  2. **Depresión y Trastornos del Ánimo:**
     > *"Hola [Nombre] 🌿 Te saluda Valentina Castro, psicóloga clínica de Centro Paz. Comprendo profundamente lo agotador que es sostener el desánimo, el cansancio y la falta de motivación. En Centro Paz abrimos un espacio cálido, gradual y sin presiones para comprender qué está sintiendo tu cuerpo y reconstruir tu bienestar."*
  3. **Trastornos de la Personalidad (TLP / Borderline):**
     > *"Hola [Nombre] 🌿 Qué gusto saludarte, soy Valentina Castro de Centro Paz. Entiendo perfectamente la intensidad afectiva, el miedo al rechazo y lo desgastante que puede ser sentir que las emociones desbordan. Trabajamos desde un encuadre compasivo, libre de juicios y enfocado en tu autorregulación emocional y vincular."*
  4. **Evaluaciones Psicodiagnósticas e Informes Formales:**
     > *"Hola [Nombre] 🌿 Te saluda Valentina Castro, psicóloga clínica acreditada de Centro Paz. Respecto a tu consulta por la evaluación psicodiagnóstica: realizamos un proceso clínico formal y estructurado (baterías validadas en 3 a 4 sesiones) con entrega de informe formal firmado para tu psiquiatra tratante o interconsulta médica."*

### Bloque 2: Transparencia de Arancel e Isapre (Derriba el Miedo al Costo)
> *"Para tu tranquilidad, la sesión de 50 minutos tiene un valor de **$45.000 CLP** y al terminar te envío de inmediato la boleta electrónica con código de psicología clínica para que reembolses en tu Isapre ([Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres]) y Seguro Complementario. En promedio, los pacientes pagan un copago real de entre **$9.000 y $18.000 CLP** (promedio ~$12.000 CLP)."*

### Bloque 3: Cierre con Doble Alternativa de Horarios
> *"Para coordinar tu ingreso esta semana, tengo estas dos opciones disponibles:
> 1. Este **jueves a las 17:00 hrs** ([Presencial en Ñuñoa / Online])
> 2. Este **sábado a las 11:00 hrs** ([Presencial en Ñuñoa / Online])
> ¿Cuál de estos dos horarios te acomoda mejor para reservarte el espacio?"*

---

## 3. Registro en el Tablero de 100 Pacientes (CRM Clínico)

Una vez confirmada la hora:
1. Abre tu terminal y ejecuta: `python3 cpaz.py`.
2. Selecciona la opción **`7`** (*Tablero Clínico de Ingresos*).
3. Selecciona **`1`** (*Registrar nuevo paciente*) e ingresa:
   * **Alias/Iniciales:** Ej: `M. Rojas` o `Paciente #1` (confidencial, sin RUT ni datos sensibles).
   * **Especialidad:** Ansiedad, Depresión, TLP (Trastornos de la Personalidad) o Psicodiagnóstico / Evaluación Formal.
   * **Modalidad:** Presencial Ñuñoa u Online.
   * **Isapre:** Colmena, CruzBlanca, Banmédica, Consalud, etc.
   * **Estado:** `agendado` o `en_tratamiento`.

---

## 4. Enlaces Clave de la Consulta

* **Página Web Principal:** `https://www.centropaz.cl/`
* **Landing Ansiedad y Crisis de Angustia:** `https://www.centropaz.cl/ansiedad-crisis-angustia.html`
* **Landing Depresión y Trastornos del Ánimo:** `https://www.centropaz.cl/depresion-trastornos-animo.html`
* **Landing Trastornos de la Personalidad (TLP):** `https://www.centropaz.cl/trastornos-personalidad-tlp.html`
* **Landing Evaluación Psicodiagnóstica e Informes:** `https://www.centropaz.cl/evaluacion-psicodiagnostica-informes.html`
* **Landing Consulta Presencial Ñuñoa:** `https://www.centropaz.cl/psicologo-nunoa.html`
* **Landing Simulador Reembolso Isapre:** `https://www.centropaz.cl/reembolso-isapre-psicologia.html`
* **Biblioteca de 28 Guías Clínicas:** `https://www.centropaz.cl/blog/`
* **WhatsApp Oficial:** `https://wa.me/56965163893` (+56 9 6516 3893)
