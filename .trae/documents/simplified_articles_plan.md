# 简化文章管理功能计划

## 需求分析

当前的文章管理功能比较复杂，需要填写很多字段。用户希望简化流程：

### 当前流程
1. 管理员需要填写：标题、内容、来源、链接、分类、摘要等多个字段
2. 文章内容存储在数据库中
3. 用户在平台内查看文章详情

### 简化后的流程
1. 管理员只需要填写：外网链接（必填）、分类（可选）
2. 后端自动访问链接，解析出标题和摘要
3. 用户点击文章标题，直接跳转到外网链接阅读

## 技术方案

### 1. 数据库模型调整

修改 `Article` 模型，简化字段：

```python
class Article(Base):
    __tablename__ = "articles"
    
    id = Column(String, primary_key=True)
    url = Column(String, nullable=False, unique=True)  # 外网链接（必填，唯一）
    title = Column(String, nullable=False)  # 自动抓取的标题
    summary = Column(Text, nullable=True)  # 自动抓取的摘要（可选）
    image_url = Column(String, nullable=True)  # 自动抓取的图片（可选）
    category = Column(String, default="general")  # 分类（可选）
    source = Column(String, nullable=True)  # 自动提取的来源域名
    is_published = Column(Boolean, default=True)
    view_count = Column(Integer, default=0)
    added_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

**删除的字段**：
- `content` - 不再存储文章内容
- `source_url` - 用 `url` 替代
- `author` - 简化，不存储
- `published_at` - 简化，不存储

### 2. 后端实现

#### 2.1 网页内容抓取服务

创建 `backend/app/services/url_fetcher.py`：

```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from typing import Dict, Optional

class URLFetcher:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def fetch_url_info(self, url: str) -> Dict:
        """访问URL并提取标题、摘要、图片等信息"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 提取标题
            title = self._extract_title(soup)
            
            # 提取摘要
            summary = self._extract_summary(soup)
            
            # 提取图片
            image_url = self._extract_image(soup)
            
            # 提取来源
            source = self._extract_source(url)
            
            return {
                'title': title,
                'summary': summary,
                'image_url': image_url,
                'source': source
            }
        except Exception as e:
            return {
                'title': url,  # 如果抓取失败，使用URL作为标题
                'summary': None,
                'image_url': None,
                'source': urlparse(url).netloc
            }
    
    def _extract_title(self, soup: BeautifulSoup) -> str:
        # 尝试从 og:title, twitter:title, title 标签提取
        ...
    
    def _extract_summary(self, soup: BeautifulSoup) -> Optional[str]:
        # 尝试从 og:description, twitter:description, meta description 提取
        ...
    
    def _extract_image(self, soup: BeautifulSoup) -> Optional[str]:
        # 尝试从 og:image, twitter:image 提取
        ...
    
    def _extract_source(self, url: str) -> str:
        # 从URL提取域名
        return urlparse(url).netloc
```

#### 2.2 修改文章API

修改 `backend/app/routers/articles.py`：

```python
# 创建文章 - 简化版
@router.post("", response_model=ArticleDetailResponse)
def create_article(
    url: str,  # 必填：外网链接
    category: str = "general",  # 可选：分类
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    # 检查URL是否已存在
    existing = db.query(Article).filter(Article.url == url).first()
    if existing:
        raise HTTPException(status_code=400, detail="该链接已存在")
    
    # 抓取网页信息
    fetcher = URLFetcher()
    url_info = fetcher.fetch_url_info(url)
    
    # 创建文章记录
    article = Article(
        url=url,
        title=url_info['title'],
        summary=url_info['summary'],
        image_url=url_info['image_url'],
        source=url_info['source'],
        category=category,
        added_by=current_user.id
    )
    
    db.add(article)
    db.commit()
    db.refresh(article)
    return article
```

### 3. 前端实现

#### 3.1 简化文章创建表单

修改 `frontend/src/pages/ArticleForm.tsx`：

```typescript
// 简化后的表单只需要：
// 1. URL输入框（必填）
// 2. 分类选择（可选）
// 3. 预览按钮 - 点击后显示抓取的信息
// 4. 保存按钮

interface SimplifiedArticleForm {
  url: string  // 必填
  category: string  // 可选，默认 "general"
}
```

#### 3.2 修改文章列表和详情

- **文章列表**: 点击文章卡片直接跳转到外网链接
- **文章详情页**: 删除，不再需要
- **文章卡片**: 添加外链图标，提示用户将跳转到外部网站

### 4. 实施步骤

1. **修改数据库模型** - 简化 Article 模型字段
2. **创建URL抓取服务** - 实现 URLFetcher 类
3. **修改后端API** - 简化创建文章接口
4. **修改前端表单** - 简化为只需要URL和分类
5. **修改文章展示** - 点击直接跳转到外网链接
6. **删除文章详情页** - 不再需要
7. **测试功能** - 验证抓取和跳转功能

### 5. 数据迁移

需要处理现有数据：
- 保留现有文章记录
- 将 `source_url` 重命名为 `url`
- 如果 `content` 为空，将文章标记为"链接类型"

### 6. 用户体验优化

- **抓取预览**: 管理员输入URL后，可以预览抓取的标题和摘要
- **手动编辑**: 允许管理员手动修改抓取的标题和摘要
- **外链提示**: 在文章卡片上显示外链图标
- **新窗口打开**: 点击文章链接时在新窗口打开

### 7. 错误处理

- URL抓取失败时，使用URL作为标题
- 重复URL检测，避免重复添加
- URL格式验证
- 超时处理（10秒超时）

### 8. 性能考虑

- 抓取操作异步处理（可选）
- 缓存抓取结果
- 限制抓取频率

## 预期效果

### 管理员操作流程
1. 访问文章管理页面
2. 点击"添加文章"
3. 输入外网链接
4. （可选）选择分类
5. 点击"预览"查看抓取的信息
6. 点击"保存"

### 学员操作流程
1. 在首页或文章列表看到文章卡片
2. 点击文章标题
3. 在新窗口打开外网链接
4. 阅读原文

## 技术依赖

### 新增依赖
- **后端**: `beautifulsoup4` (已安装), `requests` (已安装)
- **前端**: 无需新增

### 现有依赖
- FastAPI
- SQLAlchemy
- React
- Tailwind CSS

## 总结

这个简化方案大大降低了管理员添加文章的工作量，只需要粘贴链接即可。用户可以直接跳转到原文阅读，避免了内容复制可能带来的版权问题。技术实现简单，主要工作是网页信息抓取和前端表单简化。