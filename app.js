/**
 * Centro Paz (CPAZ) — Motor de Interacción y Alta Conversión de Pacientes
 * Diseñado para maximizar la captación y resolver objeciones en tiempo real.
 */

const CPAZ_CONFIG = {
  whatsappNumber: "56965163893",
  email: "contacto.centropaz@gmail.com",
  instagram: "centropaz.cl",
  tiktok: "centropaz.cl",
  facebook: "https://www.facebook.com/profile.php?id=61593207820690",
  domain: "www.centropaz.cl",
  therapistName: "Valentina Castro Núñez",
  centerName: "Centro Paz",
  standardFee: 45000, // Arancel estándar de referencia en CLP
};

function getUTMContext() {
  try {
    const params = new URLSearchParams(window.location.search);
    const source = params.get("utm_source") || params.get("source") || params.get("ref");
    const campaign = params.get("utm_campaign") || params.get("c");
    if (source || campaign) {
      return `\n\n[Ref: ${source || "web"}${campaign ? ' · ' + campaign : ''}]`;
    }
  } catch (e) {}
  return "";
}

// Estado del Triaje / Orientador
const triageState = {
  step: 1,
  forWhom: null,
  reason: null,
  modality: null,
  timePreference: "Tarde",
};

// Datos del flujo del Orientador
const triageData = {
  who: {
    title: "¿Para quién buscas atención psicológica?",
    desc: "Selecciona el perfil de quien recibirá las sesiones para orientar el enfoque terapéutico.",
    options: [
      { id: "adulto", icon: "👤", title: "Adulto (18+ años)", desc: "Online (todo Chile) o Presencial en Ñuñoa. Ansiedad, depresión, personalidad o diagnóstico." },
      { id: "joven", icon: "🌱", title: "Joven / Adolescente (12 a 17 años)", desc: "Online (todo Chile) o Presencial en Ñuñoa. Regulación del ánimo, crisis y autoconocimiento." },
      { id: "psicodiagnostico", icon: "📋", title: "Evaluación Psicodiagnóstica / Derivación", desc: "Evaluación clínica estructurada de personalidad y estado del ánimo con informe escrito." }
    ]
  },
  reason: {
    adulto: [
      { id: "ansiedad", icon: "🌊", title: "Ansiedad y Crisis de Angustia", desc: "Manejo de angustia, crisis de pánico, sobrepensamiento y síntomas somáticos." },
      { id: "depresion", icon: "🌱", title: "Depresión y Trastornos del Ánimo", desc: "Desánimo, pérdida de motivación, anhedonia y fluctuaciones anímicas." },
      { id: "personalidad", icon: "🧩", title: "Trastornos de la Personalidad / TLP", desc: "Inestabilidad emocional, desregulación afectiva y patrones vinculares." },
      { id: "psicodiagnostico", icon: "📋", title: "Psicodiagnóstico e Informe Clínico", desc: "Evaluación diagnóstica formal para clarificación clínica o interconsulta." }
    ],
    joven: [
      { id: "ansiedad_joven", icon: "🌊", title: "Ansiedad, angustia o sobrecarga", desc: "Manejo de crisis, sobreexigencia y herramientas de autorregulación." },
      { id: "animo_joven", icon: "🌱", title: "Desánimo, cambios anímicos o aislamiento", desc: "Acompañamiento en fluctuaciones del ánimo, autoestima y sentido vital." },
      { id: "regulacion_joven", icon: "🧩", title: "Regulación emocional e identidad", desc: "Comprensión de emociones intensas, vínculos e impulsividad." },
      { id: "eval_joven", icon: "📋", title: "Evaluación psicológica / Diagnóstica", desc: "Clarificación del perfil emocional y psicológico juvenil." }
    ],
    psicodiagnostico: [
      { id: "eval_personalidad", icon: "🧩", title: "Evaluación de Personalidad y Estructura", desc: "Evaluación clínica para diagnóstico diferencial de rasgos y funcionamiento." },
      { id: "eval_animo", icon: "🌱", title: "Evaluación del Estado del Ánimo", desc: "Evaluación diagnóstica en cuadros afectivos y fluctuaciones del ánimo." },
      { id: "informe_interconsulta", icon: "📄", title: "Informe para Psiquiatría o Médico", desc: "Proceso estructurado con sesión de devolución e informe clínico formal." },
      { id: "clarificacion_dx", icon: "🧭", title: "Clarificación Diagnóstica Integral", desc: "Segunda opinión clínica basada en baterías diagnósticas validadas." }
    ]
  },
  modality_general: [
    { id: "online", icon: "💻", title: "Online (Videollamada Segura)", desc: "Disponible para todo Chile para adultos y jóvenes desde los 12 años." },
    { id: "presencial", icon: "🛋️", title: "Presencial en Ñuñoa (Santiago)", desc: "Sesión en consulta clínica en un entorno de calma y confidencialidad." },
    { id: "indiferente", icon: "✨", title: "Cualquiera de las dos", desc: "Sujeto a disponibilidad y coordinación con Valentina." }
  ]
};

