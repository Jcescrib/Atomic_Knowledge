# -*- coding: utf-8 -*-
"""Genera los AKUs de «Pricing Psychology» (Nick Kolenda) — una táctica por AKU.
Escribe ficheros con relaciones vacías y luego cablea supports->núcleo + puentes (b)
cross-corpus con akupatch (sync 3 capas). source-tag: kolenda."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/kolenda/pricing-psychology-by-nick-kolenda/pricing-psychology-by-nick-kolenda.md"
CORE = "aku-pricing-psychology-el-precio-es-percepcion-concept"

TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "Nick Kolenda — Pricing Psychology"
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

def wrap(s):
    return "\n".join("  " + l for l in s.strip().split("\n"))

# (slug, class, dom-extra, statement)
A = [
 # ── VISUALS ──
 ("aku-mostrar-precios-en-fuente-pequena-claim","claim","visual,fonts",
  "Mostrar el precio en una fuente pequeña lo hace parecer numéricamente menor, porque el cerebro confunde el tamaño visual con el tamaño numérico (Coulter & Coulter 2005). Cautela: con varios productos a comparar, una fuente grande puede funcionar mejor porque agranda la diferencia de precio percibida."),
 ("aku-posicionar-precios-arriba-o-a-la-izquierda-claim","claim","visual,position",
  "Colocar el precio arriba o a la izquierda lo hace parecer más ligero y pequeño: la izquierda es el «fulcro visual» y se asocia a números pequeños (leemos de izquierda a derecha), y lo de arriba se percibe más liviano. Los precios parecen caros abajo-derecha."),
 ("aku-quitar-la-coma-de-los-precios-claim","claim","visual,numerals",
  "Quitar la coma de los precios los hace parecer más baratos (\\$1499 vs \\$1,499): además de la longitud escrita, reduce el tamaño fonético (5 sílabas vs 10), y el cerebro codifica la versión fonética aunque no la digas (Coulter, Choi & Monroe 2012)."),
 ("aku-agrupar-palabras-de-tamano-pequeno-junto-al-precio-claim","claim","visual,framing",
  "Las palabras cercanas al precio contagian su tamaño percibido: usa términos que evoquen pequeñez («low», «small», «tiny»). Unos patines parecieron más baratos con «Low Friction» junto al precio y más caros con «High Performance» (Coulter & Coulter 2005)."),
 ("aku-insertar-aliteracion-en-los-precios-claim","claim","visual,phonetics",
  "Insertar aliteración en el precio aumenta la compra: la coincidencia fonética «se siente bien» y el cliente atribuye esa sensación agradable al producto (dos camisetas por \\$25 —«twenty-five»— por las «t» coincidentes; Davis, Bagchi & Block 2016)."),
 ("aku-mostrar-dos-multiplos-del-precio-cerca-claim","claim","numerals,fluency",
  "Mostrar cerca dos multiplos del precio lo hace sentir «correcto»: exponer dos números (p.ej. 6 y 4) activa su producto (24) por las «number facts» memorizadas, y el cliente malatribuye esa fluidez al deseo de comprar (King & Janiszewski 2011). Ej.: «\\$120: 4 sesiones de 30 min»."),
 ("aku-mostrar-precios-en-rojo-a-los-hombres-claim","claim","visual,color,gender",
  "Mostrar precios en rojo persuade a los hombres, que deciden rápido y asumen que el rojo implica ahorro (Puccinelli et al. 2013). Cautela: todos los precios deben ser rojos; cambiar el color de uno solo puede salir mal."),
 ("aku-en-productos-emocionales-orienta-hacia-beneficios-no-al-precio-claim","claim","framing,emotional",
  "Los productos emocionales tienen beneficios fuertes pero valor económico débil, así que conviene orientar al cliente hacia los beneficios y no hacia el precio (reduciendo la saliencia del precio, mostrando el producto antes que el precio y enfatizando tiempo/uso sobre dinero)."),
 ("aku-muestra-el-producto-antes-del-precio-en-productos-emocionales-claim","claim","framing,price-primacy",
  "La primera exposición —precio vs producto— fija el criterio de decisión (fMRI): si ves el producto primero te centras en beneficios; si ves el precio primero, en el valor económico. Muestra productos emocionales antes del precio, y al revés para productos racionales (Karmarkar, Shiv & Knutson 2015)."),
 ("aku-enfatiza-tiempo-y-uso-en-vez-de-dinero-claim","claim","framing,time-money",
  "Enfatizar el tiempo que el cliente pasará con el producto, en vez del dinero, mejora la actitud: un cartel de limonada con «spend a little time» atrajo al doble de gente (que pagó el doble) que el de «spend a little money» (Mogilner & Aaker 2009)."),
 ("aku-quitar-el-simbolo-de-moneda-reduce-el-dolor-de-pagar-claim","claim","framing,pain-of-paying",
  "Si el número es claramente un precio, quitar el símbolo de moneda reduce el dolor de pagar al distraer del coste (Yang, Kimes & Sessarego 2009). Funciona mejor en contextos de lujo (p.ej. restaurantes de alta gama)."),
 # ── FRAMING ──
 ("aku-exponer-a-cualquier-numero-alto-eleva-el-precio-de-referencia-claim","claim","framing,anchoring",
  "Exponer al cliente a cualquier número alto sube su precio de referencia y hace que tu precio real parezca más barato (anclaje). Funciona incluso con números irrelevantes (los últimos dígitos del número de la seguridad social predijeron la disposición a pagar; Ariely et al. 2003). Ej.: «Únete a 5.487 clientes»."),
 ("aku-colocar-el-numero-mayor-a-la-izquierda-principio-de-sustraccion-claim","claim","framing,subtraction",
  "Coloca el número mayor a la izquierda (precio original o cantidad) para que la resta sea más fácil y la diferencia parezca mayor —principio de sustracción— (Biswas et al. 2013). Igual con cantidades: «70 items por \\$29» supera a «\\$29 por 70 items»."),
 ("aku-mostrar-precios-altos-antes-que-bajos-claim","claim","framing,ordering",
  "Ordenar los precios de mayor a menor empuja a elegir opciones más caras: los precios iniciales altos hacen que los siguientes parezcan baratos, y la aversión a la pérdida presiona a comprar antes de perder calidad al bajar (Suk, Lee & Lichtenstein 2012)."),
 ("aku-distinguir-visualmente-la-opcion-mas-cara-claim","claim","framing,reference",
  "El efecto de ordenar precios viene del orden en que se evalúan, así que basta con dar una distinción visual a la opción más cara: si el cliente la evalúa primero, fija un precio de referencia alto que abarata las demás."),
 ("aku-ofrecer-una-version-similar-pero-mas-cara-como-senuelo-decoy-claim","claim","framing,decoy",
  "Añadir una versión similar pero más cara («decoy») desplaza la demanda hacia una opción cara: en el clásico de The Economist, la suscripción «print» a \\$125 (que nadie elige) empuja hacia «print+digital» al mismo precio. Considera un señuelo similar y más caro."),
 ("aku-mencionar-la-equivalencia-diaria-del-precio-claim","claim","framing,reframing",
  "Enmarca el precio en términos diarios (p.ej. \\$1,60/día; Gourville 1998): el cliente compara ese valor pequeño con su precio de referencia, o lo equipara a un gasto trivial (un café), reduciendo la resistencia."),
 ("aku-no-agrupar-items-baratos-con-caros-promediacion-claim","claim","framing,bundling",
  "No agrupes un item barato con uno caro (un home gym de \\$500 con un DVD de \\$5): el cliente no suma los valores, los promedia, así que los items baratos restan valor percibido a los caros (Brough & Chernev 2012)."),
 ("aku-crear-un-medio-de-pago-separado-reduce-el-dolor-de-pagar-claim","claim","framing,pain-of-paying",
  "Transformar el pago en un medio separado (créditos mensuales, gift cards, saldo) hace que gastar duela menos y el cliente gaste más (Nunes & Park 2003). Ej.: pedir un depósito reembolsable de \\$10 que reside en una cuenta aparte."),
 ("aku-atribuir-el-descuento-al-producto-emocional-del-bundle-claim","claim","framing,guilt",
  "Queremos comprar productos emocionales pero sentimos culpa, así que en un bundle conviene atribuir el descuento al item hedónico: ese framing da la justificación que reduce la culpa de la compra (Khan & Dhar 2010)."),
 ("aku-cobrar-antes-de-que-el-cliente-consuma-claim","claim","framing,prepayment",
  "Cobra antes de que el cliente consuma: es más probable cobrar, y el cliente es más feliz porque al prepagar anticipa los beneficios, mientras que tras consumir nada amortigua el dolor de pagar (Prelec & Loewenstein 1998). Si cobras mensual, cobra a principio de mes."),
 ("aku-describir-los-costes-del-producto-aumenta-la-percepcion-de-justicia-claim","claim","framing,cost-transparency",
  "Los clientes prefieren precios determinados por costes de material antes que por oferta y demanda, así que describir tus costes aumenta la percepción de justicia y las ventas (Xia, Monroe & Cox 2004; confirmado por Mohan, Buell & John 2020: una cartera vendió más detallando cuero \\$14,68, construcción \\$38,56...)."),
 ("aku-fomentar-el-presupuesto-temprano-aumenta-el-gasto-claim","claim","framing,budgeting",
  "Fomentar que el cliente presupueste temprano aumenta el gasto: presupuestar pronto te separa de ese dinero y, al alejarte de los fondos, pagar duele menos (Chloe & Kan 2021). Ej.: ofrecer upgrades a quien reserva con antelación."),
 # ── NUMERALS ──
 ("aku-reducir-el-digito-izquierdo-en-uno-charm-pricing-claim","claim","numerals,left-digit",
  "Reducir el dígito izquierdo en uno («charm pricing»: \\$2,99 vs \\$3,00) abarata la percepción: el cerebro codifica la magnitud en cuanto ve el primer dígito, así que una diferencia de un céntimo se siente como de un dólar (efecto left-digit; Thomas & Morwitz 2005)."),
 ("aku-elegir-precios-con-menos-silabas-claim","claim","numerals,phonetics",
  "Elige precios con menos sílabas: \\$28,16 («twenty-eight sixteen», 5 sílabas) se siente menor que \\$27,82 (7 sílabas) pese a ser mayor, porque el cerebro codifica la versión fonética del número aunque no lo digas (Coulter, Choi & Monroe 2012)."),
 ("aku-dividir-el-precio-en-unidades-mas-pequenas-partitioned-prices-claim","claim","numerals,partitioned",
  "Divide el precio «primario» en unidades más pequeñas («partitioned prices»): separar el envío o vender en cuotas (12 pagos de \\$115 en vez de \\$1.250) hace que el cliente compare la cifra menor con su precio de referencia (Morwitz, Greenleaf & Johnson 1998). Cautela: hoy muchos esperan envío gratis."),
 ("aku-ser-preciso-con-precios-grandes-claim","claim","numerals,precision",
  "Sé preciso con precios grandes: en 27.000 transacciones inmobiliarias, precios específicos (\\$362.978) fueron más efectivos que redondos (\\$350.000), porque asociamos los números específicos con valores pequeños (Thomas, Simon & Kadiyali 2007)."),
 ("aku-colocar-numerales-bajos-tras-digitos-orientados-a-la-derecha-claim","claim","numerals,attention",
  "Los dígitos «miran» en direcciones (5 y 6 a la derecha; 2,3,4,7,9 a la izquierda) y guían la atención: pon numerales bajos tras dígitos orientados a la derecha para que el cliente fije la vista al final y redondee a la baja; tras dígitos izquierdos puedes poner numerales altos porque los ignorará (Coulter 2007)."),
 ("aku-ajustar-los-numerales-al-nombre-o-cumpleanos-egotismo-implicito-claim","claim","numerals,implicit-egotism",
  "Ajustar los numerales del precio para que coincidan con el nombre o cumpleaños del cliente aumenta su agrado y la intención de compra (egotismo implícito: preferimos lo que se nos parece; Coulter & Grewal 2014). Ej.: en un presupuesto, adapta las cifras tras mirar su perfil."),
 ("aku-usar-precios-redondos-en-el-contexto-adecuado-claim","claim","numerals,round",
  "Usa precios redondos (\\$50) cuando «sentirse bien/fácil» ayuda: compras emocionales (sensación de corrección), compras de conveniencia (sensación de rapidez) y productos sociales (la conectividad numérica se confunde con la social). Usa precios específicos para compras racionales (Wadhwa & Zhang 2015)."),
 ("aku-anadir-ligeras-diferencias-de-precio-en-el-surtido-claim","claim","numerals,assortment",
  "Añade ligeras diferencias de precio en un surtido similar: precios idénticos hacen que los packs parezcan menos similares y el cliente busque diferencias; precios algo distintos (62¢ vs 64¢) mantienen el foco en las similitudes y aumentan la compra (Kim, Novemsky & Dhar 2013)."),
 ("aku-subir-el-precio-en-incrementos-pequenos-y-frecuentes-method","method","numerals,jnd",
  "Sube el precio en incrementos pequeños y frecuentes, por debajo de la «just noticeable difference»: de \\$11 a \\$12 se nota menos que a \\$20. El error común es esperar por miedo hasta que es necesario un salto grande y perceptible; ajusta antes, en pasos pequeños."),
 ("aku-reducir-una-caracteristica-distinta-del-precio-claim","claim","numerals,shrinkflation",
  "Puedes cambiar el precio efectivo sin cambiar los numerales: si el cliente es muy sensible al precio, reduce una característica menos perceptible (p.ej. el tamaño físico en sus tres dimensiones a la vez, que se nota menos; Chandon & Ordabayeva 2009). Sé transparente y no abuses."),
 # ── DISCOUNTS ──
 ("aku-hacer-que-el-precio-de-oferta-se-vea-distinto-contrast-fluency-claim","claim","discounts,contrast",
  "Haz que el precio de oferta se vea visualmente distinto del original (color, tamaño, fuente): el cerebro malatribuye la distinción visual a una distinción abstracta —«algo se ve diferente, debe ser muy diferente»— («contrast fluency»; Coulter & Coulter 2005)."),
 ("aku-anadir-espacio-entre-precio-original-y-de-oferta-claim","claim","discounts,distance",
  "Añade espacio entre el precio original y el de oferta: concebimos los números en una regla horizontal, así que confundimos la distancia visual con la numérica y la diferencia parece mayor (Coulter & Norberg 2009)."),
 ("aku-colocar-el-precio-de-oferta-debajo-del-original-claim","claim","discounts,vertical",
  "Cuando puedas, dispón el descuento en vertical (oferta debajo del original): los números verticales son más fáciles de restar dígito a dígito y el cálculo fácil agranda la brecha percibida (Feng et al. 2017). Cautela: el horizontal va mejor para descuentos pequeños porque dificulta el cálculo."),
 ("aku-reducir-todos-los-digitos-en-el-precio-de-oferta-claim","claim","discounts,digits",
  "Reduce todos los dígitos en el precio de oferta: el cliente compara dígito a dígito, así que de \\$465 busca un numeral menor en cada posición (quizá manteniendo el dígito derecho para facilitar la resta de los izquierdos; Korvorst & Damian 2008)."),
 ("aku-ofrecer-descuentos-con-digitos-derechos-bajos-claim","claim","discounts,digits",
  "Ofrece descuentos con dígitos pequeños en las posiciones derechas: como 3 es 50% mayor que 2 pero 8 solo 14% mayor que 7, la diferencia entre dígitos bajos se percibe mayor, agrandando la brecha del descuento (Coulter & Coulter 2007)."),
 ("aku-regla-del-100-porcentaje-bajo-100-absoluto-sobre-100-method","method","discounts,rule-of-100",
  "Regla del 100 para descuentos: bajo \\$100 da el descuento en porcentaje, sobre \\$100 dalo en absoluto —en ambos casos muestras el numeral más alto—. Para un blender de \\$50, «20% off» persuade más que «\\$10 off»; para uno de \\$150, «\\$30 off» supera a «20% off» (González et al. 2016)."),
 ("aku-mencionar-el-incremento-desde-el-precio-de-oferta-claim","claim","discounts,framing",
  "En vez de enfatizar la bajada («ahora 20% menos»), enmarca el descuento como el incremento desde el precio de oferta («era 25% más caro»): es más persuasivo porque muestra un numeral más alto (Guha et al. 2018)."),
 ("aku-dar-una-razon-para-el-descuento-claim","claim","discounts,reason",
  "Da una razón para el descuento (clearance, recorte de proveedores): así parece temporal, no daña el precio de referencia futuro del cliente y le empuja a aprovecharlo ya. Sin razón, el descuento encarece la percepción de tus precios futuros (Mazumdar, Raj & Sinha 2005)."),
 ("aku-ofrecer-descuentos-en-numeros-redondos-claim","claim","discounts,round",
  "Ofrece los descuentos en números redondos (al revés que los precios, que conviene específicos): como quieres agrandar el descuento, los numerales redondos se calculan más fácil y la facilidad agranda la brecha percibida (Thomas & Morwitz 2009)."),
 ("aku-dar-dos-descuentos-en-orden-ascendente-claim","claim","discounts,double",
  "Dos ganancias se prefieren a una suma única (Kahneman & Tversky 1979), así que parte el descuento en dos (10% y luego 40%) y, si puedes, en orden ascendente: el momentum creciente hace que el descuento total parezca mayor (Gong, Huang & Goh 2019)."),
 ("aku-ofrecer-descuentos-hacia-el-final-del-mes-claim","claim","discounts,timing",
  "Los pagos duelen más desde un presupuesto pequeño, así que los descuentos son más efectivos hacia el final del mes, cuando la gente ha agotado su presupuesto y busca ahorrar; da pruebas gratis a principio de mes, cuando el presupuesto está alto (Soster, Gershoff & Bearden 2014)."),
 ("aku-arreglar-descuentos-en-tramos-escalonados-claim","claim","discounts,tiers",
  "Dispón los descuentos en tramos escalonados (\\$5 off \\$20 / \\$10 off \\$50 / \\$50 off \\$200): el cliente no imagina el umbral de \\$200, pero el de \\$20 sí, y una vez imagina gastar \\$20 le resulta más fácil imaginar el siguiente umbral, y el siguiente («simulation fluency»)."),
 ("aku-retirar-los-descuentos-gradualmente-claim","claim","discounts,decreasing",
  "Retira los descuentos gradualmente («steadily decreasing discounts»): frente a Hi-Lo o Everyday-Low-Pricing, una retirada gradual (\\$999→\\$799→\\$899→\\$999) maximizó ingresos en un test de 30 semanas (Tsiros & Hardesty 2010)."),
 ("aku-no-descontar-productos-premium-claim","claim","discounts,premium",
  "No descuentes productos premium: retirar el descuento empuja al cliente a esperar el siguiente o irse a la competencia, y como descontar premium es poco común, atrae la atención al precio —justo lo que no conviene si ya es alto— (Wathieu, Muthukrishnan & Bronnenberg 2004). Sigue enfatizando la calidad."),
]

def main():
    written = 0
    for slug, cls, domx, stmt in A:
        dom = "kolenda, " + domx
        path = os.path.join(ROOT, "aku", slug + ".md")
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(TPL.format(cls=cls, slug=slug, stmt=wrap(stmt), dom=dom, src=SRC))
        written += 1
    print(f"Escritos {written} AKUs de tácticas + núcleo ya existe.")
    # cablear: cada táctica supports -> núcleo
    edges = [(slug, "supports", CORE) for slug, *_ in A]
    # puentes (b) cross-corpus / intra (related)
    B = [
     ("aku-exponer-a-cualquier-numero-alto-eleva-el-precio-de-referencia-claim","aku-cuando-te-meten-un-numero-en-la-cabeza-moverte-de-el-se-siente-como-perdida-claim"),  # anclaje (50-cent)
     ("aku-ofrecer-una-version-similar-pero-mas-cara-como-senuelo-decoy-claim","aku-cialdini-escasez-concept"),  # decoy/contraste -> persuasion (proxy)
     ("aku-quitar-el-simbolo-de-moneda-reduce-el-dolor-de-pagar-claim","aku-crear-un-medio-de-pago-separado-reduce-el-dolor-de-pagar-claim"),  # pain of paying (intra)
     ("aku-cobrar-antes-de-que-el-cliente-consuma-claim","aku-crear-un-medio-de-pago-separado-reduce-el-dolor-de-pagar-claim"),  # pain of paying (intra)
     ("aku-dividir-el-precio-en-unidades-mas-pequenas-partitioned-prices-claim","aku-mencionar-la-equivalencia-diaria-del-precio-claim"),  # reframing pequeno (intra)
    ]
    edges += [(a, "related", b) for a, b in B]
    wire(edges)

if __name__ == "__main__":
    main()
