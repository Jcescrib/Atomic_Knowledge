# -*- coding: utf-8 -*-
"""Ingesta — The Dichotomy of Leadership, Cap 2 'Own It All, but Empower Others'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/dichotomy-of-leadership/dichotomy-of-leadership.md"
ORIGIN = "Jocko Willink & Leif Babin, The Dichotomy of Leadership (2018)"
BAL = "aku-balance-ownership-decentralized-command-concept"
MICRO = "aku-micromanagement-mata-iniciativa-claim"
HANDS = "aku-hands-off-laissez-faire-descoordina-claim"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "mando"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(MICRO, "claim",
        "El micromanagement fracasa por dos razones: ninguna persona puede controlar a múltiples individuos ejecutando muchas acciones en un entorno dinámico, y además inhibe el crecimiento de los subordinados —acostumbrados a que les digan qué hacer, esperan instrucciones, y la iniciativa, la creatividad y la acción audaz mueren, convirtiendo al equipo en autómatas que no entienden lo que hacen.",
        DOM + ["micromanagement"],
        {"supports": [BAL], "related": ["aku-micromanagement-disuelve-en-caos-claim"]}),
    aku(HANDS, "claim",
        "El líder hands-off (laissez-faire) es el extremo opuesto: no da dirección específica, así que el equipo «piensa demasiado», desarrolla ideas, tácticas y hasta estrategias propias más allá de su responsabilidad y no alineadas con la visión de la empresa, y se mueve en direcciones aleatorias o conflictivas en vez de hacia los objetivos estratégicos.",
        DOM + ["laissez-faire"],
        {"supports": [BAL], "related": ["aku-decentralized-limites-de-autoridad-claim"]}),
    aku("aku-sintomas-de-micromanagement-method", "method",
        "Señales de que un líder se ha inclinado demasiado al micromanagement: (1) el equipo no toma iniciativa, no actúa salvo que se le ordene; (2) no busca soluciones, espera que se las den; (3) no se moviliza ni en una emergencia; (4) la acción audaz y agresiva escasea; (5) la creatividad se detiene; (6) se queda en su silo por miedo a sobrepasar sus límites; (7) pasividad general y falta de reacción.",
        DOM + ["diagnostico"],
        {"related": [MICRO]}),
    aku("aku-sintomas-de-hands-off-method", "method",
        "Señales de que un líder es demasiado hands-off: (1) falta de visión de qué hace el equipo y cómo; (2) falta de coordinación, esfuerzos que compiten o interfieren; (3) la iniciativa sobrepasa los límites de autoridad; (4) fallo de coordinación por ignorancia (olvidan que otros equipos maniobran); (5) el equipo persigue la prioridad equivocada o soluciones no alineadas con el commander's intent; (6) demasiada gente intentando liderar y pocos ejecutando («too many coaches, not enough players»).",
        DOM + ["diagnostico"],
        {"related": [HANDS]}),
    aku("aku-corregir-micromanagement-method", "method",
        "Para corregir el micromanagement: retirarse de dar dirección detallada; en vez de explicar qué es la misión y cómo hacerla, explicar el objetivo amplio, el end state deseado y por qué importa, y dejar que el equipo planifique cómo ejecutarla; seguir monitorizando el progreso pero abstenerse de guiar la ejecución salvo que el plan vaya a tener resultados muy negativos; y, cuando el tiempo y el riesgo lo permitan, apartarse del todo y dejar que planifique y ejecute solo.",
        DOM + ["correccion"],
        {"supports": [BAL], "related": ["aku-sintomas-de-micromanagement-method"]}),
    aku("aku-corregir-hands-off-method", "method",
        "Para corregir un liderazgo demasiado hands-off: dar guía clara (misión, objetivo y end state de forma simple, clara y concisa); definir los límites y qué hacer al toparse con ellos; cuando hay esfuerzos solapados, decidir e implementar el curso de acción elegido; educar al equipo sobre los esfuerzos de otros equipos para desconflictar; y si hay «demasiados entrenadores y pocos jugadores», asignar y delinear claramente la cadena de mando, roles y autoridad.",
        DOM + ["correccion"],
        {"supports": [BAL], "related": ["aku-sintomas-de-hands-off-method"]}),
    aku("aku-asignar-lead-claro-evita-planes-divergentes-claim", "claim",
        "Cuando se asigna una misión a varios equipos sin designar claramente quién lleva el lead, cada uno desarrolla planes separados y divergentes, malgastando tiempo y esfuerzo; designar a uno como elemento líder y al otro como de apoyo coordina los esfuerzos en un plan unificado.",
        DOM + ["coordinacion"],
        {"supports": [BAL], "related": ["aku-main-effort-supporting-efforts-concept", "aku-decentralizar-proceso-planificacion-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
# enriquecer balance-ownership-decentralized-command con 2a fuente
found = next((o for o in patch_ops if o["id"] == BAL), None)
if found:
    found["add_source"] = SRC; found["confidence"] = 0.60
else:
    patch_ops.append({"id": BAL, "add_source": SRC, "confidence": 0.60, "updated": D})
akupatch.apply(ROOT, patch_ops)
print("cross + enrich aplicados sobre", len(patch_ops), "AKUs")
for t in ops: print("  ", t, [r[0] for r in ops[t]])
