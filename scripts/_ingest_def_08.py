# -*- coding: utf-8 -*-
"""Ingesta — Discipline Equals Freedom, Batch 6C (Fuel/Fasting/Stretch/Injuries/Workouts) + 3 TAKUs. Cierra contenido libro 3."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/discipline-equals-freedom/discipline-equals-freedom.md"
ORIGIN = "Jocko Willink, Discipline Equals Freedom: Field Manual (2017)"
GLU = "aku-homeostasis-glucosa-insulina-concept"
SUGAR = "aku-azucar-es-adictivo-como-droga-claim"
PALEO = "aku-dieta-paleo-fuel-concept"
R100 = "aku-regla-100-no-80-20-claim"
FAST = "aku-ayuno-beneficios-fisicos-y-psicologicos-method"
STRETCH = "aku-estiramiento-rutina-method"
INJ = "aku-lesiones-enfermedad-do-what-you-can-claim"
WARM = "aku-calentamiento-progresivo-method"
WO = "aku-estructura-workout-pull-push-lift-squat-method"
SOMETHING = "aku-en-el-workout-lo-importante-es-hacer-algo-y-trackear-claim"
D = "2026-06-05"
DOM = ["jocko", "nutricion", "salud"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(GLU, "concept",
        "El cuerpo mantiene homeostasis (balance); el nivel de glucosa en sangre lo influimos al comer: los carbohidratos suben el azúcar en sangre → el páncreas libera insulina → empuja el azúcar a las células grasas y frena la quema de grasa → engordas; para usar la grasa como energía hay que agotar antes la glucosa (ejercicio, ayuno o reducir carbohidratos); la insulina crónicamente alta lleva a resistencia a la insulina → diabetes tipo 2, cardiopatía, ceguera, ictus y fallo renal.",
        DOM + ["metabolismo"],
        {"related": ["aku-stress-bueno-y-malo-cortisol-claim"]}),
    aku(SUGAR, "claim",
        "El azúcar es adictivo: estimula las mismas zonas del cerebro que la heroína y la cocaína, así que cuando lo tomas quieres más y al dejarlo sientes síndrome de abstinencia; por eso cuesta tanto dejarlo.",
        DOM + ["adiccion"],
        {"related": [GLU, "aku-comida-basura-es-veneno-claim"]}),
    aku(PALEO, "concept",
        "La «dieta paleo» (fuel) consiste en comer lo que evolucionamos para comer, antes de los granos (que el cuerpo aún no ha adaptado y se convierten en azúcar): comer carne (idealmente de pasto), aves (campero), pescado, huevos, frutos secos, verduras, hongos, raíces, algo de lácteo entero y fruta limitada; evitar granos, patatas, sal refinada, azúcar refinada, aceites procesados y legumbres; invierte la pirámide estándar: sobre todo grasa, luego proteína, mínimos carbohidratos.",
        DOM + ["dieta"],
        {"related": [GLU, "aku-comida-basura-es-veneno-claim"]}),
    aku(R100, "claim",
        "No sigas la regla del 80/20 en la dieta —se desliza a 60/40, 40/60 y al final todo vale—: sigue la regla del 100% (que se volverá 99%, y eso está bien); eres un adicto al azúcar, y ningún adicto puede usar su droga el 20% del tiempo; ir «a pelo» (cold turkey) y mantener la línea es lo que funciona, y con el tiempo pierdes el gusto por lo dulce.",
        DOM + ["dieta", "disciplina"],
        {"related": [PALEO, SUGAR]}),
    aku(FAST, "method",
        "El ayuno es beneficioso y una herramienta ante la falta de comida sana (aeropuerto, fiesta, viaje): no tienes que comer. Beneficios físicos: mejora función de células/genes/hormonas, induce pérdida de grasa, reduce riesgo de resistencia a la insulina/diabetes, reduce estrés oxidativo e inflamación, induce reparación celular, sube BDNF y endorfinas y activa la detoxificación. Beneficios psicológicos: ejercita la voluntad y recalibra el hambre (no estás «muriendo de hambre»: el humano aguanta 30 días). Pauta de Jocko: ayunos de 24 h con regularidad y de 72 h cada ~3 meses, manteniendo la actividad normal.",
        DOM + ["ayuno"],
        {"related": [GLU, PALEO, "aku-mind-control-controla-tu-propia-mente-concept"]}),
    aku(STRETCH, "method",
        "El estiramiento mejora el rango de movimiento, ayuda a la recuperación y previene lesiones; explora rutinas (yoga, Pavel Tsatsouline, MobilityWOD de Kelly Starrett) y quédate con las que te funcionen (p. ej. flexor de cadera de rodillas, swimmer, Cossack, couch stretch, downward dog); estira también usando el rango completo en los calentamientos; con 10-15 min basta, pero hazlo con consistencia como parte de la rutina.",
        DOM + ["movilidad", "recuperacion"],
        {"related": [WARM, SOMETHING]}),
    aku(INJ, "claim",
        "Te vas a lesionar y te vas a poner enfermo porque eres humano; la regla para superarlo es «do what you can» (haz lo que puedas): no lo uses de excusa para saltarte el entreno —¿rodilla mal? trabaja tren superior y la pierna buena; ¿hombro? piernas y core—; si la enfermedad te tumba de verdad, escucha al cuerpo y descansa (sin contagiar en el gimnasio); aprovecha la baja física para hacer cosas que normalmente no tienes tiempo de hacer (escribir, crear, aprender).",
        DOM + ["lesiones", "recuperacion"],
        {"related": ["aku-not-feeling-it-go-anyway-claim", "aku-good-mindset-concept"]}),
    aku(WARM, "method",
        "Calentamiento progresivo antes del entreno: ejercicios o movimientos con peso ligero, lentos y por todo el rango de movimiento; un ciclo (colgarse de la barra, hold en plancha, estirar abdomen/isquios, sentadilla lenta, burpee, jumping jacks) repetido aumentando repeticiones de 1 a 5; luego haz el movimiento del día con peso ligero para calentar y reforzar la memoria muscular; aviso: no levantes peso excesivo ni con mala técnica o te lesionarás.",
        DOM + ["entrenamiento", "calentamiento"],
        {"related": [WO]}),
    aku(WO, "method",
        "Los entrenamientos se estructuran en tipos de movimiento —Pull (tirar), Push (empujar), Lift (levantar) y Squat (sentadilla)—, más trabajo de «Gut» (core) y acondicionamiento metabólico (MetCon); se organizan en tres niveles (principiante, intermedio, avanzado) que sirven de guía y se ajustan a medida que progresas; lo esencial es la consistencia y empezar por meterse en el gimnasio.",
        DOM + ["entrenamiento", "estructura"],
        {"related": [SOMETHING, "aku-home-gym-equipo-basico-concept"]}),
]

def links(jb, **extra):
    d = {"justified_by": jb, "constrained_by": [], "breaks_when": [], "illustrates": [], "challenges": []}
    d.update(extra); return d

takus = [
    {
        "id": "taku-dieta-paleo", "taku_type": "tool",
        "title": "Dieta paleo + regla del 100%",
        "origin": ORIGIN, "domain": ["jocko", "nutricion", "dieta"],
        "when_to_use": "Para estructurar la alimentación hacia el control de la glucosa/insulina y la pérdida de grasa.",
        "when_not_to_use": "Ante condiciones médicas o necesidades nutricionales específicas que requieran supervisión profesional.",
        "aku_links": links([PALEO, R100, GLU]), "taku_relations": {},
        "body": """## Summary
