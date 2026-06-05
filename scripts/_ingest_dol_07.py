# -*- coding: utf-8 -*-
"""Ingesta — The Dichotomy of Leadership, Cap 7 'Disciplined, Not Rigid'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/dichotomy-of-leadership/dichotomy-of-leadership.md"
ORIGIN = "Jocko Willink & Leif Babin, The Dichotomy of Leadership (2018)"
DICH = "aku-dichotomy-of-leadership-concept"
DEF = "aku-discipline-equals-freedom-concept"
DR = "aku-disciplined-not-rigid-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "disciplina"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(DR, "concept",
        "Dicotomía «disciplinado, no rígido» (disciplined, not rigid): los SOPs, procesos repetibles y metodologías consistentes ayudan, pero la disciplina excesiva ahoga el pensamiento libre; hay que equilibrar los procedimientos disciplinados con la libertad de aplicar el sentido común, romper los SOPs cuando es necesario, pensar alternativas y adaptarse a la realidad.",
        DOM + ["dicotomia", "sop"],
        {"supports": [DICH], "related": [DEF, "aku-simple-law-of-combat-concept"]}),
    aku("aku-disciplina-da-libertad-de-maniobra-claim", "claim",
        "Cuanta más disciplina ejerce un equipo (SOPs), más libertad de maniobra tiene: en vez de crear un plan desde cero, sigue los SOPs para el grueso del plan y hace pequeños ajustes; los SOPs son una línea de la que desviarse, no una atadura, y dan libertad para actuar con rapidez.",
        DOM + ["sop", "libertad"],
        {"supports": [DR], "related": [DEF, "aku-planning-process-estandarizado-concept"]}),
    aku("aku-exceso-de-sops-ahoga-iniciativa-claim", "claim",
        "Demasiados SOPs estrictos inhiben la voluntad y la capacidad de pensar de los líderes subordinados; llevado al extremo, los líderes confinados a procedimientos estrictos se limitan a seguirlos aun cuando es evidente que conducen al fracaso, en vez de hacer los cambios necesarios.",
        DOM + ["sop", "iniciativa"],
        {"supports": [DR], "related": ["aku-micromanagement-mata-iniciativa-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
found = next((o for o in patch_ops if o["id"] == DEF), None)
if found: found["add_source"] = SRC; found["confidence"] = 0.60
else: patch_ops.append({"id": DEF, "add_source": SRC, "confidence": 0.60, "updated": D})
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
print("enrich discipline-equals-freedom: +2a fuente, 0.60")
