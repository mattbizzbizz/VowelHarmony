#!/bin/bash

#SBATCH --job-name=CharRNN-training-Finnish
#SBATCH --mail-type=ALL
#SBATCH --mail-user=matabuzz@iu.edu
#SBATCH -o slurm/slurm-Finnish-%j.out
#SBATCH -t 4-00:00:00

module purge

module load PrgEnv-gnu
module load deeplearning

python train.py Finnish
