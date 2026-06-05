# -*- coding: utf-8 -*-
"""Ingesta — Leadership Strategy and Tactics, Part 2 Sec 1 'Becoming a Leader' + 3 TAKUs."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/leadership-strategy-and-tactics/leadership-strategy-and-tactics.md"
ORIGIN = "Jocko Willink, Leadership Strategy and Tactics: Field Manual (2020)"
RULES = "aku-12-reglas-del-nuevo-lider-method"
IMPOSTER = "aku-imposter-syndrome-es-bueno-claim"
SHERIFF = "aku-new-sheriff-cambio-segun-estado-equipo-method"
INDIRECT = "aku-liderazgo-indirecto-supera-al-directo-claim"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(RULES, "method",
        "Doce reglas fundamentales para tener éxito como nuevo líder: (1) sé humilde; (2) no actúes como si lo supieras todo, haz preguntas inteligentes; (3) escucha y atiende los consejos; (4) trata a todos con respeto; (5) asume los fallos y errores; (6) pasa el crédito de los éxitos arriba y abajo; (7) trabaja más duro que nadie, ningún trabajo está por debajo de ti; (8) ten integridad (haz lo que dices); (9) sé equilibrado (los extremos rara vez son buenos); (10) sé decisivo; (11) construye relaciones (tu meta principal); (12) cumple la misión (el rendimiento cuenta).",
        DOM + ["nuevo-lider"],
        {"related": ["aku-humildad-es-la-cualidad-mas-importante-claim", "aku-lider-conoce-trabajos-y-pide-ayuda-claim", "aku-power-of-relationships-liderazgo-concept"]}),
    aku("aku-como-ser-elegido-lider-claim", "claim",
        "Para que te elijan líder: lo número uno es el rendimiento (trabaja duro, sé el primero en llegar y el último en irse, ofrécete para las tareas difíciles e ingratas); y no hagas de «ser elegido» tu meta, sino de «ayudar al equipo a ganar» —sé buen seguidor cuando otro toma el mando—; pero no seas tan humilde que parezca que no quieres liderar: ofrécete cuando puedas.",
        DOM + ["ascenso", "rendimiento"],
        {"related": ["aku-rendimiento-construye-confianza-del-jefe-claim", "aku-mejores-lideres-mision-no-ego-claim"]}),
    aku("aku-cuando-no-te-eligen-pedir-feedback-method", "method",
        "Cuando no te eligen: guárdate la frustración; haz una autoevaluación honesta y, ya calmado, pide feedback al superior con tacto («quiero prepararme para liderar cuando llegue la próxima oportunidad, ¿en qué puedo mejorar?», no «¿por qué no me elegiste a mí que soy mejor?»); escucha de verdad y asume tus carencias; y no guardes rencor a quien ascendió —apóyalo y ayúdale a ganar—.",
        DOM + ["feedback", "ascenso"],
        {"related": ["aku-humildad-asumir-errores-claim", "aku-regret-solo-vale-por-la-leccion-claim"]}),
    aku(IMPOSTER, "claim",
        "El «imposter syndrome» (sentir que no estás listo o que no mereces el puesto) es en realidad bueno: significa humildad, que te prepararás a fondo y serás reflexivo con tus palabras, actos y decisiones; el extremo opuesto —sentirse eminentemente cualificado, sin necesidad de prepararse ni escuchar— es arrogancia que destruye al líder y al equipo; pero hay que equilibrar, porque demasiada poca confianza también es visible y dañina.",
        DOM + ["confianza", "humildad"],
        {"related": ["aku-humildad-es-la-cualidad-mas-importante-claim", "aku-confident-but-not-cocky-concept"]}),
    aku("aku-senales-de-confianza-desequilibrada-claim", "claim",
        "Señales de exceso de confianza: fricción con el equipo, o una ausencia total de resistencia (callan porque saben que les tumbarás las ideas); señal de falta de confianza (imposter): el equipo no respeta tus ideas y te tumba en cada esquina; solución al exceso: da un paso atrás y deja que lideren; solución al imposter: ábrete, haz preguntas y pide input, en vez de encerrarte.",
        DOM + ["confianza", "ego"],
        {"related": [IMPOSTER, "aku-confident-but-not-cocky-concept", "aku-check-the-ego-concept"]}),
    aku("aku-inseguridad-admitir-no-ocultar-claim", "claim",
        "La inseguridad se vuelve problema cuando intentas ocultarla (desvías conversaciones, evitas preguntas, usas subterfugios): todos lo ven, y cuanto más lo tapas, más obvio es y más te atacan; la forma de superarla es la contraria: admite con humildad tus vulnerabilidades, exponlas y pide ayuda (humildad + vulnerabilidad te hacen mejor), sin pasarte presentándote como incompetente.",
        DOM + ["humildad", "vulnerabilidad"],
        {"related": [IMPOSTER, "aku-lider-conoce-trabajos-y-pide-ayuda-claim"]}),
    aku("aku-transicion-de-par-a-lider-claim", "claim",
        "Al pasar de par/seguidor a líder de tu propio grupo hay que dar el paso y diferenciar quién eras de quién eres ahora: trae un plan, da dirección simple/clara/concisa, mantente humilde y escucha, y lidera (caso Larry vs Brian); además, sal de la maleza —«look up and out, not down and in», deja que la tropa haga el hacer— sin caer en la aloofness; ni con las manos en los bolsillos ni con las manos en todo.",
        DOM + ["transicion", "nuevo-lider"],
        {"related": ["aku-liderar-desde-frente-y-desde-atras-concept", "aku-dar-ordenes-solo-commanders-intent-claim"]}),
    aku("aku-overcoming-grudge-ex-pares-method", "method",
        "Cuando te ascienden por encima de tus antiguos pares: no les impongas el rango; agradece su experiencia y diles que contarás con ellos, déjales proponer planes y ponles al cargo de tareas (les demuestra confianza); pero algunos hipersensibles lo verán como condescendencia —si carecen de la humildad y madurez para liderar (lo más probable por lo que no ascendieron), sé cordial y paciente sin esperar mejora rápida y no dejes que te distraigan de la misión—.",
        DOM + ["relaciones", "ascenso"],
        {"related": ["aku-dar-confianza-incrementalmente-method", "aku-humildad-es-la-cualidad-mas-importante-claim"]}),
    aku(SHERIFF, "method",
        "Al tomar el mando de un equipo, el enfoque depende de su estado (conócelo antes vía documentos, turnover y expedientes): equipo bueno → entra suave, «if it ain't broke don't fix it», observa y construye relaciones; equipo que falla con causa conocida → agresivo, cambios inmediatos, visión clara, mover/terminar personas; equipo que falla con causa desconocida → cambios benignos que llaman la atención sin interferir (comunicación, reuniones, código de vestimenta), entrevista todos los niveles buscando trusted agents y haz cambios de impacto de forma incremental; ojo: el líder saliente pudo ser la causa, no estorbes al equipo cuando se libere de él.",
        DOM + ["transicion", "cambio"],
        {"related": ["aku-dar-confianza-incrementalmente-method", "aku-corregir-micromanagement-method"]}),
    aku(INDIRECT, "claim",
        "El liderazgo casi siempre debe ser sutil e indirecto: no vayas pregonando «¡yo mando, escúchenme!» (ofende egos —«don't be Rambo»—); lidera por sugerencia, pon tus ideas y deja que la tropa las adopte como propias (instila ownership), y haz igual al mentorizar/coachear («¿cómo crees que deberíamos ejecutar?» en vez de «déjame que te enseñe»); PERO el liderazgo directo es necesario en momentos de presión, emergencia o indecisión —y como el líder se contiene normalmente, cuando da la orden directa se le respeta (una voz que se oye demasiado pierde valor)—.",
        DOM + ["influencia", "comunicacion"],
        {"related": ["aku-dar-ordenes-solo-commanders-intent-claim", "aku-lider-percibido-como-decisivo-claim", "aku-decentralizar-proceso-planificacion-claim"]}),
]

def links(jb, **extra):
    d = {"justified_by": jb, "constrained_by": [], "breaks_when": [], "illustrates": [], "challenges": []}
    d.update(extra); return d

takus = [
    {
        "id": "taku-nuevo-lider", "taku_type": "tool",
        "title": "Las 12 reglas del nuevo líder",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "nuevo-lider"],
        "when_to_use": "Al asumir una nueva posición de liderazgo; revísalas a menudo (mañana, antes de reuniones, antes de dormir).",
        "when_not_to_use": "No como sustituto del juicio situacional: son fundamentos, no una receta rígida.",
        "aku_links": links([RULES, "aku-humildad-es-la-cualidad-mas-importante-claim"]),
        "taku_relations": {},
        "body": """## Summary
