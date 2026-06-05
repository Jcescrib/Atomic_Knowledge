# -*- coding: utf-8 -*-
"""Almanack of Naval — Meditation(rest) + Choosing to Build Yourself + Choosing to Grow
Yourself. Solo items NUEVOS."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/naval/almanack-of-naval-ravikant/almanack-of-naval-ravikant.md"
ORIGIN = "Naval Ravikant — The Almanack of Naval Ravikant (ed. Eric Jorgenson, 2020)"
D = "2026-06-05"
N = "naval"

def c(idn, cls, st, dom, rel=None):
    return {"id": idn, "class": cls, "statement": st, "origin": ORIGIN,
            "domain": dom, "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    # ── Meditation (rest) ──
    c("aku-meditar-60-min-60-dias-para-llegar-a-un-inbox-cero-mental-method", "method",
      "Para limpiar la mente, medita una hora cada mañana durante unos sesenta días sin "
      "resistir tus pensamientos: las experiencias no resueltas (como percebes pegados desde "
      "la infancia) van burbujeando una a una como un buzón de correos atrasados y, al "
      "observarlas con la distancia de un adulto, se resuelven solas; con el tiempo llegas a un "
      "«inbox cero» mental, un estado de dicha y paz. Solo sentarse y no hacer nada: si vienen "
      "pensamientos, ni los combates ni los abrazas.",
      [N, "meditacion", "practica"],
      {"related": ["aku-choiceless-awareness-acepta-sin-juzgar-y-el-90-por-ciento-de-pensamientos-son-miedo-concept"]}),
    c("aku-la-atraccion-de-las-drogas-y-los-thrills-es-espiritual-claim", "claim",
      "La atracción de las drogas (y de los thrills, los flow states o los orgasmos) es "
      "espiritual: la gente los busca para controlar su estado mental y, sobre todo, para salir "
      "de su propia cabeza, escapando de la voz interior y del sentido del yo sobredesarrollado.",
      [N, "mente", "ego"]),
    c("aku-la-meditacion-revela-cuan-fuera-de-control-esta-tu-mente-y-en-la-separacion-hay-liberacion-claim", "claim",
      "La ventaja de la meditación no es ganar el superpoder de controlar tu estado interno, "
      "sino reconocer cuán fuera de control está tu mente (un mono lanzando heces, "
      "incontrolable); solo al ver a esa criatura en acción sientes rechazo y empiezas a "
      "separarte de ella, y en esa separación está la liberación: la sola consciencia ya te "
      "calma.",
      [N, "meditacion", "consciencia"]),
    c("aku-awareness-vs-ego-eres-mas-que-tu-monkey-mind-concept", "concept",
      "La consciencia (awareness) puede entenderse como un OS multicapa: un kernel de awareness "
      "siempre calmo, pacífico y contento, sobre el que corren aplicaciones como la «monkey "
      "mind» (siempre preocupada, asustada y ansiosa); incluye no activar la monkey mind hasta "
      "que se necesita, para no malgastar energía ni dejar que se convierta en ti; implica que "
      "eres más que tu mente, tus hábitos y tus preferencias: eres un nivel de consciencia y un "
      "cuerpo.",
      [N, "consciencia", "ego"]),
    c("aku-la-mente-es-un-musculo-que-puedes-reprogramar-con-consciencia-claim", "claim",
      "La mente es un músculo que puede entrenarse y condicionarse: la sociedad la ha "
      "condicionado de forma azarosa para estar fuera de tu control, pero si la observas con "
      "consciencia e intención (un trabajo de cada momento) puedes desempaquetar tus "
      "emociones, pensamientos y reacciones y reescribir el programa hacia lo que quieres, "
      "incluido elegir tus estados de ánimo.",
      [N, "mente", "reprogramacion"],
      {"related": ["aku-descondicionate-revisa-si-tus-habitos-aun-te-sirven-claim"]}),
    c("aku-meditacion-es-apagar-a-la-sociedad-y-escucharte-y-adopta-muchas-formas-claim", "claim",
      "Meditar es apagar a la sociedad y escucharte a ti mismo, y solo «funciona» cuando se "
      "hace por su propio bien; adopta muchas formas: caminar (hiking) es meditación andando, "
      "el journaling es meditación escribiendo, rezar es meditación de gratitud, ducharse es "
      "meditación accidental y sentarse en silencio es meditación directa.",
      [N, "meditacion"]),
    # ── Choosing to Build Yourself ──
    c("aku-el-mayor-superpoder-es-la-capacidad-de-cambiarte-a-ti-mismo-claim", "claim",
      "El mayor superpoder es la capacidad de cambiarte a ti mismo: el entorno actual programa "
      "el cerebro, pero un cerebro hábil puede elegir su próximo entorno y, con ello, "
      "reescribirse.",
      [N, "cambio", "autotransformacion"]),
    c("aku-actua-sin-ira-y-con-vision-a-largo-plazo-y-dejaran-de-ser-errores-claim", "claim",
      "Si haces las mismas cosas correctas pero con menos emoción e ira y con un punto de vista "
      "a muy largo plazo, dejan de ser errores: la ira y las emociones son una consecuencia "
      "enorme e innecesaria; lo que la mayoría lamentaría de su pasado no es lo que hizo, sino "
      "la angustia con que lo hizo.",
      [N, "emociones", "largo-plazo"]),
    c("aku-te-conviertes-en-tus-habitos-y-cambiarlos-es-un-viaje-de-anos-claim", "claim",
      "Te conviertes en tus hábitos: de adultos somos una colección de miles de hábitos "
      "corriendo en subconsciente, con solo un poco de neocórtex para problemas nuevos; por eso "
      "nada sostenible se logra en tres meses —ponerse en forma o cambiarse es un viaje de unos "
      "diez años, rompiendo malos hábitos y adoptando buenos cada seis meses—.",
      [N, "habitos", "cambio"],
      {"related": ["aku-descondicionate-revisa-si-tus-habitos-aun-te-sirven-claim"]}),
    c("aku-para-tener-paz-mental-primero-hay-que-tener-paz-del-cuerpo-claim", "claim",
      "Para tener paz mental, primero hay que tener paz del cuerpo: un entrenamiento físico "
      "ligero pero diario produce una transformación astonishing tanto física como mental, lo "
      "que revela que el estado del cuerpo condiciona el de la mente.",
      ["salud", N, "cuerpo-mente"]),
    c("aku-cuando-de-verdad-quieres-cambiar-cambias-intentar-es-aplazar-claim", "claim",
      "Cuando de verdad quieres cambiar, simplemente cambias; decir «voy a intentar» formar un "
      "hábito es escaquearse y darse un margen, porque cuando tus emociones quieren algo, lo "
      "haces sin más (Krishnamurti: estar en revolución interna permanente); al menos sé "
      "honesto y reconoce cuándo no estás listo.",
      [N, "cambio", "honestidad"]),
    c("aku-comprometete-externamente-para-cambiar-o-fija-una-meta-menor-honesta-method", "method",
      "Para cambiar una conducta, comprométete externamente ante suficiente gente (p. ej. di a "
      "todos «he dejado de fumar, doy mi palabra»); si no estás listo para ese compromiso "
      "total, sé honesto y fija una meta menor pero real a la que sí puedas comprometerte "
      "externamente durante tres o seis meses, y luego da el siguiente paso, en lugar de "
      "machacarte.",
      [N, "cambio", "compromiso"]),
    c("aku-impaciencia-con-las-acciones-paciencia-con-los-resultados-claim", "claim",
      "Impaciencia con las acciones, paciencia con los resultados: haz cuanto antes y con plena "
      "atención lo que tengas que hacer (la inspiración es perecedera: actúa en el instante en "
      "que la tienes), pero sé paciente con los resultados, porque los sistemas complejos y las "
      "personas tardan en adoptar y madurar.",
      [N, "accion", "paciencia"]),
    # ── Choosing to Grow Yourself ──
    c("aku-sistemas-no-metas-disena-tu-entorno-para-tener-exito-concept", "concept",
      "Conviene montar sistemas, no metas (Scott Adams): en vez de objetivos específicos, usa "
      "tu juicio para identificar los entornos en los que prosperas y crea a tu alrededor un "
      "entorno que te haga estadísticamente probable tener éxito; incluye buscar ser la versión "
      "más exitosa de ti mismo trabajando lo menos posible y fallando en muy pocos sitios "
      "(éxito en 999 de 1.000 vidas); implica que el cerebro hábil elige su entorno futuro.",
      [N, "sistemas", "entorno"],
      {"related": ["aku-hacerse-rico-sin-suerte-es-ser-determinista-claim"]}),
    c("aku-si-hay-algo-que-quieres-hacer-luego-hazlo-ahora-no-hay-luego-claim", "claim",
      "Si hay algo que quieres hacer «más tarde», hazlo ahora: no hay «más tarde», tu vida se "
      "escapa y no quieres gastarla esperando ni haciendo cosas que no son parte de tu misión.",
      [N, "accion", "presente"],
      {"related": ["aku-empezar-aqui-y-ahora-method"]}),
    c("aku-ciencia-es-el-estudio-de-la-verdad-y-las-matematicas-su-lenguaje-concept", "concept",
      "La ciencia es el estudio de la verdad y la única disciplina verdadera, porque hace "
      "predicciones falsables y cambia el mundo (la ciencia aplicada se vuelve tecnología); "
      "incluye que las matemáticas son el lenguaje de la ciencia y de la naturaleza; implica "
      "que estudiar las leyes del universo puede vivirse como el acto más devocional y "
      "espiritual, dando un sentido de asombro y de pequeñez del yo.",
      [N, "ciencia", "matematicas"],
      {"related": ["aku-falsabilidad-sin-predicciones-falsables-no-es-ciencia-concept"]}),
    c("aku-casi-todo-lo-que-se-lee-busca-aprobacion-social-los-retornos-estan-fuera-del-rebano-claim", "claim",
      "Casi todo lo que la gente lee hoy está diseñado para la aprobación social (leen cien "
      "libros sobre evolución pero no a Darwin, tratados de economía pero no a Adam Smith): "
      "leer lo que lee el rebaño te hace pensar como el rebaño, pero los retornos de la vida "
      "están fuera del rebaño, así que hace falta contrarianismo para aprender lo que te "
      "interesa al margen del resultado social.",
      [N, "lectura", "contrarian"]),
    c("aku-los-mas-exitosos-empezaron-como-losers-fuera-del-rebano-claim", "claim",
      "Las personas más listas y exitosas suelen haber empezado como «losers»: quien se ve "
      "expulsado de la sociedad normal y sin rol en ella hace lo suyo y es mucho más probable "
      "que encuentre un camino ganador; ayuda partir de «nunca seré popular ni aceptado, así "
      "que tengo que ser feliz siendo yo».",
      [N, "exito", "contrarian"]),
    c("aku-para-mejorar-sin-autodisciplina-actualiza-tu-autoimagen-claim", "claim",
      "Para la automejora sin depender de la autodisciplina, actualiza tu autoimagen: cuando "
      "cambias quién crees que eres, la conducta nueva deja de requerir fuerza de voluntad "
      "porque pasa a ser simplemente «quien eres ahora».",
      [N, "autoimagen", "cambio"],
      {"related": ["aku-metodo-de-cambio-de-habitos-la-autodisciplina-es-un-puente-a-una-nueva-autoimagen-method"]}),
    c("aku-la-motivacion-es-relativa-encuentra-la-cosa-en-la-que-te-metes-claim", "claim",
      "La motivación es relativa: todo el mundo está motivado para algo —incluso los que "
      "llamamos desmotivados se motivan muchísimo jugando a videojuegos—, así que en lugar de "
      "forzar disciplina conviene encontrar la cosa en la que de verdad te metes.",
      [N, "motivacion", "vocacion"]),
    c("aku-lega-a-tus-hijos-leer-matematicas-y-persuasion-claim", "claim",
      "Las habilidades fundacionales que conviene legar (a hijos o a uno mismo) son tres: "
      "leer (todo, por su propio bien, sin la noción de «basura»), las matemáticas (lenguaje "
      "de la naturaleza, base de dinero, ciencia, economía y computación) y la persuasión "
      "(influir en otros para lograr cosas, y es aprendible).",
      [N, "aprendizaje", "habilidades-fundacionales"]),
]

written, cross = akugen.generate(akus, [], ROOT)
print("WRITTEN:", len(written))
for w in written: print("  ", os.path.relpath(w, ROOT))
ops_by_id = {}
for new_id, field, inv, tgt in cross:
    ops_by_id.setdefault(tgt, {"id": tgt, "add_rel": []})["add_rel"].append((inv, new_id))
akupatch.apply(ROOT, list(ops_by_id.values()))
print("\nPATCHED:", list(ops_by_id.keys()))
print("CROSS count:", len(cross))
