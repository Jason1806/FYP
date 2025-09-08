#!/bin/bash

# Build script for creating the executable
echo "Building AI-Powered Penetration Testing Tool..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Download NLTK data
echo "Downloading NLTK data..."
python -c "import nltk; nltk.download('punkt', quiet=True); nltk.download('stopwords', quiet=True); nltk.download('wordnet', quiet=True)"

# Run tests (if available)
echo "Running basic functionality test..."
python -c "from pentestool.main import main; print('Import successful!')"

# Build executable
echo "Building executable with PyInstaller..."
pyinstaller pentestool.spec

# Check if build was successful
if [ -f "dist/PenTestTool" ]; then
    echo "Build successful! Executable created at dist/PenTestTool"
    echo "You can run the tool with: ./dist/PenTestTool --help"
else
    echo "Build failed. Please check the error messages above."
fi

echo "Done!"