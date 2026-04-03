# AI Learning Platform - Backend Deployment

## 环境要求

- Python 3.11 或更高版本
- pip 包管理器

## 快速部署

### Windows
双击运行 `start.bat`

### Linux/Mac
```bash
chmod +x start.sh
./start.sh
```

## 手动部署

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 初始化数据库（首次运行）：
```bash
python init_db.py
```

3. 启动服务：
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API 访问

- API 地址：http://localhost:8000
- API 文档：http://localhost:8000/docs
- 健康检查：http://localhost:8000/health

## 配置说明

默认配置在 `app/config.py` 中。如需修改，可以设置环境变量：

| 环境变量 | 说明 | 默认值 |
|---------|------|--------|
| SECRET_KEY | JWT密钥 | your-secret-key |
| DATABASE_URL | 数据库URL | sqlite:///./data/learning.db |
| OPENAI_API_KEY | OpenAI API密钥 | - |

## 目录结构

```
deploy-backend/
├── app/              # 应用代码
│   ├── models/       # 数据模型
│   ├── routers/      # API路由
│   ├── services/     # 业务服务
│   └── utils/        # 工具函数
├── data/             # 数据库文件目录
├── requirements.txt  # Python依赖
├── init_db.py        # 数据库初始化脚本
├── start.bat         # Windows启动脚本
└── start.sh          # Linux/Mac启动脚本
```
