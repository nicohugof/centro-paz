#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Motor de Publicación Automática Multi-Slot (Meta Graph API & n8n).

Mecanismo estándar para publicación autónoma en 2 momentos diarios clave:
  1. Slot Mediodía (12:00 CLT): Infografía Educativa de Alto Valor (Feed Instagram + Facebook)
  2. Slot Tarde/Noche (18:30 CLT): Video Vertical / Reel de 30-40s (Reels Instagram + Video Facebook)

Uso:
  python3 -m agent.auto_publisher --auto-slot              (Detecta la hora y publica el contenido del slot actual)
  python3 -m agent.auto_publisher --slot feed             (Publica la infografía del día en el Feed)
  python3 -m agent.auto_publisher --slot reel             (Publica el video vertical del día como Reel)
  python3 -m agent.auto_publisher --slot both             (Ejecuta ambos slots en secuencia)
  python3 -m agent.auto_publisher --video 1               (Publica el video 1 manualmente)
  python3 -m agent.auto_publisher --post 1                (Publica la infografía 1 manualmente)
  python3 -m agent.auto_publisher --dry-run --auto-slot   (Modo simulación sin llamar a las APIs de Meta)
"""
from __future__ import annotations

import argparse
import datetime
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
BASE_VIDEO_RAW_URL = "https://raw.githubusercontent.com/nicohugof/centro-paz/main/assets/videos"


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

VIDEOS_CATALOG = {
    1: {
        "file": "cpaz_short01_tdah.mp4",
        "title": "3 señales de TDAH en adultos que sueles confundir con flojera",
        "caption": """¿Y si tu cansancio no es flojera, sino TDAH en la adultez? 🧠

La procrastinación y la fatiga mental en personas con TDAH tienen una raíz fisiológica, no moral. En Centro Paz acompañamos desde un enfoque neuroafirmativo para devolverte el control sin juicios ni culpa.

🌿 Modalidad Online (desde 12 años) para todo Chile y Presencial en Ñuñoa.
💳 Boletas reembolsables en todas las Isapres y Seguros.

👉 Escríbenos directamente por WhatsApp al +56 9 6516 3893 o ingresa a www.centropaz.cl

