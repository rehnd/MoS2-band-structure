#!/bin/bash 

#SBATCH --job-name=mos2-dynmat
#SBATCH --output=espresso.out
#SBATCH --error=espresso.err
#SBATCH --time=48:00:00
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --mem=4000
#SBATCH --ntasks-per-node=16

PREFIX=mos2

cp -r ../3-phonon/out .
cp -r ../3-phonon/$PREFIX.dyn .

/home/rehnd/.local/qe-6.2.1/bin/dynmat.x < $PREFIX.dynmat.in > $PREFIX.dynmat.out
