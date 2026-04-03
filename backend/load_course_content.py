import os
import sys
import json
import re
from pathlib import Path
from typing import List, Dict, Optional

backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

from app.utils.database import SessionLocal
from app.models.models import Module, Lesson, KnowledgePoint, Term, LessonTerm
from app.services.content_parser import ContentParser, ParsedContent

backend_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(backend_dir))
CONTENT_BASE_PATH = os.path.join(project_root, "AI Courses")

def get_full_path(relative_path: str) -> str:
    relative_path = relative_path.replace('/', os.sep).replace('\\', os.sep)
    return os.path.join(CONTENT_BASE_PATH, relative_path)

def parse_materials_field(materials_str: str) -> List[Dict]:
    materials = []
    pattern = r'\*\*(.+?)\*\*\s*\[(.+?)\]\((.+?)\)'
    for match in re.finditer(pattern, materials_str):
        materials.append({
            "title": match.group(1),
            "text": match.group(2),
            "path": match.group(3)
        })
    return materials

def parse_course_schedule(schedule_path: str) -> List[Dict]:
    with open(schedule_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    modules = []
    current_module = None
    current_week_lessons = []
    
    chinese_num_map = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10}
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        module_match = re.match(r'## 第([一二三四五六七八九十]+)模块[：:](.+)', line)
        if module_match:
            if current_module:
                current_module['lessons'].extend(current_week_lessons)
                modules.append(current_module)
                current_week_lessons = []
            
            chinese_num = module_match.group(1)
            order = chinese_num_map.get(chinese_num, len(modules) + 1)
            name = module_match.group(2).strip()
            name = re.sub(r'[（(].+[）)]', '', name).strip()
            
            current_module = {
                'order': order,
                'name': name,
                'lessons': []
            }
            i += 1
            continue
        
        break_match = re.match(r'### Break \d+[：:](.+)', line)
        if break_match and current_module:
            current_module['lessons'].extend(current_week_lessons)
            current_week_lessons = []
            i += 1
            continue
        
        break_match2 = re.match(r'### Break[：:](.+)', line)
        if break_match2 and current_module:
            current_module['lessons'].extend(current_week_lessons)
            current_week_lessons = []
            i += 1
            continue
        
        lesson_match = re.match(r'\|\s*(\d+月\d+日)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|', line)
        if lesson_match and current_module:
            date_str = lesson_match.group(1)
            title = lesson_match.group(2).strip()
            topics_str = lesson_match.group(3)
            materials_str = lesson_match.group(4)
            
            date_match = re.match(r'(\d+)月(\d+)日', date_str)
            if date_match:
                date = f"2026-{int(date_match.group(1)):02d}-{int(date_match.group(2)):02d}"
            else:
                date = date_str
            
            topics = [t.strip() for t in topics_str.split('；') if t.strip()]
            if not topics:
                topics = [t.strip() for t in topics_str.split('+') if t.strip()]
            
            difficulty = "basic"
            time_estimate = 60
            if '🔥' in title:
                difficulty = "advanced"
            if '⏰' in title:
                time_estimate = 90
            
            title = re.sub(r'[🔥⏰]\s*', '', title).strip()
            
            materials = parse_materials_field(materials_str)
            
            lesson = {
                'date': date,
                'title': title,
                'topics': topics,
                'difficulty': difficulty,
                'time_estimate': time_estimate,
                'materials': materials
            }
            current_week_lessons.append(lesson)
        
        i += 1
    
    if current_module:
        current_module['lessons'].extend(current_week_lessons)
        modules.append(current_module)
    
    return modules

