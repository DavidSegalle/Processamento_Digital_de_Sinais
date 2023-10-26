import pds
import numpy as np

x = np.array([7,5,9,3])

xe = x[:-1:2]
xo = x[1::2]

xee = xe[:-1:2]
xeo = xe[1::2]

xoe = xo[:-1:2]
xoo = xo[1::2]

Xe = np.fft.fft(xe)
Xo = np.fft.fft(xo)