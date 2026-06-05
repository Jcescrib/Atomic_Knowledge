#!/usr/bin/env bash
# scripts/pipeline.sh — Deterministic phases of the AKU/TAKU ingestion pipeline.
#
# Subcommands:
#   discover     <folder>   List PDFs, EPUBs (recursive) and pre-converted .md
#   convert      <pdf>      Run MinerU; move only .md + images/ to raw/<slug>/;
#                           rewrite image paths flat; discard MinerU scaffolding
#   convert-epub <epub>     Convert an EPUB with ebooklib + BeautifulSoup;
#                           write .md + flat images/ into raw/<slug>/
#   adopt        <markdown> Adopt a pre-converted .md into raw/<slug>/
#                           (auto-detects an adjacent images/ folder)
#   slug         <name>     Print the canonical slug for a name (debug helper)
#
# Image classification, vision analysis, and AKU/TAKU extraction are handled
# by the /pipeline slash command (LLM phases). This script only does the
# deterministic file work that does not require model judgment.
#
# Vault root is computed from this script's location.

set -euo pipefail

VAULT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMP_ROOT="$VAULT_ROOT/outputs/pipeline-temp"
mkdir -p "$TEMP_ROOT" "$VAULT_ROOT/raw"

# Locate the mineru binary. On Windows + user-install pip, the script lives
# in %APPDATA%\Python\Python<ver>\Scripts and is NOT on PATH by default.
find_mineru() {
  if command -v mineru >/dev/null 2>&1; then
    command -v mineru
    return 0
  fi
  local cand
  for cand in \
    "$HOME/AppData/Roaming/Python/Python312/Scripts/mineru.exe" \
    "$HOME/AppData/Roaming/Python/Python313/Scripts/mineru.exe" \
    "$HOME/AppData/Roaming/Python/Python311/Scripts/mineru.exe" \
    "$HOME/AppData/Roaming/Python/Python310/Scripts/mineru.exe" \
    "$HOME/AppData/Local/Programs/Python/Python312/Scripts/mineru.exe" \
    "/c/Python312/Scripts/mineru.exe" \
    "$HOME/anaconda3/Scripts/mineru.exe"; do
    if [ -x "$cand" ]; then
      echo "$cand"
      return 0
    fi
  done
  return 1
}
MINERU_BIN="$(find_mineru || true)"

# ─── helpers ────────────────────────────────────────────────────────────────

slugify() {
  # lower-case, transliterate to ASCII when iconv supports it, hyphenate non-alnum
  local in="$1" out
  if command -v iconv >/dev/null 2>&1; then
    out="$(printf '%s' "$in" | iconv -f utf-8 -t ascii//translit 2>/dev/null || printf '%s' "$in")"
  else
    out="$in"
  fi
  # Note: file extensions are stripped by callers (cmd_convert, cmd_adopt)
  # BEFORE calling slugify, so we do NOT attempt extension stripping here —
  # the prior `s/\.[^.]+$//` was greedy and ate everything after the FIRST
  # dot in names like "2.1-Análisis...". Replace any non-alnum with hyphens
  # and let dots in "2.1" become hyphens naturally.
  printf '%s\n' "$out" \
    | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g; s/--+/-/g'
}

flatten_image_refs() {
  # Rewrite any ![alt](.../images/file.ext) → ![alt](images/file.ext)
  # Works in-place. Uses sed -E (POSIX extended).
  local md="$1"
  sed -i -E 's#!\[([^]]*)\]\([^)]*/images/([^)]+)\)#![\1](images/\2)#g' "$md"
}

# ─── subcommands ────────────────────────────────────────────────────────────

cmd_discover() {
  local folder="${1:-}"
  [ -n "$folder" ] || { echo "ERROR: discover requires a folder path" >&2; exit 1; }
  [ -d "$folder" ] || { echo "ERROR: not a directory: $folder" >&2; exit 1; }

  echo "## PDFs"
  find "$folder" -type f -iname '*.pdf' 2>/dev/null | sort
  echo
  echo "## EPUBs"
  find "$folder" -type f -iname '*.epub' 2>/dev/null | sort
  echo
  echo "## Pre-converted markdowns (candidate sources)"
  find "$folder" -type f -iname '*.md' 2>/dev/null | sort
}

