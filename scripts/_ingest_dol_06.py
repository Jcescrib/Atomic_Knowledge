# -*- coding: utf-8 -*-
"""Ingesta — The Dichotomy of Leadership, Cap 6 'Aggressive, Not Reckless'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/dichotomy-of-leadership/dichotomy-of-leadership.md"
ORIGIN = "Jocko Willink & Leif Babin, The Dichotomy of Leadership (2018)"
DICH = "aku-dichotomy-of-leadership-concept"
AGG = "aku-aggressive-not-reckless-concept"
DEFAULT = "aku-default-agresivo-proactivo-dictar-situacion-claim"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(AGG, "concept",
        "Dicotomía «agresivo, no temerario» (aggressive, not reckless): el líder debe ser agresivo —proactivo, tomar acción para resolver problemas, porque no se resuelven solos— pero equilibrarlo con pensamiento y análisis cuidadosos para asegurar que los riesgos se han evaluado y mitigado; ser demasiado agresivo sin pensamiento crítico es temerario y puede llevar al desastre.",
        DOM + ["dicotomia", "riesgo"],
        {"supports": [DICH], "related": [DEFAULT, "aku-valiente-no-temerario-concept", "aku-calcular-y-mitigar-riesgo-claim"]}),
    aku("aku-agresivo-significa-proactivo-no-iracundo-claim", "claim",
        "«Agresivo» significa proactivo, no iracundo: no implica enfadarse, perder los estribos ni ser agresivo con las personas; el líder debe tratar siempre con profesionalidad a subordinados, pares, superiores y clientes; perder los estribos es señal de debilidad; la agresión que gana se dirige a resolver problemas y cumplir la misión, no contra las personas.",
        DOM + ["proactividad", "profesionalidad"],
        {"supports": [AGG], "related": ["aku-calmado-no-robotico-concept"]}),
    aku("aku-hesitar-a-veces-es-prudente-claim", "claim",
        "A veces la vacilación es prudente: detenerse un momento permite entender mejor la situación para reaccionar correctamente (¿es un reconocimiento por fuego?, ¿una finta?, ¿un señuelo hacia una emboscada?); un instante de consideración puede revelar las verdaderas intenciones del adversario, mientras que actuar sin pensamiento crítico es temerario.",
        DOM + ["prudencia", "decision"],
        {"supports": [AGG]}),
    aku("aku-disease-of-victory-concept", "concept",
        "La «disease of victory» (enfermedad de la victoria) es el patrón por el que unos pocos éxitos producen un exceso de confianza en la propia destreza mientras se subestiman las capacidades del enemigo o competidor; es un contribuyente principal a la temeridad; el líder debe combatirla para que el equipo, pese al éxito, nunca caiga en la complacencia.",
        DOM + ["sesgos", "complacencia"],
        {"supports": [AGG], "related": ["aku-nunca-complacencia-subestimar-enemigo-claim", "aku-confident-but-not-cocky-concept"]}),
    aku("aku-sopesar-riesgo-recompensa-coste-inaccion-claim", "claim",
        "El riesgo de cualquier acción debe sopesarse cuidadosamente frente a las recompensas potenciales del éxito de la misión, y a su vez frente al coste de la inacción; equilibrar agresión y cautela exige pesar ambos lados y no «correr hacia la propia muerte» solo por el instinto de actuar.",
        DOM + ["riesgo", "decision"],
        {"supports": [AGG], "related": ["aku-calcular-y-mitigar-riesgo-claim", "aku-esperar-certeza-causa-paralisis-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
# enrich default-agresivo con 2a fuente
found = next((o for o in patch_ops if o["id"] == DEFAULT), None)
if found: found["add_source"] = SRC; found["confidence"] = 0.60
else: patch_ops.append({"id": DEFAULT, "add_source": SRC, "confidence": 0.60, "updated": D})
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
print("enrich default-agresivo: +2a fuente, 0.60")
