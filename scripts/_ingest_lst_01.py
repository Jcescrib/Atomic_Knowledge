# -*- coding: utf-8 -*-
"""Ingesta — Leadership Strategy and Tactics, Sección 1 'Foundations' + 2 TAKUs."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/leadership-strategy-and-tactics/leadership-strategy-and-tactics.md"
ORIGIN = "Jocko Willink, Leadership Strategy and Tactics: Field Manual (2020)"
REL = "aku-power-of-relationships-liderazgo-concept"
LONG = "aku-play-the-long-game-concept"
DISOBEY = "aku-cuando-desobedecer-ultimo-recurso-method"
REDIR = "aku-redirigir-al-jefe-onus-en-ti-method"
PERF = "aku-rendimiento-construye-confianza-del-jefe-claim"
EGO = "aku-subordinate-your-ego-desactiva-choque-method"
BORN = "aku-lideres-nacen-y-se-hacen-claim"
COMP = "aku-lider-compensa-debilidades-con-el-equipo-claim"
TRUTH = "aku-lideres-dicen-la-verdad-claim"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(REL, "concept",
        "El liderazgo requiere relaciones: buenas relaciones hacia arriba, hacia abajo y a los lados de la cadena de mando son la base de todo buen liderazgo; cuanto mejores son las relaciones, más abierta y eficaz es la comunicación, y cuanta más comunicación, más fuerte el equipo.",
        DOM + ["relaciones"],
        {"related": ["aku-confianza-se-construye-no-se-da-claim", "aku-leading-up-the-chain-concept", "aku-leading-down-the-chain-concept"]}),
    aku(REDIR, "method",
        "Para redirigir a un jefe que va por mal camino, hazlo con tacto poniendo el onus en ti mismo («quiero apoyar el plan pero me cuesta entender esta parte; ¿puedes explicarme por qué quieres hacerlo así?»); antes, pregúntate: ¿cuánto se gana?, ¿es solo mi ego?, ¿muevo la relación hacia delante o hacia atrás? Elige tus batallas con cuidado.",
        DOM + ["influencia", "comunicacion"],
        {"related": ["aku-preguntar-por-que-method", "aku-leadership-capital-concept", REL]}),
    aku(PERF, "claim",
        "La forma más simple de construir confianza con los superiores es el rendimiento: completa las tareas a tiempo, en presupuesto y sin drama —incluidas las que no compartes del todo—, sé la solución a cada problema y no te quejes ni busques elogios; así ganas «clout» y, cuando sí planteas una objeción, el jefe escucha (porque «cuanto más hablas, menos te escuchan»).",
        DOM + ["confianza", "rendimiento"],
        {"related": ["aku-presentar-frente-unido-claim", "aku-ejecutar-decision-como-propia-claim", "aku-leadership-capital-concept"]}),
    aku(LONG, "concept",
        "«Play the long game» (juega a largo plazo): no la fuerza bruta de tierra quemada (funciona a corto y luego destruye todo), sino apoyar al jefe y construir confianza y relaciones arriba y abajo (escuchar y decir sí cuando puedas, para que tu «no» se acepte después); no por interés personal ni ascenso, sino para cumplir la misión; no es debilidad ni adulación, es optimizar y acumular leadership capital.",
        DOM + ["estrategia", "relaciones"],
        {"related": ["aku-leadership-capital-concept", REL, PERF]}),
    aku(DISOBEY, "method",
        "Desobedecer al jefe es el último recurso (causa enorme disrupción y casi no se puede deshacer); hay que rehusar las órdenes ilegales/inmorales/no éticas (y reportarlas). Antes de negarse: pide al jefe que reformule el propósito, presenta tus preocupaciones y una solución de forma indirecta y sin ofender (onus en ti, dale una salida airosa atando la idea a él), documenta y escala el caso; sopesa los desenlaces de negarte (puede reconsiderar; o cavar más hondo y poner a un yes-man; o perder toda influencia). Napoleón: el subordinado que ejecuta una misión que sabe equivocada es culpable.",
        DOM + ["cadena-de-mando", "etica", "decision"],
        {"related": ["aku-excepcion-resistir-ordenes-ilegales-inmorales-claim", "aku-ejecutar-decision-como-propia-claim", "aku-preguntar-por-que-method"]}),
    aku(BORN, "claim",
        "¿Los líderes nacen o se hacen? Ambos: se nace con rasgos útiles (ser articulado, saber simplificar, carisma, voz potente, leer a la gente) limitados por la genética, pero todos se pueden mejorar con práctica; y un líder construye un equipo que contrarresta sus debilidades; la única excepción es quien carece de humildad: nunca mejora porque no reconoce sus debilidades.",
        DOM + ["talento", "humildad"],
        {"related": ["aku-eleccion-vence-naturaleza-y-crianza-claim", "aku-humildad-es-la-cualidad-mas-importante-claim", COMP]}),
    aku(COMP, "claim",
        "Un buen líder compensa sus propias debilidades incorporando al equipo a personas que las contrarrestan (el oficial SEAL de voz débil usaba a su hombre más vocal para retransmitir las órdenes); combinado con el trabajo por mejorar, así se superan incluso los mayores déficits de liderazgo.",
        DOM + ["equipos", "talento"],
        {"related": ["aku-span-of-control-concept"]}),
    aku("aku-liderazgo-vs-manipulacion-concept", "concept",
        "Liderazgo y manipulación usan las mismas técnicas (construir relaciones, influencia, maniobra política, capitalizar egos) y ambos buscan que la gente haga lo que quieres (idealmente porque ellos quieren); la diferencia única y decisiva: el manipulador busca su propio beneficio, el líder el del equipo y las personas; ambas actitudes acaban aflorando, y a largo plazo el verdadero líder gana.",
        DOM + ["influencia", "etica"],
        {"related": ["aku-mejores-lideres-mision-no-ego-claim", "aku-check-the-ego-concept"]}),
    aku(EGO, "method",
        "Para desactivar un choque de egos, subordina tu PROPIO ego: humíllate un momento y da crédito al otro; el ego es como blindaje reactivo (cuanto más empujas, más empuja) así que se desarma rebajando el propio; subordinar el ego es la forma suprema de autoconfianza y gana respeto —si no puedes hacerlo por miedo a parecer débil, es que eres débil—.",
        DOM + ["ego", "relaciones"],
        {"related": ["aku-check-ego-asumiendo-culpa-primero-method", "aku-check-the-ego-concept", "aku-el-ego-mas-dificil-es-el-propio-claim"]}),
    aku(TRUTH, "claim",
        "La verdad y la honestidad son quizá las cualidades de liderazgo más esenciales: di la verdad a tu gente, a tu jefe, a tus pares y a ti mismo, con tacto; las verdades duras (estamos perdiendo, tu desempeño es deficiente) hay que decirlas pronto y a menudo (si no, los rumores y la desconfianza se agravan y se pierde la creencia en el líder); incluso cuando algo es confidencial, di la verdad sobre por qué no puedes decir la verdad.",
        DOM + ["honestidad", "comunicacion"],
        {"related": ["aku-believe-in-the-mission-concept", "aku-senior-debe-explicar-el-porque-claim", "aku-humildad-asumir-errores-claim"]}),
    aku("aku-no-usar-sandwich-de-critica-claim", "claim",
        "La técnica del «sándwich» (meter la crítica negativa entre dos halagos) es un atajo para no tener relaciones reales con tu gente; no deberías fabricar puntos buenos para envolver los malos: con una buena relación no hace falta; aun así, como a casi nadie le gusta la crítica, lo mejor es entregarla de forma indirecta y con la mínima negatividad necesaria para lograr el cambio.",
        DOM + ["feedback", "relaciones"],
        {"related": [TRUTH, REL]}),
    aku("aku-estudiar-liderazgo-lente-de-liderazgo-claim", "claim",
        "Un líder nunca es lo bastante bueno y debe estudiar y mejorar siempre: mira todo a través de la «lente del liderazgo» (en cualquier grupo está ocurriendo liderazgo: observa qué funciona), aplícala a lo que lees y a la historia, y superpón los principios (Cover and Move, Simple, Prioritize and Execute, Decentralized Command, Extreme Ownership, Dicotomía) a todo lo que ves; nada de esto ocurre sin humildad.",
        DOM + ["aprendizaje", "humildad"],
        {"related": ["aku-lideres-nunca-satisfechos-mejora-continua-claim", "aku-humildad-es-la-cualidad-mas-importante-claim", "aku-laws-of-combat-concept"]}),
]

def links(jb, **extra):
    d = {"justified_by": jb, "constrained_by": [], "breaks_when": [], "illustrates": [], "challenges": []}
    d.update(extra); return d

takus = [
    {
        "id": "taku-cuando-desobedecer-al-jefe", "taku_type": "protocol",
        "title": "Cuándo y cómo desobedecer a un jefe (último recurso)",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "cadena-de-mando"],
        "when_to_use": "Cuando un jefe ordena algo ilegal/inmoral, o un plan que llevará a fracaso catastrófico, y has agotado las vías de influencia.",
        "when_not_to_use": "Por desacuerdos de eficiencia o de ego: ahí se ejecuta y se construye relación, no se desobedece.",
        "aku_links": links([DISOBEY, "aku-excepcion-resistir-ordenes-ilegales-inmorales-claim", "aku-ejecutar-decision-como-propia-claim"]),
        "taku_relations": {},
        "body": """## Purpose
