# Guía de Indexación Gratuita Inmediata en Google Search Console y Bing

Este manual describe el procedimiento exacto paso a paso (100% gratuito, sin inversión publicitaria) para que Google y Bing indexen las **41 URLs canónicas** de `centropaz.cl` (incluyendo las 4 landing pages de especialidades clínicas, páginas locales, simulador de reembolso y las 28 guías clínicas) en menos de 24 a 48 horas.

---

## 1. Verificación de Propiedad en Google Search Console (GSC)

Google Search Console es la herramienta oficial de Google para monitorear el posicionamiento orgánico y enviar el mapa del sitio.

### Paso 1: Acceso a Google Search Console
1. Ingresa a: [search.google.com/search-console](https://search.google.com/search-console).
2. Inicia sesión con la cuenta de Google de Centro Paz (`contacto.centropaz@gmail.com`).

### Paso 2: Añadir Propiedad de Dominio
1. En el panel principal, selecciona **Añadir propiedad**.
2. Selecciona la opción de la izquierda: **Prefijo de la URL**.
3. Escribe exactamente: `https://www.centropaz.cl/` y haz clic en **Continuar**.

### Paso 3: Método de Verificación Recomendado (Etiqueta HTML o Google Analytics)
* **Si usas Google Analytics 4:** Si ya tienes acceso a la cuenta de GA4 asociada a ese correo, la verificación se completará automáticamente en 1 segundo con un clic.
* **Si usas Etiqueta HTML:**
  1. Copia el código meta que entrega Google: `<meta name="google-site-verification" content="TU_CODIGO_AQUI" />`.
  2. Pégalo en el `<head>` de `index.html` (o solicita que lo agreguemos al repositorio).
  3. Haz clic en **Verificar**.

---

## 2. Envío del Sitemap XML (Indexación de 41 URLs Canónicas)

Una vez verificada la propiedad:
1. En el menú lateral izquierdo de Google Search Console, haz clic en **Sitemaps** (bajo la sección *Indexación*).
2. En el campo *"Añadir un nuevo sitemap"*, escribe: `sitemap.xml`.
3. La URL completa quedará: `https://www.centropaz.cl/sitemap.xml`.
4. Haz clic en **Enviar**.
5. Verás el estado en verde: **Correcto** (Google leerá las 41 URLs del sitio, incluyendo las 4 landing pages de especialidades clínicas, las páginas de proximidad y reembolso, y los 28 artículos de blog).

---

## 3. Solicitud de Indexación Prioritaria (Inspección de URLs de Alta Intención)

Para que las páginas más importantes y de mayor conversión aparezcan en los resultados de Google hoy mismo sin esperar el ciclo regular de rastreo:

1. En la barra superior de búsqueda de Search Console (*"Inspeccionar cualquier URL de https://www.centropaz.cl/"*), pega una por una las siguientes URLs clave del nuevo catálogo clínico:
   * `https://www.centropaz.cl/` (Portada institucional y triaje)
   * `https://www.centropaz.cl/ansiedad-crisis-angustia.html` (Landing: Ansiedad y Crisis de Angustia)
   * `https://www.centropaz.cl/depresion-trastornos-animo.html` (Landing: Depresión y Trastornos del Ánimo)
   * `https://www.centropaz.cl/trastornos-personalidad-tlp.html` (Landing: Trastornos de la Personalidad / TLP)
   * `https://www.centropaz.cl/evaluacion-psicodiagnostica-informes.html` (Landing: Evaluación Psicodiagnóstica e Informes)
   * `https://www.centropaz.cl/psicologo-nunoa.html` (Landing Local: Consulta Ñuñoa)
   * `https://www.centropaz.cl/reembolso-isapre-psicologia.html` (Simulador de Reembolso Isapre)
   * `https://www.centropaz.cl/blog/` (Biblioteca de 28 Guías Clínicas)
2. Presiona Enter.
3. Haz clic en el botón blanco **Solicitar indexación**.
4. Repite el proceso con estas 8 URLs principales. Googlebot las pondrá en su cola de prioridad máxima.

---

## 4. Indexación en Bing Webmaster Tools & Red IndexNow (Bing, Copilot, Perplexity)

Microsoft Bing alimenta los motores de búsqueda de Windows y la IA de Microsoft Copilot:
1. Ingresa a: [bing.com/webmasters](https://www.bing.com/webmasters).
2. Haz clic en **Comenzar** e inicia sesión con Google.
3. Selecciona **Importar desde Google Search Console** (se sincroniza en 1 clic sin configuraciones adicionales).
4. El sitemap se importará automáticamente con las 41 URLs.
5. **Automatización IndexNow en Centro Paz:** Ejecutar `python3 cpaz.py` (Opción 1) o `python3 agent/instant_search_indexer.py` para notificar en lote las 41 URLs instantáneamente a la red global de IndexNow (Bing, Yandex, Perplexity y Copilot).

---

## 5. Glosario Técnico

### 1. Google Search Console (GSC)
* **¿Qué es?** Un servicio web gratuito de Google que permite a los propietarios de sitios web supervisar el estado de indexación, optimizar la visibilidad orgánica y diagnosticar errores de rastreo.
* **¿Para qué lo usamos?** Para asegurarnos de que Google conozca todas las páginas de psicología de Centro Paz sin pagar publicidad y saber qué palabras clave buscan los usuarios en Chile para encontrarnos.

### 2. Sitemap XML
* **¿Qué es?** Un archivo estructurado en lenguaje XML (`sitemap.xml`) que lista todas las URLs indexables de un sitio web junto con la fecha de su última modificación.
* **¿Para qué lo usamos?** Para entregarle a los robots de búsqueda un mapa directo y exhaustivo de las 41 URLs canónicas del centro, facilitando su indexación en segundos.

### 3. Googlebot (Rastreador Web de Google)
* **¿Qué es?** El robot o agente de software automatizado de Google que navega por internet descubriendo, descargando y analizando páginas web para agregarlas al índice del buscador.
* **¿Para qué lo usamos?** Para que descargue nuestro contenido clínico, lea los datos estructurados Schema.org de Valentina y nos posicione en las búsquedas de psicología en Ñuñoa.
