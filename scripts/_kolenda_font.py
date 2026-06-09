# -*- coding: utf-8 -*-
"""AKUs de «Font Psychology» (Nick Kolenda). source-tag: kolenda."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/kolenda/font-psychology-by-nick-kolenda/font-psychology-by-nick-kolenda.md"
CORE = "aku-font-psychology-las-fuentes-significan-por-congruencia-de-rasgos-concept"
CORE_STMT = ("Las fuentes adquieren significado porque sus rasgos visuales (ancho, peso, redondez, inclinacion, "
 "altura) se parecen a objetos del mundo sensorial y activan, por spreading activation, los conceptos asociados, "
 "ademas de su experiencia pasada (semantica y emocional). Incluye elegir rasgos congruentes con el contexto; "
 "excluye ignorar la adecuacion al contexto; implica que la congruencia rasgo-contexto «se siente bien» y el "
 "lector malatribuye esa emocion positiva a la fuente y al producto.")
TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "Nick Kolenda — Font Psychology"
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
        fh.write(TPL.format(cls=cls,slug=slug,stmt=wrap(stmt),dom="kolenda, fonts, "+dom,src=SRC))
A = [
 ("aku-lineas-finas-y-altas-en-fuentes-transmiten-belleza-claim","claim","beauty",
  "Las lineas finas, ligeras y altas en una fuente transmiten belleza: el estandar de belleza en la mayoria de culturas es alto y delgado, asi que esos rasgos activan el concepto de belleza (las tipografias ligeras se ven delicadas, gentiles y femeninas; Brumberger 2003). Ideal para marcas de belleza (logo de Avon)."),
 ("aku-fuentes-bold-transmiten-poder-y-masculinidad-claim","claim","power",
  "Las fuentes bold transmiten poder, fuerza y masculinidad por su parecido a una estatura corpulenta (Lieven et al. 2015); pueden significar «atrevido/solido» pero tambien «dominante/avasallador». Para legibilidad, los pesos medios fueron los mas legibles (Luckiesh & Moss 1940)."),
 ("aku-fuentes-redondeadas-transmiten-comodidad-y-suavidad-claim","claim","shape",
  "Las fuentes redondeadas transmiten comodidad y suavidad porque preferimos lo redondo (lo afilado se siente amenazante; Bar & Neta 2006): buenas para suavidad, feminidad/belleza y comida dulce. Las angulares, en cambio, van mejor para un tono formal/oficial, rasgos masculinos y comida amarga/salada/agria."),
 ("aku-fuentes-simples-transmiten-franqueza-claim","claim","simplicity",
  "Las fuentes simples y rigidas transmiten franqueza y van mejor para mensajes directos, porque su simplicidad visual encaja con la simplicidad del contexto (Li & Suen 2010)."),
 ("aku-fuentes-complejas-o-dificiles-de-leer-transmiten-exclusividad-claim","claim","disfluency",
  "Las fuentes complejas y dificiles de leer transmiten exclusividad en productos premium: en lo cotidiano la fluidez senala familiaridad y sube la evaluacion, pero en productos especiales/high-end la dificultad de procesamiento los hace sentir mas especiales (la gente compro mas un queso gourmet con fuente dificil; Pocheptsova, Labroo & Dhar 2010)."),
 ("aku-fuentes-inclinadas-transmiten-velocidad-claim","claim","slant",
  "Las fuentes inclinadas (italicas) transmiten movimiento rapido: la convencion grafica retrata los objetos inclinados hacia su movimiento, y la gente identifica antes las palabras «fast» en fuentes inclinadas (Lewis & Walker 1989). Usa italica para comunicar velocidad (p.ej. servicio rapido)."),
 ("aku-fuentes-rectas-transmiten-estabilidad-claim","claim","straight",
  "Las fuentes rectas, con su estructura rigida, transmiten estabilidad y durabilidad."),
 ("aku-serif-vs-sans-serif-eleccion-segun-medio-y-tono-claim","claim","serif",
  "Serif vs sans-serif segun medio y tono: las serif son mas legibles en impreso (los remates guian el flujo horizontal de lectura) y parecen cientificas y elegantes; las sans-serif son mas legibles en pantalla y parecen modernas, informales e innovadoras."),
 ("aku-mayusculas-minusculas-y-caja-mixta-transmiten-poder-compasion-y-legibilidad-claim","claim","case",
  "El uso de mayusculas o minusculas comunica: las minusculas funcionan para marcas «cuidadoras» que promueven compasion y altruismo; las mayusculas para marcas «heroe» que transmiten poder, energia y foco (BMW, Nike, Sony); y la caja mixta es la mas legible (se espera ese patron y las mayusculas se distinguen peor entre si)."),
 ("aku-fuentes-condensadas-vs-espaciadas-transmiten-precision-vs-amplitud-claim","claim","spacing",
  "Las fuentes condensadas transmiten estrechez y precision y van mejor con productos slim (moviles); si las letras se tocan, ese contacto transmite cercania. Las fuentes espaciadas se sienten relajantes («room to breathe»), mientras que las condensadas pueden sentirse abarrotadas o restrictivas (Choi & Kang 2013)."),
 ("aku-fuentes-cortas-vs-altas-transmiten-estabilidad-vs-ligereza-claim","claim","height",
  "La altura de la fuente evoca la gravedad: las fuentes cortas, mas cerca del suelo, transmiten pesadez, estabilidad y durabilidad; las fuentes altas transmiten ligereza, rapidez, aspiracion y lujo (Choi & Kang 2013; Van Rompay et al. 2012)."),
]
def main():
    write(CORE,"concept","typography, perception, marketing-psychology",CORE_STMT)
    for slug,cls,dom,stmt in A: write(slug,cls,dom,stmt)
    print(f"Escritos {len(A)+1} AKUs.")
    edges = [(slug,"supports",CORE) for slug,*_ in A]
    edges += [
     (CORE,"related","aku-identidad-de-marca-concept"),                                    # branding (Power MBA)
     (CORE,"related","aku-que-los-rasgos-linguisticos-reflejen-el-mensaje-claim"),          # copywriting (misma congruencia)
    ]
    wire(edges)
if __name__=="__main__": main()
