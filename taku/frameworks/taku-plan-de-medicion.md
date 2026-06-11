---
type: taku
taku_type: framework
id: taku-plan-de-medicion
title: "Plan de medición analítica (Objetivos · Estrategias · KPIs · Metas · Segmentos)"
origin: "The Power MBA — Módulo 15 «Analítica» — Plantilla Plan de Medición"
domain: [marketing-digital, analitica, medicion, power-mba]

when_to_use: "Antes de lanzar una campaña o iniciativa digital, para conectar objetivos de negocio con su medición."
when_not_to_use: "Como sustituto del análisis cualitativo o cuando no hay objetivos de negocio definidos."

aku_links:
  justified_by:
    - id: aku-plan-de-medicion-concept
      link_validation: human-validated
      link_note: "Define los cinco bloques del plan de medición."
    - id: aku-objetivos-negocio-concept
      link_validation: human-validated
      link_note: "El plan parte de los objetivos de negocio."
    - id: aku-ley-de-goodhart-cuando-una-medida-se-vuelve-objetivo-deja-de-ser-buena-claim
      link_validation: human-validated
      link_note: "deducible: corrobora aku-plan-de-medicion-concept desde [james-clear] (cross-source)"
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
  follows: []

created: 2026-06-04
updated: 2026-06-04
status: draft
status_note: ""
---

## Summary

Plantilla para alinear la analítica con el negocio definiendo objetivos, estrategias,
KPIs, metas y segmentos.

## Core Components

1. **Objetivos**: qué quieres lograr (captación de leads, branding, ventas, customer
   loyalty…); considera conversiones macro y micro.
2. **Estrategias**: el cómo, las acciones para cumplir cada objetivo.
3. **KPIs**: pocas métricas relevantes que monitorizan el avance.
4. **Metas**: valores numéricos asignados a cada KPI.
5. **Segmentos**: grupos de usuarios a monitorizar (tipo de cliente, canal de
   atracción, área geográfica, nuevos vs. recurrentes…).

## How to Apply

1. Para cada objetivo, define estrategias, KPIs y sus metas numéricas.
2. Selecciona segmentos relevantes para desglosar el análisis.
3. Instrumenta la medición (Google Analytics, UTMs, objetivos) y revisa periódicamente.

## Underlying Claims

Medir sin alinear KPIs y metas con los objetivos de negocio produce métricas
vanidosas; conviene centrarse en pocas métricas accionables.

## Strengths

Da foco, evita vanity metrics y permite saber si se cumplen los objetivos.

## Limitations and Criticisms

Requiere objetivos claros y disciplina de revisión; metas mal calibradas desorientan.

## Variants and Extensions

Ejemplo: objetivo «atraer tráfico cualificado» → KPI duración media de sesión (meta 3
min) y % rebote (meta <50%); «captar suscriptores» → total suscriptores (meta 2.000/
mes); «generar ventas» → ingresos (meta 30.000€/mes), ticket medio, ratio conversión.

## Relaciones

**justified_by** ← [[aku-plan-de-medicion-concept]] · [[aku-objetivos-negocio-concept]] · [[aku-ley-de-goodhart-cuando-una-medida-se-vuelve-objetivo-deja-de-ser-buena-claim]]
