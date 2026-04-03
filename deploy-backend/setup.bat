@echo off
setlocal enabledelayedexpansion

echo ========================================
echo   AI Learning Platform - Backend Setup
echo ========================================
echo.

cd /d "%~dp0"

echo [1/3] Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python 3.11 or higher.
    echo Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo [2/3] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies.
    pause
    exit /b 1
)

echo.
echo [3/3] Initializing database...
python init_db.py

echo.
echo ========================================
echo   Backend setup completed!
echo ========================================
echo.
echo To start the backend server, run:
echo   start-backend.bat
echo.
pause
