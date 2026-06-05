# -*- coding: utf-8 -*-
"""Atomic Habits — Conclusion (keep identity small) + Little Lessons from the Four Laws.
Cierra el libro."""
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
    c("aku-manten-tu-identidad-pequena-y-flexible-para-poder-crecer-claim", "claim",
      "Cuanto más fuerte te aferras a una identidad, más difícil es crecer más allá de ella, "
      "porque la defiendes de la crítica y niegas tus puntos débiles; conviene «mantener tu "
      "identidad pequeña» (Paul Graham) y redefinirla en términos flexibles, no frágiles "
      "(«soy atleta» → «soy de los que aman un reto físico»), para que, como el agua que rodea "
      "el obstáculo, se adapte a las circunstancias cambiantes en vez de romperse (Lao Tzu: lo "
      "blando y flexible prevalece).",
      [JC, "habitos", "identidad", "adaptabilidad"],
      {"related": ["aku-debes-editar-y-expandir-tu-identidad-continuamente-claim",
                   "aku-para-ser-honesto-habla-sin-identidad-las-etiquetas-te-atan-claim"]}),
    c("aku-con-un-porque-suficientemente-grande-superas-cualquier-como-claim", "claim",
      "Con un «porqué» suficientemente grande puedes superar casi cualquier «cómo» (Nietzsche: "
      "«quien tiene un porqué para vivir puede soportar casi cualquier cómo»): si tu motivación "
      "y deseo son lo bastante grandes, actúas incluso cuando es muy difícil, porque un gran "
      "craving puede impulsar una gran acción aunque la fricción sea alta.",
      [JC, "motivacion", "proposito"],
      {"related": ["aku-tu-curriculum-real-es-tu-catalogo-de-sufrimiento-claim"]}),
    c("aku-ser-curioso-es-mejor-que-ser-listo-el-deseo-no-la-inteligencia-mueve-la-conducta-claim", "claim",
      "Ser curioso y motivado vale más que ser listo, porque lleva a la acción: la "
      "inteligencia por sí sola no produce resultados si no te hace actuar, y es el deseo, no "
      "el intelecto, lo que mueve la conducta —como dice Naval, «el truco para hacer cualquier "
      "cosa es primero cultivar un deseo por ella»—.",
      [JC, "motivacion", "deseo"],
      {"related": ["aku-la-motivacion-es-relativa-encuentra-la-cosa-en-la-que-te-metes-claim"]}),
    c("aku-system-1-vs-system-2-solo-somos-racionales-tras-ser-emocionales-concept", "concept",
      "Las emociones impulsan la conducta: el modo primario del cerebro es sentir (System 1, "
      "rápido, no consciente, optimizado para sentir y anticipar) y el secundario es pensar "
      "(System 2, lento, consciente y racional); incluye que el sentimiento (craving) llega "
      "antes que la respuesta y que solo somos racionales después de haber sido emocionales; "
      "implica que apelar a la emoción suele ser más poderoso que apelar a la razón, y que para "
      "decidir bien conviene partir de una posición emocional neutra.",
      [JC, "habitos", "emociones", "decisiones"],
      {"related": ["aku-una-emocion-es-biologia-prediciendo-el-futuro-a-menudo-exagerada-concept",
                   "aku-el-deseo-y-el-ego-nublan-la-realidad-claim"]}),
    c("aku-el-sufrimiento-impulsa-el-progreso-el-deseo-de-cambiar-de-estado-mueve-a-actuar-claim", "claim",
      "La fuente de todo sufrimiento —el deseo de cambiar de estado— es también la fuente de "
      "todo progreso: ese deseo es lo que te impulsa a actuar y lo que empuja a la humanidad a "
      "mejorar y crear; con craving estamos insatisfechos pero motivados, y sin craving "
      "satisfechos pero sin ambición.",
      [JC, "deseo", "progreso"],
      {"related": ["aku-el-deseo-es-la-diferencia-entre-donde-estas-y-donde-quieres-estar-claim",
                   "aku-todo-pensamiento-positivo-contiene-uno-negativo-por-dualidad-claim"]}),
    c("aku-tus-acciones-revelan-tus-verdaderas-motivaciones-claim", "claim",
      "Tus acciones revelan cuánto deseas algo de verdad: si repites que algo es prioridad "
      "pero nunca actúas sobre ello, en realidad no lo quieres; conviene tener una conversación "
      "honesta contigo mismo, porque la conducta —no las palabras— delata tus verdaderas "
      "motivaciones.",
      [JC, "motivacion", "accion"],
      {"related": ["aku-intenciones-no-importan-importan-las-acciones-claim"]}),
    c("aku-el-autocontrol-cuesta-porque-no-es-satisfactorio-hay-que-soltar-el-deseo-no-satisfacerlo-claim", "claim",
      "El autocontrol es difícil porque no es satisfactorio: inhibir un deseo no lo resuelve "
      "—resistir la tentación no satisface el craving, solo lo ignora y crea espacio para que "
      "pase—, así que el autocontrol exige soltar el deseo en lugar de satisfacerlo, lo que "
      "explica por qué la mera fuerza de voluntad es poco fiable a largo plazo.",
      [JC, "habitos", "autocontrol", "deseo"],
      {"related": ["aku-el-autocontrol-es-de-corto-plazo-haz-invisibles-los-cues-de-los-malos-habitos-claim"]}),
    c("aku-satisfaccion-igual-liking-menos-wanting-las-expectativas-determinan-la-satisfaccion-claim", "claim",
      "La satisfacción es liking menos wanting (Satisfaction = Liking − Wanting): el desajuste "
      "entre lo que esperas (cravings) y lo que obtienes (rewards) determina cómo de "
      "satisfecho te sientes; una experiencia media precedida de altas expectativas decepciona "
      "y la misma precedida de bajas expectativas deleita; por eso, como dijo Séneca, «ser "
      "pobre no es tener poco, es querer más»: si tus deseos superan a tus gustos, siempre "
      "estarás insatisfecho.",
      [JC, "felicidad", "expectativas", "satisfaccion"],
      {"related": ["aku-felicidad-es-ausencia-de-deseo-y-presencia-en-el-momento-claim",
                   "aku-mentalidad-relativa-y-envidia-impiden-la-riqueza-claim"]}),
    c("aku-la-esperanza-declina-con-la-experiencia-y-se-convierte-en-aceptacion-claim", "claim",
      "La esperanza declina con la experiencia y es sustituida por la aceptación: la primera "
      "vez que surge una oportunidad, tu expectativa se basa solo en la promesa; con la "
      "repetición se asienta en la realidad y la esperanza se cambia por una predicción más "
      "exacta; por eso seguimos cayendo en esquemas de hacerse-rico-rápido o adelgazar-rápido "
      "—lo nuevo ofrece esperanza ilimitada porque no hay experiencia que la ancle—.",
      [JC, "expectativas", "aceptacion"],
      {"related": ["aku-no-hay-esquemas-para-hacerse-rico-rapido-claim"]}),
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
