import requests

# 登录获取token
login_data = {'username': 'testuser', 'password': 'test123'}
r = requests.post('http://127.0.0.1:8000/api/auth/login', data=login_data)
print('Login response:', r.status_code)

 
if r.status_code == 200:
    token = r.json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}
    
    # 获取模块列表
    r = requests.get('http://127.0.0.1:8000/api/courses/modules', headers=headers)
    print('Modules response:', r.status_code)
    
    if r.status_code == 200:
        modules = r.json()
        print(f'Found {len(modules)} modules')
        
        if modules:
            module_id = modules[0]['id']
            print(f'Getting lessons for module: {module_id}')
            
            # 获取模块的课程
            r = requests.get(f'http://127.0.0.1:8000/api/courses/modules/{module_id}/lessons', headers=headers)
            print(f'Lessons response:', r.status_code)
            
            if r.status_code == 200:
                lessons = r.json()
                print(f'Found {len(lessons)} lessons')
                
                if lessons:
                    lesson_id = lessons[0]['id']
                    print(f'Getting lesson detail for: {lesson_id}')
                    r = requests.get(f'http://127.0.0.1:8000/api/courses/lessons/{lesson_id}', headers=headers)
                    print(f'Lesson detail response:', r.status_code)
                    
                    if r.status_code == 200:
                        lesson = r.json()
                        print(f'Lesson title: {lesson["title"]}')
                        print(f'Knowledge points: {len(lesson.get("knowledge_points", []))}')
                        
                        if lesson.get('knowledge_points'):
                            kp_id = lesson['knowledge_points'][0]['id']
                            print(f'Testing with KP ID: {kp_id}')
                            
                            # 获取练习题
                            r = requests.get(f'http://127.0.0.1:8000/api/practice/knowledge-point/{kp_id}', headers=headers)
                            print(f'Practice questions response:', r.status_code)
                            print(f'Response text: {r.text[:500]}')
                            
                            if r.status_code == 200:
                                questions = r.json()
                                print(f'Found {len(questions)} practice questions')
                                if questions:
                                    print(f'First question: {questions[0]["question_text"]}')
                            else:
                                print('No questions in response')
                        else:
                            print('No knowledge points in lesson')
                    else:
                        print('No lessons found')
            else:
                print('No modules found')
    else:
        print('Login failed')