// Datos del Checklist / Screener
const checklistData = {
  ansiedad_animo: [
    "Sientes una opresión constante en el pecho, taquicardia o dificultad para relajarte.",
    "Experimentas sobrepensamiento incesante, anticipando siempre escenarios difíciles.",
    "Has tenido crisis de angustia o ataques de pánico que te hacen sentir sin control.",
    "Sientes una desmotivación profunda, vacío o pérdida de interés en lo que antes disfrutabas.",
    "Te cuesta levantarte por las mañanas o experimentas fluctuaciones abruptas en tu ánimo y energía.",
    "Sientes que el estrés diario sobrepasa tus recursos y te mantiene en alerta permanente."
  ],
  personalidad_diag: [
    "Experimentas cambios emocionales muy intensos en pocas horas y te cuesta volver a la calma.",
    "Sientes un miedo profundo al abandono o al rechazo en tus vínculos y relaciones cercanas.",
    "Tienes dudas persistentes sobre quién eres o experimentas una sensación de vacío interno.",
    "Reaccionas con impulsividad o frustración intensa ante situaciones de desacuerdo.",
    "Buscas una evaluación diagnóstica estructurada para entender con certeza qué te ocurre.",
    "Tu médico psiquiatra o equipo tratante te solicitó un informe psicodiagnóstico formal."
  ]
};

window.dataLayer = window.dataLayer || [];

/**
 * Disparador unificado de analítica y conversiones CPAZ
 * Empuja eventos a dataLayer (GTM / GA4) y ejecuta gtag() si está disponible.
 */
function trackCPAZEvent(eventName, params = {}) {
  const eventPayload = {
    event: eventName,
    page_location: window.location.href,
    page_path: window.location.pathname,
    timestamp: new Date().toISOString(),
    ...params
  };

  window.dataLayer.push(eventPayload);

  if (typeof window.gtag === "function") {
    window.gtag("event", eventName, params);
  }

  if (window.location.hostname === "localhost" || window.location.search.includes("debug=true")) {
    console.log(`[CPAZ Analytics] Event: ${eventName}`, eventPayload);
  }
}

let currentChecklistTab = "adultos";
let selectedSymptoms = new Set();

document.addEventListener("DOMContentLoaded", () => {
  initAnalyticsTracking();
  initTriage();
  initFAQ();
  initWhatsAppLinks();
  initMobileNav();
  initCalculator();
  initChecklist();
  initStickyWhatsApp();
  initLibrary();
  initCoreWebVitals();
});

/* ----------------------------------------------------
   MONITOREO DE EVENTOS & CAPTACIÓN DE CONVERSIONES (GA4 / ADS)
---------------------------------------------------- */
function initAnalyticsTracking() {
  document.addEventListener("click", (e) => {
    const link = e.target.closest("a");
    if (!link) return;

    const href = link.getAttribute("href") || "";
    if (href.includes("wa.me") || href.includes("api.whatsapp.com")) {
      const action = link.getAttribute("data-wa-action") || link.id || "general_whatsapp";
      trackCPAZEvent("generate_lead", {
        lead_type: "whatsapp",
        lead_source: action,
        element_text: link.innerText ? link.innerText.trim().slice(0, 50) : "WhatsApp CTA",
        value: 45000,
        currency: "CLP"
      });
    }
  });
}

/* ----------------------------------------------------
   MONITOREO DE RENDIMIENTO Y CORE WEB VITALS
---------------------------------------------------- */
function initCoreWebVitals() {
  if (!("PerformanceObserver" in window)) return;
  try {
    const poLCP = new PerformanceObserver((list) => {
      const entries = list.getEntries();
      const lastEntry = entries[entries.length - 1];
      if (lastEntry && window.location.hostname === "localhost") {
        console.log(`[CPAZ Web 2.0 CWV] LCP: ${Math.round(lastEntry.startTime)} ms`);
      }
    });
    poLCP.observe({ type: "largest-contentful-paint", buffered: true });

    let clsValue = 0;
    const poCLS = new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        if (!entry.hadRecentInput) {
          clsValue += entry.value;
        }
      }
      if (window.location.hostname === "localhost") {
        console.log(`[CPAZ Web 2.0 CWV] CLS: ${clsValue.toFixed(3)}`);
      }
    });
    poCLS.observe({ type: "layout-shift", buffered: true });
  } catch (e) {}
}

/* ----------------------------------------------------
   ORIENTADOR DE CONSULTA / TRIAJE
---------------------------------------------------- */
function initTriage() {
  const step1Container = document.getElementById("step1-options");
  const step3Container = document.getElementById("step3-options");

  if (!step1Container) return;

  // Render Paso 1
  step1Container.innerHTML = triageData.who.options.map(opt => `
    <button type="button" class="option-btn" data-id="${opt.id}" onclick="selectTriageWho('${opt.id}', '${opt.title.replace(/'/g, "\\'")}')">
      <span class="option-icon">${opt.icon}</span>
      <span class="option-title">${opt.title}</span>
      <span class="option-sub">${opt.desc}</span>
    </button>
  `).join("");

  // Render Paso 3 inicial
  if (step3Container) {
    step3Container.innerHTML = triageData.modality_general.map(opt => `
      <button type="button" class="option-btn" data-id="${opt.id}" onclick="selectTriageModality('${opt.id}', '${opt.title.replace(/'/g, "\\'")}')">
        <span class="option-icon">${opt.icon}</span>
        <span class="option-title">${opt.title}</span>
        <span class="option-sub">${opt.desc}</span>
      </button>
    `).join("");
  }
}

