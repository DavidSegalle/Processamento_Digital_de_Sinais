# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:00:44 2023

@author: DAELN
"""
import matplotlib.pyplot as plt
import numpy as np
import pds

#media movel
M=5
n=np.arange(-3,10)
x = pds.delta(n)
b = np.ones(M+1)/(M+1)
a = np.ones(1)
h_ref = pds.lfilter(b,a,x)
h = pds.eqdif(b,a,x)
plt.figure(1)
plt.stem(n, h_ref)
print(pds.mse(h_ref, h))

#sistema IIR
b = np.ones(1)
a = np.array([1,.5])
n=np.arange(-3,10)
x = pds.delta(n)
h_ref = pds.lfilter(b,a,x)
h = pds.eqdif(b,a,x)
plt.figure(2)
plt.stem(n, h_ref)
print(pds.mse(h_ref, h))

plt.show()
