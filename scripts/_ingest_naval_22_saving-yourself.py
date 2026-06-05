# -*- coding: utf-8 -*-
"""Almanack of Naval — Saving Yourself (be yourself, care for yourself, diet, exercise,
meditation + mental strength). Solo items NUEVOS."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/naval/almanack-of-naval-ravikant/almanack-of-naval-ravikant.md"
ORIGIN = "Naval Ravikant — The Almanack of Naval Ravikant (ed. Eric Jorgenson, 2020)"
D = "2026-06-05"
N = "naval"

def c(idn, cls, st, dom, rel=None):
    return {"id": idn, "class": cls, "statement": st, "origin": ORIGIN,
            "domain": dom, "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    c("aku-salvate-a-ti-mismo-nadie-mas-te-hara-sano-ni-sabio-claim", "claim",
      "Sálvate a ti mismo: los médicos no te harán sano, los nutricionistas no te harán "
      "delgado, los profesores no te harán listo, los gurús no te darán calma, los mentores no "
      "te harán rico ni los entrenadores te pondrán en forma; en última instancia la "
      "responsabilidad es tuya.",
      ["salud", N, "responsabilidad"]),
    c("aku-eres-irremplazable-encuentra-lo-que-mas-te-necesita-claim", "claim",
      "Nadie te gana siendo tú: por la combinatoria asombrosa del ADN y la experiencia humana, "
      "no hay dos personas substituibles, así que tu meta vital es encontrar a las personas, el "
      "negocio, el proyecto o el arte que más te necesitan; no construyas checklists ni marcos "
      "de decisión basados en lo que hacen otros, porque nunca serás bueno siendo otro.",
      [N, "autenticidad", "proposito"],
      {"related": ["aku-escapa-la-competencia-mediante-autenticidad-claim"]}),
    c("aku-para-una-contribucion-original-hay-que-estar-irracionalmente-obsesionado-claim", "claim",
      "Para hacer una contribución original tienes que estar irracionalmente obsesionado con "
      "algo: solo esa intensidad desproporcionada produce trabajo verdaderamente único.",
      [N, "creatividad", "obsesion"]),
    c("aku-tu-salud-es-la-prioridad-numero-uno-por-encima-de-todo-claim", "claim",
      "La salud debe ser la prioridad número uno, por encima de la felicidad, la familia y el "
      "trabajo: primero la salud física, luego la mental, luego la espiritual, después la salud "
      "y el bienestar de la familia, y solo entonces el resto del mundo.",
      ["salud", N, "prioridades"]),
    c("aku-vivimos-en-desajuste-evolutivo-con-el-mundo-moderno-concept", "concept",
      "El mundo moderno nos aleja de cómo estamos evolucionados para vivir (desajuste "
      "evolutivo): incluye dietas para las que no evolucionamos, ejercicio de gimnasio en vez "
      "de juego, dominio del córtex visual sobre los otros sentidos, calzado y ropa constantes "
      "en vez de algo de exposición al frío, entornos demasiado estériles (hipótesis de la "
      "higiene), tribus diminutas perdidas y el móvil cada cinco minutos; implica que muchos "
      "males físicos y de ansiedad nacen de esa discrepancia.",
      ["salud", N, "evolucion", "mundo-moderno"],
      {"related": ["aku-evolucionamos-para-la-escasez-pero-vivimos-en-abundancia-claim"]}),
    c("aku-evolucionamos-para-la-escasez-pero-vivimos-en-abundancia-claim", "claim",
      "Evolucionamos para la escasez pero vivimos en la abundancia: nuestros genes siempre "
      "quieren decir que sí (al azúcar, al alcohol, a las drogas, a quedarse en la relación), "
      "así que hay una lucha constante por aprender a decir no que nuestro cuerpo no sabe "
      "ejecutar.",
      ["salud", N, "evolucion", "autocontrol"]),
    c("aku-la-grasa-sacia-el-azucar-da-hambre-y-su-combinacion-es-letal-claim", "claim",
      "La grasa dietética sacia y el azúcar dietético da hambre, y el efecto del azúcar domina "
      "al de la grasa; como en la naturaleza es rarísimo encontrar carbohidratos y grasa "
      "juntos (solo en frutas tropicales), su combinación —base de todos los postres— es letal "
      "y dispara el atracón: cualquier dieta sensata la evita.",
      ["salud", N, "dieta", "nutricion"]),
    c("aku-los-sanos-cuidan-mas-que-comen-que-cuanto-comen-claim", "claim",
      "Las personas en forma y sanas se centran mucho más en qué comen (calidad) que en cuánto "
      "(cantidad): el control de calidad es más fácil que el de cantidad y conduce a él; de "
      "hecho, ayunar (desde una base low-carb/paleo) es más fácil que el control de porciones, "
      "porque una vez el cuerpo detecta comida, anula al cerebro.",
      ["salud", N, "dieta", "ayuno"]),
    c("aku-cuanto-mas-procesado-el-alimento-menos-comer-y-resta-antes-de-anadir-claim", "claim",
      "La dieta más simple del mundo: cuanto más procesado es un alimento, menos hay que "
      "consumirlo; conviene descartar a los extremistas y cualquier alimento inventado en los "
      "últimos cientos de años, y en medicina y nutrición, restar antes que añadir.",
      ["salud", N, "dieta", "nutricion"]),
    c("aku-no-tengo-tiempo-significa-no-es-una-prioridad-claim", "claim",
      "«No tengo tiempo» es solo otra forma de decir «no es una prioridad»: si algo es tu "
      "prioridad número uno, lo harás; con una cesta difusa de diez o quince prioridades no "
      "lograrás ninguna, así que hay que decidir explícitamente qué es prioritario.",
      [N, "prioridades", "tiempo"],
      {"related": ["aku-tu-salud-es-la-prioridad-numero-uno-por-encima-de-todo-claim"]}),
    c("aku-haz-algo-fisico-cada-dia-el-mejor-ejercicio-es-el-que-haras-cada-dia-claim", "claim",
      "Para la forma física lo decisivo es hacer algo cada día; casi no importa qué sea: "
      "obsesionarse con si pesas, tenis, pilates o HIIT es perder el punto, porque el mejor "
      "ejercicio para ti es el que te entusiasma lo bastante como para hacerlo a diario.",
      ["salud", N, "ejercicio", "habitos"]),
    c("aku-elecciones-faciles-vida-dificil-elecciones-dificiles-vida-facil-claim", "claim",
      "«Elecciones fáciles, vida difícil; elecciones difíciles, vida fácil» (Jerzy Gregorek): "
      "si haces el sacrificio a corto plazo (comer bien, entrenar, ahorrar, cuidar tus valores "
      "y relaciones), tu vida a largo plazo será fácil; si tomas las opciones fáciles ahora, "
      "tu vida será mucho más dura.",
      ["salud", N, "disciplina", "largo-plazo"],
      {"related": ["aku-run-uphill-ante-un-empate-elige-el-camino-mas-doloroso-a-corto-plazo-claim"]}),
    c("aku-una-emocion-es-biologia-prediciendo-el-futuro-a-menudo-exagerada-concept", "concept",
      "Una emoción es nuestra biología evolucionada prediciendo el impacto futuro de un evento "
      "actual; incluye que en los entornos modernos suele estar exagerada o sencillamente "
      "equivocada; implica que no conviene tomar las emociones como lecturas fiables de la "
      "realidad ni decidir desde ellas.",
      [N, "emociones", "biologia"]),
    c("aku-la-respiracion-es-la-puerta-al-sistema-nervioso-autonomo-concept", "concept",
      "La respiración es uno de los pocos lugares donde el sistema nervioso autónomo se "
      "encuentra con el voluntario (es involuntaria pero también controlable), lo que la "
      "convierte en la puerta de entrada para influir en el cuerpo; incluye que respirar "
      "relajado le dice al cuerpo que está a salvo, liberando energía del forebrain hacia el "
      "hindbrain y el sistema inmune; por eso tantas prácticas de meditación se centran en el "
      "aliento.",
      [N, "meditacion", "fisiologia"]),
    c("aku-la-mayor-parte-del-sufrimiento-viene-de-la-evitacion-claim", "claim",
      "La mayor parte de nuestro sufrimiento viene de la evitación: como en la ducha fría, el "
      "sufrimiento está en entrar de puntillas, no en estar dentro; el cuerpo diciendo «tengo "
      "frío» es distinto de la mente diciéndolo, así que conviene reconocer la sensación del "
      "cuerpo, aceptarla y no sufrir mentalmente por ella, entrando de golpe antes de "
      "escuchar la voz que avisa.",
      [N, "sufrimiento", "aceptacion"]),
    c("aku-la-meditacion-es-ayuno-intermitente-para-la-mente-concept", "concept",
      "La meditación es ayuno intermitente para la mente: así como demasiado azúcar lleva a un "
      "cuerpo pesado, demasiadas distracciones llevan a una mente pesada; incluye que el tiempo "
      "a solas y sin distracción (autoexamen, journaling, meditación) resuelve lo no resuelto y "
      "te lleva de mentalmente gordo a mentalmente en forma.",
      [N, "meditacion", "mente"]),
    c("aku-choiceless-awareness-acepta-sin-juzgar-y-el-90-por-ciento-de-pensamientos-son-miedo-concept", "concept",
      "La Choiceless Awareness (atención sin elección, no enjuiciadora) consiste en aceptar el "
      "momento sin emitir juicios ni decisiones mientras haces tu vida; incluye observar los "
      "pensamientos según surgen y notar que ~90% son basados en miedo y ~10% en deseo, y que "
      "el instante en que reconoces un miedo, sin esfuerzo, este se desvanece; implica que "
      "diez o quince minutos así aquietan la mente y producen un estado pacífico y agradecido.",
      [N, "meditacion", "miedo"],
      {"related": ["aku-la-felicidad-requiere-presencia-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print("WRITTEN:", len(written))
for w in written: print("  ", os.path.relpath(w, ROOT))
ops_by_id = {}
for new_id, field, inv, tgt in cross:
    ops_by_id.setdefault(tgt, {"id": tgt, "add_rel": []})["add_rel"].append((inv, new_id))
akupatch.apply(ROOT, list(ops_by_id.values()))
print("\nPATCHED:", list(ops_by_id.keys()))
print("CROSS count:", len(cross))