window.selectTriageWho = function(id, label) {
  triageState.forWhom = { id, label };
  updateOptionSelection("step1-options", id);

  const step2Container = document.getElementById("step2-options");
  const reasons = triageData.reason[id] || triageData.reason.adulto;

  if (step2Container) {
    step2Container.innerHTML = reasons.map(opt => `
      <button type="button" class="option-btn" data-id="${opt.id}" onclick="selectTriageReason('${opt.id}', '${opt.title.replace(/'/g, "\\'")}')">
        <span class="option-icon">${opt.icon}</span>
        <span class="option-title">${opt.title}</span>
        <span class="option-sub">${opt.desc}</span>
      </button>
    `).join("");
  }

  setTimeout(() => goToStep(2), 220);
};

window.selectTriageReason = function(id, label) {
  triageState.reason = { id, label };
  updateOptionSelection("step2-options", id);

  // Adaptar dinámicamente el Paso 3 (Modalidad)
  const step3Desc = document.querySelector("#triage-step-3 .triage-step-desc");
  const step3Container = document.getElementById("step3-options");

  if (step3Container) {
    if (step3Desc) {
      step3Desc.innerHTML = "Modalidad <strong>Online</strong> disponible para todo Chile (adultos y jóvenes desde los 12 años), y <strong>Presencial</strong> en nuestra consulta en Ñuñoa (Santiago).";
    }

    step3Container.innerHTML = triageData.modality_general.map(opt => `
      <button type="button" class="option-btn" data-id="${opt.id}" onclick="selectTriageModality('${opt.id}', '${opt.title.replace(/'/g, "\\'")}')">
        <span class="option-icon">${opt.icon}</span>
        <span class="option-title">${opt.title}</span>
        <span class="option-sub">${opt.desc}</span>
      </button>
    `).join("");
  }

  setTimeout(() => goToStep(3), 220);
};

window.selectTriageModality = function(id, label) {
  triageState.modality = { id, label };
  updateOptionSelection("step3-options", id);
  setTimeout(() => {
    buildTriageResult();
    goToStep(4);
  }, 250);
};

window.setTimePreference = function(timeStr, evt) {
  triageState.timePreference = timeStr;
  document.querySelectorAll(".time-btn").forEach(b => b.classList.remove("active"));
  const clickedBtn = evt && evt.currentTarget;
  if (clickedBtn) clickedBtn.classList.add("active");
  buildTriageResult();
};

window.goToStep = function(stepNum) {
  triageState.step = stepNum;

  for (let i = 1; i <= 4; i++) {
    const stepEl = document.getElementById(`triage-step-${i}`);
    const nodeEl = document.getElementById(`node-step-${i}`);
    
    if (stepEl) {
      if (i === stepNum) {
        stepEl.classList.add("active");
      } else {
        stepEl.classList.remove("active");
      }
    }

    if (nodeEl) {
      nodeEl.classList.remove("active", "completed");
      if (i === stepNum) {
        nodeEl.classList.add("active");
      } else if (i < stepNum) {
        nodeEl.classList.add("completed");
      }
    }
  }

  const progressBar = document.getElementById("triage-progress-bar");
  if (progressBar) {
    const percentages = { 1: "0%", 2: "33%", 3: "66%", 4: "100%" };
    progressBar.style.width = percentages[stepNum] || "0%";
  }

  const triageSection = document.getElementById("orientador");
  if (triageSection && stepNum > 1) {
    triageSection.scrollIntoView({ behavior: "smooth", block: "start" });
  }
};

window.restartTriage = function() {
  triageState.forWhom = null;
  triageState.reason = null;
  triageState.modality = null;

  document.querySelectorAll(".option-btn").forEach(btn => btn.classList.remove("selected"));
  goToStep(1);
};

function updateOptionSelection(containerId, selectedId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.querySelectorAll(".option-btn").forEach(btn => {
    btn.classList.toggle("selected", btn.dataset.id === selectedId);
  });
}

