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

def chi_pdf(x):
	return np.exp(-x/2)/2
	
vec_chi_pdf = scipy.vectorize(chi_pdf)
	
plt.plot(x,pdf,label='simulated')             # plotting estimated PDF
plt.plot(x,vec_chi_pdf(x),'o',label='Theory')#plotting the PDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_V(x_i)$')
plt.legend(["Numerical","Theory"])

plt.savefig('../../Figs/Chapter4/chisq_pdf.pdf')
plt.savefig('../../Figs/Chapter4/chisq_pdf.png')

plt.show()
