# -*- coding: utf-8 -*-
"""Ingesta — Discipline Equals Freedom, Batch 6B (Martial arts -> Immediate Action Drills) + 3 TAKUs."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/discipline-equals-freedom/discipline-equals-freedom.md"
ORIGIN = "Jocko Willink, Discipline Equals Freedom: Field Manual (2017)"
MA = "aku-progresion-artes-marciales-concept"
DEF_H = "aku-defensa-propia-jerarquia-mente-correr-arma-claim"
JJ = "aku-jiu-jitsu-meta-escapar-no-ir-al-suelo-claim"
GUN = "aku-cuatro-reglas-seguridad-armas-method"
IAD = "aku-immediate-action-drills-amenaza-method"
SCHOOL = "aku-elegir-academia-jiu-jitsu-method"
D = "2026-06-05"
DOM = ["jocko", "artes-marciales", "defensa-personal"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(MA, "concept",
        "Todo el mundo debería entrenar artes marciales; hay tres formas: grappling, striking y armas; el orden recomendado de aprendizaje es empezar por jiu-jitsu brasileño (el más complejo y cerebral, grappling), luego boxeo, después Muay Thai y lucha (wrestling), y más tarde judo, SAMBO, Krav Maga, etc.; sus beneficios van más allá de la defensa personal (condición física, dureza mental, acostumbrarse a la incomodidad y seguir luchando).",
        DOM,
        {"related": ["aku-train-hard-but-train-smart-concept", "aku-disciplina-se-extiende-a-todo-claim"]}),
    aku(DEF_H, "claim",
        "La jerarquía de la defensa personal: la forma más crítica es la mente (ser consciente y evitar situaciones de peligro); cuando la mente ya no basta, el igualador definitivo es el arma de fuego (con entrenamiento); la primera línea física es huir/correr; y el grappling sirve para escapar de la sujeción cuando no puedes huir.",
        DOM + ["defensa-personal"],
        {"related": ["aku-mind-control-controla-tu-propia-mente-concept", JJ]}),
    aku(JJ, "claim",
        "En defensa personal, la meta del jiu-jitsu no es llevar la pelea al suelo, sino al contrario: escapar de la sujeción del atacante y levantarse para poder huir; aun así, como las peleas suelen acabar en el suelo, hay que estar preparado para ello (no entrenar jiu-jitsu por no querer ir al suelo es como no aprender a nadar por no querer entrar al agua).",
        DOM + ["jiu-jitsu"],
        {"supports": [MA]}),
    aku(GUN, "method",
        "Las cuatro reglas de seguridad con armas de fuego: (1) trata toda arma como si estuviera cargada; (2) nunca apuntes a algo que no estés dispuesto a destruir; (3) mantén el dedo fuera del gatillo hasta tener la mira en el objetivo; (4) asegúrate siempre de tu objetivo y de lo que hay detrás; además, guárdalas en lugar seguro y no las poseas sin entrenamiento.",
        DOM + ["armas", "seguridad"],
        {}),
    aku(IAD, "method",
        "Drills de acción inmediata ante una amenaza: entrena duro para el peor caso; evita las zonas de alto riesgo; mantén conciencia situacional (evalúa personas, rutas de escape, cover/concealment) y, si percibes la amenaza, aléjate proactivamente; si te sorprenden, ACTÚA: corre si puedes; si te sujetan, ataca con violencia y luego corre; si hay disparos, agáchate y llama a la policía (disparos sueltos→corre; fuego rápido→cúbrete y corre en una pausa; tirador activo→atrinchérate/escóndete o prepárate para enjambrar); usa el arma solo con extrema cautela (conoce objetivo y trasfondo; la policía puede verte a ti como amenaza).",
        DOM + ["defensa-personal", "amenaza"],
        {"related": ["aku-relax-look-around-make-a-call-method", DEF_H]}),
    aku(SCHOOL, "method",
        "Para elegir academia de jiu-jitsu: busca escuelas cercanas (la proximidad determina la frecuencia con que entrenarás); visítalas con tu equipo y participa (no solo mires); evalúa cómo se enseña, la actitud del instructor y los alumnos, si hay mucho ego y si sus metas se parecen a las tuyas; investiga el linaje y legitimidad del instructor (basta cinturón marrón o morado si no hay negro); y recuerda que el jiu-jitsu debe ser divertido y no un culto.",
        DOM + ["jiu-jitsu", "eleccion"],
        {"supports": [MA]}),
]

def links(jb, **extra):
    d = {"justified_by": jb, "constrained_by": [], "breaks_when": [], "illustrates": [], "challenges": []}
    d.update(extra); return d

takus = [
    {
        "id": "taku-progresion-artes-marciales", "taku_type": "framework",
        "title": "Progresión recomendada de artes marciales",
        "origin": ORIGIN, "domain": ["jocko", "artes-marciales"],
        "when_to_use": "Al planificar qué artes marciales aprender y en qué orden para defensa personal y desarrollo.",
        "when_not_to_use": "No como dogma rígido: la disponibilidad local y los objetivos personales pueden alterar el orden.",
        "aku_links": links([MA, JJ]), "taku_relations": {},
        "body": """## Summary
