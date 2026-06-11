# -*- coding: utf-8 -*-
"""_kol_reconnect.py — reconecta AKUs Kolenda sub-conectados (grado<=2) a sus mejores
hermanos del MISMO libro por solape de terminos distintivos. Evita singletons sueltos.

Uso: python scripts/_kol_reconnect.py dry|apply [max_deg=2] [topk=3] [min_score=5.0]
"""
import sys, os, re, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _audit_analyze as AA
import _audit_wire as W
from collections import defaultdict, Counter

mode = sys.argv[1] if len(sys.argv) > 1 else "dry"
MAXDEG = int(sys.argv[2]) if len(sys.argv) > 2 else 2
TOPK = int(sys.argv[3]) if len(sys.argv) > 3 else 3
MINSC = float(sys.argv[4]) if len(sys.argv) > 4 else 5.0

ids = set(AA.akus)
adj = defaultdict(set)
for x, d in AA.akus.items():
    for f in AA.AKU_FIELDS:
        for t in d["rel"][f]:
            if t in ids: adj[x].add(t); adj[t].add(x)

def book(a):
    for s in AA.akus[a]["sources"]:
        m = re.search(r"raw/libros/kolenda/([^/]+)/", s)
        if m: return m.group(1)
    return None

STOP = set("para que con los las del una uno este esta estos estas como mas pero por sus sobre cuando donde porque entre cada solo segun hacia desde aunque tras ante bajo sin puede deben debe hace hacer hacen tiene tienen ser estar suele suelen mejor mejores peor producto productos cliente clientes precio precios persona personas gente forma formas efecto efectos hacerlo siempre nunca todo toda todos todas algun alguna mismo misma tambien menos muy etc incluye implica excluye concepto mecanismo paso pasos parte version relacion relaciones manera modo cosa cosas momento parece parecen hacen mientras tener anadir mayor menor grande grandes pequeno pequenos numero numeros opcion opciones marca empresa negocio valor aumenta reduce cuanto tanto nombre nombres usuario usuarios diseno mensaje kolenda psychology percepcion".split())
WORD = re.compile(r"[a-záéíóúñ]{5,}")
kol = [a for a in ids if AA.akus[a]["corpus"] == "kolenda"]
TER = {a: set(w for w in WORD.findall((AA.akus[a]["statement"] + " " + " ".join(AA.akus[a]["domain"])).lower()) if w not in STOP) for a in kol}
df = Counter()
for a in kol:
    for w in TER[a]: df[w] += 1
N = len(kol)
idf = lambda w: math.log((N + 1) / (df[w] + 1))
bk = {a: book(a) for a in kol}
bybook = defaultdict(list)
for a in kol: bybook[bk[a]].append(a)

HUBWORDS = None
low = [a for a in kol if len(adj[a]) <= MAXDEG]
edges = []
seen = set()
proposals = {}
for a in low:
    cands = []
    for b in bybook[bk[a]]:
        if b == a or b in adj[a]: continue
        sh = [w for w in (TER[a] & TER[b]) if df[w] <= 30]
        if len(sh) < 2: continue
        sc = sum(idf(w) for w in sh)
        if sc >= MINSC:
            cands.append((sc, b, sh))
    cands.sort(reverse=True)
    picked = cands[:TOPK]
    proposals[a] = picked
    for sc, b, sh in picked:
        key = tuple(sorted((a, b)))
        if key in seen: continue
        seen.add(key)
        edges.append((a, "related", b))

print(f"Kolenda grado<=2: {len(low)} | aristas propuestas: {len(edges)}")
still = [a for a in low if not proposals[a]]
print(f"Sin candidato (quedarian sueltos): {len(still)}")
for a in still: print("   x", a)

if mode == "dry":
    show = sys.argv[5:] if len(sys.argv) > 5 else low[:18]
    for a in show:
        if a not in proposals: continue
        print(f"\n{a} [{bk[a]}] (deg {len(adj[a])})")
        for sc, b, sh in proposals[a]:
            print(f"   ->({sc:.1f}) {b}  [{','.join(sh[:4])}]")
elif mode == "apply":
    W.wire(edges)
    print(f"APLICADO: {len(edges)} aristas.")
