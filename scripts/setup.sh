#!/bin/bash

echo "Starting project setup..."

# Check if Python 3 is installed
if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: Python 3 is not installed."
    exit 1
fi

echo "Python 3 is installed."

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "Setup completed successfully!"