Checklist de doce fundamentos para empezar con buen pie como nuevo líder.

## Mechanic
Revisar y aplicar las 12 reglas hasta que se vuelvan segunda naturaleza.

## Input
Una nueva posición de liderazgo y disposición a la autoevaluación frecuente.

## Process
1. Sé humilde. 2. No actúes como si lo supieras todo; pregunta. 3. Escucha y atiende consejos. 4. Respeta a todos. 5. Asume fallos. 6. Pasa el crédito arriba y abajo. 7. Trabaja más que nadie. 8. Ten integridad. 9. Sé equilibrado. 10. Sé decisivo. 11. Construye relaciones. 12. Cumple la misión.

## Output
Arranque sólido en el rol, con respeto y confianza del equipo.

## Interpretation Guide
Si te sientes perdido, párate y relee la lista para comprobar cuál estás incumpliendo.

## Limitations
No eres infalible ni omnisciente: prepárate (terminología, principios, nombres y caras) sin usar lo «nuevo» como excusa de ignorancia.

## Example Application
Larry, al ser nombrado LPO, dio guía clara y humilde en 30 minutos; Brian floundered por no dar el paso.""",
    },
    {
        "id": "taku-tomar-el-mando-nuevo-equipo", "taku_type": "protocol",
        "title": "Tomar el mando de un equipo (New Sheriff in Town)",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "transicion", "cambio"],
        "when_to_use": "Al asumir el liderazgo de un equipo ya existente, para calibrar el ritmo y alcance del cambio.",
        "when_not_to_use": "No apliques cambios uniformes: el enfoque debe modularse según el estado real del equipo.",
        "aku_links": links([SHERIFF, "aku-dar-confianza-incrementalmente-method"]),
        "taku_relations": {},
        "body": """## Purpose
