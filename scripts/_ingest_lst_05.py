# -*- coding: utf-8 -*-
"""Ingesta — Leadership Strategy and Tactics, Part 2 Sec 2 'Leadership Skills' + 2 TAKUs."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/leadership-strategy-and-tactics/leadership-strategy-and-tactics.md"
ORIGIN = "Jocko Willink, Leadership Strategy and Tactics: Field Manual (2020)"
ITER = "aku-iterative-decision-making-method"
CONFORM = "aku-conform-to-influence-claim"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku("aku-pausa-tactica-ante-vacio-de-liderazgo-method", "method",
        "Ante un vacío de liderazgo (nadie toma el mando), no siempre saltes de inmediato: si hay amenaza inmediata, llénalo ya; si es más lento, haz una pausa táctica —detach, observa, confirma—; deja que otro dé un paso al frente (si guía bien, apóyalo), deja que el problema se haga visible para todos (así tu decisión es la que esperan y la ejecutan), evita chocar con otro que también entre, y la pausa hará que tu decisión sea mejor.",
        DOM + ["decision", "iniciativa"],
        {"related": ["aku-relax-look-around-make-a-call-method", "aku-detach-tactico-estrategico-concept", "aku-decisiveness-amid-uncertainty-concept"]}),
    aku("aku-no-amontonarse-en-el-lider-claim", "claim",
        "«Don't bunch up» (no os amontonéis): en combate, amontonarse hace que una sola bala o bomba hiera a muchos —hay que dispersarse—; en liderazgo, la gente tiende a «amontonarse» sobre el líder (por ego o por querer contribuir), invadiendo su espacio mental, socavando su autoridad y estorbando; hay que apartarse y dar al líder espacio para liderar.",
        DOM + ["espacio", "ego"],
        {"related": ["aku-check-the-ego-concept", "aku-no-care-detachment-via-ego-method"]}),
    aku("aku-no-tomarse-las-cosas-personalmente-claim", "claim",
        "No te tomes nada personalmente —ni la crítica a tu plan, idea, presentación o decisión—: incluso viniendo de tu mayor rival o de alguien que crees sin nivel para opinar, desapégate, escucha con mente objetiva, mira si puedes aprender algo, aplícalo y da las gracias; cuesta y exige humildad, pero te hace mejor.",
        DOM + ["humildad", "ego"],
        {"related": ["aku-check-the-ego-concept", "aku-no-usar-sandwich-de-critica-claim"]}),
    aku("aku-dont-dig-in-no-sobrecomprometerse-claim", "claim",
        "«Don't dig in» (no te atrincheres): como decía Patton, no se puede avanzar atrincherado, así que no te sobrecomprometas con tus ideas u opiniones —mantén la mente abierta y déjate una salida—; no argumentes por TU idea sino por la MEJOR idea (si la tuya no es mejor, cédela; si son iguales, deja la suya para darles ownership); atrinchérate solo si tienes 100% de certeza (casi nunca), o ante lo inmoral/ilegal/no ético, o si violan las Leyes del Combate, y aun así déjate margen.",
        DOM + ["ego", "decision"],
        {"related": ["aku-play-the-long-game-concept", "aku-dar-ordenes-solo-commanders-intent-claim", "aku-ejecutar-decision-como-propia-claim"]}),
    aku(ITER, "method",
        "«Iterative decision-making»: cuando no estás seguro o falta información, no sobrecomprometas; toma decisiones pequeñas que avanzan hacia tu mejor conjetura, con puntos de control para reevaluar (ej.: objetivo a 300 millas → avanzar por etapas reevaluando la inteligencia en cada base hacia delante, y dar la vuelta si cambia); es contrario a «sé decisivo», pero mitiga el riesgo: sé decisivo cuando debas, pero no decidas hasta que tengas que hacerlo.",
        DOM + ["decision", "incertidumbre"],
        {"related": ["aku-decisiveness-amid-uncertainty-concept", "aku-no-hay-solucion-100-correcta-claim", "aku-contingency-planning-anticipar-method"]}),
    aku("aku-delegar-todo-para-liderar-no-pareciendo-vago-claim", "claim",
        "Mando descentralizado: «si quieres estar al cargo de todo, intenta estar al cargo de nada» —delega todas las acciones para poder liderar de verdad (mirar up and out)—; pero como puede parecer pereza, contrarréstalo asumiendo de vez en cuando las tareas más duras o desagradables y bordándolas (da ejemplo); y si un quejica cede gustoso su trabajo sin que le duela el ego, revela que no le importa → empieza a buscar reemplazo.",
        DOM + ["delegacion", "mando"],
        {"related": ["aku-decentralized-command-concept", "aku-ningun-trabajo-es-demasiado-bajo-claim", "aku-liderar-desde-frente-y-desde-atras-concept"]}),
    aku("aku-no-seas-el-easy-button-claim", "claim",
        "Asumir el ownership de las tareas duras no significa hacerlo todo por tu equipo: si te conviertes en su «easy button» (les resuelves cada problema), dejarán de aprender a pensar y solo aprenderán a pedirte soluciones, frenando su crecimiento, y tú quedarás atrapado «down and in»; en su lugar, hazles resolver («ve, descíflalo y vuelve cuando tengas un plan»), corrige sus carencias y deja que mejoren.",
        DOM + ["delegacion", "desarrollo"],
        {"related": ["aku-dar-confianza-incrementalmente-method", "aku-decentralized-command-concept", "aku-micromanagement-mata-iniciativa-claim"]}),
    aku("aku-juzgar-reputaciones-dar-empezar-de-cero-claim", "claim",
        "No juzgues a las personas nuevas solo por su reputación o expediente: toma nota de su historial, pero dales un borrón y cuenta nueva; lo anotado te permite confirmar más rápido un problema si se repite, pero da la oportunidad —un mal jefe anterior, falta de experiencia o errores inmaduros suelen superarse si se lidera bien a la persona—.",
        DOM + ["personas", "juicio"],
        {"related": ["aku-when-to-mentor-when-to-fire-concept", "aku-lideres-nacen-y-se-hacen-claim"]}),
    aku(CONFORM, "claim",
        "Para influir en un grupo, hay que estar DENTRO de él: «no puedo cambiar al grupo si no estoy en el grupo»; ser sobreagresivo (Rambo) te aísla y te quita influencia, así que conforma lo suficiente para construir relaciones (sin perder tu individualidad) y mueve al grupo desde dentro; para reconducir a un compañero negativo, ni le des la razón del todo ni le contradigas de frente: usa un punto medio que abra diálogo («¿por qué crees que el liderazgo nos tiene en esto?»); pero plántate ante lo ilegal/inmoral/no ético.",
        DOM + ["influencia", "relaciones"],
        {"related": ["aku-play-the-long-game-concept", "aku-power-of-relationships-liderazgo-concept", "aku-ganar-respeto-e-influencia-dandolos-claim", "aku-liderazgo-indirecto-supera-al-directo-claim"]}),
    aku("aku-positivo-pero-realista-no-pollyanna-claim", "claim",
        "Mantén una actitud positiva ante lo malo (encuentra el «good»: «nos negaron fondos → bien, seremos más eficientes»), pero atémperala con realismo («pero no TAN bueno»): si el equipo solo oye positividad al 100%, parecerás un Pollyanna ciego a la realidad y perderás credibilidad; sé positivo pero realista, sin ignorar ni maquillar los problemas.",
        DOM + ["actitud", "realismo"],
        {"related": ["aku-good-mindset-concept", "aku-lideres-dicen-la-verdad-claim", "aku-actitud-lider-marca-el-tono-claim"]}),
]

def links(jb, **extra):
    d = {"justified_by": jb, "constrained_by": [], "breaks_when": [], "illustrates": [], "challenges": []}
    d.update(extra); return d

takus = [
    {
        "id": "taku-iterative-decision-making", "taku_type": "protocol",
        "title": "Toma de decisiones iterativa bajo incertidumbre",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "decision", "incertidumbre"],
        "when_to_use": "Cuando hay que avanzar pero falta información o certeza, y sobrecomprometerse sería arriesgado.",
        "when_not_to_use": "Cuando una amenaza inmediata exige una decisión rápida y firme: ahí, decide ya.",
        "aku_links": links([ITER, "aku-decisiveness-amid-uncertainty-concept"]),
        "taku_relations": {},
        "body": """## Purpose
