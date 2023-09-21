import numpy as np
import matplotlib.pyplot as plt
import pds

def Ha(w, beta=.2, alpha=.8):
    return beta/(1-alpha*np.exp(-1j*w))

plt.figure(1)
beta = 0.2
alpha = 0.8

W = np.linspace(-np.pi, np.pi, 1024)

#plt.figure(1)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(W, np.abs(Ha(W)), 'tab:blue')
ax2.plot(W, np.angle(Ha(W)), 'black')

ax1.grid(True, axis='both')

a = [1, -alpha]
b = [beta]
w, Hn = pds.freqz(b, a, W, whole=True)

#plt.figure(2)
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

ax1.plot(w, np.abs(Hn), 'tab:blue')
ax2.plot(w, np.angle(Hn), 'black')
ax1.grid(True, axis='both')
plt.show()
