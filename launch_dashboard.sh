#!/bin/bash

echo "=========================================="
echo "  Mobility-AI Dashboard Launcher"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python3 found"

# Check if merged_clean.csv exists
if [ ! -f "merged_clean.csv" ]; then
    echo "❌ Error: merged_clean.csv not found in current directory"
    echo "   Please ensure the data file is present."
    exit 1
fi

echo "✓ Data file found"

# Check if requirements are installed
echo ""
echo "Checking dependencies..."
pip3 show dash > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "⚠️  Dependencies not found. Installing..."
    pip3 install -r requirements.txt
else
    echo "✓ Dependencies installed"
fi

echo ""
echo "=========================================="
echo "🚀 Launching Dashboard..."
echo "=========================================="
echo ""
echo "The dashboard will open at:"
echo "   http://127.0.0.1:8050/"
echo ""
echo "Press CTRL+C to stop the server"
echo ""

# Launch the dashboard
python3 interactive_dashboard.py

