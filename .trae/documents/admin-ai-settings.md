# 管理员AI API Key设置功能计划

## 一、需求概述

为管理员添加AI配置功能：
1. 设置OpenAI API Key
2. 选择使用云端AI（OpenAI）或本地大模型
3. 配置本地大模型地址（如Ollama）

## 二、现状分析

### 现有配置
- `config.py`: 从环境变量读取 `OPENAI_API_KEY`
- 配置存储在 `.env` 文件中
- 无数据库持久化配置

### 需要扩展
- 数据库存储AI配置
- 支持多种AI后端
- 管理员界面配置

## 三、技术方案

### 3.1 数据模型

**新增 SystemSettings 表：**
```python
class AISettings(Base):
    __tablename__ = "ai_settings"
    
    id = Column(String, primary_key=True, default="default")
    provider = Column(String, default="openai")  # openai, local, none
    openai_api_key = Column(String, nullable=True)
    openai_base_url = Column(String, nullable=True)  # 自定义API地址
    local_model_url = Column(String, nullable=True)  # 本地模型地址
    local_model_name = Column(String, nullable=True)  # 模型名称
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

### 3.2 后端API设计

```
GET /api/admin/ai-settings
Response: {
  provider: string,
  openai_api_key: string (masked),
  openai_base_url: string,
  local_model_url: string,
  local_model_name: string
}

PUT /api/admin/ai-settings
Body: {
  provider: string,
  openai_api_key: string,
  openai_base_url: string,
  local_model_url: string,
  local_model_name: string
}

POST /api/admin/ai-settings/test
Body: { provider: string }
Response: { success: boolean, message: string }
```

### 3.3 AI服务抽象

```python
class AIProvider:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError

class OpenAIProvider(AIProvider):
    def __init__(self, api_key: str, base_url: str = None):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
    
    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(...)
        return response.choices[0].message.content

class LocalModelProvider(AIProvider):
    def __init__(self, url: str, model_name: str):
        self.url = url
        self.model_name = model_name
    
    def generate(self, prompt: str) -> str:
        # 调用本地模型API (如Ollama)
        response = requests.post(f"{self.url}/api/generate", ...)
        return response.json()["response"]
```

### 3.4 前端页面设计

```
┌─────────────────────────────────────────────────────────────────┐
│ AI设置                                                    [保存] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ AI提供商                                                        │
│ ○ OpenAI (云端)                                                │
│ ○ 本地大模型 (Ollama等)                                         │
│ ○ 禁用AI功能                                                    │
│                                                                 │
│ ─── OpenAI 设置 ─────────────────────────────────────────────── │
│ API Key                                                         │
│ [sk-**********************] [显示]                              │
│                                                                 │
│ API Base URL (可选，用于代理)                                    │
│ [https://api.openai.com/v1]                                     │
│                                                                 │
│ ─── 本地模型设置 ─────────────────────────────────────────────── │
│ 服务地址                                                        │
│ [http://localhost:11434]                                        │
│                                                                 │
│ 模型名称                                                        │
│ [llama2]                                                        │
│                                                                 │
│ [测试连接]                                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 四、实施步骤

### 阶段一：后端开发

1. **创建数据模型**
   - 文件：`backend/app/models/models.py`
   - 添加 `AISettings` 表

2. **创建AI服务**
   - 文件：`backend/app/services/ai_service.py`
   - 实现 OpenAI 和本地模型提供者
   - 实现配置读取和切换

3. **创建管理API**
   - 文件：`backend/app/routers/admin.py`
   - 添加AI设置CRUD接口
   - 添加连接测试接口

### 阶段二：前端开发

1. **创建AI设置页面**
   - 文件：`frontend/src/pages/AdminAISettings.tsx`
   - 表单：提供商选择、API配置、测试连接

2. **更新路由和导航**
   - 文件：`frontend/src/App.tsx`
   - 文件：`frontend/src/components/Layout.tsx`

## 五、文件变更清单

### 新增文件

| 文件路径 | 描述 |
|----------|------|
| `backend/app/services/ai_service.py` | AI服务抽象层 |
| `frontend/src/pages/AdminAISettings.tsx` | AI设置页面 |

### 修改文件

| 文件路径 | 变更内容 |
|----------|----------|
| `backend/app/models/models.py` | 添加AISettings模型 |
| `backend/app/routers/admin.py` | 添加AI设置API |
| `frontend/src/services/admin.ts` | 添加AI设置API方法 |
| `frontend/src/App.tsx` | 添加AI设置路由 |
| `frontend/src/components/Layout.tsx` | 添加AI设置导航 |

## 六、安全考虑

1. **API Key加密存储**：使用加密存储API Key
2. **前端掩码显示**：API Key只显示前4位和后4位
3. **权限控制**：仅管理员可访问设置
4. **测试连接**：保存前可测试连接有效性

## 七、预估工作量

| 任务 | 预估时间 |
|------|----------|
| 后端数据模型 | 10分钟 |
| AI服务实现 | 30分钟 |
| 后端API | 20分钟 |
| 前端页面 | 30分钟 |
| 测试验证 | 15分钟 |
| **总计** | **约2小时** |

## 八、支持的本地模型

- **Ollama**: `http://localhost:11434`
- **LM Studio**: `http://localhost:1234`
- **vLLM**: `http://localhost:8000`
- **其他兼容OpenAI API的服务**
