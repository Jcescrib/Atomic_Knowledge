#!/usr/bin/env python3
"""One-off migration: reorganise raw/ by origin.

Power MBA course modules  -> raw/cursos/power-mba/<slug>/
Nick Kolenda books        -> raw/libros/kolenda/<slug>/

Classification is deterministic, from _meta/pipeline-manifest.yml:
  original: contains 'nickkolenda'  -> libros/kolenda
  else (all remaining are 'Apuntes Power MBA') -> cursos/power-mba

Updates functional references only: aku/*.md sources[], manifest raw_path:,
.obsidian/workspace.json. Idempotent. Run from the vault root.
"""
import re, glob, os, shutil
from pathlib import Path

VAULT = Path(".").resolve()
MAN = VAULT / "_meta" / "pipeline-manifest.yml"

# --- 1. parse manifest: slug -> original -------------------------------------
man = MAN.read_text(encoding="utf-8")
blocks = re.split(r"\n(?=  - original:)", man)
slug_origin = {}
for b in blocks:
    mo = re.search(r'original:\s*"?(.*?)"?\s*$', b, re.M)
    mr = re.search(r'raw_path:\s*"?(.*?)"?\s*$', b, re.M)
    if mo and mr:
        rp = mr.group(1).strip().strip("/")
        rp = rp[4:] if rp.startswith("raw/") else rp
        slug_origin[rp] = mo.group(1)

def dest_prefix(slug):
    o = slug_origin.get(slug, "")
    if "nickkolenda" in o.lower() or "kolenda" in o.lower():
        return "raw/libros/kolenda"
    return "raw/cursos/power-mba"

# --- 2. snapshot current top-level raw/ folders (exclude new containers) -----
raw = VAULT / "raw"
folders = sorted(
    p.name for p in raw.iterdir()
    if p.is_dir() and p.name not in ("cursos", "libros")
)

# --- 3. create containers + move --------------------------------------------
(raw / "cursos" / "power-mba").mkdir(parents=True, exist_ok=True)
(raw / "libros" / "kolenda").mkdir(parents=True, exist_ok=True)

moved = {"raw/cursos/power-mba": 0, "raw/libros/kolenda": 0}
slug_newprefix = {}
for slug in folders:
    pref = dest_prefix(slug)
    slug_newprefix[slug] = f"{pref}/{slug}/"
    src = raw / slug
    dst = VAULT / pref / slug
    if src.exists() and not dst.exists():
        shutil.move(str(src), str(dst))
        moved[pref] += 1
    elif dst.exists() and not src.exists():
        pass  # already migrated (idempotent)

# --- 4. rewrite functional references ---------------------------------------
def rewrite(path):
    p = Path(path)
    t = p.read_text(encoding="utf-8")
    orig = t
    for slug, newpref in slug_newprefix.items():
        t = t.replace(f"raw/{slug}/", newpref)
    if t != orig:
        p.write_text(t, encoding="utf-8")
        return 1
    return 0

aku_changed = sum(rewrite(f) for f in glob.glob("aku/*.md"))
man_changed = rewrite(str(MAN))
ws = ".obsidian/workspace.json"
ws_changed = rewrite(ws) if os.path.exists(ws) else 0

# --- 5. summary --------------------------------------------------------------
print("folders moved -> cursos/power-mba:", moved["raw/cursos/power-mba"])
print("folders moved -> libros/kolenda :", moved["raw/libros/kolenda"])
print("aku/*.md files rewritten        :", aku_changed)
print("manifest rewritten              :", bool(man_changed))
print(".obsidian/workspace.json rewrite:", bool(ws_changed))
