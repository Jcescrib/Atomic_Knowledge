# -*- coding: utf-8 -*-
"""Ingesta — Discipline Equals Freedom, Batch 2 (Weakness -> Default Aggressive) + TAKU."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/discipline-equals-freedom/discipline-equals-freedom.md"
ORIGIN = "Jocko Willink, Discipline Equals Freedom: Field Manual (2017)"
ROOT_AKU = "aku-disciplina-raiz-de-toda-buena-cualidad-concept"
DEF = "aku-discipline-equals-freedom-concept"
DICH = "aku-dichotomy-of-leadership-concept"
DEFAULT = "aku-default-agresivo-proactivo-dictar-situacion-claim"
STRESS = "aku-gestionar-stress-detach-y-perspectiva-method"
QUEST = "aku-cuestionarlo-todo-y-a-uno-mismo-method"
KNOW = "aku-conocimiento-es-el-arma-definitiva-claim"
RELENT = "aku-no-relajarse-hasta-completar-la-mision-claim"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "disciplina"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku("aku-fortaleza-puede-ser-debilidad-y-viceversa-claim", "claim",
        "La mayor fortaleza de una persona suele ser también su mayor debilidad, y sus debilidades pueden convertirse en fortalezas; no hay que aceptar que uno está condenado a ser lo que es: cada día se puede luchar contra las propias debilidades para ser un poco mejor que ayer.",
        DOM + ["autoconocimiento"],
        {"related": ["aku-check-the-ego-concept"]}),
    aku(STRESS, "method",
        "Para gestionar el estrés: (1) gana perspectiva (otros han afrontado cosas mucho peores); (2) desapégate (detach) del problema. El estrés lo causa lo que no controlas: si es algo que SÍ puedes controlar y no lo haces, es falta de disciplina y de ownership → toma el control y resuélvelo; si es algo que NO puedes controlar, abrázalo, míralo desde otro ángulo y conviértelo en tu aliado para volverte más agudo y eficaz.",
        DOM + ["estres", "control"],
        {"related": ["aku-detach-tactico-estrategico-concept", "aku-extreme-ownership-concept"]}),
    aku("aku-destroyer-mode-emocion-y-logica-concept", "concept",
        "El «destroyer mode» (modo destructor/berserker que no se detiene) es lo que permite ir más allá de los límites, y nace del equilibrio de dos fuerzas opuestas: emoción y lógica; cuando la lógica se agota y no tiene sentido seguir, se usa la emoción (rabia, frustración, miedo) para empujar; cuando la emoción flaquea, se sobreescribe con lógica y voluntad: combatir la emoción débil con la lógica y la lógica débil con la emoción, hasta decir «I don't stop».",
        DOM + ["resiliencia", "dicotomia"],
        {"related": [DICH, RELENT]}),
    aku(RELENT, "claim",
        "La tendencia a relajarse en cuanto se cumple el objetivo primario de una misión es peligrosa: no puedes relajarte hasta que la misión ENTERA está completa, porque el enemigo acecha el momento de debilidad (el exhalar, bajar el arma); hay que ser implacable (relentless) —nunca está terminado, siempre hay otra misión, tarea u objetivo—.",
        DOM + ["implacabilidad"],
        {"supports": [ROOT_AKU], "related": ["aku-nunca-complacencia-subestimar-enemigo-claim"]}),
    aku("aku-disciplina-se-extiende-a-todo-claim", "claim",
        "La disciplina empieza por madrugar, pero se extiende a todo lo demás: entrenar a diario, comer bien, disciplinar las emociones para decidir bien, controlar el ego, tratar a los demás como querrías que te trataran, hacer las tareas que no quieres pero te ayudan, afrontar los miedos y tomar el camino difícil/cuesta arriba; la disciplina parece tu peor enemigo pero es tu mejor amigo y te pone en el camino a la libertad.",
        DOM,
        {"supports": [ROOT_AKU, DEF]}),
    aku(KNOW, "claim",
        "El conocimiento es el arma definitiva y el «maestro de las herramientas»: triunfa sobre todas las demás armas, porque es el pensamiento y la mente lo que gana; y el conocimiento se adquiere haciendo preguntas.",
        DOM + ["conocimiento"],
        {}),
    aku(QUEST, "method",
        "Para aprender, cuestiónalo todo y no aceptes nada como verdad: cuando no entiendas una palabra, ve al diccionario; un concepto, descomponlo hasta entenderlo; un mecanismo, indaga hasta comprenderlo; y sobre todo, cuestiónate a ti mismo cada día (¿quién soy?, ¿qué he aprendido/creado?, ¿qué progreso he hecho?, ¿estoy dando todo lo que puedo?) y respóndete con sinceridad.",
        DOM + ["aprendizaje"],
        {"supports": [KNOW], "related": ["aku-preguntar-por-que-method"]}),
    aku("aku-pelear-hasta-el-final-nada-que-perder-claim", "claim",
        "«Go down swinging»: si peleas con todo lo que tienes, la mayoría de las veces no caerás en absoluto, ganarás; hay que hacer de esa actitud parte de la vida diaria (la repetición extra, la milla extra, el asalto extra); y ante un reto que crees que no puedes ganar, recuerda que no tienes nada que perder, así que ponte en pie y avanza.",
        DOM + ["actitud", "lucha"],
        {"supports": [ROOT_AKU], "related": [RELENT]}),
    aku("aku-compromiso-externo-si-interno-no-concept", "concept",
        "Dicotomía del compromiso: externamente, trabajar con otras personas, situaciones y acuerdos exige compromiso (hallar terreno común, fusionar enfoques, unificar) —no comprometer es a menudo no triunfar—; pero internamente, con uno mismo y la propia autodisciplina y estándares, NO puede haber compromiso: ahí se mantiene la línea, «not now, not ever».",
        DOM + ["dicotomia", "compromiso"],
        {"supports": [DICH], "related": ["aku-self-discipline-viene-de-dentro-concept"]}),
]

takus = [
    {
        "id": "taku-gestion-del-stress", "taku_type": "technique",
        "title": "Gestión del estrés: perspectiva, detach y control-o-abraza",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "estres", "resiliencia"],
        "when_to_use": "Cuando la presión o el estrés amenazan con abrumar el juicio o la ejecución.",
        "when_not_to_use": "No sustituye la acción sobre las causas controlables: si puedes resolver la fuente del estrés, resuélvela.",
        "aku_links": {"justified_by": [STRESS, "aku-detach-tactico-estrategico-concept"],
                       "constrained_by": [], "breaks_when": [], "illustrates": [], "challenges": []},
        "taku_relations": {},
        "body": """## Summary
