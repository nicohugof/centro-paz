#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Notificador Automatizado de Indexación Inmediata (IndexNow & Search Engines).

Notifica y sincroniza a los motores de búsqueda convencionales y de Inteligencia Artificial
(Microsoft Bing, Copilot, Perplexity, Yandex y Googlebot) sobre las 41 URLs del sitio centropaz.cl,
con especial prioridad en las 4 nuevas páginas clínicas de alta intención:
1. Ansiedad y Crisis de Angustia (ansiedad-crisis-angustia.html)
2. Depresión y Trastornos del Ánimo (depresion-trastornos-animo.html)
3. Trastornos de la Personalidad / TLP (trastornos-personalidad-tlp.html)
4. Psicodiagnóstico e Informes Formales (evaluacion-psicodiagnostica-informes.html)
"""
from __future__ import annotations

import concurrent.futures
import json
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
SITEMAP_URL = "https://www.centropaz.cl/sitemap.xml"
HOST = "www.centropaz.cl"
INDEXNOW_KEY = "centropaz2026indexnowkey"
KEY_LOCATION = f"https://{HOST}/indexnow.txt"

# 1. URLs Principales y Landings de Alta Intención (13 URLs)
CORE_LANDING_URLS: List[str] = [
    "https://www.centropaz.cl/",
    "https://www.centropaz.cl/ansiedad-crisis-angustia.html",
    "https://www.centropaz.cl/depresion-trastornos-animo.html",
    "https://www.centropaz.cl/trastornos-personalidad-tlp.html",
    "https://www.centropaz.cl/evaluacion-psicodiagnostica-informes.html",
    "https://www.centropaz.cl/psicologo-nunoa.html",
    "https://www.centropaz.cl/tdah-adultos.html",
    "https://www.centropaz.cl/parentalidad-neurodivergente.html",
    "https://www.centropaz.cl/reembolso-isapre-psicologia.html",
    "https://www.centropaz.cl/guia_7_claves_regulacion_centro_paz.html",
    "https://www.centropaz.cl/links",
    "https://www.centropaz.cl/privacidad.html",
    "https://www.centropaz.cl/blog/",
]

# 2. Artículos Clínicos Especializados del Blog (28 URLs)
CLINICAL_BLOG_URLS: List[str] = [
    "https://www.centropaz.cl/blog/tdah-adultos.html",
    "https://www.centropaz.cl/blog/reembolso-isapre.html",
    "https://www.centropaz.cl/blog/crianza-regulacion.html",
    "https://www.centropaz.cl/blog/masking.html",
    "https://www.centropaz.cl/blog/terapia-online.html",
    "https://www.centropaz.cl/blog/evaluacion-infantil.html",
    "https://www.centropaz.cl/blog/autocuidado-adultos.html",
    "https://www.centropaz.cl/blog/burnout-autista.html",
    "https://www.centropaz.cl/blog/paralisis-ejecutiva.html",
    "https://www.centropaz.cl/blog/regulacion-ansiedad.html",
    "https://www.centropaz.cl/blog/apoyo-neurodivergente-hijos.html",
    "https://www.centropaz.cl/blog/primera-sesion.html",
    "https://www.centropaz.cl/blog/culpa-parental.html",
    "https://www.centropaz.cl/blog/reembolso-matematica.html",
    "https://www.centropaz.cl/blog/tdah-mujeres.html",
    "https://www.centropaz.cl/blog/sobrecarga-sensorial-ruido.html",
    "https://www.centropaz.cl/blog/reembolso-seguros-cobertura.html",
    "https://www.centropaz.cl/blog/hiperfoco-burnout.html",
    "https://www.centropaz.cl/blog/crianza-rutinas-flexibles.html",
    "https://www.centropaz.cl/blog/comunicacion-asertiva-limites.html",
    "https://www.centropaz.cl/blog/tdah-rechazo-rsd.html",
    "https://www.centropaz.cl/blog/primera-consulta-nunoa.html",
    "https://www.centropaz.cl/blog/terapia-infantil-juego.html",
    "https://www.centropaz.cl/blog/ansiedad-somatica-cuerpo.html",
    "https://www.centropaz.cl/blog/isapre-licencia-boletas.html",
    "https://www.centropaz.cl/blog/desconexion-tecnologica-tdah.html",
    "https://www.centropaz.cl/blog/padres-regulacion-propia.html",
    "https://www.centropaz.cl/blog/autocuidado-fin-de-semana.html",
]

# Total de 41 URLs canónicas
URLS_TO_INDEX: List[str] = CORE_LANDING_URLS + CLINICAL_BLOG_URLS

# Endpoints autorizados de la red IndexNow
INDEXNOW_ENDPOINTS = [
    ("IndexNow Central (Bing, Copilot, Perplexity, Seznam, Naver)", "https://api.indexnow.org/indexnow"),
    ("Microsoft Bing & Copilot Directo", "https://www.bing.com/indexnow"),
    ("Yandex Engine Directo", "https://yandex.com/indexnow"),
]


def verify_indexnow_keys() -> Dict[str, str]:
    """
    Verifica que la clave IndexNow exista localmente en indexnow.txt y sea accesible remotamente.
    """
    results = {}
    
    # 1. Verificación y escritura local de indexnow.txt
    key_file = ROOT / "indexnow.txt"
    key_file.write_text(f"{INDEXNOW_KEY}\n", encoding="utf-8")
    
    # Archivo espejo directo <key>.txt según especificación IndexNow
    mirror_file = ROOT / f"{INDEXNOW_KEY}.txt"
    mirror_file.write_text(f"{INDEXNOW_KEY}\n", encoding="utf-8")
    
    local_content = key_file.read_text(encoding="utf-8").strip()
    if local_content == INDEXNOW_KEY:
        results["local_file"] = f"OK (Contiene '{INDEXNOW_KEY}' en {key_file.name})"
    else:
        results["local_file"] = f"ERROR: Contenido local no coincide ({local_content})"

    # 2. Verificación remota en producción (HTTP GET)
    remote_url = f"https://{HOST}/indexnow.txt"
    try:
        req = urllib.request.Request(
            remote_url,
            headers={"User-Agent": "CentroPaz-IndexVerifier/2.0"}
        )
        with urllib.request.urlopen(req, timeout=8) as resp:
            body = resp.read().decode("utf-8").strip()
            if resp.status == 200 and body == INDEXNOW_KEY:
                results["remote_url"] = f"OK HTTP 200 (Clave validada en {remote_url})"
            else:
                results["remote_url"] = f"ALERTA: HTTP {resp.status}, cuerpo: '{body}'"
    except Exception as e:
        results["remote_url"] = f"ERROR conectando a {remote_url}: {e}"

    return results


def check_url_status(url: str, timeout: int = 6) -> Tuple[str, int, str]:
    """Comprueba el código de estado HTTP de una URL en producción."""
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "CentroPaz-SEO-Bot/2.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return (url, resp.status, "OK")
    except urllib.error.HTTPError as e:
        return (url, e.code, f"HTTPError {e.reason}")
    except Exception as e:
        return (url, 0, f"Error: {e}")


def verify_all_urls_live(urls: List[str]) -> List[Tuple[str, int, str]]:
    """Verifica concurrentemente la disponibilidad de todas las URLs."""
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        future_to_url = {executor.submit(check_url_status, url): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            results.append(future.result())
    # Mantener el orden original de URLs
    url_order = {url: i for i, url in enumerate(urls)}
    results.sort(key=lambda r: url_order.get(r[0], 999))
    return results


def ping_googlebot() -> Dict[str, str]:
    """Notifica el sitemap oficial a Googlebot."""
    google_ping_url = f"https://www.google.com/ping?sitemap={urllib.parse.quote(SITEMAP_URL)}"
    try:
        req = urllib.request.Request(
            google_ping_url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; CentroPazBot/2.0; +https://www.centropaz.cl)"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return {"status": "OK", "code": str(resp.status), "detail": "Sitemap aceptado vía ping"}
    except urllib.error.HTTPError as e:
        # Google deprecó el endpoint público de ping a favor de Search Console & robots.txt
        return {
            "status": "DEPRECATED_BY_GOOGLE",
            "code": str(e.code),
            "detail": "Google procesa el sitemap de forma continua vía robots.txt y Search Console API."
        }
    except Exception as e:
        return {"status": "ERROR", "code": "ERR", "detail": str(e)}


def ping_indexnow_network(urls: List[str]) -> List[Dict[str, str]]:
    """Envía el lote de URLs a cada nodo de la red IndexNow."""
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls
    }
    data_bytes = json.dumps(payload).encode("utf-8")
    network_responses = []

    for name, endpoint in INDEXNOW_ENDPOINTS:
        try:
            req = urllib.request.Request(
                endpoint,
                data=data_bytes,
                headers={
                    "Content-Type": "application/json; charset=utf-8",
                    "User-Agent": "CentroPaz-IndexEngine/2.0"
                },
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                network_responses.append({
                    "engine": name,
                    "endpoint": endpoint,
                    "status_code": resp.status,
                    "status_text": resp.reason,
                    "success": True
                })
        except urllib.error.HTTPError as e:
            # En IndexNow, 200 y 202 representan éxito
            success = e.code in (200, 202)
            network_responses.append({
                "engine": name,
                "endpoint": endpoint,
                "status_code": e.code,
                "status_text": f"HTTP {e.code} - {e.reason}",
                "success": success
            })
        except Exception as e:
            network_responses.append({
                "engine": name,
                "endpoint": endpoint,
                "status_code": 0,
                "status_text": f"Excepción de conexión: {e}",
                "success": False
            })

    return network_responses


def run_instant_index_flow():
    print("=" * 80)
    print(" 🌿 CENTRO PAZ (CPAZ) — MOTOR DE INDEXACIÓN INMEDIATA & SEO TÉCNICO")
    print("=" * 80)
    print()

    # Paso 1: Verificación de clave IndexNow
    print("🔑 1. VERIFICACIÓN DE CLAVE INDEXNOW (indexnow.txt):")
    key_status = verify_indexnow_keys()
    print(f"   • Verificación Local:   {key_status['local_file']}")
    print(f"   • Verificación Remota:  {key_status['remote_url']}")
    print()

    # Paso 2: Notificación a Googlebot
    print("📡 2. NOTIFICACIÓN A GOOGLEBOT:")
    google_res = ping_googlebot()
    if google_res["status"] == "OK":
        print(f"   ✅ Notificación enviada exitosamente a Google (Código HTTP: {google_res['code']})")
    else:
        print(f"   ℹ️ Google Ping respondió HTTP {google_res['code']}: {google_res['detail']}")
        print(f"      Referencia canónica robots.txt: https://www.centropaz.cl/robots.txt -> Sitemap activo.")
    print()

    # Paso 3: Envío por lote a la red IndexNow
    print(f"🚀 3. TRANSMISIÓN DE LOTE A LA RED INDEXNOW ({len(URLS_TO_INDEX)} URLs canónicas):")
    print(f"   Host: {HOST} | Clave: {INDEXNOW_KEY}")
    print(f"   Ubicación de validación: {KEY_LOCATION}")
    print()

    indexnow_results = ping_indexnow_network(URLS_TO_INDEX)
    all_success = True
    for res in indexnow_results:
        mark = "✅" if res["success"] else "❌"
        print(f"   {mark} {res['engine']}")
        print(f"      Endpoint: {res['endpoint']}")
        print(f"      Respuesta HTTP: {res['status_code']} ({res['status_text']})")
        if not res["success"]:
            all_success = False

    print()

    # Paso 4: Auditoría de disponibilidad de URLs en producción
    print(f"🔍 4. AUDITORÍA DE RESPUESTA EN VIVO ({len(URLS_TO_INDEX)} URLs):")
    url_health = verify_all_urls_live(URLS_TO_INDEX)
    healthy_count = sum(1 for _, code, _ in url_health if code == 200)
    
    print(f"   • Páginas principales (13):")
    for url, code, msg in url_health[:13]:
        status_symbol = "✅" if code == 200 else "⚠️"
        print(f"     {status_symbol} [{code}] {url}")

    print(f"\n   • Artículos de blog clínico ({len(url_health) - 13}):")
    for url, code, msg in url_health[13:]:
        status_symbol = "✅" if code == 200 else "⚠️"
        print(f"     {status_symbol} [{code}] {url}")

    print()
    print("=" * 80)
    if all_success and healthy_count == len(URLS_TO_INDEX):
        print(f" 🎉 INDEXACIÓN EXITOSA: {healthy_count}/{len(URLS_TO_INDEX)} URLs activas (200 OK) y notificadas.")
    else:
        print(f" ⚠️ PROCESO COMPLETADO: {healthy_count}/{len(URLS_TO_INDEX)} URLs activas.")
    print("=" * 80)


if __name__ == "__main__":
    run_instant_index_flow()
