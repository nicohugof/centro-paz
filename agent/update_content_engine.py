#!/usr/bin/env python3
"""
Actualiza agent/content_engine.py para contener los 28 tópicos clínicos completos,
las 4 semanas de calendario y la matriz omnicanal para n8n y redes sociales.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET_FILE = ROOT / "agent" / "content_engine.py"

CONTENT = '''"""
Motor de Contenidos Clínicos y Copywriting de Alta Conversión para Centro Paz (CPAZ).
Diseñado para alimentar publicaciones de redes sociales, anuncios y guiones de Reels/TikTok
con derivación directa a WhatsApp (+56 9 6516 3893) y atención en Ñuñoa / Online.
"""
from __future__ import annotations

from typing import List, Dict, Any

BRAND = {
    "name": "Centro Paz",
    "therapist": "Valentina Castro Núñez",
    "title": "Psicóloga Clínica",
    "registration": "Superintendencia de Salud de Chile (SIS)",
    "approach": "Humanista, Integrativo y Neuroafirmativo",
    "phone": "+56965163893",
    "phone_display": "+56 9 6516 3893",
    "email": "contacto.centropaz@gmail.com",
    "instagram": "@centropaz.cl",
    "tiktok": "@centropaz.cl",
    "facebook": "https://www.facebook.com/profile.php?id=61593207820690",
    "web": "https://www.centropaz.cl",
    "wa_link": "https://wa.me/56965163893",
    "isapres": "Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres, Nueva Masvida y Seguros Complementarios",
    "session_price": "$45.000 CLP (Boleta 100% reembolsable)",
    "location": "Ñuñoa (Santiago Oriente) y Online para todo Chile",
}

HASHTAGS_BASE = [
    "#CentroPaz", "#PsicologiaChile", "#PsicologaClinica", "#SaludMentalChile",
    "#TerapiaOnlineChile", "#ReembolsoIsapre", "#ValentinaCastroPsicologa", "#PsicologiaSantiago", "#PsicologiaÑuñoa"
]

TOPICS: Dict[str, Dict[str, Any]] = {
    "tdah_adultos": {
        "id": 1,
        "kicker": "Neurodivergencias en Adultos",
        "title": "¿Y si ese cansancio crónico no es flojera, sino TDAH tardío?",
        "hook": "¿Siempre te dijeron que eras 'demasiado disperso' o que no te esforzabas lo suficiente?",
        "points": [
            "Procrastinación paralizante ante tareas que parecen simples para otros.",
            "Agotamiento crónico por 'masking' (forzarte a encajar y compensar el doble).",
            "Sensibilidad aguda al rechazo o miedo constante a equivocarte.",
            "Hipersensibilidad sensorial (ruidos, luces, sobreestimulación)."
        ],
        "category": "Neurodivergencias",
        "caption": """¿Te pasa que quieres empezar mil cosas y sientes una pared invisible que te frena? 🧠✨

Muchas personas adultas descubren su neurodivergencia (TDAH o TEA) después de los 25 o 30 años, tras décadas de sentirse "diferentes" o sobrecargadas sin entender por qué.

En Centro Paz no buscamos encajarte en moldes ni juzgarte: trabajamos desde un enfoque neuroafirmativo para ayudarte a comprender tu funcionamiento singular y construir estrategias reales para tu vida cotidiana y laboral.

📍 Sesiones online (todo Chile) y presenciales en Ñuñoa (Santiago).
💳 Boletas 100% reembolsables en Isapres y Seguros Complementarios.

👉 ¿Te gustaría agendar una primera sesión? Escríbenos directo por WhatsApp al +56 9 6516 3893 o ingresa a www.centropaz.cl""",
        "hashtags": HASHTAGS_BASE + ["#TDAHAdultos", "#TDAHChile", "#NeurodivergenciaChile", "#AutismoAdultos", "#TEAChile"]
    },
    "reembolso_isapre": {
        "id": 2,
        "kicker": "Claridad y Cobertura",
        "title": "Cómo reembolsar tus sesiones de psicología en 3 pasos",
        "hook": "¿Sabías que tu Isapre o Seguro puede cubrir entre el 50% y el 80% de tu terapia?",
        "points": [
            "1. Asistes a tu sesión online o presencial con Valentina.",
            "2. Al terminar recibes tu boleta electrónica de honorarios profesionales.",
            "3. La subes a la app de tu Isapre y recibes el depósito directo en tu cuenta bancaria."
        ],
        "category": "Reembolsos",
        "caption": """Cuidar tu salud mental no tiene por qué ser una carga económica abrumadora 🌿💳

En Centro Paz emitimos boletas electrónicas de honorarios profesionales con código de psicología clínica válidas para:
✨ Todas las Isapres (Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres, Nueva Masvida).
✨ Seguros Complementarios de Salud (MetLife, Bice, Bci, etc.).

El copago real puede quedar tan bajo como $12.000 a $18.000 por sesión según tu plan.

👉 Usa el simulador de reembolsos en www.centropaz.cl o escríbenos por WhatsApp al +56 9 6516 3893 para orientarte con tu cobertura.""",
        "hashtags": HASHTAGS_BASE + ["#ReembolsoPsicologia", "#IsapreColmena", "#IsapreBanmedica", "#IsapreCruzBlanca", "#CopagoPsicologia"]
    },
    "crianza_regulacion": {
        "id": 3,
        "kicker": "Infancia & Crianza",
        "title": "Una rabieta intensa no es manipulación: es sobrecarga sensorial",
        "hook": "Cuando un niño/a se desborda, no busca molestarte: su sistema nervioso colapsó.",
        "points": [
            "Evita el 'cálmate ya': durante el desborde la corteza lógica está apagada.",
            "Baja luces y ruidos ambientales para descomprimir la sobrecarga sensorial.",
            "Valida con calma: 'Veo que esto te sobrepasó, estoy aquí contigo'."
        ],
        "category": "Crianza Respetuosa",
        "caption": """Criar a un hijo/a con desafíos de regulación emocional o características neurodivergentes puede ser agotador cuando no se tienen las herramientas adecuadas 🌱🤍

El castigo o el aislamiento en momentos de desborde aumentan la angustia. Lo que ayuda es la corregulación: prestarle tu calma hasta que su sistema nervioso vuelva al equilibrio.

En Centro Paz acompañamos a niños, niñas y adolescentes, y brindamos orientación continua a padres para construir un hogar en calma y sin gritos.

