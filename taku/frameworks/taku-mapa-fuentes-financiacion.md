---
type: taku
taku_type: framework
id: taku-mapa-fuentes-financiacion
title: "Mapa de fuentes de financiación por fase"
origin: "The Power MBA — Módulo 6.3 «Fuentes de financiación: quién»"
domain: [emprendimiento, financiacion, startup, inversion, power-mba]

when_to_use: >
  Al planificar la financiación de una startup: identificar qué fuentes encajan
  con la fase de desarrollo actual (seed/early/growth/expansion) y a quién dirigir
  la búsqueda de fondos.
when_not_to_use: >
  Para negocios autofinanciados sin intención de levantar capital externo, o para
  decidir la propuesta concreta al inversor (eso es el pitch deck).

aku_links:
  justified_by:
    - id: aku-fuentes-financiacion-concept
      link_validation: human-validated
      link_note: "El inventario de fuentes (el «quién»)."
    - id: aku-fases-financiacion-concept
      link_validation: human-validated
      link_note: "El mapa fase de desarrollo ↔ fase de financiación ↔ fuentes."
    - id: aku-bootstrapping-concept
      link_validation: human-validated
      link_note: "Opción transversal a todas las fases."
    - id: aku-incubadora-aceleradora-concept
      link_validation: human-validated
      link_note: "Fuentes de fases iniciales/intermedias."
    - id: aku-venture-capital-concept
      link_validation: human-validated
      link_note: "Fuente de early-stage/growth con tracción."
    - id: aku-free-bootstrap-plataforma-claim
      link_validation: human-validated
      link_note: "deducible: corrobora aku-bootstrapping-concept desde [(unknown)] (cross-source)"
  constrained_by:
    - id: aku-vc-busca-x10-claim
      link_validation: human-validated
      link_note: "El VC solo aplica si hay potencial de x10."
  breaks_when: []
  illustrates: []
  challenges: []

content_validation:
  status: llm-authored
  reviewed_by: ""
  review_date: ""
  review_notes: ""

human_certainty:
  status: unvalidated
  iterations: 0
  context_boundary: ""
  validated_by: ""
  validation_date: ""
  method: ""

taku_relations:
  complementary: [taku-eleccion-proyecto-fit]
  alternative_to: []
  precedes: []
  follows: []

created: 2026-06-04
updated: 2026-06-04
status: draft
status_note: ""
---

## Summary

Marco que asocia cada fase de desarrollo de una startup con su fase de
financiación y las fuentes adecuadas, para dirigir la búsqueda de fondos al
inversor correcto en el momento correcto.

## Core Components

| Desarrollo | Fase | Fuentes |
|---|---|---|
| Problem-Solution Fit | Seed | Bootstrap · FFF · Incubadora · Business Angel |
| Product-Market Fit | Early stage | Bootstrap · Aceleradora · Business Angel · Venture Capital |
| Motor de Crecimiento | Growth | Bootstrap · Business Angel · Media 4 Equity |
| Escalar | Expansion | Bootstrap · Business Angel · Socio Industrial |

Otras: equity crowdfunding, organismos públicos (préstamos participativos). El
venture builder NO es una fuente para startups externas.

## How to Apply

1. Situar el proyecto en su fase de desarrollo (PSF/PMF/growth/scale).
2. Mapear las fuentes admisibles para esa fase.
3. Filtrar por encaje (p. ej. VC solo si hay potencial x10 y tracción).
4. Preparar la aproximación al inversor adecuado.

## Underlying Claims

- Acudir a una fuente antes de su fase (VC en seed) no funciona.
- El VC exige perspectiva de retorno x10.

## Strengths

- Evita perder tiempo con inversores que no encajan con la fase.

## Limitations and Criticisms

- El mapa es orientativo; los límites entre fases son difusos y varían por sector/país.

## Variants and Extensions

- Se complementa con la elección de proyecto (implicación «financiación necesaria»)
  y con el pitch deck (cómo se presenta al inversor).

## Relaciones

**justified_by** ← [[aku-fuentes-financiacion-concept]] · [[aku-fases-financiacion-concept]] · [[aku-bootstrapping-concept]] · [[aku-incubadora-aceleradora-concept]] · [[aku-venture-capital-concept]] · [[aku-free-bootstrap-plataforma-claim]]
**constrained_by** ← [[aku-vc-busca-x10-claim]]
**complementary** ↔ [[taku-eleccion-proyecto-fit]]
