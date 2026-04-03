# 修复课程列表500错误计划

## 一、问题分析

课程列表接口 `/api/courses/modules` 返回500错误，可能原因：

1. **structured_content字段问题**：`LessonResponse` 模型添加了 `structured_content` 字段，但 `get_module_lessons` 函数未返回该字段
2. **数据库连接问题**：数据库初始化或连接异常
3. **配置问题**：`ContentRenderer` 初始化可能出错

## 二、排查步骤

### 步骤1：测试后端启动
```bash
cd backend
python -c "from app.main import app; print('App loaded successfully')"
```

### 步骤2：检查数据库
```bash
cd backend
python init_db.py
```

### 步骤3：检查具体接口错误
直接调用接口查看详细错误

## 三、修复方案

### 修复1：统一LessonResponse返回字段

**问题位置**：`courses.py` 第158-171行 `get_module_lessons` 函数

**修复内容**：在返回的 `LessonResponse` 中添加 `structured_content` 字段

```python
result.append(LessonResponse(
    id=lesson.id,
    module_id=lesson.module_id,
    date=lesson.date,
    title=lesson.title,
    topics=lesson.topics or [],
    difficulty=lesson.difficulty,
    time_estimate=lesson.time_estimate,
    materials=[MaterialResponse(**m) for m in (lesson.materials or [])],
    materials_count=len(lesson.materials or []),
    material_titles=[m.get('title') for m in (lesson.materials or [])],
    summary=lesson.summary,
    progress_status=progress.status if progress else "not_started",
    knowledge_points=[],  # get_module_lessons不返回详细知识点
    terms=[],  # get_module_lessons不返回详细术语
    structured_content=lesson.structured_content  # 添加此行
))
```

### 修复2：确保数据类型一致

`structured_content` 在Pydantic模型中定义为 `Optional[dict] = None`，需要确保：
- 数据库返回的None值被正确处理
- JSON字段被正确序列化

### 修复3：数据库迁移

如果 `structured_content` 列不存在，需要重新运行数据库迁移：
```python
# 在 init_db.py 中确保所有表都创建
from app.models.models import Base
Base.metadata.create_all(bind=engine)
```

## 四、执行清单

1. [ ] 检查后端能否正常启动
2. [ ] 检查数据库表是否完整
3. [ ] 修复 `get_module_lessons` 函数，添加 `structured_content` 字段
4. [ ] 重启后端服务
5. [ ] 测试接口是否正常

## 五、文件变更

| 文件 | 变更内容 |
|------|---------|
| `backend/app/routers/courses.py` | 在 `get_module_lessons` 函数的 `LessonResponse` 返回中添加 `structured_content` 字段 |
| `backend/init_db.py` | 确保数据库迁移完整 |
