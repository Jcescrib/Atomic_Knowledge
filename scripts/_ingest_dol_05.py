# -*- coding: utf-8 -*-
"""Ingesta — The Dichotomy of Leadership, Cap 5 'Train Hard, but Train Smart'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/dichotomy-of-leadership/dichotomy-of-leadership.md"
ORIGIN = "Jocko Willink & Leif Babin, The Dichotomy of Leadership (2018)"
DICH = "aku-dichotomy-of-leadership-concept"
TR = "aku-train-hard-but-train-smart-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "entrenamiento"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(TR, "concept",
        "Dicotomía «entrena duro pero entrena inteligente» (train hard, but train smart): el entrenamiento debe ser duro —empujar al equipo más allá de su zona de confort, porque no hay crecimiento en la comodidad— pero a la vez inteligente —no tan brutal que aplaste, desmoralice o abrume hasta impedir el aprendizaje—; se equilibra con tres aspectos: realismo, fundamentos y repetición.",
        DOM + ["dicotomia"],
        {"supports": [DICH]}),
    aku("aku-train-how-you-fight-claim", "claim",
        "«Entrenas como peleas y peleas como entrenas» (you train how you fight): el mejor entrenamiento empuja al equipo mucho más allá de su zona de confort para que aprenda de sus errores en el entrenamiento y así no los cometa en la realidad; no hay crecimiento en la zona de confort.",
        DOM + ["zona-de-confort"],
        {"supports": [TR]}),
    aku("aku-entrenamiento-realismo-fundamentos-repeticion-method", "method",
        "El buen entrenamiento se enfoca en tres aspectos: (1) realismo —cada escenario basado en algo probable en la realidad, con tomas inmediatamente aplicables y recreando el caos y la incertidumbre, incl. role-plays de alta presión—; (2) fundamentos —dominar las tácticas básicas que no cambian, porque las «tácticas avanzadas» son inútiles sin los fundamentos—; (3) repetición —entrenamiento continuo para todos, porque cada uno mejora con las iteraciones—.",
        DOM + ["metodo"],
        {"supports": [TR], "related": ["aku-repetir-tarea-hasta-estandar-method"]}),
    aku("aku-entrenamiento-desde-abajo-no-desde-arriba-claim", "claim",
        "Los mejores programas de entrenamiento no se orquestan desde arriba sino que se impulsan desde abajo —los líderes de primera línea más cercanos a la acción y las lecciones aprendidas—; hay que tomar Extreme Ownership del entrenamiento y usar a los miembros más capaces para dirigirlo; «no hay presupuesto» y «no hay tiempo» para entrenar no son excusas válidas.",
        DOM + ["iniciativa"],
        {"supports": [TR], "related": ["aku-extreme-ownership-concept", "aku-analisis-constante-medir-efectividad-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
