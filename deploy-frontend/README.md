# AI Learning Platform - Frontend Deployment

## 环境要求

- Nginx (Linux/Mac) 或
- Windows 版 Nginx

## 快速部署

### Windows
1. 下载 Nginx for Windows
2. 解压到当前目录
3. 双击运行 `start.bat`

### Linux/Mac
```bash
chmod +x start.sh
./start.sh
```

## 手动部署

1. 配置 nginx：
```bash
nginx -c /path/to/nginx.conf
```

2. 或使用 Python 简单服务器（开发模式）：
```bash
cd dist
python -m http.server 80
```

## 目录结构

```
deploy-frontend/
├── dist/           # 构建产物（运行 npm run build 后生成）
├── nginx.conf      # Nginx 配置
├── start.bat       # Windows 启动脚本
├── start.sh        # Linux/Mac 启动脚本
└── README.md
```

## 构建前端

如果 dist 目录为空，需要先构建：

```bash
cd ai-learning-platform/frontend
npm install
npm run build
```

构建产物将在 `frontend/dist` 目录中。

## API 配置

前端通过 `/api` 路径访问后端 API。确保 nginx 配置中包含正确的代理设置：

```nginx
location /api {
    proxy_pass http://backend:8000;
    ...
}
```
