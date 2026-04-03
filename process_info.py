from start_db import OBTENER_LICITACIONES
import numpy as np
from scipy import stats

data = [x[2] for x in OBTENER_LICITACIONES()]
print("Datos:", data)

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

# Vallas de Tukey
valla_inferior = q1 - 1.5 * iqr
valla_superior = q3 + 1.5 * iqr

print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Valla inferior (Tukey): {valla_inferior}")
print(f"Valla superior (Tukey): {valla_superior}")

outliers = [x for x in data if x < valla_inferior or x > valla_superior]
print(f"Outliers: {outliers}")