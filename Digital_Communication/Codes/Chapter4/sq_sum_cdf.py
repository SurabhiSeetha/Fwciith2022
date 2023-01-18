import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux
#import subprocess
#import shlex
#end if



x = np.linspace(0,15,60)    #points on the x axis
samples = int(1e6)           #number of samples
prob = []                    #declaring probability list
pdf=[]
X1 = np.random.normal(0, 1, samples)
X2 = np.random.normal(0, 1, samples)
V = X1**2 + X2**2

for i in range(60):
  count=0
  for j in V:
    if j < x[i]:
      count+=1
  prob.append(count/samples)

pdf = np.gradient(prob, x, edge_order=2)

def chi_cdf(x):
  return 1-np.exp(-(x)/2)

vec_chi=scipy.vectorize(chi_cdf)	

plt.plot(x,prob)   #plotting the CDF
plt.plot(x,vec_chi(x),'o',label='Theory')
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_V(x)$')
plt.legend(['simulated' , 'Theory'])

plt.savefig('../../Figs/Chapter4/chisq_cdf.pdf')
plt.savefig('../../Figs/Chapter4/chisq_cdf.png')

plt.show()

