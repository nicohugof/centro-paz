#!/usr/bin/env python3
"""
Genera los archivos para el pack de la semana 2 (2026-09-15 a 2026-09-21):
- marketing/pack-semana-2026-09-15/pack_semana_n8n.json
- marketing/pack-semana-2026-09-15/LEEME.md
"""
import json
from pathlib import Path
from agent import content_engine

ROOT = Path(__file__).resolve().parent.parent
target_dir = ROOT / "marketing" / "pack-semana-2026-09-15"
target_dir.mkdir(parents=True, exist_ok=True)

cal2 = content_engine.get_weekly_calendar(week=2)
brand = content_engine.BRAND

dates = [
    ("2026-09-15", "Lunes"),
    ("2026-09-16", "Martes"),
    ("2026-09-17", "Miércoles"),
    ("2026-09-18", "Jueves"),
    ("2026-09-19", "Viernes"),
    ("2026-09-20", "Sábado"),
    ("2026-09-21", "Domingo")
]

posts_json = []
for (fec, dia_name), item in zip(dates, cal2):
    posts_json.append({
        "fecha": fec,
        "dia": dia_name,
        "hora_feed": "12:00",
        "hora_stories": "07:30 / 21:00",
        "hora_reel_tiktok": "18:00",
        "topic_key": item["topic_key"],
        "image_file": f"post_{item['id']:02d}_{item['topic_key']}.png",
        "image_url": f"https://www.centropaz.cl/assets/instagram/post_{item['id']:02d}_{item['topic_key']}.png",
        "caption": item["copy"],
        "hashtags": item["hashtags"],
        "cta_whatsapp": "https://wa.me/56965163893",
        "cta_web": "https://www.centropaz.cl",
        "platforms": ["instagram", "facebook", "tiktok"]
    })

data = {
    "week_start": "2026-09-15",
    "week_end": "2026-09-21",
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
        "isapres": brand["isapres"],
        "session_price": brand["session_price"],
        "location": brand["location"]
    },
    "posts": posts_json,
    "whatsapp_note": "PERSONAL Valentina — Centro Paz only",
    "status": "ready_for_publish"
}

(target_dir / "pack_semana_n8n.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

lines = [
    "# Pack de publicación — semana 2026-09-15 → 2026-09-21\n",
    "Guía corta para publicar Centro Paz esta semana (Semana 2). Zona horaria: **America/Santiago**.\n",
    "No inventar claims clínicos ni testimonios. Usar solo el copy y los hashtags de `agent/n8n_marketing_payload.json` (`calendar_week_2` + `posts_catalog`). Las piezas PNG ya están en `assets/instagram/`.\n",
    "## Contacto y marca\n",
    "| Campo | Valor |",
    "| :--- | :--- |",
    "| CTA WhatsApp | **PERSONAL de Valentina Castro Núñez** · `+56 9 6516 3893` · [wa.me/56965163893](https://wa.me/56965163893) |",
    "| Web | [https://www.centropaz.cl](https://www.centropaz.cl) |",
    "| Instagram / TikTok | `@centropaz.cl` |\n",
    "**Nunca** usar este WhatsApp para Ironcross ni ironcross-web. Solo Centro Paz.\n",
    "JSON listo para n8n: [`pack_semana_n8n.json`](./pack_semana_n8n.json).\n",
    "## Ritmo diario (America/Santiago)\n",
    "| Hora | Pieza | Dónde |",
    "| :--- | :--- | :--- |",
    "| 07:30 | Stories | Instagram (+ Facebook Stories si está conectado) |",
    "| 12:00 | Feed | Instagram + Facebook |",
    "| 18:00 | Reel = TikTok | Mismo video/pieza en Instagram Reels y TikTok |",
    "| 21:00 | Stories | Instagram (+ Facebook Stories si está conectado) |\n",
    "En stories: gancho del día + sticker de WhatsApp o enlace a `https://wa.me/56965163893`. En feed: caption + hashtags de abajo. En Reel/TikTok: el mismo gancho, CTA a bio / WhatsApp.\n"
]

for (fec, dia_name), item in zip(dates, cal2):
    img_file = f"post_{item['id']:02d}_{item['topic_key']}.png"
    lines.append("---\n")
    lines.append(f"## {dia_name} {fec} — `{img_file}`\n")
    lines.append(f"- **Archivo:** [`assets/instagram/{img_file}`](../../assets/instagram/{img_file})")
    lines.append(f"- **URL:** https://www.centropaz.cl/assets/instagram/{img_file}")
    lines.append(f"- **topic_key:** `{item['topic_key']}`\n")
    lines.append("**Caption**\n")
    lines.append("```text")
    lines.append(item["copy"])
    lines.append("```\n")
    lines.append("**Hashtags**\n")
    lines.append(f"`{item['hashtags']}`\n")

(target_dir / "LEEME.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("✅ Pack semana 2026-09-15 generado correctamente.")
