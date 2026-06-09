# -*- coding: utf-8 -*-
"""AKUs de «Packaging Psychology» (Nick Kolenda). source-tag: kolenda."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/kolenda/packaging-psychology-by-nick-kolenda/packaging-psychology-by-nick-kolenda.md"
CORE = "aku-packaging-psychology-el-envase-comunica-por-heuristicas-visuales-concept"
CORE_STMT = ("El envase comunica significado mediante antropomorfismo (el cliente compara los rasgos del envase con "
 "humanos) y heuristicas visuales de tamano, forma, material y color que moldean la percepcion del producto. "
 "Incluye elegir size/shape/material/diseno congruentes con el posicionamiento; excluye tratar el envase como "
 "mero contenedor; implica que la forma fisica del envase altera frescura, peso, salud, genero y lujo percibidos.")
TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "Nick Kolenda — Packaging Psychology"
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
        fh.write(TPL.format(cls=cls,slug=slug,stmt=wrap(stmt),dom="kolenda, packaging, "+dom,src=SRC))
A = [
 ("aku-envases-altos-parecen-mas-grandes-claim","claim","size",
  "Los envases altos parecen mas grandes porque el cliente usa la altura para estimar el tamano (las botellas parecen mayores que las latas; Raghubir & Krishna 1999). Desventaja: al parecer mayores, se compra menos (latas a +64% de cantidad que botellas). Altos para compras puntuales; anchos para compras a granel."),
 ("aku-envases-altos-parecen-sanos-y-lujosos-claim","claim","size",
  "Por antropomorfismo, los envases altos parecen sanos y lujosos: el cliente los compara con una persona alta y esbelta (asociada a salud y a clase socioeconomica alta), asi que se perciben mas efectivos en mercados premium (van Ooijen et al. 2017; Chen et al. 2020)."),
 ("aku-envases-anchos-parecen-mas-pesados-claim","claim","size",
  "Los envases anchos parecen mas pesados por la heuristica de estabilidad: los objetos estables se perciben mas pesados, y el cliente paga mas (Yang, Yan & Raghubir 2021). Un yogur «cremoso» rinde mejor en envase ancho; uno «light», estrechando la base para que se vea inestable y ligero."),
 ("aku-envases-pequenos-parecen-densos-y-potentes-claim","claim","size",
  "Los productos parecen mas densos y potentes en envases pequenos: el cafe sabe mas intenso en taza estrecha (Van Doorn et al. 2017) por tres razones —se conceptualiza como version condensada del promedio, el precio por unidad mas alto infla la calidad percibida, y la racion individual se siente como porcion completa (no parcial; Tide Pods)."),
 ("aku-envases-redondeados-parecen-dulces-y-femeninos-claim","claim","shape",
  "Los envases redondeados parecen femeninos (la angularidad parece masculina por raices evolutivas: el cuerpo femenino es mas curvo) y heredan rasgos femeninos como la dulzura (Velasco et al. 2014). Elige envase redondo para chocolate dulce y angular para comida picante."),
 ("aku-mantener-la-forma-completa-del-envase-claim","claim","shape",
  "Manten la forma completa del envase: cualquier seccion ausente (un hueco como asa) hace que parezca mas pequeno y menos deseable (heuristica de completitud; Sevilla & Kahn 2014). Mejor anadir un accesorio separado que recortar el envase."),
 ("aku-ventanas-transparentes-transmiten-frescura-claim","claim","shape",
  "Las ventanas transparentes transmiten frescura: ver la comida directamente la hace mas saliente que un grafico impreso y eleva el hambre y los antojos (Simmonds, Woods & Spence 2018). Cautela con productos fragiles (chips): solo si confias en que no se rompen."),
 ("aku-quitar-el-envase-de-productos-frescos-claim","claim","material",
  "Quita el envase de los productos frescos: el envase actua como barrera simbolica que separa el producto de la naturaleza y reduce la naturalidad percibida (Szocs, Williamson & Mills 2022). Si necesitas envase, enfatiza una conexion con la naturaleza (materiales sostenibles, «recogido en el vinedo»)."),
 ("aku-envases-mate-parecen-mas-sanos-claim","claim","material",
  "Los envases mate parecen mas sanos y naturales, y los brillantes mas grasos: por exposicion real (lo glossy suele contener snacks poco sanos), el cliente cree que la comida en envase mate es mas natural, mientras lo brillante recuerda a lo grasiento (Ye, Morrin & Kampfer 2020)."),
 ("aku-texturas-rugosas-parecen-masculinas-claim","claim","material",
  "Las texturas rugosas parecen masculinas y las suaves femeninas (se prefirieron aromas masculinos en papel rugoso; Krishna, Elder & Caldara 2010). Si tu producto es masculino, anade textura rugosa en todos los touchpoints (identidad de marca, packaging, material)."),
 ("aku-el-vidrio-parece-mejor-que-el-plastico-claim","claim","material",
  "El cliente prefiere los productos en envase de vidrio frente al plastico (Balzarotti et al. 2015); conviene medir el aumento de preferencia y si compensa el sobrecoste del vidrio."),
 ("aku-las-marcas-desconocidas-deben-invertir-en-packaging-claim","claim","design",
  "Las marcas desconocidas deben invertir en packaging: el cliente elige una marca nueva y mas cara si el envase es bello y captador de atencion (Reimann et al. 2010), incluso frente a marcas conocidas y baratas."),
 ("aku-mostrar-mas-unidades-de-producto-en-el-envase-claim","claim","design",
  "Muestra mas unidades de producto en el envase: el cliente equipara la imageneria exterior con el contenido (mas unidades fuera = mas dentro; Madzharov & Block 2010). Cautela con lo organico: se prefiere packaging minimalista porque parece mas natural y libre de quimicos."),
 ("aku-mostrar-imagenes-realistas-en-productos-emocionales-claim","claim","design",
  "Muestra imagenes realistas en productos emocionales (postres): las fotos realistas persuaden mas porque retratan la experiencia mas vividamente (Ketron et al. 2021). Haz lo contrario en experiencias negativas (verduras, ejercicio): usa imagenes simbolicas o digitales para difuminar esa imageneria."),
 ("aku-colocar-productos-pesados-abajo-o-a-la-derecha-claim","claim","design,location",
  "Coloca las imagenes de producto pesado abajo o a la derecha del envase (los objetos pesados se hunden; lo de la derecha «tira» hacia abajo en el lienzo visual; Deng & Kahn 2009) y las de producto ligero/sano a la izquierda, lo que influye incluso en el sabor y la cantidad ingerida."),
 ("aku-elegir-colores-claros-y-naturales-para-productos-sanos-claim","claim","design,color",
  "Elige colores claros y naturales para productos sanos: los oscuros parecen pesados y los claros «ligeros» (faciles de levantar; Arnheim 1997), y los tonos au-naturel (beige) parecen autenticos. El beige supero al naranja para arroz y zanahorias; la comida parece menos sana en envases muy saturados (Mead & Richerson 2018)."),
]
def main():
    write(CORE,"concept","packaging, anthropomorphism, marketing-psychology",CORE_STMT)
    for slug,cls,dom,stmt in A: write(slug,cls,dom,stmt)
    print(f"Escritos {len(A)+1} AKUs.")
    edges = [(slug,"supports",CORE) for slug,*_ in A]
    edges += [
     ("aku-colocar-productos-pesados-abajo-o-a-la-derecha-claim","related","aku-posicionar-precios-arriba-o-a-la-izquierda-claim"),  # Deng&Kahn (cross-libro Pricing)
     ("aku-envases-redondeados-parecen-dulces-y-femeninos-claim","related","aku-fuentes-redondeadas-transmiten-comodidad-y-suavidad-claim"),  # round=feminine (cross-libro Font)
     ("aku-texturas-rugosas-parecen-masculinas-claim","related","aku-fuentes-bold-transmiten-poder-y-masculinidad-claim"),  # masculino (cross-libro Font)
     ("aku-las-marcas-desconocidas-deben-invertir-en-packaging-claim","related","aku-identidad-de-marca-concept"),  # branding
     (CORE,"related","aku-font-psychology-las-fuentes-significan-por-congruencia-de-rasgos-concept"),  # rasgos visuales->significado
    ]
    wire(edges)
if __name__=="__main__": main()
