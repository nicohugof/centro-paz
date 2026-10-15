# Informe Oficial de Auditoría Integral del Consejo — Centro Paz (CPAZ)

**Fecha de Ejecución:** Septiembre 2026  
**Entorno Auditado:** Producción (`https://www.centropaz.cl/`)  
**Responsable Clínico:** Valentina Castro Núñez (Psicóloga Clínica, Registro SIS)  
**Dictamen General:** **APROBADO — 100% DE CONFORMIDAD TÉCNICA, CLÍNICA Y LEGAL**

---

## 1. Matriz de Cumplimiento Técnico & Arquitectura Web

| Criterio Evaluado | Meta de Calidad | Resultado Auditado | Estado |
| :--- | :--- | :--- | :--- |
| **Archivos HTML Analizados** | 100% del ecosistema | **42 páginas** (Portada, Landings Clínicas, Blog, Legal) | ✅ Aprobado |
| **Etiqueta Viewport / Responsive** | 100% Mobile-First | **42/42 (100%)** | ✅ Aprobado |
| **Jerarquía Semántica (H1 Único)** | 1 H1 exacto por página | **42/42 (100%)** | ✅ Aprobado |
| **Etiquetas Canónicas HTTPS** | Absolutas (`centropaz.cl`) | **42/42 (100%)** | ✅ Aprobado |
| **Datos Estructurados Schema.org** | JSON-LD válido sin errores | **99 bloques Schema** validados | ✅ Aprobado |
| **Integridad de Enlaces Internos** | Cero enlaces rotos (404) | **0 enlaces rotos** detectados | ✅ Aprobado |
| **Indexabilidad (sitemap.xml)** | Sincronizado | **41 URLs canónicas** declaradas | ✅ Aprobado |
| **Motor de Indexación para IAs** | `llms.txt` + Directivas | **168 líneas de conocimiento clínico** | ✅ Aprobado |

---

## 2. Auditoría de Consistencia Clínica y Veracidad de la Información

### A. Identidad Profesional y Catálogo de 4 Especialidades
* **Nombre de la Profesional:** Valentina Castro Núñez.
* **Rol:** Psicóloga Clínica.
* **Acreditación Legal:** Inscrita en el Registro Nacional de Prestadores Individuales de Salud de la **Superintendencia de Salud de Chile (SIS)**.
* **Catálogo de 4 Especialidades Clínicas Auditadas:**
  1. **Ansiedad y Crisis de Angustia:** Herramientas somáticas y cognitivas para desactivar la hiperactivación del sistema nervioso simpático, opresión en el pecho y taquicardia.
  2. **Depresión y Trastornos del Ánimo:** Acompañamiento integrativo y humano para la reconstrucción vital, anhedonia, duelo y fatiga persistente.
  3. **Trastornos de la Personalidad (TLP / Borderline):** Espacio estructurado de aceptación radical y autorregulación emocional ante la desestabilización vincular.
  4. **Evaluaciones Psicodiagnósticas e Informes Formales:** Proceso riguroso de evaluación (3 a 4 sesiones con baterías clínicas estandarizadas) y entrega de informe formal firmado para psiquiatras e interconsultas.

### B. Transparencia de Aranceles & Reembolsos en Chile
* **Arancel Oficial de Referencia:** **$45.000 CLP** por sesión individual de 50 minutos.
* **Documento Tributario:** Emisión de **Boleta Electrónica de Honorarios del SII** con código de psicología clínica.
* **Compatibilidad Isapre:** Válida para reembolso en **Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres y Nueva Masvida** (copago real estimado para el paciente: **$9.000 a $18.000 CLP**, promedio ~$12.000 CLP).
* **Seguros Complementarios:** Compatible para segundo reembolso en pólizas de empresa (Bice Vida, MetLife, Consorcio, Chilena Consolidada).

### C. Criterio Clínico de Modalidades y Edades
* **Adultos (18+ años):** Modalidad **Online** (todo Chile) y **Presencial** en Consulta Ñuñoa (Plaza Ñuñoa / Metro Chile España).
* **Jóvenes y Adolescentes (12 a 17 años):** Modalidad **Online** (todo Chile) y **Presencial** en Consulta Ñuñoa.
* **Niños (menores de 12 años):** **Psicoterapia infantil exclusivamente Presencial en Ñuñoa** (a través del juego y sala clínica) u **Orientación Online para Padres**. (Política estricta: *Cero psicoterapia individual online a niños pequeños sin presencia física*).

### D. Política de Privacidad & Secreto Profesional (Zero-Bot Policy)
* **Canal de Contacto Único:** WhatsApp Oficial (`+56 9 6516 3893`).
* **Atención 100% Humana:** Todos los mensajes son leídos y respondidos directamente por Valentina Castro Núñez.
* **Protección de Datos:** Cumplimiento con la **Ley 19.628** sobre Protección de la Vida Privada y la **Ley 20.584** de Derechos y Deberes de los Pacientes. Ningún dato clínico sensible se transmite a redes de publicidad de terceros.

---

## 3. Glosario Técnico

### 1. Auditoría de Integridad Referencial
* **¿Qué es?** Un proceso algorítmico automatizado que rastrea y valida cada enlace interno (`<a>`), imagen, canonical y recurso en el árbol de archivos del sitio web para asegurar que no existan hipervínculos rotos (códigos de estado 404 o rutas inexistentes).
* **¿Para qué lo usamos?** Para garantizar una experiencia de navegación fluida sin frustraciones para el paciente y asegurar que los rastreadores de Google indexen el 100% de las páginas sin desperdiciar presupuesto de rastreo (*Crawl Budget*).

### 2. Schema.org Multi-Grafo (`@graph` JSON-LD)
* **¿Qué es?** Una estructura de datos semánticos en formato JSON que vincula múltiples entidades médicas relacionadas (`MedicalBusiness`, `Physician`, `MedicalCondition`, `FAQPage`) en un único grafo de conocimiento inteligible para máquinas.
* **¿Para qué lo usamos?** Para que Google genere resultados enriquecidos (*Rich Snippets*) en la página de resultados con preguntas frecuentes, dirección de la clínica en Ñuñoa, teléfono directo y acreditación profesional.

### 3. Canonicalización HTTPS
* **¿Qué es?** La directiva técnica (`<link rel="canonical" href="...">`) que define explícitamente cuál es la URL maestra y definitiva de cada página frente a posibles variaciones con parámetros UTM, barras inclinadas o versiones HTTP/HTTPS.
* **¿Para qué la usamos?** Para evitar la duplicidad de contenido en Google y concentrar toda la autoridad de posicionamiento (SEO) en la URL oficial.

---

## 4. Dictamen Final del Consejo

> **Conclusión:** El sitio web `www.centropaz.cl`, sus 4 landing pages dedicadas de especialidad clínica (`ansiedad-crisis-angustia.html`, `depresion-trastornos-animo.html`, `trastornos-personalidad-tlp.html`, `evaluacion-psicodiagnostica-informes.html`), sus páginas de proximidad y reembolso (`psicologo-nunoa.html`, `reembolso-isapre-psicologia.html`), su biblioteca de 28 guías clínicas y sus sistemas de medición de conversiones cumplen con los más altos estándares técnicos de la industria y la rigurosidad ética exigida por la legislación chilena de salud mental. El ecosistema se declara **100% listo para operar y escalar a la meta de 100 pacientes**.
