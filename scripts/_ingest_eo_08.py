# -*- coding: utf-8 -*-
"""Ingesta — Extreme Ownership, Cap 8 'Decentralized Command' (Law of Combat #4)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/extreme-ownership/extreme-ownership.md"
ORIGIN = "Jocko Willink & Leif Babin, Extreme Ownership (2015)"
LOC = "aku-laws-of-combat-concept"
DC = "aku-decentralized-command-concept"
SOC = "aku-span-of-control-concept"
TRUST = "aku-decentralized-requiere-confianza-bidireccional-claim"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "descentralizacion"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(DC, "concept",
        "«Decentralized Command» (mando descentralizado) es la cuarta Ley del Combate: dividir el equipo en elementos manejables de 4-6 personas con un líder claramente designado y empoderado para tomar decisiones sobre las tareas clave de la misión; incluye que los líderes de todos los niveles estén empoderados para decidir en entornos caóticos y cambiantes; excluye tanto el micromanagement desde arriba como el caos de cada uno a su aire.",
        DOM + ["combate", "mando"],
        {"supports": [LOC], "related": ["aku-believe-in-the-mission-concept", "aku-contingency-planning-anticipar-method", "aku-simple-law-of-combat-concept"]}),
    aku("aku-limite-cognitivo-6-10-personas-claim", "claim",
        "Los seres humanos no suelen ser capaces de gestionar a más de seis a diez personas —y bajo presión, cuando surgen las contingencias inevitables, el máximo efectivo baja a unas cuatro a seis—; por eso los equipos deben dividirse en elementos de 4-5 operadores con un líder.",
        DOM + ["cognicion", "equipos"],
        {"supports": [DC, SOC]}),
    aku("aku-commanders-intent-concept", "concept",
        "El «Commander's Intent» (intención del mando) es el objetivo último de la misión, que cada líder subordinado debe comprender además del qué hacer: explicitarlo directamente a las tropas les permite ejecutar de forma que apoye el objetivo global sin pedir permiso; incluye el porqué de la misión, no solo el qué (mission statement); excluye dar solo un enunciado de misión sin propósito.",
        DOM + ["mando", "proposito"],
        {"supports": [DC], "related": ["aku-believe-in-the-mission-concept", "aku-senior-debe-explicar-el-porque-claim"]}),
    aku("aku-decentralized-limites-de-autoridad-claim", "claim",
        "Decentralized Command no significa que los líderes junior operen a su aire (eso es caos): deben comprender con claridad los «left and right limits» de su autoridad de decisión, recomendar hacia arriba las decisiones fuera de su alcance y pasar información crítica por la cadena para que el mando superior decida informado.",
        DOM + ["mando", "limites"],
        {"supports": [DC]}),
    aku("aku-lideres-junior-proactivos-no-reactivos-claim", "claim",
        "Los líderes junior deben ser proactivos, no reactivos: averiguar qué hay que hacer y hacerlo, comunicando a la autoridad superior qué planean hacer en lugar de preguntar «¿qué quieres que haga?».",
        DOM + ["iniciativa", "mando"],
        {"supports": [DC]}),
    aku(TRUST, "claim",
        "Para estar empoderados, los líderes de primera línea deben ejecutar con confianza —entendiendo la misión y el Commander's Intent y confiando en que sus superiores respaldarán sus decisiones—; esto exige flujo bidireccional de «situational awareness»: los seniors empujan información hacia abajo y los junior la empujan hacia arriba.",
        DOM + ["confianza", "comunicacion"],
        {"supports": [DC], "related": ["aku-feedback-hacia-arriba-cadena-claim"]}),
    aku("aku-battlefield-aloofness-concept", "concept",
        "«Battlefield aloofness» (distanciamiento del líder) es el anti-patrón del líder senior tan alejado de las tropas de primera línea que se vuelve inefectivo: aparenta tener el control pero no sabe qué hacen sus tropas ni puede dirigirlas, creando una desconexión entre liderazgo y equipo.",
        DOM + ["anti-patron", "mando"],
        {"related": [DC, "aku-micromanagement-disuelve-en-caos-claim"]}),
    aku("aku-micromanagement-disuelve-en-caos-claim", "claim",
        "Los líderes que intentan asumir demasiado ellos mismos hacen que las operaciones se disuelvan en caos; la solución es empoderar a los líderes de primera línea mediante mando descentralizado, sin micromanagement desde arriba (extremo opuesto al battlefield aloofness).",
        DOM + ["anti-patron", "mando"],
        {"related": [DC]}),
    aku("aku-posicionamiento-del-lider-flexible-claim", "claim",
        "El líder no está atado a una posición fija: debe ser libre de moverse adonde más se le necesite (lo cual cambia durante la operación), ni tan al frente que se vea absorbido por la minucia y pierda la conciencia situacional, ni tan atrás que no sepa qué pasa delante; la posición correcta suele estar en medio, con el grueso de la fuerza.",
        DOM + ["mando", "posicionamiento"],
        {"supports": [DC]}),
    aku(SOC, "concept",
        "«Span of control» (alcance de control) es el número de personas que un líder puede liderar eficazmente; varía con la experiencia y calidad del líder, el nivel de habilidad de las tropas y el grado de caos del entorno; incluye determinar el tamaño óptimo del equipo; implica que superar ese alcance hace perder el control bajo presión.",
        DOM + ["mando", "equipos"],
        {"supports": [DC]}),
    aku("aku-confianza-se-construye-no-se-da-claim", "claim",
        "La confianza no se da a ciegas: se construye con el tiempo mediante conversaciones abiertas, la superación de estrés y el trabajo en emergencias; a veces el jefe debe apartarse y dejar que los líderes junior resuelvan un problema —y respaldarlos aunque no acierten— siempre que la decisión buscara el objetivo estratégico.",
        DOM + ["confianza", "mando"],
        {"supports": [DC], "related": [TRUST]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
akupatch.apply(ROOT, patch_ops)
print(f"cross-links inversos sobre {len(patch_ops)} AKUs existentes:")
for t, rels in ops.items():
    print(f"  {t}: +{rels}")
