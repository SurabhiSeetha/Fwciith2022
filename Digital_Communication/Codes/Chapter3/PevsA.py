import random
import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

def pe(x):
    return 0.5*sp.erfc(x/np.sqrt(2))

samples = 1000000

X = np.asarray(random.choices([-1,1],k=samples))

N = np.random.normal(0,1,samples)

A_db = np.arange(0, 11)

err=[]
Pe=[]
for i in A_db:
	A = 10**(0.1*i)
	Y = A*X+N
	pe_est = (np.count_nonzero((X == 1) & (Y < 0)) + np.count_nonzero((X == -1) & (Y > 0)))
	err.append(pe_est/samples)
	Pe.append(pe(A))

plt.semilogy(A_db, err,'o')
plt.semilogy(A_db, Pe,)
plt.grid()
plt.xlabel("$A_{dB}$")
plt.ylabel("$P_e(A_{dB})$")
plt.legend(['Numerical', 'Theory'])

plt.savefig('../../Figs/Chapter3/Pe_vs_A.pdf')
plt.savefig('../../Figs/Chapter3/Pe_vs_A.png')
plt.show()
