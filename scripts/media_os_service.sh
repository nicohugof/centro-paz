#!/usr/bin/env bash
# ==============================================================================
# Centro Paz (CPAZ) — Gestor de Servicio Local Permanente para CPAZ Media OS
# ==============================================================================
# Uso:
#   bash scripts/media_os_service.sh start|stop|restart|status|token|open|install-launchd|uninstall-launchd
# ==============================================================================

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CPAZ_DIR="${HOME}/.cpaz"
PID_FILE="${CPAZ_DIR}/media_os.pid"
LOG_FILE="${CPAZ_DIR}/media_os.log"
TOKEN_FILE="${CPAZ_DIR}/media_os_token"
LAUNCHD_PLIST="${HOME}/Library/LaunchAgents/cl.centropaz.media_os.plist"
PYTHON_BIN="/Library/Frameworks/Python.framework/Versions/3.14/bin/python3"

if [[ ! -x "${PYTHON_BIN}" ]]; then
  PYTHON_BIN="$(which python3)"
fi

mkdir -p "${CPAZ_DIR}"
chmod 700 "${CPAZ_DIR}" 2>/dev/null || true

get_token() {
  "${PYTHON_BIN}" -c "from media_os.dashboard import get_or_create_persistent_token; print(get_or_create_persistent_token())"
}

is_running() {
  if lsof -i :8765 -sTCP:LISTEN -t >/dev/null 2>&1; then
    return 0
  fi
  if [[ -f "${PID_FILE}" ]]; then
    local pid
    pid="$(cat "${PID_FILE}" 2>/dev/null || true)"
    if [[ -n "${pid}" ]] && ps -p "${pid}" >/dev/null 2>&1; then
      return 0
    fi
  fi
  return 1
}

cmd_start() {
  if is_running; then
    local pid
    pid="$(lsof -i :8765 -sTCP:LISTEN -t 2>/dev/null || cat "${PID_FILE}" 2>/dev/null || echo 'desconocido')"
    echo "✅ CPAZ Media OS ya está en ejecución (PID: ${pid}) en http://127.0.0.1:8765"
    return 0
  fi

  echo "🚀 Iniciando CPAZ Media OS en segundo plano..."
  cd "${ROOT_DIR}"
  nohup "${PYTHON_BIN}" -m media_os.cli serve --host 127.0.0.1 --port 8765 >> "${LOG_FILE}" 2>&1 &
  local new_pid=$!
  echo "${new_pid}" > "${PID_FILE}"
  chmod 600 "${PID_FILE}" 2>/dev/null || true

  # Esperar disponibilidad del socket
  local retries=15
  while [[ ${retries} -gt 0 ]]; do
    if lsof -i :8765 -sTCP:LISTEN >/dev/null 2>&1; then
      break
    fi
    sleep 0.2
    retries=$((retries - 1))
  done

  if is_running; then
    local tok
    tok="$(get_token)"
    echo "=========================================================================="
    echo " 🌿 CPAZ Media OS OPERATIVO"
    echo " 🌐 URL Local: http://127.0.0.1:8765/"
    echo " 🔑 Token de Sesión: ${tok}"
    echo " 📄 Registro de logs: ${LOG_FILE}"
    echo "=========================================================================="
  else
    echo "❌ Error al iniciar el servidor. Revisa el registro en: ${LOG_FILE}"
    return 1
  fi
}

cmd_stop() {
  if ! is_running; then
    echo "ℹ️ CPAZ Media OS no está en ejecución."
    rm -f "${PID_FILE}"
    return 0
  fi

  echo "🛑 Deteniendo CPAZ Media OS..."
  local pids
  pids="$(lsof -i :8765 -sTCP:LISTEN -t 2>/dev/null || true)"
  if [[ -z "${pids}" ]] && [[ -f "${PID_FILE}" ]]; then
    pids="$(cat "${PID_FILE}" 2>/dev/null || true)"
  fi

  for p in ${pids}; do
    if [[ -n "${p}" ]]; then
      kill -TERM "${p}" 2>/dev/null || true
    fi
  done

  sleep 0.8

  # Forzar cierre si aún persiste
  local lingering
  lingering="$(lsof -i :8765 -sTCP:LISTEN -t 2>/dev/null || true)"
  for p in ${lingering}; do
    if [[ -n "${p}" ]]; then
      kill -9 "${p}" 2>/dev/null || true
    fi
  done

  rm -f "${PID_FILE}"
  echo "✅ Servidor detenido correctamente."
}

