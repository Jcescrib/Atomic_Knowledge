# -*- coding: utf-8 -*-
"""Almanack of Naval — Learn Skills of Decision-Making + Collect Mental Models +
Learn to Love to Read (cierra Building Judgment / Part I). Solo items NUEVOS."""
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
    c("aku-no-hay-soluciones-permanentes-en-un-sistema-dinamico-claim", "claim",
      "En un sistema dinámico no hay soluciones permanentes: igual que Facebook o Twitter se "
      "rediseñan, las personalidades, las carreras y los equipos también necesitan rediseños "
      "periódicos; aferrarse a una identidad o solución fija deja de servir cuando el entorno "
      "cambia.",
      [N, "cambio", "identidad"]),
    c("aku-las-virtudes-clasicas-son-heuristicas-para-optimizar-el-largo-plazo-concept", "concept",
      "Las virtudes clásicas son, en el fondo, heurísticas de toma de decisiones que te hacen "
      "optimizar para el largo plazo en lugar del corto; incluye que actuar virtuosamente es "
      "elegir consistentemente la opción con mejor consecuencia diferida; implica que la ética "
      "y el buen juicio convergen en el horizonte largo.",
      [N, "etica", "decisiones"]),
    c("aku-las-conclusiones-interesadas-exigen-un-liston-mas-alto-claim", "claim",
      "Las conclusiones que te benefician (self-serving) deben superar un listón de evidencia "
      "más alto: precisamente porque el deseo de que sean ciertas sesga tu juicio, conviene "
      "exigirles más prueba que a las conclusiones neutras.",
      [N, "juicio", "sesgos"]),
    c("aku-los-sesgos-son-heuristicas-de-ahorro-de-tiempo-descartalos-en-decisiones-importantes-claim", "claim",
      "Casi todos los sesgos son heurísticas de ahorro de tiempo útiles en lo rutinario, pero "
      "para las decisiones importantes conviene descartar la memoria y la identidad y centrarse "
      "limpiamente en el problema, decidiendo en el momento sin recurrir a juicios "
      "preempaquetados.",
      [N, "sesgos", "decisiones"]),
    c("aku-honestidad-radical-mentir-a-otro-es-mentirte-a-ti-mismo-claim", "claim",
      "La honestidad radical es una vía a la libertad: en el momento en que dices a alguien "
      "algo deshonesto, te has mentido a ti mismo, empiezas a creer tu propia mentira y te "
      "desconectas de la realidad; como dijo Feynman, la persona más fácil de engañar eres tú "
      "mismo.",
      [N, "honestidad", "realidad"],
      {"related": ["aku-no-puedes-ocultarte-de-ti-mismo-tus-valores-determinan-tu-autoestima-claim"]}),
    c("aku-elogia-en-concreto-critica-en-general-method", "method",
      "Para que los egos jueguen a tu favor y no en tu contra, aplica la regla de Buffett: si "
      "criticas, no critiques a la persona sino el enfoque general o la clase de actividad; si "
      "elogias, busca a la persona que mejor ejemplifica lo que elogias y elógiala en concreto "
      "y por su nombre.",
      [N, "comunicacion", "liderazgo"]),
    c("aku-carisma-es-proyectar-confianza-y-amor-a-la-vez-concept", "concept",
      "El carisma es la capacidad de proyectar confianza y amor al mismo tiempo; incluye que "
      "casi siempre es posible ser honesto y positivo a la vez; implica que la honestidad "
      "instintiva no exige ser brusco, y que se entrena empezando ya y diciéndoselo a todo el "
      "mundo.",
      [N, "carisma", "comunicacion"]),
    c("aku-cuanto-mas-sabes-menos-diversificas-claim", "claim",
      "Cuanto más sabes, menos diversificas: el conocimiento profundo te permite concentrar "
      "apuestas en lo que entiendes de verdad, mientras que la diversificación es la respuesta "
      "racional a la ignorancia.",
      [N, "decisiones", "conocimiento"]),
    c("aku-modelos-mentales-concept", "concept",
      "Los modelos mentales son principios compactos que el cerebro —una máquina de "
      "predicción por memoria— usa para decidir; incluye que son mejores que «X pasó antes, "
      "luego X pasará» y que funcionan como punteros o mnemónicos para recuperar tu propia "
      "experiencia subyacente; excluye las citas sin experiencia detrás (que se olvidan); "
      "implica cargar la cabeza de modelos de evolución, teoría de juegos, economía y autores "
      "como Munger o Taleb.",
      [N, "modelos-mentales", "decisiones"],
      {"related": ["aku-inversion-buscar-evitar-errores-en-vez-de-acertar-concept",
                   "aku-principal-agent-problem-concept",
                   "aku-falsabilidad-sin-predicciones-falsables-no-es-ciencia-concept"]}),
    c("aku-inversion-buscar-evitar-errores-en-vez-de-acertar-concept", "concept",
      "La inversión (inversion) como modelo mental consiste en, en lugar de intentar decir qué "
      "funcionará, eliminar lo que no funcionará: el éxito va más de evitar juicios incorrectos "
      "y no cometer errores que de tener el juicio correcto; implica abordar los problemas "
      "desde su negación.",
      [N, "modelos-mentales", "inversion"]),
    c("aku-principal-agent-problem-concept", "concept",
      "El principal-agent problem es, para Naval, el problema más fundamental de la "
      "microeconomía: el principal (el dueño) se preocupa y hace un gran trabajo, mientras que "
      "el agente (quien actúa por cuenta ajena) optimiza para sí mismo y puede hacerlo mal; "
      "incluye que cuanto más pequeña es la empresa o más se ata la compensación al valor exacto "
      "creado, más se convierte a la gente en principales; implica preferir y crear principals.",
      [N, "modelos-mentales", "economia"]),
    c("aku-falsabilidad-sin-predicciones-falsables-no-es-ciencia-concept", "concept",
      "La falsabilidad es el principio más importante para cualquiera que reclame «ciencia»: si "
      "algo no hace predicciones falsables, no es ciencia; incluye que para creer que algo es "
      "verdad debe tener poder predictivo y ser falsable; implica que la macroeconomía, al no "
      "hacer predicciones falsables ni permitir contraejemplos, está corrompida como ciencia.",
      [N, "modelos-mentales", "ciencia"]),
    c("aku-las-ciencias-duras-explican-la-sociedad-evolucion-y-complejidad-claim", "claim",
      "La evolución, la termodinámica, la teoría de la información y la complejidad tienen gran "
      "poder explicativo y predictivo sobre muchos aspectos de la vida (gran parte de la "
      "sociedad moderna se explica por la evolución y la selección sexual); además, la "
      "complejidad enseña los límites de nuestro conocimiento y de nuestra capacidad de "
      "predecir, recomendando operar asumiendo la propia ignorancia.",
      [N, "modelos-mentales", "ciencia"]),
    c("aku-si-no-puedes-decidir-la-respuesta-es-no-claim", "claim",
      "Ante una decisión difícil y muy duradera (casarse, un trabajo, una casa, una ciudad, un "
      "socio), si no puedes decidir, la respuesta es no: la sociedad moderna está llena de "
      "opciones que no estamos biológicamente preparados para percibir, así que solo conviene "
      "decir que sí cuando estás muy seguro; si necesitas una hoja de pros y contras, es un no.",
      [N, "decisiones", "heuristica"]),
    c("aku-run-uphill-ante-un-empate-elige-el-camino-mas-doloroso-a-corto-plazo-claim", "claim",
      "Run uphill: si estás dividido a partes iguales en una decisión difícil, elige el camino "
      "más doloroso a corto plazo, porque tu cerebro evita el dolor inmediato empujándolo al "
      "futuro; por definición, si los dos están empatados y uno tiene dolor a corto plazo, ese "
      "tiene ganancia a largo plazo, y casi todas las ganancias de la vida vienen de sufrir a "
      "corto para cobrar a largo.",
      [N, "decisiones", "heuristica"],
      {"related": ["aku-la-direccion-importa-mas-que-la-velocidad-sobre-todo-con-leverage-claim"]}),
    c("aku-amar-leer-es-un-superpoder-vivimos-en-la-era-de-alejandria-claim", "claim",
      "El amor genuino por la lectura, cultivado, es un superpoder: vivimos en la era de "
      "Alejandría, con cada libro y conocimiento a un toque de distancia, de modo que los "
      "medios de aprendizaje son abundantes y lo escaso es el deseo de aprender.",
      [N, "lectura", "aprendizaje"]),
    c("aku-lee-lo-que-amas-hasta-que-ames-leer-claim", "claim",
      "Lee lo que amas hasta que ames leer: el camino para volverse lector es seguir el propio "
      "gusto sin que padres ni profesores prescriban qué está permitido leer, aunque sea "
      "«comida basura mental», porque el hábito y el amor por leer importan más que la calidad "
      "inicial del material.",
      [N, "lectura", "habitos"]),
    c("aku-leer-ciencia-mate-filosofia-una-hora-al-dia-te-eleva-en-siete-anos-claim", "claim",
      "Leer ciencia, matemáticas y filosofía una hora al día te situará probablemente en el "
      "escalón más alto del éxito humano en unos siete años: el efecto compuesto del "
      "aprendizaje fundacional diario es enorme.",
      [N, "lectura", "interes-compuesto"]),
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
