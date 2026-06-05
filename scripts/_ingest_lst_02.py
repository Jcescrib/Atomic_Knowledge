# -*- coding: utf-8 -*-
"""Ingesta — Leadership Strategy and Tactics, Sección 2 'Core Tenets' + 2 TAKUs."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/leadership-strategy-and-tactics/leadership-strategy-and-tactics.md"
ORIGIN = "Jocko Willink, Leadership Strategy and Tactics: Field Manual (2020)"
GIVE = "aku-dar-confianza-incrementalmente-method"
IMPORTANT = "aku-saber-que-es-importante-y-que-no-method"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku("aku-lider-conoce-trabajos-y-pide-ayuda-claim", "claim",
        "El líder debe estar familiarizado con los trabajos, habilidades y equipos de quienes están bajo su mando (sin ser experto en todo); cuando no sabe algo, debe pedir ayuda y aprender haciéndolo de verdad, en vez de fingir que lo sabe todo (eso es ego); los subordinados respetan más al líder que baja a la primera línea a aprender y hacer su trabajo —demuestra humildad— y hay que volver a por más con regularidad.",
        DOM + ["humildad", "competencia"],
        {"related": ["aku-check-the-ego-concept", "aku-humildad-es-la-cualidad-mas-importante-claim", "aku-power-of-relationships-liderazgo-concept"]}),
    aku(GIVE, "method",
        "Para construir confianza hacia abajo hay que DAR confianza de forma incremental: empieza dejando que el subordinado lleve una misión pequeña y de bajo riesgo, tome una decisión menor o resuelva un problema fácilmente recuperable; si tiene éxito, sube el listón gradualmente; si falla, mentorízalo en vez de castigarlo; a medida que crece la confianza, pasas de micromanagement a hands-off.",
        DOM + ["confianza", "delegacion"],
        {"related": ["aku-confianza-se-construye-no-se-da-claim", "aku-decentralized-command-concept", "aku-corregir-micromanagement-method"]}),
    aku("aku-confianza-arriba-no-decir-lo-que-quieren-oir-claim", "claim",
        "Para construir confianza hacia arriba, no le digas al jefe lo que cree que quiere oír (falsas tranquilidades como «la moral es genial» o «llegaremos a las cifras» se vuelven en tu contra y dañan tu credibilidad); di la verdad, pero distingue entre lo que el jefe necesita saber y quejarse de cada pequeñez.",
        DOM + ["confianza", "honestidad"],
        {"related": ["aku-lideres-dicen-la-verdad-claim", "aku-feedback-hacia-arriba-cadena-claim"]}),
    aku("aku-decentralized-descansa-en-confianza-tiempo-critico-claim", "claim",
        "En situaciones críticas y sensibles al tiempo no hay margen para explicar el porqué: el subordinado debe confiar y ejecutar de inmediato; y a la inversa, el líder debe confiar cuando el subordinado responde «¡Negativo!» (ve algo que el líder no ve), y entonces darle el porqué para que adapte la ejecución; la confianza opera en ambos sentidos y es lo que sostiene al equipo cuando no hay tiempo de diálogo.",
        DOM + ["confianza", "mando"],
        {"related": ["aku-decentralized-command-concept", "aku-decentralized-requiere-confianza-bidireccional-claim", "aku-believe-in-the-mission-concept"]}),
    aku("aku-ganar-respeto-e-influencia-dandolos-claim", "claim",
        "El rango da un respeto y una influencia limitados; para ganar más hay que DARLOS: trata a la gente con respeto (deja que opinen, escucha sin interrumpir, no menosprecies su trabajo, comparte las cargas duras) y permite que te influyan (escucha de verdad, considera e incorpora sus ideas, mente abierta); cuanto más respetas e influyes-recibes, más respeto e influencia tendrás.",
        DOM + ["respeto", "influencia"],
        {"related": ["aku-leading-up-requiere-influencia-no-autoridad-claim", "aku-power-of-relationships-liderazgo-concept"]}),
    aku("aku-preemptive-ownership-concept", "concept",
        "La «preemptive ownership» (ownership preventiva) es la forma más alta de Extreme Ownership: como el líder sabe que no podrá culpar a nadie ni a nada, asume la responsabilidad ANTES de que surjan los problemas —entrena al artillero, prepara planes de contingencia para el mal tiempo—; el ownership no es solo asumir la culpa después, sino prevenir los errores antes de que ocurran.",
        DOM + ["responsabilidad"],
        {"related": ["aku-extreme-ownership-concept", "aku-contingency-planning-anticipar-method", "aku-lider-mirar-al-espejo-claim"]}),
    aku("aku-tomar-ownership-cuando-te-culpan-claim", "claim",
        "Cuando te culpan de algo (seas líder, o subordinado por el error de otro), acéptalo: «Sí, es culpa mía, soy responsable, y esto es lo que voy a hacer para arreglarlo», y pasa de inmediato a resolver el problema; el ego y la defensividad empujan a negar o desviar la culpa, pero asumir el error ajeno demuestra liderazgo, y todo líder quiere en su equipo a quien asume, no a quien esquiva.",
        DOM + ["responsabilidad", "ego"],
        {"related": ["aku-extreme-ownership-concept", "aku-atribucion-sesgada-exito-fracaso-claim"]}),
    aku("aku-ningun-trabajo-es-demasiado-bajo-claim", "claim",
        "El líder está por encima en rango pero no es superior a sus subordinados, así que ningún trabajo es demasiado bajo o menial para él («picking up brass»); hacer de vez en cuando las tareas duras, incómodas o de riesgo junto a la tropa demuestra humildad, construye relaciones, revela quién holgazanea y mantiene el respeto por el trabajo y por quienes lo hacen a diario.",
        DOM + ["humildad", "ejemplo"],
        {"related": ["aku-liderar-desde-posicion-mas-dificil-claim", "aku-draw-fire-concept"]}),
    aku("aku-liderar-desde-frente-y-desde-atras-concept", "concept",
        "«Lead from the front» importa (dar ejemplo y actuar cuando los demás se paralizan por miedo o ante tareas arduas), pero el líder también debe liderar desde atrás o desde el medio: ir al frente aumenta su riesgo y lo absorbe en el problema táctico inmediato, haciéndole perder el cuadro general; debe posicionarse para «detach», evaluar y dar apoyo («up and out, not down and in»), y en la planificación liderar desde atrás dejando que el equipo cree y posea el plan.",
        DOM + ["posicionamiento", "dicotomia"],
        {"related": ["aku-detach-tactico-estrategico-concept", "aku-pull-off-the-firing-line-claim", "aku-posicionamiento-del-lider-flexible-claim", "aku-decentralizar-proceso-planificacion-claim"]}),
    aku("aku-no-sobrerreaccionar-mantener-la-calma-claim", "claim",
        "Cuando algo va mal, el buen líder se mantiene sereno: controla las emociones, evalúa con mesura y se reserva sus opiniones, porque lo que diga en caliente se basa en información incompleta e inexacta; deja que la situación se aclare antes de hablar; sobrerreaccionar lleva a malas decisiones y proyecta que el líder no tiene el control.",
        DOM + ["autocontrol", "decision"],
        {"related": ["aku-calmado-no-robotico-concept", "aku-relax-look-around-make-a-call-method"]}),
    aku("aku-no-care-detachment-via-ego-method", "method",
        "«No me importa» (I don't care) es una forma poderosa —y difícil— de detachment: la capacidad de marcharse (en una negociación) o de no aferrarse a quién lidera, a hacer la tarea ingrata o a que se use tu plan; requiere subordinar el ego, porque casi todo lo que nos «importa» está enraizado en él; para ganar el juego largo y estratégico hay que sobreponerse al ego y aprender a no preocuparse, y paradójicamente así el ego acaba satisfecho.",
        DOM + ["detach", "ego"],
        {"related": ["aku-subordinate-your-ego-desactiva-choque-method", "aku-detach-tactico-estrategico-concept", "aku-play-the-long-game-concept"]}),
    aku("aku-everyone-same-everyone-different-concept", "concept",
        "Dicotomía «todos son iguales, todos son distintos»: hay arquetipos que se repiten en toda organización (el líder natural, el solitario, el cerebral, el agresivo…) y a la vez cada persona es única (motivaciones, manías, ideas propias); el líder es como un ebanista que debe usar herramientas distintas Y aplicarlas de forma distinta a cada pieza de madera única; aplicar la misma herramienta «más fuerte» cuando no funciona arruina al equipo o al individuo (como agrietar la madera); el arte del liderazgo es el tacto y la prudencia al elegir y aplicar la herramienta.",
        DOM + ["dicotomia", "personas"],
        {"related": ["aku-dichotomy-of-leadership-concept", "aku-when-to-mentor-when-to-fire-concept"]}),
    aku("aku-encajar-atributos-con-el-rol-claim", "claim",
        "Encaja los atributos de cada persona con su rol —no fuerces a un introvertido tímido a vender ni a un perfeccionista meticuloso a un caos—: no luches contra la naturaleza, úsala; pero, de forma medida y controlada, sácalos también de su zona de confort para que crezcan en sus debilidades; las funciones principales deben reflejar sus fortalezas naturales.",
        DOM + ["talento", "roles"],
        {"related": ["aku-lider-responsable-del-output-maximizar-potencial-claim", "aku-lider-compensa-debilidades-con-el-equipo-claim"]}),
    aku("aku-isolation-burden-of-command-claim", "claim",
        "El líder debe estar cómodo en soledad (trabaja más, llega antes y se va después, y decide solo: la carga del mando), pero el liderazgo no tiene por qué ser solitario: cultiva con cautela y profesionalidad unos pocos «trusted agents» arriba y abajo para tomar el pulso del equipo, contrastar ideas y desahogarte; aun así, la decisión final recae siempre en el líder y solo en él.",
        DOM + ["soledad", "responsabilidad"],
        {"related": ["aku-burden-of-command-concept", "aku-confianza-se-construye-no-se-da-claim"]}),
    aku(IMPORTANT, "method",
        "Como un cinturón negro de jiu-jitsu, el líder debe discriminar lo importante de lo trivial (ignorar el «reconocimiento por fuego» y las fintas): para ello, detach y elévate sobre la situación y, antes de meterte en un problema, pregúntate: ¿cómo impacta esto en los objetivos estratégicos?, ¿puede causar el fracaso de la misión?, ¿merece mi tiempo?, ¿cómo de mal puede ir si lo dejo estar?; por norma, inclínate por NO involucrarte (que los problemas se resuelvan al nivel más bajo), salvo que el problema realmente requiera al líder.",
        DOM + ["priorizacion", "detach"],
        {"related": ["aku-detach-tactico-estrategico-concept", "aku-prioritize-and-execute-concept", "aku-target-fixation-concept"]}),
]

def links(jb, **extra):
    d = {"justified_by": jb, "constrained_by": [], "breaks_when": [], "illustrates": [], "challenges": []}
    d.update(extra); return d

takus = [
    {
        "id": "taku-construir-confianza-incrementalmente", "taku_type": "technique",
        "title": "Construir confianza dando confianza (incremental)",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "confianza", "delegacion"],
        "when_to_use": "Para desarrollar a los subordinados y habilitar el mando descentralizado construyendo confianza mutua.",
        "when_not_to_use": "Cuando un fallo tendría consecuencias catastróficas inmediatas y no recuperables: ahí aún no toca soltar.",
        "aku_links": links([GIVE, "aku-confianza-se-construye-no-se-da-claim", "aku-decentralized-command-concept"]),
        "taku_relations": {},
        "body": """## Summary
