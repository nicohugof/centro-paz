#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Motor de Publicación Automática en Redes Sociales (Meta Graph API & n8n).

Mecanismo estándar de la industria y GitHub para publicación 100% autónoma en:
  - Instagram Professional (@centropaz.cl)
  - Facebook Page (Centro Paz)
  - Disparador de Webhooks para n8n / Make / Buffer

Uso:
  python3 -m agent.auto_publisher --post 1                 (Publica el post 1 inmediatamente)
  python3 -m agent.auto_publisher --post-all              (Publica o programa toda la parrilla semanal)
  python3 -m agent.auto_publisher --test-connection       (Verifica tokens y conexión con Meta Graph API)
  python3 -m agent.auto_publisher --webhook-url "URL"     (Envía payload a webhook de n8n)
"""
from __future__ import annotations

import argparse
import json
import os
import time
import urllib.parse
import urllib.request
from pathlib import Path
from agent import content_engine

ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = ROOT / "agent" / "meta_config.json"
BASE_RAW_URL = "https://raw.githubusercontent.com/nicohugof/centro-paz/main/assets/instagram"

POSTS_CATALOG = {
    1: {
        "id": "post_01",
        "file": "post_01_tdah_adultos.png",
        "title": "TDAH en Adultos",
        "caption": """¿Te pasa que quieres empezar mil cosas y sientes una pared invisible que te paraliza? 🧠✨

Muchas personas adultas descubren su neurodivergencia (TDAH o TEA) después de los 25 o 30 años, tras décadas de sentirse "diferentes", agotadas o sobreexigidas sin entender por qué.

El cansancio crónico muchas veces no es flojera, sino el costo del "masking" (el esfuerzo constante de forzarte a encajar) o de un sistema nervioso sobreestimulado.

En Centro Paz no buscamos encajarte en moldes ni juzgarte: trabajamos desde un enfoque humanista y neuroafirmativo para ayudarte a:
🌿 Comprender tu funcionamiento cognitivo y sensorial singular.
🌿 Desarrollar herramientas de autorregulación respetuosas con tu energía.
🌿 Construir rutinas y estrategias reales para tu vida cotidiana y laboral.

📍 Modalidad Online (todo Chile) y Presencial (Santiago).
💳 Boletas 100% reembolsables en todas las Isapres y Seguros Complementarios.

👉 Si resuenas con esto y te gustaría agendar una primera sesión, haz clic en el enlace de nuestra biografía o escríbenos directo por WhatsApp al +56 9 6516 3893.

