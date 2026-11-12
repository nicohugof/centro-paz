"""
Estudio Audiovisual y Edición Desacoplada — CPAZ Media OS.

¿Qué es?
Orquestador sobre los motores existentes (`assets/instagram/*.png`, `assets/videos/*.mp4`,
Remotion en `video_engine/`) conectado mediante subprocesos CLI a `ffprobe` y `ffmpeg` (8.1.1).

¿Para qué lo usamos?
Auditar activos existentes, extraer metadatos reales A/V, generar miniaturas o clips
lighweight locales sin tocar `video_engine/public/` ni vincular librerías GPL en Python,
manteniendo además el adaptador `ComfyUI` deshabilitado por defecto (Mac 8 GB / GPL-3.0).
"""

from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

from media_os.privacy import assert_path_not_clinical

ROOT = Path(__file__).resolve().parent.parent
INSTAGRAM_DIR = ROOT / "assets" / "instagram"
VIDEOS_DIR = ROOT / "assets" / "videos"
VIDEO_ENGINE_PUBLIC_DIR = ROOT / "video_engine" / "public"
DEFAULT_EXPORTS_DIR = ROOT / "data" / "media_os" / "exports"


class UnsafeOutputPathError(ValueError):
    """Bloquea escrituras sobre directorios protegidos como `video_engine/public/`."""


def _assert_safe_output_path(output_path: Path | str) -> Path:
    resolved = Path(output_path).resolve()
    assert_path_not_clinical(resolved)
    pub_resolved = VIDEO_ENGINE_PUBLIC_DIR.resolve()
    if resolved == pub_resolved or pub_resolved in resolved.parents:
        raise UnsafeOutputPathError(
            f"Escritura bloqueada: '{output_path}' pertenece al directorio protegido video_engine/public/."
        )
    return resolved


@dataclass
class ComfyUIAdapter:
    """
    Contrato HTTP desacoplado para ComfyUI (GPL-3.0, requiere 16-32 GB RAM/VRAM).
    Permanece deshabilitado por defecto para proteger el Mac (8 GB) y Oracle VPS (954 MiB).
    """

    endpoint: str = "http://127.0.0.1:8188"
    enabled: bool = False
    license_name: str = "GPL-3.0"

    def generate_image(self, workflow_payload: Dict[str, Any]) -> Dict[str, Any]:
        if not self.enabled:
            return {
                "executed": False,
                "status": "disabled_by_policy",
                "reason": (
                    "ComfyUI deshabilitado por defecto (licencia GPL-3.0 y >16 GB RAM/VRAM; "
                    "Mac actual posee 8 GB RAM unificada y se prioriza HTML->Chrome PNG + Remotion)."
                ),
            }
        raise NotImplementedError("Requiere habilitación explícita con servidor GPU externo autorizado.")