function buildTriageResult() {
  const whoLabel = triageState.forWhom?.label || "Atención general";
  const reasonLabel = triageState.reason?.label || "Bienestar emocional";
  const modLabel = triageState.modality?.label || "Por coordinar";
  const timePref = triageState.timePreference || "Horario flexible";

  let recommendedApproach = "Psicoterapia Individual con Ps. Valentina Castro Núñez";
  if (triageState.forWhom?.id === "psicodiagnostico" || triageState.reason?.id?.includes("psicodiagnostico") || triageState.reason?.id?.includes("eval")) {
    recommendedApproach = "Evaluación Psicodiagnóstica e Informe Clínico Formal";
  } else if (triageState.reason?.id === "personalidad" || triageState.reason?.id === "regulacion_joven") {
    recommendedApproach = "Abordaje Clínico en Trastornos de la Personalidad (TLP) & Regulación";
  } else if (triageState.reason?.id === "depresion" || triageState.reason?.id === "animo_joven") {
    recommendedApproach = "Psicoterapia para Depresión y Procesos del Ánimo";
  } else if (triageState.reason?.id === "ansiedad" || triageState.reason?.id === "ansiedad_joven") {
    recommendedApproach = "Tratamiento Clínico de Ansiedad, Pánico y Manejo de Crisis";
  } else if (triageState.forWhom?.id === "joven") {
    recommendedApproach = "Psicoterapia para Jóvenes y Adolescentes (12 a 17 años)";
  }

  let relevantArticle = {
    title: "Artículo clínico: 7 Claves de regulación del sistema nervioso ante la ansiedad",
    url: "blog/regulacion-ansiedad.html"
  };
  if (triageState.forWhom?.id === "psicodiagnostico" || triageState.reason?.id?.includes("psicodiagnostico") || triageState.reason?.id?.includes("eval")) {
    relevantArticle = {
      title: "Guía clínica: ¿En qué consiste una evaluación psicodiagnóstica?",
      url: "blog/primera-sesion.html"
    };
  } else if (triageState.reason?.id === "personalidad" || triageState.reason?.id === "regulacion_joven") {
    relevantArticle = {
      title: "Artículo clínico: Regulación emocional y límites sanos sin culpa",
      url: "blog/comunicacion-asertiva-limites.html"
    };
  } else if (triageState.reason?.id === "depresion" || triageState.reason?.id === "animo_joven") {
    relevantArticle = {
      title: "Artículo clínico: El valor de pedir ayuda y recuperar la motivación",
      url: "blog/autocuidado-adultos.html"
    };
  } else {
    relevantArticle = {
      title: "Guía paso a paso: Cómo reembolsar tus sesiones en Isapre y Seguros",
      url: "blog/reembolso-isapre.html"
    };
  }

  const resultBox = document.getElementById("triage-result-content");
  if (resultBox) {
    resultBox.innerHTML = `
      <div class="result-summary">
        <div class="result-icon">
          <svg fill="currentColor" viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
        </div>
        <div class="result-details">
          <span class="tag-pill" style="margin-bottom:8px; display:inline-block;">Enfoque sugerido</span>
          <h4>${recommendedApproach}</h4>
          <p style="font-size:0.95rem; margin-top:4px;">Tu consulta será atendida directamente por <strong>${CPAZ_CONFIG.therapistName}</strong> en un espacio seguro, empático y con rigor clínico.</p>
          <div class="result-tags">
            <span class="tag-pill">🎯 Para: ${whoLabel}</span>
            <span class="tag-pill">🌱 Motivo: ${reasonLabel}</span>
            <span class="tag-pill">📍 Modalidad: ${modLabel}</span>
          </div>
        </div>
      </div>

      <div style="margin: 20px 0 16px;">
        <label style="font-size:0.9rem; font-weight:700; color:var(--burdeo-dark); display:block; margin-bottom:8px;">
          ¿Qué horario te acomoda más para tus sesiones?
        </label>
        <div style="display:flex; gap:10px; flex-wrap:wrap;">
          <button type="button" class="tab-btn time-btn ${timePref === 'Mañana' ? 'active' : ''}" onclick="setTimePreference('Mañana', event)">🌅 Mañana (09:00 - 13:00)</button>
          <button type="button" class="tab-btn time-btn ${timePref === 'Tarde' ? 'active' : ''}" onclick="setTimePreference('Tarde', event)">🌇 Tarde (14:00 - 20:00)</button>
          <button type="button" class="tab-btn time-btn ${timePref === 'Sábado' ? 'active' : ''}" onclick="setTimePreference('Sábado', event)">🌿 Sábado</button>
        </div>
      </div>

      <div class="result-guarantee">
        🛡️ <strong>Boletas 100% Reembolsables:</strong> Emitimos boleta electrónica oficial para reembolso en tu Isapre y Seguro Complementario de Salud.
      </div>

      <div style="margin-top:16px; padding:12px 16px; background:var(--crema-warm); border-radius:var(--radius-md); border-left:3px solid var(--verde-dark); font-size:0.9rem;">
        <span style="font-weight:700; color:var(--verde-dark); display:block; margin-bottom:4px;">📖 Lectura clínica recomendada para tu caso:</span>
        <a href="${relevantArticle.url}" target="_blank" rel="noopener noreferrer" style="color:var(--burdeo); font-weight:700; text-decoration:none;">${relevantArticle.title} →</a>
      </div>
    `;
  }

  // Generar mensaje personalizado de WhatsApp
  const utmSuffix = getUTMContext();
  const rawMessage = `Hola Valentina 🌿 Estuve revisando el sitio web de Centro Paz y completé el orientador de consulta.\n\n` +
    `• Paciente: ${whoLabel}\n` +
    `• Motivo: ${reasonLabel}\n` +
    `• Modalidad preferida: ${modLabel}\n` +
    `• Preferencia de horario: ${timePref}\n\n` +
    `Me gustaría coordinar una primera sesión contigo. ¿Qué disponibilidad de fecha y hora tienes? Muchas gracias.${utmSuffix}`;

  const encodedMessage = encodeURIComponent(rawMessage);
  const whatsappUrl = `https://wa.me/${CPAZ_CONFIG.whatsappNumber}?text=${encodedMessage}`;

  const ctaBtn = document.getElementById("triage-whatsapp-btn");
  if (ctaBtn) {
    ctaBtn.href = whatsappUrl;
    ctaBtn.target = "_blank";
    ctaBtn.rel = "noopener noreferrer";
  }

  // Micro-conversión: Orientador completado
  trackCPAZEvent("complete_triage", {
    triage_target: whoLabel,
    triage_reason: reasonLabel,
    triage_modality: modLabel,
    triage_schedule: timePref
  });
}

