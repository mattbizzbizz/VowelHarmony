#!/bin/bash

#SBATCH --job-name=CharRNN-training-Turkish
#SBATCH --mail-type=ALL
#SBATCH --mail-user=matabuzz@iu.edu
#SBATCH -o slurm/slurm-Turkish-%j.out
#SBATCH -t 4-00:00:00

module purge

module load PrgEnv-gnu
module load deeplearning

python train.py Turkish
