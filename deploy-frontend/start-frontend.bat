@echo off
setlocal enabledelayedexpansion

echo ========================================
echo   AI Learning Platform - Frontend Server
echo ========================================
echo.
echo Choose server mode:
echo   1. Python Server (Simple, recommended)
echo   2. Nginx (Requires separate installation)
echo.

set /p CHOICE="Enter choice (1 or 2): "

cd /d "%~dp0"

if "%CHOICE%"=="1" (
    echo.
    echo Starting Python HTTP server on port 80...
    echo Open http://localhost in your browser
    echo Press Ctrl+C to stop
    echo.
    cd dist
    python -m http.server 3000
) else if "%CHOICE%"=="2" (
    if exist "nginx\nginx.exe" (
        echo Starting Nginx...
        start /b nginx\nginx.exe -c "%~dp0nginx.conf"
        echo Server started. Open http://localhost
    ) else (
        echo Nginx not found. Please download nginx for Windows
        echo Or use Python server option (1)
        pause
    )
) else (
    echo Invalid choice
    pause
)

pause
