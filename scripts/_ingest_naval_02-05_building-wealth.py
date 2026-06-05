# -*- coding: utf-8 -*-
"""Almanack of Naval — Building Wealth ch02-05 (specific knowledge, long-term games,
accountability, equity). Elaboran ch01 (mismo libro): solo items NUEVOS."""
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
    # ── ch02 Find and Build Specific Knowledge ──
    c("aku-specific-knowledge-no-se-ensena-pero-se-aprende-claim", "claim",
      "El specific knowledge no se puede enseñar (no se imparte en un aula) pero sí se puede "
      "aprender: se adquiere por aprendizaje (apprenticeship), práctica brutal directa y "
      "exposición real, no por instrucción formal; aun las habilidades de venta, que son una "
      "forma de specific knowledge, se mejoran practicando, no en clase.",
      ["riqueza", N, "specific-knowledge", "aprendizaje"],
      {"related": ["aku-specific-knowledge-concept"]}),
    c("aku-specific-knowledge-es-lo-que-hacias-sin-esfuerzo-de-nino-claim", "claim",
      "Para hallar tu specific knowledge, identifica qué hacías de niño o adolescente casi sin "
      "esfuerzo —algo que ni considerabas una habilidad pero que la gente a tu alrededor "
      "notaba—: es una combinación de rasgos únicos de tu ADN, tu crianza y tu respuesta a "
      "ella, casi horneada en tu identidad, que luego puedes pulir.",
      ["riqueza", N, "specific-knowledge", "autoconocimiento"],
      {"related": ["aku-specific-knowledge-concept"]}),
    c("aku-escapa-la-competencia-mediante-autenticidad-claim", "claim",
      "Escapa de la competencia mediante la autenticidad: compites con otros solo cuando los "
      "copias intentando hacer lo mismo, pero como cada humano es distinto, si construyes y "
      "comercializas algo que es una extensión auténtica de quien eres, nadie puede competir "
      "contigo en eso; nadie puede competir contigo en ser tú.",
      ["riqueza", N, "autenticidad", "unicidad"],
      {"related": ["aku-se-el-mejor-del-mundo-redefiniendo-lo-que-haces-claim",
                   "aku-categoria-de-uno-concept"]}),
    c("aku-ser-aprendiz-perpetuo-es-la-habilidad-clave-para-hacerse-rico-claim", "claim",
      "La habilidad más importante para hacerse rico hoy es convertirse en aprendiz perpetuo: "
      "saber aprender cualquier cosa que quieras; el modelo viejo (estudiar 4 años y ejercer "
      "30) ya no aplica porque las profesiones se vuelven obsoletas rápido y hay que dominar "
      "un campo nuevo en 9-12 meses.",
      ["riqueza", N, "aprendizaje", "adaptabilidad"]),
    c("aku-las-fundaciones-importan-mas-que-la-profundidad-equivocada-claim", "claim",
      "Las fundaciones (aritmética básica, expresarse con claridad en lenguaje sencillo, "
      "persuasión al hablar) importan mucho más que la sofisticación mal colocada (cálculo, "
      "vocabulario extenso, marketing digital experto): es mejor ser 9/10 o 10/10 en "
      "fundamentos que profundizar prematuramente, porque con buenas fundaciones ningún libro "
      "te asusta.",
      ["riqueza", N, "aprendizaje", "fundamentos"]),
    c("aku-solo-se-logra-maestria-en-una-o-dos-cosas-claim", "claim",
      "Solo se puede alcanzar la maestría en una o dos cosas, y suelen ser aquellas por las "
      "que estás obsesionado: hay que ser profundo en algo (no una milla de ancho y una "
      "pulgada de hondo) para obtener lo que quieres de la vida.",
      ["riqueza", N, "maestria", "foco"]),
    c("aku-ciencia-aguas-arriba-de-tecnologia-y-negocio-concept", "concept",
      "La sociedad, los negocios y el dinero están aguas abajo de la tecnología, que a su vez "
      "está aguas abajo de la ciencia: la ciencia aplicada es el motor de la humanidad; "
      "incluye el corolario de que los científicos aplicados son las personas más poderosas "
      "del mundo; implica que el valor fundamental se origina en el descubrimiento científico.",
      ["riqueza", N, "ciencia", "tecnologia"],
      {"related": ["aku-technology-cosas-que-aun-no-funcionan-concept"]}),
    c("aku-mejores-trabajos-ni-decretados-ni-titulados-claim", "claim",
      "Los mejores trabajos no son ni decretados (asignados por una autoridad) ni titulados "
      "(obtenidos por un diploma): son expresiones creativas de aprendices continuos en "
      "mercados libres.",
      ["riqueza", N, "carrera", "creatividad"]),
    # ── ch03 Play Long-Term Games with Long-Term People ──
    c("aku-interes-compuesto-aplica-a-relaciones-reputacion-conocimiento-claim", "claim",
      "El interés compuesto no se limita al capital: aplica igual a las relaciones (la "
      "confianza acumulada simplifica toda negociación futura), a la reputación (una "
      "reputación impecable mantenida durante décadas llega a valer miles de veces más que el "
      "talento sin continuidad) y al conocimiento; por eso conviene quedarse con lo bueno y "
      "componer durante años.",
      ["riqueza", N, "largo-plazo", "reputacion"],
      {"related": ["aku-juega-juegos-iterados-retornos-del-interes-compuesto-claim",
                   "aku-elige-juegos-largo-plazo-con-gente-largo-plazo-claim"]}),
    c("aku-intenciones-no-importan-importan-las-acciones-claim", "claim",
      "Las intenciones no importan; importan las acciones: por eso ser ético es difícil, "
      "porque exige actuar de forma consistente, no solo querer lo correcto; la confianza y la "
      "reputación se construyen con actos repetidos, no con propósitos.",
      ["riqueza", N, "etica", "accion"]),
    c("aku-99-por-ciento-del-esfuerzo-se-desperdicia-encuentra-el-1-claim", "claim",
      "En el sentido orientado a objetivos, el 99% del esfuerzo se desperdicia y solo el ~1% "
      "rinde de verdad (aunque nada se pierde como aprendizaje); por eso, en relaciones, "
      "estudio y trabajo, lo que buscas es identificar ese 1% en el que puedes ir all-in para "
      "ganar interés compuesto, y cuando lo encuentras, te entregas y olvidas el resto.",
      ["riqueza", N, "foco", "largo-plazo"],
      {"related": ["aku-con-quien-y-en-que-trabajas-importa-mas-que-cuanto-claim"]}),
    # ── ch04 Take on Accountability ──
    c("aku-fallar-en-publico-bajo-tu-nombre-da-poder-claim", "claim",
      "Quienes tienen la capacidad de fallar en público bajo su propio nombre ganan mucho "
      "poder: seguimos socialmente programados para temer el fracaso público bajo nuestro "
      "nombre, así que asumir ese riesgo —exponerse, opinar, emprender abiertamente— diferencia "
      "y otorga credibilidad, recompensa y leverage.",
      ["riqueza", N, "accountability", "riesgo"],
      {"related": ["aku-accountability-bajo-tu-nombre-concept"]}),
    c("aku-el-riesgo-a-la-baja-de-fracasar-es-pequeno-asume-mas-accountability-claim", "claim",
      "En la sociedad moderna el riesgo a la baja de fracasar es pequeño (no hay prisión por "
      "deudas, la bancarrota personal limpia deudas en buenos ecosistemas y se perdona el "
      "fracaso honesto y de alta integridad), así que las personas deberían asumir mucha más "
      "accountability de la que asumen.",
      ["riqueza", N, "accountability", "riesgo"],
      {"related": ["aku-accountability-bajo-tu-nombre-concept"]}),
    # ── ch05 Build or Buy Equity in a Business ──
    c("aku-sin-propiedad-tus-inputs-estan-atados-a-tus-outputs-claim", "claim",
      "Sin propiedad (equity), tus inputs están estrechamente atados a tus outputs: en "
      "cualquier empleo asalariado —incluso muy bien pagado, como médico o abogado— cobras por "
      "hora, así que cuando duermes, te jubilas o estás de vacaciones no ganas, y no puedes "
      "ganar de forma no lineal; el ingreso pasivo exige poseer un negocio que gane por ti.",
      ["riqueza", N, "equity", "ingreso-pasivo"],
      {"related": ["aku-no-te-haces-rico-alquilando-tu-tiempo-debes-poseer-equity-claim"]}),
    c("aku-equity-es-el-upside-deuda-es-downside-garantizado-concept", "concept",
      "Poseer equity de una empresa significa poseer el upside (la subida), mientras que "
      "poseer deuda significa flujos de ingreso garantizados y el downside (la bajada); "
      "incluye que el dueño que asume el riesgo, la accountability, la IP y la marca captura la "
      "riqueza y paga al asalariado el mínimo necesario; implica que para crear riqueza real "
      "quieres equity, no salario ni deuda.",
      ["riqueza", N, "equity", "upside"],
      {"related": ["aku-equity-value-concept",
                   "aku-no-te-haces-rico-alquilando-tu-tiempo-debes-poseer-equity-claim"]}),
]

