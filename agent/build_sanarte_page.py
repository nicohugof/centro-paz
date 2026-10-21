# -*- coding: utf-8 -*-
import json
import os
import re
import urllib.parse
from bs4 import BeautifulSoup

def get_curated_products():
    curated_path = os.path.join(os.path.dirname(__file__), 'sanarte_curated.json')
    if os.path.exists(curated_path):
        with open(curated_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    # Parse directly from scraped ML content
    scraped_path = '/Users/nigoku/.gemini/antigravity/brain/27ed2f52-dbc2-4a68-be83-85842add3f10/.system_generated/steps/521/content.md'
    with open(scraped_path, 'r', encoding='utf-8') as f:
        html_text = f.read()

    soup = BeautifulSoup(html_text, 'html.parser')
    raw_products = []
    seen = set()

    for card in soup.find_all('div', class_=re.compile(r'poly-card')):
        title_a = card.find('a', class_=re.compile(r'poly-component__title'))
        if not title_a:
            title_a = card.find('a', href=re.compile(r'mercadolibre\.cl/'))
        if not title_a:
            continue
        title = title_a.get_text(strip=True)
        href = title_a.get('href', '').split('#')[0]
        if not title or title in seen:
            continue
        seen.add(title)
        price_span = card.find('span', class_=re.compile(r'andes-money-amount__fraction'))
        price = price_span.get_text(strip=True) if price_span else ''
        img = card.find('img')
        img_url = ''
        if img:
            img_url = img.get('data-src') or img.get('src') or ''
        raw_products.append({
            'title': title,
            'price': price,
            'link': href,
            'image': img_url
        })

    excluded_keywords = ['zapatos', 'anillas para cunas']
    curated = []
    idx = 1
    for p in raw_products:
        title_lower = p['title'].lower()
        if any(k in title_lower for k in excluded_keywords):
            continue

        title = p['title']
        price = p['price']
        link_ml = p['link']
        img = p['image']
        code = f'SANARTE-{idx:02d}'
        idx += 1

        cat = 'Joyería y Minerales'
        cat_slug = 'joyeria'
        symbolism = 'Recordatorio de presencia, calma y conexión personal.'
        badge = 'Disponible'

        if 'selenita' in title_lower:
            cat = 'Minerales en Bruto'
            cat_slug = 'minerales'
            symbolism = 'Tradicionalmente asociada a la serenidad del espacio, claridad mental y pureza.'
            badge = 'Pieza Destacada'
        elif 'chakras' in title_lower:
            cat = 'Alineación y Centros'
            cat_slug = 'amuletos'
            symbolism = 'Simbología de equilibrio de los 7 centros energéticos corporales y armonía interior.'
            badge = 'Muy Solicitado'
        elif 'amazonita' in title_lower:
            cat = 'Minerales Nobles'
            cat_slug = 'minerales'
            symbolism = 'Asociada a la tranquilidad emocional, la expresión sincera y la amabilidad.'
        elif 'cuarzo rosado' in title_lower or 'cuarzo rosa' in title_lower:
            cat = 'Cuarzos & Afecto'
            cat_slug = 'joyeria'
            symbolism = 'Símbolo ancestral del amor propio, la compasión y la reconciliación personal.'
        elif 'cuarzo blanco' in title_lower:
            cat = 'Minerales en Bruto'
            cat_slug = 'minerales'
            symbolism = 'Símbolo de luz, orden de pensamientos y enfoque consciente.'
        elif 'lapislázuli' in title_lower or 'lapislazuli' in title_lower:
            cat = 'Piedra Nacional'
            cat_slug = 'joyeria'
            symbolism = 'Piedra chilena de las cumbres de Ovalle, vinculada a la verdad interna y sabiduría.'
            badge = 'Plata 925'
        elif 'obsidiana' in title_lower:
            cat = 'Protección Simbólica'
            cat_slug = 'amuletos'
            symbolism = 'Vidrio volcánico asociado a la fijación de límites saludables y enraizamiento.'
        elif 'ojo de tigre' in title_lower:
            cat = 'Fuerza y Determinación'
            cat_slug = 'joyeria'
            symbolism = 'Asociado al coraje, la confianza personal y la perseverancia serena.'
        elif 'citrino' in title_lower:
            cat = 'Vitalidad & Luz'
            cat_slug = 'joyeria'
            symbolism = 'Tonalidad solar vinculada al optimismo, la creatividad y la energía vital.'
        elif 'rojas de la protección' in title_lower or 'pulseras rojas' in title_lower:
            cat = 'Amuletos de Protección'
            cat_slug = 'amuletos'
            symbolism = 'Tradición del hilo rojo como anclaje de autocuidado y contención frente a tensiones.'
            badge = 'Pack 3 Unidades'
        elif 'atrapasueño' in title_lower:
            cat = 'Artesanías para Espacios'
            cat_slug = 'artesanias'
            symbolism = 'Creación artesanal de filtro simbólico para descansar la mente y decorar con calidez.'
        elif 'strap' in title_lower:
            cat = 'Accesorios con Cristales'
            cat_slug = 'accesorios'
            symbolism = 'Diseño práctico para lentes con cuentas de piedra natural como detalle cotidiano consciente.'
        elif 'tobillera' in title_lower:
            cat = 'Tejido Macramé & Hilo'
            cat_slug = 'accesorios'
            symbolism = 'Elaborada a mano con hilo encerado resistente; símbolo de libertad y contacto con la naturaleza.'
        elif 'turquesa' in title_lower:
            cat = 'Piedras Naturales'
            cat_slug = 'joyeria'
            symbolism = 'Tono celeste asociado a la frescura de espíritu y la calma en momentos de prisa.'

        curated.append({
            'code': code,
            'title': title,
            'price': price,
            'category': cat,
            'category_slug': cat_slug,
            'symbolism': symbolism,
            'badge': badge,
            'link_ml': link_ml,
            'image': img
        })

    with open(curated_path, 'w', encoding='utf-8') as f:
        json.dump(curated, f, indent=2, ensure_ascii=False)

    return curated

def generate_catalog():
    products = get_curated_products()
    cards_html = []
    schema_items = []

    for i, p in enumerate(products, 1):
        price_val = p['price']
        title_val = p['title']
        code_val = p['code']
        cat_val = p['category']
        slug_val = p['category_slug']
        sym_val = p['symbolism']
        badge_val = p['badge']
        img_val = p['image']
        ml_val = p['link_ml']

        wa_msg = f"Hola Valentina 💎 Quisiera encargar en San_Arte el producto: {title_val} por ${price_val} CLP (Ref: {code_val}). ¿Está disponible y cómo coordinamos la entrega/envío?"
        wa_url = f"https://wa.me/56965163893?text={urllib.parse.quote(wa_msg)}"
        price_clean = price_val.replace('.', '')

        schema_items.append({
            "@type": "ListItem",
            "position": i,
            "item": {
                "@type": "Product",
                "name": title_val,
                "image": img_val,
                "description": sym_val,
                "sku": code_val,
                "offers": {
                    "@type": "Offer",
                    "priceCurrency": "CLP",
                    "price": price_clean,
                    "availability": "https://schema.org/InStock",
                    "url": ml_val
                }
            }
        })

        card = f"""          <!-- Producto {i}: {title_val} -->
          <article class="product-card" data-category="{slug_val}">
            <div class="product-image-container">
              <img src="{img_val}" alt="{title_val} - San_Arte Artesanías y Joyas Centro Paz" class="product-card-img" loading="lazy" width="320" height="256" onerror="this.style.opacity='0'">
              <div class="product-image-placeholder" style="z-index: -1;">
                <span class="product-symbol-icon">💎</span>
                <span style="font-weight:700; font-size:1.05rem;">{title_val[:35]}</span>
              </div>
              <span class="product-stock-badge">{badge_val}</span>
            </div>
            <div class="product-body">
              <span class="product-category-tag">{cat_val} · Ref: {code_val}</span>
              <h2 class="product-title">{title_val}</h2>
              <div class="product-symbolism">
                <strong>Significado simbólico:</strong> {sym_val}
              </div>
              <div class="product-footer">
                <div class="product-price-box">
                  <span class="product-price-label">Precio Oficial</span>
                  <span class="product-price-value">${price_val} <small style="font-size:0.75rem;">CLP</small></span>
                </div>
              </div>
              <div class="product-actions-grid">
                <a href="{wa_url}" class="product-cta-btn" data-wa-action="sanarte-producto" data-product-name="{title_val}" data-product-code="{code_val}" target="_blank" rel="noopener noreferrer" title="Comprar directamente en la web con Valentina vía WhatsApp">
                  <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0012.04 2zm.01 1.67c4.54 0 8.24 3.7 8.24 8.24 0 2.2-.86 4.27-2.42 5.82-1.55 1.56-3.62 2.42-5.82 2.42-1.47 0-2.9-.39-4.16-1.13l-.3-.18-3.1.81.83-3.02-.2-.31c-.81-1.3-1.24-2.8-1.24-4.41 0-4.54 3.7-8.24 8.24-8.24zm4.52 11.66c-.25-.13-1.47-.72-1.7-.81-.23-.08-.39-.13-.56.13-.17.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.13-1.06-.39-2.02-1.25-.75-.67-1.25-1.5-1.4-1.75-.14-.25-.02-.39.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.42.08-.17.04-.31-.02-.44-.06-.13-.56-1.34-.76-1.84-.2-.48-.4-.42-.56-.43h-.47c-.17 0-.44.06-.67.31-.23.25-.88.86-.88 2.1 0 1.24.9 2.44 1.03 2.61.13.17 1.77 2.7 4.29 3.79.6.26 1.07.41 1.43.53.6.19 1.15.16 1.58.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.08.15-1.18-.07-.1-.23-.17-.48-.29z"/></svg>
                  <span>Pedir en la Web (WhatsApp)</span>
                </a>
                <a href="{ml_val}" class="product-ml-btn" target="_blank" rel="noopener noreferrer" title="Ver publicación o comprar con Mercado Pago / cuotas en MercadoLibre">
                  <svg viewBox="0 0 24 24"><path d="M12 2L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-3zm-1 15l-4-4 1.41-1.41L11 14.17l6.59-6.59L19 9l-8 8z"/></svg>
                  <span>Comprar también en MercadoLibre 🛡️</span>
                </a>
              </div>
            </div>
          </article>"""
        cards_html.append(card)

    cards_joined = "\n\n".join(cards_html)
    schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Catálogo San_Arte Artesanías & Joyas Centro Paz",
        "itemListElement": schema_items
    }, indent=2, ensure_ascii=False)

    return cards_joined, schema_json, len(products)

