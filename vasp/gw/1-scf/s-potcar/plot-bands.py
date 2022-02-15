from pylab import *
import subprocess as sp
import os
rcParams.update({'font.size':48, 'text.usetex': True})


def getEfermi():
    efermi = []
    folder = '.'
    f = open(folder + '/vasprun.xml', 'r')
    while True:
        line = f.readline()
        if "efermi" in line:
            efermi.append(line.split()[2])
            break
    return array(list(map(float,efermi)))

def getnbands():
    output = sp.Popen(["grep NBANDS vasprun.xml | head -n 1 | awk '{print $4}'"],shell=True,stdout=sp.PIPE).communicate()[0].decode()
    nbands = int(str(output).split('<')[0])
    return nbands

def getbandpoints(xmax):
    G = array([0,0,0])
    M = array([0.5,0,0])
    K = array([1./3,1./3,0])
    GG = 0
    GM = norm(M-G)
    MK = norm(K-M) + GM
    KG = norm(G-K) + MK
    return array([GG, GM/KG*xmax, MK/KG*xmax, KG/KG*xmax])
    
if __name__ == '__main__':
    efermi = getEfermi()
    nbands = getnbands()
    print('Found nbands = ', nbands)
    print('E_f = ', efermi[0], ' eV')

    bands = genfromtxt('wannier90_band.dat')
    n = shape(bands)[0]
    nx = int(n/nbands)

    be = bands[:,1].reshape((nbands,nx))
    bk = bands[:,0].reshape((nbands,nx))

    xmax = max(bk[0,:])
    gmk = getbandpoints(xmax)
    gmk = (0.00000, 1.01936, 1.60782,2.78476)

    ec = amin(be[26,:])
    ev = amax(be[25,:])
    print('Ec-Ev = ', ec-ev, ' eV')
    
    elow = be[0,0]
    elowvar = amax(be[0,:]) - amin(be[0,:])
    print('elow=', elow, ' eV with width = ', elowvar, ' eV')
    print('ev-elow=',ev-elow)
    print('ec-elow=',ec-elow)
    
    figure(figsize=(12,10))
    for i in range(nbands):
        plot(bk[i,:],be[i,:],color='k')
        
    axhline(ec,color='r',lw=2)
    axhline(ev,color='g',lw=2)
    axhline(efermi,color='b',lw=1)
    xlim(0,xmax)
    #ylim(-5,5)
    for kp in gmk:
        axvline(kp, color='k',lw=1)

    xticks(gmk, ['$\Gamma$', '$\mathrm{M}$', '$\mathrm{K}$', '$\Gamma$'])
    ylabel('Energy (eV)')
    tight_layout()
    show()
