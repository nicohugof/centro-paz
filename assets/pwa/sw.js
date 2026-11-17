/* Service Worker de Centro Paz / CPAZ Media OS */
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
