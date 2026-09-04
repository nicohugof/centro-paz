# 🔑 Guía Rápida: Conectar Meta Graph API para Publicación 100% Automática

En la comunidad de desarrolladores y en GitHub, la forma oficial, permanente y sin riesgo de baneo para publicar automáticamente en Instagram y Facebook es a través de la **Meta Graph API** (Content Publishing API).

---

## ⏱️ Configuración en 3 Minutos (Paso a Paso)

### 1. Entrar al Portal de Desarrolladores de Meta
1. Abre [developers.facebook.com](https://developers.facebook.com/) con tu cuenta de Facebook administradora de la página de Centro Paz.
2. Haz clic en **Mis Apps** (My Apps) ➡️ **Crear App** (Create App).
3. Selecciona tipo: **Otro (Other)** o **Negocios (Business)** ➡️ Nombre: `Centro Paz Automation`.

---

### 2. Generar el Token de Publicación
1. En el menú lateral izquierdo, ve a **Herramientas (Tools)** ➡️ **Explorador de la Graph API (Graph API Explorer)**.
2. En *Meta App*, selecciona tu app (`Centro Paz Automation`).
3. En *Permisos (Permissions)*, agrega estos 3 permisos:
   - `pages_show_list`
   - `pages_read_engagement`
   - `pages_manage_posts`
   - `instagram_basic`
   - `instagram_content_publish`
4. Haz clic en **Generar Access Token (Generate Access Token)** y aprueba el acceso para la página de Centro Paz y la cuenta `@centropaz.cl`.

---

### 3. Guardar el Token en tu Agente en la Terminal
Copia el token generado y ejecútalo en la terminal de tu proyecto:

```bash
# Guardar el token de acceso
python3 -m agent.auto_publisher --set-token "TU_TOKEN_AQUI"

# Guardar tu ID de cuenta de Instagram (aparece en el explorador de Meta)
python3 -m agent.auto_publisher --set-ig-id "TU_IG_ACCOUNT_ID"
```

---

## 🚀 ¡Listo! Publicación 100% Automática desde la Terminal

Una vez guardado el token, puedes publicar cualquier post de la semana con un solo comando:

```bash
# Verificar que el token y las cuentas responden:
python3 -m agent.auto_publisher --test-connection

# Publicar el Post 1 (TDAH en Adultos) en Instagram y Facebook simultáneamente:
python3 -m agent.auto_publisher --post 1

# Publicar el Post 2 (Reembolso Isapres):
python3 -m agent.auto_publisher --post 2

# Publicar solo en Instagram:
python3 -m agent.auto_publisher --post 3 --platform instagram

# Publicar toda la parrilla (1 al 7) con 5 segundos de pausa:
python3 -m agent.auto_publisher --post-all
```

---

## 🔄 Integración Alternativa con n8n / Webhooks

Si ya utilizas **n8n** o Make para automatizar flujos:
```bash
python3 -m agent.auto_publisher --webhook-url "https://tu-instancia-n8n.com/webhook/centropaz-social" --post 1
```
El agente envía la URL pública de la imagen alojada en GitHub y el copy con formato completo.

---

## 🤖 Publicación automática por n8n (cron 09/13/18/21)

Lo de arriba publica **a mano desde la terminal**. Esto es lo que publica **solo**.

### Por qué no estaba publicando (2026-09-03)

Había dos workflows distintos, los dos llamados "Autónoma":

- `agent/n8n_cpaz_workflow.json` (este repo) — tiene el **cron** y elige el post. Nunca se importó.
- `cpazAutoPublish01` (desplegado en n8n) — es un **webhook pasivo**: publica sólo lo que le
  manden por POST. Nadie lo llamaba. Se borra.

Además el de este repo tenía dos bugs que lo habrían roto igual, ya corregidos:

1. Leía el token con `{{$env.META_ACCESS_TOKEN || 'YOUR_META_TOKEN'}}`. **n8n bloquea `$env`
   en expresiones por defecto** (`N8N_BLOCK_ENV_ACCESS_IN_NODE=true` desde la v2), así que caía
   al literal y Meta devolvía 400 sin que nada avisara. Ahora el token va en una **credencial
   Query Auth de n8n**, cifrada en reposo. *No* desbloquear `$env`: el workflow `r-b2be0168` de
   la intrusión del 24/08 se dedicaba justamente a volcar `process.env`.
2. El selector hacía `schedule.find(...) || schedule[0]`: cuando no encontraba el slot,
   **republicaba el post 1 en silencio, para siempre**. Ahora lanza error.

También quedó fijada la zona horaria a `America/Santiago`, para que el cron y el selector no
dependan del timezone del contenedor.

### Desplegar (necesita SSH al Oracle)

1. **Comprobá que el sitio sirve la parrilla** — si esto falla, lo demás no sirve:
   ```bash
   curl -sI https://www.centropaz.cl/parrilla_semanal_n8n.json | head -1   # espera: 200
   ```
2. **Creá la credencial en n8n**: *Credentials → New → Query Auth*
   - Nombre del parámetro: `access_token`
   - Valor: el token **nuevo**, ya rotado tras el incidente. Nunca el viejo.
3. **Importá** `agent/n8n_cpaz_workflow.json` y asigná esa credencial a los 3 nodos HTTP.
4. **Completá `instagram_account_id`** en el nodo `Config CPAZ` (el mismo de
   `agent/meta_config.json`). Es el único campo a llenar; sin él el workflow falla al arrancar,
   a propósito.
5. **Probá a mano** con *Execute workflow* antes de activarlo.
6. **Borrá** `cpazAutoPublish01` y activá este.
7. Agregá el id nuevo a `ironcross-backup/n8n/workflows_permitidos.txt`.

### Verificación

- `Seleccionar Post del Horario` devuelve el post del horario actual, no vacío.
- `1. Crear Contenedor IG` devuelve un `id`, que `2. Publicar en Instagram` consume.
- El post aparece en la cuenta real de Instagram y en la página de Facebook.
- Con una credencial inválida, el nodo da error visible — no pasa de largo.
