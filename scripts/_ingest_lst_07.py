# -*- coding: utf-8 -*-
"""Ingesta — Leadership Strategy and Tactics, Part 2 Sec 4 'Communication' (cierra libro 4) + 2 TAKUs."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/leadership-strategy-and-tactics/leadership-strategy-and-tactics.md"
ORIGIN = "Jocko Willink, Leadership Strategy and Tactics: Field Manual (2020)"
ULT = "aku-ultimatums-ultimo-recurso-method"
RD = "aku-reflect-and-diminish-method"
INFORM = "aku-keep-troops-informed-asumir-que-no-saben-claim"
PRAISE = "aku-balancing-praise-elogio-con-cautela-claim"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "comunicacion"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(INFORM, "claim",
        "Mantén a todo el equipo lo más informado posible (lección de las posiciones en la patrulla: cuanto más atrás vas, menos sabes → más miseria y mayor riesgo táctico); no asumas que el equipo ve lo que tú ves —asume que no sabe NADA— y sé proactivo manteniéndolos al día, porque no puedes contar con que pregunten (no saben lo que no saben).",
        DOM + ["informacion"],
        {"related": ["aku-conexion-rol-big-picture-no-intuitiva-claim", "aku-leading-down-the-chain-concept", "aku-senior-debe-explicar-el-porque-claim"]}),
    aku("aku-rumor-control-llenar-vacio-de-informacion-claim", "claim",
        "Los rumores crecen en el vacío de información: si no cuentas lo que pasa, la gente inventa versiones peores («¡nos vamos a la quiebra!»); adelántate a las malas noticias y ataca los rumores diciendo la verdad de forma directa y a tiempo —cuanto más esperas, más grandes se hacen y más difícil es controlarlos—.",
        DOM + ["rumores"],
        {"related": [INFORM, "aku-lideres-dicen-la-verdad-claim", "aku-culpar-se-contagia-claim"]}),
    aku("aku-thread-of-why-conectar-al-individuo-claim", "claim",
        "Explicar el porqué no basta: el porqué debe tener un «hilo» que conecte de vuelta con cada persona de la cadena (el «beneficio para los accionistas» no motiva a la primera línea; hay que atarlo a su seguridad laboral, crecimiento y oportunidades); enmarca el porqué desde la perspectiva de la tropa, mostrando cómo la misión les impacta a ELLOS.",
        DOM + ["proposito", "motivacion"],
        {"related": ["aku-senior-debe-explicar-el-porque-claim", "aku-believe-in-the-mission-concept", "aku-conexion-rol-big-picture-no-intuitiva-claim"]}),
    aku(PRAISE, "claim",
        "El elogio es una herramienta que se maneja con cautela: demasiado → complacencia (el desastre por exceso de confianza en el kill house tras un gran cumplido); demasiado poco → pérdida de esperanza; dalo con criterio, atemperado con una meta que aún exija empujar, sin ser el líder nunca satisfecho (mover la portería desmoraliza); y dirígelo a individuos concretos, no al equipo en bloque, para que se gane.",
        DOM + ["elogio", "motivacion"],
        {"related": ["aku-disease-of-victory-concept", "aku-nunca-complacencia-subestimar-enemigo-claim", "aku-lideres-nunca-satisfechos-mejora-continua-claim"]}),
    aku("aku-hope-no-es-curso-de-accion-pero-debe-existir-claim", "claim",
        "«La esperanza no es un curso de acción»: no puedes basar la planificación ni la ejecución en la esperanza (planifica, contempla contingencias, carga los dados a tu favor); pero la esperanza SÍ debe existir en el corazón de quienes ejecutan —sin ella, la voluntad no aguanta y llega la rendición—, así que el líder es responsable de sostenerla (explicar que la victoria es posible, fijar victorias a corto plazo; e incluso ante la derrota inevitable, mantener la línea construye reputación, y eso es esperanza para seguir luchando).",
        DOM + ["esperanza", "moral"],
        {"related": ["aku-believe-in-the-mission-concept", "aku-metas-intermedias-visibles-method", "aku-mantener-objetivo-largo-plazo-a-la-vista-claim"]}),
    aku(ULT, "method",
        "Los ultimátums no son herramientas óptimas (no dejan margen, la gente se siente atrapada) y solo se usan en casos rarísimos cuando «basta es basta», manteniendo siempre la línea (nunca des un ultimátum que no puedas cumplir): como jefe, pregúntate primero «¿dónde falló mi liderazgo?», hazlo explícito (requisito + consecuencia) y, en un equipo, ponlo sobre el líder; como subordinado, un ultimátum hacia arriba es un movimiento de alto riesgo que revela los límites de tu lealtad (mejor discusión o aviso); y si te lo ponen a ti, di la verdad (a ti, a tu equipo y a tu jefe) y mantén la dignidad si el jefe se mantiene firme.",
        DOM + ["negociacion", "ultimo-recurso"],
        {"related": ["aku-dont-dig-in-no-sobrecomprometerse-claim", "aku-excepcion-resistir-ordenes-ilegales-inmorales-claim"]}),
    aku(RD, "method",
        "Para desescalar a un subordinado emocional, no le digas «cálmate» (lo enfada más): usa «Reflect and Diminish» (reflejar y atenuar) —refleja su emoción pero a una intensidad algo menor para volverte su aliado y desescalar («¡No me lo puedo creer! ¿Cuánto se han retrasado?»)—; funciona con ira, tristeza, envidia e incluso humor, y sirve tanto hacia abajo como hacia arriba en la cadena.",
        DOM + ["emociones", "desescalada"],
        {"related": ["aku-no-sobrerreaccionar-mantener-la-calma-claim", "aku-calmado-no-robotico-concept"]}),
    aku("aku-cuando-gritar-casi-nunca-y-calculado-claim", "claim",
        "Gritar con emoción es liderazgo débil (el equipo imita: si te enfadas, se enfadan; si entras en pánico, entran en pánico); grita solo por volumen (ruido) o de forma rarísima y calculada, en privado, tras varias escaladas serenas fallidas —entonces «deja marca»—; si no te entienden, es culpa TUYA por no articular con claridad, no motivo para gritar.",
        DOM + ["autocontrol", "voz"],
        {"related": ["aku-calmado-no-robotico-concept", "aku-briefear-al-minimo-comun-denominador-claim", "aku-agresivo-significa-proactivo-no-iracundo-claim"]}),
    aku("aku-getting-people-to-listen-deja-que-hablen-claim", "claim",
        "Para que la gente te escuche y aumentar tu influencia, deja que hablen primero: es la mejor cura para el que habla mucho (que saque sus ideas) y así conoces todo lo que ellos saben para formular el punto más fuerte; «cuanto menos hablas, más te escuchan»: habla cuando haga falta, con contundencia, sin malgastar palabras.",
        DOM + ["escucha", "influencia"],
        {"related": ["aku-no-yes-men-fomentar-pushback-claim", "aku-rendimiento-construye-confianza-del-jefe-claim"]}),
    aku("aku-apologizing-no-es-debilidad-claim", "claim",
        "Disculparse no es debilidad (quien lo cree suele ser inseguro): es parte de asumir el ownership; pide perdón cuando hayas impactado negativamente a alguien o cometido un error real (con explicación), pero no por cada pequeñez; si crees que no debes una disculpa porque «no fue tu culpa», revisa tu ego —probablemente sí podrías haber hecho algo distinto— y desarma a quien busca culpables asumiéndolo tú.",
        DOM + ["responsabilidad", "humildad"],
        {"related": ["aku-extreme-ownership-concept", "aku-humildad-asumir-errores-claim", "aku-tomar-ownership-cuando-te-culpan-claim"]}),
    aku("aku-be-approachable-pero-cuidado-con-las-palabras-claim", "claim",
        "Cierra la brecha con la tropa (pasa tiempo con ellos, no presumas de dinero ni de rango, habla de vida/familia/futuro) para que compartan problemas; pero hay una línea: no te vuelvas demasiado familiar —el cotilleo, el sarcasmo y los comentarios a la ligera de un líder pesan demasiado—; las palabras del líder tienen un impacto inmenso (lo positivo enciende, lo negativo aplasta), así que sé juicioso con qué dices, a quién y cómo.",
        DOM + ["relaciones", "palabras"],
        {"related": ["aku-isolation-burden-of-command-claim", PRAISE]}),
]

def links(jb, **extra):
    d = {"justified_by": jb, "constrained_by": [], "breaks_when": [], "illustrates": [], "challenges": []}
    d.update(extra); return d

takus = [
    {
        "id": "taku-reflect-and-diminish", "taku_type": "technique",
        "title": "Reflect and Diminish (reflejar y atenuar para desescalar)",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "emociones", "desescalada"],
        "when_to_use": "Cuando un subordinado (o tu jefe) llega cargado de emoción (ira, tristeza, envidia) y necesitas desescalar y resolver.",
        "when_not_to_use": "No para manipular ni para validar emociones destructivas: el fin es desescalar y pasar a la solución.",
        "aku_links": links([RD, "aku-no-sobrerreaccionar-mantener-la-calma-claim"]), "taku_relations": {},
        "body": """## Summary
