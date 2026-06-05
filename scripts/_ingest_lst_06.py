# -*- coding: utf-8 -*-
"""Ingesta — Leadership Strategy and Tactics, Part 2 Sec 3 'Maneuvers' + 3 TAKUs."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/leadership-strategy-and-tactics/leadership-strategy-and-tactics.md"
ORIGIN = "Jocko Willink, Leadership Strategy and Tactics: Field Manual (2020)"
TEACH = "aku-liderazgo-como-herramienta-para-ensenar-concept"
HUM = "aku-ensenar-humildad-con-mision-dificil-method"
CONF = "aku-construir-confianza-con-mision-asequible-method"
BOSSES = "aku-manejar-jefe-micromanager-indeciso-debil-method"
QUIT = "aku-cuando-rendirse-tactico-no-estrategico-claim"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(TEACH, "concept",
        "El propio liderazgo es una de las herramientas más potentes para enseñar y desarrollar a las personas: poner a alguien en una posición de mando le cambia la perspectiva y le revela sus propios errores; es un «remedio» versátil para arreglar actitudes, enseñar humildad, construir confianza y formar jugadores de alto nivel.",
        DOM + ["desarrollo", "mentoria"],
        {"related": ["aku-dar-confianza-incrementalmente-method", "aku-when-to-mentor-when-to-fire-concept"]}),
    aku("aku-arreglar-mala-actitud-con-responsabilidad-que-importa-claim", "claim",
        "Para arreglar la mala actitud de alguien con talento (a menudo aburrido o no desafiado), ponle al cargo de algo que IMPORTE y le rete —no de una tarea menial de castigo, que empeora la actitud—: el peso de una responsabilidad significativa suele reencauzarle.",
        DOM + ["actitud", "desarrollo"],
        {"supports": [TEACH], "related": ["aku-lider-responsable-del-output-maximizar-potencial-claim"]}),
    aku(HUM, "method",
        "Para enseñar humildad a un líder arrogante, ponle al cargo de una misión difícil (no imposible) que probablemente fallará: o reconoce que le supera y pide ayuda (humillado), o fracasa y se humilla; si lo logra, dale misiones progresivamente más duras hasta que falle o pida ayuda; solo en entrenamiento/bajo riesgo, nunca en una misión real de alto riesgo.",
        DOM + ["humildad", "mentoria"],
        {"supports": [TEACH], "related": ["aku-check-the-ego-concept", "aku-humildad-es-la-cualidad-mas-importante-claim"]}),
    aku(CONF, "method",
        "Para construir o reconstruir la confianza de un subordinado, ponle al cargo de una misión que sabes que puede ejecutar bien (incluso fácil); con cada éxito, dale una un poco más dura, y así su confianza crece hasta poder afrontar retos serios; mitiga el riesgo (no mandes al inseguro a una misión crítica), pero que no sea tan fácil que la sienta un «softball» y refuerce su inseguridad.",
        DOM + ["confianza", "mentoria"],
        {"supports": [TEACH], "related": ["aku-dar-confianza-incrementalmente-method", "aku-imposter-syndrome-es-bueno-claim"]}),
    aku("aku-desarrollar-poniendo-junior-al-mando-claim", "claim",
        "Se desarrolla a jugadores de alto nivel poniendo a los junior al mando de operaciones de entrenamiento: comprenden cómo su trabajo encaja en la misión estratégica y se vuelven mejores en su puesto y como futuros líderes (caso Freddie: «bajo riesgo, estos saben liderar»).",
        DOM + ["desarrollo", "descentralizacion"],
        {"supports": [TEACH], "related": ["aku-liderazgo-en-todos-los-niveles-claim", "aku-decentralizar-proceso-planificacion-claim"]}),
    aku("aku-liderar-pares-via-influencia-y-ego-en-jaque-claim", "claim",
        "Liderar a los pares es de lo más difícil (a igual rango los egos se hacen más visibles): exige más tacto y una relación aún mejor para influir; subordina primero TU ego (si no, sacas el peor ego de tus pares → «blue-on-blue»/fuego amigo), apoya sus ideas, asume las tareas duras sin pasarte, posee los problemas y no busques crédito; el juego «¿a quién ascenderías?» recuerda que se asciende a quien asume, no a quien culpa —juega el largo plazo, los egoístas acaban descubiertos—.",
        DOM + ["pares", "ego", "influencia"],
        {"related": ["aku-play-the-long-game-concept", "aku-subordinate-your-ego-desactiva-choque-method", "aku-liderazgo-vs-manipulacion-concept"]}),
    aku(BOSSES, "method",
        "Manejar jefes difíciles: con el MICROMANAGER (falta de confianza) → inúndalo de información y rinde impecablemente a su manera hasta que te dé margen; con el INDECISO (no prioriza, «todo es prioridad») → preséntale una lista priorizada con tacto o fija tú las prioridades, enmarcando la decisión para que solo tenga que decir «sí»; con el DÉBIL → es una oportunidad: haz tú el plan, clarifica, asume y lidera, pero con lenguaje suave que no hiera su ego.",
        DOM + ["jefes", "influencia"],
        {"related": ["aku-rendimiento-construye-confianza-del-jefe-claim", "aku-prioritize-and-execute-concept", "aku-leadership-capital-concept"]}),
    aku("aku-cuando-micromanage-es-necesario-method", "method",
        "El micromanagement es una herramienta necesaria cuando un individuo o equipo no hace su trabajo: primero asegúrate de que entiende misión/rol (en positivo), escala a dirección directa («esto es exactamente lo que tienes que hacer»), luego micromanagea (muéstralo, hazlo, monitoriza de cerca, e incluso explícale que es temporal); afloja según mejoran y aprieta si recaen; no es solución permanente —si no mejoran, da expectativas y consecuencias claras y, en su defecto, termina o reemplaza—.",
        DOM + ["micromanagement", "correccion"],
        {"related": ["aku-corregir-micromanagement-method", "aku-dar-confianza-incrementalmente-method", "aku-ni-muy-rapido-ni-muy-lento-para-despedir-claim"]}),
    aku("aku-jefe-quiere-el-credito-daselo-claim", "claim",
        "Si el jefe quiere todo el crédito, dáselo: es tu ego el que se resiste, y pedir crédito es un pésimo movimiento; un jefe inseguro que quiere crédito se vuelve antagonista si se lo quitas; déjaselo —cuando lo asciendan, elegirá para reemplazarlo a quien lo apoyó (probablemente tú)—; y el crédito no pedido que llega después vale el doble (pareces competente Y humilde).",
        DOM + ["credito", "ego"],
        {"related": ["aku-owner-no-toma-credito-da-honor-claim", "aku-play-the-long-game-concept", "aku-mejores-lideres-mision-no-ego-claim"]}),
    aku("aku-defender-al-jefe-casi-indefendible-claim", "claim",
        "Apoya siempre a tu jefe (socavarlo te daña a ti, a la moral y a la tropa, y das mal ejemplo); presenta como propios incluso los planes con los que discrepas (tras debatirlos en privado); ante un jefe «casi indefendible» (egotista, malas decisiones) ni lo defiendas a ciegas (pierdes credibilidad) ni lo denigres abiertamente (destruye la disciplina): usa frases equilibradas («no es perfecto, pero nos lleva hacia los mismos objetivos»); solo ante lo ilegal/inmoral o riesgo real, considera ir por encima o el motín.",
        DOM + ["cadena-de-mando", "equilibrio"],
        {"related": ["aku-presentar-frente-unido-claim", "aku-ejecutar-decision-como-propia-claim", "aku-excepcion-resistir-ordenes-ilegales-inmorales-claim"]}),
    aku("aku-aliviar-stress-sacar-del-entorno-method", "method",
        "Para gestionar el estrés de un subordinado: construye relación (así te lo dirá, o notarás cambios de conducta —Dick Winters: cabeza hundida entre las manos = al borde del colapso—); el mejor tratamiento es SACARLO del entorno estresante: asígnale una «misión» en retaguardia sin decirle que es descanso (evita la vergüenza); como la luz de «Check Engine», hay que dar servicio al motor o reventará catastróficamente.",
        DOM + ["estres", "cuidado"],
        {"related": ["aku-gestionar-stress-detach-y-perspectiva-method", "aku-taking-care-of-people-con-disciplina-claim", "aku-burden-of-command-concept"]}),
    aku("aku-castigo-raro-y-con-lineas-claras-claim", "claim",
        "El castigo debe ser raro: si la tropa no ejecuta, mírate primero al espejo (probablemente no diste la dirección adecuada); castiga solo por reglas claras y documentadas («cuando se cruzan líneas» que están definidas), expón de antemano las consecuencias (que nadie se sorprenda), pondera el historial de la persona (la clemencia no es debilidad sino sensatez) y reparte el castigo con justicia.",
        DOM + ["disciplina", "consecuencias"],
        {"related": ["aku-lider-mirar-al-espejo-claim", "aku-extreme-ownership-concept", "aku-no-es-lo-que-predicas-sino-lo-que-toleras-claim"]}),
    aku(QUIT, "claim",
        "Hay un momento para rendirse: el «never quit» del entrenamiento SEAL hay que modularlo; está bien abandonar un PLAN o un objetivo TÁCTICO que no funciona (el «barricaded shooter» del pasillo → retírate y flanquea por la ventana), y a veces rendirse tácticamente es necesario PARA la misión estratégica (la retirada de Washington de Nueva York, Galípoli, Dunkerque: vivir para luchar otro día); pero nunca abandones la misión ESTRATÉGICA ni tus objetivos a largo plazo.",
        DOM + ["decision", "estrategia"],
        {"related": ["aku-dont-dig-in-no-sobrecomprometerse-claim", "aku-mantener-objetivo-largo-plazo-a-la-vista-claim", "aku-prioritize-and-execute-concept"]}),
]

def links(jb, **extra):
    d = {"justified_by": jb, "constrained_by": [], "breaks_when": [], "illustrates": [], "challenges": []}
    d.update(extra); return d

takus = [
    {
        "id": "taku-usar-liderazgo-para-desarrollar", "taku_type": "framework",
        "title": "Usar el liderazgo como herramienta para desarrollar personas",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "desarrollo", "mentoria"],
        "when_to_use": "Para corregir actitudes, enseñar humildad, construir confianza o formar futuros líderes en tu equipo.",
        "when_not_to_use": "En misiones reales de alto riesgo donde un fallo del que aprende tendría consecuencias graves.",
        "aku_links": links([TEACH, HUM, CONF]), "taku_relations": {},
        "body": """## Summary
