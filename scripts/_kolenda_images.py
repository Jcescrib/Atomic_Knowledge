# -*- coding: utf-8 -*-
"""Embebe en cada AKU de Kolenda la(s) figura(s) que ilustran su tactica.
Segmentacion robusta por keywords de tactica (fronteras). ![[hash.jpg]] bajo '## Figura'."""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = "raw/libros/kolenda/"

def imgs_in(lines):
    out = []
    for l in lines:
        out += re.findall(r"!\[(?:image)?\]\(images/([^)]+)\)", l)
    return out

def map_by_keywords(md_path, ordered):
    lines = open(md_path, encoding="utf-8").read().split("\n")
    pos = []
    for slug, kw in ordered:
        idx = next((i for i, l in enumerate(lines)
                    if re.match(r"^#{1,4}\s", l) and kw.lower() in l.lower()), None)
        pos.append((idx, slug))
    located = sorted([(i, s) for i, s in pos if i is not None])
    res = {}
    for k, (i, slug) in enumerate(located):
        end = located[k+1][0] if k+1 < len(located) else len(lines)
        res[slug] = imgs_in(lines[i:end])
    return res

def reset(slug):
    p = os.path.join(ROOT, "aku", slug + ".md")
    if not os.path.exists(p): return
    txt = open(p, encoding="utf-8").read()
    txt = re.sub(r"## Figura\n.*?\n\n(?=## Relaciones)", "", txt, flags=re.S)
    open(p, "w", encoding="utf-8", newline="\n").write(txt)

def embed(slug, images):
    p = os.path.join(ROOT, "aku", slug + ".md")
    if not images or not os.path.exists(p): return False
    txt = open(p, encoding="utf-8").read()
    if "## Figura" in txt: return False
    block = "## Figura\n\n" + "\n".join(f"![[{img}]]" for img in images) + "\n\n"
    txt = txt.replace("## Relaciones", block + "## Relaciones", 1)
    open(p, "w", encoding="utf-8", newline="\n").write(txt)
    return True

def run(md_rel, ordered):
    for slug, _ in ordered: reset(slug)
    m = map_by_keywords(os.path.join(ROOT, md_rel), ordered)
    done = sum(1 for slug, _ in ordered if embed(slug, m.get(slug, [])))
    print(f"  {md_rel.split('/')[-2]:38s}: figuras en {done}/{len(ordered)} AKUs")

