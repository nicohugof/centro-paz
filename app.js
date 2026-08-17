/**
 * Centro Paz (CPAZ) — Motor de Interacción y Alta Conversión de Pacientes
 * Diseñado para maximizar la captación y resolver objeciones en tiempo real.
 */

const CPAZ_CONFIG = {
  whatsappNumber: "56965163893",
  therapistName: "Valentina Castro Núñez",
  centerName: "Centro Paz",
  standardFee: 45000, // Arancel estándar de referencia en CLP
};

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
    desc: "Selecciona quién recibirá el acompañamiento para orientar el enfoque terapéutico.",
    options: [
      { id: "adulto", icon: "👤", title: "Para mí (Adulto)", desc: "Acompañamiento individual, bienestar emocional y autoconocimiento." },
      { id: "hijo", icon: "🌱", title: "Para mi hijo/a o adolescente", desc: "Apoyo infanto-juvenil, neurodivergencias y etapa escolar." },
      { id: "familia", icon: "🏡", title: "Para la familia o pareja", desc: "Mejora de la dinámica vincular, comunicación y crianza." }
    ]
  },
  reason: {
    adulto: [
      { id: "ansiedad", icon: "🌊", title: "Ansiedad, estrés o sobrecarga", desc: "Manejo de angustia, crisis y equilibrio diario." },
      { id: "tea_tdah_adulto", icon: "🧠", title: "Neurodivergencia (TEA / TDAH)", desc: "Sospecha, diagnóstico tardío o acompañamiento." },
      { id: "trauma_duelo", icon: "🕯️", title: "Trauma, duelo o quiebres", desc: "Elaboración de pérdidas y experiencias difíciles." },
      { id: "crecimiento", icon: "✨", title: "Autoestima y desarrollo personal", desc: "Reconexión con tus metas y bienestar integral." }
    ],
    hijo: [
      { id: "tea_tdah_infantil", icon: "🧩", title: "Evaluación o apoyo TEA / TDAH", desc: "Estrategias de regulación, sensoriales y escolares." },
      { id: "emocional_infantil", icon: "🎨", title: "Manejo emocional o conductual", desc: "Frustración, miedos, cambios familiares o escolares." },
      { id: "adolescencia", icon: "🌿", title: "Etapa adolescente", desc: "Identidad, motivación, autoestima y relaciones sociales." },
      { id: "orientacion_padres", icon: "🤝", title: "Orientación a padres", desc: "Pautas de crianza respetuosa y contención." }
    ],
    familia: [
      { id: "comunicacion", icon: "💬", title: "Dificultades de comunicación", desc: "Conflictos recurrentes y distancia afectiva." },
      { id: "crianza_compartida", icon: "🧭", title: "Crianza y acuerdos", desc: "Alineación en la dinámica del hogar y límites sanos." },
      { id: "crisis_familiar", icon: "🛡️", title: "Crisis o transición familiar", desc: "Separaciones, mudanzas o duelos compartidos." }
    ]
  },
  modality: [
    { id: "online", icon: "💻", title: "Online (Videollamada)", desc: "Comodidad y flexibilidad desde cualquier lugar de Chile o el extranjero." },
    { id: "presencial", icon: "🛋️", title: "Presencial (Consulta)", desc: "Sesión en consulta clínica en un entorno de calma y confidencialidad." },
    { id: "indiferente", icon: "✨", title: "Cualquiera de las dos", desc: "Sujeto a disponibilidad y recomendación de la terapeuta." }
  ]
};

// Datos del Checklist / Screener
const checklistData = {
  adultos: [
    "Sientes que vives con una sobrecarga mental o cansancio que no se quita descansando.",
    "Sospechas que podrías tener TDAH o TEA (dificultad para concentrarte, hipersensibilidad o desregulación).",
    "Te cuesta poner límites sanos o tiendes a complacer a los demás a costa de tu bienestar.",
    "Experimentas angustia, ansiedad física (pecho apretado) o miedo constante al futuro.",
    "Has pasado por un duelo, quiebre o experiencia traumática que aún duele.",
    "Sientes que 'enmascaras' quién eres para encajar en el trabajo o la sociedad."
  ],
  padres: [
    "Tu hijo/a tiene episodios de frustración intensa o desbordes emocionales difíciles de calmar.",
    "El colegio sugiere una evaluación por sospecha de TEA, TDAH o dificultades de atención.",
    "Notas que le afectan mucho los ruidos fuertes, texturas o cambios imprevistos de rutina.",
    "Te sientes sobrepasada/o o con dudas constantes sobre cómo ejercer una crianza respetuosa.",
    "Tu hijo/a o adolescente se aísla, muestra baja autoestima o dificultades para hacer amigos.",
    "Deseas fortalecer el vínculo y la comunicación en el hogar sin gritos ni castigos."
  ]
};

