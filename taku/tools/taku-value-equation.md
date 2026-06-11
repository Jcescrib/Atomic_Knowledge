---
type: taku
taku_type: tool
id: taku-value-equation
title: "Ecuación de valor (Value Equation)"
origin: "Alex Hormozi — $100M Offers"
domain: [value-proposition, pricing, hormozi]

when_to_use: "Para diagnosticar y aumentar el valor percibido de una oferta, comparar vehículos que satisfacen el mismo deseo, o decidir dónde invertir para diferenciarte."
when_not_to_use: "No sustituye la validación con clientes reales: rinde una estimación de valor percibido, no una métrica de mercado."

aku_links:
  justified_by:
    - id: aku-value-equation-concept
      link_validation: human-validated
      link_note: ""
    - id: aku-dream-outcome-concept
      link_validation: human-validated
      link_note: ""
    - id: aku-perceived-likelihood-achievement-concept
      link_validation: human-validated
      link_note: ""
    - id: aku-time-delay-value-concept
      link_validation: human-validated
      link_note: ""
    - id: aku-effort-sacrifice-concept
      link_validation: human-validated
      link_note: ""
    - id: aku-ecuacion-valor-claim
      link_validation: human-validated
      link_note: "deducible: corrobora aku-value-equation-concept desde [power-mba] (cross-source)"
    - id: aku-matriz-rice-concept
      link_validation: human-validated
      link_note: "deducible: corrobora aku-value-equation-concept desde [power-mba] (cross-source)"
    - id: aku-propuesta-de-valor-concept
      link_validation: human-validated
      link_note: "deducible: corrobora aku-value-equation-concept desde [power-mba] (cross-source)"
    - id: aku-cosas-importantes-concept
      link_validation: human-validated
      link_note: "deducible: corrobora aku-dream-outcome-concept desde [power-mba] (cross-source)"
    - id: aku-emocion-prevalece-razon-claim
      link_validation: human-validated
      link_note: "deducible: corrobora aku-dream-outcome-concept desde [power-mba] (cross-source)"
    - id: aku-beneficio-emocional-concept
      link_validation: human-validated
      link_note: "deducible: corrobora aku-dream-outcome-concept desde [power-mba] (cross-source)"
    - id: aku-copy-aportar-pruebas-claim
      link_validation: human-validated
      link_note: "deducible: corrobora aku-perceived-likelihood-achievement-concept desde [power-mba] (cross-source)"
    - id: aku-cialdini-autoridad-concept
      link_validation: human-validated
      link_note: "deducible: corrobora aku-perceived-likelihood-achievement-concept desde [power-mba] (cross-source)"
  constrained_by:
    - id: aku-perception-is-reality-value-claim
      link_validation: human-validated
      link_note: ""
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

Herramienta para cuantificar y mejorar el valor percibido de una oferta a partir de
cuatro drivers: dos a maximizar (Dream Outcome, Probabilidad Percibida de Logro) y dos
a minimizar (Time Delay, Esfuerzo y Sacrificio).

## Mechanic

Valor ≈ (Dream Outcome × Probabilidad Percibida de Logro) / (Time Delay × Esfuerzo y
Sacrificio). El denominador manda: cuanto más cerca de 0, mayor el valor.

## Input

Una oferta concreta (vehículo) y el deseo del cliente al que sirve.

## Process

1. Define el dream outcome del cliente (en términos de status).
2. Puntúa cada driver (p. ej. 0/1 o 0–10): los dos de arriba más alto = mejor; los dos
   de abajo más bajo = mejor.
3. Identifica el driver más débil y rediseña la oferta para mejorarlo —prioriza la parte
   de abajo (time delay y esfuerzo), más difícil de copiar.
4. Asegúrate de **comunicar** cada mejora: el valor solo cuenta si se percibe.

## Output

Un perfil de los cuatro drivers y una lista priorizada de mejoras a la oferta.

## Interpretation Guide

Si dos ofertas comparten dream outcome, la diferencia de precio la explican los otros
tres drivers. «Done for you» > «do it yourself» por menor esfuerzo y mayor probabilidad
percibida. Velocidad (bajar time delay) supera incluso a «gratis».

## Limitations

Los drivers son perceptuales, no numéricos exactos; el scoring es orientativo. No mide
demanda de mercado: una oferta de valor alto en un mal mercado igualmente fracasa.

## Example Application

Meditación vs Xanax (mismo dream outcome «relajación»): Xanax puntúa 4/4 y la meditación
1,5/4 por su mayor probabilidad percibida, menor time delay y menor esfuerzo — de ahí la
enorme diferencia de valor de mercado pese al mismo resultado prometido.

## Relaciones

**justified_by** ← [[aku-value-equation-concept]] · [[aku-dream-outcome-concept]] · [[aku-perceived-likelihood-achievement-concept]] · [[aku-time-delay-value-concept]] · [[aku-effort-sacrifice-concept]] · [[aku-ecuacion-valor-claim]] · [[aku-matriz-rice-concept]] · [[aku-propuesta-de-valor-concept]] · [[aku-cosas-importantes-concept]] · [[aku-emocion-prevalece-razon-claim]] · [[aku-beneficio-emocional-concept]] · [[aku-copy-aportar-pruebas-claim]] · [[aku-cialdini-autoridad-concept]]

**constrained_by** ← [[aku-perception-is-reality-value-claim]]
