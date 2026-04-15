import pandas as pd
import logomaker
import matplotlib.pyplot as plt

secuencias = [
    "MLPGLALLLLAAWTMRALEVPTDGNAPLLVEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRAQCKTHPHFVIPYRCLVGEFVSDALLAPDKCKFLHQERMDVCETHLHWHTV",
    "MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV",
    "MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV",
]

# Construir matriz de conteos: filas = posiciones, columnas = aminoácidos
counts_matrix = logomaker.alignment_to_matrix(secuencias, to_type="counts")

# Convertir a frecuencias
logo = logomaker.Logo(counts_matrix, color_scheme="chemistry")

logo.ax.set_title("Sequence Logo")
logo.ax.set_xlabel("Posición")
logo.ax.set_ylabel("Counts")

plt.tight_layout()
plt.savefig("sequence_logo.png", dpi=150)
plt.show()
