---
type: taku
taku_type: framework
id: taku-digital-growth-engine-metrics-map
title: "Mapa de métricas del motor de crecimiento digital"
origin: "The Power MBA — Módulo 2.2 «Motores de crecimiento — principales métricas»"
domain: [growth, unit-economics, business-model, metrics]

when_to_use: >
  Cuando se necesita diagnosticar la salud económica de un motor de
  crecimiento digital, definir los KPIs financieros de un negocio digital o
  evaluar la sostenibilidad de la captación de clientes en modelos de
  suscripción o transaccionales con base de clientes recurrente.

when_not_to_use: >
  En negocios no-digitales con dinámicas de adquisición y retención
  fundamentalmente distintas (industriales pesados, B2B enterprise con ciclos
  de venta plurianuales y contratación única, government/regulado). En esos
  contextos el ratio CLTV/CAC y el churn rate pueden no ser las palancas
  operativas dominantes.

aku_links:
  justified_by:
    - id: aku-cltv-concept
      link_validation: llm-proposed
      link_note: "Concepto central — sin CLTV no hay marco."
    - id: aku-cac-concept
      link_validation: llm-proposed
      link_note: "Segundo concepto central — el par CLTV/CAC define el marco."
    - id: aku-arpu-concept
      link_validation: llm-proposed
      link_note: "Componente del cálculo de CLTV en modelos de suscripción."
    - id: aku-churn-rate-concept
      link_validation: llm-proposed
      link_note: "Determina el lifetime esperado, input de CLTV; métrica clave del motor sticky."
    - id: aku-cac-payback-concept
      link_validation: llm-proposed
      link_note: "Métrica temporal del marco — pregunta «¿en cuánto tiempo recuperamos?»"
    - id: aku-cltv-cac-ratio-concept
      link_validation: llm-proposed
      link_note: "Métrica de multiplicador — pregunta «¿por cuánto?»"
    - id: aku-cltv-minus-cac-concept
      link_validation: llm-proposed
      link_note: "Métrica de utilidad absoluta — pregunta «¿cuánto ganamos por cliente?»"
    - id: aku-cltv-subscription-formula
      link_validation: llm-proposed
      link_note: "Método de cálculo de CLTV para el contexto de suscripción."
    - id: aku-cltv-transactional-formula
      link_validation: llm-proposed
      link_note: "Método de cálculo de CLTV para el contexto transaccional."
    - id: aku-cltv-gross-margin-over-revenue
      link_validation: llm-proposed
      link_note: "Refina la base monetaria correcta para todas las métricas derivadas."
    - id: aku-cltv-cac-dual-optimization
      link_validation: llm-proposed
      link_note: "Claim estratégico que da sentido a coordinar las dos métricas centrales."
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
    - taku-tres-motores-crecimiento
  alternative_to: []
  precedes: []
  follows: []

created: 2026-06-03
updated: 2026-06-03
status: draft
status_note: ""
---

## Summary

Mapa que asocia las seis preguntas estratégicas necesarias para diagnosticar
un motor de crecimiento digital con las métricas financieras que las
contestan. Sirve como cuadro de mandos mínimo de unit economics para un
negocio digital: seis preguntas, una métrica anclada a cada una, todas
interconectadas. Complementario a la taxonomía `taku-tres-motores-crecimiento`
del módulo 2.2.1, que dice QUÉ motor opera; este TAKU dice QUÉ MEDIR para
gestionarlo.

## Core Components

| Pregunta | Métrica | AKU |
|---|---|---|
| ¿Cuál es el valor que un cliente puede generar? | CLTV (con ARPU como input recurrente) | `aku-cltv-concept`, `aku-arpu-concept` |
| ¿Cuánto cuesta captar un cliente? | CAC | `aku-cac-concept` |
| ¿Cuánto ganamos con cada cliente? | CLTV − CAC | `aku-cltv-minus-cac-concept` |
| ¿En cuánto tiempo recuperamos la inversión? | CAC payback | `aku-cac-payback-concept` |
| ¿Por cuánto multiplicamos la inversión? | CLTV / CAC | `aku-cltv-cac-ratio-concept` |
| ¿Cuántos clientes perdemos? | churn rate | `aku-churn-rate-concept` |

