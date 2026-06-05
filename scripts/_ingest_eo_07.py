# -*- coding: utf-8 -*-
"""Ingesta — Extreme Ownership, Cap 7 'Prioritize and Execute' (Law of Combat #3)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/extreme-ownership/extreme-ownership.md"
ORIGIN = "Jocko Willink & Leif Babin, Extreme Ownership (2015)"
LOC = "aku-laws-of-combat-concept"
PAE = "aku-prioritize-and-execute-concept"
RELAX = "aku-relax-look-around-make-a-call-method"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(PAE, "concept",
        "«Prioritize and Execute» (priorizar y ejecutar) es la tercera Ley del Combate: ante múltiples problemas que se acumulan, el líder determina la tarea de mayor prioridad y la ejecuta, una a una, en vez de atacarlas todas a la vez; se verbaliza como «Relax, look around, make a call»; incluye recurrir a este principio cuando uno se siente abrumado.",
        DOM + ["combate", "priorizacion", "decision"],
        {"supports": [LOC], "supported_by": [RELAX], "related": ["aku-main-effort-supporting-efforts-concept"]}),
    aku("aku-lider-abrumado-multiples-tareas-falla-claim", "claim",
        "Incluso el líder más competente puede verse abrumado si intenta abordar múltiples problemas o tareas simultáneamente, y es probable que el equipo fracase en todas ellas; la salida es priorizar y ejecutar la tarea de mayor prioridad primero.",
        DOM + ["foco", "decision"],
        {"supports": [PAE]}),
    aku("aku-contingency-planning-anticipar-method", "method",
        "Para priorizar y ejecutar bajo presión, mantente uno o dos pasos por delante de los problemas en tiempo real mediante planificación de contingencias: anticipa los desafíos probables durante la ejecución y traza la respuesta antes de que ocurran; así el equipo no se ve desbordado, gana decisión y, si está briefado, ejecuta ante la contingencia sin dirección específica (habilita el mando descentralizado).",
        DOM + ["planificacion", "contingencias"],
        {"supports": [PAE]}),
    aku("aku-pull-off-the-firing-line-claim", "claim",
        "Los líderes, sobre todo los de la cima, deben «pull themselves off the firing line» (apartarse de la línea de fuego): dar un paso atrás y mantener el cuadro estratégico para priorizar correctamente, y luego ayudar a sus líderes subordinados a priorizar sus esfuerzos.",
        DOM + ["estrategia", "perspectiva"],
        {"supports": [PAE], "related": ["aku-detach-tactico-estrategico-concept"]}),
    aku("aku-prioridades-cambian-comunicar-claim", "claim",
        "Las prioridades pueden cambiar rápida y constantemente; cuando lo hacen, comunicar ese cambio al resto del equipo —hacia arriba y hacia abajo en la cadena de mando— es crítico para mantener la coordinación.",
        DOM + ["comunicacion", "adaptabilidad"],
        {"supports": [PAE]}),
    aku("aku-target-fixation-concept", "concept",
        "«Target fixation» (fijación en un objetivo) es el anti-patrón por el que un equipo se obsesiona con un único problema y no reconoce cuándo la máxima prioridad se ha desplazado a otra cosa; incluye perder la capacidad de re-priorizar; excluye mantener la conciencia situacional de otros problemas emergentes.",
        DOM + ["anti-patron", "foco"],
        {"related": [PAE]}),
    aku("aku-prioritize-and-execute-pasos-method", "method",
        "Para implementar Prioritize and Execute: (1) evaluar el problema de mayor prioridad; (2) exponer en términos simples, claros y concisos el esfuerzo de máxima prioridad; (3) desarrollar la solución buscando input de líderes clave y del equipo cuando sea posible; (4) dirigir la ejecución concentrando todos los esfuerzos y recursos en esa tarea; (5) pasar al siguiente problema prioritario y repetir; (6) cuando las prioridades cambien, pasar la conciencia situacional arriba y abajo; (7) no dejar que el foco en una prioridad cause target fixation.",
        DOM + ["priorizacion", "procedimiento"],
        {"supports": [PAE], "related": ["aku-target-fixation-concept"]}),
    aku("aku-decisively-engaged-concept", "concept",
        "«Decisively engaged» (comprometido decisivamente) describe una unidad atrapada en un combate duro del que no puede maniobrar ni extricarse —no puede retirarse, debe ganar—; se usa como metáfora de una empresa demasiado dispersa que libra demasiadas «batallas» (iniciativas) a la vez.",
        DOM + ["combate", "foco"],
        {}),
    aku("aku-enfocar-una-iniciativa-a-la-vez-claim", "claim",
        "No hay que dispersarse en muchas iniciativas a la vez: enfoca todo el esfuerzo en una prioridad hasta completarla o darle un impulso real, y solo entonces pasa a la siguiente; estando demasiado disperso no se «mueve la aguja» en ninguna.",
        DOM + ["foco", "ejecucion"],
        {"supports": [PAE], "related": ["aku-decisively-engaged-concept"]}),
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
