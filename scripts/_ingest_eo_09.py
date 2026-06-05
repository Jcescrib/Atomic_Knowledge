# -*- coding: utf-8 -*-
"""Ingesta — Extreme Ownership, Cap 9 'Plan' (Parte III)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/extreme-ownership/extreme-ownership.md"
ORIGIN = "Jocko Willink & Leif Babin, Extreme Ownership (2015)"
PLAN = "aku-planning-process-estandarizado-concept"
DBR = "aku-post-operational-debrief-method"
RISK = "aku-calcular-y-mitigar-riesgo-claim"
ANAL = "aku-analisis-constante-medir-efectividad-claim"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "planificacion"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(PLAN, "concept",
        "Un «planning process» estandarizado es un proceso de planificación efectivo, repetible y documentado como checklist, que los demás —incluso con menos experiencia— pueden seguir; incluye que use formato y terminología comunes para que otros departamentos y activos de apoyo lo entiendan y lo usen; excluye depender de que cada líder experimentado «se las apañe» sin proceso. Es crítico para el éxito sostenido a medida que el equipo crece.",
        DOM,
        {"related": ["aku-simple-law-of-combat-concept", "aku-commanders-intent-concept"]}),
    aku("aku-stand-back-be-the-tactical-genius-claim", "claim",
        "El líder senior supervisa la planificación pero no debe empantanarse en los detalles: manteniéndose por encima del «microterreno» del plan puede «stand back and be the tactical genius» —detectar debilidades o huecos que quienes están inmersos en el detalle pasaron por alto— y rellenarlos antes de la ejecución.",
        DOM + ["perspectiva", "estrategia"],
        {"supports": [PLAN], "related": ["aku-detach-tactico-estrategico-concept", "aku-pull-off-the-firing-line-claim"]}),
    aku("aku-leaders-checklist-planning-method", "method",
        "Checklist de planificación del líder: (1) analizar la misión —entender la misión, Commander's Intent y endstate del mando superior, y fijar el propio—; (2) identificar personal, activos, recursos y tiempo disponibles; (3) descentralizar la planificación empoderando a líderes clave para analizar cursos de acción; (4) determinar un curso de acción concreto, inclinándose por el más simple; (5) empoderar a líderes clave para desarrollar el plan; (6) planificar contingencias en cada fase; (7) mitigar los riesgos controlables; (8) delegar partes del plan y del brief, y «stand back and be the tactical genius»; (9) revisar y cuestionar continuamente el plan contra la información emergente; (10) briefar a todos los participantes y apoyos enfatizando el Commander's Intent y fomentando preguntas; (11) tras la ejecución, hacer post-operational debrief y aplicar las lecciones.",
        DOM + ["checklist", "procedimiento"],
        {"supports": [PLAN]}),
    aku(DBR, "method",
        "El «post-operational debrief» se realiza tras cada operación —por agotados u ocupados que estén— examinando todas las fases (de la planificación a la ejecución) en formato conciso con tres preguntas: ¿qué salió bien?, ¿qué salió mal?, ¿cómo podemos adaptar nuestras tácticas para ser más efectivos?; luego se implementan las lecciones en la planificación futura para no repetir errores.",
        DOM + ["debrief", "mejora-continua"],
        {"supports": [PLAN], "related": ["aku-lideres-nunca-satisfechos-mejora-continua-claim"]}),
    aku("aku-brief-orientado-a-frontline-claim", "claim",
        "El brief de un plan debe orientarse a las tropas de primera línea que lo ejecutan —no a impresionar a los jefes o instructores con destreza en PowerPoint—; la prueba de un buen brief es simple: ¿lo entienden el equipo y los elementos de apoyo?; debe priorizar la información de forma simple para evitar la sobrecarga y fomentar preguntas hasta del personal más junior.",
        DOM + ["comunicacion", "brief"],
        {"supports": [PLAN], "related": ["aku-briefear-al-minimo-comun-denominador-claim", "aku-facilitar-preguntas-clarificacion-claim"]}),
    aku(RISK, "claim",
        "Aunque a los SEALs se les conoce por asumir riesgos, en realidad los calculan con cuidado: un buen plan maximiza la probabilidad de éxito mientras mitiga todo el riesgo posible; hay riesgos que no se pueden mitigar, así que el líder debe enfocarse en los que sí se pueden controlar.",
        DOM + ["riesgo"],
        {"supports": [PLAN]}),
    aku("aku-los-que-no-arriesgan-no-ganan-claim", "claim",
        "«Those who will not risk cannot win» (John Paul Jones): los líderes deben sentirse cómodos aceptando cierto nivel de riesgo, porque sin asumir riesgo no se puede ganar.",
        DOM + ["riesgo"],
        {"related": [RISK]}),
    aku(ANAL, "claim",
        "Los mejores equipos analizan constantemente sus tácticas y miden su efectividad para adaptar sus métodos e implementar las lecciones aprendidas en misiones futuras; la excusa de «no hay tiempo» para ese análisis es falsa: hay que hacer tiempo, porque de ello depende el éxito futuro.",
        DOM + ["mejora-continua", "analisis"],
        {"supports": [PLAN], "related": [DBR, "aku-lideres-nunca-satisfechos-mejora-continua-claim"]}),
    aku("aku-decentralizar-proceso-planificacion-claim", "claim",
        "Hay que descentralizar el proceso de planificación: empoderar a los líderes clave del equipo para que analicen los posibles cursos de acción y desarrollen el plan del curso elegido, en vez de que el líder senior planifique todo solo.",
        DOM + ["descentralizacion"],
        {"supports": [PLAN], "related": ["aku-decentralized-command-concept"]}),
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
