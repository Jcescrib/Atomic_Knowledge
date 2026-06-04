---
type: taku
taku_type: framework
id: taku-tres-motores-crecimiento
title: "Los tres motores de crecimiento (pago, viral, sticky)"
origin: "The Power MBA — Módulo 2.2.1 «Tipos de motores de crecimiento»"
domain: [growth, business-model, strategy, power-mba]

when_to_use: >
  Cuando se necesita diagnosticar qué motor de crecimiento opera (o debería
  operar) en un negocio digital, qué métricas priorizar para gestionarlo y
  qué implicaciones financieras tiene la elección (cuánta financiación
  externa necesita el modelo para escalar). Útil tanto para auditar un
  negocio existente como para tomar decisiones estratégicas sobre dónde
  invertir capital y atención operativa.

when_not_to_use: >
  En negocios cuyo crecimiento no es sistemático ni replicable (proyectos
  one-off, ventas por relación personal, M&A oportunista). Tampoco aplica
  como única lente: muchos negocios reales combinan elementos de los tres
  motores; el marco identifica el motor dominante, no el único.

aku_links:
  justified_by:
    - id: aku-motor-crecimiento-concept
      link_validation: llm-proposed
      link_note: "El concepto meta que define qué es un motor de crecimiento."
    - id: aku-motor-crecimiento-pago-concept
      link_validation: llm-proposed
      link_note: "Primer arquetipo — crecimiento financiado por reinversión del margen CLTV-CAC."
    - id: aku-motor-crecimiento-viral-concept
      link_validation: llm-proposed
      link_note: "Segundo arquetipo — crecimiento orgánico vía coeficiente de viralidad."
    - id: aku-motor-crecimiento-sticky-concept
      link_validation: llm-proposed
      link_note: "Tercer arquetipo — crecimiento por retención de larga duración."
    - id: aku-coeficiente-viralidad-concept
      link_validation: llm-proposed
      link_note: "Métrica clave del motor viral; permite diagnosticarlo cuantitativamente."
    - id: aku-viral-bajo-cltv-compatible-claim
      link_validation: llm-proposed
      link_note: "Claim contraintuitivo que el marco hace explícito y operacionalizable."
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
  complementary:
    - taku-digital-growth-engine-metrics-map
  alternative_to: []
  precedes:
    - id: taku-digital-growth-engine-metrics-map
      sequence_type: recommended
  follows: []

created: 2026-06-03
updated: 2026-06-03
status: draft
status_note: ""
---

## Summary

Taxonomía de los tres motores de crecimiento principales en negocios digitales: **pago** (adquisición vía publicidad pagada), **viral** (adquisición orgánica vía uso del producto), y **sticky** (retención de larga duración). Cada motor tiene su métrica clave, su dinámica financiera y su perfil de financiación. El marco fuerza una decisión sobre cuál es el motor dominante del negocio para alinear métricas y operaciones.

## Core Components

| Motor | Mecánica | Métricas clave | Implicación financiera | Ejemplos |
|---|---|---|---|---|
| **Pago** | Publicidad pagada → captación → margen CLTV−CAC → reinversión | CAC, CLTV, CLTV−CAC, CAC payback | Auto-financiación posible si CAC payback corto | Hawkers, e-commerce |
| **Viral** | Uso del producto → cada cliente atrae más de uno orgánicamente | Coeficiente de viralidad | CAC puede ser 0; CLTV bajo aceptable | Redes sociales |
| **Sticky** | Lifetime largo, retención sostenida | Churn rate, lifetime | Capital-intensivo (CAC payback alto) | Netflix, Tulotero |

## How to Apply

1. **Identificar el motor dominante** observando cómo llegan los clientes en la práctica (no como dicen las narrativas):
   - ¿La mayoría llega vía anuncios pagados? → Pago.
   - ¿Llegan recomendados por otros usuarios? → Viral.
   - ¿Se quedan años sin re-captar? → Sticky.
2. **Priorizar la métrica del motor identificado**:
   - Pago → CAC payback (acelerar reinversión).
   - Viral → coeficiente de viralidad (mantenerlo > 1).
   - Sticky → churn rate (minimizarlo).
3. **Asignar foco operativo**: en pago, optimizar embudo y unit economics; en viral, optimizar referidos y la experiencia que motiva compartir; en sticky, optimizar onboarding y reducción de bajas.
4. **Calibrar expectativas de financiación**: pago puede auto-financiarse; viral requiere poco capital pero es difícil de conseguir; sticky exige capital externo significativo durante la fase de captación.
5. **Reconsiderar si el motor actual es el adecuado**: a veces un negocio opera con un motor por inercia que no es el que mejor encaja con su propuesta.

## Underlying Claims

- El concepto meta `aku-motor-crecimiento-concept` postula que tres arquetipos cubren la mayoría de los modelos de crecimiento sistemático en negocios digitales.
- Cada concepto-AKU específico (pago, viral, sticky) describe la mecánica, métrica clave e implicación financiera de su motor.
- `aku-viral-bajo-cltv-compatible-claim` hace explícito el aspecto contraintuitivo del motor viral (un CLTV bajo no es necesariamente malo, depende del motor).

## Strengths

- Marco simple de tres categorías mutuamente comparables.
- Conecta directamente con la elección de métricas a priorizar.
- Hace explícitas las implicaciones financieras (cuánto capital externo necesita el modelo).
- Mismo lenguaje que el resto de marcos de unit economics (CLTV, CAC, churn).

## Limitations and Criticisms

- **Es una simplificación**: muchos negocios reales combinan dos o los tres motores; el marco identifica el dominante.
- **No incluye otros motores reconocidos en la literatura**: e.g., motor de marca/contenido, motor de plataforma multi-side, motor de comunidad/network effects más allá del coeficiente de viralidad puro.
- **La frase "Muy pocas compañías son capaces" sobre el motor viral** es una afirmación de frecuencia sin datos en la fuente —debería tratarse como advertencia, no como ley.
- **Métricas insuficientemente operacionalizadas en esta fuente**: la fuente nombra las métricas pero no las define en detalle; ese material está en el módulo 2.2.

## Variants and Extensions

- **Eric Ries — The Lean Startup**: define tres motores de crecimiento (pegajoso, viral, pagado) muy similares pero con énfasis en métricas accionables y experimentos para validar cada uno.
- **a16z y SaaS metrics frameworks**: extienden el motor sticky con métricas de cohorte (retention curves, NDR — Net Dollar Retention).
- **Motor de plataforma / network effects de dos lados**: variante del viral para marketplaces y plataformas multi-side donde el coeficiente de viralidad debe medirse por lado.

## Relaciones

**justified_by** ← [[aku-motor-crecimiento-concept]] · [[aku-motor-crecimiento-pago-concept]] · [[aku-motor-crecimiento-viral-concept]] · [[aku-motor-crecimiento-sticky-concept]] · [[aku-coeficiente-viralidad-concept]] · [[aku-viral-bajo-cltv-compatible-claim]]

**complementary** ↔ [[taku-digital-growth-engine-metrics-map]]

**precedes** → [[taku-digital-growth-engine-metrics-map]]
