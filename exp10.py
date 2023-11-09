import numpy as np
import matplotlib.pyplot as plt
import pds

M = 20
m = np.arange(M+1)

w5 = np.pi
w4 = 4*np.pi/5

h = pds.sinc2(m-M/2, w4) - pds.sinc2(m-M/2, w5)

H, w = pds.dtft(h, m, np.linspace(0, np.pi, 1024))

fig, ax1 = plt.subplots()
ax1.grid()

#ax2 = ax1.twinx()

ax1.plot(w/np.pi, np.abs(H), "C4")

plt.show()
