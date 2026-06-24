# Inferencias Evolutivas - Respuestas

## Desafío I

La táctica sería comparar la secuencia del Cyt del *bartmosca* con las secuencias de mosca y humano mediante alineamientos de secuencias. El alineamiento es el paso más crítico porque establece las correspondencias posicionales en la evolución, y a partir de él se puede cuantificar la divergencia entre las secuencias.

Como criterio de comparación, no alcanza con simplemente contar las sustituciones entre secuencias, ya que el número de sustituciones observadas puede subestimar los eventos evolutivos reales por el fenómeno de **homoplasia** (sustituciones convergentes o reversiones). Por eso es necesario aplicar modelos evolutivos (como Jukes-Cantor o Kimura 2P) que corrigen esa diferencia entre lo observado y lo esperado, obteniendo distancias evolutivas más precisas. Además, conviene considerar no solo identidad sino también similitud, usando matrices de sustitución como BLOSUM o PAM que ponderan los cambios según su probabilidad evolutiva.

Con esas distancias, se construye un árbol filogenético que permite visualizar con cuál organismo se agrupa más *bartmosca*. Para poder interpretar el árbol correctamente, es decir, darle sentido histórico y saber quién divergió de quién, ademas es necesario incluir una secuencia externa al grupo (de interes) que permita enraizar el árbol.

Si se usara el resto de las secuencias del análisis, el árbol permitiría ubicar a *bartmosca* en un contexto evolutivo más amplio. Dado que el Citocromo C es una proteína altamente conservada en eucariotas, pequeñas diferencias son evolutivamente informativas, y esperaríamos que *bartmosca* se agrupara más cerca de uno de los dos organismos, lo que indicaría qué porción de su secuencia predomina.

## Desafio II

<img src="./alineamiento_bart_mosca.png" />

## Desafio III

#### Modelo de Sustitución
El modelo de sustitución describe matemáticamente cómo cambian los aminoácidos o nucleótidos durante la evolución. Es fundamental elegir el correcto: para proteínas como Cytochrome c usamos WAG, no GTR (que es para DNA). Diferentes modelos reflejan diferentes tasas y patrones de cambio evolutivo.

#### Bootstrap
Es un método de remuestreo donde generamos 1000 versiones aleatorias del alineamiento original (tomando posiciones al azar con reemplazo) y construimos un árbol para cada una. Luego contamos: de esos 1000 árboles, ¿en cuántos aparece cada rama? El porcentaje es el valor de soporte de bootstrap.

Ejemplo: si una rama aparece en 900 de 1000 árboles = 90% de soporte = esa agrupación es confiable.

#### Calidad del Árbol
El bootstrap solo mide robustez estadística:

> 90%: Rama muy confiable
70-90%: Rama aceptable
< 70%: Rama no confiable

Un alto valor no garantiza que sea biológicamente correcto, solo que es consistente en nuestros datos.

#### Número de Bootstraps
A más bootstraps, más precisión, pero con rendimientos decrecientes. El estándar es 1000 bootstraps para proteínas. Pasar de 100 a 1000 mejora mucho; pasar de 1000 a 2000 mejora poco.

(Utilice otra pagina por que no me funcionaba figtree) (Utilice ITOL)
<img width="1145" height="274" alt="Captura de pantalla 2026-06-17 a la(s) 5 43 51 p  m" src="https://github.com/user-attachments/assets/03e2f86a-8763-445f-9902-da268898a625" />

* Rhizobium sp. CF097 (WP_037127040) — bacteria, outgroup
* Drosophila melanogaster — animal (insecto)
* bartmosca — animal (humano-insecto?)
* Homo sapiens — animal (mamífero)
* Ectocarpus siliculosus — alga parda (heteroconta)
* Hordeum vulgare — planta (monocot)
* Vigna radiata — planta (leguminosa)
* Lupinus albus — planta (leguminosa)
* Betula platyphylla — planta (árbol)

#### Conclusiones:
- Respeta la división fundamental procariota-eucariota
- Separa correctamente plantas de animales
- Las plantas se agrupan entre sí
- Los animales se agrupan entre sí
- Cytochrome c es una proteína muy conservada
- Pocos cambios acumulados incluso en organismos muy divergentes
