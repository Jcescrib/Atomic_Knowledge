# -*- coding: utf-8 -*-
"""Atomic Habits — ch15 Cardinal Rule (immediate vs delayed reward) + ch16 habit tracking /
never miss twice / Goodhart (4ª Ley)."""
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
    c("aku-entorno-de-recompensa-inmediata-vs-diferida-concept", "concept",
      "El cerebro humano evolucionó en un immediate-return environment (entorno de recompensa "
      "inmediata, como la sabana) y prefiere los pagos rápidos, pero la sociedad moderna es un "
      "delayed-return environment (recompensa diferida); incluye la time inconsistency: el "
      "cerebro valora el presente más que el futuro; implica que los costes de los buenos "
      "hábitos están en el presente y sus recompensas en el futuro, y al revés en los malos "
      "—por eso cuanto más placer inmediato da una acción, más conviene cuestionar si alinea "
      "con tus metas a largo plazo—.",
      [JC, "habitos", "4a-ley", "gratificacion"],
      {"related": ["aku-run-uphill-ante-un-empate-elige-el-camino-mas-doloroso-a-corto-plazo-claim"]}),
    c("aku-anade-placer-inmediato-al-buen-habito-para-cerrar-la-brecha-temporal-claim", "claim",
      "Regla Cardinal actualizada: lo que se recompensa de inmediato se repite, lo que se "
      "castiga de inmediato se evita; como las recompensas de los buenos hábitos son diferidas, "
      "hay que añadirles un poco de placer inmediato (reinforcement: un premio al terminar) y "
      "un poco de dolor inmediato a los malos, para sentirte exitoso ya; con los hábitos de "
      "evitación, hazlos visibles (transfiere dinero a una cuenta «chaqueta» cada vez que te "
      "saltas una compra), volviendo satisfactorio el no hacer nada.",
      [JC, "habitos", "4a-ley", "refuerzo"]),
    c("aku-los-incentivos-inician-un-habito-la-identidad-lo-sostiene-claim", "claim",
      "Los incentivos inician un hábito, pero la identidad lo sostiene: las recompensas "
      "externas mantienen la motivación a corto plazo mientras llegan las intrínsecas (mejor "
      "ánimo, energía), hasta que la propia identidad se vuelve el reforzador («lo hago porque "
      "es quien soy»); por eso conviene elegir premios a corto plazo que refuercen tu identidad "
      "y no que la contradigan (un masaje, no un helado, si quieres ser una persona sana).",
      [JC, "habitos", "4a-ley", "identidad"],
      {"related": ["aku-el-cambio-de-conducta-duradero-es-cambio-de-identidad-claim"]}),
    c("aku-habit-tracker-no-rompas-la-cadena-method", "method",
      "Un habit tracker mide si hiciste un hábito (p. ej. una X en el calendario por cada día; "
      "la Paper Clip Strategy de mover un clip por cada llamada); funciona porque activa varias "
      "Leyes a la vez —es obvio (cue visual), atractivo (el progreso motiva) y satisfactorio "
      "(registrar la victoria)— y da prueba visual de los votos hacia tu identidad; el mantra "
      "es «don't break the chain» (Seinfeld). Hazlo fácil: automatiza cuando puedas, limita el "
      "registro manual a tus hábitos clave y anótalo justo al terminar (habit stacking).",
      [JC, "habitos", "4a-ley", "seguimiento"],
      {"related": ["aku-habit-stacking-method",
                   "aku-cada-accion-es-un-voto-por-el-tipo-de-persona-que-quieres-ser-claim"]}),
    c("aku-never-miss-twice-claim", "claim",
      "Regla «never miss twice»: como la perfección es imposible y la vida interrumpe, lo "
      "decisivo no es el primer fallo (un accidente) sino evitar el segundo seguido (que inicia "
      "un nuevo mal hábito); evita el ciclo todo-o-nada —el problema no es resbalar sino creer "
      "que si no puedes hacerlo perfecto mejor no lo hagas—; presentarte en los días malos "
      "(aunque hagas menos) reafirma tu identidad y, como en el interés compuesto, los días "
      "perdidos dañan más que lo que ayudan los buenos: «nunca interrumpas el compounding».",
      [JC, "habitos", "4a-ley", "resiliencia"],
      {"related": ["aku-caer-del-path-es-inevitable-lo-decisivo-es-volver-claim",
                   "aku-los-habitos-son-el-interes-compuesto-de-la-mejora-personal-claim"]}),
    c("aku-ley-de-goodhart-cuando-una-medida-se-vuelve-objetivo-deja-de-ser-buena-claim", "claim",
      "Ley de Goodhart: «cuando una medida se convierte en objetivo, deja de ser una buena "
      "medida»; como la mente quiere ganar el juego que se mide, optimizamos para lo que "
      "medimos (horas en vez de trabajo significativo, número en la báscula en vez de salud), "
      "así que medir lo equivocado produce la conducta equivocada; la medición solo sirve para "
      "guiar dentro de un sistema mayor, no para consumirte, y conviene valorar también lo "
      "difícil de cuantificar (non-scale victories).",
      [JC, "habitos", "medicion", "metricas"]),
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
