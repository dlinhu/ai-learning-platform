@echo off
REM Build deployment packages for AI Learning Platform

cd /d "%~dp0"

echo ========================================
echo   AI Learning Platform - Build Script
echo ========================================
echo.

echo Building frontend...
cd ..\frontend
call npm run build
if errorlevel 1 (
    echo Frontend build failed!
    pause
    exit /b 1
)

echo.
echo Copying frontend dist to deploy-frontend...
cd ..
if exist "deploy-frontend\dist" rmdir /s /q "deploy-frontend\dist"
xcopy /e /i "frontend\dist" "deploy-frontend\dist"

echo.
echo ========================================
echo   Build completed successfully!
echo ========================================
echo.
echo Deployment packages:
echo   - deploy-backend\    (Backend Python package)
echo   - deploy-frontend\  (Frontend static files)
echo.
echo Next steps:
echo   1. Copy deploy-backend to your server
echo   2. Copy deploy-frontend to your server
echo   3. Configure and run start.bat/start.sh
echo.
pause
