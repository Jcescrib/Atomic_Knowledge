# -*- coding: utf-8 -*-
"""_kolenda_integrate.py — propone puentes para AKUs Kolenda sub-conectados.

A diferencia de _audit_bridges.py (solo cross-corpus), este considera candidatos
INTRA-Kolenda (tácticas hermanas que comparten mecanismo) Y hacia el resto del
grafo. Foco: cada AKU Kolenda con grado 1-2 (sub-conectado). Solo lectura.

Para cada AKU Kolenda sub-conectado, busca otros AKUs (cualquier corpus) no ya
enlazados que comparten >=2 términos distintivos (idf-weighted, df<=40), y rankea.

Uso: python scripts/_kolenda_integrate.py [min_score] [out.json]
"""
import os, re, math, sys, json
from collections import defaultdict, Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _audit_analyze as AA
akus = AA.akus
ROOT = AA.ROOT

STOP = set("""para que con los las del una uno este esta estos estas como mas pero por sus
sobre cuando donde porque entre cada solo segun hacia desde aunque tras ante bajo sin
puede deben debe hace hacer hacen tiene tienen ser estar suele suelen mejor mejores peor
producto productos nombre nombres usuario usuarios cliente clientes precio precios
interfaz diseno disenar elemento elementos mensaje persona personas gente forma formas
efecto efectos hacerlo siempre nunca todo toda todos todas algun alguna mismo misma
tambien menos muy etc incluye implica concepto mecanismo paso pasos parte version
relacion relaciones manera modo cosa cosas momento parecer parecen parece hacen
mientras tener anadir hacer mayor menor grande grandes pequeno pequenos alto altos
numero numeros opcion opciones marca marcas empresa negocio kolenda psychology
percepcion valor aumenta reduce cuanto tanto""".split())

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

# degree + linked set
linked = defaultdict(set)
deg = defaultdict(int)
for aid, a in akus.items():
    for f in AA.AKU_FIELDS:
        for t in a["rel"][f]:
            linked[aid].add(t); linked[t].add(aid)
for aid in akus:
    deg[aid] = len(linked[aid])

MIN = float(sys.argv[1]) if len(sys.argv) > 1 else 9.0
OUT = sys.argv[2] if len(sys.argv) > 2 else None

# Kolenda under-connected (degree 1-2) are the anchors we want to integrate
anchors = [aid for aid, a in akus.items()
           if a["corpus"] == "kolenda" and deg[aid] in (1, 2)]

pairs = []
seen = set()
ids = sorted(akus)
for aid in anchors:
    a = akus[aid]
    for oid in ids:
        if oid == aid: continue
        key = tuple(sorted((aid, oid)))
        if key in seen: continue
        if oid in linked[aid]: continue
        shared = TERMS[aid] & TERMS[oid]
        if not shared: continue
        distinct = [w for w in shared if df[w] <= 40]
        if len(distinct) < 2: continue
        score = sum(idf(w) for w in distinct)
        if score >= MIN:
            seen.add(key)
            o = akus[oid]
            pairs.append(dict(
                score=round(score, 2),
                shared=sorted(distinct, key=lambda w: -idf(w))[:6],
                a_id=aid, a_corpus=a["corpus"], a_class=a["aku_class"],
                a_deg=deg[aid], a_stmt=a["statement"][:200],
                b_id=oid, b_corpus=o["corpus"], b_class=o["aku_class"],
                b_deg=deg[oid], b_stmt=o["statement"][:200],
                intra=(o["corpus"] == "kolenda")))

pairs.sort(key=lambda p: -p["score"])
print(f"Anchors Kolenda sub-conectados (grado 1-2): {len(anchors)}")
print(f"Pares candidatos (score>={MIN}, >=2 términos distintivos df<=40): {len(pairs)}")
intra = sum(1 for p in pairs if p["intra"])
print(f"  intra-Kolenda: {intra}  |  cross-corpus: {len(pairs)-intra}")
if OUT:
    json.dump(pairs, open(os.path.join(ROOT, OUT), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"Escrito: {OUT}")
else:
    for p in pairs[:80]:
        tag = "INTRA" if p["intra"] else "CROSS"
        print(f"\n[{p['score']:5.1f}] {tag} {p['a_corpus']}<>{p['b_corpus']} :: {', '.join(p['shared'])}")
        print(f"   A(d{p['a_deg']}) {p['a_id']}")
        print(f"        {p['a_stmt']}")
        print(f"   B(d{p['b_deg']}) {p['b_id']}")
        print(f"        {p['b_stmt']}")
