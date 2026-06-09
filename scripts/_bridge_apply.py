# -*- coding: utf-8 -*-
"""_bridge_apply.py — aplica los veredictos del workflow de vetado de puentes.
Lee un JSON {a:[{a_id,b_id,reason}], b:[{a_id,b_id,reason}]}.
- Nivel (a): cablea como `related` (valida ids, dedup, salta self/ya-enlazados/inexistentes).
- Nivel (b): vuelca a outputs/bridges/proposals_b.md para aprobacion humana.
Uso: python scripts/_bridge_apply.py <verdicts.json> [--apply]
"""
import os, sys, json, glob, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire

ids = set(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(ROOT, "aku", "*.md")))

# linked sets (para dedup)
import _audit_analyze as AA
linked = {}
for aid, a in AA.akus.items():
    s = set()
    for f in AA.AKU_FIELDS:
        for t in a["rel"][f]: s.add(t)
    linked[aid] = s

def norm_pair(x, y): return tuple(sorted([x, y]))

def main():
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    apply = "--apply" in sys.argv
    a = data.get("a", []); b = data.get("b", [])
    # nivel (a): validar + dedup
    seen = set(); edges = []; dropped = []
    for v in a:
        x, y = v.get("a_id"), v.get("b_id")
        if not x or not y or x == y: dropped.append((x, y, "self/empty")); continue
        if x not in ids or y not in ids: dropped.append((x, y, "id inexistente")); continue
        if y in linked.get(x, set()): dropped.append((x, y, "ya enlazado")); continue
        k = norm_pair(x, y)
        if k in seen: continue
        seen.add(k); edges.append((x, "related", y))
    print(f"nivel (a): {len(a)} veredictos -> {len(edges)} aristas validas ({len(dropped)} descartadas)")
    # informe nivel (b)
    rep = os.path.join(ROOT, "outputs", "bridges", "proposals_b.md")
    bseen = set(); brows = []
    for v in b:
        x, y = v.get("a_id"), v.get("b_id")
        if not x or not y or x == y: continue
        if x not in ids or y not in ids: continue
        if y in linked.get(x, set()): continue
        k = norm_pair(x, y)
        if k in bseen: continue
        bseen.add(k); brows.append((x, y, v.get("reason", "")))
    with open(rep, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(f"# Propuestas de puente nivel (b) — conceptuales, requieren aprobacion\n\n")
        fh.write(f"Total: {len(brows)} pares unicos (no ya enlazados).\n\n")
        for x, y, r in brows:
            fh.write(f"- [ ] `{x}` ↔ `{y}`\n      - {r}\n")
    print(f"nivel (b): {len(brows)} propuestas -> {rep}")
    if apply and edges:
        wire(edges)
    elif edges:
        print("(dry-run; usa --apply para cablear nivel a)")

if __name__ == "__main__":
    main()
