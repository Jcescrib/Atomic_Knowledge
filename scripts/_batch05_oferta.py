# -*- coding: utf-8 -*-
"""Batch 05 — puentes cross-corpus OFERTA/VALOR/COPY (hormozi/power-mba/kolenda)."""
import sys
from _audit_wire import wire
EDGES = [
 ("aku-value-equation-concept","related","aku-ecuacion-valor-claim"),
 ("aku-effort-sacrifice-concept","related","aku-coste-percibido-amplio-concept"),
 ("aku-focus-bottom-value-equation-claim","supports","aku-reducir-costes-no-precio-claim"),
 ("aku-costes-ocultos-oferta-gratis-claim","related","aku-coste-percibido-amplio-concept"),
 ("aku-perceived-likelihood-achievement-concept","related","aku-copy-aportar-pruebas-claim"),
 ("aku-dream-outcome-concept","related","aku-cosas-importantes-concept"),
 ("aku-status-driver-compra-claim","related","aku-vete-a-beneficios-ultimos-claim"),
 ("aku-cta-hormozi-concept","related","aku-cta-concept"),
 ("aku-cta-hormozi-concept","related","aku-copy-incluir-cta-claim"),
 ("aku-siete-componentes-headline-concept","related","aku-formulas-titulos-potentes-concept"),
 ("aku-callout-cocktail-party-claim","related","aku-copy-incluir-titular-claim"),
 ("aku-lead-magnet-hormozi-concept","related","aku-lead-magnet-concept"),
 ("aku-lead-contactable-hormozi-concept","related","aku-lead-concept"),
 ("aku-affiliate-hormozi-concept","related","aku-recomendacion-vs-viralizacion-concept"),
 ("aku-grand-slam-offer-concept","related","aku-innovacion-valor-concept"),
 ("aku-constraint-mayor-drop-off-claim","related","aku-cuello-botella-funnel-concept"),
 ("aku-reason-why-aumenta-accion-claim","supports","aku-palabras-frases-persuasivas-concept"),
]
if __name__=="__main__": wire(EDGES, dry="--dry" in sys.argv)
