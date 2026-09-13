#!/usr/bin/env python3
"""
Genera los archivos para el pack de la semana 3 (2026-09-22 a 2026-09-28):
- marketing/pack-semana-2026-09-22/pack_semana_n8n.json
- marketing/pack-semana-2026-09-22/LEEME.md
"""
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from agent import content_engine

ROOT = Path(__file__).resolve().parent.parent
target_dir = ROOT / "marketing" / "pack-semana-2026-09-22"
target_dir.mkdir(parents=True, exist_ok=True)

cal3 = content_engine.get_weekly_calendar(week=3)
brand = content_engine.BRAND

dates = [
    ("2026-09-22", "Lunes", "cpaz_short05_tdah_mujeres_es_local.mp4"),
    ("2026-09-23", "Martes", "cpaz_short07_sobrecarga_es_local.mp4"),
    ("2026-09-24", "Miércoles", "cpaz_short02_isapre_es_local.mp4"),
    ("2026-09-25", "Jueves", "cpaz_short01_tdah_es_local.mp4"),
    ("2026-09-26", "Viernes", "cpaz_short03_crianza_es_local.mp4"),
    ("2026-09-27", "Sábado", "cpaz_short04_burnout_autista_es_local.mp4"),
    ("2026-09-28", "Domingo", "cpaz_short06_rsd_es_local.mp4")
]

posts_json = []
for (fec, dia_name, video_file), item in zip(dates, cal3):
    posts_json.append({
        "fecha": fec,
        "dia": dia_name,
        "hora_feed": "12:00",
        "hora_stories": "07:30 / 21:00",
        "hora_reel_tiktok": "18:00",
        "topic_key": item["topic_key"],
        "image_file": f"post_{item['id']:02d}_{item['topic_key']}.png",
        "image_url": f"https://www.centropaz.cl/assets/instagram/post_{item['id']:02d}_{item['topic_key']}.png",
        "video_vertical": video_file,
        "caption": item["copy"],
        "hashtags": item["hashtags"],
        "cta_whatsapp": "https://wa.me/56965163893",
        "cta_web": "https://www.centropaz.cl",
        "cta_links": "https://www.centropaz.cl/links",
        "platforms": ["instagram", "facebook", "tiktok", "youtube_shorts"]
    })

data = {
    "week_start": "2026-09-22",
    "week_end": "2026-09-28",
    "timezone": "America/Santiago",
    "brand": {
        "name": brand["name"],
        "therapist": brand["therapist"],
        "title": brand["title"],
        "registration": brand["registration"],
        "approach": brand["approach"],
        "phone": brand["phone"],
        "phone_display": brand["phone_display"],
        "email": brand["email"],
        "instagram": brand["instagram"],
        "tiktok": brand["tiktok"],
        "facebook": brand["facebook"],
        "web": brand["web"],
        "wa_link": brand["wa_link"],
        "links_hub": "https://www.centropaz.cl/links",
        "isapres": brand["isapres"],
        "session_price": brand["session_price"],
        "location": brand["location"]
    },
    "posts": posts_json,
    "whatsapp_note": "PERSONAL Valentina Castro Núñez (+56 9 6516 3893) — Atención directa a pacientes. Sin bots ni respuestas automáticas.",
    "status": "ready_for_publish"
}

(target_dir / "pack_semana_n8n.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

lines = [
    "# Pack de publicación — semana 2026-09-22 → 2026-09-28\n",
    "Guía operativa para publicar Centro Paz en Semana 3. Zona horaria: **America/Santiago**.\n",
    "No inventar claims clínicos ni testimonios. Usar solo el copy y los hashtags de `agent/content_engine.py` (`calendar_week_3`). Las piezas estáticas PNG ya están en `assets/instagram/` y los videos verticales 9:16 en `output/` de YouTube IA.\n",
    "## Contacto y marca\n",
    "| Campo | Valor |",
    "| :--- | :--- |",
    "| CTA WhatsApp | **PERSONAL de Valentina Castro Núñez** · `+56 9 6516 3893` · [wa.me/56965163893](https://wa.me/56965163893) |",
    "| Web Principal | [https://www.centropaz.cl](https://www.centropaz.cl) |",
    "| Link en Bio Oficial | [https://www.centropaz.cl/links](https://www.centropaz.cl/links) |",
    "| Instagram / TikTok | `@centropaz.cl` |\n",
    "**Regla estricta de atención:** Valentina atiende directamente a todos los pacientes. No utilizar bots ni respuestas rápidas en WhatsApp. Cero cruce con Ironcross.\n",
    "JSON listo para n8n: [`pack_semana_n8n.json`](./pack_semana_n8n.json).\n",
    "## Ritmo diario (America/Santiago)\n",
    "| Hora | Pieza | Dónde | Video Corto Asociado (YouTube IA) |",
    "| :--- | :--- | :--- | :--- |",
    "| 07:30 | Stories | Instagram (+ Facebook Stories) | — |",
    "| 12:00 | Feed (Estático) | Instagram + Facebook | Publicación automática / manual de infografía del día |",
    "| 18:00 | Reel · TikTok · Shorts | Instagram Reels, TikTok, YouTube Shorts | **Video Vertical 9:16 de YouTube IA (ver asignación diaria abajo)** |",
    "| 21:00 | Stories | Instagram (+ Facebook Stories) | Repost del Reel o sticker directo a `centropaz.cl/links` |\n",
    "En stories: gancho del día + sticker de WhatsApp o enlace a `https://www.centropaz.cl/links`. En feed: caption + hashtags de abajo. En Reel/TikTok/Shorts: video vertical de YouTube IA con comentario fijado hacia WhatsApp.\n"
]

for (fec, dia_name, video_file), item in zip(dates, cal3):
    img_file = f"post_{item['id']:02d}_{item['topic_key']}.png"
    lines.append("---\n")
    lines.append(f"## {dia_name} {fec} — `{img_file}`\n")
    lines.append(f"- **Pieza Feed (12:00):** [`assets/instagram/{img_file}`](../../assets/instagram/{img_file})")
    lines.append(f"- **Video Reels / Shorts / TikTok (18:00):** `{video_file}` (generado en YouTube IA)")
    lines.append(f"- **URL Feed:** https://www.centropaz.cl/assets/instagram/{img_file}")
    lines.append(f"- **topic_key:** `{item['topic_key']}`\n")
    lines.append("**Caption**\n")
    lines.append("```text")
    lines.append(item["copy"])
    lines.append("```\n")
    lines.append("**Hashtags**\n")
    lines.append(f"`{item['hashtags']}`\n")

(target_dir / "LEEME.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("✅ Pack semana 2026-09-22 generado correctamente en marketing/pack-semana-2026-09-22/")
