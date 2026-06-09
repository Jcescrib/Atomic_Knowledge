# -*- coding: utf-8 -*-
"""AKUs de «Visual Attention» (Nick Kolenda) — modo máximo-exhaustivo. source-tag: kolenda."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/kolenda/visual-attention-by-nick-kolenda/visual-attention-by-nick-kolenda.md"
CORE = "aku-visual-attention-captamos-estimulos-de-amenaza-ancestral-concept"
CORE_STMT = ("La atencion es selectiva (percibimos solo una fraccion de los estimulos que entran), y captamos "
 "automaticamente aquellos que ayudaron a sobrevivir a nuestros ancestros —amenazas, presas, parejas— por "
 "mecanismos heredados de deteccion rapida que interrumpen la atencion voluntaria. Incluye saliencia, movimiento, "
 "agentes, claves espaciales, alta activacion, lo inesperado y lo auto/meta-relevante; implica que para captar "
 "atencion hay que mostrar estimulos que amenazaban la supervivencia ancestral, aunque hoy parezcan inofensivos.")
TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "Nick Kolenda — Visual Attention"
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
        fh.write(TPL.format(cls=cls,slug=slug,stmt=wrap(stmt),dom="kolenda, visual-attention, "+dom,src=SRC))
A = [
 ("aku-el-color-capta-la-atencion-claim","salience","El color es quiza la dimension mas saliente: usa un color que contraste con el entorno (mira los thumbnails vecinos en YouTube y elige uno que destaque). Las mujeres notan mas los estimulos rojos por su rol recolector ancestral (Milosavljevic & Cerf 2008; Regan et al. 2001)."),
 ("aku-la-desalineacion-de-orientacion-capta-la-atencion-claim","salience","Notamos la desalineacion: un estimulo inclinado respecto a su entorno capta la atencion (Treisman & Gormican 1988). Ej.: anade rectangulos blancos arriba y abajo de un post de Facebook para que se vea ladeado."),
 ("aku-el-tamano-contrastante-capta-la-atencion-claim","salience","El tamano contrastante capta la atencion, sobre todo con longitudes y numeros (Huang & Pashler 2005). Ej.: si los titulares vecinos en Reddit/HN son cortos, escribe uno largo, y viceversa."),
 ("aku-el-motion-onset-capta-la-atencion-claim","motion","El inicio del movimiento («motion onset») capta la atencion (Abrams & Christ 2003). Ej.: anade un motion onset sutil (pulso) al boton de tu web para que se note."),
 ("aku-el-movimiento-looming-capta-la-atencion-claim","motion","El movimiento «looming» (algo que se agranda, acercandose) capta la atencion porque sugiere urgencia conductual: lo que se aproxima exige reaccion inmediata mas que lo que se aleja (Franconeri & Simons 2005). Ej.: empieza un video con un zoom hacia dentro."),
 ("aku-el-movimiento-animado-impredecible-capta-la-atencion-claim","motion","El movimiento animado —impredecible— capta la atencion: nuestros ancestros necesitaban detectar el movimiento de depredadores que atacaban sin aviso (Pratt et al. 2010)."),
 ("aku-la-imagineria-dinamica-capta-la-atencion-claim","motion","El movimiento no necesita ser literal: las imagenes que solo representan movimiento captan mas atencion (Cian, Krishna & Elder 2015). Ej.: anade movimiento (dinamismo) al thumbnail de una app o a una senal de trafico."),
 ("aku-la-capacidad-de-movimiento-de-una-forma-capta-la-atencion-claim","motion","La capacidad de movimiento de una forma capta la atencion: una «V» se encuentra mas rapido que una «Λ» porque puede inclinarse de lado a lado (mientras la Λ es estable), y notamos mas los estimulos con capacidad de moverse (Larson, Aronoff & Stearns 2007; reinterpretado por Kolenda)."),
 ("aku-el-movimiento-biologico-capta-la-atencion-claim","motion","El movimiento biologico —los movimientos corporales naturales de nuestra especie— capta la atencion (la pSTS responde mas al movimiento humano que al animal): hasta los pollitos recien nacidos prefieren el movimiento natural de una gallina al de una artificial (Troje 2008; Vallortigara et al. 2005)."),
 ("aku-las-caras-captan-la-atencion-claim","agents","Las caras captan la atencion (activan el fusiform gyrus; detectamos cambios en caras mejor que en otros objetos), pero deben estar derechas (face inversion effect). Ironicamente, las caras esquematicas/geometricas captan mas que las realistas porque el cerebro busca el patron geometrico (Allison et al. 2000; Aronoff 2006)."),
 ("aku-los-cuerpos-humanos-captan-la-atencion-claim","agents","Los cuerpos humanos captan la atencion (region cortical selectiva en la corteza lateral occipitotemporal): unos «blobs» captaron mas atencion cuando se parecian a un cuerpo humano, y se atiende aun mas cuando hay cara y cuerpo a la vez (Downing et al. 2001, 2004)."),
 ("aku-las-partes-del-cuerpo-realistas-captan-la-atencion-claim","agents","Hay regiones cerebrales que detectan partes del cuerpo individuales, con relacion directa entre activacion y realismo (mas activacion con manos realistas; Peelen & Downing 2007; Desimone et al. 1984)."),
 ("aku-los-animales-captan-la-atencion-claim","agents","Los animales captan la atencion (de ahi la viralidad de los gatos): nuestros ancestros recolectores necesitaban detectarlos (depredadores, comida, peligros), y el sistema es category-driven, activado automaticamente por cualquier cosa categorizada como animal (New, Cosmides & Tooby 2007)."),
 ("aku-la-mirada-eye-gaze-capta-la-atencion-claim","spatial","La mirada (eye gaze) capta la atencion automaticamente, ligada a la dominancia social: todos miran mas a la criatura dominante, y los ancestros que no seguian esas miradas elegian la pelea equivocada y morian. Por eso el seguimiento de mirada esta «hard-wired» y los ojos evolucionaron para ser muy salientes (Emery 2000; Langton et al. 2000)."),
 ("aku-la-orientacion-del-cuerpo-capta-la-atencion-claim","spatial","La orientacion del cuerpo implica la direccion de la mirada y capta la atencion; su efecto es aditivo con el eye gaze, asi que conviene incorporar tantas claves espaciales como sea posible (Langton & Bruce 2000)."),
 ("aku-senalar-con-el-dedo-capta-la-atencion-claim","spatial","Senalar capta la atencion, y un dedo indice aislado es el gesto que mas atencion capta (tiene la optima facilidad/precision; los padres ensenan el mundo senalando, lo que instila una respuesta automatica de mirar; Ariga & Watanabe 2009)."),
 ("aku-las-flechas-captan-la-atencion-claim","spatial","Las flechas captan la atencion, igual que otras claves espaciales aprendidas (Ristic & Kingstone 2006)."),
 ("aku-las-palabras-direccionales-captan-la-atencion-claim","spatial","Las palabras direccionales/espaciales captan la atencion (Hommel et al. 2001). Ej.: no pidas «envia el formulario amarillo» (hay daltonicos); pide «envia el formulario amarillo debajo de las instrucciones»."),
 ("aku-las-amenazas-captan-la-atencion-alta-activacion-claim","arousal","Las emociones de alta activacion (arousal) captan la atencion, y las amenazas especialmente: el cerebro detecta una amenaza y dispara la defensa antes de notarla conscientemente (de ahi el miedo a serpientes/aranas, detectando la forma curvilinea, no el animal en si; Anderson 2005; Öhman & Mineka 2001; LoBue 2014)."),
 ("aku-los-estimulos-sexuales-captan-la-atencion-claim","arousal","Los estimulos sexuales estan hard-wired en el sistema de atencion: nuestros ancestros se reproducian mas al encontrar pareja, asi que captan la atencion automaticamente (Most et al. 2007)."),
 ("aku-las-palabras-tabu-captan-la-atencion-claim","unexpected","Las palabras tabu captan mas atencion que las palabras meramente emocionales (Mathewson, Arnell & Mansfield 2008); algunos oradores (Tony Robbins) sostienen la atencion con tacos."),
 ("aku-la-novedad-capta-la-atencion-claim","unexpected","La novedad capta la atencion (los bebes miran mas los patrones nuevos): detectar lo nuevo tenia valor de supervivencia. Ej.: la pique technique —pedir una cantidad inusual (37 centavos) en vez de una estandar— evita el rechazo automatico al forzar a evaluar la peticion (Fantz 1964; Santos, Leve & Pratkanis 1994)."),
 ("aku-tu-nombre-capta-la-atencion-cocktail-party-claim","self","Tu propio nombre capta la atencion (efecto cocktail party): aunque estes inmerso en una conversacion, oir tu nombre cerca te lo arranca la atencion (activa el cortex prefrontal medial), incluso de forma subliminal. La personalizacion es potente pero puede resultar creepy con demasiada (Moray 1959; Alexopoulos et al. 2012)."),
 ("aku-tu-cara-capta-la-atencion-claim","self","Tu propia cara es tan potente como tu nombre para captar tu atencion (red bilateral con alta implicacion del hemisferio derecho; Tacikowski & Nowicka 2010). Ej.: un probador virtual donde el usuario sube su foto para verse la ropa puesta."),
 ("aku-se-capta-mas-atencion-con-baja-carga-cognitiva-sin-meta-activa-claim","goal","Se notan mas los estimulos cuando no hay una meta activa, porque la carga cognitiva es menor y deja sitio para la atencion: los compradores notaron menos un banner mientras buscaban productos concretos, y mas cuando solo curioseaban. Anuncia en contextos de baja carga cognitiva (Cartwright-Finch & Lavie 2007; Resnick & Albert 2014)."),
 ("aku-haz-tu-estimulo-similar-a-lo-que-el-objetivo-monitorea-goal-directed-claim","goal","Cuando alguien busca un estimulo (p.ej. azul) no nota los demas (rojos): para captar su atencion, haz tu estimulo similar a lo que esta monitoreando. Ej.: emitir un anuncio durante una pausa con una celebridad de la serie que el espectador esta viendo, porque monitorea inconscientemente claves de su programa (Baluch & Itti 2011)."),
]
def main():
    write(CORE,"concept","attention, evolutionary-psychology, marketing-psychology",CORE_STMT)
    for slug,dom,stmt in A: write(slug, "claim", dom, stmt)
    print(f"Escritos {len(A)+1} AKUs.")
    edges=[(slug,"supports",CORE) for slug,_,_ in A]
    edges += [
     ("aku-el-color-capta-la-atencion-claim","related","aku-los-colores-saturados-parecen-mas-grandes-claim"),       # color/atencion (cross-libro Color)
     ("aku-tu-nombre-capta-la-atencion-cocktail-party-claim","related","aku-ajustar-los-numerales-al-nombre-o-cumpleanos-egotismo-implicito-claim"),  # egotismo implicito (cross-libro Pricing)
     ("aku-la-mirada-eye-gaze-capta-la-atencion-claim","related","aku-colocar-la-opcion-objetivo-en-el-centro-claim"),  # gaze (cross-libro Choice)
     ("aku-la-novedad-capta-la-atencion-claim","related","aku-crear-percepcion-de-demanda-y-exclusividad-enciende-la-demanda-real-claim"),  # novedad/atencion (50-cent)
    ]
    wire(edges)
if __name__=="__main__": main()
