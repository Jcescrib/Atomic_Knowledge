---
type: taku
taku_type: technique
id: taku-estrategia-concordancias-google
title: "Estrategia de concordancias de palabras clave en Google Ads"
origin: "The Power MBA — Módulo 11 «Google Ads» — Concordancia de palabras clave"
domain: [marketing-digital, sem, google-ads, keywords]

when_to_use: "Al configurar las palabras clave de una campaña de Google Ads para equilibrar alcance y relevancia según el objetivo."
when_not_to_use: "Cuando no se dispone de datos para iterar ni presupuesto para explorar términos amplios."

aku_links:
  justified_by:
    - id: aku-concordancia-palabras-clave-concept
      link_validation: llm-proposed
      link_note: "Define el conjunto de ajustes de concordancia disponibles."
    - id: aku-concordancia-alcance-relevancia-tradeoff-claim
      link_validation: llm-proposed
      link_note: "Justifica la combinación de tipos según el tradeoff alcance/relevancia."
    - id: aku-concordancia-negativa-concept
      link_validation: llm-proposed
      link_note: "Justifica el uso de negativas para filtrar tráfico no deseado."
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

Combinar los distintos tipos de concordancia (amplia, modificada, frase, exacta y
negativa) para captar el tráfico relevante con el equilibrio deseado entre alcance y
relevancia.

## When to Use

Al estructurar las keywords de una campaña, especialmente al lanzar y al optimizar
con datos.

## Prerequisites

Lista de keywords objetivo, conocimiento del producto/marca y de los términos a
excluir.

## Steps

1. Usa **concordancia amplia** para el nombre de marca y para explorar términos.
2. Aplica el **modificador (+)** sobre los términos imprescindibles para acotar.
3. Usa **concordancia de frase («…»)** como opción por defecto en la mayoría de
   keywords.
4. Reserva la **concordancia exacta ([…])** para modelos/colecciones específicas de
   alta intención.
5. Añade **palabras clave negativas (−)** para excluir búsquedas no deseadas
   (p. ej. −barato, −mujer si no aplica).
6. Revisa el informe de términos de búsqueda y reajusta concordancias y negativas.

## Anti-patterns

Dejar todo en amplia por defecto (gasto en tráfico irrelevante); no usar negativas;
no revisar términos de búsqueda reales.

## Expected Outcome

Tráfico más cualificado, mejor relevancia y gasto más eficiente.

## Failure Signals

Muchas impresiones con bajo CTR/conversión; aparición en búsquedas irrelevantes.

## Underlying Logic

Cada tipo de concordancia mueve el equilibrio alcance/relevancia; combinarlos permite
captar volumen donde interesa y precisión donde importa.

## Notes and Variants

Ejemplo (Montblanc): marca en amplia; «+plumas +oficina» en modificada; «plumas
estilográficas» en frase; [Montblanc Meisterstück] en exacta; −baratas en negativa.

## Relaciones

**justified_by** ← [[aku-concordancia-palabras-clave-concept]] · [[aku-concordancia-alcance-relevancia-tradeoff-claim]] · [[aku-concordancia-negativa-concept]]
