# -*- coding: utf-8 -*-
"""_kol_apply.py — agrega veredictos del vetado Kolenda y aplica los (a). Temporal.

Uso:
  python scripts/_kol_apply.py dry     # valida + dry-run, no escribe grafo
  python scripts/_kol_apply.py apply   # aplica aristas (a) via wire()
Siempre escribe el informe (b) en outputs/.
"""
import os, sys, glob, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _audit_wire as W
import _audit_analyze as AA

ROOT = AA.ROOT
ids = set(AA.akus)
PAIR = W.PAIR

mode = sys.argv[1] if len(sys.argv) > 1 else "dry"

rows = []
for p in sorted(glob.glob(os.path.join(ROOT, "outputs", "_kol_results", "batch_*.json"))):
    rows.extend(json.load(open(p, encoding="utf-8")))

a_rows = [r for r in rows if r.get("verdict") == "a"]
b_rows = [r for r in rows if r.get("verdict") == "b"]
d_rows = [r for r in rows if r.get("verdict") == "discard"]
print(f"Veredictos: {len(a_rows)} (a) | {len(b_rows)} (b) | {len(d_rows)} discard | total {len(rows)}")

# --- construir aristas (a), validar y dedup ---
edges = []
seen = set()
bad = []
for r in a_rows:
    src, field, dst = r.get("src"), r.get("field"), r.get("dst")
    if not src or not dst or field not in PAIR:
        # fallback: usar a_id/b_id con related si el agente dejó campos nulos
        src, dst, field = r.get("a_id"), r.get("b_id"), "related"
    if src not in ids or dst not in ids:
        bad.append(f"id inexistente: {src} / {dst}"); continue
    if src == dst:
        bad.append(f"self-loop: {src}"); continue
    key = tuple(sorted((src, dst)))
    if key in seen:
        continue
    # ¿ya enlazados en el grafo actual? (cualquier campo)
    already = any(dst in AA.akus[src]["rel"][f] for f in AA.AKU_FIELDS)
    if already:
        continue
    seen.add(key)
    edges.append((src, field, dst))

print(f"Aristas (a) válidas, dedup, no-existentes: {len(edges)}")
if bad:
    print("DESCARTADAS por validación:")
    for b in bad[:20]:
        print("  -", b)

# corpus breakdown
intra = sum(1 for s, f, d in edges if AA.akus[s]["corpus"] == AA.akus[d]["corpus"] == "kolenda")
print(f"  intra-Kolenda: {intra} | con otro corpus: {len(edges)-intra}")
from collections import Counter
fc = Counter(f for _, f, _ in edges)
print("  por campo:", dict(fc))

# --- informe (b) para aprobación ---
b_out = os.path.join(ROOT, "outputs", "_kol_proposals_b.json")
json.dump(b_rows, open(b_out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
md = ["# Propuestas (b) conceptuales — integración Kolenda", "",
      f"Total: {len(b_rows)} pares. Requieren aprobación humana antes de escribir.", ""]
for r in b_rows:
    md.append(f"- `{r.get('src') or r.get('a_id')}` **{r.get('field') or 'related'}** "
              f"`{r.get('dst') or r.get('b_id')}` — {r.get('reason','')}")
open(os.path.join(ROOT, "outputs", "_kol_proposals_b.md"), "w", encoding="utf-8").write("\n".join(md))
print(f"Informe (b): outputs/_kol_proposals_b.md ({len(b_rows)} props)")

if mode == "dry":
    print("\n=== DRY-RUN aristas (a) (primeras 30) ===")
    for s, f, d in edges[:30]:
        print(f"  [{AA.akus[s]['corpus']}->{AA.akus[d]['corpus']}] {s} --{f}--> {d}")
elif mode == "apply":
    W.wire(edges)
    print("APLICADO.")
