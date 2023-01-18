import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

#if using termux
#import subprocess
#import shlex
#end if


A = 5
s0 = np.array([1,0]).reshape(2,1)
s1 = np.array([0,1]).reshape(2,1)


samples = 100
N = np.random.normal(size=(2, samples))


Ys0 = A*s0 + N
Ys1 = A*s1 + N

# Condition is x^ = s0 if y>x, x^ = s1 if y<x
plt.scatter(Ys0[0], Ys0[1])
plt.scatter(Ys1[0], Ys1[1],color='red')
plt.plot(np.linspace(-1, A+1, 100), np.linspace(-1, A+1, 100), color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(["$y|s_0$","$y|s_1$"])
plt.grid()

plt.savefig('../../Figs/Chapter5/bfsk_scatter.pdf')
plt.savefig('../../Figs/Chapter5/bfsk_scatter.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter5/biv_scatter.pdf"))
#else
plt.show() #opening the plot window
