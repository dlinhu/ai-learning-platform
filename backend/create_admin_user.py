from app.utils.database import SessionLocal
from app.models.models import User, UserRole
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

db = SessionLocal()

existing_admin = db.query(User).filter(User.username == 'admin').first()

if existing_admin:
    print(f"Admin user already exists: {existing_admin.username} ({existing_admin.email})")
    print(f"Role: {existing_admin.role}")
else:
    admin_user = User(
        username='admin',
        email='admin@example.com',
        password_hash=pwd_context.hash('admin123'),
        role=UserRole.ADMIN.value,
        group='group1'
    )
    db.add(admin_user)
    db.commit()
    db.refresh(admin_user)
    
    print("Admin user created successfully!")
    print(f"Username: admin")
    print(f"Email: admin@example.com")
    print(f"Password: admin123")
    print(f"Role: {admin_user.role}")
    print("\nPlease change the password after first login!")

db.close()
