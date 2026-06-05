# -*- coding: utf-8 -*-
"""Ingesta hiper-exhaustiva — Extreme Ownership, Introducción (cap 0)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/extreme-ownership/extreme-ownership.md"
ORIGIN = "Jocko Willink & Leif Babin, Extreme Ownership (2015)"
D = "2026-06-05"

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement,
            "origin": ORIGIN, "domain": domain, "llm_confidence": 0.50,
            "epistemic_type": "sourced", "sources": [SRC],
            "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku("aku-extreme-ownership-concept", "concept",
        "Extreme Ownership es el mindset por el que el líder asume la responsabilidad total y absoluta de todo lo que ocurre en su ámbito —misión, equipo, errores, fallos y resultados— sin culpar a nadie ni a las circunstancias; incluye admitir los propios errores y buscar primero en uno mismo la causa de cualquier fallo del equipo; implica que es el fundamento sobre el que se apoyan todos los demás principios de liderazgo.",
        ["liderazgo", "jocko", "responsabilidad", "mindset"],
        {"supported_by": ["aku-humildad-asumir-errores-claim", "aku-mejores-lideres-mision-no-ego-claim"]}),
    aku("aku-liderazgo-factor-mas-importante-claim", "claim",
        "El liderazgo es el factor más importante en el campo de batalla y la mayor razón individual detrás del éxito o el fracaso de cualquier equipo; ningún otro factor influye tanto en el desempeño del equipo como la calidad de su liderazgo.",
        ["liderazgo", "jocko", "equipos"],
        {"related": ["aku-medida-significativa-liderazgo-claim", "aku-liderazgo-en-todos-los-niveles-claim"]}),
    aku("aku-medida-significativa-liderazgo-claim", "claim",
        "La única medida significativa de un líder es si su equipo cumple la misión (éxito) o no (fracaso); todas las demás definiciones, descripciones y rasgos de carácter son irrelevantes frente a este criterio binario de resultado.",
        ["liderazgo", "jocko", "equipos"],
        {"constrains": ["aku-lider-efectivo-vs-inefectivo-concept"]}),
    aku("aku-lider-efectivo-vs-inefectivo-concept", "concept",
        "Solo existen dos categorías de líder que importan: el efectivo, cuyo equipo cumple la misión y gana, y el inefectivo, cuyo equipo no lo logra; incluye que la distinción se basa exclusivamente en el resultado del equipo; excluye clasificar a los líderes por estilo, carisma o rasgos personales.",
        ["liderazgo", "jocko"]),
    aku("aku-liderazgo-en-todos-los-niveles-claim", "claim",
        "El liderazgo decisivo para el éxito de un equipo no es solo el del mando superior, sino el de los líderes de cada nivel de la organización —líderes de equipos de cuatro, de escuadras de ocho, y suboficiales junior que dan un paso al frente y asumen el mando.",
        ["liderazgo", "jocko", "equipos", "descentralizacion"]),
    aku("aku-laws-of-combat-concept", "concept",
        "Las Leyes del Combate (Laws of Combat) son los cuatro conceptos —Cover and Move (cubrir y avanzar), Simple, Prioritize and Execute (priorizar y ejecutar) y Decentralized Command (mando descentralizado)— que, comprendidos y aplicados conjuntamente, permiten a cualquier equipo rendir al máximo nivel y dominar; incluye que son interdependientes y mutuamente reforzantes; excluye tratarlos como tácticas aisladas.",
        ["liderazgo", "jocko", "combate", "equipos"],
        {"supported_by": ["aku-extreme-ownership-concept"]}),
    aku("aku-principios-combate-aplican-a-negocio-claim", "claim",
        "Los mismos principios de liderazgo que hacen efectivos a los líderes SEAL en combate se aplican con igual éxito a cualquier equipo, empresa u organización, porque el combate es un reflejo intensificado y amplificado de la vida: cualquier situación en que un grupo debe trabajar unido para ejecutar una tarea y cumplir una misión.",
        ["liderazgo", "jocko", "transferibilidad", "negocio"],
        {"related": ["aku-laws-of-combat-concept"]}),
    aku("aku-humildad-asumir-errores-claim", "claim",
        "Para un líder, la humildad de admitir y asumir los propios errores y de diseñar un plan para superarlos es esencial para el éxito; los mejores líderes no son infalibles, sino que convierten sus errores en sus mayores lecciones.",
        ["liderazgo", "jocko", "humildad", "errores"]),
    aku("aku-mejores-lideres-mision-no-ego-claim", "claim",
        "Los mejores líderes no se mueven por el ego ni por agendas personales, sino que se enfocan exclusivamente en la misión y en cómo cumplirla mejor.",
        ["liderazgo", "jocko", "ego", "mision"]),
    aku("aku-simple-but-not-easy-concept", "concept",
        "Los principios de liderazgo eficaz son «simples pero no fáciles» (simple, but not easy): conceptualmente sencillos y basados en el sentido común, pero a menudo contraintuitivos y que exigen habilidad, esfuerzo enfocado, entrenamiento y disciplina sostenida en el tiempo para implementarlos y dominarlos.",
        ["liderazgo", "jocko", "implementacion"],
        {"related": ["aku-laws-of-combat-concept"]}),
    aku("aku-relax-look-around-make-a-call-method", "method",
        "Ante una situación de presión extrema o caos, el protocolo de decisión es «Relax, look around, make a call» (relájate, mira alrededor, toma una decisión): recuperar la calma para no dejarse abrumar, evaluar la situación global priorizando la amenaza mayor, y decidir y ejecutar sin paralizarse; condición: aplicable cuando el pánico o la inacción agravan el riesgo.",
        ["liderazgo", "jocko", "decision", "presion"],
        {"related": ["aku-laws-of-combat-concept"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
for w in written:
    print("  +", os.path.relpath(w, ROOT))
print(f"cross-links a existentes (inverso manual): {len(cross)}")
for c in cross:
    print("  CROSS:", c)
