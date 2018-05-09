import os
from pylab import *
rcParams.update({'font.size': 36, 'text.usetex': True})

#os.system("/home/rehnd/.local/qe-6.2.1/bin/dos.x < mote2.dos.in")

dos = genfromtxt("mote2.dos")
efermi = 2.3896

figure(figsize=(6,12))
plot(dos[:,1], dos[:,0]-efermi,lw=4)
axhline(0,color='k',linestyle=':')
xlim(0,10)
ylim(-7,5)
xlabel("EDOS")
ylabel("$E-E_f$ (eV)")
tight_layout()
show()
