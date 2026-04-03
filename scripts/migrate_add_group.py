import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(script_dir, '..', 'backend')
backend_dir = os.path.abspath(backend_dir)
sys.path.insert(0, backend_dir)

os.chdir(backend_dir)

from app.utils.database import SessionLocal, engine
from app.models.models import User
from sqlalchemy import text

def migrate_add_group():
    db = SessionLocal()
    try:
        with engine.connect() as conn:
            result = conn.execute(text("PRAGMA table_info(users)"))
            columns = [row[1] for row in result.fetchall()]
            
            if 'group' not in columns:
                print("Adding 'group' column to users table...")
                conn.execute(text('ALTER TABLE users ADD COLUMN "group" VARCHAR DEFAULT \'group1\''))
                conn.commit()
                print("Column 'group' added successfully!")
            else:
                print("Column 'group' already exists.")
        
        users = db.query(User).all()
        updated_count = 0
        for user in users:
            if not hasattr(user, 'group') or user.group is None:
                user.group = 'group1'
                updated_count += 1
        
        if updated_count > 0:
            db.commit()
            print(f"Updated {updated_count} users with default group 'group1'")
        
        print("Migration completed successfully!")
        
    except Exception as e:
        print(f"Migration failed: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    migrate_add_group()
