# Auditoría de grafo — corpus 50-cent (2026-06-08)

Tras ingestar «Hustle Harder, Hustle Smarter» (159 AKUs + 3 TAKUs) y cablear los puentes
aprobados por Joan.

## Integridad
- `verify_graph`: **1999/1999 AKU simétrico, 0 errores** (0 body-drift, 0 wikilinks rotos, 0 sources→aku).
- Componentes conectados: **1** (largest = 1999). Huérfanos (degree 0): **0**.
- Sub-conectados (degree 1-2): 1173 (normal: hojas-claim).

## Cableado aplicado (54 aristas `related`, sync 3 capas vía akupatch)
- **50 puentes** cross-corpus (b) + cross-chapter (a) aprobados — `scripts/_50cent_bridges.py`.
- **4 aristas correctoras de islas**: el audit detectó 2 islas de 2 nodos que mi INTEGRATE
  por capítulo no había puenteado al grafo principal, ahora resueltas:
  - `crab-in-the-barrel` + `no-hay-espacio-para-suckers` → vía `homeboy-complex` y
    `identifica-y-manten-distancia-de-quienes-te-arrastran-al-fondo` (Ch9).
  - `ofrece-valor-en-vez-de-pedir-un-puesto` + `trabaja-gratis-como-intern` → vía
    `just-do-shit` y `probar-que-sabes-hacer-algo`.

## Cómo se integra 50-cent con el resto del grafo (conexiones principales)
- **Jocko** (mayor afinidad): entitlement/responsabilidad ↔ `extreme-ownership` (hub, ahora
  degree 35); aprender-de-Ls ↔ `good-mindset`; disciplina-equipo ↔ extreme-ownership;
  adaptar-liderazgo ↔ `dichotomy-of-leadership`; miedo-útil ↔ `miedo-al-fracaso-es-bueno`;
  tiempo-más-caro ↔ `tiempo-recurso-mas-valioso`; admitir-error ↔ `humildad-asumir-errores`.
- **Naval**: pedir-equity & quien-te-emplea-paga-menos ↔ `no-te-haces-rico-alquilando-tu-tiempo`;
  meditación-mantra ↔ `choiceless-awareness`; juez-de-carácter & cambiar-de-opinión ↔
  `judgment-naval`; trabajo=felicidad ↔ `felicidad-es-satisfacción`; want-como-motor ↔
  `el-deseo-es-un-contrato-para-ser-infeliz` (tensión productiva); depósitos/retiros &
  círculo ↔ `juega-juegos-iterados` (gente de largo plazo); just-do-shit/responsabilidad ↔
  `accountability-bajo-tu-nombre`.
- **Robert Greene / 48 Laws** (coautoría «The 50th Law»): competencia ↔ L15 crush-enemy &
  L06 court-attention; subvertir-expectativas ↔ L46 never-appear-too-perfect; fake-it ↔
  L37 create-compelling-spectacles; juez-de-carácter ↔ L02 never-trust-friends.
- **Cialdini / Power MBA / Hormozi**: act-like-you-dont-need-it & exclusividad ↔
  `cialdini-escasez` + `tipos-y-tacticas-escasez` (Hormozi); toque-antebrazo ↔
  `cialdini-simpatia`; percepción & señales ↔ `identidad-de-marca`/`branding`; keep-a-book ↔
  `cinco-fuerzas-porter`; due-diligence-equity ↔ `equity-value`; liderazgo-situacional;
  vision-boards ↔ `compartir-objetivos-compromiso`.
- **Atomic Habits**: cambiar-hábito-30-días ↔ `never-miss-twice`; trabajo-duro ↔
  `enamórate-del-aburrimiento`; evolucionar ↔ `editar-tu-identidad`; aprender-de-Ls ↔
  `reflexión-y-revisión`.

## Coherencia y estructura del corpus 50-cent
- **Topología interna**: cada capítulo forma un sub-cluster alrededor de su concept-AKU
  núcleo (9 principios), unidos por el framework TAKU `los-9-principios`. El concepto
  paraguas `calle-y-negocios-comparten-principios` y `sostener-el-exito` actúan de raíz.
- **Uso de `related`**: 101/159 AKUs son solo-`related` (0 typed). Es esperable y correcto
  para un memoir de lecciones normativas débilmente acopladas (claims paralelos del mismo
  tema), a diferencia de los frameworks fuertemente tipados de Hormozi/Power MBA. Los
  concept-núcleo sí portan `supported_by` y sus claims `supports`. No es un error; el lint
  podría marcarlos >30d para revisión de upgrade tipado, pero la mayoría son genuinamente
  `related` (no upgradeables a supports/constrains).
- **Tensiones valiosas** (no contradicciones estrictas): `want-como-motor` (50 Cent: el deseo
  motiva) ↔ `el-deseo-es-un-contrato-para-ser-infeliz` (Naval). Modeladas como `related`.
- **Contenido amoral**: caps. 6 (percepción/manipulación) y 7 (competencia) ingestados como
  descripción de tácticas, framing descriptivo en los statements. Conecta deliberadamente
  con el cluster 48-laws (también amoral) y contrasta con Jocko (integridad).

## TAKUs creados (3, todos draft / llm-authored / links llm-proposed)
- `taku-los-9-principios-hustle-harder-hustle-smarter` (framework, 10 justified_by).
- `taku-vision-board` (tool).
- `taku-cuatro-cualidades-de-una-estrella` (framework).

## Pendiente de validación humana
- Validar `human_certainty` de los 159 AKUs y activar los 3 TAKUs cuando proceda.
- Revisar si algún solo-`related` merece upgrade a `supports`/`constrains` (rigor > cantidad).
