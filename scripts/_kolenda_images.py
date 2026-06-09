# -*- coding: utf-8 -*-
"""Embebe en cada AKU de Kolenda la(s) figura(s) que ilustran su tactica.
Segmentacion ROBUSTA: usa los keywords de tactica (en orden) como unicas fronteras, de modo
que los sub-headers no rompan el segmento. Inserta ![[hash.jpg]] bajo '## Figura' antes de
'## Relaciones'. reset() limpia bloques '## Figura' previos para rehacer."""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def imgs_in(lines):
    out = []
    for l in lines:
        out += re.findall(r"!\[(?:image)?\]\(images/([^)]+)\)", l)
    return out

def map_by_keywords(md_path, ordered):
    """ordered: lista [(slug, keyword)]. Devuelve {slug:[imgs]} usando keywords como fronteras."""
    lines = open(md_path, encoding="utf-8").read().split("\n")
    # localizar la primera linea de header que contiene cada keyword
    pos = []
    for slug, kw in ordered:
        idx = next((i for i, l in enumerate(lines)
                    if re.match(r"^#{1,4}\s", l) and kw.lower() in l.lower()), None)
        pos.append((idx, slug))
    # ordenar por posicion y cortar
    located = sorted([(i, s) for i, s in pos if i is not None])
    res = {}
    for k, (i, slug) in enumerate(located):
        end = located[k+1][0] if k+1 < len(located) else len(lines)
        res[slug] = imgs_in(lines[i:end])
    return res

def reset(slug):
    p = os.path.join(ROOT, "aku", slug + ".md")
    if not os.path.exists(p): return
    txt = open(p, encoding="utf-8").read()
    txt = re.sub(r"## Figura\n.*?\n\n(?=## Relaciones)", "", txt, flags=re.S)
    open(p, "w", encoding="utf-8", newline="\n").write(txt)

def embed(slug, images):
    p = os.path.join(ROOT, "aku", slug + ".md")
    if not images or not os.path.exists(p): return False
    txt = open(p, encoding="utf-8").read()
    if "## Figura" in txt: return False
    block = "## Figura\n\n" + "\n".join(f"![[{img}]]" for img in images) + "\n\n"
    txt = txt.replace("## Relaciones", block + "## Relaciones", 1)
    open(p, "w", encoding="utf-8", newline="\n").write(txt)
    return True

def run(md_rel, ordered):
    for slug, _ in ordered: reset(slug)
    m = map_by_keywords(os.path.join(ROOT, md_rel), ordered)
    done = sum(1 for slug, _ in ordered if embed(slug, m.get(slug, [])))
    miss = [slug for slug, _ in ordered if not m.get(slug)]
    print(f"{md_rel}: figuras en {done}/{len(ordered)} AKUs. Sin imagen: {len(miss)}")
    return m

# ── FONT ── (orden tal como aparecen en la fuente)
FONT_MD = "raw/libros/kolenda/font-psychology-by-nick-kolenda/font-psychology-by-nick-kolenda.md"
FONT = [
 ("aku-font-psychology-las-fuentes-significan-por-congruencia-de-rasgos-concept","Want to choose the right font"),
 ("aku-lineas-finas-y-altas-en-fuentes-transmiten-belleza-claim","Long Thin Lines"),
 ("aku-fuentes-bold-transmiten-poder-y-masculinidad-claim","Bold Fonts Are Powerful"),
 ("aku-fuentes-redondeadas-transmiten-comodidad-y-suavidad-claim","Round Fonts Convey"),
 ("aku-fuentes-simples-transmiten-franqueza-claim","Simple Fonts Convey"),
 ("aku-fuentes-complejas-o-dificiles-de-leer-transmiten-exclusividad-claim","Complex Fonts Convey"),
 ("aku-fuentes-inclinadas-transmiten-velocidad-claim","Slanted Fonts"),
 ("aku-serif-vs-sans-serif-eleccion-segun-medio-y-tono-claim","Serif vs"),
 ("aku-fuentes-condensadas-vs-espaciadas-transmiten-precision-vs-amplitud-claim","Condensed vs"),
 ("aku-fuentes-cortas-vs-altas-transmiten-estabilidad-vs-ligereza-claim","Short Fonts Convey"),
]

if __name__ == "__main__":
    run(FONT_MD, FONT)
