import numpy as np
import matplotlib.pyplot as plt
import scipy.signal.windows as wndws
import pds

wp = .25*np.pi
ws = .35*np.pi
wc = (wp+ws)/2

Ap = .1
As = 50

dp = (10**(Ap/20) - 1)/(10**(Ap/20)+1)
ds = 10**(-As/20)

M = 66
m = np.arange(M+1)
hhamming = wndws.hamming(M+1)*pds.sinc2(m-M/2,wc)

Hhamming, w = pds.dtft(hhamming, m, np.linspace(0, np.pi, 1024))

M = 60
beta = 4.53
m = np.arange(M+1)
hkaiser = wndws.kaiser(M+1, beta)* pds.sinc2(m-M/2, wc)
Hkaiser, w = pds.dtft(hkaiser, m, np.linspace(0, np.pi, 1024))

fig, ax1 = plt.subplots()
ax1.grid()
ax1.plot(w, np.abs(Hhamming), w, np.abs(Hkaiser))

ax1.plot([wp, wp], [0, 1-dp])
ax1.plot([0, wp], [1+dp, 1+dp])
ax1.plot([0, wp], [1-dp, 1-dp])

ax1.plot([ws, ws], [ds, 1])
ax1.plot([ws, np.pi], [ds, ds])

plt.show()