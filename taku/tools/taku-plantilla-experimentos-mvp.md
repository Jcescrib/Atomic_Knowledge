---
type: taku
taku_type: tool
id: taku-plantilla-experimentos-mvp
title: "Plantilla de experimentos Lean Startup (Hipótesis · MVP · Aprendizaje)"
origin: "The Power MBA — Módulo 3.0.1 «El método Lean Startup»"
domain: [lean-startup, mvp, validation, methodology, power-mba]

when_to_use: >
  Cuando se va a ejecutar cada vuelta del ciclo Build-Measure-Learn:
  documentar la hipótesis crítica a testar, el experimento o MVP elegido
  para validarla y lo que se medirá, y al cierre el aprendizaje validado y
  la consecuencia para la siguiente iteración. Útil para mantener
  disciplina del método y construir histórico de aprendizajes a lo largo
  del proyecto.

when_not_to_use: >
  Como sustituto del trabajo de identificar las hipótesis críticas (la
  plantilla no decide qué testar, solo lo registra). Tampoco como vehículo
  de teatro Lean: rellenarla sin haber realizado el experimento real ni
  medido comportamiento real anula su valor.

aku_links:
  justified_by:
    - id: aku-lean-startup-method-concept
      link_validation: llm-proposed
      link_note: "Marco donde la plantilla opera."
    - id: aku-hipotesis-concept
      link_validation: llm-proposed
      link_note: "Primer campo de la plantilla."
    - id: aku-mvp-concept
      link_validation: llm-proposed
      link_note: "Segundo campo — qué experimento se hace."
    - id: aku-aprendizaje-validado-concept
      link_validation: llm-proposed
      link_note: "Tercer campo — qué se aprendió, qué cambia."
    - id: aku-build-measure-learn-concept
      link_validation: llm-proposed
      link_note: "Es una vuelta concreta del ciclo."
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
  complementary: [taku-entrevista-problem-solution]
  alternative_to: []
  precedes: []
  follows: []

created: 2026-06-03
updated: 2026-06-03
status: draft
status_note: ""
---

## Summary

Plantilla mínima de tres campos para documentar cada vuelta del ciclo Build-Measure-Learn. Fuerza a articular la hipótesis explícitamente antes de actuar, definir el experimento concreto y la métrica que confirmaría/falsificaría la hipótesis antes de ejecutar, y cerrar con el aprendizaje obtenido y la decisión sobre la siguiente vuelta. Su valor está en la disciplina, no en la sofisticación.

## Mechanic

Tres campos en serie:

1. **HIPÓTESIS** — «Creemos que...»  
   Articular la afirmación concreta que aún no se ha validado. Buena hipótesis: específica, falsificable, atribuible a una variable del modelo (cliente, precio, canal, retención…). Ejemplo: «Creemos que el cliente va a pagar 35€/mes por nuestro software».

2. **EXPERIMENTOS / MVP** — «Para validarlo vamos a... Y vamos a medir...»  
   Diseñar el experimento mínimo que valide la hipótesis. Definir QUÉ se va a hacer y QUÉ se va a medir antes de actuar. El umbral de éxito/fracaso debe ser explícito ANTES de mirar los datos para evitar racionalización post-hoc.

3. **APRENDIZAJE** — «Hemos aprendido que... Así que vamos a cambiar...»  
   Cerrar con qué se confirmó/falsificó y qué decisión concreta sigue. Si la hipótesis falla, pivotar; si se confirma, abordar la siguiente hipótesis crítica.

## Input

- Una idea de negocio o decisión con alta incertidumbre.
- Una hipótesis crítica identificada (la plantilla NO ayuda a descubrirla, solo a documentarla).

## Process

1. Rellenar el campo **HIPÓTESIS** con la afirmación específica y falsificable.
2. Definir el **EXPERIMENTO / MVP** y la métrica de éxito ANTES de actuar.
3. Acordar el umbral de éxito/fracaso antes de mirar los datos.
4. Ejecutar el experimento.
5. Medir el resultado con la métrica acordada.
6. Rellenar el campo **APRENDIZAJE**: ¿se valida o no?
7. Decidir la siguiente iteración (pivotar o seguir).
8. Archivar la plantilla — construir histórico de aprendizajes.

## Output

Un registro estructurado por ciclo Build-Measure-Learn con:
- Hipótesis testada.
- Experimento ejecutado y métrica.
- Aprendizaje validado.
- Decisión derivada.

Sumadas, las plantillas forman un histórico que documenta cómo el modelo evolucionó hasta encontrar PMF (o por qué se abandonó).

## Interpretation Guide

- Una hipótesis sin métrica de éxito específica NO es testable; volver a formularla.
- Si el aprendizaje es «hemos aprendido que necesitamos más datos», la métrica no estaba bien definida o el MVP era prematuro.
- Si todas las hipótesis se «validan», sospechar de sesgo de confirmación o métricas demasiado laxas.
- Un histórico de plantillas con muchos pivots NO es señal de fracaso; es señal de aprendizaje activo. Cero pivots es la señal de alerta.

## Limitations

- No ayuda a identificar QUÉ hipótesis testar primero (eso requiere análisis aparte del modelo).
- No previene rellenarla sin ejecutar el experimento (teatro Lean).
- No incorpora cuantitativamente el coste/riesgo del experimento; útil añadir esos campos al usar la plantilla en contextos con presupuestos limitados.
- Asume disciplina del equipo en mirar los resultados con honestidad; si el equipo está enamorado de la idea, la plantilla no protege contra racionalización.

## Example Application

> **HIPÓTESIS**: Creemos que un 5% de las visitas a la landing page se convertirán en leads cualificados (email + teléfono).
> 
> **EXPERIMENTO / MVP**: Vamos a lanzar landing page con propuesta concreta + CTA («Empezar prueba gratis»). Vamos a llevarle 1.000 visitas vía publicidad dirigida en Facebook Ads (presupuesto: 200€). Vamos a medir conversión visita → lead durante 7 días.
> 
> **APRENDIZAJE**: Hemos aprendido que la conversión real fue del 1,2% (12 leads de 1.000 visitas), muy por debajo del 5% hipotetizado. Así que vamos a cambiar: probar dos variantes de propuesta de valor en la landing (A/B test) antes de invertir más en captación, porque la hipótesis crítica ahora es la propuesta, no el volumen.

## Relaciones

**justified_by** ← [[aku-lean-startup-method-concept]] · [[aku-hipotesis-concept]] · [[aku-mvp-concept]] · [[aku-aprendizaje-validado-concept]] · [[aku-build-measure-learn-concept]]

**complementary** ↔ [[taku-entrevista-problem-solution]]
