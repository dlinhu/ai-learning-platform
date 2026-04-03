import sqlite3
import os

db_path = './data/learning.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 检查表结构
    cursor.execute('PRAGMA table_info(lessons)')
    columns = [row[1] for row in cursor.fetchall()]
    print('Current columns:', columns)

    # 添加structured_content列
    if 'structured_content' not in columns:
        cursor.execute('ALTER TABLE lessons ADD COLUMN structured_content TEXT DEFAULT "{}"')
        conn.commit()
        print('Added structured_content column')

    # 验证
    cursor.execute('PRAGMA table_info(lessons)')
    columns = [row[1] for row in cursor.fetchall()]
    print('Updated columns:', columns)

    conn.close()
else:
    print('Database not found at:', db_path)