Poner a las personas en posiciones de liderazgo (calibrando la dificultad) como remedio versátil para desarrollarlas.

## Core Components
1. **Arreglar actitud**: dar responsabilidad que importe y rete (no tareas meniales de castigo).
2. **Enseñar humildad**: misión difícil (no imposible) que probablemente falle → pide ayuda o se humilla.
3. **Construir confianza**: misión asequible, escalando en dificultad con cada éxito.
4. **Formar jugadores de alto nivel**: poner a junior al mando de operaciones de entrenamiento.

## How to Apply
Diagnostica qué necesita la persona (actitud/humildad/confianza/desarrollo) y elige el tipo y dificultad de la responsabilidad acorde; mitiga siempre el riesgo (entrenamiento/bajo riesgo).

## Underlying Claims
El mando cambia la perspectiva y revela los propios errores; la responsabilidad significativa reencauza.

## Strengths
Una sola herramienta (dar liderazgo) cubre múltiples problemas de desarrollo; genera ownership.

## Limitations and Criticisms
No usar en alto riesgo real; calibrar mal la dificultad puede humillar a quien hay que animar (o animar a quien hay que humillar).

## Variants and Extensions
Se combina con dar-confianza-incrementalmente y con la corrección micromanagement/hands-off.""",
    },
    {
        "id": "taku-manejar-jefes-dificiles", "taku_type": "protocol",
        "title": "Manejar jefes difíciles (micromanager / indeciso / débil)",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "jefes", "influencia"],
        "when_to_use": "Cuando tu jefe es micromanager, indeciso sobre prioridades, o débil/poco involucrado.",
        "when_not_to_use": "Ante un jefe que ordena lo ilegal/inmoral o pone en riesgo real al equipo: ahí, ver el protocolo de desobediencia.",
        "aku_links": links([BOSSES, "aku-rendimiento-construye-confianza-del-jefe-claim", "aku-leadership-capital-concept"]),
        "taku_relations": {},
        "body": """## Purpose
