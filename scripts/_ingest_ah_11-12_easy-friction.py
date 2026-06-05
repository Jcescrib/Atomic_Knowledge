# -*- coding: utf-8 -*-
"""Atomic Habits — ch11 Walk Slowly (motion vs action) + ch12 Law of Least Effort (3ª Ley)."""
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
    c("aku-motion-vs-action-concept", "concept",
      "Hay una diferencia clave entre estar en movimiento (motion) y pasar a la acción "
      "(action): el movimiento es planificar, estrategizar y aprender —se siente como "
      "progreso— pero no produce resultado; la acción es la conducta que entrega el resultado "
      "(no es hablar con el entrenador, es entrenar); incluye que solemos quedarnos en "
      "movimiento para retrasar el fracaso y evitar el juicio; implica que para dominar un "
      "hábito hay que empezar por la repetición, no por la perfección: «get your reps in».",
      [JC, "habitos", "3a-ley", "accion"],
      {"related": ["aku-impaciencia-con-las-acciones-paciencia-con-los-resultados-claim",
                   "aku-haz-algo-fisico-cada-dia-el-mejor-ejercicio-es-el-que-haras-cada-dia-claim"]}),
    c("aku-los-habitos-se-forman-por-frecuencia-no-por-tiempo-claim", "claim",
      "Los hábitos se forman por frecuencia (número de repeticiones), no por el tiempo "
      "transcurrido: no hay nada mágico en «21 días»; la repetición produce automaticidad vía "
      "long-term potentiation —«las neuronas que se activan juntas se conectan juntas» (Hebb)— "
      "y cambios físicos en el cerebro (más materia gris/hipocampo según el uso); hay que "
      "encadenar suficientes repeticiones exitosas hasta cruzar la «Habit Line».",
      [JC, "habitos", "automaticidad", "repeticion"],
      {"related": ["aku-habito-concept"]}),
    c("aku-ley-del-minimo-esfuerzo-concept", "concept",
      "La Law of Least Effort (ley del mínimo esfuerzo) sostiene que, entre dos opciones "
      "similares, la gente gravita hacia la que requiere menos trabajo: el cerebro está "
      "cableado para conservar energía, así que la conducta que se realiza es la que entrega "
      "más valor por el menor esfuerzo; incluye que no quieres el hábito en sí sino el "
      "resultado que entrega, y cada hábito es un obstáculo (fricción) hacia ese resultado; "
      "implica hacer los buenos hábitos tan fáciles que los hagas incluso sin ganas.",
      [JC, "habitos", "3a-ley", "esfuerzo"],
      {"related": ["aku-camino-de-menor-resistencia-claim"]}),
    c("aku-reduce-la-friccion-para-hacer-el-buen-habito-el-camino-de-menor-resistencia-method", "method",
      "Para crear buenos hábitos, reduce la fricción que los rodea (y auméntala para los "
      "malos): «addition by subtraction» (como la lean production japonesa que eliminó "
      "movimiento desperdiciado); diseña el entorno para que la acción correcta sea el camino "
      "de menor resistencia —pon el gimnasio en tu ruta, quita la curva de la manguera en vez "
      "de bombear más agua— y mete fricción en los malos (desenchufa la tele, deja el móvil en "
      "otra habitación).",
      [JC, "habitos", "3a-ley", "friccion", "entorno"],
      {"related": ["aku-disena-tu-entorno-se-su-arquitecto-no-su-victima-method"]}),
    c("aku-prime-tu-entorno-para-el-uso-futuro-method", "method",
      "Prepara («prime») tu entorno para el uso futuro: al organizar un espacio para su "
      "propósito previsto, haces fácil la siguiente acción («resetear la habitación» de "
      "Nuckols —dejar todo en su sitio listo para la próxima vez—, sacar la ropa de deporte la "
      "noche antes, cortar fruta el finde); es ser «proactivamente perezoso», y también vale "
      "invertido para dificultar lo malo.",
      [JC, "habitos", "3a-ley", "entorno"],
      {"related": ["aku-habits-scorecard-method"]}),
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
