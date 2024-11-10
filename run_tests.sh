#!/bin/bash

# Checking if the virtual environment exists
if [[ ! -d "venv" ]]; then
    echo "Virtual environment 'venv' not found. Creating a new one..."
    python3 -m venv .venv
else
    echo "Virtual environment 'venv' found."
fi

# Activating the virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Checking if the environment is activated
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "Failed to activate the virtual environment."
    exit 1
else
    echo "Virtual environment is activated."
fi

# Checking if the requirements.txt file exists
if [[ -f "requirements.txt" ]]; then
    echo "Checking for missing dependencies..."

    # Attempting to install dependencies if they are missing
    pip install -r requirements.txt --quiet
else
    echo "requirements.txt not found. Skipping dependency check."
fi

# Running tests with  report generation
echo "Running  tests and generating  report"
pytest --html=report/report.html

# Deactivating the virtual environment
deactivate
