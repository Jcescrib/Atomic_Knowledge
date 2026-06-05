# -*- coding: utf-8 -*-
"""Ingest The Code (libro 6 Jocko) — Section Three: THE PROTOCOLS."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/the-code/the-code.md"
ORIGIN = "Jocko Willink, Dave Berke & Sarah Armstrong — The Code. The Evaluation. The Protocols. (2020)"
D = "2026-06-05"
B = "desarrollo-personal"

akus = [
    {"id": "aku-caer-del-path-es-inevitable-lo-decisivo-es-volver-claim", "class": "claim",
     "statement": (
        "Caer de The Path es inevitable y le pasa a todo el mundo —a veces por uno mismo, "
        "a veces por algo imprevisto (enfermedad, accidente, hechos fuera de control)—; lo "
        "que importa no es la caída sino tu reacción: la situación no dicta lo que te pasa, "
        "tú dictas la situación, así que haces una autoevaluación implacable del porqué, "
        "identificas medidas correctoras y las ejecutas sin piedad para volver al Path "
        "ahora."),
     "origin": ORIGIN, "domain": [B, "jocko", "the-path", "resiliencia", "ownership"],
     "sources": [SRC], "created": D, "updated": D,
     "rel": {"related": ["aku-the-path-concept", "aku-eqh-no-es-estado-sino-camino-sin-fin-claim",
                          "aku-good-mindset-concept", "aku-extreme-ownership-concept"]}},

    {"id": "aku-paso-pequeno-reevaluar-ante-incertidumbre-method", "class": "method",
     "statement": (
        "Cuando no sabes qué hacer (algo malo pasó y ni sabes por dónde empezar), el "
        "procedimiento es: da un paso atrás y detach, respira y evalúa todo lo que ocurre; "
        "piensa qué decisiones podrías tomar ahora mismo y sus probables resultados; "
        "escríbelo (qué es el éxito aquí, cómo llegar, cuánto debería tardar, quién puede "
        "aconsejarte); luego da un paso pequeño —no gigante— hacia la mejor decisión, "
        "pausa, reevalúa y repite presionando hasta el punto de fricción, donde surge una "
        "oportunidad nueva o la necesidad de replegarte y reevaluar."),
     "origin": ORIGIN, "domain": [B, "jocko", "toma-de-decisiones", "incertidumbre", "maniobra"],
     "sources": [SRC], "created": D, "updated": D,
     "rel": {"related": ["aku-detach-tactico-estrategico-concept",
                          "aku-prioritize-and-execute-concept"]}},

    {"id": "aku-buscar-ayuda-profesional-sin-que-el-ego-lo-impida-claim", "class": "claim",
     "statement": (
        "Para cualquier cosa que afecte la salud de tu mente o tu cuerpo (adicción, "
        "trauma, enfermedad grave) hay que buscar ayuda profesional ahora, no apoyarse en "
        "un amigo o familiar; y no se debe dejar que el ego impida pedir esa ayuda: "
        "negarse a buscarla por orgullo agrava el problema."),
     "origin": ORIGIN, "domain": [B, "jocko", "salud", "ayuda-profesional", "ego"],
     "sources": [SRC], "created": D, "updated": D,
     "rel": {"related": ["aku-el-ego-mas-dificil-es-el-propio-claim",
                          "aku-humildad-asumir-errores-claim"]}},

    {"id": "aku-tras-el-exito-agradecer-tomar-stock-ir-mas-duro-claim", "class": "claim",
     "statement": (
        "Cuando el éxito llega en The Path, lo correcto no es detenerse: agradece a quienes "
        "te ayudaron, haz balance de lo logrado y luego ve más duro; lidera —a tu familia, "
        "tu comunidad, tu país— y guía a otros hacia The Path, mostrándoles The Way, porque "
        "no hay punto final."),
     "origin": ORIGIN, "domain": [B, "jocko", "exito", "liderazgo", "the-path"],
     "sources": [SRC], "created": D, "updated": D,
     "rel": {"related": ["aku-the-path-concept",
                          "aku-power-of-relationships-liderazgo-concept"]}},
]


def proto(idn, title, topic, when, whennot, justified, body):
    return {"id": idn, "taku_type": "protocol", "subdir": "protocols", "title": title,
            "origin": ORIGIN, "domain": [B, "jocko", "protocolo", topic],
            "when_to_use": when, "when_not_to_use": whennot,
            "aku_links": {"justified_by": justified}, "created": D, "updated": D, "body": body}


def pbody(purpose, trigger, resources, steps, decisions, exitc, failure, review):
    s = "## Purpose\n\n" + purpose + "\n\n"
    s += "## Trigger Conditions\n\n" + trigger + "\n\n"
    s += "## Required Resources\n\n" + resources + "\n\n"
    s += "## Protocol Steps\n\n" + steps + "\n\n"
    s += "## Decision Points\n\n" + decisions + "\n\n"
    s += "## Exit Conditions\n\n" + exitc + "\n\n"
    s += "## Failure Handling\n\n" + failure + "\n\n"
    s += "## Review Trigger\n\n" + review
    return s


takus = [
    proto("taku-protocolo-ruptura", "Protocolo: ruptura de pareja", "relaciones",
          "Cuando una relación de pareja ha terminado y no sabes qué hacer.",
          "Como excusa para vengarte o humillar a la otra persona, o para racionalizar volver con quien ha demostrado no ser de fiar.",
          ["aku-detach-tactico-estrategico-concept",
           "aku-caer-del-path-es-inevitable-lo-decisivo-es-volver-claim",
           "aku-good-mindset-concept"],
          pbody(
            "Recuperarte de una ruptura sin que las emociones te lleven a malas decisiones, y volver a The Path.",
            "Tu relación de pareja se ha roto.",
            "Un lugar privado para descargar emociones; actividad física (saco, correr); papel para reflexionar.",
            "1. Detach: tus emociones son tu enemigo; mira la situación desde fuera. Si cuesta, ve al paso 1.a.\n"
            "   a. Saca las emociones sin afectar la situación: grita, llora o exértate físicamente (saco, correr).\n"
            "   b. Repite 1.a. según necesites.\n"
            "2. Evalúa quién es realmente esa persona: no era quien creías; lo ha demostrado con sus actos. No te aferres a lo que fue ni a lo que pudo ser.\n"
            "3. Sé agradecido: la mentira se descubrió ahora y no más tarde; ya puedes avanzar.\n"
            "4. Deséale suerte: la va a necesitar. Sin rencor; que te recuerden como alguien maduro.\n"
            "5. Aléjate y sigue adelante.\n"
            "6. No mires atrás: tu mente te engañará («quizá funcione»); no va a cambiar. Cuanto más vuelves, más te rebajas.\n"
            "7. Vuelve a The Path: madruga, entrena, lee, escribe, come limpio, ordena tu espacio, progresa en el trabajo; aprende de los errores y red flags que pasaste por alto y busca a alguien de fiar sin cargar con lastre.",
            "¿Consigues detach (paso 1) o necesitas descargar emociones primero (1.a)? ¿Hay tentación de volver? → no mirar atrás (paso 6).",
            "Has dejado de mirar atrás, has extraído las lecciones y estás de vuelta en The Path con hábitos diarios.",
            "Si la mente te arrastra a volver o a la amargura, repite el detach (1.a) y reancla en los hábitos del paso 7.",
            "Revisa al sentir recaída emocional o tentación de volver a contactar."),
          ),
    proto("taku-protocolo-duelo-muerte", "Protocolo: duelo por la muerte de un ser querido", "duelo",
          "Cuando alguien a quien amabas ha muerto y no sabes cómo afrontar la pérdida.",
          "Para reprimir por completo el duelo o para hacerlo todo sobre ti mismo ignorando a los demás afectados.",
          ["aku-incluso-en-la-muerte-hay-good-claim",
           "aku-detach-tactico-estrategico-concept",
           "aku-caer-del-path-es-inevitable-lo-decisivo-es-volver-claim"],
          pbody(
            "Procesar la pérdida de un ser querido honrando su memoria y volviendo a vivir plenamente.",
            "Una persona amada ha fallecido.",
            "Papel para una eulogía y una carta; tiempo para visitar la tumba.",
            "1. Acepta que la muerte es cruel y no siempre justa, pero inescapable y parte de la vida.\n"
            "2. Recuerda todo lo que esa persona te dio: experiencias, su carácter, su mirada del mundo.\n"
            "3. Escribe una eulogía con esos recuerdos, la pronuncies o no.\n"
            "4. No seas egoísta: otros también sufren; apoya a la familia. Sé fuerte.\n"
            "5. Acepta que perderás el control de tus emociones a oleadas; déjalas salir cuando sea apropiado. Con el tiempo serán menos intensas y frecuentes; no es que te importe menos, es que vas procesando.\n"
            "6. Reconoce la suerte de haber tenido a esa persona; te enseñó lo preciosa que es la vida.\n"
            "7. Escribe una carta al difunto: qué significó, qué te enseñó, disculpas pendientes; promete vivir la mejor vida posible y hacerle sentir orgulloso.\n"
            "8. Lleva la carta a su tumba, ponla junto a la lápida, despídete y ve a vivir.\n"
            "9. Cada año, en su cumpleaños o aniversario, visita la tumba, léela en alto y evalúa si cumples la promesa.",
            "¿Las oleadas de emoción son apropiadas de soltar ahora? ¿Estás haciéndolo sobre ti o apoyando a los demás (paso 4)?",
            "Has honrado a la persona (eulogía/carta), aceptado la pérdida y retomado tu vida con la promesa de vivirla bien.",
            "Si la pena te paraliza o se vuelve patológica, busca ayuda profesional; mantén los rituales de los pasos 7-9.",
            "Revisa cada año en el aniversario; evalúa si cumples la promesa de vivir la mejor vida posible."),
          ),
    proto("taku-protocolo-problemas-de-dinero", "Protocolo: problemas de dinero", "finanzas",
          "Cuando el dinero está apretado (pérdida de empleo, gasto médico inesperado, emergencia familiar).",
          "Como sustituto de ayuda profesional financiera en situaciones de insolvencia grave, o para ocultar la situación a la familia.",
          ["aku-disciplina-se-extiende-a-todo-claim",
           "aku-prioritize-and-execute-concept",
           "aku-caer-del-path-es-inevitable-lo-decisivo-es-volver-claim"],
          pbody(
            "Recuperar la libertad financiera mediante disciplina y un presupuesto, saliendo del agujero con la familia como equipo.",
            "Ingresos insuficientes o gasto imprevisto que tensiona las finanzas.",
            "Un presupuesto de ingresos y gastos; registro de gastos pasados; educación financiera básica.",
            "1. La libertad financiera exige disciplina financiera, que empieza por trazar todas tus actividades financieras: haz un presupuesto de ingresos y gastos; sabe a dónde va tu dinero.\n"
            "2. Revisa el gasto pasado para reducir o eliminar; si no registras gastos, empieza ahora; edúcate en planificación y ahorro.\n"
            "3. Toma decisiones agresivas e inmediatas: vende lo innecesario, cancela servicios no esenciales (consola, cable), come más en casa, gimnasio en el garaje; aplaza ropa, vacaciones y coche nuevo.\n"
            "4. Sigue minimizando la carga: renegocia intereses con el banco, paga primero la deuda más cara y evita deuda nueva; busca un segundo empleo o un puesto mejor pagado; maximiza ingresos y minimiza gastos.\n"
            "5. No mantengas a la familia en la oscuridad: que sea un esfuerzo de equipo; explica que el presupuesto no es castigo sino la herramienta para la libertad financiera.\n"
            "6. Revisa el presupuesto cada mes, compara real vs presupuestado y ajusta.",
            "¿Qué gastos son eliminables ya (paso 3)? ¿Qué deuda tiene mayor interés (paso 4)? ¿Implicas a la familia (paso 5)?",
            "Ingresos y gastos bajo control, deuda en reducción y presupuesto mensual en marcha con la familia alineada.",
            "Si la deuda no cede pese a la disciplina, busca asesoría financiera profesional; mantén el ciclo mensual del paso 6.",
            "Revisión mensual obligatoria: real vs presupuesto, y ajuste."),
          ),
    proto("taku-protocolo-traicion-confianza", "Protocolo: traición de confianza", "relaciones",
          "Cuando alguien te ha traicionado y no sabes qué hacer.",
          "Para estallar emocionalmente, actuar sin pruebas o dejar que el traidor controle tus emociones.",
          ["aku-detach-tactico-estrategico-concept",
           "aku-no-sobrerreaccionar-mantener-la-calma-claim",
           "aku-responder-no-reaccionar-da-control-claim"],
          pbody(
            "Responder a una traición con control emocional, pruebas y profesionalidad, sin entregar el control de tus emociones al otro.",
            "Alguien ha traicionado tu confianza.",
            "Capacidad de detach; evidencia; en su caso, la cadena de mando.",
            "1. Reconoce que has aprendido algo del carácter de esa persona: ahora sabes mejor con quién tratas y debes estar alerta.\n"
            "2. Si es laboral y hay vidas en riesgo o algo moral/ético/ilegal, confronta de inmediato y escala por la cadena de mando.\n"
            "3. Asegúrate de tener evidencia y no actúes a medio cocer: los engañosos se preparan para defenderse y no les importa quién salga dañado; obsérvalos con cuidado.\n"
            "4. Si la traición personal es grave, detach mentalmente, evalúa cómo desvincularte y distánciate.\n"
            "5. Si es menor (quizá ni merece llamarse traición), regístrala internamente: esa persona no es de fiar. Mantén la desconfianza interna.\n"
            "6. Eres profesional y emocionalmente estable: sé diplomático y con tacto; que las maniobras del otro no te alteren ni controlen tus emociones.",
            "¿Hay riesgo para vidas o ilegalidad? → escalar (paso 2). ¿Es traición grave o menor? → desvincularte (4) o registrar (5).",
            "Has asegurado evidencia, escalado si correspondía y mantenido el control emocional y profesional.",
            "Si la ira te domina, vuelve al detach (paso 4/6) antes de actuar; no actúes sin pruebas.",
            "Revisa si reaparecen patrones de la persona o si surge nueva evidencia."),
          ),
    proto("taku-protocolo-problemas-en-el-trabajo", "Protocolo: todo se derrumba en el trabajo", "trabajo",
          "Cuando todo parece venirse abajo a la vez en el trabajo y no sabes qué hacer.",
          "Para rendirse, culpar a otros o descargar el estrés en la familia sin un plan.",
          ["aku-prioritize-and-execute-concept", "aku-the-warpath-concept",
           "aku-good-mindset-concept", "aku-extreme-ownership-concept"],
          pbody(
            "Afrontar una avalancha de problemas laborales priorizando, ejecutando y dejando que la adversidad te fortalezca.",
            "Múltiples problemas laborales se acumulan y se siente la derrota.",
            "Una lista de problemas priorizada; comunicación con familia, jefe y compañeros.",
            "1. Reconoce que a veces la vida funciona así: los problemas se compactan y es fácil sentirse vencido.\n"
            "2. No te rindas: haz lo contrario, pelea más duro, ve a la warpath. Empieza por una ley fundamental del liderazgo de combate: PRIORITIZE AND EXECUTE.\n"
            "3. Haz una lista: ¿cuál es el mayor problema?, ¿qué causa más estrés?, ¿afecta tu vida en casa?\n"
            "4. En casa: tu familia ha notado tu tensión; explícales el plan; si trabajarás más horas, que lo sepan y planifiquen cómo ayudar.\n"
            "5. En el trabajo: habla con tu jefe, dale la cara; di que vas a dar un paso al frente (llegar pronto, comer trabajando, quedarte tarde) y que estás 100% comprometido con la empresa y la misión.\n"
            "6. Con un compañero: ten una conversación profesional; nadie lee tu mente; toma ownership y escucha tu parte con mente abierta; acordad qué haréis ambos para mejorar.\n"
            "7. Será duro porque la vida es dura; ponte de pie y enfréntalos en fila; deja que el reto te eleve y te haga más fuerte.\n"
            "8. Deja que la adversidad de hoy te convierta en mejor persona mañana: «Gracias — me hiciste mejor».",
            "¿Cuál es la prioridad #1 ahora (paso 2-3)? ¿Quién debe estar informado: familia, jefe, compañero (4-6)?",
            "Problemas priorizados y en ejecución, stakeholders alineados y actitud de warpath restablecida.",
            "Si te paraliza el volumen, vuelve a PRIORITIZE AND EXECUTE (un problema cada vez); toma ownership en vez de culpar.",
            "Revisa al cerrar cada problema prioritario o si reaparece la sensación de derrota."),
          ),
    proto("taku-protocolo-disculpa", "Protocolo: disculpa", "relaciones",
          "Cuando dijiste o hiciste algo que hirió a alguien y necesitas repararlo.",
          "Para medias disculpas con tono de cumplir el trámite, sacar a relucir agravios pasados o disculparte en mal momento/lugar.",
          ["aku-humildad-asumir-errores-claim", "aku-extreme-ownership-concept",
           "aku-el-ego-mas-dificil-es-el-propio-claim"],
          pbody(
            "Reparar una relación dañada asumiendo la responsabilidad con humildad y sinceridad.",
            "Heriste a alguien con tus palabras o actos.",
            "Tiempo y lugar adecuados; reflexión previa sobre qué decir.",
            "1. Toma ownership: eres responsable de tus palabras y actos; a veces basta un «lo siento» sincero, a veces hay que pedir perdón.\n"
            "2. Si disculparte te incomoda, reflexiona por qué: ¿hiriste a esa persona?, ¿cuánto te importa?, ¿es tu ego el que te lo impide?, ¿te falta humildad para reconocer que te equivocaste?\n"
            "3. Encuentra el lugar y momento adecuados (ni de noche cansados ni en público); piensa y ensaya qué decir; sé auténtico pero prepárate.\n"
            "4. Evita medias disculpas con tono de trámite; no saques agravios pasados; céntrate en esa situación.\n"
            "5. Si tus hijos presenciaron la pelea, hazles saber que te equivocaste y pediste perdón: disculparse es señal de fuerza, no de debilidad.\n"
            "6. Contrólate en el futuro: el objetivo es mantener el control de palabras y actos para preservar tus relaciones; si lo perdiste, el camino de vuelta empieza en ti.",
            "¿Es tu ego lo que te frena (paso 2)? ¿Es el lugar/momento adecuado (paso 3)?",
            "Has pedido perdón con sinceridad, sin medias tintas, y asumido la responsabilidad.",
            "Si la disculpa se enfría en excusa, vuelve al paso 1 (ownership) y al 4 (sin medias disculpas).",
            "Revisa si vuelves a perder el control de palabras/actos con esa persona."),
          ),
    proto("taku-protocolo-accidente-enfermedad", "Protocolo: accidente o enfermedad grave", "salud",
          "Cuando debes seguir adelante tras un accidente o un diagnóstico médico severo.",
          "Como sustituto del tratamiento médico profesional, o para enfrentar la batalla en solitario sin apoyo.",
          ["aku-good-mindset-concept",
           "aku-buscar-ayuda-profesional-sin-que-el-ego-lo-impida-claim",
           "aku-prioritize-and-execute-concept"],
          pbody(
            "Afrontar un accidente o enfermedad grave como una guerra larga que se puede ganar, con plan, apoyo y disciplina.",
            "Diagnóstico grave (cáncer, lesiones serias) o accidente que cambia tus circunstancias.",
            "Médicos, familia, amigos y recursos; un counterpart de confianza; un sistema para tracking de papeleo, citas y facturas.",
            "1. La pelea no ha terminado: acaba de empezar. Aparta lo que no apunte a vencer el diagnóstico o adaptarte; puede llevar años.\n"
            "2. Estás vivo ahora: es hora de pelear; prepárate para la guerra larga.\n"
            "3. Primer movimiento: pide ayuda; reúne las herramientas (médicos, familia, amigos, recursos); construye un plan y ejecútalo con disciplina y fe.\n"
            "4. Necesitas un counterpart de confianza que haga preguntas duras y dé respuestas francas a ti, a tus médicos y a tu familia; su cualidad clave es decir la verdad y, cuanto más a tu lado, mejor.\n"
            "5. Organízate: papeleo, citas, recetas, facturas y mil detalles; trackéalos con un sistema y úsalo.\n"
            "6. Habla con tu trabajo: explica la situación, pide ayuda, usa sus recursos.\n"
            "7. Vas a necesitar ayuda y te la ofrecerán; úsala, pero que una persona lidere el equipo de apoyo para que la logística no te desborde.\n"
            "8. Sabe que puedes ganar y salir más fuerte: ahora conoces la oscuridad y aprecias la luz.\n"
            "9. Céntrate en vencer; pase lo que pase, sabrás que diste todo por luchar y ganar, y eso ya es una victoria.",
            "¿Quién es tu counterpart (paso 4) y quién lidera el equipo de apoyo (paso 7)? ¿Qué recursos profesionales activas (paso 3/6)?",
            "Tienes plan, equipo de apoyo organizado y sistema de tracking, peleando con disciplina.",
            "Si la logística o el ánimo te desbordan, delega el liderazgo del apoyo (paso 7) y reancla en el plan (paso 3).",
            "Revisa al cambiar el diagnóstico/tratamiento o si el sistema de tracking se desorganiza."),
          ),
    proto("taku-protocolo-adiccion", "Protocolo: adicción", "salud",
          "Cuando algo externo (sustancia, actividad) te controla y no sabes cómo romperlo.",
          "Como sustituto de la ayuda profesional cuando esta es necesaria, o para culpar a otros de la adicción.",
          ["aku-buscar-ayuda-profesional-sin-que-el-ego-lo-impida-claim",
           "aku-extreme-ownership-concept", "aku-disciplina-se-extiende-a-todo-claim",
           "aku-caer-del-path-es-inevitable-lo-decisivo-es-volver-claim"],
          pbody(
            "Romper una adicción tomando responsabilidad total, con plan disciplinado y, si hace falta, ayuda profesional.",
            "Una sustancia o actividad te controla y empeora tu vida.",
            "Ayuda profesional si es necesaria; papel para el análisis coste/beneficio; un entorno y personas que apoyen.",
            "Nota: tratar la adicción puede requerir ayuda profesional; si es el caso, búscala ya y no dejes que el ego lo impida.\n\n"
            "1. Admite que algo externo te controla, empeora tu vida y te impide alcanzar tu potencial.\n"
            "2. No culpes a otros ni te asumas víctima: toma responsabilidad total de la situación.\n"
            "3. Escribe todo lo malo que viene de esto: coste financiero, emocional, mental, físico y el impacto en tus relaciones.\n"
            "4. Escribe todo lo bueno que viene de ello.\n"
            "5. Escribe el resultado a largo plazo de mantener la adicción y cómo afectará a tu vida y a los demás.\n"
            "6. Construye un plan para parar; es algo que puedes controlar, pero quizá necesites ayuda profesional: no la subestimes.\n"
            "7. Domina el plan: comprométete con los pasos y sé disciplinado cada día.\n"
            "8. Sepárate de la adicción: evita a quienes la facilitan; rodéate de quienes quieren verte ganar.\n"
            "9. Cuando llegue el impulso, discipline con ejercicio, lectura, escritura o lo que sea que evite recaer.\n"
            "10. Si recaes, vuelve a The Path.\n"
            "11. Haz lo necesario: sabes la respuesta y qué hacer; controlas el 100% de tus actos.",
            "¿Requiere ayuda profesional (nota/paso 6)? ¿Quiénes facilitan vs apoyan (paso 8)?",
            "Tienes un plan disciplinado en marcha, entorno de apoyo y mecanismos para el impulso; recaídas gestionadas volviendo al Path.",
            "Si recaes, no te declares víctima: vuelve a The Path (paso 10) y refuerza el entorno de apoyo (paso 8); escala a profesional si no cede.",
            "Revisa ante cada impulso fuerte o recaída, y al cambiar tu entorno."),
          ),
    proto("taku-protocolo-trauma", "Protocolo: trauma psicológico", "salud",
          "Cuando has sufrido un trauma psicológico y no sabes cómo afrontarlo.",
          "Como sustituto de la ayuda profesional cuando esta es necesaria, o para anestesiar el dolor con alcohol/drogas.",
          ["aku-buscar-ayuda-profesional-sin-que-el-ego-lo-impida-claim",
           "aku-good-mindset-concept", "aku-extreme-ownership-concept"],
          pbody(
            "Procesar un trauma sin negarlo ni anestesiarlo, encontrando la fuerza y la luz a través de la oscuridad.",
            "Un evento serio ha tenido un impacto psicológico real en tu vida.",
            "Ayuda profesional si es necesaria; papel para el análisis; una rutina disciplinada; personas de apoyo.",
            "Nota: tratar el trauma puede requerir ayuda profesional; si es el caso, búscala ya y no dejes que el ego lo impida.\n\n"
            "1. Acepta que te afectó un evento serio con impacto psicológico real.\n"
            "2. No te asumas víctima: la situación es difícil, pero controlas cómo respondes.\n"
            "3. Escribe todo lo malo que vino del trauma: impacto físico, mental y emocional; reconoce dónde estás por lo ocurrido.\n"
            "4. Escribe todo lo bueno que vino de ello:\n"
            "   a. ¿Te hace apreciar lo que tenías?\n"
            "   b. ¿Te hace ver que pudo ser peor?\n"
            "   c. ¿Ves que otros han soportado algo peor?\n"
            "   d. ¿Te ha mostrado la resiliencia y fuerza que llevas dentro?\n"
            "5. Evita conductas contraproducentes: no bebas, no te drogues, no busques anestesiar el dolor.\n"
            "6. Construye un horario disciplinado: madruga y entrena, come sano, trabaja duro, pasa tiempo de calidad con los tuyos.\n"
            "7. Cuando sientas que no te entienden, tienes razón, no lo entienden.\n"
            "8. Está bien, porque tú sí lo entiendes; no evites la oscuridad ni la ignores.\n"
            "9. Conoces la oscuridad y, por eso, conoces la luz.\n"
            "10. Ponte en marcha hacia la luz: busca alegría, risa, sol, ejercicio y naturaleza.\n"
            "11. No dejes que el trauma te venza ni te quite eso; avanza cada día.\n"
            "12. Vence el trauma viviendo tu vida.",
            "¿Requiere ayuda profesional (nota)? ¿Qué conductas contraproducentes debes cortar (paso 5)?",
            "Has aceptado el trauma sin victimismo, mantienes rutina disciplinada y avanzas hacia la luz viviendo tu vida.",
            "Si recurres a anestesiar el dolor (paso 5) o te paralizas, escala a ayuda profesional y reancla en la rutina (paso 6).",
            "Revisa al aparecer conductas de evitación/anestesia o recaídas en el ánimo."),
          ),
    proto("taku-protocolo-lo-desconocido", "Protocolo: lo desconocido (qué hacer cuando no sabes qué hacer)", "toma-de-decisiones",
          "Cuando algo malo ha pasado y no sabes siquiera por dónde empezar; el protocolo de estrategia para lo no contemplado.",
          "Para grandes saltos precipitados sin información, o para quedarse paralizado sin dar ningún paso.",
          ["aku-paso-pequeno-reevaluar-ante-incertidumbre-method",
           "aku-detach-tactico-estrategico-concept",
           "aku-prioritize-and-execute-concept"],
          pbody(
            "Actuar con buen juicio ante lo desconocido mediante detach, pasos pequeños y reevaluación hasta el punto de fricción.",
            "Algo malo ha ocurrido y no sabes por dónde empezar; ningún protocolo específico aplica.",
            "Capacidad de detach; papel para definir éxito y plan; posibles asesores.",
            "1. Da un paso atrás. Detach. Respira y mira alrededor; evalúa todo lo que ocurre.\n"
            "2. Piensa qué posibilidades tienes y qué decisiones podrías tomar AHORA, y sus probables resultados.\n"
            "3. Escríbelo: ¿qué es el éxito aquí?, ¿cómo llegar?, ¿cuánto debería tardar?, ¿quién puede aconsejarte?\n"
            "4. Trabaja el plan: actúa avanzando; no te quedes estancado ni le des vueltas. Da un paso pequeño —no gigante, porque no sabes exactamente qué ocurre— que te permita volver a evaluar antes de decidir el siguiente.\n"
            "5. Empuja, pausa y reevalúa; repite presionando hasta el punto de fricción, donde ves una oportunidad nueva o la necesidad de replegarte y reevaluar.\n"
            "6. Date margen de maniobra: cuando se ponga duro, no te rindas ni abandones; entonces no has fracasado: solo necesitas reagruparte y reatacar. Has aprendido, ganado experiencia y SIGUES VIVO.",
            "¿El paso es lo bastante pequeño para reevaluar (paso 4)? ¿Has llegado al punto de fricción: oportunidad o repliegue (paso 5)?",
            "Has pasado de la parálisis a un avance iterativo con reevaluación continua hacia un éxito definido.",
            "Si te paralizas o saltas demasiado lejos, vuelve al paso 1 (detach) y reduce el tamaño del paso (paso 4).",
            "Revisa en cada punto de fricción y cuando cambien las condiciones."),
          ),
]

written, cross = akugen.generate(akus, takus, ROOT)
print("WRITTEN:")
for w in written:
    print("  ", os.path.relpath(w, ROOT))

# same-author dedup target that receives the-code as added source
ADD_SOURCE = {"aku-good-mindset-concept"}
ops_by_id = {}
for new_id, field, inv, tgt in cross:
    op = ops_by_id.setdefault(tgt, {"id": tgt, "add_rel": []})
    op["add_rel"].append((inv, new_id))
for tgt in ADD_SOURCE:
    op = ops_by_id.setdefault(tgt, {"id": tgt})
    op["add_source"] = SRC
    op["updated"] = D

akupatch.apply(ROOT, list(ops_by_id.values()))
print("\nPATCHED EXISTING (aku-aku related inverses + source):")
for k, v in ops_by_id.items():
    print("  ", k, "| rel:", v.get("add_rel", []), "| src" if v.get("add_source") else "")
print("\nCROSS (new aku -> existing aku) count:", len(cross))
print("NOTE: TAKU justified_by -> existing AKU es unidireccional (sin inverso en AKU).")
