>
>**PARA PENSAR** 🤔: ¿Qué tipo de información se puede extraer de la comparación de secuencias? ¿Cómo esperás que se vea en una comparación? 🤔
>

Se puede extraer informacion sobre su historia evolutiva, y su funcion.


>
>**PARA PENSAR** 🤔: ¿Por qué crees que es mejor evaluar las relaciones evolutivas lejanas comparando proteínas? 🤔
>

Porque las secuencias proteicas son más informativas. Las proteínas acumulan cambios más lentamente que el ADN (por la presión selectiva sobre su función), y además el alfabeto de 20 aminoácidos es más informativo que el de 4 nucleótidos, lo que reduce la probabilidad de coincidencias al azar.

---

## DESAFIO I: Alineamiento de "BANANA" y "MANZANA"

Al intentar alinear las palabras BANANA (6 caracteres) y MANZANA (7 caracteres) en la tabla interactiva, se observa que **no existe una única forma de alinearlas**. Dado que las secuencias tienen distinta longitud, es necesario introducir al menos un gap para generar el alineamiento, y ese gap puede colocarse en distintas posiciones, generando múltiples alineamientos posibles. Algunos ejemplos:

**Alineamiento 1:**
```
BAN-ANA
MANZANA
```
Coincidencias: A, N, A, N, A → 5 matches | Mismatch: B/M → 1

**Alineamiento 2:**
```
-BANANA
MANZANA
```
Coincidencias: A, N, A → 3 matches | Mismatches: B/A, A/N, N/Z → 3 

**Alineamiento 3:**
```
BANANA-
MANZANA
```
Coincidencias: A, N → 2 matches | Mismatches: B/M, A/Z, N/A, A/N → 4

**¿Es alguno mejor que otro?** Sí. El **Alineamiento 1** (`BAN-ANA / MANZANA`) es claramente el mejor porque maximiza el número de posiciones coincidentes (5 de 7) y minimiza tanto los gaps como los mismatches. Coloca el gap frente a la Z —el único caracter de MANZANA que no tiene par en BANANA—, permitiendo que el resto de la secuencia (ANANA) quede perfectamente alineada.

**El mejor alineamiento no es simplemente poner una secuencia sobre la otra, sino encontrar la disposición que maximice la similitud biológicamente relevante**, minimizando las penalizaciones por gaps y mismatches. La elección de dónde colocar los gaps tiene un impacto directo en la puntuación del alineamiento y, por ende, en las inferencias evolutivas que se deriven de él.

---

## DESAFIO II: Identidad en alineamientos de "ANA" y "ANANA"

Los valores de identidad **no son iguales** para todos los alineamientos. Por ejemplo:

```
ANA--       --ANA      A-NA-
ANANA       ANANA      ANANA
```
El primero y el segundo dan 3 matches; el tercero da menos. Pero incluso con la misma cantidad de matches, el valor de identidad depende de **cómo se calcula el denominador**:
- Matches / longitud de la secuencia más larga → 3/5 = 60%
- Matches / longitud de la secuencia más corta → 3/3 = 100%
- Matches / total de posiciones alineadas (incluyendo gaps) → varía. Ej: `ANA-- / ANANA` tiene 3 matches sobre 5 posiciones totales = 60%

No todas las formas son igualmente válidas en biología: usar la secuencia más corta como denominador puede inflar artificialmente la identidad, ignorando los gaps. Lo más informativo es considerar la longitud total del alineamiento o de la secuencia de referencia.

---

## DESAFIO III: Efecto de la penalización de gaps en la identidad

Al aumentar la penalización por gap, los alineamientos con más gaps reciben puntajes más bajos, favoreciendo aquellos que los evitan aunque introduzcan más mismatches. Al disminuirla, se toleran más gaps para maximizar los matches.

Una mayor penalización de gaps tiene sentido biológico porque las inserciones/deleciones son eventos mutacionales menos frecuentes que las sustituciones. Sin embargo, penalizar demasiado puede llevar a alineamientos con muchos mismatches que son biológicamente incorrectos.

Una forma de penalización no contemplada en el ejemplo es la **penalización por extensión de gap** (gap extension penalty): en lugar de penalizar igual cada posición de un gap, se cobra un costo fijo al abrir el gap y un costo menor por cada posición adicional.

---

## DESAFIO IV: Gaps en alineamientos de secuencias nucleotídicas

**PARA PENSAR previo:** Abrir un gap en una secuencia nucleotídica implica un **corrimiento del marco de lectura (frameshift)**: todos los codones posteriores al gap quedan desplazados, cambiando completamente la proteína traducida a partir de ese punto. Si la inserción o deleción abarca más de un residuo pero **no es múltiplo de 3**, el frameshift persiste. Si es **múltiplo de 3**, se insertan o eliminan aminoácidos completos sin alterar el marco de lectura del resto de la secuencia.

**¿Da lo mismo dónde cae el gap dentro del codón?** No. Un gap en la **primera o segunda posición** del codón altera ese codón y todos los siguientes. Un gap en la **tercera posición** (posición wobble) también causa frameshift, pero el codón afectado puede cambiar a uno sinónimo o a uno que codifica un aminoácido diferente. En cualquier caso, el impacto sobre la traducción aguas abajo es igualmente severo.

**¿Cómo ponderar estas observaciones para evaluar el parecido?** Un gap en un alineamiento de nucleótidos no es equivalente a un mismatch: tiene consecuencias funcionales mucho más drásticas. Por eso, al comparar secuencias codificantes conviene penalizar fuertemente los gaps y, mejor aún, evaluar el parecido a nivel de la secuencia proteica resultante, que absorbe la degeneración del código genético y refleja más directamente la conservación funcional.

