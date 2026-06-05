# -*- coding: utf-8 -*-
"""Ingesta — Extreme Ownership, Cap 12 'Discipline Equals Freedom — The Dichotomy
of Leadership' (cierra el libro). Catálogo de dicotomías = puente al Libro 2."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/extreme-ownership/extreme-ownership.md"
ORIGIN = "Jocko Willink & Leif Babin, Extreme Ownership (2015)"
DICH = "aku-dichotomy-of-leadership-concept"
EO = "aku-extreme-ownership-concept"
DC = "aku-decentralized-command-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "dicotomia"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

def dich(id, statement, extra=None):
    rel = {"supports": [DICH]}
    if extra:
        rel.update(extra)
    return aku(id, "concept", statement, DOM, rel)

akus = [
    aku(DICH, "concept",
        "La «Dichotomy of Leadership» (dicotomía del liderazgo) es el principio de que liderar bien consiste en hallar el equilibrio entre cualidades aparentemente contradictorias, entre un extremo y el opuesto; incluye que el mero reconocimiento de esta dicotomía es una de las herramientas más poderosas del líder; implica que cuando un líder falla, la causa raíz suele ser haberse inclinado demasiado en una dirección.",
        DOM),
    aku("aku-discipline-equals-freedom-concept", "concept",
        "«Discipline equals freedom» (la disciplina es libertad): disciplina y libertad son fuerzas opuestas que deben equilibrarse; es la dicotomía arquetípica del liderazgo —cuanta más disciplina te impones, más libertad y capacidad de acción ganas—.",
        DOM + ["disciplina"],
        {"supports": [DICH]}),
    dich("aku-lider-y-seguidor-concept",
        "Dicotomía líder-seguidor: un líder debe liderar pero también estar listo para seguir cuando otro miembro del equipo está en mejor posición (más experiencia o mejor idea) para planificar o decidir; un líder seguro no se siente intimidado cuando otros dan un paso al frente, deja a un lado el ego y no busca el reconocimiento."),
    dich("aku-agresivo-no-prepotente-concept",
        "Dicotomía agresivo-no prepotente: el líder debe ser agresivo y empujar a por las misiones difíciles, pero no tan prepotente que los subordinados no se atrevan a acercarse con preocupaciones, ideas o desacuerdos; debe fomentar que cualquiera, sea cual sea su rango, plantee una visión opuesta."),
    dich("aku-calmado-no-robotico-concept",
        "Dicotomía calmado-no robótico: el líder debe controlar sus emociones (quien pierde los nervios pierde el respeto), pero mostrar emoción es normal y necesario; un líder sin ninguna emoción parece un robot, y la gente no sigue a los robots."),
    dich("aku-valiente-no-temerario-concept",
        "Dicotomía valiente-no temerario: el líder debe aceptar el riesgo y actuar con coraje, pero nunca ser imprudente; es su trabajo mitigar todo lo posible los riesgos controlables sin sacrificar al equipo ni dilapidar recursos críticos."),
    dich("aku-competitivo-buen-perdedor-concept",
        "Dicotomía competitivo-buen perdedor: el líder debe impulsar la competición y exigir el máximo nivel, pero nunca anteponer su propio afán de éxito personal al éxito de la misión del equipo mayor; debe actuar con profesionalidad y reconocer las contribuciones de los demás."),
    dich("aku-atento-detalle-no-obsesionado-concept",
        "Dicotomía atento al detalle-no obsesionado: el líder debe monitorizar y verificar el progreso del equipo en las tareas más críticas, pero sin empantanarse en la minucia táctica a costa del éxito estratégico ni perder de vista el cuadro general."),
    dich("aku-fuerte-con-resistencia-concept",
        "Dicotomía fuerza-resistencia: el líder debe ser fuerte pero también tener resistencia, física y mental, para sostener el máximo nivel a largo plazo; debe reconocer los límites y dosificarse a sí mismo y al equipo para mantener un buen desempeño indefinidamente."),
    dich("aku-humilde-no-pasivo-concept",
        "Dicotomía humilde-no pasivo: el líder debe tener humildad —controlar el ego, escuchar, admitir errores y asumirlos—, pero no ser pasivo: debe saber alzar la voz cuando importa y plantarse respetuosamente ante una decisión u orden que perjudique el éxito de la misión."),
    dich("aku-callado-no-silencioso-concept",
        "Dicotomía callado-no silencioso: el líder no necesita acaparar la palabra, pero tampoco debe permanecer en silencio cuando algo importa; debe hablar para defender al equipo y discrepar respetuosamente cuando es necesario."),
    dich("aku-cercano-pero-no-demasiado-concept",
        "Dicotomía cercanía con los subordinados: los mejores líderes conocen las motivaciones, la vida y la familia de su gente, pero nunca tan cerca que un miembro pese más que otro o más que la misión, ni tanto que el equipo olvide quién manda."),
    dich("aku-balance-ownership-decentralized-command-concept",
        "Dicotomía Extreme Ownership-Decentralized Command: el líder debe ejercer Extreme Ownership (poseer todo) y, simultáneamente, ceder el control a los líderes subordinados mediante mando descentralizado; equilibrar ambas es una de las tensiones centrales del liderazgo.",
        {"related": [EO, DC]}),
    dich("aku-nada-que-probar-pero-todo-que-probar-concept",
        "Dicotomía «nada que probar pero todo que probar»: por su rango y posición el líder no tiene que demostrar que manda (tomar el control de minucias para reforzar la autoridad es señal de liderazgo pobre e inseguro), pero sí tiene todo que probar cada día: ganarse la confianza del equipo demostrando con hechos buen juicio, calma y que cuida sus intereses a largo plazo."),
    aku("aku-lider-se-desvia-por-inclinarse-demasiado-claim", "claim",
        "Cuando un líder tiene problemas, la causa raíz suele ser que se ha inclinado demasiado en una dirección de alguna dicotomía y se ha desviado del rumbo; la conciencia de las dicotomías del liderazgo permite descubrirlo y corregirlo.",
        DOM,
        {"supports": [DICH]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
# añadir manualmente confident-but-not-cocky (existente) como instancia del paraguas
cross = list(cross) + [("aku-confident-but-not-cocky-concept", "supports", "supported_by", DICH)]
# (lo gestionamos como patch directo: confident -> supports dichotomy, dichotomy.supported_by += confident)
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
# además, en el fichero confident-but-not-cocky añadir supports -> DICH
ops.setdefault("aku-confident-but-not-cocky-concept", []).append(("supports", DICH))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
akupatch.apply(ROOT, patch_ops)
print(f"cross-links inversos sobre {len(patch_ops)} AKUs existentes:")
for t, rels in ops.items():
    print(f"  {t}: +{len(rels)} {[r[0] for r in rels]}")
