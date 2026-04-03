import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import hashlib
from app.utils.database import SessionLocal
from app.models.models import AINews

class NewsFetcher:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def fetch_openai_blog(self) -> List[Dict]:
        """Fetch news from OpenAI Blog"""
        news_list = []
        try:
            response = requests.get('https://openai.com/blog/', headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            articles = soup.find_all('article', limit=5)
            for article in articles:
                title_elem = article.find('h2')
                link_elem = article.find('a')
                
                if title_elem and link_elem:
                    title = title_elem.get_text(strip=True)
                    link = 'https://openai.com' + link_elem.get('href', '')
                    
                    news_list.append({
                        'title': title,
                        'summary': f"OpenAI发布的最新动态：{title}",
                        'source': 'OpenAI Blog',
                        'source_url': link,
                        'category': 'OpenAI',
                        'published_at': datetime.utcnow()
                    })
        except Exception as e:
            print(f"Error fetching OpenAI blog: {e}")
        
        return news_list
    
    def fetch_anthropic_blog(self) -> List[Dict]:
        """Fetch news from Anthropic Blog"""
        news_list = []
        try:
            response = requests.get('https://www.anthropic.com/news', headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            articles = soup.find_all('article', limit=5)
            for article in articles:
                title_elem = article.find(['h2', 'h3'])
                link_elem = article.find('a')
                
                if title_elem and link_elem:
                    title = title_elem.get_text(strip=True)
                    link = link_elem.get('href', '')
                    if not link.startswith('http'):
                        link = 'https://www.anthropic.com' + link
                    
                    news_list.append({
                        'title': title,
                        'summary': f"Anthropic发布的最新动态：{title}",
                        'source': 'Anthropic Blog',
                        'source_url': link,
                        'category': 'Anthropic',
                        'published_at': datetime.utcnow()
                    })
        except Exception as e:
            print(f"Error fetching Anthropic blog: {e}")
        
        return news_list
    
    def fetch_google_ai_blog(self) -> List[Dict]:
        """Fetch news from Google AI Blog"""
        news_list = []
        try:
            response = requests.get('https://blog.google/technology/ai/', headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            articles = soup.find_all('article', limit=5)
            for article in articles:
                title_elem = article.find(['h2', 'h3'])
                link_elem = article.find('a')
                
                if title_elem and link_elem:
                    title = title_elem.get_text(strip=True)
                    link = link_elem.get('href', '')
                    
                    news_list.append({
                        'title': title,
                        'summary': f"Google AI发布的最新动态：{title}",
                        'source': 'Google AI Blog',
                        'source_url': link,
                        'category': 'Google AI',
                        'published_at': datetime.utcnow()
                    })
        except Exception as e:
            print(f"Error fetching Google AI blog: {e}")
        
        return news_list
    
    def fetch_36kr_ai(self) -> List[Dict]:
        """Fetch AI news from 36Kr"""
        news_list = []
        try:
            response = requests.get('https://36kr.com/information/AI', headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            articles = soup.find_all('div', class_='article-item', limit=5)
            for article in articles:
                title_elem = article.find('a', class_='article-item-title')
                
                if title_elem:
                    title = title_elem.get_text(strip=True)
                    link = title_elem.get('href', '')
                    if not link.startswith('http'):
                        link = 'https://36kr.com' + link
                    
                    news_list.append({
                        'title': title,
                        'summary': f"36氪AI资讯：{title}",
                        'source': '36Kr AI',
                        'source_url': link,
                        'category': 'AI Industry',
                        'published_at': datetime.utcnow()
                    })
        except Exception as e:
            print(f"Error fetching 36Kr AI: {e}")
        
        return news_list
    
    def deduplicate_news(self, news_item: Dict) -> bool:
        """Check if news already exists"""
        db = SessionLocal()
        try:
            # Create a hash based on title and source
            news_hash = hashlib.md5(f"{news_item['title']}_{news_item['source']}".encode()).hexdigest()
            
            # Check if exists
            existing = db.query(AINews).filter(
                AINews.title == news_item['title'],
                AINews.source == news_item['source']
            ).first()
            
            return existing is not None
        finally:
            db.close()
    
    def save_news(self, news_list: List[Dict]) -> int:
        """Save news to database"""
        db = SessionLocal()
        saved_count = 0
        
        try:
            for news_item in news_list:
                # Skip if already exists
                if self.deduplicate_news(news_item):
                    continue
                
                # Create news record
                news = AINews(
                    title=news_item['title'],
                    summary=news_item.get('summary', ''),
                    content=news_item.get('content'),
                    source=news_item['source'],
                    source_url=news_item['source_url'],
                    category=news_item.get('category', 'general'),
                    image_url=news_item.get('image_url'),
                    published_at=news_item.get('published_at', datetime.utcnow()),
                    fetched_at=datetime.utcnow()
                )
                
                db.add(news)
                saved_count += 1
            
            db.commit()
        except Exception as e:
            print(f"Error saving news: {e}")
            db.rollback()
        finally:
            db.close()
        
        return saved_count
    
    def fetch_all_news(self) -> int:
        """Fetch news from all sources"""
        all_news = []
        
        # Fetch from different sources
        all_news.extend(self.fetch_openai_blog())
        all_news.extend(self.fetch_anthropic_blog())
        all_news.extend(self.fetch_google_ai_blog())
        all_news.extend(self.fetch_36kr_ai())
        
        # Save to database
        saved_count = self.save_news(all_news)
        
        return saved_count

def fetch_ai_news():
    """Main function to fetch AI news"""
    fetcher = NewsFetcher()
    saved_count = fetcher.fetch_all_news()
    print(f"Fetched and saved {saved_count} news articles")
    return saved_count

if __name__ == "__main__":
    fetch_ai_news()
