#!/bin/bash
# Automatización de Configuración de Cloudflare Tunnel para CPAZ Media OS (panel.centropaz.cl)
set -euo pipefail

CERT_FILE="${HOME}/.cloudflared/cert.pem"
CLOUDFLARED_BIN="/opt/homebrew/bin/cloudflared"

if [ ! -f "$CERT_FILE" ]; then
    echo "❌ cert.pem no encontrado en ~/.cloudflared/"
    echo "Por favor autoriza la zona 'centropaz.cl' en el navegador abierto por 'cloudflared tunnel login'."
    exit 1
fi

echo "✅ Certificado de Cloudflare detectado en $CERT_FILE"

# 1. Crear o recuperar el túnel cpaz-media-os
TUNNEL_NAME="cpaz-media-os"
echo "🔍 Verificando existencia del túnel '$TUNNEL_NAME'..."

EXISTING_TUNNEL=$($CLOUDFLARED_BIN tunnel list | grep "$TUNNEL_NAME" || true)

if [ -n "$EXISTING_TUNNEL" ]; then
    TUNNEL_ID=$(echo "$EXISTING_TUNNEL" | awk '{print $1}')
    echo "ℹ️ Túnel ya existe con ID: $TUNNEL_ID"
else
    echo "🚀 Creando túnel '$TUNNEL_NAME'..."
    CREATE_OUTPUT=$($CLOUDFLARED_BIN tunnel create "$TUNNEL_NAME")
    TUNNEL_ID=$(echo "$CREATE_OUTPUT" | grep -oE "[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}")
    echo "✅ Túnel creado con ID: $TUNNEL_ID"
fi

CRED_FILE="${HOME}/.cloudflared/${TUNNEL_ID}.json"

# 2. Generar archivo de configuración local
CONFIG_FILE="${HOME}/.cloudflared/config.yml"
cat <<EOF > "$CONFIG_FILE"
tunnel: ${TUNNEL_ID}
credentials-file: ${CRED_FILE}

ingress:
  - hostname: panel.centropaz.cl
    service: http://127.0.0.1:8765
    originRequest:
      connectTimeout: 10s
      noTLSVerify: false
      httpHostHeader: panel.centropaz.cl
  - service: http_status:404
EOF
echo "✅ Configuración generada en $CONFIG_FILE"

# 3. Enrutar el DNS en Cloudflare
echo "🌐 Enrutando DNS: panel.centropaz.cl -> túnel..."
$CLOUDFLARED_BIN tunnel route dns "$TUNNEL_NAME" panel.centropaz.cl || true

# 4. Configurar LaunchAgent para arranque permanente del túnel
PLIST_FILE="${HOME}/Library/LaunchAgents/cl.centropaz.cloudflared.plist"
echo "⚙️ Configurando LaunchAgent en $PLIST_FILE..."

cat <<EOF > "$PLIST_FILE"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>cl.centropaz.cloudflared</string>
    <key>ProgramArguments</key>
    <array>
        <string>${CLOUDFLARED_BIN}</string>
        <string>tunnel</string>
        <string>--config</string>
        <string>${CONFIG_FILE}</string>
        <string>run</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>${HOME}/.cpaz/cloudflared.log</string>
    <key>StandardErrorPath</key>
    <string>${HOME}/.cpaz/cloudflared.log</string>
</dict>
</plist>
EOF

launchctl unload "$PLIST_FILE" 2>/dev/null || true
launchctl load "$PLIST_FILE"
echo "✅ LaunchAgent cl.centropaz.cloudflared cargado y en ejecución."

echo "=========================================================================="
echo " 🎉 CLOUDFLARE TUNNEL CONFIGURADO CON ÉXITO"
echo " 🌐 Dominio Público: https://panel.centropaz.cl"
echo " 🔗 Destino Local:   http://127.0.0.1:8765/"
echo " 📄 Logs del túnel:  ${HOME}/.cpaz/cloudflared.log"
echo "=========================================================================="
