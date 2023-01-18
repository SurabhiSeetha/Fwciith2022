import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

#if using termux
#import subprocess
#import shlex
#end if


samples = 1000000

s0 = np.array([1,0]).reshape(2,1)

max_snr = 10
snr_db = np.arange(0, max_snr+1)

pe_est = np.zeros(len(snr_db))
pe_theory = np.zeros(len(snr_db))
for i in snr_db:
    N = np.random.normal(size=(2, samples))
    snr = 10**(0.1*i)
    Y = snr*s0 + N
    pe_val = np.count_nonzero(np.where(Y[0] < Y[1], 1, 0))
    pe_est[i] = pe_val/samples
    pe_theory[i] = 0.5*sp.erfc(snr/2)


plt.scatter(snr_db, pe_est,color='red')
plt.semilogy(snr_db, pe_theory)

plt.xlabel('$SNR_{dB}$')
plt.ylabel('$P_e(SNR_{dB})$')
plt.legend(["Numerical","Theory"])

plt.savefig('../../Figs/Chapter5/pe_vs_snr.pdf')
plt.savefig('../../Figs/Chapter5/pe_vs_snr.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter5/biv_pe_vs_snr.pdf"))
#else
plt.show() #opening the plot window
