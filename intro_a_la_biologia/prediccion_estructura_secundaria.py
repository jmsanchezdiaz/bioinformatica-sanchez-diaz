# Desafío V — Predicción de estructura secundaria proteica

# Qué inputs tendría tu programa? 
# una secuencia de aminoacidos (en este caso una lista de caracteres)
# ¿De qué modo se te ocurre configurar el output? 
# una lista de caracteres, string de la estructura predicha.

# Propensidades de Chou-Fasman: (Pa_helix, Pb_sheet)
PROPENSIDADES = {
    "A": (1.42, 0.83), "R": (0.98, 0.93), "N": (0.67, 0.89),
    "D": (1.01, 0.54), "C": (0.70, 1.19), "E": (1.51, 0.37),
    "Q": (1.11, 1.10), "G": (0.57, 0.75), "H": (1.00, 0.87),
    "I": (1.08, 1.60), "L": (1.21, 1.30), "K": (1.16, 0.74),
    "M": (1.45, 1.05), "F": (1.13, 1.38), "P": (0.57, 0.55),
    "S": (0.77, 0.75), "T": (0.83, 1.19), "W": (1.08, 1.37),
    "Y": (0.69, 1.47), "V": (1.06, 1.70),
}


def predecir(secuencia):
    prediccion = ""
    for aa in secuencia.upper():
        if aa not in PROPENSIDADES:
            prediccion += "?"
            continue
        pa, pb = PROPENSIDADES[aa]
        if pa > 1.0 and pa > pb:
            prediccion += "H"
        elif pb > 1.0 and pb >= pa:
            prediccion += "B"
        # No necesito ver el valor del loop pq las otras condiciones no se cumplen por lo tanto es bucle.
        else:
            prediccion += "L"
    return prediccion


# --- Input ---
secuencia = input("Ingresá la secuencia proteica: ").strip()

# --- Predicción ---
prediccion = predecir(secuencia)

# --- Output ---
print("\nSecuencia:", secuencia.upper())
print("Predicción:", prediccion)
print("\nH = α-hélice  |  B = hoja-β  |  L = loop")