let currentChecklistTab = "adultos";
let selectedSymptoms = new Set();

document.addEventListener("DOMContentLoaded", () => {
  initTriage();
  initFAQ();
  initWhatsAppLinks();
  initMobileNav();
  initCalculator();
  initChecklist();
});

/* ----------------------------------------------------
   ORIENTADOR DE CONSULTA / TRIAJE
---------------------------------------------------- */
function initTriage() {
  const step1Container = document.getElementById("step1-options");
  const step3Container = document.getElementById("step3-options");

  if (!step1Container) return;

  // Render Paso 1
  step1Container.innerHTML = triageData.who.options.map(opt => `
    <button type="button" class="option-btn" onclick="selectTriageWho('${opt.id}', '${opt.title}')">
      <span class="option-icon">${opt.icon}</span>
      <span class="option-title">${opt.title}</span>
      <span class="option-sub">${opt.desc}</span>
    </button>
  `).join("");

  // Render Paso 3
  step3Container.innerHTML = triageData.modality.map(opt => `
    <button type="button" class="option-btn" onclick="selectTriageModality('${opt.id}', '${opt.title}')">
      <span class="option-icon">${opt.icon}</span>
      <span class="option-title">${opt.title}</span>
      <span class="option-sub">${opt.desc}</span>
    </button>
  `).join("");
}

window.selectTriageWho = function(id, label) {
  triageState.forWhom = { id, label };
  updateOptionSelection("step1-options", id);

  const step2Container = document.getElementById("step2-options");
  const reasons = triageData.reason[id] || triageData.reason.adulto;

  step2Container.innerHTML = reasons.map(opt => `
    <button type="button" class="option-btn" onclick="selectTriageReason('${opt.id}', '${opt.title}')">
      <span class="option-icon">${opt.icon}</span>
      <span class="option-title">${opt.title}</span>
      <span class="option-sub">${opt.desc}</span>
    </button>
  `).join("");

  setTimeout(() => goToStep(2), 220);
};

