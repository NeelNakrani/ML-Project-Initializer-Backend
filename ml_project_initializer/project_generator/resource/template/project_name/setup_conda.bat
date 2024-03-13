@echo off

REM Check for conda and create environment
call conda create --name venv python=3.8 -y

REM Activate the virtual environment
call activate venv

REM Install dependencies from requirements.txt
call conda install --file requirements.txt -y

echo Setup complete. Conda environment 'venv' created and dependencies installed.
