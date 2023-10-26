import numpy as np
import matplotlib.pyplot as plt
import pds

N = 6

w1 = np.pi*2 / N

n = np.arange(-20, 20)
k = np.arange(-20, 20)

x = np.cos(w1*n)
X = np.fft.fft(x) # pds.dft, pegar código

plt.figure(1)
plt.stem(k, x)
plt.figure(2)
plt.stem(k / 20 * np.pi, np.abs(X))

# Mais amostras, menos vazamento, maior resolução
N = 100
n = np.arange(N)
k = np.arange(N)
#x = np.cos(w1*n) + (3/4) * np.cos(w2*n)
X = np.fft.fft(x) # pds.dft, pegar código
#np.pad(1, )

n = np.arange(-20, 20)
x1 = pds.u(n+10)

#plt.figure(2)
#plt.stem(k, np.abs(X)/N)
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