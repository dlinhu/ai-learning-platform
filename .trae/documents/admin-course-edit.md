# 管理员课程编辑功能计划

## 一、需求概述

为管理员添加课程编辑功能，包括：
1. 编辑课程标签（topics）
2. 编辑模块名称
3. 新增课程（上传文档用AI解析成课程）

## 二、现状分析

### 数据模型
- `Module`: 模块（id, name, description, order_index）
- `Lesson`: 课程（id, module_id, date, title, topics, difficulty, time_estimate, materials, summary）
- `KnowledgePoint`: 知识点
- `Term`: 术语

### 现有服务
- `content_parser.py`: 解析Markdown、Jupyter Notebook、Python文件
- `config.py`: 已配置 `OPENAI_API_KEY`（可选）

### 现有管理员功能
- 用户管理（查看、修改分组）
- 统计数据查看

## 三、技术方案

### 3.1 后端API设计

#### 编辑课程
```
PUT /api/admin/lessons/{lesson_id}
Body: {
  title: string,
  topics: string[],
  difficulty: string,
  time_estimate: number,
  summary: string
}
```

#### 编辑模块
```
PUT /api/admin/modules/{module_id}
Body: {
  name: string,
  description: string,
  order_index: number
}
```

#### 新增课程（AI解析）
```
POST /api/admin/lessons/upload
Content-Type: multipart/form-data
Body: {
  module_id: string,
  file: File,
  title: string (可选),
  date: string (可选)
}
Response: {
  lesson_id: string,
  title: string,
  summary: string,
  topics: string[],
  knowledge_points: KnowledgePoint[],
  materials: Material[]
}
```

#### 删除课程
```
DELETE /api/admin/lessons/{lesson_id}
```

#### 新增模块
```
POST /api/admin/modules
Body: {
  name: string,
  description: string
}
```

### 3.2 AI解析流程

```
上传文档 → 解析文档 → AI提取结构 → 创建课程 → 返回结果
    ↓          ↓           ↓
  .md/.ipynb  content_parser  OpenAI API
```

**AI解析Prompt设计：**
```
请分析以下文档内容，提取课程信息：
1. 课程标题
2. 学习主题标签（3-5个）
3. 课程摘要（200字以内）
4. 难度等级（basic/intermediate/advanced）
5. 预估学习时间（分钟）
6. 知识点列表

文档内容：
{content}
```

### 3.3 前端页面设计

#### 管理员课程管理页面
- 路由：`/admin/courses`
- 功能：模块列表、课程列表、编辑、新增、删除

#### 课程编辑弹窗
- 编辑标题、标签、难度、时长、摘要
- 标签支持添加/删除

#### 课程上传弹窗
- 选择模块
- 上传文件（.md, .ipynb, .txt）
- AI解析进度显示
- 预览解析结果
- 确认创建

## 四、实施步骤

### 阶段一：后端API开发

1. **创建课程管理API**
   - 文件：`backend/app/routers/admin.py`
   - 添加课程CRUD接口
   - 添加模块CRUD接口

2. **实现AI解析服务**
   - 文件：`backend/app/services/ai_parser.py`
   - 调用OpenAI API解析文档
   - 提取课程结构信息

3. **文件上传处理**
   - 使用FastAPI的`UploadFile`
   - 支持.md, .ipynb, .txt格式

### 阶段二：前端页面开发

1. **创建课程管理页面**
   - 文件：`frontend/src/pages/AdminCourses.tsx`
   - 模块和课程的树形展示
   - 编辑、删除按钮

2. **创建编辑弹窗组件**
   - 文件：`frontend/src/components/LessonEditModal.tsx`
   - 表单：标题、标签、难度、时长、摘要

3. **创建上传弹窗组件**
   - 文件：`frontend/src/components/LessonUploadModal.tsx`
   - 文件上传、AI解析、结果预览

4. **更新路由和导航**
   - 文件：`frontend/src/App.tsx`
   - 文件：`frontend/src/components/Layout.tsx`

## 五、文件变更清单

### 新增文件

| 文件路径 | 描述 |
|----------|------|
| `backend/app/services/ai_parser.py` | AI解析服务 |
| `frontend/src/pages/AdminCourses.tsx` | 课程管理页面 |
| `frontend/src/components/LessonEditModal.tsx` | 课程编辑弹窗 |
| `frontend/src/components/LessonUploadModal.tsx` | 课程上传弹窗 |

