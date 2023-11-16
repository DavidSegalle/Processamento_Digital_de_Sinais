import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
import math


def mse(x, y):
    return np.mean(np.abs(x - y) ** 2)


def delta(n):
    return 1.0 * (n == 0)


def u(n):
    return 1.0 * (n >= 0)


def eqdif(b, a, x):
    y = np.zeros_like(x)
    for n in range(len(y)):
        for k in range(1, len(a)):
            if n - k >= 0:
                y[n] -= a[k] * y[n - k]
        for k in range(len(b)):
            if n - k >= 0:
                y[n] += b[k] * x[n - k]
    return y


def sinc2(n, wc):
    x = np.zeros(len(n))
    x[n != 0] = np.sin(wc * n[n != 0]) / (np.pi * n[n != 0])
    x[n == 0] = wc / np.pi
    return x


def dtft(x, n, w=np.linspace(-np.pi, np.pi, 1024)):
    out = np.zeros(w.shape, dtype=complex)
    for k in range(len(w)):
        for i in range(len(n)):
            out[k] += x[i] * np.exp(-1j * w[k] * n[i])
    return out, w


def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=np.complex128)
    W = np.exp(-1j * 2 * np.pi / N)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * (W ** (k * n))
        # X[k] = complex(Fraction(X[k].real).limit_denominator(),
        # Fraction(X[k].imag).limit_denominator())
    return X


def fft(x):
    N = len(x)
    if N > 1:
        xe = x[0::2]
        xo = x[1::2]
        Xe = fft(xe)
        Xo = fft(xo)
        W = np.exp(-1j * 2 * np.pi / N)
        k = np.arange(N // 2)
        X = np.zeros(N, dtype=complex)
        X[k] = Xe + W**k * Xo
        X[k + N // 2] = Xe - W**k * Xo
        return X
    else:
        return x


def multifaixa(A, w, M):
    h = np.zeros(M + 1)
    m = np.arange(M + 1)
    k = len(A)
    for k in range(k - 1):
        h += (A[k] - A[k + 1]) * sinc2(m - M / 2, w[k])

    h += A[-1] * sinc2(m - M / 2, w[-1])

    return h


def kaiserord(A, Dw):
    if A < 21:
        beta = 0
    elif A <= 50:
        beta = 0.5842 * (A - 21) ** 0.4 + 0.07886 * (A - 21)
    else:
        beta = 0.1102 * (A - 8.7)

    M = math.ceil((A - 8) / (2.285 * Dw))
    M += M % 2

    return M, beta