Convertir las carencias del jefe en oportunidades, ganando margen y moviendo al equipo hacia la misión.

## Trigger Conditions
Jefe micromanager, indeciso o débil que dificulta la ejecución.

## Required Resources
Paciencia, ego en jaque, lenguaje tactful, capacidad de rendir de forma sostenida.

## Protocol Steps
1. **Micromanager**: inúndalo de información detallada y rinde impecablemente a su manera; sostenido en el tiempo, te dará margen.
2. **Indeciso**: preséntale una lista priorizada con tacto («¿te parece bien cómo lo he priorizado?»); si insiste en que «todo es prioridad», fija tú las prioridades y avanza.
3. **Indeciso (decisión)**: enmárcala para que solo diga «sí» («creo que deberíamos ir por aquí para cumplir tu objetivo; ¿tiene sentido?»).
4. **Débil**: asume el vacío —haz el plan, clarifica, posee y lidera— con lenguaje suave que no hiera su ego.

## Decision Points
¿Qué carencia tiene? ¿Mi enfoque le hiere el ego? Ajusta el tacto.

## Exit Conditions
El jefe te da margen, tienes prioridades claras y el equipo avanza hacia la misión.

## Failure Handling
Si nada funciona y el jefe es inepto y dañino, escala o (rarísimo) considera el motín.

