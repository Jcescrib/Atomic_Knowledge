# -*- coding: utf-8 -*-
"""Atomic Habits — ch13 Two-Minute Rule + ch14 commitment devices/automation (cierran 3ª Ley)
+ ch15 The Cardinal Rule (inicio 4ª Ley)."""
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
    c("aku-momentos-decisivos-concept", "concept",
      "Los momentos decisivos son las pocas elecciones diarias que funcionan como "
      "bifurcaciones en el camino (ponerte la ropa de deporte, pedir takeout o cocinar) y "
      "fijan las opciones disponibles para tu yo futuro; incluye que el 40-50% de las acciones "
      "diarias son habituales y que un hábito es la puerta de entrada, no el destino (el taxi, "
      "no el gimnasio), porque encarrila las decisiones conscientes que siguen; implica que "
      "dominar esos pocos momentos determina la trayectoria del día.",
      [JC, "habitos", "3a-ley", "decisiones"]),
    c("aku-two-minute-rule-method", "method",
      "La Two-Minute Rule dice que, al empezar un hábito nuevo, debe poder hacerse en menos de "
      "dos minutos: escala cualquier hábito a su versión mínima («leer» → «leer una página», "
      "«correr 5 km» → «atarme las zapatillas»), creando un «gateway habit» que te lleva por "
      "el camino productivo; el objetivo no es hacer una cosa sino dominar el hábito de "
      "presentarte (showing up) y «estandarizar antes de optimizar»; luego se escala con habit "
      "shaping.",
      [JC, "habitos", "3a-ley", "tecnica"],
      {"related": ["aku-empezar-aqui-y-ahora-method",
                   "aku-cada-accion-es-un-voto-por-el-tipo-de-persona-que-quieres-ser-claim"]}),
    c("aku-commitment-device-method", "method",
      "Un commitment device (dispositivo de compromiso) es una elección que haces en el "
      "presente para controlar tus acciones futuras —fijar buenos hábitos y restringir los "
      "malos— (Victor Hugo encerró su ropa para escribir; pedir media ración para llevar antes "
      "de comer; pagar el yoga por adelantado); funciona como inversión de la 3ª Ley (make it "
      "difficult): cambia la tarea para que cueste más salir del buen hábito que empezarlo.",
      [JC, "habitos", "3a-ley", "compromiso"],
      {"related": ["aku-comprometete-externamente-para-cambiar-o-fija-una-meta-menor-honesta-method"]}),
    c("aku-automatiza-tus-habitos-con-tecnologia-y-decisiones-unicas-method", "method",
      "La forma definitiva de fijar la conducta futura es automatizar los hábitos en vez de "
      "confiar en la fuerza de voluntad del momento: las decisiones únicas (one-time actions) "
      "—comprar un buen colchón, plan de ahorro automático, filtro de agua, quitar la tele del "
      "dormitorio— exigen un poco de esfuerzo inicial y rinden retornos crecientes; la "
      "tecnología (como la caja registradora que volvió imposible robar) puede hacer "
      "inevitables los buenos hábitos e imposibles los malos, aunque también puede volverse "
      "en contra (autoplay).",
      [JC, "habitos", "3a-ley", "automatizacion"],
      {"related": ["aku-disena-tu-entorno-se-su-arquitecto-no-su-victima-method"]}),
    c("aku-cardinal-rule-lo-recompensado-se-repite-lo-castigado-se-evita-concept", "concept",
      "La Regla Cardinal del cambio de conducta (4ª Ley: hazlo satisfactorio) es: lo que se "
      "recompensa se repite, lo que se castiga se evita; incluye que las emociones positivas "
      "cultivan hábitos y las negativas los destruyen (el jabón Safeguard que olía bien volvió "
      "habitual lavarse las manos en Karachi); excluye recompensas tardías como motor de "
      "repetición; implica que, mientras las tres primeras leyes hacen que la conducta se "
      "ejecute esta vez, la cuarta hace que se repita la próxima, cerrando el habit loop.",
      [JC, "habitos", "4a-ley", "recompensa"],
      {"related": ["aku-habit-loop-cue-craving-response-reward-concept",
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
