import pds
import numpy as np
import matplotlib.pyplot as plt

N = 4
n = np.arange(N)
x = n

W = pds.dftxmtx(N)
X = W@x

np.set_printoptions(precision=3, suppress=True)

xinv = (1/N)*np.conj(W)@X

print(xinv)

N = 12

np.arange(N)
x = 1 + 4*np.cos(np.pi/3*n) + np.sin(5*np.pi/6*n)

W = pds.dftmtx(N)
X = W@x

print(X)