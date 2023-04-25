#!/bin/bash

#SBATCH --job-name=onmt-training
#SBATCH --mail-type=ALL
#SBATCH --mail-user=matabuzz@iu.edu
#SBATCH -o onmt-%j.out
#SBATCH -t 2-00:00:00
#SBATCH -A general
#SBATCH -p gpu
#SBATCH --gpus-per-node=1
#SBATCH --nodes=1

module purge

module load PrgEnv-gnu
module load deeplearning/2.12.0

onmt_train -config turkish.yaml
#onmt_train -config finnish.yaml
#onmt_train -config chukchi.yaml
