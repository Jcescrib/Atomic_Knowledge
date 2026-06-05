# -*- coding: utf-8 -*-
"""Ingesta — Discipline Equals Freedom, Batch 6A (Parte 2 Actions: training -> home gym) + 3 TAKUs."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/discipline-equals-freedom/discipline-equals-freedom.md"
ORIGIN = "Jocko Willink, Discipline Equals Freedom: Field Manual (2017)"
ROOT_AKU = "aku-disciplina-raiz-de-toda-buena-cualidad-concept"
SLEEP = "aku-sueno-es-necesidad-7-9h-claim"
FALL = "aku-conciliar-sueno-temprano-pasos-method"
NAP = "aku-power-nap-pies-elevados-method"
GYM = "aku-home-gym-equipo-basico-concept"
SOMETHING = "aku-en-el-workout-lo-importante-es-hacer-algo-y-trackear-claim"
D = "2026-06-05"
DOM = ["jocko", "fisico", "salud"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku("aku-entrenamiento-fisico-cuerpo-y-mente-claim", "claim",
        "El entrenamiento físico mejora cuerpo y mente: te hace más sano (sube endorfinas, testosterona, hormona de crecimiento, volumen cardíaco, sensibilidad a la insulina; previene hipertensión, obesidad, cardiopatía, diabetes tipo 2, insomnio y depresión) y más listo (mejora el flujo sanguíneo al cerebro, genera nuevas neuronas, la plasticidad sináptica y libera dopamina, serotonina y BDNF).",
        DOM,
        {"related": ["aku-disciplina-se-extiende-a-todo-claim"]}),
    aku("aku-stress-bueno-y-malo-cortisol-claim", "claim",
        "El estrés es bueno y malo: hace falta algo de estrés para mejorar (hay que empujar cuerpo y mente), y el cortisol que libera da energía y foco; pero el cortisol crónicamente alto reprime la inmunidad, sube la tensión, deposita grasa y causa sobreentrenamiento; el ejercicio condiciona al cuerpo a equilibrar el cortisol, así que hay que estresar el cuerpo algo, pero no en exceso.",
        DOM + ["estres", "fisiologia"],
        {"related": ["aku-gestionar-stress-detach-y-perspectiva-method"]}),
    aku("aku-madrugar-predawn-stand-to-claim", "claim",
        "La mayor excusa para no entrenar es la falta de tiempo, pero hay un momento que nadie te puede quitar: el predawn (antes del amanecer); como el «Stand To» militar (estar despierto y listo para el ataque antes del alba), hay que levantarse antes del sol y atacar el día; cuesta al principio pero se vuelve normal y mejora el día.",
        DOM + ["disciplina", "rutina"],
        {"related": ["aku-no-razonar-con-la-debilidad-solo-actuar-claim", "aku-empezar-aqui-y-ahora-method"]}),
    aku("aku-willpower-no-es-finita-disciplina-engendra-disciplina-claim", "claim",
        "Al contrario de la idea de que la fuerza de voluntad es un recurso finito que se agota con el uso a lo largo del día, la disciplina y la voluntad se fortalecen cuanto más se usan: «la disciplina engendra disciplina, la voluntad propaga más voluntad»; ponerse en el camino (planear el entreno, dejar la ropa lista, listar tareas, madrugar) mantiene en el camino (comer limpio, ejecutar), y salirse de él hace descarrilar todo.",
        DOM + ["disciplina", "voluntad"],
        {"supports": [ROOT_AKU], "related": ["aku-self-discipline-viene-de-dentro-concept"]}),
    aku(SLEEP, "claim",
        "El sueño es una necesidad: su falta provoca cambios hormonales negativos, peor metabolismo de la glucosa, más tensión, inmunidad suprimida, menos hormona de crecimiento (menos músculo y huesos más débiles) y deterioro cognitivo (atención, razonamiento, hasta paranoia y alucinaciones); la mayoría de adultos necesita 7-9 h; para madrugar y dormir lo suficiente, acuéstate antes; estar en forma, comer limpio y tener la mente clara hace dormirse más rápido y necesitar menos.",
        DOM + ["sueno"],
        {"related": ["aku-madrugar-predawn-stand-to-claim"]}),
    aku(FALL, "method",
        "Pasos para conciliar el sueño temprano: (1) cánsate de verdad durante el día (entreno matinal duro; evita entrenar a menos de 2 h de dormir); (2) apaga ordenador y móvil, deja las redes y el clickbait (su luz y su diseño te mantienen despierto); (3) lee un libro relajante —si es demasiado bueno, lee uno aburrido/educativo—; (4) lo clave: madruga (aunque hoy duermas poco, mañana caerás antes); (5) hazlo cada día, incluido el finde, para no romper el ciclo; si necesitas más, echa una power nap.",
        DOM + ["sueno", "habitos"],
        {"related": [SLEEP]}),
    aku(NAP, "method",
        "Técnica de power nap: túmbate, eleva los pies por encima del corazón (alivia el sistema circulatorio y moviliza la sangre estancada en piernas), pon la alarma a 6-8 minutos y duerme; despertarás renovado; advertencia: no dejes que la siesta de 6-8 min se convierta en un sueño de 2 horas o romperás el patrón nocturno.",
        DOM + ["sueno", "recuperacion"],
        {"related": [SLEEP]}),
    aku(SOMETHING, "claim",
        "En un entrenamiento lo más importante es hacer ALGO (caminar, correr, calistenia, nadar, levantar, burpees, jiu-jitsu): el ejercicio no necesita ser una metodología compleja; conviene registrar pesos, repeticiones y tiempos (para seguir el progreso, fijar metas y detectar sobreentrenamiento) y mantener la rutina aunque estés cansado (ve y estira/muévete) —no te tomes el día libre, porque se convierte en una semana—.",
        DOM + ["entrenamiento", "consistencia"],
        {"related": ["aku-not-feeling-it-go-anyway-claim", "aku-analisis-constante-medir-efectividad-claim"]}),
    aku(GYM, "concept",
        "El gimnasio en casa elimina excusas y puede estar en cualquier sitio (garaje, sótano, habitación, patio); el equipo básico esencial es: barra de dominadas, anillas de gimnasia, y un squat rack (con barra de dominadas y dip) más barra olímpica y discos bumper; con eso basta para una forma física excepcional; extras (kettlebells, remo, GHD, etc.) son útiles pero no necesarios.",
        DOM + ["entrenamiento", "equipamiento"],
        {"related": [SOMETHING]}),
]

def links(jb, **extra):
    d = {"justified_by": jb, "constrained_by": [], "breaks_when": [], "illustrates": [], "challenges": []}
    d.update(extra); return d

takus = [
    {
        "id": "taku-conciliar-el-sueno", "taku_type": "protocol",
        "title": "Protocolo para conciliar el sueño temprano",
        "origin": ORIGIN, "domain": ["jocko", "sueno", "habitos"],
        "when_to_use": "Cuando cuesta dormirse a la hora necesaria para madrugar y se quiere fijar un ciclo de sueño consistente.",
        "when_not_to_use": "Ante trastornos del sueño clínicos que requieren evaluación médica.",
        "aku_links": links([FALL, SLEEP]), "taku_relations": {},
        "body": """## Purpose
