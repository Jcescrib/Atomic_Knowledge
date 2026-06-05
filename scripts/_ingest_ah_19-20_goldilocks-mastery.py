# -*- coding: utf-8 -*-
"""Atomic Habits — ch19 Goldilocks Rule (boredom) + ch20 Downside of Good Habits (mastery/review)."""
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
    c("aku-goldilocks-rule-dificultad-justo-manejable-concept", "concept",
      "La Goldilocks Rule afirma que los humanos sienten la máxima motivación trabajando en "
      "tareas justo al borde de su capacidad actual —ni demasiado fáciles (aburrimiento) ni "
      "demasiado difíciles (ansiedad)—; incluye que es la base del flow (un reto ~4% por "
      "encima de tu nivel) y se corresponde con la ley de Yerkes-Dodson; implica que, una vez "
      "establecido un hábito, hay que avanzar en pequeños incrementos para mantenerlo novedoso, "
      "atractivo y satisfactorio.",
      [JC, "habitos", "motivacion", "flow"]),
    c("aku-el-mayor-enemigo-del-exito-no-es-el-fracaso-sino-el-aburrimiento-claim", "claim",
      "El mayor enemigo del éxito no es el fracaso sino el aburrimiento: al volverse rutinarios "
      "y esperables, los hábitos dejan de deleitarnos y buscamos novedad, saltando de dieta en "
      "dieta o de plan en plan aunque el anterior funcionara (Maquiavelo: hasta quien va bien "
      "desea cambio); las recompensas variables (variable rewards, como las tragaperras) "
      "amplifican un deseo ya existente y reducen el aburrimiento, con el punto óptimo del deseo "
      "en un 50/50 entre éxito y fracaso.",
      [JC, "habitos", "aburrimiento", "novedad"]),
    c("aku-enamorate-del-aburrimiento-los-profesionales-aparecen-sin-importar-el-animo-claim", "claim",
      "Para lograr resultados notables hay que enamorarse del aburrimiento: las personas muy "
      "exitosas sienten la misma falta de motivación que cualquiera, pero encuentran la forma "
      "de presentarse pese al tedio; la diferencia entre un profesional y un amateur es que el "
      "profesional cumple el calendario y actúa aunque el ánimo no acompañe (no es un "
      "«fair-weather» nada), mientras el amateur deja que la vida lo desvíe.",
      [JC, "habitos", "disciplina", "consistencia"],
      {"related": ["aku-no-cuentes-con-motivacion-cuenta-disciplina-claim",
                   "aku-los-ganadores-son-los-tan-adictos-que-siguen-pese-a-la-utilidad-marginal-decreciente-claim"]}),
    c("aku-habitos-mas-practica-deliberada-igual-maestria-concept", "concept",
      "Los hábitos son necesarios pero no suficientes para la maestría: automatizar reduce la "
      "sensibilidad al feedback y lleva a la repetición sin pensar (tras dominar una habilidad "
      "suele haber un ligero declive), así que Mastery = Habits + Deliberate Practice; incluye "
      "que la maestría es estrechar el foco en un elemento, internalizarlo como hábito y usarlo "
      "de cimiento para avanzar a la siguiente frontera; implica un ciclo sin fin en que cada "
      "hábito desbloquea el siguiente nivel de desempeño.",
      [JC, "habitos", "maestria", "practica-deliberada"],
      {"related": ["aku-solo-se-logra-maestria-en-una-o-dos-cosas-claim",
                   "aku-agregacion-de-ganancias-marginales-concept"]}),
    c("aku-establece-un-sistema-de-reflexion-y-revision-de-tus-habitos-method", "method",
      "Para mejorar a largo plazo y no caer en la complacencia, establece un sistema de "
      "reflexión y revisión que te haga consciente de tus errores y posibles mejoras (como el "
      "Career Best Effort de Pat Riley con los Lakers, pidiendo +1% por temporada, o el "
      "decision journal de inversores); Clear usa dos: una Annual Review (qué fue bien, qué no, "
      "qué aprendí) y un Integrity Report (cuáles son mis valores, vivo conforme a ellos, cómo "
      "avanzo hacia quien quiero ser), reconectando los hábitos con la identidad.",
      [JC, "habitos", "reflexion", "mejora-continua"],
      {"related": ["aku-debes-editar-y-expandir-tu-identidad-continuamente-claim"]}),
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
