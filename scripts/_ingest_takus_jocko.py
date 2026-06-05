# -*- coding: utf-8 -*-
"""Crea los 6 TAKUs flaggeados de los libros 1-2 de Jocko (estructuras ejecutables)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGIN = "Jocko Willink & Leif Babin (Extreme Ownership / The Dichotomy of Leadership)"
D = "2026-06-05"

def jb(*ids):
    return {"justified_by": list(ids)}

takus = [
    {
        "id": "taku-laws-of-combat", "taku_type": "framework",
        "title": "Las cuatro Leyes del Combate (Laws of Combat)",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "equipos", "combate"],
        "when_to_use": "Cuando un equipo debe ejecutar bajo presión, caos o incertidumbre y se busca máximo rendimiento coordinado.",
        "when_not_to_use": "Como sustituto del fundamento (Extreme Ownership): las leyes operan sobre esa base, no la reemplazan.",
        "aku_links": jb("aku-laws-of-combat-concept", "aku-cover-and-move-concept", "aku-simple-law-of-combat-concept", "aku-prioritize-and-execute-concept", "aku-decentralized-command-concept"),
        "taku_relations": {"complementary": ["taku-prioritize-and-execute"]},
        "body": """## Summary
Las cuatro Leyes del Combate son el marco operativo que, aplicado conjuntamente, permite a cualquier equipo rendir al máximo y dominar: son interdependientes y mutuamente reforzantes.

## Core Components
1. **Cover and Move** — trabajo en equipo: todos los elementos se apoyan mutuamente; romper silos.
2. **Simple** — planes y órdenes simples, claros y concisos; si el equipo no lo entiende, has fallado.
3. **Prioritize and Execute** — determinar la prioridad más alta y ejecutarla, una a una («Relax, look around, make a call»).
4. **Decentralized Command** — equipos de 4-6 con líderes empoderados que entienden el Commander's Intent.

## How to Apply
Briefar las cuatro leyes como lenguaje común del equipo; ante el caos, recurrir a ellas en orden de necesidad; el líder mantiene la perspectiva estratégica mientras los subordinados ejecutan.

## Underlying Claims
Ver AKUs enlazados: cada ley está soportada por su concepto y sus claims/métodos.

## Strengths
Aplicable a cualquier equipo (combate, negocio, deporte); convierte el caos en ejecución coordinada; escala vía mando descentralizado.

## Limitations and Criticisms
Requiere el fundamento de Extreme Ownership y entrenamiento; sin cultura de ownership, las leyes se aplican mecánicamente y pierden eficacia.

## Variants and Extensions
Cada ley tiene su propio desarrollo (ver taku-prioritize-and-execute). Se complementa con el proceso de planificación.""",
    },
    {
        "id": "taku-prioritize-and-execute", "taku_type": "protocol",
        "title": "Prioritize and Execute (priorizar y ejecutar bajo presión)",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "priorizacion", "decision"],
        "when_to_use": "Cuando múltiples problemas se acumulan simultáneamente y el líder o el equipo se sienten abrumados.",
        "when_not_to_use": "Cuando solo hay una tarea o no hay presión de simultaneidad; el protocolo añade fricción innecesaria.",
        "aku_links": jb("aku-prioritize-and-execute-concept", "aku-prioritize-and-execute-pasos-method", "aku-relax-look-around-make-a-call-method"),
        "taku_relations": {"complementary": ["taku-laws-of-combat", "taku-planning-checklist"]},
        "body": """## Purpose
Evitar el fallo por intentar abordar demasiados problemas a la vez, concentrando el esfuerzo en la prioridad más alta.

## Trigger Conditions
Sobrecarga de problemas simultáneos; sensación de estar abrumado; el equipo se dispersa.

## Required Resources
Conciencia situacional; capacidad de detach (apartarse de la línea de fuego); comunicación con el equipo.

## Protocol Steps
1. «Relax, look around, make a call» — recuperar la calma y evaluar.
2. Evaluar el problema de mayor prioridad.
3. Exponerlo en términos simples, claros y concisos.
4. Desarrollar la solución buscando input de líderes clave.
5. Dirigir la ejecución concentrando todos los recursos.
6. Pasar a la siguiente prioridad y repetir.
7. Comunicar los cambios de prioridad arriba y abajo.

## Decision Points
¿Ha cambiado la prioridad más alta? ¿Hay target fixation? Reevaluar continuamente.

