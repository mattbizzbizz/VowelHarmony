#!/bin/bash

#SBATCH --job-name=CharRNN-test
#SBATCH --mail-type=ALL
#SBATCH --mail-user=matabuzz@iu.edu
#SBATCH -o slurm/slurm-%j.out
#SBATCH -t 4-00:00:00

module purge

module load PrgEnv-gnu
module load deeplearning

python test.py Turkish
python test.py Finnish
python test.py Chukchi
