# -*- coding: utf-8 -*-
"""_merge_aku.py — fusion segura de un AKU duplicado en su canonico (cross-source).

Por cada (canonical, duplicate):
 - anade las sources[] del duplicate al canonical (dedup),
 - recomputa llm_confidence del canonical = 0.50 + 0.10*(n_sources_indep-1), cap 0.95,
 - re-apunta las relaciones del duplicate hacia el canonical (wire, manteniendo simetria),
 - marca el duplicate status: merged y lo enlaza related al canonical + nota,
 - NUNCA borra (regla del vault).

Uso: python scripts/_merge_aku.py apply outputs/_pilot/_merges.json
  donde _merges.json = [{"canonical":id,"duplicate":id,"reason":...}, ...]
"""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _audit_analyze as AA
import _audit_wire as W
import akupatch

ROOT = AA.ROOT
mode = sys.argv[1] if len(sys.argv) > 1 else "dry"
path = sys.argv[2] if len(sys.argv) > 2 else "outputs/_pilot/_merges.json"
merges = json.load(open(os.path.join(ROOT, path), encoding="utf-8"))

def reload():
    import importlib; importlib.reload(AA); return set(AA.akus)

def set_status_merged(aid, canonical):
    p = os.path.join(ROOT, "aku", aid + ".md")
    t = open(p, encoding="utf-8").read()
    if re.search(r"^status:", t, re.M):
        t = re.sub(r"^status:.*$", "status: merged", t, count=1, flags=re.M)
    else:
        # insert after 'id:' line
        t = re.sub(r"^(id:.*)$", r"\1\nstatus: merged", t, count=1, flags=re.M)
    if "merged_into:" not in t:
        t = re.sub(r"^(status: merged)$", r"\1\nmerged_into: " + canonical, t, count=1, flags=re.M)
    open(p, "w", encoding="utf-8", newline="\n").write(t)

ids = set(AA.akus)
applied = 0
for m in merges:
    can, dup = m["canonical"], m["duplicate"]
    if can not in ids or dup not in ids or can == dup:
        print("SKIP", can, dup); continue
    dsrc = AA.akus[dup]["sources"]
    csrc = set(AA.akus[can]["sources"])
    newsrc = [s for s in dsrc if s not in csrc]
    # re-apuntar relaciones del duplicate al canonico
    edges = []
    for f in AA.AKU_FIELDS:
        for tgt in AA.akus[dup]["rel"][f]:
            if tgt != can and tgt in ids:
                edges.append((can, f, tgt))
    if mode == "dry":
        print(f"MERGE {dup} -> {can} | +{len(newsrc)} sources | reapunta {len(edges)} edges")
        continue
    # 1) sources + confidence en canonico
    n_indep = len(csrc | set(dsrc))
    conf = min(0.95, 0.50 + 0.10 * (n_indep - 1))
    ops = [{"id": can, "add_source": s} for s in newsrc]
    if ops: akupatch.apply(ROOT, ops)
    akupatch.apply(ROOT, [{"id": can, "confidence": conf}])
    # 2) heredar relaciones + enlazar dup<->can
    W.wire(edges + [(dup, "related", can)])
    # 3) marcar dup como merged
    set_status_merged(dup, can)
    applied += 1
    print(f"MERGED {dup} -> {can} (conf {conf:.2f}, +{len(newsrc)} src, +{len(edges)} edges)")

if mode != "dry":
    print(f"Total fusiones: {applied}")
