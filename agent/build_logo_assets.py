#!/usr/bin/env python3
"""
Genera todos los formatos de logotipo de alta resolución para Centro Paz:
- assets/logo/logo_original.jpg
- assets/logo/logo_transparent.png
- assets/logo/icon.png (512x512)
- assets/logo/icon-profile-1024.png (1024x1024)
- assets/logo/lockup-1200.png (1200x630 OG image)
- assets/logo/icon.svg (Vector)
- assets/logo/lockup.svg (Vector)
"""
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOGO_DIR = ROOT / "assets" / "logo"
LOGO_DIR.mkdir(parents=True, exist_ok=True)

SRC_IMG = LOGO_DIR / "logo_original.jpg"
if not SRC_IMG.exists():
    fallback_src = Path("/Users/nigoku/.gemini/antigravity/brain/192b3f06-36d5-4903-b070-3d94bce7e501/.user_uploaded/media_1789306822716.jpg")
    import shutil
    shutil.copy(fallback_src, SRC_IMG)

print(f"Procesando imagen fuente: {SRC_IMG}")
img_bgr = cv2.imread(str(SRC_IMG))
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
h, w, _ = img_rgb.shape

# 1. Separar plano de fondo blanco con alpha matting fino
arr = img_rgb.astype(np.float32)
diff = 255.0 - arr
max_diff = np.max(diff, axis=2)

# Umbral suave para preservar anti-aliasing
# Fondo blanco puro -> alpha 0
# Elementos de color -> alpha 1
alpha = np.clip((max_diff - 10.0) / (180.0 - 10.0), 0.0, 1.0)
alpha = alpha * alpha * (3.0 - 2.0 * alpha) # Hermite smoothstep

# Reconstruir color RGB sin contaminación blanca
fg = np.zeros_like(arr)
mask = alpha > 0.02
for c in range(3):
    fg[..., c] = np.where(mask, np.clip((arr[..., c] - 255.0 * (1.0 - alpha)) / np.maximum(alpha, 0.02), 0, 255), arr[..., c])

rgba = np.dstack([fg, alpha * 255.0]).astype(np.uint8)
pil_transparent = Image.fromarray(rgba, "RGBA")

# Recorte exacto alrededor del logo con un pequeño margen
# Bounding box del contenido alfa
bbox = pil_transparent.getbbox()
print(f"Bounding box original del logo: {bbox}")
# Hacemos el recorte cuadrado centrado
bw = bbox[2] - bbox[0]
bh = bbox[3] - bbox[1]
cx = (bbox[0] + bbox[2]) // 2
cy = (bbox[1] + bbox[3]) // 2
size = max(bw, bh) + 20

