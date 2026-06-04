# -*- coding: utf-8 -*-
"""
akupatch.py — parchea ficheros AKU existentes con sync 3-capas garantizado.

Operaciones por fichero (todas opcionales):
  add_rel:    [(field, target_id), ...]  añade relación en frontmatter + cuerpo
  add_source: "raw/....md"               añade fuente (dedup)
  confidence: 0.60                        fija llm_confidence
  updated:    "2026-06-04"                fija updated
  add_domain: "hormozi"                   añade tag de dominio si falta

Maneja relations en estilo inline ([], [a, b]) y en bloque (- item),
normalizando a bloque al añadir. El cuerpo `## Relaciones` se mantiene
sincronizado (añade al `**field**` existente o crea la línea).
"""
import os, re

AKU_FIELDS = ["supported_by", "supports", "constrained_by", "constrains",
              "context_breaks_at", "breaks_context_of", "contradicts", "related"]
ARROW = {"supported_by": "←", "supports": "→", "constrained_by": "←",
         "constrains": "→", "context_breaks_at": "→", "breaks_context_of": "→",
         "contradicts": "↔", "related": "↔"}


def _parse_rel_field(lines, i):
    """Devuelve (items, j) leyendo el campo de relación que empieza en lines[i]."""
    m = re.match(r"^  (\w+):\s*(.*)$", lines[i])
    rest = m.group(2).strip()
    items = []
    if rest.startswith("[") and rest.endswith("]"):
        inner = rest[1:-1].strip()
        if inner:
            items = [x.strip() for x in inner.split(",") if x.strip()]
        return items, i + 1
    # block style: gather following '    - x'
    j = i + 1
    while j < len(lines) and re.match(r"^    - ", lines[j]):
        items.append(lines[j].strip()[2:].strip())
        j += 1
    return items, j


def _rebuild_rel_block(rel):
    out = ["relations:"]
    for f in AKU_FIELDS:
        items = rel.get(f) or []
        if not items:
            out.append(f"  {f}: []")
        else:
            out.append(f"  {f}:")
            for it in items:
                out.append(f"    - {it}")
    return out


def apply_one(root, op):
    p = os.path.join(root, "aku", op["id"] + ".md")
    with open(p, encoding="utf-8") as fh:
        text = fh.read()
    lines = text.split("\n")

    # --- frontmatter relations ---
    # find 'relations:' and its span
    ri = next(k for k, l in enumerate(lines) if l.rstrip() == "relations:")
    rel = {}
    k = ri + 1
    while k < len(lines) and re.match(r"^  \w+:", lines[k]):
        f = re.match(r"^  (\w+):", lines[k]).group(1)
        items, k = _parse_rel_field(lines, k)
        rel[f] = items
    rel_end = k  # first line after relations block
    for field, tgt in op.get("add_rel", []):
        rel.setdefault(field, [])
        if tgt not in rel[field]:
            rel[field].append(tgt)
    new_rel_block = _rebuild_rel_block(rel)
    lines = lines[:ri] + new_rel_block + lines[rel_end:]

    # --- sources ---
    if op.get("add_source"):
        si = next(k for k, l in enumerate(lines) if l.rstrip() == "sources:")
        k = si + 1
        while k < len(lines) and re.match(r"^  - ", lines[k]):
            k += 1
        existing = [lines[x].strip()[2:].strip().strip('"') for x in range(si + 1, k)]
        if op["add_source"] not in existing:
            lines.insert(k, f"  - {op['add_source']}")

    # --- confidence / updated / domain (scalar edits) ---
    for idx, l in enumerate(lines):
        if op.get("confidence") is not None and re.match(r"^llm_confidence:", l):
            lines[idx] = f"llm_confidence: {format(op['confidence'], '.2f')}"
        if op.get("updated") and re.match(r"^updated:", l):
            lines[idx] = f"updated: {op['updated']}"
        if op.get("add_domain") and re.match(r"^domain:\s*\[", l):
            mm = re.match(r"^domain:\s*\[(.*)\]\s*$", l)
            tags = [t.strip() for t in mm.group(1).split(",") if t.strip()]
            if op["add_domain"] not in tags:
                tags.append(op["add_domain"])
                lines[idx] = f"domain: [{', '.join(tags)}]"

    # --- body wikilinks ---
    if op.get("add_rel"):
        # locate body '## Relaciones'
        bi = next(k for k, l in enumerate(lines) if l.strip() == "## Relaciones")
        body = lines[bi:]
        # map field -> line index within body
        for field, tgt in op["add_rel"]:
            wl = f"[[{tgt}]]"
            found = False
            for bj in range(len(body)):
                if body[bj].startswith(f"**{field}**"):
                    if wl not in body[bj]:
                        body[bj] = body[bj].rstrip() + f" · {wl}"
                    found = True
                    break
            if not found:
                # append new field line with blank-line separation
                if body and body[-1].strip() != "":
                    body.append("")
                body.append(f"**{field}** {ARROW[field]} {wl}")
        # strip trailing blanks then ensure newline
        while body and body[-1].strip() == "":
            body.pop()
        lines = lines[:bi] + body

    out = "\n".join(lines)
    if not out.endswith("\n"):
        out += "\n"
    with open(p, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(out)
    return p


def apply(root, ops):
    return [apply_one(root, o) for o in ops]
