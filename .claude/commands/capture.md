---
description: Append a rough observation to today's daily capture file
argument-hint: <text — raw thought, observation, claim, technique, failure>
---

Append `$ARGUMENTS` to `capture/daily/YYYY-MM-DD.md` (today's date from conversation context).

If the file does not exist, create it from `_meta/templates/daily.md` first (replace `YYYY-MM-DD` placeholders with today's date). Add the new content as a bullet under the most appropriate existing section header. If none fits cleanly, append under `## Observations`.

**Hard rules:**
- Do NOT propose AKUs or TAKUs from a single capture line. Capture is rough; processing is deliberate.
- Do NOT structure the text — preserve the human's phrasing.
- Do NOT auto-link to AKUs.
- Only append. Never edit prior bullets in today's file.

After appending, commit with `capture: YYYY-MM-DD` (single commit per capture session is fine — the human may call `/capture` multiple times before they want a commit; if multiple captures are queued, batch into one commit when explicitly asked).

When the human later runs `/ingest capture/daily/YYYY-MM-DD.md`, that file becomes the source for AKU/TAKU proposals — but only at that point, not now.

No output beyond confirming where the line was appended.
