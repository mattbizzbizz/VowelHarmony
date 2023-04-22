#!/bin/bash

#SBATCH --job-name=CharRNN-training-Chukchi
#SBATCH --mail-type=ALL
#SBATCH --mail-user=matabuzz@iu.edu
#SBATCH -o slurm/slurm-Chukchi-%j.out
#SBATCH -t 4-00:00:00

module purge

module load PrgEnv-gnu
module load deeplearning

python train.py Chukchi
