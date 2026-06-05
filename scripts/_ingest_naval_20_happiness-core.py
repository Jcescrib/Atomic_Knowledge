# -*- coding: utf-8 -*-
"""Almanack of Naval — Part II Happiness core (Happiness Is Learned rest, Is a Choice,
Requires Presence/Peace, Every Desire Is a Chosen Unhappiness, Success Does Not Earn
Happiness, Envy Is the Enemy). Solo items NUEVOS."""
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

F = "felicidad"
akus = [
    c("aku-el-estado-neutral-es-un-estado-de-perfeccion-como-el-de-los-ninos-claim", "claim",
      "El estado neutral que queda al eliminar la sensación de que falta algo no es soso sino "
      "un estado de perfección: es el que viven los niños pequeños, inmersos en el entorno y el "
      "momento sin pensar en cómo deberían ser las cosas según sus preferencias; se puede ser "
      "muy feliz mientras no te enredes demasiado en tu propia cabeza.",
      [F, N, "presente"],
      {"related": ["aku-felicidad-es-el-estado-por-defecto-cuando-no-falta-nada-concept"]}),
    c("aku-nosotros-somos-maleables-y-el-mundo-es-en-gran-parte-fijo-claim", "claim",
      "Solemos creernos fijos y al mundo maleable, cuando en realidad somos nosotros los "
      "maleables y el mundo es en gran parte fijo: por eso la palanca de la felicidad está en "
      "cambiarnos a nosotros (la interpretación, los deseos), no el entorno.",
      [F, N, "aceptacion"]),
    c("aku-la-felicidad-real-es-un-subproducto-de-la-paz-via-aceptacion-claim", "claim",
      "La felicidad real solo llega como subproducto de la paz, y esta procede sobre todo de "
      "la aceptación, no de cambiar tu entorno externo; meditar ayuda, pero asombrosamente "
      "poco cuando llega el momento real de sufrimiento.",
      [F, N, "paz", "aceptacion"]),
    c("aku-se-encuentra-paz-cultivando-indiferencia-a-lo-que-no-controlas-claim", "claim",
      "Una persona racional encuentra la paz cultivando la indiferencia hacia las cosas que "
      "están fuera de su control: aceptar lo que no depende de ti elimina una fuente enorme de "
      "perturbación.",
      [F, N, "paz", "control"]),
    c("aku-mejora-metodica-de-tu-baseline-de-felicidad-method", "method",
      "Puedes subir lenta pero metódicamente tu baseline de felicidad, igual que tu forma "
      "física, mediante prácticas deliberadas: bajar la identidad, bajar el parloteo mental, "
      "dejar de preocuparte por lo que no importa, no meterte en política, no rodearte de gente "
      "infeliz, valorar tu tiempo, leer filosofía, meditar y rodearte de gente feliz.",
      [F, N, "habitos", "practica"]),
    c("aku-memoria-e-identidad-son-cargas-del-pasado-que-impiden-vivir-el-presente-claim", "claim",
      "La memoria y la identidad son cargas del pasado que te impiden vivir libremente en el "
      "presente: aceptamos la voz de nuestra cabeza como fuente de toda verdad y nos aceptamos "
      "tal como fuimos programados de jóvenes, cuando todo es maleable y cada día es nuevo.",
      [F, N, "identidad", "presente"],
      {"related": ["aku-el-ego-se-construye-en-las-primeras-dos-decadas-concept"]}),
    c("aku-la-felicidad-requiere-presencia-claim", "claim",
      "La felicidad requiere presencia: en cualquier momento solo un pequeño porcentaje de tu "
      "cerebro está en el presente y el resto planifica el futuro o lamenta el pasado, lo que "
      "te impide ver la belleza y sentir gratitud; vivir en delirios del futuro o comparar el "
      "pasado con el presente destruye tu felicidad.",
      [F, N, "presente"]),
    c("aku-iluminacion-es-el-espacio-entre-tus-pensamientos-concept", "concept",
      "La iluminación es el espacio entre tus pensamientos; incluye que no es algo que se logra "
      "tras treinta años en una montaña, sino algo alcanzable momento a momento y en cierto "
      "porcentaje cada día; implica que reducir el flujo de pensamientos aumenta tu presencia y "
      "tu paz.",
      [F, N, "iluminacion", "presente"]),
    c("aku-felicidad-es-paz-no-alegria-paz-en-reposo-y-felicidad-en-movimiento-concept", "concept",
      "Para Naval la felicidad es paz, no alegría: es una propiedad emergente de la paz "
      "interior y exterior; incluye que la paz es felicidad en reposo y la felicidad es paz en "
      "movimiento, convertibles a voluntad; implica que conviene buscar la paz la mayor parte "
      "del tiempo, porque entonces cualquier actividad se vuelve una actividad feliz.",
      [F, N, "paz"],
      {"related": ["aku-felicidad-es-ausencia-de-deseo-y-presencia-en-el-momento-claim"]}),
    c("aku-persona-feliz-es-la-que-interpreta-sin-perder-su-paz-innata-claim", "claim",
      "Una persona feliz no es la que está feliz todo el tiempo, sino la que interpreta sin "
      "esfuerzo los acontecimientos de modo que no pierde su paz innata.",
      [F, N, "paz", "interpretacion"]),
    c("aku-la-ansiedad-son-pensamientos-en-marcha-elige-la-paz-sobre-el-pensamiento-claim", "claim",
      "La ansiedad pervasiva de bajo nivel no es más que una serie de pensamientos en marcha "
      "(el «nexting» de saltar siempre a lo siguiente); no se combate luchando contra ella, "
      "sino notándola y preguntándote «¿prefiero tener este pensamiento o mi paz?», porque "
      "mientras tengas los pensamientos no puedes tener la paz.",
      [F, N, "ansiedad", "paz"]),
    c("aku-la-unica-paz-interior-es-abandonar-la-idea-de-problemas-claim", "claim",
      "Hoy creemos que la paz se consigue resolviendo todos los problemas externos, pero estos "
      "son ilimitados; la única forma de obtener paz interior de verdad es renunciar a la idea "
      "misma de problemas, fluyendo con la vida y aceptándola.",
      [F, N, "paz", "aceptacion"]),
    c("aku-el-deseo-es-un-contrato-para-ser-infeliz-hasta-conseguirlo-concept", "concept",
      "El deseo es un contrato que haces contigo mismo para ser infeliz hasta que consigues lo "
      "que quieres; incluye ser el eje de tu sufrimiento (el área donde has elegido ser "
      "infeliz); excluye la acción sana de autorrealizarte; implica elegir los deseos con mucho "
      "cuidado y no tener más de un gran deseo a la vez.",
      [F, N, "deseo", "sufrimiento"],
      {"related": ["aku-felicidad-es-ausencia-de-deseo-y-presencia-en-el-momento-claim"]}),
    c("aku-buscar-fuera-de-ti-la-felicidad-es-la-delusion-fundamental-claim", "claim",
      "La delusión fundamental que todos sufrimos es creer que algo externo nos hará felices y "
      "plenos para siempre («seré feliz cuando consiga X»): mirar fuera de ti para obtener "
      "felicidad permanente es delirante, aunque sí debas actuar en el mundo y "
      "autorrealizarte.",
      [F, N, "deseo", "delusion"]),
    c("aku-ten-un-solo-gran-deseo-a-la-vez-y-perfecciona-tus-deseos-claim", "claim",
      "Es más importante perfeccionar tus deseos que esforzarte en algo que no deseas al 100%: "
      "conviene tener un solo gran deseo a la vez, porque al hacer más (sobre todo de joven y "
      "sano) asumes más y más deseos que, sin darte cuenta, van destruyendo tu felicidad.",
      [F, N, "deseo", "foco"]),
    c("aku-trifecta-tiempo-salud-dinero-segun-la-edad-concept", "concept",
      "Existe una trifecta de tiempo, salud y dinero que la edad reparte de forma incompleta: "
      "de joven tienes tiempo y salud pero no dinero; de mediana edad, dinero y salud pero no "
      "tiempo; de viejo, dinero y tiempo pero no salud; implica que el reto vital es tener los "
      "tres a la vez antes de que, al darte cuenta de que tienes suficiente dinero, hayas "
      "perdido tiempo y salud.",
      [F, N, "tiempo", "salud"]),
    c("aku-puedes-lograr-casi-cualquier-cosa-si-es-una-sola-y-la-quieres-mas-que-nada-claim", "claim",
      "Puedes conseguir casi cualquier cosa que quieras de la vida, siempre que sea una sola "
      "cosa y la quieras mucho más que cualquier otra: la dispersión del deseo es lo que impide "
      "lograrlo.",
      [F, N, "deseo", "foco"]),
    c("aku-felicidad-es-satisfaccion-el-exito-viene-de-la-insatisfaccion-claim", "claim",
      "La felicidad es estar satisfecho con lo que tienes, mientras que el éxito viene de la "
      "insatisfacción: son fuerzas opuestas entre las que hay que elegir conscientemente.",
      [F, N, "exito", "satisfaccion"]),
    c("aku-todo-exito-real-es-interno-la-adaptacion-hedonica-borra-el-externo-claim", "claim",
      "Todo éxito real es interno y tiene poco que ver con las circunstancias externas: por la "
      "adaptación hedónica te acostumbras rápidamente a cualquier logro, y quienes alcanzan los "
      "éxitos materiales y sociales que perseguías no parecen más felices, lo que revela que la "
      "felicidad es interna.",
      [F, N, "exito", "adaptacion-hedonica"]),
    c("aku-los-verdaderos-ganadores-salen-del-juego-por-completo-claim", "claim",
      "Los verdaderos ganadores son los que se salen del juego por completo, los que no "
      "necesitan nada de nadie y están en paz, sanos e indiferentes a ganar más o menos que el "
      "vecino (Jerzy Gregorek, Buda, Krishnamurti); como dijo Pascal, todos los males del "
      "hombre vienen de no poder sentarse solo y en silencio en una habitación: si puedes "
      "sentarte treinta minutos y ser feliz, tienes éxito.",
      [F, N, "exito", "paz"]),
    c("aku-dominar-un-juego-con-grandes-recompensas-te-hace-seguir-jugando-de-mas-claim", "claim",
      "El problema de volverse bueno en un juego, sobre todo uno con grandes recompensas, es "
      "que sigues jugándolo mucho después de que deberías haberlo superado: el impulso de "
      "supervivencia y replicación nos sube a la cinta del trabajo y la adaptación hedónica nos "
      "mantiene en ella; el truco es saber cuándo bajarse y jugar.",
      [F, N, "exito", "hedonic-treadmill"],
      {"related": ["aku-los-ganadores-son-los-tan-adictos-que-siguen-pese-a-la-utilidad-marginal-decreciente-claim"]}),
    c("aku-elimina-el-deberia-de-tu-vida-es-culpa-y-programacion-social-claim", "claim",
      "Conviene eliminar la palabra «debería» de tu vida: cuando aparece en tu mente es culpa o "
      "programación social, y hacer algo porque «deberías» significa que en realidad no quieres "
      "hacerlo y solo te hace miserable.",
      [F, N, "valores", "programacion-social"]),
    c("aku-la-felicidad-es-un-juego-de-un-solo-jugador-concept", "concept",
      "Entrenarte para ser feliz es un juego de un solo jugador, completamente interno, sin "
      "progreso ni validación externa, en el que compites contigo mismo; incluye contrastar con "
      "los juegos multijugador competitivos que la sociedad nos programa (ganar dinero, lucir "
      "bien); implica que hemos olvidado jugar y ganar los juegos de un solo jugador y solo "
      "competimos en multijugador, siendo las expectativas sociales el enemigo de la paz "
      "mental.",
      [F, N, "juego-de-un-jugador", "programacion-social"]),
    c("aku-la-vida-es-fundamentalmente-un-juego-de-un-solo-jugador-claim", "claim",
      "La vida es, en el fondo, un juego de un solo jugador: naces solo, mueres solo, todas tus "
      "interpretaciones y recuerdos son en solitario, y en tres generaciones nadie te "
      "recordará; reconocerlo libera de la dependencia de la validación ajena.",
      [F, N, "filosofia", "juego-de-un-jugador"],
      {"related": ["aku-la-felicidad-es-un-juego-de-un-solo-jugador-concept"]}),
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