class MediaStudio:
    """Gestiona inventario audiovisual existente y edición real vía FFmpeg/FFprobe CLI."""

    def __init__(self, *, exports_dir: Optional[Path | str] = None) -> None:
        self.exports_dir = Path(exports_dir) if exports_dir else DEFAULT_EXPORTS_DIR

    @staticmethod
    def capabilities() -> Dict[str, Any]:
        return {
            "ffmpeg_bin": shutil.which("ffmpeg"),
            "ffprobe_bin": shutil.which("ffprobe"),
            "npx_bin": shutil.which("npx"),
            "remotion_dir_exists": (ROOT / "video_engine" / "src").exists(),
            "comfyui_enabled": False,
        }

    def inventory_existing_assets(self) -> Dict[str, Any]:
        ig_pngs = sorted(INSTAGRAM_DIR.glob("*.png")) if INSTAGRAM_DIR.exists() else []
        ig_htmls = sorted(INSTAGRAM_DIR.glob("*.html")) if INSTAGRAM_DIR.exists() else []
        videos = sorted(VIDEOS_DIR.glob("*.mp4")) if VIDEOS_DIR.exists() else []
        public_files = sorted(VIDEO_ENGINE_PUBLIC_DIR.glob("*")) if VIDEO_ENGINE_PUBLIC_DIR.exists() else []

        return {
            "instagram_png_count": len(ig_pngs),
            "instagram_html_count": len(ig_htmls),
            "videos_mp4_count": len(videos),
            "videos": [
                {"name": v.name, "size_kb": round(v.stat().st_size / 1024, 1), "path": str(v)}
                for v in videos
            ],
            "protected_video_engine_public": [p.name for p in public_files],
            "remotion_entrypoint": str(ROOT / "video_engine" / "generate_short_remotion.py"),
        }

    def probe_video(self, video_path: Path | str) -> Dict[str, Any]:
        """Ejecuta `ffprobe` real en subproceso CLI para leer códec, dimensiones y duración."""
        src = Path(video_path)
        assert_path_not_clinical(src)
        if not src.exists():
            raise FileNotFoundError(f"Video no encontrado: {src}")
        ffprobe_bin = shutil.which("ffprobe")
        if not ffprobe_bin:
            raise RuntimeError("Binario `ffprobe` no disponible en PATH.")

        cmd = [
            ffprobe_bin,
            "-v",
            "error",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            str(src),
        ]
        proc = subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=20)
        raw = json.loads(proc.stdout)
        streams = raw.get("streams", [])
        fmt = raw.get("format", {})
        video_stream = next((s for s in streams if s.get("codec_type") == "video"), {})
        audio_stream = next((s for s in streams if s.get("codec_type") == "audio"), {})
        duration_sec = float(fmt.get("duration") or video_stream.get("duration") or 0.0)
        return {
            "file": src.name,
            "path": str(src),
            "size_bytes": src.stat().st_size,
            "duration_sec": round(duration_sec, 2),
            "width": int(video_stream.get("width") or 0),
            "height": int(video_stream.get("height") or 0),
            "video_codec": video_stream.get("codec_name", "none"),
            "audio_codec": audio_stream.get("codec_name", "none"),
            "is_vertical_short": int(video_stream.get("height") or 0) > int(video_stream.get("width") or 0),
        }

    def extract_thumbnail(
        self,
        video_path: Path | str,
        output_image: Optional[Path | str] = None,
        *,
        at_sec: float = 1.0,
    ) -> Dict[str, Any]:
        """Extrae una miniatura PNG/JPG real usando `ffmpeg` CLI desacoplado."""
        src = Path(video_path)
        assert_path_not_clinical(src)
        if not src.exists():
            raise FileNotFoundError(f"Video no encontrado: {src}")
        ffmpeg_bin = shutil.which("ffmpeg")
        if not ffmpeg_bin:
            raise RuntimeError("Binario `ffmpeg` no disponible en PATH.")

        dest = Path(output_image) if output_image else (self.exports_dir / f"{src.stem}_thumb.jpg")
        safe_dest = _assert_safe_output_path(dest)
        safe_dest.parent.mkdir(parents=True, exist_ok=True)

        cmd = [
            ffmpeg_bin,
            "-y",
            "-ss",
            f"{max(0.0, float(at_sec)):.2f}",
            "-i",
            str(src),
            "-frames:v",
            "1",
            "-q:v",
            "3",
            str(safe_dest),
        ]
        subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=30)
        return {
            "source_video": str(src),
            "thumbnail_path": str(safe_dest),
            "size_bytes": safe_dest.stat().st_size,
            "at_sec": round(float(at_sec), 2),
        }

    def create_preview_clip(
        self,
        video_path: Path | str,
        output_mp4: Optional[Path | str] = None,
        *,
        start_sec: float = 0.0,
        duration_sec: float = 2.0,
    ) -> Dict[str, Any]:
        """Recorta un clip liviano de previsualización vía `ffmpeg` CLI (`stream copy` / rápido)."""
        src = Path(video_path)
        assert_path_not_clinical(src)
        if not src.exists():
            raise FileNotFoundError(f"Video no encontrado: {src}")
        ffmpeg_bin = shutil.which("ffmpeg")
        if not ffmpeg_bin:
            raise RuntimeError("Binario `ffmpeg` no disponible en PATH.")

        dest = Path(output_mp4) if output_mp4 else (self.exports_dir / f"{src.stem}_preview.mp4")
        safe_dest = _assert_safe_output_path(dest)
        safe_dest.parent.mkdir(parents=True, exist_ok=True)

        cmd = [
            ffmpeg_bin,
            "-y",
            "-ss",
            f"{max(0.0, float(start_sec)):.2f}",
            "-i",
            str(src),
            "-t",
            f"{max(0.5, float(duration_sec)):.2f}",
            "-c:v",
            "libx264",
            "-preset",
            "ultrafast",
            "-c:a",
            "aac",
            "-movflags",
            "+faststart",
            str(safe_dest),
        ]
        subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=45)
        probed = self.probe_video(safe_dest)
        return {
            "source_video": str(src),
            "clip_path": str(safe_dest),
            "duration_sec": probed["duration_sec"],
            "width": probed["width"],
            "height": probed["height"],
            "size_bytes": safe_dest.stat().st_size,
        }

    def inspect_all_videos(self) -> List[Dict[str, Any]]:
        if not VIDEOS_DIR.exists():
            return []
        results: List[Dict[str, Any]] = []
        for mp4 in sorted(VIDEOS_DIR.glob("*.mp4")):
            try:
                results.append(self.probe_video(mp4))
            except Exception as exc:
                results.append({"file": mp4.name, "path": str(mp4), "error": str(exc)})
        return results