Técnica para convertir el estrés en una ventaja en vez de un lastre, distinguiendo lo controlable de lo incontrolable.

## When to Use
Bajo presión alta, incertidumbre o caos, antes de tomar decisiones importantes.

## Prerequisites
Capacidad de detach (apartarse mentalmente); honestidad para distinguir lo que controlas de lo que no.

## Steps
1. Gana perspectiva: recuerda que otros han afrontado cosas mucho peores; relativiza.
2. Detach: apártate mentalmente del problema para verlo entero.
3. Clasifica: ¿es controlable o no?
4. Si es controlable y no lo estás controlando → es falta de disciplina/ownership: toma el control y resuélvelo.
5. Si es incontrolable → abrázalo: míralo desde otro ángulo, conviértelo en aliado para estar más agudo y alerta.

## Anti-patterns
Estresarse por lo incontrolable; negar el estrés; paralizarse en vez de detach.

## Expected Outcome
Decisión más clara y serena; el estrés se usa como combustible, no como freno.

## Failure Signals
Rumiación sobre lo incontrolable; parálisis; decisiones impulsivas dictadas por la emoción.

## Underlying Logic
El estrés nace de la falta de control; clasificar y actuar (o aceptar) restaura la agencia.

## Notes and Variants
Se combina con «destroyer mode» (equilibrio emoción/lógica) cuando hay que empujar más allá del límite.""",
    },
]

written, cross = akugen.generate(akus, takus, ROOT)
print(f"escritos: {len(written)} ficheros")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
found = next((o for o in patch_ops if o["id"] == DEFAULT), None)
if found: found["add_source"] = SRC; found["confidence"] = 0.70
else: patch_ops.append({"id": DEFAULT, "add_source": SRC, "confidence": 0.70, "updated": D})
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
print("enrich default-agresivo: 3a fuente, 0.70")
