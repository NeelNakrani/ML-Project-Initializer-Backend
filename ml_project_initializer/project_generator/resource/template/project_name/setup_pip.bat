@echo off

python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

echo Setup complete. Virtual environment 'venv' created and dependencies installed.