def build_page(canonical_url, page_title):
    cards_joined, schema_json, total_prods = generate_catalog()

    template = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>__PAGE_TITLE__</title>
  <meta name="description" content="San_Arte por Valentina Castro en Centro Paz: Joyería en piedras naturales, cuarzo, selenita, amazonita, lapislázuli, 7 chakras y artesanías con significado simbólico. Compra directa en la web por WhatsApp y respaldo en MercadoLibre. Envíos a todo Chile y entregas en Metro Irarrázaval.">
  <link rel="canonical" href="__CANONICAL_URL__">
  <link rel="icon" type="image/svg+xml" href="assets/logo/icon.svg">
  <link rel="apple-touch-icon" href="assets/logo/icon-profile-1024.png">
  <meta name="theme-color" content="#385E28">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <meta name="author" content="Valentina Castro Núñez · San_Arte Centro Paz">

  <!-- Open Graph -->
  <meta property="og:site_name" content="San_Arte · Centro Paz">
  <meta property="og:title" content="San_Arte Artesanías & Joyas con Significado Simbólico | Centro Paz">
  <meta property="og:description" content="Catálogo oficial San_Arte: Minerales naturales, joyería consciente y artesanías de Valentina Castro. Compra directa por WhatsApp y tienda oficial en MercadoLibre.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="__CANONICAL_URL__">
  <meta property="og:image" content="https://www.centropaz.cl/assets/logo/lockup-1200.png">
  <meta property="og:locale" content="es_CL">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="San_Arte Artesanías y Joyas | Centro Paz">
  <meta name="twitter:description" content="Minerales nobles, cuarzos, amuletos y joyería artesanal con sentido. Compra en web o MercadoLibre.">
  <meta name="twitter:image" content="https://www.centropaz.cl/assets/logo/lockup-1200.png">

  <!-- Tipografías -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400..700;1,400..700&family=Nunito+Sans:ital,opsz,wght@0,6..12,300..900;1,6..12,300..900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css?v=20261021.1">

  <!-- Schema.org JSON-LD para Tienda y Catálogo -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Store",
    "name": "San_Arte Artesanías y Joyas · Centro Paz",
    "url": "__CANONICAL_URL__",
    "description": "Área de artesanías, orfebrería y objetos simbólicos de Valentina Castro Núñez. Minerales nobles, cuarzos y accesorios con sentido.",
    "telephone": "+56965163893",
    "currenciesAccepted": "CLP",
    "paymentAccepted": "Transferencia Bancaria, WhatsApp Asistido, Mercado Pago",
    "sameAs": [
      "https://www.instagram.com/sanarte.artesanias",
      "https://www.facebook.com/share/18MZqpism4/?mibextid=wwXIfr",
      "https://listado.mercadolibre.cl/_CustId_192299793"
    ],
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Ñuñoa / Santiago",
      "addressRegion": "Región Metropolitana",
      "addressCountry": "CL"
    }
  }
  </script>

  <script type="application/ld+json">
