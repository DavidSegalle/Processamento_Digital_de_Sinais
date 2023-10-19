import numpy as np 
import sounddevice as sd
import pds

y = np.load("123test_noisy.npy")
fs = 8192 # Hz

sd.play(y, fs, blocking=True)

r = .99

f1 = 500
f2 = 3000

b1 = 
b2 = 

a1 = 
a2 = 

x1 = pds.lfilter(b1, a1, y)


x2 = pds.lfilter(b1, a1, x1)