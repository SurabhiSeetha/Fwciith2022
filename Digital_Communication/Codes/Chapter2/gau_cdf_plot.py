import numpy as np
import matplotlib.pyplot as plt

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


plt.plot(x.T,prob)   #plotting the CDF
plt.grid()          #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.savefig('../../Figs/Chapter2/gau_cdf_plot.pdf')
plt.savefig('../../Figs/Chapter2/gau_cdf_plot.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter2/uni_cdf.pdf"))
#else
plt.show() #opening the plot window
