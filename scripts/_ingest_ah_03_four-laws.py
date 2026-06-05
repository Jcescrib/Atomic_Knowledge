# -*- coding: utf-8 -*-
"""Atomic Habits — ch3 How to Build Better Habits in 4 Simple Steps (habit loop + 4 Laws)."""
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
    c("aku-habito-concept", "concept",
      "Un hábito es una conducta repetida las veces suficientes como para volverse automática; "
      "incluye ser una solución fiable a problemas recurrentes del entorno y un atajo mental "
      "(la memoria de los pasos que antes resolvieron el problema), que reduce la carga "
      "cognitiva y libera atención consciente; se forma por trial-and-error (try, fail, learn, "
      "try differently) hasta automatizarse; implica que su propósito último es resolver los "
      "problemas de la vida con el mínimo esfuerzo.",
      [JC, "habitos", "automaticidad"],
      {"related": ["aku-habit-loop-cue-craving-response-reward-concept"]}),
    c("aku-los-habitos-crean-libertad-no-la-restringen-claim", "claim",
      "Los hábitos no restringen la libertad, la crean: quienes no tienen sus hábitos resueltos "
      "son los que menos libertad tienen (siempre luchando por el siguiente dólar, sin energía "
      "o por detrás); al automatizar los fundamentos de la vida, liberas el espacio mental "
      "necesario para el pensamiento libre, la creatividad y los nuevos retos.",
      [JC, "habitos", "libertad"]),
    c("aku-habit-loop-cue-craving-response-reward-concept", "concept",
      "El habit loop es el ciclo de retroalimentación neurológico de cuatro pasos por el que "
      "operan todos los hábitos, siempre en el mismo orden: cue (señal que predice una "
      "recompensa y dispara la conducta), craving (anhelo: la fuerza motivacional), response "
      "(la conducta ejecutada) y reward (la recompensa que satisface el anhelo y queda asociada "
      "a la señal); incluye dos fases —problema (cue+craving) y solución (response+reward)—; "
      "implica que si falla cualquiera de los cuatro pasos el hábito no se forma ni se repite.",
      [JC, "habitos", "habit-loop"]),
    c("aku-no-anhelas-el-habito-sino-el-cambio-de-estado-interno-claim", "claim",
      "Lo que anhelas no es el hábito en sí, sino el cambio de estado interno que entrega: no "
      "ansías fumar un cigarrillo sino el alivio que da, no quieres encender la tele sino "
      "entretenerte; toda craving está ligada al deseo de cambiar tu estado interno, y las "
      "señales son neutras hasta que los pensamientos y emociones del observador las "
      "convierten en anhelo.",
      [JC, "habitos", "deseo"],
      {"related": ["aku-el-deseo-es-un-contrato-para-ser-infeliz-hasta-conseguirlo-concept"]}),
    c("aku-todo-habito-resuelve-un-problema-recurrente-con-minimo-esfuerzo-claim", "claim",
      "Toda conducta está impulsada por el deseo de resolver un problema (obtener algo bueno o "
      "aliviar un dolor), y el propósito último de los hábitos es resolver los problemas "
      "recurrentes de la vida con el mínimo de energía y esfuerzo posible; por eso el cerebro "
      "los construye: para preservar la atención consciente, que es su cuello de botella.",
      [JC, "habitos", "automaticidad"]),
    c("aku-cuatro-leyes-del-cambio-de-conducta-concept", "concept",
      "Las Cuatro Leyes del Cambio de Conducta son el framework práctico de Clear, una por "
      "cada paso del habit loop, para crear buenos hábitos: 1ª (cue) hazlo obvio, 2ª (craving) "
      "hazlo atractivo, 3ª (response) hazlo fácil, 4ª (reward) hazlo satisfactorio; incluye sus "
      "inversiones para romper malos hábitos: hazlo invisible, poco atractivo, difícil e "
      "insatisfactorio; implica que cada ley es una palanca y que basta preguntarse «¿cómo lo "
      "hago obvio/atractivo/fácil/satisfactorio?».",
      [JC, "habitos", "framework", "cuatro-leyes"],
      {"related": ["aku-habit-loop-cue-craving-response-reward-concept"]}),
]

