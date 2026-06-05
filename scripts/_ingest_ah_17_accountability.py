# -*- coding: utf-8 -*-
"""Atomic Habits — ch17 How an Accountability Partner Can Change Everything (inversion 4ª Ley)."""
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
    c("aku-el-castigo-inmediato-reduce-el-mal-habito-claim", "claim",
      "El dolor es un maestro eficaz: cuanto más inmediato y costoso es el castigo de una "
      "conducta, más rápido se aprende a evitarla (la inversión de la 4ª Ley: make it "
      "unsatisfying); para que funcione, la fuerza del castigo debe igualar la de la conducta "
      "a corregir y debe aplicarse de forma fiable, y cuanto más local, tangible, concreta e "
      "inmediata sea la consecuencia, más cambia la conducta —al contrario que las "
      "consecuencias globales, vagas y diferidas—.",
      [JC, "habitos", "4a-ley", "castigo"]),
    c("aku-habit-contract-y-accountability-partner-method", "method",
      "Para volver un mal hábito doloroso en el momento, crea un habit contract: un acuerdo "
      "verbal o escrito donde declaras tu compromiso con un hábito y el castigo si no cumples, "
      "firmado por uno o dos accountability partners (como las leyes son un contrato social que "
      "el grupo hace cumplir); incluso sin contrato formal, tener un accountability partner "
      "añade un coste inmediato a la inacción —saber que alguien observa motiva, porque no "
      "quieres que te vean poco fiable o vago, fallándote a ti y a otros—.",
      [JC, "habitos", "4a-ley", "compromiso"],
      {"related": ["aku-comprometete-externamente-para-cambiar-o-fija-una-meta-menor-honesta-method",
                   "aku-accountability-bajo-tu-nombre-concept"]}),
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
