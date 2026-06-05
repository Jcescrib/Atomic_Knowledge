# -*- coding: utf-8 -*-
"""Atomic Habits — ch18 The Truth About Talent (genes, personality, choosing the right game)."""
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
    c("aku-elige-el-campo-de-competicion-correcto-tus-genes-marcan-tus-areas-de-oportunidad-claim", "claim",
      "El secreto para maximizar tus probabilidades de éxito es elegir el campo de competición "
      "correcto: los hábitos son más fáciles y satisfactorios cuando encajan con tus "
      "inclinaciones y capacidades naturales; los genes no determinan tu destino sino tus áreas "
      "de oportunidad («predisponen pero no predeterminan»), y el entorno decide la utilidad de "
      "tus talentos, así que conviene alinear tu ambición con tu habilidad y jugar donde las "
      "probabilidades están a tu favor (Phelps en el agua, El Guerrouj en la pista).",
      [JC, "habitos", "talento", "genes"],
      {"related": ["aku-specific-knowledge-concept",
                   "aku-encuentra-trabajo-que-se-sienta-como-juego-claim"]}),
    c("aku-construye-habitos-que-encajen-con-tu-personalidad-big-five-concept", "concept",
      "Tu personalidad —el conjunto de rasgos consistentes entre situaciones, con base "
      "genética— se describe con los Big Five: apertura a la experiencia, responsabilidad "
      "(conscientiousness), extroversión, amabilidad (agreeableness) y neuroticismo; incluye "
      "que los genes te empujan en cierta dirección sin determinarte; implica construir hábitos "
      "que encajen con tu personalidad (quien puntúa bajo en responsabilidad debe apoyarse más "
      "en el diseño del entorno) y elegir la versión de cada hábito que te dé alegría, no la "
      "más popular.",
      [JC, "habitos", "personalidad", "big-five"]),
    c("aku-explore-exploit-trade-off-method", "method",
      "Para encontrar el juego con las probabilidades a tu favor usa el explore/exploit "
      "trade-off: al principio de una actividad, explora amplio (probar muchas opciones); luego "
      "enfócate en la mejor solución hallada pero sigue experimentando un poco (≈80-90% explotar "
      "/ 10-20% explorar, como el 20% de Google); si ganas, explota; si pierdes, explora; y con "
      "más tiempo disponible, explora más. Guía la exploración con preguntas: ¿qué me resulta "
      "diversión pero a otros trabajo?, ¿qué me hace perder la noción del tiempo (flow)?, ¿dónde "
      "obtengo mayores retornos que la media?, ¿qué me sale natural?",
      [JC, "habitos", "talento", "estrategia"],
      {"related": ["aku-specific-knowledge-es-lo-que-hacias-sin-esfuerzo-de-nino-claim"]}),
    c("aku-cuando-no-puedes-ganar-siendo-mejor-gana-siendo-diferente-claim", "claim",
      "Cuando no puedes ganar siendo mejor, gana siendo diferente: combinando varias "
      "habilidades reduces la competencia y destacas (Scott Adams: dibujar + escribir chistes + "
      "negocio); un buen jugador se esfuerza por ganar el juego de todos, pero un gran jugador "
      "crea un juego nuevo que favorece sus fortalezas y evita sus debilidades; la "
      "especialización en una categoría estrecha permite ser el mejor aun sin el mayor talento "
      "natural.",
      [JC, "talento", "especializacion", "competencia"],
      {"related": ["aku-escapa-la-competencia-mediante-autenticidad-claim",
                   "aku-categoria-de-uno-concept",
                   "aku-se-el-mejor-del-mundo-redefiniendo-lo-que-haces-claim"]}),
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
