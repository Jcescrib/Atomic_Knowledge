# -*- coding: utf-8 -*-
"""_concept_dump.py — vuelca, por cada concepto canonico, los AKUs (de TODOS los corpus)
cuyo statement/id casa con el patron, para el motor cross-source.

Escribe outputs/_pilot/<concept>_set.json = [{id,corpus,class,statement,linked_to}].
"""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _audit_analyze as AA
from collections import defaultdict

adj = defaultdict(set)
for x, d in AA.akus.items():
    for f in AA.AKU_FIELDS:
        for t in d["rel"][f]:
            if t in AA.akus: adj[x].add(t); adj[t].add(x)

CONCEPTS = {
 "escasez": r"escas|scarcity|limitad|agotad|solo quedan|edici[oó]n limitada|stock|urgenc",
 "prueba-social": r"prueba social|social proof|testimoni|rese[nñ]|popular|la mayor[ií]a|otros (compran|eligen|usan)|consenso|bandwagon|wisdom of",
 "reciprocidad": r"reciprocidad|reciprocity|devolver el favor|favor|obligaci[oó]n de devolver|regalo previo|dar primero",
 "compromiso-consistencia": r"compromiso|consistenc|coheren|commitment|foot-in-the-door|peque[nñ]o s[ií]|micro-?compromiso|publicamente",
 "autoridad": r"autoridad|authority|experto|credencial|experiencia demostrada|t[ií]tulo|bata blanca",
 "simulacion-mental": r"simulaci[oó]n|imagery|imaginar|visualiz|simular (la|la compra)|mental simulation|que el cliente se imagine|proyectarse",
 "fluency": r"fluen|fluidez|f[aá]cil de procesar|f[aá]cil de (leer|pronunciar)|legibilidad|disfluen|procesamiento",
 "framing": r"framing|encuadr|enmarcar|reformul|c[oó]mo se presenta|presentar como|reencuadr",
 "loss-aversion": r"aversi[oó]n a la p[eé]rdida|loss aversion|miedo a perder|dolor de perder|perder.*duele|se siente como (una )?p[eé]rdida",
 "apalancamiento": r"apalancamiento|leverage|escalar sin|sin tiempo adicional|code y media|capital, productos|trabajar una vez",
 "disciplina-ownership": r"disciplina|discipline|extreme ownership|responsabilidad (total|extrema)|asumir la responsabilidad|ownership",
}

os.makedirs(os.path.join(AA.ROOT, "outputs", "_pilot"), exist_ok=True)
for name, pat in CONCEPTS.items():
    rx = re.compile(pat, re.I)
    hits = [a for a, d in AA.akus.items() if rx.search(d["statement"]) or rx.search(a)]
    data = [{"id": a, "corpus": AA.akus[a]["corpus"], "class": AA.akus[a]["aku_class"],
             "statement": AA.akus[a]["statement"][:300], "linked_to": sorted(adj[a])}
            for a in hits]
    json.dump(data, open(os.path.join(AA.ROOT, "outputs", "_pilot", f"{name}_set.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    from collections import Counter
    cc = Counter(AA.akus[a]["corpus"] for a in hits)
    print(f"{name:26s} {len(hits):4d}  {dict(cc)}")
