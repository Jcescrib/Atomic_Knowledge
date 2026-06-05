# -*- coding: utf-8 -*-
"""Ingesta — Extreme Ownership, Cap 5 'Cover and Move' (Law of Combat #1)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/extreme-ownership/extreme-ownership.md"
ORIGIN = "Jocko Willink & Leif Babin, Extreme Ownership (2015)"
LOC = "aku-laws-of-combat-concept"
CAM = "aku-cover-and-move-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "equipos"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(CAM, "concept",
        "«Cover and Move» (cubrir y avanzar) es la primera Ley del Combate y la táctica más fundamental —quizá la única—: significa trabajo en equipo; todos los elementos del equipo mayor trabajan juntos y se apoyan mutuamente por un propósito único; incluye romper silos y entender de quién dependes y quién depende de ti; excluye operar de forma independiente o unos contra otros.",
        DOM + ["combate", "teamwork"],
        {"supports": [LOC]}),
    aku("aku-romper-silos-interdependencia-claim", "claim",
        "Los departamentos y grupos dentro de un equipo deben romper los silos, depender unos de otros y entender quién depende de ellos; si abandonan este principio y operan de forma independiente o trabajan unos contra otros, los resultados pueden ser catastróficos para el desempeño global.",
        DOM + ["silos", "interdependencia"],
        {"supports": [CAM]}),
    aku("aku-subteams-compiten-pierden-perspectiva-claim", "claim",
        "Cuando los equipos pequeños dentro del equipo se enfocan tanto en sus tareas inmediatas, olvidan lo que hacen los demás o cómo dependen de otros, empiezan a competir entre sí y surgen animosidad, culpa y fricción que inhiben el desempeño del equipo global.",
        DOM + ["fricciones"],
        {"supports": [CAM]}),
    aku("aku-lider-mantiene-perspectiva-estrategica-claim", "claim",
        "Corresponde al líder mantener continuamente la perspectiva de la misión estratégica y recordar al equipo que forma parte de un equipo mayor cuya misión es lo primordial, por encima de las tareas inmediatas de cada subgrupo.",
        DOM + ["estrategia", "perspectiva"],
        {"supports": [CAM], "related": ["aku-detach-tactico-estrategico-concept", "aku-parte-de-algo-mas-grande-claim"]}),
    aku("aku-main-effort-supporting-efforts-concept", "concept",
        "«Main effort y supporting efforts» (esfuerzo principal y esfuerzos de apoyo): aunque cada miembro del equipo es crítico para el éxito, hay que identificar con claridad cuál es el esfuerzo principal y cuáles los esfuerzos de apoyo en cada momento; incluye que todos los esfuerzos de apoyo se subordinan al principal.",
        DOM + ["priorizacion", "combate"],
        {"supports": [CAM]}),
    aku("aku-equipo-gana-o-falla-en-conjunto-claim", "claim",
        "Si el equipo global fracasa, todos fracasan, aunque un miembro o elemento concreto haya hecho bien su trabajo; y cuando el equipo triunfa, todos los que lo integran y lo apoyan comparten el éxito: cumplir la misión estratégica es la prioridad más alta.",
        DOM + ["exito-colectivo"],
        {"supports": [CAM]}),
    aku("aku-competidor-es-externo-no-interno-claim", "claim",
        "El enemigo o competidor está fuera (las demás empresas que pugnan por tus clientes), no dentro de los muros de la organización: los departamentos y filiales bajo la misma estructura de liderazgo están en el mismo equipo, y hay que superar la mentalidad de «nosotros contra ellos» y apoyarse mutuamente.",
        DOM + ["competencia", "cultura"],
        {"supports": [CAM]}),
    aku("aku-cover-and-move-construir-relacion-method", "method",
        "Para aplicar Cover and Move con otro equipo que no controlas: comprométete y construye una relación personal con ellos, explícales qué necesitas de ellos y por qué, pregúntales qué puedes hacer para ayudarles a darte lo que necesitas, y hazlos parte de tu equipo, no la excusa de tu equipo.",
        DOM + ["colaboracion", "comunicacion"],
        {"supports": [CAM]}),
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