Lograr dormirse temprano para poder madrugar manteniendo 7-9 h y un ciclo consistente.

## Trigger Conditions
Dificultad para dormirse; ciclo de sueño desajustado; necesidad de madrugar.

## Required Resources
Un libro (preferiblemente aburrido/educativo); disciplina para apagar pantallas; alarma.

## Protocol Steps
1. Cánsate durante el día con un entreno matinal duro (no a menos de 2 h de dormir).
2. Apaga ordenador, móvil y redes antes de acostarte.
3. Lee algo relajante en la cama; si te engancha, cambia a un libro aburrido.
4. Sobre todo: madruga al día siguiente aunque hoy duermas poco.
5. Repite cada día, incluido el fin de semana, para no romper el ciclo.

## Decision Points
¿Sigues despierto? Lee algo más aburrido. ¿Cansancio acumulado? Power nap, no dormir hasta tarde.

## Exit Conditions
Te duermes a la hora objetivo y te levantas a la hora fijada sin romper el patrón.

## Failure Handling
Si rompes el ciclo un día (te acuestas tarde), levántate igualmente a la hora; la falta de sueño de hoy te hará dormir antes mañana.

## Review Trigger
Si el patrón se desajusta de forma recurrente, revisa carga de entrenamiento, cafeína y exposición a pantallas.""",
    },
    {
        "id": "taku-power-nap", "taku_type": "technique",
        "title": "Power nap con pies elevados (6-8 min)",
        "origin": ORIGIN, "domain": ["jocko", "sueno", "recuperacion"],
        "when_to_use": "Cuando estás muy cansado o con déficit de sueño y dispones de 6-15 minutos.",
        "when_not_to_use": "Cerca de la hora de dormir, o si no puedes limitar la duración (riesgo de siesta larga).",
        "aku_links": links([NAP]), "taku_relations": {},
        "body": """## Summary
