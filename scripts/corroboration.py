# -*- coding: utf-8 -*-
"""corroboration.py — señal de verdad por corroboración cross-source.

Para un AKU X, la corroboración = nº de FUENTES (corpus) independientes que sostienen
el mismo concepto, contando X + sus vecinos directos (depth 1) por relaciones de acuerdo
(`related`, `supports`, `supported_by`, `constrains`, `constrained_by`). `contradicts`
NO corrobora: se reporta aparte como contra-evidencia.

Uso:
  python scripts/corroboration.py <aku-id>     # corroboración de un AKU
  python scripts/corroboration.py top [N]      # AKUs mejor corroborados cross-source
  python scripts/corroboration.py term <texto> # AKUs que casan + su corroboración
"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _audit_analyze as AA
from collections import defaultdict

AGREE = ["related", "supports", "supported_by", "constrains", "constrained_by"]

nbr = defaultdict(lambda: defaultdict(set))  # aid -> {"agree": set, "contra": set}
for x, d in AA.akus.items():
    for f in AA.AKU_FIELDS:
        for t in d["rel"][f]:
            if t not in AA.akus:
                continue
            kind = "contra" if f == "contradicts" else ("agree" if f in AGREE else None)
            if kind:
                nbr[x][kind].add(t); nbr[t][kind].add(x)

def corro(aid):
    cluster = {aid} | nbr[aid]["agree"]
    corpora = {}
    for c in cluster:
        corpora.setdefault(AA.akus[c]["corpus"], []).append(c)
    contra = [(AA.akus[c]["corpus"], c) for c in nbr[aid]["contra"]]
    return corpora, contra

def truth_signal(aid):
    d = AA.akus[aid]
    corpora, contra = corro(aid)
    n = len(corpora)
    hs = ""
    # human prevails if set away from unvalidated
    return n, corpora, contra

def show(aid):
    if aid not in AA.akus:
        print("no existe:", aid); return
    d = AA.akus[aid]
    corpora, contra = corro(aid)
    print(f"{aid}")
    print(f"  {d['statement'][:160]}")
    print(f"  corroboración cross-source: {len(corpora)} fuentes -> {sorted(corpora)}")
    for c, lst in sorted(corpora.items()):
        if c != d["corpus"]:
            for x in lst:
                print(f"      · [{c}] {x}")
    if contra:
        print(f"  ⚠ contradicen ({len(contra)}): {contra}")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "top"
    if cmd == "top":
        N = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        rows = []
        for a in AA.akus:
            corpora, _ = corro(a)
            if len(corpora) >= 2:
                rows.append((len(corpora), a, sorted(corpora)))
        rows.sort(reverse=True)
        print(f"AKUs con corroboración cross-source >=2 fuentes: {len(rows)}")
        for n, a, cs in rows[:N]:
            print(f"  {n}  {a}  {cs}")
    elif cmd == "term":
        term = " ".join(sys.argv[2:]).lower()
        for a, d in AA.akus.items():
            if term in d["statement"].lower() or term in a.lower():
                show(a)
    else:
        show(cmd)
