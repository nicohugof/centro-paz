#!/usr/bin/env python3
"""
Generador de activos PWA oficiales para Centro Paz / CPAZ Media OS.
Deriva iconos optimizados para iOS/Safari y Android/Chrome a partir de los
activos de marca oficiales en assets/logo/.
"""
from pathlib import Path
from PIL import Image
import json

ROOT = Path(__file__).resolve().parent.parent
LOGO_DIR = ROOT / "assets" / "logo"
PWA_DIR = ROOT / "assets" / "pwa"
PWA_DIR.mkdir(parents=True, exist_ok=True)

SRC_ICON_PROFILE = LOGO_DIR / "icon-profile-1024.png"
SRC_ICON_TRANSPARENT = LOGO_DIR / "icon.png"

def generate_icons():
    # 1. Apple Touch Icon (180x180) basado en el avatar con fondo suave
    if SRC_ICON_PROFILE.exists():
        img_profile = Image.open(SRC_ICON_PROFILE)
        apple_icon = img_profile.resize((180, 180), Image.Resampling.LANCZOS)
        apple_icon.save(PWA_DIR / "apple-touch-icon.png", format="PNG", optimize=True)
        apple_icon.save(PWA_DIR / "apple-touch-icon-180x180.png", format="PNG", optimize=True)
        print("✓ Creado: apple-touch-icon.png (180x180)")

        # Favicons
        fav_32 = img_profile.resize((32, 32), Image.Resampling.LANCZOS)
        fav_32.save(PWA_DIR / "favicon-32x32.png", format="PNG", optimize=True)
        fav_16 = img_profile.resize((16, 16), Image.Resampling.LANCZOS)
        fav_16.save(PWA_DIR / "favicon-16x16.png", format="PNG", optimize=True)
        print("✓ Creados: favicons 32x32 y 16x16")

    # 2. PWA Standard Icons (192x192 y 512x512)
    # Se genera versión con fondo para compatibilidad "maskable" y standalone
    if SRC_ICON_PROFILE.exists():
        img_profile = Image.open(SRC_ICON_PROFILE)
        icon_192 = img_profile.resize((192, 192), Image.Resampling.LANCZOS)
        icon_192.save(PWA_DIR / "icon-192x192.png", format="PNG", optimize=True)
        
        icon_512 = img_profile.resize((512, 512), Image.Resampling.LANCZOS)
        icon_512.save(PWA_DIR / "icon-512x512.png", format="PNG", optimize=True)
        print("✓ Creados: icon-192x192.png y icon-512x512.png")

def generate_manifest():
    manifest = {
        "name": "Centro Paz",
        "short_name": "Centro Paz",
        "id": "cpaz-media-os",
        "start_url": "/",
        "scope": "/",
        "display": "standalone",
        "orientation": "portrait-primary",
        "background_color": "#f6f8f6",
        "theme_color": "#2c6e58",
        "description": "Centro Paz — CPAZ Media OS: Gestión de calendario editorial, atribución y QA clínico.",
        "categories": ["medical", "business", "productivity"],
        "lang": "es-CL",
        "icons": [
            {
                "src": "/icons/icon-192x192.png",
                "sizes": "192x192",
                "type": "image/png",
                "purpose": "any maskable"
            },
            {
                "src": "/icons/icon-512x512.png",
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "any maskable"
            },
            {
                "src": "/apple-touch-icon.png",
                "sizes": "180x180",
                "type": "image/png",
                "purpose": "any"
            }
        ]
    }
    manifest_path = PWA_DIR / "manifest.webmanifest"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print("✓ Creado: manifest.webmanifest")

def generate_service_worker():
    # Service worker seguro: cachea solo shell estático e iconos.
    # NUNCA cachea peticiones de API (/api/*), datos de pacientes ni sesiones.
    sw_code = """/* Service Worker de Centro Paz / CPAZ Media OS */
const CACHE_NAME = 'cpaz-media-os-v1';
const STATIC_ASSETS = [
  '/',
  '/manifest.webmanifest',
  '/apple-touch-icon.png',
  '/icons/icon-192x192.png',
  '/icons/icon-512x512.png',
  '/icons/favicon-32x32.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(STATIC_ASSETS);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);

  // Aislamiento clínico estricto (Ley 19.628): NUNCA interceptar ni almacenar en caché endpoints de API ni mutaciones POST
  if (url.pathname.startsWith('/api/') || event.request.method !== 'GET') {
    return;
  }

  // Network-first con fallback a caché para navegación e interfaz
  event.respondWith(
    fetch(event.request)
      .then((response) => {
        if (response.ok && (url.pathname === '/' || url.pathname.startsWith('/icons/') || url.pathname.endsWith('.png') || url.pathname.endsWith('.webmanifest'))) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
        }
        return response;
      })
      .catch(() => {
        return caches.match(event.request);
      })
  );
});
"""
    sw_path = PWA_DIR / "sw.js"
    with open(sw_path, "w", encoding="utf-8") as f:
        f.write(sw_code)
    print("✓ Creado: sw.js (Aislamiento clínico garantizado)")

if __name__ == "__main__":
    generate_icons()
    generate_manifest()
    generate_service_worker()
