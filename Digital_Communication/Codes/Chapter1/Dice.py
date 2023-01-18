from random import randint
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

# Roll the two dice how many times?
samples = 10000

# Create a dictionary to store the results
results = defaultdict(int)

# Loop n times
for _ in range(samples):
    # Get random numbers for the two dice
    die_1 = randint(1, 6)
    die_2 = randint(1, 6)
    # Increase the corresponding result by 1
    results[die_1 + die_2] += 1
    
print(results)

# Print results

for i in results:
    results[i] = results[i]/samples
    
print(results)

plt.stem(results.keys(), results.values(), markerfmt='o', use_line_collection=True, label='Simulation')

n = range(2,13)
n1 = range(2,8)
n2 = range(8,13)
panal1 = (n1 -np.ones((1,6)))
panal2 = (13*np.ones((1,5))-n2)
panal = np.concatenate((panal1,panal2),axis=None)/36
plt.stem(n,panal, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.legend()

plt.savefig('../../Figs/Chapter1/dice.pdf')
plt.savefig('../../Figs/Chapter1/dice.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter2/uni_cdf.pdf"))
#else
plt.show() #opening the plot window



