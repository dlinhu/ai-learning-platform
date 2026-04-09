#!/bin/bash

echo "开始打包网站健康度监控程序..."

# 创建打包目录
mkdir -p monitor_package

# 复制必要文件
cp health_monitor.py monitor_package/
cp requirements.txt monitor_package/
cp start_monitor.sh monitor_package/
cp start_monitor.bat monitor_package/
cp start_monitor_background.sh monitor_package/

# 创建README文件
cat > monitor_package/README.md << 'EOF'
# 网站健康度监控程序

## 功能
- 定时检查网站健康度（默认每10分钟一次）
- 支持邮件和短信通知
- 详细的日志记录
- 跨平台支持（Linux/Mac/Windows）

## 部署步骤

### 1. 上传文件
将打包后的文件上传到云端服务器。

### 2. 安装依赖
```bash
# Linux/Mac
chmod +x start_monitor.sh start_monitor_background.sh
./start_monitor.sh

# 或后台运行
./start_monitor_background.sh
```

### 3. 配置通知
编辑 health_monitor.py 文件，配置邮件和短信通知参数：
- EMAIL_CONFIG：邮件通知配置
- SMS_CONFIG：短信通知配置

### 4. 调整监控参数
编辑 health_monitor.py 文件，调整监控参数：
- WEBSITE_URL：要监控的网站URL
- CHECK_INTERVAL：检查间隔（分钟）

## 查看日志
- health_monitor.log：详细监控日志
- monitor_output.log：程序输出日志

## 停止监控
```bash
# 查找进程ID
ps aux | grep health_monitor.py | grep -v grep

# 停止进程
kill <进程ID>
```
EOF

# 打包文件
tar -czf monitor_package.tar.gz monitor_package/

# 清理临时目录
rm -rf monitor_package/

echo "打包完成！生成文件：monitor_package.tar.gz"
echo "可以将此文件上传到云端服务器进行部署"
