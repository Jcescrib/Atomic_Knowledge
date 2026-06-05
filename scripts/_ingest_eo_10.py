# -*- coding: utf-8 -*-
"""Ingesta — Extreme Ownership, Cap 10 'Leading Up and Down the Chain of Command'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/extreme-ownership/extreme-ownership.md"
ORIGIN = "Jocko Willink & Leif Babin, Extreme Ownership (2015)"
EO = "aku-extreme-ownership-concept"
DOWN = "aku-leading-down-the-chain-concept"
UP = "aku-leading-up-the-chain-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "cadena-de-mando"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(DOWN, "concept",
        "«Leading down the chain» (liderar hacia abajo) es comunicar de forma rutinaria a los líderes junior y a las tropas cómo su rol contribuye al éxito del cuadro general, para que conecten sus operaciones del día a día con los objetivos estratégicos; incluye salir del despacho, conversar cara a cara, observar a la primera línea en acción y leerlos en el Commander's Intent; facilita el mando descentralizado; excluye asumir que la conexión es obvia para ellos.",
        DOM,
        {"related": ["aku-decentralized-command-concept", "aku-commanders-intent-concept", "aku-senior-debe-explicar-el-porque-claim"]}),
    aku("aku-conexion-rol-big-picture-no-intuitiva-claim", "claim",
        "La conexión entre el trabajo diario y los objetivos estratégicos no es intuitiva y nunca resulta tan obvia para los empleados de base como los líderes asumen; por eso el líder debe comunicarla de forma rutinaria para que el equipo pueda priorizar sus esfuerzos en un entorno dinámico.",
        DOM + ["comunicacion"],
        {"supports": [DOWN], "related": ["aku-senior-debe-explicar-el-porque-claim"]}),
    aku(UP, "concept",
        "«Leading up the chain» (liderar hacia arriba) es el compromiso táctico con el jefe inmediato (o el mando superior) para obtener las decisiones y el apoyo que el equipo necesita para cumplir su misión, empujando «situational awareness» hacia arriba; incluye que el liderazgo no solo fluye hacia abajo sino también hacia arriba; es una aplicación de Extreme Ownership («poseer todo en tu mundo», incluidos los jefes).",
        DOM,
        {"supported_by": [EO], "related": [DOWN]}),
    aku("aku-boss-no-da-soporte-culpate-primero-claim", "claim",
        "Si tu jefe no toma decisiones a tiempo o no da el apoyo que tú y tu equipo necesitáis, no culpes al jefe: cúlpate primero a ti mismo y examina qué puedes hacer para transmitir mejor la información crítica que permita tomar las decisiones y asignar el apoyo.",
        DOM + ["responsabilidad"],
        {"supports": [UP], "related": ["aku-lider-mirar-al-espejo-claim"]}),
    aku("aku-leading-up-requiere-influencia-no-autoridad-claim", "claim",
        "Liderar hacia arriba exige mucha más astucia y habilidad que liderar hacia abajo: no puedes apoyarte en la autoridad de tu posición, sino usar la influencia, la experiencia, el conocimiento, la comunicación y la máxima profesionalidad.",
        DOM + ["influencia"],
        {"supports": [UP]}),
    aku("aku-humildad-aceptar-prioridades-superiores-claim", "claim",
        "Al empujar tus necesidades hacia arriba, debes comprender que el jefe asigna recursos limitados con el cuadro general en mente: tu equipo puede no ser el esfuerzo prioritario en ese momento, o la dirección puede haber elegido otro rumbo; hay que tener la humildad de entenderlo y aceptarlo.",
        DOM + ["humildad", "priorizacion"],
        {"supports": [UP]}),
    aku("aku-presentar-frente-unido-claim", "claim",
        "Uno de los trabajos más importantes de un líder es apoyar a su propio jefe: la cadena de mando debe presentar siempre un frente unido ante las tropas, porque una muestra pública de descontento o desacuerdo con la cadena de mando socava la autoridad de los líderes de todos los niveles y es catastrófica para el desempeño.",
        DOM + ["cohesion"],
        {"supports": [UP]}),
    aku("aku-ejecutar-decision-como-propia-claim", "claim",
        "Los líderes no siempre estarán de acuerdo, pero una vez terminado el debate sobre un curso de acción y tomada la decisión por el jefe —aunque sea una que tú argumentaste en contra—, debes ejecutar el plan como si fuera tuyo.",
        DOM + ["compromiso"],
        {"supports": [UP], "related": ["aku-believe-in-the-mission-concept"]}),
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
