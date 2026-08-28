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
def build_posts_catalog() -> dict:
    catalog = {}
    for key, topic in content_engine.TOPICS.items():
        num = topic["id"]
        catalog[num] = {
            "id": f"post_{num:02d}",
            "key": key,
            "file": f"post_{num:02d}_{key}.png",
            "title": topic["title"],
            "caption": topic["caption"],
            "category": topic["category"],
            "hashtags": " ".join(topic["hashtags"])
        }
    return catalog


POSTS_CATALOG = build_posts_catalog()



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


def http_get(url: str) -> dict:
    req = urllib.request.Request(url, method="GET")
    req.add_header("User-Agent", "CentroPaz-AutoPublisher/1.0")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        try:
            return {"error": json.loads(body)}
        except Exception:
            return {"error": body, "status_code": e.code}
    except Exception as e:
        return {"error": str(e)}


def http_post(url: str, data: dict) -> dict:
    encoded_data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=encoded_data, method="POST")
    req.add_header("User-Agent", "CentroPaz-AutoPublisher/1.0")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        try:
            return {"error": json.loads(body)}
        except Exception:
            return {"error": body, "status_code": e.code}
    except Exception as e:
        return {"error": str(e)}


def test_connection(config: dict) -> bool:
    token = config.get("access_token")
    if not token:
        print("⚠️ Falta 'access_token' en agent/meta_config.json o META_ACCESS_TOKEN")
        return False
    print("🔌 Verificando token con Meta Graph API...")
    me = http_get(f"https://graph.facebook.com/v19.0/me?fields=id,name&access_token={urllib.parse.quote(token)}")
    if "error" in me:
        print(f"❌ Token inválido: {me['error']}")
        return False
    print(f"   ✓ Token válido. App/usuario: {me.get('name')} ({me.get('id')})")
    ig_id = config.get("instagram_account_id")
    if ig_id:
        ig = http_get(
            f"https://graph.facebook.com/v19.0/{urllib.parse.quote(str(ig_id))}"
            f"?fields=id,username&access_token={urllib.parse.quote(token)}"
        )
        if "error" in ig:
            print(f"⚠️ Instagram Account ID no accesible: {ig['error']}")
        else:
            print(f"   ✓ Instagram: @{ig.get('username', ig.get('id'))}")
    page_id = config.get("facebook_page_id")
    if page_id:
        page = http_get(
            f"https://graph.facebook.com/v19.0/{urllib.parse.quote(str(page_id))}"
            f"?fields=id,name&access_token={urllib.parse.quote(token)}"
        )
        if "error" in page:
            print(f"⚠️ Facebook Page ID no accesible: {page['error']}")
        else:
            print(f"   ✓ Facebook Page: {page.get('name')} ({page.get('id')})")
    return True


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


def publish_one(post_num: int, config: dict, platform: str) -> None:
    if platform in ["all", "instagram"]:
        publish_to_instagram_graph(post_num, config)
    if platform in ["all", "facebook"]:
        publish_to_facebook_page(post_num, config)


def main():
    max_posts = len(POSTS_CATALOG)
    parser = argparse.ArgumentParser(description="Centro Paz — Publicador Automático de Redes Sociales")
    parser.add_argument("--post", type=int, choices=range(1, max_posts + 1), help=f"Número de post a publicar (1 al {max_posts})")
    parser.add_argument("--post-all", action="store_true", help=f"Publicar toda la parrilla (posts 1 al {max_posts}) con pausa entre cada uno")
    parser.add_argument("--platform", choices=["all", "instagram", "facebook"], default="all", help="Plataforma de destino")
    parser.add_argument("--webhook-url", type=str, help="Disparar webhook a n8n / Make")
    parser.add_argument("--set-token", type=str, help="Guardar Meta Graph API Access Token")
    parser.add_argument("--set-ig-id", type=str, help="Guardar Instagram Account ID")
    parser.add_argument("--test-connection", action="store_true", help="Verificar tokens y conexión con Meta Graph API")
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

    if args.test_connection:
        test_connection(config)
        return

    no_action = not (
        args.list or args.post or args.post_all or args.webhook_url
        or args.set_token or args.set_ig_id or args.test_connection
    )
    if args.list or no_action:
        print("\n" + "=" * 70)
        print(f" 🌿 CENTRO PAZ (CPAZ) — CATÁLOGO DE {max_posts} POSTS AUTOMATIZABLES")
        print("=" * 70)
        for num, p in sorted(POSTS_CATALOG.items()):
            print(f" 📌 Post #{num:02d}: {p['title']}  ({p['file']})")
        print("=" * 70 + "\n")
        return

    if args.webhook_url:
        trigger_n8n_webhook(args.webhook_url, args.post or 1)
        return

    if args.post_all:
        for n in sorted(POSTS_CATALOG.keys()):
            publish_one(n, config, args.platform)
            if n < max(POSTS_CATALOG.keys()):
                time.sleep(5)
        return

    if args.post:
        publish_one(args.post, config, args.platform)


if __name__ == "__main__":
    main()

