from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from app.utils.database import get_db
from app.models.models import AINews, User
from app.routers.auth import get_current_user, require_admin
from app.services.news_fetcher import fetch_ai_news

router = APIRouter(prefix="/api/news", tags=["news"])

class NewsResponse(BaseModel):
    id: str
    title: str
    summary: Optional[str]
    source: str
    source_url: str
    category: str
    image_url: Optional[str]
    published_at: Optional[datetime]
    view_count: int
    is_featured: bool
    
    class Config:
        from_attributes = True

class NewsListResponse(BaseModel):
    news: List[NewsResponse]
    total: int
    page: int
    per_page: int

@router.get("", response_model=NewsListResponse)
def get_news_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=50),
    category: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get list of AI news"""
    query = db.query(AINews).order_by(AINews.published_at.desc())
    
    # Filter by category
    if category:
        query = query.filter(AINews.category == category)
    
    # Search by title or summary
    if search:
        search_term = f"%{search}%"
        query = query.filter(
            (AINews.title.ilike(search_term)) | 
            (AINews.summary.ilike(search_term))
        )
    
    # Get total count
    total = query.count()
    
    # Paginate
    offset = (page - 1) * per_page
    news_list = query.offset(offset).limit(per_page).all()
    
    return NewsListResponse(
        news=[NewsResponse.from_orm(news) for news in news_list],
        total=total,
        page=page,
        per_page=per_page
    )

@router.get("/{news_id}", response_model=NewsResponse)
def get_news_detail(
    news_id: str,
    db: Session = Depends(get_db)
):
    """Get news detail by ID"""
    news = db.query(AINews).filter(AINews.id == news_id).first()
    
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    
    # Increment view count
    news.view_count += 1
    db.commit()
    
    return NewsResponse.from_orm(news)

@router.post("/admin/fetch")
def trigger_fetch_news(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Manually trigger news fetching (admin only)"""
    try:
        saved_count = fetch_ai_news()
        return {
            "message": f"Successfully fetched {saved_count} news articles",
            "saved_count": saved_count
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch news: {str(e)}")

@router.put("/admin/{news_id}/feature")
def toggle_feature_news(
    news_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Toggle news featured status (admin only)"""
    news = db.query(AINews).filter(AINews.id == news_id).first()
    
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    
    news.is_featured = not news.is_featured
    db.commit()
    
    return {
        "message": f"News {'featured' if news.is_featured else 'unfeatured'} successfully",
        "is_featured": news.is_featured
    }

@router.delete("/admin/{news_id}")
def delete_news(
    news_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Delete news (admin only)"""
    news = db.query(AINews).filter(AINews.id == news_id).first()
    
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    
    db.delete(news)
    db.commit()
    
    return {"message": "News deleted successfully"}

@router.get("/categories/list")
def get_news_categories(db: Session = Depends(get_db)):
    """Get list of news categories"""
    categories = db.query(AINews.category).distinct().all()
    return {"categories": [cat[0] for cat in categories if cat[0]]}
