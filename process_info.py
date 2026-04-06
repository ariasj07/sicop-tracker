from start_db import OBTENER_LICITACIONES
import numpy as np
from scipy import stats

data = [x[2] for x in OBTENER_LICITACIONES()]
print("Datos:", data)
print(np.mean(data))