takus = [
    {"id": "taku-cuatro-leyes-del-cambio-de-conducta", "taku_type": "framework", "subdir": "frameworks",
     "title": "Las Cuatro Leyes del Cambio de Conducta (Atomic Habits)",
     "origin": ORIGIN, "domain": [JC, "habitos", "framework"],
     "when_to_use": "Para diseñar deliberadamente un buen hábito o desmontar uno malo, ajustando las palancas de cada paso del habit loop.",
     "when_not_to_use": "Como fórmula rígida garantizada para cualquier conducta; Clear lo presenta como casi-exhaustivo, no infalible.",
     "aku_links": {"justified_by": [
         "aku-cuatro-leyes-del-cambio-de-conducta-concept",
         "aku-habit-loop-cue-craving-response-reward-concept",
         "aku-habito-concept",
         "aku-no-subes-al-nivel-de-tus-metas-caes-al-de-tus-sistemas-claim"]},
     "created": D, "updated": D,
     "body": (
        "## Summary\n\n"
        "Framework de James Clear que convierte los cuatro pasos del habit loop (cue, craving, "
        "response, reward) en cuatro palancas accionables para crear buenos hábitos, con sus "
        "inversiones para romper los malos.\n\n"
        "## Core Components\n\n"
        "**Crear un buen hábito:**\n"
        "1. **1ª Ley (Cue) — Hazlo obvio.**\n"
        "2. **2ª Ley (Craving) — Hazlo atractivo.**\n"
        "3. **3ª Ley (Response) — Hazlo fácil.**\n"
        "4. **4ª Ley (Reward) — Hazlo satisfactorio.**\n\n"
        "**Romper un mal hábito (inversión):**\n"
        "1. Hazlo invisible · 2. Hazlo poco atractivo · 3. Hazlo difícil · 4. Hazlo insatisfactorio.\n\n"
        "## How to Apply\n\n"
        "Ante cualquier conducta que quieras cambiar, pregúntate: ¿cómo la hago obvia / "
        "atractiva / fácil / satisfactoria? (o sus inversiones para eliminarla). Cada ley se "
        "despliega en tácticas concretas en los capítulos siguientes del libro.\n\n"
        "## Underlying Claims\n\n"
        "Se apoya en el habit loop de 4 pasos, en que un hábito es una solución automática a un "
        "problema recurrente, y en que caes al nivel de tus sistemas, no subes al de tus metas.\n\n"
        "## Strengths\n\n"
        "Simple, memorable y aplicable a casi cualquier dominio; mapea cada palanca a una etapa "
        "neurológica concreta; sirve igual para crear que para romper hábitos (por inversión).\n\n"
        "## Limitations and Criticisms\n\n"
        "El propio autor admite que no es un marco exhaustivo de toda conducta humana; requiere "
        "diagnóstico correcto de qué etapa falla; no aborda por sí solo conflictos de identidad "
        "profundos.\n\n"
        "## Variants and Extensions\n\n"
        "Se complementa con los hábitos basados en la identidad (capa más profunda) y con "
        "tácticas específicas por ley: habit stacking, diseño del entorno, temptation bundling, "
        "two-minute rule, habit tracking, contratos de hábitos."),
    },
]

written, cross = akugen.generate(akus, takus, ROOT)
print("WRITTEN:", len(written))
for w in written: print("  ", os.path.relpath(w, ROOT))
ops_by_id = {}
for new_id, field, inv, tgt in cross:
    ops_by_id.setdefault(tgt, {"id": tgt, "add_rel": []})["add_rel"].append((inv, new_id))
akupatch.apply(ROOT, list(ops_by_id.values()))
print("PATCHED:", list(ops_by_id.keys()))
print("CROSS:", len(cross))
