# Infraestructura y Despliegue — panel.centropaz.cl

Este directorio contiene las configuraciones completas y reproducibles para conectar CPAZ Media OS con el dominio público `panel.centropaz.cl` bajo HTTPS seguro.

---

## 1. Arquitectura Recomendada: Cloudflare Tunnel (Cero Costo, Cero Puertos Abiertos)

Dado que `centropaz.cl` ya es gestionado por los servidores de nombres Anycast de Cloudflare (`tom.ns.cloudflare.com`, `kay.ns.cloudflare.com`), la arquitectura recomendada es **Cloudflare Tunnel (`cloudflared`)**.

```
[iPhone / Safari]
       │
       ▼ (HTTPS : 443 - TLS Gestionado por Cloudflare)
[panel.centropaz.cl - Cloudflare Anycast Edge]
       │
       ▼ (Túnel cifrado de salida QUIC / HTTP2)
[Daemon cloudflared en Mac / VPS]
       │
       ▼ (Loopback local 127.0.0.1:8765)
[CPAZ Media OS (Python 3.14 + launchd)]
```

### Ventajas Operativas:
1. **$0/mes de costo.**
2. **CERO puertos entrantes abiertos:** No requiere abrir puertos en el router hogareño ni exponer la IP pública de la conexión residencial.
3. **Certificado SSL/TLS automático:** Terminado en la red global de Cloudflare.
4. **Protección Anti-DDoS y Web Application Firewall:** Filtro de tráfico no legítimo antes de llegar a la máquina.

---

## 2. Pasos para Activación con Autorización de Nicolás

Cuando Nicolás autorice la conexión en el panel de Cloudflare, se ejecutan estos 3 pasos:

### Paso 1: Crear el Túnel en Cloudflare
```bash
# Instalar cloudflared si no está presente
brew install cloudflare/cloudflare/cloudflared

# Autenticar con la cuenta de Cloudflare de Centro Paz
cloudflared tunnel login

# Crear el túnel para el panel
cloudflared tunnel create cpaz-media-os
```

### Paso 2: Vincular el DNS de panel.centropaz.cl
```bash
# Asocia el registro CNAME automáticamente en la zona centropaz.cl
cloudflared tunnel route dns cpaz-media-os panel.centropaz.cl
```

### Paso 3: Iniciar el Servicio del Túnel
```bash
# Copiar configuración preparada
cp deploy/cloudflared-config.yml ~/.cloudflared/config.yml

# Iniciar túnel como servicio de fondo
cloudflared service install
```

---

## 3. Alternativa 2: Reverse Proxy Caddy / Nginx

Si se desea utilizar el servidor Oracle VPS (`146.181.44.106` / `100.88.96.68`):
1. Apuntar registro DNS tipo `A` en Cloudflare: `panel.centropaz.cl` $\rightarrow$ `146.181.44.106`.
2. Utilizar [`deploy/Caddyfile`](Caddyfile) o [`deploy/nginx-panel.conf`](nginx-panel.conf).
3. Caddy adquiere automáticamente certificados de Let's Encrypt y reenvía el tráfico por la red privada Tailscale a `100.109.254.61:8765`.

---

## 4. Monitorización de Salud Automática
El script [`deploy/healthcheck.sh`](healthcheck.sh) comprueba periódicamente que el backend local y los activos de la PWA respondan con código HTTP 200, registrando eventos en `~/.cpaz/healthcheck.log` sin exponer credenciales.
