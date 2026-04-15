"""
Desafío VII — Búsqueda del motivo de N-glicosilación
=====================================================
Dado una lista de IDs de UniProt, busca el motivo N{P}[ST]{P} en cada proteína
e imprime las posiciones donde aparece (base 1).

Motivo: N - (cualquiera excepto P) - (S o T) - (cualquiera excepto P)
"""

import sys
import urllib.request


def obtener_secuencia(uniprot_id):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    with urllib.request.urlopen(url) as response:
        lineas = response.read().decode().splitlines()
    # La primera línea es el encabezado (>sp|...)
    return "".join(lineas[1:])


def buscar_motivo(secuencia):
    """Devuelve lista de posiciones (base 1) donde aparece N{P}[ST]{P}."""
    ventana = 4
    posiciones = []
    # Con len(secuencia) - ventana + 1 me aseguro q haya 4 ultimos en este caso para chequear
    for i in range(len(secuencia) - ventana + 1):
        if (secuencia[i]     == "N"
        and secuencia[i + 1] != "P"
        and secuencia[i + 2] in ("S", "T")
        and secuencia[i + 3] != "P"):
            posiciones.append(i + 1)  # base 1
    return posiciones


ids = sys.argv[1:] if len(sys.argv) > 1 else input("IDs de UniProt (separados por espacio): ").split()

for uniprot_id in ids:
    secuencia = obtener_secuencia(uniprot_id)
    posiciones = buscar_motivo(secuencia)
    if posiciones:
        print(uniprot_id)
        print(" ".join(map(str, posiciones)))
