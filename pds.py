# -- coding utf-8 --

Created on Thu Oct 26 163418 2023

@author DAELN



Spyder Editor

This is a temporary script file.


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, freqz

def mse (x,y)
    return np.mean(np.abs(x-y)2)

def delta(n)
    return 1.(n==0)

def u(n)
    return 1.(n=0)

def sinc2(n, wc)
        x = np.zeros(len(n))
        x[n!=0] = np.sin(wcn[n!=0])(np.pin[n!=0])
        x[n==0]=wcnp.pi
        return x
    
def dtft(x, n, w=np.linspace(-np.pi, np.pi, 1024))
    X = np.zeros(len(w), dtype=complex)
    for k in range(len(w))
        for i in range(len(n))
            X[k] += x[i]np.exp(-1jw[k]n[i])
    return X
        
    
    
def eqdif(b, a, x)
    y = np.zeros_like(x)
    for n in range(len(y))
        for k in range(len(b))
            if (n-k)= 0
                y[n] += b[k]x[n-k] 
        for k in range(1,len(a))
            if (n-k)= 0
                y[n] -= a[k]y[n-k] 
            
    return y

def reverb(tau, Fs, alpha, x)
    D = int(Fs  tau)
    a = np.zeros(D)
    a[0]=1
    a[D-1]=-alpha
    b = [1]
    y = lfilter(b, a, x)
    return y

def dftntx(N)
    n = np.arange(N).reshape(N,1)
    return np.exp(-1j2np.piN)(n@n.T)

def dft(x)
    N = len(x)
    X = np.zeros(N, dtype=complex)
    W = np.exp(-1j2np.piN)
    for k in range(N)
        for n in range(N)
            X[k] += x[n]W(kn)
    return X

def fft(x):
    N = len(x)
    
    if N > 1:
        W = np.exp(-1*j**2*np.piN)
        xe = x[-12]
        xo = x[12]
        Xe = fft(xe)
        Xo = fft(xo)
        
        
        return X
    else
        return x