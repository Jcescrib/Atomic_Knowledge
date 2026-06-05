# -*- coding: utf-8 -*-
"""Atomic Habits — ch2 How Your Habits Shape Your Identity."""
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
    c("aku-tres-capas-del-cambio-de-conducta-concept", "concept",
      "El cambio de conducta ocurre en tres capas (como una cebolla): cambiar los outcomes "
      "(resultados — lo que obtienes), cambiar los processes (procesos/hábitos — lo que "
      "haces) y cambiar la identity (identidad/creencias — lo que crees); incluye que las tres "
      "son útiles y que el problema no es cuál es mejor sino la dirección del cambio; implica "
      "que lo duradero parte de la capa más profunda, la identidad.",
      [JC, "habitos", "identidad"],
      {"related": ["aku-habitos-basados-en-la-identidad-vs-en-resultados-concept"]}),
    c("aku-habitos-basados-en-la-identidad-vs-en-resultados-concept", "concept",
      "Los hábitos basados en resultados (outcome-based) empiezan por lo que quieres lograr, "
      "mientras que los basados en la identidad (identity-based) empiezan por quién deseas "
      "llegar a ser; incluye que la dirección recomendada es identity-based (de dentro afuera: "
      "identidad→procesos→resultados); excluye fijar metas sin tocar las creencias que las "
      "sostienen; implica que la motivación intrínseca máxima es cuando el hábito pasa a ser "
      "parte de tu identidad («soy un lector», no «quiero leer un libro»).",
      [JC, "habitos", "identidad"],
      {"related": ["aku-para-mejorar-sin-autodisciplina-actualiza-tu-autoimagen-claim"]}),
    c("aku-el-cambio-de-conducta-duradero-es-cambio-de-identidad-claim", "claim",
      "El verdadero cambio de conducta es cambio de identidad: puedes empezar un hábito por "
      "motivación, pero solo lo mantienes cuando pasa a formar parte de quién eres; la "
      "conducta incongruente con el yo no perdura, así que sin cambiar la creencia subyacente "
      "las mejoras son solo temporales.",
      [JC, "habitos", "identidad"]),
    c("aku-tu-identidad-emerge-de-tus-habitos-claim", "claim",
      "Tu identidad emerge de tus hábitos: no naces con creencias prefijadas, sino que las "
      "aprendes por experiencia, y tus hábitos son cómo encarnas («embody») tu identidad "
      "—la palabra identidad viene de essentitas (ser) e identidem (repetidamente): tu "
      "«ser repetido»—; cuanto más repites una conducta, más evidencia acumulas de la "
      "identidad asociada, así que construir hábitos es el proceso de convertirte en ti mismo.",
      [JC, "habitos", "identidad"],
      {"related": ["aku-te-conviertes-en-tus-habitos-y-cambiarlos-es-un-viaje-de-anos-claim"]}),
    c("aku-cada-accion-es-un-voto-por-el-tipo-de-persona-que-quieres-ser-claim", "claim",
      "Cada acción que tomas es un voto por el tipo de persona que quieres llegar a ser: "
      "ningún acto aislado transforma tus creencias, pero al acumularse los votos crece la "
      "evidencia de tu nueva identidad; no necesitas unanimidad, solo la mayoría, así que "
      "algún voto por un mal hábito no arruina la elección si ganas la mayoría de las veces.",
      [JC, "habitos", "identidad"]),
    c("aku-proceso-de-dos-pasos-para-cambiar-tu-identidad-method", "method",
      "Para cambiar tu identidad sigue dos pasos: (1) decide el tipo de persona que quieres "
      "ser (trabajando hacia atrás desde el resultado deseado: «¿quién es la persona que "
      "podría lograr esto?»), y (2) demuéstratelo con pequeñas victorias; una guía práctica es "
      "preguntarte en cada decisión «¿qué haría una persona [sana/lectora/...]?» y actuar en "
      "consecuencia hasta convertirte en ella.",
      [JC, "habitos", "identidad", "cambio"]),
    c("aku-debes-editar-y-expandir-tu-identidad-continuamente-claim", "claim",
      "Convertirte en la mejor versión de ti exige editar continuamente tus creencias y "
      "expandir tu identidad: el mayor obstáculo al cambio positivo (individual, de equipo o "
      "social) es el conflicto de identidad —resistes acciones porque «ese no soy yo»—, así "
      "que no conviene apegarse a una sola versión de uno mismo, porque el progreso requiere "
      "desaprender.",
      [JC, "habitos", "identidad"],
      {"related": ["aku-descondicionate-revisa-si-tus-habitos-aun-te-sirven-claim",
                   "aku-no-hay-soluciones-permanentes-en-un-sistema-dinamico-claim"]}),
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
