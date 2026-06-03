---
# ─── IDENTITY ──────────────────────────────────────────────────────────────────
type: taku
taku_type: technique     # technique | case | tool | framework | heuristic | story | protocol | <custom>
id: taku-REPLACE-WITH-SLUG
title: ""
origin: ""
domain: [tag-one, tag-two]

# ─── CONTEXT OF APPLICABILITY ──────────────────────────────────────────────────
when_to_use: ""
when_not_to_use: ""      # required for technique, protocol, tool; optional for case, story

# ─── AKU LINKS (every link carries its own validation state) ───────────────────
aku_links:
  justified_by:          # core: claims that make this TAKU work
    - id: aku-REPLACE
      link_validation: llm-proposed     # llm-proposed | human-validated
      link_note: ""
  constrained_by: []     # scoping conditions (not contradictions)
  breaks_when: []        # conditions where this TAKU stops working
  illustrates: []        # for case / story types
  challenges: []         # AKUs this TAKU's real-world outcomes call into question

# ─── VALIDATION STATE ──────────────────────────────────────────────────────────
content_validation:
  status: llm-authored   # llm-authored | human-reviewed | human-authored
  reviewed_by: ""
  review_date: ""
  review_notes: ""

human_certainty:
  status: unvalidated    # unvalidated | validated-working | validated-failing | context-dependent
  iterations: 0
  context_boundary: ""
  validated_by: ""
  validation_date: ""
  method: ""

# ─── TAKU-TO-TAKU RELATIONS ────────────────────────────────────────────────────
taku_relations:
  complementary: []      # bidirectional
  alternative_to: []     # bidirectional
  precedes:              # directional; inverse goes in the other TAKU's `follows`
    - id: taku-REPLACE
      sequence_type: recommended    # recommended | required
  follows: []            # inverse of precedes; keep in sync

# ─── LIFECYCLE ─────────────────────────────────────────────────────────────────
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: draft            # draft | active | deprecated  (never auto-activate)
status_note: ""
---

<!--
Replace this block with the type-specific body. Pick the section headers for your
declared taku_type. Lint verifies these headers exist.

▸ technique:  ## Summary  ## When to Use  ## Prerequisites  ## Steps
              ## Anti-patterns  ## Expected Outcome  ## Failure Signals
              ## Underlying Logic  ## Notes and Variants

▸ case:       ## Context  ## Situation  ## Actions Taken  ## Outcome
              ## Analysis  ## Lessons  ## What Would Change

▸ tool:       ## Summary  ## Mechanic  ## Input  ## Process  ## Output
              ## Interpretation Guide  ## Limitations  ## Example Application

▸ framework:  ## Summary  ## Core Components  ## How to Apply
              ## Underlying Claims  ## Strengths
              ## Limitations and Criticisms  ## Variants and Extensions

▸ heuristic:  ## The Rule  ## What It Replaces  ## When It Holds
              ## When It Fails  ## Why It Works  ## Calibration

▸ story:      ## The Story  ## What It Illustrates  ## Why This Story  ## Cautions
              (Recommended addition: ## AKU Moment — exact narrative beat that
               instantiates the target AKU)

▸ protocol:   ## Purpose  ## Trigger Conditions  ## Required Resources
              ## Protocol Steps  ## Decision Points  ## Exit Conditions
              ## Failure Handling  ## Review Trigger
-->

## Relaciones

<!--
Mandatory final body section. Mirror every non-empty aku_links.* and
taku_relations.* field as [[wikilink]]. See CLAUDE.md § Body wikilinks.

Format:  **<field>** <arrow> [[target-1]] · [[target-2]] · ...
Arrows:  AKU-link incoming (justified_by, constrained_by) ← ;
         AKU-link outgoing (breaks_when, illustrates, challenges) → ;
         TAKU symmetric (complementary, alternative_to) ↔ ;
         TAKU sequence: precedes → , follows ← .
Omit empty fields entirely.

Example:
**justified_by** ← [[aku-x]] · [[aku-y]]
**constrained_by** ← [[aku-z]]
**breaks_when** → [[aku-w]]
**complementary** ↔ [[taku-a]]
**precedes** → [[taku-b]]
-->
