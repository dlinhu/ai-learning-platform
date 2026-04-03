from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import auth, courses, progress, dashboard, terms, practice, admin, news

app = FastAPI(
    title=settings.APP_NAME,
    description="AI培训在线学习平台API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(progress.router)
app.include_router(dashboard.router)
app.include_router(terms.router)
app.include_router(practice.router)
app.include_router(admin.router)
app.include_router(news.router)

@app.get("/")
async def root():
    return {"message": "AI Learning Platform API", "version": "1.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
