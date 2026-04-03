# AI课程内容解析与生成功能计划

## 一、需求概述

管理员上传课程文件后，系统调用AI进行智能解析：
1. 解析文档内容生成课程结构（标题、摘要、主题等）
2. 自动生成知识点（KnowledgePoint）
3. 为每个知识点生成练习题（PracticeQuestion）

## 二、现有系统分析

### 已有组件
- **AI服务层**: `ai_service.py` - 支持OpenAI和本地模型
- **上传接口**: `POST /api/admin/lessons/upload` - 基础文件解析
- **数据模型**: 
  - `Lesson` - 课程
  - `KnowledgePoint` - 知识点
  - `PracticeQuestion` - 练习题

### 需要增强
- 上传接口需要调用AI进行内容解析
- 新增知识点生成逻辑
- 新增练习题生成逻辑

## 三、技术方案

### 3.1 后端实现

#### 3.1.1 创建AI内容解析服务
文件: `backend/app/services/ai_content_generator.py`

```python
class AIContentGenerator:
    def __init__(self, ai_provider):
        self.ai_provider = ai_provider
    
    def parse_course_content(self, raw_content: str) -> dict:
        """解析课程内容，返回结构化数据"""
        
    def generate_knowledge_points(self, content: str, count: int = 5) -> list:
        """生成知识点列表"""
        
    def generate_practice_questions(self, knowledge_point: dict, count: int = 3) -> list:
        """为知识点生成练习题"""
```

#### 3.1.2 更新上传接口
文件: `backend/app/routers/admin.py`

修改 `upload_lesson` 接口：
1. 解析文档内容
2. 调用AI生成课程结构
3. 创建Lesson记录
4. 调用AI生成知识点
5. 创建KnowledgePoint记录
6. 为每个知识点生成练习题
7. 创建PracticeQuestion记录

#### 3.1.3 API响应结构
```json
{
  "id": "lesson-uuid",
  "title": "AI生成的标题",
  "summary": "AI生成的摘要",
  "topics": ["主题1", "主题2"],
  "knowledge_points": [
    {
      "id": "kp-uuid",
      "title": "知识点标题",
      "description": "知识点描述",
      "questions_count": 3
    }
  ],
  "questions_count": 15,
  "message": "课程创建成功，已生成X个知识点和Y道练习题"
}
```

### 3.2 前端实现

#### 3.2.1 更新上传模态框
文件: `frontend/src/pages/AdminCourses.tsx`

增强上传结果展示：
- 显示AI生成的知识点列表
- 显示生成的练习题数量
- 支持预览知识点和练习题

#### 3.2.2 新增预览组件
- KnowledgePointPreview: 知识点预览
- QuestionPreview: 练习题预览

## 四、AI Prompt设计

### 4.1 课程内容解析Prompt
```
你是一个专业的课程内容分析师。请分析以下课程内容，提取关键信息：

课程内容：
{content}

请以JSON格式返回：
{
  "title": "课程标题",
  "summary": "课程摘要（100-200字）",
  "topics": ["主题1", "主题2", "主题3"],
  "difficulty": "basic/intermediate/advanced",
  "time_estimate": 预计学习时间（分钟）,
  "key_concepts": ["核心概念1", "核心概念2"]
}
```

### 4.2 知识点生成Prompt
```
基于以下课程内容，生成{count}个知识点：

课程内容：
{content}

请以JSON数组格式返回知识点：
[
  {
    "title": "知识点标题",
    "description": "详细描述",
    "category": "分类",
    "importance": 1-5,
    "key_concepts": ["关键概念"],
    "examples": ["示例说明"]
  }
]
```

### 4.3 练习题生成Prompt
```
基于以下知识点，生成{count}道练习题：

知识点：
{knowledge_point}

请以JSON数组格式返回练习题：
[
  {
    "question_type": "single_choice/multiple_choice/fill_blank/short_answer",
    "question_text": "题目内容",
    "options": ["选项A", "选项B", "选项C", "选项D"],
    "correct_answer": "正确答案",
    "explanation": "答案解析",
    "difficulty": 1-3
  }
]
```

## 五、任务清单

### 后端任务
1. [ ] 创建 `ai_content_generator.py` AI内容生成服务
2. [ ] 实现课程内容解析方法
3. [ ] 实现知识点生成方法
4. [ ] 实现练习题生成方法
5. [ ] 更新 `admin.py` 上传接口，集成AI解析
6. [ ] 添加批量创建知识点和练习题的逻辑

### 前端任务
7. [ ] 更新上传结果展示，显示AI生成的内容
8. [ ] 添加知识点预览组件
9. [ ] 添加练习题预览组件
10. [ ] 优化加载状态和错误处理

## 六、错误处理

1. **AI未配置**: 提示用户先配置AI设置
2. **AI调用失败**: 回退到基础解析，记录错误日志
3. **JSON解析失败**: 重试或使用默认值
4. **超时处理**: 设置合理的超时时间，提供进度反馈

## 七、性能优化

1. 异步处理：AI生成过程使用后台任务
2. 缓存机制：相同内容不重复调用AI
3. 批量生成：知识点和练习题批量创建
4. 进度反馈：WebSocket或轮询显示生成进度

## 八、测试要点

1. 不同格式文档上传测试（md, ipynb, txt）
2. AI配置状态测试（未配置/OpenAI/本地模型）
3. 大文件处理测试
4. 知识点和练习题质量验证
