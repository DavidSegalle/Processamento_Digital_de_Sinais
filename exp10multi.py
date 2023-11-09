import numpy as np 
import matplotlib.pyplot as plt
import pds

A = [1, 3, 5, 4, 2]

w = np.arange(1, 6) * np.pi / 5

M = 60
m = np.arange(M + 1)

h = pds.multifaixa(A, w, M)
H, w = pds.dtft(h, m, np.linspace(0, np.pi, 1024))

fig1, ax1 = plt.subplots()

ax1.plot(w/np.pi, np.abs(H), "C4")

plt.show()