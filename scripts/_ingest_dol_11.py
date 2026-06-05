# -*- coding: utf-8 -*-
"""Ingesta — The Dichotomy of Leadership, Cap 11 'Humble, Not Passive'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/dichotomy-of-leadership/dichotomy-of-leadership.md"
ORIGIN = "Jocko Willink & Leif Babin, The Dichotomy of Leadership (2018)"
HNP = "aku-humilde-no-pasivo-concept"
CHK = "aku-check-the-ego-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "humildad"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku("aku-humildad-es-la-cualidad-mas-importante-claim", "claim",
        "La humildad es la cualidad más importante en un líder: cuando se destituía a líderes SEAL casi nunca era por ser tácticamente flojos, no estar en forma o ser incompetentes, sino casi siempre por no ser humildes —no poder controlar el ego, rechazar la crítica constructiva o no asumir sus errores—; la humildad es esencial para construir relaciones sólidas arriba y abajo de la cadena de mando.",
        DOM,
        {"supports": [CHK], "related": [HNP, "aku-el-ego-mas-dificil-es-el-propio-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
found = next((o for o in patch_ops if o["id"] == HNP), None)
if found: found["add_source"] = SRC; found["confidence"] = 0.60
else: patch_ops.append({"id": HNP, "add_source": SRC, "confidence": 0.60, "updated": D})
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
print("enrich humilde-no-pasivo: +2a fuente, 0.60")