/* ----------------------------------------------------
   SIMULADOR DE REEMBOLSO ISAPRE / SEGUROS
---------------------------------------------------- */
function initCalculator() {
  const isapreSelect = document.getElementById("calc-isapre");
  const insuranceSelect = document.getElementById("calc-insurance");

  if (isapreSelect) {
    isapreSelect.addEventListener("change", updateReimbursementCalc);
  }
  if (insuranceSelect) {
    insuranceSelect.addEventListener("change", updateReimbursementCalc);
  }

  updateReimbursementCalc();
}

window.updateReimbursementCalc = function() {
  const isapreSelect = document.getElementById("calc-isapre");
  const insuranceSelect = document.getElementById("calc-insurance");
  const resultAmount = document.getElementById("calc-copay-amount");
  const resultSub = document.getElementById("calc-reimburse-sub");
  const calcWaBtn = document.getElementById("calc-whatsapp-btn");

  if (!isapreSelect || !resultAmount) return;

  const isapreCoverage = parseFloat(isapreSelect.value) || 0.60;
  const hasInsurance = insuranceSelect ? insuranceSelect.value === "yes" : false;

  let totalReimburseRatio = isapreCoverage;
  if (hasInsurance) {
    totalReimburseRatio = Math.min(isapreCoverage + 0.20, 0.85); // hasta 85% de cobertura combinada
  }

  const baseFee = CPAZ_CONFIG.standardFee;
  const estimatedReimbursed = Math.round(baseFee * totalReimburseRatio);
  const estimatedCopay = baseFee - estimatedReimbursed;

  resultAmount.textContent = `$${estimatedCopay.toLocaleString("es-CL")}`;
  resultSub.textContent = `Reembolso estimado de ~$${estimatedReimbursed.toLocaleString("es-CL")} por sesión`;

  const isapreText = isapreSelect.options[isapreSelect.selectedIndex].text;
  const utmSuffix = getUTMContext();
  const waMessage = `Hola Centro Paz 🌿 Estuve usando el simulador de reembolsos de su web. Tengo Isapre ${isapreText}${hasInsurance ? ' + Seguro Complementario' : ''} y quisiera consultar por aranceles y disponibilidad para agendar mi primera sesión con Valentina.${utmSuffix}`;

  if (calcWaBtn) {
    calcWaBtn.href = `https://wa.me/${CPAZ_CONFIG.whatsappNumber}?text=${encodeURIComponent(waMessage)}`;
  }

  // Micro-conversión: Cálculo de Reembolso
  trackCPAZEvent("calculate_reimbursement", {
    isapre: isapreText,
    with_insurance: hasInsurance,
    estimated_copay: estimatedCopay,
    estimated_reimburse: estimatedReimbursed
  });
};

/* ----------------------------------------------------
   CHECKLIST INTERACTIVO / AUTODIAGNÓSTICO
---------------------------------------------------- */
function initChecklist() {
  renderChecklist();
}

window.switchChecklistTab = function(tabName) {
  currentChecklistTab = tabName;
  selectedSymptoms.clear();

  document.querySelectorAll(".tab-btn").forEach(btn => {
    if (btn.getAttribute("data-tab") === tabName) {
      btn.classList.add("active");
    } else if (btn.getAttribute("data-tab")) {
      btn.classList.remove("active");
    }
  });

  renderChecklist();
};

function renderChecklist() {
  const container = document.getElementById("symptoms-container");
  if (!container) return;

  const items = checklistData[currentChecklistTab] || [];
  container.innerHTML = items.map((text, idx) => `
    <div class="symptom-item ${selectedSymptoms.has(idx) ? 'checked' : ''}" onclick="toggleSymptom(${idx})">
      <div class="symptom-checkbox">
        <svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
      </div>
      <div class="symptom-text">${text}</div>
    </div>
  `).join("");

  updateChecklistFeedback();
}

window.toggleSymptom = function(idx) {
  if (selectedSymptoms.has(idx)) {
    selectedSymptoms.delete(idx);
  } else {
    selectedSymptoms.add(idx);
  }
  renderChecklist();
};

