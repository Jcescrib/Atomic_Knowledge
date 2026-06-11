# -*- coding: utf-8 -*-
"""_taku_rejustify.py — enlaza cada TAKU a los AKUs justificantes DEDUCIBLES:
los corroboradores CROSS-SOURCE de sus justified_by actuales (mismo mecanismo, otra fuente).

Edita aku_links.justified_by (frontmatter, link_validation: llm-proposed) + wikilink en
el cuerpo ## Relaciones (**justified_by** ← [[...]]). dry|apply. Cap por TAKU.

Uso: python scripts/_taku_rejustify.py dry|apply [cap=8]
"""
import sys, os, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _audit_analyze as AA
from collections import defaultdict

mode = sys.argv[1] if len(sys.argv) > 1 else "dry"
CAP = int(sys.argv[2]) if len(sys.argv) > 2 else 8

AGREE = {"related", "supports", "supported_by", "constrains", "constrained_by"}
agree = defaultdict(set)
for x, d in AA.akus.items():
    for f in AA.AKU_FIELDS:
        if f in AGREE:
            for t in d["rel"][f]:
                if t in AA.akus:
                    agree[x].add(t); agree[t].add(x)
corp = lambda a: AA.akus[a]["corpus"]

def parse_justified(lines):
    """devuelve (ids actuales, idx_inicio_justified, idx_fin_justified)"""
    ji = next((k for k, l in enumerate(lines) if re.match(r"^  justified_by:", l)), None)
    if ji is None:
        return [], None, None
    ids = []
    k = ji + 1
    while k < len(lines):
        m = re.match(r"^    - id:\s*(.+)$", lines[k])
        if m:
            ids.append(m.group(1).strip()); k += 1
            while k < len(lines) and re.match(r"^      \w", lines[k]):
                k += 1
        elif re.match(r"^  \w", lines[k]):  # next 2-space field
            break
        else:
            k += 1
    return ids, ji, k

total_add = 0; touched = 0
for p in glob.glob(os.path.join(AA.ROOT, "taku", "**", "*.md"), recursive=True):
    text = open(p, encoding="utf-8").read()
    lines = text.split("\n")
    cur, ji, jend = parse_justified(lines)
    if ji is None:
        continue
    curset = set(cur)
    # deducibles = corroboradores cross-source de cada justified_by actual
    cand = {}
    for x in cur:
        if x not in AA.akus:
            continue
        for y in agree[x]:
            if y in curset or y in cand:
                continue
            if corp(y) != corp(x):  # cross-source
                cand[y] = x  # y corrobora x
    # priorizar por nº de justificantes actuales que y corrobora
    score = defaultdict(int)
    for x in cur:
        if x in AA.akus:
            for y in agree[x]:
                if corp(y) != corp(x) and y not in curset:
                    score[y] += 1
    adds = sorted(cand, key=lambda y: -score[y])[:CAP]
    if not adds:
        continue
    total_add += len(adds); touched += 1
    if mode == "dry":
        print(f"{os.path.basename(p)[:-3]}: +{len(adds)} (de {len(cur)} actuales)")
        continue
    # 1) frontmatter: insertar entradas antes de jend
    block = []
    for y in adds:
        block.append(f"    - id: {y}")
        block.append(f"      link_validation: llm-proposed")
        block.append(f"      link_note: \"deducible: corrobora {cand[y]} desde [{corp(y)}] (cross-source)\"")
    lines = lines[:jend] + block + lines[jend:]
    # 2) cuerpo ## Relaciones, linea **justified_by**
    bi = next((k for k, l in enumerate(lines) if l.strip().startswith("**justified_by**")), None)
    wl = " · ".join(f"[[{y}]]" for y in adds)
    if bi is not None:
        lines[bi] = lines[bi].rstrip() + " · " + wl
    else:
        ri = next((k for k, l in enumerate(lines) if l.strip() == "## Relaciones"), None)
        if ri is not None:
            lines.insert(ri + 1, f"**justified_by** ← {wl}")
    open(p, "w", encoding="utf-8", newline="\n").write("\n".join(lines))

print(f"\nTAKUs tocados: {touched} | enlaces justified_by deducibles añadidos: {total_add}")
