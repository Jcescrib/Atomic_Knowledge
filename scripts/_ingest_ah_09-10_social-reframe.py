# -*- coding: utf-8 -*-
"""Atomic Habits — ch9 Family/Friends (social norms) + ch10 Causes of Bad Habits (reframing).
Cierran la 2ª Ley."""
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
    # ── ch9 social norms ──
    c("aku-imitamos-los-habitos-de-tres-grupos-cercanos-muchos-poderosos-concept", "concept",
      "Como animales de manada que ansían pertenecer, imitamos los hábitos de tres grupos: los "
      "cercanos (familia y amigos —cuanto más próximos, más copiamos), los muchos (la tribu) y "
      "los poderosos (quienes tienen estatus y prestigio, a quienes copiamos para ganarlo); "
      "incluye que una conducta es atractiva cuando nos ayuda a encajar; implica que la cultura "
      "en que vives determina qué conductas te resultan atractivas —«lo normal» fija tus "
      "expectativas—.",
      [JC, "habitos", "2a-ley", "normas-sociales"],
      {"related": ["aku-teoria-de-los-cinco-chimpances-concept",
                   "aku-al-trabajar-rodeate-de-mas-exitosos-al-jugar-de-mas-felices-claim"]}),
    c("aku-unete-a-una-cultura-donde-tu-conducta-deseada-sea-lo-normal-method", "method",
      "Una de las cosas más eficaces para construir mejores hábitos es unirte a una cultura "
      "donde (1) tu conducta deseada sea la conducta normal y (2) ya tengas algo en común con "
      "el grupo: ver a otros hacerlo a diario vuelve el hábito alcanzable, y nada sostiene la "
      "motivación como pertenecer a la tribu, porque la identidad compartida («somos lectores/"
      "músicos/ciclistas») refuerza la personal y embebe el cambio a largo plazo.",
      [JC, "habitos", "2a-ley", "entorno-social"]),
    c("aku-la-conducta-normal-de-la-tribu-vence-a-la-deseada-del-individuo-claim", "claim",
      "La conducta normal de la tribu suele vencer a la conducta deseada del individuo: en el "
      "experimento de Asch, ~75% de los sujetos cedió a una respuesta obviamente incorrecta del "
      "grupo; la recompensa de ser aceptado pesa más que tener razón, así que la mayoría de los "
      "días preferimos equivocarnos con la multitud que acertar en solitario, y nadar contra la "
      "cultura exige esfuerzo extra.",
      [JC, "habitos", "conformidad"],
      {"related": ["aku-casi-todo-lo-que-se-lee-busca-aprobacion-social-los-retornos-estan-fuera-del-rebano-claim"]}),
    # ── ch10 reframing / where cravings come from ──
    c("aku-cada-conducta-tiene-un-craving-de-superficie-y-un-motivo-profundo-concept", "concept",
      "Cada conducta tiene un craving de superficie y un motivo subyacente más profundo: los "
      "hábitos son soluciones modernas a deseos antiguos (conservar energía, obtener comida y "
      "agua, hallar amor y reproducirse, vincularse, ganar aceptación social, reducir "
      "incertidumbre, lograr estatus); incluye que productos adictivos (Tinder, Facebook, "
      "Instagram, Google, videojuegos) no crean motivación nueva sino que se enganchan a esos "
      "motivos; implica que un mismo motivo admite muchas soluciones, así que tu hábito actual "
      "no es necesariamente la mejor.",
      [JC, "habitos", "deseo", "motivos"],
      {"related": ["aku-el-deseo-es-un-contrato-para-ser-infeliz-hasta-conseguirlo-concept"]}),
    c("aku-la-causa-de-tus-habitos-es-la-prediccion-que-los-precede-claim", "claim",
      "La causa real de tus hábitos es la predicción que los precede: la vida se siente "
      "reactiva pero es predictiva —cada acción va precedida de una predicción sobre qué hacer—, "
      "y tu conducta depende de cómo interpretas los eventos, no de su realidad objetiva; el "
      "mismo cue (un cigarrillo) dispara un buen o mal hábito según tu predicción, así que "
      "reprogramar la predicción cambia el hábito.",
      [JC, "habitos", "prediccion", "interpretacion"],
      {"related": ["aku-el-cerebro-es-una-maquina-de-prediccion-que-codifica-cues-claim"]}),
    c("aku-el-deseo-es-la-diferencia-entre-donde-estas-y-donde-quieres-estar-claim", "claim",
      "El deseo (craving) es la sensación de que algo falta: la diferencia entre tu estado "
      "actual y el estado en que quieres estar; cuando comes compulsivamente, fumas o miras "
      "redes, lo que de verdad quieres no es la patata frita ni los likes, sino sentirte "
      "distinto; ese gap entre el estado presente y el deseado es la razón para actuar, y sin "
      "emociones (que marcan las cosas como buenas, malas o indiferentes) perderíamos la "
      "capacidad de decidir.",
      [JC, "habitos", "deseo"],
      {"related": ["aku-no-anhelas-el-habito-sino-el-cambio-de-estado-interno-claim"]}),
    c("aku-reencuadra-tus-habitos-de-have-to-a-get-to-method", "method",
      "Para hacer atractivo un hábito difícil, reencuádralo destacando sus beneficios en vez de "
      "sus costes: cambia «tengo que» (have to) por «consigo» (get to) —ambas versiones son "
      "ciertas, pero eliges la que te sirve—, reinterpreta los nervios como adrenalina útil, el "
      "ahorro como libertad futura, las distracciones al meditar como práctica; y crea un "
      "motivation ritual asociando el hábito a algo que disfrutas (música, una rutina) hasta "
      "que ese cue dispare por sí solo el estado deseado.",
      [JC, "habitos", "2a-ley", "reencuadre"],
      {"related": ["aku-good-mindset-concept",
                   "aku-deja-de-preguntar-por-que-y-empieza-a-decir-wow-gratitud-por-la-abundancia-claim"]}),
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