function updateChecklistFeedback() {
  const feedbackEl = document.getElementById("checklist-feedback");
  const count = selectedSymptoms.size;

  if (!feedbackEl) return;

  if (count === 0) {
    feedbackEl.innerHTML = `
      <div>
        <strong>Selecciona las situaciones con las que te sientas identificado/a.</strong>
        <p style="font-size:0.85rem; margin:0; color:var(--gris);">Te ayudaremos a comprender qué tipo de acompañamiento es el ideal para ti.</p>
      </div>
    `;
  } else {
    const tabLabel = currentChecklistTab === "ansiedad_animo" ? "Ansiedad y Trastornos del Ánimo" : "Personalidad (TLP) y Psicodiagnóstico";
    const utmSuffix = getUTMContext();
    const rawWa = `Hola Valentina 🌿 Estuve revisando el checklist de ${tabLabel} en la web de Centro Paz y me identifiqué con ${count} de las vivencias descritas. Me gustaría consultar por una primera sesión para trabajar en esto.${utmSuffix}`;

    feedbackEl.innerHTML = `
      <div>
        <strong style="color:var(--burdeo-dark);">Te identificas con ${count} vivencia${count > 1 ? 's' : ''}:</strong>
        <p style="font-size:0.9rem; margin:2px 0 0; color:var(--gris);">No tienes que procesar este malestar en soledad. En Centro Paz te acompañamos a encontrar calma, claridad y herramientas clínicas.</p>
      </div>
      <a href="https://wa.me/${CPAZ_CONFIG.whatsappNumber}?text=${encodeURIComponent(rawWa)}" target="_blank" class="btn btn-whatsapp btn-sm" style="flex-shrink:0;">
        <span>Conversar con Valentina por WhatsApp</span>
      </a>
    `;
  }
}

/* ----------------------------------------------------
   ACORDEÓN DE PREGUNTAS FRECUENTES
---------------------------------------------------- */
function initFAQ() {
  const faqItems = document.querySelectorAll(".faq-item");
  faqItems.forEach(item => {
    const question = item.querySelector(".faq-question");
    if (question) {
      question.addEventListener("click", () => {
        const isActive = item.classList.contains("active");
        faqItems.forEach(i => i.classList.remove("active"));
        if (!isActive) {
          item.classList.add("active");
        }
      });
    }
  });
}

/* ----------------------------------------------------
   ENLACES GENERALES A WHATSAPP
---------------------------------------------------- */
function initWhatsAppLinks() {
  const genericLinks = document.querySelectorAll("[data-wa-action]");
  const utmSuffix = getUTMContext();

  genericLinks.forEach(link => {
    const action = link.getAttribute("data-wa-action");
    let msg = "Hola Valentina 🌿 Quisiera consultar por atención psicológica en Centro Paz y disponibilidad de horas.";

    if (action === "ansiedad") {
      msg = "Hola Valentina 🌊 Quisiera consultar por atención clínica para manejo de ansiedad, crisis de angustia y disponibilidad de horas.";
    } else if (action === "depresion") {
      msg = "Hola Valentina 🌱 Quisiera consultar por psicoterapia para depresión, estados del ánimo y disponibilidad de horas.";
    } else if (action === "personalidad") {
      msg = "Hola Valentina 🧩 Quisiera consultar por acompañamiento clínico en Trastorno Límite de la Personalidad (TLP) o regulación emocional.";
    } else if (action === "psicodiagnostico") {
      msg = "Hola Valentina 📋 Quisiera consultar por el proceso de evaluación psicodiagnóstica y emisión de informe clínico formal.";
    } else if (action === "nunoa") {
      msg = "Hola Valentina 🛋️ Quisiera consultar por disponibilidad para sesiones presenciales en la consulta de Ñuñoa.";
    } else if (action === "lead-magnet") {
      msg = "Hola Valentina ✨ Me gustaría solicitar la Guía Gratuita de 7 Claves para la Regulación de la Ansiedad y Emociones.";
    } else if (action === "hero" || action === "sticky") {
      msg = "Hola Valentina 🌿 Vi el sitio web de Centro Paz y me gustaría coordinar una primera sesión contigo.";
    }

    link.href = `https://wa.me/${CPAZ_CONFIG.whatsappNumber}?text=${encodeURIComponent(msg + utmSuffix)}`;
    link.target = "_blank";
    link.rel = "noopener noreferrer";
  });
}

/* ----------------------------------------------------
   MENÚ MÓVIL
---------------------------------------------------- */
function initMobileNav() {
  const navToggle = document.querySelector(".nav-toggle");
  const navLinks = document.querySelector(".nav-links");

  if (navToggle && navLinks) {
    navToggle.addEventListener("click", () => {
      const isOpen = navLinks.classList.toggle("is-open");
      navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      navToggle.setAttribute("aria-label", isOpen ? "Cerrar menú de navegación" : "Abrir menú de navegación");
    });

    navLinks.querySelectorAll("a").forEach(a => {
      a.addEventListener("click", () => {
        navLinks.classList.remove("is-open");
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.setAttribute("aria-label", "Abrir menú de navegación");
      });
    });
  }
}

/* ----------------------------------------------------
   BARRA STICKY MÓVIL (DISMISSIBLE)
---------------------------------------------------- */
function initStickyWhatsApp() {
  const bar = document.getElementById("mobile-sticky-bar");
  const dismiss = document.getElementById("mobile-sticky-dismiss");
  if (!bar || !dismiss) return;

  const hideBar = () => {
    bar.hidden = true;
    document.body.classList.add("sticky-wa-dismissed");
    try {
      sessionStorage.setItem("cpaz-sticky-wa-dismissed", "1");
    } catch (e) {}
  };

  try {
    if (sessionStorage.getItem("cpaz-sticky-wa-dismissed") === "1") {
      hideBar();
    }
  } catch (e) {}

  dismiss.addEventListener("click", hideBar);
}

