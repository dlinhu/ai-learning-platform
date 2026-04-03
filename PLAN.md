# 管理员统计功能开发计划

## 一、需求概述

为管理员添加统计系统中所有注册人员学习时长和进度的展示功能。

## 二、现有系统分析

### 已有基础设施
- 用户角色系统：`UserRole.STUDENT` / `UserRole.ADMIN`
- 学习进度模型：`Progress` 包含 `time_spent`, `status`, `started_at`, `completed_at`
- 现有管理员API：`/api/dashboard/admin/all-progress`（仅返回基础进度数据）
- 前端认证状态：`useAuthStore` 包含用户角色信息

### 需要扩展的部分
1. 后端API需要增强，提供更详细的统计数据
2. 前端需要新增管理员仪表盘页面

## 三、技术方案

### 3.1 后端API扩展

#### 新增API端点

| 端点 | 方法 | 描述 |
|------|------|------|
| `/api/admin/stats` | GET | 获取系统整体统计概览 |
| `/api/admin/users` | GET | 获取所有用户学习详情列表（支持分页/排序/筛选） |
| `/api/admin/users/{user_id}/detail` | GET | 获取单个用户详细学习记录 |

#### 数据模型

**系统统计概览响应：**
```python
class AdminStatsResponse(BaseModel):
    total_users: int                    # 总用户数
    active_users_today: int             # 今日活跃用户数
    active_users_week: int              # 本周活跃用户数
    total_time_spent: int               # 全平台总学习时长（分钟）
    avg_time_per_user: float            # 人均学习时长
    total_completions: int              # 总完成课程数
    avg_completion_rate: float          # 平均完成率
```

**用户学习详情：**
```python
class UserLearningDetail(BaseModel):
    user_id: str
    username: str
    email: str
    role: str
    created_at: datetime
    total_time_spent: int               # 总学习时长（分钟）
    completed_lessons: int              # 已完成课程数
    in_progress_lessons: int            # 进行中课程数
    completion_rate: float              # 完成率
    last_active: Optional[datetime]     # 最后活跃时间
    current_streak: int                 # 当前连续学习天数
    module_progress: List[dict]         # 各模块进度
```

### 3.2 前端页面设计

#### 新增页面
- **管理员仪表盘** (`/admin`)

#### 页面功能模块

1. **统计概览卡片**
   - 总用户数
   - 今日活跃用户
   - 本周活跃用户
   - 全平台总学习时长
   - 平均完成率

2. **用户学习数据表格**
   - 列：用户名、邮箱、学习时长、完成课程、完成率、最后活跃、操作
   - 支持排序（按学习时长、完成率等）
   - 支持搜索（用户名/邮箱）
   - 支持分页

3. **用户详情弹窗**
   - 各模块学习进度可视化
   - 学习时长分布
   - 学习日历热力图

4. **数据可视化图表**
   - 用户学习时长分布柱状图
   - 模块完成率对比图

### 3.3 权限控制

- 路由守卫：检查 `user.role === 'admin'`
- API权限：后端验证 `current_user.role == "admin"`

## 四、实施步骤

### 阶段一：后端API开发（优先级：高）

1. **创建管理员路由模块**
   - 文件：`backend/app/routers/admin.py`
   - 实现权限验证装饰器

2. **实现统计API**
   - `/api/admin/stats` - 系统整体统计
   - `/api/admin/users` - 用户列表（含分页、排序、搜索）
   - `/api/admin/users/{user_id}/detail` - 用户详情

3. **注册路由**
   - 在 `main.py` 中注册管理员路由

### 阶段二：前端页面开发（优先级：高）

1. **创建管理员服务**
   - 文件：`frontend/src/services/admin.ts`
   - 封装管理员API调用

2. **创建管理员仪表盘页面**
   - 文件：`frontend/src/pages/AdminDashboard.tsx`
   - 实现统计概览组件
   - 实现用户数据表格组件
   - 实现用户详情弹窗组件

3. **更新路由配置**
   - 在 `App.tsx` 添加管理员路由
   - 添加管理员路由守卫

4. **更新导航菜单**
   - 在 `Layout.tsx` 中为管理员用户显示管理入口

### 阶段三：优化与测试（优先级：中）

