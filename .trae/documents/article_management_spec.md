# 管理员文章管理功能技术规格

## 功能概述

为管理员添加一个功能，允许管理员将外网看到的优秀文章添加到网站中，方便学员学习。

## 技术架构

### 后端 (FastAPI)
- **框架**: FastAPI
- **数据库**: SQLite (现有的数据库系统)
- **认证**: JWT token 验证
- **权限控制**: 基于角色的访问控制 (admin-only)

### 前端 (React + TypeScript)
- **框架**: React 18
- **状态管理**: Zustand
- **样式**: Tailwind CSS
- **路由**: React Router

## 详细设计

### 1. 数据库模型

**新增 `Article` 模型**
```python
class Article(Base):
    __tablename__ = "articles"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String, nullable=False)  # 文章来源
    source_url = Column(String, nullable=False)  # 原始链接
    category = Column(String, default="general")  # 文章分类
    summary = Column(Text)  # 文章摘要
    image_url = Column(String, nullable=True)  # 文章图片
    author = Column(String, nullable=True)  # 作者
    published_at = Column(DateTime, nullable=True)  # 发布时间
    added_by = Column(String, ForeignKey("users.id"))  # 添加者
    is_published = Column(Boolean, default=True)  # 是否发布
    view_count = Column(Integer, default=0)  # 浏览次数
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 关系
    user = relationship("User", backref="articles")
```

### 2. 后端 API 设计

#### 文章管理路由 (`/api/articles`)

| 端点 | 方法 | 功能 | 权限 |
|------|------|------|------|
| `/api/articles` | `GET` | 获取文章列表 (支持分页、搜索、分类过滤) | 所有用户 |
| `/api/articles/{id}` | `GET` | 获取文章详情 | 所有用户 |
| `/api/articles` | `POST` | 创建新文章 | 仅管理员 |
| `/api/articles/{id}` | `PUT` | 更新文章 | 仅管理员 |
| `/api/articles/{id}` | `DELETE` | 删除文章 | 仅管理员 |
| `/api/articles/{id}/publish` | `PUT` | 发布/取消发布文章 | 仅管理员 |

#### 文章分类路由 (`/api/article-categories`)

| 端点 | 方法 | 功能 | 权限 |
|------|------|------|------|
| `/api/article-categories` | `GET` | 获取所有分类 | 所有用户 |
| `/api/article-categories` | `POST` | 创建新分类 | 仅管理员 |
| `/api/article-categories/{id}` | `PUT` | 更新分类 | 仅管理员 |
| `/api/article-categories/{id}` | `DELETE` | 删除分类 | 仅管理员 |

### 3. 前端实现

#### 组件结构

1. **文章管理页面** (`AdminArticles.tsx`)
   - 文章列表 (支持搜索、过滤、分页)
   - 文章创建按钮
   - 文章编辑/删除操作

2. **文章编辑组件** (`ArticleForm.tsx`)
   - 标题输入
   - 内容编辑器 (支持富文本)
   - 来源信息 (来源名称、URL)
   - 分类选择
   - 图片URL输入
   - 发布状态切换

3. **文章详情页面** (`ArticleDetail.tsx`)
   - 文章标题、作者、发布时间
   - 文章内容展示
   - 来源链接
   - 浏览次数统计

4. **文章列表组件** (`ArticleList.tsx`)
   - 文章卡片展示
   - 分类过滤
   - 搜索功能

#### 状态管理

```typescript
// stores/articleStore.ts
interface Article {
  id: string;
  title: string;
  content: string;
  source: string;
  source_url: string;
  category: string;
  summary: string;
  image_url: string | null;
  author: string | null;
  published_at: string | null;
  is_published: boolean;
  view_count: number;
  created_at: string;
  updated_at: string;
}

interface ArticleStore {
  articles: Article[];
  currentArticle: Article | null;
  categories: string[];
  loading: boolean;
  error: string | null;
  
  // 方法
  fetchArticles: (params?: { page?: number; category?: string; search?: string }) => Promise<void>;
  fetchArticleById: (id: string) => Promise<void>;
  createArticle: (article: Omit<Article, 'id' | 'created_at' | 'updated_at' | 'view_count'>) => Promise<void>;
  updateArticle: (id: string, article: Partial<Article>) => Promise<void>;
  deleteArticle: (id: string) => Promise<void>;
  togglePublish: (id: string, isPublished: boolean) => Promise<void>;
  fetchCategories: () => Promise<void>;
  createCategory: (category: string) => Promise<void>;
}
```

### 4. 权限控制

- **后端**: 使用现有的 `require_admin` 依赖函数确保只有管理员可以访问文章管理API
- **前端**: 在路由和组件层面检查用户角色，确保只有管理员可以访问文章管理页面

### 5. 数据验证

**文章创建/更新验证**:
- 标题: 必填，最大长度 255
- 内容: 必填
- 来源: 必填
- 来源URL: 必填，必须是有效的URL格式
- 分类: 必填
- 图片URL: 可选，必须是有效的URL格式

### 6. 性能优化

- **分页**: 文章列表支持分页，默认每页10条
- **缓存**: 文章列表和分类数据可适当缓存
- **搜索索引**: 为文章标题和内容添加搜索索引

### 7. 用户界面设计

#### 管理员文章管理页面
- 顶部搜索栏和分类过滤器
- 文章列表表格 (标题、来源、分类、发布状态、创建时间、操作)
- 批量操作功能
- 响应式设计，支持移动端

#### 文章编辑表单
- 富文本编辑器 (可使用 `react-quill` 或类似库)
- 实时预览功能
- 表单验证提示
- 保存/取消按钮

#### 文章详情页面
- 干净的阅读界面
- 文章元信息展示
- 来源链接跳转
- 相关文章推荐

### 8. 集成点

- **导航栏**: 在管理员导航中添加"文章管理"入口
- **首页**: 可在首页展示最新或推荐的文章
- **课程页面**: 可关联相关文章到课程内容

### 9. 实现步骤

1. **数据库迁移**: 创建 `articles` 表
2. **后端API**: 实现文章管理和分类管理API
3. **前端组件**: 开发文章管理页面和相关组件
4. **状态管理**: 实现文章相关的状态管理
5. **权限集成**: 确保只有管理员可以访问管理功能
6. **测试**: 功能测试和性能测试
7. **部署**: 部署到生产环境

### 10. 技术依赖

**新增依赖**:
- 后端: 无 (使用现有依赖)
- 前端: `react-quill` (富文本编辑器) - 可选

### 11. 安全考虑

- **XSS防护**: 对文章内容进行HTML转义或使用安全的富文本编辑器
- **URL验证**: 验证来源URL的有效性和安全性
- **权限检查**: 确保只有管理员可以修改文章
- **输入验证**: 对所有用户输入进行严格验证

### 12. 预期效果

- 管理员可以方便地添加、编辑、删除文章
- 学员可以浏览和搜索文章
- 文章内容清晰展示，支持富文本格式
- 系统运行稳定，性能良好

## 总结

本功能将为管理员提供一个完整的文章管理系统，使其能够将外网的优秀文章整合到平台中，为学员提供更多学习资源。系统设计遵循现有的技术栈和架构风格，确保与现有功能的良好集成。