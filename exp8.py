import numpy as np
import matplotlib.pyplot as plt
import pds

N = 6
n = np.arange(-20,20)
K = 20
k = np.arange(K)
N1 = 64
n1 = np.arange(0, N1)
k1 = np.arange(0, N1)
w1 =(2*np.pi/N)
w2 = (2*np.pi/9)
w3 = (4*np.pi/7)
#PG19
x0=np.cos(w1*n)
xzero = np.cos(w2*n1) + (3/4)*np.cos(w3*n1)
xum = pds.u(n1) - pds.u(np.arange(-32, 32))
xconv = xzero*xum
plt.figure(1)
plt.stem(n, x0)

X0 = pds.dtft(x0, n, w=np.linspace(-np.pi, np.pi, 40))
plt.figure(2)
plt.stem(n/20*np.pi, np.abs(X0)/N)

n = np.arange(-20, 20)
x1 = pds.u(n+10) - pds.u(n-10)
plt.figure(3)
plt.stem(n, x1)

X1 = pds.dtft(x1, n, w=np.linspace(-np.pi, np.pi, 1024))
plt.figure(4)
plt.plot((X1))

#PG20
x2=x0*x1
plt.figure(5)
plt.stem(n, x2)

X2 = pds.dtft(x2, n, w=np.linspace(-np.pi, np.pi, 1024))
plt.figure(6)
plt.plot((X2))

x3 = np.pad(x2, (0), mode='constant')
x3[x3==0]=np.nan
plt.figure(7)
plt.stem(n, x3)


x4s = pds.dtft(x2, np.arange(-20,20), np.linspace(-np.pi,np.pi,20))
x4cont = pds.dtft(x2, np.arange(-20,20))
plt.figure(8)
plt.stem(np.linspace(-np.pi,np.pi,20), x4s)
plt.plot(np.linspace(-np.pi,np.pi,1024), x4cont, '--')


#PG28
X5 = pds.dft(xconv)
plt.figure(9)
plt.stem(k1, np.abs(X5))
plt.show()