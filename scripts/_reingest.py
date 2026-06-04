# -*- coding: utf-8 -*-
"""Motor de reingesta diferencial: parsea enums, ancla relaciones, genera AKUs."""
import sys, os, re, json, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = '--write' not in sys.argv
BOOKS = {
 'offers': dict(src="raw/libros/hormozi/100m-offers/100m-offers.md", orig="Alex Hormozi — $100M Offers",
                dom=["oferta","hormozi"], fallback="aku-grand-slam-offer-concept"),
 'leads':  dict(src="raw/libros/hormozi/100m-leads/100m-leads.md", orig="Alex Hormozi — $100M Leads",
                dom=["marketing-digital","captacion","hormozi"], fallback="aku-core-four-concept"),
 'money':  dict(src="raw/libros/hormozi/100m-money-models/100m-money-models.md", orig="Alex Hormozi — $100M Money Models",
                dom=["monetizacion","money-model","hormozi"], fallback="aku-money-model-concept"),
}
# (regex sobre slug, anchor_id existente, tipo_relacion). Primer match gana.
# supported_by => el nuevo concept es soportado por el paraguas (paraguas.supports -> nuevo).
ANCHORS = [
 # --- money: offers types (explode umbrellas) ---
 (r"giveaway", "aku-giveaway-offer-concept", "related"),
 (r"decoy", "aku-decoy-offer-concept", "related"),
 (r"win-money-back|win-your-money", "aku-win-your-money-back-concept", "related"),
 (r"buy-x-get-y|mas-gratis|mas-y-mejor-gratis|free-stuff|subir-precios-antes|seguir-vendiendo-a-prepagados|compra-unica", "aku-buy-x-get-y-free-concept", "related"),
 (r"pay-less|pay-later|pay-now", "aku-pay-less-now-or-more-later-concept", "related"),
 (r"classic-upsell|menu-upsell|anchor-upsell|rollover-upsell", "aku-cuatro-upsells-concept", "supported_by"),
 (r"unselling|prescription|ab-upsell|card-on-file|say-no-to-say-yes|economist|decoy-pricing|gift-card-play", "aku-cuatro-upsells-concept", "related"),
 (r"anchor-the-gasp|anchor-no-fake|anchor-features|rollover-precio|rollover-urgencia|rollover-antes|rollover-roba", "aku-cuatro-upsells-concept", "related"),
 (r"upsell|hyper-buying|bamfam|surprise-and-delight|bonos-gratis-crean|acceso-rapido|nombrar-bundles|integrar-upsells|actually-do-the-upsell|cobrar-por-garantias|vender-agotado", "aku-upsell-offer-concept", "related"),
 (r"payment-plan-downsell|trial-with-penalty-concept|feature-downsell-concept", "aku-tres-downsells-concept", "supported_by"),
 (r"payment-plan|trial-penalty|trial-with-penalty|feature-downsell|seesaw|reward-prepago|tarjeta-credito-reframe|alinear-cobros|billing-cadence|llamar-trial|pay-less-vs-trial|barter-descuento|free-orientation|nombrar-feature|alternar-payment|no-significa-este|nunca-negociar", "aku-downsell-offer-concept", "related"),
 (r"continuity-bonus-concept|continuity-discount-concept|waived-fee-concept", "aku-tres-continuity-offers-concept", "supported_by"),
 (r"continuity|waived-fee|lifetime-discount|cancellation|billing-cada|processing-fee|dos-formas-de-pago|exit-interview|facilitar-cancel|titulos-como-bono|anunciar-bono|bonos-fisicos|commitment-a-cambio|bulk-prepaid|standalone-ratio|extender-termino|no-standalone", "aku-continuity-offer-concept", "related"),
 (r"money-model|tres-palancas|todo-negocio|hard-selling|dar-refund|no-vender-lo-que|reputacion|no-arrancar|perfeccionar-una|raise-price-in-stages|cien-formas|afiliados-rellenan|attraction-a-continuity|mezclar-ofertas|bootstrapped|rompe-cash|se-rompe-cuando|orden-de-los-tres|crecimiento-multiplicativo|bad-money-model", "aku-money-model-concept", "related"),
 (r"attraction|descuento|discount|cuatro-formas-anunciar", "aku-attraction-offer-concept", "related"),
 # --- offers ---
 (r"gross-profit", "aku-margen-bruto-concept", "related"),
 (r"ltgp|lifetime-value", "aku-cltv-concept", "related"),
 (r"price-to-value|discrepancia-coste", "aku-ampliar-gap-valor-precio-claim", "related"),
 (r"magic-magnet|magic-avatar|magic-goal|magic-interval|magic-container|magnet-concept|avatar-concept|goal-concept|interval-concept|container-concept", "aku-magic-naming-concept", "supported_by"),
 (r"unconditional-guarantee|conditional-guarantee|anti-guarantee", "aku-garantia-reversion-riesgo-concept", "supported_by"),
 (r"guarantee|garantia|reversion-riesgo|stacking-guarantee", "aku-garantia-reversion-riesgo-concept", "related"),
 (r"seats|limited-bonuses|never-available|business-cap|growth-rate-cap|cohort-cap|honest-scarcity|extreme-scarcity|tres-tipos-escasez|escasez-servicios", "aku-tipos-y-tacticas-escasez-concept", "related"),
 (r"cohort-rolling|rolling-seasonal|pricing-bonus-urgency|seasonal-urgency", "aku-urgencia-concept", "related"),
 (r"bonus|bonos", "aku-bonuses-stack-concept", "related"),
 (r"naming|magic|ofertas-fatigan|orden-variacion|implicit-egotism|marketing-local", "aku-magic-naming-concept", "related"),
 (r"gso-cinco|listar-problemas|problema-a-solucion|trim-and-stack|delivery-vehicles|bundle-tres|resolver-cada-problema|sales-fulfillment", "aku-grand-slam-offer-concept", "related"),
 (r"grow-or-die|tres-formas-crecer|premium-decision|quien-necesita-menos|no-competir-en-precio|pricing-imitativo|offer-definicion", "aku-grand-slam-offer-concept", "related"),
 (r"perception-is-reality|dream-outcome-status|vender-lo-que-valoran", "aku-value-equation-concept", "related"),
 (r"cuando-sube-demanda-corta", "aku-vender-menos-aumenta-demanda-claim", "related"),
 # --- leads ---
 (r"lead-contactable|engaged-leads-son|advertising-making|doblar-leads", "aku-core-four-concept", "related"),
 (r"lead-magnet|core-offer|siete-pasos|multiples-formatos|cuatro-funciones|scarcity-real|headline-80", "aku-lead-magnet-concept", "related"),
 (r"cta-hormozi", "aku-cta-concept", "related"),
 (r"warm-outreach|warm-100|nueve-word|preguntar-si-conocen|subir-precio-cada-cinco|free-stuff-too-expensive|comunicacion-1a1", "aku-warm-outreach-concept", "related"),
 (r"hook|topic|headline|format-matchea|listas-steps|short-vs-long|content|give-ask|integrated-vs|depth-then|siete-lecciones|how-to-vs-how-i|puddles|benchmarks-crecimiento", "aku-core-four-concept", "related"),
 (r"cold|construir-lista|volumen-cold|personalizar-como-warm|10-20-tech", "aku-cold-outreach-concept", "related"),
 (r"paid-ads|cuatro-requisitos|callout|landing|ocho-elementos|what-when|presupuesto|ltgp-cac|cac-similar|diagnostico-cac|sales-problem|mejor-contenido|ltgp-concept", "aku-paid-ads-concept", "related"),
 (r"more-better|rule-of-100|constraint|un-test-por|size-of-pie|orden-new|volumen-test|leverage-leads|high-roi|one-page|100m-lead-machine|many-sided", "aku-core-four-concept", "related"),
 (r"referido|referral|goodwill|wins-rapidos|replicar-acciones|mejora-continua|vender-mejores|bajar-expectativas|vender-de-nuevo|un-solo-cliente|siete-formas-pedir|tres-componentes-referral|referir-es-riesgo|falta-referidos|pedir-referidos", "aku-referral-growth-exponential-claim", "related"),
 (r"empleado|trade-40|internal-core|entrenar-seguir|coste-por-engaged|diagnostico-sales|negocio-sin-ti", "aku-empleados-lead-getters-concept", "related"),
 (r"agencia|agency|dos-agencias|diez-criterios", "aku-usar-agencias-para-aprender-claim", "related"),
 (r"affiliate|afiliado|super-afiliado|affiliate-army|oferta-al-afiliado|cualificar-afiliado|payout|whisper|launch-then|pagar-afiliados|cuatro-fortalezas", "aku-marketing-afiliados-concept", "related"),
 (r"open-to-goal|roadmap|get-started", "aku-roadmap-7-niveles-captacion-concept", "related"),
]

