# -*- coding: utf-8 -*-
"""Atomic Habits — ch4 The Man Who Didn't Look Right (1st Law: Make It Obvious / awareness)."""
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
    c("aku-el-cerebro-es-una-maquina-de-prediccion-que-codifica-cues-claim", "claim",
      "El cerebro es una máquina de predicción que, al experimentar algo repetidamente, "
      "aprende a notar qué es importante, resalta las señales (cues) relevantes y las cataloga "
      "para el futuro; con suficiente práctica detectas las señales que predicen un resultado "
      "sin pensarlo conscientemente (la intuición experta del paramédico, el analista de radar "
      "o el curador de arte), y esa capacidad de notar cues es la base de todo hábito.",
      [JC, "habitos", "cue", "prediccion"]),
    c("aku-no-necesitas-ser-consciente-del-cue-para-que-un-habito-empiece-claim", "claim",
      "No necesitas ser consciente de la señal para que un hábito comience: puedes notar una "
      "oportunidad y actuar sin dedicarle atención consciente, lo que hace los hábitos útiles "
      "pero también peligrosos, porque caes en patrones viejos en piloto automático antes de "
      "darte cuenta; con el tiempo los cues se vuelven invisibles y la urgencia de actuar "
      "parece surgir de la nada.",
      [JC, "habitos", "automaticidad", "cue"],
      {"related": ["aku-habit-loop-cue-craving-response-reward-concept"]}),
    c("aku-el-cambio-de-conducta-siempre-empieza-con-la-consciencia-claim", "claim",
      "El proceso de cambio de conducta siempre empieza por la consciencia: si un hábito sigue "
      "siendo automático e inconsciente, no puedes mejorarlo; como dijo Jung, «hasta que haces "
      "consciente lo inconsciente, este dirigirá tu vida y lo llamarás destino», así que "
      "primero hay que reconocer los hábitos actuales y las señales que los disparan.",
      [JC, "habitos", "consciencia"],
      {"related": ["aku-choiceless-awareness-acepta-sin-juzgar-y-el-90-por-ciento-de-pensamientos-son-miedo-concept"]}),
    c("aku-pointing-and-calling-eleva-la-consciencia-de-un-habito-method", "method",
      "Pointing-and-Calling (señalar y nombrar en voz alta, del sistema ferroviario japonés) "
      "eleva un hábito de nivel inconsciente a consciente al obligar a usar ojos, manos, boca y "
      "oídos: el operador apunta a la señal y dice «semáforo en verde», etc.; reduce errores "
      "hasta un 85% y accidentes un 30%; aplicado a la vida personal, di en voz alta la acción "
      "que vas a tomar y su consecuencia («voy a comerme esta galleta, pero no la necesito; "
      "engordaré») para hacer reales las consecuencias.",
      [JC, "habitos", "consciencia", "tecnica"]),
    c("aku-habits-scorecard-method", "method",
      "El Habits Scorecard es un ejercicio de consciencia: lista todos tus hábitos diarios y, "
      "junto a cada uno, marca «+» si es bueno, «–» si es malo o «=» si es neutro, según su "
      "beneficio a largo plazo; el objetivo inicial no es cambiar nada sino observar lo que "
      "realmente ocurre sin juicio ni autocrítica; ante la duda, pregunta «¿esta conducta me "
      "ayuda a ser quien quiero ser?, ¿es un voto a favor o en contra de mi identidad "
      "deseada?».",
      [JC, "habitos", "consciencia", "autoevaluacion"],
      {"related": ["aku-cada-accion-es-un-voto-por-el-tipo-de-persona-que-quieres-ser-claim"]}),
    c("aku-no-hay-buenos-ni-malos-habitos-solo-habitos-efectivos-claim", "claim",
      "No hay hábitos buenos ni malos, solo hábitos efectivos (eficaces resolviendo un "
      "problema): todos te sirven de algún modo —por eso los repites—, así que conviene "
      "clasificarlos por su resultado neto a largo plazo (los buenos tienen resultado neto "
      "positivo, los malos negativo); fumar reduce el estrés ahora, pero no es sano a largo "
      "plazo.",
      [JC, "habitos", "efectividad"]),
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