👉 Para coordinar una primera sesión de orientación infanto-juvenil, escríbenos a WhatsApp al +56 9 6516 3893 o en www.centropaz.cl""",
        "hashtags": HASHTAGS_BASE + ["#CrianzaRespetuosa", "#PsicologiaInfantil", "#TEAInfantil", "#TDAHInfantil", "#OrientacionAPadres"]
    },
    "masking": {
        "id": 4,
        "kicker": "Agotamiento Invisible",
        "title": "El costo invisible del masking: llegar a casa sin energía ni para hablar",
        "hook": "¿Llegas a casa después del trabajo sintiendo que tu batería social está en -100%?",
        "points": [
            "Forzar contacto visual, modular gestos y reprimir incomodidades sensoriales todo el día.",
            "El sobreesfuerzo de parecer 'funcional' ante jefes, compañeros o familia.",
            "Aprender a desenmascarar en un espacio terapéutico seguro y sin exigencias."
        ],
        "category": "Neurodivergencias",
        "caption": """¿Llegas a casa sintiendo que no puedes ni pronunciar una palabra? 🧠

El 'masking' es el esfuerzo consciente o inconsciente de forzar gestos y reprimir tu forma natural de procesar el mundo para encajar. Tu cuerpo gastó el doble de energía que los demás.

En Centro Paz te acompañamos a construir un espacio seguro donde puedas soltar las máscaras y cuidar tu bienestar emocional.

📍 Sesiones online (todo Chile) y presenciales en Ñuñoa.
💳 Boletas reembolsables en todas las Isapres.