def load_course_content():
    print("Loading course content...")
    db = SessionLocal()
    
    try:
        schedule_path = os.path.join(CONTENT_BASE_PATH, "Context_Engineering_课程编排.md")
        parsed_modules = parse_course_schedule(schedule_path)
        
        content_parser = ContentParser(CONTENT_BASE_PATH)
        
        for mod_data in parsed_modules:
            module = db.query(Module).filter(Module.order_index == mod_data['order']).first()
            if not module:
                module = Module(
                    name=mod_data['name'],
                    description="",
                    order_index=mod_data['order']
                )
                db.add(module)
                db.flush()
            else:
                module.name = mod_data['name']
            
            print(f"\nModule {mod_data['order']}: {mod_data['name']}")
            
            for lesson_data in mod_data['lessons']:
                lesson = db.query(Lesson).filter(
                    Lesson.module_id == module.id,
                    Lesson.title == lesson_data['title']
                ).first()
                
                if not lesson:
                    lesson = Lesson(
                        module_id=module.id,
                        date=lesson_data['date'],
                        title=lesson_data['title'],
                        topics=lesson_data['topics'],
                        difficulty=lesson_data['difficulty'],
                        time_estimate=lesson_data['time_estimate'],
                        materials=lesson_data['materials']
                    )
                    db.add(lesson)
                    db.flush()
                else:
                    lesson.date = lesson_data['date']
                    lesson.topics = lesson_data['topics']
                    lesson.difficulty = lesson_data['difficulty']
                    lesson.time_estimate = lesson_data['time_estimate']
                    lesson.materials = lesson_data['materials']
                
                all_content = []
                all_knowledge_points = []
                all_terms = []
                
                for material in lesson_data['materials']:
                    full_path = get_full_path(material['path'])
                    if os.path.exists(full_path):
                        try:
                            parsed = content_parser.parse_file(material['path'])
                            if parsed:
                                all_content.append(f"## {material['title']}\n\n{parsed.summary}")
                                all_knowledge_points.extend(parsed.knowledge_points)
                                all_terms.extend(parsed.terms)
                                print(f"    Parsed: {material['path']}")
                        except Exception as e:
                            print(f"    Error parsing {material['path']}: {e}")
                    else:
                        print(f"    File not found: {full_path}")
                
                if all_content:
                    lesson.summary = "\n\n".join(all_content[:3])
                    lesson.raw_content = "\n\n---\n\n".join(all_content)
                
                db.flush()
                
                for kp in all_knowledge_points[:15]:
                    existing_kp = db.query(KnowledgePoint).filter(
                        KnowledgePoint.lesson_id == lesson.id,
                        KnowledgePoint.title == kp.title
                    ).first()
                    
                    if not existing_kp:
                        knowledge_point = KnowledgePoint(
                            lesson_id=lesson.id,
                            title=kp.title,
                            description=kp.description,
                            category=kp.category,
                            importance=kp.importance,
                            related_terms=kp.related_terms
                        )
                        db.add(knowledge_point)
                
                seen_terms = set()
                for term_data in all_terms:
                    if term_data.term in seen_terms:
                        continue
                    seen_terms.add(term_data.term)
                    
                    existing_term = db.query(Term).filter(Term.term == term_data.term).first()
                    
                    if not existing_term:
                        existing_term = Term(
                            term=term_data.term,
                            definition=term_data.definition,
                            category=term_data.category,
                            examples=term_data.examples,
                            related_terms=term_data.related_terms,
                            is_predefined=True
                        )
                        db.add(existing_term)
                        db.flush()
                    
                    existing_link = db.query(LessonTerm).filter(
                        LessonTerm.lesson_id == lesson.id,
                        LessonTerm.term_id == existing_term.id
                    ).first()
                    
                    if not existing_link:
                        lesson_term = LessonTerm(
                            lesson_id=lesson.id,
                            term_id=existing_term.id
                        )
                        db.add(lesson_term)
                
                print(f"  - Lesson: {lesson.title} ({len(all_knowledge_points)} knowledge points, {len(seen_terms)} terms)")
        
        db.commit()
        print("\nCourse content loaded successfully!")
        
        modules_count = db.query(Module).count()
        lessons_count = db.query(Lesson).count()
        kp_count = db.query(KnowledgePoint).count()
        terms_count = db.query(Term).count()
        
        print(f"\nStatistics:")
        print(f"  Modules: {modules_count}")
        print(f"  Lessons: {lessons_count}")
        print(f"  Knowledge Points: {kp_count}")
        print(f"  Terms: {terms_count}")
        
    except Exception as e:
        print(f"Error loading course content: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    load_course_content()
