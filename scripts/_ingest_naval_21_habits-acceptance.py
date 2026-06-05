# -*- coding: utf-8 -*-
"""Almanack of Naval — Envy(rest) + Happiness Is Built by Habits + Happiness Habits +
Changing Habits + Find Happiness in Acceptance (death). Solo items NUEVOS + 1 TAKU."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/naval/almanack-of-naval-ravikant/almanack-of-naval-ravikant.md"
ORIGIN = "Naval Ravikant — The Almanack of Naval Ravikant (ed. Eric Jorgenson, 2020)"
D = "2026-06-05"
N = "naval"
F = "felicidad"

def c(idn, cls, st, dom, rel=None):
    return {"id": idn, "class": cls, "statement": st, "origin": ORIGIN,
            "domain": dom, "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    c("aku-todos-los-marcadores-reales-son-internos-claim", "claim",
      "Todos los marcadores (scorecards) que de verdad cuentan son internos: como pregunta "
      "Buffett, ¿prefieres ser el mejor amante del mundo y que te crean el peor, o el peor y "
      "que te crean el mejor?; vivir según un marcador interno, y no la opinión ajena, es la "
      "base de la paz.",
      [F, N, "exito", "validacion"],
      {"related": ["aku-todo-exito-real-es-interno-la-adaptacion-hedonica-borra-el-externo-claim",
                   "aku-la-felicidad-es-un-juego-de-un-solo-jugador-concept"]}),
    c("aku-los-celos-son-inutiles-no-querrias-ser-otra-persona-al-100-claim", "claim",
      "Los celos son una emoción venenosa e inútil: no puedes elegir solo aspectos de la vida "
      "de otro (su cuerpo, su dinero, su personalidad), tendrías que ser esa persona al 100% "
      "con todas sus reacciones, deseos y problemas; al darte cuenta de que no querrías ese "
      "intercambio total, los celos se desvanecen porque prefieres ser tú.",
      [F, N, "celos", "aceptacion"]),
    c("aku-al-trabajar-rodeate-de-mas-exitosos-al-jugar-de-mas-felices-claim", "claim",
      "Cuando trabajas, rodéate de gente más exitosa que tú; cuando juegas, rodéate de gente "
      "más feliz que tú: el entorno tira de ti en la dimensión que cultivas en cada contexto.",
      [F, N, "entorno", "relaciones"]),
    c("aku-para-la-mente-el-placebo-es-100-efectivo-se-positivamente-inclinado-claim", "claim",
      "Cuando se trata de medicinas para la mente, el efecto placebo es 100% efectivo: como la "
      "felicidad es totalmente interna, conviene abordar las técnicas (meditación, ejercicios "
      "de presencia) con una mentalidad positivamente inclinada y no incrédula, porque creer "
      "que funcionará ayuda a que funcione.",
      [F, N, "mentalidad", "placebo"]),
    c("aku-teoria-de-los-cinco-chimpances-concept", "concept",
      "La «teoría de los cinco chimpancés» sostiene que puedes predecir el comportamiento de "
      "un chimpancé (y de una persona) por los cinco con los que más se relaciona; incluye que "
      "conviene elegir esos cinco con mucho cuidado —positivos, optimistas, de baja "
      "mantenimiento, a quienes admiras pero no envidias— y no al azar por vecindad o trabajo; "
      "implica que eres una combinación de tus hábitos y de la gente con la que pasas más "
      "tiempo.",
      [F, N, "entorno", "relaciones"]),
    c("aku-evita-las-relaciones-conflictivas-e-insostenibles-claim", "claim",
      "La primera regla para manejar el conflicto es no rodearte de gente que vive en conflicto "
      "constante: conviene evitar cualquier relación insostenible o difícil de sostener, hasta "
      "el punto de que si no te ves trabajando con alguien de por vida, no trabajes con esa "
      "persona ni un día.",
      [F, N, "relaciones", "conflicto"]),
    c("aku-deja-de-preguntar-por-que-y-empieza-a-decir-wow-gratitud-por-la-abundancia-claim", "claim",
      "«Deja de preguntar por qué y empieza a decir wow»: damos por sentado casi todo, cuando "
      "estar presente revela la inmensa abundancia y los regalos que nos rodean en todo momento "
      "(techo, ropa, comida, comunicarnos a través del espacio y el tiempo); la gratitud por lo "
      "que ya hay es una fuente directa de felicidad.",
      [F, N, "gratitud", "presente"]),
    c("aku-la-adaptacion-hedonica-es-mas-fuerte-en-lo-artificial-que-en-lo-natural-claim", "claim",
      "La adaptación hedónica es más poderosa para las cosas hechas por el hombre (coches, "
      "casas, ropa, dinero) que para las naturales (comida, sexo, ejercicio): por eso el placer "
      "de lo material se desvanece más rápido que el de lo natural.",
      [F, N, "adaptacion-hedonica", "deseo"]),
    c("aku-toda-actividad-de-pantalla-resta-felicidad-claim", "claim",
      "Sin excepciones, todas las actividades de pantalla se asocian con menos felicidad y "
      "todas las actividades sin pantalla con más felicidad: reducir tiempo de pantalla es una "
      "palanca fiable del estado de ánimo.",
      [F, N, "habitos", "pantallas"]),
    c("aku-cuantos-mas-secretos-tienes-menos-feliz-eres-claim", "claim",
      "Cuantos más secretos guardas, menos feliz eres: la carga de ocultar erosiona la paz "
      "interior, en línea con que no puedes ocultarte nada a ti mismo.",
      [F, N, "honestidad", "secretos"],
      {"related": ["aku-no-puedes-ocultarte-de-ti-mismo-tus-valores-determinan-tu-autoestima-claim"]}),
    c("aku-di-a-tus-amigos-que-eres-feliz-para-conformarte-a-ello-claim", "claim",
      "Dile a tus amigos que eres una persona feliz: el sesgo de consistencia te forzará a "
      "estar a la altura de esa etiqueta porque ellos esperarán que la cumplas, ayudándote a "
      "conformarte a ese estado.",
      [F, N, "habitos", "consistencia"]),
    c("aku-metodo-de-cambio-de-habitos-la-autodisciplina-es-un-puente-a-una-nueva-autoimagen-method", "method",
      "Para cambiar un hábito: elige una sola cosa, cultiva el deseo y visualízalo; planifica "
      "un camino sostenible; identifica necesidades, disparadores y sustitutos; díselo a tus "
      "amigos; trackea meticulosamente; entiende que la autodisciplina es un puente hacia una "
      "nueva autoimagen y, finalmente, integra esa nueva autoimagen como quien eres ahora.",
      [F, N, "habitos", "disciplina"]),
    c("aku-cinco-etapas-saber-entender-explicar-sentir-ser-concept", "concept",
      "El dominio profundo de algo atraviesa cinco etapas sucesivas: primero lo sabes, luego "
      "lo entiendes, después puedes explicarlo, más tarde puedes sentirlo y, finalmente, lo "
      "eres; implica que la integración plena de un aprendizaje (como un nuevo hábito o "
      "autoimagen) es convertirse en ello, no solo conocerlo.",
      [F, N, "aprendizaje", "maestria"]),
    c("aku-cambiar-aceptar-o-dejar-concept", "concept",
      "Ante cualquier situación siempre tienes tres opciones: cambiarla, aceptarla o dejarla; "
      "incluye que querer cambiarla es un deseo que causa sufrimiento hasta lograrlo (por eso "
      "elige pocos); excluye la peor opción —quedarse deseando cambiarla sin cambiarla, querer "
      "irse sin irse y sin aceptar—, ya que esa lucha o aversión es responsable de la mayor "
      "parte de la infelicidad; implica que la palabra clave es «acepta».",
      [F, N, "aceptacion", "decisiones"],
      {"related": ["aku-la-felicidad-real-es-un-subproducto-de-la-paz-via-aceptacion-claim",
                   "aku-el-deseo-es-un-contrato-para-ser-infeliz-hasta-conseguirlo-concept"]}),
    c("aku-abrazar-la-muerte-da-sentido-y-no-hay-legado-concept", "concept",
      "El gran hack para aceptar lo que no puedes cambiar es abrazar la muerte: reconocerla en "
      "vez de huir de ella trae gran sentido y paz; incluye que no hay legado (todo —hijos, "
      "obras, civilizaciones, planeta— será polvo) y que tu vida es el parpadeo de una "
      "luciérnaga en la noche; implica que, al aceptar la futilidad, la vida se revela como un "
      "juego divertido en el que solo importa experimentar tu realidad e interpretarla del modo "
      "más positivo posible.",
      [F, N, "muerte", "aceptacion"]),
]

takus = [
    {"id": "taku-habitos-de-felicidad-naval", "taku_type": "heuristic", "subdir": "heuristics",
     "title": "Hábitos de felicidad de Naval",
     "origin": ORIGIN, "domain": [N, F, "habitos"],
     "when_to_use": "Para subir tu baseline de felicidad de forma deliberada mediante hábitos diarios entrenables.",
     "when_not_to_use": "Como recetas universales garantizadas: la felicidad es trial-and-error y muy personal; lo que funciona para uno puede no servir a otro.",
     "aku_links": {"justified_by": [
         "aku-la-felicidad-es-una-habilidad-que-se-aprende-concept",
         "aku-mejora-metodica-de-tu-baseline-de-felicidad-method",
         "aku-felicidad-requiere-presencia-claim",
         "aku-toda-actividad-de-pantalla-resta-felicidad-claim"]},
     "created": D, "updated": D,
     "body": (
        "## The Rule\n\n"
        "Trata la felicidad como una habilidad entrenable y aplica hábitos diarios, probando "
        "por trial-and-error qué funciona para ti:\n\n"
        "- **Meditación insight**: observar cómo funciona tu mente.\n"
        "- **Reinterpretación positiva**: al pillarte juzgando, pregúntate «¿cuál es la lectura positiva de esto?».\n"
        "- **Cuestiona el deseo**: «¿esto es tan importante como para ser infeliz si no sale a mi modo?».\n"
        "- **Cuerpo**: sol en la piel, sonríe mirando arriba, entrena a diario (paz del cuerpo → paz de la mente).\n"
        "- **Quita estimulantes/dopamina barata**: deja cafeína, alcohol, azúcar; minimiza redes y videojuegos.\n"
        "- **Minimiza tres apps**: teléfono, calendario y despertador.\n"
        "- **Menos secretos**, menos pantallas, más juegos de suma positiva.\n"
        "- **Serotonina sin drogas**: sol, ejercicio, pensamiento positivo, triptófano.\n"
        "- **Declara que eres feliz** a tus amigos (sesgo de consistencia).\n"
        "- **Reset en bajón**: meditación, música y ejercicio; luego elige un nuevo rumbo para el día.\n\n"
        "## What It Replaces\n\n"
        "Sustituye la búsqueda de felicidad en circunstancias externas y la dopamina barata de "
        "pantallas por hábitos internos sostenibles.\n\n"
        "## When It Holds\n\n"
        "Cuando los practicas religiosamente hasta volverlos segunda naturaleza y priorizas la "
        "felicidad por encima de otras metas.\n\n"
        "## When It Fails\n\n"
        "Si los aplicas como dogma sin experimentar cuál te sirve, o si esperas resultados sin "
        "constancia; ningún hábito sustituye a la aceptación.\n\n"
        "## Why It Works\n\n"
        "La paz y la felicidad son habilidades condicionables; sustituir hábitos malos "
        "irreflexivos por buenos, y el entorno (cinco chimpancés) por gente feliz, eleva el "
        "baseline.\n\n"
        "## Calibration\n\n"
        "Cambia un hábito cada vez con el método de cambio de hábitos (elige uno, visualiza, "
        "trackea, díselo a amigos) y mide tu métrica personal: cuánto del día haces por "
        "obligación vs. por interés."),
    },
]

written, cross = akugen.generate(akus, takus, ROOT)
print("WRITTEN:", len(written))
for w in written: print("  ", os.path.relpath(w, ROOT))
ops_by_id = {}
for new_id, field, inv, tgt in cross:
    ops_by_id.setdefault(tgt, {"id": tgt, "add_rel": []})["add_rel"].append((inv, new_id))
akupatch.apply(ROOT, list(ops_by_id.values()))
print("\nPATCHED:", list(ops_by_id.keys()))
print("CROSS count:", len(cross))
