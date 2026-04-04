from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, HttpUrl

from app.utils.database import get_db
from app.models.models import Article, User
from app.routers.auth import get_current_user, require_admin
from app.services.url_fetcher import url_fetcher

router = APIRouter(prefix="/api/articles", tags=["articles"])

# 文章列表响应模型
class ArticleResponse(BaseModel):
    id: str
    title: str
    summary: Optional[str] = None
    source: str
    source_url: str
    category: str
    author: Optional[str] = None
    published_at: Optional[datetime] = None
    is_published: bool
    view_count: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# 文章创建请求模型
class ArticleCreate(BaseModel):
    title: str
    content: str
    source: str
    source_url: str
    category: str = "general"
    summary: Optional[str] = None
    author: Optional[str] = None
    published_at: Optional[datetime] = None
    is_published: bool = True

# 文章更新请求模型
class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    source: Optional[str] = None
    source_url: Optional[str] = None
    category: Optional[str] = None
    summary: Optional[str] = None
    author: Optional[str] = None
    published_at: Optional[datetime] = None
    is_published: Optional[bool] = None

# 文章详情响应模型
class ArticleDetailResponse(ArticleResponse):
    content: str
    added_by: Optional[str] = None

    class Config:
        from_attributes = True

# URL抓取请求模型
class URLFetchRequest(BaseModel):
    url: HttpUrl

# URL抓取响应模型
class URLFetchResponse(BaseModel):
    title: str
    summary: Optional[str] = None
    source: str
    success: bool
    error: Optional[str] = None

# 抓取URL信息
@router.post("/fetch-url", response_model=URLFetchResponse)
def fetch_url_info(
    request: URLFetchRequest,
    current_user: User = Depends(require_admin)
):
    url_info = url_fetcher.fetch_url_info(str(request.url))
    return url_info

# 文章列表
@router.get("", response_model=List[ArticleResponse])
def get_articles(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=50),
    category: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Article).filter(Article.is_published == True)
    
    if category:
        query = query.filter(Article.category == category)
    
    if search:
        query = query.filter(
            (Article.title.ilike(f"%{search}%") |
             Article.content.ilike(f"%{search}%") |
             Article.summary.ilike(f"%{search}%") |
             Article.author.ilike(f"%{search}%") |
             Article.source.ilike(f"%{search}%"))
        )
    
    total = query.count()
    articles = query.offset((page - 1) * per_page).limit(per_page).all()
    
    return articles

# 文章详情
@router.get("/{article_id}", response_model=ArticleDetailResponse)
def get_article(
    article_id: str,
    db: Session = Depends(get_db)
):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found"
        )
    
    # 增加浏览次数
    article.view_count += 1
    db.commit()
    
    return article

# 创建文章
@router.post("", response_model=ArticleDetailResponse, status_code=status.HTTP_201_CREATED)
def create_article(
    article_data: ArticleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    article = Article(
        **article_data.model_dump(),
        added_by=current_user.id
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article

# 更新文章
@router.put("/{article_id}", response_model=ArticleDetailResponse)
def update_article(
    article_id: str,
    article_data: ArticleUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found"
        )
    
    update_data = article_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(article, field, value)
    
    db.commit()
    db.refresh(article)
    return article

# 删除文章
@router.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(
    article_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found"
        )
    
    db.delete(article)
    db.commit()
    return None

# 发布/取消发布文章
@router.put("/{article_id}/publish")
def toggle_publish(
    article_id: str,
    is_published: bool,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found"
        )
    
    article.is_published = is_published
    db.commit()
    db.refresh(article)
    return {"message": "Article status updated successfully", "is_published": article.is_published}

# 获取文章分类
@router.get("/categories/list")
def get_categories(
    db: Session = Depends(get_db)
):
    categories = db.query(Article.category).distinct().all()
    return [cat[0] for cat in categories]

# 搜索文章
@router.get("/search/results")
def search_articles(
    q: str = Query(..., description="Search query"),
    db: Session = Depends(get_db)
):
    articles = db.query(Article).filter(
        (Article.is_published == True) &
        ((Article.title.ilike(f"%{q}%") |
          Article.content.ilike(f"%{q}%") |
          Article.summary.ilike(f"%{q}%") |
          Article.author.ilike(f"%{q}%") |
          Article.source.ilike(f"%{q}%")))
    ).limit(20).all()
    
    return articles
