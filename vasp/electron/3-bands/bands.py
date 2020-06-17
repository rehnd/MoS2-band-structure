from pylab import *


def getbands(fname):
    efermi = 0
    nbands = 0
    nelect = 0
    nspin  = 0
    f = open(fname,'r')

    spts = []
    kpts = []
    evals = []
    reclat = []
    i = 0
    while True:
        line = f.readline()
        if "efermi" in line:
            efermi = float(line.split()[2])
        if '"NBANDS"' in line:
            nbands = int(line.split()[3].split('<')[0])
        if '"NELECT"' in line:
            nelect = int(float(line.split()[2].split('<')[0]))
        if '"ISPIN"' in line:
            nspin = int(line.split()[3].split('<')[0])

        if '<i name="divisions" type="int">' in line:
            while True:
                nextline = f.readline()
                if not "</generation>" in nextline:
                    spts.append(array([float(k) for k in nextline.split()[1:4]]))
                else:
                    break
        if '<varray name="rec_basis" >' in line:
            while True:
                nextline = f.readline()
                if not "</varray>" in nextline:
                    reclat.append(array([float(k) for k in nextline.split()[1:4]]))
                else:
                    break

                
        if '<varray name="kpointlist"' in line:
            while True:
                nextline = f.readline()
                if not "</varray>" in nextline:
                    kpts.append(array([float(k) for k in nextline.split()[1:4]]))
                else:
                    break

        if '<set comment="kpoint' in line:
            evs = []
            while True:
                nextline = f.readline()
                if not "</set>" in nextline:
                    evs.append(float(nextline.split()[1]))
                else:
                    break
            evals.append(evs)
        if not line:
            break

    reclat = array(reclat)
    spts = matmul(array(spts),transpose(reclat))
    kspt = zeros(len(spts[:,0]))

    for i in range(1,len(kspt)):
        kspt[i] = kspt[i-1] + norm(spts[i,:]-spts[i-1,:])

    kpts = matmul(array(kpts),transpose(reclat))
    kx = zeros(len(kpts[:,0]))
    for i in range(1,len(kx)):
        dk = norm(kpts[i,:]-kpts[i-1,:])
        if dk < 0.2:
            kx[i] = kx[i-1] + dk
        else:
            kx[i] = kx[i-1] + 0.01

    evals = array(evals)

    return efermi, nbands, nelect, nspin, kspt, kx, evals
    

def getEgap(nelect, nspin, evals):
    if nspin == 1:
        nelect /= 2
    nelect = int(nelect)
    ev = max(evals[:,nelect-1])
    ec = min(evals[:,nelect])
    egap = ec - ev
    
    return egap, ev, ec


if __name__ == '__main__':

    efermi, nbands, nelect, nspin, kspt, kx, evals = getbands('vasprun.xml')

    egap, ev, ec = getEgap(nelect, nspin, evals)
    print('Found E_gap = %05.3f eV'%egap)

    figure()
    for k in kspt:
        axvline(k, lw=1, color='k')
    for i in range(nbands):
        plot(kx, evals[:,i]-efermi,color='k')

    axhline(0, lw=1, color='k')
    axhline(ec-efermi, lw=1, color='r')
    axhline(ev-efermi, lw=1, color='g')
    ylim(-5,5)
    xlim(0,kx[-1])
    ylabel('$E - E_f$ (eV)')
    tight_layout()
    show()
