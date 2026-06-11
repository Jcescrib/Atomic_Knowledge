# -*- coding: utf-8 -*-
"""_resync_body.py — reconstruye las lineas de wikilinks del cuerpo ## Relaciones de
cada AKU para que casen EXACTAMENTE con el frontmatter (fuente canonica). Solo reescribe
los ficheros con drift. Idempotente.
"""
import sys, os, re, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AKU_FIELDS = ["supported_by", "supports", "constrained_by", "constrains",
              "context_breaks_at", "breaks_context_of", "contradicts", "related"]
ARROW = {"supported_by": "←", "supports": "→", "constrained_by": "←", "constrains": "→",
         "context_breaks_at": "→", "breaks_context_of": "→", "contradicts": "↔", "related": "↔"}
mode = sys.argv[1] if len(sys.argv) > 1 else "dry"

def parse_fm_rel(lines):
    ri = next((k for k, l in enumerate(lines) if l.rstrip() == "relations:"), None)
    rel = {}
    if ri is None: return rel
    k = ri + 1
    while k < len(lines) and re.match(r"^  \w+:", lines[k]):
        m = re.match(r"^  (\w+):\s*(.*)$", lines[k]); f = m.group(1); rest = m.group(2).strip()
        if rest.startswith("["):
            inner = rest[1:-1].strip(); rel[f] = [x.strip() for x in inner.split(",") if x.strip()]; k += 1
        else:
            k += 1; rel[f] = []
            while k < len(lines) and re.match(r"^    - ", lines[k]):
                rel[f].append(lines[k].strip()[2:].strip()); k += 1
    return rel

fixed = 0
for p in glob.glob(os.path.join(ROOT, "aku", "*.md")):
    text = open(p, encoding="utf-8").read()
    parts = text.split("---")
    fm = parts[1]; body = "---".join(parts[2:])
    rel = parse_fm_rel(fm.split("\n"))
    # build expected wikilink lines
    want = {f: [f"[[{t}]]" for t in rel[f]] for f in AKU_FIELDS if rel.get(f)}
    # current body wikilinks per field
    cur = {}
    for bl in body.split("\n"):
        m = re.match(r"^\*\*(\w+)\*\*", bl)
        if m:
            cur[m.group(1)] = re.findall(r"\[\[([^\]]+)\]\]", bl)
    drift = False
    for f in AKU_FIELDS:
        want_set = set(rel.get(f) or [])
        cur_set = set(cur.get(f, []))
        if want_set != cur_set:
            drift = True; break
    if not drift:
        continue
    fixed += 1
    if mode != "apply":
        print("drift:", os.path.basename(p)[:-3]); continue
    # rebuild ## Relaciones section
    blines = body.split("\n")
    ri = next((k for k, l in enumerate(blines) if l.strip() == "## Relaciones"), None)
    new_rel = ["## Relaciones", ""]
    for f in AKU_FIELDS:
        if rel.get(f):
            new_rel.append(f"**{f}** {ARROW[f]} " + " · ".join(f"[[{t}]]" for t in rel[f]))
    if ri is not None:
        blines = blines[:ri] + new_rel
    else:
        if blines and blines[-1].strip() != "": blines.append("")
        blines += new_rel
    newbody = "\n".join(blines)
    out = parts[0] + "---" + fm + "---" + newbody
    if not out.endswith("\n"): out += "\n"
    open(p, "w", encoding="utf-8", newline="\n").write(out)

print(f"{'reparados' if mode=='apply' else 'con drift'}: {fixed}")