# Decide the raw/ subpath for a source file based on its origin path.
# Nick Kolenda books → raw/libros/kolenda ; Hormozi → raw/libros/hormozi ;
# Jocko Willink → raw/libros/jocko ; Power MBA modules → raw/cursos/power-mba ;
# anything else → raw (root, generic fallback).
raw_subdir_for() {
  local src="$1"
  case "$src" in
    *nickkolenda*|*Kolenda*|*kolenda*) echo "raw/libros/kolenda" ;;
    *HORMOZI*|*Hormozi*|*hormozi*) echo "raw/libros/hormozi" ;;
    *JOCKO*|*Jocko*|*jocko*) echo "raw/libros/jocko" ;;
    *"Apuntes Power MBA"*|*"Power MBA"*) echo "raw/cursos/power-mba" ;;
    *) echo "raw" ;;
  esac
}

cmd_convert() {
  local pdf="${1:-}"
  [ -n "$pdf" ] || { echo "ERROR: convert requires a PDF path" >&2; exit 1; }
  [ -f "$pdf" ] || { echo "ERROR: not a file: $pdf" >&2; exit 1; }

  local base; base="$(basename "$pdf")"
  local name="${base%.[pP][dD][fF]}"
  local slug; slug="$(slugify "$name")"
  local tmp="$TEMP_ROOT/$slug"

  rm -rf "$tmp"
  mkdir -p "$tmp"

  if [ -z "$MINERU_BIN" ]; then
    echo "ERROR: mineru binary not found. Checked PATH and common user-install" >&2
    echo "       locations (AppData/Roaming/Python/Python3xx/Scripts/mineru.exe)." >&2
    echo "       Install or add to PATH, or edit find_mineru() in this script." >&2
    exit 4
  fi

  # -b pipeline: force CPU backend (default hybrid-auto-engine requires CUDA)
  # -l latin:    Latin-alphabet OCR (correct for Spanish/English content;
  #              the MinerU default `-l ch` would degrade accent handling)
  echo "[convert] MinerU ($MINERU_BIN) -b pipeline -l latin → $tmp" >&2
  if ! "$MINERU_BIN" -p "$pdf" -o "$tmp" -b pipeline -l latin; then
    echo "ERROR: MinerU failed for $pdf" >&2
    exit 2
  fi

  # Locate the produced .md and images/ inside the temp output tree.
  local md imgdir
  md="$(find "$tmp" -maxdepth 6 -type f -iname '*.md' 2>/dev/null | head -n 1)"
  imgdir="$(find "$tmp" -maxdepth 6 -type d -name 'images' 2>/dev/null | head -n 1)"

  if [ -z "$md" ]; then
    echo "ERROR: MinerU produced no .md in $tmp" >&2
    echo "Temp tree:" >&2
    find "$tmp" -maxdepth 4 >&2
    exit 3
  fi

  local dest="$VAULT_ROOT/$(raw_subdir_for "$pdf")/$slug"
  mkdir -p "$dest"

  mv "$md" "$dest/$slug.md"
  if [ -n "$imgdir" ]; then
    rm -rf "$dest/images"
    mv "$imgdir" "$dest/images"
  fi

  flatten_image_refs "$dest/$slug.md"

  # Wipe the temp tree entirely — all remaining contents are MinerU
  # scaffolding (middle.json, model.json, content_list*.json, layout.pdf,
  # span.pdf, origin.pdf, etc.) that we do not keep.
  rm -rf "$tmp"

  echo "$dest"
}

# Locate a Python interpreter (python, then python3, then py launcher).
find_python() {
  local cand
  for cand in python python3; do
    if command -v "$cand" >/dev/null 2>&1; then
      command -v "$cand"
      return 0
    fi
  done
  if command -v py >/dev/null 2>&1; then
    echo "py"
    return 0
  fi
  return 1
}

