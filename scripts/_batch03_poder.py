# -*- coding: utf-8 -*-
"""Batch 03 — puentes cross-corpus PODER/INFLUENCIA (robert-greene/jocko/naval/power-mba/hormozi)."""
import sys
from _audit_wire import wire
EDGES = [
 ("aku-48laws-05-guard-your-reputation-concept","related","aku-cialdini-autoridad-concept"),
 ("aku-48laws-09-win-through-actions-not-argument-concept","related","aku-copy-aportar-pruebas-claim"),
 ("aku-48laws-04-always-say-less-than-necessary-concept","related","aku-getting-people-to-listen-deja-que-hablen-claim"),
 ("aku-48laws-13-appeal-to-self-interest-concept","related","aku-thread-of-why-conectar-al-individuo-claim"),
 ("aku-48laws-43-work-on-hearts-and-minds-concept","contradicts","aku-liderazgo-vs-manipulacion-concept"),
 ("aku-48laws-33-discover-each-mans-thumbscrew-concept","related","aku-liderazgo-vs-manipulacion-concept"),
 ("aku-48laws-16-use-absence-to-increase-respect-concept","related","aku-liderazgo-indirecto-supera-al-directo-claim"),
 ("aku-48laws-39-stir-up-waters-to-catch-fish-concept","related","aku-cuando-gritar-casi-nunca-y-calculado-claim"),
 ("aku-48laws-12-selective-honesty-to-disarm-concept","contradicts","aku-lideres-dicen-la-verdad-claim"),
 ("aku-48laws-27-play-on-need-to-believe-concept","related","aku-cialdini-pertenencia-concept"),
 ("aku-48laws-23-concentrate-your-forces-concept","related","aku-leadership-capital-concept"),
 ("aku-reason-why-aumenta-accion-claim","related","aku-enforzar-estandares-siempre-con-el-porque-claim"),
 ("aku-entender-primero-para-influir-claim","related","aku-dolor-es-el-pitch-claim"),
 ("aku-conform-to-influence-claim","related","aku-48laws-38-think-as-you-like-behave-like-others-concept"),
]
if __name__=="__main__": wire(EDGES, dry="--dry" in sys.argv)
