@echo off
echo ========================================
echo SMS Spam Detection System
echo ========================================
echo.

echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo.
echo Installing/Updating dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Starting the application...
echo Open your browser and go to: http://localhost:8501
echo Press Ctrl+C to stop the application
echo.

streamlit run app.py

pause