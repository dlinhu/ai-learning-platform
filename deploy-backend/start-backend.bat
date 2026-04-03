@echo off
setlocal enabledelayedexpansion

echo ========================================
echo   AI Learning Platform - Backend Server
echo ========================================
echo.
echo Starting backend on http://localhost:8000
echo API docs: http://localhost:8000/docs
echo Press Ctrl+C to stop the server
echo.

cd /d "%~dp0"

echo Starting server...
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000

pause
