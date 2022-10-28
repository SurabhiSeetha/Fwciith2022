import random as rd
  2 import numpy as np
  3 import matplotlib.pyplot as plt
  4
  5 #if using termux
  6 import subprocess
  7 import shlex
  8 #end if
  9
 10
 11 x1 = np.linspace(-8,10,100)
 12 y1 = 1 / (x1 - 3)
 13 plt.plot(x1,y1, color="Blue")
 14 plt.grid() # minor
 15 plt.show()
 16
 17
 18 #plt.savefig('/sdcard/Download/conicfig.pdf')
 19 #subprocess.run(shlex.split("termux-open '/sdcard/Do    wnload/conicfig.pdf'"))
