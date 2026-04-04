# 学员首页文章展示功能技术规格

## 功能概述

在学员首页（Home页面）展示管理员添加的文章，方便学员浏览和学习优质内容。

## 技术架构

### 后端 (FastAPI)
- **API端点**: 复用现有的 `/api/articles` 接口
- **数据过滤**: 只展示已发布的文章
- **排序**: 按创建时间倒序，最新的文章在前

### 前端 (React + TypeScript)
- **页面**: Home.tsx (学员首页)
- **组件**: 新增文章列表展示组件
- **样式**: Tailwind CSS，与现有设计保持一致

## 详细设计

### 1. 后端API调整

现有的 `/api/articles` 接口已经支持：
- 获取已发布文章列表
- 分页功能
- 分类过滤
- 搜索功能

**无需修改后端代码**，直接复用现有接口。

### 2. 前端实现

#### 新增组件: ArticleList.tsx

展示文章列表的组件，包含：
- 文章卡片展示（标题、摘要、来源、分类、发布时间）
- 分类筛选
- 查看更多链接
- 响应式布局

```typescript
interface Article {
  id: string
  title: string
  summary: string | null
  source: string
  category: string
  image_url: string | null
  published_at: string | null
  view_count: number
}

interface ArticleListProps {
  articles: Article[]
  loading: boolean
  onCategoryChange?: (category: string) => void
  categories: string[]
  selectedCategory: string
}
```

#### 修改页面: Home.tsx

在现有首页内容下方添加文章展示区域：

1. **文章展示区域**
   - 标题: "推荐文章" 或 "学习资源"
   - 文章列表（最多展示6篇）
   - "查看更多" 链接跳转到文章列表页面

2. **布局设计**
   - 使用网格布局（桌面端3列，平板2列，手机1列）
   - 卡片式设计，包含文章基本信息
   - 分类标签展示

### 3. 数据获取

在 Home.tsx 中添加数据获取逻辑：

```typescript
const [articles, setArticles] = useState<Article[]>([])
const [articleLoading, setArticleLoading] = useState(true)
const [articleCategories, setArticleCategories] = useState<string[]>([])
const [selectedCategory, setSelectedCategory] = useState('')

// 获取文章列表
const fetchArticles = async () => {
  setArticleLoading(true)
  try {
    const params = new URLSearchParams()
    params.append('page', '1')
    params.append('per_page', '6') // 首页只展示6篇
    if (selectedCategory) params.append('category', selectedCategory)
    
    const response = await api.get(`/articles?${params.toString()}`)
    setArticles(response.data)
  } catch (err) {
    console.error('Error fetching articles:', err)
  } finally {
    setArticleLoading(false)
  }
}

// 获取分类列表
const fetchCategories = async () => {
  try {
    const response = await api.get('/articles/categories/list')
    setArticleCategories(response.data)
  } catch (err) {
    console.error('Error fetching categories:', err)
  }
}

useEffect(() => {
  fetchArticles()
  fetchCategories()
}, [selectedCategory])
```

### 4. 文章卡片设计

每篇文章展示：
- **标题**: 最多2行，超出省略
- **摘要**: 最多3行，超出省略
- **来源**: 显示文章来源
- **分类**: 彩色标签
- **发布时间**: 相对时间（刚刚、X小时前、X天前）
- **浏览次数**: 可选显示

### 5. 新增页面: Articles.tsx (文章列表页)

创建独立的文章列表页面，展示所有文章：
- 完整的分页功能
- 搜索功能
- 分类筛选
- 文章详情链接

路由: `/articles`

### 6. 新增页面: ArticleDetail.tsx (文章详情页)

展示单篇文章的详细内容：
- 完整标题
- 文章内容
- 来源链接（可点击跳转原文）
- 作者信息
- 发布时间
- 浏览次数
- 相关文章推荐

路由: `/articles/:id`

### 7. 路由配置

在 App.tsx 中添加新路由：

```typescript
<Route path="/articles" element={<PrivateRoute><Articles /></PrivateRoute>} />
<Route path="/articles/:id" element={<PrivateRoute><ArticleDetail /></PrivateRoute>} />
```

### 8. 导航栏调整

在 Layout.tsx 的导航栏中添加"文章"入口：

```typescript
const navItems = [
  { path: '/', label: '首页' },
  { path: '/courses', label: '课程' },
  { path: '/articles', label: '文章' }, // 新增
  { path: '/dashboard', label: '仪表盘' },
]
```

## 实现步骤

1. **创建文章列表组件** (ArticleList.tsx)
2. **修改首页** (Home.tsx) - 添加文章展示区域
3. **创建文章列表页面** (Articles.tsx)
4. **创建文章详情页面** (ArticleDetail.tsx)
5. **添加路由配置** (App.tsx)
6. **更新导航栏** (Layout.tsx)
7. **测试功能完整性**

## UI设计

### 首页文章区域

```
┌─────────────────────────────────────────────────────┐
│  推荐文章                              [查看全部 >]  │
├─────────────────────────────────────────────────────┤
│  [全部] [AI] [技术] [教育] [研究]                    │
├─────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │
│  │ 文章标题    │  │ 文章标题    │  │ 文章标题    │  │
│  │ 摘要内容... │  │ 摘要内容... │  │ 摘要内容... │  │
│  │ [分类标签]  │  │ [分类标签]  │  │ [分类标签]  │  │
│  │ 来源 · 时间 │  │ 来源 · 时间 │  │ 来源 · 时间 │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │
│  │ 文章标题    │  │ 文章标题    │  │ 文章标题    │  │
│  │ 摘要内容... │  │ 摘要内容... │  │ 摘要内容... │  │
│  │ [分类标签]  │  │ [分类标签]  │  │ [分类标签]  │  │
│  │ 来源 · 时间 │  │ 来源 · 时间 │  │ 来源 · 时间 │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  │
└─────────────────────────────────────────────────────┘
```

### 文章卡片样式

- 白色背景，圆角，阴影
- 悬停效果：轻微上浮，阴影加深
- 分类标签：彩色圆角标签
- 响应式：移动端单列，桌面端三列

## 技术依赖

**无需新增依赖**，使用现有技术栈：
- React + TypeScript
- React Router
- Tailwind CSS
- Axios (通过 api 服务)

## 性能考虑

- 首页只加载6篇文章，减少初始加载时间
- 文章详情页按需加载
- 图片懒加载（如有图片）
- 缓存文章列表数据

## 安全考虑

- 文章内容需要XSS过滤
- 来源链接需要验证
- 只有已发布文章才展示

## 预期效果

- 学员可以在首页看到管理员推荐的优质文章
- 点击文章可以查看详情
- 可以按分类筛选文章
- 可以跳转到文章列表页查看更多
- 提升平台内容价值，增加学员学习资源

## 总结

本功能将在学员首页展示管理员添加的优质文章，为学员提供更多学习资源。设计遵循现有的UI风格，确保用户体验的一致性。