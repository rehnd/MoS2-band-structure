from pylab import *
rcParams.update({'font.size': 48, 'text.usetex': True})

f = open('DOSCAR')
ef = float(f.readlines()[5].split()[3])
f.close()

dos = genfromtxt('DOSCAR', skip_header=6)

f=figure(figsize=(14,12))
plot(dos[:,0]-ef,dos[:,1])
axhline(0,color='k',linewidth=2)
axvline(0,color='k',linewidth=1)
ylabel('DOS (states/eV/cell)')
xlabel("Energy (eV)")
#savefig('edos_mote2.png', bbox_inches='tight', dpi=200)
tight_layout()
show()
