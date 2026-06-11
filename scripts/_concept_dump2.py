# -*- coding: utf-8 -*-
"""_concept_dump2.py — segunda tanda de conceptos canonicos para el motor cross-source."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _audit_analyze as AA
from collections import defaultdict, Counter

adj = defaultdict(set)
for x, d in AA.akus.items():
    for f in AA.AKU_FIELDS:
        for t in d["rel"][f]:
            if t in AA.akus: adj[x].add(t); adj[t].add(x)

CONCEPTS = {
 "confirmation-bias": r"sesgo de confirmaci|confirmation bias|confirmar (su|sus|la|las) creenc|buscar.*confirmar|interpretaci[oó]n sesgada|motivated reasoning",
 "garantia-risk-reversal": r"garant[ií]a|risk reversal|invertir el riesgo|eliminar.*riesgo|devoluci[oó]n|money.?back|reembolso|sin riesgo|reducir.*riesgo percibido",
 "especificidad": r"specific knowledge|especificidad|especializaci|nicho|especialis|conocimiento espec[ií]fico|ser el mejor en (una|algo)",
 "interes-compuesto": r"inter[eé]s compuesto|compound|compuesto|acumulativ|agregaci[oó]n marginal|bola de nieve|efecto acumul|peque[nñ]as mejoras",
 "identidad": r"identidad|self-?concept|basad[oa] en la identidad|qui[eé]n (eres|quieres ser)|self-?image|auto-?imagen|identity-based",
 "habito-loop": r"h[aá]bito|habit loop|se[nñ]al.*rutina|cue|trigger|rutina-recompensa|bucle del h[aá]bito|automatiz.*conducta",
 "pertenencia-tribu": r"pertenen|tribu|in-?group|encajar|normas sociales|grupo de referencia|sentido de comunidad|belonging",
 "narrativa-story": r"narrativ|storytelling|contar (una )?historia|relato|story\b|historias (venden|persuaden)",
 "contraste-relativo": r"contraste|comparaci[oó]n relativa|context effect|evaluamos.*relativ|efecto de contexto|comparar opciones",
 "largo-plazo-paciencia": r"largo plazo|paciencia|gratificaci[oó]n diferida|juego.*largo|long-?term|diferir.*recompensa|jugar a largo",
 "foco-priorizacion": r"foco|priorizaci|prioridad|prioritize and execute|una sola cosa|lo esencial|enfoc(ar|arse)|menos es m[aá]s",
 "avatar-segmentacion": r"avatar|segmento|segmentaci|cliente ideal|p[uú]blico objetivo|ICP|buyer persona|customer persona|nicho de mercado",
}

os.makedirs(os.path.join(AA.ROOT, "outputs", "_pilot2"), exist_ok=True)
for name, pat in CONCEPTS.items():
    rx = re.compile(pat, re.I)
    hits = [a for a, d in AA.akus.items() if rx.search(d["statement"]) or rx.search(a)]
    data = [{"id": a, "corpus": AA.akus[a]["corpus"], "class": AA.akus[a]["aku_class"],
             "statement": AA.akus[a]["statement"][:300], "linked_to": sorted(adj[a])}
            for a in hits]
    json.dump(data, open(os.path.join(AA.ROOT, "outputs", "_pilot2", f"{name}_set.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    cc = Counter(AA.akus[a]["corpus"] for a in hits)
    print(f"{name:24s} {len(hits):4d}  {dict(cc)}")