Construir confianza con un subordinado dándole responsabilidad creciente en pasos pequeños y recuperables.

## When to Use
Al desarrollar a alguien hacia mayor autonomía y mando descentralizado.

## Prerequisites
Tareas/decisiones/problemas de bajo riesgo disponibles; disposición a mentorizar el fallo en vez de castigarlo.

## Steps
1. Asigna una misión pequeña, una decisión menor o un problema fácilmente recuperable.
2. Si tiene éxito: sube el listón gradualmente (misión/decisión/problema mayores).
3. Si falla: trátalo como oportunidad de aprendizaje; mentoriza y vuelve a intentarlo con algo más de supervisión.
4. A medida que aumenta el riesgo, deja que lidere pero con más oversight para evitar el fallo catastrófico.
5. Conforme se gana la confianza, reduce la supervisión: de micromanagement a hands-off.

## Anti-patterns
Empezar por una misión crítica de alto riesgo; castigar el fallo (mata la iniciativa); no soltar nunca.

## Expected Outcome
Confianza mutua creciente; el subordinado gana autonomía y el líder gana un líder en quien delegar.

## Failure Signals
El subordinado espera instrucciones, no toma iniciativa, o comete fallos repetidos sin aprender.

## Underlying Logic
Para que confíen en ti, debes darles confianza; la confianza se construye con el tiempo y con hechos.

