import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux
#import subprocess
#import shlex
#end if

x = np.linspace(-3,3,30)    #points on the x axis
simlen = int(1e6)           #number of samples
prob = []                    #declaring probability list
randvar = np.loadtxt('gau.dat', dtype='double')

for i in range(30):
  count=0
  for j in randvar:
    if j < x[i]:
      count+=1
  prob.append(count/simlen)

pdf = np.gradient(prob, x, edge_order=2)

def gauss_pdf(x):
  return 1/np.sqrt(2*np.pi)*np.exp(-x**2/2.0)

vec_gauss_pdf = scipy.vectorize(gauss_pdf)


plt.plot(x,pdf,'o')             # plotting estimated PDF
plt.plot(x,vec_gauss_pdf(x))    # plotting theoretical PDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.savefig('../../Figs/Chapter2/gau_pdf_plot.pdf')
plt.savefig('../../Figs/Chapter2/gau_pdf_plot.png')

plt.show()
