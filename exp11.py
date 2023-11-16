import numpy as np
import matplotlib.pyplot as plt
import scipy.signal.windows as wndws
import pds

A = [0, 1, 0]
wl = [0.2, 0.3, 0.7, 0.78]
w = [np.pi * i for i in wl]
Dw = [np.pi *0.1,np.pi * 0.08]
d = [0.005, 0.01, 0.03]
M, beta = pds.kaiserord(-20*np.log10(min(d)), min(Dw))
m = np.arange(M+1)


hkaiser = wndws.kaiser(M+1, beta)*pds.multifaixa(A, [0.25*np.pi, 0.74*np.pi], M)
Hkaiser, W = pds.dtft(hkaiser, m, np.linspace(0, np.pi, 1048))


fig, ax1 = plt.subplots()
ax1.grid()
ax1.plot(W, np.abs(Hkaiser))

ax1.plot([0, w[0]], [d[0], d[0]])
ax1.plot([w[0], w[0]], [d[0], A[1]+d[1]])
ax1.plot([w[0], w[3]], [A[1]+d[1], A[1]+d[1]])
ax1.plot([w[3], w[3]], [A[1]+d[1], d[2]])
ax1.plot([w[3], np.pi], [d[2], d[2]])

ax1.plot([w[1], w[1]], [0, A[1]-d[1]])
ax1.plot([w[1], w[2]], [A[1]-d[1], A[1]-d[1]])
ax1.plot([w[2], w[2]], [A[1]-d[1], 0])

print(M)
print(beta)

plt.show()