#!/bin/bash

echo "Starting application..."

# Check if app.py exists
if [ ! -f app.py ]; then
    echo "Error: app.py not found!"
    exit 1
fi

# Run the application
python3 app.py
