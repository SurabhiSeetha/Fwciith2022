import random
import numpy as np

samples = 1000000

x = random.choices([-1,1],k=samples)

unique, counts = np.unique(x, return_counts=True)

print(unique)
print(counts)

psim = counts/samples

print(psim)