.
.
.
#CentroPaz #PsicologiaChile #PsicologaClinica #SaludMentalChile #TerapiaOnlineChile #ReembolsoIsapre #ValentinaCastroPsicologa #TDAHAdultos #TDAHChile #NeurodivergenciaChile #AutismoAdultos #TEAChile #PsicologiaSantiago"""
    },
    2: {
        "id": "post_02",
        "file": "post_02_reembolso_isapre.png",
        "title": "Reembolso Isapres y Seguros",
        "caption": """Cuidar tu salud mental no tiene por qué ser una carga económica abrumadora 🌿💳

En Centro Paz emitimos boletas electrónicas de honorarios profesionales con código de psicología clínica válidas para:
✨ Todas las Isapres (Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres, Nueva Masvida).
✨ Seguros Complementarios de Salud (MetLife, Bice, Bci, etc.).

El copago real puede quedar tan bajo como $15.000 por sesión según tu plan.

👉 Usa el simulador de reembolsos en nuestra web (link en bio) o escríbenos por WhatsApp al +56 9 6516 3893 para orientarte con tu cobertura."""
    },
    3: {
        "id": "post_03",
        "file": "post_03_crianza_regulacion.png",
        "title": "Crianza Respetuosa & Regulación Infantil",
        "caption": """Criar a un hijo/a con desafíos de regulación emocional o características neurodivergentes puede ser agotador cuando no se tienen las herramientas adecuadas 🌱🤍

El castigo o el aislamiento en momentos de desborde aumentan la angustia. Lo que ayuda es la corregulación: prestarle tu calma hasta que su sistema nervioso vuelva al equilibrio.

En Centro Paz acompañamos a niños, niñas y adolescentes, y brindamos orientación continua a padres para construir un hogar en calma y sin gritos.

👉 Para coordinar una primera sesión de orientación infanto-juvenil, encuéntranos en el link de la biografía o al WhatsApp +56 9 6516 3893."""
    },
    4: {
        "id": "post_04",
        "file": "post_04_masking.png",
        "title": "El Costo Invisible del Masking",
        "caption": """¿Llegas a casa después del trabajo o reuniones sintiendo que no te queda energía ni para hablar? 🧠

El "masking" es el esfuerzo consciente o inconsciente de forzar gestos, reprimir incomodidades sensoriales y actuar "como los demás esperan" para no ser juzgado/a.

En Centro Paz te acompañamos a construir un espacio seguro donde puedas desenmascarar con tranquilidad y proteger tu salud mental.

📍 Sesiones online y presenciales con boleta reembolsable en Isapres y Seguros.
👉 Agenda en el enlace de la bio o al WhatsApp +56 9 6516 3893."""
    },
    5: {
        "id": "post_05",
        "file": "post_05_terapia_online.png",
        "title": "Efectividad de la Terapia Online",
        "caption": """Atenderte desde tu habitación o espacio de calma reduce la ansiedad y elimina los tiempos de traslado 💻🌿

La terapia online cuenta con la misma rigurosidad y efectividad clínica, y recibes tu boleta electrónica exactamente igual para reembolsar en tu Isapre o Seguro.

👉 Encuentra el acompañamiento que necesitas en www.centropaz.cl (Link en Bio)."""
    },
    6: {
        "id": "post_06",
        "file": "post_06_evaluacion_infantil.png",
        "title": "Señales de Alerta en Infancia",
        "caption": """¿Cuándo es momento de consultar con una psicóloga infantil? 🌱

Desbordes intensos frecuentes, hipersensibilidad a ruidos o texturas, y dificultades de adaptación escolar son señales de que tu hijo/a necesita apoyo y tú como mamá o papá necesitas pautas clínicas claras.

👉 Contáctanos por WhatsApp al +56 9 6516 3893 para coordinar una primera sesión de orientación."""
    },
    7: {
        "id": "post_07",
        "file": "post_07_autocuidado_adultos.png",
        "title": "No tienes que poder con todo solo/a",
        "caption": """Pedir ayuda profesional no es debilidad: es reconocer que tu salud mental y tu bienestar importan ✨

50 minutos a la semana dedicados 100% a ti, con la psicóloga Valentina Castro Núñez.

👉 Da el primer paso hoy. Agenda en www.centropaz.cl o al WhatsApp +56 9 6516 3893."""
    }
}


def load_config() -> dict:
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {
        "instagram_account_id": os.environ.get("META_IG_ACCOUNT_ID", ""),
        "facebook_page_id": os.environ.get("META_FB_PAGE_ID", "61593207820690"),
        "access_token": os.environ.get("META_ACCESS_TOKEN", ""),
        "n8n_webhook_url": os.environ.get("N8N_WEBHOOK_URL", "")
    }


def save_config(cfg: dict) -> None:
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")


def http_post(url: str, data: dict) -> dict:
    encoded_data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=encoded_data, method="POST")
    req.add_header("User-Agent", "CentroPaz-AutoPublisher/1.0")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        try:
            return {"error": json.loads(body)}
        except Exception:
            return {"error": body, "status_code": e.code}


def publish_to_instagram_graph(post_num: int, config: dict) -> bool:
    ig_id = config.get("instagram_account_id")
    token = config.get("access_token")

    if not ig_id or not token:
        print("⚠️ Falta 'instagram_account_id' o 'access_token' en agent/meta_config.json")
        return False

    item = POSTS_CATALOG.get(post_num)
    if not item:
        print(f"❌ Post #{post_num} no existe en el catálogo.")
        return False

    img_url = f"{BASE_RAW_URL}/{item['file']}"
    print(f"🚀 [Meta Graph API] Publicando Post #{post_num} ({item['title']}) en Instagram...")
    print(f"   URL de imagen: {img_url}")

    # Paso 1: Crear Contenedor de Medios
    create_url = f"https://graph.facebook.com/v19.0/{ig_id}/media"
    container_res = http_post(create_url, {
        "image_url": img_url,
        "caption": item["caption"],
        "access_token": token
    })

    if "error" in container_res:
        print(f"❌ Error al crear contenedor de Instagram: {container_res['error']}")
        return False

    container_id = container_res.get("id")
    print(f"   ✓ Contenedor creado ID: {container_id}")

    # Esperar 2 segundos para procesamiento de imagen por Meta
    time.sleep(2)

    # Paso 2: Publicar el Contenedor
    publish_url = f"https://graph.facebook.com/v19.0/{ig_id}/media_publish"
    pub_res = http_post(publish_url, {
        "creation_id": container_id,
        "access_token": token
    })

    if "error" in pub_res:
        print(f"❌ Error al publicar en Instagram: {pub_res['error']}")
        return False

    print(f"🎉 ¡POST #{post_num} PUBLICADO EXITOSAMENTE EN INSTAGRAM! Post ID: {pub_res.get('id')}\n")
    return True