Ruta práctica para aprender artes marciales, priorizando lo más efectivo y transferible a la defensa real.

## Core Components
1. **Brazilian Jiu-Jitsu** (base): grappling, el más cerebral; escapar de la sujeción y levantarse.
2. **Boxeo**: striking simple y efectivo; ángulos, movimiento, velocidad; golpear y no ser golpeado.
3. **Muay Thai** y **Wrestling**: arsenal de golpeo (codos, rodillas, espinillas) y dominio de la posición/derribo.
4. **Otras** (judo, SAMBO, Krav Maga, Escrima/Kali): explorar tras una buena base.

## How to Apply
Empieza por BJJ en una buena academia cercana; añade boxeo; luego Muay Thai y wrestling; explora el resto sin dejar de entrenar.

## Underlying Claims
Las teorías ya se han probado (UFC, combate real, vídeo): hay realidad pragmática, no hace falta teorizar sobre «cuál es mejor».

## Strengths
Cubre grappling y striking; transfiere a defensa real; aporta condición física y dureza mental.

## Limitations and Criticisms
Las artes marciales evolucionan: hay que evolucionar con ellas; el arma de fuego sigue siendo el igualador definitivo cuando la mente no basta.

## Variants and Extensions
Catch wrestling (sumisiones), judo como reemplazo de BJJ donde no haya; armas (Escrima/Kali, Dog Brothers).""",
    },
    {
        "id": "taku-immediate-action-drills", "taku_type": "protocol",
        "title": "Drills de acción inmediata ante una amenaza",
        "origin": ORIGIN, "domain": ["jocko", "defensa-personal", "amenaza"],
        "when_to_use": "Para prepararse y reaccionar ante una confrontación o amenaza violenta en la vida real.",
        "when_not_to_use": "No sustituye el entrenamiento real ni el juicio legal sobre el uso de la fuerza.",
        "aku_links": links([IAD, DEF_H]), "taku_relations": {},
        "body": """## Purpose
Reaccionar con la mayor probabilidad de supervivencia ante una amenaza súbita.

## Trigger Conditions
Percepción de amenaza o confrontación violenta inminente o en curso.

## Required Resources
Entrenamiento previo (martial arts/armas); conciencia situacional.

## Protocol Steps
1. Prevén: entrena duro para el peor caso y evita zonas de alto riesgo.
2. Mantén conciencia situacional: evalúa personas, rutas de escape, cover (protege de balas) y concealment (oculta).
3. Si percibes amenaza, aléjate proactivamente; no esperes a que empeore.
4. Si te sorprenden: ACTÚA. Corre si puedes; si te sujetan, ataca con violencia y luego corre.
5. Si hay disparos: agáchate, llama a la policía. Disparos sueltos → corre. Fuego rápido → cúbrete y corre en una pausa.
6. Tirador activo en tu sala: atrinchérate/escóndete o prepárate para enjambrarlo entre todos.

## Decision Points
¿Puedo huir? ¿Hay cover? ¿Es momento de actuar o esperar la pausa?

## Exit Conditions
Estás a salvo y/o la amenaza ha sido neutralizada.

## Failure Handling
Si el plan falla, recurre al siguiente: huir → cubrirse → atacar. Adapta a la realidad.

## Review Trigger
USA EXTREMA CAUTELA con el arma: conoce objetivo y trasfondo; la policía puede verte como amenaza. Identifícate como amigo en cuanto puedas.""",
    },
    {
        "id": "taku-seguridad-armas-cuatro-reglas", "taku_type": "protocol",
        "title": "Las cuatro reglas de seguridad con armas de fuego",
        "origin": ORIGIN, "domain": ["jocko", "armas", "seguridad"],
        "when_to_use": "Siempre que se maneje, almacene o entrene con un arma de fuego.",
        "when_not_to_use": "No aplica: las cuatro reglas se mantienen en todo momento, sin excepción.",
        "aku_links": links([GUN]), "taku_relations": {},
        "body": """## Purpose
Prevenir lesiones y muertes accidentales manteniendo cuatro reglas constantes al manejar armas.

## Trigger Conditions
Cualquier interacción con un arma de fuego.

## Required Resources
Conciencia constante; entrenamiento con buen instructor; almacenamiento seguro.

## Protocol Steps
1. Trata toda arma como si estuviera cargada.
2. Nunca apuntes a algo que no estés dispuesto a destruir.
3. Mantén el dedo fuera del gatillo hasta tener la mira en el objetivo.
4. Asegúrate siempre de tu objetivo y de lo que hay detrás.

## Decision Points
Ante cualquier duda sobre estado del arma, línea de fuego o trasfondo: detente y verifica.

## Exit Conditions
Arma asegurada y guardada en lugar seguro fuera del alcance indebido.

## Failure Handling
Una violación de cualquier regla es un cuasi-accidente: para, corrige y re-entrena la seguridad.

## Review Trigger
Sin entrenamiento adecuado, poseer un arma es inútil o más peligroso para el dueño: forma continua con buen instructor.""",
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
