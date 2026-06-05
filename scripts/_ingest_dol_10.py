# -*- coding: utf-8 -*-
"""Ingesta — The Dichotomy of Leadership, Cap 10 'Plan, but Remain Flexible'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/dichotomy-of-leadership/dichotomy-of-leadership.md"
ORIGIN = "Jocko Willink & Leif Babin, The Dichotomy of Leadership (2018)"
DICH = "aku-dichotomy-of-leadership-concept"
PF = "aku-plan-but-remain-flexible-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "planificacion"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(PF, "concept",
        "Dicotomía «planifica, pero mantente flexible» (plan, but remain flexible): la planificación cuidadosa es esencial, pero no se puede planificar para cada contingencia —intentar una solución para cada problema posible abruma al equipo y al proceso y sobrecomplica las decisiones (el exceso de planificación crea problemas mayores)—; pero tampoco hay que irse al otro extremo de no planificar lo suficiente, desestimando amenazas probables.",
        DOM + ["dicotomia", "contingencias"],
        {"supports": [DICH], "related": ["aku-planning-process-estandarizado-concept", "aku-el-enemigo-tiene-voto-concept", "aku-simplicidad-permite-ajuste-rapido-claim"]}),
    aku("aku-priorizar-3-4-contingencias-mas-probables-method", "method",
        "Para no sobreplanificar, enfocarse solo en las contingencias más probables de cada fase de la operación: elegir como máximo las tres o cuatro contingencias más probables de cada fase, más el escenario del peor caso; eso prepara al equipo para ejecutar sin abrumarlo.",
        DOM + ["contingencias", "metodo"],
        {"supports": [PF], "related": ["aku-contingency-planning-anticipar-method", "aku-leaders-checklist-planning-method"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
