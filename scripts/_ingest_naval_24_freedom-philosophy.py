# -*- coding: utf-8 -*-
"""Almanack of Naval — Choosing to Free Yourself + Philosophy (meanings of life, values,
Rational Buddhism, the present). Solo items NUEVOS."""
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
    c("aku-lo-mas-dificil-no-es-hacer-lo-que-quieres-sino-saber-que-quieres-claim", "claim",
      "Lo más difícil no es hacer lo que quieres, sino saber qué quieres: una vez tienes claro "
      "el deseo, la ejecución es lo de menos; la verdadera dificultad es la claridad sobre el "
      "objetivo.",
      [N, "deseo", "claridad"]),
    c("aku-no-hay-adultos-todos-improvisan-encuentra-tu-camino-claim", "claim",
      "Conviene ser consciente de que no hay «adultos»: todo el mundo improvisa sobre la "
      "marcha, así que tienes que encontrar tu propio camino —eligiendo, escogiendo y "
      "descartando como veas— en lugar de esperar que alguien con autoridad te diga cómo se "
      "hace.",
      [N, "autonomia", "vida"]),
    c("aku-freedom-from-vs-freedom-to-concept", "concept",
      "La libertad tiene dos formas: «freedom to» (libertad para hacer cualquier cosa, cuando "
      "quieras) y «freedom from» (libertad interna: de la reacción, de la ira, de la tristeza, "
      "de verse forzado); incluye que la madurez desplaza el valor de la primera a la segunda; "
      "implica que la libertad más profunda es interna, no la mera ausencia de restricciones "
      "externas.",
      [N, "libertad", "madurez"],
      {"related": ["aku-la-libertad-es-el-valor-supremo-claim"]}),
    c("aku-el-coraje-es-no-importarte-lo-que-piensen-los-demas-claim", "claim",
      "El coraje no es lanzarse contra un nido de ametralladoras, sino no importarte lo que "
      "piensen los demás: liberarse del juicio ajeno es la valentía relevante para la mayoría "
      "de las decisiones de la vida.",
      [N, "coraje", "validacion"]),
    c("aku-no-eres-responsable-de-la-felicidad-de-otros-valora-tu-tiempo-claim", "claim",
      "Tu tiempo es todo lo que tienes —más importante que el dinero o los amigos— así que no "
      "lo malgastes haciendo felices a otros: la felicidad de los demás es su problema; si tú "
      "eres feliz, eso ya hace felices a los demás y podrán aprender de ti, pero no eres "
      "responsable de su felicidad.",
      [N, "tiempo", "responsabilidad"],
      {"related": ["aku-tiempo-recurso-mas-valioso-y-limitado-claim"]}),
    c("aku-las-expectativas-ajenas-sobre-ti-son-su-problema-no-el-tuyo-claim", "claim",
      "Si hieres a otros porque tenían expectativas sobre ti, ese es su problema, no el tuyo "
      "(un acuerdo sí sería tu problema, pero una expectativa no): la gente tendrá muchas "
      "expectativas en la vida, y cuanto antes las desmontes, mejor.",
      [N, "expectativas", "libertad"]),
    c("aku-la-ira-es-un-contrato-para-el-tormento-y-su-propio-castigo-concept", "concept",
      "La ira es una forma de señalar al otro con toda tu fuerza que eres capaz de violencia "
      "(es su precursora) y una pérdida de control sobre la situación; incluye ser un contrato "
      "que haces contigo mismo para estar en tormento físico, mental y emocional hasta que la "
      "realidad cambie; implica que es su propio castigo —quien empuja tu cabeza bajo el agua "
      "se ahoga contigo—.",
      [N, "ira", "emociones"]),
    c("aku-vivir-muy-por-debajo-de-tus-medios-da-una-libertad-inimaginable-claim", "claim",
      "Quien vive muy por debajo de sus medios disfruta de una libertad que quienes están "
      "ocupados mejorando su tren de vida no pueden ni concebir; una vez controlas tu propio "
      "destino, ya no dejas que nadie te diga qué hacer, y un poco de libertad puede volverte "
      "ininempleable.",
      [N, "libertad", "dinero"],
      {"related": ["aku-no-subas-tu-tren-de-vida-al-ganar-mas-claim"]}),
    c("aku-la-mente-debe-ser-sirviente-no-amo-claim", "claim",
      "La mente debe ser un sirviente y una herramienta, no un amo: la «monkey mind» que "
      "juzga, reproduce el ayer y fantasea el mañana es útil para planificar y resolver "
      "problemas, pero es mala para la felicidad y no debería conducirte 24/7; además, una "
      "mente ocupada acelera el paso subjetivo del tiempo.",
      [N, "mente", "presente"],
      {"related": ["aku-awareness-vs-ego-eres-mas-que-tu-monkey-mind-concept"]}),
    c("aku-la-lucha-moderna-individuos-vs-ejercitos-que-explotan-la-abundancia-concept", "concept",
      "La lucha moderna enfrenta a individuos solitarios que invocan una fuerza de voluntad "
      "sobrehumana (ayunando, meditando, ejercitándose) contra ejércitos de científicos y "
      "estadísticos que convierten comida, pantallas y medicina abundantes en comida basura, "
      "clickbait, porno infinito, juegos sin fin y drogas adictivas; implica que mantener la "
      "salud y la atención hoy exige resistir un entorno diseñado para capturarlas.",
      [N, "mundo-moderno", "autocontrol"],
      {"related": ["aku-vivimos-en-desajuste-evolutivo-con-el-mundo-moderno-concept"]}),
    c("aku-los-tres-significados-de-la-vida-concept", "concept",
      "Ante el sentido de la vida hay tres respuestas: (1) es personal —debes encontrarlo tú, y "
      "lo importante es la pregunta, no la respuesta—; (2) no hay sentido ni propósito "
      "intrínseco —todo se desvanece, así que creas el tuyo—; (3) quizá el «sentido» físico es "
      "que los seres vivos revierten localmente la entropía mientras la aceleran globalmente "
      "hacia la heat death del universo, donde todo se iguala y somos una sola cosa; implica "
      "que, en cualquier caso, el significado es algo que uno fabrica.",
      [N, "sentido-de-la-vida", "filosofia"],
      {"related": ["aku-abrazar-la-muerte-da-sentido-y-no-hay-legado-concept"]}),
    c("aku-solo-relaciones-entre-iguales-no-jerarquicas-claim", "claim",
      "Naval solo cree en relaciones entre iguales, no jerárquicas: no quiere estar por encima "
      "ni por debajo de nadie, y si no puede tratar a alguien como par ni ser tratado como tal, "
      "prefiere no interactuar.",
      [N, "relaciones", "valores"]),
    c("aku-busca-personas-cuyos-valores-encajen-con-los-tuyos-claim", "claim",
      "Gran parte de encontrar grandes relaciones, socios o pareja es hallar personas cuyos "
      "valores encajen con los tuyos: si los valores coinciden, las pequeñas cosas no importan, "
      "y casi todas las peleas vienen de valores que no se alinean; como dice Munger, «para "
      "encontrar una pareja digna, sé digno de una pareja digna».",
      [N, "valores", "relaciones"],
      {"related": ["aku-elige-socios-con-integridad-sobre-todo-claim"]}),
    c("aku-tener-un-hijo-responde-a-la-pregunta-del-sentido-de-la-vida-claim", "claim",
      "Tener un hijo responde, de golpe, a la pregunta del sentido de la vida: lo más "
      "importante del universo se traslada de tu cuerpo al del hijo, lo que te cambia y vuelve "
      "tus valores mucho menos egoístas.",
      [N, "sentido-de-la-vida", "familia"]),
    c("aku-rational-buddhism-concept", "concept",
      "El Rational Buddhism (budismo racional) de Naval reconcilia dos polos: la evolución "
      "(principio que explica al humano como máquina de supervivencia y replicación) y el "
      "budismo (la filosofía espiritual más antigua y probada sobre el estado interno); incluye "
      "aceptar solo lo que puedes verificar por ti mismo o vía ciencia (meditar es bueno, hay "
      "una capa de awareness bajo la monkey mind) y rechazar lo no falsable (vidas pasadas, "
      "chakras, levitación); implica «pruébalo todo, sé escéptico, quédate lo útil y descarta "
      "lo demás».",
      [N, "filosofia", "budismo"],
      {"related": ["aku-falsabilidad-sin-predicciones-falsables-no-es-ciencia-concept",
                   "aku-choiceless-awareness-acepta-sin-juzgar-y-el-90-por-ciento-de-pensamientos-son-miedo-concept"]}),
    c("aku-la-sabiduria-es-descartar-vicios-y-volver-a-la-virtud-via-conocimiento-claim", "claim",
      "Todos empiezan inocentes y todos se corrompen; la sabiduría es el descarte de los vicios "
      "y el retorno a la virtud por la vía del conocimiento, entendiendo las consecuencias a "
      "largo plazo de los propios actos.",
      [N, "sabiduria", "virtud"],
      {"related": ["aku-sabiduria-es-conocer-consecuencias-a-largo-plazo-juicio-es-aplicarla-concept"]}),
    c("aku-el-presente-es-todo-lo-que-hay-concept", "concept",
      "El presente es literalmente todo lo que hay: nadie ha vuelto al pasado ni ha predicho el "
      "futuro de un modo que importe, y lo único que existe es este punto exacto en el espacio "
      "y el tiempo; incluye que cada momento es perfectamente único y se escapa antes de poder "
      "agarrarlo, y que mueres y renaces en cada instante; implica que todo es más bello porque "
      "estamos condenados —nunca estarás más hermoso que ahora y nunca volveremos a estar "
      "aquí—.",
      [N, "presente", "filosofia"],
      {"related": ["aku-la-felicidad-requiere-presencia-claim"]}),
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
