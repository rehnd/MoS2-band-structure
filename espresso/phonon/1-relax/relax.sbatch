#!/bin/bash 

#SBATCH --job-name=mos2-relax
#SBATCH --output=espresso.out
#SBATCH --error=espresso.err
#SBATCH --time=48:00:00
#SBATCH --qos=normal
#SBATCH --nodes=8
#SBATCH --mem=64000
#SBATCH --ntasks-per-node=16

PREFIX=mos2

#rm -rf *out
mpirun -np 128 /home/rehnd/.local/qe-6.2.1/bin/pw.x < $PREFIX.pw.in > $PREFIX.pw.out
