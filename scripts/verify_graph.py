# -*- coding: utf-8 -*-
"""verify_graph.py — chequeos de integridad del grafo AKU (simetría, body, targets)."""
import os, re, glob, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AKU_FIELDS = ["supported_by", "supports", "constrained_by", "constrains",
              "context_breaks_at", "breaks_context_of", "contradicts", "related"]
PAIR = {"supported_by": "supports", "supports": "supported_by",
        "constrained_by": "constrains", "constrains": "constrained_by",
        "context_breaks_at": "breaks_context_of",
        "breaks_context_of": "context_breaks_at",
        "contradicts": "contradicts", "related": "related"}


def parse(path):
    t = open(path, encoding="utf-8").read()
    parts = t.split("---")
    fm = parts[1]
    body = "---".join(parts[2:])
    lines = fm.split("\n")
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
    src = re.findall(r"^  - (.+)$", "\n".join(
        lines[next((k for k,l in enumerate(lines) if l.rstrip()=="sources:"), len(lines)):]), re.M)
    src = [s.strip().strip('"') for s in src]
    # body wikilinks per field
    bwl = {}
    for bl in body.split("\n"):
        m = re.match(r"^\*\*(\w+)\*\*", bl)
        if m:
            bwl[m.group(1)] = re.findall(r"\[\[([^\]]+)\]\]", bl)
    return rel, src, bwl


akus = {}
for p in glob.glob(os.path.join(ROOT, "aku", "*.md")):
    akus[os.path.basename(p)[:-3]] = parse(p)

errors = []
ids = set(akus)
for aid, (rel, src, bwl) in akus.items():
    # sources must not cite akus
    for s in src:
        if s.startswith("aku-") or "/aku/" in s:
            errors.append(f"{aid}: source cita AKU: {s}")
    for f in AKU_FIELDS:
        for tgt in rel[f]:
            if tgt not in ids:
                errors.append(f"{aid}.{f} -> target inexistente {tgt}")
                continue
            # symmetry
            inv = PAIR[f]
            if aid not in akus[tgt][0][inv]:
                errors.append(f"ASIMETRIA: {aid}.{f}->{tgt} pero {tgt}.{inv} no contiene {aid}")
        # body must match frontmatter
        fm_set = set(rel[f])
        bd_set = set(bwl.get(f, []))
        if fm_set != bd_set:
            miss = fm_set - bd_set
            extra = bd_set - fm_set
            errors.append(f"BODY-DRIFT {aid}.{f}: faltan={miss} sobran={extra}")

print(f"AKUs: {len(akus)}  | errores: {len(errors)}")
for e in errors:
    print("  -", e)
sys.exit(1 if errors else 0)
