#!/bin/bash

echo "开始部署网站健康度监控程序（后台运行）..."

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "错误: Python 3 未安装"
    exit 1
fi

# 安装依赖
echo "安装依赖包..."
pip3 install -r requirements.txt

# 后台启动监控程序
echo "后台启动网站健康度监控程序..."
nohup python3 health_monitor.py > monitor_output.log 2>&1 &

# 显示进程信息
echo "监控程序已启动，进程信息："
ps aux | grep health_monitor.py | grep -v grep

echo "监控日志将输出到 monitor_output.log 文件"
echo "可以使用 'tail -f monitor_output.log' 查看实时日志"