👉 Agenda en www.centropaz.cl o al WhatsApp +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#Masking", "#AutismoAdultos", "#TEAChile", "#TDAHAdultos", "#BurnoutAutista"]
    },
    "terapia_online": {
        "id": 5,
        "kicker": "Atención Flexible",
        "title": "Terapia online con la misma rigurosidad clínica, desde tu espacio de calma",
        "hook": "¿El tráfico de Santiago o vivir en regiones te frena de empezar terapia?",
        "points": [
            "Atiéndete desde tu habitación, sin traslados ni salas de espera.",
            "Misma eficacia clínica y boleta electrónica para reembolso en Isapres.",
            "Plataforma segura y confidencial con Valentina Castro Núñez."
        ],
        "category": "Modalidad",
        "caption": """Atenderte desde tu habitación o espacio de calma reduce la ansiedad y elimina los tiempos de traslado 💻🌿

La terapia online cuenta con la misma rigurosidad y calidez clínica. Recibes tu boleta electrónica para reembolsar en tu Isapre o Seguro.

👉 Encuentra tu horario disponible en www.centropaz.cl o escríbenos a WhatsApp al +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#TerapiaOnline", "#PsicologiaOnlineChile", "#SaludMentalChile"]
    },
    "evaluacion_infantil": {
        "id": 6,
        "kicker": "Desarrollo & Colegio",
        "title": "¿Cuándo consultar con una psicóloga infantil?",
        "hook": "¿El colegio sugiere evaluación o notas desbordes intensos difíciles de calmar?",
        "points": [
            "Señales de alerta: cambios bruscos de conducta, irritabilidad o aislamiento.",
            "Dificultades de adaptación escolar o hipersensibilidad sensorial.",
            "Acompañamiento clínico cálido + orientación continua a padres."
        ],
        "category": "Infancia",
        "caption": """¿Cuándo es momento de consultar con una psicóloga infantil? 🌱

Desbordes intensos frecuentes, hipersensibilidad a ruidos o texturas y dificultades de adaptación escolar son señales de que tu hijo/a necesita apoyo y tú como papá o mamá requieres pautas claras.

En Centro Paz acompañamos a niños y adolescentes desde un enfoque lúdico y cálido, con orientación continua a la familia.

👉 Contáctanos por WhatsApp al +56 9 6516 3893 o en www.centropaz.cl""",
        "hashtags": HASHTAGS_BASE + ["#PsicologiaInfantil", "#OrientacionAPadres", "#TDAHInfantil", "#TEAInfantil"]
    },
    "autocuidado_adultos": {
        "id": 7,
        "kicker": "Salud Mental",
        "title": "Pedir ayuda no es debilidad: es cuidar tu sistema nervioso",
        "hook": "¿Cuánto tiempo llevas posponiendo tu bienestar emocional por atender a los demás?",
        "points": [
            "50 minutos a la semana dedicados 100% a ti, sin juicios.",
            "Herramientas concretas para regular la ansiedad y poner límites.",
            "Boletas 100% reembolsables en todas las Isapres y Seguros."
        ],
        "category": "Adultos",
        "caption": """Pedir ayuda profesional no es debilidad: es reconocer que tu bienestar importa ✨

50 minutos a la semana dedicados 100% a ti, con la psicóloga clínica Valentina Castro Núñez.

🌿 Espacio sin juicios ni imposiciones.
🌿 Enfoque humanista, integrativo y neuroafirmativo.
💳 Boletas 100% reembolsables en todas las Isapres.

👉 Da el primer paso hoy. Agenda en www.centropaz.cl o al WhatsApp +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#Autocuidado", "#PedirAyuda", "#TerapiaAdultosChile", "#PsicologiaSantiago"]
    },
    "burnout_autista": {
        "id": 8,
        "kicker": "Agotamiento Profundo",
        "title": "¿Qué es el Burnout Autista y por qué no se quita descansando?",
        "hook": "¿Sientes que dormir un fin de semana entero ya no te devuelve la energía?",
        "points": [
            "Pérdida temporal de habilidades y funciones ejecutivas.",
            "Hipersensibilidad sensorial al límite: ruidos o luces provocan dolor.",
            "Necesidad urgente de aislamiento tras meses de sobreexigencia social.",
            "Acompañamiento neuroafirmativo para rediseñar tus demandas sensoriales."
        ],
        "category": "Neurodivergencias",
        "caption": """El Burnout Autista no es simplemente estrés laboral: es un colapso del sistema nervioso tras meses o años de forzarte a encajar 🧠✨

Requiere reestructurar demandas sensoriales, validar límites y recibir acompañamiento neuroafirmativo.

👉 Escríbenos por WhatsApp al +56 9 6516 3893 o visita www.centropaz.cl""",
        "hashtags": HASHTAGS_BASE + ["#BurnoutAutista", "#TEAAdultos", "#AutismoChile", "#Neurodivergencia"]
    },
    "paralisis_ejecutiva": {
        "id": 9,
        "kicker": "TDAH en Adultos",
        "title": "¿Por qué postergas lo importante aunque tengas ganas de hacerlo?",
        "hook": "¿Te quedas horas frente a la pantalla sabiendo qué hacer pero sin poder 'arrancar'?",
        "points": [
            "No es flojera: es un bloqueo en la función ejecutiva de la corteza prefrontal.",
            "Déficit en la regulación de dopamina para iniciar tareas de baja estimulación.",
            "La culpa empeora el bloqueo: la solución clínica es la micro-fricción cero."
        ],
        "category": "TDAH Adultos",
        "caption": """La parálisis ejecutiva en personas con TDAH no es falta de voluntad: es una barrera neurobiológica de inicio 🧠

Obligarte con culpa aumenta la respuesta de amenaza y empeora el bloqueo. En terapia desarrollamos estrategias de micro-fricción y adaptación ambiental.

👉 Agenda en www.centropaz.cl o al WhatsApp +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#ParalisisEjecutiva", "#TDAHAdultos", "#TDAHChile", "#FuncionesEjecutivas"]
    },
    "regulacion_ansiedad": {
        "id": 10,
        "kicker": "Herramientas Somáticas",
        "title": "3 Anclas para regular la ansiedad cuando tu mente sobrepiensa",
        "hook": "Si tu mente no para de proyectar escenarios y angustia, haz este ejercicio somático.",
        "points": [
            "1. Suspiro fisiológico: 2 inhalaciones nasales y 1 exhalación lenta por la boca.",
            "2. Presión propioceptiva: apoya los pies firmes y presiona las palmas.",
            "3. Orientación visual: busca 3 objetos de color verde a tu alrededor."
        ],
        "category": "Ansiedad",
        "caption": """Si tu mente no para de sobrepensar, habla con tu cuerpo antes de intentar razonar 🌊🌿

El nervio vago responde a señales fisiológicas directas como la respiración prolongada y el enraizamiento.

👉 Aprende herramientas de regulación integrativa en Centro Paz. WhatsApp: +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#AnsiedadChile", "#Sobrepensar", "#RegulacionEmocional", "#SistemaNervioso"]
    },
    "apoyo_neurodivergente_hijos": {
        "id": 11,
        "kicker": "Crianza Neuroafirmativa",
        "title": "Cómo apoyar a un hijo/a con sospecha de TEA o TDAH",
        "hook": "¿Sientes que los métodos tradicionales de crianza y premios/castigos no funcionan?",
        "points": [
            "Comprender su perfil sensorial: anticipar sobrecargas por ropa, ruidos o texturas.",
            "Eliminar el castigo: los desbordes son desregulaciones, no desobediencia.",
            "Estructurar el entorno con apoyos visuales y rutinas predecibles.",
            "Orientación continua a padres para cuidar el clima familiar."
        ],
        "category": "Crianza",
        "caption": """Los niños neurodivergentes no necesitan mano dura: necesitan adultos que comprendan su sistema nervioso 🌱

En Centro Paz trabajamos en conjunto con los padres para entregarles herramientas prácticas y respetuosas.

👉 Escríbenos a WhatsApp al +56 9 6516 3893 o ingresa a www.centropaz.cl""",
        "hashtags": HASHTAGS_BASE + ["#CrianzaNeuroafirmativa", "#TEAInfantil", "#TDAHInfantil", "#OrientacionParental"]
    },
    "primera_sesion": {
        "id": 12,
        "kicker": "Educación Clínica",
        "title": "¿Qué pasa realmente en una primera sesión de terapia psicológica?",
        "hook": "¿Te da nervios dar el primer paso porque no sabes con qué te vas a encontrar?",
        "points": [
            "No tienes que llegar con todo claro ni saber exactamente qué decir.",
            "Es una conversación cálida de 50 minutos para conocerte y entender qué necesitas.",
            "Trazamos juntos los objetivos del proceso a tu propio ritmo.",
            "Entrega inmediata de boleta electrónica para reembolso en tu Isapre."
        ],
        "category": "Proceso Terapéutico",
        "caption": """¿Te da nervios agendar tu primera sesión? 🌿✨

La primera sesión es un encuentro protegido y sin juicios para escucharte y acordar juntos el camino terapéutico.

📍 Modalidad Online (todo Chile) y Presencial en Ñuñoa.
💳 Boletas reembolsables en Isapres y Seguros.

👉 Agenda en www.centropaz.cl o al WhatsApp +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#PrimeraSesion", "#TerapiaChile", "#PsicologiaSantiago", "#PsicologaValentinaCastro"]
    },
    "culpa_parental": {
        "id": 13,
        "kicker": "Crianza Consciente",
        "title": "Soltar la culpa en la crianza: padres regulados vs. padres perfectos",
        "hook": "¿Terminas el día sintiendo que perdiste la paciencia y te invade la culpa?",
        "points": [
            "Tus hijos no necesitan padres perfectos: necesitan adultos que sepan reparar la conexión.",
            "Pedir perdón a un hijo/a le enseña que equivocarse es parte de ser humano.",
            "Aprender a regularte tú es el mayor regalo emocional que puedes brindarles."
        ],
        "category": "Crianza",
        "caption": """Para los papás y mamás que terminan el día sintiendo que hoy fallaron 🌱

La capacidad de reparar la conexión emocional después de un mal momento es más valiosa que la exigencia de no equivocarse jamás.

👉 Agenda tu sesión de orientación parental en www.centropaz.cl o al WhatsApp +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#CulpaParental", "#CrianzaRespetuosa", "#MaternidadReal", "#PaternidadConsciente"]
    },
    "reembolso_matematica": {
        "id": 14,
        "kicker": "Transparencia Financiera",
        "title": "La matemática real del reembolso: ¿Cuánto pagas y cuánto te devuelven?",
        "hook": "¿Crees que la atención psicológica particular es inaccesible con Isapre?",
        "points": [
            "Arancel sesión particular oficial: $45.000 CLP.",
            "Reembolso Isapre habitual (50% a 70%): $22.500 a $31.500 CLP devueltos.",
            "Seguro Complementario adicional: cubre hasta el 50%-80% del saldo restante.",
            "Copago final real estimado: entre $10.000 y $18.000 CLP por sesión."
        ],
        "category": "Reembolso Isapres",
        "caption": """¿Sabías que con tu plan de Isapre y seguro complementario tu sesión de psicología clínica puede tener un copago similar o menor que Fonasa? 💳🌿

En Centro Paz emitimos boleta electrónica oficial con código SIS para que reembolses en minutos desde el celular.

👉 Usa nuestro simulador en www.centropaz.cl o escríbenos a WhatsApp al +56 9 6516 3893 para guiarte en tu reembolso.""",
        "hashtags": HASHTAGS_BASE + ["#IsapreChile", "#ReembolsoIsapre", "#Banmedica", "#Colmena", "#CruzBlanca", "#Consalud"]
    },
    "tdah_mujeres": {
        "id": 15,
        "kicker": "Diagnóstico Tardío",
        "title": "¿Por qué el TDAH en mujeres se descubre 10 años más tarde?",
        "hook": "¿Siempre fuiste catalogada como 'demasiado autoexigente' o 'emocional'?",
        "points": [
            "Manifestación internalizada: desorganización y ansiedad silenciosa en vez de hiperactividad motora.",
            "Hiper-compensación (Masking): perfeccionismo extremo para no fallar a costa de un colapso privado.",
            "Diagnósticos previos erróneos de depresión o ansiedad sin tratar la base neurobiológica.",
            "Acompañamiento neuroafirmativo respetuoso con tu energía."
        ],
        "category": "Neurodivergencias",
        "caption": """¿Por qué tantas mujeres adultas descubren su TDAH recién a los 30 o 35 años? 🧠✨

A diferencia del estereotipo clásico, en mujeres el TDAH suele manifestarse de forma internalizada: sobrepensamiento incesante, fatiga crónica, perfeccionismo paralizante y una lucha invisible por mantener el orden.

En Centro Paz brindamos un espacio clínico libre de juicios para comprender tu funcionamiento y diseñar estrategias que respeten tu ritmo.

📍 Atención Online para todo Chile y Presencial en Ñuñoa (Santiago).
💳 Boletas 100% reembolsables en todas las Isapres y Seguros de Salud.

👉 Escríbenos directo por WhatsApp al +56 9 6516 3893 o agenda en www.centropaz.cl""",
        "hashtags": HASHTAGS_BASE + ["#TDAHMujeres", "#TDAHAdultas", "#NeurodivergenciaChile", "#SaludMentalMujeres"]
    },
    "sobrecarga_sensorial_ruido": {
        "id": 16,
        "kicker": "Sistema Nervioso",
        "title": "Hipersensibilidad al ruido: no es mal genio, es tu sistema nervioso",
        "hook": "¿El ruido del teclado, la masticación o un centro comercial te provocan irritabilidad súbita?",
        "points": [
            "Sobrecarga auditiva: el cerebro no filtra los estímulos ambientales irrelevantes.",
            "La amígdala reacciona como si existiera un peligro físico inminente.",
            "Forzarte a 'tolerarlo' genera agotamiento extremo y pérdida de energía.",
            "Acomodaciones sensoriales válidas y desculpabilizadas en tu día a día."
        ],
        "category": "Regulación Sensorial",
        "caption": """La hipersensibilidad al ruido no es 'falta de paciencia': es una respuesta física de tu sistema nervioso 🎧🌿

En personas neurodivergentes o altamente sensibles, los estímulos auditivos continuos saturan el procesamiento sensorial y activan la respuesta de alerta.

En sesión trabajamos en la identificación de tus desencadenantes y en pautas de regulación sensorial para el trabajo y el hogar.

👉 Contáctanos por WhatsApp (+56 9 6516 3893) para agendar tu primera sesión con Valentina Castro Núñez.""",
        "hashtags": HASHTAGS_BASE + ["#Hipersensibilidad", "#Sensorial", "#MisofoniaChile", "#TEAChile", "#TDAHChile"]
    },
    "reembolso_seguros_cobertura": {
        "id": 17,
        "kicker": "Finanzas & Salud",
        "title": "Cómo combinar Isapre + Seguro para pagar el mínimo en terapia",
        "hook": "¿Sabías que puedes recuperar casi la totalidad del arancel combinando ambos beneficios?",
        "points": [
            "Paso 1: Asistes a tu sesión en Centro Paz y recibes tu boleta electrónica oficial.",
            "Paso 2: Subes la boleta a tu Isapre ➡️ Te reembolsan entre 50% y 70%.",
            "Paso 3: Subes el comprobante a tu Seguro Complementario ➡️ Cubren el saldo.",
            "Copago final real estimado: entre $8.000 y $12.000 CLP por sesión."
        ],
        "category": "Cobertura & Isapres",
        "caption": """¿Sabías cómo funciona la doble cobertura de Isapre y Seguro Complementario? 💳✨

Al emitirte una boleta electrónica oficial con código SIS, puedes presentarla primero en tu Isapre y luego el saldo remanente en tu seguro laboral o personal.

👉 Simula tu cobertura en www.centropaz.cl o escríbenos a WhatsApp (+56 9 6516 3893).""",
        "hashtags": HASHTAGS_BASE + ["#SeguroComplementario", "#ReembolsoIsapre", "#CopagoMinimo", "#PsicologiaSantiago"]
    },
    "hiperfoco_burnout": {
        "id": 18,
        "kicker": "Gestión de Energía",
        "title": "El ciclo del Hiperfoco: De la genialidad al colapso en 48 hrs",
        "hook": "¿Pasas de trabajar 10 horas seguidas sin parar a no poder levantarte de la cama al día siguiente?",
        "points": [
            "Fase 1 (Obsesión productiva): 10 horas trabajando sin comer ni descansar.",
            "Fase 2 (Caída de dopamina): la novedad se apaga y la tarea se vuelve tediosa.",
            "Fase 3 (Culpa y colapso): cansancio extremo y sensación de no ser constante.",
            "Estrategia clínica: pausas fisiológicas antes de agotar la reserva neurobiológica."
        ],
        "category": "TDAH en Adultos",
        "caption": """El hiperfoco es el superpoder y a la vez la trampa del TDAH en adultos 🧠⚡

Aprender a poner frenos antes de que la dopamina se agote por completo es fundamental para evitar el ciclo de burnout recurrente.

👉 Acompañamiento clínico en Centro Paz. WhatsApp: +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#Hiperfoco", "#TDAHAdultos", "#BurnoutTDAH", "#ProductividadNeurodivergente"]
    },
    "crianza_rutinas_flexibles": {
        "id": 19,
        "kicker": "Hogar en Calma",
        "title": "Rutinas visuales para niños sin batallas diarias ni gritos",
        "hook": "¿Cada mañana o noche es una discusión interminable para vestirse o lavarse los dientes?",
        "points": [
            "Anticipación gráfica: los cerebros infantiles procesan imágenes 10x más rápido que órdenes verbales.",
            "Transiciones respetuosas con avisos a los 10 y 5 minutos.",
            "Opciones limitadas para devolverles el sentido de control y autonomía.",
            "Orientación a padres para diseñar rutinas adaptadas a su hogar."
        ],
        "category": "Crianza Respetuosa",
        "caption": """Las órdenes verbales repetidas agotan a los padres y saturan a los niños 🌱

Implementar apoyos visuales y previsibilidad reduce la fricción diaria en más del 70%.

👉 Agenda tu consulta de orientación a padres por WhatsApp (+56 9 6516 3893) o en www.centropaz.cl.""",
        "hashtags": HASHTAGS_BASE + ["#RutinasVisuales", "#CrianzaRespetuosa", "#PsicologiaInfantil", "#TEAInfantil"]
    },
    "comunicacion_asertiva_limites": {
        "id": 20,
        "kicker": "Salud Emocional",
        "title": "Aprender a decir 'No tengo la energía' sin pedir perdón",
        "hook": "¿Aceptas favores o reuniones por compromiso y luego te arrepientes?",
        "points": [
            "El 'Sí' complaciente agota profundamente tu batería emocional.",
            "Un límite sano no es un ataque hacia el otro, es una protección hacia ti.",
            "Aprende a comunicarte con asertividad y calma en sesión.",
            "Desactiva la culpa asociada a priorizar tu descanso."
        ],
        "category": "Bienestar Adultos",
        "caption": """Decir que 'no' a una demanda externa es decirte que 'sí' a tu propia salud mental 🌿

En terapia trabajamos el origen de la necesidad de complacer y desarrollamos límites claros y tranquilos.

👉 Inicia tu proceso con Valentina Castro en www.centropaz.cl o al WhatsApp +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#LimitesSanos", "#Asertividad", "#AutocuidadoAdultos", "#SaludEmocional"]
    },
    "tdah_rechazo_rsd": {
        "id": 21,
        "kicker": "Sensibilidad Emocional",
        "title": "Sensibilidad al Rechazo (RSD): Por qué una crítica duele tanto",
        "hook": "¿Una pequeña observación en el trabajo te arruina el día entero y te hace dudar de tu valor?",
        "points": [
            "Dolor físico real: la percepción de rechazo activa centros somáticos en el cerebro TDAH.",
            "Reacción de catástrofe y necesidad compulsiva de disculparse.",
            "Parálisis social: evitar postular a nuevos proyectos por temor al juicio.",
            "Regulación clínica: herramientas para desescalar la alarma interna."
        ],
        "category": "TDAH & Emociones",
        "caption": """La Disforia Sensible al Rechazo (RSD) es uno de los aspectos más dolorosos y menos hablados del TDAH 🧠💔

No eres 'débil' ni 'exagerado/a': tu cerebro reacciona con una intensidad neuroquímica real ante la crítica.

👉 Acompañamiento neuroafirmativo en Centro Paz. WhatsApp: +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#RSDChile", "#SensibilidadAlRechazo", "#TDAHEmocional", "#TDAHAdultos"]
    },
    "primera_consulta_nunoa": {
        "id": 22,
        "kicker": "Atención Presencial",
        "title": "¿Cómo es una sesión presencial en Ñuñoa en Centro Paz?",
        "hook": "¿Prefieres el contacto humano cara a cara en un ambiente cuidado y tranquilo?",
        "points": [
            "Ubicación céntrica y conectada: Sector Plaza Ñuñoa / Metro Chile España.",
            "Espacio de calma sensorial: iluminación suave, bajo ruido y total confidencialidad.",
            "Enfoque humanista: una conversación humana de 50 minutos centrada en tu bienestar.",
            "Boleta electrónica reembolsable entregada al finalizar la sesión."
        ],
        "category": "Consulta Ñuñoa",
        "caption": """Te abrimos las puertas de nuestra consulta presencial en Ñuñoa 🛋️🌿

Un espacio cálido y respetuoso diseñado para desconectar del ruido de la ciudad y trabajar en tu salud mental.

📍 Presencial en Ñuñoa y Online para todo Chile.
💳 Boletas 100% reembolsables en Isapres y Seguros.

👉 Agenda tu hora con Valentina Castro al WhatsApp +56 9 6516 3893 o en www.centropaz.cl.""",
        "hashtags": HASHTAGS_BASE + ["#PsicologiaÑuñoa", "#ConsultaPresencialSantiago", "#PlazaÑuñoa", "#MetroChileEspaña"]
    },
    "terapia_infantil_juego": {
        "id": 23,
        "kicker": "Psicología Infantil",
        "title": "En terapia infantil el juego es la herramienta más rigurosa",
        "hook": "¿Sabías que los niños procesan sus emociones jugando y no conversando como adultos?",
        "points": [
            "El juego es el lenguaje natural del niño para expresar miedos y angustias.",
            "Permite elaborar dinámicas escolares y familiares sin presión.",
            "Alianza con la familia: sesiones de orientación para los padres.",
            "Enfoque neuroafirmativo y respetuoso con la singularidad de cada niño/a."
        ],
        "category": "Infanto-Juvenil",
        "caption": """En la terapia infanto-juvenil, jugar no es pasar el tiempo: es la forma más rigurosa de evaluar y sanar 🌱🎨

Acompañamos a tu hijo/a a comprender sus emociones y te entregamos pautas claras para el hogar.

👉 Coordina una sesión de ingreso en www.centropaz.cl o al WhatsApp +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#TerapiaDeJuego", "#PsicologiaInfantilChile", "#CrianzaRespetuosa", "#InfanciaFeliz"]
    },
    "ansiedad_somatica_cuerpo": {
        "id": 24,
        "kicker": "Cuerpo & Mente",
        "title": "Cuando la ansiedad se siente en el cuerpo: Terapia integrativa",
        "hook": "¿Bruxismo, nudo en la garganta, pecho apretado o molestias estomacales continuas?",
        "points": [
            "El cuerpo retiene la tensión antes de que la mente consciente pueda procesarla.",
            "Más allá de 'pensar positivo': estimulación del nervio vago y grounding.",
            "Aprende a escuchar las señales fisiológicas antes de llegar a la crisis.",
            "Recupera la sensación de seguridad y calma en tu sistema nervioso."
        ],
        "category": "Ansiedad Adultos",
        "caption": """La ansiedad no está solo en tus pensamientos: está grabada en tu respuesta física 🌊🌿

En sesión trabajamos con herramientas integrativas para bajar el estado de alarma de tu sistema nervioso.

👉 Agenda en www.centropaz.cl o al WhatsApp +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#TerapiaSomatica", "#AnsiedadFisica", "#BruxismoEmocional", "#SaludMentalSantiago"]
    },
    "isapre_licencia_boletas": {
        "id": 25,
        "kicker": "Guía Práctica",
        "title": "Boletas de Psicología: Todo lo que debes saber para tu Isapre",
        "hook": "¿Tienes dudas sobre cómo emitir y solicitar el reembolso de tu atención?",
        "points": [
            "Boleta electrónica oficial con RUT profesional inscrito en la SIS.",
            "Código de prestación clínica reconocido por Colmena, Banmédica, CruzBlanca y Consalud.",
            "Depósito directo en tu cuenta bancaria en 3 a 5 días hábiles.",
            "Te enviamos el PDF listo al terminar cada sesión."
        ],
        "category": "Educación Financiera",
        "caption": """Hacemos que el reembolso de tu sesión sea rápido y sin fricciones 💳🌿

Al finalizar cada consulta recibes tu boleta oficial lista para subir a la app de tu Isapre o seguro.

👉 Conoce más en www.centropaz.cl o consúltanos por WhatsApp al +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#IsapreChile", "#ReembolsoFacil", "#SaludMentalAccesible", "#CentroPaz"]
    },
    "desconexion_tecnologica_tdah": {
        "id": 26,
        "kicker": "Dopamina & Pantallas",
        "title": "La trampa del Doomscrolling en cerebros con TDAH",
        "hook": "¿Te quedas 2 horas en la noche mirando videos sabiendo que mañana tienes que madrugar?",
        "points": [
            "Búsqueda de micro-dopamina inmediata que atrapa a la corteza prefrontal.",
            "La parálisis de pantalla: querer apagar el celular y sentir el cuerpo bloqueado.",
            "Rediseño de fricción ambiental (dejar el cargador fuera del dormitorio).",
            "Recuperar tu descanso y sueño reparador sin castigarte."
        ],
        "category": "TDAH & Hábitos",
        "caption": """El doomscrolling nocturno en cerebros con TDAH no es falta de disciplina: es una trampa de dopamina 📱🧠

Aprende estrategias de higiene ambiental para recuperar tu descanso.

👉 Acompañamiento en Centro Paz. WhatsApp: +56 9 6516 3893.""",
        "hashtags": HASHTAGS_BASE + ["#Doomscrolling", "#TDAHHabitos", "#HigieneDelSueño", "#Dopamina"]
    },
    "padres_regulacion_propia": {
        "id": 27,
        "kicker": "Regla del Oxígeno",
        "title": "No puedes regular a tu hijo si tu sistema está en alarma",
        "hook": "¿Sientes que la rutina diaria te tiene al borde de explotar con tus hijos?",
        "points": [
            "Neuronas espejo: los niños absorben la tensión de los padres antes de escuchar sus palabras.",
            "La pausa de 5 segundos antes de intervenir en un conflicto.",
            "Cuidar al cuidador: la crianza exige un espacio propio de descarga y orientación.",
            "Acompañamiento clínico empático para mamás y papás en Centro Paz."
        ],
        "category": "Crianza Consciente",
        "caption": """En un avión te dicen: 'Ponte la máscara de oxígeno tú primero antes de ayudar a tu hijo' 🌱

En la crianza es igual: tu calma es la herramienta más potente para regular a tus hijos.

👉 Agenda una sesión de orientación familiar al WhatsApp +56 9 6516 3893 o en www.centropaz.cl.""",
        "hashtags": HASHTAGS_BASE + ["#CrianzaConsciente", "#CuidarAlCuidador", "#OrientacionParental", "#CentroPaz"]
    },
    "autocuidado_fin_de_semana": {
        "id": 28,
        "kicker": "Pausa Consciente",
        "title": "Descanso pasivo vs. Descanso Sensorial: Cómo reponer energía",
        "hook": "¿Pasa el fin de semana y el lunes sientes que estás igual o más cansado/a?",
        "points": [
            "Descanso pasivo: mirar series en el sillón (aún hay estímulos sensoriales continuos).",
            "Descanso sensorial real: silencio, luz tenue, ropa holgada y cero exigencias sociales.",
            "Validar tus necesidades de baja estimulación como medicina preventiva.",
            "50 minutos semanales dedicados a tu bienestar con Valentina Castro Núñez."
        ],
        "category": "Autocuidado Adultos",
        "caption": """Descansar no es solo no trabajar: es permitir que tu sistema nervioso se sienta a salvo 🌿✨

Inicia tu proceso de psicoterapia en Centro Paz (presencial en Ñuñoa y online para todo Chile).

👉 Agenda tu hora al WhatsApp +56 9 6516 3893 o en www.centropaz.cl.""",
        "hashtags": HASHTAGS_BASE + ["#DescansoSensorial", "#AutocuidadoReal", "#SaludMentalChile", "#CentroPazÑuñoa"]
    }
}

