# -*- coding: utf-8 -*-
"""Batch 07 — resolucion §4.2: 6 pares propuestos como contradicts -> cableados RELATED.
Decision del usuario (2026-06-08): NO contradicts; conectar como related."""
import sys
from _audit_wire import wire
EDGES = [
 ("aku-willpower-no-es-finita-disciplina-engendra-disciplina-claim","related","aku-el-autocontrol-cuesta-porque-no-es-satisfactorio-hay-que-soltar-el-deseo-no-satisfacerlo-claim"),
 ("aku-precio-alto-aumenta-valor-percibido-claim","related","aku-reducir-costes-no-precio-claim"),
 ("aku-48laws-43-work-on-hearts-and-minds-concept","related","aku-no-obligar-sino-liderar-claim"),
 ("aku-48laws-07-get-others-to-do-the-work-take-credit-concept","related","aku-liderar-pares-via-influencia-y-ego-en-jaque-claim"),
 ("aku-las-personas-disciplinadas-estructuran-su-entorno-para-no-necesitar-fuerza-de-voluntad-claim","related","aku-no-cuentes-con-motivacion-cuenta-disciplina-claim"),
 ("aku-las-personas-disciplinadas-estructuran-su-entorno-para-no-necesitar-fuerza-de-voluntad-claim","related","aku-self-discipline-viene-de-dentro-concept"),
 ("aku-elige-el-campo-de-competicion-correcto-tus-genes-marcan-tus-areas-de-oportunidad-claim","related","aku-eleccion-vence-naturaleza-y-crianza-claim"),
]
if __name__=="__main__": wire(EDGES, dry="--dry" in sys.argv)
