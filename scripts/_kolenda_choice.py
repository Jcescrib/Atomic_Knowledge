# -*- coding: utf-8 -*-
"""AKUs de «Choice Psychology» (Nick Kolenda). source-tag: kolenda."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/kolenda/choice/choice.md"
CORE = "aku-choice-psychology-tres-mecanismos-de-decision-concept"
CORE_STMT = ("Las decisiones se rigen por tres mecanismos: (1) simulation fluency —simulas el resultado (beneficios) "
 "menos el proceso (costes) y actuas si hay superavit emocional—; (2) la escala de decision —equilibras misdeeds/"
 "mishaps/obligations/enrichment, asi que una compra emocional (misdeed) pide una justificacion u obligacion que "
 "reequilibre—; y (3) las comparaciones relativas —evaluas las opciones comparandolas entre si, generando context "
 "effects—. Influir en la decision es modular esos tres mecanismos.")
TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "Nick Kolenda — Choice Psychology"
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
status_note: ""
---

## Relaciones
"""
def wrap(s): return "\n".join("  " + l for l in s.strip().split("\n"))
def write(slug, cls, dom, stmt):
    with open(os.path.join(ROOT,"aku",slug+".md"),"w",encoding="utf-8",newline="\n") as fh:
        fh.write(TPL.format(cls=cls,slug=slug,stmt=wrap(stmt),dom="kolenda, choice, "+dom,src=SRC))
