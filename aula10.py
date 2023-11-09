import numpy as np
import matplotlib.pyplot as plt
import pds

wc = np.pi/2
M = 10
m = np.arange(M+1)
h10 = pds.sinc2(m-M/2, wc)
H10, w = pds.dtft(h10, m)

#plt.figure(1)
fig, ax1 = plt.subplots()

ax1.plot(w, np.abs(H10), "C0")
#ax1.set_ylabel(color = "C0")

#plt.stem(m, h10)

ax2 = ax1.twinx()
ax2.plot(w, np.unwrap(np.angle(H10)), "C1")

plt.show()