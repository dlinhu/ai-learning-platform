# 添加 Group Admin 角色技术规格

## 需求分析

在现有系统中添加一个新的角色 `group_admin`（组长），这个角色具有以下权限：
- 只能查看自己组内学生的学习进度
- 不能管理其他组的成员
- 不能修改系统设置

### 当前角色
1. **student** - 学生，查看自己的学习进度
2. **admin** - 管理员，管理所有用户和内容

### 新增角色
3. **group_admin** - 组长，管理自己组内的成员和查看进度

## 技术方案

### 1. 数据库模型调整

#### 修改 User 模型
```python
class UserRole(enum.Enum):
    STUDENT = "student"
    GROUP_ADMIN = "group_admin"
    ADMIN = "admin"

class User(Base):
    # ... 其他字段
    role = Column(String, default=UserRole.STUDENT.value)
    group = Column(String, nullable=True)  # 所属组
```

#### 添加 Group 模型（可选）
```python
class Group(Base):
    __tablename__ = "groups"
    
    id = Column(String, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
```

### 2. 后端 API 修改

#### 权限控制装饰器

创建新的权限验证函数：

```python
# app/routers/auth.py

async def require_group_admin(current_user: User = Depends(get_current_user)):
    """验证用户是否为组长或管理员"""
    if current_user.role not in [UserRole.GROUP_ADMIN.value, UserRole.ADMIN.value]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Group admin access required"
        )
    return current_user

async def require_same_group_or_admin(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """验证用户是否有权限访问该组的数据"""
    if current_user.role == UserRole.ADMIN.value:
        return current_user  # 管理员可以访问所有组
    
    if current_user.role == UserRole.GROUP_ADMIN.value:
        return current_user  # 组长可以访问自己组
    
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Access denied"
    )
```

#### 修改管理端点

```python
# app/routers/admin.py

@router.get("/groups/{group_name}/progress")
def get_group_progress(
    group_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_same_group_or_admin)
):
    # 如果是组长，只能查看自己组的进度
    if current_user.role == UserRole.GROUP_ADMIN.value:
        if current_user.group != group_name:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can only view your own group's progress"
            )
    
    # 查询该组所有成员的学习进度
    ...
```

### 3. 前端实现

#### 修改角色选择

在管理员界面添加 `group_admin` 选项：

```typescript
// AdminDashboard.tsx 或 AdminUsers.tsx

const roles = [
  { value: 'student', label: '学生' },
  { value: 'group_admin', label: '组长' },
  { value: 'admin', label: '管理员' }
]
```

#### 组长仪表盘

创建 `GroupAdminDashboard.tsx`：

```typescript
// 只显示自己组的数据
- 组内成员列表
- 组内学习进度统计
- 组内成员详细进度
```

#### 权限控制

```typescript
// 检查用户角色
const isGroupAdmin = user?.role === 'group_admin'
const isAdmin = user?.role === 'admin'

// 根据角色显示不同的菜单
if (isGroupAdmin) {
  // 只显示组管理相关菜单
} else if (isAdmin) {
  // 显示所有管理菜单
}
```

### 4. 路由配置

```typescript
// App.tsx

<Route path="group-admin" element={<GroupAdminRoute><GroupAdminDashboard /></GroupAdminRoute>} />
<Route path="group-admin/progress" element={<GroupAdminRoute><GroupProgress /></GroupAdminRoute>} />

function GroupAdminRoute({ children }: { children: React.ReactNode }) {
  const { user } = useAuthStore()
  if (!user) return <Navigate to="/login" />
  if (user.role !== 'group_admin' && user.role !== 'admin') {
    return <Navigate to="/dashboard" />
  }
  return <>{children}</>
}
```

### 5. 实施步骤

1. **数据库迁移**
   - 添加 `group_admin` 角色到枚举
   - 确保所有现有用户的 `group` 字段正确

2. **后端修改**
   - 添加权限验证函数
   - 修改管理端点，添加组过滤逻辑
   - 添加组长专用端点

3. **前端修改**
   - 添加角色选择选项
   - 创建组长仪表盘
   - 修改导航菜单

4. **测试**
   - 测试组长权限
   - 测试权限隔离
   - 测试数据过滤

### 6. 权限矩阵

| 功能 | student | group_admin | admin |
|------|---------|-------------|-------|
| 查看自己的进度 | ✅ | ✅ | ✅ |
| 查看组内进度 | ❌ | ✅（仅自己组） | ✅（所有组） |
| 管理用户 | ❌ | ❌ | ✅ |
| 管理课程 | ❌ | ❌ | ✅ |
| 管理文章 | ❌ | ❌ | ✅ |
| 修改用户角色 | ❌ | ❌ | ✅ |

### 7. 数据隔离

**组长查看进度时的过滤逻辑**：

```python
def get_group_members_progress(db: Session, group_name: str, current_user: User):
    # 验证权限
    if current_user.role == UserRole.GROUP_ADMIN.value:
        if current_user.group != group_name:
            raise HTTPException(status_code=403, detail="Access denied")
    
    # 查询组内成员
    members = db.query(User).filter(User.group == group_name).all()
    
    # 查询进度
    progress_data = []
    for member in members:
        progress = db.query(UserProgress).filter(
            UserProgress.user_id == member.id
        ).all()
        progress_data.append({
            'user': member,
            'progress': progress
        })
    
    return progress_data
```

### 8. UI 设计

#### 组长仪表盘布局

```
┌─────────────────────────────────────────┐
│  组长仪表盘                              │
├─────────────────────────────────────────┤
│  组名: XXX组                             │
│  成员数: XX 人                           │
│  平均进度: XX%                           │
├─────────────────────────────────────────┤
│  成员列表                                │
│  ┌───────┬───────┬───────┬───────┐      │
│  │ 姓名  │ 进度  │ 状态  │ 操作  │      │
│  ├───────┼───────┼───────┼───────┤      │
│  │ 张三  │ 80%   │ 在线  │ 查看  │      │
│  │ 李四  │ 60%   │ 离线  │ 查看  │      │
│  │ 王五  │ 90%   │ 在线  │ 查看  │      │
│  └───────┴───────┴───────┴───────┘      │
└─────────────────────────────────────────┘
```

### 9. 安全考虑

- **权限验证**: 每个请求都验证用户角色和组权限
- **数据隔离**: 组长只能访问自己组的数据
- **SQL注入防护**: 使用参数化查询
- **前端验证**: 前端也要验证用户权限，但后端是主要防线

### 10. 性能优化

- **缓存组数据**: 缓存组内成员列表
- **分页查询**: 成员列表分页显示
- **索引优化**: 为 `group` 字段添加索引

## 预期效果

### 管理员
- 可以创建和分配组长
- 可以查看所有组的进度
- 可以管理所有用户

### 组长
- 登录后看到组长仪表盘
- 只能查看自己组的成员
- 可以查看组内成员的详细进度
- 不能访问其他管理功能

### 学生
- 无变化，继续查看自己的进度

## 总结

本方案通过添加 `group_admin` 角色，实现了组级别的权限管理。组长只能查看自己组内的学习进度，实现了数据的隔离和权限的细分。技术实现主要涉及数据库模型调整、后端权限验证和前端界面修改。