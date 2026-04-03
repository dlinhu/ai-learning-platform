from app.utils.database import SessionLocal, engine
from app.models.models import Base, AINews
from datetime import datetime

print("=== Creating AI News Table ===\n")

# Create table
Base.metadata.create_all(bind=engine)

print("AI News table created successfully\n")

# Verify table creation
db = SessionLocal()
try:
    # Try to query
    count = db.query(AINews).count()
    print(f"Table verification successful, current news count: {count}")
except Exception as e:
    print(f"Table verification failed: {e}")
finally:
    db.close()

print("\n=== Migration Complete ===")
