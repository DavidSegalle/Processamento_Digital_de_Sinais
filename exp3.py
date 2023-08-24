# Eco simples, y[n] = x[n] + ax[n - D]

# Múltiplos ecos y[n] = x[n] + ax[n - D] + a²x[n-2D]...
# mas ay[n-D] = ax[n-D] + a²x[n-2D]...

# Subtraindo as 2ª e 3ª equações y[n] = ay[n-D] + x[n]

# Sistema IIR
# Utilizar a função lfilter()
import numpy as np
import matplotlib.pyplot as plt
import pds
from scipy import signal
import sounddevice as sd

x = np.load("123test.npy")

fs = 8192
alpha = 0.7
tau = 0.005

d = round(tau * fs)

b = np.array([1])
a = np.zeros(d)
a[-1] = alpha
a[0] = 1

y = signal.lfilter(b, a, x)

sd.play(y, fs, blocking=True)