### 修改文件

| 文件路径 | 变更内容 |
|----------|----------|
| `backend/app/routers/admin.py` | 添加课程和模块管理API |
| `frontend/src/services/admin.ts` | 添加课程管理API方法 |
| `frontend/src/App.tsx` | 添加课程管理路由 |
| `frontend/src/components/Layout.tsx` | 添加课程管理导航入口 |

## 六、UI设计

### 课程管理页面

```
┌─────────────────────────────────────────────────────────────────┐
│ 课程管理                                    [+ 新增模块] [↑ 上传课程] │
├─────────────────────────────────────────────────────────────────┤
│ ┌─ Prompts 提示词工程 ───────────────────────── [编辑] [删除] ─┐│
│ │  ┌─ 3月16日: 原子 + 零/少样本 ──── [编辑] [删除] ─────────┐ ││
│ │  │  标签: Zero-shot, Few-shot, 原子提示                    │ ││
│ │  └────────────────────────────────────────────────────────┘ ││
│ │  ┌─ 3月17日: CoT + 角色 ───────── [编辑] [删除] ─────────┐  ││
│ │  │  标签: CoT, 角色, 约束                                  │ ││
│ │  └────────────────────────────────────────────────────────┘ ││
│ └─────────────────────────────────────────────────────────────┘│
│ ┌─ RAG 检索增强生成 ─────────────────────────── [编辑] [删除] ─┐│
│ │  ...                                                        ││
│ └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

### 课程编辑弹窗

```
┌─────────────────────────────────────────┐
│ 编辑课程                          [×]  │
├─────────────────────────────────────────┤
│ 课程标题                                │
│ [________________________]              │
│                                         │
│ 标签（逗号分隔）                         │
│ [Zero-shot, Few-shot, 原子提示]         │
│                                         │
│ 难度                                    │
│ [▼ 基础        ]                        │
│                                         │
│ 预估时长（分钟）                         │
│ [60]                                    │
│                                         │
│ 摘要                                    │
│ [________________________]              │
│ [________________________]              │
│                                         │
│           [取消]  [保存]                │
└─────────────────────────────────────────┘
```

### 课程上传弹窗

```
┌─────────────────────────────────────────┐
│ 上传课程                          [×]  │
├─────────────────────────────────────────┤
│ 选择模块                                │
│ [▼ Prompts 提示词工程]                  │
│                                         │
│ 上传文件                                │
│ ┌─────────────────────────────────────┐│
│ │     拖拽文件到此处或点击上传          ││
│ │     支持 .md, .ipynb, .txt          ││
│ └─────────────────────────────────────┘│
│                                         │
│ 课程日期（可选）                         │
│ [3月20日]                               │
│                                         │
│           [取消]  [上传并解析]          │
└─────────────────────────────────────────┘

AI解析中...
┌─────────────────────────────────────────┐
│ 正在解析文档...                         │
│ ████████████░░░░░░░░ 60%               │
└─────────────────────────────────────────┘

解析结果预览
┌─────────────────────────────────────────┐
│ 标题: Day 1: Zero-shot Prompting       │
│ 标签: Zero-shot, Prompt, AI             │
│ 难度: 基础                              │
│ 时长: 45分钟                            │
│ 摘要: 本课程介绍Zero-shot提示技术...    │
│                                         │
│ 知识点:                                 │
│ • Zero-shot定义                         │
│ • 提示词设计原则                        │
│                                         │
│           [取消]  [确认创建]            │
└─────────────────────────────────────────┘
```

## 七、预估工作量

| 任务 | 预估时间 |
|------|----------|
| 后端课程CRUD API | 30分钟 |
| AI解析服务 | 30分钟 |
| 前端课程管理页面 | 45分钟 |
| 编辑弹窗组件 | 20分钟 |
| 上传弹窗组件 | 30分钟 |
| 测试验证 | 20分钟 |
| **总计** | **约3小时** |

## 八、注意事项

1. **AI解析限制**：如果未配置OPENAI_API_KEY，使用基础解析（仅提取标题和内容）
2. **文件大小限制**：上传文件限制为10MB
3. **权限控制**：所有课程管理API仅管理员可访问
4. **数据验证**：编辑时验证必填字段
5. **删除确认**：删除课程前需确认，同时删除关联的进度记录
