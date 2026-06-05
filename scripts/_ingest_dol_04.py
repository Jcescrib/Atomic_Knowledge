# -*- coding: utf-8 -*-
"""Ingesta — The Dichotomy of Leadership, Cap 4 'When to Mentor, When to Fire'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/dichotomy-of-leadership/dichotomy-of-leadership.md"
ORIGIN = "Jocko Willink & Leif Babin, The Dichotomy of Leadership (2018)"
DICH = "aku-dichotomy-of-leadership-concept"
MF = "aku-when-to-mentor-when-to-fire-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "equipos"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(MF, "concept",
        "Dicotomía «cuándo mentorizar, cuándo despedir» (when to mentor, when to fire): equilibrar entre cuidar al individuo (mantenerlo aunque le falte la capacidad) y proteger al equipo (apartar a quien lo perjudica); el líder debe ser leal al individuo y a la vez al equipo, asegurando que cada miembro tenga un impacto neto positivo y no reste a la ejecución de la misión.",
        DOM + ["dicotomia"],
        {"supports": [DICH], "related": ["aku-entrenar-mentorizar-underperformer-claim", "aku-lealtad-mision-sobre-individuo-claim", "aku-no-bad-teams-only-bad-leaders-concept"]}),
    aku("aku-lider-responsable-del-output-maximizar-potencial-claim", "claim",
        "El líder es responsable del output de los individuos de su equipo y su meta es sacar el máximo de cada uno —llevarlo a su potencial máximo para que el equipo alcance el suyo—; pero los humanos tienen limitaciones y no todos encajan en un puesto concreto, así que el líder debe ubicarlos donde sus fortalezas se capitalicen (p. ej. una posición menos técnica), sin descartarlos como inútiles.",
        DOM + ["desempeno", "talento"],
        {"supports": [MF]}),
    aku("aku-invertir-en-uno-puede-perjudicar-al-equipo-claim", "claim",
        "Si el líder sigue invirtiendo tiempo, energía y dinero en un individuo que no mejora, se descuidan otros miembros y prioridades y el equipo empieza a flaquear; además, el resto del equipo puede cuestionar el juicio del líder al verlo volcar recursos en un no-rendidor: la mantra «no hay equipos malos, solo líderes malos» puede volverse en contra aquí.",
        DOM + ["desempeno"],
        {"supports": [MF], "related": ["aku-no-bad-teams-only-bad-leaders-concept", "aku-lealtad-mal-entendida-proteger-underperformers-claim"]}),
    aku("aku-ni-muy-rapido-ni-muy-lento-para-despedir-claim", "claim",
        "El momento correcto para despedir es cuando el líder ha hecho todo lo posible por poner a alguien al nivel sin ver resultados: ni demasiado rápido (sin darle guía y oportunidad suficientes para ganar competencia) ni demasiado lento (cuando ya no muestra potencial y perjudica al equipo); hay que encontrar el equilibrio y mantener la línea.",
        DOM + ["decisiones-dificiles", "timing"],
        {"supports": [MF], "related": ["aku-lealtad-mision-sobre-individuo-claim", "aku-cortar-cancers-del-equipo-rapido-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
