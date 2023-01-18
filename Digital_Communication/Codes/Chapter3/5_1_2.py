import random
import numpy as np

samples = 1000000

X = np.asarray(random.choices([-1,1],k=samples))
print(X)

N = np.random.normal(0,1,samples)
print(N)

A_db=5 
A=10**(0.1*A_db)
Y = A*X + N
print(Y)