/* ----------------------------------------------------
   BIBLIOTECA CLÍNICA Y BUSCADOR INTERACTIVO (28 ARTÍCULOS)
---------------------------------------------------- */
const clinicalArticlesList = [
  { slug: "tdah_adultos", category: "tdah", tag: "TDAH Adultos", title: "¿Y si tu cansancio no es flojera, sino TDAH no diagnosticado?", desc: "Diferencias entre procrastinación, baja dopamina y parálisis ejecutiva en la adultez.", time: "6 min" },
  { slug: "reembolso_isapre", category: "isapre", tag: "Reembolso Isapre", title: "Cuánto cuesta REALMENTE ir al psicólogo: Guía de reembolsos Isapre", desc: "Cómo recuperar entre el 50% y el 80% del arancel mediante boleta electrónica oficial.", time: "5 min" },
  { slug: "crianza_regulacion", category: "infantil", tag: "Crianza & Infancia", title: "Pataleta vs. Colapso Sensorial: Cómo acompañar desbordes sin gritos", desc: "Herramientas de corregulación y pautas respetuosas para padres sobrepasados.", time: "7 min" },
  { slug: "masking", category: "tdah", tag: "Neurodivergencias", title: "El precio invisible del masking: Por qué llegas agotado a las 19:00 hrs", desc: "El esfuerzo inconsciente de sobre-adaptarte para encajar en el trabajo y la vida diaria.", time: "6 min" },
  { slug: "terapia_online", category: "general", tag: "Modalidad", title: "Terapia Online en Chile: Efectividad, privacidad y cómo prepararte", desc: "Por qué la atención por videollamada segura tiene la misma efectividad clínica que presencial.", time: "5 min" },
  { slug: "orientacion_padres", category: "infantil", tag: "Crianza & Infancia", title: "Orientación a Padres: Criar con límites claros sin culpa ni castigos", desc: "Sesiones especializadas para madres y padres que buscan pautas de regulación en el hogar.", time: "6 min" },
  { slug: "primera_sesion", category: "general", tag: "Proceso Clínico", title: "¿Qué pasa en tu primera sesión de psicología?", desc: "Paso a paso de un espacio de acogida sin juicios, confidencial y a tu propio ritmo.", time: "4 min" },
  { slug: "burnout_autista", category: "tea", tag: "Autismo (TEA)", title: "Burnout Autista en Adultos: Por qué dormir el fin de semana no te recupera", desc: "Descompresión sensorial, validación de límites y prevención del colapso crónico.", time: "7 min" },
  { slug: "paralisis_ejecutiva", category: "tdah", tag: "TDAH Adultos", title: "Parálisis ejecutiva: Cuando tu mente quiere arrancar pero tu cuerpo se bloquea", desc: "Estrategias de micro-acción y dopamina para superar la barrera del inicio.", time: "5 min" },
  { slug: "regulacion_ansiedad", category: "ansiedad", tag: "Ansiedad & Estrés", title: "7 Claves de regulación del sistema nervioso para frenar el sobrepensamiento", desc: "Herramientas somáticas e integrativas para calmar la respuesta de alarma del cuerpo.", time: "6 min" },
  { slug: "apoyo_neurodivergente_hijos", category: "infantil", tag: "Crianza & Infancia", title: "Mi hijo fue diagnosticado con TEA o TDAH: Primeros pasos para padres", desc: "Cómo procesar el diagnóstico, coordinar apoyos escolares y cuidar el clima familiar.", time: "8 min" },
  { slug: "culpa_parental", category: "infantil", tag: "Crianza & Infancia", title: "Reparar después del grito: Cómo reconectar con tus hijos sin culpa", desc: "La reparación vincular como la herramienta más poderosa de la crianza respetuosa.", time: "5 min" },
  { slug: "reembolso_matematica", category: "isapre", tag: "Reembolso Isapre", title: "La matemática de la salud mental: Cuánto pagas de tu bolsillo por sesión", desc: "Simulación de copagos reales desde $9.000 a $15.000 CLP según tu plan de salud.", time: "5 min" },
  { slug: "tdah_mujeres", category: "tdah", tag: "TDAH Adultos", title: "TDAH en mujeres: El diagnóstico tardío y la autoexigencia silenciosa", desc: "Por qué tantas mujeres son diagnosticadas después de los 25 o 30 años.", time: "7 min" },
  { slug: "sobrecarga_sensorial_ruido", category: "tea", tag: "Neurodivergencias", title: "Hipersensibilidad al ruido y misofonía: No es mal genio, es tu sistema nervioso", desc: "Acomodaciones auditivas y regulación en espacios laborales y domésticos.", time: "6 min" },
  { slug: "reembolso_seguros_cobertura", category: "isapre", tag: "Reembolso Isapre", title: "Doble reembolso: Cómo combinar Isapre + Seguro Complementario", desc: "Guía para presentar la liquidación de Isapre en tu seguro colectivo de empresa.", time: "5 min" },
  { slug: "hiperfoco_burnout", category: "tdah", tag: "TDAH Adultos", title: "El ciclo del hiperfoco y el bajón de energía: Cómo sostener tu productividad", desc: "Manejo del ritmo circadiano y descansos planificados en mentes neurodivergentes.", time: "6 min" },
  { slug: "crianza_rutinas_flexibles", category: "infantil", tag: "Crianza & Infancia", title: "Rutinas visuales y límites amorosos sin batallas diarias", desc: "Cómo organizar las mañanas y noches con niños sin recurrir a amenazas ni premios.", time: "6 min" },
  { slug: "comunicacion_asertiva_limites", category: "ansiedad", tag: "Autoestima", title: "Poner límites sin culpa: Cómo decir que no sin sentir que estás dañando al otro", desc: "Desactivar el complacer compulsivo y cuidar tu espacio personal.", time: "5 min" },
  { slug: "tdah_rechazo_rsd", category: "tdah", tag: "TDAH Adultos", title: "Sensibilidad al Rechazo (RSD): Por qué una crítica duele físicamente", desc: "Comprendiendo la disforia sensible al rechazo en personas con TDAH.", time: "6 min" },
  { slug: "primera_consulta_nunoa", category: "nunoa", tag: "Consulta Ñuñoa", title: "Cómo es tu primera consulta presencial en Ñuñoa", desc: "Ambiente cálido, cercano a Metro Chile España, sin juicios y con boleta Isapre.", time: "4 min" },
  { slug: "terapia_infantil_juego", category: "infantil", tag: "Crianza & Infancia", title: "Terapia infantil a través del juego: Cómo sanan los niños en sesión", desc: "El juego como lenguaje natural para procesar emociones, miedos y cambios.", time: "6 min" },
  { slug: "ansiedad_somatica_cuerpo", category: "ansiedad", tag: "Ansiedad & Estrés", title: "Ansiedad somática: Cuando el cuerpo avisa con opresión en el pecho", desc: "Escuchar las señales físicas de alarma y devolver seguridad al cuerpo.", time: "6 min" },
  { slug: "isapre_licencia_boletas", category: "isapre", tag: "Reembolso Isapre", title: "Guía definitiva de boletas de honorarios y glosas para Isapres", desc: "Qué datos debe tener tu boleta para que el reembolso se apruebe en 48 horas.", time: "5 min" },
  { slug: "desconexion_tecnologica_tdah", category: "tdah", tag: "TDAH Adultos", title: "El ciclo del scroll infinito y la búsqueda de dopamina en TDAH", desc: "Estrategias de fricción ambiental para desconectar pantallas sin frustración.", time: "5 min" },
  { slug: "padres_regulacion_propia", category: "infantil", tag: "Crianza & Infancia", title: "Regularte tú antes de calmar a tu hijo: El secreto de la corregulación", desc: "Por qué un niño desregulado necesita la calma de un adulto, no dos desregulados.", time: "6 min" },
  { slug: "autocuidado_fin_de_semana", category: "ansiedad", tag: "Bienestar", title: "Descanso sensorial de fin de semana: Desconectar sin culpa", desc: "Planificar momentos de baja estimulación para recargar tu sistema nervioso.", time: "5 min" },
  { slug: "tdah_vs_ansiedad", category: "tdah", tag: "TDAH Adultos", title: "¿TDAH o Ansiedad Generalizada? Cómo diferenciarlos clínicamente", desc: "Identificar si la dispersión viene de una corteza prefrontal desregulada o de un estado de alerta.", time: "7 min" }
];