cmd_convert_epub() {
  local ebook="${1:-}"
  [ -n "$ebook" ] || { echo "ERROR: convert-epub requires an EPUB path" >&2; exit 1; }
  [ -f "$ebook" ] || { echo "ERROR: not a file: $ebook" >&2; exit 1; }

  local base; base="$(basename "$ebook")"
  local name="${base%.[eE][pP][uU][bB]}"
  local slug; slug="$(slugify "$name")"
  local dest="$VAULT_ROOT/$(raw_subdir_for "$ebook")/$slug"

  local py; py="$(find_python || true)"
  if [ -z "$py" ]; then
    echo "ERROR: no Python interpreter found (tried python, python3, py)." >&2
    exit 4
  fi

  echo "[convert-epub] ebooklib ($py) → $dest" >&2
  if ! "$py" "$VAULT_ROOT/scripts/epub_to_md.py" "$ebook" "$dest"; then
    echo "ERROR: EPUB conversion failed for $ebook" >&2
    exit 2
  fi

  # epub_to_md.py already writes flat images/<file> refs; flatten again is a
  # harmless idempotent safety net consistent with the PDF/adopt paths.
  flatten_image_refs "$dest/$slug.md"

  echo "$dest"
}

cmd_adopt() {
  local md="${1:-}"
  [ -n "$md" ] || { echo "ERROR: adopt requires a markdown path" >&2; exit 1; }
  [ -f "$md" ] || { echo "ERROR: not a file: $md" >&2; exit 1; }

  local base; base="$(basename "$md")"
  local name="${base%.[mM][dD]}"
  local slug; slug="$(slugify "$name")"
  local dest="$VAULT_ROOT/$(raw_subdir_for "$md")/$slug"
  mkdir -p "$dest"

  cp "$md" "$dest/$slug.md"

  # Look for an adjacent images/ folder under several plausible layouts.
  local src_dir; src_dir="$(dirname "$md")"
  local adopted=""
  local cand
  for cand in \
    "$src_dir/images" \
    "$src_dir/$name/images" \
    "$src_dir/${name}_images" \
    "$src_dir/${name}-images" \
    "$src_dir/img"; do
    if [ -d "$cand" ]; then
      rm -rf "$dest/images"
      cp -r "$cand" "$dest/images"
      adopted="$cand"
      break
    fi
  done

  flatten_image_refs "$dest/$slug.md"

  echo "$dest"
  if [ -n "$adopted" ]; then
    echo "[adopt] images folder copied from: $adopted" >&2
  else
    echo "[adopt] no images/ folder found alongside the markdown" >&2
  fi
}

cmd_slug() {
  slugify "${1:-}"
}

# ─── dispatch ───────────────────────────────────────────────────────────────

cmd="${1:-help}"
shift || true

case "$cmd" in
  discover)     cmd_discover     "$@" ;;
  convert)      cmd_convert      "$@" ;;
  convert-epub) cmd_convert_epub "$@" ;;
  adopt)        cmd_adopt        "$@" ;;
  slug)         cmd_slug         "$@" ;;
  help|*)
    cat <<'USAGE'
scripts/pipeline.sh — AKU/TAKU ingestion pipeline (deterministic phases)

Subcommands:
  discover     <folder>   List PDFs, EPUBs (recursive) and pre-converted .md
  convert      <pdf>      Run MinerU; move only .md+images/ into raw/<slug>/;
                          rewrite image paths flat; discard scaffolding
  convert-epub <epub>     Convert an EPUB (ebooklib + BeautifulSoup); write
                          .md + flat images/ into raw/<slug>/
  adopt        <markdown> Adopt a pre-converted markdown into raw/<slug>/
                          (auto-detects an adjacent images/ folder)
  slug         <name>     Print canonical slug for a name (debug helper)

Image classification, vision analysis, and AKU/TAKU extraction are LLM
phases handled by the /pipeline slash command, not by this script.
USAGE
    ;;
esac
