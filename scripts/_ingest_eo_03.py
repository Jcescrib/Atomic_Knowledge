# -*- coding: utf-8 -*-
"""Ingesta — Extreme Ownership, Cap 3 'Believe'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/extreme-ownership/extreme-ownership.md"
ORIGIN = "Jocko Willink & Leif Babin, Extreme Ownership (2015)"
EO = "aku-extreme-ownership-concept"
BEL = "aku-believe-in-the-mission-concept"
WHY = "aku-preguntar-por-que-method"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(BEL, "concept",
        "«Believe» (creer en la misión): para convencer e inspirar a otros a seguirle y cumplir una misión, el líder debe ser un verdadero creyente en ella y en la causa mayor; incluye que una creencia resuelta en la misión es, con mucho, más importante que el entrenamiento o el equipamiento para que un equipo gane; excluye liderar una misión en la que el propio líder no cree.",
        DOM + ["creencia", "mision"],
        {"supported_by": [EO]}),
    aku("aku-creer-para-asumir-riesgos-y-convencer-claim", "claim",
        "Si un líder no cree en la misión, no asumirá los riesgos necesarios para superar los desafíos inevitables que exige ganar, ni será capaz de convencer a los demás —especialmente a las tropas de primera línea que deben ejecutar— de que lo hagan.",
        DOM + ["creencia", "riesgo"],
        {"supports": [BEL]}),
    aku("aku-parte-de-algo-mas-grande-claim", "claim",
        "Los líderes deben operar siempre con la conciencia de que forman parte de algo más grande que ellos mismos y sus intereses personales, e impartir esa conciencia a sus equipos hasta los operadores de nivel táctico.",
        DOM + ["proposito", "mision"],
        {"supports": [BEL]}),
    aku("aku-creencia-del-lider-se-transmite-claim", "claim",
        "Cuando un líder cree, esa creencia se transmite hacia arriba y hacia abajo en la cadena de mando: sus palabras y actos reflejan una confianza y seguridad imposibles cuando la creencia está en duda; a la inversa, cuando la confianza del líder se quiebra, quienes deben seguirle empiezan a dudar de su propia creencia en la misión.",
        DOM + ["creencia", "confianza"],
        {"supports": [BEL]}),
    aku(WHY, "method",
        "Cuando un líder recibe una orden que cuestiona o no entiende, debe preguntar «¿por qué?»: dar un paso atrás, deconstruir la situación, analizar el cuadro estratégico y llegar a una conclusión; si no encuentra por sí mismo una respuesta satisfactoria, debe preguntar hacia arriba en la cadena de mando hasta entenderlo.",
        DOM + ["comunicacion", "estrategia"],
        {"supports": [BEL]}),
    aku("aku-detach-tactico-estrategico-concept", "concept",
        "«Detach» (desapegarse) es la capacidad del líder de despegarse de la misión táctica inmediata para entender cómo encaja en los objetivos estratégicos; incluye salir del detalle del momento para ver el cuadro general; es prerrequisito para preguntar por qué y para creer en la misión.",
        DOM + ["estrategia", "perspectiva"],
        {"supports": [WHY]}),
    aku("aku-senior-debe-explicar-el-porque-claim", "claim",
        "Es responsabilidad de los líderes senior tomarse el tiempo de explicar y responder las preguntas de sus líderes junior —explicar no solo el qué hacer, sino el porqué—, porque las tropas de primera línea nunca tienen una comprensión del cuadro estratégico tan clara como los seniors asumen.",
        DOM + ["comunicacion", "estrategia"],
        {"supports": [BEL], "related": [WHY]}),
    aku("aku-objetivos-alineados-organizacion-claim", "claim",
        "En cualquier organización los objetivos deben estar siempre alineados; si en algún nivel no lo están, el problema debe abordarse y corregirse, porque un subordinado que no entiende una estrategia no creerá en ella.",
        DOM + ["objetivos", "alineamiento"],
        {"supports": [BEL]}),
    aku("aku-feedback-hacia-arriba-cadena-claim", "claim",
        "Los líderes junior deben no solo preguntar, sino también dar feedback hacia arriba en la cadena de mando, para que los líderes senior comprendan las ramificaciones de cómo sus planes estratégicos afectan a la ejecución sobre el terreno.",
        DOM + ["comunicacion", "feedback"],
        {"related": [WHY]}),
    aku("aku-subordinado-responsable-de-entender-porque-claim", "claim",
        "Si no entiendes o no crees en las decisiones que bajan de tu liderazgo, es tu responsabilidad (Extreme Ownership) preguntar hasta entender cómo y por qué se toman; no conocer el porqué impide creer en la misión y, en una posición de liderazgo, es una receta para el fracaso e inaceptable.",
        DOM + ["responsabilidad", "creencia"],
        {"supports": [EO], "related": [WHY]}),
    aku("aku-preguntar-requiere-coraje-claim", "claim",
        "Preguntar hacia arriba en la cadena —admitir que no entiendes la estrategia— requiere coraje: la gente teme parecer estúpida ante el jefe, pero se sentirá mucho peor intentando explicar a su equipo una misión que ella misma no entiende ni cree.",
        DOM + ["coraje", "comunicacion"],
        {"supports": [WHY]}),
    aku("aku-liderazgo-es-grupo-no-individuo-concept", "concept",
        "El liderazgo no es una persona liderando a un equipo, sino un grupo de líderes trabajando juntos —arriba y abajo en la cadena de mando— para liderar; incluye que los subordinados cubren los fallos del jefe sin invadir su «terreno de liderazgo»; excluye al líder en solitario, que por bueno que sea no podrá con todo.",
        DOM + ["equipos", "descentralizacion"],
        {"related": ["aku-liderazgo-en-todos-los-niveles-claim"]}),
    aku("aku-jefe-subestima-peso-de-su-posicion-claim", "claim",
        "Un error común de los jefes (militares o ejecutivos) es no comprender del todo el peso y el poder de su posición: se creen accesibles y con «política de puertas abiertas», pero en la mente de sus subordinados siguen siendo «El Jefe», y cuestionar sus ideas les parece una falta de respeto o un riesgo de quedar mal.",
        DOM + ["poder", "comunicacion"],
        {"related": ["aku-preguntar-requiere-coraje-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
akupatch.apply(ROOT, patch_ops)
print(f"cross-links inversos sobre {len(patch_ops)} AKUs existentes:")
for t, rels in ops.items():
    print(f"  {t}: +{rels}")
