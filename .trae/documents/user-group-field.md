# 用户Group字段添加计划

## 一、需求概述

为用户添加`group`字段，支持6个分组（group1-6），用户注册时需要选择分组，方便后续按分组统计数据。

## 二、现状分析

### 后端结构
- `User` 模型位于 `backend/app/models/models.py`
- 注册API位于 `backend/app/routers/auth.py`
- 用户响应模型 `UserResponse` 包含 id, username, email, role, created_at

### 前端结构
- 登录/注册页面：`frontend/src/pages/Login.tsx`
- 用户类型定义：`frontend/src/services/auth.ts` 和 `frontend/src/stores/authStore.ts`
- 注册API调用：`authApi.register(username, email, password)`

## 三、技术方案

### 3.1 后端修改

**User模型扩展：**
```python
class UserGroup(str, enum.Enum):
    GROUP_1 = "group1"
    GROUP_2 = "group2"
    GROUP_3 = "group3"
    GROUP_4 = "group4"
    GROUP_5 = "group5"
    GROUP_6 = "group6"

class User(Base):
    # ... 现有字段
    group = Column(String, default=UserGroup.GROUP_1.value)
```

**API修改：**
- `UserCreate`: 添加 `group` 字段（必填）
- `UserResponse`: 添加 `group` 字段
- 注册接口：保存用户分组

### 3.2 前端修改

**类型定义扩展：**
```typescript
interface User {
  id: string
  username: string
  email: string
  role: string
  group: string  // 新增
  created_at: string
}
```

**注册表单：**
- 添加分组选择下拉框
- 6个选项：Group 1 - Group 6

### 3.3 管理员统计扩展（可选）

在管理员统计API中添加按分组统计的功能：
- 每个分组的学习时长统计
- 每个分组的完成率统计

## 四、实施步骤

### 阶段一：后端修改

1. **修改 User 模型**
   - 文件：`backend/app/models/models.py`
   - 添加 `UserGroup` 枚举
   - 添加 `group` 字段

2. **修改认证API**
   - 文件：`backend/app/routers/auth.py`
   - `UserCreate` 添加 `group` 字段
   - `UserResponse` 添加 `group` 字段
   - 注册逻辑保存 `group`

3. **修改管理员API**
   - 文件：`backend/app/routers/admin.py`
   - 用户列表返回 `group` 字段
   - 统计API添加按分组统计

### 阶段二：前端修改

1. **更新类型定义**
   - 文件：`frontend/src/services/auth.ts`
   - 文件：`frontend/src/stores/authStore.ts`
   - 添加 `group` 字段

2. **修改注册表单**
   - 文件：`frontend/src/pages/Login.tsx`
   - 添加分组选择下拉框

3. **更新管理员页面**
   - 文件：`frontend/src/pages/AdminDashboard.tsx`
   - 用户列表显示分组
   - 添加按分组筛选功能

### 阶段三：数据库迁移

由于使用SQLite，需要处理现有数据：
- 方案1：删除数据库重新创建（开发环境）
- 方案2：手动ALTER TABLE添加字段

## 五、文件变更清单

### 后端修改

| 文件路径 | 变更内容 |
|----------|----------|
| `backend/app/models/models.py` | 添加UserGroup枚举，User模型添加group字段 |
| `backend/app/routers/auth.py` | UserCreate/UserResponse添加group字段 |
| `backend/app/routers/admin.py` | 用户列表和统计添加group支持 |

### 前端修改

| 文件路径 | 变更内容 |
|----------|----------|
| `frontend/src/services/auth.ts` | User接口添加group字段 |
| `frontend/src/stores/authStore.ts` | User接口添加group字段 |
| `frontend/src/pages/Login.tsx` | 注册表单添加分组选择 |
| `frontend/src/pages/AdminDashboard.tsx` | 用户列表显示分组，添加分组筛选 |

## 六、UI 设计

### 注册表单分组选择

```
┌─────────────────────────────────────────┐
│  用户名                                 │
│  [________________]                     │
│                                         │
│  邮箱                                   │
│  [________________]                     │
│                                         │
│  分组 *                                 │
│  [▼ Group 1                    ]       │
│                                         │
│  密码                                   │
│  [________________]                     │
│                                         │
│  [注册]                                 │
└─────────────────────────────────────────┘
```

### 管理员页面分组显示

```
┌─────────────────────────────────────────────────────┐
│ 用户名     邮箱           分组      学习时长  完成率 │
├─────────────────────────────────────────────────────┤
│ student1  a@example.com  Group 1   450分钟   29.4% │
│ student2  b@example.com  Group 2   380分钟   25.1% │
└─────────────────────────────────────────────────────┘
```

## 七、预估工作量

| 任务 | 预估时间 |
|------|----------|
| 后端模型和API修改 | 20分钟 |
| 前端类型和注册表单 | 15分钟 |
| 管理员页面更新 | 15分钟 |
| 数据库迁移 | 10分钟 |
| 测试验证 | 10分钟 |
| **总计** | **约70分钟** |

## 八、注意事项

1. **数据库迁移**：现有用户需要设置默认分组（group1）
2. **向后兼容**：API响应需要包含group字段，前端需要处理
3. **分组名称**：使用"Group 1"到"Group 6"作为显示名称
4. **必填验证**：注册时分组为必填项
