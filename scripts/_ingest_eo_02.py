# -*- coding: utf-8 -*-
"""Ingesta — Extreme Ownership, Cap 2 'No Bad Teams, Only Bad Leaders'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/extreme-ownership/extreme-ownership.md"
ORIGIN = "Jocko Willink & Leif Babin, Extreme Ownership (2015)"
EO = "aku-extreme-ownership-concept"
NBT = "aku-no-bad-teams-only-bad-leaders-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku(NBT, "concept",
        "«No hay equipos malos, solo líderes malos» (no bad teams, only bad leaders): el desempeño de un equipo lo determina la calidad de su liderazgo, no la calidad inherente de sus miembros; incluye que cambiar solo al líder puede transformar a un equipo del peor al mejor en las mismas circunstancias; excluye atribuir el bajo rendimiento a la mala suerte o a la composición del equipo. Captura la esencia de Extreme Ownership.",
        DOM + ["equipos", "desempeno"],
        {"supported_by": [EO], "related": ["aku-liderazgo-factor-mas-importante-claim"]}),
    aku("aku-actitud-lider-marca-el-tono-claim", "claim",
        "La actitud del líder marca el tono de todo el equipo y se transmite a sus miembros: una actitud negativa o de victimismo infecta al equipo y justifica el bajo rendimiento, mientras que una actitud ganadora lo eleva.",
        DOM + ["actitud", "equipos"],
        {"supports": [NBT], "related": ["aku-actitud-lider-determina-exito-claim"]}),
    aku("aku-no-es-lo-que-predicas-sino-lo-que-toleras-claim", "claim",
        "En materia de estándares, «no es lo que predicas, es lo que toleras» (it's not what you preach, it's what you tolerate): si se acepta el desempeño por debajo del estándar sin consecuencias ni accountability, ese mal desempeño se convierte en el nuevo estándar; por tanto el líder debe hacer cumplir los estándares.",
        DOM + ["estandares", "accountability"],
        {"supports": [NBT]}),
    aku("aku-repetir-tarea-hasta-estandar-method", "method",
        "Para hacer cumplir un estándar, las consecuencias del fallo no necesitan ser inmediatamente severas, pero el líder debe asegurar que la tarea se repita hasta alcanzar el estándar superior esperado.",
        DOM + ["estandares", "entrenamiento"],
        {"supports": ["aku-no-es-lo-que-predicas-sino-lo-que-toleras-claim"]}),
    aku("aku-gente-quiere-ganar-necesita-forcing-function-claim", "claim",
        "La mayoría de las personas quieren formar parte de un equipo ganador, pero a menudo no saben cómo o solo necesitan motivación y aliento; el equipo necesita una «forcing function» —el liderazgo— que obligue a sus distintos miembros a trabajar juntos para cumplir la misión.",
        DOM + ["motivacion", "equipos"],
        {"supports": [NBT]}),
    aku("aku-cultura-ownership-resiste-perdida-lider-claim", "claim",
        "Una vez construida una cultura de Extreme Ownership en todos los niveles, el equipo sigue rindiendo bien incluso cuando se retira temporalmente a un líder fuerte, porque los líderes junior dan un paso al frente y asumen el mando; toda organización necesita líderes junior listos para sustituir a sus jefes inmediatos.",
        DOM + ["cultura", "resiliencia", "descentralizacion"],
        {"related": ["aku-extreme-ownership-cultura-equipo-claim", "aku-liderazgo-en-todos-los-niveles-claim"]}),
    aku("aku-lideres-nunca-satisfechos-mejora-continua-claim", "claim",
        "Los líderes nunca deben estar satisfechos: deben buscar siempre mejorar e inculcar ese mindset al equipo, afrontando los hechos mediante una evaluación realista y brutalmente honesta de sí mismos y del desempeño del equipo, identificando debilidades y planificando cómo superarlas.",
        DOM + ["mejora-continua", "autoevaluacion"],
        {"supports": [NBT], "related": ["aku-ver-problemas-lente-objetiva-claim"]}),
    aku("aku-tortured-genius-concept", "concept",
        "El «Tortured Genius» (genio torturado) es el mindset opuesto a Extreme Ownership: el individuo que, por evidente que sea su fallo o válida la crítica, acepta cero responsabilidad, pone excusas y culpa a los demás de sus fracasos y los de su equipo, convencido de que el resto del mundo no aprecia su genialidad; incluye que puede tener un impacto catastrófico en el desempeño del equipo.",
        DOM + ["anti-patron", "ego", "responsabilidad"],
        {"contradicts": [EO], "related": ["aku-atribucion-sesgada-exito-fracaso-claim"]}),
    aku("aku-si-no-ganas-no-tomas-buenas-decisiones-claim", "claim",
        "Si no estás ganando, entonces no estás tomando las decisiones correctas: el resultado del equipo es la medida de la calidad de las decisiones del líder, y no se puede afirmar que se decide bien mientras se pierde.",
        DOM + ["decisiones", "desempeno"],
        {"related": ["aku-medida-significativa-liderazgo-claim"]}),
    aku("aku-liderar-desde-posicion-mas-dificil-claim", "claim",
        "El líder debe ponerse en la posición más difícil —al frente— y liderar desde ahí, exigiendo al equipo más de lo que cree que puede dar, en lugar de mandar desde la comodidad o protegerse del esfuerzo.",
        DOM + ["ejemplo", "esfuerzo"],
        {"supports": [NBT]}),
    aku("aku-metas-intermedias-visibles-method", "method",
        "Para sostener el desempeño hacia un objetivo lejano, enfocar el esfuerzo del equipo no en la meta final aún invisible, sino en una meta inmediata y visible (el siguiente hito a la vista); alcanzar metas visibles sucesivas se acumula en un desempeño sustancialmente mayor a lo largo del tiempo.",
        DOM + ["objetivos", "ejecucion"],
        {"supports": [NBT]}),
    aku("aku-lealtad-mal-entendida-proteger-underperformers-claim", "claim",
        "La lealtad mal entendida de proteger o «cobijar» a los underperformers crónicos de la rendición de cuentas (mentalidad «nosotros contra ellos» frente a los estándares) arrastra al resto del equipo y es un flaco favor: no se tiene derecho a obligar a otros a cargar con los miembros más débiles.",
        DOM + ["lealtad", "estandares"],
        {"related": ["aku-lealtad-mision-sobre-individuo-claim", "aku-entrenar-mentorizar-underperformer-claim"]}),
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
