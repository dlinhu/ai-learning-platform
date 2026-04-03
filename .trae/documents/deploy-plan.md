# 前后端打包部署计划

## 一、项目现状分析

### 1.1 现有配置文件
- **后端 Dockerfile**: `backend/Dockerfile` - Python 3.11-slim 基础镜像
- **前端 Dockerfile**: `frontend/Dockerfile` - Node 20-alpine 基础镜像
- **docker-compose.yml**: 已有编排配置，包含 backend、frontend、nginx 三个服务
- **nginx.conf**: 反向代理配置

### 1.2 当前问题
1. 前端 VITE_API_URL 配置错误（设为 localhost:8000，应为相对路径或 nginx 地址）
2. docker-compose.yml 中前端环境变量 VITE_API_URL 设置不正确
3. 缺少前端构建产物本地打包步骤
4. 缺少部署包打包脚本

---

## 二、部署方案

### 方案一：使用 Docker Compose 部署（推荐）
适合有 Docker 环境的远程服务器

### 方案二：分别打包前后端（纯静态文件部署）
适合无 Docker 的传统 VPS

---

## 三、具体实施步骤

### 步骤 1：修复前端环境变量配置
修改 `frontend/vite.config.ts`，添加环境变量配置：
```typescript
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      }
    }
  },
  build: {
    outDir: 'dist',
    sourcemap: false,
  }
})
```

### 步骤 2：修改前端 Dockerfile
- 优化多阶段构建
- 添加环境变量注入
- 使用 nginx 或 serve 静态文件

### 步骤 3：修改 docker-compose.yml
- 修正 VITE_API_URL 配置
- 添加 VITE_API_URL 构建参数
- 添加健康检查

### 步骤 4：添加 .dockerignore 文件
排除不必要的文件（node_modules、.git、__pycache__ 等）

### 步骤 5：创建部署打包脚本
- `scripts/build-docker.sh` - Docker 方式打包
- `scripts/build-standalone.sh` - 独立部署打包

### 步骤 6：创建独立部署包
后端：
- 包含 requirements.txt 和所有 Python 代码
- 数据库文件（data/learning.db）
- 启动脚本

前端：
- 已构建的 dist 目录（纯静态文件）
- nginx 配置文件（或简单的静态服务器配置）

---

## 四、部署包内容

### 4.1 Docker 部署包
```
deploy-docker/
├── docker-compose.yml
├── nginx.conf
├── backend/
│   └── Dockerfile
├── frontend/
│   └── Dockerfile
└── README.md
```

### 4.2 独立部署包（后端）
```
deploy-backend/
├── app/                  # 后端代码
├── data/                 # 数据库文件
├── requirements.txt
├── start.sh
└── README.md
```

### 4.3 独立部署包（前端）
```
deploy-frontend/
├── dist/                 # 构建产物
├── nginx.conf
├── start.sh
└── README.md
```

---

## 五、执行命令

### Docker 方式部署
```bash
cd deploy-docker
docker-compose up -d --build
```

### 独立部署打包
```bash
# 后端打包
cd scripts
python build_backend_pkg.py

# 前端打包（需先在 frontend 目录执行 npm run build）
python build_frontend_pkg.py
```