REELS_SCRIPTS: Dict[str, Dict[str, Any]] = {
    "reel_01_procrastinacion_tdah": {
        "title": "Procrastinación vs. Parálisis de Dopamina",
        "duration": "35 segundos",
        "hook_visual": "Texto en grande: '¿Por qué no puedo empezar tareas simples si de verdad quiero?'",
        "hook_audio": "¿Alguna vez te has quedado horas sentado mirando el celular sabiendo exactamente lo que tienes que hacer, pero sintiendo que tu cuerpo pesa una tonelada?",
        "development": [
            "No es pereza: en el cerebro con TDAH la corteza prefrontal tiene un déficit en la liberación de dopamina para iniciar secuencias de baja estimulación.",
            "Decirte 'esfuérzate más' solo genera frustración y culpa.",
            "El truco es la micro-fricción cero: divide la tarea en un paso ridículamente pequeño (ej. solo abrir el documento) y asócialo a un estímulo sensorial."
        ],
        "cta": "En Centro Paz te acompañamos a comprender tu cerebro neurodivergente. Link directo a WhatsApp en nuestra biografía.",
        "recommended_audio": "Lo-fi relajante / tendencia explicativa suave"
    },
    "reel_02_reembolso_express": {
        "title": "Cómo Reembolsar tu Sesión en 3 Toques",
        "duration": "30 segundos",
        "hook_visual": "Boleta electrónica + App de Isapre en pantalla",
        "hook_audio": "¿Sabías que tu Isapre te puede devolver hasta el 70% del valor de tu sesión de psicología?",
        "development": [
            "Paso 1: Asistes a tu sesión online o presencial en Centro Paz con Valentina.",
            "Paso 2: Al terminar, te llega la boleta electrónica con código clínico a tu correo.",
            "Paso 3: La subes en la app de tu Isapre y el reembolso entra directo a tu cuenta bancaria."
        ],
        "cta": "Escríbenos a nuestro WhatsApp oficial (+56 9 6516 3893) y te ayudamos a simular tu cobertura.",
        "recommended_audio": "Upbeat acústico claro"
    },
    "reel_03_rabietas_desbordes": {
        "title": "Qué hacer ante una rabieta intensa",
        "duration": "40 segundos",
        "hook_visual": "Primer plano empático: 'Deja de decirle cálmate a un niño desbordado'",
        "hook_audio": "Cuando un niño o niña tiene un desborde emocional intenso, su cerebro lógico está completamente apagado.",
        "development": [
            "No es manipulación: es sobrecarga sensorial o emocional.",
            "Hablarle de consecuencias o castigos en ese instante solo eleva el cortisol.",
            "Primero correcibe: baja tu tono de voz, atenúa luces, ponte a su nivel visual y ofrece presencia física segura.",
            "La conversación sobre lo sucedido se hace horas después, cuando su sistema nervioso volvió a la calma."
        ],
        "cta": "Descarga gratis nuestra Guía de 7 Claves de Regulación en PDF. Pídenosla por WhatsApp.",
        "recommended_audio": "Piano suave y reflexivo"
    },
    "reel_04_masking_agotamiento": {
        "title": "El costo invisible del Masking",
        "duration": "35 segundos",
        "hook_visual": "'Llegar a casa y no querer que nadie te hable...'",
        "hook_audio": "¿Te pasa que en el trabajo eres súper funcional, pero llegas a tu casa sintiendo que no puedes ni pronunciar una palabra?",
        "development": [
            "Se llama 'Masking': el esfuerzo invisible de modular tu tono de voz, contacto visual y reprimir incomodidades sensoriales todo el día.",
            "Tu cuerpo gastó el doble de energía que el resto para parecer 'normal'.",
            "El colapso llega en privado y no se quita solo durmiendo."
        ],
        "cta": "Acompañamiento neuroafirmativo online y presencial en Ñuñoa. Escríbenos por WhatsApp.",
        "recommended_audio": "Música ambient suave y reflexiva"
    },
    "reel_05_ansiedad_ancla": {
        "title": "Ejercicio de 30s para frenar el sobrepensamiento nocturno",
        "duration": "30 segundos",
        "hook_visual": "'Si estás sobrepensando en la cama, haz esto ahora'",
        "hook_audio": "Si tu mente no para de proyectar problemas a las 2 AM, haz este ejercicio de estimulación del nervio vago.",
        "development": [
            "Haz dos inhalaciones cortas por la nariz y una exhalación muy lenta por la boca (suspiro fisiológico).",
            "Presiona suavemente las palmas de tus manos una contra la otra.",
            "Le estás indicando físicamente a tu amígdala que no hay ningún peligro inminente."
        ],
        "cta": "Aprende herramientas clínicas para tu bienestar emocional. Agenda tu hora en Centro Paz por WhatsApp.",
        "recommended_audio": "Sonido calmante con ondas binaurales"
    },
    "reel_06_tdah_paralisis": {
        "title": "Parálisis ejecutiva en TDAH adulto",
        "duration": "35 segundos",
        "hook_visual": "'Cuando tu mente quiere pero tu cuerpo no responde'",
        "hook_audio": "¿Te has quedado horas sentado mirando una tarea sabiendo que debes hacerla, sintiendo una barrera invisible?",
        "development": [
            "No es falta de voluntad: es una dificultad en la regulación de dopamina en la corteza prefrontal.",
            "Obligarte con culpa aumenta la respuesta de amenaza y empeora el bloqueo.",
            "La solución clínica: micro-fricción cero y estímulos sensoriales adaptados."
        ],
        "cta": "Atención neuroafirmativa para adultos en Centro Paz. WhatsApp en el perfil.",
        "recommended_audio": "Voz en off explicativa con fondo lo-fi"
    },
    "reel_07_culpa_maternidad": {
        "title": "Soltar la culpa en la crianza",
        "duration": "35 segundos",
        "hook_visual": "'Para la mamá o papá que siente que hoy lo hizo todo mal'",
        "hook_audio": "Si hoy perdiste la paciencia con tus hijos y te invade la culpa, escucha esto.",
        "development": [
            "No necesitas ser un padre o madre perfecto: la neurociencia demuestra que la clave es la capacidad de reparar.",
            "Pedir disculpas y validar a tu hijo/a le enseña que equivocarse es humano.",
            "Aprender a regularte tú es el mayor regalo emocional que puedes darles."
        ],
        "cta": "Orientación continua a padres en Centro Paz. Link a WhatsApp en bio.",
        "recommended_audio": "Piano acústico suave y reflexivo"
    }
}

