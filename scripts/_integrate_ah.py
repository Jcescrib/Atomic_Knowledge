# -*- coding: utf-8 -*-
"""INTEGRATE pass para el cluster Atomic Habits: enruta cada AKU aislado a un hub
tematico con related bidireccional, eliminando huerfanos."""
import os, sys, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MAP = {
  "aku-anade-placer-inmediato-al-buen-habito-para-cerrar-la-brecha-temporal-claim": "aku-cardinal-rule-lo-recompensado-se-repite-lo-castigado-se-evita-concept",
  "aku-cada-accion-es-un-voto-por-el-tipo-de-persona-que-quieres-ser-claim": "aku-habitos-basados-en-la-identidad-vs-en-resultados-concept",
  "aku-construye-habitos-que-encajen-con-tu-personalidad-big-five-concept": "aku-elige-el-campo-de-competicion-correcto-tus-genes-marcan-tus-areas-de-oportunidad-claim",
  "aku-el-cambio-de-conducta-duradero-es-cambio-de-identidad-claim": "aku-habitos-basados-en-la-identidad-vs-en-resultados-concept",
  "aku-el-castigo-inmediato-reduce-el-mal-habito-claim": "aku-cardinal-rule-lo-recompensado-se-repite-lo-castigado-se-evita-concept",
  "aku-el-cerebro-es-una-maquina-de-prediccion-que-codifica-cues-claim": "aku-habit-loop-cue-craving-response-reward-concept",
  "aku-el-mayor-enemigo-del-exito-no-es-el-fracaso-sino-el-aburrimiento-claim": "aku-enamorate-del-aburrimiento-los-profesionales-aparecen-sin-importar-el-animo-claim",
  "aku-goldilocks-rule-dificultad-justo-manejable-concept": "aku-habitos-mas-practica-deliberada-igual-maestria-concept",
  "aku-la-vision-es-el-mayor-catalizador-de-la-conducta-claim": "aku-disena-tu-entorno-se-su-arquitecto-no-su-victima-method",
  "aku-las-adicciones-pueden-disolverse-al-cambiar-radicalmente-el-entorno-claim": "aku-el-contexto-es-el-cue-un-espacio-un-uso-concept",
  "aku-ley-de-goodhart-cuando-una-medida-se-vuelve-objetivo-deja-de-ser-buena-claim": "aku-habit-tracker-no-rompas-la-cadena-method",
  "aku-los-habitos-crean-libertad-no-la-restringen-claim": "aku-habito-concept",
  "aku-momentos-decisivos-concept": "aku-two-minute-rule-method",
  "aku-mucha-gente-cree-que-le-falta-motivacion-cuando-le-falta-claridad-claim": "aku-implementation-intention-method",
  "aku-no-hay-buenos-ni-malos-habitos-solo-habitos-efectivos-claim": "aku-habito-concept",
  "aku-plateau-of-latent-potential-valley-of-disappointment-concept": "aku-los-habitos-son-el-interes-compuesto-de-la-mejora-personal-claim",
  "aku-pointing-and-calling-eleva-la-consciencia-de-un-habito-method": "aku-el-cambio-de-conducta-siempre-empieza-con-la-consciencia-claim",
  "aku-proceso-de-dos-pasos-para-cambiar-tu-identidad-method": "aku-habitos-basados-en-la-identidad-vs-en-resultados-concept",
  "aku-todo-habito-resuelve-un-problema-recurrente-con-minimo-esfuerzo-claim": "aku-habito-concept",
  "aku-tus-resultados-son-una-medida-rezagada-de-tus-habitos-claim": "aku-no-subes-al-nivel-de-tus-metas-caes-al-de-tus-sistemas-claim",
  "aku-unete-a-una-cultura-donde-tu-conducta-deseada-sea-lo-normal-method": "aku-imitamos-los-habitos-de-tres-grupos-cercanos-muchos-poderosos-concept",
}

ops = []
for iso, hub in MAP.items():
    assert os.path.exists(os.path.join(ROOT, "aku", iso + ".md")), iso
    assert os.path.exists(os.path.join(ROOT, "aku", hub + ".md")), hub
    ops.append({"id": iso, "add_rel": [("related", hub)]})
    ops.append({"id": hub, "add_rel": [("related", iso)]})
akupatch.apply(ROOT, ops)
print("integrados:", len(MAP))

# limpia placeholder obsoleto
fixed = 0
for p in glob.glob(os.path.join(ROOT, "aku", "*.md")):
    t = open(p, encoding="utf-8").read()
    if "<!-- sin relaciones -->" in t and re.search(r"^\*\*\w+\*\* ", t, re.M):
        lines = [l for l in t.split("\n") if l.strip() != "<!-- sin relaciones -->"]
        out = re.sub(r"\n\n\n+", "\n\n", "\n".join(lines))
        open(p, "w", encoding="utf-8", newline="\n").write(out)
        fixed += 1
print("placeholder limpiado en", fixed, "ficheros")
