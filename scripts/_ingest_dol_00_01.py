# -*- coding: utf-8 -*-
"""Ingesta — The Dichotomy of Leadership, Introducción + Cap 1 'The Ultimate Dichotomy'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/dichotomy-of-leadership/dichotomy-of-leadership.md"
ORIGIN = "Jocko Willink & Leif Babin, The Dichotomy of Leadership (2018)"
DICH = "aku-dichotomy-of-leadership-concept"
ULT = "aku-ultimate-dichotomy-cuidar-vs-mision-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    # --- Introducción ---
    aku("aku-liderazgo-requiere-balance-no-extremos-claim", "claim",
        "Extreme Ownership es el fundamento del buen liderazgo, pero el liderazgo rara vez exige ideas o actitudes extremas: al contrario, exige equilibrio; el mayor desafío que enfrentan los líderes es encontrar ese equilibrio entre cualidades opuestas.",
        DOM + ["balance"],
        {"supports": [DICH]}),
    # --- Cap 1: The Ultimate Dichotomy ---
    aku(ULT, "concept",
        "La «dicotomía definitiva» (the ultimate dichotomy) es cuidar profundamente de cada miembro del equipo y, a la vez, aceptar los riesgos necesarios para cumplir la misión; es la más difícil de equilibrar; incluye sus dos extremos de fallo: demasiada cercanía (no poder tomar decisiones duras → la misión fracasa) y cuidar demasiado de la misión (sacrificar a la gente sin ganancia → el equipo pierde el respeto y se desmorona).",
        DOM + ["equipos", "mision"],
        {"supports": [DICH], "related": ["aku-cercano-pero-no-demasiado-concept", "aku-lealtad-mision-sobre-individuo-claim"]}),
    aku("aku-burden-of-command-concept", "concept",
        "El «burden of command» (la carga del mando) es la pesada responsabilidad que el líder siente por las vidas —o, en la empresa, los medios de vida— de las personas que trabajan para él; incluye que las decisiones del líder determinan el sustento de su gente.",
        DOM + ["responsabilidad"],
        {"related": [ULT]}),
    aku("aku-cuidar-demasiado-impide-decisiones-duras-claim", "claim",
        "Si el líder desarrolla relaciones demasiado estrechas con su gente, puede no estar dispuesto a hacerles hacer lo necesario, a despedir a individuos aunque convenga a la empresa, o a tener las conversaciones difíciles (decirles que deben mejorar).",
        DOM + ["cercania"],
        {"supports": [ULT], "related": ["aku-cercano-pero-no-demasiado-concept", "aku-lealtad-mal-entendida-proteger-underperformers-claim"]}),
    aku("aku-demasiado-desapegado-dana-al-equipo-claim", "claim",
        "Si el líder está demasiado desapegado del equipo, puede sobrecargarlo, sobreexponerlo o dañarlo sin obtener valor significativo de ese sacrificio, o despedir demasiado rápido para ahorrar, ganándose la reputación de no preocuparse por su gente más allá de su utilidad.",
        DOM + ["desapego"],
        {"supports": [ULT], "related": ["aku-battlefield-aloofness-concept"]}),
    aku("aku-a-veces-hay-que-herir-para-ayudar-claim", "claim",
        "Para ayudar al equipo, a veces el líder tiene que hacerle daño (como un cirujano que corta para salvar una vida); no tomar la decisión dura hace más daño a las personas que se aprecia que tomarla.",
        DOM + ["decisiones-dificiles"],
        {"supports": [ULT]}),
    aku("aku-proteger-a-pocos-arriesga-a-todos-claim", "claim",
        "Preocuparse por unos pocos individuos más que por la misión puede poner en riesgo la misión entera y a todos los demás (proteger 147 empleos puso en riesgo otros 600 y las 5 minas); sobreproteger a algunos sacrifica el bien mayor del equipo.",
        DOM + ["mision", "decisiones-dificiles"],
        {"supports": [ULT], "related": ["aku-lealtad-mision-sobre-individuo-claim", "aku-equipo-gana-o-falla-en-conjunto-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
# enriquecer dichotomy-of-leadership con 2a fuente (+0.10 -> 0.60)
patch_ops.append({"id": DICH, "add_source": SRC, "confidence": 0.60, "updated": D})
akupatch.apply(ROOT, patch_ops)
print("cross + enrich aplicados:")
for o in patch_ops:
    print("  ", o["id"], o.get("add_rel"), "src+" if o.get("add_source") else "", o.get("confidence") or "")
