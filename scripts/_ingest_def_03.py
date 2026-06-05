# -*- coding: utf-8 -*-
"""Ingesta — Discipline Equals Freedom, Batch 3 (Nature vs Nurture -> Focus) + TAKU."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/discipline-equals-freedom/discipline-equals-freedom.md"
ORIGIN = "Jocko Willink, Discipline Equals Freedom: Field Manual (2017)"
ROOT_AKU = "aku-disciplina-raiz-de-toda-buena-cualidad-concept"
DEF = "aku-discipline-equals-freedom-concept"
WAR = "aku-the-warpath-concept"
GOANY = "aku-not-feeling-it-go-anyway-claim"
QUIT = "aku-instinto-de-rendirse-es-mentiroso-claim"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "disciplina"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku("aku-eleccion-vence-naturaleza-y-crianza-claim", "claim",
        "Lo que determina el éxito no es la naturaleza ni la crianza, sino la elección: las personas exitosas deciden serlo y toman otras decisiones (estudiar duro, trabajar duro, asumir los trabajos difíciles, liderar cuando nadie más lo hace, elegir a quién emular); superan tanto su naturaleza como su crianza, y nunca es demasiado tarde para hacer esa elección.",
        DOM + ["eleccion", "responsabilidad"],
        {"related": ["aku-extreme-ownership-concept", "aku-self-discipline-viene-de-dentro-concept"]}),
    aku("aku-miedo-al-fracaso-es-bueno-claim", "claim",
        "El miedo al fracaso es bueno y no hay que superarlo: mantiene despierto planificando, ensayando contingencias, entrenando duro y sin cortar esquinas; pero, más importante aún, hay que estar aterrorizado del estancamiento —de no hacer nada, mirar desde la banda y despertar en seis meses o seis años sin haber progresado nada—.",
        DOM + ["miedo", "accion"],
        {"related": ["aku-contingency-planning-anticipar-method"]}),
    aku(WAR, "concept",
        "«The Warpath» (la senda de guerra) es la guerra diaria e interminable contra las propias debilidades, la ignorancia y la confusión —que conduce a la fuerza, el conocimiento y la comprensión—, una guerra que es el camino de la disciplina sin mitigar en todas las cosas; lleva al control y la ownership de la propia vida y, por ello, a la libertad y, al final, a la paz.",
        DOM + ["disciplina", "mentalidad"],
        {"related": [DEF, ROOT_AKU, "aku-extreme-ownership-concept"]}),
    aku("aku-comida-basura-es-veneno-claim", "claim",
        "La comida basura (donuts, galletas, refrescos, patatas fritas) no es comida sino veneno: no te nutre, te mata y hace lo contrario de fortalecerte; ante su tentación —«sugarcoated lies»— hay que mantener la línea y decir NO, ejercitando la voluntad (más fuerte que la de un donut); además, salvo ayuno prolongado, no necesitas comer (el humano aguanta ~30 días sin comer).",
        DOM + ["nutricion"],
        {"related": ["aku-disciplina-se-extiende-a-todo-claim", "aku-mind-control-controla-tu-propia-mente-concept"]}),
    aku(QUIT, "claim",
        "Hay un instinto que combatir: el que dice «ya has tenido bastante, puedes parar, descansar, rendirte»; es un mentiroso, un mecanismo de defensa del ego que ofrece una salida cómoda; no tomes la salida fácil por instinto —si debes retirarte para reconstruir, decídelo por lógica, no por el instinto de rendición— y reemplázalo por el instinto «levántate, ve, sigue luchando».",
        DOM + ["resiliencia", "instintos"],
        {"related": ["aku-destroyer-mode-emocion-y-logica-concept", "aku-no-relajarse-hasta-completar-la-mision-claim"]}),
    aku(GOANY, "claim",
        "En los días en que «no lo sientes» (cansado, harto del grind), ve igualmente y hazlo, aunque sea yendo por inercia (go through the motions); el deseo de descansar suele ser debilidad y camino de menor resistencia; procrastina solo una cosa —el descanso—: déjalo para mañana, y lo más probable es que mañana no lo necesites.",
        DOM + ["consistencia"],
        {"supports": [ROOT_AKU], "related": ["aku-camino-de-menor-resistencia-claim", "aku-empezar-aqui-y-ahora-method"]}),
    aku("aku-regret-solo-vale-por-la-leccion-claim", "claim",
        "El arrepentimiento en sí mismo es inútil: lo único valioso en él es la lección aprendida y el conocimiento ganado; no seas esclavo del arrepentimiento —aprende y sigue adelante— y deja que el miedo a arrepentirte impulse la acción ahora, porque solo tienes una vida y un intento.",
        DOM + ["aprendizaje"],
        {"related": ["aku-humildad-asumir-errores-claim", "aku-post-operational-debrief-method"]}),
    aku("aku-mantener-objetivo-largo-plazo-a-la-vista-claim", "claim",
        "Hay que mantener el objetivo a largo plazo incrustado en la mente y nunca perderlo de vista, asegurando que las tareas y metas cortas conducen a la victoria estratégica; la ansia de gratificación instantánea hace perder de vista la meta y abandonar las disciplinas diarias → sin progreso; por eso, cada día, haz algo —por pequeño que sea— que te acerque a la meta: es todo cosa tuya.",
        DOM + ["objetivos", "foco"],
        {"related": ["aku-metas-intermedias-visibles-method", "aku-enfocar-una-iniciativa-a-la-vez-claim"]}),
]

takus = [
    {
        "id": "taku-ir-igualmente", "taku_type": "heuristic",
        "title": "Ve igualmente: procrastina solo el descanso",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "consistencia", "disciplina"],
        "when_to_use": "En los días de baja motivación, cansancio o desgana ante una tarea o rutina que sabes que te conviene.",
        "when_not_to_use": "Ante señales reales de lesión, enfermedad o agotamiento que requieren descanso genuino.",
        "aku_links": {"justified_by": [GOANY, QUIT], "constrained_by": [], "breaks_when": [], "illustrates": [], "challenges": []},
        "taku_relations": {},
        "body": """## The Rule
Cuando no te apetezca, ve igualmente y hazlo —aunque sea por inercia—; procrastina solo una cosa: el descanso, déjalo para mañana.

## What It Replaces
La decisión emocional «hoy descanso» tomada en caliente por desgana.

## When It Holds
Cuando la desgana es debilidad o búsqueda del camino de menor resistencia, no una necesidad fisiológica real.

## When It Fails
Cuando hay señales reales de lesión, enfermedad o sobreentrenamiento: ahí el descanso es necesario y no debe posponerse indefinidamente.

## Why It Works
Posponer el descanso a mañana neutraliza la gratificación inmediata; al día siguiente, casi siempre, la necesidad de descanso ha desaparecido y mantienes la racha de disciplina.

## Calibration
Si tras posponerlo un día sigues necesitando descanso, tómalo; si el patrón se repite, evalúa carga y recuperación con honestidad.""",
    },
]

written, cross = akugen.generate(akus, takus, ROOT)
print(f"escritos: {len(written)} ficheros")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
