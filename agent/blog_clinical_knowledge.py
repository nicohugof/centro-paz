"""
Base de Conocimiento Clínico Extendido para los 28 Artículos de Centro Paz.
Elaborado con rigor clínico, enfoque neuroafirmativo y redacción empática para pacientes.
Supervisión: Valentina Castro Núñez (Psicóloga Clínica, Registro SIS).
"""

CLINICAL_ARTICLES = {
    "tdah_adultos": {
        "subtitle": "Identificación, Neurobiología y Estrategias Reales en la Adultez",
        "lead_story": """¿Alguna vez te has sentido como un motor de Ferrari atrapado en una carrocería con frenos de bicicleta? Muchas personas adultas pasan 20, 30 o incluso 40 años conviviendo con la etiqueta de ser 'flojos', 'desorganizados' o 'inconstantes'. Intentan agendas, métodos de productividad japoneses y alarmas infinitas, solo para volver a la frustración y la culpa.

La flojera es una decisión consciente de no hacer algo porque no te importa. En el TDAH adulto, la persona quiere desesperadamente hacer la tarea, pero siente una parálisis física que le impide comenzar. No es un fallo moral ni falta de voluntad: es una diferencia neuroquímica en la corteza prefrontal.""",
        "what_is_happening": """El Trastorno por Déficit de Atención e Hiperactividad (TDAH) en adultos no es una falta de atención, sino una dificultad neurobiológica en su regulación. El cerebro con TDAH no puede dirigir voluntariamente sus recursos atencionales hacia tareas que carecen de novedad, interés intrínseco o urgencia inmediata.

La corteza prefrontal —encargada de la memoria de trabajo, la priorización y la activación— opera con un tono dopaminérgico basal reducido. Cuando intentas hacer una tarea rutinaria (como contestar correos o archivar boletas), tu cerebro experimenta una resistencia neuroquímica real. Si a esto se suman décadas de autoexigencia, el resultado es fatiga crónica y desregulación emocional.""",
        "daily_scenarios": [
            ("La barrera del inicio (Parálisis)", "Sabes que tienes un documento de 15 minutos, pero pasas 3 horas postergándolo mientras una angustia física crece en tu pecho."),
            ("Agotamiento por Masking", "En el trabajo te esfuerzas el doble para parecer ordenado y seguir la conversación, llegando a casa a las 19:00 hrs sin energía ni para hablar."),
            ("La memoria de trabajo volátil", "Vas a la cocina por agua, ves una taza sucia, abres el teléfono y 40 minutos después olvidaste para qué fuiste a la cocina."),
            ("Sensibilidad al rechazo", "Un comentario neutro de tu jefatura o pareja detona una sensación interna de catástrofe y duda sobre tu valor profesional.")
        ],
        "practical_steps": [
            ("Micro-acción de 2 minutos", "No te propongas 'terminar el informe'. Tu único objetivo neurológico es abrir el archivo y escribir una frase. Al bajar la fricción, la inercia dopaminérgica ayuda a continuar."),
            ("Externalizar la memoria de trabajo", "Tu mente es para tener ideas, no para guardarlas. Usa temporizadores visuales y notas adhesivas en lugares visibles, no en apps ocultas en el teléfono."),
            ("Body Doubling (Acompañamiento)", "Trabajar en compañía de otra persona (incluso en silencio o por videollamada) reduce la activación de amenaza y facilita sostener la atención.")
        ],
        "how_valentina_works": """En Centro Paz, el acompañamiento que realiza Valentina Castro Núñez es 100% neuroafirmativo y despatologizante. No buscamos encajarte en moldes rígidos que aumenten tu agotamiento.

En sesión trabajamos en desarmar la culpa histórica, comprender el funcionamiento de tu cerebro y diseñar acomodaciones externas para tu trabajo y vida cotidiana. Modalidad Online para todo Chile y Presencial en Ñuñoa (Santiago), con boletas reembolsables en Isapre.""",
        "whatsapp_prompt": "¿Sospechas que tu cansancio crónico o tu dispersión tienen base en un TDAH no diagnosticado? Escríbele directamente a Valentina por WhatsApp para orientarte sobre los pasos de evaluación o terapia.",
        "faqs": [
            ("¿Es obligatorio hacer una evaluación formal para empezar terapia?", "No obligatoriamente. Muchas personas inician psicoterapia centrada en herramientas prácticas y alivio de la ansiedad, y si es necesario, se coordina un proceso de evaluación estructurada."),
            ("¿A qué edad se suele diagnosticar el TDAH en adultos?", "Es muy habitual entre los 25 y 45 años, especialmente ante cambios de vida con mayor carga de gestión o el nacimiento de hijos."),
            ("¿Las sesiones se reembolsan en mi Isapre?", "Sí. Emitimos boleta electrónica oficial con código de psicología clínica reconocida por la Superintendencia de Salud para todas las Isapres y seguros complementarios.")
        ]
    },

    "reembolso_isapre": {
        "subtitle": "Guía Práctica, Coberturas del 50% al 80% y Trámite Digital",
        "lead_story": """Muchas personas postergan el inicio de su psicoterapia creyendo que la atención de calidad en salud mental es un lujo financiero. Se asume que pagar $45.000 CLP por sesión particular significará un desbalance presupuestario insostenible.

Sin embargo, el sistema de salud privado en Chile (Isapres y Seguros Complementarios) cuenta con convenios de libre elección diseñados para que el paciente elija al profesional de su confianza y recupere entre el 50% y el 80% del arancel pagado.""",
        "what_is_happening": """Las Isapres (Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres, Nueva Masvida) cuentan con tablas de bonificación para consultas de psicología clínica. Cuando un psicólogo clínico habilitado emite una Boleta de Honorarios Electrónica con su número de registro de prestador de salud (SIS), la Isapre debe reembolsar según el plan contratado.

Si además cuentas con un seguro complementario laboral o personal (MetLife, BiceVida, Bci, etc.), este actúa cubriendo el copago remanente, permitiendo que el costo neto por sesión quede entre $8.000 y $15.000 CLP.""",
        "daily_scenarios": [
            ("El temor al desembolso total", "Crees que pagarás $45.000 limpios de tu bolsillo, pero tras subir la boleta a la app tu Isapre te transfiere $28.000 de vuelta en pocos días."),
            ("La combinación Isapre + Seguro de empresa", "Tu Isapre cubre el 60% ($27.000) y tu seguro colectivo cubre el 70% del remanente ($12.600). Tu copago final real fue de solo $5.400 CLP."),
            ("Trámite 100% digital desde el celular", "Ya no hay que hacer filas: tomas una captura al PDF que te enviamos al terminar la sesión y la cargas en la app de tu Isapre en 1 minuto."),
            ("Previsibilidad mes a mes", "Al conocer tu tasa de reembolso real, puedes planificar un proceso de 2 a 4 sesiones mensuales con total tranquilidad.")
        ],
        "practical_steps": [
            ("Paso 1: Asiste a tu sesión con Valentina", "Ya sea online o presencial en Ñuñoa, al terminar recibes tu boleta electrónica con RUT y código SIS oficial."),
            ("Paso 2: Sube la boleta a la app de tu Isapre", "En 'Reembolsos' adjuntas el archivo. En la gran mayoría de los planes de Isapre no se exige orden médica para psicología."),
            ("Paso 3: Presenta el remanente en tu seguro complementario", "Descarga la liquidación de la Isapre y súbela al portal de tu seguro laboral para recibir el depósito final.")
        ],
        "how_valentina_works": """En Centro Paz entregamos máxima transparencia administrativa. Valentina Castro Núñez cuenta con registro activo en el Registro Nacional de Prestadores Individuales de la Superintendencia de Salud.

Emitimos tus boletas inmediatamente después de cada sesión con todas las glosas correctas para evitar rechazos. Si tienes dudas sobre tu plan, te orientamos para simular tu reembolso antes de agendar.""",
        "whatsapp_prompt": "¿Quieres saber exactamente cuánto te reembolsará tu Isapre por sesión? Escríbenos a WhatsApp indicando tu Isapre y te orientamos sin costo.",
        "faqs": [
            ("¿Necesito orden médica para reembolsar psicología?", "En Colmena, Banmédica, CruzBlanca y la mayoría de las Isapres no se requiere derivación médica. Si tu seguro laboral específico la pide, te indicamos cómo gestionarla."),
            ("¿Cuánto demora el depósito del reembolso?", "Habitualmente entre 48 horas y 5 días hábiles directo a tu cuenta bancaria."),
            ("¿Qué pasa si tengo Fonasa?", "La atención en Centro Paz es particular. Si cuentas con un Seguro Complementario de Salud en tu trabajo, puedes presentar la boleta para reembolso según tu póliza.")
        ]
    },

    "crianza_regulacion": {
        "subtitle": "Neurociencia Infantil, Meltdowns Sensoriales y Corregulación",
        "lead_story": """Es un martes por la tarde. Tu hijo/a de 6 años se tira al suelo, grita intensamente o arroja un juguete porque es hora de apagar la televisión. A tu alrededor sientes miradas de reproche y por dentro una mezcla asfixiante de culpa, impotencia y agotamiento.

El impulso natural es levantar la voz, exigirle que se calme o amenazar con un castigo. Sin embargo, notas que mientras más le pides que razone, el llanto empeora. No eres un mal padre o madre: lo que ocurre es que estás intentando razonar con un cerebro que tiene su corteza lógica temporalmente desconectada.""",
        "what_is_happening": """Durante un desborde emocional intenso, la amígdala cerebral del niño detecta una sobrecarga o amenaza (que a menudo es sensorial: fatiga, ruidos, hambre o frustración) y activa el sistema nervioso simpático de lucha o huida.

La corteza prefrontal, encargada de la lógica y el autocontrol, madura plenamente recién a los 25 años. En un niño pequeño o con neurodivergencia, pedirle 'cálmate' en medio de una crisis es neurológicamente inviable. Lo que el niño necesita con urgencia biológica es la corregulación: el apoyo de un adulto regulado que le preste su calma.""",
        "daily_scenarios": [
            ("El colapso de las 18:00 hrs", "Tu hijo llega del colegio tras 7 horas de portarse 'perfecto' y explota por el detalle más mínimo: es el efecto descompresión por haber contenido sobrecargas."),
            ("La batalla de las transiciones", "Dejar una pantalla, salir de la ducha o ponerse los zapatos detona una crisis de llanto prolongada."),
            ("La culpa posterior al enojo", "Pierdes la paciencia, gritas y luego te invade un remordimiento devastador pensando que dañaste a tu hijo."),
            ("La sobrecarga sensorial invisible", "Una etiqueta de ropa, zapatos apretados o un ambiente ruidoso saturan el sistema del niño sin que sepa expresarlo en palabras.")
        ],
        "practical_steps": [
            ("Baja tus propios decibeles primero", "El sistema nervioso del niño escanea el tuyo. Si gritas, confirmas la señal de peligro. Respira lento, ponte a su altura y habla en tono suave."),
            ("Reduce estímulos del entorno", "Apaga pantallas, baja la luz, reduce el ruido y ofrece un espacio seguro sin bombardear con preguntas."),
            ("Conexión antes que lección", "Valida con pocas palabras: 'Veo que estás muy enojado, estoy aquí contigo'. La conversación sobre límites se realiza 30 minutos después, cuando el agua volvió a su cauce.")
        ],
        "how_valentina_works": """En Centro Paz acompañamos a familias con herramientas realistas, basadas en evidencia y libres de juicios. Valentina Castro Núñez orienta a los padres para descifrar el perfil sensorial del niño y transformar la dinámica del hogar sin gritos ni castigos.

Sesiones de orientación a padres Online y Presenciales en Ñuñoa, con reembolso en Isapre.""",
        "whatsapp_prompt": "¿Sientes que los desbordes de tu hijo/a sobrepasan la paciencia de tu hogar y necesitas pautas claras? Escríbele a Valentina por WhatsApp para coordinar orientación parental.",
        "faqs": [
            ("¿Cuál es la diferencia entre una rabieta común y un colapso sensorial?", "La rabieta busca conseguir un objetivo y cede si obtiene lo deseado. El colapso (meltdown) es una sobrecarga neurosensorial involuntaria donde el niño pierde el control y no puede parar por sí solo."),
            ("¿Debo llevar al niño a la primera sesión?", "En orientación a padres, habitualmente la primera sesión es solo con los adultos para hablar con total libertad sin tensionar al niño."),
            ("¿A qué edad se recomienda consultar?", "Desde los 2 o 3 años cuando los desbordes son diarios, intensos o afectan seriamente la vida familiar o escolar.")
        ]
    },

    "masking": {
        "subtitle": "El Costo Invisible de Parecer Normal y Cómo Descomprimir",
        "lead_story": """Sales de tu casa por la mañana con una armadura invisible. Sonríes cuando corresponde, fuerzas el contacto visual, ensayas mentalmente cada frase antes de hablar y modulas tus expresiones para encajar. Los demás ven a un profesional eficiente o a alguien muy sociable.

Pero en cuanto cierras la puerta de tu hogar a las siete de la tarde, la armadura se desploma: sientes un vacío absoluto, dolor de cabeza y una imposibilidad física de responder un mensaje de texto. Este fenómeno se llama Masking o Camuflaje Social.""",
        "what_is_happening": """El masking es un mecanismo de adaptación aprendido para sobrevivir y evitar el rechazo en un entorno que sanciona la diferencia neurodivergente (autismo, TDAH, altas capacidades).

A nivel cerebral, mantener la monitorización social constante consume una cantidad inmensa de glucosa y neurotransmisores en la corteza prefrontal. La amígdala permanece en hipervigilancia vigilando signos de reproche social. Este sobreesfuerzo crónico es el principal detonante de colapsos, ansiedad social y depresión en personas neurodivergentes adultas.""",
        "daily_scenarios": [
            ("El guion mental continuo", "Repasas en tu cabeza cada interacción antes de que ocurra y analizas por horas si dijiste algo 'raro' en una reunión."),
            ("El agotamiento post-evento", "Tras un almuerzo familiar o una fiesta, necesitas 24 a 48 horas de aislamiento en silencio para recuperar tu energía."),
            ("Desconexión de tus propias necesidades", "Te acostumbras tanto a complacer las expectativas ajenas que olvidas qué te gusta, qué te cansa o cuándo necesitas parar."),
            ("Somatizaciones corporales", "Bruxismo severo, tensión crónica en cuello y hombros o problemas digestivos por contener la sobrecarga interna.")
        ],
        "practical_steps": [
            ("Reconoce tus micro-máscaras", "Observa qué comportamientos haces por genuina comodidad y cuáles haces por miedo al rechazo. El primer paso es tomar conciencia sin juzgarte."),
            ("Crea una zona de descompresión diaria", "Dedica 30 minutos al llegar a casa sin demandas: ropa holgada, luces tenues y sin la obligación de socializar."),
            ("Límites asertivos simples", "Aprende a decir: 'Hoy no tengo la energía disponible para ir, gracias por la invitación'. No necesitas inventar excusas.")
        ],
        "how_valentina_works": """En Centro Paz brindamos un espacio terapéutico donde no necesitas la armadura. Valentina Castro Núñez te acompaña a reencontrarte con tus necesidades genuinas, reducir la sobreexigencia y desarmar el miedo al juicio social.

Atención en Ñuñoa y Online para todo Chile, con boletas reembolsables en Isapre.""",
        "whatsapp_prompt": "¿Sientes que estás viviendo para cumplir expectativas ajenas y tu energía está en cero? Escríbele a Valentina por WhatsApp para coordinar tu primera sesión.",
        "faqs": [
            ("¿Desenmascarar significa volverme descortés?", "Para nada. Significa comunicarte desde la autenticidad y el respeto mutuo, sin forzar a tu sistema nervioso al punto de colapsar."),
            ("¿El masking solo ocurre en el autismo?", "No, es extremadamente común en mujeres con TDAH, personas con alta sensibilidad y quienes crecieron en entornos con poca validación emocional."),
            ("¿Cómo ayuda la psicoterapia en este proceso?", "Te entrega herramientas para identificar tus límites biológicos y expresarlos con seguridad y sin culpa.")
        ]
    },

    "terapia_online": {
        "subtitle": "Eficacia Clínica, Espacio Seguro y Eliminación de Barreras",
        "lead_story": """Para muchas personas, ir al psicólogo evoca correr contra el reloj, enfrentar el tráfico de la ciudad, buscar estacionamiento y esperar en una sala fría. Cuando entras a la consulta, tu sistema nervioso ya llega agotado y en alerta.

La telepsicología clínica permite acceder a un espacio de acompañamiento profundo y riguroso desde la comodidad y seguridad de tu propio hogar, sin tiempos muertos ni desgaste sensorial.""",
        "what_is_happening": """Múltiples metaanálisis clínicos internacionales demuestran que la psicoterapia online tiene exactamente la misma eficacia clínica y fortaleza en el vínculo terapéutico que la atención presencial para el tratamiento de la ansiedad, el TDAH, el autismo y la orientación a padres.

Al encontrarte en tu propio espacio familiar, tu sistema nervioso activa con mayor facilidad el tono vagal parasimpático (la rama del reposo y la seguridad). Esto reduce la resistencia inicial y facilita abordar temas personales con mayor serenidad.""",
        "daily_scenarios": [
            ("Pacientes en regiones de Chile", "Acceder a profesionales especializadas en neurodivergencias desde cualquier ciudad sin necesidad de viajar a Santiago."),
            ("Sensibilidad sensorial y fobia social", "Evitar el estrés de luces fluorescentes, salas de espera ruidosas y transporte público abarrotado."),
            ("Compatibilidad laboral", "Tomar tu sesión de 50 minutos durante el día sin perder 2 horas de traslado ida y vuelta."),
            ("Continuidad del tratamiento", "Mantener tus sesiones aunque estés de viaje, en reposo o con alta carga laboral.")
        ],
        "practical_steps": [
            ("Elige tu rincón privado", "Busca un espacio donde puedas cerrar la puerta y hablar con libertad. Usa audífonos para mayor nitidez y confidencialidad."),
            ("Transición de 5 minutos antes", "Tómate un vaso de agua o té y respira unos minutos antes de conectarte para desacelerar la mente."),
            ("Reembolso digital idéntico", "La boleta de honorarios emitida cuenta con el mismo código SIS oficial y se reembolsa con las mismas condiciones en tu Isapre.")
        ],
        "how_valentina_works": """Valentina Castro Núñez atiende a pacientes de todo Chile mediante videollamada confidencial para personas adultas y jóvenes desde los 12 años en adelante, además de sesiones remotas de orientación a padres. El encuadre es cálido, estructurado y centrado en tus metas personales.

Boleta electrónica de psicología clínica entregada inmediatamente tras la sesión.""",
        "whatsapp_prompt": "¿Prefieres la comodidad de atenderte online desde tu hogar? Escríbenos a WhatsApp para consultar horarios disponibles.",
        "faqs": [
            ("¿Atienden a niños de forma online?", "No. En Centro Paz la terapia individual online está disponible para adultos y jóvenes desde los 12 años. En menores de 12 años la terapia requiere juego y presencia física en nuestra consulta de Ñuñoa. Para familias en regiones ofrecemos Orientación a Padres 100% online."),
            ("¿La Isapre reembolsa igual la terapia online?", "Sí, el reembolso es exactamente idéntico al de una consulta presencial según tu plan de salud."),
            ("¿Qué plataforma se utiliza?", "Plataformas seguras y encriptadas como Google Meet o Zoom, fáciles de abrir desde el celular o computador.")
        ]
    },

    "evaluacion_infantil": {
        "subtitle": "Cuándo Consultar, Señales en la Infancia y Diagnóstico Temprano",
        "lead_story": """Los padres a menudo dudan meses antes de consultar con un profesional: '¿Será solo una etapa?', '¿Es muy consentido?', '¿Qué pasa si el colegio exagera?'. Mientras tanto, los problemas en el aula o los desbordes en el hogar van en aumento, generando tensiones y desgaste en toda la familia.

Pedir una consulta con una psicóloga infantil no significa que tu hijo 'tenga un problema grave': significa entregarle herramientas a tiempo para que su infancia y su autoestima no se vean dañadas por la incomprensión.""",
        "what_is_happening": """Durante la infancia, el cerebro experimenta una poda y reorganización sináptica acelerada. Cuando existen características de TDAH, Condición del Espectro Autista o dificultades de regulación emocional, las demandas académicas y sociales del colegio suelen superar los recursos del niño.

Si estas dificultades no se comprenden a tiempo, el niño internaliza la idea de que es 'malo' o 'tonto', acumulando ansiedad y desmotivación escolar. La intervención temprana no busca etiquetar, sino identificar el perfil neurobiológico singular para adaptar el entorno escolar y familiar.""",
        "daily_scenarios": [
            ("El informe escolar de alerta", "Profesores que señalan que el niño se desconecta con frecuencia, se para de su asiento o tiene conflictos recurrentes con compañeros."),
            ("Desbordes intensos ante pequeñas negativas", "Llantos incontrolables o conductas desafiantes cuando algo no sale exactamente como esperaba."),
            ("Hipersensibilidad a texturas o ruidos", "Molestia extrema ante el ruido del patio escolar, rechazo a cortarse las uñas o a ciertas prendas de vestir."),
            ("Aislamiento en los recreos", "Dificultad para iniciar o sostener el juego con otros niños de su edad, prefiriendo jugar solo.")
        ],
        "practical_steps": [
            ("Observa y anota patrones", "Lleva un registro de los momentos del día y las situaciones donde surgen los desbordes o bloqueos."),
            ("Evita comparar con hermanos o primos", "Cada niño tiene un ritmo madurativo y neurobiológico único; comparar solo aumenta la angustia familiar."),
            ("Agenda una sesión de orientación inicial", "Conversar con una especialista te permitirá saber con claridad si se requiere una evaluación formal o ajustes en las rutinas del hogar.")
        ],
        "how_valentina_works": """Valentina Castro Núñez combina una evaluación clínica rigurosa y lúdica para los niños con un acompañamiento cercano y práctico para los padres. Coordinamos reuniones con colegios y equipos PIE cuando es necesario para asegurar apoyos escolares adecuados.

Atención en Ñuñoa y Online para todo Chile, con boletas reembolsables en Isapres.""",
        "whatsapp_prompt": "¿El colegio te recomendó consultar o tienes dudas sobre el desarrollo de tu hijo/a? Escríbele a Valentina por WhatsApp para coordinar una primera evaluación.",
        "faqs": [
            ("¿A qué edad se puede evaluar a un niño/a?", "A partir de los 2 o 3 años ya es posible realizar pesquisas del desarrollo y orientación parental."),
            ("¿El proceso incluye informe para el colegio?", "Sí, en procesos de evaluación diagnóstica se entrega un informe clínico completo con recomendaciones para el colegio y la familia."),
            ("¿Las sesiones son reembolsables?", "Sí, todas las sesiones emiten boleta electrónica de psicología clínica para Isapres y seguros.")
        ]
    },

    "autocuidado_adultos": {
        "subtitle": "Pedir Ayuda No es Debilidad: Proteger tu Sistema Nervioso",
        "lead_story": """Vivimos en una cultura que premia la productividad sin descanso y la capacidad de 'poder con todo'. En ese ritmo, muchas personas postergan su bienestar emocional durante años: postergan el chequeo médico, el descanso y la terapia psicológica, convencidas de que primero están los hijos, el trabajo, las deudas o las demandas de los demás.

El problema es que cuando el sistema nervioso colapsa —a través de crisis de pánico, insomnio crónico, irritabilidad o depresión—, ya no puedes estar disponible para nadie. Cuidar de ti no es egoísmo: es la base indispensable para sostener tu vida.""",
        "what_is_happening": """El estrés crónico mantiene al eje hipotálamo-hipófisis-adrenal (HHA) inundando el organismo de cortisol y adrenalina de forma permanente. Este estado de alarma constante desgasta el sistema inmunológico, altera la microbiota intestinal y agota los receptores de serotonina y dopamina.

Pedir ayuda profesional es un acto de responsabilidad fisiológica y emocional: permite crear una pausa protegida donde el sistema nervioso puede descender de la hiperactivación y reorganizarse.""",
        "daily_scenarios": [
            ("La sensación de estar al límite", "Cualquier imprevisto doméstico o laboral te detona ganas de llorar o una ira desproporcionada que te asusta."),
            ("Insomnio y rumiación nocturna", "Te acuestas exhausto pero tu cabeza repasa pendientes y conversaciones pasadas hasta las 3 de la madrugada."),
            ("La dificultad para decir 'no'", "Aceptar favores y proyectos adicionales por miedo a defraudar, sintiendo un resentimiento sordo."),
            ("Desconexión del placer", "Actividades que antes disfrutabas ahora se sienten como una obligación más en tu lista.")
        ],
        "practical_steps": [
            ("Reserva 50 minutos no negociables", "Considera tu sesión de terapia como una cita médica vital que no se cancela por urgencias menores."),
            ("Práctica de respiración diafragmática diaria", "Inhala en 4 segundos, retén 4 y exhala en 6 segundos durante 5 minutos para activar el nervio vago."),
            ("Establece micro-límites cotidianos", "Comienza a decir: 'Puedo revisarlo mañana en la mañana' en lugar de resolverlo todo en la noche.")
        ],
        "how_valentina_works": """En Centro Paz, Valentina Castro Núñez ofrece un espacio seguro, cálido y sin presiones. Trabajamos en identificar el origen de la sobreexigencia, regular la respuesta de ansiedad y construir hábitos sostenibles de autocuidado.

Sesiones en Ñuñoa y Online para todo Chile, con boletas reembolsables en Isapres.""",
        "whatsapp_prompt": "¿Sientes que llevas demasiado tiempo postergando tu bienestar? Da el primer paso hoy y escríbele a Valentina por WhatsApp para coordinar tu primera sesión.",
        "faqs": [
            ("¿Con qué frecuencia son las sesiones?", "Habitualmente se inicia con una frecuencia semanal o quincenal de 50 minutos, adaptándose a tus necesidades y posibilidades."),
            ("¿Cuánto dura un proceso terapéutico?", "Depende de cada persona y motivo de consulta; trabajamos con objetivos claros y revisiones periódicas conjuntas."),
            ("¿Qué necesito para mi primera sesión?", "Solo ganas de conversar y un espacio tranquilo. No necesitas preparar ningún discurso.")
        ]
    },

    "burnout_autista": {
        "subtitle": "Colapso Neurosensorial, Pérdida de Habilidades y Recuperación",
        "lead_story": """Llegas al viernes esperando que un fin de semana en cama te devuelva la energía. Pero el lunes despiertas con el mismo agotamiento demoledor. Peor aún: cosas que antes hacías con facilidad —prepararte el desayuno, responder un correo, elegir qué ponerte o tolerar el ruido de la calle— ahora se sienten como escalar el Everest.

Esto no es flojera ni un bajón pasajero: es Burnout Autista. Un estado de colapso físico, mental y sensorial acumulado tras meses o años de forzar tu sistema nervioso a operar más allá de su capacidad biológica.""",
        "what_is_happening": """A diferencia del estrés laboral común, el burnout autista se caracteriza por una regresión o pérdida temporal de habilidades adaptativas y funciones ejecutivas, acompañada de un aumento drástico de la sensibilidad sensorial y episodios de mutismo o desconexión.

Ocurre cuando el costo de sostener el masking social y tolerar entornos sensorialmente agresivos agota las reservas neuronales. El sistema colapsa para forzar una detención biológica de emergencia. Descansar de forma pasiva viendo pantallas a menudo no cura el burnout autista, porque la pantalla sigue estimulando el sistema visual y dopaminérgico.""",
        "daily_scenarios": [
            ("Incapacidad para tomar decisiones simples", "Quedarte bloqueado 20 minutos frente al refrigerador sin poder decidir qué comer."),
            ("Intolerancia al ruido y a la luz", "El sonido del teclado o la luz de la oficina provocan irritabilidad y dolor físico real."),
            ("Pérdida de fluidez verbal", "Dificultad para articular palabras o encontrar términos comunes en una conversación."),
            ("Aislamiento social involuntario", "Sentir que responder un mensaje de WhatsApp requiere una energía que sencillamente no tienes.")
        ],
        "practical_steps": [
            ("Baja drástica de demandas sensoriales", "Usa tapones reductores de ruido (Loop) o audífonos con cancelación, luces cálidas y ropa holgada."),
            ("Permiso explícito para no socializar", "Informa a tus cercanos que estás en un periodo de recuperación y que responderás mensajes a tu ritmo."),
            ("Descanso sensorial real", "Pasa tiempo en silencio, en oscuridad o realizando tu hiperfoco favorito sin culpa ni metas de productividad.")
        ],
        "how_valentina_works": """Valentina Castro Núñez aborda el burnout autista desde un marco neuroafirmativo riguroso: validamos tu experiencia, desarmamos la culpa por la pérdida de habilidades y diseñamos un plan de acomodaciones ambientales y laborales para recuperar tu estabilidad.

Sesiones en Ñuñoa y Online para todo Chile, reembolsables en Isapres.""",
        "whatsapp_prompt": "¿Sientes que tus habilidades colapsaron y el descanso común no te repone? Escríbele a Valentina por WhatsApp para acompañarte en tu recuperación.",
        "faqs": [
            ("¿Cuánto tiempo tarda en superarse el burnout autista?", "Varía desde semanas hasta varios meses dependiendo del nivel de sobrecarga previa y de la capacidad de reducir demandas del entorno."),
            ("¿Se pueden recuperar las habilidades perdidas?", "Sí, a medida que el sistema nervioso recupera la regulación y se reducen los estresores crónicos, las funciones ejecutivas se restablecen."),
            ("¿Se puede evaluar autismo en adultos durante el burnout?", "A menudo es el momento en que las personas consultan, aunque se debe considerar el estado de fatiga para interpretar adecuadamente las evaluaciones.")
        ]
    },

    "paralisis_ejecutiva": {
        "subtitle": "Por Qué Tu Cerebro se Bloquea y Cómo Destrabar la Acción",
        "lead_story": """Tienes toda la intención de ordenar tu pieza, enviar un informe o pagar las cuentas del mes. Te sientas frente al computador, tienes tiempo de sobra y sabes exactamente qué hacer. Y sin embargo, pasan las horas y no te mueves. Te quedas mirando el celular, ordenando cosas irrelevantes o en un estado de congelamiento interno mientras la culpa te carcome.

Por fuera parece que 'no tienes ganas' o que eres 'irresponsable'. Por dentro, sientes una pared de concreto invisible que separa tu intención de tu acción física. Esto es la Parálisis Ejecutiva en el TDAH.""",
        "what_is_happening": """La función ejecutiva de 'iniciación de tarea' depende de una descarga de dopamina en el estriado y la corteza prefrontal que señalice al cuerpo que vale la pena gastar energía en esa acción.

En cerebros con TDAH, si una tarea no es inherentemente estimulante, novedosa o urgente (con riesgo de catástrofe inmediata), el cerebro no libera esa chispa dopaminérgica inicial. Forzarte con reproches ('eres flojo, muévete ya') activa la amígdala con cortisol y miedo, lo que provoca una respuesta de congelamiento somático (freeze), bloqueando aún más la capacidad de actuar.""",
        "daily_scenarios": [
            ("La tarea de los 5 minutos que tarda semanas", "Una llamada telefónica o un correo breve que pospones durante un mes entero con una angustia constante."),
            ("La parálisis por sobre-análisis", "Tener tantas opciones o pasos posibles que el cerebro colapsa sin saber cuál es el primer paso."),
            ("La culpa del final del día", "Llegar a la noche agotado no por haber trabajado, sino por haber luchado 8 horas contra tu propia parálisis interna."),
            ("El botón de urgencia como único motor", "Solo poder arrancar cuando faltan 3 horas para la entrega límite y el pánico suministra la adrenalina que faltaba.")
        ],
        "practical_steps": [
            ("Bajar la fricción a nivel microscópico", "Si tienes que estudiar, no digas 'voy a estudiar 2 horas'. Tu único objetivo es sentarte en la silla y abrir el cuaderno. Nada más."),
            ("Activar dopamina previa sin pantallas", "Escucha tu canción favorita con ritmo rápido o haz 10 saltos antes de sentarte para elevar el tono fisiológico."),
            ("Fraccionar en listas de 'micro-pasos tontos'", "Escribe pasos ridículamente pequeños: 1. Prender computador. 2. Abrir navegador. 3. Poner contraseña.")
        ],
        "how_valentina_works": """Valentina Castro Núñez trabaja con pacientes con TDAH para eliminar el ciclo de culpa y diseñar sistemas externos personalizados que superen la parálisis ejecutiva sin necesidad de vivir al borde del pánico.

Atención en Ñuñoa y Online para todo Chile, con boletas reembolsables en Isapre.""",
        "whatsapp_prompt": "¿Cansado/a de vivir atrapado/a en la parálisis de inicio y la culpa? Escríbele a Valentina por WhatsApp para coordinar tu primera sesión.",
        "faqs": [
            ("¿La parálisis ejecutiva es lo mismo que la procrastinación común?", "No. En la procrastinación común prefieres hacer algo más placentero. En la parálisis ejecutiva estás angustiado/a deseando hacer la tarea, pero tu sistema nervioso está bloqueado."),
            ("¿Cómo ayuda la terapia psicológica en esto?", "Te enseña a reconocer tus señales de bloqueo y a implementar acomodaciones que no dependan de la fuerza de voluntad pura."),
            ("¿Las sesiones son reembolsables?", "Sí, en todas las Isapres con boleta oficial de psicología clínica.")
        ]
    },

    "regulacion_ansiedad": {
        "subtitle": "Herramientas Somáticas, Nervio Vago y Fisiología de la Calma",
        "lead_story": """Tu mente está a mil por hora: anticipa problemas que aún no ocurren, repasa errores pasados y construye escenarios catastróficos. Intentas calmarte diciéndote a ti mismo/a 'no pienses en eso', 'todo va a estar bien' o 'no te preocupes tanto'. Pero mientras más intentas controlar tus pensamientos con la lógica, tu corazón late más rápido y tu pecho se aprieta más.

Esto ocurre porque estás intentando apagar un incendio en el segundo piso usando palabras, cuando el fuego se originó en el sótano: tu sistema nervioso corporal.""",
        "what_is_happening": """La respuesta de ansiedad es primordialmente fisiológica: el nervio vago y la rama simpática inundan el cuerpo de adrenalina, acelerando el pulso y contrayendo la musculatura para prepararte para pelear o huir.

La comunicación entre el cuerpo y el cerebro es un 80% ascendente (del cuerpo al cerebro a través de las fibras aferentes del nervio vago) y solo un 20% descendente. Intentar calmar la mente solo pensando es muy poco efectivo cuando el cuerpo sigue gritando peligro. Para calmar la mente, primero debemos calmar el cuerpo con señales somáticas directas.""",
        "daily_scenarios": [
            ("Opresión en el pecho o nudo en la garganta", "Sensación física de ahogo o dificultad para respirar hondo aun en reposo."),
            ("El bucle de sobrepensamiento antes de dormir", "La mente proyecta catástrofes laborales o familiares en cuanto te acuestas en silencio."),
            ("Tensión muscular crónica y mandíbula apretada", "Despertar con dolor de cuello o dientes adoloridos por apretar durante la noche."),
            ("Urgencia digestiva ante el estrés", "Molestias estomacales, colon irritable o náuseas ante situaciones de presión o incertidumbre.")
        ],
        "practical_steps": [
            ("El Suspiro Fisiológico (Neurociencia de Stanford)", "Toma dos inhalaciones seguidas por la nariz (una profunda y otra corta al final) y luego exhala todo el aire lento por la boca. Hazlo 3 veces para colapsar el dióxido de carbono y desacelerar el ritmo cardíaco."),
            ("Enraizamiento visual 3-3-3", "Nombra en voz baja 3 cosas que ves, 3 sonidos que escuchas y mueve 3 partes de tu cuerpo (tobillos, dedos, hombros) para traer la mente al presente físico."),
            ("Presión propioceptiva", "Cruza tus brazos sobre el pecho y date un abrazo firme o apoya los pies descalzos contra el suelo frío sintiendo el peso de tu cuerpo.")
        ],
        "how_valentina_works": """Valentina Castro Núñez combina la terapia cognitivo-conductual con técnicas somáticas integrativas y regulación del sistema nervioso. Te entrega herramientas prácticas para gestionar la ansiedad desde el cuerpo y la mente.

Sesiones en Ñuñoa y Online para todo Chile, con reembolso en Isapre.""",
        "whatsapp_prompt": "¿Sientes que sobrepensar te está agotando físicamente y necesitas recuperar la calma? Escríbele a Valentina por WhatsApp para coordinar tu primera sesión.",
        "faqs": [
            ("¿Por qué las técnicas de respiración a veces aumentan mi ansiedad?", "Si respiras muy rápido o hiperventilas, subes el oxígeno y aumentas el mareo. La clave siempre es que la exhalación sea el doble de larga que la inhalación."),
            ("¿Se puede curar la ansiedad o siempre viviré con ella?", "La ansiedad es una emoción biológica necesaria, pero su desregulación crónica sí se supera. En terapia aprendes a regularla para que deje de gobernar tu vida."),
            ("¿Las sesiones se reembolsan en Isapre?", "Sí, 100% reembolsables en todas las Isapres y seguros complementarios.")
        ]
    },

    "apoyo_neurodivergente_hijos": {
        "subtitle": "Crianza Neuroafirmativa, Perfil Sensorial y Clima Familiar",
        "lead_story": """Criar a un hijo o hija con sospecha o diagnóstico de TEA o TDAH puede sentirse como intentar navegar en aguas desconocidas con un mapa que no coincide con el terreno. Los consejos tradicionales de familiares o colegios —'lo que le falta es mano dura', 'está muy consentido', 'si no le haces caso se le pasa'— no solo no funcionan, sino que aumentan el sufrimiento del niño y la culpa de los padres.

Los niños con cerebros neurodivergentes no procesan las recompensas, las transiciones ni las demandas del entorno como sus pares neurotípicos. Cuando colapsan, no buscan desafiarte: su sistema nervioso está pidiendo ayuda porque sobrepasó su umbral biológico de tolerancia.""",
        "what_is_happening": """En el autismo y el TDAH infantil existen particularidades en el procesamiento sensorial y en el desarrollo de las funciones ejecutivas. Un patio escolar ruidoso, una textura de ropa o un cambio imprevisto de planes generan dolor y estrés fisiológico real.

Cuando se aplican castigos o aislamiento ('tiempo fuera'), el niño interpreta que su vínculo de seguridad está en riesgo justo en el momento en que menos recursos internos tiene para calmarse. El enfoque neuroafirmativo enseña a los padres a ser detectives sensoriales para anticipar la sobrecarga y corregular en la calma.""",
        "daily_scenarios": [
            ("Selectividad alimentaria extrema", "Rechazar alimentos por textura, color o temperatura; no es maña, es hipersensibilidad oral."),
            ("Colapso al llegar del colegio", "El niño acumuló sobrecarga durante 7 horas conteniéndose y explota al subirse al auto o llegar al hogar."),
            ("Rigidez ante cambios de planes", "Si un paseo se suspende por lluvia, el cambio imprevisto detona una crisis prolongada."),
            ("Llamados frecuentes del colegio", "Quejas de que 'no para quieto', 'se aísla' o 'le cuesta seguir instrucciones grupales'.")
        ],
        "practical_steps": [
            ("Anticipación visual y rutinas predecibles", "Usa dibujos o pictogramas para mostrar la secuencia del día. El cerebro ansioso se calma cuando sabe qué esperar."),
            ("Acomodaciones sensoriales en casa", "Identifica etiquetas molestas, mantén zonas con luz tenue y evalúa audífonos reductores de ruido en lugares saturados."),
            ("Rincón de la Calma voluntario", "Crea un espacio acogedor con cojines y juguetes sensoriales donde pueda acudir a regularse, jamás como castigo.")
        ],
        "how_valentina_works": """Valentina Castro Núñez entrega orientación continua y cercana a padres, ayudándoles a descifrar las necesidades singulares de sus hijos sin culpas. Coordinamos con colegios y equipos PIE para garantizar un trato respetuoso.

Atención en Ñuñoa y Online para todo Chile, con boletas reembolsables en Isapres.""",
        "whatsapp_prompt": "¿Sientes que los métodos tradicionales de crianza no funcionan con tu hijo/a y necesitas herramientas reales? Escríbele directamente a Valentina por WhatsApp.",
        "faqs": [
            ("¿El diagnóstico temprano limita a mi hijo?", "Al contrario: entrega claridad, alivia la culpa del niño y abre la puerta a acomodaciones escolares oportunas."),
            ("¿Puedo tomar sesiones solo de orientación parental?", "Sí, la orientación a padres es una de las herramientas de mayor impacto en el bienestar familiar."),
            ("¿Las sesiones se reembolsan en Isapre?", "Sí, emitimos boleta oficial de psicología clínica válida para todas las Isapres.")
        ]
    },

    "primera_sesion": {
        "subtitle": "Qué Esperar, Cómo Funciona y Por Qué No Hay Juicios",
        "lead_story": """Dar el primer paso para consultar al psicólogo genera incertidumbre: ¿Qué le voy a decir? ¿Por dónde empiezo si siento que todo en mi vida está enredado? ¿Y si me juzga o me dice algo que no quiero escuchar?

Muchas personas pasan meses dando vueltas a la idea antes de animarse a agendar. Es completamente normal sentir nerviosismo ante lo desconocido. Por eso, desmitificar qué sucede realmente en esos primeros 50 minutos es el mejor antídoto contra la vacilación.""",
        "what_is_happening": """La primera sesión de psicoterapia no es un interrogatorio ni un examen donde debas rendir cuentas. Es un encuentro humano, seguro y confidencial donde el terapeuta escucha tu historia sin preconcepciones.

A nivel clínico, el objetivo principal del primer encuentro es establecer la alianza terapéutica: que sientas que estás con una profesional que te comprende, valida tu ritmo y no te va a juzgar. Se exploran tus motivos de consulta actuales, cómo te impactan y qué esperas lograr con el proceso.""",
        "daily_scenarios": [
            ("No saber qué decir", "Llegar a la sesión sintiendo que tienes mil ideas desordenadas; Valentina te guiará con preguntas amables sin forzarte."),
            ("Miedo a ser juzgado/a", "Temor a contar hábitos, desórdenes o emociones de las que te avergüenzas, encontrando en cambio empatía clínica y comprensión."),
            ("Definir objetivos compartidos", "Acordar juntos hacia dónde apuntar: alivio de ansiedad, autoconocimiento neurodivergente o herramientas de crianza."),
            ("Tranquilidad administrativa", "Recibir tu boleta electrónica al terminar para reembolsar en tu Isapre sin demoras.")
        ],
        "practical_steps": [
            ("No necesitas preparar nada", "No tienes que escribir un resumen ni ordenar tus pensamientos; la conversación fluirá de forma natural."),
            ("Elige tu modalidad preferida", "Presencial en nuestra consulta en Ñuñoa (Plaza Egaña) u Online por videollamada desde tu habitación."),
            ("Pregunta con total libertad", "Puedes consultar sobre el enfoque terapéutico, la frecuencia de sesiones y cómo funciona el reembolso de tu plan.")
        ],
        "how_valentina_works": """Valentina Castro Núñez se caracteriza por un trato humano, cercano y horizontal. Su enfoque integra la psicología humanista con la evidencia contemporánea en neurodivergencias y salud mental de adultos y familias.

Arancel transparente de $45.000 CLP con boleta reembolsable en todas las Isapres.""",
        "whatsapp_prompt": "¿Tienes dudas sobre cómo sería tu primera sesión o quieres consultar por disponibilidad? Escríbele a Valentina por WhatsApp para orientarte con calidez.",
        "faqs": [
            ("¿Qué pasa si me emociono o lloro en la sesión?", "El espacio terapéutico está diseñado precisamente para que puedas expresar tus emociones sin vergüenza ni contención forzada."),
            ("¿Tengo que comprometerme a un número fijo de sesiones?", "No, la frecuencia y duración del proceso se acuerdan de común acuerdo según tus metas y posibilidades."),
            ("¿Cómo agendo?", "Puedes escribirnos directo por WhatsApp al +56 9 6516 3893 o reservar a través de nuestra web.")
        ]
    },

    "culpa_parental": {
        "subtitle": "Padres Regulados vs Padres Perfectos y Reparación del Vínculo",
        "lead_story": """Termina el día. Tus hijos ya se durmieron y la casa finalmente queda en silencio. Te sientas al borde de la cama o en el sillón y una ola de culpa te invade: 'Hoy le grité otra vez', 'No tuve paciencia', 'Pasó demasiado tiempo en la tablet', 'Soy una mala madre/mal padre'.

Vivimos bombardeados por imágenes de crianza idealizada en redes sociales que nos hacen creer que los buenos padres jamás pierden la calma, jamás se cansan y siempre responden con una sonrisa zen. La realidad clínica es que la perfección en la crianza no solo no existe, sino que es perjudicial para el desarrollo de los niños.""",
        "what_is_happening": """El célebre psicoanalista y pediatra Donald Winnicott acuñó el concepto de la 'madre (o padre) suficientemente bueno'. Los niños no necesitan figuras perfectas que anticipen cada deseo; necesitan adultos humanos, predecibles y capaces de **reparar la conexión cuando se ha roto**.

Cuando un padre pierde la paciencia, lo que daña al niño no es el error en sí, sino el silencio o la frialdad posterior. Si el adulto se regula y luego vuelve con calidez a pedir disculpas ('Perdón por haber gritado, estaba muy cansado/a y no fue tu culpa'), le entrega al niño la lección emocional más valiosa: que los errores se pueden reparar y que el amor es incondicional.""",
        "daily_scenarios": [
            ("El agotamiento al final de la jornada", "Llegar del trabajo con la batería en cero y responder de forma cortante ante una demanda menor del niño."),
            ("La trampa de la comparación digital", "Ver en Instagram a familias 'perfectas' y sentir que tú estás fallando en todo."),
            ("El miedo a 'traumar' a tus hijos", "Vivir con la angustia constante de que un mal día arruinará la salud mental futura de tu hijo."),
            ("La dificultad de pedir perdón", "Sentir que disculparte con tu hijo te quita autoridad, cuando en realidad construye un apego seguro indestructible.")
        ],
        "practical_steps": [
            ("Aprende a reparar después del desborde", "Espera a que ambos estén en calma. Acércate, ponte a su altura y di: 'Me equivoqué al levantar la voz. Te quiero y la próxima vez respiraré antes de hablar'."),
            ("Prioriza tu propia regulación primero", "No puedes dar de un vaso vacío. Si estás sobrepasado, di: 'Mamá/Papá necesita 5 minutos para respirar y vuelvo contigo'."),
            ("Suelta la expectativa de la perfección", "Reconoce que ser un buen padre o madre incluye tener días difíciles y pedir ayuda profesional cuando la carga es excesiva.")
        ],
        "how_valentina_works": """En Centro Paz acompañamos a padres y madres a liberarse de la culpa paralizante y a construir pautas de crianza respetuosa adaptadas a la realidad cotidiana de cada hogar.

Sesiones en Ñuñoa y Online para todo Chile, con boletas reembolsables en Isapre.""",
        "whatsapp_prompt": "¿Sientes que la culpa en la crianza te está consumiendo y necesitas orientación sin juicios? Escríbele a Valentina por WhatsApp para coordinar una sesión de orientación.",
        "faqs": [
            ("¿Pedir perdón a mi hijo me hace perder autoridad?", "Al contrario. Le enseña humildad, responsabilidad afectiva y que las relaciones sanas se basan en el respeto mutuo."),
            ("¿Qué hago si mi pareja tiene un estilo de crianza diferente?", "En orientación a padres trabajamos en alinear criterios comunes y reducir discrepancias frente a los hijos."),
            ("¿Las sesiones de crianza son reembolsables?", "Sí, emiten boleta electrónica de psicología clínica para todas las Isapres.")
        ]
    },

    "reembolso_matematica": {
        "subtitle": "Desglose Financiero, Simulador y Coberturas Reales",
        "lead_story": """A la hora de iniciar un tratamiento médico o terapéutico, la claridad financiera es un pilar fundamental de la tranquilidad del paciente. Nadie quiere sorpresas desagradables a fin de mes ni letras chicas que encarezcan el cuidado de la salud mental.

En Centro Paz operamos bajo un principio innegociable de transparencia: te explicamos exactamente cuánto pagas, cuánto te devuelve tu Isapre y cuál es el copago neto que sale de tu bolsillo en cada sesión.""",
        "what_is_happening": """El arancel de la sesión particular de 50 minutos con Valentina Castro Núñez es de **$45.000 CLP**. Este valor incluye la emisión inmediata de tu Boleta de Honorarios Electrónica con código oficial de psicología clínica y número de prestador individual de la Superintendencia de Salud.

Las Isapres bonifican según el plan contratado por cada persona:
- **Planes con cobertura del 60% al 80%:** Bonifican entre $27.000 y $36.000 CLP por sesión, dejando tu copago real entre $9.000 y $18.000 CLP.
- **Planes con tope arancelario:** Suelen cubrir un monto fijo de entre $20.000 y $30.000 CLP por sesión.
- **Seguros Complementarios:** Si cuentas con seguro laboral, este cubre habitualmente entre el 50% y el 80% del remanente que no pagó la Isapre, reduciendo el copago final a cifras tan bajas como $5.000 a $10.000 CLP.""",
        "daily_scenarios": [
            ("Ejemplo Plan Colmena / Banmédica al 70%", "Pagas $45.000 CLP. La Isapre te reembolsa $31.500 CLP. Tu gasto real por sesión: $13.500 CLP."),
            ("Ejemplo con Seguro Complementario de Trabajo", "Pagas $45.000 CLP. Isapre cubre $25.000 CLP. Seguro complementario cubre $14.000 CLP. Copago final: $6.000 CLP."),
            ("Facilidad de pago", "Puedes pagar con transferencia electrónica o tarjeta de débito/crédito, coordinando tus pagos con tus fechas de reembolso."),
            ("Acompañamiento en el trámite", "Te enviamos la boleta en PDF con todos los datos necesarios para cargarla en la app de tu aseguradora en un par de clics.")
        ],
        "practical_steps": [
            ("Usa nuestro simulador web", "Ingresa a www.centropaz.cl para estimar tu cobertura según tu plan de Isapre."),
            ("Verifica si tienes seguro complementario", "Consulta en el departamento de personas de tu empresa si tienes seguro de salud colectivo vigente."),
            ("Coordina con Valentina", "Si tienes dudas sobre las glosas de tu aseguradora, te orientamos antes de emitir tu boleta.")
        ],
        "how_valentina_works": """En Centro Paz no hay cobros ocultos ni trámites engorrosos. Valentina Castro Núñez está debidamente inscrita en la Superintendencia de Salud para que tus reembolsos se procesen sin trabas.

Atención en Ñuñoa y Online para todo Chile.""",
        "whatsapp_prompt": "¿Quieres saber exactamente cuánto te costará tu proceso terapéutico según tu Isapre y seguro? Escríbenos a WhatsApp y te hacemos el cálculo de inmediato.",
        "faqs": [
            ("¿El arancel de $45.000 incluye boleta para reembolso?", "Sí, el 100% de nuestras sesiones incluye boleta electrónica válida para Isapres y seguros."),
            ("¿Tengo que esperar a fin de mes para reembolsar?", "No, puedes subir cada boleta el mismo día en que se emite."),
            ("¿Aceptan pagos con tarjeta de crédito?", "Sí, puedes coordinar el medio de pago que te resulte más cómodo.")
        ]
    }
}

