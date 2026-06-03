---
type: aku
aku_class: method
id: aku-cltv-subscription-formula
statement: >
  En negocios de suscripción, el customer lifetime value se computa como ARPU
  multiplicado por el lifetime esperado del cliente, ambos expresados en la
  misma unidad temporal (CLTV = ARPU × lifetime).
origin: "The Power MBA — Módulo 2.2 «Motor de crecimiento digital — principales métricas»"
domain: [growth, unit-economics, subscription, metrics]

llm_confidence: 0.50

human_certainty:
  status: unvalidated
  iterations: 0
  context_boundary: ""
  validated_by: ""
  validation_date: ""
  method: ""

epistemic_type: sourced

relations:
  supported_by:
    - aku-cltv-concept
    - aku-arpu-concept
    - aku-churn-rate-concept
  supports: []
  constrained_by: []
  constrains: []
  context_breaks_at:
    - aku-cltv-transactional-formula
  breaks_context_of:
    - aku-cltv-transactional-formula
  contradicts: []
  related: []

sources:
  - "raw/2.2-Motores de crecimiento - proncipales métricas.pdf"

created: 2026-06-02
updated: 2026-06-03
status: active
status_note: ""
---

## Relaciones

**supported_by** ← [[aku-cltv-concept]] · [[aku-arpu-concept]] · [[aku-churn-rate-concept]]

**context_breaks_at** → [[aku-cltv-transactional-formula]]

**breaks_context_of** → [[aku-cltv-transactional-formula]]
