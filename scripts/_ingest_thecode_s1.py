# -*- coding: utf-8 -*-
"""Ingest The Code (libro 6 Jocko) — Section One: THE CODE."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/the-code/the-code.md"
ORIGIN = "Jocko Willink, Dave Berke & Sarah Armstrong — The Code. The Evaluation. The Protocols. (2020)"
D = "2026-06-05"

akus = [
    {
        "id": "aku-the-code-concept", "class": "concept",
        "statement": (
            "El Code (El Código) es un estándar personal codificado en 10 compromisos "
            "—cuidar salud física y entorno, desarrollarse mentalmente, no malgastar el "
            "tiempo, no malgastar el dinero, fijar metas, excelir en el trabajo, ser "
            "humilde y controlar el ego, controlar las emociones, anteponer y proteger a "
            "los demás, y estar preparado para defender a los tuyos— que define el ideal "
            "de Eminently Qualified Human hacia el que se aspira; incluye ser el estándar "
            "más alto posible (casi imposible) que revela y delinea The Path; excluye ser "
            "inalterable (es personalizable) y ser alcanzable a la perfección; implica que, "
            "aun sin poder cumplirlo del todo, el mero hecho de intentarlo te hace mejor."),
        "origin": ORIGIN, "domain": ["desarrollo-personal", "jocko", "the-code", "disciplina", "estandar"],
        "sources": [SRC], "created": D, "updated": D,
        "rel": {"related": [
            "aku-the-path-concept", "aku-eminently-qualified-human-concept",
            "aku-disciplina-se-extiende-a-todo-claim", "aku-empezar-aqui-y-ahora-method",
            "aku-pequenas-elecciones-diarias-construyen-todo-claim"]},
    },
    {
        "id": "aku-the-path-concept", "class": "concept",
        "statement": (
            "The Path (El Camino) es cómo te conviertes en quien quieres ser, quien "
            "necesitas ser y lo que el mundo necesita que seas: el camino de la disciplina "
            "que conduce a la libertad y a alcanzar tu potencial; incluye ser "
            "simultáneamente único para cada persona (tus metas, sueños y lo que quieres "
            "llegar a ser) y en gran parte común a todos (el esfuerzo por ser un Eminently "
            "Qualified Human); se descubre respondiendo qué te importa, quién quieres ser y "
            "qué necesitan de ti los más importantes, y escribiendo lo que debes hacer; "
            "implica una guerra contra la debilidad, la ignorancia y la confusión que "
            "produce fuerza, conocimiento y entendimiento."),
        "origin": ORIGIN, "domain": ["desarrollo-personal", "jocko", "the-path", "disciplina", "libertad"],
        "sources": [SRC], "created": D, "updated": D,
        "rel": {"related": [
            "aku-the-code-concept", "aku-eminently-qualified-human-concept",
            "aku-discipline-equals-freedom-concept",
            "aku-empezar-aqui-y-ahora-method",
            "aku-pequenas-elecciones-diarias-construyen-todo-claim"]},
    },
    {
        "id": "aku-eminently-qualified-human-concept", "class": "concept",
        "statement": (
            "El Eminently Qualified Human (EQH) es la persona que ha alcanzado la maestría "
            "en cada faceta de la vida y ha desarrollado su pleno potencial en toda "
            "dimensión medible, viviendo The Code; incluye sobresalir simultáneamente en "
            "salud, desarrollo personal y profesional, carácter/liderazgo, relaciones y "
            "preparación/seguridad; excluye ser un estatus que se alcanza o una meta final "
            "(es estar en un Path que no termina); implica que siempre queda más por hacer "
            "y que los logros se erosionan si se descuidan."),
        "origin": ORIGIN, "domain": ["desarrollo-personal", "jocko", "eminently-qualified-human", "maestria", "potencial"],
        "sources": [SRC], "created": D, "updated": D,
        "rel": {"related": ["aku-the-code-concept", "aku-the-path-concept"]},
    },
    {
        "id": "aku-pequenas-elecciones-diarias-construyen-todo-claim", "class": "claim",
        "statement": (
            "Cada momento de vida se compone de elecciones diminutas que por separado no "
            "significan nada pero combinadas lo significan todo; mantenerse en The Path "
            "exige tomar repetidamente la elección correcta y difícil —negar la "
            "gratificación inmediata y empujar contra la debilidad, la pereza, el ego y el "
            "miedo— cada día, imponiendo una disciplina diaria sin concesiones en todas las "
            "cosas (Unmitigated Daily Discipline in all things)."),
        "origin": ORIGIN, "domain": ["desarrollo-personal", "jocko", "disciplina", "decisiones", "gratificacion-diferida"],
        "sources": [SRC], "created": D, "updated": D,
        "rel": {"related": [
            "aku-the-code-concept", "aku-the-path-concept",
            "aku-disciplina-se-extiende-a-todo-claim",
            "aku-empezar-aqui-y-ahora-method",
            "aku-willpower-no-es-finita-disciplina-engendra-disciplina-claim"]},
    },
]

takus = [
    {
        "id": "taku-el-codigo-10-compromisos", "taku_type": "heuristic", "subdir": "heuristics",
        "title": "El Código — los 10 compromisos diarios",
        "origin": ORIGIN, "domain": ["desarrollo-personal", "jocko", "the-code", "disciplina"],
        "when_to_use": "Cuando quieres un estándar personal concreto y medible para orientar tu vida diaria hacia tu máximo potencial.",
        "when_not_to_use": "Como dogma rígido idéntico para todos: el Código es un punto de partida personalizable, no una ley inmutable.",
        "aku_links": {"justified_by": [
            "aku-the-code-concept", "aku-eminently-qualified-human-concept",
            "aku-disciplina-se-extiende-a-todo-claim", "aku-empezar-aqui-y-ahora-method"]},
        "created": D, "updated": D,
        "body": (
            "## The Rule\n\n"
            "Vive según un código personal de 10 compromisos diarios e imponte Unmitigated "
            "Daily Discipline in all things:\n\n"
            "1. Cuidar la salud física (ejercicio, nutrición, descanso) y el entorno (orden).\n"
            "2. Desarrollarse mentalmente (leer, escribir, dibujar, construir, crear).\n"
            "3. No malgastar el tiempo: es precioso.\n"
            "4. No malgastar el dinero y tomar decisiones financieras prudentes.\n"
            "5. Fijar metas hacia las que esforzarse.\n"
            "6. Excelir en el trabajo, porque el trabajo es parte integral de la vida.\n"
            "7. Ser humilde y no dejar que el ego perjudique las decisiones.\n"
            "8. Controlar las emociones y no dejar que perjudiquen las decisiones.\n"
            "9. Anteponer a los demás: ayudar y proteger a quien no puede protegerse, cuidar de amigos y familia, tratar con respeto.\n"
            "10. Estar listo para proteger a amigos y familia: equipo preparado, entrenamiento de defensa.\n\n"
            "## What It Replaces\n\n"
            "Sustituye el vagar sin objetivo, estándar ni rumbo —vivir reactivamente— por un "
            "ideal explícito y codificado contra el que evaluarse cada día.\n\n"
            "## When It Holds\n\n"
            "Cuando se personaliza a la propia vida y se usa como punto de partida exigente "
            "(el estándar debe ser alto, casi imposible); el valor está en esforzarse, no en "
            "cumplirlo a la perfección.\n\n"
            "## When It Fails\n\n"
            "Si se trata como ley inmutable y universal, o como checklist que se cumple "
            "mecánicamente sin honestidad ni disciplina real; un código sin acción diaria no "
            "cambia nada.\n\n"
            "## Why It Works\n\n"
            "Define con precisión el objetivo (Eminently Qualified Human) y delinea The Path, "
            "convirtiendo un ideal difuso en compromisos concretos y evaluables; la disciplina "
            "diaria sobre pequeñas elecciones, combinada, lo significa todo.\n\n"
            "## Calibration\n\n"
            "Revisa y ajusta el código a tu contexto; sube el listón a medida que tu capacidad "
            "crece (lo que hoy es exigente mañana será base). Empareja con La Evaluación para "
            "medir el progreso."),
    },
]

written, cross = akugen.generate(akus, takus, ROOT)
print("WRITTEN:")
for w in written:
    print("  ", os.path.relpath(w, ROOT))

# --- dedup enrichments (same-author Jocko: add source + updated, NO confidence bump) ---
dedup_ops = [
    {"id": "aku-empezar-aqui-y-ahora-method", "add_source": SRC, "updated": D},
    {"id": "aku-disciplina-se-extiende-a-todo-claim", "add_source": SRC, "updated": D},
]
# --- cross-link inverses on existing AKUs ---
cross_ops = {}
for new_id, field, inv, tgt in cross:
    cross_ops.setdefault(tgt, {"id": tgt, "add_rel": []})
    cross_ops[tgt]["add_rel"].append((inv, new_id))

# merge dedup + cross ops by id
ops_by_id = {}
for op in dedup_ops:
    ops_by_id[op["id"]] = op
for tgt, op in cross_ops.items():
    if tgt in ops_by_id:
        ops_by_id[tgt].setdefault("add_rel", []).extend(op["add_rel"])
    else:
        ops_by_id[tgt] = op

akupatch.apply(ROOT, list(ops_by_id.values()))
print("\nPATCHED EXISTING:")
for k in ops_by_id:
    print("  ", k, ops_by_id[k].get("add_rel", ""), "src" if ops_by_id[k].get("add_source") else "")
print("\nCROSS (new->existing) count:", len(cross))
