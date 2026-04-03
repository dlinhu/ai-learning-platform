import requests

# 登录
r = requests.post('http://127.0.0.1:8000/api/auth/login', data={'username': 'testuser', 'password': 'test123'})
if r.status_code == 200:
    token = r.json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}
    
    # 获取模块列表
    r = requests.get('http://127.0.0.1:8000/api/courses/modules', headers=headers)
    modules = r.json()
    print(f'Total Modules: {len(modules)}')
    
    # 找到RAG模块
    for m in modules:
        if 'RAG' in m['name']:
            print(f"\n=== RAG Module: {m['name']} ===")
            
            # 获取课程列表
            r = requests.get(f'http://127.0.0.1:8000/api/courses/modules/{m["id"]}/lessons', headers=headers)
            lessons = r.json()
            print(f'Total Lessons: {len(lessons)}')
            
            # 显示前5个课程
            for l in lessons[:5]:
                print(f"  - {l['title']}")
            
            if len(lessons) > 5:
                print(f"  ... and {len(lessons) - 5} more lessons")
            
            # 获取第一个课程的详情
            if lessons:
                r = requests.get(f'http://127.0.0.1:8000/api/courses/lessons/{lessons[0]["id"]}', headers=headers)
                lesson = r.json()
                print(f"\nFirst lesson details:")
                print(f"  Title: {lesson['title']}")
                print(f"  Knowledge points: {len(lesson.get('knowledge_points', []))}")
                print(f"  Terms: {len(lesson.get('terms', []))}")
                print(f"  Materials: {len(lesson.get('materials', []))}")
else:
    print(f'Login failed: {r.status_code}')
