# -*- coding: utf-8 -*-
"""Almanack of Naval — cierre de Learn to Love to Read + Part II Happiness
(Learning Happiness / Happiness Is Learned, hasta l.1526). Solo items NUEVOS."""
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
    # ── Learn to Love to Read (cierre) ──
    c("aku-relee-los-grandes-libros-identifica-los-tuyos-claim", "claim",
      "Más que leerlo todo, conviene releer una y otra vez los grandes libros e identificar "
      "cuáles son los grandes para ti (distintos libros hablan a distintas personas); leer no "
      "es una carrera: cuanto mejor es el libro, más despacio hay que absorberlo.",
      [N, "lectura", "aprendizaje"],
      {"related": ["aku-lee-lo-que-amas-hasta-que-ames-leer-claim"]}),
    c("aku-numero-de-libros-terminados-es-una-metrica-de-vanidad-claim", "claim",
      "El número de libros terminados es una métrica de vanidad: a medida que sabes más, dejas "
      "más libros sin terminar; conviene no sentir obligación de acabarlos, tratarlos como "
      "posts desechables (leyendo entre diez y veinte a la vez, saltando y empezando por el "
      "medio) y centrarse en conceptos nuevos con poder predictivo.",
      [N, "lectura", "habitos"]),
    c("aku-si-lo-escribieron-para-ganar-dinero-no-lo-leas-claim", "claim",
      "Si un libro fue escrito para ganar dinero, no lo leas: muchos bestsellers «pseudocientíficos» "
      "tienen un único punto y lo repiten con ejemplo tras ejemplo, así que basta captar la "
      "esencia y soltarlos.",
      [N, "lectura", "filtro"]),
    c("aku-ensenar-obliga-a-aprender-explica-lo-que-aprendes-claim", "claim",
      "Enseñar obliga a aprender: explicar a otra persona lo que has aprendido es una de las "
      "mejores prácticas para internalizar y organizar el conocimiento de lo que lees.",
      [N, "aprendizaje", "ensenanza"],
      {"related": ["aku-pensador-claro-mejor-que-listo-explica-a-un-nino-desde-los-fundamentos-claim"]}),
    c("aku-lee-los-originales-y-clasicos-para-una-base-solida-claim", "claim",
      "Para una base sólida, lee los originales y los clásicos antes que las interpretaciones "
      "actuales (Darwin antes que Dawkins; Adam Smith, Mises o Hayek antes que un comentarista): "
      "quien lee las cosas equivocadas en el orden equivocado puede ser muy leído pero poco "
      "inteligente, porque juzga las ideas nuevas sobre una base falsa; la base es crítica.",
      [N, "lectura", "fundamentos"],
      {"related": ["aku-domina-lo-basico-los-conceptos-avanzados-solo-senalan-pertenencia-claim"]}),
    c("aku-cuanto-mas-viejo-el-problema-mas-vieja-la-solucion-claim", "claim",
      "Cuanto más viejo es el problema, más vieja debe ser la solución que busques: para "
      "problemas modernos (conducir, volar) lee lo moderno, pero para problemas antiguos "
      "(salud, calma, valores, criar una familia) las soluciones antiguas suelen ser mejores, "
      "porque un libro que ha sobrevivido dos mil años ha sido filtrado por mucha gente y sus "
      "principios tienen más probabilidad de ser correctos.",
      [N, "lectura", "sabiduria"]),
    c("aku-mente-en-calma-cuerpo-sano-y-hogar-con-amor-no-se-compran-se-ganan-claim", "claim",
      "Una mente en calma, un cuerpo en forma y un hogar lleno de amor no pueden comprarse: "
      "deben ganarse; son los bienes centrales de una buena vida y ninguno se obtiene con "
      "dinero.",
      [N, "felicidad", "salud"]),
    # ── Part II: Happiness (intro + Learning Happiness) ──
    c("aku-riqueza-salud-felicidad-se-persiguen-en-ese-orden-pero-importan-al-reves-claim", "claim",
      "Las tres grandes metas de la vida son riqueza, salud y felicidad: solemos perseguirlas "
      "en ese orden, pero su importancia real es la inversa (la felicidad primero, luego la "
      "salud, y la riqueza al final).",
      [N, "felicidad", "prioridades"]),
    c("aku-la-felicidad-es-una-habilidad-que-se-aprende-concept", "concept",
      "La felicidad es una habilidad altamente personal que se aprende y cultiva con técnicas, "
      "como la forma física o la nutrición, no algo que se hereda o se elige una vez; incluye "
      "que su definición es distinta para cada persona y evoluciona con el tiempo (flow, "
      "satisfacción, contento); implica que se puede pasar deliberadamente de un 2/10 a un "
      "9/10 trabajándola.",
      [N, "felicidad", "habilidad"],
      {"related": ["aku-felicidad-es-el-estado-por-defecto-cuando-no-falta-nada-concept",
                   "aku-la-realidad-es-neutral-y-la-felicidad-es-una-eleccion-concept"]}),
    c("aku-felicidad-es-el-estado-por-defecto-cuando-no-falta-nada-concept", "concept",
      "La felicidad es el estado por defecto que aparece cuando eliminas la sensación de que "
      "algo falta en tu vida; incluye que, al no faltar nada, la mente deja de correr al pasado "
      "o al futuro y se produce un silencio interior del que nacen el contento y la felicidad; "
      "excluye depender de pensamientos positivos; implica que somos máquinas juzgadoras "
      "atrapadas en una red de deseos que rompe ese estado.",
      [N, "felicidad", "deseo"]),
    c("aku-felicidad-es-ausencia-de-deseo-y-presencia-en-el-momento-claim", "claim",
      "Para Naval la felicidad no es pensamiento positivo ni negativo, sino la ausencia de "
      "deseo —sobre todo de deseo por cosas externas— y la presencia en el momento: cuantos "
      "menos deseos tienes y más aceptas el estado actual, menos se mueve la mente y más feliz "
      "eres; aferrarse a «estoy feliz» y querer perpetuarlo te saca de la felicidad.",
      [N, "felicidad", "presente"],
      {"related": ["aku-el-deseo-y-el-ego-nublan-la-realidad-claim"]}),
    c("aku-todo-pensamiento-positivo-contiene-uno-negativo-por-dualidad-claim", "claim",
      "Todo pensamiento positivo contiene en su interior la semilla de uno negativo, y "
      "viceversa, por dualidad y polaridad (Tao Te Ching): decir «soy feliz» implica haber "
      "estado triste; por eso gran parte de la grandeza de la vida sale del sufrimiento, pues "
      "hay que ver lo negativo para aspirar a lo positivo y apreciarlo.",
      [N, "felicidad", "dualidad"]),
    c("aku-la-realidad-es-neutral-y-la-felicidad-es-una-eleccion-concept", "concept",
      "La realidad es neutral y no emite juicios —la naturaleza solo sigue leyes matemáticas y "
      "una cadena de causa y efecto, y todo es perfecto tal como es—; incluye que el mundo "
      "refleja de vuelta tus propios sentimientos y que la infelicidad solo existe en tu mente "
      "por lo que deseas; implica que la felicidad es una elección, y creer que lo es es el "
      "primer paso para trabajarla.",
      [N, "felicidad", "realidad"]),
    c("aku-la-insignificancia-del-yo-ayuda-a-la-felicidad-claim", "claim",
      "Creer en la completa insignificancia del yo ayuda mucho a la felicidad: si te creyeras "
      "lo más importante del universo, tendrías que doblegarlo entero a tu voluntad y cualquier "
      "cosa que no se conformara a tus deseos te parecería un error.",
      [N, "felicidad", "ego"],
      {"related": ["aku-el-ego-se-construye-en-las-primeras-dos-decadas-concept"]}),
    c("aku-no-te-tomes-tan-en-serio-eres-un-mono-con-un-plan-claim", "claim",
      "No te tomes tan en serio: no eres más que un mono con un plan; rebajar la "
      "autoimportancia y el peso del propio ego facilita aprender la felicidad.",
      [N, "felicidad", "ego"]),
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