## Review Trigger
Reevalúa la relación y el margen ganado tras varios ciclos de rendimiento.""",
    },
    {
        "id": "taku-cuando-rendirse-tactico", "taku_type": "heuristic",
        "title": "Cuándo rendirse: el plan táctico, no la misión estratégica",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "decision", "estrategia"],
        "when_to_use": "Cuando un plan o un objetivo táctico no funciona y persistir dañaría la misión estratégica.",
        "when_not_to_use": "Nunca para abandonar la misión estratégica ni los objetivos a largo plazo.",
        "aku_links": links([QUIT, "aku-dont-dig-in-no-sobrecomprometerse-claim"]), "taku_relations": {},
        "body": """## The Rule
Está bien rendirse (retirarse) de un plan u objetivo TÁCTICO que no funciona; nunca abandones la misión ESTRATÉGICA.

## What It Replaces
El «never quit» mal aplicado, que lleva a estrellarse repetidamente contra un plan fallido (el pasillo del barricaded shooter).

## When It Holds
Cuando persistir en lo táctico cuesta recursos sin avanzar y pone en peligro el objetivo estratégico.

## When It Fails
Si lo usas para abandonar el objetivo estratégico o a la primera dificultad: eso es rendirse de verdad.

## Why It Works
Retirarse de un plan para flanquear o regroup preserva la fuerza para ganar después (Washington en NY, Galípoli, Dunkerque).

## Calibration
Pregúntate: ¿es esto táctico o estratégico? Detach, mira alrededor, busca otra vía (p. ej. flanquear por la ventana). «Quit» aquí significa retreat/reagrupar, no surrender.""",
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
