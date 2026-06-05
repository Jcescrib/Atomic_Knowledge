# -*- coding: utf-8 -*-
"""Ingesta — Discipline Equals Freedom, Batch 4 (Hesitation -> Staying Motivated) + TAKU GOOD."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/discipline-equals-freedom/discipline-equals-freedom.md"
ORIGIN = "Jocko Willink, Discipline Equals Freedom: Field Manual (2017)"
ROOT_AKU = "aku-disciplina-raiz-de-toda-buena-cualidad-concept"
GOOD = "aku-good-mindset-concept"
DEATH = "aku-incluso-en-la-muerte-hay-good-claim"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "disciplina"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku("aku-hesitacion-es-el-enemigo-claim", "claim",
        "La hesitación es el enemigo: el miedo en el momento entre decidir y actuar causa vacilación, y la vacilación causa la derrota (deja pasar el momento, pierde la oportunidad, da ventaja al enemigo y deviene en cobardía); para ganar hay que superar ese instante —ir, moverse, tomar la acción, no esperar—.",
        DOM + ["decision", "accion"],
        {"related": ["aku-hesitar-a-veces-es-prudente-claim", "aku-default-agresivo-proactivo-dictar-situacion-claim"]}),
    aku("aku-draw-fire-concept", "concept",
        "«Draw fire» (atraer el fuego) como liderazgo: cuando pasan cosas malas, el líder da un paso al frente para absorber el impacto y la negatividad —como el soldado que se expone para atraer el fuego enemigo y dar al equipo la oportunidad de moverse—; es ser el punto firme y fiable al que los demás miran, de modo que la actitud positiva se contagie y el equipo siga luchando.",
        DOM + ["liderazgo", "adversidad"],
        {"related": ["aku-liderar-desde-posicion-mas-dificil-claim", "aku-lider-percibido-como-decisivo-claim"]}),
    aku(GOOD, "concept",
        "El mindset «GOOD» (bien): la forma de afrontar contratiempos, fallos, retrasos y derrotas resumida en una palabra, «Good», porque de todo lo malo saldrá algo bueno (otra misión en que enfocarse, mantenerlo simple, una lección, la oportunidad de hallar solución); no es positividad ingenua (que ignora la dura verdad) ni quedarse rumiando el problema: es aceptar la realidad pero enfocarse en la solución y convertir el revés en algo bueno; y si puedes decir «good», es que sigues vivo y te queda lucha.",
        DOM + ["resiliencia", "mentalidad"],
        {"related": ["aku-extreme-ownership-concept", "aku-actitud-lider-marca-el-tono-claim"]}),
    aku(DEATH, "claim",
        "Incluso en la muerte hay «good»: gratitud por haber tenido a la persona (los momentos, los recuerdos), por lo que su vida y su muerte te enseñaron —lo preciosa que es la vida—; la muerte es parte de la vida (sin muerte no hay vida); la respuesta es vivir cada día con propósito y pasión para honrar a quienes ya no viven.",
        DOM + ["duelo", "proposito"],
        {"related": [GOOD]}),
    aku("aku-es-un-trabajo-de-cada-dia-claim", "claim",
        "Esto no es un trabajo a tiempo parcial ni de fichar y marcharse: no hay fines de semana libres, cada día es lunes —un nuevo comienzo y una nueva oportunidad de atacar el día—; uno se cansará, recibirá golpes y tendrá días malos, pero no se detiene.",
        DOM + ["consistencia"],
        {"related": ["aku-no-relajarse-hasta-completar-la-mision-claim", "aku-the-warpath-concept"]}),
    aku("aku-no-mas-excusas-claim", "claim",
        "«No more»: no más excusas, no más «empiezo mañana», no más «solo esta vez», no más camino fácil, no más esperar el momento perfecto, no más indecisión ni debilidad; ahora es el momento de la fuerza, la voluntad y la disciplina inquebrantable para convertirse en quien uno quiere ser.",
        DOM + ["excusas"],
        {"related": [ROOT_AKU, "aku-empezar-aqui-y-ahora-method"]}),
    aku("aku-no-cuentes-con-motivacion-cuenta-disciplina-claim", "claim",
        "No cuentes con la motivación —es voluble, va y viene, no es fiable, y contar con ella hace que te quedes corto—: cuenta con la disciplina; no existe la píldora mágica ni el life hack que elimine el trabajo: tienes que hacer el trabajo y hacer que ocurra obligándote mediante la disciplina.",
        DOM + ["motivacion"],
        {"supports": [ROOT_AKU], "related": ["aku-no-hay-atajo-ni-hack-claim"]}),
]

takus = [
    {
        "id": "taku-good-mindset", "taku_type": "heuristic",
        "title": "«GOOD»: reencuadrar todo contratiempo",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "resiliencia", "mentalidad"],
        "when_to_use": "Ante cualquier contratiempo, fallo, retraso, derrota o problema inesperado, propio o del equipo.",
        "when_not_to_use": "Como positividad ingenua que ignora la realidad o evita actuar sobre la causa: «good» exige aceptar el hecho y atacar la solución.",
        "aku_links": {"justified_by": [GOOD, DEATH], "constrained_by": [], "breaks_when": [], "illustrates": [], "challenges": []},
        "taku_relations": {},
        "body": """## The Rule
Ante un revés, responde con una sola palabra: «Good». Busca el bien que puede salir de ello, acepta la realidad y enfócate en la solución.

## What It Replaces
La reacción de frustración, queja o parálisis ante los problemas.

## When It Holds
Siempre que haya un margen de acción o aprendizaje: misión cancelada → enfócate en otra; te lesionaste → necesitabas descanso; te ganaron → aprendiste.

## When It Fails
Si degenera en positividad vacía que ignora la dura verdad o sustituye a la acción correctiva. No basta con decir «good»: hay que actuar.

## Why It Works
Reencuadra el revés como oportunidad, corta la espiral negativa y, en un equipo, contagia la actitud; mientras puedas decir «good» sigues vivo y con lucha.

## Calibration
Empareja siempre el «good» con la pregunta «¿qué hago ahora?»: aceptar realidad + atacar solución. Si solo dices «good» sin actuar, lo estás usando mal.""",
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
