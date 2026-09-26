# Guía de Indexación Gratuita Inmediata en Google Search Console y Bing

Este manual describe el procedimiento exacto paso a paso (100% gratuito, sin inversión publicitaria) para que Google y Bing indexen las 36 páginas de `centropaz.cl` en menos de 24 a 48 horas.

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

## 2. Envío del Sitemap XML (Indexación de 36 URLs)

Una vez verificada la propiedad:
1. En el menú lateral izquierdo de Google Search Console, haz clic en **Sitemaps** (bajo la sección *Indexación*).
2. En el campo *"Añadir un nuevo sitemap"*, escribe: `sitemap.xml`.
3. La URL completa quedará: `https://www.centropaz.cl/sitemap.xml`.
4. Haz clic en **Enviar**.
5. Verás el estado en verde: **Correcto** (Google leerá las 36 páginas del sitio, incluyendo las 3 landing pages y los 28 artículos de blog).

---

## 3. Solicitud de Indexación Prioritaria (Inspección de URLs)

Para que las páginas más importantes aparezcan en los resultados de Google hoy mismo sin esperar el ciclo regular de rastreo:

1. En la barra superior de búsqueda de Search Console (*"Inspeccionar cualquier URL de https://www.centropaz.cl/"*), pega una por una las siguientes URLs clave:
   * `https://www.centropaz.cl/`
   * `https://www.centropaz.cl/psicologo-nunoa.html`
   * `https://www.centropaz.cl/tdah-adultos.html`
   * `https://www.centropaz.cl/reembolso-isapre-psicologia.html`
   * `https://www.centropaz.cl/blog/`
2. Presiona Enter.
3. Haz clic en el botón blanco **Solicitar indexación**.
4. Repite el proceso con las 5 URLs principales. Googlebot las pondrá en cola de prioridad alta.

---

## 4. Indexación en Bing Webmaster Tools (Tráfico Orgánico Adicional)

Microsoft Bing alimenta los motores de búsqueda de Windows y la IA de Microsoft Copilot:
1. Ingresa a: [bing.com/webmasters](https://www.bing.com/webmasters).
2. Haz clic en **Comenzar** e inicia sesión con Google.
3. Selecciona **Importar desde Google Search Console** (se sincroniza en 1 clic sin configuraciones adicionales).
4. El sitemap se importará automáticamente.

---

## 5. Glosario Técnico

### 1. Google Search Console (GSC)
* **¿Qué es?** Un servicio web gratuito de Google que permite a los propietarios de sitios web supervisar el estado de indexación, optimizar la visibilidad orgánica y diagnosticar errores de rastreo.
* **¿Para qué lo usamos?** Para asegurarnos de que Google conozca todas las páginas de psicología de Centro Paz sin pagar publicidad y saber qué palabras clave buscan los usuarios en Chile para encontrarnos.

### 2. Sitemap XML
* **¿Qué es?** Un archivo estructurado en lenguaje XML (`sitemap.xml`) que lista todas las URLs indexables de un sitio web junto con la fecha de su última modificación.
* **¿Para qué lo usamos?** Para entregarle a los robots de búsqueda un mapa directo y exhaustivo de las 36 páginas del centro, facilitando su indexación en segundos.

### 3. Googlebot (Rastreador Web de Google)
* **¿Qué es?** El robot o agente de software automatizado de Google que navega por internet descubriendo, descargando y analizando páginas web para agregarlas al índice del buscador.
* **¿Para qué lo usamos?** Para que descargue nuestro contenido clínico, lea los datos estructurados Schema.org de Valentina y nos posicione en las búsquedas de psicología en Ñuñoa.
