# Transformada Z

import matplotlib.pyplot as plt
import numpy as np
import pds

from scipy.signal import residuez
# B: coeficientes do nominador
# A: coeficientes do denoinador

b = [6, -10, 2]
a = [1, -3, 2]


# R são os numeradores
# P são os polos da divisão
# K são os resultados (se possível)
r, p, k = residuez(b, a)

#print(r)
print(p)
#print(k)

n = np.arange(-3, 10) # Pode ser qualquer entrada

h_a = 2* pds.u(n) + 3 * (2.**n)*pds.u(n) + pds.delta(n) # Resposta ao impulso analítica

h_n = pds.lfilter(b, a, pds.delta(n)) # Resposta ao impulso numérica

#print(pds.mse(h_a, h_n))

plt.figure(1)
plt.stem(n, h_a)
plt.show()