crop_box = (
    max(0, cx - size // 2),
    max(0, cy - size // 2),
    min(w, cx + size // 2),
    min(h, cy + size // 2)
)
logo_cropped = pil_transparent.crop(crop_box)

# Guardar transparent PNG
logo_cropped.save(LOGO_DIR / "logo_transparent.png")
print("✓ Creado: assets/logo/logo_transparent.png")

# 2. Icon 512x512 transparente
icon_512 = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
# Escalar logo manteniendo relación de aspecto para que ocupe ~420x420
logo_res_512 = logo_cropped.resize((420, 420), Image.Resampling.LANCZOS)
icon_512.paste(logo_res_512, (46, 46), logo_res_512)
icon_512.save(LOGO_DIR / "icon.png")
print("✓ Creado: assets/logo/icon.png (512x512)")

# 3. Icon Profile 1024x1024 (avatar circular / apple touch icon)
# Fondo blanco suave con círculo blanco puro y borde sutil
profile_1024 = Image.new("RGBA", (1024, 1024), (250, 246, 243, 255))
draw = ImageDraw.Draw(profile_1024)
# Círculo blanco central
draw.ellipse((48, 48, 976, 976), fill=(255, 255, 255, 255), outline=(220, 230, 215, 255), width=6)
logo_res_800 = logo_cropped.resize((760, 760), Image.Resampling.LANCZOS)
profile_1024.paste(logo_res_800, (132, 132), logo_res_800)
# Convertir a RGB para máxima compatibilidad con avatar y apple-touch-icon
profile_1024_rgb = profile_1024.convert("RGB")
profile_1024_rgb.save(LOGO_DIR / "icon-profile-1024.png", quality=96)
print("✓ Creado: assets/logo/icon-profile-1024.png (1024x1024)")

# 4. Lockup 1200x630 (OpenGraph / Twitter / Redes Sociales)
og_1200 = Image.new("RGBA", (1200, 630), (250, 246, 243, 255))
draw_og = ImageDraw.Draw(og_1200)

# Colocar logo a la izquierda
logo_og = logo_cropped.resize((400, 400), Image.Resampling.LANCZOS)
og_1200.paste(logo_og, (100, 115), logo_og)

# Tipografía para "Centro Paz" y "Psicología Clínica"
# Si Lora / Georgia están disponibles en el sistema:
try:
    font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 80)
    font_sub = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 34)
    font_details = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 26)
except Exception:
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_details = ImageFont.load_default()

# Dibujar texto
draw_og.text((540, 190), "Centro Paz", font=font_title, fill=(92, 31, 41)) # #5C1F29
draw_og.text((545, 285), "PSICOLOGÍA CLÍNICA", font=font_sub, fill=(66, 97, 19)) # #426113
# Línea divisoria elegante
draw_og.line((545, 340, 1050, 340), fill=(220, 230, 215), width=3)
draw_og.text((545, 365), "Atención Neuroafirmativa · Adultos & Infantil", font=font_details, fill=(70, 70, 70))
draw_og.text((545, 405), "Sesiones Online y en Ñuñoa · Reembolso Isapre", font=font_details, fill=(110, 110, 110))

og_1200_rgb = og_1200.convert("RGB")
og_1200_rgb.save(LOGO_DIR / "lockup-1200.png", quality=95)
print("✓ Creado: assets/logo/lockup-1200.png (1200x630)")

# 5. Generar SVG Vectorial de alta precisión (Psi + Laurel)
# Extraemos contornos limpios de la versión sin fondo
gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
is_fg = (gray < 230).astype(np.uint8) * 255
b, g, r = cv2.split(img_bgr)
is_psi = (is_fg > 0) & (r > 120)
is_wreath = (is_fg > 0) & (r <= 120)

def to_svg_paths(mask, eps=0.65):
    contours, hier = cv2.findContours((mask * 255).astype(np.uint8), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_L1)
    if hier is None:
        return ""
    d_list = []
    for c in contours:
        app = cv2.approxPolyDP(c, eps, True)
        if len(app) < 3:
            continue
        pts = app.reshape(-1, 2)
        d = f"M {pts[0][0]} {pts[0][1]} " + " ".join(f"L {p[0]} {p[1]}" for p in pts[1:]) + " Z"
        d_list.append(d)
    return " ".join(d_list)

psi_path = to_svg_paths(is_psi)
wreath_path = to_svg_paths(is_wreath)

# El contenido está entre x=65..340, y=65..345 (viewBox 280x280)
svg_icon = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="60 60 284 284" width="100%" height="100%">
  <!-- Centro Paz — Nuevo Logo Oficial (Ψ & Laureles) -->
  <path d="{psi_path}" fill="#B0B61E" fill-rule="evenodd"/>
  <path d="{wreath_path}" fill="#426113" fill-rule="evenodd"/>
</svg>
"""
(LOGO_DIR / "icon.svg").write_text(svg_icon, encoding="utf-8")
(LOGO_DIR / "icon-square.svg").write_text(svg_icon, encoding="utf-8")
print("✓ Creado: assets/logo/icon.svg y icon-square.svg")

# 6. Lockup SVG
svg_lockup = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 160" width="100%" height="100%">
  <!-- Icono -->
  <g transform="translate(10, 10) scale(0.48)">
    <path d="{psi_path}" fill="#B0B61E" fill-rule="evenodd" transform="translate(-60, -60)"/>
    <path d="{wreath_path}" fill="#426113" fill-rule="evenodd" transform="translate(-60, -60)"/>
  </g>
  <!-- Tipografía -->
  <text x="165" y="76" font-family="Lora, Georgia, serif" font-size="44" font-weight="700" fill="#5C1F29">Centro Paz</text>
  <text x="167" y="108" font-family="'Nunito Sans', -apple-system, sans-serif" font-size="19" font-weight="700" fill="#426113" letter-spacing="2.5">PSICOLOGÍA CLÍNICA</text>
</svg>
"""
(LOGO_DIR / "lockup.svg").write_text(svg_lockup, encoding="utf-8")
print("✓ Creado: assets/logo/lockup.svg")

print("\n🎉 Todos los activos de marca de assets/logo/ fueron generados exitosamente.")
