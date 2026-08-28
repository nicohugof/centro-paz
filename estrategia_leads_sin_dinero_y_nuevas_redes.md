# 🚀 Estrategias de Captación de Pacientes Sin Dinero (Zero-Budget) & Nuevas Redes Sociales

Este documento resume la investigación sobre **cómo generar pacientes y leads calificados de forma 100% gratuita y automatizable** para Centro Paz en **Ñuñoa y Online**.

---

## 📺 1. Redes Sociales Inexploradas con Mayor Potencial Orgánico

| Red Social | Por qué funciona para Psicología & Neurodivergencias | Formato & Acción en Centro Paz |
| :--- | :--- | :--- |
| **YouTube Shorts** | **El algoritmo #1 para búsquedas a largo plazo.** Un Short indexa en Google Search de por vida cuando la gente busca *"como saber si tengo TDAH adulto chile"* o *"reembolso isapre psicologia"*. | Videos de 30-40s generados con [`agent/video_shorts_generator.py`](file:///Users/nigoku/CPAZ/agent/video_shorts_generator.py). |
| **Pinterest** | **Búsquedas visuales de mamás y mujeres jóvenes (25-45 años).** Altísima tasa de guardados en tableros de salud mental, infografías de crianza y TDAH. | Subir los 14 PNGs de [`assets/instagram/`](file:///Users/nigoku/CPAZ/assets/instagram/) como "Idea Pins" con enlace directo a la web. |
| **LinkedIn** | **Captación de profesionales corporativos con planes de Isapre top.** Los adultos con sobrecarga laboral y sospecha de TDAH interactúan activamente con posts de parálisis ejecutiva y límites. | Artículos cortos y posts reflexivos firmados por Valentina Castro. |
| **TikTok** | **Mayor viralidad inmediata para neurodivergencias.** No requiere seguidores previos para alcanzar miles de visualizaciones. | Reutilizar exactamente los mismos videos de YouTube Shorts. |

---

## 💡 2. Los 5 Métodos Gratuitos (Zero-Budget) para Generar Pacientes Hoy

### 🎯 Método 1: Social Listening & Ayuda Clínica en Foros Locales
* **Mecánica:** Monitorear Reddit (`r/chile`), Twitter/X y Grupos de Facebook de Ñuñoa/Santiago donde personas publican a diario: *"¿Recomiendan psicólogo para TDAH?", "¿Alguien sabe de psicóloga infantil en Ñuñoa?", "¿Cómo reembolsan en Isapre?"*.
* **Herramienta en el repo:**
  ```bash
  python3 -m agent.organic_lead_scout --query "tdah"
  python3 -m agent.organic_lead_scout --query "nunoa"
  ```
* **Efecto:** Al responder con sustento clínico y dejar el enlace al orientador o WhatsApp, se generan contactos directos con cero inversión.

---

### 🎯 Método 2: Embudo del Lead Magnet (Guía Gratuita 7 Claves en PDF)
* **Mecánica:** En lugar de vender la sesión directamente (que genera fricción), se ofrece en comunidades: *"Comparto gratis la Guía de 7 Claves de Regulación Emocional y Sensorial en PDF para adultos y familias"*.
* **Conversión:** Quien pide la guía por WhatsApp (**`+56 9 6516 3893`**) recibe el PDF interactivo. De cada 10 personas que la solicitan, **2 a 3 terminan agendando su primera sesión**.
* **Archivo:** [`https://www.centropaz.cl/guia_7_claves_regulacion_centro_paz.pdf`](https://www.centropaz.cl/guia_7_claves_regulacion_centro_paz.pdf)

---

### 🎯 Método 3: Ficha de Google Perfil de Negocio (Google Maps Ñuñoa)
* **Mecánica:** Crear o reclamar gratis el perfil en **Google Business** como:  
  `Centro Paz — Psicología Clínica & Neurodivergencias Ñuñoa`.
* **Beneficio:** Aparece en el mapa local de Google cuando cualquier vecino de Ñuñoa o Providencia busca *"psicólogo cerca de mí"*.

---

### 🎯 Método 4: Alianzas y Derivación Cruzada Local en Ñuñoa
* **Mecánica:** Contactar por mensaje o email a profesionales complementarios de la zona que no compiten con psicoterapia:
  - Fonoaudiólogos y Terapeutas Ocupacionales de Ñuñoa/La Reina.
  - Centros médicos o neurólogos infantiles/adultos del sector.
  - Equipos PIE de colegios de Ñuñoa.
* **Mensaje:** Ofrecerse como red de derivación para psicoterapia neuroafirmativa y orientación a padres.

---

### 🎯 Método 5: Automatización de Contenidos Multi-Canal (1 Esfuerzo ➡️ 5 Redes)
* **Mecánica:** 1 solo video vertical o infografía se publica simultáneamente en:
  1. YouTube Shorts
  2. TikTok
  3. Instagram Reels
  4. Facebook Reels
  5. Pinterest Idea Pin
* **Herramienta:** [`agent/video_shorts_generator.py`](file:///Users/nigoku/CPAZ/agent/video_shorts_generator.py)
