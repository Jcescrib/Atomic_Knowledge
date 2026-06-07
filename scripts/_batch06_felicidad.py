# -*- coding: utf-8 -*-
"""Batch 06 — puentes cross-corpus FELICIDAD/MENTE/SALUD (naval/jocko/james-clear/power-mba)."""
import sys
from _audit_wire import wire
EDGES = [
 ("aku-el-deseo-es-un-contrato-para-ser-infeliz-hasta-conseguirlo-concept","related","aku-el-deseo-es-la-diferencia-entre-donde-estas-y-donde-quieres-estar-claim"),
 ("aku-felicidad-es-ausencia-de-deseo-y-presencia-en-el-momento-claim","related","aku-satisfaccion-igual-liking-menos-wanting-las-expectativas-determinan-la-satisfaccion-claim"),
 ("aku-el-sufrimiento-impulsa-el-progreso-el-deseo-de-cambiar-de-estado-mueve-a-actuar-claim","related","aku-felicidad-es-satisfaccion-el-exito-viene-de-la-insatisfaccion-claim"),
 ("aku-estimulos-supernormales-concept","related","aku-la-adaptacion-hedonica-es-mas-fuerte-en-lo-artificial-que-en-lo-natural-claim"),
 ("aku-el-autocontrol-cuesta-porque-no-es-satisfactorio-hay-que-soltar-el-deseo-no-satisfacerlo-claim","related","aku-evolucionamos-para-la-escasez-pero-vivimos-en-abundancia-claim"),
 ("aku-la-meditacion-es-ayuno-intermitente-para-la-mente-concept","related","aku-ayuno-beneficios-fisicos-y-psicologicos-method"),
 ("aku-meditacion-es-apagar-a-la-sociedad-y-escucharte-y-adopta-muchas-formas-claim","related","aku-mindfulness-concept"),
 ("aku-la-meditacion-revela-cuan-fuera-de-control-esta-tu-mente-y-en-la-separacion-hay-liberacion-claim","related","aku-mente-de-mono-concept"),
 ("aku-la-ansiedad-son-pensamientos-en-marcha-elige-la-paz-sobre-el-pensamiento-claim","related","aku-mente-mono-no-estar-presente-concept"),
 ("aku-toda-actividad-de-pantalla-resta-felicidad-claim","related","aku-minimalismo-digital-concept"),
 ("aku-tu-salud-es-la-prioridad-numero-uno-por-encima-de-todo-claim","related","aku-evaluation-health-concept"),
 ("aku-para-tener-paz-mental-primero-hay-que-tener-paz-del-cuerpo-claim","related","aku-entrenamiento-fisico-cuerpo-y-mente-claim"),
 ("aku-haz-algo-fisico-cada-dia-el-mejor-ejercicio-es-el-que-haras-cada-dia-claim","related","aku-en-el-workout-lo-importante-es-hacer-algo-y-trackear-claim"),
 ("aku-cuanto-mas-procesado-el-alimento-menos-comer-y-resta-antes-de-anadir-claim","related","aku-dieta-paleo-fuel-concept"),
 ("aku-la-grasa-sacia-el-azucar-da-hambre-y-su-combinacion-es-letal-claim","related","aku-homeostasis-glucosa-insulina-concept"),
 ("aku-autoevaluacion-cuerpo-mente-alma-concept","related","aku-evaluation-health-concept"),
]
if __name__=="__main__": wire(EDGES, dry="--dry" in sys.argv)
