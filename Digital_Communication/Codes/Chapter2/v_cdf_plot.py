import numpy as np
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

x = np.linspace(-2,30,60)    #points on the x axis
simlen = int(1e6)           #number of samples
prob = []                    #declaring probability list
randvar = np.loadtxt('v.dat', dtype='double')

for i in range(60):
  count=0
  for j in randvar:
    if j < x[i]:
      count+=1
  prob.append(count/simlen)	



def exp_cdf(x):
	return np.piecewise(x, [x<0, x>=0], [0, lambda x: 1-np.exp(-x/2)])

plt.plot(x, prob, 'o') #plotting CDF numerical
plt.plot(x, exp_cdf(x)) #plottong CDF theory
plt.grid()
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Numerical","Theory"])


plt.savefig('../../Figs/Chapter2/v_cdf_plot.pdf')
plt.savefig('../../Figs/Chapter2/v_cdf_plot.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter2/uni_cdf.pdf"))
#else
plt.show() #opening the plot window
