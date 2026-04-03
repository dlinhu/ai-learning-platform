import os
import sys
import json
from datetime import datetime

backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

from app.utils.database import SessionLocal
from app.models.models import Module, Lesson, KnowledgePoint, Term, LessonTerm, PracticeQuestion

def collect_all_questions():
    """收集所有练习题"""
    db = SessionLocal()
    all_questions = []
    
    try:
        modules = db.query(Module).all()
        
        for module in modules:
            lessons = db.query(Lesson).filter(Lesson.module_id == module.id).all()
            
            for lesson in lessons:
                kps = db.query(KnowledgePoint).filter(KnowledgePoint.lesson_id == lesson.id).all()
                
                for kp in kps:
                    questions = db.query(PracticeQuestion).filter(
                        PracticeQuestion.knowledge_point_id == kp.id
                    ).all()
                    
                    for q in questions:
                        question_data = {
                            'module_id': module.id,
                            'module_name': module.name,
                            'lesson_id': lesson.id,
                            'lesson_title': lesson.title,
                            'knowledge_point_id': kp.id,
                            'knowledge_point_title': kp.title,
                            'question_id': q.id,
                            'question_type': q.question_type,
                            'question_text': q.question_text,
                            'options': q.options,
                            'correct_answer': q.correct_answer,
                            'explanation': q.explanation,
                            'difficulty': q.difficulty
                        }
                        all_questions.append(question_data)
        
        return all_questions
    
    finally:
        db.close()

def generate_markdown_document(questions):
    """生成Markdown格式的综合练习题文档"""
    
    # 按模块分组
    modules_dict = {}
    for q in questions:
        module_name = q['module_name']
        if module_name not in modules_dict:
            modules_dict[module_name] = {
                'name': module_name,
                'questions': []
            }
        modules_dict[module_name]['questions'].append(q)
    
    content = """# AI学习平台综合练习题集

## Comprehensive Practice Questions for AI Learning Platform

---

**生成时间 / Generated**: {date}

**总题数 / Total Questions**: {total}

**模块数 / Total Modules**: {modules}

---

## 目录 / Table of Contents

""".format(
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        total=len(questions),
        modules=len(modules_dict)
    )
    
    # 添加目录
    for i, (module_name, module_data) in enumerate(modules_dict.items(), 1):
        content += f"{i}. [{module_name}](#{module_name.replace(' ', '-').replace('/', '-')}) ({len(module_data['questions'])}题)\n"
    
    content += "\n---\n\n"
    
    # 按模块生成题目
    for module_name, module_data in modules_dict.items():
        content += f"""## {module_name}

### 模块概述 / Module Overview

本模块包含 {len(module_data['questions'])} 道练习题，涵盖该领域的核心知识点。

---

"""
        
        # 按题型分类
        single_choice = [q for q in module_data['questions'] if q['question_type'] == 'single_choice']
        multiple_choice = [q for q in module_data['questions'] if q['question_type'] == 'multiple_choice']
        true_false = [q for q in module_data['questions'] if q['question_type'] == 'true_false']
        
        # 单选题
        if single_choice:
            content += f"### 单选题 / Single Choice ({len(single_choice)}题)\n\n"
            for i, q in enumerate(single_choice, 1):
                content += f"""#### {i}. {q['question_text']}

"""
                if q['options']:
                    for opt in q['options']:
                        content += f"- {opt}\n"
                
                content += f"""
**答案**: {q['correct_answer']}

**解析**: {q['explanation']}

**知识点**: {q['knowledge_point_title']}

**课程**: {q['lesson_title']}

**难度**: {'⭐' * q['difficulty']}

---

"""
        
        # 多选题
        if multiple_choice:
            content += f"### 多选题 / Multiple Choice ({len(multiple_choice)}题)\n\n"
            for i, q in enumerate(multiple_choice, 1):
                content += f"""#### {i}. {q['question_text']}

"""
                if q['options']:
                    for opt in q['options']:
                        content += f"- {opt}\n"
                
                content += f"""
**答案**: {q['correct_answer']}

**解析**: {q['explanation']}

**知识点**: {q['knowledge_point_title']}

**课程**: {q['lesson_title']}

**难度**: {'⭐' * q['difficulty']}

---

"""
        
        # 判断题
        if true_false:
            content += f"### 判断题 / True or False ({len(true_false)}题)\n\n"
            for i, q in enumerate(true_false, 1):
                content += f"""#### {i}. {q['question_text']}

**答案**: {q['correct_answer']}

**解析**: {q['explanation']}

**知识点**: {q['knowledge_point_title']}

**课程**: {q['lesson_title']}

**难度**: {'⭐' * q['difficulty']}

---

"""
        
        content += "\n"
    
    # 添加答案速查表
    content += """---

## 答案速查表 / Quick Answer Key

"""
    
    for module_name, module_data in modules_dict.items():
        content += f"\n### {module_name}\n\n"
        for i, q in enumerate(module_data['questions'], 1):
            content += f"{i}. {q['correct_answer']}\n"
    
    content += """

---

## 学习建议 / Study Tips

1. **先学习课程内容**: 在做练习题之前，确保已经学习相关课程内容。
2. **独立思考**: 尝试自己回答问题，再看答案和解析。
3. **记录错题**: 将做错的题目记录下来，定期复习。
4. **理解原理**: 不要只记住答案，要理解背后的原理。

---

## 统计信息 / Statistics

| 模块 | 单选题 | 多选题 | 判断题 | 总计 |
|------|--------|--------|--------|------|
"""
    
    for module_name, module_data in modules_dict.items():
        sc = len([q for q in module_data['questions'] if q['question_type'] == 'single_choice'])
        mc = len([q for q in module_data['questions'] if q['question_type'] == 'multiple_choice'])
        tf = len([q for q in module_data['questions'] if q['question_type'] == 'true_false'])
        total = len(module_data['questions'])
        content += f"| {module_name} | {sc} | {mc} | {tf} | {total} |\n"
    
    total_sc = len([q for q in questions if q['question_type'] == 'single_choice'])
    total_mc = len([q for q in questions if q['question_type'] == 'multiple_choice'])
    total_tf = len([q for q in questions if q['question_type'] == 'true_false'])
    content += f"| **总计** | **{total_sc}** | **{total_mc}** | **{total_tf}** | **{len(questions)}** |\n"
    
    content += """

---

*本文档由AI学习平台自动生成 / This document is auto-generated by AI Learning Platform*
"""
    
    return content

