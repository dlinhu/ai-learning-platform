# AI培训在线学习平台 - Code Wiki

## 目录

1. [项目概述](#项目概述)
2. [技术架构](#技术架构)
3. [目录结构](#目录结构)
4. [后端模块详解](#后端模块详解)
   - [数据模型层 (Models)](#数据模型层-models)
   - [API路由层 (Routers)](#api路由层-routers)
   - [业务服务层 (Services)](#业务服务层-services)
   - [工具层 (Utils)](#工具层-utils)
5. [前端模块详解](#前端模块详解)
   - [页面组件 (Pages)](#页面组件-pages)
   - [服务层 (Services)](#服务层-services)
   - [状态管理 (Stores)](#状态管理-stores)
   - [自定义Hooks](#自定义hooks)
6. [API接口文档](#api接口文档)
7. [数据流与依赖关系](#数据流与依赖关系)
8. [部署与运行](#部署与运行)
9. [配置说明](#配置说明)

---

## 项目概述

本项目是一个轻量级的AI培训在线学习平台，用于管理Context Engineering综合课程的学习进度。系统提供课程展示、学习进度追踪、知识扩展、学习仪表盘等核心功能，支持管理员进行用户管理和课程管理。

### 核心功能

| 功能模块 | 描述 |
|---------|------|
| 课程展示 | 模块视图、时间线视图、Markdown/Notebook渲染 |
| 进度追踪 | 学习状态管理、时长统计、完成率计算 |
| 知识扩展 | 术语提取、AI生成解释、相关资源推荐 |
| 学习仪表盘 | 统计数据、学习日历、连续学习天数追踪 |
| 管理后台 | 用户管理、课程管理、AI设置配置 |
| 练习系统 | 知识点练习题、答题记录、进度统计 |

---

## 技术架构

### 整体架构图

```
┌─────────────────────────────────────────────────────────────────┐
│                         客户端 (Browser)                         │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    前端 (React + Vite)                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │   Pages     │  │  Services   │  │       Stores            │ │
│  │  (页面组件)  │──│  (API调用)   │──│  (Zustand状态管理)       │ │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  │ HTTP/REST API
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    后端 (FastAPI)                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │   Routers   │──│   Services  │──│       Models            │ │
│  │  (API路由)   │  │  (业务逻辑)  │  │  (SQLAlchemy数据模型)    │ │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    数据层                                        │
│  ┌─────────────────────┐  ┌─────────────────────────────────┐  │
│  │   SQLite Database   │  │   File System (课程内容文件)     │  │
│  └─────────────────────┘  └─────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 技术栈详情

#### 后端技术栈

| 技术 | 版本 | 用途 |
|-----|------|------|
| FastAPI | 0.109.0 | Web框架，提供REST API |
| SQLAlchemy | 2.0.25 | ORM，数据库操作 |
| Pydantic | 2.5.3 | 数据验证和序列化 |
| python-jose | 3.3.0 | JWT认证 |
| passlib | 1.7.4 | 密码哈希 |
| markdown | 3.5.2 | Markdown渲染 |
| nbconvert | 7.14.0 | Jupyter Notebook转换 |
| OpenAI | 1.10.0 | AI内容生成 |

#### 前端技术栈

| 技术 | 版本 | 用途 |
|-----|------|------|
| React | 18.2.0 | UI框架 |
| TypeScript | 5.3.3 | 类型安全 |
| Vite | 5.0.11 | 构建工具 |
| React Router | 6.21.0 | 路由管理 |
| Zustand | 4.4.7 | 状态管理 |
| Axios | 1.6.5 | HTTP客户端 |
| TailwindCSS | 3.4.1 | 样式框架 |
| react-markdown | 9.0.1 | Markdown渲染 |

#### 部署技术

| 技术 | 用途 |
|-----|------|
| Docker | 容器化部署 |
| Nginx | 反向代理和静态资源服务 |
| Docker Compose | 多容器编排 |

---

## 目录结构

```
ai-learning-platform/
├── backend/                      # 后端代码
│   ├── app/                      # 应用主目录
│   │   ├── models/               # 数据模型
│   │   │   ├── __init__.py
│   │   │   └── models.py         # SQLAlchemy模型定义
│   │   ├── routers/              # API路由
│   │   │   ├── __init__.py
│   │   │   ├── admin.py          # 管理员API
│   │   │   ├── auth.py           # 认证API
│   │   │   ├── courses.py        # 课程API
│   │   │   ├── dashboard.py      # 仪表盘API
│   │   │   ├── practice.py       # 练习API
│   │   │   ├── progress.py       # 进度API
│   │   │   └── terms.py          # 术语API
│   │   ├── services/             # 业务服务
│   │   │   ├── __init__.py
│   │   │   ├── ai_content_generator.py  # AI内容生成
│   │   │   ├── ai_service.py            # AI服务抽象
│   │   │   ├── content_parser.py        # 内容解析
│   │   │   ├── content_renderer.py      # 内容渲染
│   │   │   └── course_parser.py         # 课程解析
│   │   ├── utils/                # 工具函数
│   │   │   ├── __init__.py
│   │   │   └── database.py       # 数据库配置
│   │   ├── __init__.py
│   │   ├── config.py             # 应用配置
│   │   └── main.py               # 应用入口
│   ├── course_content/           # 课程内容文件(Markdown/Notebook)
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/                     # 前端代码
│   ├── src/
│   │   ├── components/           # 公共组件
│   │   │   └── Layout.tsx        # 页面布局
│   │   ├── hooks/                # 自定义Hooks
│   │   │   ├── useAutoLogout.ts  # 自动登出
│   │   │   └── useTimeTracker.ts # 学习时间追踪
│   │   ├── pages/                # 页面组件
│   │   │   ├── AdminAISettings.tsx   # AI设置页
│   │   │   ├── AdminCourses.tsx      # 课程管理页
│   │   │   ├── AdminDashboard.tsx    # 管理员仪表盘
│   │   │   ├── CourseList.tsx        # 课程列表页
│   │   │   ├── Dashboard.tsx         # 用户仪表盘
│   │   │   ├── Home.tsx              # 首页
│   │   │   ├── LessonDetail.tsx      # 课时详情页
│   │   │   ├── Login.tsx             # 登录页
│   │   │   └── ModuleDetail.tsx      # 模块详情页
│   │   ├── services/             # API服务
│   │   │   ├── admin.ts          # 管理员API
│   │   │   ├── api.ts            # Axios实例
│   │   │   ├── auth.ts           # 认证API
│   │   │   └── courses.ts        # 课程API
│   │   ├── stores/               # 状态管理
│   │   │   └── authStore.ts      # 认证状态
│   │   ├── App.tsx               # 应用入口
│   │   ├── index.css
│   │   └── main.tsx
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.ts
├── data/                         # 数据文件
│   └── terms.json                # 预定义术语
├── deploy/                       # 部署脚本
├── scripts/                      # 工具脚本
│   ├── create_admin.py           # 创建管理员
│   └── init_db.py                # 初始化数据库
├── docker-compose.yml            # Docker编排配置
├── nginx.conf                    # Nginx配置
└── README.md
```

---

## 后端模块详解

### 数据模型层 (Models)

数据模型位于 [backend/app/models/models.py](backend/app/models/models.py)，使用SQLAlchemy ORM定义。

#### 核心数据模型

##### User (用户模型)

```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True)           # UUID主键
    username = Column(String, unique=True)          # 用户名
    email = Column(String, unique=True)             # 邮箱
    password_hash = Column(String)                  # 密码哈希
    role = Column(String)                           # 角色: student/admin
    group = Column(String)                          # 分组: group1-group6
    created_at = Column(DateTime)                   # 创建时间
    settings = Column(JSON)                         # 用户设置
```

**关系**:
- `progress`: 一对多关联Progress模型
- `notes`: 一对多关联Note模型

##### Module (模块模型)

```python
class Module(Base):
    __tablename__ = "modules"
    
    id = Column(String, primary_key=True)
    name = Column(String)               # 模块名称
    description = Column(Text)          # 模块描述
    order_index = Column(Integer)       # 排序索引
```

**关系**:
- `lessons`: 一对多关联Lesson模型

##### Lesson (课时模型)

```python
class Lesson(Base):
    __tablename__ = "lessons"
    
    id = Column(String, primary_key=True)
    module_id = Column(String, ForeignKey)    # 所属模块
    date = Column(String)                      # 日期
    title = Column(String)                     # 标题
    topics = Column(JSON)                      # 主题列表
    difficulty = Column(String)                # 难度: basic/intermediate/advanced
    time_estimate = Column(Integer)            # 预估时长(分钟)
    materials = Column(JSON)                   # 课程材料
    summary = Column(Text)                     # 摘要
    raw_content = Column(Text)                 # 原始内容
    structured_content = Column(JSON)          # 结构化内容
```

**关系**:
- `module`: 多对一关联Module
- `progress`: 一对多关联Progress
- `knowledge_points`: 一对多关联KnowledgePoint
- `lesson_terms`: 一对多关联LessonTerm

##### Progress (进度模型)

```python
class Progress(Base):
    __tablename__ = "progress"
    
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey)       # 用户ID
    lesson_id = Column(String, ForeignKey)     # 课时ID
    status = Column(String)                     # 状态: not_started/in_progress/completed
    started_at = Column(DateTime)               # 开始时间
    completed_at = Column(DateTime)             # 完成时间
    time_spent = Column(Integer)                # 学习时长(分钟)
    bookmarked = Column(Boolean)                # 是否收藏
```

##### KnowledgePoint (知识点模型)

```python
class KnowledgePoint(Base):
    __tablename__ = "knowledge_points"
    
    id = Column(String, primary_key=True)
    lesson_id = Column(String, ForeignKey)     # 所属课时
    title = Column(String)                      # 标题
    description = Column(Text)                  # 描述
    category = Column(String)                   # 分类
    importance = Column(Integer)                # 重要性(1-5)
    related_terms = Column(JSON)                # 相关术语
    related_knowledge = Column(JSON)            # 相关知识
    examples = Column(JSON)                     # 示例
    key_concepts = Column(JSON)                 # 关键概念
    common_mistakes = Column(JSON)              # 常见错误
    best_practices = Column(JSON)               # 最佳实践
    external_links = Column(JSON)               # 外部链接
```

##### Term (术语模型)

```python
class Term(Base):
    __tablename__ = "terms"
    
    id = Column(String, primary_key=True)
    term = Column(String, unique=True)          # 术语
    definition = Column(Text)                    # 定义
    category = Column(String)                    # 分类
    examples = Column(JSON)                      # 示例
    related_terms = Column(JSON)                 # 相关术语
    external_links = Column(JSON)                # 外部链接
    is_predefined = Column(Boolean)              # 是否预定义
    detailed_definition = Column(Text)           # 详细定义
    related_concepts = Column(JSON)              # 相关概念
    usage_examples = Column(JSON)                # 用法示例
    common_questions = Column(JSON)              # 常见问题
```

##### PracticeQuestion (练习题模型)

```python
class PracticeQuestion(Base):
    __tablename__ = "practice_questions"
    
    id = Column(String, primary_key=True)
    knowledge_point_id = Column(String, ForeignKey)  # 所属知识点
    question_type = Column(String)                    # 题型: single_choice/multiple_choice等
    question_text = Column(Text)                      # 题目内容
    options = Column(JSON)                            # 选项
    correct_answer = Column(Text)                     # 正确答案
    explanation = Column(Text)                        # 解析
    difficulty = Column(Integer)                      # 难度(1-3)
    order_index = Column(Integer)                     # 排序
```

##### AISettings (AI设置模型)

```python
class AISettings(Base):
    __tablename__ = "ai_settings"
    
    id = Column(String, primary_key=True)        # 固定为"default"
    provider = Column(String)                     # 提供商: none/openai/local
    openai_api_key = Column(String)               # OpenAI API密钥
    openai_base_url = Column(String)              # OpenAI基础URL
    local_model_url = Column(String)              # 本地模型URL
    local_model_name = Column(String)             # 本地模型名称
```

#### 枚举类型

```python
class UserRole(str, enum.Enum):
    STUDENT = "student"
    ADMIN = "admin"

class UserGroup(str, enum.Enum):
    GROUP_1 = "group1"
    GROUP_2 = "group2"
    # ... group3-group6

class ProgressStatus(str, enum.Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
```

### API路由层 (Routers)

#### 认证路由 (auth.py)

[backend/app/routers/auth.py](backend/app/routers/auth.py)

**核心函数**:

| 函数名 | 方法 | 路径 | 描述 |
|-------|------|------|------|
| `register` | POST | /api/auth/register | 用户注册 |
| `login` | POST | /api/auth/login | 用户登录，返回JWT |
| `get_me` | GET | /api/auth/me | 获取当前用户信息 |
| `get_current_user` | - | - | 依赖注入，获取当前用户 |
| `create_access_token` | - | - | 创建JWT令牌 |
| `verify_password` | - | - | 验证密码 |
| `get_password_hash` | - | - | 生成密码哈希 |

**关键代码**:

```python
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user
```

#### 课程路由 (courses.py)

[backend/app/routers/courses.py](backend/app/routers/courses.py)

**核心端点**:

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | /api/courses/modules | 获取所有模块列表 |
| GET | /api/courses/modules/{id} | 获取单个模块详情 |
| GET | /api/courses/modules/{id}/lessons | 获取模块下的课时列表 |
| GET | /api/courses/lessons/{id} | 获取课时详情(含知识点、术语) |
| GET | /api/courses/content/{path} | 获取课程内容(渲染后) |
| GET | /api/courses/timeline | 获取时间线视图 |
| GET | /api/courses/terms | 获取所有术语 |

#### 进度路由 (progress.py)

[backend/app/routers/progress.py](backend/app/routers/progress.py)

**核心端点**:

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | /api/progress | 获取用户所有进度 |
| POST | /api/progress/{lesson_id}/start | 开始学习课时 |
| POST | /api/progress/{lesson_id}/complete | 完成课时 |
| PUT | /api/progress/{lesson_id}/time | 更新学习时长 |
| POST | /api/progress/update-time | 累加学习时长 |
| POST | /api/progress/{lesson_id}/bookmark | 切换收藏状态 |
| GET | /api/progress/bookmarks | 获取收藏列表 |
| POST | /api/progress/notes | 创建笔记 |
| GET | /api/progress/notes/{lesson_id} | 获取课时笔记 |
| PUT | /api/progress/notes/{lesson_id} | 更新笔记 |

#### 仪表盘路由 (dashboard.py)

[backend/app/routers/dashboard.py](backend/app/routers/dashboard.py)

**核心端点**:

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | /api/dashboard/stats | 获取学习统计(完成率、连续天数等) |
| GET | /api/dashboard/modules | 获取各模块进度 |
| GET | /api/dashboard/time-stats | 获取时间统计(周/月分布) |
| GET | /api/dashboard/calendar | 获取学习日历(近30天) |
| GET | /api/dashboard/today | 获取今日课程 |
| GET | /api/dashboard/admin/all-progress | 管理员获取所有用户进度 |

**统计计算逻辑**:

```python
def get_stats(db, current_user):
    # 计算连续学习天数
    completed_dates = db.query(Progress.completed_at).filter(
        Progress.user_id == current_user.id,
        Progress.status == "completed"
    ).order_by(Progress.completed_at.desc()).all()
    
    dates = sorted(set([d[0].date() for d in completed_dates if d[0]]), reverse=True)
    
    today = datetime.utcnow().date()
    streak = 0
    for i, date in enumerate(dates):
        expected = today - timedelta(days=i)
        if date == expected:
            streak += 1
        else:
            break
    current_streak = streak
```

#### 管理员路由 (admin.py)

[backend/app/routers/admin.py](backend/app/routers/admin.py)

**核心端点**:

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | /api/admin/stats | 获取系统统计概览 |
| GET | /api/admin/users | 获取用户列表(分页/排序/搜索) |
| PUT | /api/admin/users/{id}/group | 更新用户分组 |
| GET | /api/admin/users/{id}/detail | 获取用户详情 |
| GET | /api/admin/modules | 获取所有模块 |
| POST | /api/admin/modules | 创建模块 |
| PUT | /api/admin/modules/{id} | 更新模块 |
| DELETE | /api/admin/modules/{id} | 删除模块 |
| POST | /api/admin/lessons | 创建课时 |
| POST | /api/admin/lessons/upload | 上传课程文件 |
| GET | /api/admin/ai-settings | 获取AI设置 |
| PUT | /api/admin/ai-settings | 更新AI设置 |
| POST | /api/admin/ai-settings/test | 测试AI连接 |

**权限验证**:

```python
def require_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user
```

#### 练习路由 (practice.py)

[backend/app/routers/practice.py](backend/app/routers/practice.py)

**核心端点**:

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | /api/practice/knowledge-point/{kp_id} | 获取知识点练习题 |
| POST | /api/practice/submit | 提交答案 |
| GET | /api/practice/progress/{kp_id} | 获取练习进度 |

#### 术语路由 (terms.py)

[backend/app/routers/terms.py](backend/app/routers/terms.py)

**核心端点**:

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | /api/terms/{term_name} | 获取术语详情 |
| GET | /api/terms/lesson/{lesson_id} | 获取课时相关术语 |
| GET | /api/terms/search/{query} | 搜索术语 |

### 业务服务层 (Services)

#### AI服务 (ai_service.py)

[backend/app/services/ai_service.py](backend/app/services/ai_service.py)

提供AI提供商的抽象层，支持多种AI后端。

**类结构**:

```
AIProvider (ABC)
├── NoneProvider        # AI功能禁用
├── OpenAIProvider      # OpenAI API
└── LocalModelProvider  # 本地模型(Ollama/OpenAI兼容)
```

**核心方法**:

```python
class AIProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        pass
    
    @abstractmethod
    def test_connection(self) -> tuple[bool, str]:
        pass
```

**工厂函数**:

```python
def get_ai_provider(settings) -> AIProvider:
    if not settings or settings.provider == "none":
        return NoneProvider()
    if settings.provider == "openai":
        return OpenAIProvider(settings.openai_api_key, settings.openai_base_url)
    if settings.provider == "local":
        return LocalModelProvider(settings.local_model_url, settings.local_model_name)
    return NoneProvider()
```

#### AI内容生成器 (ai_content_generator.py)

[backend/app/services/ai_content_generator.py](backend/app/services/ai_content_generator.py)

**核心功能**:

| 方法 | 描述 |
|------|------|
| `parse_course_content` | 解析课程内容，提取标题、摘要、主题等 |
| `generate_knowledge_points` | 生成知识点列表 |
| `generate_practice_questions` | 生成练习题 |
| `generate_lesson_content` | 生成结构化课程内容 |

**使用示例**:

```python
ai_generator = AIContentGenerator(ai_provider)

# 解析课程内容
result = ai_generator.parse_course_content(raw_content, filename)
# 返回: {title, summary, topics, difficulty, time_estimate, key_concepts}

# 生成知识点
knowledge_points = ai_generator.generate_knowledge_points(content, count=5)

# 生成练习题
questions = ai_generator.generate_practice_questions(knowledge_point, count=3)
```

#### 内容解析器 (content_parser.py)

[backend/app/services/content_parser.py](backend/app/services/content_parser.py)

**支持的文件格式**:
- Markdown (.md)
- Jupyter Notebook (.ipynb)
- Python (.py)

**核心类**:

```python
@dataclass
class ParsedContent:
    title: str
    summary: str
    sections: List[Dict]
    knowledge_points: List[KnowledgePoint]
    terms: List[Term]
    code_examples: List[Dict]
    raw_content: str

class ContentParser:
    def parse_file(self, file_path: str) -> Optional[ParsedContent]:
        # 根据文件扩展名选择解析方法
        ext = full_path.suffix.lower()
        if ext == '.md':
            return self._parse_markdown(full_path)
        elif ext == '.ipynb':
            return self._parse_notebook(full_path)
        elif ext == '.py':
            return self._parse_python(full_path)
```

**知识点提取逻辑**:

```python
def _extract_knowledge_points(self, content: str, sections: List[Dict]) -> List[KnowledgePoint]:
    # 从标题和内容中提取知识点
    # 自动关联预定义的AI术语
    for term in self.ai_terms:
        if term.lower() in content_text.lower():
            related.append(term)
```

#### 内容渲染器 (content_renderer.py)

[backend/app/services/content_renderer.py](backend/app/services/content_renderer.py)

**核心功能**:
- Markdown转HTML（支持代码高亮、表格、目录）
- Jupyter Notebook转HTML
- Python代码格式化

```python
class ContentRenderer:
    def render_content(self, relative_path: str) -> Dict:
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext == '.md':
            return self.render_markdown(file_path)
        elif ext == '.ipynb':
            return self.render_notebook(file_path)
        # ...
```

#### 课程解析器 (course_parser.py)

[backend/app/services/course_parser.py](backend/app/services/course_parser.py)

解析课程编排Markdown文件，提取模块和课时信息。

**数据结构**:

```python
@dataclass
class Material:
    title: str
    text: str
    path: str

@dataclass
class LessonData:
    date: str
    title: str
    topics: List[str]
    difficulty: str
    time_estimate: int
    materials: List[Material]

@dataclass
class ModuleData:
    order: int
    name: str
    description: str
    lessons: List[LessonData]
```

**解析逻辑**:

```python
class CourseScheduleParser:
    def parse(self) -> List[ModuleData]:
        # 解析 "## 第X模块：XXX" 格式的模块标题
        # 解析表格形式的课时安排
        # 提取日期、标题、主题、材料链接
```

### 工具层 (Utils)

#### 数据库配置 (database.py)

[backend/app/utils/database.py](backend/app/utils/database.py)

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLite需要
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

#### 应用配置 (config.py)

[backend/app/config.py](backend/app/config.py)

```python
class Settings(BaseSettings):
    APP_NAME: str = "AI Learning Platform"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./data/learning.db"
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7天
    CONTENT_PATH: str = "../AI Courses"
    OPENAI_API_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings()
```

---

## 前端模块详解

### 页面组件 (Pages)

#### 路由配置 (App.tsx)

[frontend/src/App.tsx](frontend/src/App.tsx)

```tsx
function PrivateRoute({ children }) {
  const { user } = useAuthStore()
  return user ? <>{children}</> : <Navigate to="/login" />
}

function AdminRoute({ children }) {
  const { user } = useAuthStore()
  if (!user) return <Navigate to="/login" />
  if (user.role !== 'admin') return <Navigate to="/dashboard" />
  return <>{children}</>
}

// 路由配置
<Routes>
  <Route path="/login" element={<Login />} />
  <Route path="/" element={<Layout />}>
    <Route index element={<Home />} />
    <Route path="dashboard" element={<PrivateRoute><Dashboard /></PrivateRoute>} />
    <Route path="courses" element={<PrivateRoute><CourseList /></PrivateRoute>} />
    <Route path="admin" element={<AdminRoute><AdminDashboard /></AdminRoute>} />
    // ...
  </Route>
</Routes>
```

#### Dashboard (用户仪表盘)

[frontend/src/pages/Dashboard.tsx](frontend/src/pages/Dashboard.tsx)

**功能**:
- 显示学习统计（完成进度、学习时长、连续天数）
- 模块进度条展示
- 学习日历热力图
- 本周学习时长柱状图

**数据加载**:

```tsx
const loadData = async () => {
  const [statsRes, progressRes, calendarRes, timeStatsRes] = await Promise.all([
    api.get<Stats>('/dashboard/stats'),
    api.get<ModuleProgress[]>('/dashboard/modules'),
    api.get<CalendarDay[]>('/dashboard/calendar'),
    api.get<TimeStats>('/dashboard/time-stats')
  ])
  // ...
}
```

#### AdminDashboard (管理员仪表盘)

[frontend/src/pages/AdminDashboard.tsx](frontend/src/pages/AdminDashboard.tsx)

**功能**:
- 系统统计概览（总用户、活跃用户、学习时长）
- 用户列表（支持搜索、排序、分页）
- 用户详情弹窗（模块进度、学习日历、最近活动）
- 用户分组管理

**关键状态**:

```tsx
const [stats, setStats] = useState<AdminStats | null>(null)
const [users, setUsers] = useState<UserListItem[]>([])
const [selectedUser, setSelectedUser] = useState<UserDetailResponse | null>(null)
const [sortBy, setSortBy] = useState<'time_spent' | 'completion_rate' | 'last_active' | 'username'>('time_spent')
```

### 服务层 (Services)

#### API实例 (api.ts)

[frontend/src/services/api.ts](frontend/src/services/api.ts)

```tsx
const api = axios.create({
  baseURL: '/api',
  headers: { 'Content-Type': 'application/json' }
})

// 请求拦截器：添加JWT Token
api.interceptors.request.use((config) => {
  const token = useAuthStore.getState().token
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// 响应拦截器：处理401错误
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      useAuthStore.getState().logout()
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)
```

#### 认证服务 (auth.ts)

[frontend/src/services/auth.ts](frontend/src/services/auth.ts)

```tsx
export const authApi = {
  async login(username: string, password: string): Promise<LoginResponse> {
    const params = new URLSearchParams()
    params.append('username', username)
    params.append('password', password)
    const response = await api.post<LoginResponse>('/auth/login', params, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    })
    return response.data
  },
  
  async register(username: string, email: string, password: string, group: string): Promise<User>,
  async getMe(): Promise<User>
}
```

#### 课程服务 (courses.ts)

[frontend/src/services/courses.ts](frontend/src/services/courses.ts)

```tsx
export const courseApi = {
  async getModules(): Promise<Module[]>,
  async getModule(id: string): Promise<Module>,
  async getModuleLessons(moduleId: string): Promise<Lesson[]>,
  async getLesson(id: string): Promise<Lesson>,
  async getContent(path: string): Promise<Content>,
  async getTimeline(): Promise<TimelineItem[]>,
  async getPracticeQuestions(knowledgePointId: string): Promise<PracticeQuestion[]>,
  async submitAnswer(request: SubmitAnswerRequest): Promise<SubmitAnswerResponse>,
  async getPracticeProgress(knowledgePointId: string): Promise<PracticeProgress>
}
```

#### 管理员服务 (admin.ts)

[frontend/src/services/admin.ts](frontend/src/services/admin.ts)

```tsx
export const adminApi = {
  getStats: async (): Promise<AdminStats>,
  getUsers: async (params: UsersListParams): Promise<UsersListResponse>,
  getUserDetail: async (userId: string): Promise<UserDetailResponse>,
  updateUserGroup: async (userId: string, group: string),
  getModules: async (),
  createModule: async (name: string, description?: string),
  updateModule: async (moduleId: string, data),
  deleteModule: async (moduleId: string),
  createLesson: async (data),
  uploadLesson: async (moduleId: string, file: File, title?: string, date?: string),
  getAISettings: async (),
  updateAISettings: async (data),
  testAISettings: async (data)
}
```

### 状态管理 (Stores)

#### 认证状态 (authStore.ts)

[frontend/src/stores/authStore.ts](frontend/src/stores/authStore.ts)

使用Zustand进行状态管理，支持持久化存储。

```tsx
interface AuthState {
  user: User | null
  token: string | null
  setAuth: (user: User, token: string) => void
  logout: () => void
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      user: null,
      token: null,
      setAuth: (user, token) => set({ user, token }),
      logout: () => set({ user: null, token: null }),
    }),
    { name: 'auth-storage' }  // localStorage key
  )
)
```

### 自定义Hooks

#### 自动登出 (useAutoLogout.ts)

[frontend/src/hooks/useAutoLogout.ts](frontend/src/hooks/useAutoLogout.ts)

用户无操作10分钟后自动登出。

```tsx
const INACTIVITY_TIMEOUT = 10 * 60 * 1000  // 10分钟

export function useAutoLogout() {
  const { user, logout } = useAuthStore()
  const navigate = useNavigate()
  
  useEffect(() => {
    if (!user) return
    
    const resetTimer = () => {
      if (timerRef.current) clearTimeout(timerRef.current)
      timerRef.current = setTimeout(() => {
        logout()
        navigate('/login')
      }, INACTIVITY_TIMEOUT)
    }
    
    const events = ['mousedown', 'keydown', 'scroll', 'touchstart', 'mousemove']
    events.forEach(event => {
      window.addEventListener(event, resetTimer, true)
    })
    
    return () => {
      events.forEach(event => {
        window.removeEventListener(event, resetTimer, true)
      })
    }
  }, [user])
}
```

#### 时间追踪 (useTimeTracker.ts)

[frontend/src/hooks/useTimeTracker.ts](frontend/src/hooks/useTimeTracker.ts)

追踪用户学习时长，定期保存到后端。

```tsx
export function useTimeTracker({ 
  lessonId, 
  onSaveInterval = 300000,  // 5分钟
  onVisibilityChange = true 
}: TimeTrackerOptions) {
  // 开始追踪
  const startTracking = useCallback(() => {
    startTimeRef.current = new Date()
    isTrackingRef.current = true
  }, [])
  
  // 停止追踪并保存
  const stopTracking = useCallback(() => {
    const sessionTime = endTime.getTime() - startTimeRef.current.getTime()
    saveTime(sessionTime)
  }, [saveTime])
  
  // 页面可见性变化时暂停/恢复
  const handleVisibilityChange = useCallback(() => {
    if (document.hidden) {
      stopTracking()
    } else {
      startTracking()
    }
  }, [startTracking, stopTracking])
  
  // 页面关闭前保存
  const handleBeforeUnload = useCallback(() => {
    navigator.sendBeacon('/api/progress/update-time', JSON.stringify({...}))
  }, [lessonId])
}
```

---

## API接口文档

### 认证接口

| 方法 | 路径 | 描述 | 请求体 | 响应 |
|------|------|------|--------|------|
| POST | /api/auth/register | 用户注册 | `{username, email, password, group}` | `UserResponse` |
| POST | /api/auth/login | 用户登录 | `FormData: username, password` | `{access_token, token_type}` |
| GET | /api/auth/me | 获取当前用户 | - | `UserResponse` |

### 课程接口

| 方法 | 路径 | 描述 | 认证 |
|------|------|------|------|
| GET | /api/courses/modules | 获取模块列表 | 需要 |
| GET | /api/courses/modules/{id} | 获取模块详情 | 需要 |
| GET | /api/courses/modules/{id}/lessons | 获取课时列表 | 需要 |
| GET | /api/courses/lessons/{id} | 获取课时详情 | 需要 |
| GET | /api/courses/content/{path} | 获取课程内容 | 需要 |
| GET | /api/courses/timeline | 获取时间线 | 需要 |

### 进度接口

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | /api/progress | 获取用户进度 |
| POST | /api/progress/{id}/start | 开始学习 |
| POST | /api/progress/{id}/complete | 完成学习 |
| PUT | /api/progress/{id}/time | 更新时长 |
| POST | /api/progress/update-time | 累加时长 |
| POST | /api/progress/{id}/bookmark | 收藏/取消 |

### 仪表盘接口

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | /api/dashboard/stats | 学习统计 |
| GET | /api/dashboard/modules | 模块进度 |
| GET | /api/dashboard/time-stats | 时间统计 |
| GET | /api/dashboard/calendar | 学习日历 |

### 管理员接口

| 方法 | 路径 | 描述 | 权限 |
|------|------|------|------|
| GET | /api/admin/stats | 系统统计 | Admin |
| GET | /api/admin/users | 用户列表 | Admin |
| GET | /api/admin/users/{id}/detail | 用户详情 | Admin |
| PUT | /api/admin/users/{id}/group | 更新分组 | Admin |
| POST | /api/admin/lessons/upload | 上传课程 | Admin |
| GET/PUT | /api/admin/ai-settings | AI设置 | Admin |

---

## 数据流与依赖关系

### 模块依赖图

```
┌─────────────────────────────────────────────────────────────────┐
│                          main.py                                │
│                      (应用入口，路由注册)                         │
└─────────────────────────────────────────────────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
        ▼                       ▼                       ▼
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│    Routers    │     │    Config     │     │    Utils      │
│  (API路由层)   │     │  (配置管理)    │     │  (数据库工具)  │
└───────────────┘     └───────────────┘     └───────────────┘
        │                                           │
        │                                           │
        ▼                                           ▼
┌───────────────┐                         ┌───────────────┐
│   Services    │                         │    Models     │
│  (业务逻辑层)  │                         │  (数据模型)    │
└───────────────┘                         └───────────────┘
        │                                           │
        └───────────────────┬───────────────────────┘
                            │
                            ▼
                  ┌───────────────┐
                  │   Database    │
                  │   (SQLite)    │
                  └───────────────┘
```

### 请求处理流程

```
Client Request
      │
      ▼
┌─────────────────┐
│  Nginx (80)     │
│  反向代理        │
└─────────────────┘
      │
      ├──────────────────────┐
      │                      │
      ▼                      ▼
┌─────────────────┐  ┌─────────────────┐
│  Frontend:3000  │  │  Backend:8000   │
│  React静态资源   │  │  FastAPI API    │
└─────────────────┘  └─────────────────┘
                            │
                            ▼
                     ┌─────────────────┐
                     │  JWT验证        │
                     │  (auth.py)      │
                     └─────────────────┘
                            │
                            ▼
                     ┌─────────────────┐
                     │  Router处理     │
                     │  (业务路由)      │
                     └─────────────────┘
                            │
                            ▼
                     ┌─────────────────┐
                     │  Service处理    │
                     │  (业务逻辑)      │
                     └─────────────────┘
                            │
                            ▼
                     ┌─────────────────┐
                     │  Model/DB操作   │
                     │  (数据持久化)    │
                     └─────────────────┘
```

### 前端数据流

```
User Action
      │
      ▼
┌─────────────────┐
│  Page Component │
│  (页面组件)      │
└─────────────────┘
      │
      ├──────────────────────┐
      │                      │
      ▼                      ▼
┌─────────────────┐  ┌─────────────────┐
│  Service Layer  │  │  Zustand Store  │
│  (API调用)       │  │  (状态管理)      │
└─────────────────┘  └─────────────────┘
      │
      ▼
┌─────────────────┐
│  Axios Instance │
│  (HTTP请求)      │
└─────────────────┘
      │
      ▼
┌─────────────────┐
│  Backend API    │
└─────────────────┘
```

---

## 部署与运行

### 方式一：Docker部署（推荐）

```bash
# 克隆项目
cd ai-learning-platform

# 启动服务
docker-compose up -d

# 访问
# 前端: http://localhost
# API文档: http://localhost:8000/docs
```

**Docker Compose配置**:

```yaml
services:
  backend:
    build: ./backend
    ports: ["8000:8000"]
    volumes:
      - ./data:/app/data
      - ../AI Courses:/app/content:ro
    environment:
      - DATABASE_URL=sqlite:///./data/learning.db
      - SECRET_KEY=${SECRET_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}

  frontend:
    build: ./frontend
    ports: ["3000:3000"]
    depends_on: [backend]

  nginx:
    image: nginx:alpine
    ports: ["80:80"]
    depends_on: [frontend, backend]
```

### 方式二：本地开发

#### 后端启动

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

# 创建管理员账户
python ../scripts/create_admin.py

# 启动服务
uvicorn app.main:app --reload --port 8000
```

#### 前端启动

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build
```

### 数据库初始化

```bash
# 初始化数据库表结构
python scripts/init_db.py

# 创建管理员账户
python scripts/create_admin.py --username admin --password admin123 --email admin@example.com
```

---

## 配置说明

### 环境变量

| 变量 | 描述 | 默认值 |
|------|------|--------|
| DATABASE_URL | 数据库连接 | sqlite:///./data/learning.db |
| SECRET_KEY | JWT密钥 | (需修改) |
| OPENAI_API_KEY | OpenAI API密钥 | (可选) |
| CONTENT_PATH | 课程内容路径 | ../AI Courses |

### 后端配置 (config.py)

```python
class Settings(BaseSettings):
    APP_NAME: str = "AI Learning Platform"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./data/learning.db"
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080  # 7天
    CONTENT_PATH: str = "../AI Courses"
    OPENAI_API_KEY: Optional[str] = None
```

### 前端配置 (vite.config.ts)

```typescript
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
})
```

### Nginx配置

```nginx
server {
    listen 80;
    
    location / {
        proxy_pass http://frontend:3000;
    }
    
    location /api {
        proxy_pass http://backend:8000;
    }
}
```

---

## 附录

### 常用命令

```bash
# 后端
uvicorn app.main:app --reload --port 8000  # 开发模式
uvicorn app.main:app --host 0.0.0.0 --port 8000  # 生产模式

# 前端
npm run dev      # 开发模式
npm run build    # 构建
npm run preview  # 预览构建结果

# Docker
docker-compose up -d        # 启动
docker-compose down         # 停止
docker-compose logs -f      # 查看日志
docker-compose build        # 重新构建
```

### 文件说明

| 文件/目录 | 说明 |
|----------|------|
| backend/course_content/ | 课程Markdown/Notebook文件 |
| data/terms.json | 预定义术语库 |
| data/learning.db | SQLite数据库文件 |
| scripts/ | 工具脚本 |
| deploy/ | 部署相关脚本 |

### 错误排查

| 问题 | 解决方案 |
|------|---------|
| 数据库锁定 | 确保只有一个进程访问SQLite |
| JWT过期 | 重新登录获取新token |
| CORS错误 | 检查后端CORS配置 |
| 文件找不到 | 检查CONTENT_PATH配置 |

---

*文档生成时间: 2026-04-03*
