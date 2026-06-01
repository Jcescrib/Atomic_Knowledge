# Log — AKU/TAKU Vault

Append-only operational history. Never edit past entries.

Format per entry:
```
## YYYY-MM-DD HH:MM — <event-type>
<one-line summary>
- <details, one bullet per fact>
```

Event types: `bootstrap` · `ingest` · `update` · `lint` · `capture` · `query` · `validate` · `deprecate` · `meta`

---

## 2026-06-01 — bootstrap
Vault initialized from `_spec/AKU-System-Specification.md` and `_spec/TAKU-System-Specification.md`.
- Folder skeleton created: `raw/` (flat), `capture/daily/`, `aku/`, `taku/{7 types}/`, `outputs/{queries,reports,lint}/`, `_meta/templates/`, `.claude/commands/`.
- Templates written: `aku.md`, `taku.md`, `daily.md`, `source.md`.
- Operating manual `CLAUDE.md` encoded (198 lines).
- Slash commands installed: `/ingest`, `/lint`, `/query`, `/capture`.
- `.gitignore` configured for Obsidian + outputs/.
- Branch renamed `master` → `main`. Initial commit `meta: bootstrap AKU/TAKU vault`.
- `validated_by` identity: Joan Cepero.
- Local semantic search (qmd) deferred — not wired in this bootstrap.