Marco de alimentación basado en comer lo que evolucionamos para comer y mantener la línea al 100%.

## Mechanic
Evitar los alimentos que disparan la insulina (granos, azúcar) y priorizar grasa y proteína.

## Input
Acceso a alimentos frescos; voluntad para mantener la línea.

## Process
COME: carne (de pasto), aves (campero), pescado, huevos, frutos secos, verduras, hongos, raíces, algo de lácteo entero, fruta limitada.
EVITA: granos, patatas, sal refinada, azúcar refinada, aceites procesados, legumbres.
Macros: sobre todo grasa, luego proteína, mínimos carbohidratos.

## Output
Glucosa/insulina controladas, pérdida de grasa, pérdida del «sweet tooth».

## Interpretation Guide
Sigue la regla del 100% (que se vuelve 99%), NO la del 80/20 (resbala a todo vale). Cuando estés adaptado, alguna excursión ocasional ganada con ejercicio.

## Limitations
Cuando no haya comida sana disponible (viaje, eventos): la solución es ayunar, no comer veneno.

## Example Application
Treats limpios: chocolate 80%+ con coco, nata con MCT, frutos secos con nata montada.""",
    },
    {
        "id": "taku-ayuno-intermitente", "taku_type": "protocol",
        "title": "Ayuno (intermitente y prolongado)",
        "origin": ORIGIN, "domain": ["jocko", "nutricion", "ayuno"],
        "when_to_use": "Cuando no hay comida sana disponible, para perder grasa, o para ejercitar la voluntad y recalibrar el hambre.",
        "when_not_to_use": "Ante condiciones médicas (diabetes en tratamiento, embarazo, trastornos alimentarios) sin supervisión.",
        "aku_links": links([FAST, GLU]), "taku_relations": {},
        "body": """## Purpose
