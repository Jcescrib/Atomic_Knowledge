# -*- coding: utf-8 -*-
"""Ingesta — The Dichotomy of Leadership, Cap 9 'A Leader and a Follower'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/dichotomy-of-leadership/dichotomy-of-leadership.md"
ORIGIN = "Jocko Willink & Leif Babin, The Dichotomy of Leadership (2018)"
LYS = "aku-lider-y-seguidor-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku("aku-excepcion-resistir-ordenes-ilegales-inmorales-claim", "claim",
        "Un líder subordinado debe seguir y apoyar la cadena de mando incluso cuando discrepa; solo debe plantarse firme contra las directivas de sus superiores si las órdenes son ilegales, inmorales, no éticas o suponen un riesgo significativo para la vida, la integridad o el éxito estratégico de la organización —y esos casos deben ser raros—; no seguir socava la autoridad de toda la cadena (incluida la del propio líder rebelde) y crea antagonismo que perjudica al equipo.",
        DOM + ["cadena-de-mando", "etica"],
        {"related": [LYS, "aku-ejecutar-decision-como-propia-claim", "aku-presentar-frente-unido-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
# enrich lider-y-seguidor con 2a fuente
found = next((o for o in patch_ops if o["id"] == LYS), None)
if found: found["add_source"] = SRC; found["confidence"] = 0.60
else: patch_ops.append({"id": LYS, "add_source": SRC, "confidence": 0.60, "updated": D})
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
print("enrich lider-y-seguidor: +2a fuente, 0.60")