THREADS_POSTS: Dict[str, List[str]] = {
    "tdah_masking": [
        "🧵 1/3 El cansancio crónico en personas adultas muchas veces no es flojera ni falta de vitaminas: es el costo invisible del 'masking'.",
        "2/3 Pasar 8 horas al día forzando contacto visual, modulando tu tono de voz y reprimiendo incomodidades sensoriales para 'encajar' consume el doble de energía que una jornada laboral común.",
        "3/3 En Centro Paz acompañamos a adultos con TDAH y TEA desde un enfoque neuroafirmativo. Sesiones online y presenciales en Ñuñoa con boleta reembolsable en Isapres. Escríbenos por WhatsApp (+56 9 6516 3893) o en https://www.centropaz.cl"
    ],
    "reembolso_claridad": [
        "🧵 1/3 Mucha gente pospone la terapia psicológica creyendo que es inaccesible con Isapre. Aquí te dejamos la matemática real:",
        "2/3 Sesión particular oficial: $45.000 CLP. Con boleta electrónica de psicología clínica, tu Isapre (Colmena, Banmédica, CruzBlanca, Consalud, etc.) y seguro te reembolsan entre el 50% y el 80%.",
        "3/3 Tu copago real puede quedar tan bajo como $12.000 a $18.000 por sesión. Simula tu cobertura en https://www.centropaz.cl o al WhatsApp +56 9 6516 3893."
    ],
    "desbordes_infantiles": [
        "🧵 1/3 Por qué decirle 'cálmate' a un niño en plena rabieta nunca funciona:",
        "2/3 Durante un desborde emocional, la corteza prefrontal (lógica y lenguaje) está temporalmente desconectada por la sobrecarga del sistema límbico. Hablar de consecuencias en ese instante solo aumenta el cortisol.",
        "3/3 Primero baja luces, habla en voz baja y ofrece presencia física segura (corregulación). Descarga nuestra Guía gratuita de 7 Claves en PDF pidiéndola por WhatsApp al +56 9 6516 3893 o en https://www.centropaz.cl"
    ]
}

