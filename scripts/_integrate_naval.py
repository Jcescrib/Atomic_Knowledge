# -*- coding: utf-8 -*-
"""INTEGRATE pass (paso 5.5) para el cluster Naval: enruta cada AKU aislado a un
concepto-ancla temático con `related` bidireccional, eliminando nodos huérfanos."""
import os, sys, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# anclas temáticas (todas wired)
A_RIQUEZA   = "aku-armate-con-specific-knowledge-accountability-y-leverage-claim"
A_LEVERAGE  = "aku-leverage-multiplicador-de-juicio-concept"
A_JUICIO    = "aku-judgment-naval-concept"
A_FELICIDAD = "aku-felicidad-es-el-estado-por-defecto-cuando-no-falta-nada-concept"
A_PAZ       = "aku-cambiar-aceptar-o-dejar-concept"
A_DESEO     = "aku-el-deseo-es-un-contrato-para-ser-infeliz-hasta-conseguirlo-concept"
A_HABITOS   = "aku-la-felicidad-es-una-habilidad-que-se-aprende-concept"
A_MEDITAC   = "aku-choiceless-awareness-acepta-sin-juzgar-y-el-90-por-ciento-de-pensamientos-son-miedo-concept"
A_MENTE     = "aku-awareness-vs-ego-eres-mas-que-tu-monkey-mind-concept"
A_LECTURA   = "aku-modelos-mentales-concept"
A_SALUD     = "aku-vivimos-en-desajuste-evolutivo-con-el-mundo-moderno-concept"
A_RELAC     = "aku-busca-personas-cuyos-valores-encajen-con-los-tuyos-claim"
A_LIBERTAD  = "aku-la-libertad-es-el-valor-supremo-claim"
A_VIDA      = "aku-los-tres-significados-de-la-vida-concept"

# orden de prioridad de routing (primer token que matchee gana)
ROUTES = [
    (["leverage"], A_LEVERAGE),
    (["specific-knowledge"], A_RIQUEZA),
    (["dieta", "nutricion", "ejercicio", "ayuno", "cuerpo-mente"], A_SALUD),
    (["salud"], A_SALUD),
    (["meditacion", "fisiologia"], A_MEDITAC),
    (["consciencia", "ego", "biologia"], A_MENTE),
    (["mente"], A_MENTE),
    (["lectura"], A_LECTURA),
    (["aprendizaje", "fundamentos", "pensamiento", "modelos-mentales", "ciencia", "pensamiento-independiente", "contrarian", "creencias"], A_LECTURA),
    (["decisiones", "juicio", "sesgos", "sabiduria", "estrategia", "etica"], A_JUICIO),
    (["paz", "aceptacion", "sufrimiento", "muerte", "ansiedad", "control", "interpretacion"], A_PAZ),
    (["deseo", "delusion", "foco"], A_DESEO),
    (["habitos", "disciplina", "cambio", "autotransformacion", "compromiso", "autoimagen", "practica", "motivacion", "vocacion"], A_HABITOS),
    (["relaciones", "entorno", "socios", "reputacion", "generosidad", "amor", "familia", "carrera", "comunicacion", "liderazgo", "carisma", "confianza", "señales", "valores"], A_RELAC),
    (["dinero", "libertad", "libertad-financiera", "independencia", "riesgo", "expectativas", "coraje", "validacion"], A_LIBERTAD),
    (["sentido-de-la-vida", "sentido", "filosofia", "autonomia"], A_VIDA),
    (["exito", "satisfaccion", "adaptacion-hedonica", "psicologia"], A_FELICIDAD),
    (["riqueza", "mentalidad", "trabajo", "escalar", "tecnologia", "ventas", "habilidad", "maestria", "unicidad", "internet", "productividad", "constancia", "tiempo", "accion", "paciencia", "juventud", "largo-plazo", "creatividad", "obsesion", "claridad", "valor", "supervivencia"], A_RIQUEZA),
]
DEFAULT = A_FELICIDAD


def domain_tokens(path):
    txt = open(path, encoding="utf-8").read()
    m = re.search(r"^domain:\s*\[(.*)\]", txt, re.M)
    if not m:
        return []
    return [t.strip() for t in m.group(1).split(",")]


def route(tokens):
    for keys, anchor in ROUTES:
        for k in keys:
            if k in tokens:
                return anchor
    return DEFAULT


# recolecta AKUs Naval aislados
iso = []
for path in glob.glob(os.path.join(ROOT, "aku", "*.md")):
    txt = open(path, encoding="utf-8").read()
    if "raw/libros/naval/" in txt and "<!-- sin relaciones -->" in txt:
        iso.append(os.path.basename(path)[:-3])

print(f"aislados a integrar: {len(iso)}")
ops = []
spokes = {}
for aku_id in iso:
    anchor = route(domain_tokens(os.path.join(ROOT, "aku", aku_id + ".md")))
    if anchor == aku_id:
        anchor = DEFAULT if aku_id != DEFAULT else A_RIQUEZA
    ops.append({"id": aku_id, "add_rel": [("related", anchor)]})
    ops.append({"id": anchor, "add_rel": [("related", aku_id)]})
    spokes[anchor] = spokes.get(anchor, 0) + 1

akupatch.apply(ROOT, ops)
print("spokes por ancla:")
for a, n in sorted(spokes.items(), key=lambda x: -x[1]):
    print(f"  {n:3d}  {a}")
