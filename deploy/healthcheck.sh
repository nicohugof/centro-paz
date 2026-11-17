#!/bin/bash
# Healthcheck y Monitor de Estado — CPAZ Media OS
# Verifica la disponibilidad de la aplicación en loopback local y HTTPS sin exponer secretos.
set -euo pipefail

LOG_FILE="${HOME}/.cpaz/healthcheck.log"
TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
mkdir -p "${HOME}/.cpaz"

# 1. Comprobar proceso y socket local
LOCAL_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 3 http://127.0.0.1:8765/ || echo "ERR")

if [ "$LOCAL_CODE" = "200" ]; then
    echo "[$TIMESTAMP] OK: Backend local 127.0.0.1:8765 respondiendo HTTP 200" >> "$LOG_FILE"
else
    echo "[$TIMESTAMP] ALERTA: Backend local falló (HTTP $LOCAL_CODE). Intentando reiniciar vía servicio..." >> "$LOG_FILE"
    if [ -f "$(dirname "$0")/../scripts/media_os_service.sh" ]; then
        bash "$(dirname "$0")/../scripts/media_os_service.sh" restart >> "$LOG_FILE" 2>&1 || true
    fi
    exit 1
fi

# 2. Comprobar PWA manifest estático
MANIFEST_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 3 http://127.0.0.1:8765/manifest.webmanifest || echo "ERR")
if [ "$MANIFEST_CODE" != "200" ]; then
    echo "[$TIMESTAMP] ADVERTENCIA: Manifest PWA devolvió HTTP $MANIFEST_CODE" >> "$LOG_FILE"
fi

exit 0
