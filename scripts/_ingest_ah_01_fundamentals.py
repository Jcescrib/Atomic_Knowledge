# -*- coding: utf-8 -*-
"""Atomic Habits — ch1 The Surprising Power of Atomic Habits (THE FUNDAMENTALS)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/james-clear/atomic-habits/atomic-habits.md"
ORIGIN = "James Clear — Atomic Habits (2018)"
D = "2026-06-05"
JC = "james-clear"

def c(idn, cls, st, dom, rel=None):
    return {"id": idn, "class": cls, "statement": st, "origin": ORIGIN,
            "domain": dom, "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    c("aku-habito-atomico-concept", "concept",
      "Un hábito atómico es un hábito diminuto (un cambio marginal, una mejora del 1%) que "
      "forma parte de un sistema mayor; incluye el doble sentido de «atómico»: pequeño y fácil "
      "de hacer, pero también una unidad fundamental —como los átomos son los bloques de las "
      "moléculas— y fuente de un poder enorme por composición; excluye el cambio aislado y "
      "puntual; implica que los grandes resultados se construyen con rutinas pequeñas dentro "
      "de un sistema de crecimiento compuesto.",
      [JC, "habitos", "atomic-habits"],
      {"related": ["aku-agregacion-de-ganancias-marginales-concept"]}),
    c("aku-agregacion-de-ganancias-marginales-concept", "concept",
      "La agregación de ganancias marginales (Dave Brailsford, British Cycling) es la "
      "filosofía de buscar una mejora del 1% en todo lo que haces: si descompones cualquier "
      "actividad en sus partes y mejoras cada una un 1%, la suma produce un incremento "
      "significativo; incluye atacar áreas pasadas por alto e inesperadas; implica que muchas "
      "mejoras diminutas acumuladas transforman un desempeño mediocre en dominante.",
      [JC, "habitos", "mejora-continua"]),
    c("aku-los-habitos-son-el-interes-compuesto-de-la-mejora-personal-claim", "claim",
      "Los hábitos son el interés compuesto de la mejora personal: igual que el dinero se "
      "multiplica por interés compuesto, los efectos de tus hábitos se multiplican al "
      "repetirlos; mejorar un 1% cada día durante un año te deja ~37 veces mejor (1.01^365 = "
      "37,78), mientras que empeorar un 1% diario te reduce casi a cero (0.99^365 = 0,03).",
      [JC, "habitos", "interes-compuesto"],
      {"related": ["aku-capitalizar-interes-compuesto-method",
                   "aku-habito-atomico-concept"]}),
    c("aku-plateau-of-latent-potential-valley-of-disappointment-concept", "concept",
      "El Plateau of Latent Potential (meseta del potencial latente) es el patrón por el que "
      "los hábitos no parecen producir resultados hasta cruzar un umbral crítico, momento en "
      "que se libera de golpe el progreso almacenado (como el hielo que solo se derrite a "
      "32 °F tras subir de 25 a 31 sin cambio visible); incluye la «Valley of Disappointment» "
      "—la fase inicial en que el esfuerzo parece no rendir y la gente abandona—; implica que "
      "el trabajo no se desperdicia, solo se almacena, y exige paciencia hasta el breakthrough.",
      [JC, "habitos", "paciencia"]),
    c("aku-tus-resultados-son-una-medida-rezagada-de-tus-habitos-claim", "claim",
      "Tus resultados son una medida rezagada (lagging measure) de tus hábitos: tu patrimonio "
      "lo es de tus hábitos financieros, tu peso de tus hábitos alimentarios, tu conocimiento "
      "de tus hábitos de aprendizaje —obtienes lo que repites—; por eso conviene preocuparse "
      "más por la trayectoria actual que por los resultados actuales.",
      [JC, "habitos", "resultados"]),
    c("aku-sistemas-vs-metas-en-atomic-habits-concept", "concept",
      "En Atomic Habits, las metas (goals) son los resultados que quieres lograr y los "
      "sistemas (systems) son los procesos que llevan a esos resultados; incluye cuatro "
      "problemas de centrarse en metas: (1) ganadores y perdedores comparten las mismas metas, "
      "(2) lograr una meta es un cambio momentáneo si no cambias el sistema, (3) las metas "
      "restringen la felicidad («seré feliz cuando…»), y (4) las metas chocan con el progreso "
      "a largo plazo (efecto yo-yo); implica que para mejorar de verdad hay que olvidar las "
      "metas y enfocarse en el sistema —el pensamiento a largo plazo es goal-less—.",
      [JC, "habitos", "sistemas"],
      {"related": ["aku-sistemas-no-metas-disena-tu-entorno-para-tener-exito-concept",
                   "aku-no-subes-al-nivel-de-tus-metas-caes-al-de-tus-sistemas-claim"]}),
    c("aku-no-subes-al-nivel-de-tus-metas-caes-al-de-tus-sistemas-claim", "claim",
      "No subes al nivel de tus metas, sino que caes al nivel de tus sistemas: si tienes "
      "problemas para cambiar tus hábitos, el problema no eres tú sino tu sistema; arregla los "
      "inputs (el sistema) y los outputs (los resultados) se arreglarán solos.",
      [JC, "habitos", "sistemas"]),
]

written, cross = akugen.generate(akus, [], ROOT)
print("WRITTEN:", len(written))
for w in written: print("  ", os.path.relpath(w, ROOT))
ops_by_id = {}
for new_id, field, inv, tgt in cross:
    ops_by_id.setdefault(tgt, {"id": tgt, "add_rel": []})["add_rel"].append((inv, new_id))
akupatch.apply(ROOT, list(ops_by_id.values()))
print("PATCHED:", list(ops_by_id.keys()))
print("CROSS:", len(cross))