__SCHEMA_JSON__
  </script>
</head>
<body class="landing-page-body">

  <header class="navbar">
    <div class="container nav-container">
      <a href="index.html" class="logo-brand">
        <div class="logo-symbol">
          <img src="assets/logo/icon.svg" alt="Centro Paz" width="32" height="32" style="object-fit: contain; display: block;">
        </div>
        <div class="logo-text">
          <span class="logo-name">Centro Paz</span>
          <span class="logo-tagline">San_Arte Artesanías & Joyas</span>
        </div>
      </a>

      <nav>
        <ul class="nav-links" id="site-nav">
          <li><a href="index.html">Inicio</a></li>
          <li><a href="index.html#terapeuta">Sobre mí / Centro Paz</a></li>
          <li><a href="terapias.html">Terapias</a></li>
          <li><a href="mindfulness.html">Mindfulness</a></li>
          <li><a href="sanarte.html" style="color:var(--dorado-dark); font-weight:800;">San_Arte (Artesanías)</a></li>
          <li><a href="https://wa.me/56965163893?text=Hola%20Valentina%20%F0%9F%92%8E%20Quisiera%20consultar%20por%20las%20piezas%20de%20San_Arte%20Artesan%C3%ADas%20y%20Joyas." class="nav-cta btn-whatsapp" data-wa-action="tienda-general" target="_blank" rel="noopener noreferrer">Contacto / Pedidos</a></li>
        </ul>
      </nav>

      <button class="nav-toggle" type="button" aria-label="Abrir menú de navegación" aria-expanded="false" aria-controls="site-nav">
        <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </header>

  <main>
    <div class="container">
      <nav class="breadcrumb-nav" aria-label="Miga de pan">
        <ol>
          <li><a href="index.html">Inicio</a></li>
          <li><a href="artesanias-joyas.html">Artesanías y Joyas</a></li>
          <li aria-current="page">San_Arte Catálogo Oficial</li>
        </ol>
      </nav>
    </div>

    <!-- Encabezado Hero de San_Arte -->
    <section class="landing-hero" style="padding-top:16px; padding-bottom:24px;">
      <div class="container">
        <div class="landing-badge">💎 San_Arte · Hecho a Mano con Sentido Simbólico</div>
        <h1 class="landing-title">San_Arte: Artesanías, Joyas y Minerales</h1>
        <p class="landing-subtitle">Creaciones artesanales de <strong>Valentina Castro Núñez</strong> pensadas como anclajes cotidianos de serenidad, autocuidado y conexión. Compra directamente en nuestra web con atención personalizada vía WhatsApp o en nuestra tienda oficial de MercadoLibre.</p>

        <!-- Barra Social y Confianza -->
        <div class="sanarte-brand-hero">
          <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:16px;">
            <div>
              <span style="font-weight:800; color:var(--verde-dark); font-size:1.05rem;">Conéctate con la comunidad de San_Arte:</span>
              <p style="margin:4px 0 0 0; font-size:0.9rem; color:var(--gris);">Encuentra novedades semanales, detrás de cámara y opiniones reales de compradores.</p>
            </div>
            <div class="sanarte-delivery-badge">
              <span>🚇 Entregas: Metro Irarrázaval</span>
              <span>·</span>
              <span>📦 Envíos a todo Chile</span>
            </div>
          </div>

          <div class="sanarte-social-links-bar">
            <!-- Instagram -->
            <a href="https://www.instagram.com/sanarte.artesanias?psln=bWg0M2s1Y2tyYnUy" class="sanarte-social-chip instagram" target="_blank" rel="noopener noreferrer" title="Seguir a @sanarte.artesanias en Instagram">
              <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
              <span>Instagram @sanarte.artesanias (3.500+ seguidores)</span>
            </a>

            <!-- Facebook -->
            <a href="https://www.facebook.com/share/18MZqpism4/?mibextid=wwXIfr" class="sanarte-social-chip facebook" target="_blank" rel="noopener noreferrer" title="Visitar página oficial en Facebook">
              <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
              <span>Facebook Oficial San Arte</span>
            </a>

            <!-- MercadoLibre Store -->
            <a href="https://listado.mercadolibre.cl/_CustId_192299793?item_id=MLC522990684&category_id=MLC1434&seller_id=192299793&client=recoview-selleritems&recos_listing=true#origin=upp&component=sellerData&typeSeller=classic" class="sanarte-social-chip mercadolibre" target="_blank" rel="noopener noreferrer" title="Ver catálogo completo en MercadoLibre con reputación oficial">
              <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-3zm-1 15l-4-4 1.41-1.41L11 14.17l6.59-6.59L19 9l-8 8z"/></svg>
              <span>Tienda Oficial en MercadoLibre 🛡️</span>
            </a>
          </div>
        </div>
        
        <!-- Nota Ética -->
        <div class="catalog-notice" style="margin-top:20px;">
          <span style="font-size:1.5rem;">🌿</span>
          <div style="text-align:left;">
            <strong>Nota de Honestidad Intelectual y Transparencia:</strong> En Centro Paz y San_Arte creemos en la armonía sincera. Estas piezas poseen un valor estético, cultural y simbólico tradicional (recordatorios de respiración, autoaprecio y serenidad). <em>No atribuimos propiedades curativas médicas a los minerales ni sustituyen el tratamiento médico o psicológico profesional.</em>
          </div>
        </div>
      </div>
    </section>

    <!-- Catálogo de Productos San_Arte -->
    <section style="padding: 10px 0 60px 0;">
      <div class="container">
        
        <!-- Filtros Rápidos -->
        <div class="shop-filter-bar">
          <button type="button" class="shop-filter-btn active" data-filter="all">Todos los Productos (__TOTAL_PRODS__)</button>
          <button type="button" class="shop-filter-btn" data-filter="minerales">Minerales en Bruto</button>
          <button type="button" class="shop-filter-btn" data-filter="joyeria">Joyería & Cristales</button>
          <button type="button" class="shop-filter-btn" data-filter="amuletos">Amuletos & Chakras</button>
          <button type="button" class="shop-filter-btn" data-filter="accesorios">Straps & Tobilleras</button>
          <button type="button" class="shop-filter-btn" data-filter="artesanias">Atrapasueños</button>
        </div>

        <!-- Grilla de Productos -->
        <div class="product-grid" id="productGrid">
