# -*- coding: utf-8 -*-
"""Ingest Almanack of Naval — cap 'Understand How Wealth Is Created' (Building Wealth)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/naval/almanack-of-naval-ravikant/almanack-of-naval-ravikant.md"
ORIGIN = "Naval Ravikant — The Almanack of Naval Ravikant (ed. Eric Jorgenson, 2020)"
D = "2026-06-05"
N = "naval"

def c(idn, cls, st, dom, rel=None):
    return {"id": idn, "class": cls, "statement": st, "origin": ORIGIN,
            "domain": dom, "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    # ── Concepts: wealth / money / status ──
    c("aku-wealth-activos-que-ganan-mientras-duermes-concept", "concept",
      "Wealth (riqueza) es poseer activos que ganan dinero mientras duermes —negocios, "
      "robots/fábricas, software que sirve a clientes de noche, dinero reinvertido en otros "
      "activos—; incluye cualquier cosa que produzca rendimiento sin tu tiempo presente; "
      "excluye money (mero medio de transferencia) y status (posición social); implica que "
      "la libertad financiera viene de activos que trabajan por ti, no de vender tu tiempo.",
      ["riqueza", N, "wealth", "activos"],
      {"related": ["aku-money-transfiere-tiempo-y-riqueza-concept",
                   "aku-status-posicion-en-jerarquia-social-concept",
                   "aku-equity-value-concept"]}),
    c("aku-money-transfiere-tiempo-y-riqueza-concept", "concept",
      "Money (dinero) es cómo transferimos riqueza y tiempo: son créditos sociales, la "
      "capacidad de tener créditos y débitos del tiempo de otras personas; incluye ser un "
      "IOU que la sociedad te da por el valor creado; excluye ser riqueza en sí (es solo su "
      "vehículo de transferencia); implica que acumular dinero no es el fin, sino un medio.",
      ["riqueza", N, "money", "dinero"],
      {"related": ["aku-status-posicion-en-jerarquia-social-concept"]}),
    c("aku-status-posicion-en-jerarquia-social-concept", "concept",
      "Status es tu lugar en la jerarquía social; incluye ser un juego de suma cero que se "
      "gana atacando a otros; excluye crear valor nuevo (es reposicionarse frente a los "
      "demás); implica que quienes juegan juegos de estatus ganan posición atacando a "
      "quienes juegan juegos de creación de riqueza.",
      ["riqueza", N, "status", "jerarquia"]),
    # ── Specific knowledge ──
    c("aku-specific-knowledge-concept", "concept",
      "Specific knowledge (conocimiento específico) es conocimiento para el que no te pueden "
      "entrenar: si la sociedad puede entrenarte, puede entrenar a otro y reemplazarte; "
      "incluye ser hallado persiguiendo tu curiosidad y pasión genuinas (no lo que está de "
      "moda), sentirse como juego para ti pero parecer trabajo para otros, enseñarse por "
      "aprendizaje (apprenticeship) no en escuelas, y ser altamente técnico o creativo; "
      "excluye lo que puede externalizarse o automatizarse; implica que es tu fuente de "
      "ventaja insustituible.",
      ["riqueza", N, "specific-knowledge", "conocimiento"]),
    # ── Leverage ──
    c("aku-leverage-multiplicador-de-juicio-concept", "concept",
      "Leverage (apalancamiento, en el sentido de Naval) es un multiplicador de fuerza para "
      "tu juicio: las fortunas lo requieren; incluye tres fuentes —capital (dinero), labor "
      "(personas trabajando para ti) y productos con coste marginal de replicación nulo "
      "(código y medios)—; excluye el mero trabajo duro sin palanca; implica que aplicar "
      "specific knowledge con accountability y leverage produce resultados desproporcionados.",
      ["riqueza", N, "leverage", "apalancamiento"],
      {"related": ["aku-apalancamiento-financiero-concept",
                   "aku-permissioned-vs-permissionless-leverage-concept",
                   "aku-judgment-naval-concept"]}),
    c("aku-permissioned-vs-permissionless-leverage-concept", "concept",
      "El leverage se divide en permissioned (con permiso) y permissionless (sin permiso): "
      "capital y labor son permissioned —alguien tiene que darte el dinero o decidir "
      "seguirte—; código y medios son permissionless —puedes crear software y contenido que "
      "trabajan por ti mientras duermes, sin pedir permiso a nadie—; implica que el código y "
      "los medios son la palanca detrás de los nuevos ricos.",
      ["riqueza", N, "leverage", "codigo-y-medios"]),
    # ── Accountability / Judgment ──
    c("aku-accountability-bajo-tu-nombre-concept", "concept",
      "Accountability (responsabilidad personal, en Naval) es asumir riesgos de negocio bajo "
      "tu propio nombre, exponiéndote públicamente; incluye aceptar el lado negativo a cambio "
      "del positivo; excluye esconderse en el anonimato; implica que la sociedad te recompensa "
      "con responsabilidad, equity y leverage por aceptar accountability.",
      ["riqueza", N, "accountability", "responsabilidad"]),
    c("aku-judgment-naval-concept", "concept",
      "Judgment (juicio) es la capacidad de saber qué hacer, multiplicada por el leverage; "
      "incluye requerir experiencia pero poder construirse más rápido aprendiendo habilidades "
      "fundacionales (microeconomía, teoría de juegos, psicología, persuasión, ética, "
      "matemáticas, computación); implica que en un mundo apalancado te pagan cada vez más por "
      "tu buen juicio y cada vez menos por tu tiempo o esfuerzo.",
      ["riqueza", N, "judgment", "juicio"]),
    # ── Productize yourself / technology ──
    c("aku-productize-yourself-concept", "concept",
      "«Productize yourself» (productízate) es el mnemónico de Naval para hacerse rico: "
      "«yourself» aporta unicidad, accountability y specific knowledge; «productize» aporta "
      "leverage y specific knowledge; incluye preguntarte si lo que ofreces es auténtico a ti "
      "y si lo estás escalando (con labor, capital, código o medios); implica combinar quién "
      "eres de forma única con un vehículo que escale.",
      ["riqueza", N, "productize-yourself", "escalar"],
      {"related": ["aku-specific-knowledge-concept",
                   "aku-accountability-bajo-tu-nombre-concept",
                   "aku-leverage-multiplicador-de-juicio-concept"]}),
    c("aku-technology-cosas-que-aun-no-funcionan-concept", "concept",
      "Technology (tecnología) es el conjunto de cosas que aún no funcionan del todo (Danny "
      "Hillis); una vez algo funciona, deja de ser tecnología; incluye que democratiza el "
      "consumo pero consolida la producción (el mejor del mundo en algo lo hace para todos); "
      "implica que para hacerte rico debes proveer a la sociedad algo que quiere pero aún no "
      "sabe cómo obtener, y luego escalarlo.",
      ["riqueza", N, "tecnologia", "escalar"]),
    # ── Methods ──
    c("aku-aspirational-hourly-rate-method", "method",
      "Fija y haz cumplir una tarifa horaria personal aspiracional: si arreglar un problema "
      "ahorra menos que tu tarifa horaria, ignóralo; si externalizar una tarea cuesta menos "
      "que tu tarifa horaria, externalízala; implica usar la tarifa como filtro sistemático "
      "para decidir en qué inviertes tu tiempo.",
      ["riqueza", N, "productividad", "tiempo"]),
    # ── Claims (tweetstorm + prose) ──
    c("aku-hacer-dinero-es-habilidad-que-se-aprende-claim", "claim",
      "Hacer dinero no es algo que haces sino una habilidad que se aprende: es un skillset "
      "desarrollable por cualquiera, hasta el punto de que, perdido todo y dejado en una "
      "calle al azar de cualquier país anglófono, en 5-10 años se podría volver a ser rico.",
      ["riqueza", N, "mentalidad", "habilidad"]),
    c("aku-riqueza-es-entender-que-quien-cuando-no-solo-trabajo-duro-claim", "claim",
      "Hacerse rico va de saber qué hacer, con quién y cuándo —es más comprensión que puro "
      "trabajo duro—: puedes trabajar 80 horas semanales en un restaurante y no enriquecerte; "
      "el trabajo duro importa y no se puede escatimar, pero debe dirigirse en la dirección "
      "correcta, y antes hay que averiguar en qué deberías trabajar.",
      ["riqueza", N, "estrategia", "trabajo"]),
    c("aku-busca-wealth-no-money-ni-status-claim", "claim",
      "Hay que buscar wealth (riqueza), no money ni status: la riqueza son activos que "
      "trabajan por ti, mientras money y status son medios o posiciones que no constituyen el "
      "fin; perseguir estatus o acumular dinero por sí mismos desvía de la creación de riqueza.",
      ["riqueza", N, "mentalidad"],
      {"related": ["aku-wealth-activos-que-ganan-mientras-duermes-concept"]}),
    c("aku-no-te-haces-rico-alquilando-tu-tiempo-debes-poseer-equity-claim", "claim",
      "No te harás rico alquilando tu tiempo: para lograr libertad financiera debes poseer "
      "equity —una parte de un negocio—, porque solo los activos que ganan sin tu presencia "
      "generan riqueza.",
      ["riqueza", N, "equity", "libertad-financiera"],
      {"related": ["aku-equity-value-concept",
                   "aku-wealth-activos-que-ganan-mientras-duermes-concept"]}),
    c("aku-da-a-la-sociedad-lo-que-quiere-a-escala-claim", "claim",
      "Te haces rico dando a la sociedad lo que quiere pero aún no sabe cómo obtener, a "
      "escala: la sociedad paga por crear cosas que desea pero no sabe producir (si supiera, "
      "no te necesitaría), y hay que escalarlo a miles o millones de unidades.",
      ["riqueza", N, "escalar", "valor"]),
    c("aku-creacion-de-riqueza-etica-es-posible-claim", "claim",
      "La creación ética de riqueza es posible, y conviene creerlo: si secretamente desprecias "
      "la riqueza, te eludirá; la actitud hacia la riqueza condiciona la capacidad de crearla.",
      ["riqueza", N, "mentalidad", "etica"]),
    c("aku-juega-juegos-iterados-retornos-del-interes-compuesto-claim", "claim",
      "Hay que jugar juegos iterados: todos los retornos de la vida —en riqueza, relaciones o "
      "conocimiento— vienen del interés compuesto, así que la repetición con las mismas "
      "personas y dominios a lo largo del tiempo es lo que multiplica los resultados.",
      ["riqueza", N, "largo-plazo", "interes-compuesto"],
      {"related": ["aku-capitalizar-interes-compuesto-method",
                   "aku-elige-juegos-largo-plazo-con-gente-largo-plazo-claim"]}),
    c("aku-elige-juegos-largo-plazo-con-gente-largo-plazo-claim", "claim",
      "Elige una industria donde puedas jugar juegos a largo plazo con personas a largo "
      "plazo: la reputación y la confianza acumuladas con contrapartes estables son las que "
      "componen retornos, a diferencia de los entornos de relaciones efímeras.",
      ["riqueza", N, "largo-plazo", "reputacion"]),
    c("aku-elige-socios-con-integridad-sobre-todo-claim", "claim",
      "Elige socios de negocio con alta inteligencia, energía y, por encima de todo, "
      "integridad: sin integridad, la inteligencia y la energía se vuelven en tu contra.",
      ["riqueza", N, "socios", "integridad"]),
    c("aku-no-te-asocies-con-cinicos-ni-pesimistas-claim", "claim",
      "No te asocies con cínicos ni pesimistas: sus creencias son autocumplidas y arrastran "
      "el resultado del proyecto hacia abajo.",
      ["riqueza", N, "socios", "mentalidad"]),
    c("aku-aprende-a-vender-y-a-construir-claim", "claim",
      "Aprende a vender y aprende a construir: si puedes hacer ambas cosas, serás imparable, "
      "porque combinas la creación de valor con la capacidad de capturarlo.",
      ["riqueza", N, "habilidades", "ventas"]),
    c("aku-no-existe-la-habilidad-de-los-negocios-claim", "claim",
      "No existe una habilidad llamada «negocios»: hay que evitar las revistas y clases de "
      "negocios genéricas y estudiar en su lugar microeconomía, teoría de juegos, psicología, "
      "persuasión, ética, matemáticas y computación, que son las habilidades fundacionales del "
      "buen juicio.",
      ["riqueza", N, "aprendizaje", "juicio"],
      {"related": ["aku-judgment-naval-concept"]}),
    c("aku-leer-mas-rapido-que-escuchar-hacer-mas-rapido-que-ver-claim", "claim",
      "Leer es más rápido que escuchar y hacer es más rápido que ver: para aprender y avanzar "
      "conviene priorizar los medios de mayor ancho de banda y la práctica directa.",
      ["riqueza", N, "aprendizaje", "productividad"]),
    c("aku-con-quien-y-en-que-trabajas-importa-mas-que-cuanto-claim", "claim",
      "Trabaja tan duro como puedas, pero con quién trabajas y en qué trabajas importan más "
      "que cuán duro trabajas: el esfuerzo mal dirigido rinde poco frente al esfuerzo en la "
      "palanca correcta.",
      ["riqueza", N, "trabajo", "estrategia"]),
    c("aku-se-el-mejor-del-mundo-redefiniendo-lo-que-haces-claim", "claim",
      "Conviértete en el mejor del mundo en lo que haces, y sigue redefiniendo lo que haces "
      "hasta que eso sea cierto: la unicidad (una categoría de uno) es lo que captura el "
      "valor en un mundo que premia al mejor del mundo en cada cosa.",
      ["riqueza", N, "maestria", "unicidad"]),
    c("aku-no-hay-esquemas-para-hacerse-rico-rapido-claim", "claim",
      "No hay esquemas para hacerse rico rápido: lo que se vende como tal es solo otro "
      "haciéndose rico a tu costa; aplicar specific knowledge con leverage durante años es lo "
      "que acaba dándote lo que mereces.",
      ["riqueza", N, "mentalidad"]),
    c("aku-internet-amplia-el-espacio-de-carreras-claim", "claim",
      "Internet ha ampliado enormemente el espacio posible de carreras y la mayoría aún no se "
      "ha dado cuenta: permite encontrar y monetizar specific knowledge en nichos antes "
      "inviables.",
      ["riqueza", N, "internet", "carrera"]),
    c("aku-armate-con-specific-knowledge-accountability-y-leverage-claim", "claim",
      "Ármate con specific knowledge, accountability y leverage: es la tríada operativa para "
      "crear y capturar riqueza —conocimiento insustituible, asumido bajo tu nombre y "
      "multiplicado por una palanca—.",
      ["riqueza", N, "framework"],
      {"related": ["aku-specific-knowledge-concept",
                   "aku-accountability-bajo-tu-nombre-concept",
                   "aku-leverage-multiplicador-de-juicio-concept"]}),
]

takus = [
    {"id": "taku-como-hacerse-rico-sin-suerte", "taku_type": "framework", "subdir": "frameworks",
     "title": "Cómo hacerse rico (sin suerte) — el mapa de Naval",
     "origin": ORIGIN, "domain": [N, "riqueza", "wealth"],
     "when_to_use": "Para orientar decisiones de carrera y negocio hacia la creación de riqueza real (activos que trabajan por ti) en vez de salario, dinero o estatus.",
     "when_not_to_use": "Como esquema para hacerse rico rápido, o en contextos donde no puedes asumir accountability ni construir specific knowledge propio.",
     "aku_links": {"justified_by": [
         "aku-armate-con-specific-knowledge-accountability-y-leverage-claim",
         "aku-specific-knowledge-concept",
         "aku-leverage-multiplicador-de-juicio-concept",
         "aku-productize-yourself-concept",
         "aku-no-te-haces-rico-alquilando-tu-tiempo-debes-poseer-equity-claim"]},
     "created": D, "updated": D,
     "body": (
        "## Summary\n\n"
        "Síntesis del tweetstorm «How to Get Rich (Without Getting Lucky)» de Naval: la "
        "riqueza es un skillset aprendible que se construye combinando specific knowledge, "
        "accountability y leverage, y productizándote para escalar.\n\n"
        "## Core Components\n\n"
        "1. **Busca wealth, no money ni status** (activos que ganan mientras duermes).\n"
        "2. **Specific knowledge** — conocimiento insustituible hallado por curiosidad genuina.\n"
        "3. **Accountability** — asume riesgos bajo tu propio nombre.\n"
        "4. **Leverage** — capital, labor y código/medios (permissionless) multiplican tu juicio.\n"
        "5. **Productize yourself** — combina unicidad con un vehículo que escale.\n"
        "6. **Judgment** — construido con habilidades fundacionales, no con clases de negocios.\n\n"
        "## How to Apply\n\n"
        "1. Averigua en qué puedes ser único antes de machacarte trabajando.\n"
        "2. Persigue tu curiosidad para acumular specific knowledge (te parecerá juego).\n"
        "3. Asume accountability públicamente bajo tu nombre.\n"
        "4. Añade leverage sin permiso: escribe, codifica, graba, construye productos.\n"
        "5. Juega juegos iterados a largo plazo con gente íntegra; deja componer al interés.\n"
        "6. Fija una tarifa horaria aspiracional y filtra tu tiempo con ella.\n\n"
        "## Underlying Claims\n\n"
        "Hacerse rico es habilidad aprendible; understanding > trabajo duro; no te enriqueces "
        "alquilando tu tiempo; los retornos vienen del interés compuesto; el código/medios son "
        "palanca sin permiso.\n\n"
        "## Strengths\n\n"
        "Modelo atemporal e independiente del sector; pone el foco en activos y palanca, no en "
        "horas; integra conocimiento, riesgo y escala en un solo mapa.\n\n"
        "## Limitations and Criticisms\n\n"
        "Requiere horizonte de una década y tolerancia al riesgo personal; presupone acceso a "
        "internet/mercados; «specific knowledge» es difícil de identificar a priori; no es una "
        "receta paso a paso garantizada.\n\n"
        "## Variants and Extensions\n\n"
        "Mnemónico «Productize Yourself»; se complementa con la rama de Building Judgment "
        "(modelos mentales, pensar con claridad) del mismo libro."),
    },
]

written, cross = akugen.generate(akus, takus, ROOT)
print("WRITTEN:", len(written))
for w in written:
    print("  ", os.path.relpath(w, ROOT))
# cross-link inverses on existing AKUs (no same-author here: distinto autor que Power MBA)
ops_by_id = {}
for new_id, field, inv, tgt in cross:
    ops_by_id.setdefault(tgt, {"id": tgt, "add_rel": []})["add_rel"].append((inv, new_id))
akupatch.apply(ROOT, list(ops_by_id.values()))
print("\nPATCHED EXISTING:")
for k, v in ops_by_id.items():
    print("  ", k, v.get("add_rel"))
print("\nCROSS count:", len(cross))
