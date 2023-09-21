import numpy as np
import matplotlib.pyplot as plt

l = 10

w = np.linspace(-np.pi, np.pi, 1024)

x1 = np.exp(-1j * w*(l-1)/2)

x2 = np.sin(w*l/2) / np.sin(w/2)
x = x1*x2

plt.figure(1)
plt.plot(w, np.abs(x))

plt.figure(2)
plt.plot(w, np.angle(x))

plt.show()