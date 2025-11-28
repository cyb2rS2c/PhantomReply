#!/bin/bash
set -e

if [ ! -d "myvenv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv myvenv
fi

echo "Activating virtual environment..."
source myvenv/bin/activate

if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
fi

echo "Running phantomreply.py..."
clear
python3 src/phantomreply.py