PRICING = ("pricing-psychology-by-nick-kolenda/pricing-psychology-by-nick-kolenda.md", [
 ("aku-mostrar-precios-en-fuente-pequena-claim","Show Prices in Small Fonts"),
 ("aku-posicionar-precios-arriba-o-a-la-izquierda-claim","Position Prices Near the Top"),
 ("aku-quitar-la-coma-de-los-precios-claim","Remove the Comma"),
 ("aku-agrupar-palabras-de-tamano-pequeno-junto-al-precio-claim","Group Small Elements"),
 ("aku-insertar-aliteracion-en-los-precios-claim","Insert Alliteration"),
 ("aku-mostrar-dos-multiplos-del-precio-cerca-claim","Show Two Multiples"),
 ("aku-mostrar-precios-en-rojo-a-los-hombres-claim","Display Red Prices"),
 ("aku-en-productos-emocionales-orienta-hacia-beneficios-no-al-precio-claim","Deemphasize the Price of Emotional"),
 ("aku-exponer-a-cualquier-numero-alto-eleva-el-precio-de-referencia-claim","Expose People to Any High Number"),
 ("aku-colocar-el-numero-mayor-a-la-izquierda-principio-de-sustraccion-claim","Place a Large Number on the Left"),
 ("aku-mostrar-precios-altos-antes-que-bajos-claim","Show Higher Prices Before Lower"),
 ("aku-distinguir-visualmente-la-opcion-mas-cara-claim","Distinguish the Most Expensive"),
 ("aku-no-agrupar-items-baratos-con-caros-promediacion-claim","Bundle Cheap and Expensive"),
 ("aku-crear-un-medio-de-pago-separado-reduce-el-dolor-de-pagar-claim","Create a Payment Medium"),
 ("aku-atribuir-el-descuento-al-producto-emocional-del-bundle-claim","Attribute Discounts to Emotional"),
 ("aku-cobrar-antes-de-que-el-cliente-consuma-claim","Charge Customers Before They Consume"),
 ("aku-usar-precios-redondos-en-el-contexto-adecuado-claim","Use Round Prices in the Right Context"),
 ("aku-subir-el-precio-en-incrementos-pequenos-y-frecuentes-method","Raise Your Price in Small Increments"),
 ("aku-hacer-que-el-precio-de-oferta-se-vea-distinto-contrast-fluency-claim","Make Sale Prices Look Different"),
 ("aku-colocar-el-precio-de-oferta-debajo-del-original-claim","Place Sale Prices Below"),
 ("aku-reducir-todos-los-digitos-en-el-precio-de-oferta-claim","Reduce Every Digit"),
 ("aku-ofrecer-descuentos-con-digitos-derechos-bajos-claim","Discounts With Low Right Digits"),
 ("aku-retirar-los-descuentos-gradualmente-claim","End Discounts Gradually"),
])
COPY = ("copywriting-psychology-by-nick-kolenda/copywriting-psychology-by-nick-kolenda.md", [
 ("aku-reemplazar-beneficios-vagos-por-ejemplos-concretos-claim","Replace Vague Benefits"),
 ("aku-adaptar-las-palabras-al-escenario-claim","Tailor Your Words"),
 ("aku-usar-voz-activa-claim","Construct Sentences With Active Voice"),
 ("aku-terminar-las-frases-con-una-imagen-concreta-claim","End Sentences With a Concrete Image"),
 ("aku-que-los-rasgos-linguisticos-reflejen-el-mensaje-claim","Symbolize the Message"),
 ("aku-ajustar-la-distancia-entre-palabras-claim","Adjust the Distance Between Words"),
 ("aku-retratar-acciones-con-verbos-imperfectos-claim","Portray Actions With Imperfect"),
 ("aku-restringir-a-una-sola-interpretacion-claim","Constrain Your Writing"),
 ("aku-mencionar-inconvenientes-argumento-bilateral-claim","Mention Drawbacks"),
])
PACK = ("packaging-psychology-by-nick-kolenda/packaging-psychology-by-nick-kolenda.md", [
 ("aku-envases-altos-parecen-sanos-y-lujosos-claim","Tall Packages Seem Healthy"),
 ("aku-envases-anchos-parecen-mas-pesados-claim","Wide Packages Seem Heavier"),
 ("aku-envases-pequenos-parecen-densos-y-potentes-claim","Small Packages Seem Dense"),
 ("aku-mantener-la-forma-completa-del-envase-claim","Maintain the Full Shape"),
 ("aku-quitar-el-envase-de-productos-frescos-claim","Remove Packaging From Fresh"),
 ("aku-texturas-rugosas-parecen-masculinas-claim","Rough Textures Seem Masculine"),
 ("aku-las-marcas-desconocidas-deben-invertir-en-packaging-claim","Unknown Brands Should Invest"),
 ("aku-mostrar-mas-unidades-de-producto-en-el-envase-claim","Show More Product Units"),
 ("aku-mostrar-imagenes-realistas-en-productos-emocionales-claim","Display Realistic Images"),
 ("aku-elegir-colores-claros-y-naturales-para-productos-sanos-claim","Light and Natural Colors"),
])
COLOR = ("color-psychology2/color-psychology2.md", [
 ("aku-los-colores-oscuros-parecen-pesados-claim","Weight"),
 ("aku-los-colores-saturados-parecen-mas-grandes-claim","Size"),
 ("aku-los-colores-saturados-parecen-mas-cercanos-claim","Proximity"),
 ("aku-los-colores-desaturados-grayscale-transmiten-lujo-claim","Luxury"),
 ("aku-los-colores-saturados-orientan-al-detalle-claim","Details"),
 ("aku-el-blanco-facilita-la-accion-y-el-oscuro-retiene-claim","Actionability"),
 ("aku-el-blanco-promueve-visibilidad-y-el-oscuro-la-oculta-claim","Visibility"),
 ("aku-el-rojo-refuerza-la-atraccion-social-claim","Sociality"),
 ("aku-los-colores-calidos-y-saturados-estimulan-el-azul-relaja-claim","Stimulating"),
 ("aku-el-rojo-aumenta-la-agresividad-y-el-dominio-claim","Aggressive"),
 ("aku-esquema-de-color-complementario-claim","Complementary Colors"),
 ("aku-esquema-de-color-triadico-claim","Triadic Colors"),
 ("aku-esquema-de-color-tetradico-claim","Tetradic Colors"),
])
CHOICE = ("choice/choice.md", [
 ("aku-simulation-fluency-simulamos-resultado-menos-proceso-concept","Simulation Fluency"),
 ("aku-la-escala-de-decision-equilibra-cuatro-conductas-concept","The Decision Scale"),
 ("aku-evaluamos-por-comparaciones-relativas-context-effects-concept","Relative Comparisons"),
 ("aku-gamificar-la-eleccion-experiencial-vs-instrumental-claim","Gamify the Choice"),
 ("aku-activar-una-mentalidad-de-cual-elegir-which-to-choose-claim","Activate a Which-to-Choose"),
 ("aku-reducir-la-culpa-de-las-elecciones-emocionales-claim","Reduce the Guilt"),
 ("aku-usar-lenguaje-asertivo-en-productos-emocionales-claim","Use Assertive Language"),
 ("aku-subir-los-atributos-indeseables-por-encima-de-cero-zero-comparison-claim","Raise Undesirable Attributes"),
 ("aku-anadir-senales-sensoriales-para-captar-atencion-claim","Add Sensory Cues"),
 ("aku-alinear-las-caracteristicas-con-las-de-la-competencia-claim","Align Features With Competitors"),
])
ECOM = ("ecommerce-psychology-by-nick-kolenda/ecommerce-psychology-by-nick-kolenda.md", [
 ("aku-oscurecer-el-borde-superior-de-la-interfaz-claim","Darken the Top Border"),
 ("aku-disponer-los-productos-horizontalmente-para-explorar-claim","Arrange Products Horizontally"),
 ("aku-mostrar-el-unboxing-del-producto-claim","Show the Unboxing"),
 ("aku-ayudar-al-usuario-a-imaginar-tocar-el-producto-claim","Help Users Imagine Touching"),
 ("aku-mostrar-resenas-imperfectas-claim","Show Imperfect Reviews"),
 ("aku-traer-los-botones-al-primer-plano-claim","Bring Buttons to the Foreground"),
 ("aku-facilitar-el-movimiento-simbolico-del-progreso-en-el-checkout-claim","Ease the Symbolic Motion"),
])
VIRAL = ("pages-viral-marketing/pages-viral-marketing.md", [
 ("aku-apuntar-solo-a-influencers-no-basta-tres-problemas-claim","PROBLEMS"),
 ("aku-target-un-microsegmento-y-escala-hacia-fuera-claim","CASE STUDY: FACEBOOK"),
 ("aku-usa-maven-groups-para-promover-contenido-claim","MAVEN GROUPS"),
])

if __name__ == "__main__":
    print("Embebiendo figuras Kolenda:")
    for md, mp in [PRICING, COPY, PACK, COLOR, CHOICE, ECOM, VIRAL]:
        run(B + md, mp)
