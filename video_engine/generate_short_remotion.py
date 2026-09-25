#!/usr/bin/env python3
"""
Pipeline de Renderizado de Videos Verticales con Remotion y Whisper para Centro Paz.
Genera videos de psicología con motion graphics, B-roll animado y subtítulos palabra por palabra.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent
VIDEO_ENGINE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = ROOT / "assets" / "videos"
TEMP_DIR = VIDEO_ENGINE_DIR / "temp"


async def synthesize_speech(text: str, voice: str, out_audio: Path):
    import edge_tts
    comm = edge_tts.Communicate(text, voice)
    await comm.save(str(out_audio))


def extract_word_timestamps(audio_path: Path) -> List[Dict[str, Any]]:
    print("🎙️ Analizando audio con Faster-Whisper para subtítulos palabra por palabra...")
    try:
        from faster_whisper import WhisperModel
        # Usar modelo 'base' o 'small' para velocidad y precisión en español
        model = WhisperModel("base", device="cpu", compute_type="int8")
        segments, info = model.transcribe(str(audio_path), language="es", word_timestamps=True)
        
        words = []
        for segment in segments:
            if segment.words:
                for w in segment.words:
                    clean_word = w.word.strip()
                    if clean_word:
                        words.append({
                            "word": clean_word,
                            "start": round(w.start, 2),
                            "end": round(w.end, 2)
                        })
        print(f"   ✓ {len(words)} palabras detectadas con marcas de tiempo.")
        return words
    except Exception as e:
        print(f"⚠️ Error en whisper, usando fallback por tiempo: {e}")
        # Fallback simple
        return []


def render_with_remotion(props_path: Path, output_mp4: Path) -> bool:
    print(f"🎬 Compilando video en Remotion (1080x1920 @ 30fps)...")
    cmd = [
        "npx", "remotion", "render",
        "src/index.ts",
        "PsychologyShort",
        str(output_mp4),
        f"--props={props_path}",
        "--gl=angle",
        "--concurrency=4",
        "--overwrite"
    ]
    
    res = subprocess.run(cmd, cwd=str(VIDEO_ENGINE_DIR))
    return res.returncode == 0


def build_short_01():
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    
    audio_file = TEMP_DIR / "voice_short01.mp3"
    props_file = TEMP_DIR / "props_short01.json"
    output_mp4 = ASSETS_DIR / "cpaz_short01_tdah_remotion.mp4"
    
    full_text = (
        "¿Sientes que tienes el potencial para hacer todo, pero te quedas paralizado frente a una tarea simple? "
        "Número uno: procrastinación no por desinterés, sino por parálisis ejecutiva. Tu cerebro necesita un nivel mínimo de dopamina para arrancar. "
        "Número dos: agotamiento crónico por masking, el esfuerzo inconsciente de sobre adaptarte para encajar. "
        "Número tres: hipersensibilidad al rechazo o miedo intenso a cometer un error. "
        "En Centro Paz te acompañamos con un enfoque neuroafirmativo en sesiones online y en Ñuñoa con reembolso Isapre. Escríbenos por WhatsApp."
    )
    
    print("🔊 Generando voz neuronal chilena (Catalina)...")
    asyncio.run(synthesize_speech(full_text, "es-CL-CatalinaNeural", audio_file))
    
    # Obtener duración real del audio
    probe_cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(audio_file)
    ]
    dur_str = subprocess.check_output(probe_cmd, text=True).strip()
    duration_sec = float(dur_str) + 1.0 # 1s de margen
    print(f"   ✓ Duración del audio: {duration_sec:.2f}s")
    
    words = extract_word_timestamps(audio_file)
    
    # Codificar audio a base64 para carga inmediata sin depender de rutas HTTP relativas
    import base64
    audio_b64 = base64.b64encode(audio_file.read_bytes()).decode("utf-8")
    audio_data_uri = f"data:audio/mp3;base64,{audio_b64}"

    # Copiar también a public/ por compatibilidad
    public_dir = VIDEO_ENGINE_DIR / "public"
    public_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(audio_file, public_dir / "voice_short01.mp3")
    
    # Mapear escenas
    scenes = [
        {
            "id": "s1",
            "title": "1. Parálisis Ejecutiva",
            "subtitle": "Tu cerebro necesita un nivel mínimo de dopamina para arrancar.",
            "icon": "⚡",
            "startSec": 5.5,
            "endSec": 15.0
        },
        {
            "id": "s2",
            "title": "2. Cansancio por Masking",
            "subtitle": "El esfuerzo inconsciente de sobre-adaptarte para que nadie note tu desorganización.",
            "icon": "🎭",
            "startSec": 15.0,
            "endSec": 23.0
        },
        {
            "id": "s3",
            "title": "3. Sensibilidad al Rechazo",
            "subtitle": "Hipersensibilidad al rechazo o miedo intenso a fallar.",
            "icon": "❤️‍🩹",
            "startSec": 23.0,
            "endSec": 30.5
        }
    ]
    
    props = {
        "title": "3 Señales de TDAH en Adultos",
        "kicker": "TDAH EN ADULTOS",
        "hookText": "3 cosas que parecían flojera pero eran TDAH 🧠",
        "audioUrl": audio_data_uri,
        "durationSec": duration_sec,
        "therapistName": "Valentina Castro Núñez",
        "phoneDisplay": "+56 9 6516 3893",
        "scenes": scenes,
        "words": words
    }
    
    props_file.write_text(json.dumps(props, indent=2, ensure_ascii=False), encoding="utf-8")
    
    success = render_with_remotion(props_file, output_mp4)
    if success:
        print(f"\n🎉 ¡VIDEO REMOTION GENERADO CON ÉXITO!")
        print(f"📁 Archivo: {output_mp4} ({output_mp4.stat().st_size // 1024} KB)")
        return output_mp4
    else:
        print("\n❌ Error durante el renderizado de Remotion.")
        return None


if __name__ == "__main__":
    build_short_01()
