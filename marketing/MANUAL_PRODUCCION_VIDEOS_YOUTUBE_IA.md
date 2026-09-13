# 🎬 Manual de Producción de Videos Verticales (Shorts / Reels / TikTok) con YouTube IA

> **Propósito:** Automatizar la creación y renderizado de videos clínicos de alto impacto para Centro Paz en formato vertical 9:16 (1080x1920) con voz chilena empática, subtítulos dinámicos integrados y música de fondo, liberando a Valentina para la **atención 100% personal de pacientes**.

---

## 1. Arquitectura y Roles

* **Producción Audiovisual:** Delegada en el repositorio local [`/Users/nigoku/Proyectos/youtube-ia`](/Users/nigoku/Proyectos/youtube-ia).
* **Guiones Clínicos:** Centralizados en [`marketing/GUIONES_VIDEO_VERTICALES.md`](./GUIONES_VIDEO_VERTICALES.md).
* **Atención de Pacientes e Ingreso:** **100% exclusiva, personal y empática por Valentina Castro Núñez** (`+56 9 6516 3893`). Cero bots, cero respuestas pre-enlatadas.

---

## 2. Flujo de Generación de un Episodio / Short

### Paso 1: Definir el guion en `youtube-ia`

Crear la carpeta del episodio en `youtube-ia/episodes/<id_episodio>/` con su archivo `scenes_es.yaml`:

```yaml
episode: cpaz_short01_tdah
lang: es
title: "3 Señales de TDAH en Adultos que siempre confundiste con flojera"
aspect_ratio: "9:16"             # Activa resolución 1080x1920
voice_profile: "chilean_warm"     # Voz empática chilena (es-CL-CatalinaNeural)
burn_subtitles: true             # Incrusta subtítulos en el tercio inferior
scenes:
  - id: "01_gancho"
    text: "¿Sientes que tienes el potencial para hacer todo, pero te quedas paralizado frente a una tarea simple?"
    camera_motion: "slow_push_in"
  - id: "02_paralisis_ejecutiva"
    text: "Número uno: procrastinación no por desinterés, sino por parálisis ejecutiva. Tu cerebro necesita un nivel mínimo de dopamina para arrancar."
    camera_motion: "dramatic_zoom"
  - id: "03_masking_rechazo"
    text: "Número dos: agotamiento crónico por masking. Y número tres: hipersensibilidad al rechazo o miedo intenso a fallar."
    camera_motion: "slow_pan_right"
  - id: "04_cta_centropaz"
    text: "En Centro Paz te acompañamos con enfoque neuroafirmativo, en sesiones online y en Ñuñoa con reembolso Isapre. Escríbenos por WhatsApp en el enlace de la bio."
    camera_motion: "slow_push_in"
```

### Paso 2: Generar o vincular las imágenes

Colocar las imágenes de cada escena (`01_gancho.png`, etc.) en:
`/Users/nigoku/Proyectos/youtube-ia/assets/images/<id_episodio>/local/`

> **Tip:** Las piezas de feed en `centro-paz/assets/instagram/post_*.png` pueden enmarcarse sobre lienzo 1080x1920 con fondo desenfocado elegante.

### Paso 3: Ejecutar el pipeline de renderizado

Desde el directorio `/Users/nigoku/Proyectos/youtube-ia`:

```bash
python3 -m agent.pipeline --episode <id_episodio> --lang es --images local
```

El pipeline ejecutará automáticamente:
1. **Síntesis de voz neural:** con inflexión empática y natural.
2. **Animación de cámara 2.5D / Ken Burns:** aplicando paneos y zooms sobre cada lámina según el guion.
3. **Concatenación de clips:** ensamble a 25 fps en resolución vertical 1080x1920.
4. **Banda sonora:** mezcla adaptativa con fade-in y fade-out.
5. **Quemado de subtítulos móviles:** estilo adaptado a pantallas de smartphone (respetando los márgenes de interfaz de TikTok/Reels).

### Paso 4: Resultados

Los archivos listos para publicar se exportan en:
* Video vertical terminado: `output/<id_episodio>_es_local.mp4`
* Archivo de subtítulos: `output/<id_episodio>_es_local.srt`

---

## 3. Catálogo de Guiones Disponibles para Renderizar

1. **`cpaz_short01_tdah`**: 3 señales de TDAH en adultos confundidas con flojera.
2. **`cpaz_short02_isapre`**: La matemática secreta del reembolso de Isapre (50%-80% devolución).
3. **`cpaz_short03_crianza`**: Qué hacer ante desbordes emocionales o rabietas infantiles.
