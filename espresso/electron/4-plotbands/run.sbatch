#!/bin/bash

# Note: this calculation can be run in serial and does not require SLURM (sbatch)

QE=/home/rehnd/.local/espresso-5.2.0/bin

SYST=MoS2-2H
TYPE=bands
CALC=bands

$QE/$CALC.x < $SYST.$TYPE.$CALC.in > $SYST.$TYPE.$CALC.out
