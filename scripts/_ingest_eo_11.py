# -*- coding: utf-8 -*-
"""Ingesta — Extreme Ownership, Cap 11 'Decisiveness amid Uncertainty'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/extreme-ownership/extreme-ownership.md"
ORIGIN = "Jocko Willink & Leif Babin, Extreme Ownership (2015)"
DEC = "aku-decisiveness-amid-uncertainty-concept"
CANCER = "aku-cortar-cancers-del-equipo-rapido-claim"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "decision"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(DEC, "concept",
        "«Decisiveness amid uncertainty» (decisión en medio de la incertidumbre) es la capacidad del líder de actuar con decisión pese al caos y la información incompleta, tomando la mejor decisión posible con lo disponible en el momento y ajustándola rápido según evolucione; incluye no dejarse paralizar por el miedo (que lleva a la inacción); excluye esperar a tener el cuadro completo.",
        DOM + ["incertidumbre"],
        {"related": ["aku-relax-look-around-make-a-call-method", "aku-prioritize-and-execute-concept", "aku-contingency-planning-anticipar-method"]}),
    aku("aku-no-hay-solucion-100-correcta-claim", "claim",
        "No existe una solución 100% correcta y el cuadro nunca está completo; el líder debe estar cómodo con ello, decidir con prontitud y estar listo para ajustar la decisión rápidamente ante nueva información.",
        DOM + ["incertidumbre"],
        {"supports": [DEC], "related": ["aku-el-enemigo-tiene-voto-concept"]}),
    aku("aku-esperar-certeza-causa-paralisis-claim", "claim",
        "Esperar a la solución 100% correcta y segura conduce a la demora, la indecisión y la incapacidad de ejecutar; la recopilación de inteligencia e investigación son importantes pero deben usarse con expectativas realistas y no impedir la toma de decisiones ágil, que a menudo marca la diferencia entre victoria y derrota.",
        DOM + ["paralisis-analisis"],
        {"supports": [DEC]}),
    aku("aku-conjetura-educada-method", "method",
        "Para decidir bajo incertidumbre, el líder hace una «conjetura educada» (educated guess) basada en la experiencia previa, el conocimiento de cómo opera el adversario, los desenlaces probables y la inteligencia disponible en el momento inmediato.",
        DOM + ["incertidumbre", "heuristica"],
        {"supports": [DEC]}),
    aku("aku-default-agresivo-proactivo-dictar-situacion-claim", "claim",
        "El ajuste por defecto de un líder debe ser agresivo —proactivo en lugar de reactivo—: en vez de dejar que la situación dicte sus decisiones, debe dictar él la situación; el enfoque pasivo de «esperar a ver» (decidir no decidir) suele ser una decisión inferior.",
        DOM + ["proactividad"],
        {"supports": [DEC], "related": ["aku-lideres-junior-proactivos-no-reactivos-claim"]}),
    aku("aku-lider-percibido-como-decisivo-claim", "claim",
        "El líder necesita ser percibido como decisivo y dispuesto a tomar decisiones difíciles, no como indeciso ni como alguien al que se puede tener de rehén con amenazas o ultimátums; la primera línea respeta la decisión firme y su lealtad aumenta.",
        DOM + ["percepcion"],
        {"supports": [DEC]}),
    aku(CANCER, "claim",
        "Los individuos destructivos o tóxicos son «cánceres»: su actitud metastatiza y contagia la negatividad al resto del equipo; cuanto antes se les extirpe, menos daño harán, menos negatividad propagarán y a menos gente arrastrarán consigo.",
        DOM + ["equipos", "toxicidad"],
        {"related": ["aku-tortured-genius-concept", "aku-lealtad-mision-sobre-individuo-claim"]}),
    aku("aku-battlefield-promotion-concept", "concept",
        "Una «battlefield promotion» (promoción en el campo de batalla) es ascender a personal de primera línea de alto potencial para cubrir a líderes que se retiran o se eliminan, partiendo de que el conocimiento profundo y real de los proyectos suele estar en la primera línea, no en los mandos salientes.",
        DOM + ["talento", "ascensos"],
        {"related": [CANCER]}),
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
