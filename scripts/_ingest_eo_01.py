# -*- coding: utf-8 -*-
"""Ingesta — Extreme Ownership, Cap 1 'Extreme Ownership'. Claims que elaboran
el concepto fundacional (ya creado en intro). Cross-links auto-aplicados."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/extreme-ownership/extreme-ownership.md"
ORIGIN = "Jocko Willink & Leif Babin, Extreme Ownership (2015)"
EO = "aku-extreme-ownership-concept"
D = "2026-06-05"

def aku(id, statement, domain, rel=None):
    return {"id": id, "class": "claim", "statement": statement,
            "origin": ORIGIN, "domain": domain, "llm_confidence": 0.50,
            "epistemic_type": "sourced", "sources": [SRC],
            "created": D, "updated": D, "rel": rel or {}}

DOM = ["liderazgo", "jocko"]
akus = [
    aku("aku-lider-mirar-al-espejo-claim",
        "Cuando los subordinados no rinden como deberían, el líder que ejerce Extreme Ownership no puede culparlos: debe mirarse primero al espejo y buscar la causa en su propio liderazgo —si explicó bien la misión, si dio las tácticas, el entrenamiento y los recursos.",
        DOM + ["responsabilidad"], {"supports": [EO], "related": ["aku-lider-responsable-mision-tactica-recursos-claim"]}),
    aku("aku-lider-responsable-mision-tactica-recursos-claim",
        "El líder es plenamente responsable de explicar la misión estratégica, desarrollar las tácticas y asegurar el entrenamiento y los recursos que permiten al equipo ejecutar correctamente y con éxito.",
        DOM + ["responsabilidad"], {"supports": [EO]}),
    aku("aku-entrenar-mentorizar-underperformer-claim",
        "Ante un miembro del equipo que no rinde al nivel requerido para que el equipo tenga éxito, el líder debe primero entrenarlo y mentorizarlo para elevar su desempeño antes de cualquier otra medida.",
        DOM + ["equipos", "desempeno"], {"supports": [EO], "related": ["aku-lealtad-mision-sobre-individuo-claim"]}),
    aku("aku-lealtad-mision-sobre-individuo-claim",
        "Si el underperformer fracasa continuamente en alcanzar los estándares pese al entrenamiento, el líder con Extreme Ownership debe ser leal al equipo y a la misión por encima de cualquier individuo, y tomar la decisión difícil de sustituirlo por alguien que pueda hacer el trabajo.",
        DOM + ["equipos", "decisiones-dificiles"], {"supports": [EO]}),
    aku("aku-atribucion-sesgada-exito-fracaso-claim",
        "Por defecto las personas atribuyen el éxito ajeno a la suerte o las circunstancias y excusan sus propios fallos y los del equipo culpando a la mala suerte, a circunstancias fuera de su control o a los subordinados —a cualquiera menos a sí mismas; superar este sesgo para aceptar la responsabilidad total del fracaso exige una humildad y un coraje extraordinarios.",
        DOM + ["sesgos", "humildad"], {"supports": [EO], "related": ["aku-humildad-asumir-errores-claim"]}),
    aku("aku-owner-no-toma-credito-da-honor-claim",
        "El líder que ejerce Extreme Ownership no se atribuye el mérito de los éxitos del equipo, sino que otorga ese honor a sus líderes subordinados y a los miembros del equipo: asume los fallos y comparte el crédito.",
        DOM + ["ego", "equipos"], {"supports": [EO], "related": ["aku-mejores-lideres-mision-no-ego-claim"]}),
    aku("aku-extreme-ownership-cultura-equipo-claim",
        "Cuando el líder modela Extreme Ownership y lo exige a los líderes junior, el mindset se convierte en la cultura del equipo en todos los niveles: los líderes junior asumen el mando de su parte de la misión y la eficiencia y la eficacia aumentan exponencialmente.",
        DOM + ["cultura", "equipos", "descentralizacion"], {"supports": [EO]}),
    aku("aku-ver-problemas-lente-objetiva-claim",
        "Extreme Ownership exige mirar los problemas de la organización a través de la lente objetiva de la realidad, sin apego emocional a agendas ni a planes: dejar el ego a un lado, aceptar la responsabilidad de los fallos y atacar las debilidades.",
        DOM + ["objetividad", "ego"], {"supports": [EO], "related": ["aku-mejores-lideres-mision-no-ego-claim"]}),
    aku("aku-actitud-lider-determina-exito-claim",
        "Sometidas a escenarios de entrenamiento idénticos, es casi siempre la actitud del líder —asumir la responsabilidad frente a culpar a los demás— lo que determina si la unidad triunfa o fracasa, por encima de las circunstancias, el equipamiento o la experiencia de la tropa.",
        DOM + ["equipos", "desempeno"], {"supports": [EO]}),
    aku("aku-no-obligar-sino-liderar-claim",
        "No se puede obligar a las personas a escuchar ni a ejecutar —a lo sumo es una solución temporal para una tarea simple—; para lograr que un equipo acometa algo verdaderamente complejo, difícil o peligroso hay que liderarlo, no forzarlo.",
        DOM + ["influencia", "equipos"], {"supports": [EO]}),
    aku("aku-culpar-se-contagia-claim",
        "La actitud de culpar a los demás se contagia hacia abajo: cuando un líder culpa a otros, los subordinados la imitan y el equipo se vuelve incapaz de ejecutar el plan; es el espejo negativo de la propagación de la cultura de ownership.",
        DOM + ["cultura", "equipos"], {"supports": [EO], "related": ["aku-extreme-ownership-cultura-equipo-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
# auto-aplicar inversos de cross-links (new -> existing) agrupados por target
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
akupatch.apply(ROOT, patch_ops)
print(f"cross-links inversos aplicados sobre {len(patch_ops)} AKUs existentes:")
for t, rels in ops.items():
    print(f"  {t}: +{len(rels)} ({rels[0][0]})")
