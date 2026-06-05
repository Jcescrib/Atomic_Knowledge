# -*- coding: utf-8 -*-
"""Atomic Habits — ch8 How to Make a Habit Irresistible (2nd Law: dopamine + temptation bundling)."""
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
    c("aku-estimulos-supernormales-concept", "concept",
      "Un estímulo supernormal es una versión exagerada de la realidad que provoca una "
      "respuesta más fuerte de lo normal (Tinbergen: las crías de gaviota picotean más fuerte "
      "un pico de cartón con tres puntos rojos grandes que el real); incluye que el cerebro "
      "humano, evolucionado para la escasez, cae ante versiones hiperexageradas modernas "
      "—comida basura (sal/azúcar/grasa, bliss point, dynamic contrast), redes sociales, "
      "porno, publicidad—; implica que cuanto más atractiva es una oportunidad, más adictiva "
      "se vuelve, y que las tentaciones futuras serán aún más concentradas.",
      [JC, "habitos", "2a-ley", "deseo"],
      {"related": ["aku-la-lucha-moderna-individuos-vs-ejercitos-que-explotan-la-abundancia-concept"]}),
    c("aku-los-habitos-son-un-bucle-de-retroalimentacion-de-dopamina-claim", "claim",
      "Los hábitos son un bucle de retroalimentación impulsado por dopamina: toda conducta muy "
      "adictiva (drogas, comida basura, videojuegos, redes) se asocia a niveles altos de "
      "dopamina, y sin dopamina muere el deseo (ratas sin dopamina dejan de querer comer aunque "
      "aún disfruten el sabor: distinción entre «wanting» y «liking»); el cerebro dedica mucho "
      "más circuito a querer (wanting) que a gustar (liking), porque el deseo es el motor de "
      "la conducta.",
      [JC, "habitos", "dopamina"],
      {"related": ["aku-habit-loop-cue-craving-response-reward-concept"]}),
    c("aku-la-dopamina-se-libera-al-anticipar-la-recompensa-no-solo-al-recibirla-claim", "claim",
      "La dopamina se libera no solo al experimentar el placer sino al anticiparlo: el adicto "
      "al juego tiene el pico de dopamina justo antes de apostar, no al ganar; es la "
      "anticipación de la recompensa —no su obtención— la que nos mueve a actuar, y como el "
      "mismo sistema cerebral se activa al anticipar y al recibir, anticipar algo suele sentar "
      "mejor que conseguirlo.",
      [JC, "habitos", "dopamina", "anticipacion"],
      {"related": ["aku-no-anhelas-el-habito-sino-el-cambio-de-estado-interno-claim"]}),
    c("aku-temptation-bundling-method", "method",
      "El temptation bundling (emparejamiento de tentaciones) hace un hábito más atractivo "
      "vinculando una acción que QUIERES hacer con una que NECESITAS hacer (p. ej. solo ver "
      "Netflix mientras pedaleas en la bici estática); se apoya en el principio de Premack "
      "—las conductas más probables refuerzan a las menos probables— y se puede combinar con "
      "el habit stacking: «después de [hábito actual] haré [hábito que necesito]; después de "
      "[hábito que necesito] haré [hábito que quiero]».",
      [JC, "habitos", "2a-ley", "tecnica"],
      {"related": ["aku-habit-stacking-method",
                   "aku-cuatro-leyes-del-cambio-de-conducta-concept"]}),
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
