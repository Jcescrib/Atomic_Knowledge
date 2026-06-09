# -*- coding: utf-8 -*-
"""_bridge_rechunk.py — re-trocea los lotes fallidos en sub-lotes pequenos.
Lee batchLO..batchHI de outputs/bridges/ y reescribe en outputs/bridges2/ en chunks pequenos.
Uso: python scripts/_bridge_rechunk.py <lo> <hi> <chunk>
"""
import os, sys, json, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lo = int(sys.argv[1]); hi = int(sys.argv[2]); chunk = int(sys.argv[3]) if len(sys.argv) > 3 else 15
src = os.path.join(ROOT, "outputs", "bridges")
dst = os.path.join(ROOT, "outputs", "bridges2")
os.makedirs(dst, exist_ok=True)
for f in glob.glob(os.path.join(dst, "*.json")): os.remove(f)
pairs = []
for i in range(lo, hi + 1):
    p = os.path.join(src, f"batch{i:03d}.json")
    if os.path.exists(p): pairs.extend(json.load(open(p, encoding="utf-8")))
batches = [pairs[i:i+chunk] for i in range(0, len(pairs), chunk)]
for i, b in enumerate(batches):
    json.dump(b, open(os.path.join(dst, f"b{i:03d}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"pares={len(pairs)} chunks={len(batches)} (chunk={chunk})")
