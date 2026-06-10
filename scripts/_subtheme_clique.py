# -*- coding: utf-8 -*-
"""_subtheme_clique.py — entrelaza (clique related) los AKUs de cada sub-tema.

Input: uno o varios JSON de particion en outputs/, cada uno un dict
       { "<sub-tema>": ["aku-id", ...], ... }
Para cada sub-tema con >=2 miembros, anade aristas `related` entre TODOS los pares
de miembros que no esten ya enlazados (cualquier campo). Sync 3-capas via wire().

Uso:
  python scripts/_subtheme_clique.py dry  outputs/_part_kolenda/*.json
  python scripts/_subtheme_clique.py apply outputs/_part_kolenda/*.json
"""
import os, sys, glob, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _audit_wire as W
import _audit_analyze as AA

ROOT = AA.ROOT
ids = set(AA.akus)
mode = sys.argv[1] if len(sys.argv) > 1 else "dry"

# linked actual (cualquier campo) para no duplicar
linked = {a: set() for a in ids}
for aid, a in AA.akus.items():
    for f in AA.AKU_FIELDS:
        for t in a["rel"][f]:
            if t in ids:
                linked[aid].add(t); linked[t].add(aid)

patterns = sys.argv[2:]
files = []
for p in patterns:
    files.extend(glob.glob(p))
parts = {}
for fp in files:
    d = json.load(open(fp, encoding="utf-8"))
    for k, v in d.items():
        parts.setdefault(k, [])
        parts[k].extend(v)

edges, seen, badids, skipped_subt = [], set(), set(), 0
for sub, members in parts.items():
    members = [m for m in dict.fromkeys(members)]          # dedup, keep order
    valid = [m for m in members if m in ids]
    for m in members:
        if m not in ids:
            badids.add(m)
    if len(valid) < 2:
        skipped_subt += 1
        continue
    for i in range(len(valid)):
        for j in range(i + 1, len(valid)):
            a, b = valid[i], valid[j]
            key = tuple(sorted((a, b)))
            if key in seen:
                continue
            if b in linked[a]:                              # ya enlazados
                continue
            seen.add(key)
            edges.append((a, "related", b))

print(f"Sub-temas: {len(parts)} (saltados <2 validos: {skipped_subt}) | aristas nuevas: {len(edges)}")
if badids:
    print(f"IDs inexistentes ignorados: {len(badids)}")
    for b in list(badids)[:15]:
        print("   -", b)

if mode == "dry":
    for sub, members in list(parts.items())[:40]:
        v = [m for m in members if m in ids]
        print(f"  [{len(v):2d}] {sub}")
elif mode == "apply":
    if edges:
        W.wire(edges)
    print(f"APLICADO: {len(edges)} aristas related.")
