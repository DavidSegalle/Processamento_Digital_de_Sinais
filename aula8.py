import numpy as np
import matplotlib.pyplot as plt
import pds

N = 32

w1 = 4*(2*np.pi/N)
w2 = 8*(2*np.pi/N)

n = np.arange(N)
k = np.arange(N)

x = np.cos(w1*n) + (3/4) * np.cos(w2*n)
X = np.fft.fft(x) # pds.dft, pegar código

plt.figure(1)
plt.stem(k, np.abs(X)/N)

# Mais amostras, menos vazamento, maior resolução
N = 100
n = np.arange(N)
k = np.arange(N)
x = np.cos(w1*n) + (3/4) * np.cos(w2*n)
X = np.fft.fft(x) # pds.dft, pegar código

plt.figure(2)
plt.stem(k, np.abs(X)/N)
'''
# 0 padding
N = 32
K = 100
n = np.arange(N)
k = np.arange(K)
x2 = np.pad(x, (0, K-N), mode='constant')
X2 = np.fft.fft(x2) # pds.dft, pegar código

plt.figure(3)
plt.stem(k, np.abs(X2)/N)
'''
plt.show()