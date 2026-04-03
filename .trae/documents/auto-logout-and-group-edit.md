# 自动登出和管理员修改用户分组功能计划

## 一、需求概述

1. **自动登出**：用户如果10分钟没有任何网页操作，则自动登出
2. **管理员修改分组**：admin用户可以修改用户的group分组

## 二、现状分析

### 认证状态管理

- 使用 Zustand 管理认证状态 (`authStore.ts`)
- Token 存储在 localStorage
- 已有 `logout` 方法清除认证状态

### 管理员页面

- `AdminDashboard.tsx` 显示用户列表
- 用户列表包含分组信息
- 目前只能查看，不能修改

## 三、技术方案

### 3.1 自动登出功能

**实现思路：**

- 使用 `useEffect` 监听用户活动事件
- 事件类型：`mousedown`、`keydown`、`scroll`、`touchstart`
- 设置10分钟（600秒）倒计时
- 倒计时结束自动调用 `logout` 并跳转登录页

**核心代码：**

```typescript
// useAutoLogout.ts
import { useEffect, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuthStore } from '../stores/authStore'

const INACTIVITY_TIMEOUT = 10 * 60 * 1000 // 10分钟

export function useAutoLogout() {
  const { user, logout } = useAuthStore()
  const navigate = useNavigate()
  const timerRef = useRef<NodeJS.Timeout | null>(null)

  useEffect(() => {
    if (!user) return

    const resetTimer = () => {
      if (timerRef.current) clearTimeout(timerRef.current)
      timerRef.current = setTimeout(() => {
        logout()
        navigate('/login')
      }, INACTIVITY_TIMEOUT)
    }

    const events = ['mousedown', 'keydown', 'scroll', 'touchstart']
    events.forEach(event => window.addEventListener(event, resetTimer))
    resetTimer()

    return () => {
      if (timerRef.current) clearTimeout(timerRef.current)
      events.forEach(event => window.removeEventListener(event, resetTimer))
    }
  }, [user, logout, navigate])
}
```

### 3.2 管理员修改用户分组

**后端API：**

```python
# admin.py
@router.put("/users/{user_id}/group")
def update_user_group(
    user_id: str,
    group: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if group not in ["group1", "group2", "group3", "group4", "group5", "group6"]:
        raise HTTPException(status_code=400, detail="Invalid group")
    
    user.group = group
    db.commit()
    return {"message": "Group updated", "group": group}
```

**前端UI：**

- 在用户列表的分组列添加下拉选择框
- 选择后自动调用API更新

## 四、实施步骤

### 阶段一：自动登出功能

1. **创建自动登出Hook**
   - 文件：`frontend/src/hooks/useAutoLogout.ts`
   - 实现活动监听和倒计时逻辑
2. **在Layout中应用Hook**
   - 文件：`frontend/src/components/Layout.tsx`
   - 引入并调用 `useAutoLogout()`

### 阶段二：管理员修改分组功能

1. **后端API**
   - 文件：`backend/app/routers/admin.py`
   - 添加 `PUT /api/admin/users/{user_id}/group` 接口
2. **前端API服务**
   - 文件：`frontend/src/services/admin.ts`
   - 添加 `updateUserGroup` 方法
3. **前端UI修改**
   - 文件：`frontend/src/pages/AdminDashboard.tsx`
   - 分组列改为下拉选择框

## 五、文件变更清单

### 新增文件

| 文件路径                                  | 描述       |
| ------------------------------------- | -------- |
| `frontend/src/hooks/useAutoLogout.ts` | 自动登出Hook |

### 修改文件

| 文件路径                                    | 变更内容       |
| --------------------------------------- | ---------- |
| `frontend/src/components/Layout.tsx`    | 引入自动登出Hook |
| `backend/app/routers/admin.py`          | 添加修改分组API  |
| `frontend/src/services/admin.ts`        | 添加修改分组方法   |
| `frontend/src/pages/AdminDashboard.tsx` | 分组列改为下拉选择框 |

## 六、UI 设计

### 管理员页面分组修改

```
┌─────────────────────────────────────────────────────┐
│ 用户名     邮箱           分组         学习时长     │
├─────────────────────────────────────────────────────┤
│ student1  a@example.com  [▼ Group 4]   450分钟     │
│ student2  b@example.com  [▼ Group 2]   380分钟     │
└─────────────────────────────────────────────────────┘
```

下拉选项：Group 1 - Group 6

## 七、预估工作量

| 任务        | 预估时间      |
| --------- | --------- |
| 自动登出Hook  | 15分钟      |
| Layout集成  | 5分钟       |
| 后端修改分组API | 10分钟      |
| 前端API服务   | 5分钟       |
| 前端UI修改    | 15分钟      |
| 测试验证      | 10分钟      |
| **总计**    | **约60分钟** |

## 八、注意事项

1. **自动登出时机**：仅在用户已登录状态下启用
2. **事件清理**：组件卸载时需清理事件监听和定时器
3. **分组验证**：后端需验证分组值有效性
4. **即时反馈**：修改分组后显示成功提示

