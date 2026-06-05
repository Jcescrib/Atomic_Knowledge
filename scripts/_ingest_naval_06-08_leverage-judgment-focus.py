# -*- coding: utf-8 -*-
"""Almanack of Naval — ch06 Find a Position of Leverage, ch07 Get Paid for Your
Judgment, ch08 Prioritize and Focus. Solo items NUEVOS (dedup vs ch01)."""
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
    # ── ch06 Find a Position of Leverage ──
    c("aku-haz-cosas-por-su-propio-bien-produce-tu-mejor-trabajo-claim", "claim",
      "Hacer las cosas por su propio bien (como el arte) produce tu mejor trabajo y, "
      "paradójicamente, también el mayor éxito y riqueza: cuanto menos deseas, obsesionas o "
      "fuerzas algo, más natural es y mejor sale, porque lo haces a tu manera y con calidad; "
      "el año en que Naval generó más riqueza fue el que menos duro trabajó haciendo cosas por "
      "diversión.",
      ["riqueza", N, "motivacion", "maestria"]),
    c("aku-sigue-tu-curiosidad-intelectual-mas-que-lo-de-moda-claim", "claim",
      "Seguir tu curiosidad intelectual genuina es mejor cimiento para una carrera que "
      "perseguir lo que da dinero ahora: el conocimiento que solo tú o pocos tienen sale de "
      "tus pasiones y hobbies, y si tu curiosidad te lleva a donde la sociedad querrá ir, te "
      "pagarán extremadamente bien.",
      ["riqueza", N, "curiosidad", "carrera"],
      {"related": ["aku-specific-knowledge-concept"]}),
    c("aku-ahora-es-apalancado-vs-no-apalancado-claim", "claim",
      "La división relevante hoy ya no es rico vs pobre ni cuello-blanco vs cuello-azul, sino "
      "apalancado vs no apalancado: como trabajador quieres estar lo más apalancado posible "
      "para tener gran impacto sin tanto tiempo ni esfuerzo físico.",
      ["riqueza", N, "leverage", "trabajo"],
      {"related": ["aku-leverage-multiplicador-de-juicio-concept"]}),
    c("aku-labor-es-la-peor-forma-de-leverage-claim", "claim",
      "La labor (otras personas trabajando para ti) es la forma de leverage más antigua y la "
      "peor en el mundo moderno: gestionar personas es desordenado, exige enormes dotes de "
      "liderazgo y te deja a un paso de un motín; conviene preferir capital y, sobre todo, "
      "código/medios.",
      ["riqueza", N, "leverage", "labor"],
      {"related": ["aku-permissioned-vs-permissionless-leverage-concept"]}),
    c("aku-capital-escala-mejor-que-las-personas-claim", "claim",
      "El capital como leverage escala mucho mejor que la labor: si te vuelves bueno "
      "gestionando capital, puedes gestionar cantidades crecientes con mucha más facilidad que "
      "gestionar cada vez más personas; por eso muchos CEOs de grandes empresas no tech "
      "ocupan, en esencia, un puesto financiero.",
      ["riqueza", N, "leverage", "capital"]),
    c("aku-optimiza-por-independencia-no-por-paga-claim", "claim",
      "Siempre que puedas, optimiza por independencia antes que por paga: tener independencia "
      "y ser evaluado por tu output (no por tu input) es el ideal, porque te devuelve el "
      "control de tu tiempo.",
      ["riqueza", N, "independencia", "tiempo"]),
    c("aku-trabajador-apalancado-rinde-1000x-y-el-juicio-supera-las-horas-claim", "claim",
      "Un trabajador apalancado puede superar a uno no apalancado por un factor de mil o diez "
      "mil; en él, el juicio importa mucho más que cuántas horas pone o cuán duro trabaja: "
      "existen programadores 1.000x, y un ingeniero puede crear 500M$ de valor con el código "
      "correcto mientras diez trabajando más duro pero con el modelo equivocado pierden el "
      "tiempo.",
      ["riqueza", N, "leverage", "juicio"],
      {"related": ["aku-judgment-naval-concept"]}),
    c("aku-desconexion-input-output-concept", "concept",
      "La desconexión input-output es la propiedad de ciertas profesiones donde las horas "
      "invertidas no se corresponden con el resultado producido; incluye que cuanto mayor es "
      "el componente creativo y el uso de herramientas/leverage, más desconectados están "
      "input y output (construir y vender productos, alta venta); excluye los roles de soporte "
      "(p. ej. atención al cliente), donde input y output van ligados; implica que en "
      "profesiones de input-output conectado es muy difícil crear riqueza.",
      ["riqueza", N, "leverage", "productividad"]),
    c("aku-knowledge-workers-funcionan-como-atletas-sprint-y-descanso-claim", "claim",
      "Los knowledge workers funcionan como atletas —entrenan y esprintan, luego descansan y "
      "reevalúan—, no en jornadas uniformes: la semana de 40 horas es una reliquia de la era "
      "industrial; conviene trabajar en ráfagas de alta energía y no forzar en los momentos de "
      "baja energía.",
      ["riqueza", N, "productividad", "energia"]),
    c("aku-subir-la-escalera-de-leverage-accountability-specific-knowledge-crea-riqueza-claim", "claim",
      "Crear riqueza es subir, con el tiempo y el interés compuesto, una escalera en la que "
      "cada nivel suma más leverage, más accountability y specific knowledge más profundo "
      "(p. ej. en inmobiliario: peón → contratista → promotor → gestor de fondo → plataforma "
      "tech-inmobiliaria), acercándote a poseer todo el upside en lugar de cobrar un salario.",
      ["riqueza", N, "leverage", "accountability"],
      {"related": ["aku-armate-con-specific-knowledge-accountability-y-leverage-claim"]}),
    c("aku-evita-el-riesgo-de-ruina-con-apuestas-racionalmente-optimistas-claim", "claim",
      "Lo único que debes evitar a toda costa es el riesgo de ruina: no hagas nada ilegal "
      "(nunca compensa el mono naranja), evita la pérdida catastrófica total de tu capital y "
      "cuida tu salud; no lo apuestes todo a una sola jugada, sino haz apuestas racionalmente "
      "optimistas con gran upside.",
      ["riqueza", N, "riesgo", "supervivencia"]),
    c("aku-earn-with-your-mind-not-your-time-claim", "claim",
      "Hay que ganar con la mente, no con el tiempo: el objetivo es que un robot, el capital o "
      "un ordenador hagan el trabajo y que a ti te paguen por tu juicio y conocimiento único, "
      "midiéndote por outputs y no por inputs, para ser dueño de tu propio tiempo.",
      ["riqueza", N, "juicio", "tiempo"],
      {"related": ["aku-judgment-naval-concept"]}),
    # ── ch07 Get Paid for Your Judgment ──
    c("aku-pequenas-diferencias-de-juicio-se-amplifican-con-leverage-claim", "claim",
      "Pequeñas diferencias de juicio se amplifican enormemente con el leverage: alguien "
      "acertado el 85% de las veces en lugar del 75%, dirigiendo un barco de 100.000M$, vale "
      "decenas o cientos de millones; por eso los CEOs cobran tanto —su juicio, multiplicado "
      "por la palanca, mueve cantidades inmensas—.",
      ["riqueza", N, "juicio", "leverage"],
      {"related": ["aku-judgment-naval-concept"]}),
    c("aku-juicio-demostrado-con-credibilidad-atrae-leverage-infinito-claim", "claim",
      "El juicio demostrado —con alta accountability, track record público e integridad— es "
      "lo que atrae leverage infinito: como Warren Buffett, cuando has acertado una y otra vez "
      "en público y eres de fiar, la gente respalda tu juicio sin preguntar cuánto trabajas.",
      ["riqueza", N, "juicio", "reputacion"],
      {"related": ["aku-judgment-naval-concept",
                   "aku-fallar-en-publico-bajo-tu-nombre-da-poder-claim"]}),
    c("aku-decide-despacio-actua-rapido-y-deja-que-el-acto-dure-decadas-claim", "claim",
      "Conviene decidir despacio y actuar rápido: malgastamos el tiempo con pensamiento "
      "cortoplacista y busywork, mientras que (como Buffett) pasar un año decidiendo y un día "
      "actuando produce un acto que dura décadas.",
      ["riqueza", N, "juicio", "decisiones"]),
    # ── ch08 Prioritize and Focus ──
    c("aku-riqueza-se-construye-apilando-muchas-cosas-pequenas-claim", "claim",
      "La riqueza rara vez llega en un único gran pago: se construye apilando consistentemente "
      "muchas cosas pequeñas —más negocios, más opciones, más inversiones—, creando "
      "oportunidades de forma sostenida en lugar de esperar un golpe único.",
      ["riqueza", N, "constancia", "largo-plazo"]),
    c("aku-nadie-te-valora-mas-de-lo-que-tu-te-valoras-claim", "claim",
      "Nadie te valorará más de lo que tú te valoras: por eso hay que fijar una tarifa horaria "
      "personal muy alta —que se sienta absurdamente alta— y tratarte conforme a ella desde "
      "joven, antes incluso de tener dinero, para que el mercado acabe ajustándose a tu propia "
      "valoración.",
      ["riqueza", N, "autovaloracion", "tiempo"],
      {"related": ["aku-aspirational-hourly-rate-method"]}),
    c("aku-mentalidad-relativa-y-envidia-impiden-la-riqueza-claim", "claim",
      "Una mentalidad relativa (compararse y envidiar a quienes lo hacen mejor) impide crear "
      "riqueza: los demás perciben esos juicios y malos sentimientos al hacer negocios "
      "contigo; ser anti-riqueza te quita el espíritu adecuado, mientras que los optimistas, a "
      "largo plazo, lo hacen mejor.",
      ["riqueza", N, "mentalidad", "optimismo"],
      {"related": ["aku-creacion-de-riqueza-etica-es-posible-claim"]}),
    c("aku-juegos-de-suma-positiva-vs-suma-cero-concept", "concept",
      "En la vida y los negocios se juegan dos tipos de juego: el de creación de riqueza (suma "
      "positiva, donde el valor se crea y todos pueden ganar) y el de estatus (suma cero, "
      "donde se asciende en la jerarquía social atacando a otros); incluye que muchos juegan "
      "suma cero disfrazando su juego de estatus de superioridad moral («el dinero es malo»); "
      "implica buscar a los pocos jugadores de suma positiva entre la multitud.",
      ["riqueza", N, "teoria-de-juegos", "status"],
      {"related": ["aku-status-posicion-en-jerarquia-social-concept",
                   "aku-busca-wealth-no-money-ni-status-claim"]}),
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
