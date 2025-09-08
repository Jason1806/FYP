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

# Upgrade pip first
echo "Upgrading pip..."
pip install --upgrade pip

# Install setuptools and wheel first to avoid build issues
echo "Installing build tools..."
pip install setuptools wheel

# Install core dependencies first (those without complex build requirements)
echo "Installing core dependencies..."
pip install click rich colorama pyfiglet jinja2 python-nmap requests beautifulsoup4 dnspython cryptography

# Install data science dependencies with newer versions
echo "Installing data science dependencies..."
pip install numpy pandas scikit-learn matplotlib

# Install ML dependencies (optional - may take longer)
echo "Installing AI/ML dependencies (optional)..."
pip install tensorflow nltk || echo "Warning: TensorFlow or NLTK installation failed - AI features may be limited"

# Install PyInstaller for building executable
echo "Installing PyInstaller..."
pip install pyinstaller

# Download NLTK data (only if nltk was installed successfully)
echo "Downloading NLTK data..."
python -c "try:
    import nltk
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True) 
    nltk.download('wordnet', quiet=True)
    print('NLTK data downloaded successfully')
except ImportError:
    print('NLTK not available - skipping data download')
except Exception as e:
    print(f'NLTK data download failed: {e}')"

# Run tests (if available)
echo "Running basic functionality test..."
python -c "
try:
    from pentestool.main import main
    print('✅ Main function import successful!')
except Exception as e:
    print(f'❌ Import failed: {e}')
    exit(1)"

# Build executable
echo "Building executable with PyInstaller..."
pyinstaller pentestool.spec --noconfirm

# Check if build was successful
if [ -f "dist/PenTestTool" ]; then
    echo "✅ Build successful! Executable created at dist/PenTestTool"
    echo "You can run the tool with: ./dist/PenTestTool --help"
else
    echo "❌ Build failed. Please check the error messages above."
fi

echo "Done!"