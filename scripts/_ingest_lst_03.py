# -*- coding: utf-8 -*-
"""Ingesta — Leadership Strategy and Tactics, Sección 3 'Principles' (cierra Part 1)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/leadership-strategy-and-tactics/leadership-strategy-and-tactics.md"
ORIGIN = "Jocko Willink, Leadership Strategy and Tactics: Field Manual (2020)"
SOC = "aku-span-of-control-concept"
PRIDE = "aku-pride-fuerza-de-doble-filo-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku("aku-cada-miembro-es-el-mas-importante-claim", "claim",
        "Dile a cada miembro del equipo —y créelo— que es el más importante, porque en cualquier momento cualquiera puede volverse el más importante y su fallo en un instante crítico puede ser catastrófico; explícale, incluso al del trabajo más menial, qué pasa si no hace bien su parte y cómo encaja en la misión estratégica.",
        DOM + ["motivacion", "equipos"],
        {"related": ["aku-liderazgo-en-todos-los-niveles-claim", "aku-leading-down-the-chain-concept", "aku-conexion-rol-big-picture-no-intuitiva-claim"]}),
    aku("aku-taking-care-of-people-con-disciplina-claim", "claim",
        "La disciplina es la mejor forma de cuidar a tu gente: «cuidar de tu gente» no significa mimarla, hacerla estar cómoda y darle todo el tiempo libre posible, sino empujarla y entrenarla duro para que esté preparada (que vuelva a casa / que alcance sus metas); el camino fácil lleva a la miseria, el de la disciplina a la libertad —pero hay que equilibrarlo para no quemarla—.",
        DOM + ["disciplina", "cuidado"],
        {"related": ["aku-discipline-equals-freedom-concept", "aku-disciplina-raiz-de-toda-buena-cualidad-concept", "aku-train-hard-but-train-smart-concept"]}),
    aku("aku-imposed-vs-self-discipline-en-equipo-concept", "concept",
        "La disciplina óptima de un equipo no la impone el líder, la elige el propio equipo: es autodisciplina; cuando el equipo aún no la tiene, el líder explica el porqué y da ownership para lograr el cambio voluntario; imponer por orden directa quita input y ownership → resistencia o incluso sabotaje; imponer la disciplina es un último recurso muy raro (solo ante agendas desalineadas) y se usa con cautela.",
        DOM + ["disciplina", "mando"],
        {"related": ["aku-self-discipline-viene-de-dentro-concept", "aku-no-es-lo-que-predicas-sino-lo-que-toleras-claim", "aku-dar-confianza-incrementalmente-method"]}),
    aku(PRIDE, "concept",
        "El orgullo (pride) es una fuerza de doble filo: en exceso deriva en arrogancia, estancamiento y falta de respeto al adversario; pero bien canalizado es una fuerza positiva que mantiene a la gente trabajando duro, cuidando los detalles y autoexigiéndose el máximo estándar (el equipo se auto-vigila); hay que equilibrarlo entre humildad y confianza, sin dejarlo derivar a ninguno de los dos extremos.",
        DOM + ["orgullo", "dicotomia"],
        {"related": ["aku-dichotomy-of-leadership-concept", "aku-confident-but-not-cocky-concept", "aku-disease-of-victory-concept"]}),
    aku("aku-pride-se-construye-con-sufrimiento-compartido-claim", "claim",
        "El orgullo de equipo se construye con el sufrimiento compartido: no se puede contar solo con la historia o las victorias, hay que hacer que el equipo lo gane mediante trabajo y entrenamiento duros; «si quieres construir orgullo, trae dolor»; el equipo que se lo gana se auto-vigila y da más de lo exigido —pero cuidado de no romperlos ni volverlos arrogantes—.",
        DOM + ["orgullo", "entrenamiento"],
        {"related": [PRIDE, "aku-train-hard-but-train-smart-concept"]}),
    aku("aku-dar-ordenes-solo-commanders-intent-claim", "claim",
        "Al dar órdenes, no dictes los detalles (qué tropas, vehículos, armas, tiempos, rutas): da solo el objetivo de la misión (Commander's Intent) y deja que los subordinados hagan el plan, así lo poseen; aunque tu plan sea un 90% y el suyo un 80%, deja correr el suyo (la convicción compensa el 10%), y da correcciones proporcionales a lo malo que sea su plan; el mayor obstáculo para soltar es tu ego.",
        DOM + ["mando", "delegacion"],
        {"related": ["aku-commanders-intent-concept", "aku-decentralizar-proceso-planificacion-claim", "aku-check-the-ego-concept"]}),
    aku("aku-no-yes-men-fomentar-pushback-claim", "claim",
        "Ni quieras estar rodeado de yes-men ni seas uno: los subordinados deben hacer pushback, preguntar por qué y aportar información de primera línea; un yes-man que responde «Roger that» a una orden suicida lleva a su pelotón a la muerte, mientras que un subordinado de confianza dice «jefe, eso no es buena idea» y propone una alternativa; si el pushback te incomoda, revisa tu ego (probablemente esté algo inflado).",
        DOM + ["feedback", "ego"],
        {"related": ["aku-ejecutar-decision-como-propia-claim", "aku-leading-up-the-chain-concept", "aku-no-es-lo-que-predicas-sino-lo-que-toleras-claim"]}),
    aku("aku-exception-good-team-bad-leader-claim", "claim",
        "La excepción a «no hay equipos malos, solo líderes malos»: sí puede haber un BUEN equipo que rinde pese a un MAL líder estructural, cuando hay subordinados que lideran con tacto sin rango oficial (y el líder estructural tiene la humildad de dejarles); por tanto, que un equipo rinda no implica que su líder estructural sea bueno —el líder de más arriba debe conocer qué impulsa de verdad el éxito de cada equipo para gestionar bien movimientos y ascensos—.",
        DOM + ["equipos", "matiz"],
        {"related": ["aku-no-bad-teams-only-bad-leaders-concept", "aku-liderazgo-en-todos-los-niveles-claim", "aku-humildad-es-la-cualidad-mas-importante-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
# enrich span-of-control con 2a fuente (LST)
found = next((o for o in patch_ops if o["id"] == SOC), None)
if found: found["add_source"] = SRC; found["confidence"] = 0.60
else: patch_ops.append({"id": SOC, "add_source": SRC, "confidence": 0.60, "updated": D})
akupatch.apply(ROOT, patch_ops)
print(f"cross + enrich sobre {len(patch_ops)} AKUs; enrich span-of-control 0.60")
