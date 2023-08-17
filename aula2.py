import numpy as np
import matplotlib.pyplot as plt
import pds
from scipy.signal import lfilter

m = 5
n = np.arange(-3, 10)
x = pds.delta(n)
b = np.ones(m+1)/(m+1)
a = np.ones(1)
h_ref = pds.lfilter(b, a, x)
h = pds.eqdif(b, a, x)

plt.figure()
plt.stem(n, h_ref)
plt.show()
