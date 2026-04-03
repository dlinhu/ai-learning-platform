# AI Learning Platform - Windows VM 部署指南

## 一、环境要求

### 后端服务器
- Python 3.11 或更高版本
- pip 包管理器
- 可选：Python 加入系统 PATH

### 前端服务器
- Nginx for Windows（推荐）
- 或 Python http.server（简单替代）

---

## 二、部署步骤

### 方式一：前后端分离部署（推荐）

#### 步骤 1 - 部署后端

1. 将 `deploy-backend` 文件夹复制到虚拟机
2. 进入文件夹，双击运行 `start-backend.bat`
3. 后端将在 `http://localhost:8000` 运行
4. API 文档：`http://localhost:8000/docs`

#### 步骤 2 - 部署前端

1. 将 `deploy-frontend` 文件夹复制到虚拟机
2. 安装 Nginx for Windows
3. 修改 `nginx.conf` 中的 `proxy_pass` 地址为实际后端服务器 IP
4. 运行 `start-nginx.bat` 或手动启动 Nginx

### 方式二：前后端同机部署

1. 将 `deploy-backend` 和 `deploy-frontend` 复制到虚拟机
2. 运行 `start-all.bat`（自动启动后端和前端）

---

## 三、配置说明

### 后端配置

环境变量（可选）：
```
SECRET_KEY=your-secret-key-change-in-production
DATABASE_URL=sqlite:///./data/learning.db
OPENAI_API_KEY=your-api-key
```

### Nginx 配置

编辑 `nginx.conf` 修改后端地址：
```nginx
location /api {
    proxy_pass http://127.0.0.1:8000;  # 改为实际后端地址
}
```

---

## 四、端口说明

| 服务 | 端口 | 说明 |
|-----|------|------|
| 后端 API | 8000 | FastAPI 服务 |
| 前端 Web | 3000 | Python/Nginx 静态文件服务 |

---

## 五、故障排除

### 后端启动失败
1. 确认 Python 3.11+ 已安装：`python --version`
2. 手动安装依赖：`pip install -r requirements.txt`
3. 初始化数据库：`python init_db.py`

### 前端无法访问
1. 确认 Nginx 已启动
2. 检查防火墙设置
3. 确认端口未被占用：`netstat -an | findstr "80"`

### API 请求失败
1. 检查后端是否正常运行
2. 确认 nginx.conf 中 proxy_pass 地址正确
3. 查看 nginx 错误日志

---

## 六、安全建议

1. 修改默认 SECRET_KEY
2. 配置防火墙，只开放 80 和 8000 端口
3. 使用 HTTPS（需配置 SSL 证书）
4. 数据库文件定期备份
