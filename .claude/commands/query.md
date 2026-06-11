---
description: Bidirectional retrieval across AKU and TAKU layers
argument-hint: <question | situation | concept | AKU id | TAKU id>
---

Run bidirectional retrieval per `CLAUDE.md` § Bidirectional retrieval. Query: `$ARGUMENTS`.

If no argument was provided, ask what to retrieve and offer the three modes (direct, situational, domain) plus failure-diagnosis.

**Detect the entry direction:**
- Direct AKU/TAKU ID → expand from that node.
- Concept / situation / question → semantic match across `aku/` and `taku/`, then expand from each match.
- Domain tag → filter by `domain` and return all matching AKUs + their linked TAKUs.
- TAKU + reported failure → enter failure-diagnosis mode (see CLAUDE.md).

**Retrieval rules:**
- Always include `validated-false` AKUs in domain and situational results. Mark them ✗.
- Expand typed relations normally; cap `related` expansion at depth 1.
- For hybrid AKUs, show both confidence dimensions explicitly per the human-primacy table.
- Surface `llm-proposed` AKU links on TAKUs with a ◎ marker.
- Order TAKUs: human-authored → human-reviewed → llm-authored.
- **Corroboración cross-source (señal de verdad):** para cada AKU primario, calcula y muestra
  cuántas FUENTES independientes lo sostienen, ejecutando
  `python scripts/corroboration.py <aku-id>`. Cuenta el corpus del AKU + el de sus vecinos
  directos por relaciones de acuerdo (`related`/`supports`/`supported_by`/`constrains`/
  `constrained_by`); `contradicts` NO corrobora y se reporta aparte como ⚠ contra-evidencia.
  Orden de la señal de verdad: **human_certainty prevalece** (si ≠ `unvalidated`); en su
  defecto, `llm_confidence` **ponderada por la corroboración** (más fuentes independientes
  que repiten el concepto ⇒ mayor confianza operativa). Nunca colapses ambas dimensiones.

**Output structure (always exactly two sections):**

```
RETRIEVAL — <query>

═══════════════════════════════════════════════════
KNOWLEDGE LAYER — AKUs
═══════════════════════════════════════════════════
[primary match #1]
  <statement>
  Status: <human_certainty.status> · iterations: N · domain: [tags]
  llm_confidence: <value>  [for hybrid: shown alongside human status]
  Corroboración: <N> fuentes independientes [corpus1, corpus2, ...]  ⚠ contradicen: [...]
  context_boundary: <if set>
  Cluster:
    supported_by → <linked AKUs with their status>
    constrained_by → ...
    context_breaks_at → ...
    contradicts → ... (if any)
    related → ... (depth 1 only)

[primary match #2]
  ...

[Validated-false in this domain]
  ✗ <aku-id> — <statement> (preserved as negative evidence)

═══════════════════════════════════════════════════
EXECUTABLE LAYER — TAKUs
═══════════════════════════════════════════════════
[TAKU #1] — <type>
  Title: <title>
  Status: <status> · content: <content_validation.status> · use: <human_certainty.status>
  when_to_use: <text>
  AKU links:
    ✓ justified_by → <aku-id> (human-validated)
    ◎ justified_by → <aku-id> (llm-proposed — pending validation)
    ...
[TAKU #2] ...
```

**Validation markers (use exactly these):**
- ✓ human-validated / validated-true / validated-working
- ◎ llm-proposed / unvalidated
- ✗ validated-false / validated-failing
- ○ draft

**Never:**
- Average the two confidence dimensions.
- Filter out validated-false content.
- Silently omit unvalidated content — always mark it.

If the user asks to save the result, write to `outputs/queries/YYYY-MM-DD-<slug>.md` and commit with `query: <slug>`.
