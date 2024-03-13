#!/bin/bash

# Check if conda is installed and in PATH
if ! command -v conda &> /dev/null
then
    echo "conda could not be found. Please install Anaconda or Miniconda."
    exit
fi

# Create a conda environment named 'venv'
conda create --name venv python=3.8 -y

# Activate the virtual environment
conda activate venv

# Install dependencies from requirements.txt
conda install --file requirements.txt -y

echo "Setup complete. Conda environment 'venv' created and dependencies installed."