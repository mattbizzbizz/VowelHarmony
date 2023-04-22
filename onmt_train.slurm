#!/bin/bash

#SBATCH --job-name=onmt-training-test
#SBATCH --mail-type=ALL
#SBATCH --mail-user=matabuzz@iu.edu
#SBATCH -o onmt-%j.out
#SBATCH -t 4-00:00:00
#SBATCH -A general
#SBATCH -p gpu
#SBATCH --gpus-per-node 1

module purge

module load PrgEnv-gnu
module load deeplearning

onmt_train -config toy_en_de.yaml
