# -*- coding: utf-8 -*-
"""_audit_bridges.py — propone puentes CROSS-CORPUS candidatos en TODO el grafo.
Para cada par de AKUs de corpus distintos, no ya enlazados, que comparten terminos
conceptuales distintivos (idf-weighted), calcula un score. Deduplica pares y rankea.
Solo lectura. Uso: python scripts/_audit_bridges.py [min_score] [top_n]
"""
import os, re, math, sys
from collections import defaultdict, Counter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _audit_analyze as AA
akus = AA.akus

STOP = set("""para que con los las del una uno este esta estos estas como mas pero por sus
sobre cuando donde porque entre cada solo segun hacia desde aunque tras ante bajo sin
puede deben debe hace hacer hacen tiene tienen ser estar suele suelen mejor mejores peor
producto productos nombre nombres usuario usuarios cliente clientes precio precios
interfaz diseno disenar elemento elementos mensaje persona personas gente forma formas
efecto efectos hacerlo siempre nunca todo toda todos todas algun alguna mismo misma
tambien menos muy etc incluye implica concepto mecanismo paso pasos parte version
relacion relaciones manera modo cosa cosas momento parecer parecen parece hacen
mientras tener anadir hacer mayor menor grande grandes pequeno pequenos alto altos
numero numeros opcion opciones marca marcas empresa negocio""".split())

WORD = re.compile(r"[a-záéíóúñ]{5,}")
def terms(a):
    t = (a["statement"] + " " + " ".join(a["domain"])).lower()
    return set(w for w in WORD.findall(t) if w not in STOP)

df = Counter(); TERMS = {}
for aid, a in akus.items():
    ts = terms(a); TERMS[aid] = ts
    for w in ts: df[w] += 1
N = len(akus)
def idf(w): return math.log((N+1)/(df[w]+1))

linked = defaultdict(set)
for aid, a in akus.items():
    for f in AA.AKU_FIELDS:
        for t in a["rel"][f]:
            linked[aid].add(t); linked[t].add(aid)

MIN = float(sys.argv[1]) if len(sys.argv) > 1 else 6.0
TOPN = int(sys.argv[2]) if len(sys.argv) > 2 else 200

ids = sorted(akus)
pairs = []
seen = set()
for i, aid in enumerate(ids):
    a = akus[aid]; ca = a["corpus"]
    for oid in ids[i+1:]:
        o = akus[oid]
        if o["corpus"] == ca: continue          # CROSS-CORPUS only
        if oid in linked[aid]: continue
        shared = TERMS[aid] & TERMS[oid]
        if not shared: continue
        distinct = [w for w in shared if df[w] <= 50]
        if len(distinct) < 2: continue           # exige >=2 terminos distintivos
        score = sum(idf(w) for w in distinct)
        if score >= MIN:
            pairs.append((score, aid, ca, oid, o["corpus"], sorted(distinct, key=lambda w:-idf(w))[:6]))

pairs.sort(reverse=True)
print(f"Pares cross-corpus candidatos (score>={MIN}, >=2 terminos distintivos): {len(pairs)}")
print(f"Mostrando top {min(TOPN,len(pairs))}:\n")
for score, aid, ca, oid, cb, sh in pairs[:TOPN]:
    print(f"[{score:4.1f}] {ca} <> {cb} :: {', '.join(sh)}")
    print(f"      {aid}")
    print(f"      {oid}")
