#!/usr/bin/env bash
# scripts/pipeline.sh — Deterministic phases of the AKU/TAKU ingestion pipeline.
#
# Subcommands:
#   discover <folder>     List PDFs (recursive) and pre-converted .md files
#   convert  <pdf>        Run MinerU; move only .md + images/ to raw/<slug>/;
#                         rewrite image paths flat; discard MinerU scaffolding
#   adopt    <markdown>   Adopt a pre-converted .md into raw/<slug>/
#                         (auto-detects an adjacent images/ folder)
#   slug     <name>       Print the canonical slug for a name (debug helper)
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

# ─── helpers ────────────────────────────────────────────────────────────────

slugify() {
  # lower-case, transliterate to ASCII when iconv supports it, hyphenate non-alnum
  local in="$1" out
  if command -v iconv >/dev/null 2>&1; then
    out="$(printf '%s' "$in" | iconv -f utf-8 -t ascii//translit 2>/dev/null || printf '%s' "$in")"
  else
    out="$in"
  fi
  printf '%s\n' "$out" \
    | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/\.[^.]+$//; s/[^a-z0-9]+/-/g; s/^-+|-+$//g; s/--+/-/g'
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
  echo "## Pre-converted markdowns (candidate sources)"
  find "$folder" -type f -iname '*.md' 2>/dev/null | sort
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

  echo "[convert] MinerU → $tmp" >&2
  if ! mineru -p "$pdf" -o "$tmp"; then
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

  local dest="$VAULT_ROOT/raw/$slug"
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

cmd_adopt() {
  local md="${1:-}"
  [ -n "$md" ] || { echo "ERROR: adopt requires a markdown path" >&2; exit 1; }
  [ -f "$md" ] || { echo "ERROR: not a file: $md" >&2; exit 1; }

  local base; base="$(basename "$md")"
  local name="${base%.[mM][dD]}"
  local slug; slug="$(slugify "$name")"
  local dest="$VAULT_ROOT/raw/$slug"
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
  discover) cmd_discover "$@" ;;
  convert)  cmd_convert  "$@" ;;
  adopt)    cmd_adopt    "$@" ;;
  slug)     cmd_slug     "$@" ;;
  help|*)
    cat <<'USAGE'
scripts/pipeline.sh — AKU/TAKU ingestion pipeline (deterministic phases)

Subcommands:
  discover <folder>     List PDFs (recursive) and pre-converted .md files
  convert  <pdf>        Run MinerU; move only .md+images/ into raw/<slug>/;
                        rewrite image paths flat; discard scaffolding
  adopt    <markdown>   Adopt a pre-converted markdown into raw/<slug>/
                        (auto-detects an adjacent images/ folder)
  slug     <name>       Print canonical slug for a name (debug helper)

Image classification, vision analysis, and AKU/TAKU extraction are LLM
phases handled by the /pipeline slash command, not by this script.
USAGE
    ;;
esac