let currentLibraryCategory = "all";
let currentLibraryQuery = "";

function initLibrary() {
  const grid = document.getElementById("library-articles-grid");
  const searchInput = document.getElementById("library-search-input");
  const filterBtns = document.querySelectorAll(".library-filter-btn");

  if (!grid) return;

  function renderLibrary() {
    const filtered = clinicalArticlesList.filter(article => {
      const matchCat = (currentLibraryCategory === "all") || (article.category === currentLibraryCategory);
      const q = currentLibraryQuery.toLowerCase().trim();
      const matchQuery = !q || article.title.toLowerCase().includes(q) || article.desc.toLowerCase().includes(q) || article.tag.toLowerCase().includes(q);
      return matchCat && matchQuery;
    });

    if (filtered.length === 0) {
      grid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 40px 20px; color: var(--gris);">
          <p style="font-size: 1.1rem; margin-bottom: 8px;">No encontramos artículos para "<strong>${currentLibraryQuery}</strong>".</p>
          <p style="font-size: 0.95rem;">Prueba buscando por <em>TDAH, Isapre, Ansiedad, Masking o Crianza</em>.</p>
        </div>
      `;
      return;
    }

    grid.innerHTML = filtered.map(item => `
      <a href="blog/${item.slug}.html" class="library-article-card">
        <div>
          <span class="library-card-tag">${item.tag}</span>
          <h3 class="library-card-title">${item.title}</h3>
          <p class="library-card-desc">${item.desc}</p>
        </div>
        <div class="library-card-footer">
          <span>⏱️ ${item.time}</span>
          <span class="library-card-link">
            Leer guía
            <svg fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </span>
        </div>
      </a>
    `).join("");
  }

  // Event Listeners
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      currentLibraryQuery = e.target.value;
      renderLibrary();
    });
  }

  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      currentLibraryCategory = btn.getAttribute("data-category") || "all";
      renderLibrary();
    });
  });

  renderLibrary();
}
