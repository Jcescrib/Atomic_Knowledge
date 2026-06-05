---
type: taku
taku_type: protocol
id: taku-post-operational-debrief
title: "Post-Operational Debrief (debrief tras la operación)"
origin: "Jocko Willink & Leif Babin (Extreme Ownership / The Dichotomy of Leadership)"
domain: [liderazgo, jocko, mejora-continua]

when_to_use: "Después de cada operación, proyecto o iteración significativa, por agotado u ocupado que esté el equipo."
when_not_to_use: "No aplica como sustituto de la corrección en tiempo real durante la ejecución."

aku_links:
  justified_by:
    - id: aku-post-operational-debrief-method
      link_validation: llm-proposed
      link_note: ""
    - id: aku-analisis-constante-medir-efectividad-claim
      link_validation: llm-proposed
      link_note: ""
  constrained_by: []
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
  complementary: []
  alternative_to: []
  precedes: []
  follows:
    - id: taku-planning-checklist
      sequence_type: recommended

created: 2026-06-04
updated: 2026-06-04
status: draft
status_note: ""
---

## Purpose
Extraer lecciones de cada operación e implementarlas para no repetir errores y mejorar continuamente.

## Trigger Conditions
Finalización de una operación, proyecto, sprint o iteración.

## Required Resources
Tiempo reservado (aunque haya agotamiento); honestidad brutal; participación de los ejecutores.

## Protocol Steps
1. Examinar todas las fases (de la planificación a la ejecución) en formato conciso.
2. ¿Qué salió bien?
3. ¿Qué salió mal?
4. ¿Cómo adaptamos las tácticas para ser más efectivos?
5. Documentar e implementar las lecciones en la planificación futura.

## Decision Points
¿Qué lecciones cambian el SOP o el próximo plan? ¿Qué se repite?

## Exit Conditions
Lecciones capturadas y asignadas a la siguiente iteración de planificación.

## Failure Handling
Si el debrief degenera en culpas, reconducir con Extreme Ownership: foco en el problema, no en la persona.

## Review Trigger
Cada operación; alimenta el siguiente ciclo de planificación.

## Relaciones

**justified_by** ← [[aku-post-operational-debrief-method]] · [[aku-analisis-constante-medir-efectividad-claim]]

**follows** ← [[taku-planning-checklist]]
