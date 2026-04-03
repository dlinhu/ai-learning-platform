# AI解析上传文件内容为课程内容计划

## 一、需求概述

在AI内容生成服务中追加功能：
- 解析上传文件的内容
- 将内容转换为结构化的课程内容（章节、段落、代码示例等）
- 在课程详情页展示这些AI生成的内容

## 二、现有系统分析

### 当前问题
1. 上传文件后，`raw_content` 存储原始文本，但未转换为结构化内容
2. 课程详情页依赖 `materials` 字段展示内容，上传的课程没有 materials
3. AI只生成了知识点和练习题，没有生成课程正文内容

### 数据模型
- `Lesson.raw_content` - 存储原始文件内容
- `Lesson.materials` - 课程素材列表（当前上传的课程为空）
- `Lesson.summary` - 课程摘要

## 三、技术方案

### 3.1 后端实现

#### 3.1.1 新增AI方法：生成结构化课程内容
文件: `backend/app/services/ai_content_generator.py`

新增方法：
```python
def generate_lesson_content(self, raw_content: str) -> Dict[str, Any]:
    """
    将原始内容转换为结构化课程内容
    返回格式：
    {
        "sections": [
            {
                "title": "章节标题",
                "content": "章节内容（Markdown格式）",
                "type": "text/code/example"
            }
        ]
    }
    """
```

#### 3.1.2 更新Lesson模型
在 `models.py` 中添加字段：
- `structured_content` - JSON字段，存储AI生成的结构化内容

#### 3.1.3 更新上传接口
在 `admin.py` 的 `upload_lesson` 中：
1. 调用AI生成结构化内容
2. 存储到 `structured_content` 字段

#### 3.1.4 更新课程详情API
在 `courses.py` 的 `get_lesson` 中：
- 返回 `structured_content` 字段

### 3.2 前端实现

#### 3.2.1 更新LessonDetail组件
文件: `frontend/src/pages/LessonDetail.tsx`

修改"课程内容"标签页：
- 如果有 materials，展示 materials
- 如果没有 materials 但有 structured_content，展示AI生成的内容
- 支持Markdown渲染

#### 3.2.2 更新类型定义
文件: `frontend/src/services/courses.ts`

添加 `structured_content` 字段到 `Lesson` 接口

## 四、AI Prompt设计

### 课程内容结构化Prompt
```
你是一个专业的课程内容编辑。请将以下课程原始内容转换为结构化的课程内容。

原始内容：
{raw_content}

请严格按照以下JSON格式返回：
{
  "sections": [
    {
      "title": "章节标题",
      "content": "章节内容，使用Markdown格式，包含详细的解释说明",
      "type": "text",
      "order": 1
    },
    {
      "title": "代码示例",
      "content": "```python\n# 代码示例\n```",
      "type": "code",
      "order": 2
    }
  ]
}

要求：
1. 将内容合理分段，每段一个section
2. type可以是：text（文本）、code（代码）、example（示例）、summary（总结）
3. content使用Markdown格式，便于渲染
4. 保持原文的核心内容，适当补充解释
5. 章节标题要简洁明了
```

## 五、任务清单

### 后端任务
1. [ ] 在 `ai_content_generator.py` 添加 `generate_lesson_content` 方法
2. [ ] 更新 `models.py` 添加 `structured_content` 字段
3. [ ] 运行数据库迁移
4. [ ] 更新 `admin.py` 上传接口调用新方法
5. [ ] 更新 `courses.py` API返回结构化内容

### 前端任务
6. [ ] 更新 `courses.ts` 类型定义
7. [ ] 更新 `LessonDetail.tsx` 展示结构化内容
8. [ ] 测试验证

## 六、数据结构

### structured_content 结构
```json
{
  "sections": [
    {
      "title": "概述",
      "content": "## 本节要点\n\n本节介绍...",
      "type": "text",
      "order": 1
    },
    {
      "title": "核心概念",
      "content": "### 概念1\n\n解释...\n\n### 概念2\n\n解释...",
      "type": "text",
      "order": 2
    },
    {
      "title": "代码示例",
      "content": "```python\ndef example():\n    pass\n```",
      "type": "code",
      "order": 3
    },
    {
      "title": "总结",
      "content": "本节学习了...",
      "type": "summary",
      "order": 4
    }
  ]
}
```

## 七、展示效果

课程内容页面将展示：
1. 章节导航（左侧或顶部）
2. 当前章节内容（Markdown渲染）
3. 代码高亮显示
4. 支持暗色模式
