@echo off
echo 开始部署网站健康度监控程序...

:: 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: Python 未安装
    pause
    exit /b 1
)

:: 安装依赖
echo 安装依赖包...
pip install -r requirements.txt

:: 启动监控程序
echo 启动网站健康度监控程序...
python health_monitor.py
pause
