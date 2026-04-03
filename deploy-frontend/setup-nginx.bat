@echo off
setlocal enabledelayedexpansion

echo ========================================
echo   AI Learning Platform - Frontend Setup (Nginx)
echo ========================================
echo.

cd /d "%~dp0"

echo This script requires Nginx for Windows.
echo.
echo Download Nginx: https://nginx.org/en/download.html
echo.
echo After downloading:
echo 1. Extract nginx to: %~dp0nginx
echo 2. Copy nginx.exe to: %~dp0nginx\nginx.exe
echo 3. Run this script again
echo.
echo Or use Python simple server:
echo   cd dist
echo   python -m http.server 80
echo.
pause
