import numpy as np
import matplotlib.pyplot as plt
import pds

N = 32
n = np.arange(N)
k = np.arange(N)

w1 = 4*(2*np.pi/N)
w2 = 8*(2*np.pi/N)

x = np.cos(w1*n) + (3/4) * np.cos(w2*n)
X = np.fft.fft(x) # pds.dft, pegar código

plt.figure(1)
plt.stem(k, np.abs(X))
plt.show()