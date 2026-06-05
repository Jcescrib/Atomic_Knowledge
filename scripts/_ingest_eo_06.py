# -*- coding: utf-8 -*-
"""Ingesta — Extreme Ownership, Cap 6 'Simple' (Law of Combat #2)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/extreme-ownership/extreme-ownership.md"
ORIGIN = "Jocko Willink & Leif Babin, Extreme Ownership (2015)"
LOC = "aku-laws-of-combat-concept"
SMP = "aku-simple-law-of-combat-concept"
INC = "aku-incentivos-simples-pocas-metricas-method"
ACC = "aku-conexion-accion-consecuencia-conducta-claim"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(SMP, "concept",
        "«Simple» es la segunda Ley del Combate: simplificar tanto como sea posible es crucial para el éxito; los planes y las órdenes deben comunicarse de forma simple, clara y concisa, y cada miembro debe conocer su rol y qué hacer ante las contingencias probables; incluye que la simplicidad aplica también a SOPs, comunicación y procesos; excluye la complejidad que nadie del equipo entiende.",
        DOM + ["combate", "comunicacion", "simplicidad"],
        {"supports": [LOC], "related": ["aku-simple-but-not-easy-concept"]}),
    aku("aku-complejidad-se-agrava-cuando-falla-claim", "claim",
        "Cuando los planes y órdenes son demasiado complicados la gente puede no entenderlos, y cuando algo sale mal —que inevitablemente ocurre— la complejidad agrava los problemas y puede convertirlos en un desastre que se descontrola.",
        DOM + ["complejidad", "riesgo"],
        {"supports": [SMP]}),
    aku("aku-briefear-al-minimo-comun-denominador-claim", "claim",
        "Como líder no importa lo bien que creas haber comunicado una orden, plan o estrategia: si tu equipo no lo capta, no lo has mantenido simple y has fracasado; hay que briefar para asegurar que lo entienda el mínimo común denominador del equipo.",
        DOM + ["comunicacion", "responsabilidad"],
        {"supports": [SMP]}),
    aku("aku-facilitar-preguntas-clarificacion-claim", "claim",
        "La relación operativa debe facilitar que las tropas de primera línea hagan preguntas para clarificar cuando no entienden la misión o las tareas clave; el líder debe fomentar esa comunicación y tomarse el tiempo de explicar hasta que cada miembro lo entienda.",
        DOM + ["comunicacion"],
        {"supports": [SMP], "related": ["aku-preguntar-por-que-method"]}),
    aku("aku-el-enemigo-tiene-voto-concept", "concept",
        "«The enemy gets a vote» (el enemigo tiene voto): por mucho que pienses cómo se desarrollará una operación, el enemigo —o la realidad— hará algo para perturbarla; incluye que casi ninguna misión transcurre según el plan por la cantidad de variables; implica diseñar planes simples que permitan reaccionar a lo imprevisto.",
        DOM + ["combate", "incertidumbre"],
        {"supports": [SMP]}),
    aku("aku-simplicidad-permite-ajuste-rapido-claim", "claim",
        "Si el plan es lo bastante simple, todos lo entienden y cada persona puede ajustar y modificar rápidamente lo que hace; si el plan es demasiado complejo, el equipo no puede hacer ajustes rápidos porque no existe una comprensión base compartida.",
        DOM + ["adaptabilidad", "simplicidad"],
        {"supports": [SMP]}),
    aku(ACC, "claim",
        "Los seres humanos (como todos los animales) necesitan ver la conexión entre la acción y su consecuencia para aprender y reaccionar adecuadamente; si la correlación entre la conducta y la recompensa o el castigo es demasiado débil o poco clara, la conducta no se modificará.",
        DOM + ["incentivos", "conducta"],
        {"supports": [INC]}),
    aku("aku-camino-de-menor-resistencia-claim", "claim",
        "Las personas tienden por naturaleza a tomar el camino de menor resistencia; por eso no se puede contar con que «se tomen el tiempo de descifrar» un sistema complejo: si entenderlo requiere esfuerzo, no lo harán.",
        DOM + ["conducta", "simplicidad"],
        {"related": [ACC]}),
    aku(INC, "method",
        "Para que un plan de incentivos o compensación funcione, mantenlo simple: solo dos a cuatro áreas que medir y puntuar, publicadas de forma visible para que estén siempre presentes en la mente del equipo; así incentiva de verdad la conducta deseada y puede ajustarse con facilidad.",
        DOM + ["incentivos", "simplicidad"],
        {"supports": [SMP]}),
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