FACEBOOK_COMMUNITY_POSTS: Dict[str, Dict[str, str]] = {
    "tdah_adultos_comunidad": {
        "title": "¿Cómo experimentas la sobrecarga mental en la semana laboral?",
        "text": """¿Te pasa que en el trabajo logras funcionar, pero al llegar a casa sientes que no te queda energía ni para responder un mensaje? 🧠

Muchas personas adultas descubren su TDAH o condición dentro del espectro autista después de los 25 o 30 años, tras haber vivido con la sensación de tener que esforzarse el triple para cumplir lo cotidiano.

En Centro Paz trabajamos desde un enfoque humanista y neuroafirmativo con la psicóloga clínica Valentina Castro Núñez (Registro Superintendencia de Salud).

📍 Sesiones online para todo Chile y presenciales en Ñuñoa (Santiago Oriente).
💳 Boletas electrónicas 100% reembolsables en todas las Isapres y Seguros Complementarios.

👉 Escríbenos directamente por WhatsApp al +56 9 6516 3893 o visita www.centropaz.cl para coordinar tu primera hora."""
    },
    "crianza_comunidad": {
        "title": "Orientación a Padres: Crianza Respetuosa sin Desgaste",
        "text": """Mamás y papás de Ñuñoa y Santiago: ¿Cómo acompañar a un hijo o hija con alta sensibilidad o sospecha de TEA/TDAH sin caer en la culpa ni en el agotamiento? 🌱

Criar desde la comprensión del perfil sensorial y la corregulación transforma la dinámica del hogar sin recurrir a gritos ni castigos.

En Centro Paz ofrecemos psicoterapia infanto-juvenil con sesiones continuas de orientación a padres.

👉 Agenda una sesión de orientación familiar por WhatsApp al +56 9 6516 3893 o en www.centropaz.cl"""
    }
}


