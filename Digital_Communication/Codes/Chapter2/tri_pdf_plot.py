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

pdf = np.gradient(prob, x, edge_order=2)

tri_pdf = np.piecewise(x, [x < 0, ((x >= 0) & (x < 1)), ((x >= 1) & (x < 2)), x >= 2], [0, lambda x: x, lambda x: 2-x, 0])

  
plt.plot(x,pdf,'o')             # plotting estimated PDF
plt.plot(x,tri_pdf)    # plotting theoretical PDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.savefig('../../Figs/Chapter2/tri_pdf_plot.pdf')
plt.savefig('../../Figs/Chapter2/tri_pdf_plot.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter2/uni_cdf.pdf"))
#else
plt.show() #opening the plot window
