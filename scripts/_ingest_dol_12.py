# -*- coding: utf-8 -*-
"""Ingesta — The Dichotomy of Leadership, Cap 12 'Focused, but Detached' (cierra libro 2)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/dichotomy-of-leadership/dichotomy-of-leadership.md"
ORIGIN = "Jocko Willink & Leif Babin, The Dichotomy of Leadership (2018)"
ATEN = "aku-atento-detalle-no-obsesionado-concept"
DET = "aku-detach-tactico-estrategico-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku("aku-detachment-default-high-port-claim", "claim",
        "El «detachment» (desapego del detalle) debe ser el mindset y la posición por defecto del líder: como un arma en «high port» (apuntando al cielo, dando un paso atrás para observar con el campo de visión más amplio) en vez de mirar por la mira estrecha; así el líder puede mirar y moverse para dar mando y control y mantener los objetivos generales en perspectiva; si no mantiene una posición por encima de la refriega, falla a su equipo y a la misión.",
        DOM + ["perspectiva", "mando"],
        {"supports": [DET], "related": [ATEN, "aku-pull-off-the-firing-line-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
for tgt in (ATEN, DET):
    found = next((o for o in patch_ops if o["id"] == tgt), None)
    if found: found["add_source"] = SRC; found["confidence"] = 0.60
    else: patch_ops.append({"id": tgt, "add_source": SRC, "confidence": 0.60, "updated": D})
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
print("enrich atento-detalle-no-obsesionado + detach-tactico-estrategico: +2a fuente, 0.60")