def publish_to_facebook_page(post_num: int, config: dict) -> bool:
    page_id = config.get("facebook_page_id", "61593207820690")
    token = config.get("access_token")

    if not page_id or not token:
        print("⚠️ Falta 'facebook_page_id' o 'access_token' en agent/meta_config.json")
        return False

    item = POSTS_CATALOG.get(post_num)
    if not item:
        return False

    img_url = f"{BASE_RAW_URL}/{item['file']}"
    print(f"🚀 [Meta Graph API] Publicando Post #{post_num} en la página de Facebook...")

    fb_url = f"https://graph.facebook.com/v19.0/{page_id}/photos"
    res = http_post(fb_url, {
        "url": img_url,
        "caption": item["caption"],
        "access_token": token
    })

    if "error" in res:
        print(f"❌ Error al publicar en Facebook: {res['error']}")
        return False

    print(f"🎉 ¡POST #{post_num} PUBLICADO EN FACEBOOK! Post ID: {res.get('id') or res.get('post_id')}\n")
    return True


def trigger_n8n_webhook(webhook_url: str, post_num: int = 1) -> None:
    item = POSTS_CATALOG.get(post_num, POSTS_CATALOG[1])
    payload = {
        "brand": content_engine.BRAND,
        "post_number": post_num,
        "title": item["title"],
        "image_url": f"{BASE_RAW_URL}/{item['file']}",
        "caption": item["caption"],
        "target_platforms": ["instagram", "facebook", "tiktok"],
        "status": "ready_to_publish",
        "timestamp": int(time.time())
    }

    print(f"📡 Disparando Webhook hacia n8n ({webhook_url})...")
    req = urllib.request.Request(
        webhook_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "CentroPaz-Agent/1.0"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"✅ Webhook procesado exitosamente por n8n (Status {resp.status})")
    except Exception as e:
        print(f"❌ Error conectando con n8n: {e}")


def main():
    parser = argparse.ArgumentParser(description="Centro Paz — Publicador Automático de Redes Sociales")
    parser.add_argument("--post", type=int, choices=range(1, 8), help="Número de post a publicar (1 al 7)")
    parser.add_argument("--platform", choices=["all", "instagram", "facebook"], default="all", help="Plataforma de destino")
    parser.add_argument("--webhook-url", type=str, help="Disparar webhook a n8n / Make")
    parser.add_argument("--set-token", type=str, help="Guardar Meta Graph API Access Token")
    parser.add_argument("--set-ig-id", type=str, help="Guardar Instagram Account ID")
    parser.add_argument("--list", action="store_true", help="Listar publicaciones disponibles")
    args = parser.parse_args()

    config = load_config()

    if args.set_token:
        config["access_token"] = args.set_token
        save_config(config)
        print("✅ Access Token guardado en agent/meta_config.json")
        return

    if args.set_ig_id:
        config["instagram_account_id"] = args.set_ig_id
        save_config(config)
        print("✅ Instagram Account ID guardado en agent/meta_config.json")
        return

    if args.list or not any(vars(args).values()):
        print("\n" + "=" * 65)
        print(" 🌿 CENTRO PAZ (CPAZ) — CATÁLOGO DE POSTS AUTOMATIZABLES")
        print("=" * 65)
        for num, p in POSTS_CATALOG.items():
            print(f" 📌 Post #{num}: {p['title']}  ({p['file']})")
        print("=" * 65 + "\n")
        return

    if args.webhook_url:
        trigger_n8n_webhook(args.webhook_url, args.post or 1)
        return

    if args.post:
        if args.platform in ["all", "instagram"]:
            publish_to_instagram_graph(args.post, config)
        if args.platform in ["all", "facebook"]:
            publish_to_facebook_page(args.post, config)


if __name__ == "__main__":
    main()
