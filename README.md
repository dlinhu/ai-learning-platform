# AI培训在线学习平台

一个轻量级的在线学习平台，用于管理Context Engineering综合课程的学习进度。

## 快速开始

### 方式一：Docker部署（推荐）

```bash
# 克隆或进入项目目录
cd ai-learning-platform

# 启动服务
docker-compose up -d

# 访问
# 前端: http://localhost
# API文档: http://localhost:8000/docs
```

### 方式二：本地开发

#### 后端

```bash
cd backend

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 初始化数据库
python ../scripts/init_db.py

# 启动服务
uvicorn app.main:app --reload --port 8000
```

#### 前端

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

## 项目结构

```
ai-learning-platform/
├── backend/                # FastAPI后端
│   ├── app/
│   │   ├── models/         # 数据库模型
│   │   ├── routers/        # API路由
│   │   ├── services/       # 业务逻辑
│   │   └── utils/          # 工具函数
│   └── requirements.txt
├── frontend/               # React前端
│   ├── src/
│   │   ├── components/     # React组件
│   │   ├── pages/          # 页面组件
│   │   ├── services/       # API服务
│   │   └── stores/         # 状态管理
│   └── package.json
├── data/                   # 数据库文件
├── scripts/                # 初始化脚本
├── docker-compose.yml
└── README.md
```

## 功能特性

- **课程展示**: 模块视图、时间线视图、Markdown/Notebook渲染
- **进度追踪**: 学习状态、时长统计、完成率计算
- **知识扩展**: 术语提取、AI生成解释、相关资源
- **学习仪表盘**: 统计数据、学习日历、连续学习天数

## API端点

| 端点 | 描述 |
|------|------|
| POST /api/auth/register | 用户注册 |
| POST /api/auth/login | 用户登录 |
| GET /api/courses/modules | 获取模块列表 |
| GET /api/courses/lessons/{id} | 获取课时详情 |
| GET /api/progress | 获取学习进度 |
| GET /api/dashboard/stats | 获取学习统计 |

## 环境变量

| 变量 | 描述 | 默认值 |
|------|------|--------|
| DATABASE_URL | 数据库连接 | sqlite:///./data/learning.db |
| SECRET_KEY | JWT密钥 | (需修改) |
| OPENAI_API_KEY | OpenAI API密钥 | (可选) |
| CONTENT_PATH | 课程内容路径 | ../AI Courses |

## 技术栈

- **前端**: React + Vite + TypeScript + TailwindCSS
- **后端**: FastAPI + SQLAlchemy + SQLite
- **部署**: Docker + Nginx
# ai-learning-platform
