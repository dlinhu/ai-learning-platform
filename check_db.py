import sqlite3

conn = sqlite3.connect('d:/AI/ai-learning-platform/learning.db')
cursor = conn.cursor()

print('=== 数据库表结构 ===')
cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
tables = cursor.fetchall()
for t in tables:
    print(f'表名: {t[0]}')

print('\n=== 用户表数据 ===')
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()

cursor.execute('PRAGMA table_info(users)')
columns = cursor.fetchall()
print('\n用户表字段:')
for col in columns:
    print(f'  {col[1]} ({col[2]})')

print(f'\n用户数据 (共{len(users)}条):')
for user in users:
    print(f'  {user}')

print('\n=== 学习进度表数据 ===')
cursor.execute('SELECT COUNT(*) FROM progress')
progress_count = cursor.fetchone()[0]
print(f'进度记录数: {progress_count}')

if progress_count > 0:
    cursor.execute('PRAGMA table_info(progress)')
    progress_columns = cursor.fetchall()
    print('\n进度表字段:')
    for col in progress_columns:
        print(f'  {col[1]} ({col[2]})')
    
    cursor.execute('SELECT user_id, COUNT(*) as count FROM progress GROUP BY user_id')
    user_progress = cursor.fetchall()
    print('\n各用户进度统计:')
    for up in user_progress:
        print(f'  用户ID: {up[0]}, 进度数: {up[1]}')

conn.close()