__CARDS__
        </div>

        <!-- Opciones de Compra y Envíos -->
        <div class="faq-shop-section">
          <h3 style="font-family:'Lora', serif; font-size:1.5rem; color:var(--verde-dark); margin-bottom:16px;">¿Cómo comprar en San_Arte? Tienes dos formas seguras:</h3>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px; margin-top:16px;">
            
            <div style="background:#FFFFFF; padding:20px; border-radius:var(--radius-sm); border:1px solid var(--borde-suave);">
              <h4 style="color:var(--verde-dark); margin-bottom:8px; display:flex; align-items:center; gap:8px;">
                <span>📲</span> 1. Directo en la Web (Vía WhatsApp)
              </h4>
              <p style="font-size:0.92rem; color:var(--gris); line-height:1.5;">Haz clic en <strong>«Pedir en la Web»</strong> en la pieza que te guste. Hablarás directamente con Valentina para confirmar medidas, detalles y coordinar el pago vía transferencia bancaria directa (sin comisiones extras).</p>
              <ul style="font-size:0.85rem; color:var(--verde-dark); font-weight:700; margin:10px 0 0 16px; padding:0;">
                <li>Entrega presencial en Metro Irarrázaval (Ñuñoa) sin costo de envío.</li>
                <li>Despacho rápido a todo Chile vía Starken o Chilexpress por pagar.</li>
              </ul>
            </div>

            <div style="background:#FFFFFF; padding:20px; border-radius:var(--radius-sm); border:1px solid #FFE082;">
              <h4 style="color:#7A5700; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
                <span>🛡️</span> 2. A través de MercadoLibre
              </h4>
              <p style="font-size:0.92rem; color:var(--gris); line-height:1.5;">Si prefieres pagar con tarjeta de crédito en cuotas, débito o contar con la garantía del programa Compra Protegida de MercadoLibre, haz clic en <strong>«Comprar también en MercadoLibre»</strong>.</p>
              <ul style="font-size:0.85rem; color:#7A5700; font-weight:700; margin:10px 0 0 16px; padding:0;">
                <li>Garantía oficial de Mercado Pago y Mercado Envíos.</li>
                <li>Historial y reputación comprobada como vendedora.</li>
              </ul>
            </div>

          </div>
        </div>

      </div>
    </section>

    <!-- Banner Final de Consulta y Pedidos Personalizados -->
    <section class="cta-banner" id="contacto">
      <div class="container">
        <h2>¿Buscas un amuleto especial o un encargo personalizado?</h2>
        <p>Escríbenos directamente a nuestro WhatsApp oficial y Valentina te orientará sobre disponibilidad de piedras en bruto, tallas y combinaciones.</p>
        <div class="cta-buttons">
          <a href="https://wa.me/56965163893?text=Hola%20Valentina%20%F0%9F%92%8E%20Quisiera%20consultar%20sobre%20un%20encargo%20o%20pieza%20de%20San_Arte%20Artesan%C3%ADas." class="btn btn-whatsapp btn-lg" data-wa-action="tienda-general" target="_blank" rel="noopener noreferrer">
            <svg fill="currentColor" viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0012.04 2zm.01 1.67c4.54 0 8.24 3.7 8.24 8.24 0 2.2-.86 4.27-2.42 5.82-1.55 1.56-3.62 2.42-5.82 2.42-1.47 0-2.9-.39-4.16-1.13l-.3-.18-3.1.81.83-3.02-.2-.31c-.81-1.3-1.24-2.8-1.24-4.41 0-4.54 3.7-8.24 8.24-8.24zm4.52 11.66c-.25-.13-1.47-.72-1.7-.81-.23-.08-.39-.13-.56.13-.17.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.13-1.06-.39-2.02-1.25-.75-.67-1.25-1.5-1.4-1.75-.14-.25-.02-.39.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.42.08-.17.04-.31-.02-.44-.06-.13-.56-1.34-.76-1.84-.2-.48-.4-.42-.56-.43h-.47c-.17 0-.44.06-.67.31-.23.25-.88.86-.88 2.1 0 1.24.9 2.44 1.03 2.61.13.17 1.77 2.7 4.29 3.79.6.26 1.07.41 1.43.53.6.19 1.15.16 1.58.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.08.15-1.18-.07-.1-.23-.17-.48-.29z"/></svg>
            <span>Consultar por WhatsApp (+56 9 6516 3893)</span>
          </a>
        </div>
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer>
    <div class="container footer-grid">
      <div class="footer-brand">
        <h3>Centro Paz & San_Arte</h3>
        <p>Psicología clínica, terapias integrales y artesanías conscientes con Valentina Castro Núñez. Registro SIS Nº 667344. Consulta en Ñuñoa y Envíos a todo Chile.</p>
        <div style="margin-top:14px; display:flex; gap:10px;">
          <a href="https://www.instagram.com/sanarte.artesanias?psln=bWg0M2s1Y2tyYnUy" target="_blank" rel="noopener noreferrer" style="color:#C13584; font-weight:700; font-size:0.85rem;" title="Instagram San_Arte">📸 @sanarte.artesanias</a>
          <span>·</span>
          <a href="https://www.facebook.com/share/18MZqpism4/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer" style="color:#1877F2; font-weight:700; font-size:0.85rem;" title="Facebook San Arte">📘 Facebook</a>
          <span>·</span>
          <a href="https://listado.mercadolibre.cl/_CustId_192299793" target="_blank" rel="noopener noreferrer" style="color:var(--dorado-dark); font-weight:700; font-size:0.85rem;" title="MercadoLibre Tienda">🛡️ MercadoLibre</a>
        </div>
      </div>

      <div class="footer-col">
        <h4>Terapias Integrales</h4>
        <ul class="footer-links">
          <li><a href="terapias.html">Guía de Terapias</a></li>
          <li><a href="psicologia-transpersonal-integral.html">Psicología Transpersonal</a></li>
          <li><a href="mindfulness.html">Técnicas de Mindfulness</a></li>
          <li><a href="hipnosis-terapeutica.html">Hipnosis Ericksoniana</a></li>
          <li><a href="psicoterapia-corporal.html">Psicoterapia Corporal</a></li>
          <li><a href="arteterapia.html">Arteterapia Creativa</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>San_Arte & Bienestar</h4>
        <ul class="footer-links">
          <li><a href="sanarte.html">Catálogo San_Arte</a></li>
          <li><a href="artesanias-joyas.html">Artesanías y Joyas</a></li>
          <li><a href="https://www.instagram.com/sanarte.artesanias" target="_blank" rel="noopener noreferrer">Instagram @sanarte.artesanias</a></li>
          <li><a href="https://www.facebook.com/share/18MZqpism4/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer">Facebook San Arte</a></li>
          <li><a href="https://listado.mercadolibre.cl/_CustId_192299793" target="_blank" rel="noopener noreferrer">Tienda MercadoLibre</a></li>
          <li><a href="blog/">Biblioteca Clínica →</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Contacto & Legal</h4>
        <ul class="footer-links">
          <li><a href="https://wa.me/56965163893" target="_blank" rel="noopener noreferrer">WhatsApp: +56 9 6516 3893</a></li>
          <li><a href="mailto:contacto.centropaz@gmail.com">contacto.centropaz@gmail.com</a></li>
          <li><a href="psicologo-nunoa.html">Consulta Ñuñoa</a></li>
          <li><a href="reembolso-isapre-psicologia.html">Reembolso Isapres</a></li>
          <li><a href="privacidad.html">Política de Privacidad</a></li>
        </ul>
      </div>
    </div>

    <div class="container footer-bottom">
      <p>© 2026 Centro Paz (CPAZ) · Psicóloga Valentina Castro Núñez · Registro SIS Nº 667344 · San_Arte Artesanías y Joyas · <a href="privacidad.html">Privacidad</a> · <a href="blog/">Blog</a></p>
    </div>
  </footer>

  <script src="app.js?v=20261021.1"></script>
  <script>
    // Filtro interactivo de productos
    document.querySelectorAll('.shop-filter-btn').forEach(function(btn) {
      btn.addEventListener('click', function() {
        document.querySelectorAll('.shop-filter-btn').forEach(function(b) { b.classList.remove('active'); });
        this.classList.add('active');
        var filter = this.getAttribute('data-filter');
        var cards = document.querySelectorAll('#productGrid .product-card');
        cards.forEach(function(card) {
          if (filter === 'all' || card.getAttribute('data-category') === filter) {
            card.style.display = '';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  </script>
</body>
</html>"""

    output = template.replace("__PAGE_TITLE__", page_title)
    output = output.replace("__CANONICAL_URL__", canonical_url)
    output = output.replace("__SCHEMA_JSON__", schema_json)
    output = output.replace("__TOTAL_PRODS__", str(total_prods))
    output = output.replace("__CARDS__", cards_joined)
    return output

def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    # 1. Generate sanarte.html
    html_sanarte = build_page(
        canonical_url="https://www.centropaz.cl/sanarte.html",
        page_title="San_Arte Artesanías y Joyas con Significado | Tienda Centro Paz"
    )
    with open(os.path.join(root_dir, 'sanarte.html'), 'w', encoding='utf-8') as f:
        f.write(html_sanarte)
    print("Created sanarte.html successfully.")

    # 2. Update artesanias-joyas.html
    html_artesanias = build_page(
        canonical_url="https://www.centropaz.cl/artesanias-joyas.html",
        page_title="Artesanías y Joyas con Significado Simbólico | San_Arte Centro Paz"
    )
    with open(os.path.join(root_dir, 'artesanias-joyas.html'), 'w', encoding='utf-8') as f:
        f.write(html_artesanias)
    print("Updated artesanias-joyas.html successfully.")

if __name__ == '__main__':
    main()
