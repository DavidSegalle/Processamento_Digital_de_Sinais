# Transformada Z

import matplotlib.pyplot as plt
import numpy as np
import pds

from scipy.signal import residuez
# B: coeficientes do nominador
# A: coeficientes do denoinador

p = [np.exp(1j*np.pi/10), np.exp(-1j*np.pi/10)]
a = np.poly(p)
b = (1,)

n = np.arange(-3, 100) # Pode ser qualquer entrada

h_n = pds.lfilter(b, a, pds.delta(n)) # Resposta ao impulso numérica

#print(pds.mse(h_a, h_n))

plt.figure(1)
plt.stem(n, h_n)
plt.show()
