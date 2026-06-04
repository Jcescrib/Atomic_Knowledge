#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
akugen.py — generador de ficheros AKU/TAKU con sync bidireccional + cuerpo.

Garantiza las reglas del CLAUDE.md de forma mecánica:
  - inversos bidireccionales espejados ENTRE los AKUs del mismo lote
    (supported_by<->supports, constrained_by<->constrains,
     context_breaks_at<->breaks_context_of, contradicts<->contradicts,
     related<->related).
  - cuerpo `## Relaciones` derivado de las relaciones finales (cero body-drift).
  - cross-links a AKUs existentes: NO se espejan aquí (se incluye el wikilink en
    el cuerpo del AKU nuevo, y el inverso en el fichero existente se aplica aparte
    con un Edit puntual — ver lista CROSS impresa al final).

Uso: importar `generate(akus, takus, root)` desde un script de capítulo.
"""
import os, re, textwrap

# pares bidireccionales AKU (campo -> inverso)
INVERSE = {
    "supported_by": "supports", "supports": "supported_by",
    "constrained_by": "constrains", "constrains": "constrained_by",
    "context_breaks_at": "breaks_context_of",
    "breaks_context_of": "context_breaks_at",
    "contradicts": "contradicts", "related": "related",
}
AKU_FIELDS = ["supported_by", "supports", "constrained_by", "constrains",
              "context_breaks_at", "breaks_context_of", "contradicts", "related"]
ARROW = {"supported_by": "←", "supports": "→", "constrained_by": "←",
         "constrains": "→", "context_breaks_at": "→", "breaks_context_of": "→",
         "contradicts": "↔", "related": "↔"}

# TAKU aku-link arrows / taku-taku arrows
TAKU_AKU_ARROW = {"justified_by": "←", "constrained_by": "←",
                  "breaks_when": "→", "illustrates": "→", "challenges": "→"}
TAKU_REL_ARROW = {"complementary": "↔", "alternative_to": "↔",
                  "precedes": "→", "follows": "←"}


def _fold(text):
    text = " ".join(text.split())
    lines = textwrap.wrap(text, width=78)
    return "\n".join("  " + l for l in lines)


def _yaml_list(field, items):
    if not items:
        return f"  {field}: []"
    body = "\n".join(f"    - {it}" for it in items)
    return f"  {field}:\n{body}"


def _aku_body(rel):
    out = ["## Relaciones", ""]
    any_line = False
    for f in AKU_FIELDS:
        items = rel.get(f) or []
        if items:
            links = " · ".join(f"[[{i}]]" for i in items)
            out.append(f"**{f}** {ARROW[f]} {links}")
            out.append("")
            any_line = True
    if not any_line:
        out.append("<!-- sin relaciones -->")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def _render_aku(r):
    rel = r.get("rel", {})
    fm = []
    fm.append("---")
    fm.append("type: aku")
    fm.append(f"aku_class: {r['class']}")
    fm.append(f"id: {r['id']}")
    fm.append("statement: >")
    fm.append(_fold(r["statement"]))
    fm.append(f'origin: "{r["origin"]}"')
    fm.append(f"domain: [{', '.join(r['domain'])}]")
    fm.append("")
    conf = r.get("llm_confidence", 0.50)
    fm.append(f"llm_confidence: {('null' if conf is None else format(conf, '.2f'))}")
    fm.append("")
    fm.append("human_certainty:")
    fm.append("  status: unvalidated")
    fm.append("  iterations: 0")
    fm.append('  context_boundary: ""')
    fm.append('  validated_by: ""')
    fm.append('  validation_date: ""')
    fm.append('  method: ""')
    fm.append("")
    fm.append(f"epistemic_type: {r.get('epistemic_type','sourced')}")
    fm.append("")
    fm.append("relations:")
    for f in AKU_FIELDS:
        fm.append(_yaml_list(f, rel.get(f) or []))
    fm.append("")
    fm.append("sources:")
    for s in r.get("sources", []):
        fm.append(f"  - {s}")
    fm.append("")
    fm.append(f"created: {r.get('created','2026-06-04')}")
    fm.append(f"updated: {r.get('updated','2026-06-04')}")
    fm.append("status: active")
    fm.append('status_note: ""')
    fm.append("---")
    fm.append("")
    return "\n".join(fm) + "\n" + _aku_body(rel)


def _taku_body(r):
    out = []
    out.append(r["body"].rstrip())
    out.append("")
    out.append("## Relaciones")
    out.append("")
    links = r.get("aku_links", {})
    for f in ["justified_by", "constrained_by", "breaks_when", "illustrates", "challenges"]:
        items = links.get(f) or []
        if items:
            ln = " · ".join(f"[[{i}]]" for i in items)
            out.append(f"**{f}** {TAKU_AKU_ARROW[f]} {ln}")
            out.append("")
    trel = r.get("taku_relations", {})
    for f in ["complementary", "alternative_to", "precedes", "follows"]:
        items = trel.get(f) or []
        if items:
            ln = " · ".join(f"[[{i}]]" for i in items)
            out.append(f"**{f}** {TAKU_REL_ARROW[f]} {ln}")
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def _render_taku(r):
    links = r.get("aku_links", {})
    trel = r.get("taku_relations", {})
    fm = []
    fm.append("---")
    fm.append("type: taku")
    fm.append(f"taku_type: {r['taku_type']}")
    fm.append(f"id: {r['id']}")
    fm.append(f'title: "{r["title"]}"')
    fm.append(f'origin: "{r.get("origin","")}"')
    fm.append(f"domain: [{', '.join(r['domain'])}]")
    fm.append("")
    fm.append(f'when_to_use: "{r.get("when_to_use","")}"')
    fm.append(f'when_not_to_use: "{r.get("when_not_to_use","")}"')
    fm.append("")
    fm.append("aku_links:")
    fm.append("  justified_by:")
    for i in links.get("justified_by", []):
        fm.append(f"    - id: {i}")
        fm.append("      link_validation: llm-proposed")
        fm.append('      link_note: ""')
    for f in ["constrained_by", "breaks_when", "illustrates", "challenges"]:
        items = links.get(f) or []
        if not items:
            fm.append(f"  {f}: []")
        else:
            fm.append(f"  {f}:")
            for i in items:
                fm.append(f"    - id: {i}")
                fm.append("      link_validation: llm-proposed")
                fm.append('      link_note: ""')
    fm.append("")
    fm.append("content_validation:")
    fm.append("  status: llm-authored")
    fm.append('  reviewed_by: ""')
    fm.append('  review_date: ""')
    fm.append('  review_notes: ""')
    fm.append("")
    fm.append("human_certainty:")
    fm.append("  status: unvalidated")
    fm.append("  iterations: 0")
    fm.append('  context_boundary: ""')
    fm.append('  validated_by: ""')
    fm.append('  validation_date: ""')
    fm.append('  method: ""')
    fm.append("")
    fm.append("taku_relations:")
    for f in ["complementary", "alternative_to"]:
        fm.append(_yaml_list(f, trel.get(f) or []))
    # precedes / follows carry sequence_type
    for f in ["precedes", "follows"]:
        items = trel.get(f) or []
        if not items:
            fm.append(f"  {f}: []")
        else:
            fm.append(f"  {f}:")
            for it in items:
                fm.append(f"    - id: {it['id']}")
                fm.append(f"      sequence_type: {it.get('sequence_type','recommended')}")
    fm.append("")
    fm.append(f"created: {r.get('created','2026-06-04')}")
    fm.append(f"updated: {r.get('updated','2026-06-04')}")
    fm.append("status: draft")
    fm.append('status_note: ""')
    fm.append("---")
    fm.append("")
    return "\n".join(fm) + "\n" + _taku_body(r)


def generate(akus, takus, root):
    """Espeja inversos entre AKUs del lote, escribe ficheros, devuelve cross-links."""
    by_id = {a["id"]: a for a in akus}
    for a in akus:
        a.setdefault("rel", {})
    # mirror among-set inverses
    for a in akus:
        for f in AKU_FIELDS:
            for tgt in list(a["rel"].get(f) or []):
                if tgt in by_id:
                    inv = INVERSE[f]
                    tl = by_id[tgt]["rel"].setdefault(inv, [])
                    if a["id"] not in tl:
                        tl.append(a["id"])
    # dedupe rel lists
    for a in akus:
        for f in AKU_FIELDS:
            if a["rel"].get(f):
                seen = []
                for x in a["rel"][f]:
                    if x not in seen:
                        seen.append(x)
                a["rel"][f] = seen
    written = []
    for a in akus:
        p = os.path.join(root, "aku", a["id"] + ".md")
        with open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(_render_aku(a))
        written.append(p)
    for t in takus:
        sub = t.get("subdir", t["taku_type"] + "s")
        p = os.path.join(root, "taku", sub, t["id"] + ".md")
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(_render_taku(t))
        written.append(p)
    # report cross-links (new aku -> existing aku) needing manual inverse
    cross = []
    for a in akus:
        for f in AKU_FIELDS:
            for tgt in (a["rel"].get(f) or []):
                if tgt not in by_id:
                    cross.append((a["id"], f, INVERSE[f], tgt))
    return written, cross