def create_comprehensive_module():
    """在数据库中创建综合练习模块"""
    db = SessionLocal()
    
    try:
        # 检查是否已存在综合练习模块
        existing = db.query(Module).filter(Module.name.like('%综合练习%')).first()
        if existing:
            print(f"综合练习模块已存在: {existing.name}")
            return existing
        
        # 创建新模块
        comp_module = Module(
            name="综合练习 Comprehensive Practice",
            description="涵盖所有模块的综合练习题集，用于复习和自测。/ Comprehensive practice questions covering all modules for review and self-assessment."
        )
        db.add(comp_module)
        db.commit()
        print(f"创建综合练习模块: {comp_module.name}")
        return comp_module
    
    finally:
        db.close()

def main():
    print("=" * 60)
    print("AI学习平台综合练习题集生成器")
    print("Comprehensive Practice Questions Generator")
    print("=" * 60)
    
    # 步骤1: 收集所有练习题
    print("\n[步骤1] 收集所有练习题...")
    questions = collect_all_questions()
    print(f"收集到 {len(questions)} 道练习题")
    
    # 步骤2: 生成Markdown文档
    print("\n[步骤2] 生成Markdown文档...")
    markdown_content = generate_markdown_document(questions)
    
    # 保存Markdown文件
    output_path = os.path.join(backend_dir, 'course_content', 'comprehensive_practice_questions.md')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    print(f"Markdown文档已保存: {output_path}")
    
    # 步骤3: 创建数据库模块
    print("\n[步骤3] 创建数据库综合练习模块...")
    comp_module = create_comprehensive_module()
    
    # 步骤4: 保存JSON数据
    print("\n[步骤4] 保存JSON数据...")
    json_path = os.path.join(backend_dir, 'course_content', 'comprehensive_practice_questions.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"JSON数据已保存: {json_path}")
    
    # 统计信息
    print("\n" + "=" * 60)
    print("生成完成！/ Generation Complete!")
    print("=" * 60)
    print(f"总练习题数: {len(questions)}")
    print(f"Markdown文档: {output_path}")
    print(f"JSON数据: {json_path}")
    print("=" * 60)

if __name__ == "__main__":
    main()
