from pylab import *
rcParams.update({'font.size': 48, 'text.usetex': True})

f = open('DOSCAR')
ef = float(f.readlines()[5].split()[3])
f.close()

dos = genfromtxt('DOSCAR', skip_header=6)

f=figure(figsize=(8,12))
plot(dos[:,1],dos[:,0]-ef)
axhline(0,color='k',linewidth=2)
ylim(-5,3)
#xlim(0,0.03)
xlabel('EDOS')
ylabel("Energy (eV)")
#savefig('edos_mote2.png', bbox_inches='tight', dpi=200)
tight_layout()
show()
