# AKU System — Complete Theoretical Specification

> **Document purpose**: This is the canonical seed document for the AKU (Atomic Knowledge Unit) system. It contains everything a person or an LLM agent needs to understand, implement, and operate the system from scratch. No prior context is assumed.

---

## Table of Contents

1. [What This System Is](#1-what-this-system-is)
2. [Core Philosophy](#2-core-philosophy)
3. [What Is an AKU](#3-what-is-an-aku)
4. [AKU Anatomy — Every Field Defined](#4-aku-anatomy--every-field-defined)
5. [Confidence Architecture — Two Independent Dimensions](#5-confidence-architecture--two-independent-dimensions)
6. [Relation Types — The Typed Graph](#6-relation-types--the-typed-graph)
7. [Epistemic Types](#7-epistemic-types)
8. [Knowledge States](#8-knowledge-states)
9. [The Graph — How AKUs Connect](#9-the-graph--how-akus-connect)
10. [Retrieval Logic](#10-retrieval-logic)
11. [Lifecycle of an AKU](#11-lifecycle-of-an-aku)
12. [What the System Is Not](#12-what-the-system-is-not)
13. [Known Risks and Mitigations](#13-known-risks-and-mitigations)
14. [Canonical AKU Example — Fully Annotated](#14-canonical-aku-example--fully-annotated)
15. [Congruence Audit — Design Weaknesses Identified](#15-congruence-audit--design-weaknesses-identified)

---

## 1. What This System Is

The AKU System is a **personal knowledge graph** designed to capture, structure, validate, and retrieve knowledge — including knowledge that has never been written anywhere.

It differs from a traditional note-taking system, a wiki, or a RAG (Retrieval-Augmented Generation) pipeline in one fundamental way: **the unit of knowledge is not a document, not a note, and not a chunk. It is an atomic claim that carries its own validation status.**

The system is built on three premises:

**Premise 1 — Most valuable knowledge is not written.**
The knowledge that creates competitive advantage — sales tactics, negotiation patterns, execution heuristics, business logic — is largely tacit. It lives in practitioners, not in books. A system that only processes written sources is systematically blind to the most valuable knowledge layer.

**Premise 2 — Confidence is not binary.**
A claim is not simply true or false. It has a degree of support from external sources, and a separate degree of personal validation through practice. These two dimensions are independent and must be tracked separately.

**Premise 3 — Context is not a footnote; it is part of the claim.**
A claim that is true in 90% of contexts but false in 10% is not a 90%-true claim. It is a fully true claim with a bounded domain of application. The boundary conditions are structural, not optional metadata.

---

## 2. Core Philosophy

### 2.1 Atomicity

Each AKU contains **exactly one claim**. Not a topic. Not a subject. One falsifiable, actionable proposition.

**Not atomic (wrong):**
> "Jocko Willink's concept of Default Aggressive covers decision-making under uncertainty and the importance of action bias."

**Atomic (correct):**
> "When facing uncertainty, advancing by default produces better outcomes than waiting for perfect information."

The test for atomicity: can this claim be independently validated or falsified? If yes, it is atomic. If it requires another claim to be true in order to be testable, it should be split.

### 2.2 Human Primacy

When a human has validated a claim through direct practice with sufficient iterations, that validation overrides any LLM-derived confidence score. The LLM processes written sources. The human processes reality. When they diverge, reality wins.

### 2.3 The Graph Over the List

AKUs do not live in categories or folders. They live in a graph of typed relations. The meaning of an AKU is not determined by where it is stored, but by what it connects to. An AKU that constrains another AKU, and is supported by two others, and breaks at a fourth — that full cluster is the knowledge unit, not the individual node.

### 2.4 Falsified Knowledge Is Preserved

An AKU that has been tested and found to be false is not deleted. It is marked as `validated-false` and preserved permanently. A falsified AKU with 20 iterations is highly valuable: it is a mapped mine. Without it, any new source can reintroduce the same false claim and the system has no memory that it was already tested.

---

## 3. What Is an AKU

An **Atomic Knowledge Unit (AKU)** is the minimum indivisible piece of knowledge that:

- Contains a single falsifiable claim
- Carries its own confidence metadata (source-based and practice-based, independently)
- Carries its own epistemic type (where does this knowledge come from)
- Carries its own domain of valid application (when does it apply)
- Carries typed relations to other AKUs (what does it support, what constrains it, what does it break at)
- Has a defined lifecycle (from creation through validation or falsification)

An AKU is **not**:
- A summary of a document
- A topic page
- A tag or category
- A technique or procedure (techniques are a separate layer built on top of AKUs)
- A hypothesis without a defined validation method

---

## 4. AKU Anatomy — Every Field Defined

```yaml
---
# ─── IDENTITY ──────────────────────────────────────────────────────────────────
type: aku
# Required. Always "aku". This distinguishes AKUs from other file types
# in the vault (techniques, session logs, synthesis documents, etc.)

id: aku-[slug]
# Required. Globally unique identifier. Format: "aku-" followed by a
# lowercase hyphenated slug derived from the claim.
# Examples: aku-default-aggressive, aku-silence-after-price
# Rules:
#   - Never reuse an ID even if the AKU is deleted
#   - The ID is permanent — it does not change if the statement is refined
#   - All relation references use this ID

statement: >
  Single-sentence claim. Present tense. Falsifiable.
  Must be understandable without reading any other AKU.
# Required. The claim itself.
# Rules:
#   - One claim only. If you need "and", split into two AKUs.
#   - Must be falsifiable in principle (there is a test that could prove it wrong)
#   - Must be actionable or explanatory (not decorative)
#   - Present tense, active voice
#   - Maximum 3 lines. If longer, the claim is not atomic.

origin: "Source name or 'personal experience'"
# Required. Who or what is the original source of this claim.
# If from a book, author + book title.
# If from a course, instructor + course name.
# If from personal practice with no external source: "personal experience"
# If derived from combining multiple sources: "synthesis"
# This is NOT the same as the sources[] list. origin is the intellectual credit.
# sources[] is the list of raw files that contain evidence.

domain: [tag1, tag2, tag3]
# Required. Open taxonomy — any tags are valid.
# Purpose: enables filtering by domain without hierarchical categories.
# Multiple domains are allowed and expected.
# Examples: [sales, negotiation], [decision-making, execution, leadership],
#           [biology, research-methodology], [software-architecture, team-management]
# Rules:
#   - Use lowercase, hyphenated
#   - Be specific enough to be useful, broad enough to enable cross-domain discovery
#   - The same AKU can belong to multiple domains

# ─── CONFIDENCE ────────────────────────────────────────────────────────────────
llm_confidence: 0.82
# The LLM's assessment of how well external written sources support this claim.
# Scale: 0.0 to 1.0
# Baseline rules (applied by the LLM agent):
#   - 1 source, no contradiction:        0.50
#   - Each independent corroborating source: +0.10 (cap at 0.95)
#   - Contradicting claim found:         -0.30 on the older claim
#   - Cap at 0.95 (1.0 is reserved for human-axiom designation only)
# Set to null if epistemic_type is "tacit" (no written sources exist)
# This value is SUBORDINATE to human_certainty when human data is present.

human_certainty:
  status: unvalidated
  # Required. Current validation status. One of:
  #   unvalidated        — No personal testing done yet
  #   validated-true     — Tested in practice, confirmed
  #   validated-false    — Tested in practice, disproven
  #   partial            — True in some conditions, false in others (requires context_boundary)
  #   context-dependent  — Cannot be evaluated without specifying context (requires context_boundary)

  iterations: 0
  # Number of real-world applications of this claim observed by the human.
  # Starts at 0 for unvalidated AKUs.
  # No minimum required for validated-true or validated-false —
  # but low iteration count should be noted in the method field.

  context_boundary: ""
  # Free text. Describes WHEN and WHERE this claim applies and where it breaks.
  # Required if status is "partial" or "context-dependent".
  # Optional but strongly recommended for validated-true and validated-false.
  # Examples:
  #   "Valid in B2B consultive sales, ticket >5k€. Fails with procurement-led processes."
  #   "Applies to teams of 3-15 people. Not observed in teams >30."
  # Note: context_boundary in prose here is for human readability.
  # Structural context breaks are in relations.context_breaks_at[]

  validated_by: ""
  # Name of the person who performed the validation.
  # Typically the system owner. Relevant if the system is used by a team.

  validation_date: ""
  # ISO date or year-month of most recent validation update.
  # Format: YYYY-MM or YYYY-MM-DD

  method: ""
  # Optional. How was this tested?
  # Examples:
  #   "Direct observation in 40 sales calls Q1-Q2 2026"
  #   "A/B test over 3 months, 120 samples"
  #   "Systematic reflection after each client engagement"

# ─── EPISTEMIC TYPE ────────────────────────────────────────────────────────────
epistemic_type: sourced
# Required. Where does this knowledge come from? One of:
#   sourced    — Derived primarily from external written sources.
#                The LLM can evaluate, corroborate, or challenge it.
#   tacit      — Derived from personal practice. No written source exists or applies.
#                llm_confidence must be null.
#                The LLM cannot challenge this on source grounds.
#   hybrid     — External sources suggest it, but personal validation in a
#                specific context has confirmed or refined it.
#                Both llm_confidence and human_certainty are populated.
# This field determines how the system weights the two confidence dimensions.

# ─── RELATIONS ─────────────────────────────────────────────────────────────────
relations:
  supported_by:
    - aku-[id]    # This AKU is explained or reinforced by these AKUs
  # The referenced AKUs provide the mechanism or foundation for this claim.
  # Reading this AKU without its supported_by AKUs leaves the "why" unanswered.

  supports:
    - aku-[id]    # This AKU explains or reinforces these other AKUs
  # Inverse of supported_by. The agent should maintain both directions.

  constrained_by:
    - aku-[id]    # These AKUs limit the scope or application of this AKU
  # The referenced AKUs do not contradict this claim — they define the conditions
  # under which this claim operates. Without reading these, this AKU is incomplete.

  constrains:
    - aku-[id]    # This AKU limits the scope or application of these other AKUs
  # Inverse of constrained_by. Agent should maintain both directions.

  context_breaks_at:
    - aku-[id]    # These AKUs describe conditions where this AKU does NOT apply
  # Critical distinction from constrained_by:
  #   constrained_by = "how to apply this correctly"
  #   context_breaks_at = "when this stops being true entirely"
  # Referenced AKUs are the structural encoding of the context_boundary prose field.

  breaks_context_of:
    - aku-[id]    # This AKU is a breaking condition for these other AKUs
  # Inverse of context_breaks_at. Must be maintained bidirectionally.
  # If AKU-A has context_breaks_at: [aku-B], then AKU-B must have breaks_context_of: [aku-A].
  # Lint enforces this pair exactly like constrained_by/constrains.
  # This makes it navigable in both directions:
  #   From AKU-A: "what breaks my applicability?" → context_breaks_at
  #   From AKU-B: "which AKUs does my condition break?" → breaks_context_of

  contradicts:
    - aku-[id]    # This AKU is in tension with these other AKUs
  # Both claims cannot be true simultaneously in the same context.
  # Contradictions are NOT errors — they are signals of context-dependence or
  # of genuine unresolved tension in the knowledge domain.
  # Contradictions must be reviewed periodically (see Lint).

  related:
    - aku-[id]    # Thematically connected but no typed causal/logical relationship
  # Use when two AKUs share domain, vocabulary, or context but the relationship
  # is associative rather than logical. If a stronger typed relation applies, use that instead.

# ─── SOURCES ───────────────────────────────────────────────────────────────────
sources:
  - raw/[path-to-source-file]
# List of raw source files (not wiki files, not other AKUs) that contain
# the evidence for this claim.
# Rules:
#   - Only raw/ files are valid sources. An AKU cannot cite another AKU as source.
#     (This prevents the closed epistemic loop where the system cites itself.)
#   - Sources are files in the raw/ vault directory: articles, books, transcripts,
#     papers, course notes, interview recordings.
#   - Empty list is valid if epistemic_type is "tacit".

# ─── LIFECYCLE ─────────────────────────────────────────────────────────────────
created: YYYY-MM-DD
# Date the AKU was first created.

updated: YYYY-MM-DD
# Date of last modification to any field.

status: active
# One of: active | deprecated | merged
#   active     — In use, current
#   deprecated — Superseded by a more refined AKU. Kept for traceability.
#                The superseding AKU's ID is noted in the status_note field.
#   merged     — Two AKUs were found to be identical and merged into one.
#                The surviving AKU's ID is noted in the status_note field.

status_note: ""
# Explanation for non-active status. Required if status != active.
---
```

---

## 5. Confidence Architecture — Two Independent Dimensions

### 5.1 The Two Dimensions

Every AKU carries two independent confidence scores:

| Dimension | Field | What it measures | Who sets it | Can be null? |
|---|---|---|---|---|
| Source confidence | `llm_confidence` | How well written sources support the claim | LLM agent | Yes (for tacit AKUs) |
| Practice confidence | `human_certainty.status` | How well personal experience validates the claim | Human | No |

These are **not averaged** into a single score. They are displayed and used separately.

### 5.2 Primacy Rules

**Rule 1 — Human primacy when practice data exists.**
If `human_certainty.status` is anything other than `unvalidated`, the human assessment is the operative confidence signal. The `llm_confidence` score becomes secondary context, not a decision input.

**Rule 2 — LLM confidence is operative only when unvalidated.**
If `human_certainty.status` is `unvalidated`, `llm_confidence` is the only available signal. The retrieval system flags this explicitly: this claim has not been personally tested.

**Rule 3 — Divergence is information.**
When `llm_confidence` is high (e.g., 0.88) but `human_certainty.status` is `validated-false`, this divergence is not an error. It means: the literature supports this claim but it fails in this person's specific context. This is the most valuable kind of knowledge the system can contain — it marks the gap between generic best practices and actual personal reality.

### 5.3 Confidence Decay

Validated-true AKUs do not remain valid indefinitely without renewal. Knowledge becomes stale. The system applies decay according to the following logic:

- AKUs with `status: validated-true` and no update in >365 days are flagged by lint as "confidence review due"
- AKUs with `status: unvalidated` and no activity in >180 days are flagged as "stale — test or deprecate"
- AKUs with `status: validated-false` do not decay — a falsification is permanent unless re-tested

**Source freshness rule (Estructural 3 fix)**: AKUs with `epistemic_type: sourced`, `human_certainty.status: unvalidated`, and `updated` older than 365 days receive a lint flag: "source freshness review due." The `llm_confidence` score is not automatically changed — it remains as computed. But the lint flag forces a human decision: are the original sources still current? If the field has evolved, the sources may no longer be representative, and `llm_confidence` may be overstated. The human must either re-confirm the sources are still valid (update the `updated` date) or mark the AKU for re-evaluation.

Decay does not automatically change confidence values. It generates a lint flag that requires human review. The human decides whether to re-validate, update the date, or deprecate.

### 5.4 The Iteration Weight

The `iterations` count is not used to compute a score automatically, but it provides interpretive context:

- iterations 1–3: preliminary signal, treat with caution
- iterations 4–10: emerging pattern, directionally reliable
- iterations 11–30: established pattern, high personal confidence warranted
- iterations 31+: deeply embedded, should be considered a personal axiom

These thresholds are guidelines, not automatic triggers. Context matters: 5 iterations of a high-stakes irreversible decision carries more weight than 50 iterations of a low-stakes repeatable one.

---

## 6. Relation Types — The Typed Graph

All relations between AKUs are typed. The type of the relation carries semantic meaning that the retrieval system uses to expand a query result into a useful cluster.

### 6.1 Relation Type Definitions

**`supported_by`** / **`supports`** (bidirectional pair)
The mechanical or logical foundation of a claim. If AKU-A is `supported_by` AKU-B, it means: AKU-B explains why AKU-A is true, or provides the underlying mechanism.
Example: "Default Aggressive" is `supported_by` "Decision Fatigue Has Real Cost" — because if decisions cost cognitive energy, postponing them makes the cost cumulative.

**`constrained_by`** / **`constrains`** (bidirectional pair)
A scoping relationship. AKU-B does not contradict AKU-A — it defines the conditions under which AKU-A works correctly.
Example: "Default Aggressive" is `constrained_by` "Minimum Viable Correctable Action" — because advancing without limiting action scope leads to irreversible over-commitment.
Key distinction: constrained_by = "how to apply this correctly without breaking it"

**`context_breaks_at`** (directional)
The conditions under which the claim stops being true. Unlike constrained_by (which tells you how to apply it correctly), context_breaks_at tells you where the claim simply does not hold.
Example: "Default Aggressive" has `context_breaks_at` "Irreversible Decision with Asymmetric Consequences" — because in that context, advancing by default can cause catastrophic, unrecoverable outcomes.
Key distinction: context_breaks_at = "when to stop using this entirely"

**`contradicts`** (bidirectional)
A logical tension between two claims in the same domain. Both cannot be true simultaneously in the same context. Contradictions require either (a) a context boundary that resolves them, or (b) a lint flag marking them as unresolved tension.
Example: "Cold outreach with voice notes outperforms text" contradicts "Written communication allows higher precision in technical contexts"
Note: contradictions between AKUs are not failures of the system. They are honest representations of a reality where different truths apply in different contexts.

**`related`** (bidirectional)
Associative connection without a defined logical relationship. Use when two AKUs share vocabulary, domain, or topic but no causal or logical structure applies.
Treat as the weakest link: if a stronger relation type fits, use that instead. An over-populated `related` list is a signal that deeper structure has not been mapped yet.

**Retrieval depth limit for `related`**: expansion through `related` links has a maximum depth of 1. The system retrieves the directly related AKUs but does not expand their `related` links in turn. This prevents retrieval loops and unbounded cluster growth. All other relation types (supported_by, constrained_by, context_breaks_at, contradicts) expand normally.

### 6.2 Relation Rules

**Bidirectional maintenance**: when AKU-A adds `constrained_by: aku-B`, the agent must also add `constrains: aku-A` to AKU-B. All bidirectional pairs must be kept in sync. The lint operation detects and repairs broken bidirectionality.

**No cross-layer citing in sources**: a relation can reference another AKU. It cannot reference a raw source file. Sources go in the `sources[]` field, not in relations.

**An AKU cannot relate to itself**: trivially true but worth stating for lint rule completeness.

**Relation count as a health signal**:
- An AKU with zero relations: isolated node, likely not yet integrated. Flag for review.
- An AKU with only `related` links and no typed structural links: shallow integration. Flag for deeper mapping.
- An AKU with 10+ `supports` or `supported_by` links: likely a foundational AKU. Consider whether it should be designated as an axiom in the confidence field.

---

## 7. Epistemic Types

### 7.1 `sourced`

The claim derives from external written sources that the LLM agent has processed. The claim exists in books, papers, courses, articles, interviews, or other text-based media.

Implications:
- `llm_confidence` is populated by the LLM based on source corroboration
- The LLM can challenge, refine, or flag contradictions in this claim based on new sources
- Human validation is still required for the claim to move beyond `unvalidated`
- Sources list must be non-empty

### 7.2 `tacit`

The claim derives from personal practice. It has no written source, either because no one has written about it, or because the relevant written material does not capture the specific context in which this claim was validated.

This is the most valuable epistemic type in the system, precisely because it is the least accessible to external tools.

Implications:
- `llm_confidence` must be `null`
- The LLM cannot challenge this claim on source grounds
- The LLM can help articulate, refine, and connect it to other AKUs, but the claim itself is the human's
- Sources list is empty
- `human_certainty.iterations` and `method` are particularly important to populate

### 7.3 `hybrid`

The claim exists in external sources AND has been personally validated in a specific context. The personal context may confirm, refine, or bound the original claim.

This is the richest type: it combines the breadth of sourced knowledge with the specificity of personal practice.

Implications:
- Both `llm_confidence` and `human_certainty` are fully populated
- The human's `context_boundary` may be narrower or different from the general claim in the literature
- If the human validation contradicts the source material, this must be reflected in `human_certainty.status: partial` or `validated-false`, with notes explaining the divergence

**Confidence display rule for `hybrid` AKUs — human always prevails:**

| `human_certainty.status` | Operative confidence in retrieval | Role of `llm_confidence` |
|---|---|---|
| `unvalidated` | `llm_confidence` is the active signal | Primary |
| `validated-true` | Human status prevails | Shown as informational context only |
| `validated-false` | Human status prevails — AKU is false regardless of sources | Shown as informational context only |
| `partial` | Human `partial` is operative; both signals shown without collapsing into one | Shown alongside human status explicitly |
| `context-dependent` | Both signals shown explicitly, marked as unresolved | Shown alongside human status explicitly |

Example retrieval display for a `hybrid` AKU with `status: partial` and `llm_confidence: 0.90`:
> **[PARTIAL — context-dependent]** Human validation: true in context A, false in context B (see context_boundary).
> Source confidence: 0.90 (informational — does not override human assessment).

---

## 8. Knowledge States

An AKU passes through defined states across its lifecycle. These are not just metadata — they determine how the system uses the AKU in retrieval.

### 8.1 `human_certainty.status` Values

> **Terminology note**: AKUs use `validated-true` / `validated-false` because they evaluate **claims about the world** — a claim is either true or false in a given context. TAKUs use `validated-working` / `validated-failing` because they evaluate **procedures** — a procedure works or fails in practice. The difference is intentional and reflects the semantic distinction between the two layers. It is not an inconsistency.

**`unvalidated`**
The AKU has been created (from a source, or from a tacit observation not yet tested systematically). It is available for retrieval but flagged as untested. The system presents it with explicit uncertainty.
Next step: deliberate testing in practice → update to one of the validated states.

**`validated-true`**
The claim has been tested in practice and confirmed. The `context_boundary`, `iterations`, `method`, and `validation_date` fields should all be populated.
Retrieval: full weight, presented as reliable. Flagged for decay review after 365 days.

**`validated-false`**
The claim has been tested in practice and disproven. This AKU is not deleted. It is preserved as a falsification record — a mapped mine.

Retrieval behavior: `validated-false` AKUs are **always included** in domain and situational retrieval alongside valid AKUs. They are never filtered out. This is by design: seeing a falsified claim next to a valid one gives a complete picture of the knowledge landscape, including what has been explored and found unreliable.

Example: a query about negotiation tactics surfaces both `aku-full-transparency-builds-trust` (`validated-false`, 12 iterations) and `aku-strategic-information-control` (`validated-true`, 30 iterations). The system presents both, clearly labeled. The falsified one provides the contrast that makes the valid one more actionable.

Critical: an AKU that is `validated-false` in one context may be `validated-true` in another. The `context_boundary` field captures this. If the falsification is total (no context where it holds), mark it clearly. If partial, use `status: partial` instead.

The `contradicts` relations on a `validated-false` AKU provide the structural explanation of why it is false: the AKUs that contradict it are, by contrast, the claims that have been validated. A `validated-false` AKU with many `contradicts` links from `validated-true` AKUs is self-explaining within the graph.

**`partial`**
The claim is true in some contexts and false in others. The `context_boundary` field is mandatory. The `context_breaks_at` relation should encode the structural version of the boundary.
Retrieval: presented with explicit context-dependence. The retrieval system expands the cluster to include the `context_breaks_at` AKUs.

**`context-dependent`**
The claim cannot be evaluated without specifying context. Different from `partial` — here the evaluation has not yet been done across contexts. The claim is known to be context-sensitive, but the boundaries have not been mapped.
This is a temporary state. Lint flags any AKU that remains `context-dependent` for more than 90 days without progress toward `partial` or one of the validated states.

---

## 9. The Graph — How AKUs Connect

### 9.1 The Graph Is the Knowledge

Individual AKUs are the nodes. The typed relations between them are the edges. The knowledge is not in the nodes alone — it is in the structure of the graph.

This means:
- Retrieving a single AKU is rarely the right answer to a real question
- The answer to "what should I do in situation X" is the **cluster** of AKUs reachable from the most relevant entry node, expanded through the typed relations
- The quality of the system depends heavily on the quality of the relations, not just the quality of the individual claim statements

### 9.2 Cluster Retrieval

When a query matches AKU-A, the system expands to the full cluster:

```
AKU-A (primary match)
  ├── supported_by → AKU-B, AKU-C    (why A is true)
  ├── constrained_by → AKU-D         (how to apply A correctly)
  ├── context_breaks_at → AKU-E      (when A does not apply)
  └── contradicts → AKU-F            (tension to be aware of)
```

The response synthesizes this cluster into a coherent, actionable answer. The primary AKU provides the core claim. The cluster provides the complete operational picture.

### 9.3 Emergent Hierarchy

The system has no predefined hierarchy of importance. A foundational AKU — one that many others point to via `supported_by` — will have high in-degree in the graph. This makes its foundational nature structurally visible without requiring manual categorization.

An AKU that appears in the `supported_by` list of 15 other AKUs is empirically foundational. An AKU with zero incoming links is empirically peripheral. This emerges from the graph without imposed taxonomy.

### 9.4 Contradiction Resolution

When two AKUs are in a `contradicts` relationship, the system does not attempt to resolve the contradiction automatically. It surfaces both, along with their respective `human_certainty` and `context_boundary` fields, and lets the human determine which applies to the current situation.

Contradictions are never silently resolved. If the human finds a resolution (e.g., both are true but in different contexts), the resolution is encoded by:
1. Changing `contradicts` to `context_breaks_at` or `constrained_by` if a logical structure is found
2. Adding explicit `context_boundary` to both AKUs
3. Removing the `contradicts` link and replacing it with the appropriate typed relation

---

## 10. Retrieval Logic

### 10.1 Retrieval Modes

**Direct retrieval** — "Tell me about AKU-X"
Returns the full AKU plus its first-degree cluster (all AKUs directly linked by any relation type).

**Situational retrieval** — "What should I do in situation X?"
The agent finds the most relevant AKUs by semantic match to the situation description, then expands each to its cluster, then synthesizes across clusters. The synthesis prioritizes:
1. AKUs with `validated-true` over `unvalidated`
2. AKUs with `context_boundary` that matches the described situation
3. AKUs with `context_breaks_at` links that match the described situation (these produce warnings, not just information)

**Domain retrieval** — "Show me what I know about domain X"
Filters by `domain` tag, returns all matching AKUs with their confidence states. Useful for auditing what is known, what is unvalidated, and what has been falsified in a given area.

### 10.2 Confidence Display Rules

In any retrieval, the system explicitly labels confidence states:

- `validated-true` + iterations > 10: presented as established personal knowledge
- `validated-true` + iterations 1–10: presented as preliminary personal validation
- `unvalidated` + llm_confidence > 0.7: presented as "well-sourced, not personally tested"
- `unvalidated` + llm_confidence ≤ 0.7: presented as "tentative — low source support, not tested"
- `validated-false`: presented as "FALSIFIED — preserved as negative evidence"
- `partial`: presented as "context-dependent — see boundary conditions"

### 10.3 The Tacit Knowledge Advantage

AKUs with `epistemic_type: tacit` and `validated-true` represent the system's unique competitive advantage. They cannot be recovered from any external source. The retrieval system should explicitly mark them as personal knowledge to distinguish them from externally sourced claims.

---

## 11. Lifecycle of an AKU

### 11.1 Creation

An AKU is created in one of three ways:

**Ingest-triggered creation**: The LLM agent processes a new source file in `raw/`, extracts atomic claims, creates draft AKUs with `epistemic_type: sourced`, `status: unvalidated`, and a `llm_confidence` score based on source analysis.

**Semantic deduplication check at creation (mandatory)**: Before creating any new AKU, the agent must check whether a semantically equivalent AKU already exists in the graph. This is not an optional step — it enforces the atomicity principle. Two AKUs cannot represent the same claim.

Deduplication protocol:
1. Agent compares the candidate statement against all existing active AKU statements semantically (not just string matching).
2. If an equivalent AKU is found: the new source is added to the existing AKU's `sources[]` list and `llm_confidence` is recalculated. No new AKU is created.
3. If a similar but distinct AKU is found: agent flags the pair for human review with a proposed comparison: "These two claims may be equivalent — review and merge if so."
4. If no equivalent exists: proceed to create the new AKU.

This check prevents graph contamination with redundant nodes. Atomicity is a creation constraint, not a post-hoc cleanup task.

**Human-triggered creation**: The human observes a pattern in their own practice, articulates it as an atomic claim, creates the AKU directly with `epistemic_type: tacit` or `hybrid`, and populates the `human_certainty` fields immediately.

**Synthesis-triggered creation**: During a lint or synthesis operation, the agent identifies a pattern across multiple existing AKUs that has not yet been articulated as its own AKU. It proposes a new AKU for human review before creating it.

### 11.2 Validation

After creation, the AKU enters the human's queue for deliberate testing. The human:
1. Tests the claim in relevant real-world situations
2. Updates `iterations` after each observation
3. Updates `status` when a clear pattern emerges
4. Populates `context_boundary` to document where the claim holds and where it breaks
5. Updates `validation_date`

Validation is not a one-time event. A claim that was `validated-true` can be demoted to `partial` or `validated-false` if new contradicting evidence emerges from practice.

### 11.3 Refinement

As the human gains more experience with a claim, they may:
- Narrow the `context_boundary` (make it more specific)
- Add new `context_breaks_at` links as edge cases are discovered
- Add new `constrained_by` links as enabling conditions are identified
- Increase `iterations`
- Upgrade from `partial` to `validated-true` after mapping the full context space

### 11.4 Deprecation

An AKU is deprecated when:
- A more refined AKU supersedes it (the new AKU's ID is recorded in the deprecated AKU's `status_note`)
- Two AKUs are found to be semantically identical and merged
- The claim is found to be so context-specific that it belongs as a `context_boundary` note inside another AKU rather than as an independent claim

Deprecated AKUs are never deleted. They are marked `status: deprecated` and remain in the graph for traceability and historical record.

### 11.5 Permanent Falsification

A `validated-false` AKU with clear, repeated testing is never deprecated unless the falsification itself was wrong (i.e., later testing reveals it is actually true in some contexts). It is a permanent entry in the knowledge map marking territory that has been explored and found unreliable.

---

## 12. What the System Is Not

**Not a document wiki.** The LLM Wiki pattern (Karpathy, 2026) maintains topic pages. The AKU system maintains atomic claims with typed relations. A document wiki page about "negotiation" contains many claims; the AKU system has one file per claim.

**Not a Zettelkasten.** Zettelkasten (Luhmann) uses atomic notes with links, but does not carry confidence metadata, validation status, or typed relation semantics. The AKU system is structurally similar but epistemically richer.

**Not a RAG pipeline.** RAG retrieves document chunks and synthesizes at query time. The AKU system synthesizes at ingest time and retrieves pre-compiled structured knowledge.

**Not a beliefs database.** The system does not track opinions, preferences, or general beliefs. It tracks claims about how the world works, structured as falsifiable propositions.

**Not a task manager.** AKUs are not actions. They inform actions through the techniques layer (defined separately), but they are not themselves executable.

---

## 13. Known Risks and Mitigations

### Risk 1 — Knowledge Base Poisoning
**Description**: If an LLM-authored AKU is treated as a source for future ingest operations, errors compound. The system begins citing its own synthesized claims as evidence for new claims.
**Mitigation**: Hard rule — only `raw/` files are valid entries in the `sources[]` field of any AKU. An AKU cannot cite another AKU as a source. This is enforced by lint.

### Risk 2 — Confidence Drift
**Description**: An AKU validated 3 years ago may no longer reflect current reality, but its `validated-true` status makes it appear reliable.
**Mitigation**: Decay lint flags AKUs with `validated-true` status and `validation_date` older than 365 days. Human must explicitly re-confirm or update.

### Risk 3 — False Atomicity
**Description**: A claim that appears atomic actually contains two embedded claims, one of which is true and one false. The aggregate appears partially validated but the root confusion is structural.
**Mitigation**: Atomicity test at creation: can this claim be independently falsified? If the claim requires a conjunction to be evaluated ("X is true AND Y is true"), it must be split. Lint flags AKU statements containing "and" or "both" or "while" that may indicate compound claims.

### Risk 4 — Unresolved Contradictions
**Description**: Two AKUs in a `contradicts` relationship are left unresolved indefinitely, creating confusion in retrieval.
**Mitigation**: Lint flags contradictions unresolved for more than 30 days. Human must either resolve by adding context boundaries and converting to structural relations, or confirm the contradiction is genuine and document why both coexist.

### Risk 5 — Tacit Knowledge Extraction Failure
**Description**: Tacit knowledge is difficult to articulate at the moment of practice. The capture moment (during action) and the reflection moment (during review) rarely coincide.
**Mitigation**: A lightweight daily capture protocol exists outside the AKU schema: a daily note where observations are logged as rough sentences. The LLM agent processes these daily notes periodically and proposes draft AKUs for human review. The human approves, rejects, or refines.

### Risk 6 — Shallow Relation Mapping
**Description**: AKUs are created but only `related` links are added. The richer structural relations (constrained_by, context_breaks_at, contradicts) are skipped because they require more thought. The graph remains flat and retrieval is shallow.
**Mitigation**: Lint flags AKUs with only `related` links and no typed structural relations after 14 days of existence. These are valid for newly created AKUs but not for established ones.

### Risk 7 — Domain Sprawl
**Description**: With an open domain taxonomy, the same concept gets different domain tags in different AKUs (e.g., "sales", "selling", "B2B-sales"), fragmenting domain-based retrieval.
**Mitigation**: Lint generates a periodic domain vocabulary report showing clusters of similar tags. The human reviews and normalizes. The agent does not auto-normalize domains without human confirmation.

---

## 14. Canonical AKU Example — Fully Annotated

This example contains two fully specified AKUs from a real conceptual cluster, with all fields populated and annotations explaining each decision.

```yaml
# FILE: wiki/akus/aku-default-aggressive.md

---
type: aku
id: aku-default-aggressive
# Slug derived from the claim's core concept. Short, unique, permanent.

statement: >
  When facing uncertainty, advancing by default produces better outcomes
  than waiting for perfect information.
# Atomic: one falsifiable claim. Present tense. Understandable standalone.
# Source concept: Jocko Willink. Refined to make it domain-independent.

origin: "Jocko Willink — Leadership Strategy"
# Credit to originator. Not the same as sources[] which points to raw files.

domain: [decision-making, execution, leadership, uncertainty-management]
# Four domains: this claim is applicable across all of them.
# Open taxonomy: no predefined list required.

llm_confidence: 0.82
# LLM assessed 5 independent sources corroborating this claim.
# Baseline 0.50 + 4 additional sources × 0.10 = 0.90, then -0.08 for one
# partially contradicting source. Final: 0.82.

human_certainty:
  status: validated-true
  # Personally confirmed through practice.

  iterations: 40
  # 40 observed instances. High iteration count. Well-established personal pattern.

  context_boundary: >
    Valid in ~90% of action contexts. Fails in: irreversible decisions with
    high consequence asymmetry, negotiation contexts where initiating first
    reveals preference, regulatory processes with strict sequencing requirements.
  # Prose boundary for human readability. Structural version encoded in
  # context_breaks_at relations below.

  validated_by: "Joan Cepero"
  validation_date: 2026-05
  method: "Systematic observation across project execution, team decisions,
           and client situations over 18 months"

epistemic_type: hybrid
# Sourced (literature supports it) AND personally validated (40 iterations).
# The personal validation has refined and bounded the original claim.

relations:
  constrained_by:
    - aku-minimum-viable-correctable-action
    # This AKU does not contradict Default Aggressive.
    # It defines HOW to advance correctly: limit scope to reversible actions.
    # Reading Default Aggressive without this constraint risks over-application.

  supported_by:
    - aku-decision-fatigue-cost
    # Mechanistic support: if decisions cost cognitive energy, deferring them
    # accumulates cost. This explains WHY advancing by default is efficient.

    - aku-bias-toward-action-outcomes
    # Empirical support: studies showing action-biased decisions outperform
    # analysis-paralysis decisions in uncertain environments.

  context_breaks_at:
    - aku-irreversible-decision-asymmetry
    # STRUCTURAL encoding of the context boundary.
    # When a decision is irreversible AND the downside significantly outweighs
    # the upside, Default Aggressive stops being true entirely.

  related:
    - aku-bias-toward-action-outcomes
    # Associative — shares domain and vocabulary but the logical relationship
    # is already captured in supported_by above. Listed here for completeness.

sources:
  - raw/books/extreme-ownership-willink-2017.md
  - raw/courses/sdracademy-execution-module.md
  - raw/articles/2024-decision-making-uncertainty-mckinsey.md
# Only raw/ files. No other AKUs in this list.

created: 2026-03-15
updated: 2026-05-20
status: active
status_note: ""
---
```

```yaml
# FILE: wiki/akus/aku-minimum-viable-correctable-action.md

---
type: aku
id: aku-minimum-viable-correctable-action

statement: >
  Limiting the scope of an action to the minimum reversible unit reduces
  the cost of execution errors without reducing the value of advancing.
# Atomic. Independently falsifiable. Complements Default Aggressive
# without contradicting it.

origin: "synthesis"
# No single originator. Emerged from combining Default Aggressive with
# risk management literature and personal practice.

domain: [execution, risk-management, decision-making]

llm_confidence: 0.88
# Strong source corroboration from risk management, lean execution,
# and software development (minimum viable product literature).

human_certainty:
  status: validated-true
  iterations: 25
  context_boundary: >
    Applies wherever actions can be scoped. Less applicable in contexts
    where the minimum viable unit is inherently large
    (e.g., regulatory filings, physical infrastructure changes).
  validated_by: "Joan Cepero"
  validation_date: 2026-05
  method: "Applied consistently in project scoping and client commitment decisions"

epistemic_type: hybrid

relations:
  constrains:
    - aku-default-aggressive
    # Inverse of aku-default-aggressive.constrained_by.
    # This AKU limits the scope of Default Aggressive.
    # Agent must maintain both directions in sync.

  supported_by:
    - aku-optionality-value
    # Smaller reversible actions preserve optionality. This explains the mechanism.

    - aku-error-cost-asymmetry
    # In uncertain environments, error costs are often asymmetric (losses hurt
    # more than equivalent gains help). Minimum viable scope limits downside.

  related:
    - aku-default-aggressive
    # Also listed in constrains, but related is maintained for associative
    # discovery across the domain.

sources:
  - raw/books/antifragile-taleb-2012.md
  - raw/books/lean-startup-ries-2011.md
  - raw/articles/2025-reversible-decisions-bezos-framework.md

created: 2026-03-20
updated: 2026-05-20
status: active
status_note: ""
---
```

**Cluster visualization of this example**:
```
[aku-decision-fatigue-cost] ──supports──→
[aku-bias-toward-action]    ──supports──→ [aku-default-aggressive] ──context_breaks_at──→ [aku-irreversible-decision-asymmetry]
                                                     ↑
                                          constrained_by
                                                     │
                                    [aku-minimum-viable-correctable-action]
                                          ↑          ↑
                           supported_by──┘           └──supported_by
                    [aku-optionality-value]    [aku-error-cost-asymmetry]
```

When a query asks "what should I do when I don't have all the information?", the retrieval system returns this full cluster. The answer is not just "advance by default" — it is "advance by default, scoped to the minimum reversible action, unless the decision is irreversible and consequence-asymmetric."

---

## 15. Congruence Audit — Design Weaknesses Identified

The following are identified gaps, tensions, and undefined areas in this specification. Items marked RESOLVED have been fixed in the current version.

### Gap 1 — No defined threshold for iteration count before upgrading status
**Issue**: The spec says human validation drives status, but does not define the minimum iterations required to move from `unvalidated` to `validated-true`. One iteration is technically sufficient but epistemically weak.
**Current state**: Undefined. Left to human judgment.
**Recommendation**: Define soft thresholds per epistemic_type. For `tacit` AKUs (harder to test in controlled conditions): 5+ iterations. For `sourced` AKUs being tested empirically: 3+ iterations. These are guidelines, not hard rules.

### Gap 2 — ~~Bidirectional relation maintenance creates sync risk~~ RESOLVED
**Resolution**: All bidirectional pairs (supported_by/supports, constrained_by/constrains, context_breaks_at/breaks_context_of, contradicts) are now fully defined with their inverses. Lint enforces bidirectionality on all pairs. The `breaks_context_of` inverse of `context_breaks_at` was added to make the graph fully navigable in both directions.

### Gap 3 — The `related` relation type is ambiguous
**Issue**: `related` is defined as "associative connection without a defined logical relationship," which is essentially a placeholder. An overused `related` field defeats the purpose of typed relations.
**Current state**: Retrieval depth limited to 1 for `related` links (Menor 2 fix applied). The risk of indefinite expansion is resolved. The risk of over-use remains.
**Recommendation**: Add a lint rule that flags any `related` link older than 30 days in an active AKU, prompting the human to either (a) convert it to a typed relation, or (b) confirm it is genuinely only associative by marking it `related-confirmed`.

### Gap 4 — No specification for how the LLM agent computes `llm_confidence` consistently
**Issue**: The spec defines baseline rules (0.50 start, +0.10 per corroborating source, etc.) but does not specify how the agent counts independent sources, what counts as corroboration vs. repetition, or how to weight primary sources vs. secondary sources.
**Current state**: Left to LLM judgment, which will vary across sessions.
**Recommendation**: Add an explicit corroboration protocol: (a) sources from the same author/organization count as one source regardless of count, (b) sources that cite a primary source also count as one (only the primary counts), (c) only sources present in `raw/` are counted.

### Gap 5 — ~~The Techniques layer is not yet defined~~ RESOLVED
**Resolution**: The TAKU System Specification defines the full executable layer including techniques, cases, tools, frameworks, heuristics, stories, and protocols.

### Gap 6 — No multi-session conflict resolution protocol
**Issue**: If two LLM sessions write to the same AKU file simultaneously, conflicts occur. With git, this produces merge conflicts. Without git, data is overwritten.
**Current state**: The spec assumes a single active LLM session at a time.
**Recommendation**: Use git as the underlying version control layer. All writes go through a git commit. Concurrent session conflicts appear as merge conflicts and are resolved by the human.

### Gap 7 — `context-dependent` is a fragile state
**Issue**: `context-dependent` is meant to be temporary (lint flags after 90 days), but in practice, some claims may genuinely require extended observation before context boundaries can be mapped. 90 days may be too short for low-frequency situations.
**Current state**: Fixed 90-day flag threshold.
**Recommendation**: Allow the human to extend the timeout per AKU by adding `context_review_date: YYYY-MM-DD` to override the default 90-day lint rule.

### Gap 8 — No capture protocol for tacit knowledge
**Issue**: The specification acknowledges that tacit knowledge must be captured outside the structured AKU schema (during practice) and processed later. But the capture mechanism itself — the daily note protocol, the LLM processing cycle, the approval flow — is not specified here.
**Current state**: Acknowledged in Risk 5 but not specified.
**Recommendation**: Define a daily capture protocol as a companion document. Minimum spec: a `capture/` directory where rough observations are logged as plain sentences; a weekly LLM pass that proposes draft AKUs from `capture/` files; human reviews and approves/rejects.

---

*End of AKU System Specification — v1.0*
*This document is the seed for generating the system. The Techniques layer specification is the required next document.*
