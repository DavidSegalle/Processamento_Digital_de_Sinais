import numpy as np
import matplotlib.pyplot as plt
import pds

n = np.arange(-10, 31)
w0 = np.pi/10
p = 10
w0 = round(w0*p)/p

x = np.cos(w0*n)

w2 = w0 + 2 * np.pi * 7
x2 = np.cos(w2 * n)

print(w0)

plt.figure(1)
plt.stem(n, x)

plt.figure(2)
plt.stem(n, x2)

plt.show()