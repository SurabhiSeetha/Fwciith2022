import random
import numpy as np
import matplotlib.pyplot as plt

samples = 1000

X = np.asarray(random.choices([-1,1],k=samples))

N = np.random.normal(0,1,samples)

A_db=5 
A=10**(0.1*A_db)

Y = A*X + N

y0 = np.extract(X==-1, Y)
y1 = np.extract(X==1, Y)

plt.scatter(np.zeros(len(y0)), y0)
plt.scatter(np.zeros(len(y1)), y1)
plt.plot(np.linspace(-0.1,0.1,10),np.zeros(10),  color="red")
plt.grid()
plt.legend(["$y|0$","$y|1$"])


plt.savefig('../../Figs/Chapter3/bpsk_scatter.pdf')
plt.savefig('../../Figs/Chapter3/bpsk_scatter.png')


plt.show()