Resolver el dilema de oponerse a un superior minimizando el daño al equipo, la misión y uno mismo.

## Trigger Conditions
Orden ilegal/inmoral/no ética, o plan con riesgo de fracaso catastrófico para el equipo y la misión.

## Required Resources
Relación y leadership capital con el jefe; análisis de riesgo documentado; tacto.

## Protocol Steps
1. ¿Es ilegal/inmoral/no ético? → rehúsa y repórtalo. (Caso claro.)
2. Si es un mal plan: pide al jefe que reformule el propósito; presenta tus preocupaciones de forma indirecta (onus en ti) y aporta una solución.
3. Da al jefe una salida airosa: ata la idea a algo que él dijo; no enfrentes tu idea contra la suya.
4. Si insiste: documenta con más detalle los desenlaces negativos y vuelve a presentarlo, sin emoción.
5. Si aun así insiste: sopesa los desenlaces de negarte (reconsidera / te sustituye por un yes-man / pierdes toda influencia).

## Decision Points
¿Qué hay en riesgo? Poca eficiencia → ejecuta. Riesgo catastrófico e inamovible → considera la línea en la arena.

## Exit Conditions
El plan se ajusta, o entiendes el porqué y lo ejecutas, o (último recurso) rehúsas asumiendo las consecuencias.

