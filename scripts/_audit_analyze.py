# -*- coding: utf-8 -*-
"""_audit_analyze.py — analiza el grafo AKU completo: corpus, dominios, grados,
componentes conectados, y candidatos cross-corpus. Solo lectura."""
import os, re, glob, json, sys
from collections import defaultdict, Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AKU_FIELDS = ["supported_by", "supports", "constrained_by", "constrains",
              "context_breaks_at", "breaks_context_of", "contradicts", "related"]

SOURCE_TAGS = {
    "raw/cursos/power-mba/": "power-mba",
    "raw/libros/hormozi/": "hormozi",
    "raw/libros/jocko/": "jocko",
    "raw/libros/kolenda/": "kolenda",
    "raw/libros/naval/": "naval",
    "raw/libros/james-clear/": "james-clear",
    "raw/libros/robert-greene/": "robert-greene",
    "raw/libros/50-cent/": "50-cent",
}

def corpus_of(sources):
    for s in sources:
        for pref, tag in SOURCE_TAGS.items():
            if s.startswith(pref):
                return tag
    return "(unknown)"

def parse(path):
    t = open(path, encoding="utf-8").read()
    parts = t.split("---")
    fm = parts[1]
    body = "---".join(parts[2:])
    lines = fm.split("\n")
    def scalar(key):
        for l in lines:
            m = re.match(rf"^{key}:\s*(.*)$", l)
            if m: return m.group(1).strip()
        return ""
    # statement (may be block scalar with >)
    statement = ""
    for i, l in enumerate(lines):
        if re.match(r"^statement:\s*>", l):
            j = i+1
            buf = []
            while j < len(lines) and (lines[j].startswith("  ") or lines[j].strip()==""):
                if re.match(r"^\w", lines[j]): break
                buf.append(lines[j].strip())
                j += 1
            statement = " ".join(x for x in buf if x)
            break
        m = re.match(r"^statement:\s*(.+)$", l)
        if m:
            statement = m.group(1).strip()
            break
    aku_class = scalar("aku_class")
    epistemic = scalar("epistemic_type")
    domain_raw = scalar("domain")
    domain = []
    if domain_raw.startswith("["):
        domain = [x.strip() for x in domain_raw[1:-1].split(",") if x.strip()]
    origin = scalar("origin").strip('"')
    # relations
    rel = {f: [] for f in AKU_FIELDS}
    ri = next((k for k, l in enumerate(lines) if l.rstrip() == "relations:"), None)
    if ri is not None:
        k = ri + 1
        while k < len(lines) and re.match(r"^  \w+:", lines[k]):
            m = re.match(r"^  (\w+):\s*(.*)$", lines[k])
            f, rest = m.group(1), m.group(2).strip()
            if f not in AKU_FIELDS:
                break
            if rest.startswith("["):
                inner = rest[1:-1].strip()
                rel[f] = [x.strip() for x in inner.split(",") if x.strip()] if inner else []
                k += 1
            else:
                k += 1
                while k < len(lines) and re.match(r"^    - ", lines[k]):
                    rel[f].append(lines[k].strip()[2:].strip())
                    k += 1
    # sources
    src = []
    si = next((k for k,l in enumerate(lines) if l.rstrip()=="sources:"), None)
    if si is not None:
        k = si+1
        while k < len(lines) and re.match(r"^  - ", lines[k]):
            src.append(lines[k].strip()[2:].strip().strip('"'))
            k += 1
    return dict(statement=statement, aku_class=aku_class, epistemic=epistemic,
                domain=domain, origin=origin, rel=rel, sources=src,
                corpus=corpus_of(src), body=body)

akus = {}
for p in glob.glob(os.path.join(ROOT, "aku", "*.md")):
    akus[os.path.basename(p)[:-3]] = parse(p)

# degree
deg = defaultdict(int)
for aid, a in akus.items():
    for f in AKU_FIELDS:
        deg[aid] += len(a["rel"][f])
        for t in a["rel"][f]:
            deg[t] += 0  # ensure presence handled by symmetry