# Artículos 15 al 28
CLINICAL_ARTICLES_EXTENDED = {
    "tdah_mujeres": {
        "subtitle": "Diagnóstico Tardío, Perfeccionismo y Manifestación Internalizada",
        "lead_story": """Durante décadas, los criterios diagnósticos del TDAH se construyeron observando a niños varones hiperactivos que interrumpían la clase o corrían sin parar. Como resultado, millones de niñas y mujeres crecieron con su neurodivergencia completamente invisibilizada, catalogadas simplemente como 'soñadoras', 'demasiado sensibles', 'desordenadas' o 'ansiosas'.

El diagnóstico en mujeres suele llegar recién a los 30 o 35 años, a menudo tras un quiebre vital: el nacimiento del primer hijo, un ascenso laboral con alta demanda de gestión o una crisis de agotamiento crónico tras décadas de compensar el doble.""",
        "what_is_happening": """En mujeres, el TDAH se manifiesta predominantemente como presentación inatenta o internalizada: la hiperactividad no es motora sino mental (rumiación incesante, sobrepensamiento y saltos asociativos constantes).

Para evitar el reproche social, muchas mujeres desarrollan un masking hiper-exigente: son las alumnas o profesionales ultra-responsables que entregan todo a tiempo, pero a costa de no dormir, sufrir ansiedad paralizante y vivir al borde del colapso. Además, las fluctuaciones de estrógeno durante el ciclo menstrual, el posparto o la perimenopausia alteran los niveles de dopamina, agravando los síntomas atencionales y ejecutivos.""",
        "daily_scenarios": [
            ("Agotamiento por hiper-compensación", "Trabajar hasta la medianoche para revisar cinco veces un informe por miedo a haber cometido un error tonto."),
            ("La sensación de fraude interno (Síndrome del Impostor)", "Sentir que si los demás vieran el caos de tu closet, tu correo o tu mente, descubrirían que 'no eres tan capaz'."),
            ("Diagnósticos previos de ansiedad o depresión", "Haber tomado antidepresivos durante años sin que la desorganización de base y la fatiga mental remitan."),
            ("Sensibilidad hormonal marcada", "Notar que la semana previa a la menstruación tus funciones ejecutivas colapsan y la irritabilidad se dispara.")
        ],
        "practical_steps": [
            ("Deconstruir la culpa del perfeccionismo", "Reconoce que tu autoexigencia extrema fue un mecanismo de supervivencia, no un defecto de carácter."),
            ("Mapear tu ciclo hormonal y tu energía", "Planifica tareas de alta demanda cognitiva en fases de mayor estrógeno y reduce exigencias en la fase lútea."),
            ("Consultar con enfoque neuroafirmativo", "Acude a una profesional especializada que comprenda el fenotipo femenino del TDAH.")
        ],
        "how_valentina_works": """Valentina Castro Núñez brinda un espacio especializado en neurodivergencias en mujeres adultas, abordando tanto la evaluación clínica como el acompañamiento psicoterapéutico centrado en la autocompasión y la autonomía.

Atención en Ñuñoa y Online para todo Chile, con boletas reembolsables en Isapres.""",
        "whatsapp_prompt": "¿Te identificas con estas señales y sospechas de un TDAH no reconocido en tu adultez? Escríbele a Valentina por WhatsApp para coordinar una primera sesión.",
        "faqs": [
            ("¿Por qué no me diagnosticaron en la infancia?", "Porque las niñas suelen manifestar inatención silenciosa y enmascaran mejor sus dificultades para agradar a su entorno."),
            ("¿Qué cambia recibir un diagnóstico a los 30 o 40 años?", "Cambia todo: te libera de décadas de culpa, te permite comprender tu funcionamiento y abre el camino a estrategias efectivas."),
            ("¿Las sesiones son reembolsables en Isapre?", "Sí, 100% reembolsables en todas las Isapres.")
        ]
    },

    "sobrecarga_sensorial_ruido": {
        "subtitle": "Misofonía, Hipersensibilidad Acústica y Descompresión",
        "lead_story": """Estás en la oficina o en la mesa familiar. Alguien mastica una manzana, el teclado de al lado suena como martillazos, o el murmullo de un mall te provoca una irritación tan intensa que sientes ganas de salir corriendo o gritar. A tu alrededor te dicen: 'no seas tan mañoso/a', 'no exageres' o 'aprende a tolerar'.

Esto no es falta de paciencia ni mal carácter. Es una respuesta física de tu sistema nervioso ante la sobrecarga sensorial auditiva.""",
        "what_is_happening": """En personas neurodivergentes o con alta sensibilidad, los filtros talámicos del cerebro no atenúan los sonidos de fondo de manera automática. Tu cerebro procesa todos los decibeles al mismo volumen y con la misma prioridad.

Cuando la sobrecarga supera tu umbral biológico, la amígdala lo interpreta como un ataque físico y activa la respuesta de lucha o huida. En la misofonía, ciertos sonidos específicos detonan una respuesta emocional de furia o angustia inmediata debido a conexiones hiperactivas entre la corteza auditiva y el sistema límbico.""",
        "daily_scenarios": [
            ("La saturación en espacios concurridos", "Terminar con dolor de cabeza o náuseas tras pasar 1 hora en un supermercado o centro comercial ruidoso."),
            ("Irritabilidad repentina ante ruidos repetitivos", "Sentir ira involuntaria ante el goteo de una llave, el masticar de alguien o el clic de un lápiz."),
            ("Agotamiento al final del día laboral", "Sentir que el ruido ambiente de la oficina te drenó más energía que el trabajo mismo."),
            ("Dificultad para concentrarse con música o voces", "Necesitar silencio absoluto o ruido blanco para poder redactar un texto.")
        ],
        "practical_steps": [
            ("Usa protección auditiva sin culpa", "Tapones reductores de ruido como Loop o audífonos con cancelación activa son adaptaciones tan legítimas como usar anteojos para ver bien."),
            ("Pausas de descompresión en silencio", "Tómate 5 minutos de aislamiento acústico en el baño o en una sala vacía durante tu jornada."),
            ("Comunica tus límites con serenidad", "Explica a tu entorno cercano que el ruido te genera sobrecarga física, no rechazo hacia ellos.")
        ],
        "how_valentina_works": """Valentina Castro Núñez te ayuda a mapear tu perfil sensorial, diseñar acomodaciones cotidianas y regular el sistema nervioso para que la hipersensibilidad no limite tu calidad de vida.

Atención en Ñuñoa y Online para todo Chile, con reembolso en Isapre.""",
        "whatsapp_prompt": "¿Sientes que el ruido te sobrepasa a diario y necesitas herramientas para regular tu sistema sensorial? Escríbele a Valentina por WhatsApp.",
        "faqs": [
            ("¿La hipersensibilidad al ruido se puede quitar?", "No se trata de 'eliminarla' forzándote a aguantar, sino de aprender a regular el entorno y proteger tus sentidos."),
            ("¿Es común en el TDAH y el autismo?", "Sí, es uno de los rasgos sensoriales más prevalentes en ambos perfiles."),
            ("¿Las sesiones se reembolsan en Isapre?", "Sí, emitimos boleta oficial con código de psicología clínica.")
        ]
    },

    "reembolso_seguros_cobertura": {
        "subtitle": "Doble Cobertura: Cómo Combinar Isapre + Seguro de Empresa",
        "lead_story": """Muchas personas desconocen que pueden activar simultáneamente dos beneficios de salud para financiar su psicoterapia: su plan de Isapre y su Seguro Complementario de Salud (personal o contratado por su empleador).

Al combinar ambas coberturas de forma secuencial, el copago final que sale de tu bolsillo puede quedar tan bajo como $8.000 a $12.000 CLP por sesión.""",
        "what_is_happening": """El mecanismo de doble bonificación opera así: la Isapre actúa como asegurador primario, cubriendo su porcentaje habitual (50% a 70%). El saldo remanente que no cubrió la Isapre no se pierde: se presenta ante tu compañía de seguros complementarios como copago no bonificado.

La aseguradora complementaria aplica su propia tasa de cobertura (habitualmente 60% a 80% sobre el saldo restante), cubriendo casi la totalidad de la diferencia.""",
        "daily_scenarios": [
            ("Pagar una fracción del valor real", "Una sesión de $45.000 CLP termina costándote menos que un almuerzo o una salida al cine."),
            ("Acceso a tratamiento continuo", "Poder sostener un proceso terapéutico de 4 sesiones mensuales sin estrés financiero."),
            ("Trámite digital sin papeles", "Cargar la boleta en la app de la Isapre y luego subir el comprobante de liquidación a la app del seguro en 2 minutos."),
            ("Aprovechar beneficios laborales", "Hacer valer los seguros de salud que tu empresa ya paga mensualmente por ti.")
        ],
        "practical_steps": [
            ("Paso 1: Boleta oficial en Centro Paz", "Recibes tu boleta electrónica con código SIS al finalizar tu sesión con Valentina."),
            ("Paso 2: Reembolso primario en Isapre", "Subes la boleta a tu Isapre y descargas el comprobante de bonificación emitido."),
            ("Paso 3: Reembolso secundario en Seguro", "Ingresas al portal de tu seguro complementario y adjuntas la boleta original + el comprobante de la Isapre.")
        ],
        "how_valentina_works": """Valentina Castro Núñez emite boletas electrónicas estandarizadas aceptadas por todas las compañías de seguro del país (MetLife, BiceVida, Bci, Consorcio, Chilena Consolidada, etc.).

Sesiones en Ñuñoa y Online para todo Chile.""",
        "whatsapp_prompt": "¿Quieres saber cómo tramitar la doble cobertura de tu Isapre y seguro? Escríbenos a WhatsApp y te asesoramos paso a paso.",
        "faqs": [
            ("¿El seguro complementario exige orden médica?", "Algunas pólizas corporativas la solicitan una vez al año. Si es tu caso, te explicamos cómo tramitarla con facilidad."),
            ("¿Puedo reembolsar sesiones pasadas?", "La mayoría de las Isapres y seguros permiten reembolsar boletas con hasta 60 o 90 días de antigüedad."),
            ("¿Las sesiones presenciales y online tienen la misma cobertura?", "Sí, exactamente la misma bonificación.")
        ]
    },

    "hiperfoco_burnout": {
        "subtitle": "El Ciclo de la Obsesión Productiva al Colapso en 48 Horas",
        "lead_story": """El lunes te obsesionas con un nuevo proyecto: trabajas 12 horas seguidas sin parar, olvidas almorzar, no vas al baño y avanzas lo que otros tardan un mes en hacer. Sientes que eres imparable y que encontraste la genialidad.

Pero llega el miércoles y tu energía cae al fondo de un abismo. No puedes ni abrir el archivo, la tarea te parece insoportablemente aburrida y te invade la culpa por no ser constante. Este es el ciclo clásico del Hiperfoco y Burnout en el TDAH.""",
        "what_is_happening": """El hiperfoco es un estado de concentración intensa e involuntaria que ocurre cuando una tarea estimula fuertemente los receptores de dopamina en el cerebro con TDAH. Durante el hiperfoco, la corteza prefrontal inhibe todas las señales periféricas (incluso señales fisiológicas de hambre, sed o fatiga).

El problema es que la dopamina es un neurotransmisor biológico que se agota. Trabajar 12 horas en hiperfoco consume tus reservas de neurotransmisores y satura el sistema nervioso, provocando un bajón neuroquímico severo que dura días. El hiperfoco no es un superpoder sostenible si no aprendes a poner frenos antes de quemarte.""",
        "daily_scenarios": [
            ("El colapso post-entrega", "Entregar un proyecto brillante y pasar los tres días siguientes sin energía para levantarte de la cama."),
            ("La pérdida de interés fulminante", "Comprar todos los materiales para un nuevo hobby, obsesionarte 1 semana y abandonarlo por completo al mes siguiente."),
            ("Desatender necesidades básicas", "Pasar un día entero sin comer ni tomar agua por estar absorto/a en una pantalla o tarea."),
            ("La culpa de la inconsistencia", "Sentir que eres 'capaz de cosas increíbles pero totalmente incapaz de ser constante'.")
        ],
        "practical_steps": [
            ("Pausas fisiológicas obligatorias", "Pon una alarma cada 90 minutos para levantarte, tomar agua y caminar 3 minutos, incluso si estás en pleno hiperfoco."),
            ("No agotes la dopamina al 100%", "Detén la tarea cuando aún tengas ganas de continuar; esto deja una reserva dopaminérgica que facilita retomar al día siguiente."),
            ("Validar que tu ritmo no es lineal", "Acepta que tu productividad funciona por ciclos y aprende a gestionar los valles de energía sin castigarte.")
        ],
        "how_valentina_works": """Valentina Castro Núñez trabaja con personas con TDAH para aprender a regular el hiperfoco, diseñar rutinas flexibles y prevenir los ciclos recurrentes de colapso laboral y emocional.

Sesiones en Ñuñoa y Online para todo Chile, reembolsables en Isapres.""",
        "whatsapp_prompt": "¿Cansado/a de vivir en la montaña rusa del hiperfoco y el agotamiento? Escríbele a Valentina por WhatsApp para coordinar una primera sesión.",
        "faqs": [
            ("¿El hiperfoco es exclusivo del TDAH?", "También es muy frecuente en personas autistas y en perfiles con altas capacidades."),
            ("¿Se puede controlar el hiperfoco a voluntad?", "No se puede encender como un interruptor, pero sí se pueden crear condiciones para canalizarlo y ponerle frenos saludables."),
            ("¿Las sesiones se reembolsan en Isapre?", "Sí, 100% reembolsables en todas las Isapres.")
        ]
    },

    "crianza_rutinas_flexibles": {
        "subtitle": "Apoyos Visuales Infantiles, Anticipación y Hogar sin Batallas",
        "lead_story": """'Lávate los dientes', 'ponte los zapatos', 'guarda los juguetes', 'apúrate que vamos a llegar tarde'. Para muchos padres, cada mañana y cada noche se convierte en un disco rayado de instrucciones verbales repetidas diez veces, que inevitablemente terminan en gritos, llanto y frustración mutua.

El problema no es que tu hijo/a sea 'sordo' o desobediente: el problema es que el cerebro infantil procesa el lenguaje verbal a un tercio de la velocidad de las imágenes visuales.""",
        "what_is_happening": """La memoria de trabajo de los niños es limitada y se satura con rapidez ante cadenas de órdenes verbales ('ve a la pieza, saca la mochila, busca la polera y lávate la cara'). Cuando el niño se distrae con un juguete a mitad de camino, no está desafiando tu autoridad: su memoria de trabajo simplemente borró la instrucción.

Los apoyos visuales (pizarras con dibujos, fotos de las etapas del día o tarjetas magnéticas) externalizan la memoria de trabajo. El niño no tiene que recordar qué le dijo su mamá: mira la pared y ve la secuencia concreta. Esto reduce la ansiedad, devuelve la autonomía y elimina la confrontación directa.""",
        "daily_scenarios": [
            ("La rutina caótica de la mañana", "Demorar 45 minutos en vestirse y salir apurados todos los días con tensión familiar."),
            ("La resistencia a dejar el juego", "Llantos cada vez que hay que sentarse a almorzar o ir a bañarse."),
            ("El agotamiento del adulto", "Sentir que tienes que estar encima de tu hijo como un sargento para que haga las cosas mínimas."),
            ("El niño que se siente 'malo'", "Un niño que empieza a creer que siempre hace todo mal porque recibe reproches constantes.")
        ],
        "practical_steps": [
            ("Crea una rutina visual sencilla", "Usa dibujos simples o fotos de tu hijo haciendo la acción: 1. Pijama off. 2. Ropa on. 3. Desayuno. 4. Dientes. 5. Mochila."),
            ("Transiciones con aviso de 10 y 5 minutos", "Usa temporizadores con arena o reloj visual: 'Cuando la arena baje, cambiamos a cenar'."),
            ("Ofrece 2 opciones válidas", "'¿Quieres lavarte los dientes con el cepillo verde o con el azul?'. Dar opciones controladas devuelve la sensación de control al niño.")
        ],
        "how_valentina_works": """Valentina Castro Núñez asesora a familias para diseñar rutinas visuales personalizadas que se adapten al temperamento y necesidades de cada niño, devolviendo la paz al hogar.

Atención en Ñuñoa y Online para todo Chile, con reembolso en Isapre.""",
        "whatsapp_prompt": "¿Quieres terminar con las batallas diarias de las mañanas y noches con tus hijos? Escríbele a Valentina por WhatsApp para coordinar una sesión de orientación.",
        "faqs": [
            ("¿Las rutinas visuales sirven para niños sin diagnóstico?", "Absolutamente. Benefician a cualquier niño pequeño, y son indispensables para niños con TEA o TDAH."),
            ("¿A qué edad se pueden implementar?", "Desde los 2 años con imágenes simples, adaptándose con texto conforme crecen."),
            ("¿Las sesiones de orientación son reembolsables?", "Sí, emiten boleta electrónica oficial para Isapre.")
        ]
    },

    "comunicacion_asertiva_limites": {
        "subtitle": "Decir 'No Tengo Energía' sin Pedir Perdón ni Sentir Culpa",
        "lead_story": """Te piden un favor de último minuto en el trabajo, un amigo te invita a una salida a la que no quieres ir, o un familiar te hace un comentario incómodo sobre tu vida personal. En lugar de negarte con tranquilidad, sonríes, aceptas el favor o guardas silencio.

Luego pasas los tres días siguientes rumiando con rabia hacia el otro y hacia ti mismo/a por no haber sido capaz de frenarlo. Muchas personas confunden ser 'buenas personas' con no tener límites.""",
        "what_is_happening": """El hábito de complacer a los demás (people-pleasing) suele ser una respuesta adaptativa aprendida en la infancia o adolescencia para evitar el rechazo o el conflicto. Cuando creces sintiendo que tu pertenencia depende de ser útil y no causar molestias, decir 'no' activa una respuesta de amenaza en la amígdala similar al peligro de abandono.

Un límite saludable no es un muro ni un ataque hacia la otra persona: es una línea que delimita dónde terminas tú y dónde empieza el otro. Proteger tu tiempo y tu energía es la condición básica para mantener relaciones auténticas.""",
        "daily_scenarios": [
            ("Aceptar compromisos sociales por compromiso", "Ir a eventos estando enfermo o exhausto por miedo a que se enojen contigo."),
            ("La sobrecarga laboral silenciosa", "Asumir las tareas de compañeros que no hacen su parte porque te da vergüenza decir que no das abasto."),
            ("La necesidad de dar explicaciones eternas", "Inventar mentiras o dar justificaciones de 10 minutos para excusarte de una reunión simple."),
            ("El resentimiento acumulado", "Sentir que das todo por los demás pero que nadie cuida de ti, fruto de no haber comunicado tus límites.")
        ],
        "practical_steps": [
            ("La regla de la pausa antes de responder", "Nunca digas 'sí' de inmediato. Usa la frase comodín: 'Déjame revisar mi agenda y te confirmo más tarde'."),
            ("Límites breves y limpios", "No des explicaciones largas. Un simple 'No puedo esta vez, pero gracias por considerarme' es completo y asertivo."),
            ("Tolera la incomodidad inicial", "Decir que no generará un momento de tensión interna; recuérdate que esa incomodidad es el precio de tu libertad y salud mental.")
        ],
        "how_valentina_works": """Valentina Castro Núñez te acompaña a desarmar el miedo al rechazo, fortalecer tu autoestima y desarrollar una comunicación asertiva tranquila y segura.

Sesiones en Ñuñoa y Online para todo Chile, con reembolso en Isapre.""",
        "whatsapp_prompt": "¿Sientes que te cuesta decir 'no' y terminas asumiendo cargas ajenas que te agotan? Escríbele a Valentina por WhatsApp para coordinar tu primera sesión.",
        "faqs": [
            ("¿Poner límites me alejará de mis amigos?", "Alejará a quienes se beneficiaban de tu falta de límites, pero profundizará y sanará los vínculos reales."),
            ("¿Cómo poner límites a familiares invasivos?", "En terapia practicamos frases concretas y graduadas para cuidar la relación sin ceder en tu bienestar."),
            ("¿Las sesiones se reembolsan en Isapre?", "Sí, emiten boleta electrónica válida para todas las Isapres.")
        ]
    },

    "tdah_rechazo_rsd": {
        "subtitle": "Disforia Sensible al Rechazo (RSD): Por Qué una Crítica Duele Tanto",
        "lead_story": """Un correo de tu jefatura que dice simplemente 'veámonos mañana a primera hora'. Un mensaje de tu pareja sin emojis. Un amigo que no te responde un WhatsApp en todo el día. Para una persona promedio puede ser algo menor; para alguien con TDAH, puede detonar una angustia física real en el pecho, ganas de llorar y una certeza devastadora de que 'hice todo mal' o 'ya no me quieren'.

Esto tiene una base neurobiológica identificada: se llama Disforia Sensible al Rechazo (RSD por sus siglas en inglés).""",
        "what_is_happening": """La RSD es una respuesta de dolor emocional extremo ante la percepción real o imaginada de rechazo, crítica o fracaso. La palabra 'disforia' proviene del griego y significa literalmente 'difícil de soportar'.

Estudios neurocientíficos demuestran que en personas con TDAH la corteza cingulada anterior y la ínsula —las áreas cerebrales que procesan el dolor físico— se activan con una intensidad desproporcionada ante señales de desaprobación social. No es inmadurez ni exageración: para el cerebro con TDAH, el rechazo social duele con la misma fuerza que una quemadura en la piel.""",
        "daily_scenarios": [
            ("El perfeccionismo paralizante para no fallar", "Trabajar con niveles extremos de estrés solo para asegurarte de que nadie tenga nada que criticarte."),
            ("El aislamiento preventivo", "Dejar de postular a trabajos, no acercarte a personas que te gustan o no opinar en reuniones por terror al rechazo."),
            ("La reacción defensiva o ira súbita", "Sentir que un comentario constructivo es un ataque directo a tu dignidad, reaccionando a la defensiva antes de tiempo."),
            ("La rumiación destructiva", "Pasar noches enteras repasando una mirada o un comentario ambiguo buscando confirmar si te odian.")
        ],
        "practical_steps": [
            ("Ponerle nombre a la experiencia (RSD)", "Cuando sientas la ola de dolor en el pecho, di para ti mismo: 'Esto es RSD hablando, es una respuesta neuroquímica temporal, no una verdad objetiva'."),
            ("La regla de las 24 horas antes de responder", "Nunca envíes un mensaje de confrontación ni tomes decisiones de ruptura en pleno episodio de RSD."),
            ("Buscar evidencia objetiva", "Pregúntate: '¿Tengo pruebas concretas y explícitas de que esta persona me rechaza, o estoy interpretando señales ambiguas?'")
        ],
        "how_valentina_works": """Valentina Castro Núñez aborda la Disforia Sensible al Rechazo con un enfoque neuroafirmativo que valida tu sensibilidad y te enseña herramientas para regular la tormenta emocional sin destruir tus relaciones.

Atención en Ñuñoa y Online para todo Chile, con reembolso en Isapre.""",
        "whatsapp_prompt": "¿Sientes que las críticas o la frialdad de otros te provocan un dolor que te desborda? Escríbele a Valentina por WhatsApp para coordinar una primera sesión.",
        "faqs": [
            ("¿La RSD es un diagnóstico oficial separado?", "No es un trastorno independiente en el DSM-5, sino un síntoma clínico ampliamente documentado y asociado al TDAH y neurodivergencias."),
            ("¿Se puede aliviar con terapia?", "Sí, comprender el mecanismo y contar con herramientas de regulación somática reduce drásticamente el impacto y la duración de las crisis."),
            ("¿Las sesiones se reembolsan en Isapre?", "Sí, 100% reembolsables en todas las Isapres.")
        ]
    },

    "primera_consulta_nunoa": {
        "subtitle": "Atención Presencial en Santiago Oriente: Espacio Seguro y Conexión",
        "lead_story": """Aunque la atención online ha abierto fronteras en todo Chile, para muchas personas nada reemplaza la calidez de entrar a una consulta tranquila, mirar a los ojos a tu psicóloga y sentir la contención física de un espacio pensado exclusivamente para el bienestar emocional.

Nuestra consulta presencial en la comuna de Ñuñoa (Santiago Oriente) fue diseñada como un refugio de calma frente al ruido y el ajetreo urbano.""",
        "what_is_happening": """La presencia física compartida favorece la corregulación autónoma a través de micro-expresiones faciales, modulación del tono de voz y postura corporal. Para muchas personas que conviven con familiares, hijos pequeños o teletrabajo en casas con poca privacidad, salir físicamente de su hogar representa el único momento de la semana donde pueden hablar con libertad total.

Nuestra ubicación en Ñuñoa cuenta con excelente conectividad a pasos de estaciones de Metro y ejes principales de Santiago Oriente (Plaza Egaña, Avenida Ossa, Irarrázaval), facilitando el acceso desde La Reina, Providencia, Las Condes y Peñalolén.""",
        "daily_scenarios": [
            ("Privacidad total fuera del hogar", "Un espacio neutral donde no tienes miedo a que tus hijos, tu pareja o compañeros de departamento escuchen tus conversaciones."),
            ("Entorno con bajo impacto sensorial", "Iluminación cálida, ausencia de ruidos estridentes y mobiliario cómodo que invita a la relajación muscular."),
            ("Terapia infantil lúdica", "Un espacio acondicionado con materiales de juego simbólico y expresión artística para niños y adolescentes."),
            ("Cercanía en Santiago Oriente", "Fácil acceso en transporte público o vehículo con estacionamientos cercanos.")
        ],
        "practical_steps": [
            ("Coordina tu hora con anticipación", "Los cupos presenciales en Ñuñoa son limitados; agenda con antelación para asegurar tu horario fijo semanal."),
            ("Llega 5 minutos antes", "Tómate un momento en la sala de espera para desconectar del trayecto y entrar a la sesión con serenidad."),
            ("Boleta electrónica inmediata", "Emitida al finalizar para que la ingreses a tu Isapre ese mismo día.")
        ],
        "how_valentina_works": """Valentina Castro Núñez atiende de forma personalizada en su consulta de Ñuñoa, brindando un espacio profesional, empático y estrictamente confidencial.

Arancel de $45.000 CLP reembolsable en todas las Isapres y seguros.""",
        "whatsapp_prompt": "¿Prefieres la cercanía y privacidad de una sesión presencial en Ñuñoa? Escríbenos a WhatsApp para consultar cupos presenciales disponibles.",
        "faqs": [
            ("¿Dónde queda exactamente la consulta?", "En el sector de Plaza Egaña / Ñuñoa, a pasos de la estación de Metro de las Líneas 4 y 3."),
            ("¿Hay estacionamiento disponible?", "Sí, en las inmediaciones del edificio existen facilidades de estacionamiento."),
            ("¿Las sesiones presenciales se reembolsan igual que las online?", "Sí, exactamente con el mismo porcentaje en todas las Isapres.")
        ]
    },

    "terapia_infantil_juego": {
        "subtitle": "El Juego Simbólico como Herramienta Clínica Rigurosa",
        "lead_story": """Muchos papás y mamás llegan a la primera consulta con una duda comprensible: '¿Si traigo a mi hijo al psicólogo, solo va a venir a jugar? ¿Cómo le va a servir eso para resolver sus problemas en el colegio o sus desbordes?'.

Esperar que un niño de 5 o 8 años se siente en un sillón a hablar de sus angustias de forma abstracta es desconocer la mente infantil. Para un niño, el juego no es un pasatiempo: es su lenguaje natural de procesamiento emocional más riguroso y profundo.""",
        "what_is_happening": """El desarrollo cerebral infantil procesa las experiencias complejas a través de la metáfora y la proyección lúdica. Cuando un niño juega a que un monstruo destruye una casa o que un animalito se queda solo en el bosque, está ensayando la resolución de conflictos emocionales reales que no puede poner en palabras formales.

En la terapia infantil basada en el juego, la psicóloga clínica no es una espectadora pasiva: interviene a través del juego para facilitar la integración emocional, modelar estrategias de resolución y ayudar al niño a transitar vivencias difíciles en un entorno de seguridad controlada.""",
        "daily_scenarios": [
            ("Expresión de miedos y angustias", "Niños que a través de figuras o dibujos muestran temores al abandono, frustración escolar o celos de hermanos."),
            ("Desarrollo de tolerancia a la frustración", "Juegos de reglas adaptados donde ensaya perder sin colapsar y aprender a regular el impulso."),
            ("Procesamiento de cambios familiares", "Separaciones de padres, duelos o traslados escolares elaborados a través de historias simbólicas."),
            ("Alianza de confianza", "El niño no siente que va a un médico que lo evalúa, sino a un espacio cálido donde es aceptado y comprendido.")
        ],
        "practical_steps": [
            ("Explícale a tu hijo qué es la terapia con naturalidad", "'Vamos a ir donde Valentina, una persona que ayuda a los niños y a las familias a jugar y conversar para sentirse mejor'."),
            ("No interrogues a la salida", "Evita preguntarle '¿qué le contaste a la psicóloga?'. Respeta la privacidad de su espacio de juego terapéutico."),
            ("Participa activamente en las orientaciones parentales", "Gran parte del éxito radica en las herramientas que los padres aplican en casa tras las sesiones.")
        ],
        "how_valentina_works": """Valentina Castro Núñez cuenta con formación en psicología infanto-juvenil y abordaje lúdico. La terapia con niños menores de 12 años se realiza de manera presencial en nuestra consulta de Ñuñoa para garantizar el vínculo y el trabajo lúdico directo, con sesiones complementarias de orientación a padres (presencial u online).

Boletas reembolsables en todas las Isapres y seguros.""",
        "whatsapp_prompt": "¿Buscas un espacio clínico cálido y respetuoso para acompañar a tu hijo/a? Escríbele a Valentina por WhatsApp para coordinar una primera evaluación.",
        "faqs": [
            ("¿Por qué la terapia infantil no se realiza de forma online?", "En la infancia, el juego, el contacto corporal, la regulación sensorial y el uso de juguetes terapéuticos requieren la presencia física en la sala clínica. Para familias fuera de Santiago, ofrecemos Orientación Online a Padres."),
            ("¿A qué edad se utiliza la terapia a través del juego?", "Principalmente entre los 3 y 11 años, adaptando los materiales conforme a la etapa del desarrollo."),
            ("¿Cada cuánto tiempo se reúnen con los padres?", "Habitualmente cada 3 o 4 sesiones del niño se realiza una sesión exclusiva de orientación a padres.")
        ]
    },

    "ansiedad_somatica_cuerpo": {
        "subtitle": "Bruxismo, Opresión y Colon Irritable: Cuando el Cuerpo Habla",
        "lead_story": """Vas al médico por dolores de cabeza frecuentes, vas al gastroenterólogo por colon irritable y al dentista por bruxismo severo. Te hacen exámenes de sangre, ecografías y resonancias, y todos los resultados dicen lo mismo: 'Todo está normal, usted no tiene nada físico, debe ser estrés'.

Pero el dolor en tu cuello y el nudo en tu estómago son reales. No te los estás inventando. Tu cuerpo está gritando lo que tu mente intenta contener a la fuerza.""",
        "what_is_happening": """La somatización no es un invento mental: es la respuesta biológica del sistema nervioso autónomo cuando las demandas de estrés, trauma o sobreexigencia superan la capacidad de procesamiento consciente.

El eje intestino-cerebro está conectado directamente por el nervio vago y por millones de neuronas entéricas que producen el 90% de la serotonina del cuerpo. Cuando vives en alerta crónica, la sangre se desvía de los órganos digestivos hacia los músculos esqueléticos, provocando espasmos digestivos, reflujo y tensión miofascial permanente. Tratarla solo con analgésicos apaga la alarma sin desactivar el fuego.""",
        "daily_scenarios": [
            ("El despertar con mandíbula adolorida", "Apretar los dientes durante la noche como manifestación de tensiones no resueltas durante el día."),
            ("Crisis digestivas en días de reuniones importantes", "Cólicos estomacales o diarreas súbitas ante situaciones de exposición social o laboral."),
            ("Dolor crónico de espalda y trapecios", "Cargar los hombros hacia arriba todo el día en una postura defensiva inconsciente."),
            ("Fatiga que no cede con el sueño", "Despertar tan cansado como al acostarte debido a la hiperactividad del sistema simpático nocturno.")
        ],
        "practical_steps": [
            ("Escaneo corporal de descarga", "3 veces al día suelta la mandíbula (separa los labios), baja los hombros y afloja el abdomen conscientemente."),
            ("Calor local en el plexo solar y cuello", "Aplica guateros de semillas o duchas tibias para relajar las fibras nerviosas contraídas."),
            ("Terapia psicológica integrativa", "Trabaja en sesión para identificar qué emociones, exigencias o duelos no procesados están sosteniendo la tensión física.")
        ],
        "how_valentina_works": """Valentina Castro Núñez utiliza un enfoque integrativo que conecta cuerpo y mente, combinando técnicas somáticas de autorregulación con psicoterapia humanista profunda.

Atención en Ñuñoa y Online para todo Chile, reembolsable en Isapres.""",
        "whatsapp_prompt": "¿Sientes que la ansiedad se apoderó de tu cuerpo y los médicos te dicen que 'es solo estrés'? Escríbele a Valentina por WhatsApp para iniciar tu proceso.",
        "faqs": [
            ("¿La psicoterapia puede aliviar síntomas físicos reales?", "Sí, al regular el sistema nervioso autónomo y desactivar el estado de alarma crónica, las somatizaciones disminuyen notablemente."),
            ("¿Debo dejar mis controles médicos?", "No, la terapia psicológica actúa de forma complementaria e interdisciplinaria con tus tratamientos médicos."),
            ("¿Las sesiones se reembolsan en Isapre?", "Sí, emitimos boleta electrónica oficial válida para todas las Isapres.")
        ]
    },

    "isapre_licencia_boletas": {
        "subtitle": "Aspectos Legales, Glosas Correctas y Derechos del Paciente",
        "lead_story": """Navegar por la burocracia de las Isapres y las aseguradoras en Chile puede sentirse como un laberinto confuso. Glosas complejas, plazos estrictos y dudas sobre qué cubre o no cubre la póliza hacen que muchas personas pierdan dinero que por derecho les pertenece.

Contar con información clara y boletas correctamente emitidas es el primer paso para acceder a la salud mental sin fricciones ni trabas administrativas.""",
        "what_is_happening": """La Ley de Isapres y la normativa de la Superintendencia de Salud establecen que las prestaciones de psicología clínica emitidas por profesionales con título habilitado y registro en el Registro Nacional de Prestadores Individuales (SIS) tienen derecho a bonificación en los planes de libre elección.

Las boletas de honorarios deben incluir: nombre completo del paciente, RUT, glosa de 'Consulta de Psicología Clínica', fecha de atención, arancel y el número de registro del profesional. En Centro Paz emitimos boletas estandarizadas que cumplen con el 100% de los requisitos legales para evitar cualquier rechazo.""",
        "daily_scenarios": [
            ("Boleta emitida el mismo día", "Sin esperas de días para recibir tu comprobante; se envía directo a tu correo o WhatsApp tras la sesión."),
            ("Claridad sobre licencias médicas", "Los psicólogos clínicos no emiten licencias médicas directamente (facultad reservada a médicos y psiquiatras), pero emitimos informes clínicos de respaldo si tu psiquiatra los solicita."),
            ("Seguimiento de topes anuales", "Conocer cuántas sesiones bonifica tu plan al año para maximizar tu beneficio."),
            ("Cobertura en seguros colectivos", "Presentación de liquidaciones para liquidar copagos pendientes.")
        ],
        "practical_steps": [
            ("Revisa tu plan de salud una vez al año", "Fíjate en el porcentaje de bonificación en psicología de libre elección y en el tope por evento."),
            ("Conserva tus boletas en una carpeta digital", "Guarda el PDF de la boleta y el comprobante de transferencia de la Isapre para tu declaración de renta o seguro."),
            ("Consulta en Centro Paz ante cualquier duda", "Te orientamos sobre las glosas y requisitos específicos que te pida tu aseguradora.")
        ],
        "how_valentina_works": """Valentina Castro Núñez mantiene su registro SIS permanentemente actualizado y emite boletas electrónicas oficiales compatibles con Colmena, Banmédica, CruzBlanca, Consalud, Vida Tres y Nueva Masvida.

Atención en Ñuñoa y Online para todo Chile.""",
        "whatsapp_prompt": "¿Tienes dudas sobre cómo tramitar las boletas de tu Isapre o seguro? Escríbenos a WhatsApp y te orientamos con total claridad.",
        "faqs": [
            ("¿Un psicólogo puede dar licencia médica en Chile?", "No. Por ley chilena las licencias médicas son emitidas por médicos cirujanos o psiquiatras. Sin embargo, entregamos informes de tratamiento para respaldar la licencia de tu médico tratante."),
            ("¿Qué pasa si mi Isapre rechaza una boleta?", "En Centro Paz emitimos boletas con todas las formalidades del SII y la SIS; en caso de cualquier observación de la Isapre, te apoyamos de inmediato."),
            ("¿Las boletas sirven para la devolución de impuestos del SII?", "Las boletas de honorarios médicas y de salud pueden presentarse para deducciones y reembolsos según la normativa tributaria vigente.")
        ]
    },

    "desconexion_tecnologica_tdah": {
        "subtitle": "La Trampa del Doomscrolling, Dopamina Rápida y Fricción Positiva",
        "lead_story": """Te sientas en el sillón a las 22:00 hrs diciendo 'voy a ver 5 minutos Instagram o TikTok y me voy a dormir'. Cuando levantas la vista, son las 01:30 de la madrugada. Te duelen los ojos, tienes la mente acelerada y te invade una culpa tremenda por no haber descansado.

Te prometes que mañana no lo harás, pero al día siguiente el bucle se repite. La sociedad lo llama 'adicción a las pantallas' o 'falta de autocontrol'. La neurobiología explica que para un cerebro con TDAH, soltar el teléfono se siente literalmente como un abismo de subestimulación física.""",
        "what_is_happening": """Las aplicaciones de redes sociales están diseñadas algorítmicamente mediante refuerzo intermitente variable: cada scroll es como jalar la palanca de una máquina tragamonedas en busca de un video interesante. Para un cerebro con déficit basal de dopamina, esto es un festín neuroquímico de bajo costo energético.

Cuando intentas cerrar la aplicación, tu cerebro experimenta una caída dopaminérgica súbita: el mundo real (lavarse los dientes, irse a la cama, ordenar) se siente insoportablemente plano y aburrido. Intentar desconectarte a pura fuerza de voluntad rara vez funciona; la clave está en introducir fricción física y transiciones de baja fricción.""",
        "daily_scenarios": [
            ("El scrolling en la cama al despertar", "Pasar 45 minutos atrapado en el teléfono antes de poder levantarte de la cama."),
            ("El consumo compulsivo de contenido de salud mental", "Ver 50 videos sobre TDAH en TikTok en vez de aplicar una sola estrategia en tu vida real."),
            ("La multitarea digital agotadora", "Tener 40 pestañas abiertas en el navegador y 3 aplicaciones funcionando a la vez sin terminar nada."),
            ("La desconexión del cuerpo", "Pasar horas en la misma postura incómoda con dolor de cuello por no registrar las señales corporales.")
        ],
        "practical_steps": [
            ("Crea fricción física para la noche", "Carga el teléfono fuera de tu dormitorio y compra un despertador tradicional de $5.000 CLP."),
            ("El puente de transición de baja fricción", "No saltes del teléfono a intentar dormir en silencio. Pasa primero por un paso intermedio: un podcast en audio sin pantalla, música suave o ducha tibia."),
            ("Pantalla en escala de grises", "Activa el modo blanco y negro en los ajustes de accesibilidad de tu teléfono: reduce el atractivo visual en más del 70%.")
        ],
        "how_valentina_works": """Valentina Castro Núñez trabaja con personas neurodivergentes para desarmar la culpa del uso de pantallas y construir hábitos de higiene digital adaptados al funcionamiento del TDAH.

Atención en Ñuñoa y Online para todo Chile, con reembolso en Isapre.""",
        "whatsapp_prompt": "¿Sientes que el celular te roba horas de vida y energía cada día? Escríbele a Valentina por WhatsApp para coordinar estrategias de gestión de energía.",
        "faqs": [
            ("¿Debo eliminar todas mis redes sociales?", "No es necesario ni realista para la mayoría; el objetivo es recuperar el control y usarlas de manera consciente."),
            ("¿Por qué a las personas con TDAH les cuesta tanto apagar las pantallas?", "Por la búsqueda constante de dopamina y la dificultad biológica para alternar el foco atencional (transiciones ejecutivas)."),
            ("¿Las sesiones se reembolsan en Isapre?", "Sí, emiten boleta electrónica oficial para todas las Isapres.")
        ]
    },

    "padres_regulacion_propia": {
        "subtitle": "No Puedes Regular a tu Hijo si tu Sistema está en Alarma",
        "lead_story": """Tu hijo empieza a llorar o a negarse a colaborar y notas cómo tu pulso se acelera instantáneamente, tu mandíbula se tensa y sientes que vas a explotar. Respiras hondo, intentas usar la 'voz tranquila' que leíste en un libro de crianza, pero por dentro estás hirviendo. A los dos minutos terminas gritando.

El mayor secreto de la crianza respetuosa es que **no puedes prestar una calma que tú no tienes**. No se puede corregular a un niño desde un sistema nervioso adulto que está en modo supervivencia.""",
        "what_is_happening": """Los niños poseen neuronas espejo y un sistema de neurocepción (escaneo inconsciente de peligro o seguridad) extremadamente afinado. Si tú estás tenso/a, tu hijo capta tu respiración corta, la rigidez de tus hombros y la micro-tensión de tu rostro. Su cerebro interpreta que hay peligro y se desregula aún más.

Muchas veces, el llanto del niño activa en el adulto heridas de su propia infancia: recuerdos inconscientes de haber sido castigado, ignorado o censurado cuando lloraba. Por eso la rabieta del hijo no solo molesta: detona una alarma arcaica en el padre o la madre.""",
        "daily_scenarios": [
            ("La mecha corta después de un día estresante", "Explotar por un vaso de leche derramado porque tu propia capacidad de contención estaba colapsada."),
            ("Sentir que el niño te 'provoca a propósito'", "Interpretar la conducta desregulada del niño como un ataque personal contra ti."),
            ("La sensación de soledad en la crianza", "Sentir que cargas con todo el peso emocional del hogar sin tener a quién acudir."),
            ("El pánico a equivocarte", "Sobre-exigirte tanto ser el padre o madre perfecto que vives en constante ansiedad.")
        ],
        "practical_steps": [
            ("Pausa de seguridad para el adulto", "Si sientes que vas a gritar, di en voz alta: 'Mamá/Papá necesita calmarse' y aléjate 2 pasos antes de responder."),
            ("Revisa tus señales físicas de alerta", "Identifica dónde sientes la rabia primero: en el estómago, en los puños o en la garganta, y suelta esa zona."),
            ("Ten un espacio terapéutico propio", "Tener 50 minutos semanales para vaciar tu propia sobrecarga emocional es la inversión más potente para tu familia.")
        ],
        "how_valentina_works": """Valentina Castro Núñez acompaña a padres y madres a sanar su propia relación con la frustración, reconectar con la compasión y ejercer una crianza consciente y tranquila.

Sesiones en Ñuñoa y Online para todo Chile, reembolsables en Isapre.""",
        "whatsapp_prompt": "¿Sientes que estás al borde del colapso en la crianza y necesitas recuperar tu propia calma? Escríbele a Valentina por WhatsApp para coordinar orientación.",
        "faqs": [
            ("¿Tengo que hacer terapia personal o de crianza?", "En Centro Paz integramos ambas dimensiones: cuidamos de ti como persona para que puedas cuidar de tu familia con serenidad."),
            ("¿Es normal sentir rabia hacia mi hijo a veces?", "Es una emoción humana muy frecuente ante el agotamiento crónico; lo importante es no actuarla y aprender a gestionarla."),
            ("¿Las sesiones se reembolsan en Isapre?", "Sí, emiten boleta electrónica oficial para todas las Isapres.")
        ]
    },

    "autocuidado_fin_de_semana": {
        "subtitle": "Descanso Pasivo vs Descanso Sensorial: Cómo Reponer Energía",
        "lead_story": """Llega el sábado por la mañana. Pasaste toda la semana deseando que llegara el fin de semana para descansar. Te quedas en la cama mirando series en maratón, pides comida a domicilio y revisas el teléfono durante horas. Llega el domingo por la noche y te sientes tan o más cansado/a que el viernes, con una pesadez inexplicable en el cuerpo.

Esto ocurre porque confundiste el 'descanso pasivo' con el verdadero **Descanso Sensorial y Restaurativo**.""",
        "what_is_happening": """La inactividad física no equivale a descanso neurológico. Estar acostado mientras tus ojos procesan la luz azul de una pantalla y tu mente absorbe información constante mantiene a la corteza cerebral y al sistema dopaminérgico en trabajo continuo.

Para recuperarse de la fatiga crónica y el estrés del trabajo o la neurodivergencia, se requieren distintas formas de descanso identificadas por la medicina integrativa: descanso sensorial (silencio, oscuridad), descanso emocional (dejar de complacer), descanso social (estar solo o con personas seguras) y descanso creativo (conectar con la naturaleza o el arte sin metas).""",
        "daily_scenarios": [
            ("La resaca de pantalla del domingo", "Estar 8 horas frente al televisor o celular y terminar con dolor de ojos y culpa por no haber descansado."),
            ("Compromisos sociales por obligación", "Llenar el fin de semana de cumpleaños o asados cuando tu sistema nervioso necesitaba silencio absoluto."),
            ("La angustia del domingo por la tarde", "Sentir que el fin de semana se esfumó sin haber recuperado la energía para la semana entrante."),
            ("Incapacidad para desconectar del trabajo", "Revisar correos o mensajes laborales durante el fin de semana por ansiedad.")
        ],
        "practical_steps": [
            ("Media jornada de ayuno digital", "Pasa el sábado en la mañana o la tarde con el teléfono en modo avión: sal a caminar a un parque o lee un libro físico."),
            ("Contacto con la naturaleza", "Caminar entre árboles o pisar pasto descalzo reduce el cortisol y equilibra el sistema autónomo de forma comprobada."),
            ("Programa el 'no hacer nada' en tu calendario", "Agenda bloques de tiempo libre sin actividades planificadas como un compromiso sagrado contigo mismo/a.")
        ],
        "how_valentina_works": """Valentina Castro Núñez te ayuda a diseñar un estilo de vida sustentable que respete tus necesidades biológicas de recuperación, previniendo el burnout antes de que ocurra.

Sesiones en Ñuñoa y Online para todo Chile, reembolsables en Isapres.""",
        "whatsapp_prompt": "¿Sientes que tus fines de semana no alcanzan para recuperar tu energía vital? Escríbele a Valentina por WhatsApp para iniciar tu proceso terapéutico.",
        "faqs": [
            ("¿Cuánto tiempo de descanso sensorial se necesita?", "Incluso 30 a 60 minutos diarios de baja estimulación marcan una diferencia medible en los niveles de cortisol."),
            ("¿El descanso sensorial sirve para personas con TDAH?", "Es fundamental: sus cerebros están hiperconectados y necesitan espacios protegidos de descompresión."),
            ("¿Las sesiones se reembolsan en Isapre?", "Sí, emiten boleta electrónica oficial para todas las Isapres.")
        ]
    }
}

CLINICAL_ARTICLES.update(CLINICAL_ARTICLES_EXTENDED)