Reflejar la emoción del otro a una intensidad algo menor para convertirte en aliado y desescalar.

## When to Use
Ante una persona emocionalmente alterada, en cualquier dirección de la cadena de mando.

## Prerequisites
Control de tus propias emociones; intención genuina de ayudar y resolver.

## Steps
1. NO digas «cálmate» (lo enfada más y abre una brecha).
2. Refleja su emoción: súbela un poco para mostrar que estás de su lado («¡No me lo puedo creer! ¿Cuánto se han retrasado?»).
3. Atenúa: mantenla un punto por debajo de la suya para empezar a desescalar.
4. Una vez aliados y más calmados, pasa a resolver el problema real («¿cómo te ayudo a arreglarlo?»).

## Anti-patterns
Decir «cálmate»; ignorar la emoción; reflejarla sin atenuarla (la amplificas).

## Expected Outcome
La situación se serena y ambos podéis abordar el problema de fondo.

## Failure Signals
La persona se cierra o se enfada más (probablemente le dijiste que se calmara o no reflejaste).

## Underlying Logic
Compartir la emoción crea alianza; atenuarla la guía hacia abajo sin confrontación.

## Notes and Variants
Funciona con ira, tristeza, envidia e incluso humor (sonríe y luego reconduce a la seriedad).""",
    },
    {
        "id": "taku-manejar-ultimatums", "taku_type": "protocol",
        "title": "Manejar ultimátums (darlos, hacerlos hacia arriba, recibirlos)",
        "origin": ORIGIN, "domain": ["liderazgo", "jocko", "negociacion"],
        "when_to_use": "En los casos rarísimos en que un ultimátum es inevitable, o cuando te ponen uno a ti.",
        "when_not_to_use": "Como herramienta habitual: no dejan margen, atrapan a la gente y dañan la relación.",
        "aku_links": links([ULT, "aku-dont-dig-in-no-sobrecomprometerse-claim"]), "taku_relations": {},
        "body": """## Purpose
