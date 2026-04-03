import sqlite3
import shutil
from datetime import datetime

print("=== 用户数据导入脚本 ===\n")

# 步骤1: 备份当前数据库
print("步骤1: 备份当前数据库...")
backup_path = f'data/learning_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.db'
shutil.copy('data/learning.db', backup_path)
print(f"✓ 备份完成: {backup_path}\n")

# 步骤2: 连接两个数据库
print("步骤2: 连接数据库...")
source_conn = sqlite3.connect('learning.db')
target_conn = sqlite3.connect('data/learning.db')

source_cursor = source_conn.cursor()
target_cursor = target_conn.cursor()
print("✓ 数据库连接成功\n")

# 步骤3: 检查数据冲突
print("步骤3: 检查数据冲突...")

# 获取源数据库中的所有用户
source_cursor.execute('SELECT id, username, email FROM users WHERE username != "admin"')
source_users = source_cursor.fetchall()

# 获取目标数据库中的现有用户
target_cursor.execute('SELECT id, username, email FROM users')
target_users = target_cursor.fetchall()

target_usernames = {u[1] for u in target_users}
target_emails = {u[2] for u in target_users}
target_ids = {u[0] for u in target_users}

conflicts = []
for user in source_users:
    if user[1] in target_usernames:
        conflicts.append(f"用户名冲突: {user[1]}")
    if user[2] in target_emails:
        conflicts.append(f"邮箱冲突: {user[2]}")
    if user[0] in target_ids:
        conflicts.append(f"ID冲突: {user[0]}")

if conflicts:
    print("⚠ 发现冲突:")
    for conflict in conflicts:
        print(f"  - {conflict}")
    print("\n将跳过冲突的用户...\n")
else:
    print("✓ 无冲突\n")

# 步骤4: 导入用户数据
print("步骤4: 导入用户数据...")

# 获取所有非admin用户的完整数据
source_cursor.execute('''
    SELECT id, username, email, password_hash, role, created_at, settings, `group`
    FROM users 
    WHERE username != "admin"
''')
users_to_import = source_cursor.fetchall()

imported_users = 0
skipped_users = 0

for user in users_to_import:
    user_id, username, email, password_hash, role, created_at, settings, group_name = user
    
    # 检查是否已存在
    if username in target_usernames or email in target_emails or user_id in target_ids:
        skipped_users += 1
        continue
    
    # 插入用户
    target_cursor.execute('''
        INSERT INTO users (id, username, email, password_hash, role, created_at, settings, `group`)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, username, email, password_hash, role, created_at, settings, group_name))
    imported_users += 1

target_conn.commit()
print(f"✓ 用户导入完成: 导入 {imported_users} 人, 跳过 {skipped_users} 人\n")

# 步骤5: 导入学习进度
print("步骤5: 导入学习进度...")

# 获取所有进度记录
source_cursor.execute('''
    SELECT id, user_id, lesson_id, status, started_at, completed_at, time_spent, bookmarked
    FROM progress
''')
progress_to_import = source_cursor.fetchall()

# 获取目标数据库中已有的进度记录
target_cursor.execute('SELECT id FROM progress')
existing_progress_ids = {p[0] for p in target_cursor.fetchall()}

imported_progress = 0
skipped_progress = 0

for progress in progress_to_import:
    progress_id = progress[0]
    
    # 检查是否已存在
    if progress_id in existing_progress_ids:
        skipped_progress += 1
        continue
    
    # 插入进度记录
    target_cursor.execute('''
        INSERT INTO progress (id, user_id, lesson_id, status, started_at, completed_at, time_spent, bookmarked)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', progress)
    imported_progress += 1

target_conn.commit()
print(f"✓ 进度导入完成: 导入 {imported_progress} 条, 跳过 {skipped_progress} 条\n")

# 步骤6: 验证数据完整性
print("步骤6: 验证数据完整性...")

# 验证用户数量
target_cursor.execute('SELECT COUNT(*) FROM users')
total_users = target_cursor.fetchone()[0]

# 验证进度数量
target_cursor.execute('SELECT COUNT(*) FROM progress')
total_progress = target_cursor.fetchone()[0]

# 验证用户与进度的关联
target_cursor.execute('''
    SELECT COUNT(DISTINCT p.user_id)
    FROM progress p
    INNER JOIN users u ON p.user_id = u.id
''')
users_with_progress = target_cursor.fetchone()[0]

print(f"✓ 数据验证完成:")
print(f"  - 总用户数: {total_users}")
print(f"  - 总进度数: {total_progress}")
print(f"  - 有进度的用户: {users_with_progress}\n")

# 关闭连接
source_conn.close()
target_conn.close()

print("=== 导入完成 ===")
print(f"备份文件: {backup_path}")
print(f"导入用户: {imported_users} 人")
print(f"导入进度: {imported_progress} 条")
