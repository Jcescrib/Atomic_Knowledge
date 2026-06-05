# -*- coding: utf-8 -*-
"""Almanack of Naval — ch08(status) + ch09 Find Work That Feels Like Play + ch10 How
to Get Lucky. Solo items NUEVOS (dedup vs caps previos)."""
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
    # ── ch08 status games (continuación) ──
    c("aku-evita-los-juegos-de-estatus-te-vuelven-combativo-claim", "claim",
      "Conviene evitar los juegos de estatus en tu vida porque, al ser de suma cero "
      "(hierárquicos desde las tribus de monos), para ganar tienes que rebajar a otro, lo que "
      "te convierte en una persona enfadada y combativa que siempre lucha por hundir a los "
      "demás y elevar a los suyos.",
      [N, "status", "mentalidad"],
      {"related": ["aku-juegos-de-suma-positiva-vs-suma-cero-concept",
                   "aku-status-posicion-en-jerarquia-social-concept"]}),
    c("aku-tres-grandes-decisiones-donde-vives-con-quien-y-que-haces-claim", "claim",
      "Las tres decisiones dominantes de la vida temprana son dónde vives, con quién estás y "
      "qué haces; como determinan la trayectoria de tu vida durante años, deberías dedicar uno "
      "o dos años a decidir cada una y decir que no a casi todo lo demás para liberar tiempo "
      "para los problemas importantes.",
      [N, "decisiones", "vida"]),
    c("aku-regala-lo-que-se-te-da-bien-y-paga-por-adelantado-claim", "claim",
      "Para rodearte de gente exitosa, averigua en qué eres bueno y empieza a ayudar a otros "
      "con ello regalándolo y pagando por adelantado: el karma funciona porque las personas son "
      "consistentes y, en un horizonte largo, atraes lo que proyectas; pero no lo midas, o tu "
      "paciencia se agotará.",
      [N, "generosidad", "relaciones"]),
    # ── ch09 Find Work That Feels Like Play ──
    c("aku-encuentra-trabajo-que-se-sienta-como-juego-claim", "claim",
      "Busca el trabajo que para ti se sienta como juego aunque para otros parezca trabajo: "
      "como lo disfrutas, lo harás dieciséis horas al día sin agotarte, y por eso nadie podrá "
      "competir contigo —tendrían que trabajar para igualarte y perderán—.",
      [N, "vocacion", "specific-knowledge"],
      {"related": ["aku-escapa-la-competencia-mediante-autenticidad-claim",
                   "aku-haz-cosas-por-su-propio-bien-produce-tu-mejor-trabajo-claim"]}),
    c("aku-retiro-es-dejar-de-sacrificar-hoy-por-un-manana-imaginario-concept", "concept",
      "El retiro (en la definición de Naval) es dejar de sacrificar el hoy por un mañana "
      "imaginario: ocurre cuando el día de hoy es completo en sí mismo; incluye que no tiene "
      "que ver con la edad ni con jubilarse a los 65; excluye la idea de cobrar un cheque en "
      "una residencia; implica vivir el presente por su propio valor.",
      [N, "retiro", "presente"],
      {"related": ["aku-tres-caminos-al-retiro-concept"]}),
    c("aku-tres-caminos-al-retiro-concept", "concept",
      "Hay tres caminos al retiro (en el sentido de Naval): (1) ahorrar tanto que tu ingreso "
      "pasivo cubra tu burn rate; (2) reducir tu burn rate a cero volviéndote monje; (3) hacer "
      "algo que ames tanto que el dinero deje de importar; implica que la independencia es "
      "alcanzable bajando el gasto, subiendo los activos pasivos o amando el trabajo.",
      [N, "retiro", "libertad-financiera"]),
    c("aku-la-lujuria-por-el-dinero-es-un-pozo-sin-fondo-claim", "claim",
      "El dinero no es malo, pero la lujuria por el dinero es mala para ti porque es un pozo "
      "sin fondo: el deseo no se apaga en ninguna cifra, siempre quieres más y te vuelves "
      "paranoico y temeroso de perder lo que tienes; el castigo por amar el dinero se entrega a "
      "la vez que el dinero.",
      [N, "dinero", "mentalidad"]),
    c("aku-no-subas-tu-tren-de-vida-al-ganar-mas-claim", "claim",
      "La mejor forma de escapar del amor constante al dinero es no subir tu tren de vida a "
      "medida que ganas más: si mantienes fijo tu estilo de vida (y ganas idealmente en sumas "
      "grandes y no a goteo), no te dará tiempo a inflar tus gastos y puedes adelantarte tanto "
      "que llegues a ser financieramente libre.",
      [N, "dinero", "libertad-financiera"]),
    c("aku-la-libertad-es-el-valor-supremo-claim", "claim",
      "La libertad —para hacer lo que quieres, frente a lo que no quieres hacer, y frente a tus "
      "propias emociones que perturban tu paz— es el valor número uno: el dinero es bueno en la "
      "medida en que compra libertad, y malo en la medida en que te resta libertad.",
      [N, "libertad", "valores"]),
    c("aku-la-vida-son-juegos-de-horizonte-creciente-baja-del-hedonic-treadmill-concept", "concept",
      "La vida es una sucesión de juegos de horizonte cada vez más largo (el de la escuela, el "
      "social, el del dinero, el del estatus); incluye que cada meta solo lleva a otra meta y "
      "que, una vez ves a través del juego, su resultado deja de importar; implica buscar "
      "bajarse de la hedonic treadmill y vivir momento a momento sin un objetivo final.",
      [N, "filosofia", "deseo"]),
    c("aku-los-ganadores-son-los-tan-adictos-que-siguen-pese-a-la-utilidad-marginal-decreciente-claim", "claim",
      "Los ganadores de cualquier juego son las personas tan adictas que siguen jugando incluso "
      "cuando la utilidad marginal de ganar decae: la victoria sostenida nace de una adicción "
      "al propio juego, no de un cálculo racional de beneficios.",
      [N, "psicologia", "motivacion"]),
    c("aku-lo-mas-importante-de-una-empresa-es-su-red-de-alumni-claim", "claim",
      "Para quien empieza su carrera (e incluso después), lo más importante de una empresa es "
      "la red de alumni que vas a construir: piensa con quién trabajarás y qué harán esas "
      "personas después, porque esa red domina el valor a largo plazo de tu paso por ella.",
      [N, "carrera", "relaciones"]),
    # ── ch10 How to Get Lucky ──
    c("aku-cuatro-tipos-de-suerte-concept", "concept",
      "Existen cuatro tipos de suerte: (1) suerte ciega, totalmente fuera de tu control; (2) "
      "suerte por persistencia, hustle y movimiento, que generas agitando oportunidades hasta "
      "que la suerte te encuentra; (3) suerte por estar tan capacitado en un campo que detectas "
      "golpes de suerte que otros no ven; (4) suerte por construir un carácter, marca y "
      "mentalidad únicos que hacen que la suerte (los tratos) te busque a ti; implica que las "
      "tres últimas son cultivables y vuelven la fortuna casi determinista.",
      [N, "suerte", "oportunidad"],
      {"related": ["aku-construye-un-caracter-que-atrae-la-suerte-el-caracter-es-destino-claim",
                   "aku-hacerse-rico-sin-suerte-es-ser-determinista-claim"]}),
    c("aku-construye-un-caracter-que-atrae-la-suerte-el-caracter-es-destino-claim", "claim",
      "Construye un carácter y una reputación —fiable, íntegro, de pensamiento a largo plazo— "
      "que hagan que la gente te traiga tratos que otros calificarían de suerte: como el mejor "
      "buceador al que acuden los que hallan un tesoro, tu carácter se convierte en tu destino "
      "y atrae oportunidades que sabes que no fueron azar.",
      [N, "reputacion", "suerte"],
      {"related": ["aku-juicio-demostrado-con-credibilidad-atrae-leverage-infinito-claim"]}),
    c("aku-hacerse-rico-sin-suerte-es-ser-determinista-claim", "claim",
      "«Hacerse rico sin suerte» significa volver la riqueza determinista: en 1.000 universos "
      "paralelos quieres ser rico en 999, no solo en los pocos donde tuviste suerte ciega; por "
      "eso se factoriza la suerte fuera, cultivando habilidad, reputación y carácter que "
      "capitalizan o atraen las oportunidades.",
      [N, "suerte", "riqueza"]),
    c("aku-juego-largo-plazo-suma-positiva-corto-plazo-suma-cero-claim", "claim",
      "En un juego a largo plazo parece que todos se enriquecen mutuamente (suma positiva: se "
      "hornea el pastel lo más grande posible), mientras que en un juego a corto plazo parece "
      "que cada uno se enriquece a sí mismo (suma cero: se reparte el pastel); por eso conviene "
      "jugar a largo plazo.",
      [N, "teoria-de-juegos", "largo-plazo"],
      {"related": ["aku-juegos-de-suma-positiva-vs-suma-cero-concept",
                   "aku-elige-juegos-largo-plazo-con-gente-largo-plazo-claim"]}),
    c("aku-el-networking-de-negocios-es-perdida-de-tiempo-se-un-maker-claim", "claim",
      "El networking de negocios es una pérdida de tiempo: construir relaciones de negocio muy "
      "por adelantado de hacer negocios no sirve; en su lugar, sé un maker que crea algo "
      "interesante que la gente quiere, muestra y practica tu oficio, y las personas adecuadas "
      "acabarán encontrándote.",
      [N, "relaciones", "reputacion"]),
    c("aku-quien-presume-de-honesto-suele-ocultar-algo-claim", "claim",
      "Si alguien habla mucho de lo honesto que es o dedica demasiado tiempo a ensalzar sus "
      "propios valores, probablemente está encubriendo algo: presumir de integridad es un "
      "indicador revelador de su ausencia.",
      [N, "confianza", "señales"]),
    c("aku-no-puedes-ocultarte-de-ti-mismo-tus-valores-determinan-tu-autoestima-claim", "claim",
      "No puedes ocultar nada de ti mismo: tus fallos morales quedan escritos en tu psique y te "
      "son obvios, y demasiados de ellos te impiden respetarte; como el peor resultado es no "
      "tener autoestima, conviene evitar hacer cosas de las que no estarás orgulloso —«cuanto "
      "más cerca quieras estar de mí, mejores han de ser tus valores»—.",
      [N, "integridad", "autoestima"]),
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
