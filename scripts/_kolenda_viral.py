# -*- coding: utf-8 -*-
"""AKUs de «The Science of Viral Marketing» (Nick Kolenda). source-tag: kolenda."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/kolenda/pages-viral-marketing/pages-viral-marketing.md"
CORE = "aku-viral-marketing-las-redes-pequenas-causan-grandes-impactos-concept"
CORE_STMT = ("La clave de la viralidad es que las redes pequenas y densas («micronetworks») causan grandes impactos: "
 "en vez de sembrar en grandes audiencias o influencers sueltos, se infecta un cluster pequeno y muy "
 "interconectado, desde el que la difusion crece dentro de la red y luego escala hacia redes adyacentes "
 "solapadas. Incluye microsegmentar, usar maven groups y elegir temas de alta interconectividad; excluye el "
 "enfoque estandar de apuntar a segmentos grandes y dispersos.")
TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "Nick Kolenda — The Science of Viral Marketing"
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
        fh.write(TPL.format(cls=cls,slug=slug,stmt=wrap(stmt),dom="kolenda, viral-marketing, "+dom,src=SRC))
A = [
 ("aku-micronetwork-red-densa-con-interconexiones-fuertes-concept","concept","network",
  "Una «micronetwork» es una red densa con interconexiones fuertes: interconectada (la gente se conoce entre si), densa (pequena, casi todos conocen a todos) y fuerte (interaccion frecuente e importante). Es la unidad desde la que se originan los mensajes virales."),
 ("aku-apuntar-solo-a-influencers-no-basta-tres-problemas-claim","claim","strategy",
  "Apuntar solo a influencers con muchas conexiones no basta y limita la viralidad por tres problemas: baja interconectividad (sus seguidores no se conocen entre si), susceptibilidad secundaria (al difundir hacia fuera de la red llega a gente menos susceptible) y conexiones debiles (es facil ignorar el email de un influencer)."),
 ("aku-la-interconectividad-construye-la-infeccion-dentro-de-la-red-claim","claim","network",
  "La interconectividad es lo que hace que la infeccion se construya DENTRO de la red: si los nodos se conocen, un nodo expuesto dos veces dispara un efecto bola de nieve (mas exposiciones -> mas contagio -> mas exposiciones). Sin interconectividad, los mensajes se transmiten fuera de la red, a receptores menos susceptibles (Lerman & Ghosh 2010)."),
 ("aku-las-epidemias-virales-se-originan-en-micronetworks-claim","claim","network",
  "Las epidemias virales se originan en micronetworks: por epidemiologia, los brotes amplios nacen de redes pequenas como las familias (al infectarse uno, la familia que convive se vuelve susceptible), y luego escalan a redes adyacentes hasta cubrir toda la region (Ball 1997)."),
 ("aku-target-un-microsegmento-y-escala-hacia-fuera-claim","claim","strategy",
  "Apunta a un microsegmento (un cluster pequeno y muy conectado dentro de tu segmento) y escala hacia fuera, en vez de a segmentos grandes y dispersos. Facebook empezo en una micronetwork —los estudiantes de Harvard (en 24h se apunto media universidad)— y escalo dominando una serie de micronetworks solapadas (otras universidades)."),
 ("aku-usa-maven-groups-para-promover-contenido-claim","claim","strategy",
  "Usa «maven groups» —grupos pequenos que ansian conocimiento en un dominio (pequenas empresas o equipos centrados en un tema)— para promover contenido: son micronetworks muy susceptibles. El articulo de pricing de Kolenda llego a 325.000 visitas tras enviarlo, sin venta, a muchas pequenas empresas de software de pricing (que lo discutian en equipo)."),
 ("aku-elige-temas-y-segmentos-de-alta-interconectividad-verticales-claim","claim","content",
  "Al elegir temas de contenido o definir segmentos, prioriza la alta interconectividad: los temas verticales (de un solo dominio, p.ej. «pricing techniques») conectan a gente con la misma necesidad y se difunden mejor que los horizontales (que cruzan dominios, p.ej. «choice psychology»), cuya audiencia esta desconectada y la infeccion se construye por separado."),
]
def main():
    write(CORE,"concept","viral-marketing, word-of-mouth, marketing-psychology",CORE_STMT)
    for slug,cls,dom,stmt in A: write(slug,cls,dom,stmt)
    print(f"Escritos {len(A)+1} AKUs.")
    edges = [(slug,"supports",CORE) for slug,*_ in A]
    edges += [
     (CORE,"related","aku-cialdini-prueba-social-concept"),  # word-of-mouth / prueba social (Power MBA/Cialdini)
    ]
    wire(edges)
if __name__=="__main__": main()