window.selectTriageReason = function(id, label) {
  triageState.reason = { id, label };
  updateOptionSelection("step2-options", id);
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

window.setTimePreference = function(timeStr) {
  triageState.timePreference = timeStr;
  document.querySelectorAll(".time-btn").forEach(b => b.classList.remove("active"));
  const clickedBtn = event?.currentTarget;
  if (clickedBtn) clickedBtn.classList.add("active");
  buildTriageResult(); // Actualiza el mensaje final
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
  const buttons = container.querySelectorAll(".option-btn");
  buttons.forEach(btn => btn.classList.remove("selected"));
}

function buildTriageResult() {
  const whoLabel = triageState.forWhom?.label || "Atención general";
  const reasonLabel = triageState.reason?.label || "Bienestar emocional";
  const modLabel = triageState.modality?.label || "Por coordinar";
  const timePref = triageState.timePreference || "Horario flexible";

  let recommendedApproach = "Acompañamiento Psicológico Integral";
  if (triageState.forWhom?.id === "hijo") {
    recommendedApproach = "Terapia Infanto-Juvenil y Enfoque Neuroafirmativo";
  } else if (triageState.forWhom?.id === "familia") {
    recommendedApproach = "Terapia Familiar y Sistémica";
  } else if (triageState.reason?.id === "tea_tdah_adulto") {
    recommendedApproach = "Acompañamiento en Neurodivergencias Adultas";
  } else if (triageState.reason?.id === "trauma_duelo") {
    recommendedApproach = "Abordaje Integrativo del Trauma y Duelo";
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
          <p style="font-size:0.95rem; margin-top:4px;">Tu consulta será atendida directamente por <strong>${CPAZ_CONFIG.therapistName}</strong> en un espacio seguro, empático y libre de juicios.</p>
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
          <button type="button" class="tab-btn time-btn ${timePref === 'Mañana' ? 'active' : ''}" onclick="setTimePreference('Mañana')">🌅 Mañana (09:00 - 13:00)</button>
          <button type="button" class="tab-btn time-btn ${timePref === 'Tarde' ? 'active' : ''}" onclick="setTimePreference('Tarde')">🌇 Tarde (14:00 - 20:00)</button>
          <button type="button" class="tab-btn time-btn ${timePref === 'Sábado' ? 'active' : ''}" onclick="setTimePreference('Sábado')">🌿 Sábado</button>
        </div>
      </div>

      <div class="result-guarantee">
        🛡️ <strong>Boletas 100% Reembolsables:</strong> Emitimos boleta electrónica para reembolso en tu Isapre y Seguro Complementario de Salud.
      </div>
    `;
  }

  // Generar mensaje personalizado de WhatsApp
  const rawMessage = `Hola Centro Paz 🌿 Estuve revisando su sitio web y completé el orientador de consulta.\n\n` +
    `• Paciente: ${whoLabel}\n` +
    `• Motivo: ${reasonLabel}\n` +
    `• Modalidad preferida: ${modLabel}\n` +
    `• Preferencia de horario: ${timePref}\n\n` +
    `Me gustaría coordinar mi primera sesión con Valentina. ¿Qué opciones de fecha tienen disponibles? Muchas gracias.`;

  const encodedMessage = encodeURIComponent(rawMessage);
  const whatsappUrl = `https://wa.me/${CPAZ_CONFIG.whatsappNumber}?text=${encodedMessage}`;

  const ctaBtn = document.getElementById("triage-whatsapp-btn");
  if (ctaBtn) {
    ctaBtn.href = whatsappUrl;
    ctaBtn.target = "_blank";
  }
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
  const waMessage = `Hola Centro Paz 🌿 Estuve usando el simulador de reembolsos de su web. Tengo Isapre ${isapreText}${hasInsurance ? ' + Seguro Complementario' : ''} y quisiera consultar por aranceles y disponibilidad para agendar mi primera sesión.`;

  if (calcWaBtn) {
    calcWaBtn.href = `https://wa.me/${CPAZ_CONFIG.whatsappNumber}?text=${encodeURIComponent(waMessage)}`;
  }
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
        ${selectedSymptoms.has(idx) ? '✓' : ''}
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
    const tabLabel = currentChecklistTab === "adultos" ? "Bienestar de Adultos" : "Apoyo Infanto-Juvenil y Crianza";
    const rawWa = `Hola Valentina 🌿 Estuve revisando el checklist de ${tabLabel} en la web de Centro Paz y me identifiqué con ${count} de los puntos descritos. Me gustaría consultar por una primera sesión para trabajar en esto.`;

    feedbackEl.innerHTML = `
      <div>
        <strong style="color:var(--burdeo-dark);">Te identificas con ${count} punto${count > 1 ? 's' : ''}:</strong>
        <p style="font-size:0.9rem; margin:2px 0 0; color:var(--gris);">No tienes que procesar todo esto en soledad. Podemos acompañarte a encontrar calma y estrategias.</p>
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
  genericLinks.forEach(link => {
    const action = link.getAttribute("data-wa-action");
    let msg = "Hola Centro Paz, me gustaría solicitar información para agendar una primera sesión psicológica.";

    if (action === "adultos") {
      msg = "Hola Centro Paz 🌿 Quisiera consultar por atención psicológica para adultos y disponibilidad de horas con Valentina.";
    } else if (action === "neurodivergencia") {
      msg = "Hola Centro Paz 🧠 Quisiera consultar por atención especializada en Neurodivergencias (TEA / TDAH) y disponibilidad.";
    } else if (action === "infantil") {
      msg = "Hola Centro Paz 🌱 Busco apoyo psicológico infanto-juvenil para mi hijo/a. ¿Cómo es el proceso de ingreso?";
    } else if (action === "familia") {
      msg = "Hola Centro Paz 🏡 Me gustaría consultar por terapia familiar o de vínculo.";
    } else if (action === "lead-magnet") {
      msg = "Hola Centro Paz ✨ Me gustaría solicitar la Guía Gratuita de Regulación Emocional y Sensorial para familias y adultos.";
    }

    link.href = `https://wa.me/${CPAZ_CONFIG.whatsappNumber}?text=${encodeURIComponent(msg)}`;
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
      const isVisible = navLinks.style.display === "flex";
      navLinks.style.display = isVisible ? "none" : "flex";
      if (!isVisible) {
        navLinks.style.flexDirection = "column";
        navLinks.style.position = "absolute";
        navLinks.style.top = "100%";
        navLinks.style.left = "0";
        navLinks.style.right = "0";
        navLinks.style.background = "var(--crema)";
        navLinks.style.padding = "20px";
        navLinks.style.borderBottom = "1px solid var(--borde-suave)";
        navLinks.style.boxShadow = "var(--shadow-md)";
      }
    });

    navLinks.querySelectorAll("a").forEach(a => {
      a.addEventListener("click", () => {
        if (window.innerWidth <= 768) {
          navLinks.style.display = "none";
        }
      });
    });
  }
}
