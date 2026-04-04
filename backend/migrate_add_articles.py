from app.utils.database import engine, Base
from app.models.models import Article

# 创建所有表
Base.metadata.create_all(bind=engine)

print("Database migration completed successfully!")
print("Added 'articles' table to the database.")