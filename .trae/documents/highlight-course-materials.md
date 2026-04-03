# 课程列表重点标注参考素材功能计划（增强版）

## 一、需求概述

在课程学习列表中，重点标注课程编排文档中提到的参考素材。具体需求：
- 如果某个课程包含课程编排文档中引用的素材，就把该课程标记为重点学习内容
- 显示素材的关键词/标题（如"原子"、"分子"、"CoT"等）
- 使用特殊符号进行视觉突出

## 二、现状分析

### 课程编排文档结构
```
| 日期 | 主题 | 学习点 | 参考素材 |
|------|------|--------|----------|
| 3月16日 | 原子 + 零/少样本 | ... | **原子** [Context-Engineering-main/00_foundations/01_atoms_prompting.md](...)<br>**分子** [...] |
```

### 素材格式解析
- 格式：`**素材标题** [显示文本](素材路径)`
- 示例：`**原子** [Context-Engineering-main/00_foundations/01_atoms_prompting.md](...)`
- 素材标题是重点标注的关键词（如"原子"、"分子"、"CoT"）

### 数据库存储
- `Lesson.materials` 字段存储素材列表
- 每个素材包含：`title`（素材标题）、`text`（显示文本）、`path`（素材路径）

## 三、技术方案

### 3.1 数据模型扩展

**后端 Lesson 模型新增字段：**
- `materials_count`: 参考素材数量（已实现）
- `material_titles`: 素材标题列表（用于前端展示）

**API 响应扩展：**
```python
class LessonResponse(BaseModel):
    # ... 现有字段
    materials_count: int = 0
    material_titles: List[str] = []  # 新增：素材标题列表
```

### 3.2 前端展示方案

#### ModuleDetail.tsx 课程列表
- 在课程项中显示素材标题标签
- 使用 📚 图标 + 素材关键词标签
- 重点素材使用醒目样式（琥珀色背景 + ✨）

#### 展示效果
```
┌─────────────────────────────────────────────────────┐
│ [✓] 3月16日: 原子 + 零/少样本                        │
│     📚 原子 · 分子 · 最小Prompt · 零样本 · 少样本    │
│     📚✨ 5个参考素材                                 │
└─────────────────────────────────────────────────────┘
```

### 3.3 重点符号设计

| 场景 | 显示效果 | 样式 |
|------|----------|------|
| 有素材 | 📚 原子 · 分子 | 紫色标签 |
| 素材≥3 | 📚✨ 原子 · 分子 · ... | 琥珀色标签 + 星标 |
| 无素材 | 不显示 | - |

## 四、实施步骤

### 阶段一：后端数据扩展

1. **修改 API 响应**
   - 文件：`backend/app/routers/courses.py`
   - 在 `LessonResponse` 中添加 `material_titles` 字段
   - 从 `materials` 中提取 `title` 字段组成列表

### 阶段二：前端展示优化

1. **更新类型定义**
   - 文件：`frontend/src/services/courses.ts`
   - 在 `Lesson` 接口中添加 `material_titles` 字段

2. **修改课程列表页面**
   - 文件：`frontend/src/pages/ModuleDetail.tsx`
   - 在课程项中添加素材标题标签展示
   - 使用醒目的样式和图标

## 五、文件变更清单

### 修改文件

| 文件路径 | 变更内容 |
|----------|----------|
| `backend/app/routers/courses.py` | LessonResponse 添加 material_titles 字段 |
| `frontend/src/services/courses.ts` | Lesson 接口添加 material_titles 字段 |
| `frontend/src/pages/ModuleDetail.tsx` | 课程列表显示素材标题标签 |

## 六、UI 设计细节

### ModuleDetail 课程项

```tsx
// 素材标题标签
{lesson.material_titles && lesson.material_titles.length > 0 && (
  <div className="flex flex-wrap gap-1 mt-2">
    {lesson.material_titles.slice(0, 5).map((title, i) => (
      <span key={i} className={`px-2 py-0.5 text-xs rounded ${
        lesson.materials_count >= 3
          ? 'bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400'
          : 'bg-purple-100 text-purple-700 dark:bg-purple-900/30 dark:text-purple-400'
      }`}>
        {title}
      </span>
    ))}
    {lesson.material_titles.length > 5 && (
      <span className="text-xs text-gray-500">+{lesson.material_titles.length - 5}</span>
    )}
  </div>
)}
```

### 效果示例

```
课程列表项：
┌─────────────────────────────────────────────────────┐
│ [✓] 3月16日: 原子 + 零/少样本                        │
│     Zero-shot vs Few-shot; 分子提示                  │
│     ┌──────┐ ┌──────┐ ┌──────────┐ ┌──────┐ ┌──────┐│
│     │ 原子 │ │ 分子 │ │最小Prompt│ │ 零样本│ │ 少样本││
│     └──────┘ └──────┘ └──────────┘ └──────┘ └──────┘│
│     📚✨ 5个参考素材                                 │
└─────────────────────────────────────────────────────┘
```

## 七、预估工作量

| 任务 | 预估时间 |
|------|----------|
| 后端 API 修改 | 10分钟 |
| 前端类型更新 | 5分钟 |
| ModuleDetail 修改 | 15分钟 |
| 测试验证 | 10分钟 |
| **总计** | **约40分钟** |

## 八、注意事项

1. **素材标题提取**：从 `materials` 数组中提取每个素材的 `title` 字段
2. **显示数量限制**：最多显示5个素材标题，超出显示 "+N"
3. **响应式设计**：标签在小屏幕上应自动换行
4. **暗色模式**：确保暗色模式下标签颜色对比度足够