cmd_restart() {
  cmd_stop
  sleep 0.5
  cmd_start
}

cmd_status() {
  echo "=========================================================================="
  echo " 📊 ESTADO DEL SERVICIO: CPAZ MEDIA OS"
  echo "=========================================================================="
  if is_running; then
    local pid
    pid="$(lsof -i :8765 -sTCP:LISTEN -t 2>/dev/null || cat "${PID_FILE}" 2>/dev/null || echo 'desconocido')"
    local http_status
    http_status="$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8765/ || echo "DOWN")"
    echo " • Estado:          🟢 EN EJECUCIÓN"
    echo " • PID:             ${pid}"
    echo " • Puerto:          127.0.0.1:8765 (Loopback Privado)"
    echo " • Verificación:    HTTP ${http_status}"
    echo " • Token Guardado:  $(get_token)"
    echo " • URL:             http://127.0.0.1:8765/"
  else
    echo " • Estado:          🔴 DETENIDO"
    echo " • Puerto:          8765 (Libre)"
  fi

  if [[ -f "${LAUNCHD_PLIST}" ]]; then
    echo " • Launchd Daemon:  🟢 INSTALADO (${LAUNCHD_PLIST})"
  else
    echo " • Launchd Daemon:  ⚪ NO INSTALADO"
  fi
  echo "=========================================================================="
}

cmd_token() {
  local tok
  tok="$(get_token)"
  echo "${tok}"
  if [[ "${1:-}" == "--copy" ]] && command -v pbcopy >/dev/null 2>&1; then
    echo -n "${tok}" | pbcopy
    echo "📋 Token copiado al portapapeles de macOS."
  fi
}

cmd_open() {
  if ! is_running; then
    cmd_start
  fi
  echo "🌐 Abriendo CPAZ Media OS en el navegador predeterminado..."
  open "http://127.0.0.1:8765/"
}

cmd_install_launchd() {
  echo "⚙️ Configurando inicio automático permanente en macOS (launchd)..."
  mkdir -p "${HOME}/Library/LaunchAgents"

  cat <<EOF > "${LAUNCHD_PLIST}"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>cl.centropaz.media_os</string>
    <key>WorkingDirectory</key>
    <string>${ROOT_DIR}</string>
    <key>ProgramArguments</key>
    <array>
        <string>${PYTHON_BIN}</string>
        <string>-m</string>
        <string>media_os.cli</string>
        <string>serve</string>
        <string>--host</string>
        <string>127.0.0.1</string>
        <string>--port</string>
        <string>8765</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>${LOG_FILE}</string>
    <key>StandardErrorPath</key>
    <string>${LOG_FILE}</string>
</dict>
</plist>
EOF

  chmod 644 "${LAUNCHD_PLIST}"
  launchctl unload "${LAUNCHD_PLIST}" 2>/dev/null || true
  launchctl load "${LAUNCHD_PLIST}"
  echo "✅ Servicio launchd instalado y cargado con éxito:"
  echo "   ${LAUNCHD_PLIST}"
  echo "💡 CPAZ Media OS iniciará automáticamente cada vez que inicies sesión en tu Mac."
  sleep 1
  cmd_status
}

cmd_uninstall_launchd() {
  if [[ -f "${LAUNCHD_PLIST}" ]]; then
    echo "🗑️ Desinstalando servicio launchd..."
    launchctl unload "${LAUNCHD_PLIST}" 2>/dev/null || true
    rm -f "${LAUNCHD_PLIST}"
    cmd_stop
    echo "✅ Servicio launchd desinstalado y detenido."
  else
    echo "ℹ️ El servicio launchd no estaba instalado."
  fi
}

case "${1:-status}" in
  start)
    cmd_start
    ;;
  stop)
    cmd_stop
    ;;
  restart)
    cmd_restart
    ;;
  status)
    cmd_status
    ;;
  token)
    cmd_token "${2:-}"
    ;;
  open)
    cmd_open
    ;;
  install-launchd)
    cmd_install_launchd
    ;;
  uninstall-launchd)
    cmd_uninstall_launchd
    ;;
  help|--help|-h)
    echo "Uso: $0 {start|stop|restart|status|token|open|install-launchd|uninstall-launchd}"
    ;;
  *)
    echo "Comando no reconocido: $1"
    echo "Uso: $0 {start|stop|restart|status|token|open|install-launchd|uninstall-launchd}"
    exit 1
    ;;
esac
