# -*- coding: utf-8 -*-
"""Ingesta — Discipline Equals Freedom, Batch 1 (Way of Discipline -> Mind Control)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/discipline-equals-freedom/discipline-equals-freedom.md"
ORIGIN = "Jocko Willink, Discipline Equals Freedom: Field Manual (2017)"
DEF = "aku-discipline-equals-freedom-concept"
ROOT_AKU = "aku-disciplina-raiz-de-toda-buena-cualidad-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "disciplina"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(ROOT_AKU, "concept",
        "La disciplina es «la raíz de todas las buenas cualidades»: el motor de la ejecución diaria y el principio central que vence a la pereza, la apatía y las excusas (no hoy, necesito descansar, lo haré mañana); incluye que sin ella no se alcanzan metas ni se superan obstáculos.",
        DOM,
        {"supports": [DEF]}),
    aku("aku-no-hay-atajo-ni-hack-claim", "claim",
        "No hay atajo ni «hack»: volverse más fuerte, listo, rápido, sano y libre no ocurre por sí solo ni cortando esquinas; solo se logra con trabajo duro, noches y madrugadas, práctica, repetición, sudor y disciplina —el atajo es una mentira—.",
        DOM + ["esfuerzo"],
        {"supports": [ROOT_AKU]}),
    aku("aku-self-discipline-viene-de-dentro-concept", "concept",
        "La autodisciplina (self-discipline) es una fuerza interna que viene del propio YO: la disciplina impuesta desde fuera (un instructor, un gurú) no es fuerte y no sobrevive por sí sola; la autodisciplina surge cuando uno decide ser disciplinado, hacer y ser más; si alguien no es disciplinado es porque aún no lo ha decidido ni creado ni se ha convertido en ello.",
        DOM + ["autodisciplina"],
        {"supports": [DEF], "related": [ROOT_AKU]}),
    aku("aku-empezar-aqui-y-ahora-method", "method",
        "Para vencer la procrastinación y la pereza, el momento y el lugar de empezar son AQUÍ y AHORA: la idea no se ejecuta sola, el libro no se escribe solo, los pesos no se mueven solos; deja de pensar, soñar, investigar y debatir, y empieza a hacerlo —da el primer paso y hazlo realidad—.",
        DOM + ["procrastinacion", "accion"],
        {"supports": [ROOT_AKU], "related": ["aku-default-agresivo-proactivo-dictar-situacion-claim"]}),
    aku("aku-solo-te-puedes-controlar-a-ti-mismo-claim", "claim",
        "No puedes controlar a otras personas ni hacerlas como quieres que sean (serán defectuosas, egoístas, perezosas); la única persona que puedes controlar eres tú; «mata a tus ídolos»: aprende tanto de las fortalezas de otros (imítalas) como de sus defectos (ve qué no hacer), y enfócate en hacerte a ti mismo quien quieres ser, una pequeña decisión cada vez.",
        DOM + ["autocontrol", "responsabilidad"],
        {"related": ["aku-extreme-ownership-concept"]}),
    aku("aku-mind-control-controla-tu-propia-mente-concept", "concept",
        "«Mind control» (control de la mente) significa controlar la propia mente, no la de otros: tú eres tu mente, eres la máquina y puedes controlarla; impón disciplina, poder, positividad y voluntad sobre tu cerebro y declárale «ley marcial»: la debilidad, la pereza, la tristeza, la frustración, la negatividad y el mal genio «no tienen voto»; no dejes que tu mente te controle, contrólala tú.",
        DOM + ["mente", "autocontrol"],
        {"related": ["aku-solo-te-puedes-controlar-a-ti-mismo-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
found = next((o for o in patch_ops if o["id"] == DEF), None)
if found: found["add_source"] = SRC; found["confidence"] = 0.70
else: patch_ops.append({"id": DEF, "add_source": SRC, "confidence": 0.70, "updated": D})
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
print("enrich discipline-equals-freedom: +3a fuente, 0.70")
