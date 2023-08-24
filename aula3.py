import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 31)
w0 = np.pi/10
x = np.cos(w0*n)

plt.figure(1)
plt.stem(n, x)

plt.show()