import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

def gaussian_function(x, mean, stdev):
    return np.exp(-(x-mean)**2/(2*stdev**2))/(stdev*np.sqrt(2*np.pi))

p = 0.25
A_db = 4
A = 10**(0.1*A_db)
delta = np.log((1-p)/p)/(2*A)
x = np.linspace(-A-4, A+4, 100)
y_x0 = p*gaussian_function(x, A, 1)
y_x1 = (1-p)*gaussian_function(x, -A, 1)

plt.plot(x, y_x0, color='red')
plt.plot(x, y_x1, color = 'blue')
plt.vlines(delta, np.min(y_x1), np.max(y_x1), colors=['green'])
plt.grid()
plt.xlabel("$y$")
plt.ylabel("$P_X(x)P_Y(y|x)$")
plt.legend(['$pP_Y(y|x=1)$', '$(1-p)P_Y(y|x=-1)$', "$y=\\frac{1}{2A}\ln\left(\\frac{1}{p}-1\\right)$"])


plt.savefig('../../Figs/Chapter3/bpsk_map.pdf')
plt.savefig('../../Figs/Chapter3/bpsk_map.png')

plt.show()