1. **性能优化**
   - 添加API缓存
   - 实现数据懒加载

2. **用户体验优化**
   - 添加加载状态
   - 添加错误处理
   - 添加数据刷新功能

## 五、文件变更清单

### 新增文件
| 文件路径 | 描述 |
|----------|------|
| `backend/app/routers/admin.py` | 管理员API路由 |
| `frontend/src/services/admin.ts` | 管理员API服务 |
| `frontend/src/pages/AdminDashboard.tsx` | 管理员仪表盘页面 |

### 修改文件
| 文件路径 | 变更内容 |
|----------|----------|
| `backend/app/main.py` | 注册管理员路由 |
| `frontend/src/App.tsx` | 添加管理员路由 |
| `frontend/src/components/Layout.tsx` | 添加管理入口导航 |

## 六、数据库影响

无需修改数据库结构，现有模型已包含所需字段：
- `User`: 用户基本信息
- `Progress`: 学习进度、时长
- `Lesson`: 课程信息

## 七、API详细设计

### 7.1 GET /api/admin/stats

**响应示例：**
```json
{
  "total_users": 50,
  "active_users_today": 12,
  "active_users_week": 35,
  "total_time_spent": 12500,
  "avg_time_per_user": 250.5,
  "total_completions": 380,
  "avg_completion_rate": 42.3
}
```

### 7.2 GET /api/admin/users

**查询参数：**
| 参数 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| page | int | 1 | 页码 |
| per_page | int | 20 | 每页数量 |
| sort_by | string | time_spent | 排序字段 |
| order | string | desc | 排序方向 |
| search | string | - | 搜索关键词 |

**响应示例：**
```json
{
  "users": [
    {
      "user_id": "uuid",
      "username": "student1",
      "email": "student1@example.com",
      "role": "student",
      "created_at": "2024-01-15T10:00:00",
      "total_time_spent": 450,
      "completed_lessons": 15,
      "in_progress_lessons": 3,
      "completion_rate": 29.4,
      "last_active": "2024-01-20T15:30:00",
      "current_streak": 5
    }
  ],
  "total": 50,
  "page": 1,
  "per_page": 20,
  "total_pages": 3
}
```

### 7.3 GET /api/admin/users/{user_id}/detail

**响应示例：**
```json
{
  "user_id": "uuid",
  "username": "student1",
  "email": "student1@example.com",
  "total_time_spent": 450,
  "completed_lessons": 15,
  "completion_rate": 29.4,
  "module_progress": [
    {
      "module_id": "prompts",
      "module_name": "Prompts 提示词工程",
      "completed": 3,
      "total": 5,
      "time_spent": 120
    }
  ],
  "recent_activities": [
    {
      "lesson_id": "uuid",
      "lesson_title": "Day 1: Zero-shot Prompting",
      "status": "completed",
      "time_spent": 45,
      "completed_at": "2024-01-20T15:30:00"
    }
  ],
  "calendar_data": [
    {"date": "2024-01-20", "time_spent": 60, "lessons": 2}
  ]
}
```

## 八、前端组件结构

```
AdminDashboard/
├── StatsCards          # 统计概览卡片
├── UsersTable          # 用户数据表格
│   ├── SearchBar       # 搜索栏
│   ├── SortControls    # 排序控制
│   └── Pagination      # 分页控件
├── UserDetailModal     # 用户详情弹窗
│   ├── ModuleProgressChart  # 模块进度图
│   ├── TimeDistribution     # 时长分布
│   └── ActivityCalendar     # 活动日历
└── ChartsSection       # 图表区域
    ├── TimeDistributionChart  # 学习时长分布
    └── ModuleCompletionChart  # 模块完成率对比
```

## 九、预估工作量

| 任务 | 预估时间 |
|------|----------|
| 后端API开发 | 1-2小时 |
| 前端页面开发 | 2-3小时 |
| 测试与优化 | 1小时 |
| **总计** | **4-6小时** |

## 十、风险与注意事项

1. **权限安全**：确保所有管理员API都进行权限验证
2. **性能考虑**：用户量大时需要添加分页和索引优化
3. **数据隐私**：管理员查看用户数据需符合隐私政策
4. **响应式设计**：管理后台需支持不同屏幕尺寸
