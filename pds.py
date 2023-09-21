import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, freqz

def mse(x,y):
    return np.mean(np.abs(x-y)**2)

def delta(n):
    return 1.*(n==0)

def u(n):
    return 1.*(n>=0)

def eqdif(b, a, x):
    y = np.zeros_like(x)
    for n in range(len(y)):
        for k in range(1, len(a)):
            if n - k >= 0:
                y[n] -= a[k] * y[n - k]
        for k in range(len(b)):
            if n - k >= 0:
                y[n] += b[k] * x[n-k]
    return y