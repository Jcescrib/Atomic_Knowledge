# -*- coding: utf-8 -*-
"""Ingesta — The Dichotomy of Leadership, Cap 3 'Resolute, but Not Overbearing'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/dichotomy-of-leadership/dichotomy-of-leadership.md"
ORIGIN = "Jocko Willink & Leif Babin, The Dichotomy of Leadership (2018)"
DICH = "aku-dichotomy-of-leadership-concept"
RES = "aku-resolute-but-not-overbearing-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(RES, "concept",
        "Dicotomía «resoluto pero no prepotente» (resolute but not overbearing): el líder no puede ser ni demasiado indulgente ni dominante; debe fijar estándares altos y empujar al equipo a alcanzarlos, pero sin ser inflexible en asuntos de poca importancia estratégica; implica evaluar cuándo mantener la línea y dónde dar holgura, y cuándo escuchar a los subordinados y cederles ownership.",
        DOM + ["dicotomia", "estandares"],
        {"supports": [DICH], "related": ["aku-agresivo-no-prepotente-concept", "aku-no-es-lo-que-predicas-sino-lo-que-toleras-claim"]}),
    aku("aku-leadership-capital-concept", "concept",
        "El «leadership capital» (capital de liderazgo) es la cantidad finita de poder o influencia que posee un líder: se dilapida tontamente insistiendo en asuntos triviales y estratégicamente irrelevantes, se adquiere lentamente construyendo confianza al demostrar que se tiene en mente el bien a largo plazo del equipo y la misión, y se usa sabiamente priorizando dónde no se pueden comprometer los estándares (manteniendo la línea ahí) mientras se da holgura en lo menos crítico.",
        DOM + ["poder", "influencia"],
        {"supports": [RES], "related": ["aku-confianza-se-construye-no-se-da-claim"]}),
    aku("aku-enforzar-estandares-siempre-con-el-porque-claim", "claim",
        "Cuando un líder debe mantener la línea y hacer cumplir un estándar, debe hacerlo siempre explicando por qué es importante, cómo ayuda a cumplir la misión y cuáles son las consecuencias de fallar —nunca con un «porque lo digo yo»—, ya que el «porque lo digo yo» genera mucha más resistencia y dificulta que el equipo alcance el estándar.",
        DOM + ["estandares", "comunicacion"],
        {"supports": [RES], "related": ["aku-senior-debe-explicar-el-porque-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
