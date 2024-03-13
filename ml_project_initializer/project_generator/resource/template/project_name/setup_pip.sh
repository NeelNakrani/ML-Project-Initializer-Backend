#!/bin/bash

# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

echo "Setup complete. Virtual environment 'venv' created and dependencies installed."