## Exit Conditions
Cuando los problemas críticos están bajo control y el equipo ejecuta de forma estable.

## Failure Handling
Si surge target fixation, forzar un paso atrás y re-priorizar; si el equipo no ejecuta, revisar claridad y autoridad.

## Review Trigger
Tras la operación, en el post-operational debrief.""",
    },
    {
        "id": "taku-planning-checklist", "taku_type": "tool",
        "title": "Checklist de planificación del líder",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "planificacion"],
        "when_to_use": "Al planificar cualquier misión, proyecto u operación que requiera coordinación y mitigación de riesgo.",
        "when_not_to_use": "Para tareas triviales o reactivas inmediatas donde la planificación formal sobra.",
        "aku_links": jb("aku-leaders-checklist-planning-method", "aku-planning-process-estandarizado-concept", "aku-priorizar-3-4-contingencias-mas-probables-method"),
        "taku_relations": {"complementary": ["taku-prioritize-and-execute"], "precedes": [{"id": "taku-post-operational-debrief", "sequence_type": "recommended"}]},
        "body": """## Summary
Checklist repetible y estandarizado para planificar maximizando la probabilidad de éxito y minimizando el riesgo.

## Mechanic
Recorrer una lista de comprobación fija que cubre análisis de misión, recursos, descentralización, curso de acción, contingencias, riesgo, brief y debrief.

## Input
Misión y Commander's Intent del mando superior; personal, activos, recursos y tiempo disponibles.

## Process
1. Analizar la misión (intent y endstate superior + el propio). 2. Identificar recursos y tiempo. 3. Descentralizar la planificación. 4. Determinar el curso de acción más simple. 5. Empoderar a líderes clave para desarrollarlo. 6. Planificar las 3-4 contingencias más probables por fase + peor caso. 7. Mitigar riesgos controlables. 8. Delegar y «stand back and be the tactical genius». 9. Cuestionar el plan contra info emergente. 10. Briefar a todos enfatizando el intent. 11. Hacer debrief tras ejecutar.

## Output
Plan simple, comprendido por la primera línea, con contingencias y riesgos gestionados.

## Interpretation Guide
La prueba del brief: ¿lo entienden el equipo y los apoyos? Si no, simplificar.

## Limitations
No se puede planificar cada contingencia; el exceso de planificación abruma. Mantenerse flexible.

## Example Application
Operación SEAL o lanzamiento de proyecto: del análisis de misión al debrief post-ejecución.""",
    },
    {
        "id": "taku-post-operational-debrief", "taku_type": "protocol",
        "title": "Post-Operational Debrief (debrief tras la operación)",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "mejora-continua"],
        "when_to_use": "Después de cada operación, proyecto o iteración significativa, por agotado u ocupado que esté el equipo.",
        "when_not_to_use": "No aplica como sustituto de la corrección en tiempo real durante la ejecución.",
        "aku_links": jb("aku-post-operational-debrief-method", "aku-analisis-constante-medir-efectividad-claim"),
        "taku_relations": {"follows": [{"id": "taku-planning-checklist", "sequence_type": "recommended"}]},
        "body": """## Purpose
Extraer lecciones de cada operación e implementarlas para no repetir errores y mejorar continuamente.

## Trigger Conditions
Finalización de una operación, proyecto, sprint o iteración.

## Required Resources
Tiempo reservado (aunque haya agotamiento); honestidad brutal; participación de los ejecutores.

## Protocol Steps
1. Examinar todas las fases (de la planificación a la ejecución) en formato conciso.
2. ¿Qué salió bien?
3. ¿Qué salió mal?
4. ¿Cómo adaptamos las tácticas para ser más efectivos?
5. Documentar e implementar las lecciones en la planificación futura.

## Decision Points
¿Qué lecciones cambian el SOP o el próximo plan? ¿Qué se repite?

## Exit Conditions
Lecciones capturadas y asignadas a la siguiente iteración de planificación.

## Failure Handling
Si el debrief degenera en culpas, reconducir con Extreme Ownership: foco en el problema, no en la persona.

