import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from typing import Dict, Optional

class URLFetcher:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.timeout = 10
    
    def fetch_url_info(self, url: str) -> Dict:
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title = self._extract_title(soup)
            summary = self._extract_summary(soup)
            image_url = self._extract_image(soup)
            source = self._extract_source(url)
            
            return {
                'title': title,
                'summary': summary,
                'image_url': image_url,
                'source': source,
                'success': True
            }
        except Exception as e:
            return {
                'title': url,
                'summary': None,
                'image_url': None,
                'source': urlparse(url).netloc,
                'success': False,
                'error': str(e)
            }
    
    def _extract_title(self, soup: BeautifulSoup) -> str:
        og_title = soup.find('meta', property='og:title')
        if og_title and og_title.get('content'):
            return og_title['content'].strip()
        
        twitter_title = soup.find('meta', attrs={'name': 'twitter:title'})
        if twitter_title and twitter_title.get('content'):
            return twitter_title['content'].strip()
        
        title_tag = soup.find('title')
        if title_tag:
            return title_tag.get_text().strip()
        
        h1_tag = soup.find('h1')
        if h1_tag:
            return h1_tag.get_text().strip()
        
        return "Untitled"
    
    def _extract_summary(self, soup: BeautifulSoup) -> Optional[str]:
        og_desc = soup.find('meta', property='og:description')
        if og_desc and og_desc.get('content'):
            return og_desc['content'].strip()
        
        twitter_desc = soup.find('meta', attrs={'name': 'twitter:description'})
        if twitter_desc and twitter_desc.get('content'):
            return twitter_desc['content'].strip()
        
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            return meta_desc['content'].strip()
        
        paragraphs = soup.find_all('p')
        if paragraphs:
            for p in paragraphs:
                text = p.get_text().strip()
                if len(text) > 50:
                    return text[:300] + '...' if len(text) > 300 else text
        
        return None
    
    def _extract_image(self, soup: BeautifulSoup) -> Optional[str]:
        og_image = soup.find('meta', property='og:image')
        if og_image and og_image.get('content'):
            return og_image['content'].strip()
        
        twitter_image = soup.find('meta', attrs={'name': 'twitter:image'})
        if twitter_image and twitter_image.get('content'):
            return twitter_image['content'].strip()
        
        return None
    
    def _extract_source(self, url: str) -> str:
        parsed = urlparse(url)
        return parsed.netloc

url_fetcher = URLFetcher()
