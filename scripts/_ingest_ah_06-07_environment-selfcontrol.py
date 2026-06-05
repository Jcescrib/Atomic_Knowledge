# -*- coding: utf-8 -*-
"""Atomic Habits — ch6 Environment + ch7 The Secret to Self-Control (cierran 1ª Ley)."""
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
    # ── ch6 Environment ──
    c("aku-el-entorno-es-la-mano-invisible-que-moldea-la-conducta-claim", "claim",
      "El entorno es la mano invisible que moldea la conducta humana: a menudo elegimos "
      "productos no por lo que son sino por dónde están, y bajo ciertas condiciones "
      "ambientales surgen las mismas conductas pese a personalidades distintas; la forma más "
      "común de cambio no es interna sino externa (nos cambia el mundo que nos rodea), porque "
      "todo hábito es dependiente del contexto —Behavior = f(Person, Environment), Kurt Lewin—.",
      [JC, "habitos", "entorno"],
      {"related": ["aku-teoria-de-los-cinco-chimpances-concept"]}),
    c("aku-la-vision-es-el-mayor-catalizador-de-la-conducta-claim", "claim",
      "La visión es la habilidad sensorial humana más poderosa (≈10 de los 11 millones de "
      "receptores y hasta la mitad de los recursos cerebrales), por lo que las señales "
      "visuales son el mayor catalizador de la conducta: un pequeño cambio en lo que ves puede "
      "producir un gran cambio en lo que haces, así que conviene vivir y trabajar en entornos "
      "llenos de cues productivos y vacíos de los improductivos.",
      [JC, "habitos", "vision", "cue"]),
    c("aku-disena-tu-entorno-se-su-arquitecto-no-su-victima-method", "method",
      "Para crear buenos hábitos, diseña tu entorno haciendo obvios los cues de la conducta "
      "deseada en vez de ser su víctima: saca a la vista lo que quieres hacer (la fruta en un "
      "bol en la encimera, la guitarra en medio del salón, el pastillero junto al grifo), "
      "siembra múltiples disparadores del buen hábito por tu espacio y haz que la mejor opción "
      "sea la más obvia; sé el arquitecto de tu mundo, no su mero consumidor.",
      [JC, "habitos", "entorno", "diseño"],
      {"related": ["aku-sistemas-no-metas-disena-tu-entorno-para-tener-exito-concept"]}),
    c("aku-el-contexto-es-el-cue-un-espacio-un-uso-concept", "concept",
      "Con el tiempo un hábito deja de asociarse a un único cue y se asocia a todo el contexto "
      "que rodea la conducta (el contexto se convierte en el cue); incluye que nuestra "
      "conducta no la definen los objetos sino nuestra relación con ellos, por lo que conviene "
      "la regla «un espacio, un uso» —cada hábito con su sitio— y no mezclar contextos; "
      "implica que es más fácil construir un hábito nuevo en un entorno nuevo (sin cues "
      "antiguos en competencia) y que un entorno estable y predecible facilita hábitos "
      "estables.",
      [JC, "habitos", "contexto"]),
    # ── ch7 The Secret to Self-Control ──
    c("aku-las-adicciones-pueden-disolverse-al-cambiar-radicalmente-el-entorno-claim", "claim",
      "Las adicciones pueden disolverse casi de un día para otro si cambia radicalmente el "
      "entorno: el estudio de los soldados de Vietnam mostró que ~9 de cada 10 adictos a la "
      "heroína dejaron la adicción al volver a casa (5% recayó en un año), frente al ~90% de "
      "recaída del adicto típico que vuelve a su barrio con los cues de siempre; esto desafía "
      "la idea de que el mal hábito es una debilidad moral: cuando cambia el contexto, cambia "
      "el hábito.",
      [JC, "habitos", "entorno", "adiccion"]),
    c("aku-las-personas-disciplinadas-estructuran-su-entorno-para-no-necesitar-fuerza-de-voluntad-claim", "claim",
      "Las personas con más autocontrol no son muy distintas de las que luchan: simplemente "
      "estructuran su vida para no necesitar fuerza de voluntad heroica, pasando menos tiempo "
      "en situaciones tentadoras; los que mejor se autocontrolan son los que menos necesitan "
      "usarlo, así que la vía para mejorar la disciplina no es desear ser más disciplinado "
      "sino crear un entorno más disciplinado.",
      [JC, "habitos", "autocontrol", "entorno"],
      {"related": ["aku-no-cuentes-con-motivacion-cuenta-disciplina-claim"]}),
    c("aku-el-autocontrol-es-de-corto-plazo-haz-invisibles-los-cues-de-los-malos-habitos-claim", "claim",
      "El autocontrol es una estrategia de corto plazo, no de largo: puedes resistir la "
      "tentación una o dos veces, pero no vencerla siempre, y como puedes romper un hábito "
      "pero es casi imposible olvidarlo (el cue reaparece y dispara el «cue-induced wanting»), "
      "lo fiable es cortar el mal hábito en su origen reduciendo la exposición a su señal "
      "—la inversión de la 1ª Ley: hazlo invisible—, porque a largo plazo te vuelves producto "
      "de tu entorno.",
      [JC, "habitos", "autocontrol", "1a-ley"],
      {"related": ["aku-el-contexto-es-el-cue-un-espacio-un-uso-concept"]}),
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
