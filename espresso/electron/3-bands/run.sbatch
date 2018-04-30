#!/bin/bash 

#SBATCH --job-name=MoS2-2H.bands
#SBATCH --output=bands.out
#SBATCH --error=bands.err
#SBATCH --time=1:00:00
#SBATCH --qos=normal
#SBATCH --nodes=2
#SBATCH --mem=4000
#SBATCH --ntasks-per-node=16

QE=/home/rehnd/.local/espresso-5.2.0/bin

SYST=MoS2-2H
TYPE=bands
CALC=pw

mpirun -np 32 $QE/$CALC.x < $SYST.$TYPE.$CALC.in > $SYST.$TYPE.$CALC.out

