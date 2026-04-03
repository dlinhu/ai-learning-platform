import requests

# 登录
r = requests.post('http://127.0.0.1:8000/api/auth/login', data={'username': 'testuser', 'password': 'test123'})
if r.status_code == 200:
    token = r.json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}
    
    # 测试获取内容
    r = requests.get('http://127.0.0.1:8000/api/courses/content/D:/AI Materials/ai-learning-platform/backend/course_content/basic_prompt_structures.md', headers=headers)
    print(f'Status: {r.status_code}')
    print(f'Response: {r.text[:500] if r.text else "Empty"}')
else:
    print(f'Login failed: {r.status_code}')
