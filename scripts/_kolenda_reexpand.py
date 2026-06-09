# -*- coding: utf-8 -*-
"""Re-expansion retroactiva (modo máximo-exhaustivo) de los 7 libros Kolenda ya ingeridos:
desglosa los sub-tips consolidados en AKUs propios. Cada nuevo AKU supports->núcleo del libro
y related->su AKU-paraguas. source-tag: kolenda."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SRC = {
 "pricing":"raw/libros/kolenda/pricing-psychology-by-nick-kolenda/pricing-psychology-by-nick-kolenda.md",
 "copy":"raw/libros/kolenda/copywriting-psychology-by-nick-kolenda/copywriting-psychology-by-nick-kolenda.md",
 "font":"raw/libros/kolenda/font-psychology-by-nick-kolenda/font-psychology-by-nick-kolenda.md",
 "pack":"raw/libros/kolenda/packaging-psychology-by-nick-kolenda/packaging-psychology-by-nick-kolenda.md",
 "color":"raw/libros/kolenda/color-psychology2/color-psychology2.md",
 "ecom":"raw/libros/kolenda/ecommerce-psychology-by-nick-kolenda/ecommerce-psychology-by-nick-kolenda.md",
}
CORE = {
 "pricing":"aku-pricing-psychology-el-precio-es-percepcion-concept",
 "copy":"aku-copywriting-psychology-frases-persuasivas-via-simulacion-mental-concept",
 "font":"aku-font-psychology-las-fuentes-significan-por-congruencia-de-rasgos-concept",
 "pack":"aku-packaging-psychology-el-envase-comunica-por-heuristicas-visuales-concept",
 "color":"aku-color-psychology-el-significado-del-color-depende-del-contexto-y-la-experiencia-concept",
 "ecom":"aku-ecommerce-psychology-optimizar-el-funnel-via-simulacion-de-compra-concept",
}
ORIGIN = {
 "pricing":"Nick Kolenda — Pricing Psychology","copy":"Nick Kolenda — Copywriting Psychology",
 "font":"Nick Kolenda — Font Psychology","pack":"Nick Kolenda — Packaging Psychology",
 "color":"Nick Kolenda — Color Psychology","ecom":"Nick Kolenda — eCommerce Psychology",
}
TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "{origin}"
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
# (slug, book, dom, umbrella, statement)
A = [
 # ── Pricing: partitioned -> shipping + installments ──
 ("aku-separar-el-coste-de-envio-del-precio-claim","pricing","pricing,partitioned","aku-dividir-el-precio-en-unidades-mas-pequenas-partitioned-prices-claim",
  "Separar el coste de envio del precio (precio particionado) aumento los ingresos en subastas online (0,01\\$ + 3,99\\$ de envio supero a 4\\$ con envio gratis; Hossain & Morgan 2006). Cautela: hoy muchos clientes esperan envio gratis, asi que el efecto puede estar desactualizado."),
 ("aku-ofrecer-el-precio-en-cuotas-claim","pricing","pricing,partitioned","aku-dividir-el-precio-en-unidades-mas-pequenas-partitioned-prices-claim",
  "Ofrecer el precio en cuotas reduce la magnitud percibida: en vez de un curso por 1.250\\$, «12 pagos de 115\\$» hace que el cliente compare la cifra menor (115\\$) con su precio de referencia."),
 ("aku-precios-redondos-en-compras-emocionales-claim","pricing","pricing,round","aku-usar-precios-redondos-en-el-contexto-adecuado-claim",
  "En compras emocionales, los precios redondos (40\\$) «se sienten bien», una sensacion que casa con la naturaleza del producto: se prefirio champan con precio redondo (40\\$) frente a uno con precio especifico (Wadhwa & Zhang 2015)."),
 ("aku-precios-redondos-en-compras-de-conveniencia-claim","pricing","pricing,round","aku-usar-precios-redondos-en-el-contexto-adecuado-claim",
  "En compras de conveniencia, los precios redondos disparan una sensacion de «facil/rapido» que el cliente malatribuye a la transaccion (parece mas rapida); usalos cuando el cliente quiere un checkout veloz (Wieseke, Kolberg & Schons 2016)."),
 ("aku-precios-redondos-en-productos-sociales-claim","pricing","pricing,round","aku-usar-precios-redondos-en-el-contexto-adecuado-claim",
  "En productos sociales (p.ej. entradas a un evento), los precios redondos —divisibles por otros numeros— se prefieren porque el cliente confunde la conectividad numerica con la conectividad social (Yan & Sengupta 2021)."),
 # ── Copywriting: diversify -> lengths + emotions ──
 ("aku-variar-la-longitud-de-las-frases-claim","copy","copywriting,linguistics","aku-diversificar-palabras-sintaxis-y-emociones-claim",
  "Varia la longitud de las frases: una sucesion de frases cortas se vuelve repetitiva y aburrida, y el cerebro pide un cambio; intercalar una frase larga refresca la lectura. La monotonia de longitud hace perder interes al lector."),
 ("aku-variar-las-emociones-del-contenido-claim","copy","copywriting,linguistics","aku-diversificar-palabras-sintaxis-y-emociones-claim",
  "Varia las emociones del contenido: el analisis de 4.000+ peliculas y 30.000+ articulos mostro que el contenido tiene mas exito cuando cambia de emocion de forma impredecible (Berger, Kim & Meyer 2021)."),
 # ── Font: poles ──
 ("aku-fuentes-angulares-transmiten-formalidad-y-masculinidad-claim","font","fonts,shape","aku-fuentes-redondeadas-transmiten-comodidad-y-suavidad-claim",
  "Las fuentes angulares transmiten un tono formal y oficial, rasgos masculinos y van mejor con comida amarga, salada o agria (lo afilado se asocia a amenaza/dureza; Brumberger 2003; Velasco et al. 2015)."),
 ("aku-fuentes-sans-serif-son-modernas-informales-y-legibles-en-pantalla-claim","font","fonts,serif","aku-serif-vs-sans-serif-eleccion-segun-medio-y-tono-claim",
  "Las fuentes sans-serif son mas legibles en pantalla (la rejilla de pixeles degrada los remates) y parecen modernas, informales, innovadoras y cutting-edge (Tantillo et al. 1995)."),
 ("aku-las-mayusculas-transmiten-poder-y-fuerza-claim","font","fonts,case","aku-mayusculas-minusculas-y-caja-mixta-transmiten-poder-compasion-y-legibilidad-claim",
  "Las mayusculas transmiten poder, energia, coraje y foco, y van bien con marcas «heroe» (BMW, Diesel, Duracell, Nike, Sony usan mayusculas para expresar fuerza; Oosterhout 2013)."),
 ("aku-la-caja-mixta-es-la-mas-legible-claim","font","fonts,case","aku-mayusculas-minusculas-y-caja-mixta-transmiten-poder-compasion-y-legibilidad-claim",
  "La caja mixta es la mas legible porque se espera ese patron (el cerebro lo busca) y las mayusculas se distinguen peor entre si al compartir altura (Garvey, Pietrucha & Meeker 1997)."),
 ("aku-fuentes-espaciadas-se-sienten-relajantes-claim","font","fonts,spacing","aku-fuentes-condensadas-vs-espaciadas-transmiten-precision-vs-amplitud-claim",
  "Las fuentes espaciadas se sienten relajantes y dan «room to breathe / room to move», mientras que las condensadas pueden percibirse abarrotadas y restrictivas del movimiento (Choi & Kang 2013)."),
 ("aku-fuentes-altas-transmiten-ligereza-y-lujo-claim","font","fonts,height","aku-fuentes-cortas-vs-altas-transmiten-estabilidad-vs-ligereza-claim",
  "Las fuentes altas transmiten ligereza y rapidez, y resultan aspiracionales y lujosas (Choi & Kang 2013; Van Rompay et al. 2012)."),
 # ── Packaging: angular pole ──
 ("aku-envases-angulares-parecen-masculinos-y-picantes-claim","pack","packaging,shape","aku-envases-redondeados-parecen-dulces-y-femeninos-claim",
  "Los envases angulares parecen masculinos (la angularidad evoca rasgos masculinos por raices evolutivas) y heredan rasgos asociados como lo picante; elige envase angular para comida picante o productos masculinos (Pang & Ding 2021; Velasco et al. 2014)."),
 # ── Color: preferences split ──
 ("aku-preferencia-evolutiva-por-colores-calidos-claim","color","color,preferences","aku-las-preferencias-de-color-vienen-de-la-evolucion-y-la-valencia-ecologica-claim",
  "Hay una preferencia evolutiva por colores calidos/rojizos: las mujeres la desarrollaron por su rol ancestral recolector (identificar colores calidos sobre follaje verde), y algunas preferencias vienen de una necesidad biologica (los sedientos prefieren colores glossy; Alexander 2003; Meert, Pandelaere & Patrick 2014)."),
 ("aku-valencia-ecologica-preferimos-colores-de-experiencias-positivas-claim","color","color,preferences","aku-las-preferencias-de-color-vienen-de-la-evolucion-y-la-valencia-ecologica-claim",
  "Por la teoria de valencia ecologica, preferimos los colores asociados a experiencias positivas: cuanto mas disfrute te dan los objetos de un color, mas te gusta ese color, y cambia con nuevas experiencias (un coche azul que te atropella vuelve el azul menos atractivo; Palmer & Schloss 2010)."),
 # ── Color: 6 schemes ──
 ("aku-esquema-de-color-monocromatico-claim","color","color,schemes","aku-esquemas-de-combinacion-de-color-monocromatico-a-tetradico-method",
  "El esquema monocromatico usa un solo hue y se siente mas coherente y unido."),
 ("aku-esquema-de-color-analogo-claim","color","color,schemes","aku-esquemas-de-combinacion-de-color-monocromatico-a-tetradico-method",
  "El esquema analogo usa hues adyacentes en la rueda de color: se siente unido pero con mas variedad y flexibilidad que el monocromatico."),
 ("aku-esquema-de-color-complementario-claim","color","color,schemes","aku-esquemas-de-combinacion-de-color-monocromatico-a-tetradico-method",
  "El esquema complementario usa colores opuestos en la rueda: maximiza el contraste, lo que empuja la atencion hacia un objeto en primer plano (p.ej. un CTA) y resulta esteticamente agradable (figura calida sobre fondo frio y viceversa; Schloss & Palmer 2011)."),
 ("aku-esquema-de-color-split-complementario-claim","color","color,schemes","aku-esquemas-de-combinacion-de-color-monocromatico-a-tetradico-method",
  "El esquema split-complementario usa dos colores adyacentes al complementario del color base, lo que suaviza el contraste extremo de un esquema complementario puro."),
 ("aku-esquema-de-color-triadico-claim","color","color,schemes","aku-esquemas-de-combinacion-de-color-monocromatico-a-tetradico-method",
  "El esquema triadico usa tres colores a 120 grados en la rueda: es un compromiso entre la simplicidad del monocromatico y el contraste del complementario."),
 ("aku-esquema-de-color-tetradico-claim","color","color,schemes","aku-esquemas-de-combinacion-de-color-monocromatico-a-tetradico-method",
  "El esquema tetradico forma un rectangulo en la rueda de color y comunica variedad o complejidad."),
 # ── eCommerce: 6 review-content tips ──
 ("aku-corregir-las-erratas-en-las-resenas-claim","ecom","ecommerce,reviews","aku-insertar-contenido-persuasivo-en-las-resenas-claim",
  "Detecta y corrige erratas en las resenas: las resenas con errores ortograficos o gramaticales persuaden menos (Schindler & Bickart 2012)."),
 ("aku-censurar-los-tacos-en-las-resenas-claim","ecom","ecommerce,reviews","aku-insertar-contenido-persuasivo-en-las-resenas-claim",
  "Censura los tacos de las resenas: pareces mas profesional y, ademas, las resenas enfadadas ayudan menos (Lee & Koo 2012)."),
 ("aku-premiar-las-resenas-con-fotos-o-video-claim","ecom","ecommerce,reviews","aku-insertar-contenido-persuasivo-en-las-resenas-claim",
  "Premia a los usuarios que anaden media: los clientes prefieren las resenas con imagenes (Cheng & Ho 2015) o video (Xu et al. 2012)."),
 ("aku-mostrar-nombres-reales-en-las-resenas-claim","ecom","ecommerce,reviews","aku-insertar-contenido-persuasivo-en-las-resenas-claim",
  "Muestra nombres reales en las resenas: un nombre real (Joe S.) persuade mas que un username (jschmo; Liu & Park 2015)."),
 ("aku-mostrar-prueba-de-consumo-compra-verificada-en-las-resenas-claim","ecom","ecommerce,reviews","aku-insertar-contenido-persuasivo-en-las-resenas-claim",
  "Muestra prueba de consumo en las resenas: las de compradores «verificados» persuaden mas, o incentiva a subir selfies (Bjering, Havro & Moen 2015; Yang, Chen & Tan 2014)."),
 ("aku-pedir-valoracion-en-multiples-dimensiones-en-las-resenas-claim","ecom","ecommerce,reviews","aku-insertar-contenido-persuasivo-en-las-resenas-claim",
  "Pide valorar multiples dimensiones en las resenas (precio, calidad, estetica y otras relevantes), no solo una estrella global (Hong, Chen & Hitt 2012)."),
]
def main():
    for slug,book,dom,umb,stmt in A:
        with open(os.path.join(ROOT,"aku",slug+".md"),"w",encoding="utf-8",newline="\n") as fh:
            fh.write(TPL.format(cls="claim",slug=slug,stmt=wrap(stmt),origin=ORIGIN[book],
                                dom="kolenda, "+dom,src=SRC[book]))
    print(f"Escritos {len(A)} AKUs de re-expansion.")
    edges=[]
    for slug,book,dom,umb,stmt in A:
        edges.append((slug,"supports",CORE[book]))
        edges.append((slug,"related",umb))
    wire(edges)
if __name__=="__main__": main()
