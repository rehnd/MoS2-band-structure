#!/bin/bash 

#SBATCH --job-name=mos2
#SBATCH --output=vasp.out
#SBATCH --error=vasp.err
#SBATCH --time=2:00:00
#SBATCH --qos=normal
#SBATCH --nodes=2
#SBATCH --mem=64000
#SBATCH --ntasks-per-node=16

mpirun -np 16 vasp
