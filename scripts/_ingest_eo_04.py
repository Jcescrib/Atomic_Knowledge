# -*- coding: utf-8 -*-
"""Ingesta — Extreme Ownership, Cap 4 'Check the Ego'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/extreme-ownership/extreme-ownership.md"
ORIGIN = "Jocko Willink & Leif Babin, Extreme Ownership (2015)"
EO = "aku-extreme-ownership-concept"
CHK = "aku-check-the-ego-concept"
CNC = "aku-confident-but-not-cocky-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "ego"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(CHK, "concept",
        "«Check the Ego» (controlar el ego) es el principio de mantener el ego a raya y operar con un alto grado de humildad; incluye que implementar Extreme Ownership lo exige —admitir errores, asumir responsabilidad y planificar para superar desafíos—; excluye dejar que el ego nuble la evaluación honesta de uno mismo y del equipo.",
        DOM + ["humildad"],
        {"supports": [EO], "related": ["aku-humildad-asumir-errores-claim", "aku-mejores-lideres-mision-no-ego-claim"]}),
    aku("aku-ego-nubla-todo-claim", "claim",
        "El ego nubla y perturba todo: el proceso de planificación, la capacidad de aceptar buenos consejos y la de aceptar la crítica constructiva, e incluso puede ahogar el instinto de autopreservación.",
        DOM, {"supports": [CHK]}),
    aku("aku-ego-bueno-vs-destructivo-claim", "claim",
        "Todo el mundo tiene ego, y el ego impulsa a las personas más exitosas (querer ganar y ser el mejor), lo cual es bueno; pero cuando el ego nubla el juicio e impide ver el mundo como es, o cuando las agendas personales pesan más que el equipo y la misión, el ego se vuelve destructivo y el desempeño se resiente.",
        DOM, {"supports": [CHK]}),
    aku("aku-el-ego-mas-dificil-es-el-propio-claim", "claim",
        "A menudo el ego más difícil de gestionar es el de uno mismo.",
        DOM, {"supports": [CHK]}),
    aku("aku-ego-impide-evaluacion-honesta-claim", "claim",
        "El ego puede impedir que un líder realice una evaluación honesta y realista de su propio desempeño y del de su equipo.",
        DOM + ["autoevaluacion"],
        {"supports": [CHK], "related": ["aku-ver-problemas-lente-objetiva-claim", "aku-lideres-nunca-satisfechos-mejora-continua-claim"]}),
    aku(CNC, "concept",
        "«Confident but not cocky» (seguro pero no chulesco) es el principio de ser confiado en las propias habilidades y estar ansioso por misiones difíciles, pero sin caer en la arrogancia; incluye tomarse en serio al adversario y no creerse demasiado bueno para fallar; excluye la complacencia.",
        DOM + ["confianza"],
        {"related": [CHK]}),
    aku("aku-nunca-complacencia-subestimar-enemigo-claim", "claim",
        "Nunca hay que caer en la complacencia: no se puede pensar que uno es demasiado bueno para fallar ni que el adversario no es capaz, letal y ansioso por explotar las propias debilidades.",
        DOM + ["complacencia"],
        {"supports": [CNC]}),
    aku("aku-check-ego-asumiendo-culpa-primero-method", "method",
        "Para desactivar un choque de egos con un subordinado, el líder controla su propio ego asumiendo primero la culpa («nuestro equipo cometió un error y es culpa mía; no fui tan claro como debía»); al quitar el ego de en medio, el otro puede ver el problema sin la visión nublada por su propio ego, en lugar de enfrentarse en un choque de egos.",
        DOM + ["comunicacion", "responsabilidad"],
        {"supports": [CHK], "related": ["aku-lider-mirar-al-espejo-claim"]}),
    aku("aku-culpar-subordinado-natural-pero-contraproducente-claim", "claim",
        "Es natural y propio de la naturaleza humana que un líder culpe a los subordinados cuando algo sale mal (al ego no le gusta cargar con la culpa), pero es contraproducente: provoca un choque de egos; corresponde al líder ver dónde falló él en comunicar y ayudar a su gente a entender sus roles y el impacto de sus actos en el cuadro estratégico.",
        DOM + ["comunicacion"],
        {"supports": [CHK], "related": ["aku-culpar-se-contagia-claim"]}),
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
