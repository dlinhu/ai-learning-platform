@echo off
setlocal enabledelayedexpansion

echo ========================================
echo   AI Learning Platform - Build & Package
echo ========================================
echo.

cd /d "%~dp0.."

set TIMESTAMP=%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set TIMESTAMP=%TIMESTAMP: =0%

echo [1/3] Cleaning old dist...
if exist "frontend\dist" rmdir /s /q "frontend\dist"
if exist "deploy-frontend\dist" rmdir /s /q "deploy-frontend\dist"

echo.
echo [2/3] Building frontend...
cd frontend
call npm run build
if errorlevel 1 (
    echo ERROR: Frontend build failed!
    pause
    exit /b 1
)
cd ..

echo.
echo [3/3] Copying dist to deploy folder...
xcopy /e /i /y "frontend\dist" "deploy-frontend\dist"

echo.
echo ========================================
echo   Package created successfully!
echo ========================================
echo.
echo Deployment packages:
echo   - deploy-backend\    (Backend Python package)
echo   - deploy-frontend\  (Frontend static files)
echo.
echo Copy these two folders to your Windows VM.
echo.
pause
