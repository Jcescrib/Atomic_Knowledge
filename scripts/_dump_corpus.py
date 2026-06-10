# -*- coding: utf-8 -*-
"""_dump_corpus.py — vuelca los AKUs de un corpus agrupados por fuente, empaquetados
en chunks (sin partir una fuente) para reparto a subagentes de particion.

Uso: python scripts/_dump_corpus.py <corpus> [chunk_max=85]
Escribe outputs/_dump_<corpus>/chunk_NN.json (array de {id,class,statement,source}).
"""
import os, sys, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _audit_analyze as AA
from collections import defaultdict

corpus = sys.argv[1]
CMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 85

def source_slug(a):
    for s in AA.akus[a]["sources"]:
        m = re.search(r"raw/(?:cursos|libros)/[^/]+/([^/]+)/", s)
        if m:
            return m.group(1)
        m = re.search(r"raw/([^/]+)/", s)
        if m:
            return m.group(1)
    return "misc"

bys = defaultdict(list)
for a in AA.akus:
    if AA.akus[a]["corpus"] == corpus:
        bys[source_slug(a)].append(a)

# pack whole sources into chunks <= CMAX (a source bigger than CMAX is its own chunk)
sources = sorted(bys.items(), key=lambda x: -len(x[1]))
chunks, cur = [], []
cur_n = 0
for slug, lst in sources:
    if cur and cur_n + len(lst) > CMAX:
        chunks.append(cur); cur, cur_n = [], 0
    cur.extend((slug, a) for a in lst); cur_n += len(lst)
if cur:
    chunks.append(cur)

outdir = os.path.join(AA.ROOT, "outputs", f"_dump_{corpus}")
os.makedirs(outdir, exist_ok=True)
for i, ch in enumerate(chunks):
    data = [{"id": a, "class": AA.akus[a]["aku_class"],
             "statement": AA.akus[a]["statement"][:240], "source": slug}
            for slug, a in ch]
    json.dump(data, open(os.path.join(outdir, f"chunk_{i:02d}.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"  chunk_{i:02d}: {len(ch)} AKUs ({len(set(s for s,_ in ch))} fuentes)")
print(f"{corpus}: {sum(len(v) for v in bys.values())} AKUs en {len(chunks)} chunks, {len(bys)} fuentes")
