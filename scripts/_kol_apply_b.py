# -*- coding: utf-8 -*-
"""_kol_apply_b.py — aplica las (b) que sobrevivieron la verificacion adversarial. Temporal."""
import os, sys, glob, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _audit_wire as W
import _audit_analyze as AA

ROOT = AA.ROOT
ids = set(AA.akus)
PAIR = W.PAIR
mode = sys.argv[1] if len(sys.argv) > 1 else "dry"

rows = []
for p in sorted(glob.glob(os.path.join(ROOT, "outputs", "_kol_vfull", "vbres_*.json"))):
    rows.extend(json.load(open(p, encoding="utf-8")))

real = [r for r in rows if r.get("real") is True]
print(f"Verificadas: {len(rows)} | reales: {len(real)} | refutadas: {len(rows)-len(real)}")

edges, seen, skipped = [], set(), 0
for r in real:
    src, dst, field = r.get("src"), r.get("dst"), r.get("field") or "related"
    if field not in PAIR:
        field = "related"
    if src not in ids or dst not in ids or src == dst:
        continue
    key = tuple(sorted((src, dst)))
    if key in seen:
        continue
    if any(dst in AA.akus[src]["rel"][f] for f in AA.AKU_FIELDS):  # ya enlazados
        skipped += 1
        continue
    seen.add(key)
    edges.append((src, field, dst))

from collections import Counter
print(f"Aristas (b) verificadas a aplicar: {len(edges)} (ya-enlazadas saltadas: {skipped})")
print("  por campo:", dict(Counter(f for _, f, _ in edges)))

if mode == "dry":
    for s, f, d in edges[:25]:
        print(f"  {s} --{f}--> {d}")
elif mode == "apply":
    W.wire(edges)
    print("APLICADO.")
