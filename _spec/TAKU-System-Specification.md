# TAKU System — Complete Theoretical Specification
## Tactical Knowledge Units: The Executable Layer

> **Document purpose**: This is the canonical seed document for the TAKU (Tactical Knowledge Unit) system. It defines the layer of executable, procedural, and narrative knowledge that sits above the AKU graph. It contains everything a person or LLM agent needs to understand, implement, and operate this layer from scratch. No prior context is assumed beyond the AKU System Specification.
>
> **Dependency**: This document requires the AKU System Specification. AKUs are the foundational layer. TAKUs are the executable layer built on top. Read the AKU specification first.

---

## Table of Contents

1. [What This Layer Is](#1-what-this-layer-is)
2. [The Relationship Between AKUs and TAKUs](#2-the-relationship-between-akus-and-takus)
3. [What Is a TAKU](#3-what-is-a-taku)
4. [TAKU Types — Open Taxonomy](#4-taku-types--open-taxonomy)
5. [TAKU Anatomy — Every Field Defined](#5-taku-anatomy--every-field-defined)
6. [The AKU–TAKU Link — Validation Architecture](#6-the-akutaku-link--validation-architecture)
7. [Authorship Model — LLM Proposes, Human Validates](#7-authorship-model--llm-proposes-human-validates)
8. [Bidirectional Retrieval](#8-bidirectional-retrieval)
9. [Lifecycle of a TAKU](#9-lifecycle-of-a-taku)
10. [What the System Is Not](#10-what-the-system-is-not)
11. [Known Risks and Mitigations](#11-known-risks-and-mitigations)
12. [Canonical TAKU Examples — Fully Annotated](#12-canonical-taku-examples--fully-annotated)
13. [Congruence Audit — Design Weaknesses Identified](#13-congruence-audit--design-weaknesses-identified)

---

## 1. What This Layer Is

The TAKU layer is the **executable surface of the knowledge system**. Where AKUs answer "what is true about the world," TAKUs answer "what do I do with that truth."

A TAKU is not a claim. It is a structured piece of content — a procedure, a case, a tool, a framework, a story — that encodes knowledge in an actionable or illustrative form. Its defining characteristic is not atomicity (a TAKU can be complex and multi-step) but **traceability**: every TAKU must be explicitly connected to the AKUs that justify, explain, or constrain it.

This traceability creates two things:

**Epistemically grounded practice.** When you follow a technique, you know which underlying claims it rests on. If a technique fails, you can go back and examine whether the underlying AKUs are actually validated in your context, or whether new `context_breaks_at` conditions have been discovered.

**Retrieval depth.** When you ask the system a question, it can answer at two levels simultaneously: the atomic knowledge level (what is true) and the executable level (what to do with it).

The system without TAKUs is a map of claims. The system with TAKUs is a map of claims connected to instruments for navigating reality.

---

## 2. The Relationship Between AKUs and TAKUs

### 2.1 AKUs Are the Foundation, TAKUs Are the Application

```
                    ┌─────────────────────────────────┐
  EXECUTABLE LAYER  │           TAKU Layer             │
                    │  Techniques · Cases · Tools · …  │
                    └────────────────┬────────────────┘
                                     │ justified_by
                                     │ constrained_by_aku
                                     ↓
                    ┌─────────────────────────────────┐
  KNOWLEDGE LAYER   │           AKU Layer              │
                    │     Atomic Knowledge Graph       │
                    └─────────────────────────────────┘
```

The direction of dependency is unambiguous: TAKUs depend on AKUs, not the reverse. An AKU can exist without any TAKU pointing to it. A TAKU without AKUs is an undocumented procedure — it works until it doesn't, with no way to diagnose why.

### 2.2 The Causal Loop

While dependency flows downward (TAKUs depend on AKUs), information flows in both directions:

**Downward (AKU → TAKU)**: The AKU graph determines which TAKUs are applicable to a situation. If you retrieve AKU cluster X, the system surfaces all TAKUs that cite those AKUs as justification.

**Upward (TAKU → AKU)**: When a TAKU is applied in practice and succeeds or fails, that outcome is evidence about the underlying AKUs. A technique that fails repeatedly in a specific context generates a signal that one or more of its supporting AKUs may have a narrower `context_boundary` than previously defined, or may require a new `context_breaks_at` link. The TAKU layer is a real-world testing ground for the AKU layer.

This loop is not automatic. It requires deliberate human review. But the structure makes it explicit: failure of a TAKU is not just a "that didn't work" — it is a diagnostic signal pointing to specific AKUs that may need refinement.

### 2.3 One TAKU, Many AKUs. One AKU, Many TAKUs.

A single TAKU typically draws on multiple AKUs. A sales pitch technique might be justified by AKUs about attention, narrative structure, emotional decision-making, and social proof simultaneously.

A single AKU can underlie many TAKUs across different domains. The AKU "when people make decisions under time pressure, they rely more on heuristics than analysis" might appear in a negotiation technique, a UX design principle, a medical triage protocol, and a crisis communication playbook.

This many-to-many relationship is by design. It is what makes the system compound: adding one well-placed AKU can instantly enrich multiple existing TAKUs.

---

## 3. What Is a TAKU

A **Tactical Knowledge Unit (TAKU)** is a structured content document that:

- Belongs to a defined type (technique, case, tool, or custom extension)
- Contains actionable or illustrative knowledge in a form appropriate to its type
- Is explicitly linked to the AKUs that justify, explain, constrain, or are illustrated by it
- Carries a validation status for both its content (LLM-authored or human-confirmed) and its AKU links (LLM-proposed or human-validated)
- Has a defined domain and context of applicability

A TAKU is **not**:
- An AKU (it is not an atomic claim)
- A source document (it is structured knowledge derived from sources, not the source itself)
- A task or action item (it describes how to act, not a specific action to take)
- A summary (it is structured and typed, not a prose summary of content)

---

## 4. TAKU Types — Open Taxonomy

The TAKU type system is **open**: the base types defined here are the starting point, not the ceiling. Any domain can introduce new types as long as the type follows the structural requirements defined in this document (it has a schema, it links to AKUs, it carries validation metadata).

### Base Types

**`technique`**
A structured procedure for achieving a specific outcome in a defined context. Typically has steps, conditions, anti-patterns, and expected outcomes.
Examples: OREO sales pitch, STAR interview method, 5 Whys root cause analysis, Pomodoro time management, Socratic questioning.

**`case`**
A documented real-world situation with context, actions taken, outcomes, and lessons extracted. Can be first-person (personal experience) or third-party (case studies, historical examples).
Examples: a negotiation that succeeded because of a specific move, a product launch failure and its diagnosis, a clinical case study illustrating a diagnostic pattern.

**`tool`**
An analytical, conceptual, or computational instrument used to process information and generate insights. Has a mechanic (how it works), an input type, an output type, and conditions of appropriate use.
Examples: Pareto analysis for outcome distribution, decision matrix, SWOT analysis, force field analysis, Bayesian updating protocol.

**`framework`**
A structured mental model or organizing schema that is too complex to be a single AKU but is not a procedure. Frameworks organize how to think about a domain rather than what to do.
Examples: Porter's Five Forces, Jobs to Be Done, Cynefin, the Eisenhower Matrix.
Note: a framework is often the source from which multiple AKUs are extracted. The framework TAKU and its derived AKUs coexist — the TAKU provides context and narrative; the AKUs provide the falsifiable claims.

**`heuristic`**
A rule of thumb that is simpler than a technique but more structured than a single AKU. Typically a decision shortcut that works well enough in a defined context without requiring full procedural execution.
Examples: "Never negotiate against yourself," "If in doubt, zoom out," "Name the pattern before analyzing it."
Note: heuristics are close to AKUs but differ in that they are prescriptive ("do this") rather than descriptive ("this is true"). If an AKU could be reformulated as a heuristic, both forms can coexist — the AKU encodes the claim, the heuristic TAKU encodes the actionable form.

**`story`**
A narrative piece — anecdote, parable, metaphor, historical account — that illustrates one or more AKUs in a memorable, transmissible form. Not a case (which is analytical); a story is chosen for its illustrative or rhetorical power.
Examples: the Hedgehog Concept from Jim Collins, the boiling frog metaphor, a founder's story about a pivotal decision.

**`protocol`**
A formal, often sequential procedure used in high-stakes or high-precision contexts where deviation from the sequence has significant consequences. More rigid than a technique.
Examples: clinical assessment protocols, security incident response protocols, scientific experimental protocols, pre-flight checklists.

**`[custom]`**
Any type not listed here. To introduce a custom type, define it in the vault's `CLAUDE.md` schema file with: type name, description, mandatory fields, optional fields, and AKU link requirements. The agent will then apply that schema consistently.

---

## 5. TAKU Anatomy — Every Field Defined

The TAKU schema has two sections: a **universal frontmatter** that applies to all types, and a **type-specific body** that varies by type. The frontmatter is structured (YAML). The body is Markdown prose with defined section headers for each type.

### 5.1 Universal Frontmatter

```yaml
---
# ─── IDENTITY ──────────────────────────────────────────────────────────────────
type: taku
# Required. Always "taku". Distinguishes from AKUs and raw source files.

taku_type: technique
# Required. The TAKU type from the open taxonomy.
# Core types: technique | case | tool | framework | heuristic | story | protocol
# Custom types: any string defined in CLAUDE.md

id: taku-[slug]
# Required. Globally unique identifier. Format: "taku-" followed by a
# lowercase hyphenated slug.
# Examples: taku-oreo-pitch, taku-pareto-outcome-analysis, taku-star-interview
# Permanent — does not change if content is revised.

title: ""
# Required. Human-readable title. Can be updated as the TAKU is refined.
# Examples: "OREO Pitch Technique", "Pareto Analysis for Outcome Distribution"

origin: ""
# Required. Who or what is the original source of this content.
# Same rules as AKU origin field.

domain: [tag1, tag2]
# Required. Open taxonomy. Same rules as AKU domain field.

# ─── CONTEXT OF APPLICABILITY ──────────────────────────────────────────────────
when_to_use: ""
# Required. Plain text description of the situations where this TAKU is applicable.
# Be specific: audience, context, objective, constraints.
# Examples:
#   "B2B sales pitch, 5–15 minute slot, mixed technical and business audience"
#   "Root cause analysis after a process failure with multiple contributing factors"

when_not_to_use: ""
# Required for technique, protocol, tool types. Optional for case, story.
# Anti-patterns: situations where this TAKU is inapplicable or counterproductive.

# ─── AKU LINKS ─────────────────────────────────────────────────────────────────
aku_links:
  justified_by:
    - id: aku-[id]
      link_validation: llm-proposed   # llm-proposed | human-validated
      link_note: ""
      # The AKUs whose truth makes this TAKU effective or appropriate.
      # This is the primary link type: "this technique works because these claims are true."
      # link_validation: who established this link (see Section 6 for full explanation)
      # link_note: optional explanation of why this specific AKU justifies this TAKU

  constrained_by:
    - id: aku-[id]
      link_validation: llm-proposed
      link_note: ""
      # AKUs that define the conditions under which this TAKU applies correctly.
      # Similar to AKU constrained_by: not a contradiction, a scoping condition.

  breaks_when:
    - id: aku-[id]
      link_validation: llm-proposed
      link_note: ""
      # AKUs describing conditions where this TAKU stops working.
      # When these AKU conditions are true, do not use this TAKU.

  illustrates:
    - id: aku-[id]
      link_validation: llm-proposed
      link_note: ""
      # For case and story types: which AKUs does this narrative illustrate?
      # The TAKU provides the concrete instance; the AKU provides the generalized claim.

  challenges:
    - id: aku-[id]
      link_validation: llm-proposed
      link_note: ""
      # AKUs that this TAKU's real-world outcomes have called into question.
      # Used when applying the TAKU has generated evidence that may refine or
      # falsify one of the underlying AKUs. This is the upward feedback loop.

# ─── VALIDATION STATE ──────────────────────────────────────────────────────────
content_validation:
  status: llm-authored
  # Who authored and validated the content of this TAKU.
  # One of:
  #   llm-authored      — LLM generated the structure and content. Not yet
  #                       reviewed or confirmed by a human. Lower epistemic weight.
  #   human-reviewed    — A human has read and confirmed the content is accurate
  #                       and useful. The structure reflects real knowledge.
  #   human-authored    — The human wrote this TAKU directly (e.g., personal technique
  #                       never found in any source). Highest epistemic weight.

  reviewed_by: ""
  review_date: ""
  review_notes: ""
  # If status is human-reviewed or human-authored, populate these fields.

human_certainty:
  status: unvalidated
  # Has this TAKU been applied in practice?
  # One of: unvalidated | validated-working | validated-failing | context-dependent
  #
  # Terminology note: TAKUs use "validated-working" / "validated-failing" rather than
  # "validated-true" / "validated-false" (which AKUs use). This is intentional:
  # AKUs evaluate claims about the world (true or false).
  # TAKUs evaluate procedures (they work or they fail in practice).
  # The distinction is semantic, not an inconsistency between the two layers.
  iterations: 0
  context_boundary: ""
  validated_by: ""
  validation_date: ""
  method: ""
  # Same semantics as AKU human_certainty. A TAKU that has been applied
  # many times in practice carries more weight than one that has never been used.

# ─── TAKU-TO-TAKU RELATIONS ────────────────────────────────────────────────────
taku_relations:
  complementary:
    - taku-[id]
    # TAKUs that work better when applied together with this one.
    # Complementary TAKUs address the same situation from different angles,
    # or cover different phases of the same problem.
    # Using one without the other is valid but produces partial results.
    # Example: taku-oreo-pitch is complementary to taku-discovery-questions —
    # discovery informs the Opinion; OREO delivers it.
    # Relation is bidirectional: if A lists B as complementary, B lists A.

  alternative_to:
    - taku-[id]
    # TAKUs that address the same goal or situation with a different approach.
    # When multiple alternatives exist, retrieval surfaces all of them.
    # The practitioner chooses based on context, preference, or validated performance.
    # Example: taku-oreo-pitch and taku-problem-agitate-solve both structure
    # a persuasive argument — different mechanics, same objective.
    # Relation is bidirectional: if A lists B as alternative, B lists A.

  precedes:
    - id: taku-[id]
      sequence_type: recommended   # recommended | required
    # TAKUs that should be applied before this one in a sequence.
    # sequence_type: required — this TAKU cannot produce valid results without
    #   the preceding TAKU having been applied first. Hard dependency.
    # sequence_type: recommended — applying the preceding TAKU improves outcomes
    #   but this TAKU can be used independently. Soft dependency.
    # Example required: a diagnostic protocol that requires a prior assessment TAKU.
    # Example recommended: taku-discovery-questions before taku-oreo-pitch.
    # This is a directional relation: A precedes B means A comes first.
    # The inverse (B follows A) must be encoded in the other TAKU's follows field.

  follows:
    - id: taku-[id]
      sequence_type: recommended   # recommended | required
    # TAKUs that should be applied after this one in a sequence.
    # Inverse of precedes. Both directions must be maintained in sync.
    # Lint verifies bidirectionality: if A.precedes includes B,
    # then B.follows must include A with the same sequence_type.
    # Example: taku-oreo-pitch follows taku-discovery-questions (recommended).

# ─── LIFECYCLE ─────────────────────────────────────────────────────────────────
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: active
# One of: active | deprecated | draft
#   draft      — LLM has generated initial content, awaiting human review
#   active     — In use, current, passed at least basic human review
#   deprecated — Superseded or found to be consistently ineffective
status_note: ""
---
```

### 5.2 Type-Specific Body Structure

Each TAKU type has a defined Markdown body structure. The agent must use these section headers for consistency, which enables lint to verify structural completeness.

---

#### Body: `technique`

```markdown
## Summary
One paragraph. What this technique is and what it achieves.

## When to Use
Expand on the frontmatter when_to_use field with narrative context.

## Prerequisites
What knowledge, preparation, or conditions must be in place before applying this technique.
Reference relevant AKUs: the practitioner should have [[aku-X]] as validated-true before relying on this technique.

## Steps
Numbered. Each step is an action, not a description.
1. Step one: verb-object format. Specific enough to execute.
2. Step two...
[Continue as needed. No minimum or maximum step count.]

## Anti-patterns
Common ways this technique is misapplied, with explanation of why they fail.
- Anti-pattern 1: description + why it fails
- Anti-pattern 2: ...

## Expected Outcome
What success looks like. How to know the technique worked.

## Failure Signals
How to recognize the technique is not working in this application.
What to do when failure signals appear.

## Underlying Logic
Explain WHY this technique works by reference to its AKU links.
Do not just list the AKUs — explain the causal chain:
"This technique works because [aku-X] is true, which means that [mechanism],
which produces [outcome]."

## Notes and Variants
Optional. Known variations, domain-specific adaptations, evolution of the technique.
```

---

#### Body: `case`

```markdown
## Context
Who, what, when, where. Enough background to understand the situation.
For personal cases: anonymize third parties if necessary.
For third-party cases: cite the source in the sources[] field.

## Situation
The specific challenge, decision point, or problem that required action.

## Actions Taken
What was done. Chronological if relevant. Factual, not interpretive.

## Outcome
What happened. Quantify where possible. Include unexpected results.

## Analysis
Why the outcome occurred. Which AKUs were confirmed or challenged.
This is the analytical layer: connect the case to the knowledge graph.

## Lessons
What generalized claims this case supports, challenges, or illustrates.
Reference the AKUs in the aku_links.illustrates and aku_links.challenges fields.

## What Would Change
Optional. With current knowledge, what would be done differently.
```

---

#### Body: `tool`

```markdown
## Summary
What this tool does and what type of problem it addresses.

## Mechanic
How the tool works. The underlying logic or algorithm.
Not how to use it yet — why it works.

## Input
What information or data is required to use this tool.
Be specific about format, quality, and quantity requirements.

## Process
Step-by-step application of the tool.
1. Step one...
2. Step two...

## Output
What the tool produces. How to read and interpret the output.

## Interpretation Guide
How to act on the output. Common misinterpretations and how to avoid them.

## Limitations
What this tool cannot do or where it produces misleading output.
Reference breaks_when AKUs here.

## Example Application
A worked example showing the tool applied to a real or realistic situation.
```

---

#### Body: `framework`

```markdown
## Summary
What this framework is and what it helps organize or decide.

## Core Components
The elements of the framework and how they relate.
Use diagrams where helpful (Mermaid or ASCII).

## How to Apply
Practical guide to using the framework in real situations.

## Underlying Claims
Explain which AKUs this framework is built on.
A framework is often the synthesized form of multiple AKUs — make the
individual claims visible.

## Strengths
What this framework does better than alternatives.

## Limitations and Criticisms
Where the framework oversimplifies, misses important factors, or has been
disputed. Reference challenging evidence.

## Variants and Extensions
Known adaptations of the framework for specific domains.
```

---

#### Body: `heuristic`

```markdown
## The Rule
State the heuristic in the most compact, memorable form.
"[Trigger condition] → [Action]"

## What It Replaces
What slower, more complex reasoning process does this heuristic shortcut?

## When It Holds
The conditions under which this heuristic reliably produces good outcomes.

## When It Fails
The conditions under which following this heuristic leads to bad outcomes.
Reference breaks_when AKUs.

## Why It Works
The underlying mechanism. Which AKUs make this heuristic reliable?

## Calibration
How to know if you are applying this heuristic appropriately vs. inappropriately.
```

---

#### Body: `story`

```markdown
## The Story
The narrative. Write for memorability and clarity of illustration.
First person if personal. Third person if external.

## What It Illustrates
Which AKUs does this story make concrete?
"This story is a memorable instance of [aku-X]: [brief explanation of the connection]."

## Why This Story
Why this particular story is a good illustration of the target AKUs.
What makes it sticky, transferable, or persuasive.

## Cautions
Limitations of the illustration. Where the story might mislead if taken literally
beyond its intended scope.
```

---

#### Body: `protocol`

```markdown
## Purpose
What this protocol is designed to achieve or prevent.

## Trigger Conditions
The specific conditions under which this protocol must be initiated.

## Required Resources
Personnel, tools, information, or authority required before starting.

## Protocol Steps
Numbered. Strictly sequential. Each step includes:
- Action (what to do)
- Responsible party (who does it)
- Verification (how to confirm it is complete before proceeding)

1. [Action] | [Responsible] | [Verification]
2. ...

## Decision Points
Steps where the protocol branches based on conditions.
Document each branch explicitly.

## Exit Conditions
When the protocol is complete. What constitutes successful execution.

## Failure Handling
What to do if the protocol cannot be completed as specified.

## Review Trigger
When and why this protocol should be reviewed and updated.
```

---

## 6. The AKU–TAKU Link — Validation Architecture

This section defines one of the most important design decisions in the system: the two-tier validation of AKU links within TAKUs.

### 6.1 The Problem

When the LLM agent authors a TAKU from a raw source, it also proposes which AKUs are linked to it. This proposal is based on semantic analysis — the LLM identifies which existing AKUs seem relevant to the TAKU's content. This is useful but not infallible. The LLM may:
- Link to an AKU that is semantically similar but logically unrelated
- Miss a more relevant AKU that exists in the graph
- Propose a link that is technically valid but epistemically weak

This means AKU links inside TAKUs have two distinct validation states that must be tracked separately.

### 6.2 Link Validation States

**`llm-proposed`**
The LLM identified this link during authoring or processing. The link has not been reviewed by a human. It is available for retrieval but carries lower epistemic weight.

In retrieval, `llm-proposed` links are surfaced but flagged: *"This connection was proposed by the LLM and has not been human-validated."*

**`human-validated`**
A human has explicitly confirmed that this AKU correctly justifies, constrains, illustrates, or is challenged by this TAKU. This link is fully operational in retrieval with no flags.

### 6.3 Why This Matters

Consider a technique for managing conflict in teams. The LLM might propose that it is `justified_by` an AKU about social dynamics in groups. A human who has actually used the technique might recognize that the real justification is an AKU about cognitive load under stress — a more precise and useful connection. The `llm-proposed` tag is the system's way of saying: "this is a starting point, not a conclusion."

### 6.4 The Validation Queue

Any TAKU with one or more `llm-proposed` links should appear in the system's validation queue — a lint-generated list of pending human reviews. The human reviews each proposed link and either:
- Confirms it → changes `link_validation: human-validated`
- Rejects it → removes the link
- Replaces it → removes the link and adds the correct one with `human-validated`

There is no urgency requirement. A TAKU can operate with `llm-proposed` links indefinitely. But the system makes the distinction visible at all times.

### 6.5 Interaction with TAKU Content Validation

The two validation dimensions (content and links) are independent:

| Content Status | Link Status | Meaning |
|---|---|---|
| `llm-authored` | `llm-proposed` | Fully unreviewed. Use with caution. |
| `human-reviewed` | `llm-proposed` | Content is reliable, but connections to AKU graph are uncertain. |
| `llm-authored` | `human-validated` | Content unreviewed but connections are correct. |
| `human-reviewed` | `human-validated` | Fully validated. Highest epistemic weight. |
| `human-authored` | `human-validated` | Human expertise, human connections. System maximum. |

---

## 7. Authorship Model — LLM Proposes, Human Validates

### 7.1 The Standard Authorship Flow

When a new raw source is ingested, the LLM agent:

1. Reads the source completely
2. Identifies actionable procedures, tools, techniques, frameworks, or narrative cases
3. For each identified piece of content, determines the appropriate TAKU type
4. Drafts the TAKU using the type-specific body structure
5. Sets `content_validation.status: llm-authored`
6. Searches the AKU graph for relevant AKUs and proposes links with `link_validation: llm-proposed`
7. Sets the TAKU `status: draft`
8. Adds the TAKU to a review queue for the human

The human then:
1. Reviews the draft TAKU
2. Edits content if necessary
3. Validates or replaces AKU links
4. Changes `content_validation.status` to `human-reviewed` or `human-authored`
5. Changes `link_validation` on confirmed links to `human-validated`
6. Changes TAKU `status` to `active`

### 7.2 Human-First Authorship

For tacit knowledge — techniques the practitioner has developed through experience that are not in any source — the human authors the TAKU directly:

1. Human writes the TAKU content using the type-specific body structure
2. Sets `content_validation.status: human-authored`
3. Requests LLM assistance to propose AKU links: "Review this technique and propose which AKUs in the graph support or constrain it"
4. LLM proposes links with `link_validation: llm-proposed`
5. Human validates links → `human-validated`

This mirrors the tacit AKU pattern: the human's practice is the source of truth; the LLM helps integrate it into the existing knowledge structure.

### 7.3 No Auto-Publishing

The agent must never automatically set a TAKU to `status: active`. All transitions to `active` require human confirmation. This is a hard rule.

The agent can create, draft, and propose. The human activates.

---

## 8. Bidirectional Retrieval

### 8.1 The Two Retrieval Directions

The system supports queries in both directions across the AKU–TAKU graph. Neither direction is primary — both are equally valid entry points depending on what the practitioner needs.

**Direction 1 — Concept to Practice (AKU → TAKU)**
Entry: a question, situation, or concept
Process: retrieve relevant AKUs → expand AKU cluster → surface all TAKUs linked to cluster AKUs
Output: atomic knowledge + executable instruments

Triggered by questions like:
- "What should I do in situation X?"
- "What techniques do we have for domain Y?"
- "What validated knowledge do we have about persuasion, and what tools implement it?"

**Direction 2 — Practice to Concept (TAKU → AKU)**
Entry: a specific technique, tool, or case
Process: retrieve the TAKU → expand its AKU links → surface the full AKU cluster that justifies it
Output: the knowledge foundation of the practice

Triggered by questions like:
- "Why does technique X work?"
- "What concepts underlie the OREO pitch?"
- "This tool failed — what assumptions was it resting on?"

### 8.2 Retrieval Response Structure

For both directions, the retrieval response is structured in two explicit sections:

```
RETRIEVAL RESULT FOR: [query]

═══════════════════════════════════════════════════
KNOWLEDGE LAYER — AKUs
═══════════════════════════════════════════════════
[List of relevant AKUs with their validation status]
[For each AKU: statement + human_certainty.status + key context_boundary]
[AKU cluster relations explained]
[Any validated-false AKUs in this domain — presented as negative evidence]

═══════════════════════════════════════════════════
EXECUTABLE LAYER — TAKUs
═══════════════════════════════════════════════════
[List of relevant TAKUs with their type and validation status]
[For each TAKU: title + when_to_use + content_validation status]
[Ordered by validation: human-authored/reviewed first, llm-authored last]
[Explicit flag on any TAKU with llm-proposed (unvalidated) AKU links]
```

### 8.3 Validation Transparency in Retrieval

Retrieval never silently omits unvalidated content. Instead, it presents a complete picture with explicit validation markers:

- ✓ `human-validated` — personal practice confirmed
- ◎ `llm-proposed` / `unvalidated` — sourced but not personally tested
- ✗ `validated-false` — tested and found incorrect (preserved as negative evidence)
- ○ `draft` — generated, not yet reviewed

This transparency is non-negotiable. The system must never present an unvalidated claim or technique with the same weight as a validated one.

### 8.4 Failure Diagnosis Retrieval

A specialized retrieval mode triggered when a TAKU has been applied and failed:

Input: TAKU ID + context description of the failure
Process:
1. Retrieve the TAKU's full AKU link cluster
2. For each `justified_by` AKU: check if the failure context matches any `context_breaks_at` conditions
3. For each `constrained_by` AKU: check if the constraint was satisfied in the failing context
4. Propose which AKU's `context_boundary` may need refinement based on the failure
5. Propose a new `breaks_when` link to add to the TAKU

Output: diagnostic report with specific AKUs to review, proposed refinements, and a draft of the new link to add.

This mode makes the upward feedback loop (TAKU practice → AKU refinement) explicit and actionable.

---

## 9. Lifecycle of a TAKU

### 9.1 Creation

TAKUs are created through one of three paths:

**Ingest-triggered**: LLM processes a raw source, identifies structured knowledge, drafts the TAKU. Status: `draft`, content: `llm-authored`.

**Human-triggered**: Practitioner creates a TAKU from personal experience or observation. Status: `draft` (or immediately `active` if complete), content: `human-authored`.

**Synthesis-triggered**: During a lint or synthesis pass, the LLM identifies that multiple AKUs in a cluster together imply an executable procedure not yet encoded as a TAKU. It proposes a draft for human review. Status: `draft`, content: `llm-authored`.

### 9.2 Activation

A TAKU moves from `draft` to `active` when a human has:
- Reviewed the content and confirmed it is accurate and well-structured
- Changed `content_validation.status` from `llm-authored` to `human-reviewed` (or left `human-authored`)
- Reviewed at least the primary AKU links (does not require validating all links before activation)
- Explicitly set `status: active`

### 9.3 Iteration

After activation, TAKUs improve through use:

- `human_certainty.iterations` increases with each application
- `human_certainty.status` updates from `unvalidated` to `validated-working` or `validated-failing`
- `context_boundary` is refined as edge cases are discovered
- `breaks_when` links are added when new failure conditions are identified
- `challenges` links are added when the TAKU's outcomes generate evidence about its underlying AKUs

### 9.4 Deprecation

A TAKU is deprecated when:
- It has been consistently `validated-failing` and no refinement resolves the failure
- A superior TAKU supersedes it (record the successor TAKU ID in `status_note`)
- The domain or context it addresses has changed enough that the TAKU no longer applies

Deprecated TAKUs are not deleted. They are marked `status: deprecated` and remain in the graph for traceability. A deprecated TAKU that was `validated-failing` is particularly valuable: it is a documented approach that does not work, preventing its rediscovery and re-application.

---

## 10. What the System Is Not

**Not a procedures database.** Standard Operating Procedures (SOPs) in an organization are prescriptive and enforced. TAKUs are knowledge assets: they encode what is known to work, but applying them is always discretionary based on context.

**Not a training curriculum.** A curriculum sequences content for learning. The TAKU layer is unordered — content is retrieved by relevance to a situation, not by pedagogical sequence.

**Not a project management tool.** TAKUs describe how to act; they do not track whether action has been taken, by whom, or when.

**Not a substitute for the AKU layer.** A TAKU with no AKU links is a documented procedure without an epistemological foundation. It may work, but the system cannot explain why, diagnose failures, or improve it systematically. Every active TAKU should have at least one human-validated AKU link.

---

## 11. Known Risks and Mitigations

### Risk 1 — Technique Graveyard
**Description**: Many TAKUs are created, reach `active` status, and are never applied. The system accumulates a large library of techniques with `human_certainty.status: unvalidated` that look valid but have never been tested.
**Mitigation**: Lint flags active TAKUs with `human_certainty.status: unvalidated` and `created` date older than 90 days. These are not errors — they are prompts: "You have this tool. Have you used it?"

### Risk 2 — Link Inflation
**Description**: The LLM proposes too many AKU links for each TAKU, connecting it to every marginally related AKU. The result is an over-connected graph where retrieval returns too much content.
**Mitigation**: Quality over quantity rule: a TAKU should have 2–5 primary `justified_by` links representing the core causal claims. More than 7 `justified_by` links is a signal that the TAKU is trying to cover too much ground, or that the AKU graph has redundant nodes. Lint flags TAKU files with >7 `justified_by` links for human review.

### Risk 3 — Conflation of Content and Link Validation
**Description**: A TAKU with `content_validation: human-reviewed` is mistakenly treated as fully validated, ignoring that its AKU links may all be `llm-proposed`.
**Mitigation**: Retrieval always surfaces both validation states independently. The combined state table in Section 6.5 is the operative reference. A TAKU is only fully validated when both content and all primary links are human-validated.

### Risk 4 — Type Misclassification
**Description**: A case is filed as a technique, or a heuristic is filed as a protocol. Type misclassification breaks the body structure expectations and confuses retrieval.
**Mitigation**: Lint validates that each TAKU body contains the required section headers for its declared type. Missing required sections are flagged as structural errors.

### Risk 5 — Outdated TAKUs
**Description**: A technique that was `validated-working` five years ago may no longer work in a changed context (market conditions, technology, audience). But its validation status persists.
**Mitigation**: Decay lint flags TAKUs with `validated-working` and `validation_date` older than 365 days, same as AKUs. Human must re-confirm or note in `context_boundary` that the validation date is still current.

### Risk 6 — Upward Feedback Loop Not Closing
**Description**: TAKUs fail in practice, but the failure is never used to refine the underlying AKUs. The loop between practice and knowledge degrades.
**Mitigation**: Any time `human_certainty.status` is updated to `validated-failing` or `context-dependent`, the system prompts the human: "Which AKU links should be reviewed based on this failure?" The human does not have to act immediately, but the prompt is explicit. Lint flags TAKUs with `validated-failing` and no `challenges` AKU links — these are unprocessed feedback signals.

### Risk 6b — False inference: validated-working TAKU with a validated-false AKU link
**Description**: A TAKU can be `validated-working` while one of its `justified_by` AKUs is `validated-false`. This is not a system error — it is epistemologically valid and informative. The technique works in practice despite one of its theoretical justifications being incorrect. This can happen because: (a) the false AKU explains some but not all of the mechanism, and the remaining AKUs compensate; (b) the AKU is false in general but functionally true in the specific context of the technique; (c) the AKU's falsification reveals that the real explanation is different from what was documented.

**What the system does**: The `validated-false` AKU remains linked in the TAKU's `aku_links.justified_by`. When the TAKU is retrieved, the agent surfaces all its AKU links with their individual validation states — including the falsified one, clearly marked. The human sees the complete picture: "this technique works (validated-working, 35 iterations) but one of the claims used to explain why it works has been falsified."

**Why this is valuable, not a problem**: This state is a precise diagnostic signal. It indicates that either (a) the TAKU needs a replacement AKU that better explains the actual mechanism, or (b) the falsified AKU needs its `context_boundary` or `partial` status refined — it may be false in general but operative in this specific combination. The system surfaces this tension without resolving it automatically. Human investigation is required.

**Lint rule**: TAKUs with `validated-working` status and one or more `justified_by` AKUs with `validated-false` status are flagged as "mechanistic explanation gap — review AKU links." This is a low-priority flag (the technique works) but requires eventual investigation.

### Risk 7 — Custom Type Proliferation
**Description**: With an open type taxonomy, users create many narrow custom types that are essentially variations of base types. The taxonomy fragments and becomes inconsistent.
**Mitigation**: Before creating a custom type, the agent must check: can this be expressed as a base type with a domain tag? A "medical diagnostic protocol" is a `protocol` with `domain: [medicine, diagnostics]`. A "financial valuation tool" is a `tool` with `domain: [finance, valuation]`. Custom types are warranted only when the base type's body structure is genuinely inadequate for the content.

---

## 12. Canonical TAKU Examples — Fully Annotated

### Example 1 — Technique: OREO Sales Pitch

```yaml
---
type: taku
taku_type: technique
id: taku-oreo-pitch
title: "OREO Pitch Technique"
origin: "Common sales training framework (multiple sources)"
domain: [sales, communication, persuasion, B2B]

when_to_use: >
  B2B pitch, 5–15 minute slot, audience includes both technical and
  non-technical decision makers. Objective is to secure interest or
  a next step — not to close. Most effective when the core argument
  is counterintuitive or challenges the prospect's current assumption.

when_not_to_use: >
  Closing conversations (requires a different structure).
  Presentations longer than 20 minutes (OREO is a micro-structure,
  not a full presentation framework).
  Audiences that have already bought the opinion (skip to evidence).

aku_links:
  justified_by:
    - id: aku-emotion-precedes-logic-in-decisions
      link_validation: human-validated
      link_note: >
        The Opinion step creates an emotional anchor before
        the logical evidence is presented. This works because
        people form an initial reaction and then filter evidence
        through it.
    - id: aku-narrative-improves-retention
      link_validation: human-validated
      link_note: >
        The Example (E) step activates narrative processing,
        which produces higher retention than abstract argument alone.
    - id: aku-repetition-with-variation-reinforces-claim
      link_validation: llm-proposed
      link_note: >
        The closing Opinion (second O) repeats the core claim
        in different words. LLM proposed this link — to be validated.

  constrained_by:
    - id: aku-audience-trust-as-prerequisite-for-persuasion
      link_validation: human-validated
      link_note: >
        OREO requires a baseline of credibility. With zero trust,
        the opening Opinion is dismissed before the Reasons land.

  breaks_when:
    - id: aku-procurement-process-neutralizes-narrative
      link_validation: llm-proposed
      link_note: >
        In formal procurement processes where decisions are made
        on criteria matrices, narrative structure loses effectiveness.
        LLM-proposed — to be validated.

  illustrates: []
  challenges: []

content_validation:
  status: human-reviewed
  reviewed_by: "Joan Cepero"
  review_date: 2026-05
  review_notes: "Structure confirmed accurate. Third justified_by link pending validation."

human_certainty:
  status: validated-working
  iterations: 35
  context_boundary: >
    Confirmed effective in B2B SaaS contexts, ticket >5k€,
    founder-led or senior AE pitches. Less effective with
    procurement-led processes. Not tested in consumer contexts.
  validated_by: "Joan Cepero"
  validation_date: 2026-05
  method: "Applied across 35 pitches over 18 months, tracking conversion to next step"

taku_relations:
  complementary:
    - taku-discovery-questions
    # Discovery identifies the pain that becomes the Opinion in OREO.
    # OREO without prior discovery produces generic, low-impact pitches.
  alternative_to:
    - taku-problem-agitate-solve
    # PAS (Problem → Agitate → Solve) addresses the same goal — persuasive argument —
    # with a different emotional mechanic (amplifying pain vs. anchoring with conclusion).
  precedes: []
  follows:
    - taku-discovery-questions
    # Discovery runs before OREO. OREO is the delivery vehicle for what discovery revealed.
    # sequence_type: recommended — OREO can be used without prior discovery,
    # but quality of the Opinion degrades significantly.

created: 2026-03-10
updated: 2026-05-20
status: active
status_note: ""
---
```

**Body:**

```markdown
## Summary
OREO is a micro-structure for delivering a persuasive argument in a short window.
The acronym stands for: Opinion → Reason → Example → Opinion.
It is designed to lead with the conclusion, support it logically, make it concrete
through narrative, and reinforce it at the end. The counter-intuitive design
(conclusion first) works because it anchors the audience's attention before
presenting evidence, so the evidence is filtered through the desired conclusion
rather than building up to it.

## When to Use
[See frontmatter — expanded:]
Best used when you have one clear, arguable position to communicate and limited
time. Works especially well when your position is non-obvious or contradicts
what the audience currently believes.

## Prerequisites
- The practitioner must have a clear, single Opinion to deliver (if you have
  two competing opinions, resolve them before the pitch)
- Baseline credibility with the audience must exist (see [[aku-audience-trust-as-prerequisite-for-persuasion]])
- One concrete, relevant example must be prepared in advance

## Steps
1. **Opinion**: State your conclusion directly, in one sentence.
   Do not build up to it. Do not hedge.
   "Your onboarding is losing you 40% of trial users in the first 48 hours."

2. **Reason**: Provide 1–2 logical supporting reasons.
   Keep them brief. This is not the proof — it is the scaffolding.
   "Trial users form habits in the first session or they don't come back.
   Your current flow asks them to configure before they experience value."

3. **Example**: One story, case, or concrete illustration.
   Specific beats general. A named customer scenario beats a statistic.
   "We worked with a SaaS team in a similar situation. They reversed the
   sequence — value first, configuration later — and 48-hour retention
   went from 31% to 58% in one sprint."

4. **Opinion**: Restate the core conclusion in different words.
   Same claim, fresh phrasing. This is not a summary — it is a reinforcement.
   "The fix is not in your product. It is in the order you introduce it."

## Anti-patterns
- **Starting with context**: "Let me tell you a bit about who we are..."
  Why it fails: you lose the audience's attention before the Opinion lands.
- **Multiple Opinions**: trying to make two arguments in one OREO.
  Why it fails: the audience cannot form a clear anchor.
- **Choosing a generic example**: "Many companies see this..."
  Why it fails: narrative requires specificity. Generic examples do not activate
  the narrative processing that makes the Example step effective.
- **Repeating the Opinion verbatim**: the closing Opinion must vary the phrasing.
  Why it fails: verbatim repetition signals low effort and reduces, not increases, impact.

## Expected Outcome
The audience has a clear, memorable position attributed to you, supported by a
concrete story. They can reproduce your argument in a conversation with a colleague.
The desired next step (meeting, introduction, decision) feels motivated.

## Failure Signals
- The audience asks "so what exactly are you proposing?" after the pitch.
  (The Opinion was not clear enough.)
- The audience engages with the Example but not with the argument.
  (The Example was too interesting on its own — it detached from the Opinion.)
- No next step is agreed at the end.
  (OREO created interest but not urgency — check if the Opinion was consequential enough.)

## Underlying Logic
This technique works because of two compounding effects:

First, [[aku-emotion-precedes-logic-in-decisions]]: presenting the Opinion first creates
an emotional anchor (agreement, disagreement, or curiosity). The Reasons and Example
are then processed in relation to that anchor, not neutrally. This is more persuasive
than presenting evidence first and expecting the audience to construct the conclusion.

Second, [[aku-narrative-improves-retention]]: the Example activates narrative processing,
which encodes information differently than analytical processing. A prospect who hears
a story about another company's problem and solution will remember and retell it.
A prospect who hears a statistic will not.

The closing Opinion closes the loop: it provides the conclusion again, now supported
by both logic and memory from the Example. The repetition is not redundant — it is
the mechanism by which the argument becomes sticky.

## Notes and Variants
- **PEEL** (Point → Evidence → Explanation → Link) is a similar structure more
  common in academic writing. OREO is optimized for verbal delivery; PEEL for written.
- For longer presentations (>15 min), multiple OREO structures can be nested:
  each section of the presentation follows its own Opinion–Reason–Example–Opinion arc.
- In written form (email, proposal), OREO maps naturally to:
  Subject line (Opinion) → Body paragraph 1 (Reason) → Case study (Example) →
  CTA or closing sentence (Opinion).
```

---

### Example 2 — Tool: Pareto Analysis for Outcome Distribution

```yaml
---
type: taku
taku_type: tool
id: taku-pareto-outcome-analysis
title: "Pareto Analysis for Outcome Distribution"
origin: "Vilfredo Pareto (1896), popularized in quality management literature"
domain: [analysis, prioritization, decision-making, operations, research]

when_to_use: >
  When you have a list of causes, inputs, or actors and a measurable outcome,
  and you want to identify which minority of inputs is responsible for the
  majority of outputs. Applicable in sales (which 20% of clients produce 80%
  of revenue), operations (which defects cause most failures), research
  (which variables explain most variance), and resource allocation.

when_not_to_use: >
  When inputs are not independently separable (tightly coupled systems where
  all inputs interact).
  When the distribution is genuinely uniform (the 80/20 pattern does not exist
  in all datasets — verify before assuming it).
  As a substitute for causal analysis (Pareto identifies correlation and
  concentration, not causality).

aku_links:
  justified_by:
    - id: aku-power-law-distributions-in-complex-systems
      link_validation: human-validated
      link_note: >
        The Pareto principle works because many real-world systems
        follow power law distributions, not normal distributions.
        Identifying the concentrated cause is only valuable because
        concentration reliably exists in these systems.
    - id: aku-marginal-returns-decrease-with-breadth
      link_validation: llm-proposed
      link_note: >
        The actionability of Pareto analysis rests on the claim that
        concentrating effort on the top 20% produces better returns
        than distributing effort evenly. LLM-proposed — to be validated.

  breaks_when:
    - id: aku-uniform-distribution-nullifies-prioritization
      link_validation: llm-proposed
      link_note: >
        When data is normally or uniformly distributed, Pareto analysis
        produces a misleading "80/20" finding that is not operationally
        meaningful. Always verify distribution before acting on results.

content_validation:
  status: human-reviewed
  reviewed_by: "Joan Cepero"
  review_date: 2026-05

human_certainty:
  status: validated-working
  iterations: 12
  context_boundary: >
    Validated in sales pipeline analysis and client portfolio prioritization.
    Not yet applied in research or operational quality contexts.
  validated_by: "Joan Cepero"
  validation_date: 2026-04

taku_relations:
  complementary:
    - taku-root-cause-analysis-5whys
    # Pareto identifies WHERE concentration is. 5 Whys identifies WHY.
    # Used together: Pareto first to find the vital few, then 5 Whys on each.
  alternative_to:
    - taku-decision-matrix
    # Decision matrix also prioritizes options, but by multi-criteria weighting
    # rather than outcome concentration. Use decision matrix when criteria are
    # multi-dimensional; use Pareto when a single output metric is available.
  precedes:
    - taku-root-cause-analysis-5whys
    # Pareto runs first to identify which items deserve deep causal analysis.
    # sequence_type: recommended
  follows: []

created: 2026-03-25
updated: 2026-05-20
status: active
---
```

**Body:**

```markdown
## Summary
Pareto Analysis identifies the vital few inputs responsible for the majority
of outcomes in a dataset. It operationalizes the empirical observation that
in many complex systems, roughly 80% of effects come from 20% of causes.
The exact ratio varies — the insight is that distribution is typically unequal,
and the high-impact minority is identifiable and actionable.

## Mechanic
The underlying mechanism is the power law distribution: in systems with many
interacting agents or variables, outputs accumulate disproportionately around
a few nodes. Identifying those nodes allows concentration of resources where
marginal returns are highest.

## Input
- A list of items (causes, clients, defects, features, variables)
- A measurable outcome associated with each item (revenue, frequency, cost, variance)
- The data must be clean: items must be independently countable and the outcome
  metric must be consistently defined across items

## Process
1. List all items with their associated outcome metric.
2. Sort the list in descending order by outcome metric.
3. Calculate cumulative percentage of outcome as you move down the list.
4. Identify the point where cumulative outcome reaches 80%.
5. Mark the items above that threshold as the "vital few."
6. Verify: does the vital few represent approximately 20% of items?
   (If significantly more than 20%, the distribution may not follow a power law —
   see Limitations.)
7. Interpret: what do the vital few have in common? What distinguishes them?

## Output
A ranked list partitioned into:
- **Vital few**: the minority of items responsible for the majority of outcome
- **Useful many**: the majority of items responsible for the minority of outcome

A Pareto chart (bar chart sorted descending + cumulative line chart) makes
this partition visually immediate.

## Interpretation Guide
The analysis tells you WHERE concentration exists, not WHY.
Acting on Pareto results requires a second step: understanding what makes
the vital few different from the useful many.

Common misinterpretation: "We should eliminate the useful many."
Correct interpretation: "We should understand what makes the vital few vital,
replicate it where possible, and allocate disproportionate resources to it."

For client portfolio analysis: the top 20% of clients by revenue are not just
"more valuable" — they likely share characteristics (size, industry, use case,
relationship type) that explain their value. The analysis is the start, not the end.

## Limitations
- **Not causal**: identifies concentration, not cause. Requires follow-up analysis.
- **Static**: a one-time Pareto snapshot may not reflect dynamics. Run the analysis
  periodically to detect shifts in which inputs are vital.
- **Assumes separability**: if inputs are tightly coupled (removing one changes
  the output of others), simple Pareto analysis is insufficient.
- **The 80/20 is approximate**: treat it as a diagnostic heuristic, not a law.
  The real question is: is there meaningful concentration? Not: is it exactly 80/20?

## Example Application
**Context**: Sales pipeline, 45 active clients, 12-month revenue data.

**Input**: Client list with ARR (Annual Recurring Revenue) per client.

**Process**: Sorted by ARR descending. Computed cumulative %.

**Result**: Top 9 clients (20% of 45) represent €1.2M of €1.5M total ARR (80%).

**Interpretation**: These 9 clients share three characteristics:
- Company size >200 employees
- Primary user is a department head, not an individual contributor
- Contracted for annual (not monthly) billing

**Action taken**: ICP (Ideal Customer Profile) refined to these three criteria.
Prospecting effort reallocated toward this profile.
Result: pipeline quality score increased 40% over the following quarter.
```

---

## 13. Congruence Audit — Design Weaknesses Identified

### Gap 1 — No defined minimum AKU links for TAKU activation
**Issue**: The spec requires at least one human-validated AKU link for a TAKU to be considered fully validated, but does not set a minimum for activation. A TAKU could be activated with zero AKU links.
**Current state**: Undefined. The spec says TAKUs "should" have at least one human-validated link, not "must."
**Recommendation**: Define activation criteria: a TAKU with zero AKU links can only be activated as `content_validation: human-authored` (the human takes full responsibility). LLM-authored TAKUs must have at least one AKU link (even `llm-proposed`) before activation.

### Gap 2 — Upward feedback loop is human-dependent with no time constraint
**Issue**: The failure diagnosis retrieval mode generates a prompt for the human to review underlying AKUs, but there is no mechanism to ensure this actually happens. Failed TAKUs can accumulate without their signals being processed.
**Current state**: Lint flags the gap but cannot enforce resolution.
**Recommendation**: Define a maximum age for unprocessed failure signals: a TAKU with `validated-failing` and no `challenges` links that is older than 60 days is escalated to a "critical review" queue that appears in the daily capture protocol, not just the lint report.

### Gap 3 — `story` type body structure is the weakest defined
**Issue**: The story body structure is the least prescriptive of all types. "Write the narrative" is not a structural constraint, and LLMs tend to produce either overly generic stories or stories that are interesting but weakly connected to their target AKUs.
**Current state**: Defined but loose.
**Recommendation**: Add a mandatory "AKU moment" section to the story body: the specific moment in the narrative where the target AKU is most clearly illustrated. This forces the author to identify the exact instantiation of the claim within the story, which both improves the story's epistemic function and makes the `illustrates` link more precise.

### Gap 4 — Custom types have no enforcement mechanism
**Issue**: The spec says custom types must be defined in `CLAUDE.md` with a schema. But without a lint rule that checks custom type compliance, the agent cannot verify that a custom-typed TAKU follows its declared schema.
**Current state**: Defined requirement with no enforcement.
**Recommendation**: Any new custom type definition in `CLAUDE.md` must include a list of required body section headers. Lint checks TAKUs of that type against that list, same as it does for base types.

### Gap 5 — Link inflation threshold of 7 is arbitrary
**Issue**: The lint flag for TAKUs with >7 `justified_by` links is defined in the risks section but the number 7 is not derived from any principled argument.
**Current state**: Heuristic threshold.
**Recommendation**: The threshold should be calibrated to the practitioner's domain after 3–6 months of system use. Complex technical or scientific domains may legitimately require more AKU links per TAKU. The agent should flag and ask, not auto-resolve.

### Gap 6 — ~~No specification for TAKU-to-TAKU relations~~ RESOLVED in v1.0
**Resolution**: The `taku_relations` block has been added to the universal frontmatter with four typed fields:
- `complementary` — TAKUs that work better when applied together (bidirectional)
- `alternative_to` — TAKUs that address the same goal with a different approach (bidirectional)
- `precedes` — this TAKU comes before the referenced TAKU in a sequence (directional)
- `follows` — this TAKU comes after the referenced TAKU in a sequence (inverse of precedes)

Lint enforces bidirectionality on `complementary` and `alternative_to`, and the precedes/follows pair. A broken bidirectional link is a lint error.

### Gap 7 — The `heuristic` type blurs the boundary with AKUs
**Issue**: A heuristic TAKU ("never negotiate against yourself") is very close to a prescriptive AKU. The distinction (AKU = descriptive claim; heuristic TAKU = prescriptive rule) may be too subtle to maintain consistently.
**Current state**: Defined distinction but potentially fragile in practice.
**Recommendation**: Add a disambiguation test to the CLAUDE.md schema instructions: "If the content can be expressed as a falsifiable declarative sentence ('X produces Y'), it is an AKU. If it can only be expressed as an imperative ('Do X in situation Y'), it is a heuristic TAKU. If it can be expressed as both, create both and link them."

---

*End of TAKU System Specification — v1.0*
*This document is the second layer seed. The next document to generate is the CLAUDE.md operational schema — the instructions the LLM agent reads to operate both the AKU and TAKU layers.*
