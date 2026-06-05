# -*- coding: utf-8 -*-
"""Ingest The Code (libro 6 Jocko) — Section Two: THE EVALUATION."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/the-code/the-code.md"
ORIGIN = "Jocko Willink, Dave Berke & Sarah Armstrong — The Code. The Evaluation. The Protocols. (2020)"
D = "2026-06-05"
B = "desarrollo-personal"

akus = [
    {"id": "aku-the-evaluation-concept", "class": "concept",
     "statement": (
        "The Evaluation (La Evaluación) es un sistema de autoevaluación que define el "
        "objetivo (ser un Eminently Qualified Human), identifica los atributos críticos "
        "para lograrlo y permite trazar el progreso cada día; incluye seis categorías "
        "universales —Health, Personal Development, Professional Development, "
        "Character/Leadership, Relationship y Preparedness/Safety—, cada una puntuada de "
        "0 a 5; excluye comparar tu puntuación con la de otros (es you vs you, capacidad "
        "frente a desempeño); implica que, fijando un estándar alto y casi imposible, el "
        "mero esfuerzo por medirse y mejorar cada día acerca al ideal."),
     "origin": ORIGIN, "domain": [B, "jocko", "the-evaluation", "autoevaluacion", "framework"],
     "sources": [SRC], "created": D, "updated": D,
     "rel": {
        "supported_by": [
            "aku-evaluation-health-concept", "aku-evaluation-personal-development-concept",
            "aku-evaluation-professional-development-concept",
            "aku-evaluation-character-leadership-concept",
            "aku-evaluation-relationship-concept", "aku-evaluation-preparedness-safety-concept"],
        "supports": ["aku-evaluation-scoring-0-5-method"],
        "related": ["aku-the-code-concept", "aku-eminently-qualified-human-concept",
                    "aku-autoevaluacion-cuerpo-mente-alma-concept"]}},

    {"id": "aku-evaluation-health-concept", "class": "concept",
     "statement": (
        "Health (Salud) es la categoría de The Evaluation que cubre la rutina diaria de "
        "actividad física, descanso y nutrición para que el cuerpo —soporte del cerebro— "
        "soporte las demandas de la vida; incluye Physical Fitness (resistencia "
        "cardiovascular, fuerza, agilidad, flexibilidad y movilidad), Sleep/Rest (cantidad "
        "y calidad óptimas de sueño) y Diet/Nutrition (ingesta adecuada de nutrientes); "
        "implica que no puedes alcanzar tu potencial si no estás sano."),
     "origin": ORIGIN, "domain": [B, "jocko", "the-evaluation", "salud", "fitness"],
     "sources": [SRC], "created": D, "updated": D, "rel": {}},

    {"id": "aku-evaluation-personal-development-concept", "class": "concept",
     "statement": (
        "Personal Development (Desarrollo personal) es la categoría de The Evaluation "
        "centrada en nutrir y entrenar la mente y las conductas personales; incluye "
        "Intellectual Fitness (leer, escribir, crear, hacer cosas en las que no se es "
        "bueno y salir de la zona de confort), Time Management, Financial Management y "
        "Personal Goals; implica que mente y hábitos requieren la misma atención "
        "deliberada que el cuerpo."),
     "origin": ORIGIN, "domain": [B, "jocko", "the-evaluation", "desarrollo-personal", "habitos"],
     "sources": [SRC], "created": D, "updated": D,
     "rel": {"related": ["aku-tiempo-recurso-mas-valioso-y-limitado-claim"]}},

    {"id": "aku-evaluation-professional-development-concept", "class": "concept",
     "statement": (
        "Professional Development (Desarrollo profesional) es la categoría de The "
        "Evaluation sobre ser bueno en tu trabajo para sostenerte financieramente, dar "
        "ejemplo a tus hijos y alcanzar objetivos a largo plazo; incluye Performance "
        "(rendir bien, pedir y aceptar feedback, apoyar al equipo), "
        "Advancement/Qualifications (lograr certificaciones y pasos para promocionar) y "
        "encontrar significado en el trabajo (o diseñar una salida si no lo tiene); "
        "implica que el éxito profesional es clave para el éxito personal."),
     "origin": ORIGIN, "domain": [B, "jocko", "the-evaluation", "carrera", "trabajo"],
     "sources": [SRC], "created": D, "updated": D, "rel": {}},

    {"id": "aku-evaluation-character-leadership-concept", "class": "concept",
     "statement": (
        "Character/Leadership (Carácter/Liderazgo) es la categoría de The Evaluation sobre "
        "quién eres como persona —la cualidad más definitoria de tu vida, bajo tu control "
        "total— y cómo lideras e influyes en tu mundo; incluye Humility (gestionar el "
        "ego), Emotional Control y Mentorship/Charity; implica que todos pueden y deben "
        "liderar sin necesidad de estar al mando de nadie ni de nada."),
     "origin": ORIGIN, "domain": [B, "jocko", "the-evaluation", "caracter", "liderazgo"],
     "sources": [SRC], "created": D, "updated": D,
     "rel": {"related": ["aku-humildad-es-la-cualidad-mas-importante-claim",
                          "aku-ego-nubla-todo-claim",
                          "aku-no-sobrerreaccionar-mantener-la-calma-claim"]}},

    {"id": "aku-evaluation-relationship-concept", "class": "concept",
     "statement": (
        "Relationship (Relaciones) es la categoría de The Evaluation que cubre construir y "
        "reforzar los vínculos con las personas más importantes de tu mundo, aprovechando "
        "el tiempo limitado con ellas para aumentar confianza, esprit de corps y apoyo "
        "mutuo; incluye el tiempo de calidad con la familia y con amigos/colegas; implica "
        "que las relaciones son la herramienta más poderosa para el éxito a largo plazo "
        "porque no se logra mucho en solitario."),
     "origin": ORIGIN, "domain": [B, "jocko", "the-evaluation", "relaciones"],
     "sources": [SRC], "created": D, "updated": D,
     "rel": {"related": ["aku-power-of-relationships-liderazgo-concept"]}},

    {"id": "aku-evaluation-preparedness-safety-concept", "class": "concept",
     "statement": (
        "Preparedness/Safety (Preparación/Seguridad) es la categoría de The Evaluation "
        "sobre estar preparado física y mentalmente para amenazas y crisis y asegurar que "
        "los tuyos también lo estén; incluye Martial Arts/self-defense, Weapons Training, "
        "Fire/Safety/Emergency y Neighborhood/Community impact; implica que la violencia y "
        "los desastres pueden surgir sin aviso y que entrenar la respuesta es una "
        "responsabilidad."),
     "origin": ORIGIN, "domain": [B, "jocko", "the-evaluation", "preparacion", "seguridad"],
     "sources": [SRC], "created": D, "updated": D, "rel": {}},

    {"id": "aku-evaluation-scoring-0-5-method", "class": "method",
     "statement": (
        "En The Evaluation, cada atributo se puntúa de 0 a 5 midiendo tu desempeño frente "
        "a tu propia capacidad (you vs you), no frente a otros: la nota refleja cuánto "
        "esfuerzo pusiste respecto a lo que eres capaz; como la escala es relativa a la "
        "capacidad y esta crece con el tiempo, una misma acción (p. ej. caminar 1 milla) "
        "puede ser un 5 para un principiante y un 1 para alguien entrenado, y subir la "
        "nota se vuelve más difícil a medida que avanzas."),
     "origin": ORIGIN, "domain": [B, "jocko", "the-evaluation", "scoring", "autoevaluacion"],
     "sources": [SRC], "created": D, "updated": D,
     "rel": {"related": ["aku-autoevaluacion-honesta-you-vs-you-claim",
                          "aku-mejorar-mas-dificil-al-crecer-capacidad-claim"]}},

    {"id": "aku-eqh-no-es-estado-sino-camino-sin-fin-claim", "class": "claim",
     "statement": (
        "Ser un Eminently Qualified Human no es un estatus que se alcanza ni una "
        "conclusión a la que se llega, sino estar en un Path que no termina: cada día hay "
        "más por hacer; en cuanto desplazas el foco de un área a otra, los logros recién "
        "conseguidos empiezan a erosionarse y las ganancias a decaer, obligando a "
        "reconstruir lo perdido."),
     "origin": ORIGIN, "domain": [B, "jocko", "eminently-qualified-human", "mejora-continua"],
     "sources": [SRC], "created": D, "updated": D,
     "rel": {"related": ["aku-eminently-qualified-human-concept", "aku-the-path-concept",
                          "aku-the-evaluation-concept"]}},

    {"id": "aku-autoevaluacion-honesta-you-vs-you-claim", "class": "claim",
     "statement": (
        "La autoevaluación solo funciona si es brutalmente honesta y humilde: es you vs "
        "you, no se compara con los demás, y ser blando contigo mismo no te ayuda ni a ti "
        "ni a quienes te rodean; medir el esfuerzo real frente a la capacidad propia es lo "
        "que produce progreso."),
     "origin": ORIGIN, "domain": [B, "jocko", "autoevaluacion", "humildad", "honestidad"],
     "sources": [SRC], "created": D, "updated": D,
     "rel": {"related": ["aku-the-evaluation-concept", "aku-evaluation-scoring-0-5-method",
                          "aku-humildad-es-la-cualidad-mas-importante-claim",
                          "aku-ego-impide-evaluacion-honesta-claim"]}},

    {"id": "aku-mejorar-mas-dificil-al-crecer-capacidad-claim", "class": "claim",
     "statement": (
        "A medida que avanzas por The Path tu capacidad aumenta, y por eso mejorar se "
        "vuelve progresivamente más difícil: hay que trabajar más y hacer más para lograr "
        "la misma —o incluso menor— cantidad de mejora."),
     "origin": ORIGIN, "domain": [B, "jocko", "mejora-continua", "capacidad"],
     "sources": [SRC], "created": D, "updated": D,
     "rel": {"related": ["aku-evaluation-scoring-0-5-method", "aku-the-path-concept"]}},

    {"id": "aku-tiempo-recurso-mas-valioso-y-limitado-claim", "class": "claim",
     "statement": (
        "No hay recurso más valioso que el tiempo y es limitado en cantidad: nadie sabe "
        "cuánto le queda, así que hay que maximizarlo todo y evitar gastarlo en lo que no "
        "es productivo; lo bien que gestionas tu tiempo determina cuán productivo eres y, "
        "con disciplina, genera más tiempo libre para hacer lo que quieres cuando "
        "quieres."),
     "origin": ORIGIN, "domain": [B, "jocko", "tiempo", "productividad", "disciplina"],
     "sources": [SRC], "created": D, "updated": D,
     "rel": {"related": ["aku-the-path-concept"]}},
]

takus = [
    {"id": "taku-la-evaluacion-eqh", "taku_type": "framework", "subdir": "frameworks",
     "title": "La Evaluación del Eminently Qualified Human",
     "origin": ORIGIN, "domain": [B, "jocko", "the-evaluation", "autoevaluacion"],
     "when_to_use": "Para autoevaluarte a diario contra un estándar exigente en las seis áreas críticas de la vida y dirigir tu mejora.",
     "when_not_to_use": "Para compararte con otras personas o como sello de estatus alcanzado: la Evaluación es you vs you y mide un camino que no termina.",
     "aku_links": {"justified_by": [
        "aku-the-evaluation-concept", "aku-evaluation-scoring-0-5-method",
        "aku-the-code-concept", "aku-eminently-qualified-human-concept"]},
     "created": D, "updated": D,
     "body": (
        "## Summary\n\n"
        "Sistema de autoevaluación de Jocko Willink para medir y dirigir el progreso "
        "hacia el Eminently Qualified Human. Operacionaliza The Code traduciéndolo a seis "
        "categorías con atributos puntuables de 0 a 5 contra la propia capacidad.\n\n"
        "## Core Components\n\n"
        "Seis categorías, cada una con atributos:\n\n"
        "1. **Health** — Physical Fitness · Sleep/Rest · Diet/Nutrition.\n"
        "2. **Personal Development** — Intellectual Fitness · Time Management · Financial Management · Personal Goals.\n"
        "3. **Professional Development** — Performance · Advancement/Qualifications · significado en el trabajo.\n"
        "4. **Character/Leadership** — Humility · Emotional Control · Mentorship/Charity.\n"
        "5. **Relationship** — tiempo de calidad con familia · con amigos/colegas.\n"
        "6. **Preparedness/Safety** — Martial Arts · Weapons Training · Fire/Safety/Emergency · Neighborhood/Community.\n\n"
        "Escala por atributo: 0 (inacción/contraproducente) · 1 (mínimo) · 2-4 (esfuerzo serio) · 5 (máximo respecto a la capacidad actual).\n\n"
        "## How to Apply\n\n"
        "1. Para cada atributo, valora con honestidad brutal tu esfuerzo frente a tu capacidad (you vs you).\n"
        "2. Asigna 0-5 según los anclajes de la rúbrica de cada categoría.\n"
        "3. Hazlo a diario; identifica la categoría más floja y actúa sobre ella.\n"
        "4. Sube el listón a medida que tu capacidad crece (un 5 de hoy será un 1 mañana).\n"
        "5. Cuando caes del Path, usa los Protocolos para volver.\n\n"
        "## Underlying Claims\n\n"
        "Se apoya en que el objetivo (EQH) es un camino sin fin, en que la autoevaluación "
        "debe ser honesta y humilde, y en que mejorar es cada vez más difícil al crecer la "
        "capacidad.\n\n"
        "## Strengths\n\n"
        "Convierte un ideal difuso en métricas accionables y diarias; cubre la vida "
        "completa, no solo lo profesional; relativa a la capacidad propia, lo que la hace "
        "justa a cualquier nivel de partida.\n\n"
        "## Limitations and Criticisms\n\n"
        "Depende por completo de la honestidad del evaluador (sin auditor externo); la "
        "escala relativa a la capacidad es subjetiva; el estándar casi imposible puede "
        "desmotivar si se confunde el fin (esfuerzo) con la meta (puntuación perfecta).\n\n"
        "## Variants and Extensions\n\n"
        "Personalizable: las categorías y el Código pueden adaptarse al contexto de cada "
        "persona. Formularios descargables en jockopublishing.com/downloads."),
    },
]

written, cross = akugen.generate(akus, takus, ROOT)
print("WRITTEN:")
for w in written:
    print("  ", os.path.relpath(w, ROOT))

# same-author dedup targets that should also receive the-code as an added source
ADD_SOURCE = {
    "aku-humildad-es-la-cualidad-mas-importante-claim",
    "aku-ego-nubla-todo-claim",
    "aku-no-sobrerreaccionar-mantener-la-calma-claim",
    "aku-power-of-relationships-liderazgo-concept",
    "aku-ego-impide-evaluacion-honesta-claim",
}
ops_by_id = {}
for new_id, field, inv, tgt in cross:
    op = ops_by_id.setdefault(tgt, {"id": tgt, "add_rel": []})
    op["add_rel"].append((inv, new_id))
for tgt in ADD_SOURCE:
    op = ops_by_id.setdefault(tgt, {"id": tgt})
    op["add_source"] = SRC
    op["updated"] = D

akupatch.apply(ROOT, list(ops_by_id.values()))
print("\nPATCHED EXISTING:")
for k, v in ops_by_id.items():
    print("  ", k, "| rel:", v.get("add_rel", []), "| src" if v.get("add_source") else "")
print("\nCROSS count:", len(cross))
