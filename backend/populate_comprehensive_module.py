import os
import sys
import json

backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

from app.utils.database import SessionLocal
from app.models.models import Module, Lesson, KnowledgePoint, Term, LessonTerm, PracticeQuestion

def populate_comprehensive_module():
    """为综合练习模块创建课程、知识点和练习题"""
    db = SessionLocal()
    
    try:
        # 获取综合练习模块
        comp_module = db.query(Module).filter(Module.name.like('%综合练习%')).first()
        if not comp_module:
            print("未找到综合练习模块")
            return
        
        print(f"综合练习模块: {comp_module.name}")
        
        # 读取JSON数据
        json_path = os.path.join(backend_dir, 'course_content', 'comprehensive_practice_questions.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            all_questions = json.load(f)
        
        print(f"读取到 {len(all_questions)} 道练习题")
        
        # 按模块分组
        modules_dict = {}
        for q in all_questions:
            module_name = q['module_name']
            if module_name not in modules_dict:
                modules_dict[module_name] = {
                    'name': module_name,
                    'lessons': {}
                }
            
            lesson_title = q['lesson_title']
            if lesson_title not in modules_dict[module_name]['lessons']:
                modules_dict[module_name]['lessons'][lesson_title] = {
                    'title': lesson_title,
                    'knowledge_points': {}
                }
            
            kp_title = q['knowledge_point_title']
            if kp_title not in modules_dict[module_name]['lessons'][lesson_title]['knowledge_points']:
                modules_dict[module_name]['lessons'][lesson_title]['knowledge_points'][kp_title] = {
                    'title': kp_title,
                    'questions': []
                }
            
            modules_dict[module_name]['lessons'][lesson_title]['knowledge_points'][kp_title]['questions'].append(q)
        
        total_lessons = 0
        total_kps = 0
        total_questions = 0
        
        # 为每个源模块创建一个综合课程
        for module_name, module_data in modules_dict.items():
            print(f"\n处理模块: {module_name}")
            
            # 创建课程
            lesson_title = f"{module_name} - 综合练习"
            existing_lesson = db.query(Lesson).filter(
                Lesson.module_id == comp_module.id,
                Lesson.title == lesson_title
            ).first()
            
            if existing_lesson:
                lesson = existing_lesson
                # 删除已有的知识点和练习题
                db.query(PracticeQuestion).filter(
                    PracticeQuestion.knowledge_point_id.in_(
                        db.query(KnowledgePoint.id).filter(KnowledgePoint.lesson_id == lesson.id)
                    )
                ).delete(synchronize_session='fetch')
                db.query(KnowledgePoint).filter(KnowledgePoint.lesson_id == lesson.id).delete()
                print(f"  更新课程: {lesson_title}")
            else:
                lesson = Lesson(
                    module_id=comp_module.id,
                    title=lesson_title,
                    date="2024-01-01",
                    topics=[kp_title for kp_title in module_data['lessons'].keys()],
                    difficulty="intermediate",
                    time_estimate=60,
                    summary=f"{module_name}模块的综合练习题集，涵盖该模块所有知识点。",
                    materials=[]
                )
                db.add(lesson)
                db.flush()
                print(f"  创建课程: {lesson_title}")
            
            total_lessons += 1
            
            # 为每个知识点创建记录
            kp_order = 0
            for lesson_title_orig, lesson_data in module_data['lessons'].items():
                for kp_title, kp_data in lesson_data['knowledge_points'].items():
                    kp = KnowledgePoint(
                        lesson_id=lesson.id,
                        title=kp_title,
                        description=f"来自课程: {lesson_title_orig}",
                        category='comprehensive',
                        importance=2,
                        key_concepts=[],
                        examples=[],
                        common_mistakes=[],
                        best_practices=[]
                    )
                    db.add(kp)
                    db.flush()
                    total_kps += 1
                    
                    # 添加练习题
                    for q_data in kp_data['questions']:
                        question = PracticeQuestion(
                            knowledge_point_id=kp.id,
                            question_type=q_data['question_type'],
                            question_text=q_data['question_text'],
                            options=q_data['options'],
                            correct_answer=q_data['correct_answer'],
                            explanation=q_data['explanation'],
                            difficulty=q_data['difficulty'],
                            order_index=total_questions
                        )
                        db.add(question)
                        total_questions += 1
                    
                    kp_order += 1
                    if kp_order % 5 == 0:
                        print(f"    已处理 {kp_order} 个知识点...")
            
            print(f"  完成: {len(module_data['lessons'])} 个源课程, 知识点和练习题已添加")
        
        db.commit()
        
        print(f"\n{'='*50}")
        print("综合练习模块数据填充完成!")
        print(f"创建课程: {total_lessons}")
        print(f"创建知识点: {total_kps}")
        print(f"创建练习题: {total_questions}")
        print(f"{'='*50}")
        
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    populate_comprehensive_module()