Usar (o sobrevivir a) un ultimátum con el mínimo daño a la relación, el equipo y la misión.

## Trigger Conditions
Agotadas todas las vías de liderazgo, «basta es basta»; o un jefe te impone un ultimátum.

## Required Resources
Honestidad brutal; capacidad de mantener la línea (si lo das) o la dignidad (si lo recibes).

## Protocol Steps
- **Como jefe**: pregúntate «¿dónde falló mi liderazgo?»; si procede, hazlo explícito (requisito + consecuencia), no des uno que no puedas cumplir, y en un equipo ponlo sobre el líder.
- **Hacia arriba**: evita el ultimátum (revela los límites de tu lealtad); prefiere discusión o, si de verdad vas a actuar, un aviso gentil.
- **Si te lo ponen a ti**: di la verdad a ti mismo (¿es posible? ¿puedo hacer más?), a tu equipo (dig in juntos) y, si es imposible pese al máximo esfuerzo, a tu jefe (qué necesitarías y qué pasará si no).

## Decision Points
¿Es realmente el último recurso? ¿La tarea es posible? ¿El jefe tiene la humildad de escuchar la verdad?

## Exit Conditions
Se cumple, se retira/modifica el ultimátum, o lo afrontas con dignidad y proteges al equipo.

## Failure Handling
Si el jefe se mantiene firme en lo imposible: haz tu mejor esfuerzo, protege al equipo, no seas rencoroso y aguanta las consecuencias con la cabeza alta.

## Review Trigger
Tras el episodio, evalúa qué falló en el liderazgo para no volver a necesitar un ultimátum.""",
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