## Review Trigger
Cada operación; alimenta el siguiente ciclo de planificación.""",
    },
    {
        "id": "taku-dichotomy-of-leadership", "taku_type": "framework",
        "title": "La Dicotomía del Liderazgo (equilibrar fuerzas opuestas)",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "dicotomia"],
        "when_to_use": "Cuando un líder debe calibrar su conducta entre dos extremos opuestos (mandar/seguir, agresivo/prudente, etc.).",
        "when_not_to_use": "No es una fórmula fija: el punto de equilibrio depende del contexto y debe re-evaluarse.",
        "aku_links": jb("aku-dichotomy-of-leadership-concept", "aku-lider-se-desvia-por-inclinarse-demasiado-claim", "aku-balance-ownership-decentralized-command-concept"),
        "taku_relations": {"complementary": ["taku-diagnostico-micromanagement-hands-off"]},
        "body": """## Summary
Liderar bien es hallar el equilibrio entre cualidades aparentemente contradictorias; el mero reconocimiento de la dicotomía es una de las herramientas más poderosas del líder.

## Core Components
Las dicotomías clave: cuidar/cumplir misión, ownership/empower, resoluto/no prepotente, mentorizar/despedir, entrenar duro/inteligente, agresivo/no temerario, disciplinado/no rígido, accountability/no de la mano, líder/seguidor, planificar/flexible, humilde/no pasivo, enfocado/desapegado.

## How to Apply
Ante un problema de liderazgo, identificar qué dicotomía está en juego y hacia qué extremo se ha inclinado uno; corregir hacia el centro.

## Underlying Claims
Cuando un líder falla, suele ser por inclinarse demasiado en una dirección (ver AKU enlazado).

## Strengths
Marco diagnóstico universal; convierte problemas difusos de liderazgo en una pregunta concreta de equilibrio.

## Limitations and Criticisms
No da el punto de equilibrio exacto: requiere juicio y depende del contexto; mal usado, justifica la indecisión.

## Variants and Extensions
Cada dicotomía es un AKU propio con sus dos extremos de fallo; se complementa con el diagnóstico micromanagement/hands-off.""",
    },
    {
        "id": "taku-diagnostico-micromanagement-hands-off", "taku_type": "protocol",
        "title": "Diagnóstico y corrección: micromanagement vs hands-off",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "mando"],
        "when_to_use": "Cuando el rendimiento del equipo decae y se sospecha un desequilibrio en el estilo de mando del líder.",
        "when_not_to_use": "Cuando el problema es de competencia individual o recursos, no de estilo de liderazgo.",
        "aku_links": jb("aku-sintomas-de-micromanagement-method", "aku-sintomas-de-hands-off-method", "aku-corregir-micromanagement-method", "aku-corregir-hands-off-method", "aku-balance-ownership-decentralized-command-concept"),
        "taku_relations": {"complementary": ["taku-dichotomy-of-leadership"]},
        "body": """## Purpose
Detectar hacia qué extremo (micromanagement o hands-off) se ha desequilibrado el líder y reencauzarlo.

## Trigger Conditions
Caída de rendimiento, falta de iniciativa o, por el contrario, descoordinación y esfuerzos en conflicto.

## Required Resources
Observación del equipo; honestidad del líder para autoevaluarse.

## Protocol Steps
1. Chequear los 7 síntomas de micromanagement (falta de iniciativa, esperar soluciones, no movilizarse, poca audacia, creatividad detenida, quedarse en el silo, pasividad).
2. Chequear los 6 síntomas de hands-off (falta de visión, descoordinación, iniciativa que sobrepasa autoridad, fallo por ignorancia, prioridad equivocada, demasiados líderes).
3. Si micromanagement: aplicar la corrección (retirarse del detalle, dar objetivo+endstate+porqué, dejar planificar, monitorizar sin guiar, apartarse cuando se pueda).
4. Si hands-off: aplicar la corrección (guía clara, límites, decidir el curso, desconflictar, asignar cadena de mando).

## Decision Points
¿Qué conjunto de síntomas predomina? Ajustar hacia el centro sin pasarse al otro extremo.

## Exit Conditions
El equipo ejecuta con iniciativa y coordinación: guiado pero libre para decidir.

## Failure Handling
Si tras corregir aparece el extremo opuesto, recalibrar de nuevo; es un equilibrio dinámico.

## Review Trigger
Revisar periódicamente; el equilibrio se desplaza con el contexto y la madurez del equipo.""",
    },
]

written, cross = akugen.generate([], takus, ROOT)
print(f"escritos: {len(written)} TAKUs")
for w in written:
    print("  +", os.path.relpath(w, ROOT))
