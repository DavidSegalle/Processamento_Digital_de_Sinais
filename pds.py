import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

def delta(n):
    return 1.*(n==0)

def u(n):
    return 1.*(n>=0)

def eqdif(b, a, x):
    y = np.zeros_like(x)
    for n in range(len(y)):
        pass
        #for k in :
        #    y[n] += 
    return y