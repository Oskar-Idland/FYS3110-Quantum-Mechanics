import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp


def eq(z, β, K):
    return np.cos(z) + β*np.sin(z)/z - np.cos(K)

def E(β, K, n):
    z0 = (n-0.5)*np.pi + β/((n-0.5)*np.pi)
    z = sp.optimize.newton(eq, z0, None, (β, K), 1e-6, 20)
    return z*z


ℏ = 1
N = 100
L = 1
a = L/N
α = 1
m = 1
β = m*a*α/ℏ**2



l = np.arange(1,N,1)


Energy = []
Ks = np.arange(0,N,1)





# 8.5 )
n = np.arange(1,8,1)
E_n = [1,1,4/3, 6/4, 8/5, 10/6, 13/7]
plt.scatter(n, E_n)
plt.plot(n, E_n)
plt.xlabel('n')
plt.ylabel(r'$E_n / n$')
plt.savefig('8.5.pdf')
plt.show()