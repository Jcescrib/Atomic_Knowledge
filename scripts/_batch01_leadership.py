# -*- coding: utf-8 -*-
"""Batch 01 — puentes cross-corpus LIDERAZGO (jocko/power-mba/hormozi). Caso testigo."""
import sys
from _audit_wire import wire
EDGES = [
 ("aku-mind-control-controla-tu-propia-mente-concept","supports","aku-autoliderazgo-prerequisito-claim"),
 ("aku-self-discipline-viene-de-dentro-concept","supports","aku-autoliderazgo-prerequisito-claim"),
 ("aku-mind-control-controla-tu-propia-mente-concept","supports","aku-tres-capas-liderazgo-concept"),
 ("aku-disciplina-se-extiende-a-todo-claim","supports","aku-autoevaluacion-cuerpo-mente-alma-concept"),
 ("aku-everyone-same-everyone-different-concept","related","aku-liderazgo-situacional-concept"),
 ("aku-liderazgo-indirecto-supera-al-directo-claim","related","aku-liderazgo-situacional-concept"),
 ("aku-estilos-autoritario-delegativo-concept","related","aku-dar-ordenes-solo-commanders-intent-claim"),
 ("aku-no-obligar-sino-liderar-claim","supports","aku-liderazgo-concept"),
 ("aku-lideres-nacen-y-se-hacen-claim","supports","aku-aprende-nuevas-habilidades-liderazgo-claim"),
 ("aku-lider-compensa-debilidades-con-el-equipo-claim","related","aku-complementar-habilidades-equipo-claim"),
 ("aku-document-demonstrate-duplicate-concept","related","aku-entrenamiento-realismo-fundamentos-repeticion-method"),
]
if __name__=="__main__": wire(EDGES, dry="--dry" in sys.argv)