def anchor_for(slug):
    for rx, aid, rt in ANCHORS:
        if re.search(rx, slug):
            return aid, rt
    return None

existing = set(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(ROOT,"aku","*.md")))

def run_book(name):
    cfg = BOOKS[name]
    items = json.load(open(os.path.join(ROOT,f"outputs/_{name}_final.json"),encoding='utf-8'))
    akus=[]; collisions=[]; dangling=set(); seen=set()
    for it in items:
        slug=it['slug']
        if not re.match(r'^aku-[a-z0-9-]+$', slug):
            collisions.append((slug,'slug-invalido')); continue
        if slug in existing or slug in seen:
            collisions.append((slug,'ya-existe')); continue
        seen.add(slug)
        a=anchor_for(slug)
        rel={}
        if a:
            aid,rt=a; rel[rt]=[aid]
            if aid not in existing: dangling.add(aid)
        else:
            rel['related']=[cfg['fallback']]
            if cfg['fallback'] not in existing: dangling.add(cfg['fallback'])
        if it['pm'] and it['pm'] not in sum(rel.values(),[]):
            rel.setdefault('related',[]).append(it['pm'])
            if it['pm'] not in existing: dangling.add(it['pm'])
        akus.append(dict(id=slug, **{'class':it['cls']}, statement=it['stmt'], origin=cfg['orig'],
                         domain=cfg['dom'], sources=[cfg['src']], rel=rel,
                         created='2026-06-04', updated='2026-06-04'))
    return akus, collisions, dangling

if __name__=='__main__':
    books = [a for a in sys.argv[1:] if a in BOOKS] or list(BOOKS)
    for name in books:
        akus, collisions, dangling = run_book(name)
        print(f"\n=== {name}: {len(akus)} a crear | colisiones {len(collisions)} | anclas-inexistentes {len(dangling)}")
        if dangling: print("  DANGLING:", sorted(dangling))
        if collisions: print("  COLISIONES:", collisions[:40])
        if DRY:
            continue
        # build inverse patch ops for all anchors/pm targets
        written, cross = akugen.generate(akus, [], ROOT)
        ops={}
        for a,f,inv,tgt in cross:
            ops.setdefault(tgt,[]).append((inv,a))
        patchops=[{'id':t,'add_rel':rels} for t,rels in ops.items()]
        for p in akupatch.apply(ROOT, patchops): pass
        print(f"  WRITTEN {len(written)} | patched {len(patchops)} anchors")
