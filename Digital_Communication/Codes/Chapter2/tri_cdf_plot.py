import numpy as np
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

x = np.linspace(-1,3,50)    #points on the x axis
simlen = int(1e6)           #number of samples
prob = []                    #declaring probability list
randvar = np.loadtxt('t.dat',dtype='double')

for i in range(50):
  count=0
  for j in randvar:
    if j < x[i]:
      count+=1
  prob.append(count/simlen)



tri_cdf = np.piecewise(x, [x < 0, ((x >= 0) & (x < 1)), ((x >= 1) & (x < 2)), x >= 2], [0, lambda x: x**2/2, lambda x: 2*x - x**2/2 - 1, 1])

plt.plot(x,prob,'o')     # plotting estimated CDF
plt.plot(x,tri_cdf) 	# plotting theoretical CDF
plt.grid()          #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

plt.savefig('../../Figs/Chapter2/tri_cdf_plot.pdf')
plt.savefig('../../Figs/Chapter2/tri_cdf_plot.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter2/uni_cdf.pdf"))
#else
plt.show() #opening the plot window