## DESAFIO V:

Diagrama de flujo basado

1. Definir match/mismatch/gap 
2. Crear matriz (n+1)x(m+1)   
3. Inicializar fila/columna 0 (acumular penalidad gap)   
4.  Para cada celda seteo el score basandome en el maximo entre la celda izq, la celda diagonal, y la celda de arriba. Cuando lo tengo guardo el puntero (direccion de la celda con score maximo)    
5.  Traceback desde (n,m) hasta (0,0). diag=match, ↑/←=gap
6. Alineamiento óptimo + score

> **PARA PENSAR** 🤔: ¿En qué consiste la programación dinámica? ¿Por qué crees que es útil en este caso? 

La programación dinámica es una estrategia para resolver problemas que se pueden descomponer en subproblemas más chicos y repetidos. En lugar de resolver el mismo subproblema una y otra vez, lo resolvés una sola vez, guardás su resultado en una tabla (la matriz), y lo reutilizás cada vez que lo necesitás.

Nos permite resolver la alineacion de forma mas eficiente que usando fuerza bruta. Ademas al tener sub problemas que se repiten, la programacion dinamica es ideal para este caso.

---

## PARA PENSAR: Alineamiento global vs local

**¿En qué casos es útil cada uno?**

- **Global**: útil cuando las secuencias son similares en tamaño y se quiere comparar toda su extensión. Ej: comparar el mismo gen entre dos especies cercanas.
- **Local**: útil cuando las secuencias tienen distinto tamaño o solo comparten regiones conservadas. Ej: buscar si un dominio funcional específico está presente en otra proteína.

**Limitaciones:**

- **Global**: si las secuencias son muy diferentes en tamaño, fuerza el alineamiento en regiones sin similitud real, generando resultados poco informativos.
- **Local**: puede perder contexto evolutivo al ignorar el resto de la secuencia fuera de la región alineada.

---

## DESAFIO VI

Dependiendo de los valores que asignaramos al match/mismatch/gap. Comparamos la celda actual con la celdas lindantes. Si es match, sumamos el valor de la celdxa diagonal al valor del match. En cambio si es mismatch sumamos el valor de la diagonal con el valor del mismatch (negativo seguramente), luego para ambos casos calculamos el valor de la celdas izquierda, y la celda arriba sumandole el valor del gap. Cuando tenemos los 3 valores nos quedamos con el maximo score

---

## PARA PENSAR: Programas derivados de BLAST en NCBI

| Programa | Query | Base de datos | Cuándo usarlo |
|---|---|---|---|
| **blastp** | proteína | proteína | identificar proteínas homólogas |
| **blastn** | nucleótido | nucleótido | comparar genes o genomas |
| **blastx** | nucleótido (traduce 6 marcos) | proteína | cuando tenés una secuencia nucleotídica y querés inferir función proteica |
| **tblastn** | proteína | nucleótido (traduce 6 marcos) | buscar genes no anotados que codifiquen una proteína conocida |
| **tblastx** | nucleótido (traduce) | nucleótido (traduce) | comparar regiones codificantes entre genomas |

---

## DESAFIO VII

**E-value vs % identidad**

Más identidad → E-value más bajo. Pero no es estricta  un alineamiento corto puede tener identidad alta y E-value alto porque el largo del alineamiento también importa.

**Score vs % identidad**

Más identidad → más score. Más posiciones idénticas suman más en la matriz de sustitución.

**Score vs E-value**

La más consistente. Son casi matemáticamente inversos — el E-value se calcula a partir del score, entonces cuando uno sube el otro baja exponencialmente.

## DESAFIO VIII

El largo de la secuencia afecta directamente la significancia estadística. Una secuencia corta con buena identidad no necesariamente es un hit confiable porque puede ser mas probable que sea generada al azar dentro de los registros de la base de datos evaluada.

## DESAFIO IX

Proteína: acyl-ACP–UDP-N-acetylglucosamine O-acyltransferase
Organismo: Enterobacteria
Score: 505
Cobertura: 100%
E-value: 6e-180
Identidad: 92.37%

La acyl-ACP–UDP-N-acetylglucosamine O-acyltransferase (también llamada LpxA) cataliza el primer paso de la biosíntesis del lipopolisacárido (LPS). Transfiere un ácido graso al UDP-N-acetylglucosamine. El LPS es componente esencial de la membrana externa de bacterias Gram-negativas.

Pseudomonadota, clase Gammaproteobacteria, orden Enterobacterales, familia Enterobacteriaceae. Los géneros con mayor score son Klebsiella, Kluyvera, Siccibacter, Enterobacter.

¿Cuántas secuencias similares a nivel de significancia adecuada?
100 hits con E-value < 10⁻⁵

## DESAFIO X

**¿Se obtienen los mismos resultados?**

No exactamente. Los organismos coinciden (Escherichia coli, Proteobacteria) pero hay menos hits. PDB es mucho más pequeña, solo contiene proteínas con estructura 3D resuelta experimentalmente.

**¿Qué tipo de hits se recuperan?**

Proteínas con estructura tridimensional determinada. Por eso aparecen hits de E. coli K-12 con 100% identidad.

**¿Cuándo es útil buscar contra PDB?**

Cuando querés conocer la estructura 3D de tu proteína o una homóloga.