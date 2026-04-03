@echo off
setlocal enabledelayedexpansion

echo ========================================
echo   AI Learning Platform - All-in-One Start
echo ========================================
echo.

set ROOT_DIR=%~dp0
cd /d "%ROOT_DIR%"

echo Starting Backend Server...
start "Backend" cmd /k "cd /d "%ROOT_DIR%deploy-backend" && python -m uvicorn app.main:app --host 0.0.0.0 --port 8000"

timeout /t 3 /nobreak > nul

echo Starting Frontend Server...
start "Frontend" cmd /k "cd /d "%ROOT_DIR%deploy-frontend" && python -m http.server 3000"

echo.
echo ========================================
echo   Services Started!
echo ========================================
echo.
echo Backend API:  http://localhost:8000
echo Frontend:     http://localhost
echo.
echo Press any key to open browser...
pause > nul

start http://localhost:3000