A = [
 ("aku-simulation-fluency-simulamos-resultado-menos-proceso-concept","concept","simulation",
  "La «simulation fluency» es el mecanismo por el que decides: antes de actuar simulas el resultado (beneficios) y el proceso (costes), restas ambas emociones y actuas si hay superavit. Incluye buscar alternativas mas baratas y resimular hasta hallar una opcion con saldo positivo; implica que cuanto mas facil y placentera sea la simulacion, mas probable la decision."),
 ("aku-la-escala-de-decision-equilibra-cuatro-conductas-concept","concept","scale",
  "La escala de decision clasifica la conducta por valencia y agencia en cuatro tipos —misdeeds (haces algo malo), mishaps (te pasa algo malo), obligations (haces algo bueno) y enrichment (te pasa algo bueno)— y siempre se busca reequilibrar con la conducta opuesta. Una compra de lujo es un misdeed que pide una obligation o un mishap que lo justifique."),
 ("aku-evaluamos-por-comparaciones-relativas-context-effects-concept","concept","comparison",
  "Evaluamos las opciones comparandolas entre si, no en absoluto (un diccionario «como nuevo» de 10.000 entradas se prefiere solo, pero pierde frente a uno de 20.000 al lado). De ahi los context effects: el efecto compromiso (se elige la opcion intermedia) y el efecto atraccion/senuelo (se elige la opcion similar pero superior a un decoy)."),
 ("aku-gamificar-la-eleccion-experiencial-vs-instrumental-claim","claim","simulation",
  "Convierte la eleccion en experiencial, no instrumental: las elecciones por la experiencia (no por obtener algo) se sienten bien y se simulan como placenteras (Choi & Fishbach 2011). Gamifica (votar con la propina entre «gatos vs perros») transforma un proceso negativo —ceder dinero— en uno positivo de autoexpresion."),
 ("aku-activar-una-mentalidad-de-cual-elegir-which-to-choose-claim","claim","simulation",
  "Activa una mentalidad de «cual elegir»: cualquier eleccion previa (elefante vs hipopotamo) induce el modo «which-to-buy» y hace que el comprador se salte la etapa de «si comprar» y pase directo a «cual comprar» (Xu & Wyer 2008). Cuando eliges, todo parece elegible."),
 ("aku-primar-la-eleccion-con-diseno-visual-semantic-priming-claim","claim","simulation",
  "Prima la eleccion con el diseno visual (semantic priming): un patron distintivo hizo elegir mas productos distintivos (Maimaran & Wheeler 2008). Tu branding visual debe reflejar los rasgos abstractos del producto: si es unico, disenos que «sobresalgan»; si es ligero, colores ligeros."),
 ("aku-reducir-la-culpa-de-las-elecciones-emocionales-claim","claim","scale,guilt",
  "La gente siente culpa al comprar productos de lujo (un misdeed) y necesita justificacion para reequilibrar la escala: o hace algo bueno (obligation) o algo malo le ocurre (mishap). Reducir esa culpa proporcionando una justificacion aumenta la compra emocional."),
 ("aku-ofrecer-incentivos-de-caridad-en-productos-emocionales-claim","claim","scale",
  "Los incentivos de caridad funcionan mejor con productos emocionales (Strahilevitz & Myers 1998): la donacion es una obligation que equilibra la compra de lujo, y el cliente siente que «merece» el premio por su buena accion."),
 ("aku-extraer-esfuerzo-antes-de-elecciones-emocionales-claim","claim","scale",
  "Cualquier esfuerzo (una obligation) justifica las compras emocionales: mas esfuerzo desplaza la preferencia de la necesidad al lujo al reducir la culpa (Kivetz & Simonson 2002). Coloca los productos emocionales al fondo de la tienda, o pon las recompensas emocionales en los tramos altos de un programa de fidelidad."),
 ("aku-anadir-mas-atributos-a-las-descripciones-de-productos-emocionales-claim","claim","scale,attributes",
  "Los productos emocionales se sienten poco practicos, pero anadir mas atributos a la descripcion lo contrarresta: el mero numero de atributos (aunque sean irrelevantes) transforma la compra de un misdeed en una obligation, en algo que el cliente «deberia» comprar (Sela & Berger 2012)."),
 ("aku-usar-lenguaje-asertivo-en-productos-emocionales-claim","claim","scale,language",
  "El lenguaje asertivo es mas efectivo con compras emocionales (Kronrod, Grinstein & Wathieu 2012): el cliente lo usa para justificar la compra —ya no elige indulgir, «alguien le obliga»—."),
 ("aku-aislar-las-opciones-emocionales-claim","claim","scale",
  "Los productos emocionales venden mas presentados solos: la presencia de opciones racionales intensifica la culpa de comprar (Okada 2005). Crea una categoria «guilty pleasures», muestra los items individualmente (la presentacion secuencial reduce comparaciones) o restringe el numero de opciones (los menus grandes empujan a la opcion «justificable»)."),
 ("aku-mostrar-el-surtido-completo-de-opciones-claim","claim","comparison",
  "Muestra el surtido completo de opciones a la vez, nunca de una en una: en presentacion secuencial el cliente «espera» una opcion mejor que aparezca, mientras que en simultanea se centra en comparar el set actual (Mogilner, Shiv & Iyengar 2013)."),
 ("aku-subir-los-atributos-indeseables-por-encima-de-cero-zero-comparison-claim","claim","comparison",
  "Subir un atributo indeseable por encima de cero puede aumentar el valor percibido (efecto zero-comparison): frente a 0, cualquier numero es infinitamente mayor y la comparacion se vuelve imposible, asi que el cliente pierde el punto de referencia relativo (5g de grasa vs 0g no se comparan; vs 1g si; Palmeira 2011). A la inversa, baja a 0 un atributo deseable pequeno para impedir la comparacion."),
 ("aku-dividir-los-atributos-importantes-en-mas-items-claim","claim","comparison",
  "La gente reparte recursos por igual entre las opciones disponibles (partition dependence; Fox, Bardolet & Lieb 2005), asi que dividir una categoria importante en mas items aumenta su peso: separar «sano» en «verduras» y «fruta» (frente a un solo «no sano») hace que se elija mas comida sana."),
 ("aku-anadir-senales-sensoriales-para-captar-atencion-claim","claim","comparison,attention",
  "La gente elige mas una opcion si la mira mas tiempo, asi que distingue tu opcion objetivo (color, tamano, forma) o anade senales sensoriales que capten la atencion (se eligio mas una maquina expendedora bajo un altavoz; Shen & Sengupta 2014)."),
 ("aku-colocar-la-opcion-objetivo-en-el-centro-claim","claim","comparison,position",
  "Coloca tu opcion objetivo en el centro: el ojo va primero al centro y, al mirar las opciones laterales, lo cruza repetidamente (efecto central gaze cascade), y cuanto mas miras una opcion mas te gusta (y viceversa). El 71% elige productos de las dos filas centrales (Atalay et al. 2012; Christenfeld 1995)."),
 ("aku-colocar-la-opcion-objetivo-primera-o-ultima-claim","claim","comparison,position",
  "Cuando las opciones se ven de una en una (no simultaneas), coloca tu opcion primera o ultima: la primera impacta la memoria a largo plazo y la ultima la memoria de trabajo (Miller & Campbell 1959). Una entrevista a primera hora se recuerda mas a largo plazo; a ultima hora pesa mas en una decision inmediata."),
 ("aku-alinear-las-caracteristicas-con-las-de-la-competencia-claim","claim","comparison",
  "Alinea tus caracteristicas con las de la competencia: cuando el cliente cree que dos opciones son similares, cualquier ventaja menor decide (eliges «Paris + 1$» sobre «Paris», pero no sobre «Roma»). Si tu producto parece similar pero superior al rival, gravitan hacia el tuyo."),
]
def main():
    write(CORE,"concept","decision-making, marketing-psychology",CORE_STMT)
    for slug,cls,dom,stmt in A: write(slug,cls,dom,stmt)
    print(f"Escritos {len(A)+1} AKUs.")
    edges = [(slug,"supports",CORE) for slug,*_ in A]
    edges += [
     ("aku-evaluamos-por-comparaciones-relativas-context-effects-concept","related","aku-ofrecer-una-version-similar-pero-mas-cara-como-senuelo-decoy-claim"),  # decoy (cross-libro Pricing)
     ("aku-reducir-la-culpa-de-las-elecciones-emocionales-claim","related","aku-atribuir-el-descuento-al-producto-emocional-del-bundle-claim"),          # culpa emocional (cross-libro Pricing)
     ("aku-extraer-esfuerzo-antes-de-elecciones-emocionales-claim","related","aku-arreglar-descuentos-en-tramos-escalonados-claim"),                     # simulation fluency (cross-libro Pricing)
     ("aku-aislar-las-opciones-emocionales-claim","related","aku-muestra-el-producto-antes-del-precio-en-productos-emocionales-claim"),                  # productos emocionales (cross-libro Pricing)
    ]
    wire(edges)
if __name__=="__main__": main()
