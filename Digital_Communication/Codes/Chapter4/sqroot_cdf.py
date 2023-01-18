import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux
#import subprocess
#import shlex
#end if



x = np.linspace(0,10,40)    #points on the x axis
samples = int(1e6)           #number of samples
prob = []                    #declaring probability list
pdf=[]
X1 = np.random.normal(0, 1, samples)
X2 = np.random.normal(0, 1, samples)
V = np.sqrt(X1**2 + X2**2)

for i in range(40):
  count=0
  for j in V:
    if j < x[i]:
      count+=1
  prob.append(count/samples)
pdf = np.gradient(prob, x, edge_order=2)

def rayleigh_cdf(x):
	return np.piecewise(x, [x<0, x>=0], [0, lambda x: 1-np.exp(-x**2/2)])

	
plt.plot(x,prob)             # plotting estimated cdf
plt.plot(x, rayleigh_cdf(x),'o') #plotting CDF theory
plt.grid()          #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

plt.savefig('../../Figs/Chapter4/rayleigh_cdf.pdf')
plt.savefig('../../Figs/Chapter4/rayleigh_cdf.png')

plt.show()
