@echo off
REM AI Learning Platform Frontend Deployment Package

echo Starting frontend server...
echo.

cd /d "%~dp0"

echo Starting nginx on port 80...
echo.

nginx -c "%~dp0nginx.conf" -g "daemon off;"

pause