El cálculo de CLTV depende del modelo de negocio (los dos métodos son
mutuamente excluyentes por contexto):

- Suscripción: `aku-cltv-subscription-formula` (CLTV = ARPU × lifetime)
- Transaccional: `aku-cltv-transactional-formula` (CLTV = ticket × repetición)

Convención de base monetaria refinada por `aku-cltv-gross-margin-over-revenue`:
usar margen bruto en lugar de ingreso total para todas las métricas
derivadas.

## How to Apply

1. Identificar el modelo de negocio (suscripción vs transaccional) para elegir la fórmula de CLTV correcta.
2. Calcular CLTV sobre margen bruto, no sobre ingresos.
3. Calcular CAC sobre la misma base monetaria que CLTV (consistencia).
4. Derivar las tres métricas compuestas: CLTV − CAC, CLTV / CAC, CAC payback.
5. Medir churn rate por cohorte (no agregado) para no enmascarar deterioros bajo crecimiento.
6. Revisar las seis métricas conjuntamente — ninguna en aislamiento basta para diagnosticar el motor.

## Underlying Claims

El marco descansa sobre dos conceptos centrales (CLTV y CAC) y un claim estratégico que los une (`aku-cltv-cac-dual-optimization`): optimizar los dos juntos produce mejores unit economics que optimizar uno solo. Las demás métricas son derivaciones o refinamientos:

- `aku-cltv-gross-margin-over-revenue` refina la base de cálculo.
- `aku-cltv-subscription-formula` y `aku-cltv-transactional-formula` proveen los dos métodos de cómputo de CLTV, mutuamente excluyentes por contexto.
- `aku-arpu-concept` y `aku-churn-rate-concept` son inputs operativos de la fórmula de suscripción.

## Strengths

- Cubre las seis preguntas mínimas de unit economics con un único cuadro coherente.
- Las métricas se interconectan: cambiar una desplaza al menos otras dos, lo que facilita razonar sobre palancas.
- Aplicable tanto a suscripción como a transaccional, ajustando solo la fórmula de CLTV.
- Complementario al marco de tres motores: este dice qué medir, aquel dice qué motor opera.

## Limitations and Criticisms

- El marco asume un motor de crecimiento *digital*; las dinámicas en B2B enterprise con contratación única o en negocios industriales pesados pueden no encajar.
- Trata el ratio CLTV/CAC como umbral sin contexto sectorial; la heurística popular de «ratio ≥ 3» no está justificada por esta fuente y debe validarse por sector.
- La fuente no especifica cómo manejar cohortes con perfiles muy distintos (e.g., freemium vs. paid) — el marco se aplica mejor sobre cohortes homogéneas.
- No incorpora el coste de capital ni la dimensión temporal del flujo de caja más allá del payback.
- En motores virales, varias métricas pierden relevancia (CAC puede ser ~0; CLTV requerido es bajo) — el marco encaja mejor con motores de pago y sticky.

## Variants and Extensions

- Versión por cohorte: replicar el cuadro para cada cohorte relevante en lugar de para el agregado.
- Versión segmentada por canal de adquisición: distintos CAC, mismo CLTV, para priorizar canales.
- Extensión multi-producto: tratar cada producto como un motor con sus propias seis métricas y agregar al cierre.
- Versión por motor de crecimiento: aplicar el cuadro con énfasis distinto según motor dominante (CLTV/CAC para pago, churn para sticky, coeficiente de viralidad para viral).

## Relaciones

**justified_by** ← [[aku-cltv-concept]] · [[aku-cac-concept]] · [[aku-arpu-concept]] · [[aku-churn-rate-concept]] · [[aku-cac-payback-concept]] · [[aku-cltv-cac-ratio-concept]] · [[aku-cltv-minus-cac-concept]] · [[aku-cltv-subscription-formula]] · [[aku-cltv-transactional-formula]] · [[aku-cltv-gross-margin-over-revenue]] · [[aku-cltv-cac-dual-optimization]]

**complementary** ↔ [[taku-tres-motores-crecimiento]]
