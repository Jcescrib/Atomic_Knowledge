# -*- coding: utf-8 -*-
"""_unwire.py — elimina aristas AKU-AKU (ambas direcciones, frontmatter + cuerpo).

Uso: python scripts/_unwire.py apply outputs/_validate/_prune.json
  _prune.json = [["a-id","b-id"], ...]  (elimina la arista entre a y b en cualquier campo)
"""
import sys, os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AKU_FIELDS = ["supported_by", "supports", "constrained_by", "constrains",
              "context_breaks_at", "breaks_context_of", "contradicts", "related"]

def _parse_rel(lines):
    ri = next((k for k, l in enumerate(lines) if l.rstrip() == "relations:"), None)
    rel = {};
    if ri is None: return None, None, None
    k = ri + 1
    while k < len(lines) and re.match(r"^  \w+:", lines[k]):
        m = re.match(r"^  (\w+):\s*(.*)$", lines[k]); f = m.group(1); rest = m.group(2).strip()
        if rest.startswith("["):
            inner = rest[1:-1].strip()
            rel[f] = [x.strip() for x in inner.split(",") if x.strip()]; k += 1
        else:
            k += 1; rel[f] = []
            while k < len(lines) and re.match(r"^    - ", lines[k]):
                rel[f].append(lines[k].strip()[2:].strip()); k += 1
    return ri, k, rel

def _rebuild(rel):
    out = ["relations:"]
    for f in AKU_FIELDS:
        items = rel.get(f) or []
        if items:
            out.append(f"  {f}:")
            for it in items: out.append(f"    - {it}")
        else:
            out.append(f"  {f}: []")
    return out

def remove_from(aid, target):
    p = os.path.join(ROOT, "aku", aid + ".md")
    lines = open(p, encoding="utf-8").read().split("\n")
    ri, rend, rel = _parse_rel(lines)
    if ri is None: return False
    changed = False
    for f in list(rel):
        if target in rel[f]:
            rel[f] = [x for x in rel[f] if x != target]; changed = True
    if changed:
        lines = lines[:ri] + _rebuild(rel) + lines[rend:]
    # body wikilinks
    out = []
    for l in lines:
        if l.startswith("**") and f"[[{target}]]" in l:
            parts = [s for s in re.split(r"\s*·\s*", l) if f"[[{target}]]" not in s]
            # if only the field header remains (no wikilinks), drop the line
            if len(parts) == 1 and "[[" not in parts[0]:
                changed = True; continue
            l = " · ".join(parts); changed = True
        out.append(l)
    if changed:
        txt = "\n".join(out)
        if not txt.endswith("\n"): txt += "\n"
        open(p, "w", encoding="utf-8", newline="\n").write(txt)
    return changed

mode = sys.argv[1] if len(sys.argv) > 1 else "dry"
pairs = json.load(open(os.path.join(ROOT, sys.argv[2]), encoding="utf-8"))
n = 0
for a, b in pairs:
    if mode == "apply":
        c1 = remove_from(a, b); c2 = remove_from(b, a)
        if c1 or c2: n += 1
    else:
        print("would prune:", a, "<>", b)
print(f"{'podadas' if mode=='apply' else 'a podar'}: {n if mode=='apply' else len(pairs)} aristas")
