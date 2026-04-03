# AI新闻动态模块开发计划

## 📋 需求分析

在首页添加AI新闻动态模块，每日自动抓取AI圈的最新新闻，方便学员跟踪最新动态。

### 功能需求
1. **新闻展示**: 在首页显示最新AI新闻列表
2. **自动抓取**: 每日自动从网上抓取AI新闻
3. **新闻管理**: 管理员可以管理新闻内容
4. **新闻分类**: 支持不同类型的AI新闻分类
5. **新闻搜索**: 支持搜索和筛选新闻

## 🗄️ 数据库设计

### 新闻表 (ai_news)
```sql
CREATE TABLE ai_news (
    id VARCHAR PRIMARY KEY,
    title VARCHAR NOT NULL,           -- 新闻标题
    summary TEXT,                      -- 新闻摘要
    content TEXT,                      -- 新闻内容
    source VARCHAR,                    -- 新闻来源
    source_url VARCHAR,                -- 原文链接
    category VARCHAR,                  -- 新闻分类
    author VARCHAR,                    -- 作者
    published_at DATETIME,             -- 发布时间
    fetched_at DATETIME,               -- 抓取时间
    image_url VARCHAR,                 -- 图片链接
    tags JSON,                         -- 标签
    view_count INTEGER DEFAULT 0,      -- 浏览次数
    is_featured BOOLEAN DEFAULT FALSE, -- 是否精选
    created_at DATETIME,
    updated_at DATETIME
);
```

### 新闻分类
- 技术突破 (Technology)
- 产品发布 (Product)
- 研究论文 (Research)
- 行业动态 (Industry)
- 政策法规 (Policy)
- 观点评论 (Opinion)

## 🔧 后端实现

### 1. 数据模型 (`backend/app/models/models.py`)
- 添加 `AINews` 模型类
- 定义新闻字段和关系

### 2. 新闻抓取服务 (`backend/app/services/news_fetcher.py`)
- 实现新闻抓取逻辑
- 支持多个新闻源：
  - OpenAI Blog
  - Google AI Blog
  - Microsoft AI Blog
  - Anthropic Blog
  - Hugging Face Blog
  - AI News Websites
- 使用 RSS/API/Web Scraping 方式获取新闻
- 新闻去重和过滤

### 3. API接口 (`backend/app/routers/news.py`)
- `GET /api/news` - 获取新闻列表
- `GET /api/news/{news_id}` - 获取新闻详情
- `POST /api/admin/news/fetch` - 手动触发新闻抓取
- `PUT /api/admin/news/{news_id}` - 更新新闻
- `DELETE /api/admin/news/{news_id}` - 删除新闻

### 4. 定时任务 (`backend/app/tasks/news_scheduler.py`)
- 使用 APScheduler 实现定时任务
- 每日凌晨2点自动抓取新闻
- 支持手动触发

## 🎨 前端实现

### 1. 新闻组件 (`frontend/src/components/NewsCard.tsx`)
- 新闻卡片组件
- 显示标题、摘要、来源、时间
- 支持点击查看详情

### 2. 新闻列表 (`frontend/src/components/NewsList.tsx`)
- 新闻列表组件
- 支持分类筛选
- 支持搜索功能
- 分页显示

### 3. 首页集成 (`frontend/src/pages/Dashboard.tsx`)
- 在首页添加新闻模块
- 显示最新5-10条新闻
- 提供"查看更多"链接

### 4. 新闻详情页 (`frontend/src/pages/NewsDetail.tsx`)
- 新闻详情页面
- 显示完整内容
- 相关新闻推荐

### 5. 管理后台 (`frontend/src/pages/AdminNews.tsx`)
- 新闻管理界面
- 手动抓取新闻
- 编辑/删除新闻
- 设置精选新闻

## 📅 实施步骤

### 阶段1: 数据库和模型 (30分钟)
1. 创建新闻表迁移脚本
2. 添加 AINews 模型
3. 测试数据库操作

### 阶段2: 后端API (1小时)
1. 创建新闻路由
2. 实现新闻CRUD接口
3. 添加分页和筛选功能

### 阶段3: 新闻抓取服务 (1.5小时)
1. 实现新闻抓取逻辑
2. 添加多个新闻源
3. 实现去重和过滤
4. 添加定时任务

### 阶段4: 前端组件 (1小时)
1. 创建新闻卡片组件
2. 创建新闻列表组件
3. 集成到首页

### 阶段5: 测试和优化 (30分钟)
1. 测试新闻抓取
2. 测试前端显示
3. 优化性能和体验

## 🔌 新闻源配置

### RSS源
- OpenAI Blog: https://openai.com/blog/rss.xml
- Google AI Blog: https://ai.googleblog.com/feeds/posts/default
- Microsoft AI Blog: https://blogs.microsoft.com/ai/feed/
- Anthropic Blog: https://www.anthropic.com/index/blog/rss.xml

### API源
- NewsAPI: 需要API Key
- Hacker News API: 免费
- Reddit AI Subreddits

### Web Scraping
- 36氪 AI频道
- 机器之心
- 新智元

## ⚠️ 注意事项

1. **版权问题**: 只抓取公开的新闻摘要，提供原文链接
2. **频率控制**: 避免过于频繁的请求
3. **错误处理**: 处理网络错误和解析错误
4. **数据清洗**: 过滤广告和无关内容
5. **性能优化**: 使用缓存和异步处理

## 📊 预期效果

- 首页显示最新AI新闻
- 每日自动更新新闻内容
- 用户可以浏览和搜索新闻
- 管理员可以管理新闻内容
- 提升用户粘性和活跃度

## 🚀 扩展功能（可选）

1. **个性化推荐**: 根据用户兴趣推荐新闻
2. **新闻收藏**: 用户可以收藏感兴趣的新闻
3. **新闻分享**: 分享到社交媒体
4. **评论功能**: 用户可以评论新闻
5. **邮件订阅**: 每日新闻邮件推送