## Notes and Variants
Combínalo con la corrección de micromanagement/hands-off según hacia dónde se desequilibre.""",
    },
    {
        "id": "taku-discriminar-lo-importante", "taku_type": "heuristic",
        "title": "Discriminar lo importante de lo trivial (las 4 preguntas)",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "priorizacion"],
        "when_to_use": "Antes de involucrarte en un problema o cambio, para decidir si merece tu tiempo y energía como líder.",
        "when_not_to_use": "No la uses para desentenderte de problemas que sí requieren al líder: hay que reconocer cuándo bajar al detalle.",
        "aku_links": links([IMPORTANT, "aku-detach-tactico-estrategico-concept"]),
        "taku_relations": {},
        "body": """## The Rule
Antes de meterte en un problema, detach y hazte cuatro preguntas; por defecto, inclínate por NO involucrarte y deja que se resuelva al nivel más bajo.

## What It Replaces
La reacción de involucrarse en todo problema que aparece, convirtiendo molehills en montañas.

## When It Holds
Cuando el problema puede resolverse a un nivel inferior sin impacto estratégico.

## When It Fails
Cuando elevas demasiado y un problema que sí te necesitaba crece sin control: hay que saber cuándo bajar al detalle.

## Why It Works
Conserva la energía del líder (como un cinturón negro no malgasta movimiento) para lo que de verdad mueve la aguja estratégica.

## Calibration
Las 4 preguntas: ¿cómo impacta en los objetivos estratégicos?, ¿puede causar el fracaso de la misión?, ¿merece mi tiempo?, ¿cómo de mal puede ir si lo dejo estar? Equilibra: ni distraerte con lo trivial ni ignorar lo importante.""",
    },
]

written, cross = akugen.generate(akus, takus, ROOT)
print(f"escritos: {len(written)} ficheros")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
akupatch.apply(ROOT, patch_ops)
print(f"cross sobre {len(patch_ops)} AKUs existentes")