## Failure Handling
Si rehusar pondría un yes-man en tu lugar (peor para el equipo), quizá sea mejor hacer una última objeción y ejecutar mitigando el daño (recordando que, según Napoleón, sigues siendo culpable).

## Review Trigger
Proceder con extrema cautela: algunos cursos tienen desenlaces catastróficos para equipo, misión y subordinado.""",
    },
    {
        "id": "taku-influir-hacia-arriba", "taku_type": "technique",
        "title": "Influir hacia arriba: rendimiento, relación y onus en ti",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "influencia"],
        "when_to_use": "Para ganar influencia con un superior y poder redirigir sus decisiones cuando importa.",
        "when_not_to_use": "Como adulación o manipulación para beneficio propio: el fin es la misión, no el ascenso.",
        "aku_links": links([REDIR, PERF, REL, "aku-leadership-capital-concept"]),
        "taku_relations": {},
        "body": """## Summary
Ganar «clout» con el jefe mediante rendimiento y relación, para que escuche cuando de verdad importa.

## When to Use
Cuando necesitas que un superior te dé recursos, decisiones o margen, o redirigir un plan.

## Prerequisites
Disposición a ejecutar tareas (incluso ingratas) sin drama; humildad para poner el onus en ti.

## Steps
1. Rinde: completa las tareas a tiempo, en presupuesto y sin quejas; sé la solución.
2. No hables de más: cuanto menos objetes sin fundamento, más se escucha tu objeción fundada.
3. Cuando debas redirigir, hazlo con el onus en ti: «quiero apoyar el plan, ayúdame a entender por qué…».
4. Elige tus batallas: ¿cuánto se gana?, ¿es mi ego?, ¿muevo la relación adelante o atrás?

## Anti-patterns
Ser un sí-señor permanente (pareces pushover) o un quejica permanente (pierdes influencia con cada palabra).

## Expected Outcome
El jefe confía, te da lo que necesitas, se aparta y te deja cumplir la misión; y escucha tu «no» cuando llega.

## Failure Signals
El jefe ignora tus objeciones (poca clout) o te ve como fuente de excusas.

## Underlying Logic
La confianza se gana con hechos; el leadership capital acumulado se gasta sabiamente en las batallas que importan.

## Notes and Variants
Aplica también hacia abajo: escucha y di sí cuando puedas para que tu «no» se acepte.""",
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