Aprovechar los beneficios físicos y psicológicos de no comer durante periodos definidos.

## Trigger Conditions
Falta de comida sana; objetivo de pérdida de grasa; entrenar la voluntad.

## Required Resources
Agua, té; algo para masticar opcional (pipas); voluntad para ignorar el instinto de «come ya».

## Protocol Steps
1. Decide la ventana (p. ej. 24 h con regularidad; 72 h cada ~3 meses).
2. Mantén tu actividad normal: trabaja, entrena, haz jiu-jitsu.
3. Hidrátate (agua, té); ignora la señal de hambre («no estás muriendo de hambre»).
4. Rompe el ayuno con comida limpia (paleo).

## Decision Points
¿Es hambre real o aburrimiento? Casi siempre es aburrimiento o costumbre.

## Exit Conditions
Fin de la ventana de ayuno; la comida sabrá mejor y el hambre quedará recalibrada.

## Failure Handling
Si te mareas o hay señales médicas reales, rompe el ayuno con comida limpia y consulta si procede.

## Review Trigger
Tras varios ayunos, evalúa cómo ha cambiado tu percepción del hambre y tu energía.""",
    },
    {
        "id": "taku-rutina-entrenamiento-jocko", "taku_type": "tool",
        "title": "Estructura de entrenamiento: warm-up + Pull/Push/Lift/Squat",
        "origin": ORIGIN, "domain": ["jocko", "entrenamiento"],
        "when_to_use": "Para estructurar sesiones de entrenamiento de fuerza/acondicionamiento de forma consistente.",
        "when_not_to_use": "Como excusa para no entrenar mientras lo perfeccionas: lo importante es hacer ALGO con consistencia.",
        "aku_links": links([WO, WARM, SOMETHING]), "taku_relations": {},
        "body": """## Summary
Plantilla de sesión: calentamiento progresivo + trabajo en torno a cuatro patrones de movimiento.

## Mechanic
Calentar por rango de movimiento, luego trabajar Pull/Push/Lift/Squat + Gut + MetCon según el nivel.

## Input
Equipo básico (barra de dominadas, anillas, rack+barra); 10-15 min de calentamiento.

## Process
1. Warm-up: ciclo (colgarse, plancha, estiramientos, sentadilla lenta, burpee, jumping jacks) subiendo de 1 a 5 reps; luego el movimiento del día con peso ligero.
2. Trabajo principal: Pull, Push, Lift, Squat (+ Gut, + MetCon) según nivel (principiante/intermedio/avanzado).
3. Registra pesos, repeticiones y tiempos.

## Output
Sesión completa que cubre los patrones fundamentales y refuerza la memoria muscular.

## Interpretation Guide
Los tres niveles son una guía: ajusta a medida que progresas; escucha al cuerpo al final de cada sesión (cuándo empujar, cuándo contener).

## Limitations
No levantes peso excesivo ni con mala técnica (riesgo de lesión). Si estás lesionado, «do what you can».

## Example Application
Sesión diaria predawn con el equipo del home gym; estiramiento 10-15 min como parte de la rutina.""",
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