def get_weekly_calendar(week: int = 1) -> List[Dict[str, Any]]:
    """Genera una parrilla semanal estructurada de 7 publicaciones para las 4 semanas (28 días)."""
    weeks_map = {
        1: [
            ("Lunes", "Educación & Validación (Neurodivergencias)", "tdah_adultos"),
            ("Martes", "Derribador de Objeción (Reembolso Isapre)", "reembolso_isapre"),
            ("Miércoles", "Orientación a Padres & Crianza", "crianza_regulacion"),
            ("Jueves", "Agotamiento Invisible (Masking)", "masking"),
            ("Viernes", "Acceso (Terapia Online)", "terapia_online"),
            ("Sábado", "Infancia: cuándo consultar", "evaluacion_infantil"),
            ("Domingo", "Llamado a agendar (Autocuidado)", "autocuidado_adultos"),
        ],
        2: [
            ("Lunes", "Neurodivergencias Profundas (Burnout Autista)", "burnout_autista"),
            ("Martes", "Manejo Cotidiano (Parálisis Ejecutiva TDAH)", "paralisis_ejecutiva"),
            ("Miércoles", "Herramientas Prácticas (Regulación Ansiedad)", "regulacion_ansiedad"),
            ("Jueves", "Paternidad Neurodivergente", "apoyo_neurodivergente_hijos"),
            ("Viernes", "Educación Clínica (Primera Sesión)", "primera_sesion"),
            ("Sábado", "Crianza Sin Culpa (Reparación Emocional)", "culpa_parental"),
            ("Domingo", "Transparencia Financiera (Reembolso Isapre)", "reembolso_matematica"),
        ],
        3: [
            ("Lunes", "TDAH en Mujeres (Diagnóstico Tardío)", "tdah_mujeres"),
            ("Martes", "Regulación Sensorial (Misofonía y Ruido)", "sobrecarga_sensorial_ruido"),
            ("Miércoles", "Doble Reembolso (Isapre + Seguro)", "reembolso_seguros_cobertura"),
            ("Jueves", "Ciclo del Hiperfoco & Burnout", "hiperfoco_burnout"),
            ("Viernes", "Rutinas Visuales para la Infancia", "crianza_rutinas_flexibles"),
            ("Sábado", "Límites Asertivos sin Culpa", "comunicacion_asertiva_limites"),
            ("Domingo", "Sensibilidad al Rechazo (RSD)", "tdah_rechazo_rsd"),
        ],
        4: [
            ("Lunes", "Consulta Presencial en Ñuñoa", "primera_consulta_nunoa"),
            ("Martes", "Terapia Infantil a través del Juego", "terapia_infantil_juego"),
            ("Miércoles", "Ansiedad Somática y Cuerpo", "ansiedad_somatica_cuerpo"),
            ("Jueves", "Guía de Boletas para Isapres", "isapre_licencia_boletas"),
            ("Viernes", "Desconexión de Pantallas y Dopamina", "desconexion_tecnologica_tdah"),
            ("Sábado", "Regulación Emocional de los Padres", "padres_regulacion_propia"),
            ("Domingo", "Descanso Sensorial de Fin de Semana", "autocuidado_fin_de_semana"),
        ]
    }

    plan = weeks_map.get(week, weeks_map[1])
    calendar = []
    for day, theme, key in plan:
        topic = TOPICS[key]
        calendar.append({
            "dia": day,
            "tipo": theme,
            "titulo": topic["title"],
            "gancho": topic["hook"],
            "copy": topic["caption"],
            "hashtags": " ".join(topic["hashtags"]),
            "topic_key": key,
            "id": topic["id"],
        })
    return calendar