Avanzar hacia un objetivo incierto minimizando el riesgo de sobrecomprometerse con información incompleta.

## Trigger Conditions
Necesidad de moverse hacia un objetivo cuya viabilidad aún no es segura.

## Required Resources
Puntos de control donde reevaluar (información/inteligencia fresca); capacidad de pausar o revertir.

## Protocol Steps
1. Define tu mejor conjetura sobre la situación y el objetivo.
2. Toma una decisión pequeña que avance en esa dirección, sin comprometerlo todo.
3. En el siguiente checkpoint, reevalúa con la nueva información.
4. Si sigue alineado, avanza otro paso; si cambia, pausa, reevalúa o da la vuelta.
5. Repite hasta tener certeza suficiente para comprometerte del todo.

## Decision Points
En cada checkpoint: ¿la información sigue apoyando avanzar? ¿cuánto riesgo añade el siguiente paso?

## Exit Conditions
Tienes certeza suficiente para ejecutar plenamente, o abortas con bajo coste.

## Failure Handling
Si esperas demasiado y caes en analysis paralysis, recuerda: sé decisivo cuando debas; no decidir también es decidir.

## Review Trigger
Tras la operación, evalúa si los checkpoints estuvieron bien situados.""",
    },
    {
        "id": "taku-conform-to-influence", "taku_type": "heuristic",
        "title": "Conform to influence: cambiar al grupo desde dentro",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "influencia", "relaciones"],
        "when_to_use": "Cuando quieres reconducir a un grupo o compañeros con actitud negativa y no tienes autoridad directa sobre ellos.",
        "when_not_to_use": "Ante conductas ilegales/inmorales/no éticas: ahí hay que plantarse, no conformar.",
        "aku_links": links([CONFORM, "aku-power-of-relationships-liderazgo-concept"]),
        "taku_relations": {},
        "body": """## The Rule
No puedes cambiar al grupo si no estás en el grupo: conforma lo justo para construir relaciones y, desde dentro, muévelo en la dirección correcta.

## What It Replaces
La actitud sobreagresiva (Rambo) que ataca de frente las creencias del grupo y te deja aislado e impotente.

## When It Holds
Cuando careces de autoridad directa y necesitas influencia; la influencia nace de la relación.

## When It Fails
Cuando el grupo hace algo ilegal/inmoral/no ético: ahí hay que plantarse (con tacto), no conformar.

## Why It Works
La influencia requiere relación; sin relación, no hay influencia. Desde dentro puedes mover al grupo, quizá no tan rápido como quieres, pero en la dirección correcta.

## Calibration
Ante un compañero negativo, ni le des la razón del todo ni le contradigas de frente: usa el punto medio que abre diálogo («¿por qué crees que nos tienen en esto?»). Conforma lo justo, sin perder tu individualidad ni cortar a la cadena de mando a sus espaldas.""",
    },
]

written, cross = akugen.generate(akus, takus, ROOT)
print(f"escritos: {len(written)} ficheros")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
akupatch.apply(ROOT, patch_ops)
print(f"cross sobre {len(patch_ops)} AKUs")
