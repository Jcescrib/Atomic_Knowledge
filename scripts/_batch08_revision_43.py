# -*- coding: utf-8 -*-
"""Batch 08 — resolucion §4.3: ~17 pares de solapamiento tangencial -> cableados RELATED.
Decision del usuario (2026-06-08): conectar todos como related."""
import sys
from _audit_wire import wire
EDGES = [
 ("aku-enfocar-una-iniciativa-a-la-vez-claim","related","aku-single-tasking-foco-una-tarea-claim"),
 ("aku-liderazgo-factor-mas-importante-claim","related","aku-liderazgo-concept"),
 ("aku-medida-significativa-liderazgo-claim","related","aku-liderar-vs-gestionar-concept"),
 ("aku-mejores-lideres-mision-no-ego-claim","related","aku-proposito-mision-concept"),
 ("aku-evolucion-rol-fundador-concept","related","aku-delegar-todo-para-liderar-no-pareciendo-vago-claim"),
 ("aku-evolucion-rol-fundador-concept","related","aku-negocio-sin-ti-es-activo-claim"),
 ("aku-48laws-13-appeal-to-self-interest-concept","related","aku-cialdini-reciprocidad-concept"),
 ("aku-48laws-32-play-to-peoples-fantasies-concept","related","aku-cialdini-simpatia-concept"),
 ("aku-48laws-31-control-the-options-concept","related","aku-manejar-jefe-micromanager-indeciso-debil-method"),
 ("aku-reversion-riesgo-numero-uno-claim","related","aku-palabras-frases-persuasivas-concept"),
 ("aku-urgencia-concept","related","aku-palabras-frases-persuasivas-concept"),
 ("aku-emocion-prevalece-razon-claim","related","aku-dream-outcome-concept"),
 ("aku-azucar-es-adictivo-como-droga-claim","related","aku-estimulos-supernormales-concept"),
 ("aku-regla-100-no-80-20-claim","related","aku-el-autocontrol-cuesta-porque-no-es-satisfactorio-hay-que-soltar-el-deseo-no-satisfacerlo-claim"),
 ("aku-la-esperanza-declina-con-la-experiencia-y-se-convierte-en-aceptacion-claim","related","aku-no-hay-esquemas-para-hacerse-rico-rapido-claim"),
 ("aku-felicidad-es-paz-no-alegria-paz-en-reposo-y-felicidad-en-movimiento-concept","related","aku-the-warpath-concept"),
 ("aku-toda-actividad-de-pantalla-resta-felicidad-claim","related","aku-el-entorno-es-la-mano-invisible-que-moldea-la-conducta-claim"),
 ("aku-wealth-activos-que-ganan-mientras-duermes-concept","related","aku-cltv-minus-cac-concept"),
 ("aku-lead-magnet-reduce-cac-claim","related","aku-cac-concept"),
]
if __name__=="__main__": wire(EDGES, dry="--dry" in sys.argv)
