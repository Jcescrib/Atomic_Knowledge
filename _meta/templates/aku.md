---
# ─── IDENTITY ──────────────────────────────────────────────────────────────────
type: aku
aku_class: claim          # claim | method | concept  (required — see CLAUDE.md § AKU classes)
id: aku-REPLACE-WITH-SLUG
statement: >
  Single Spanish-prose proposition; keep technical terms in canonical English
  (CLTV, CAC, ARPU, churn rate, payback, ROI, lifetime, unit economics, ...).
  Statement pattern by class:
    - claim:   "X produce mejor resultado que Y bajo [conditions]."
    - method:  "En [conditions], Z se computa como [formula]."
    - concept: "W es [definition]; incluye [X]; excluye [Y]; implica [Z]."
origin: "Author — Source title  |  or 'personal experience'  |  or 'synthesis'"
domain: [tag-one, tag-two]

# ─── CONFIDENCE ────────────────────────────────────────────────────────────────
llm_confidence: 0.50
# Baseline 0.50 for one source, +0.10 per independent corroborating source (cap 0.95).
# -0.30 on the older claim when a contradiction is found.
# Set to null when epistemic_type is "tacit".

human_certainty:
  status: unvalidated   # unvalidated | validated-true | validated-false | partial | context-dependent
  iterations: 0
  context_boundary: ""  # required for partial / context-dependent
  validated_by: ""
  validation_date: ""   # YYYY-MM or YYYY-MM-DD
  method: ""

# ─── EPISTEMIC TYPE ────────────────────────────────────────────────────────────
epistemic_type: sourced   # sourced | tacit | hybrid

# ─── RELATIONS (maintain bidirectionality for all four pairs) ──────────────────
relations:
  supported_by: []        # ← pair with → supports
  supports: []
  constrained_by: []      # ← pair with → constrains
  constrains: []
  context_breaks_at: []   # ← pair with → breaks_context_of
  breaks_context_of: []
  contradicts: []         # bidirectional (self-pair)
  related: []             # weakest link; retrieval depth limited to 1

# ─── SOURCES (only raw/ files — never another AKU) ─────────────────────────────
sources:
  - raw/FILENAME.md

# ─── LIFECYCLE ─────────────────────────────────────────────────────────────────
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: active           # active | deprecated | merged
status_note: ""          # required when status ≠ active
---

## Relaciones

<!--
Mandatory body section. Mirror every non-empty frontmatter relation here as
[[wikilink]] — Obsidian only draws graph edges from wikilink syntax, not
from YAML. See CLAUDE.md § Body wikilinks.

Format:  **<field>** <arrow> [[target-1]] · [[target-2]] · ...
Arrows:  → outgoing, ← incoming, ↔ symmetric.
Omit empty relations entirely — no placeholder lines.

Example shape (delete this comment and replace):
**supports** → [[aku-target-1]] · [[aku-target-2]]
**constrained_by** ← [[aku-target-3]]
**related** ↔ [[aku-target-4]]
-->
