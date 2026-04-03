import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(script_dir, '..', 'backend')
backend_dir = os.path.abspath(backend_dir)
sys.path.insert(0, backend_dir)

os.chdir(backend_dir)

from app.utils.database import SessionLocal
from app.models.models import User
from app.routers.auth import get_password_hash

def create_admin(username: str, email: str, password: str):
    db = SessionLocal()
    try:
        existing = db.query(User).filter(
            (User.username == username) | (User.email == email)
        ).first()
        
        if existing:
            if existing.role == "admin":
                print(f"管理员账户已存在: {existing.username}")
                return
            existing.role = "admin"
            db.commit()
            print(f"用户 '{existing.username}' 已升级为管理员")
            return
        
        admin = User(
            username=username,
            email=email,
            password_hash=get_password_hash(password),
            role="admin"
        )
        db.add(admin)
        db.commit()
        print(f"管理员账户创建成功!")
        print(f"  用户名: {username}")
        print(f"  邮箱: {email}")
        
    except Exception as e:
        print(f"创建失败: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="创建管理员账户")
    parser.add_argument("--username", default="admin", help="管理员用户名")
    parser.add_argument("--email", default="admin@example.com", help="管理员邮箱")
    parser.add_argument("--password", default="admin123", help="管理员密码")
    
    args = parser.parse_args()
    create_admin(args.username, args.email, args.password)
