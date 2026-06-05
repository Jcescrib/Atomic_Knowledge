# -*- coding: utf-8 -*-
"""Atomic Habits — ch5 The Best Way to Start a New Habit (implementation intentions + habit stacking)."""
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
    c("aku-implementation-intention-method", "method",
      "Una implementation intention es un plan que haces de antemano sobre cuándo y dónde "
      "actuar, con la fórmula «cuando surja la situación X, haré la respuesta Y» o, más simple, "
      "«haré [CONDUCTA] a las [HORA] en [LUGAR]»; aprovecha las dos señales más comunes "
      "(tiempo y lugar) y, una vez fijada, elimina la necesidad de esperar a la inspiración o "
      "decidir en el momento; en un estudio, el 91% del grupo que la formuló hizo ejercicio "
      "frente al 35-38% de los demás.",
      [JC, "habitos", "1a-ley", "planificacion"],
      {"related": ["aku-cuatro-leyes-del-cambio-de-conducta-concept"]}),
    c("aku-mucha-gente-cree-que-le-falta-motivacion-cuando-le-falta-claridad-claim", "claim",
      "Mucha gente cree que le falta motivación cuando lo que le falta es claridad: no es obvio "
      "cuándo ni dónde actuar, así que se queda esperando «el momento adecuado»; ser específico "
      "sobre qué quieres y cómo lo lograrás (vía implementation intention) convierte intenciones "
      "difusas («quiero entrenar más») en un plan de acción concreto y además ayuda a decir no "
      "a lo que te desvía.",
      [JC, "habitos", "claridad", "motivacion"]),
    c("aku-efecto-diderot-y-encadenamiento-de-conductas-concept", "concept",
      "El efecto Diderot es la tendencia de que obtener una posesión nueva desencadene una "
      "espiral de consumo que lleva a compras adicionales (Diderot y su bata escarlata); "
      "incluye el principio más general de que ninguna conducta ocurre aislada: a menudo "
      "decides qué hacer a continuación según lo que acabas de terminar, de modo que cada "
      "acción se convierte en la señal (cue) que dispara la siguiente; implica que esa "
      "conectividad puede usarse a favor (encadenando buenos hábitos) o en contra (espirales "
      "de consumo).",
      [JC, "habitos", "consumo"],
      {"related": ["aku-no-subas-tu-tren-de-vida-al-ganar-mas-claim"]}),
    c("aku-habit-stacking-method", "method",
      "El habit stacking (apilamiento de hábitos, BJ Fogg) es una forma de implementation "
      "intention que empareja un hábito nuevo con uno actual en vez de con una hora/lugar, con "
      "la fórmula «después de [HÁBITO ACTUAL], haré [HÁBITO NUEVO]»; el reward de un hábito "
      "actúa como cue del siguiente, permitiendo encadenar varios; el secreto es elegir un cue "
      "específico, inmediatamente accionable y de la misma frecuencia que el hábito deseado, "
      "evitando disparadores ambiguos.",
      [JC, "habitos", "1a-ley", "tecnica"],
      {"related": ["aku-implementation-intention-method",
                   "aku-habit-loop-cue-craving-response-reward-concept"]}),
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
