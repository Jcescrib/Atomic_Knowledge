# -*- coding: utf-8 -*-
"""_kolenda_diag.py — diagnóstico de conectividad del cluster Kolenda. Solo lectura. Temporal."""
import os, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _audit_analyze as AA
akus, F = AA.akus, AA.AKU_FIELDS

# adyacencia no dirigida + corpus de cada vecino
adj = defaultdict(set)
for aid, a in akus.items():
    for f in F:
        for t in a["rel"][f]:
            if t in akus:
                adj[aid].add(t); adj[t].add(aid)

kol = [aid for aid, a in akus.items() if a["corpus"] == "kolenda"]
print(f"Total Kolenda AKUs: {len(kol)}")

# distribución de grado
degdist = Counter(len(adj[a]) for a in kol)
print("\n=== DISTRIBUCION DE GRADO (Kolenda) ===")
for d in sorted(degdist):
    print(f"  grado {d}: {degdist[d]}")
deg0 = [a for a in kol if len(adj[a]) == 0]
deg1 = [a for a in kol if len(adj[a]) == 1]
deg12 = [a for a in kol if len(adj[a]) in (1, 2)]
print(f"\n  grado 0 (huerfanos): {len(deg0)}")
print(f"  grado 1: {len(deg1)}")
print(f"  grado 1-2 (sub-conectados): {len(deg12)}  ({100*len(deg12)//len(kol)}%)")

# ¿conecta Kolenda con otros corpus o es endogamico?
only_intra = 0; has_cross = 0
for a in kol:
    corpora = set(akus[n]["corpus"] for n in adj[a])
    cross = corpora - {"kolenda"}
    if not adj[a]:
        continue
    if cross:
        has_cross += 1
    else:
        only_intra += 1
print("\n=== INTEGRACION CROSS-CORPUS (Kolenda) ===")
print(f"  Kolenda con >=1 enlace a OTRO corpus: {has_cross}")
print(f"  Kolenda enlazado SOLO a otros Kolenda (endogamico): {only_intra}")

# aristas totales que salen de Kolenda, por corpus destino
edge_targets = Counter()
for a in kol:
    for n in adj[a]:
        edge_targets[akus[n]["corpus"]] += 1
print("\n=== DESTINO DE ARISTAS DESDE KOLENDA (conteo de extremos) ===")
for k, v in edge_targets.most_common():
    print(f"  -> {k}: {v}")

# muestra de los grado-1 (los que 'se ven sueltos')
print("\n=== MUESTRA grado-1 (20) ===")
for a in deg1[:20]:
    nb = list(adj[a])[0]
    print(f"  {a}  --[{akus[nb]['corpus']}]--> {nb}")
