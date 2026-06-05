# -*- coding: utf-8 -*-
"""Ingesta — The Dichotomy of Leadership, Cap 8 'Hold People Accountable, but Don't Hold Their Hands'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/dichotomy-of-leadership/dichotomy-of-leadership.md"
ORIGIN = "Jocko Willink & Leif Babin, The Dichotomy of Leadership (2018)"
DICH = "aku-dichotomy-of-leadership-concept"
ACC = "aku-accountability-no-como-herramienta-principal-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "accountability"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(ACC, "concept",
        "Dicotomía «exige cuentas, pero no les lleves de la mano»: la accountability (rendición de cuentas) es una herramienta importante pero no debe ser la principal; hay que equilibrarla con hacer entender el porqué, empoderar a los subordinados y confiar en que harán lo correcto sin supervisión directa; apoyarse demasiado en la accountability consume el tiempo y el foco del líder e inhibe la confianza, el crecimiento y el desarrollo de los subordinados.",
        DOM + ["dicotomia"],
        {"supports": [DICH], "related": ["aku-believe-in-the-mission-concept", "aku-decentralized-command-concept"]}),
    aku("aku-accountability-no-escala-y-ciega-al-lider-claim", "claim",
        "Inspeccionar repetidamente logra el 100% de cumplimiento de una tarea, pero no escala: con múltiples subordinados y tareas el líder no puede inspeccionarlas todas, y además le atrapa mirando hacia abajo y hacia dentro, sin capacidad de mirar hacia arriba (construir relaciones e influir en la estrategia) ni hacia fuera (anticipar operaciones futuras); y sin supervisión presente, el subordinado puede dejar de ejecutar bien.",
        DOM + ["escalabilidad"],
        {"supports": [ACC], "related": ["aku-leading-up-the-chain-concept", "aku-micromanagement-mata-iniciativa-claim"]}),
    aku("aku-accountability-temporal-luego-soltar-claim", "claim",
        "La accountability debe usarse cuando hace falta —si un subordinado no rinde pese a entender el porqué, el impacto y tener ownership, el líder mantiene la línea, baja al detalle y micromanagea para reencauzarlo— pero el líder no puede quedarse ahí: debe acabar dando margen para que rinda por su impulso intrínseco basado en entender el porqué, no por ser vigilado.",
        DOM + ["estandares"],
        {"supports": [ACC], "related": ["aku-no-es-lo-que-predicas-sino-lo-que-toleras-claim", "aku-corregir-micromanagement-method"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
