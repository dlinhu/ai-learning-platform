from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    APP_NAME: str = "AI Learning Platform"
    DEBUG: bool = True
    
    DATABASE_URL: str = "sqlite:///./data/learning.db"
    
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    CONTENT_PATH: str = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "..", "AI Courses")
    COURSE_SCHEDULE_PATH: str = os.path.join(CONTENT_PATH, "Context_Engineering_课程编排.md")
    
    OPENAI_API_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings()
