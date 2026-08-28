#!/usr/bin/env python3
"""
Genera y exporta la parrilla completa de 28 días (4 semanas) en:
- parrilla_semanal_n8n.json (raíz y agent/)
- parrilla_semanal.md
"""
import json
from pathlib import Path
from agent import content_engine

ROOT = Path(__file__).resolve().parent.parent

def build_28_day_schedule():
    all_items = []
    
    # 4 semanas completas (28 días)
    for week_num in range(1, 5):
        week_cal = content_engine.get_weekly_calendar(week=week_num)
        for day_idx, item in enumerate(week_cal, start=1):
            global_day = (week_num - 1) * 7 + day_idx
            topic_id = item["id"]
            topic = content_engine.TOPICS[item["topic_key"]]
            
            # 1. Story Mañana
            all_items.append({
                "id": f"cpaz_d{global_day:02d}_01",
                "semana": week_num,
                "dia": item["dia"],
                "dia_global": global_day,
                "hora": "09:00",
                "tipo": "story",
                "titulo": f"Reflexión matutina: {topic['kicker']}",
                "url_imagen": f"https://www.centropaz.cl/assets/instagram/post_{topic_id:02d}_{item['topic_key']}.png",
                "caption": f"🌿 {topic['hook']}\n\nEn Centro Paz te acompañamos desde un enfoque humanista y neuroafirmativo en Ñuñoa y Online.\n\n📲 WhatsApp: +56 9 6516 3893\n🌐 https://www.centropaz.cl",
                "cta": "WhatsApp +56 9 6516 3893 · https://www.centropaz.cl"
            })
            
            # 2. Feed Mediodía (Pieza gráfica principal)
            all_items.append({
                "id": f"cpaz_d{global_day:02d}_02",
                "semana": week_num,
                "dia": item["dia"],
                "dia_global": global_day,
                "hora": "13:00",
                "tipo": "feed",
                "titulo": topic["title"],
                "url_imagen": f"https://www.centropaz.cl/assets/instagram/post_{topic_id:02d}_{item['topic_key']}.png",
                "caption": topic["caption"],
                "cta": "WhatsApp +56 9 6516 3893 · https://www.centropaz.cl"
            })
            
            # 3. Reel Tarde
            all_items.append({
                "id": f"cpaz_d{global_day:02d}_03",
                "semana": week_num,
                "dia": item["dia"],
                "dia_global": global_day,
                "hora": "18:00",
                "tipo": "reel",
                "titulo": f"Video: {topic['kicker']} ({topic['title'][:40]}...)",
                "url_imagen": f"https://www.centropaz.cl/assets/instagram/post_{topic_id:02d}_{item['topic_key']}.png",
                "caption": f"{topic['hook']}\n\n👉 Sesiones online y presenciales en Ñuñoa con boletas reembolsables en Isapres.\n\nWhatsApp: +56 9 6516 3893 · www.centropaz.cl",
                "cta": "WhatsApp +56 9 6516 3893 · https://www.centropaz.cl"
            })
            
            # 4. Story Noche
            all_items.append({
                "id": f"cpaz_d{global_day:02d}_04",
                "semana": week_num,
                "dia": item["dia"],
                "dia_global": global_day,
                "hora": "21:00",
                "tipo": "story",
                "titulo": "Recordatorio de bienestar y agenda",
                "url_imagen": f"https://www.centropaz.cl/assets/instagram/post_{topic_id:02d}_{item['topic_key']}.png",
                "caption": "✨ Prioriza tu salud mental esta semana. Cupos disponibles para terapia en Ñuñoa y Online.\n\n📲 WhatsApp: +56 9 6516 3893\n🌐 www.centropaz.cl",
                "cta": "WhatsApp +56 9 6516 3893 · https://www.centropaz.cl"
            })
            
    return {
        "version": "2.0.0",
        "brand": content_engine.BRAND,
        "total_days": 28,
        "total_pieces": len(all_items),
        "schedule": all_items
    }

def export_all():
    data = build_28_day_schedule()
    
    # Escribir JSON en raíz y agent/
    (ROOT / "parrilla_semanal_n8n.json").write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    (ROOT / "agent" / "parrilla_semanal_n8n.json").write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    
    # Escribir Markdown descriptivo
    md_lines = [
        "# 📅 Matriz de 28 Días de Publicaciones Autónomas — Centro Paz (CPAZ)\n",
        f"Parrilla completa de **28 días (4 semanas / 112 piezas automatizadas)** para **Instagram (`@centropaz.cl`)**, **TikTok (`@centropaz.cl`)**, **Facebook (`Centro Paz`)** y **Threads**.\n",
        "## 📡 Endpoints JSON para n8n y Automatización:",
        "- **JSON de 28 días:** `https://www.centropaz.cl/parrilla_semanal_n8n.json`",
        "- **Matriz Omnicanal:** `https://www.centropaz.cl/multiplatform_content_n8n.json`\n",
        "## 🗓️ Catálogo de las 28 Piezas Gráficas (1080x1350 PNG):\n",
        "| ID | Semana | Día | Tema / Título | URL Imagen PNG |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]
    
    for item in content_engine.get_all_catalog():
        md_lines.append(f"| Post {item['id']:02d} | Sem {(item['id']-1)//7 + 1} | {item['kicker']} | {item['title']} | [`https://www.centropaz.cl/assets/instagram/{item['image_file']}`](https://www.centropaz.cl/assets/instagram/{item['image_file']}) |")
        
    (ROOT / "parrilla_semanal.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    print(f"✅ 28 días (112 slots de publicación) exportados exitosamente en parrilla_semanal_n8n.json y parrilla_semanal.md")

if __name__ == "__main__":
    export_all()
