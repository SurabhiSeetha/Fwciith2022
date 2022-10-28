from sympy import*

import cvxpy as cp
import sympy as sy
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math
import mpmath as mp


#if using termux
import subprocess
import shlex
#end if

print("Verification Using Differentiation")

r = symbols ('r',real=True)
R = symbols ('R',real=True)
pi = symbols ('pi',real=True)
h = symbols ('h',real=True)

h = 2 * sy.sqrt(R**2 - r**2)
v = (2 * pi * ( r**2) * (sy.sqrt(R**2 - r**2)))

print("h =",h)
print("v =",v)

df = diff(v, r)

print("dV/dr:")
print(df)

sol = sy.solve(df,r,real=True)[2]

print("when dv/dr = 0, r is")

print(sol)

height = sy.simplify(h.subs(r,sol))

print("When height is equal to")
print(height)

volume = pi * height * R**2 - ( pi * height**3 /4)
print("we get the Maximum volume possible which is")
print(sy.simplify(volume))

print("Verification Using DGP cvxpy")

#Declaring Variables
h = cp.Variable(pos=True, name="h")
r = cp.Variable(pos=True, name="r")

#R = int(input("Enter R:"))
R = 4

#Computing surface area
V = 2* np.pi*(r**2)*h

constraints = [
        h == 2*R/ math.sqrt(3),
        r == R*math.sqrt(2/3)
]

#Problem Formulation
problem = cp.Problem(cp.Maximize(V), constraints)

#Checking cuvature of the objective function
print(V.log_log_curvature)

#Checking if the problem is DGP
print("Is this problem DGP?", problem.is_dgp())


#solution
problem.solve(gp=True)
print("Max Volume is:",problem.value,"h =", h.value,"r =", r.value)

#plt.savefig('/sdcard/Download/optadvfig.pdf')
#subprocess.run(shlex.split("termux-open '/sdcard/Download/optadvfig.pdf'"))

