# -*- coding: utf-8 -*-
"""INTEGRATE pass para el cluster 48 Laws of Power: encadena las 48 leyes (related N<->N+1)
y anade puentes cross-corpus (parallels/tensiones reales con Jocko/Naval/Hormozi/32-principles)."""
import os, sys, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# id por numero de ley
def lid(n):
    import glob as g
    nn = "%02d" % n
    hits = g.glob(os.path.join(ROOT, "aku", f"aku-48laws-{nn}-*-concept.md"))
    assert len(hits) == 1, (nn, hits)
    return os.path.basename(hits[0])[:-3]

LAW = {n: lid(n) for n in range(1, 49)}

ops = []
# 1) cadena secuencial 1<->2<->...<->48 (cluster conectado, mismo sistema)
for n in range(1, 48):
    ops.append({"id": LAW[n], "add_rel": [("related", LAW[n+1])]})
    ops.append({"id": LAW[n+1], "add_rel": [("related", LAW[n])]})

# 2) puentes cross-corpus (parallels/tensiones reales nivel a/b)
CROSS = {
    1:  "aku-humildad-es-la-cualidad-mas-importante-claim",                         # deferencia (tension)
    5:  "aku-juicio-demostrado-con-credibilidad-atrae-leverage-infinito-claim",     # reputacion
    9:  "aku-intenciones-no-importan-importan-las-acciones-claim",                  # demuestra no expliques
    10: "aku-teoria-de-los-cinco-chimpances-concept",                              # entorno emocional
    16: "aku-no-subas-tu-tren-de-vida-al-ganar-mas-claim",                         # escasez/valor (debil); usa 23 mejor -> dejo entorno
    23: "aku-solo-se-logra-maestria-en-una-o-dos-cosas-claim",                     # concentrar fuerzas / foco
    25: "aku-debes-editar-y-expandir-tu-identidad-continuamente-claim",            # recrearte / identidad
    28: "aku-empezar-aqui-y-ahora-method",                                         # audacia / accion
    29: "aku-decide-despacio-actua-rapido-y-deja-que-el-acto-dure-decadas-claim",  # planificar al final
    34: "aku-para-mejorar-sin-autodisciplina-actualiza-tu-autoimagen-claim",       # actuar como rey / autoimagen
    35: "aku-grandes-personas-tienen-grandes-resultados-si-eres-paciente-claim",   # timing / paciencia
    39: "aku-no-sobrerreaccionar-mantener-la-calma-claim",                         # mantente calmado
    43: "aku-power-of-relationships-liderazgo-concept",                            # corazones y mentes (tension coercion)
    46: "aku-los-celos-son-inutiles-no-querrias-ser-otra-persona-al-100-claim",    # envidia (no parezcas perfecto)
    47: "aku-el-ego-mas-dificil-es-el-propio-claim",                               # victoria/arrogancia/ego
    48: "aku-no-hay-soluciones-permanentes-en-un-sistema-dinamico-claim",          # formlessness / adaptabilidad
}
for n, ext in CROSS.items():
    if os.path.exists(os.path.join(ROOT, "aku", ext + ".md")):
        ops.append({"id": LAW[n], "add_rel": [("related", ext)]})
        ops.append({"id": ext, "add_rel": [("related", LAW[n])]})
    else:
        print("WARN missing cross target:", ext)

akupatch.apply(ROOT, ops)
print("chained 1-48 +", len(CROSS), "cross-corpus bridges")

# limpia placeholder
fixed = 0
for p in glob.glob(os.path.join(ROOT, "aku", "*.md")):
    t = open(p, encoding="utf-8").read()
    if "<!-- sin relaciones -->" in t and re.search(r"^\*\*\w+\*\* ", t, re.M):
        lines = [l for l in t.split("\n") if l.strip() != "<!-- sin relaciones -->"]
        out = re.sub(r"\n\n\n+", "\n\n", "\n".join(lines))
        open(p, "w", encoding="utf-8", newline="\n").write(out)
        fixed += 1
print("placeholder limpiado en", fixed, "ficheros")