takus = [
    {"id": "taku-encontrar-tu-specific-knowledge", "taku_type": "heuristic", "subdir": "heuristics",
     "title": "Cómo encontrar tu specific knowledge",
     "origin": ORIGIN, "domain": [N, "specific-knowledge", "autoconocimiento"],
     "when_to_use": "Cuando buscas en qué construir tu carrera o negocio para tener una ventaja insustituible.",
     "when_not_to_use": "Para elegir un campo solo porque está de moda o paga bien ahora, ignorando tu curiosidad genuina.",
     "aku_links": {"justified_by": [
         "aku-specific-knowledge-concept",
         "aku-specific-knowledge-es-lo-que-hacias-sin-esfuerzo-de-nino-claim",
         "aku-escapa-la-competencia-mediante-autenticidad-claim"]},
     "created": D, "updated": D,
     "body": (
        "## The Rule\n\n"
        "Persigue tu curiosidad y pasión genuinas hasta el borde del conocimiento; tu specific "
        "knowledge es lo que para ti parece juego y para otros parece trabajo. Para localizarlo:\n\n"
        "1. Recuerda qué hacías sin esfuerzo de niño/adolescente que otros notaban.\n"
        "2. Pregunta a tu madre o a tu mejor amigo de la infancia qué se te daba bien.\n"
        "3. Observa en qué te aburres rápido vs. en qué profundizas obsesivamente.\n"
        "4. Construye una expresión auténtica de eso (nadie compite contigo en ser tú).\n\n"
        "## What It Replaces\n\n"
        "Sustituye elegir carrera por modas o consejos de inversores por elegir según tus "
        "talentos innatos y curiosidad.\n\n"
        "## When It Holds\n\n"
        "Cuando hay un mercado (idealmente vía internet) donde ser el mejor en tu nicho auténtico "
        "tiene demanda; en el dominio de las ideas, leverage e interés compuesto amplifican la ventaja.\n\n"
        "## When It Fails\n\n"
        "Si no estás 100% metido: alguien que lo esté te superará por mucho. Tampoco funciona si "
        "te quedas una milla de ancho y una pulgada de hondo sin profundizar en nada.\n\n"
        "## Why It Works\n\n"
        "El specific knowledge no se puede entrenar ni externalizar; al ser una extensión auténtica "
        "de tu identidad, es insustituible y escapa de la competencia.\n\n"
        "## Calibration\n\n"
        "Apuntala primero las fundaciones (aritmética, claridad al expresarte, persuasión); luego "
        "profundiza en la una o dos cosas que te obsesionan hasta la maestría."),
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
