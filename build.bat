@echo off
echo Building AI-Powered Penetration Testing Tool...

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Download NLTK data
echo Downloading NLTK data...
python -c "import nltk; nltk.download('punkt', quiet=True); nltk.download('stopwords', quiet=True); nltk.download('wordnet', quiet=True)"

REM Run tests
echo Running basic functionality test...
python -c "from pentestool.main import main; print('Import successful!')"

REM Build executable
echo Building executable with PyInstaller...
pyinstaller pentestool.spec

REM Check if build was successful
if exist "dist\PenTestTool.exe" (
    echo Build successful! Executable created at dist\PenTestTool.exe
    echo You can run the tool with: dist\PenTestTool.exe --help
) else (
    echo Build failed. Please check the error messages above.
)

echo Done!
pause