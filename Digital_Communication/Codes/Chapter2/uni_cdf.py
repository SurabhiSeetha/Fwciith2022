import numpy as np
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

x = np.linspace(-3,3,30)    #points on the x axis
simlen = int(1e6)           #number of samples
prob = []                    #declaring probability list
randvar = np.loadtxt('uni.dat', dtype='double')

for i in range(30):
	count=0
	for j in randvar:
		if j < x[i]:
			count+=1
	prob.append(count/simlen)

#for i in range(0,30):
	#err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	#err_n = np.size(err_ind) #computing the probability
	#err.append(err_n/simlen) #storing the probability values in a list

	
plt.plot(x,prob)   #plotting the CDF
plt.grid()          #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.savefig('../../Figs/Chapter2/uni_cdf.pdf')
plt.savefig('../../Figs/Chapter2/uni_cdf.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter2/uni_cdf.pdf"))
#else
plt.show() #opening the plot window



