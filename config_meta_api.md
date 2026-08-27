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
