#!/usr/bin/env python3
"""
Actualiza todas las 28 piezas gráficas de Instagram (HTML + PNG) con el nuevo logotipo oficial de Centro Paz.
"""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IG_DIR = ROOT / "assets" / "instagram"
LOGO_ICON = ROOT / "assets" / "logo" / "icon.png"

NEW_CSS = """.logo-badge {
      width: 64px;
      height: 64px;
      border-radius: 50%;
      background: #FFFFFF;
      border: 2px solid #E2EAD8;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 14px rgba(66, 97, 19, 0.08);
      overflow: hidden;
      flex-shrink: 0;
    }
    .logo-badge img {
      width: 52px;
      height: 52px;
      object-fit: contain;
      display: block;
    }"""

NEW_HTML_BADGE = '<div class="logo-badge"><img src="../logo/icon.png" alt="Centro Paz" width="52" height="52"></div>'

chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
html_files = sorted(IG_DIR.glob("*.html"))
print(f"Total archivos HTML a procesar: {len(html_files)}")

# 1. Modificar plantillas HTML
updated_count = 0
for f in html_files:
    txt = f.read_text(encoding="utf-8")
    # Reemplazar CSS
    txt = re.sub(r'\.logo-badge\s*\{[^}]+\}', NEW_CSS, txt)
    # Reemplazar insignia
    txt = re.sub(r'<div class="logo-badge">\s*CP\s*</div>', NEW_HTML_BADGE, txt)
    f.write_text(txt, encoding="utf-8")
    updated_count += 1

print(f"✓ {updated_count} plantillas HTML actualizadas con el nuevo logotipo.")

# 2. Renderizar todas las piezas a PNG (1080x1350)
print("\n🎨 Renderizando las 28 piezas a PNG (1080x1350) con Google Chrome...")
success = 0
for i, f in enumerate(html_files, 1):
    png_p = f.with_suffix(".png")
    cmd = [
        chrome_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        "--window-size=1080,1350",
        f"--screenshot={png_p}",
        f.resolve().as_uri()
    ]
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode == 0 and png_p.exists():
        size_kb = png_p.stat().st_size // 1024
        print(f"  [{i:02d}/28] ✓ {png_p.name} ({size_kb} KB)")
        success += 1
    else:
        print(f"  [{i:02d}/28] ❌ Error en {f.name}")

print(f"\n🎉 Renderizado completado: {success}/{len(html_files)} imágenes generadas.")
