@echo off
REM AI Learning Platform Backend Deployment Package

echo Starting backend server...
echo.

cd /d "%~dp0"

if not exist "data" mkdir data

echo Checking Python installation...
python --version
if errorlevel 1 (
    echo Python not found. Please install Python 3.11 or higher.
    pause
    exit /b 1
)

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting server on port 8000...
echo API will be available at http://localhost:8000
echo API docs at http://localhost:8000/docs
echo.

python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

pause