Entrar en un equipo nuevo con el nivel de cambio adecuado a su estado, sin romper lo que funciona ni tolerar lo que no.

## Trigger Conditions
Asumir el mando de un equipo existente.

## Required Resources
Documentos de operaciones, turnover del líder saliente (con su sesgo), expedientes/guía de personal.

## Protocol Steps
1. Estudia mission y personas antes de llegar; ten en cuenta el sesgo del saliente.
2. Diagnostica el estado del equipo (bueno / falla con causa conocida / falla con causa desconocida).
3. Equipo bueno → entra suave, observa, construye relaciones, mejora incrementalmente.
4. Falla con causa conocida → agresivo: visión clara, cambios inmediatos, mover/terminar personas.
5. Falla con causa desconocida → cambios benignos (comms/reuniones/vestimenta), entrevista todos los niveles, busca trusted agents, cambia de impacto de forma incremental.

## Decision Points
¿Qué funciona (no tocar) y qué no (ajustar)? ¿El líder saliente era la causa?

## Exit Conditions
El equipo alcanza máxima eficiencia; tus cambios se estabilizan.

## Failure Handling
Si una emoción del equipo en crisis te da info falsa, tómala con cautela; valida con varias fuentes.

## Review Trigger
Modula guía/interacción/dirección según el desempeño real conforme el equipo progresa.""",
    },
    {
        "id": "taku-liderazgo-indirecto", "taku_type": "heuristic",
        "title": "Liderazgo indirecto: liderar por sugerencia",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "influencia"],
        "when_to_use": "En situaciones cotidianas, para guiar, mentorizar o coachear sin activar defensas ni egos.",
        "when_not_to_use": "En emergencias, presión o indecisión del equipo: ahí toca liderazgo directo y decisivo.",
        "aku_links": links([INDIRECT, "aku-dar-ordenes-solo-commanders-intent-claim"]),
        "taku_relations": {},
        "body": """## The Rule
Lidera, coachea y mentoriza por sugerencia e indirección, dejando que la tropa adopte tus ideas como propias; sé directo solo cuando haga falta.

## What It Replaces
El «¡yo mando, escúchenme!» (Rambo) y el «déjame que te enseñe» que ofenden egos y activan defensas.

## When It Holds
En el día a día, donde la dirección sutil genera ownership y compromiso.

## When It Fails
En duress/emergencia/indecisión: ahí el líder debe dar la orden directa, y se le respetará precisamente porque normalmente se contiene.

## Why It Works
La gente prefiere sus propias ideas; sembrarlas indirectamente instila ownership. Una voz que se oye demasiado pierde valor.

## Calibration
Frases: «¿cómo crees que deberíamos ejecutar?» / «¿puedes explicarme por qué lo haces así?» / «me encantaría comparar cómo lo haces tú con cómo lo hago yo». Sé sutil… hasta que no puedas; entonces lidera.""",
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
