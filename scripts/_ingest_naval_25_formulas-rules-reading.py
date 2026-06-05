# -*- coding: utf-8 -*-
"""Almanack of Naval — Bonus: Life Formulas + Naval's Rules + Recommended Reading.
Cierra el libro. Solo items NUEVOS + 1 reference TAKU."""
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
    c("aku-formula-de-la-felicidad-de-naval-salud-riqueza-relaciones-method", "method",
      "Naval modela la felicidad como un algoritmo (notas para uno mismo, no definiciones): "
      "Happiness = Health + Wealth + Good Relationships; donde Health = Exercise + Diet + "
      "Sleep, con Exercise = entrenamiento de resistencia de alta intensidad + deportes + "
      "descanso, Diet = comida natural + ayuno intermitente + plantas, y Sleep = sin alarmas + "
      "8-9 horas + ritmos circadianos.",
      [N, "felicidad", "formula", "salud"],
      {"related": ["aku-riqueza-salud-felicidad-se-persiguen-en-ese-orden-pero-importan-al-reves-claim"]}),
    c("aku-formula-de-la-riqueza-e-ingreso-de-naval-method", "method",
      "Naval modela la riqueza como un algoritmo: Wealth = Income + Wealth × (Return on "
      "Investment); donde Income = Accountability + Leverage + Specific Knowledge; "
      "Accountability = personal branding + plataforma personal + asumir riesgo; Leverage = "
      "capital + personas + propiedad intelectual; y Return on Investment = «buy-and-hold» + "
      "valoración + margen de seguridad.",
      [N, "riqueza", "formula"],
      {"related": ["aku-armate-con-specific-knowledge-accountability-y-leverage-claim",
                   "aku-leverage-multiplicador-de-juicio-concept"]}),
    c("aku-leer-es-la-meta-habilidad-definitiva-canjeable-por-cualquier-otra-claim", "claim",
      "Leer (aprender) es la meta-habilidad definitiva y puede cambiarse por cualquier otra "
      "cosa: dominar el aprendizaje te da acceso a adquirir cualquier otra habilidad que "
      "necesites, por lo que es la inversión de mayor retorno.",
      [N, "lectura", "aprendizaje"],
      {"related": ["aku-amar-leer-es-un-superpoder-vivimos-en-la-era-de-alejandria-claim"]}),
    c("aku-el-amor-se-da-no-se-recibe-claim", "claim",
      "El amor se da, no se recibe: es una decisión y una acción que parte de ti, no algo que "
      "esperas obtener o exigir de los demás.",
      [N, "amor", "valores"]),
    c("aku-salud-amor-y-mision-en-ese-orden-nada-mas-importa-claim", "claim",
      "La jerarquía vital de Naval es salud, amor y tu misión, en ese orden: nada más importa, "
      "y ordenar así las prioridades evita sacrificar lo fundamental por lo secundario.",
      [N, "prioridades", "valores"],
      {"related": ["aku-tu-salud-es-la-prioridad-numero-uno-por-encima-de-todo-claim"]}),
]

takus = [
    {"id": "taku-naval-recommended-reading", "taku_type": "reference", "subdir": "reference",
     "title": "Lecturas recomendadas por Naval Ravikant",
     "origin": ORIGIN, "domain": [N, "lectura", "referencia"],
     "when_to_use": "Para elegir lecturas de alta calidad y fundacionales que Naval recomienda, al construir una base sólida de conocimiento.",
     "when_not_to_use": "Como lista de lectura obligatoria o de prestigio social: Naval insiste en leer lo que te engancha y en releer los grandes para ti.",
     "aku_links": {"justified_by": [
         "aku-amar-leer-es-un-superpoder-vivimos-en-la-era-de-alejandria-claim",
         "aku-lee-los-originales-y-clasicos-para-una-base-solida-claim",
         "aku-relee-los-grandes-libros-identifica-los-tuyos-claim"]},
     "created": D, "updated": D,
     "body": (
        "## Descripción\n\n"
        "Lista curada de lecturas recomendadas por Naval Ravikant, recopilada en la sección "
        "Bonus de *The Almanack of Naval Ravikant*. Sirve para orientar futuras ingestas y la "
        "construcción de una base de conocimiento de alta calidad (ciencia, filosofía, "
        "fundamentos), en línea con su consejo de leer originales y clásicos y releer los "
        "grandes libros.\n\n"
        "## Recursos\n\n"
        "Categorías de la lista original (ver detalle en la fuente "
        "`raw/libros/naval/almanack-of-naval-ravikant/almanack-of-naval-ravikant.md`, "
        "líneas ~2415-2683):\n\n"
        "- **Nonfiction** — ciencia, economía, psicología, biografías y divulgación.\n"
        "- **Philosophy and Spirituality** — incluye a los clásicos y a autores como Osho, "
        "Krishnamurti, el Tao Te Ching, etc.\n"
        "- **Science Fiction** — recomendaciones de ficción especulativa.\n"
        "- **Blogs** — blogs de referencia (p. ej. Farnam Street / fs.blog).\n"
        "- **Other Recommendations** — otros recursos.\n\n"
        "Recursos para profundizar en Naval: Navalmanack.com, nav.al, su podcast, la "
        "compilación *How to Get Rich*, e ilustraciones de Jack Butcher (VisualizeValue.com).\n\n"
        "## Cómo usar esta referencia\n\n"
        "1. Empieza por los originales y clásicos antes que por las interpretaciones modernas.\n"
        "2. Prioriza fundamentos sólidos (matemáticas básicas, hard sciences, microeconomía).\n"
        "3. Lee lo que te engancha; no sientas obligación de terminar; relee los grandes.\n"
        "4. Úsala como punto de partida para futuras fuentes a ingestar en el vault."),
    },
]

written, cross = akugen.generate(akus, takus, ROOT)
print("WRITTEN:", len(written))
for w in written: print("  ", os.path.relpath(w, ROOT))
ops_by_id = {}
for new_id, field, inv, tgt in cross:
    ops_by_id.setdefault(tgt, {"id": tgt, "add_rel": []})["add_rel"].append((inv, new_id))
akupatch.apply(ROOT, list(ops_by_id.values()))
print("\nPATCHED:", list(ops_by_id.keys()))
print("CROSS count:", len(cross))
