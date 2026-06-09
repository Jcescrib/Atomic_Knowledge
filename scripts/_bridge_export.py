# -*- coding: utf-8 -*-
"""_bridge_export.py — exporta candidatos de puente cross-corpus por AKU a lotes JSON.
Para CADA AKU toma sus top-K candidatos cross-corpus (no enlazados, score idf, >=2 terminos
distintivos), deduplica pares, y escribe lotes en outputs/bridges/. Cada par lleva ambos
statements para que un agente lo clasifique (a)/(b)/skip sin tocar disco.
Uso: python scripts/_bridge_export.py [min_score] [topk_per_aku] [batch_size]
"""
import os, re, math, sys, json, glob
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

MIN = float(sys.argv[1]) if len(sys.argv) > 1 else 7.0
TOPK = int(sys.argv[2]) if len(sys.argv) > 2 else 3
BATCH = int(sys.argv[3]) if len(sys.argv) > 3 else 20

ids = sorted(akus)
pair_score = {}
pair_shared = {}
for aid in ids:
    a = akus[aid]; ca = a["corpus"]
    local = []
    for oid in ids:
        if oid == aid or oid in linked[aid]: continue
        o = akus[oid]
        if o["corpus"] == ca: continue
        shared = TERMS[aid] & TERMS[oid]
        distinct = [w for w in shared if df[w] <= 50]
        if len(distinct) < 2: continue
        score = sum(idf(w) for w in distinct)
        if score >= MIN:
            local.append((score, oid, sorted(distinct, key=lambda w:-idf(w))[:6]))
    local.sort(reverse=True)
    for score, oid, sh in local[:TOPK]:
        key = tuple(sorted([aid, oid]))
        if key not in pair_score or score > pair_score[key]:
            pair_score[key] = score; pair_shared[key] = sh

pairs = sorted(pair_score.items(), key=lambda kv: -kv[1])
def trim(s, n=420): return s[:n]
out = []
for (x, y), score in pairs:
    out.append({
        "a_id": x, "a_corpus": akus[x]["corpus"], "a_class": akus[x]["aku_class"], "a_stmt": trim(akus[x]["statement"]),
        "b_id": y, "b_corpus": akus[y]["corpus"], "b_class": akus[y]["aku_class"], "b_stmt": trim(akus[y]["statement"]),
        "shared": pair_shared[(x, y)], "score": round(score, 1),
    })

outdir = os.path.join(ROOT, "outputs", "bridges")
os.makedirs(outdir, exist_ok=True)
for f in glob.glob(os.path.join(outdir, "batch*.json")): os.remove(f)
batches = [out[i:i+BATCH] for i in range(0, len(out), BATCH)]
paths = []
for i, b in enumerate(batches):
    p = os.path.join(outdir, f"batch{i:03d}.json")
    json.dump(b, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    paths.append(f"outputs/bridges/batch{i:03d}.json")
print(f"pares unicos: {len(out)} | lotes: {len(batches)} (batch_size={BATCH})")
print(json.dumps(paths))
