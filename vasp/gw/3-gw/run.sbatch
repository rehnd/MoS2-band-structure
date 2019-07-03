#!/bin/bash 

#SBATCH --job-name=mos2
#SBATCH --output=vasp.out
#SBATCH --error=vasp.err
#SBATCH --time=48:00:00
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --mem=64000
#SBATCH --ntasks-per-node=16

cp ../2-diag/WAVECAR .
cp ../2-diag/WAVEDER .

mpirun -np 16 /home/rehnd/.local/vasp-5.3.5+wannier90/src/vasp.5.3/vasp