Siesta corta y reparadora con los pies elevados para recuperar energía sin entrar en sueño profundo.

## When to Use
Bajón de energía, déficit de sueño, pausas en jornadas largas o patrullas.

## Prerequisites
6-15 minutos; un sitio para tumbarse; una superficie para elevar los pies; alarma.

## Steps
1. Túmbate y eleva los pies por encima del corazón.
2. Pon la alarma a 6-8 minutos.
3. Duérmete (si estás cansado será rápido).
4. Levántate al sonar la alarma, renovado.

## Anti-patterns
Dejar que se alargue a 2 horas; hacerla cerca de la hora de dormir.

## Expected Outcome
Sensación de frescura y recuperación de energía.

## Failure Signals
Despertar más aturdido (siesta demasiado larga) o no poder dormir por la noche.

## Underlying Logic
Elevar los pies alivia el sistema circulatorio; la brevedad evita el sueño profundo y el aturdimiento.

## Notes and Variants
Combínalo con el protocolo de sueño nocturno; no lo uses como sustituto del sueño regular.""",
    },
    {
        "id": "taku-home-gym-basico", "taku_type": "tool",
        "title": "Home gym: equipamiento básico",
        "origin": ORIGIN, "domain": ["jocko", "entrenamiento", "equipamiento"],
        "when_to_use": "Al montar un gimnasio en casa para eliminar la excusa de la falta de tiempo o acceso.",
        "when_not_to_use": "No es excusa para no entrenar mientras lo montas: el peso corporal basta para empezar.",
        "aku_links": links([GYM, SOMETHING]), "taku_relations": {},
        "body": """## Summary
Lista mínima de equipamiento para un gimnasio doméstico que permita una forma física excepcional.

## Mechanic
Cubrir los patrones de movimiento (pull, push, lift, squat) con el mínimo de equipo.

## Input
Un espacio (garaje, sótano, habitación, patio) y presupuesto básico.

## Process
1. Barra de dominadas (pull-ups, push-ups, gut, squats).
2. Anillas de gimnasia (dips, pull-ups, push-ups, L-sits, holds).
3. Squat rack (con barra de dominadas y dip) + barra olímpica + discos bumper.

## Output
Capacidad de entrenar todo el cuerpo en casa sin excusas.

## Interpretation Guide
Con barra de dominadas + anillas + rack + barra ya tienes lo esencial; lo demás es opcional.

## Limitations
Extras (kettlebells, remo, air bike, GHD, balones, cajas, bandas) añaden variedad pero no son necesarios.

## Example Application
Garaje convertido en gimnasio; rutinas Pull/Push/Lift/Squat con el equipo básico.""",
    },
]

written, cross = akugen.generate(akus, takus, ROOT, allow_overwrite=True)
print(f"escritos: {len(written)} ficheros")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
