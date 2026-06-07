# -*- coding: utf-8 -*-
"""_audit_wire.py — aplica aristas bidireccionales al grafo AKU usando akupatch.

Uso: importar EDGES como lista de tuplas (src, field, dst) y llamar wire(EDGES).
Cada arista escribe el lado directo en src y el inverso en dst (3-capas sync).
field ∈ {supported_by, supports, constrained_by, constrains,
         context_breaks_at, breaks_context_of, contradicts, related}
Convención: declara la arista desde el nodo 'origen' con el campo SALIENTE/elegido;
el inverso se deriva automáticamente.
"""
import os, sys
import akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAIR = {"supported_by": "supports", "supports": "supported_by",
        "constrained_by": "constrains", "constrains": "constrained_by",
        "context_breaks_at": "breaks_context_of",
        "breaks_context_of": "context_breaks_at",
        "contradicts": "contradicts", "related": "related"}

def wire(edges, dry=False):
    """edges: list of (src, field, dst). Applies src.field+=dst and dst.inv+=src."""
    ids = set(os.path.basename(p)[:-3] for p in
              __import__("glob").glob(os.path.join(ROOT, "aku", "*.md")))
    ops = {}  # id -> list of (field, target)
    problems = []
    for src, field, dst in edges:
        if field not in PAIR:
            problems.append(f"campo invalido: {field}"); continue
        if src not in ids: problems.append(f"src inexistente: {src}"); continue
        if dst not in ids: problems.append(f"dst inexistente: {dst}"); continue
        if src == dst: problems.append(f"self-loop: {src}"); continue
        ops.setdefault(src, []).append((field, dst))
        ops.setdefault(dst, []).append((PAIR[field], src))
    if problems:
        print("PROBLEMAS:")
        for p in problems: print("  -", p)
        if not dry:
            print("Abortando por problemas."); sys.exit(2)
    if dry:
        import importlib.util
        spec=importlib.util.spec_from_file_location("aa",os.path.join(ROOT,"scripts","_audit_analyze.py"))
        aa=importlib.util.module_from_spec(spec); spec.loader.exec_module(aa)
        samecorp=0
        for i,(src,field,dst) in enumerate(edges):
            cs=aa.akus.get(src,{}).get("corpus","?"); cd=aa.akus.get(dst,{}).get("corpus","?")
            flag=" <<< SAME-CORPUS" if cs==cd else ""
            if cs==cd: samecorp+=1
            print(f"  {i+1}. [{cs}->{cd}]{flag} {src} --{field}--> {dst}")
        print(f"Total: {len(edges)} aristas, {len(ops)} ficheros tocados. Same-corpus: {samecorp}")
        return
    op_list = [{"id": k, "add_rel": v} for k, v in ops.items()]
    akupatch.apply(ROOT, op_list)
    print(f"Aplicadas {len(edges)} aristas en {len(ops)} ficheros.")
