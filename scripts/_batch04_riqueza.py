# -*- coding: utf-8 -*-
"""Batch 04 — puentes cross-corpus RIQUEZA/UNIT-ECONOMICS (naval/power-mba/hormozi)."""
import sys
from _audit_wire import wire
EDGES = [
 ("aku-client-financed-acquisition-concept","related","aku-cac-payback-concept"),
 ("aku-client-financed-acquisition-concept","supports","aku-cac-payback-financia-crecimiento-claim"),
 ("aku-money-model-rompe-cash-bottleneck","supports","aku-cac-payback-financia-crecimiento-claim"),
 ("aku-ltgp-cac-3-a-1-claim","related","aku-cltv-cac-ratio-concept"),
 ("aku-payout-afiliados-tiers-concept","supported_by","aku-cltv-cac-ratio-concept"),
 ("aku-no-te-haces-rico-alquilando-tu-tiempo-debes-poseer-equity-claim","related","aku-equity-value-concept"),
 ("aku-equity-es-el-upside-deuda-es-downside-garantizado-concept","related","aku-estructura-de-capital-concept"),
 ("aku-capitalizar-interes-compuesto-method","supports","aku-juega-juegos-iterados-retornos-del-interes-compuesto-claim"),
 ("aku-capitalizar-interes-compuesto-method","supports","aku-interes-compuesto-aplica-a-relaciones-reputacion-conocimiento-claim"),
]
if __name__=="__main__": wire(EDGES, dry="--dry" in sys.argv)
