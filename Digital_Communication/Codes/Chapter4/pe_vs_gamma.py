import random
import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

samples = 1000000

rng = np.random.default_rng()

X = np.asarray(random.choices([-1,1],k=samples))

N = np.random.normal(0,1,samples)

gamma_db = np.arange(0, 11)

pe=[]
theory = []

def Pe(x):
    return 0.5 - 0.5*(np.sqrt(x/(2+x)))
    
for i in gamma_db:
	gamma = 10**(0.1*i)
	A = rng.rayleigh((gamma/2)**0.5, samples) 
	Y = A + N
	pe_est = (np.count_nonzero(Y<0))
	pe.append(pe_est/samples)
	theory.append(Pe(gamma))

plt.semilogy(gamma_db,pe,'o')
plt.semilogy(gamma_db,theory)
plt.xlabel("$A_{dB}$")
plt.ylabel("$P_e(A_{dB})$")
plt.legend(['Numerical', 'Theory'])

plt.savefig('../../Figs/Chapter4/Pe_vs_gamma.pdf')
plt.savefig('../../Figs/Chapter4/Pe_vs_gamma.png')
plt.show()
