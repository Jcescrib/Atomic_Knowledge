# -*- coding: utf-8 -*-
"""AKUs de «Methods of Persuasion» (Nick Kolenda). source-tag: kolenda.
Fuente = stub de imagenes del audiolibro: contiene el framework METHODS (7 pasos, Figure 0.1),
la tabla de priming (Table 1.1) y figuras Ebbinghaus/Asch. Se extrae lo anclado en esas tablas."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/kolenda/audiobook-images-methods-of-persuasion/audiobook-images-methods-of-persuasion.md"
CORE = "aku-methods-proceso-de-persuasion-en-siete-pasos-concept"
CORE_STMT = ("El framework METHODS (Kolenda) estructura la persuasion en siete pasos agrupados en tres fases: ANTES de "
 "la peticion —(1) Mold Their Perception (moldear la percepcion), (2) Elicit Congruent Attitudes (elicitar actitudes "
 "congruentes), (3) Trigger Social Pressure (activar presion social), (4) Habituate Your Message (habituar tu mensaje)—; "
 "DURANTE la peticion —(5) Optimize Your Message (optimizar tu mensaje), (6) Drive Their Momentum (impulsar su "
 "momentum)—; y DESPUES —(7) Sustain Their Compliance (sostener su cumplimiento)—. El acronimo METHODS nombra los siete pasos.")
TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "Nick Kolenda — Methods of Persuasion"
domain: [{dom}]

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
  supported_by: []
  supports: []
  constrained_by: []
  constrains: []
  context_breaks_at: []
  breaks_context_of: []
  contradicts: []
  related: []

sources:
  - {src}

created: 2026-06-09
updated: 2026-06-09
status: active
status_note: "Fuente = stub de imagenes del audiolibro; anclado en Figure 0.1 (framework) y Table 1.1 (priming). Detalle de tacticas en la narracion del audiolibro."
---
{fig}
## Relaciones
"""
def wrap(s): return "\n".join("  " + l for l in s.strip().split("\n"))
def write(slug, cls, dom, stmt, fig=""):
    figblock = f"\n## Figura\n\n![[{fig}]]\n\n" if fig else "\n"
    with open(os.path.join(ROOT,"aku",slug+".md"),"w",encoding="utf-8",newline="\n") as fh:
        fh.write(TPL.format(cls=cls,slug=slug,stmt=wrap(stmt),dom="kolenda, methods-of-persuasion, "+dom,src=SRC,fig=figblock))

EBBING = "77c2aefe03353d7ec2fefbd602ea6a47194224903340ce97d4fc097efe18983d.jpg"
ASCH = "a66ee8e1c518ddab94963901e4273200612f3cad6d0ab2e9550ddd1ab068fe58.jpg"

STEPS = [
 ("aku-methods-step1-moldear-la-percepcion-concept","concept","before",
  "Paso 1 de METHODS — Mold Their Perception: antes de la peticion, moldea como percibe el receptor la situacion, el mensaje y a ti, porque la percepcion es relativa y maleable (ilusion de Ebbinghaus: un circulo parece mayor o menor segun los que lo rodean).", EBBING),
 ("aku-methods-step2-elicitar-actitudes-congruentes-concept","concept","before",
  "Paso 2 de METHODS — Elicit Congruent Attitudes: induce en el receptor actitudes coherentes con tu peticion antes de pedirla (p.ej. via priming), para que cuando llegue ya este predispuesto a favor.", ""),
 ("aku-methods-step3-activar-presion-social-concept","concept","before",
  "Paso 3 de METHODS — Trigger Social Pressure: activa la presion social (prueba social, conformidad) para que el receptor se alinee con lo que hacen los demas (estudio de conformidad de Asch: la gente repite una respuesta erronea del grupo).", ASCH),
 ("aku-methods-step4-habituar-tu-mensaje-concept","concept","before",
  "Paso 4 de METHODS — Habituate Your Message: expon al receptor a tu mensaje repetidamente antes de la peticion, para que la mera exposicion lo vuelva familiar y mas aceptable (mere exposure).", ""),
 ("aku-methods-step5-optimizar-tu-mensaje-concept","concept","during",
  "Paso 5 de METHODS — Optimize Your Message: durante la peticion, optimiza la formulacion del mensaje (palabras, estructura, encuadre) para maximizar su persuasion.", ""),
 ("aku-methods-step6-impulsar-su-momentum-concept","concept","during",
  "Paso 6 de METHODS — Drive Their Momentum: durante la peticion, genera impulso y compromiso progresivo (pequenos pasos que llevan al grande) para que el receptor avance hacia el si.", ""),
 ("aku-methods-step7-sostener-su-cumplimiento-concept","concept","after",
  "Paso 7 de METHODS — Sustain Their Compliance: despues de la peticion, sostiene el cumplimiento en el tiempo reforzando el compromiso y la consistencia del receptor.", ""),
]
PRIMING = ("aku-el-priming-influye-en-la-conducta-claim","claim","priming",
  "El priming —la mera exposicion a estimulos relacionados con un concepto— influye en la conducta posterior sin que la persona sea consciente: palabras de cortesia hacen esperar mas antes de interrumpir, pensar en un amigo aumenta la ayuda, escribir sobre profesores mejora el rendimiento en trivia, un olor a limpiador mantiene la mesa limpia, palabras de culpa aumentan la compra de dulces (Bargh et al. 1996; Fitzsimons & Bargh 2003; Dijksterhuis & van Knippenberg 1998; Holland et al. 2005; Goldsmith et al. 2012).")

def main():
    write(CORE,"concept","persuasion, marketing-psychology",CORE_STMT)
    for slug,cls,dom,stmt,fig in STEPS: write(slug,cls,dom,stmt,fig)
    write(PRIMING[0],PRIMING[1],PRIMING[2],PRIMING[3])
    print(f"Escritos {len(STEPS)+2} AKUs.")
    edges = [(s,"supports",CORE) for s,*_ in STEPS]
    edges += [
     ("aku-el-priming-influye-en-la-conducta-claim","supports","aku-methods-step2-elicitar-actitudes-congruentes-concept"),
     # --- cross-corpus bridges ---
     ("aku-el-priming-influye-en-la-conducta-claim","related","aku-primar-la-eleccion-con-diseno-visual-semantic-priming-claim"),  # priming (Choice)
     ("aku-methods-step1-moldear-la-percepcion-concept","related","aku-evaluamos-por-comparaciones-relativas-context-effects-concept"),  # percepcion relativa (Choice)
     ("aku-methods-step3-activar-presion-social-concept","related","aku-leyes-persuasion-cialdini-concept"),  # prueba social/conformidad (Cialdini)
     ("aku-methods-step5-optimizar-tu-mensaje-concept","related","aku-copywriting-psychology-frases-persuasivas-via-simulacion-mental-concept"),  # optimizar mensaje (Copywriting)
     ("aku-methods-proceso-de-persuasion-en-siete-pasos-concept","related","aku-leyes-persuasion-cialdini-concept"),  # framework persuasion (Cialdini)
    ]
    wire(edges)
if __name__=="__main__": main()