def get_all_catalog() -> List[Dict[str, Any]]:
    """Retorna los 28 posts completos estructurados para publicación y n8n."""
    items = []
    for key, topic in TOPICS.items():
        items.append({
            "key": key,
            "id": topic["id"],
            "image_file": f"post_{topic['id']:02d}_{key}.png",
            "image_url": f"https://www.centropaz.cl/assets/instagram/post_{topic['id']:02d}_{key}.png",
            "title": topic["title"],
            "kicker": topic["kicker"],
            "hook": topic["hook"],
            "points": topic["points"],
            "category": topic["category"],
            "caption": topic["caption"],
            "hashtags": " ".join(topic["hashtags"]),
        })
    return items


def get_reels_catalog() -> List[Dict[str, Any]]:
    """Retorna los guiones virales de alta retención para video."""
    return [{"key": k, **v} for k, v in REELS_SCRIPTS.items()]


def get_threads_catalog() -> List[Dict[str, Any]]:
    """Retorna micro-hilos listos para Threads y X."""
    return [{"key": k, "tweets": v} for k, v in THREADS_POSTS.items()]


def get_multiplatform_matrix() -> Dict[str, Any]:
    """Genera una matriz omnicanal para Instagram, Facebook, TikTok y Threads con 28 posts y 4 semanas."""
    return {
        "brand": BRAND,
        "lead_magnet_pdf": "https://www.centropaz.cl/guia_7_claves_regulacion_centro_paz.pdf",
        "total_posts": len(TOPICS),
        "channels": {
            "instagram_facebook_feed": get_all_catalog(),
            "tiktok_reels_video_scripts": get_reels_catalog(),
            "threads_micro_threads": get_threads_catalog(),
            "facebook_community_posts": [{"key": k, **v} for k, v in FACEBOOK_COMMUNITY_POSTS.items()]
        },
        "weeks": {
            "week_1": get_weekly_calendar(week=1),
            "week_2": get_weekly_calendar(week=2),
            "week_3": get_weekly_calendar(week=3),
            "week_4": get_weekly_calendar(week=4),
        },
        "status": "ready_for_omnichannel_dispatch"
    }
'''

TARGET_FILE.write_text(CONTENT, encoding="utf-8")
print("✅ agent/content_engine.py actualizado con los 28 tópicos clínicos y 4 semanas completas.")