#CentroPaz #TDAHAdultos #TDAHChile #SaludMentalChile #Neurodivergencia #PsicologiaChile #PsicologiaÑuñoa #ReelsChile"""
    },
    2: {
        "file": "cpaz_short02_isapre.mp4",
        "title": "La matemática secreta del reembolso de Isapre en psicología",
        "caption": """La matemática real del reembolso en salud mental 💡💳

¿Sabías que una consulta de .000 puede quedarte en un copago real de entre .000 y .000 CLP según tu plan de Isapre? Emitimos boletas electrónicas oficiales para tramitar el reembolso digital en minutos.

👉 Simula tu reembolso en www.centropaz.cl o escríbenos a WhatsApp al +56 9 6516 3893.

#CentroPaz #ReembolsoIsapre #IsapresChile #SaludMentalChile #PsicologiaChile #Colmena #CruzBlanca #Banmedica #Consalud"""
    },
    3: {
        "file": "cpaz_short03_crianza.mp4",
        "title": "Qué hacer ante una rabieta o sobrecarga sensorial en niños",
        "caption": """Una rabieta infantil intensa no es manipulación: es sobrecarga de su sistema nervioso 🌱

Cuando un niño entra en crisis, su cerebro racional se apaga. Castigar o gritar solo aumenta la alarma. La corregulación de los padres es el único puente seguro hacia la calma.

🌿 Atención infantil presencial en sala lúdica en Ñuñoa y orientación online a padres en todo Chile.

👉 Escríbenos a WhatsApp al +56 9 6516 3893 o visita www.centropaz.cl

#CentroPaz #CrianzaRespetuosa #PsicologiaInfantil #TEAInfantil #TDAHInfantil #OrientacionAPadres #PsicologiaÑuñoa"""
    },
    4: {
        "file": "cpaz_short04_burnout_autista.mp4",
        "title": "Burnout Autista vs. Estrés común: Por qué descansar un fin de semana no alcanza",
        "caption": """Llegar a casa sin poder hablar: ¿Estrés común o Burnout Autista? 🧠

El agotamiento autista ocurre tras meses o años de forzarte a encajar y hacer 'masking'. No se soluciona durmiendo un fin de semana: requiere reestructurar demandas sensoriales y acompañamiento neuroafirmativo.

👉 Escríbenos a WhatsApp al +56 9 6516 3893 o visita www.centropaz.cl

#CentroPaz #BurnoutAutista #TEAAdultos #AutismoChile #Neurodivergencia #PsicologiaChile #SaludMentalChile"""
    },
    5: {
        "file": "cpaz_short05_tdah_mujeres.mp4",
        "title": "Por qué el TDAH en mujeres se diagnostica recién a los 30 años",
        "caption": """¿Por qué tantas mujeres reciben su diagnóstico de TDAH recién a los 30 años? 🌸

Durante décadas el TDAH se asoció a niños hiperactivos. En mujeres adultas suele manifestarse como sobrepensamiento incesante, perfeccionismo agotador y culpa constante.

👉 Agenda con la psicóloga Valentina Castro Núñez. WhatsApp: +56 9 6516 3893 o en www.centropaz.cl

#CentroPaz #TDAHMujeres #TDAHAdultos #SaludMentalFemenina #PsicologiaChile #ReembolsoIsapre"""
    },
    6: {
        "file": "cpaz_short06_rsd.mp4",
        "title": "Sensibilidad al Rechazo (RSD): Por qué una crítica duele físicamente",
        "caption": """¿Por qué una pequeña crítica o un silencio te duele físicamente? 💔

La Disforia Sensible al Rechazo (RSD) es una respuesta neurológica intensa muy común en el TDAH. No eres 'exagerado/a': tu cerebro procesa el rechazo percibido como una amenaza física real.

👉 Acompañamiento neuroafirmativo en Centro Paz. WhatsApp: +56 9 6516 3893 o en www.centropaz.cl

#CentroPaz #RSD #SensibilidadAlRechazo #TDAHChile #SaludMentalChile #Neurodivergencia"""
    },
    7: {
        "file": "cpaz_short07_sobrecarga.mp4",
        "title": "Hipersensibilidad al Ruido y Sobrecarga Sensorial",
        "caption": """El centro comercial, la oficina o el metro te drenan la energía por completo 🎧

La hipersensibilidad acústica no es mal genio: es un filtro sensorial que no discrimina estímulos. Aprender a regular tu entorno y proteger tu sistema nervioso es vital para tu bienestar.

👉 Conoce más en www.centropaz.cl o escríbenos a WhatsApp al +56 9 6516 3893.

#CentroPaz #SobrecargaSensorial #Hipersensibilidad #TEAAdultos #TDAHChile #PsicologiaÑuñoa"""
    },
    8: {
        "file": "cpaz_short08_ansiedad_somatica.mp4",
        "title": "Ansiedad Somática: Cuando el cuerpo habla lo que la mente calla",
        "caption": """Nudo en la garganta, opresión en el pecho, bruxismo o molestias estomacales 🌊🌿

Cuando intentas ignorar lo que sientes, tu cuerpo se encarga de manifestarlo. En terapia integrativa trabajamos la conexión mente-cuerpo para desactivar la alarma fisiológica de la ansiedad.

👉 Agenda tu sesión en www.centropaz.cl o al WhatsApp +56 9 6516 3893.

#CentroPaz #AnsiedadSomatica #PsicoterapiaIntegrativa #SaludMentalChile #PsicologaClinica"""
    },
    9: {
        "file": "cpaz_short09_terapia_infantil.mp4",
        "title": "Por qué los niños no van al psicólogo a hablar sentados",
        "caption": """¿Por qué los niños no van al psicólogo a hablar sentados en un diván? 🧸🎨

El lenguaje natural de la infancia es el juego. A través de figuras, historias y dinámicas lúdicas, expresan miedos y emociones que aún no pueden formular en palabras.

📍 Terapia infantil presencial en sala lúdica en Ñuñoa.

👉 Escríbenos directamente por WhatsApp al +56 9 6516 3893 o visita www.centropaz.cl

#CentroPaz #TerapiaInfantil #PsicologiaInfantil #CrianzaRespetuosa #Ñuñoa #PsicologiaÑuñoa"""
    },
    10: {
        "file": "cpaz_short10_dopamina.mp4",
        "title": "El ciclo de pantallas y TDAH: Romper el bucle de dopamina sin culpa",
        "caption": """Abrir una app 'solo por 5 minutos' y quedar atrapado 2 horas en el teléfono 📱🧠

Para un cerebro con menor dopamina basal, el scroll infinito es un dispensador irresistible. Salir del bucle no requiere castigarte, sino diseñar micro-fricciones ambientales inteligentes.

👉 Pautas prácticas en Centro Paz. WhatsApp: +56 9 6516 3893 o en www.centropaz.cl

#CentroPaz #Doomscrolling #TDAHAdultos #Dopamina #SaludMentalChile #PsicologiaChile"""
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


def http_get(url: str) -> dict:
    req = urllib.request.Request(url, method="GET")
    req.add_header("User-Agent", "CentroPaz-AutoPublisher/2.0")
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
    req.add_header("User-Agent", "CentroPaz-AutoPublisher/2.0")
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
    """Publica imagen en el Feed de Instagram."""
    ig_id = config.get("instagram_account_id")
    token = config.get("access_token")

    if not ig_id or not token:
        print("⚠️ Falta 'instagram_account_id' o 'access_token' en configuración de Meta.")
        return False

    item = POSTS_CATALOG.get(post_num)
    if not item:
        print(f"❌ Post #{post_num} no existe en el catálogo.")
        return False

    img_url = f"{BASE_RAW_URL}/{item['file']}"
    print(f"🚀 [Meta Graph API] Publicando Feed Post #{post_num} ({item['title']}) en Instagram...")
    print(f"   URL de imagen: {img_url}")

    create_url = f"https://graph.facebook.com/v19.0/{ig_id}/media"
    container_res = http_post(create_url, {
        "image_url": img_url,
        "caption": item["caption"],
        "access_token": token
    })

    if "error" in container_res:
        print(f"❌ Error al crear contenedor de imagen en Instagram: {container_res['error']}")
        return False

    container_id = container_res.get("id")
    print(f"   ✓ Contenedor creado ID: {container_id}")
    time.sleep(3)

    publish_url = f"https://graph.facebook.com/v19.0/{ig_id}/media_publish"
    pub_res = http_post(publish_url, {
        "creation_id": container_id,
        "access_token": token
    })

    if "error" in pub_res:
        print(f"❌ Error al publicar imagen en Instagram: {pub_res['error']}")
        return False

    print(f"🎉 ¡FEED POST #{post_num} PUBLICADO EN INSTAGRAM! ID: {pub_res.get('id')}")
    return True


def publish_reel_to_instagram_graph(video_num: int, config: dict) -> bool:
    """Publica video vertical como REEL en Instagram."""
    ig_id = config.get("instagram_account_id")
    token = config.get("access_token")

    if not ig_id or not token:
        print("⚠️ Falta 'instagram_account_id' o 'access_token' para Reels en Instagram.")
        return False

    item = VIDEOS_CATALOG.get(video_num)
    if not item:
        print(f"❌ Video #{video_num} no existe en el catálogo.")
        return False

    video_url = f"{BASE_VIDEO_RAW_URL}/{item['file']}"
    print(f"🎬 [Meta Graph API] Publicando REEL #{video_num} ({item['title']}) en Instagram...")
    print(f"   URL de video: {video_url}")

    # Paso 1: Crear Contenedor REELS
    create_url = f"https://graph.facebook.com/v19.0/{ig_id}/media"
    container_res = http_post(create_url, {
        "media_type": "REELS",
        "video_url": video_url,
        "caption": item["caption"],
        "share_to_feed": "true",
        "access_token": token
    })

    if "error" in container_res:
        print(f"❌ Error al crear contenedor de Reel en Instagram: {container_res['error']}")
        return False

    container_id = container_res.get("id")
    print(f"   ✓ Contenedor Reel creado ID: {container_id}. Esperando procesamiento...")

    # Paso 2: Verificar estado de codificación de Meta
    for attempt in range(1, 11):
        time.sleep(5)
        status_res = http_get(f"https://graph.facebook.com/v19.0/{container_id}?fields=status_code&access_token={urllib.parse.quote(token)}")
        code = status_res.get("status_code")
        print(f"   [Intento {attempt}/10] Estado de procesamiento: {code}")
        if code == "FINISHED":
            break
        elif code in ["ERROR", "EXPIRED"]:
            print(f"❌ Procesamiento fallido por Meta: {status_res}")
            return False

    # Paso 3: Publicar Reel
    publish_url = f"https://graph.facebook.com/v19.0/{ig_id}/media_publish"
    pub_res = http_post(publish_url, {
        "creation_id": container_id,
        "access_token": token
    })

    if "error" in pub_res:
        print(f"❌ Error al publicar Reel en Instagram: {pub_res['error']}")
        return False

    print(f"🎉 ¡REEL #{video_num} PUBLICADO EXITOSAMENTE EN INSTAGRAM! ID: {pub_res.get('id')}")
    return True


def publish_to_facebook_page(post_num: int, config: dict) -> bool:
    page_id = config.get("facebook_page_id", "61593207820690")
    token = config.get("access_token")
    if not page_id or not token:
        return False

    item = POSTS_CATALOG.get(post_num)
    if not item:
        return False

    img_url = f"{BASE_RAW_URL}/{item['file']}"
    print(f"🚀 [Meta Graph API] Publicando Foto #{post_num} en Facebook Page...")
    res = http_post(f"https://graph.facebook.com/v19.0/{page_id}/photos", {
        "url": img_url,
        "caption": item["caption"],
        "access_token": token
    })
    if "error" in res:
        print(f"❌ Error Facebook: {res['error']}")
        return False
    print(f"🎉 ¡FOTO #{post_num} EN FACEBOOK! ID: {res.get('id') or res.get('post_id')}")
    return True


def publish_video_to_facebook_page(video_num: int, config: dict) -> bool:
    page_id = config.get("facebook_page_id", "61593207820690")
    token = config.get("access_token")
    if not page_id or not token:
        return False

    item = VIDEOS_CATALOG.get(video_num)
    if not item:
        return False

    video_url = f"{BASE_VIDEO_RAW_URL}/{item['file']}"
    print(f"🎬 [Meta Graph API] Publicando Video #{video_num} en Facebook Page...")
    res = http_post(f"https://graph.facebook.com/v19.0/{page_id}/videos", {
        "file_url": video_url,
        "description": item["caption"],
        "title": item["title"],
        "access_token": token
    })
    if "error" in res:
        print(f"❌ Error Video Facebook: {res['error']}")
        return False
    print(f"🎉 ¡VIDEO #{video_num} EN FACEBOOK! ID: {res.get('id')}")
    return True


def get_current_slot_post_num() -> int:
    base_date = datetime.date(2026, 9, 8)
    today = datetime.date.today()
    diff = max(0, (today - base_date).days)
    return (diff % len(POSTS_CATALOG)) + 1


def get_current_slot_video_num() -> int:
    base_date = datetime.date(2026, 9, 8)
    today = datetime.date.today()
    diff = max(0, (today - base_date).days)
    return (diff % len(VIDEOS_CATALOG)) + 1


def get_auto_slot_type() -> str:
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    clt_hour = (now_utc.hour - 3) % 24
    if clt_hour >= 15:
        return "reel"
    return "feed"


def execute_feed_slot(post_num: int, config: dict, dry_run: bool) -> None:
    item = POSTS_CATALOG[post_num]
    print(f"📅 [Slot Feed - 12:00 CLT] Post #{post_num:02d}: '{item['title']}'")
    print(f"   Archivo de imagen: {item['file']}")
    if dry_run:
        print(f"   🧪 [DRY-RUN] Simulación exitosa para Feed Post #{post_num:02d}. Sin llamadas de red.")
        return
    token = config.get("access_token")
    if not token:
        print("   ℹ️ Sin credenciales de Meta Graph API. El contenido se mantiene en web/blog.")
        return
    publish_to_instagram_graph(post_num, config)
    publish_to_facebook_page(post_num, config)


def execute_reel_slot(video_num: int, config: dict, dry_run: bool) -> None:
    item = VIDEOS_CATALOG[video_num]
    print(f"🎬 [Slot Reel - 18:30 CLT] Video #{video_num:02d}: '{item['title']}'")
    print(f"   Archivo de video: {item['file']}")
    if dry_run:
        print(f"   🧪 [DRY-RUN] Simulación exitosa para Reel #{video_num:02d}. Sin llamadas de red.")
        return
    token = config.get("access_token")
    if not token:
        print("   ℹ️ Sin credenciales de Meta Graph API. El contenido se mantiene en web/blog.")
        return
    publish_reel_to_instagram_graph(video_num, config)
    publish_video_to_facebook_page(video_num, config)


def main():
    max_posts = len(POSTS_CATALOG)
    max_videos = len(VIDEOS_CATALOG)
    parser = argparse.ArgumentParser(description="Centro Paz — Motor de Publicación Multi-Slot")
    parser.add_argument("--auto-slot", action="store_true", help="Detectar automáticamente si corresponde Feed (mediodía) o Reel (tarde)")
    parser.add_argument("--slot", choices=["feed", "reel", "both", "auto"], default="auto", help="Forzar slot específico de publicación")
    parser.add_argument("--dry-run", action="store_true", help="Modo simulación sin publicar en Meta")
    parser.add_argument("--post", type=int, choices=range(1, max_posts + 1), help="Publicar infografía específica")
    parser.add_argument("--video", type=int, choices=range(1, max_videos + 1), help="Publicar video vertical específico")
    parser.add_argument("--list", action="store_true", help="Listar las 28 infografías")
    parser.add_argument("--list-videos", action="store_true", help="Listar los 10 videos verticales")
    parser.add_argument("--test-connection", action="store_true", help="Verificar tokens de Meta")
    args = parser.parse_args()

    config = load_config()

    if args.test_connection:
        test_connection(config)
        return

    if args.list:
        print("\n" + "=" * 70)
        print(f" 🌿 CENTRO PAZ — CATÁLOGO DE {max_posts} INFOGRAFÍAS (SLOT FEED)")
        print("=" * 70)
        for num, p in sorted(POSTS_CATALOG.items()):
            print(f" 📌 Post #{num:02d}: {p['title']} ({p['file']})")
        print("=" * 70 + "\n")
        return

    if args.list_videos:
        print("\n" + "=" * 70)
        print(f" 🎬 CENTRO PAZ — CATÁLOGO DE {max_videos} VIDEOS VERTICALES (SLOT REEL)")
        print("=" * 70)
        for num, v in sorted(VIDEOS_CATALOG.items()):
            print(f" 🎥 Video #{num:02d}: {v['title']} ({v['file']})")
        print("=" * 70 + "\n")
        return

    if args.post:
        execute_feed_slot(args.post, config, args.dry_run)
        return

    if args.video:
        execute_reel_slot(args.video, config, args.dry_run)
        return

    # Determinación de Slot
    target_slot = args.slot
    if target_slot == "auto" or args.auto_slot:
        target_slot = get_auto_slot_type()

    cur_post = get_current_slot_post_num()
    cur_video = get_current_slot_video_num()

    if target_slot in ["feed", "both"]:
        execute_feed_slot(cur_post, config, args.dry_run)
    if target_slot in ["reel", "both"]:
        execute_reel_slot(cur_video, config, args.dry_run)


if __name__ == "__main__":
    main()
