from pymatgen.io.vasp.outputs import BSVasprun
from pymatgen.electronic_structure.plotter import BSPlotter
import pylab
pylab.rcParams.update({'font.size': 48, 'text.usetex': True})


bs = BSVasprun('vasprun.xml')
bst = bs.get_band_structure()

plotter = BSPlotter(bst)
plt = plotter.get_plot()
plt.ylabel("$E - E_f$ (eV)")
plt.xlabel("")
plt.tight_layout()
plt.show()
