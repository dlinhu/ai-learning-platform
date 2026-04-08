#!/bin/bash

echo "开始部署网站健康度监控程序..."

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "错误: Python 3 未安装"
    exit 1
fi

# 安装依赖
echo "安装依赖包..."
pip3 install -r requirements.txt

# 启动监控程序
echo "启动网站健康度监控程序..."
python3 health_monitor.py
