# Manual de Operación y PWA en iPhone — CPAZ Media OS

Este manual guía a Nicolás y al equipo de Centro Paz para operar el dashboard de CPAZ Media OS desde el iPhone y cualquier computador de manera autónoma, profesional y segura, sin requerir asistencia técnica continua.

---

## 1. ¿Cómo Ingresar al Panel desde el iPhone?

CPAZ Media OS dispone de dos vías de acceso seguro:

### Vía A: Acceso Privado Directo mediante Tailscale (Disponible de Inmediato)
Como tu iPhone (`100.89.124.62`) y tu Mac (`100.109.254.61`) forman parte de tu red privada segura Tailscale:
1. Abre **Tailscale** en tu iPhone y confirma que esté en estado **Conectado** (punto verde).
2. Abre **Safari** e ingresa a:
   ```text
   http://100.109.254.61:8765/
   ```
3. Se abrirá la pantalla oficial de acceso con el logo de Centro Paz.

### Vía B: Dominio Público Seguro `https://panel.centropaz.cl` (Requiere Activación Cloudflare)
Una vez enlazado el túnel de Cloudflare ([ver guía de despliegue](file:///Users/nigoku/CPAZ/deploy/README.md)):
1. Ingresa directamente a `https://panel.centropaz.cl` desde cualquier navegador o conexión celular (5G/Wi-Fi).
2. La conexión está cifrada de extremo a extremo con certificado SSL automático de 256 bits.

---

## 2. Instalación en la Pantalla de Inicio del iPhone (PWA Standalone)

CPAZ Media OS está configurado como una **Progressive Web App (PWA)** nativa para iOS:

1. Abre la URL en **Safari** (obligatorio en iOS para instalar PWAs).
2. Pulsa el botón **Compartir** en la barra inferior (el cuadrado con la flecha hacia arriba).
3. Desliza hacia abajo y selecciona **"Añadir a pantalla de inicio"** (Add to Home Screen).
4. Verás el nombre **"Centro Paz"** y el icono oficial de la flor/hoja de Centro Paz con fondo cálido.
5. Pulsa **Añadir** (arriba a la derecha).
6. **¡Listo!** El icono quedará instalado en tu pantalla de inicio junto a tus demás aplicaciones. Al tocarlo:
   - Se abrirá en **pantalla completa** (sin barras de navegación de Safari).
   - Tendrá barra de estado integrada con el color corporativo verde `#2c6e58`.
   - Se ejecutará en su propia ventana aislada.

---

## 3. Inicio de Sesión y Gestión de Credenciales

1. Al abrir la app, verás la tarjeta de bienvenida con el logotipo oficial.
2. Ingresa el **Token de Sesión**:
   - En tu Mac, puedes copiarlo en cualquier momento al portapapeles ejecutando:
     ```bash
     bash scripts/media_os_service.sh token --copy
     ```
   - Puedes guardarlo de forma segura en el llavero de Apple (**Ajustes → Contraseñas** de iOS) para que Safari lo autorrellene con Face ID.
3. Pulsa **"Desbloquear Dashboard"**.
4. La sesión se autentica mediante una cookie de alta seguridad (`HttpOnly; SameSite=Strict; Secure`) en la memoria del servidor (duración: 8 horas).

---

## 4. Gestión del Calendario Editorial desde el iPhone

La interfaz móvil fue diseñada específicamente para pantallas táctiles de iPhone:

* **Buscador Táctil:** Escribe cualquier palabra clave (ej: *"tdah"*, *"reembolso"*, *"crianza"*) para filtrar en tiempo real las 28 piezas.
* **Filtros Rápidos:** Toca las píldoras superiores para ver rápidamente:
  - `Todos (28)`
  - `QA (28)`
  - `Aprobados`
  - `Dry-Run`
* **Tarjetas Táctiles Móviles:** Cada publicación se presenta como una tarjeta limpia con:
  - Título y tópico clínico.
  - Canal y formato (ej: `instagram / feed_png`).
  - Estado actual y verificación de QA clínico.
* **Botón Copiar Autorización:**
  - Toca el botón grande **📋 Copiar**.
  - Automáticamente se copiará al portapapeles el comando de validación:
    `PUBLICAR cpaz-XXXXXXXX`
  - Este texto lo puedes enviar por WhatsApp a Valentina o ingresarlo en la terminal para confirmar la publicación.

---

## 5. Operaciones y Recuperación sin Antigravity

El servicio local corre en segundo plano en tu Mac mediante `launchd` (`cl.centropaz.media_os.plist`).

### Comandos de Administración en la Terminal del Mac:
```bash
# Ver estado del servicio (PID, puerto, token)
bash scripts/media_os_service.sh status

# Abrir el panel en el navegador y copiar el token al portapapeles
bash scripts/media_os_service.sh open

# Reiniciar el servicio (si se detiene o tras actualizar código)
bash scripts/media_os_service.sh restart

# Copiar el token activo al portapapeles
bash scripts/media_os_service.sh token --copy

# Rotar el token por uno nuevo criptográfico (invalida el anterior)
bash scripts/media_os_service.sh token --rotate

# Detener el servicio temporalmente
bash scripts/media_os_service.sh stop

# Iniciar el servicio
bash scripts/media_os_service.sh start
```

### ¿Qué hacer si no abre o no responde?
1. Verifica que tu Mac esté encendido y conectado a la red.
2. Abre la terminal y ejecuta: `bash scripts/media_os_service.sh status`.
3. Si el estado no está en verde, corre: `bash scripts/media_os_service.sh restart`.
4. Si accedes desde fuera de casa por Tailscale, confirma que la app Tailscale esté activa en ambos dispositivos.

---

## 6. Política de Seguridad y Privacidad Clínica

* **Cero Datos de Pacientes (Ley 19.628):** El panel no almacena en caché ni expone nombres, RUTs ni diagnósticos de pacientes.
* **Aprobación Humana Obligatoria:** Las 28 piezas permanecen en `CLINICAL_QA`. Ningún contenido se publica en redes sociales sin la aprobación explícita de Valentina mediante el comando `PUBLICAR <ID>`.
