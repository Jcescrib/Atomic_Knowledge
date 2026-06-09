# -*- coding: utf-8 -*-
"""_bridge_apply_b.py — cablea como `related` las propuestas nivel (b) del workflow.
Lee {b:[{a_id,b_id,reason}]}, valida ids, dedup, salta self/ya-enlazados/inexistentes.
Uso: python scripts/_bridge_apply_b.py <verdicts.json> [--apply]
"""
import os, sys, json, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire
import _audit_analyze as AA

ids = set(AA.akus)
linked = {}
for aid, a in AA.akus.items():
    s = set()
    for f in AA.AKU_FIELDS:
        for t in a["rel"][f]: s.add(t)
    linked[aid] = s

data = json.load(open(sys.argv[1], encoding="utf-8"))
apply = "--apply" in sys.argv
seen = set(); edges = []; drop = 0
for v in data.get("b", []):
    x, y = v.get("a_id"), v.get("b_id")
    if not x or not y or x == y or x not in ids or y not in ids: drop += 1; continue
    if y in linked.get(x, set()): drop += 1; continue
    k = tuple(sorted([x, y]))
    if k in seen: continue
    seen.add(k); edges.append((x, "related", y))
print(f"nivel (b): {len(data.get('b', []))} veredictos -> {len(edges)} aristas validas ({drop} descartadas)")
if apply and edges:
    wire(edges)
elif edges:
    print("(dry-run; usa --apply)")