# connected components (undirected over all relations)
adj = defaultdict(set)
for aid, a in akus.items():
    for f in AKU_FIELDS:
        for t in a["rel"][f]:
            if t in akus:
                adj[aid].add(t); adj[t].add(aid)
seen = set(); comps = []
for aid in akus:
    if aid in seen: continue
    stack=[aid]; comp=[]
    while stack:
        n=stack.pop()
        if n in seen: continue
        seen.add(n); comp.append(n)
        stack.extend(adj[n]-seen)
    comps.append(comp)
comps.sort(key=len, reverse=True)

def cmd_overview():
    print("=== CORPUS DISTRIBUTION ===")
    cc = Counter(a["corpus"] for a in akus.values())
    for k,v in cc.most_common(): print(f"  {k}: {v}")
    print("\n=== AKU CLASS ===")
    for k,v in Counter(a["aku_class"] for a in akus.values()).most_common(): print(f"  {k}: {v}")
    print("\n=== EPISTEMIC TYPE ===")
    for k,v in Counter(a["epistemic"] for a in akus.values()).most_common(): print(f"  {k}: {v}")
    print(f"\n=== TOPOLOGY ===")
    print(f"  total AKUs: {len(akus)}")
    print(f"  connected components: {len(comps)}")
    print(f"  largest component: {len(comps[0])}")
    orphans = [a for a in akus if deg[a]==0]
    print(f"  orphans (degree 0): {len(orphans)}")
    underc = [a for a in akus if deg[a] in (1,2)]
    print(f"  under-connected (degree 1-2): {len(underc)}")
    print(f"\n=== SMALL COMPONENTS (size<=5) ===")
    small = [c for c in comps if len(c)<=5]
    print(f"  count: {len(small)}")
    for c in small[:60]:
        print(f"   [{len(c)}] " + ", ".join(c))
    if orphans:
        print("\n=== ORPHANS ===")
        for o in orphans: print("  "+o)

def cmd_domains():
    dc = Counter()
    for a in akus.values():
        for d in a["domain"]:
            dc[d]+=1
    print("=== DOMAIN TAGS (count) ===")
    for k,v in dc.most_common(120):
        print(f"  {v:4d}  {k}")

def cmd_domain(tag):
    rows=[]
    for aid,a in akus.items():
        if tag in a["domain"]:
            rows.append((a["corpus"], aid, a["aku_class"], a["statement"][:140]))
    rows.sort()
    print(f"=== AKUs with domain '{tag}' ({len(rows)}) ===")
    for c,aid,cls,st in rows:
        print(f"[{c}/{cls}] {aid}\n     {st}")

def cmd_search(term):
    term_l=term.lower()
    rows=[]
    for aid,a in akus.items():
        hay = (term_l in a["statement"].lower() or term_l in aid.lower()
               or any(term_l in d.lower() for d in a["domain"]))
        if hay:
            rows.append((a["corpus"], aid, a["aku_class"], ",".join(a["domain"][:4]), a["statement"][:130]))
    rows.sort()
    print(f"=== search '{term}' ({len(rows)}) ===")
    for c,aid,cls,dm,st in rows:
        print(f"[{c}/{cls}] {aid}  ({dm})\n     {st}")

def cmd_components_detail():
    print(f"=== ALL COMPONENTS (sorted desc) — {len(comps)} total ===")
    for i,c in enumerate(comps):
        print(f"  comp {i}: size {len(c)}")

if __name__=="__main__":
    cmd = sys.argv[1] if len(sys.argv)>1 else "overview"
    if cmd=="overview": cmd_overview()
    elif cmd=="domains": cmd_domains()
    elif cmd=="domain": cmd_domain(sys.argv[2])
    elif cmd=="search": cmd_search(" ".join(sys.argv[2:]))
    elif cmd=="components": cmd_components_detail()
